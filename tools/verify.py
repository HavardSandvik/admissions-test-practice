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
