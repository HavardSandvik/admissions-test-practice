(() => {
  "use strict";

  const MODULES = [
    { id: "m1", name: "Mathematics 1", note: "Compulsory for everyone" },
    { id: "m2", name: "Mathematics 2" },
    { id: "phys", name: "Physics" },
    { id: "chem", name: "Chemistry" },
    { id: "bio", name: "Biology" },
  ];
  const SESSION_SECONDS = 15 * 60;
  const SESSION_SIZE = 10;
  const KEY = "esat-practice-v1";
  const LETTERS = "ABCDEFGH";

  const Q = window.QUESTIONS || [];
  const byId = Object.fromEntries(Q.map(q => [q.id, q]));
  const modName = id => (MODULES.find(m => m.id === id) || {}).name || id;

  // ------------------------------------------------------------- storage
  function blank() { return { version: 1, sets: {}, attempts: [], q: {}, modules: null, current: null }; }
  function load() {
    try {
      const s = JSON.parse(localStorage.getItem(KEY));
      if (s && s.version === 1) return Object.assign(blank(), s);
    } catch (e) { /* storage unavailable or corrupt */ }
    return blank();
  }
  let S = load();
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { /* ignore */ } }

  // ------------------------------------------------------------- helpers
  const $app = document.getElementById("app");
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const today = () => new Date().toISOString().slice(0, 10);
  const fmtDate = d => new Date(d + "T12:00:00").toLocaleDateString("en-GB", { day: "numeric", month: "short" });
  const shuffle = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  function math(el) {
    if (window.renderMathInElement) {
      window.renderMathInElement(el, {
        delimiters: [{ left: "\\(", right: "\\)", display: false }, { left: "$$", right: "$$", display: true }],
        throwOnError: false,
      });
    }
  }
  function sets() {
    const out = [];
    for (const m of MODULES) {
      const nums = [...new Set(Q.filter(q => q.module === m.id).map(q => q.set))].sort((a, b) => a - b);
      for (const n of nums) out.push({ id: `${m.id}-${n}`, module: m.id, n, qs: Q.filter(q => q.module === m.id && q.set === n) });
    }
    return out;
  }
  function chosenModules() { return S.modules && S.modules.length ? S.modules : MODULES.map(m => m.id); }

  // ------------------------------------------------------------- home
  function home() {
    stopTimer();
    document.getElementById("session-bar").hidden = true;
    document.getElementById("foot").hidden = false;
    const all = sets();
    const mods = chosenModules();
    const visible = all.filter(s => mods.includes(s.module));
    const doneCount = visible.filter(s => S.sets[s.id] && S.sets[s.id].done).length;
    const answered = S.attempts.reduce((n, a) => n + a.items.filter(i => i.chosen != null).length, 0);
    const correct = S.attempts.reduce((n, a) => n + a.items.filter(i => i.correct).length, 0);

    let h = `<h1>ESAT practice</h1>
      <p class="lede">Each set is ${SESSION_SIZE} questions in 15 minutes, the same pace as the real test (27 questions in 40 minutes). No calculator.</p>`;

    if (S.current && S.current.end > Date.now()) {
      h += `<div class="card"><div class="card-head"><h2>Session in progress</h2></div>
        <div class="btn-row"><button class="btn" data-act="resume">Resume</button>
        <button class="btn quiet" data-act="abandon">Discard</button></div></div>`;
    }

    h += `<div class="stats">
      <div class="stat"><b>${doneCount}/${visible.length}</b><span>sets done</span></div>
      <div class="stat"><b>${answered}</b><span>questions answered</span></div>
      <div class="stat"><b>${answered ? Math.round(100 * correct / answered) + "%" : "–"}</b><span>accuracy</span></div>
    </div>`;

    h += `<div class="card"><div class="card-head"><h2>My modules</h2><span class="small">Maths 1 plus the modules your courses need</span></div>
      <div class="chips">${MODULES.map(m => `<button class="chip ${mods.includes(m.id) ? "on" : ""}" data-act="mod" data-id="${m.id}">${m.name}</button>`).join("")}</div></div>`;

    for (const m of MODULES.filter(m => mods.includes(m.id))) {
      const ms = all.filter(s => s.module === m.id);
      h += `<div class="card"><div class="card-head"><h2>${m.name}</h2><span class="small">${m.note || ""}</span></div>`;
      for (const s of ms) {
        const st = S.sets[s.id];
        let badge = `<span class="badge todo">Not started</span>`;
        if (st && st.done) {
          badge = st.best != null
            ? `<span class="badge done">Done · best ${st.best}/${s.qs.length}</span>`
            : `<span class="badge done">Done</span>`;
        }
        const when = st && st.date ? `Last ${fmtDate(st.date)}` : `${s.qs.length} questions · 15 min`;
        h += `<div class="set-row">
          <div class="set-name">Set ${s.n}<span class="small">${when}</span></div>
          ${badge}
          <div class="btn-row">
            <button class="btn" data-act="start" data-id="${s.id}">${st && st.best != null ? "Retake" : "Start"}</button>
            <button class="btn quiet" data-act="toggle" data-id="${s.id}">${st && st.done ? "Mark not done" : "Mark as done"}</button>
          </div></div>`;
      }
      h += `</div>`;
    }

    h += `<div class="card"><div class="card-head"><h2>Quick mix</h2><span class="small">10 questions from your modules, favouring ones not yet seen or got wrong</span></div>
      <button class="btn ghost" data-act="mix">Start a 15-minute mix</button></div>`;

    h += topicTable();

    h += `<div class="card"><div class="card-head"><h2>Backup</h2></div>
      <div class="tools">
        <button class="btn quiet" data-act="export">Export progress</button>
        <button class="btn quiet" data-act="import">Import progress</button>
        <button class="btn quiet" data-act="reset">Reset everything</button>
        <input type="file" accept="application/json" class="hidden-file" id="import-file">
      </div><div id="tool-msg" class="note"></div></div>`;

    $app.innerHTML = h;
    window.scrollTo(0, 0);
  }

  function topicTable() {
    const t = {};
    for (const [id, r] of Object.entries(S.q)) {
      const q = byId[id]; if (!q || !chosenModules().includes(q.module)) continue;
      const k = q.module + "|" + q.topic;
      t[k] = t[k] || { module: q.module, topic: q.topic, seen: 0, correct: 0 };
      t[k].seen += r.seen; t[k].correct += r.correct;
    }
    const rows = Object.values(t).sort((a, b) => a.correct / a.seen - b.correct / b.seen || b.seen - a.seen);
    if (!rows.length) return "";
    return `<div class="card"><div class="card-head"><h2>By topic</h2><span class="small">Weakest first</span></div>
      <table class="topics">${rows.map(r => {
        const p = Math.round(100 * r.correct / r.seen);
        return `<tr><td>${esc(r.topic)} <span class="small">· ${modName(r.module)}</span></td>
          <td class="num"><span class="bar"><i style="width:${p}%"></i></span></td>
          <td class="num">${r.correct}/${r.seen}</td></tr>`;
      }).join("")}</table></div>`;
  }

  // ------------------------------------------------------------- session
  let tick = null;
  function stopTimer() { if (tick) clearInterval(tick); tick = null; }

  function startSession(kind, setId) {
    let qs;
    if (kind === "set") {
      qs = sets().find(s => s.id === setId).qs.map(q => q.id);
    } else {
      const pool = Q.filter(q => chosenModules().includes(q.module));
      const score = q => { const r = S.q[q.id]; if (!r) return 0; return r.correct < r.seen ? 1 : 2; };
      qs = shuffle(pool).sort((a, b) => score(a) - score(b)).slice(0, SESSION_SIZE).map(q => q.id);
      qs = shuffle(qs);
    }
    S.current = {
      kind, setId: setId || null,
      qs,
      order: Object.fromEntries(qs.map(id => [id, shuffle(byId[id].options.map((_, i) => i))])),
      answers: {}, flags: {}, i: 0,
      start: Date.now(), end: Date.now() + SESSION_SECONDS * 1000,
    };
    save();
    session();
  }

  function session() {
    const c = S.current; if (!c) return home();
    document.getElementById("session-bar").hidden = false;
    document.getElementById("foot").hidden = true;
    const q = byId[c.qs[c.i]];
    const order = c.order[q.id];
    const title = c.kind === "set" ? `${modName(q.module)} · Set ${q.set}` : "Quick mix";
    document.getElementById("qcount").textContent = `${c.i + 1} / ${c.qs.length}`;

    let h = `<div class="dots">${c.qs.map((id, k) =>
      `<button class="dot ${c.answers[id] != null ? "answered" : ""} ${k === c.i ? "current" : ""} ${c.flags[id] ? "flagged" : ""}" data-act="go" data-i="${k}">${k + 1}</button>`).join("")}</div>
      <div class="card">
        <div class="qmeta"><span>${esc(title)}</span><span>${esc(q.topic)}</span></div>
        <div class="qtext">${q.q}</div>
        <div class="opts">${order.map((oi, k) =>
          `<button class="opt ${c.answers[q.id] === oi ? "sel" : ""}" data-act="pick" data-o="${oi}"><span class="L">${LETTERS[k]}</span><span>${q.options[oi]}</span></button>`).join("")}</div>
        <div class="nav">
          <div class="btn-row">
            <button class="btn ghost" data-act="prev" ${c.i === 0 ? "disabled" : ""}>Previous</button>
            <button class="btn quiet flag-btn ${c.flags[q.id] ? "on" : ""}" data-act="flag">${c.flags[q.id] ? "Flagged" : "Flag"}</button>
          </div>
          <div class="btn-row">
            ${c.i < c.qs.length - 1 ? `<button class="btn" data-act="next">Next</button>` : ""}
            <button class="btn ${c.i < c.qs.length - 1 ? "quiet" : ""}" data-act="finish">Finish</button>
          </div>
        </div>
        <div id="confirm"></div>
      </div>`;
    $app.innerHTML = h;
    math($app);
    if (!tick) { tick = setInterval(updateTimer, 250); }
    updateTimer();
  }

  function updateTimer() {
    const c = S.current; if (!c) return stopTimer();
    const left = Math.max(0, Math.ceil((c.end - Date.now()) / 1000));
    const el = document.getElementById("timer");
    el.textContent = `${Math.floor(left / 60)}:${String(left % 60).padStart(2, "0")}`;
    el.classList.toggle("low", left <= 120);
    if (left <= 0) finish(true);
  }

  function finish(timeUp) {
    const c = S.current; if (!c) return;
    stopTimer();
    const items = c.qs.map(id => {
      const chosen = c.answers[id] != null ? c.answers[id] : null;
      return { id, chosen, correct: chosen === byId[id].answer };
    });
    const score = items.filter(i => i.correct).length;
    const used = Math.min(SESSION_SECONDS, Math.round((Date.now() - c.start) / 1000));
    const attempt = { date: today(), kind: c.kind, setId: c.setId, items, score, used, timeUp: !!timeUp, order: c.order };
    S.attempts.push(attempt);
    for (const it of items) {
      if (it.chosen == null) continue; // unanswered doesn't count towards topic stats
      const r = S.q[it.id] || (S.q[it.id] = { seen: 0, correct: 0 });
      r.seen++; if (it.correct) r.correct++;
    }
    if (c.setId) {
      const st = S.sets[c.setId] || {};
      st.done = true; st.date = today(); st.last = score;
      st.best = st.best != null ? Math.max(st.best, score) : score;
      S.sets[c.setId] = st;
    }
    S.current = null;
    save();
    review(S.attempts.length - 1);
  }

  // ------------------------------------------------------------- review
  function review(idx) {
    stopTimer();
    document.getElementById("session-bar").hidden = true;
    document.getElementById("foot").hidden = false;
    const a = S.attempts[idx];
    const title = a.setId ? `${modName(a.setId.split("-")[0])} · Set ${a.setId.split("-")[1]}` : "Quick mix";
    const mm = `${Math.floor(a.used / 60)}:${String(a.used % 60).padStart(2, "0")}`;
    let h = `<div class="card"><div class="small">${esc(title)}</div>
      <div class="score"><b>${a.score}/${a.items.length}</b>
      <span class="small">${a.timeUp ? "Time ran out" : "Finished in " + mm} · ${a.items.filter(i => i.chosen == null).length} unanswered</span></div>
      <div class="btn-row" style="margin-top:12px">
        <button class="btn" data-act="home">Back to sets</button>
        ${a.setId ? `<button class="btn ghost" data-act="start" data-id="${a.setId}">Retake this set</button>` : `<button class="btn ghost" data-act="mix">Another mix</button>`}
      </div></div>`;

    a.items.forEach((it, k) => {
      const q = byId[it.id]; if (!q) return;
      const order = (a.order && a.order[it.id]) || q.options.map((_, i) => i);
      const cls = it.chosen == null ? "skip" : it.correct ? "ok" : "no";
      const tag = it.chosen == null ? "Not answered" : it.correct ? "Correct" : "Incorrect";
      h += `<div class="card rq ${cls}">
        <div class="qmeta"><span>Question ${k + 1} · ${esc(q.topic)}</span><span class="tag ${cls}">${tag}</span></div>
        <div class="qtext">${q.q}</div>
        <div class="opts">${order.map((oi, j) => {
          const c = oi === q.answer ? "right" : oi === it.chosen ? "wrong" : "";
          return `<div class="opt ${c}"><span class="L">${LETTERS[j]}</span><span>${q.options[oi]}</span></div>`;
        }).join("")}</div>
        <div class="solution"><b>Solution.</b> ${q.solution}</div>
      </div>`;
    });
    $app.innerHTML = h;
    math($app);
    window.scrollTo(0, 0);
  }

  // ------------------------------------------------------------- events
  $app.addEventListener("click", e => {
    const b = e.target.closest("[data-act]"); if (!b) return;
    const act = b.dataset.act, c = S.current;
    switch (act) {
      case "start": startSession("set", b.dataset.id); break;
      case "mix": startSession("mix"); break;
      case "resume": session(); break;
      case "abandon": S.current = null; save(); home(); break;
      case "home": home(); break;
      case "mod": {
        let m = chosenModules().slice();
        const id = b.dataset.id;
        m = m.includes(id) ? m.filter(x => x !== id) : m.concat(id);
        S.modules = m.length ? MODULES.map(x => x.id).filter(x => m.includes(x)) : null;
        save(); home(); break;
      }
      case "toggle": {
        const st = S.sets[b.dataset.id] || {};
        st.done = !st.done;
        if (st.done && !st.date) st.date = today();
        S.sets[b.dataset.id] = st;
        save(); home(); break;
      }
      case "pick": {
        const id = c.qs[c.i], o = +b.dataset.o;
        c.answers[id] = c.answers[id] === o ? null : o;
        save(); session(); break;
      }
      case "flag": { const id = c.qs[c.i]; c.flags[id] = !c.flags[id]; save(); session(); break; }
      case "go": c.i = +b.dataset.i; save(); session(); break;
      case "prev": c.i = Math.max(0, c.i - 1); save(); session(); break;
      case "next": c.i = Math.min(c.qs.length - 1, c.i + 1); save(); session(); break;
      case "finish": {
        const left = c.qs.filter(id => c.answers[id] == null).length;
        const flagged = c.qs.filter(id => c.flags[id]).length;
        if (!left && !flagged) { finish(false); break; }
        const parts = [];
        if (left) parts.push(`${left} unanswered`);
        if (flagged) parts.push(`${flagged} flagged`);
        document.getElementById("confirm").innerHTML = `<div class="confirm"><p>You have ${parts.join(" and ")}. There's no penalty for wrong answers, so it's worth guessing.</p>
          <div class="btn-row"><button class="btn" data-act="finish-now">Finish anyway</button><button class="btn quiet" data-act="cancel">Keep going</button></div></div>`;
        break;
      }
      case "finish-now": finish(false); break;
      case "cancel": document.getElementById("confirm").innerHTML = ""; break;
      case "export": {
        const blob = new Blob([JSON.stringify(Object.assign({}, S, { current: null }), null, 1)], { type: "application/json" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob); a.download = `esat-progress-${today()}.json`;
        document.body.appendChild(a); a.click(); a.remove();
        break;
      }
      case "import": document.getElementById("import-file").click(); break;
      case "reset": {
        if (b.dataset.armed) { S = blank(); save(); home(); }
        else { b.dataset.armed = "1"; b.textContent = "Tap again to erase all progress"; }
        break;
      }
    }
  });

  $app.addEventListener("change", e => {
    if (e.target.id !== "import-file" || !e.target.files[0]) return;
    const r = new FileReader();
    r.onload = () => {
      try {
        const d = JSON.parse(r.result);
        if (!d || d.version !== 1) throw new Error();
        S = Object.assign(blank(), d, { current: null }); save(); home();
        document.getElementById("tool-msg").textContent = "Progress imported.";
      } catch (err) { document.getElementById("tool-msg").textContent = "That file isn't an ESAT progress export."; }
    };
    r.readAsText(e.target.files[0]);
  });

  document.getElementById("home-link").addEventListener("click", e => { e.preventDefault(); home(); });

  // Keyboard: A–H pick, arrows move
  document.addEventListener("keydown", e => {
    const c = S.current;
    if (!c || document.getElementById("session-bar").hidden || e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key.toUpperCase();
    const q = byId[c.qs[c.i]];
    const pos = LETTERS.indexOf(k);
    if (pos >= 0 && k.length === 1 && pos < q.options.length) {
      const o = c.order[q.id][pos]; c.answers[q.id] = c.answers[q.id] === o ? null : o; save(); session();
    } else if (e.key === "ArrowRight" && c.i < c.qs.length - 1) { c.i++; save(); session(); }
    else if (e.key === "ArrowLeft" && c.i > 0) { c.i--; save(); session(); }
  });

  // Resume a session after a reload; if its time ran out while away, mark it finished.
  if (S.current) {
    if (S.current.end <= Date.now()) finish(true); else session();
  } else home();
})();
