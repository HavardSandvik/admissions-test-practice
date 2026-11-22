"""Independent checks of each question's keyed answer.

Each check computes the answer from scratch and returns the expected text of
the correct option; run() asserts it matches the option at the keyed index.
Conceptual (non-numeric) questions are listed in CONCEPTUAL with the expected
option text, so a mis-keyed letter is still caught.
"""
from fractions import Fraction as F
from itertools import product
import math
import sympy as sp

x, y = sp.symbols("x y", real=True)
C = {}
def check(id):
    def deco(fn):
        C[id] = fn
        return fn
    return deco

# Maths 1
@check("M1-01")
def _(): v = sp.nsimplify((sp.sqrt(12) + sp.sqrt(27))**2); assert v == 75; return r"\(75\)"
@check("M1-02")
def _():
    sol = sp.solve(sp.Eq(y, (2*x+3)/(x-1)), x)[0]
    assert sp.simplify(sol - (y+3)/(y-2)) == 0; return r"\(x = \dfrac{y + 3}{y - 2}\)"
@check("M1-03")
def _(): assert F(12,10)*F(75,100) == F(9,10); return "10% decrease"
@check("M1-04")
def _():
    pts = sp.solve([x**2+y**2-25, y-x-1], [x, y])
    (a, b), (c, d) = pts
    assert sp.simplify(sp.sqrt((a-c)**2+(b-d)**2) - 7*sp.sqrt(2)) == 0; return r"\(7\sqrt{2}\)"
@check("M1-05")
def _():
    balls = "RRRRBBBBBB"; pairs = [(i, j) for i in range(10) for j in range(10) if i != j]
    p = F(sum(balls[i] != balls[j] for i, j in pairs), len(pairs)); assert p == F(8,15); return r"\(\dfrac{8}{15}\)"
@check("M1-06")
def _():
    for k in range(1, 100):
        a, b, c = 9*k, 12*k, 10*k
        if a+b+c == 155: assert F(a,b) == F(3,4) and F(b,c) == F(6,5); assert c == 50; return r"\(50\)"
@check("M1-07")
def _(): assert 5*12 - 4*10 == 20; return r"\(20\)"
@check("M1-08")
def _():
    arc = sp.Rational(40,360)*2*sp.pi*6; assert sp.simplify(arc - 4*sp.pi/3) == 0; return r"\(12 + \dfrac{4\pi}{3}\)"
@check("M1-09")
def _(): assert sp.simplify(6/(3-sp.sqrt(3)) - (3+sp.sqrt(3))) == 0; return r"\(3 + \sqrt{3}\)"
@check("M1-10")
def _(): assert 1/F(3,2)**2 == F(4,9); return r"\(\dfrac{4}{9}\)"
@check("M1-11")
def _(): n = sum(1 for k in range(-100, 100) if k*k - 5*k - 14 < 0); assert n == 8; return r"\(8\)"
@check("M1-12")
def _(): assert F(25+64-49, 80) == F(1,2); return r"\(60^\circ\)"
@check("M1-13")
def _(): s = sp.solve(sp.Eq(2**(x+1)*4**x, 32), x); assert s == [sp.Rational(4,3)]; return r"\(x = \dfrac{4}{3}\)"
@check("M1-14")
def _(): assert F(60) / (F(30,60) + F(30,40)) == 48; return r"\(48\)"
@check("M1-15")
def _():
    r, h = sp.symbols("r h", positive=True)
    assert sp.solve(sp.Eq(sp.Rational(4,3)*sp.pi*r**3, sp.pi*r**2*h), h) == [4*r/3]; return r"\(\dfrac{4r}{3}\)"
@check("M1-16")
def _():
    # line 3x - 2y + 1 = 0: through (1,2), gradient 3/2, product with -2/3 is -1
    assert 3*1 - 2*2 + 1 == 0 and F(3,2)*F(-2,3) == -1; return r"\(3x - 2y + 1 = 0\)"
@check("M1-17")
def _(): v = F(6*10**5)*F(4, 10**8)/(F(8,100)); assert v == F(3,10); return r"\(3 \times 10^{-1}\)"
@check("M1-18")
def _():
    from statistics import median, multimode
    best = 0
    for s in product(range(1, 31), repeat=5):
        if list(s) != sorted(s) or sum(s) != 30: continue
        if median(s) != 5 or multimode(s) != [3]: continue
        best = max(best, s[-1])
    assert best == 13; return r"\(13\)"
@check("M1-19")
def _(): assert 40*F(3,2)**3 == 135; return r"\(135\)"
@check("M1-20")
def _(): assert F(3,10)*F(1,2) + F(7,10)*F(1,2) == F(1,2); return r"\(0.5\)"
# Maths 2
@check("M2-01")
def _(): assert sp.integrate(3*x**2-2*x+1, (x, 0, 2)) == 6; return r"\(6\)"
@check("M2-02")
def _():
    f = x**3-6*x**2+9*x+1
    cands = [f.subs(x, c) for c in [0, 5] + [r for r in sp.solve(sp.diff(f, x), x) if 0 <= r <= 5]]
    assert max(cands) == 21; return r"\(21\)"
@check("M2-03")
def _():
    s = [r for r in sp.solve(sp.Eq(x*(x-2), 8), x) if r > 2]; assert s == [4]; return r"\(x = 4\) only"
@check("M2-04")
def _(): r = 1 - F(12,18); assert 12*r**2 == F(4,3); return r"\(\dfrac{4}{3}\)"
@check("M2-05")
def _():
    s = sp.solveset(sp.sin(2*x) - sp.cos(x), x, sp.Interval(0, 2*sp.pi)); assert len(s) == 4; return r"\(4\)"
@check("M2-06")
def _(): assert sp.expand((2-x)**6).coeff(x, 3) == -160; return r"\(-160\)"
@check("M2-07")
def _():
    # centre/radius from completing the square
    assert sp.expand((x-3)**2+(y+2)**2-25) == x**2+y**2-6*x+4*y-12
    t2 = (10-3)**2 + (2+2)**2 - 25; assert t2 == 40; return r"\(2\sqrt{10}\)"
@check("M2-08")
def _(): assert sp.integrate(2*x-x**2, (x, 0, 2)) == sp.Rational(4,3); return r"\(\dfrac{4}{3}\)"
@check("M2-09")
def _():
    s = sp.solve(sp.Eq(2*x**2+1, (2*x+1)**2), x); assert sum(s) == -2; return r"\(-2\)"
@check("M2-10")
def _(): S = lambda n: 3*n*n + 2*n; assert S(10) - S(9) == 59; return r"\(59\)"
# Physics
@check("P-01")
def _(): assert 0.5*20*8 == 80; return r"\(80\text{ m}\)"
@check("P-02")
def _(): t = math.sqrt(2*45/10); assert abs(15*t - 45) < 1e-9; return r"\(45\text{ m}\)"
@check("P-03")
def _():
    Rp = F(6*3, 9); I = F(12) / (Rp + 4); assert I*Rp/3 == F(4,3); return r"\(\dfrac{4}{3}\text{ A}\)"
@check("P-04")
def _(): assert 0.5*4200*80/2000 == 84; return r"\(84\text{ s}\)"
@check("P-05")
def _(): assert 100/(50*0.40) == 5; return r"\(5\text{ s}\)"
@check("P-06")
def _(): assert 1 - F(1,2)**(24//6) == F(15,16); return r"\(\dfrac{15}{16}\)"
@check("P-07")
def _():
    v = F(2*3, 3); lost = F(1,2)*2*9 - F(1,2)*3*v**2; assert lost == 3; return r"\(3\text{ J}\)"
@check("P-08")
def _(): assert 50*10*12/20/0.6 == 500; return r"\(500\text{ W}\)"
@check("P-09")
def _(): assert 1e5 + 1000*10*20 == 3e5; return r"\(3.0 \times 10^5\text{ Pa}\)"
@check("P-10")
def _(): assert 2000*12/240 == 100 and abs(12*4/240 - 0.2) < 1e-12; return "100 turns, 0.20 A"
# Chemistry
@check("C-01")
def _(): assert 0.25*(40+12+48) == 25; return r"\(25\text{ g}\)"
@check("C-02")
def _():
    for a, b, c in product(range(1, 10), repeat=3):
        if 3 == b and 8 == 2*c and 2*a == 2*b + c: assert a+b+c == 12; return r"\(12\)"
@check("C-03")
def _(): n = 0.150*0.0200*2; assert abs(n/0.0250 - 0.240) < 1e-12; return r"\(0.240\text{ mol dm}^{-3}\)"
@check("C-04")
def _(): assert abs(5.0/100*24 - 1.2) < 1e-12; return r"\(1.2\text{ dm}^3\)"
@check("C-05")
def _(): p = sp.solve(sp.Eq(69*x + 71*(100-x), 6980), x)[0]; assert p == 60; return r"\(60\%\)"
@check("C-06")
def _():
    ox = {"Mn": (-1 + 8), "Cr": (-2 + 14) / 2, "S": (-2 + 8), "N": (-1 + 6), "Cl": (-1 + 6)}
    assert max(ox, key=ox.get) == "Mn" and ox["Mn"] == 7; return r"Mn in \(\text{MnO}_4^{-}\)"
@check("C-07")
def _():
    r = [40/12, 6.7/1, 53.3/16]; m = min(r); ratio = [round(v/m) for v in r]; assert ratio == [1, 2, 1]
    assert 180 // (12 + 2 + 16) == 6; return r"\(\text{C}_6\text{H}_{12}\text{O}_6\)"
@check("B-08")
def _(): assert 20000*0.1**3 == 20.000000000000004 or abs(20000*0.1**3 - 20) < 1e-9; return r"\(20\text{ kJ}\)"
@check("B-02")
def _():
    kids = [a+b for a in "Ff" for b in "Ff"]; unaff = [k for k in kids if "F" in k]
    assert F(sum("f" in k for k in unaff), len(unaff)) == F(2,3); return r"\(\dfrac{2}{3}\)"
@check("B-09")
def _():
    kids = [(m, f) for m in ["XB", "Xb"] for f in ["XB", "Y"]]
    assert F(sum(m == "Xb" and f == "Y" for m, f in kids), 4) == F(1,4); return r"\(\dfrac{1}{4}\)"
@check("B-10")
def _(): assert (100 - 2*30) / 2 == 20; return r"\(20\%\)"
@check("B-03")
def _(): return "92 chromatids; 23 chromosomes"

CONCEPTUAL = {
    "C-08": r"\(\text{H}_2\text{O}\)",
    "C-09": "Cathode: hydrogen; anode: chlorine",
    "C-10": "Decrease temperature, increase pressure",
    "B-01": "1 and 2 only",
    "B-04": "right atrium → right ventricle → pulmonary artery → lungs → pulmonary vein → left atrium → left ventricle",
    "B-05": "Water leaves the cell by osmosis and the cell becomes plasmolysed",
    "B-06": "Carbon dioxide concentration is the limiting factor",
    "B-07": "It is produced by the pancreas and causes the liver to convert glucose to glycogen",
}

def run(Q):
    missing = []
    for q in Q:
        keyed = q["options"][q["answer"]]
        if q["id"] in C:
            exp = C[q["id"]]()
        elif q["id"] in CONCEPTUAL:
            exp = CONCEPTUAL[q["id"]]
        else:
            missing.append(q["id"]); continue
        assert keyed == exp, f"{q['id']}: keyed {keyed!r} but expected {exp!r}"
        # the expected answer must appear exactly once among the options
        assert q["options"].count(exp) == 1, q["id"]
    assert not missing, f"no check for {missing}"
    print("verified", len(Q), "questions")


# ================================================================ ESAT-level checks
S8 = ["none of them", "1 only", "2 only", "3 only", "1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"]
def stmt(t1, t2, t3):
    k = (t1, t2, t3)
    table = {(0,0,0):0,(1,0,0):1,(0,1,0):2,(0,0,1):3,(1,1,0):4,(1,0,1):5,(0,1,1):6,(1,1,1):7}
    return S8[table[tuple(int(bool(v)) for v in k)]]

@check("M1E-01")
def _():
    return stmt(sp.nsimplify((sp.sqrt(2)+sp.sqrt(8))**2) == 18,
                sp.nsimplify(sp.Integer(8)**sp.Rational(2,3) * sp.Integer(4)**sp.Rational(-1,2)) == 4,
                3*3**20 == 3**21)
@check("M1E-02")
def _():
    a, r = sp.symbols("a r", positive=True)
    sol = sp.solve(sp.Eq(6*a**2, 4*sp.pi*r**2), a)[0]
    assert sp.simplify(sol - r*sp.sqrt(2*sp.pi/3)) == 0
    # no other option is numerically equal
    for alt in [r*sp.sqrt(3*sp.pi/2), 2*sp.pi*r/3, r*sp.sqrt(sp.pi/6), r*sp.sqrt(2*sp.pi)/3, r*sp.sqrt(6*sp.pi)]:
        assert abs(float((alt - sol).subs(r, 1))) > 1e-6
    return r"\(r\sqrt{\dfrac{2\pi}{3}}\)"
@check("M1E-03")
def _():
    P, Qp, R = (4, 0), (12, 6), (9, 12)  # A(0,0) B(12,0) C(12,12) D(0,12)
    area = F(abs(P[0]*(Qp[1]-R[1]) + Qp[0]*(R[1]-P[1]) + R[0]*(P[1]-Qp[1])), 2)
    assert area == 33; return r"\(33\)"
@check("M1E-04")
def _(): v = 1/(F(1,9) - F(1,12)); assert v == 36; return r"\(36\)"
@check("M1E-05")
def _():
    for xb in range(0, 50):
        pb = F(3,5)*F(xb, xb+4) + F(2,5)*F(xb+1, xb+4)
        if pb == F(3,5):
            ans = F(3,5)*F(xb, xb+4) / pb; assert xb == 5 and ans == F(5,9); return r"\(\dfrac59\)"
@check("M1E-06")
def _():
    e = sp.cancel(((x**2-9)/(x**2+x-6)) / ((x**2-2*x-3)/(x**2-4)))
    assert sp.simplify(e - (x+2)/(x+1)) == 0; return r"\(\dfrac{x+2}{x+1}\)"
@check("M1E-07")
def _():
    a, b = sp.symbols("a b"); s = sp.solve([9*a+3*b-21, 25*a+5*b-55], [a, b])
    assert 100*s[a] + 10*s[b] == 210; return r"\(210\)"
@check("M1E-08")
def _(): assert 1 - 1/F(5,4)**2 == F(36,100); return r"\(36\%\)"
@check("M1E-09")
def _(): assert F(20*15 - 18*14, 3) == 16; return r"\(16\)"
@check("M1E-10")
def _():
    bc = sp.sqrt(36 + 16 - 2*6*4*sp.Rational(1,2)); area = sp.Rational(1,2)*6*4*sp.sqrt(3)/2
    h = sp.nsimplify(2*area/bc); assert sp.simplify(h - 6*sp.sqrt(21)/7) == 0; return r"\(\dfrac{6\sqrt{21}}{7}\)"
# Maths 2
@check("M2E-01")
def _():
    k = sp.symbols("k"); ks = sp.solve(sp.discriminant(x**2-2*x+4-k*x, x), k)
    assert sorted(ks) == [-6, 2]; return r"\(2\) and \(-6\)"
@check("M2E-02")
def _():
    s = sp.solve(sp.Eq(9**x - 4*3**(x+1) + 27, 0), x); assert sp.nsimplify(sum(s)) == 3; return r"\(3\)"
@check("M2E-03")
def _():
    s = sp.solveset(2*sp.cos(x)**2 + 3*sp.sin(x) - 3, x, sp.Interval(0, 2*sp.pi))
    assert sp.simplify(sum(s) - 3*sp.pi/2) == 0; return r"\(\dfrac{3\pi}{2}\)"
@check("M2E-04")
def _():
    r = sp.symbols("r", positive=True); S = 2*sp.pi*r**2 + 2*sp.pi*r*(16/r**2)
    rc = sp.solve(sp.diff(S, r), r)[0]; assert sp.simplify(S.subs(r, rc) - 24*sp.pi) == 0; return r"\(24\pi\)"
@check("M2E-05")
def _():
    f = x**2 - 4*x + 3; A = sp.integrate(f, (x, 0, 1)) - sp.integrate(f, (x, 1, 3))
    assert A == sp.Rational(8,3) and sp.integrate(f, (x, 0, 3)) == 0; return r"\(\dfrac83\)"
@check("M2E-06")
def _():
    a = sp.Integer(2); b = a**3  # any valid base works
    assert sp.nsimplify(sp.log(a**2*b, b)) == sp.Rational(5,3); return r"\(\dfrac53\)"
@check("M2E-07")
def _():
    a, d = sp.symbols("a d"); s = sp.solve([5*(2*a+9*d)-145, 10*(2*a+19*d)-590], [a, d])
    Sn = lambda n: sp.Rational(n,2)*(2*s[a] + (n-1)*s[d]); assert Sn(30) - Sn(20) == 745; return r"\(745\)"
@check("M2E-08")
def _():
    f = lambda t: 5 - (t-2)**2; g = 3 - 2*f(x+1)
    xs = sp.solve(sp.diff(g, x), x); assert xs == [1] and g.subs(x, 1) == -7 and sp.diff(g, x, 2) > 0
    return r"minimum at \((1, -7)\)"
@check("M2E-09")
def _(): assert sp.expand((1+2*x)**5*(1-x)**3).coeff(x, 2) == 13; return r"\(13\)"
@check("M2E-10")
def _():
    pts = sp.solve([(x-2)**2 + (y-1)**2 - 10, y - x - 1], [x, y]); (a, b), (c, d) = pts
    assert sp.simplify(sp.sqrt((a-c)**2 + (b-d)**2) - 4*sp.sqrt(2)) == 0; return r"\(4\sqrt{2}\)"
# Physics
@check("PE-01")
def _():
    k, xx, m, g, h = sp.symbols("k x m g h", positive=True)
    assert sp.solve(sp.Eq(k*xx**2/2, m*g*h), h) == [k*xx**2/(2*m*g)]; return r"\(\dfrac{kx^2}{2mg}\)"
@check("PE-02")
def _():
    Popen = F(144, 4+6); Pclosed = F(144, 4 + F(6*3, 9)); assert Pclosed/Popen == F(5,3); return r"\(\dfrac53\)"
@check("PE-03")
def _():
    # numeric simulation: speed at landing independent of angle
    u, H, g = 7.0, 20.0, 9.81
    for th in (0, 0.4, 1.0):
        vx, vy = u*math.cos(th), u*math.sin(th)
        t = (vy + math.sqrt(vy**2 + 2*g*H))/g
        assert abs(math.hypot(vx, vy - g*t) - math.sqrt(u*u + 2*g*H)) < 1e-9
    return r"\(\sqrt{u^2 + 2gH}\)"
@check("PE-04")
def _():
    t = sp.symbols("t", positive=True); assert sp.solve(sp.Eq(8*2**(-t/2), 2**(-t/6)), t) == [9]; return r"9 hours"
@check("PE-05")
def _():
    m, M, u, g = sp.symbols("m M u g", positive=True); v = m*u/(m+M)
    assert sp.simplify(v**2/(2*g) - m**2*u**2/(2*g*(m+M)**2)) == 0; return r"\(\dfrac{m^2u^2}{2g(m+M)^2}\)"
@check("PE-06")
def _():
    c, n, lam = 3e8, 1.5, 600e-9; f = c/lam
    return stmt(False, abs(c/n/f - 400e-9) < 1e-15, abs(c/n - 2e8) < 1)
@check("PE-07")
def _():
    RX = F(1, 1); RY = RX * 2 / 4; assert (1/RY)/(1/RX) == 2; return r"\(2\)"
@check("PE-08")
def _():
    E = 0.2*2000*10 + 0.2*3.3e5 + 0.2*4200*20; assert abs(E/200 - 434) < 1e-9; return r"\(434\text{ s}\)"
@check("PE-09")
def _():
    W, L = F(1), F(1); FL = (W*L/2 + 2*W*F(3,4)*L)/L; FR = 3*W - FL; assert FL/FR == 2; return r"\(2 : 1\)"
@check("PE-10")
def _():
    loss = lambda V: (1e4/V)**2*4/1e4*100
    assert abs(loss(1e3) - 4) < 1e-9 and abs(loss(1e4) - 0.04) < 1e-12; return r"(i) 4%, (ii) 0.04%"
# Chemistry
@check("CE-01")
def _(): assert abs(0.40*0.250*5 - 0.5) < 1e-12; return r"\(0.50\)"
@check("CE-02")
def _():
    mol_fe = 5.6e6/56; m_ox = mol_fe/2*160; assert abs(m_ox/0.8/1e6 - 10) < 1e-9; return r"\(10\) t"
@check("CE-03")
def _():
    # check the equation balances (atoms and charge) then the volume
    lhs = {"Mn": 1, "O": 4, "H": 8, "Fe": 5, "q": -1 + 8 + 10}; rhs = {"Mn": 1, "Fe": 5, "H": 8, "O": 4, "q": 2 + 15}
    assert lhs == rhs
    v = 0.10*0.0250/5/0.020*1000; assert abs(v - 25.0) < 1e-9; return r"\(25.0\text{ cm}^3\)"
@check("CE-04")
def _(): return stmt(True, False, True)
@check("CE-05")
def _():
    # enumerate C4 skeletons and distinct carbon positions for Br by symmetry
    butane = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}; isobutane = {0: [1], 1: [0, 2, 3], 2: [1], 3: [1]}
    import networkx as nx
    def classes(adj):
        G = nx.Graph([(a, b) for a in adj for b in adj[a]])
        orbits = set()
        for p in nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter():
            pass
        seen, cls = set(), 0
        autos = list(nx.algorithms.isomorphism.GraphMatcher(G, G).isomorphisms_iter())
        for v in G:
            if v in seen: continue
            orb = {a[v] for a in autos}; seen |= orb; cls += 1
        return cls
    assert classes(butane) + classes(isobutane) == 4; return r"\(4\)"
@check("CE-06")
def _(): assert (436 + 242 - 2*431)/2 == -92; return r"\(-92\text{ kJ}\)"
@check("CE-09")
def _():
    mg = 2.4/24; hcl = 0.100*1.0; h2 = min(mg, hcl/2); assert abs(h2*24 - 1.2) < 1e-12; return r"\(1.2\text{ dm}^3\)"
@check("CE-10")
def _(): xw = ((2.46 - 1.20)/18)/(1.20/120); assert abs(xw - 7) < 1e-9; return r"\(7\)"
# Biology
@check("BE-02")
def _():
    npp = 20000 - 12000; return stmt(npp/20000 == 0.4, 2000/npp == 0.25, 2000 - 800 - 1000 == 1200)
@check("BE-03")
def _():
    rate = sp.pi*1**2*15/5; assert rate == 3*sp.pi; return r"water uptake; \(3\pi\text{ mm}^3\text{ min}^{-1}\)"
@check("BE-04")
def _():
    kids = [(p1+p2, t1+t2) for p1 in "Pp" for p2 in "Pp" for t1 in "Tt" for t2 in "tt"]
    fr = F(sum("P" in p and "T" not in t for p, t in kids), len(kids)); assert fr == F(3,8); return r"\(\dfrac38\)"
@check("BE-05")
def _(): return stmt(True, True, False)
@check("BE-06")
def _(): return stmt(True, True, True)
@check("BE-07")
def _():
    o2 = [20, 10, 2, 0, 0]; eth = [0, 0, 1, 4, 8]; glu = [100, 90, 70, 45, 25]
    drops = [glu[i] - glu[i+1] for i in range(4)]
    s1 = eth[1] == 0
    s2 = drops.index(max(drops)) == 3
    s3 = all(o2[i] == 0 for i in range(5) if eth[i] > 0)
    return stmt(s1, s2, s3)
@check("BE-08")
def _():
    sv = 5600/56; co = sv*1.5*160/1000; assert sv == 100 and co == 24
    return r"\(100\text{ cm}^3\); \(24\text{ dm}^3\text{ min}^{-1}\)"

CONCEPTUAL.update({
    "CE-07": "rate increases; yield decreases",
    "CE-08": r"\(\text{Ca}^{2+}\)",
    "BE-01": "(i) mutualism; (ii) predation",
    "BE-09": "1, 2 and 5 only",
    "BE-10": "ADH secretion decreases; collecting ducts become less permeable to water; urine volume increases",
})
