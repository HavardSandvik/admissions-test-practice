r"""ESAT practice question bank.

Edit questions here, then run:  python3 tools/questions.py
It checks every question against an independent calculation (tools/verify.py)
and writes questions.js for the site.

Fields: id, module, level (foundation | esat), set, topic, q, options, answer (0-based index), solution.
Maths uses KaTeX with \( ... \) delimiters.
"""
import json, os, sys

Q = []
LEVEL = "foundation"   # switched to "esat" before the ESAT-level sets below
def add(id, module, set_, topic, q, options, answer, solution):
    Q.append(dict(id=id, module=module, level=LEVEL, set=set_, topic=topic, q=q,
                  options=options, answer="ABCDEFGH".index(answer), solution=solution))

# ---------------------------------------------------------------- Maths 1, set 1
add("M1-01", "m1", 1, "Surds",
    r"What is the value of \((\sqrt{12} + \sqrt{27})^2\)?",
    [r"\(15\)", r"\(39\)", r"\(75\)", r"\(39 + 18\sqrt{3}\)", r"\(225\)"], "C",
    r"\(\sqrt{12} = 2\sqrt{3}\) and \(\sqrt{27} = 3\sqrt{3}\), so the sum is \(5\sqrt{3}\). Squaring gives \(25 \times 3 = 75\). (39 comes from wrongly squaring each term separately.)")

add("M1-02", "m1", 1, "Algebra: rearranging",
    r"Given \(y = \dfrac{2x + 3}{x - 1}\), which of the following expresses \(x\) in terms of \(y\)?",
    [r"\(x = \dfrac{y - 3}{y - 2}\)", r"\(x = \dfrac{y + 3}{2 - y}\)", r"\(x = \dfrac{y + 3}{y + 2}\)",
     r"\(x = \dfrac{y + 3}{y - 2}\)", r"\(x = \dfrac{3 - y}{y + 2}\)"], "D",
    r"\(y(x-1) = 2x + 3 \Rightarrow xy - y = 2x + 3 \Rightarrow x(y - 2) = y + 3 \Rightarrow x = \dfrac{y+3}{y-2}\).")

add("M1-03", "m1", 1, "Percentages",
    r"The price of an item is increased by 20% and the new price is then decreased by 25%. What is the overall percentage change from the original price?",
    [r"5% decrease", r"10% decrease", r"5% increase", r"No change", r"15% decrease"], "B",
    r"Multipliers: \(1.2 \times 0.75 = 0.9\), so the final price is 90% of the original, a 10% decrease.")

add("M1-04", "m1", 1, "Simultaneous equations",
    r"The line \(y = x + 1\) meets the circle \(x^2 + y^2 = 25\) at two points. What is the distance between these two points?",
    [r"\(7\)", r"\(5\sqrt{2}\)", r"\(10\)", r"\(7\sqrt{2}\)", r"\(\sqrt{50}+1\)", r"\(14\)"], "D",
    r"Substitute: \(x^2 + (x+1)^2 = 25 \Rightarrow x^2 + x - 12 = 0 \Rightarrow x = 3\) or \(x = -4\). Points \((3, 4)\) and \((-4, -3)\). Distance \(= \sqrt{7^2 + 7^2} = 7\sqrt{2}\).")

add("M1-05", "m1", 1, "Probability",
    r"A bag contains 4 red and 6 blue counters. Two counters are taken at random without replacement. What is the probability that they are different colours?",
    [r"\(\dfrac{12}{25}\)", r"\(\dfrac{4}{15}\)", r"\(\dfrac{8}{15}\)", r"\(\dfrac{24}{50}\)", r"\(\dfrac{7}{15}\)"], "C",
    r"\(P(\text{RB}) + P(\text{BR}) = \dfrac{4}{10}\cdot\dfrac{6}{9} + \dfrac{6}{10}\cdot\dfrac{4}{9} = \dfrac{48}{90} = \dfrac{8}{15}\). (12/25 is the with-replacement answer.)")

add("M1-06", "m1", 1, "Ratio",
    r"\(a : b = 3 : 4\) and \(b : c = 6 : 5\). Given that \(a + b + c = 155\), what is the value of \(c\)?",
    [r"\(25\)", r"\(40\)", r"\(45\)", r"\(50\)", r"\(60\)", r"\(62\)"], "D",
    r"Make \(b\) match: \(a:b = 9:12\), \(b:c = 12:10\), so \(a:b:c = 9:12:10\), which is 31 parts. One part is \(155/31 = 5\), so \(c = 50\).")

add("M1-07", "m1", 1, "Averages",
    r"The mean of five numbers is 12. One number is removed and the mean of the remaining four numbers is 10. What number was removed?",
    [r"\(2\)", r"\(10\)", r"\(12\)", r"\(20\)", r"\(22\)"], "D",
    r"Total of five numbers \(= 60\); total of four \(= 40\). Removed number \(= 60 - 40 = 20\).")

add("M1-08", "m1", 1, "Circles: arcs and sectors",
    r"A sector of a circle has radius 6 cm and angle \(40^\circ\). What is the perimeter of the sector, in cm?",
    [r"\(\dfrac{4\pi}{3}\)", r"\(4\pi\)", r"\(12 + \dfrac{4\pi}{3}\)", r"\(12 + 4\pi\)", r"\(6 + \dfrac{4\pi}{3}\)", r"\(12 + \dfrac{2\pi}{3}\)"], "C",
    r"Arc length \(= \dfrac{40}{360}\times 2\pi \times 6 = \dfrac{4\pi}{3}\). Perimeter \(=\) arc \(+\) two radii \(= 12 + \dfrac{4\pi}{3}\). (\(4\pi\) is the area.)")

add("M1-09", "m1", 1, "Surds",
    r"Which of the following is equal to \(\dfrac{6}{3 - \sqrt{3}}\)?",
    [r"\(3 - \sqrt{3}\)", r"\(3 + \sqrt{3}\)", r"\(1 + \sqrt{3}\)", r"\(\dfrac{3 + \sqrt{3}}{2}\)", r"\(6 + 2\sqrt{3}\)"], "B",
    r"Multiply top and bottom by \(3 + \sqrt{3}\): \(\dfrac{6(3+\sqrt{3})}{9 - 3} = 3 + \sqrt{3}\).")

add("M1-10", "m1", 1, "Proportion",
    r"\(y\) is inversely proportional to \(x^2\). If \(x\) is increased by 50%, by what factor is \(y\) multiplied?",
    [r"\(\dfrac{1}{3}\)", r"\(\dfrac{4}{9}\)", r"\(\dfrac{2}{3}\)", r"\(\dfrac{3}{4}\)", r"\(\dfrac{9}{4}\)"], "B",
    r"\(y = k/x^2\). Replacing \(x\) by \(1.5x\) multiplies \(y\) by \(1/1.5^2 = 1/2.25 = 4/9\).")

# ---------------------------------------------------------------- Maths 1, set 2
add("M1-11", "m1", 2, "Inequalities",
    r"How many integers \(x\) satisfy \(x^2 - 5x - 14 < 0\)?",
    [r"\(6\)", r"\(7\)", r"\(8\)", r"\(9\)", r"\(10\)"], "C",
    r"\((x-7)(x+2) < 0 \Rightarrow -2 < x < 7\). Integers \(-1, 0, 1, \dots, 6\): that is 8 integers.")

add("M1-12", "m1", 2, "Trigonometry: cosine rule",
    r"A triangle has sides of length 5, 7 and 8. What is the size of the angle opposite the side of length 7?",
    [r"\(30^\circ\)", r"\(45^\circ\)", r"\(60^\circ\)", r"\(90^\circ\)", r"\(120^\circ\)"], "C",
    r"\(\cos\theta = \dfrac{5^2 + 8^2 - 7^2}{2 \cdot 5 \cdot 8} = \dfrac{40}{80} = \dfrac{1}{2}\), so \(\theta = 60^\circ\).")

add("M1-13", "m1", 2, "Indices",
    r"Solve \(2^{x+1} \times 4^{x} = 32\).",
    [r"\(x = 1\)", r"\(x = \dfrac{4}{3}\)", r"\(x = 2\)", r"\(x = \dfrac{3}{2}\)", r"\(x = \dfrac{5}{3}\)"], "B",
    r"\(4^x = 2^{2x}\), so \(2^{3x+1} = 2^5 \Rightarrow 3x + 1 = 5 \Rightarrow x = \dfrac{4}{3}\).")

add("M1-14", "m1", 2, "Speed, distance, time",
    r"A car travels 30 km at 60 km/h and then a further 30 km at 40 km/h. What is its average speed for the whole journey, in km/h?",
    [r"\(45\)", r"\(48\)", r"\(50\)", r"\(52\)", r"\(55\)"], "B",
    r"Time \(= 0.5 + 0.75 = 1.25\) h for 60 km, so average speed \(= 60/1.25 = 48\) km/h. (50 is the incorrect mean of the two speeds.)")

add("M1-15", "m1", 2, "Mensuration: volume",
    r"A sphere of radius \(r\) has the same volume as a cylinder of radius \(r\). What is the height of the cylinder?",
    [r"\(\dfrac{2r}{3}\)", r"\(r\)", r"\(\dfrac{4r}{3}\)", r"\(2r\)", r"\(\dfrac{3r}{4}\)"], "C",
    r"\(\tfrac{4}{3}\pi r^3 = \pi r^2 h \Rightarrow h = \tfrac{4}{3}r\).")

add("M1-16", "m1", 2, "Coordinate geometry: lines",
    r"Which line passes through \((1, 2)\) and is perpendicular to \(2x + 3y = 6\)?",
    [r"\(3x - 2y + 1 = 0\)", r"\(2x + 3y - 8 = 0\)", r"\(3x + 2y - 7 = 0\)", r"\(3x - 2y - 1 = 0\)", r"\(2x - 3y + 4 = 0\)"], "A",
    r"Given line has gradient \(-\tfrac{2}{3}\), so the perpendicular gradient is \(\tfrac{3}{2}\). \(y - 2 = \tfrac{3}{2}(x - 1) \Rightarrow 2y - 4 = 3x - 3 \Rightarrow 3x - 2y + 1 = 0\). Check: \(3 - 4 + 1 = 0\).")

add("M1-17", "m1", 2, "Standard form",
    r"What is \(\dfrac{(6 \times 10^{5}) \times (4 \times 10^{-8})}{8 \times 10^{-2}}\)?",
    [r"\(3 \times 10^{-5}\)", r"\(3 \times 10^{-2}\)", r"\(3 \times 10^{-1}\)", r"\(3 \times 10^{1}\)", r"\(0.3 \times 10^{-2}\)"], "C",
    r"Numerator \(= 24 \times 10^{-3}\). Dividing by \(8 \times 10^{-2}\) gives \(3 \times 10^{-1}\).")

add("M1-18", "m1", 2, "Averages",
    r"Five positive integers have mean 6, median 5 and a unique mode of 3. What is the largest possible value of the largest integer?",
    [r"\(11\)", r"\(12\)", r"\(13\)", r"\(14\)", r"\(15\)"], "C",
    r"Ordered: \(a \le b \le 5 \le d \le e\), sum 30. A unique mode of 3 needs \(a = b = 3\) (and no other repeated value). Then \(d + e = 19\). \(d = 5\) would make 5 appear twice and tie the mode, so \(d \ge 6\), giving \(e \le 13\): the set \(3, 3, 5, 6, 13\).")

add("M1-19", "m1", 2, "Similarity",
    r"Two cones are mathematically similar. The ratio of their surface areas is \(4 : 9\). The smaller cone has volume \(40\text{ cm}^3\). What is the volume of the larger cone, in \(\text{cm}^3\)?",
    [r"\(60\)", r"\(90\)", r"\(120\)", r"\(135\)", r"\(202.5\)"], "D",
    r"Length ratio \(= 2 : 3\), so volume ratio \(= 8 : 27\). Larger volume \(= 40 \times \tfrac{27}{8} = 135\).")

add("M1-20", "m1", 2, "Probability",
    r"Events \(A\) and \(B\) are independent, with \(P(A) = 0.3\) and \(P(B) = 0.5\). What is the probability that exactly one of \(A\) and \(B\) occurs?",
    [r"\(0.15\)", r"\(0.35\)", r"\(0.5\)", r"\(0.65\)", r"\(0.8\)"], "C",
    r"\(P(A)P(B') + P(A')P(B) = 0.3 \times 0.5 + 0.7 \times 0.5 = 0.15 + 0.35 = 0.5\).")

# ---------------------------------------------------------------- Maths 2, set 1
add("M2-01", "m2", 1, "Integration",
    r"Evaluate \(\displaystyle\int_0^2 (3x^2 - 2x + 1)\,dx\).",
    [r"\(4\)", r"\(6\)", r"\(8\)", r"\(10\)", r"\(12\)"], "B",
    r"\(\left[x^3 - x^2 + x\right]_0^2 = 8 - 4 + 2 = 6\).")

add("M2-02", "m2", 1, "Differentiation: stationary points",
    r"What is the greatest value of \(y = x^3 - 6x^2 + 9x + 1\) for \(0 \le x \le 5\)?",
    [r"\(1\)", r"\(5\)", r"\(9\)", r"\(21\)", r"\(31\)"], "D",
    r"\(y' = 3(x-1)(x-3)\): local max \(y(1) = 5\), local min \(y(3) = 1\). But check the endpoints: \(y(0) = 1\), \(y(5) = 125 - 150 + 45 + 1 = 21\). The greatest value is 21, at the endpoint.")

add("M2-03", "m2", 1, "Logarithms",
    r"Find all real solutions of \(\log_2 x + \log_2 (x - 2) = 3\).",
    [r"\(x = -2\) only", r"\(x = 4\) only", r"\(x = -2\) and \(x = 4\)", r"\(x = 5\) only", r"\(x = 2 + \sqrt{3}\) only"], "B",
    r"\(\log_2[x(x-2)] = 3 \Rightarrow x^2 - 2x - 8 = 0 \Rightarrow x = 4\) or \(-2\). \(x = -2\) is rejected because the logarithms need \(x > 2\).")

add("M2-04", "m2", 1, "Geometric series",
    r"A geometric series has first term 12 and sum to infinity 18. What is the third term?",
    [r"\(\dfrac{4}{9}\)", r"\(\dfrac{4}{3}\)", r"\(\dfrac{8}{3}\)", r"\(4\)", r"\(\dfrac{16}{3}\)"], "B",
    r"\(\dfrac{12}{1 - r} = 18 \Rightarrow r = \tfrac{1}{3}\). Third term \(= 12 \times \left(\tfrac{1}{3}\right)^2 = \tfrac{4}{3}\).")

add("M2-05", "m2", 1, "Trigonometric equations",
    r"How many solutions does \(\sin 2x = \cos x\) have for \(0 \le x \le 2\pi\)?",
    [r"\(1\)", r"\(2\)", r"\(3\)", r"\(4\)", r"\(6\)"], "D",
    r"\(2\sin x\cos x = \cos x \Rightarrow \cos x(2\sin x - 1) = 0\). \(\cos x = 0\): \(x = \tfrac{\pi}{2}, \tfrac{3\pi}{2}\). \(\sin x = \tfrac12\): \(x = \tfrac{\pi}{6}, \tfrac{5\pi}{6}\). Four solutions. (Dividing by \(\cos x\) loses two.)")

add("M2-06", "m2", 1, "Binomial expansion",
    r"What is the coefficient of \(x^3\) in the expansion of \((2 - x)^6\)?",
    [r"\(-160\)", r"\(-120\)", r"\(-20\)", r"\(120\)", r"\(160\)"], "A",
    r"\(\binom{6}{3}\,2^3(-x)^3 = 20 \times 8 \times (-1)\,x^3 = -160x^3\).")

add("M2-07", "m2", 1, "Coordinate geometry: circles",
    r"The circle \(x^2 + y^2 - 6x + 4y - 12 = 0\) is given. What is the length of a tangent drawn to the circle from the point \((10, 2)\)?",
    [r"\(5\)", r"\(\sqrt{65}\)", r"\(2\sqrt{10}\)", r"\(\sqrt{65} - 5\)", r"\(3\sqrt{5}\)"], "C",
    r"\((x-3)^2 + (y+2)^2 = 25\): centre \((3, -2)\), radius 5. Distance\(^2\) from \((10,2)\) to centre \(= 49 + 16 = 65\). The tangent is perpendicular to the radius, so length\(^2 = 65 - 25 = 40\), length \(= 2\sqrt{10}\).")

add("M2-08", "m2", 1, "Integration: area",
    r"What is the area of the finite region enclosed by \(y = x^2\) and \(y = 2x\)?",
    [r"\(\dfrac{2}{3}\)", r"\(\dfrac{4}{3}\)", r"\(\dfrac{8}{3}\)", r"\(4\)", r"\(\dfrac{20}{3}\)"], "B",
    r"They meet at \(x = 0, 2\). Area \(= \displaystyle\int_0^2 (2x - x^2)\,dx = 4 - \tfrac{8}{3} = \tfrac{4}{3}\).")

add("M2-09", "m2", 1, "Functions: composition",
    r"\(f(x) = 2x + 1\) and \(g(x) = x^2\). What is the sum of all solutions of \(fg(x) = gf(x)\)?",
    [r"\(-4\)", r"\(-2\)", r"\(0\)", r"\(2\)", r"\(4\)"], "B",
    r"\(fg(x) = 2x^2 + 1\), \(gf(x) = (2x+1)^2 = 4x^2 + 4x + 1\). Equating: \(2x^2 + 4x = 0 \Rightarrow x = 0\) or \(x = -2\). Sum \(= -2\).")

add("M2-10", "m2", 1, "Arithmetic series",
    r"The sum of the first \(n\) terms of a sequence is \(S_n = 3n^2 + 2n\). What is the 10th term?",
    [r"\(53\)", r"\(59\)", r"\(62\)", r"\(320\)", r"\(32\)"], "B",
    r"\(u_{10} = S_{10} - S_9 = 320 - 261 = 59\). (In general \(u_n = 6n - 1\).)")

# ---------------------------------------------------------------- Physics, set 1
add("P-01", "phys", 1, "Kinematics",
    r"A car accelerates uniformly from rest to \(20\text{ m s}^{-1}\) in 8.0 s. How far does it travel in this time?",
    [r"\(40\text{ m}\)", r"\(80\text{ m}\)", r"\(160\text{ m}\)", r"\(320\text{ m}\)", r"\(2.5\text{ m}\)"], "B",
    r"Distance \(=\) average speed \(\times\) time \(= \tfrac{0 + 20}{2} \times 8 = 80\) m.")

add("P-02", "phys", 1, "Projectiles",
    r"A ball is thrown horizontally at \(15\text{ m s}^{-1}\) from the top of a cliff 45 m high. Ignoring air resistance and taking \(g = 10\text{ m s}^{-2}\), how far from the base of the cliff does it land?",
    [r"\(15\text{ m}\)", r"\(30\text{ m}\)", r"\(45\text{ m}\)", r"\(67.5\text{ m}\)", r"\(90\text{ m}\)"], "C",
    r"Vertical: \(45 = \tfrac12 \times 10 \times t^2 \Rightarrow t = 3\) s. Horizontal speed is constant: \(15 \times 3 = 45\) m.")

add("P-03", "phys", 1, "Circuits",
    r"A \(6\,\Omega\) resistor and a \(3\,\Omega\) resistor are connected in parallel. This combination is connected in series with a \(4\,\Omega\) resistor across a 12 V supply of negligible internal resistance. What is the current in the \(3\,\Omega\) resistor?",
    [r"\(\dfrac{2}{3}\text{ A}\)", r"\(1\text{ A}\)", r"\(\dfrac{4}{3}\text{ A}\)", r"\(2\text{ A}\)", r"\(4\text{ A}\)"], "C",
    r"Parallel pair: \(\tfrac{6 \times 3}{6 + 3} = 2\,\Omega\). Total \(6\,\Omega\), so the supply current is 2 A. P.d. across the pair \(= 2 \times 2 = 4\) V, so the current in \(3\,\Omega\) is \(4/3\) A.")

add("P-04", "phys", 1, "Thermal physics",
    r"A 2.0 kW kettle heats 0.50 kg of water from \(20^\circ\text{C}\) to \(100^\circ\text{C}\). The specific heat capacity of water is \(4200\text{ J kg}^{-1}\,\text{K}^{-1}\). Assuming no energy losses, how long does this take?",
    [r"\(21\text{ s}\)", r"\(42\text{ s}\)", r"\(84\text{ s}\)", r"\(105\text{ s}\)", r"\(168\text{ s}\)"], "C",
    r"\(E = mc\Delta T = 0.5 \times 4200 \times 80 = 168\,000\) J. \(t = E/P = 168\,000/2000 = 84\) s.")

add("P-05", "phys", 1, "Waves",
    r"A wave has frequency 50 Hz and wavelength 40 cm. How long does it take to travel 100 m?",
    [r"\(0.2\text{ s}\)", r"\(2\text{ s}\)", r"\(5\text{ s}\)", r"\(20\text{ s}\)", r"\(50\text{ s}\)"], "C",
    r"\(v = f\lambda = 50 \times 0.40 = 20\text{ m s}^{-1}\). Time \(= 100/20 = 5\) s. (Watch the cm-to-m conversion.)")

add("P-06", "phys", 1, "Radioactivity",
    r"A radioactive isotope has a half-life of 6 hours. What fraction of the original nuclei has decayed after 1 day?",
    [r"\(\dfrac{1}{16}\)", r"\(\dfrac{1}{4}\)", r"\(\dfrac{3}{4}\)", r"\(\dfrac{7}{8}\)", r"\(\dfrac{15}{16}\)"], "E",
    r"24 h is 4 half-lives, so \(\left(\tfrac12\right)^4 = \tfrac{1}{16}\) remains and \(\tfrac{15}{16}\) has decayed.")

add("P-07", "phys", 1, "Momentum and energy",
    r"A 2.0 kg trolley moving at \(3.0\text{ m s}^{-1}\) collides with a stationary 1.0 kg trolley. They stick together. How much kinetic energy is lost in the collision?",
    [r"\(0\text{ J}\)", r"\(3\text{ J}\)", r"\(6\text{ J}\)", r"\(9\text{ J}\)", r"\(4.5\text{ J}\)"], "B",
    r"Momentum: \(2 \times 3 = 3v \Rightarrow v = 2\text{ m s}^{-1}\). KE before \(= \tfrac12 \cdot 2 \cdot 9 = 9\) J; after \(= \tfrac12 \cdot 3 \cdot 4 = 6\) J. Lost: 3 J.")

add("P-08", "phys", 1, "Power and efficiency",
    r"A motor lifts a 50 kg load vertically through 12 m in 20 s at constant speed. The motor is 60% efficient. What is the electrical power input to the motor? (\(g = 10\text{ N kg}^{-1}\))",
    [r"\(180\text{ W}\)", r"\(300\text{ W}\)", r"\(360\text{ W}\)", r"\(500\text{ W}\)", r"\(600\text{ W}\)"], "D",
    r"Useful power \(= mgh/t = 50 \times 10 \times 12 / 20 = 300\) W. Input \(= 300/0.6 = 500\) W.")

add("P-09", "phys", 1, "Pressure in fluids",
    r"Atmospheric pressure is \(1.0 \times 10^5\text{ Pa}\) and the density of water is \(1000\text{ kg m}^{-3}\). What is the total pressure on a diver 20 m below the surface of a lake? (\(g = 10\text{ N kg}^{-1}\))",
    [r"\(2.0 \times 10^5\text{ Pa}\)", r"\(3.0 \times 10^5\text{ Pa}\)", r"\(1.2 \times 10^5\text{ Pa}\)", r"\(2.1 \times 10^5\text{ Pa}\)", r"\(3.0 \times 10^6\text{ Pa}\)"], "B",
    r"Water pressure \(= \rho g h = 1000 \times 10 \times 20 = 2.0 \times 10^5\) Pa. Add atmospheric: \(3.0 \times 10^5\) Pa.")

add("P-10", "phys", 1, "Transformers",
    r"An ideal transformer has 2000 turns on its primary coil, which is connected to a 240 V supply. The secondary output is 12 V and the secondary current is 4.0 A. What are the number of secondary turns and the primary current?",
    [r"100 turns, 80 A", r"100 turns, 0.20 A", r"40 000 turns, 0.20 A", r"200 turns, 0.40 A", r"100 turns, 4.0 A"], "B",
    r"\(N_s = 2000 \times \tfrac{12}{240} = 100\). Ideal: \(V_pI_p = V_sI_s \Rightarrow I_p = \tfrac{12 \times 4}{240} = 0.20\) A.")

# ---------------------------------------------------------------- Chemistry, set 1
add("C-01", "chem", 1, "Moles",
    r"What is the mass of 0.25 mol of calcium carbonate, \(\text{CaCO}_3\)? (\(A_r\): Ca = 40, C = 12, O = 16)",
    [r"\(17\text{ g}\)", r"\(25\text{ g}\)", r"\(68\text{ g}\)", r"\(100\text{ g}\)", r"\(400\text{ g}\)"], "B",
    r"\(M_r = 40 + 12 + 3 \times 16 = 100\). Mass \(= 0.25 \times 100 = 25\) g.")

add("C-02", "chem", 1, "Balancing equations",
    r"Propane burns completely: \(\text{C}_3\text{H}_8 + a\,\text{O}_2 \rightarrow b\,\text{CO}_2 + c\,\text{H}_2\text{O}\). In the balanced equation with smallest whole numbers, what is \(a + b + c\)?",
    [r"\(9\)", r"\(10\)", r"\(11\)", r"\(12\)", r"\(13\)"], "D",
    r"C: \(b = 3\). H: \(c = 4\). O: \(2a = 6 + 4 = 10 \Rightarrow a = 5\). Sum \(= 12\).")

add("C-03", "chem", 1, "Titration calculations",
    r"\(25.0\text{ cm}^3\) of sodium hydroxide solution is exactly neutralised by \(20.0\text{ cm}^3\) of \(0.150\text{ mol dm}^{-3}\) sulfuric acid. What is the concentration of the sodium hydroxide?",
    [r"\(0.060\text{ mol dm}^{-3}\)", r"\(0.120\text{ mol dm}^{-3}\)", r"\(0.188\text{ mol dm}^{-3}\)", r"\(0.240\text{ mol dm}^{-3}\)", r"\(0.375\text{ mol dm}^{-3}\)"], "D",
    r"\(n(\text{H}_2\text{SO}_4) = 0.150 \times 0.0200 = 0.00300\) mol. \(2\text{NaOH} + \text{H}_2\text{SO}_4\), so \(n(\text{NaOH}) = 0.00600\) mol. Concentration \(= 0.00600/0.0250 = 0.240\text{ mol dm}^{-3}\). (0.120 forgets the 2 : 1 ratio.)")

add("C-04", "chem", 1, "Gas volumes",
    r"5.0 g of calcium carbonate reacts with excess hydrochloric acid. What volume of carbon dioxide is produced at room temperature and pressure? (\(M_r(\text{CaCO}_3) = 100\); 1 mol of gas occupies \(24\text{ dm}^3\) at RTP)",
    [r"\(0.12\text{ dm}^3\)", r"\(0.60\text{ dm}^3\)", r"\(1.2\text{ dm}^3\)", r"\(2.4\text{ dm}^3\)", r"\(12\text{ dm}^3\)"], "C",
    r"\(\text{CaCO}_3 + 2\text{HCl} \rightarrow \text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2\). \(n = 5.0/100 = 0.050\) mol of \(\text{CO}_2\), volume \(= 0.050 \times 24 = 1.2\text{ dm}^3\).")

add("C-05", "chem", 1, "Isotopes and relative atomic mass",
    r"Element X has two isotopes, \(^{69}\text{X}\) and \(^{71}\text{X}\). Its relative atomic mass is 69.8. What percentage of X atoms are \(^{69}\text{X}\)?",
    [r"\(20\%\)", r"\(40\%\)", r"\(60\%\)", r"\(80\%\)", r"\(90\%\)"], "C",
    r"\(69p + 71(100 - p) = 6980 \Rightarrow 7100 - 2p = 6980 \Rightarrow p = 60\%\). Sense check: 69.8 is nearer 69 than 71, so \(^{69}\text{X}\) is the majority.")

add("C-06", "chem", 1, "Oxidation states",
    r"In which species does the named element have the highest oxidation state?",
    [r"Mn in \(\text{MnO}_4^{-}\)", r"Cr in \(\text{Cr}_2\text{O}_7^{2-}\)", r"S in \(\text{SO}_4^{2-}\)", r"N in \(\text{NO}_3^{-}\)", r"Cl in \(\text{ClO}_3^{-}\)"], "A",
    r"Mn: \(x - 8 = -1 \Rightarrow +7\). Cr: \(2x - 14 = -2 \Rightarrow +6\). S: \(+6\). N: \(+5\). Cl: \(+5\). Highest is Mn, +7.")

add("C-07", "chem", 1, "Empirical and molecular formulae",
    r"A compound contains 40.0% carbon, 6.7% hydrogen and 53.3% oxygen by mass. Its relative molecular mass is 180. What is its molecular formula? (\(A_r\): C = 12, H = 1, O = 16)",
    [r"\(\text{CH}_2\text{O}\)", r"\(\text{C}_3\text{H}_6\text{O}_3\)", r"\(\text{C}_6\text{H}_{12}\text{O}_6\)", r"\(\text{C}_6\text{H}_6\text{O}_6\)", r"\(\text{C}_7\text{H}_{16}\text{O}_5\)"], "C",
    r"Moles per 100 g: C \(40/12 = 3.33\), H \(6.7/1 = 6.7\), O \(53.3/16 = 3.33\), ratio \(1 : 2 : 1\), empirical formula \(\text{CH}_2\text{O}\) (\(M_r = 30\)). \(180/30 = 6\), so \(\text{C}_6\text{H}_{12}\text{O}_6\).")

add("C-08", "chem", 1, "Intermolecular forces",
    r"Which of the following has the highest boiling point?",
    [r"\(\text{CH}_4\)", r"\(\text{NH}_3\)", r"\(\text{H}_2\text{O}\)", r"\(\text{HF}\)", r"\(\text{Ne}\)"], "C",
    r"\(\text{NH}_3\), \(\text{H}_2\text{O}\) and HF all hydrogen bond. Water forms on average two hydrogen bonds per molecule (two H atoms and two lone pairs), more than HF or \(\text{NH}_3\), so it has the highest boiling point (100 °C, versus about 20 °C for HF).")

add("C-09", "chem", 1, "Electrolysis",
    r"Concentrated aqueous sodium chloride is electrolysed using inert electrodes. What is produced at each electrode?",
    [r"Cathode: sodium; anode: chlorine", r"Cathode: hydrogen; anode: chlorine", r"Cathode: hydrogen; anode: oxygen", r"Cathode: chlorine; anode: hydrogen", r"Cathode: sodium; anode: oxygen"], "B",
    r"At the cathode, \(\text{H}^+\)/water is reduced in preference to the more reactive sodium, giving hydrogen. At the anode, concentrated chloride is oxidised to chlorine. (Oxygen forms only from dilute chloride solutions.)")

add("C-10", "chem", 1, "Equilibrium",
    r"\(\text{N}_2(\text{g}) + 3\text{H}_2(\text{g}) \rightleftharpoons 2\text{NH}_3(\text{g})\), \(\Delta H = -92\text{ kJ mol}^{-1}\). Which pair of changes would both increase the equilibrium yield of ammonia?",
    [r"Increase temperature, increase pressure", r"Increase temperature, decrease pressure", r"Decrease temperature, increase pressure", r"Decrease temperature, decrease pressure", r"Add a catalyst, increase pressure"], "C",
    r"Forward reaction is exothermic, so lower temperature shifts equilibrium right. 4 mol gas \(\rightarrow\) 2 mol gas, so higher pressure shifts right. A catalyst does not change the equilibrium yield.")

# ---------------------------------------------------------------- Biology, set 1
add("B-01", "bio", 1, "Enzymes",
    r"Which of the following statements about enzymes is/are correct?<br>1. Enzymes lower the activation energy of a reaction.<br>2. When an enzyme is denatured, the shape of its active site changes.<br>3. All human enzymes have an optimum pH of 7.",
    [r"1 only", r"2 only", r"3 only", r"1 and 2 only", r"1 and 3 only", r"1, 2 and 3"], "D",
    r"1 and 2 are correct. 3 is false: e.g. pepsin in the stomach has an optimum around pH 2.")

add("B-02", "bio", 1, "Genetics: monohybrid",
    r"Cystic fibrosis is caused by a recessive allele. Two parents are both carriers. Their first child does not have cystic fibrosis. What is the probability that this child is a carrier?",
    [r"\(\dfrac{1}{4}\)", r"\(\dfrac{1}{3}\)", r"\(\dfrac{1}{2}\)", r"\(\dfrac{2}{3}\)", r"\(\dfrac{3}{4}\)"], "D",
    r"Offspring: FF : Ff : ff \(= 1 : 2 : 1\). Given unaffected, only FF and Ff remain (3 equally likely), of which 2 are carriers: \(\tfrac{2}{3}\). (1/2 ignores the condition.)")

add("B-03", "bio", 1, "Cell division",
    r"A human body cell contains 46 chromosomes. How many chromatids are present in the cell at metaphase of mitosis, and how many chromosomes are in each cell produced by meiosis?",
    [r"46 chromatids; 23 chromosomes", r"92 chromatids; 23 chromosomes", r"92 chromatids; 46 chromosomes", r"46 chromatids; 46 chromosomes", r"184 chromatids; 23 chromosomes"], "B",
    r"DNA replicates before mitosis, so each of the 46 chromosomes has two chromatids: 92. Meiosis halves the chromosome number: 23.")

add("B-04", "bio", 1, "Circulation",
    r"Which sequence correctly shows the path of blood from the vena cava to the aorta?",
    [r"right atrium → right ventricle → pulmonary vein → lungs → pulmonary artery → left atrium → left ventricle",
     r"left atrium → left ventricle → pulmonary artery → lungs → pulmonary vein → right atrium → right ventricle",
     r"right atrium → right ventricle → pulmonary artery → lungs → pulmonary vein → left atrium → left ventricle",
     r"right ventricle → right atrium → pulmonary artery → lungs → pulmonary vein → left ventricle → left atrium",
     r"right atrium → left atrium → lungs → right ventricle → left ventricle"], "C",
    r"Deoxygenated blood enters the right atrium, then the right ventricle pumps it through the pulmonary artery to the lungs. It returns via the pulmonary vein to the left atrium, and the left ventricle pumps it into the aorta. Arteries carry blood away from the heart.")

add("B-05", "bio", 1, "Osmosis",
    r"A plant cell is placed in a concentrated sucrose solution. Which describes what happens?",
    [r"Water enters the cell by osmosis and the cell becomes turgid", r"Sucrose enters the cell by osmosis and the cell bursts", r"Water leaves the cell by osmosis and the cell becomes plasmolysed", r"Water leaves the cell by active transport and the cell wall shrinks away from the membrane", r"No net movement of water occurs because the cell wall prevents it"], "C",
    r"The solution has a lower water potential than the cell, so water moves out by osmosis (passive). The cytoplasm and membrane pull away from the cell wall: plasmolysis. Osmosis concerns water, not solute.")

add("B-06", "bio", 1, "Photosynthesis",
    r"A plant is kept at \(25^\circ\text{C}\) in bright light. Increasing light intensity further has no effect on the rate of photosynthesis, but increasing carbon dioxide concentration does increase the rate. Which statement is correct?",
    [r"Light intensity is the limiting factor", r"Carbon dioxide concentration is the limiting factor", r"Temperature is the limiting factor", r"Chlorophyll concentration is the limiting factor", r"No factor is limiting"], "B",
    r"The limiting factor is the one which, when increased, increases the rate. Only \(\text{CO}_2\) does so here.")

add("B-07", "bio", 1, "Hormones: blood glucose",
    r"Which statement about insulin is correct?",
    [r"It is produced by the liver and raises blood glucose", r"It is produced by the pancreas and causes the liver to convert glycogen to glucose", r"It is produced by the pancreas and causes the liver to convert glucose to glycogen", r"It is produced by the adrenal glands and lowers blood glucose", r"It is an enzyme that digests glucose in the blood"], "C",
    r"Insulin is released by the pancreas when blood glucose is high. It increases glucose uptake by cells and causes the liver (and muscle) to store glucose as glycogen. Glucagon does the reverse.")

add("B-08", "bio", 1, "Ecology: energy transfer",
    r"In a food chain, 10% of the energy at each trophic level is transferred to the next. Producers capture 20 000 kJ. How much energy reaches the tertiary consumers?",
    [r"\(2\text{ kJ}\)", r"\(20\text{ kJ}\)", r"\(200\text{ kJ}\)", r"\(2000\text{ kJ}\)", r"\(60\text{ kJ}\)"], "B",
    r"Producers \(\to\) primary (2000) \(\to\) secondary (200) \(\to\) tertiary (20 kJ). Three transfers, each \(\times 0.1\).")

add("B-09", "bio", 1, "Genetics: sex linkage",
    r"Red-green colour blindness is caused by a recessive allele on the X chromosome. A woman who is a carrier has children with a man who is not colour blind. What is the probability that their next child is a colour-blind boy?",
    [r"\(0\)", r"\(\dfrac{1}{8}\)", r"\(\dfrac{1}{4}\)", r"\(\dfrac{1}{2}\)", r"\(\dfrac{3}{4}\)"], "C",
    r"\(X^BX^b \times X^BY\): children \(X^BX^B, X^BX^b, X^BY, X^bY\), equally likely. Only \(X^bY\) is a colour-blind boy: \(\tfrac14\). (1/2 is the probability for a son, given it is a boy.)")

add("B-10", "bio", 1, "DNA structure",
    r"In a sample of double-stranded DNA, 30% of the bases are adenine. What percentage are guanine?",
    [r"\(20\%\)", r"\(30\%\)", r"\(40\%\)", r"\(60\%\)", r"\(70\%\)"], "A",
    r"A pairs with T, so T = 30% and A + T = 60%. G + C = 40%, and G = C, so G = 20%.")


exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions_esat.py')).read())


def main():
    for q in Q:   # statement-combination lists keep their natural order in the app
        if q["options"][0] == "none of them": q["fixed"] = True
    ids = [q["id"] for q in Q]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for q in Q:
        assert 0 <= q["answer"] < len(q["options"]), q["id"]
        assert len(set(q["options"])) == len(q["options"]), "duplicate option " + q["id"]
    sys.path.insert(0, os.path.dirname(__file__))
    import verify
    verify.run(Q)
    out = os.path.join(os.path.dirname(__file__), "..", "questions.js")
    with open(out, "w") as f:
        f.write("// Generated by tools/questions.py. Edit there, not here.\n")
        f.write("window.QUESTIONS = " + json.dumps(Q, ensure_ascii=False, indent=1) + ";\n")
    from collections import Counter
    print(len(Q), "questions;", dict(Counter((q["module"], q["level"], q["set"]) for q in Q)))
    print("answer letters:", dict(Counter("ABCDEFGH"[q["answer"]] for q in Q)))

if __name__ == "__main__":
    main()
