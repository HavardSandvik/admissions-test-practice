# ESAT-level sets. Loaded by questions.py (shares add() and Q).
# Pitched at NSAA/ENGAA Section 1 standard: multi-step, combined topics,
# symbolic answers, statement combinations and data, 5–8 options.
LEVEL = "esat"

STMT8 = ["none of them", "1 only", "2 only", "3 only", "1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"]

# ---------------------------------------------------------------- Maths 1, ESAT level 1
add("M1E-01", "m1", 1, "Number: indices and surds",
    r"Which of the following statements is/are correct?<br>1. \((\sqrt{2} + \sqrt{8})^2 = 18\)<br>2. \(8^{2/3} \times 4^{-1/2} = 4\)<br>3. \(3^{20} + 3^{20} + 3^{20} = 3^{21}\)",
    STMT8, "F",
    r"1: \(\sqrt{8} = 2\sqrt{2}\), so the sum is \(3\sqrt{2}\) and its square is 18. True. 2: \(8^{2/3} = 4\) and \(4^{-1/2} = \tfrac12\), so the product is 2. False. 3: \(3 \times 3^{20} = 3^{21}\). True.")

add("M1E-02", "m1", 1, "Mensuration: surface area",
    r"A cube of edge \(a\) has the same total surface area as a sphere of radius \(r\). Which expression gives \(a\) in terms of \(r\)?",
    [r"\(r\sqrt{\dfrac{2\pi}{3}}\)", r"\(r\sqrt{\dfrac{3\pi}{2}}\)", r"\(\dfrac{2\pi r}{3}\)", r"\(r\sqrt{\dfrac{\pi}{6}}\)",
     r"\(\dfrac{r\sqrt{2\pi}}{3}\)", r"\(r\sqrt{6\pi}\)", r"\(\dfrac{2\pi r^2}{3}\)"], "A",
    r"\(6a^2 = 4\pi r^2 \Rightarrow a^2 = \tfrac{2\pi}{3}r^2 \Rightarrow a = r\sqrt{\tfrac{2\pi}{3}}\). Forgetting the square root gives \(\tfrac{2\pi r^2}{3}\); swapping the 4 and 6 gives \(r\sqrt{\tfrac{3\pi}{2}}\).")

add("M1E-03", "m1", 1, "Geometry: area with ratios",
    r"Square \(ABCD\) has side 12 cm, labelled anticlockwise. \(P\) lies on \(AB\) with \(AP : PB = 1 : 2\). \(Q\) is the midpoint of \(BC\). \(R\) lies on \(CD\) with \(CR : RD = 1 : 3\). What is the area of triangle \(PQR\), in \(\text{cm}^2\)?",
    [r"\(24\)", r"\(30\)", r"\(33\)", r"\(36\)", r"\(39\)", r"\(42\)", r"\(48\)"], "C",
    r"Subtract the three corner triangles from the square. Lengths: \(AP = 4, PB = 8\); \(BQ = QC = 6\); \(CR = 3, RD = 9\). Corner triangles: at \(B\): \(\tfrac12 \cdot 8 \cdot 6 = 24\); at \(C\): \(\tfrac12 \cdot 6 \cdot 3 = 9\); the trapezium \(APRD\) has parallel sides \(AP = 4\) and \(DR = 9\), height 12, area \(78\). So \(PQR = 144 - 24 - 9 - 78 = 33\).")

add("M1E-04", "m1", 1, "Speed, distance, time",
    r"A cyclist rides up a hill at \(12\text{ km/h}\) and returns down the same route at \(v\text{ km/h}\). Her average speed for the round trip is \(18\text{ km/h}\). What is \(v\)?",
    [r"\(20\)", r"\(24\)", r"\(27\)", r"\(30\)", r"\(36\)", r"\(48\)"], "E",
    r"Let each leg be \(d\). Total time \(= \tfrac{d}{12} + \tfrac{d}{v} = \tfrac{2d}{18}\), so \(\tfrac{1}{v} = \tfrac19 - \tfrac1{12} = \tfrac{1}{36}\) and \(v = 36\). (24 is the 'simple mean' trap.)")

add("M1E-05", "m1", 1, "Probability: conditional",
    r"Bag A contains 3 red and 2 blue counters. Bag B contains 3 red and \(x\) blue counters. One counter is chosen at random from A and put into B. A counter is then chosen at random from B. The probability that this counter is blue is \(\tfrac35\).<br>Given that the counter chosen from B is blue, what is the probability that the counter moved from A was red?",
    [r"\(\dfrac13\)", r"\(\dfrac25\)", r"\(\dfrac{5}{12}\)", r"\(\dfrac49\)", r"\(\dfrac12\)", r"\(\dfrac59\)", r"\(\dfrac35\)", r"\(\dfrac23\)"], "F",
    r"After the move B has \(x + 4\) counters. \(P(\text{blue}) = \tfrac35 \cdot \tfrac{x}{x+4} + \tfrac25 \cdot \tfrac{x+1}{x+4} = \tfrac{5x+2}{5(x+4)} = \tfrac35 \Rightarrow 5x + 2 = 3x + 12 \Rightarrow x = 5\). Then \(P(\text{red moved and blue}) = \tfrac35 \cdot \tfrac59 = \tfrac13\), so the answer is \(\tfrac13 \div \tfrac35 = \tfrac59\).")

add("M1E-06", "m1", 1, "Algebra: algebraic fractions",
    r"Simplify fully \(\dfrac{x^2 - 9}{x^2 + x - 6} \div \dfrac{x^2 - 2x - 3}{x^2 - 4}\).",
    [r"\(\dfrac{x+2}{x+1}\)", r"\(\dfrac{x-2}{x+1}\)", r"\(\dfrac{x+2}{x-1}\)", r"\(\dfrac{x+3}{x+1}\)", r"\(1\)",
     r"\(\dfrac{x+1}{x+2}\)", r"\(\dfrac{(x+2)(x-3)}{(x+1)(x-2)}\)"], "A",
    r"\(\dfrac{(x-3)(x+3)}{(x+3)(x-2)} \times \dfrac{(x-2)(x+2)}{(x-3)(x+1)} = \dfrac{x+2}{x+1}\). Remember to invert the second fraction.")

add("M1E-07", "m1", 1, "Sequences",
    r"The \(n\)th term of a sequence is \(an^2 + bn\), where \(a\) and \(b\) are constants. The 3rd term is 21 and the 5th term is 55. What is the 10th term?",
    [r"\(110\)", r"\(190\)", r"\(200\)", r"\(210\)", r"\(220\)", r"\(230\)"], "D",
    r"\(9a + 3b = 21\) and \(25a + 5b = 55\), i.e. \(3a + b = 7\) and \(5a + b = 11\). So \(a = 2\), \(b = 1\), and the 10th term is \(200 + 10 = 210\).")

add("M1E-08", "m1", 1, "Mensuration: volume and percentages",
    r"A solid metal cylinder is melted down and recast into a cylinder whose radius is 25% larger. No metal is lost. By what percentage does the height decrease?",
    [r"\(20\%\)", r"\(25\%\)", r"\(36\%\)", r"\(44\%\)", r"\(50\%\)", r"\(56.25\%\)", r"\(64\%\)"], "C",
    r"Volume \(\propto r^2h\). \(r \to 1.25r\) multiplies \(r^2\) by \(\tfrac{25}{16}\), so \(h\) is multiplied by \(\tfrac{16}{25} = 0.64\): a 36% decrease. (64% is the new height, not the decrease.)")

add("M1E-09", "m1", 1, "Averages",
    r"The mean of 20 numbers is 15. Two of the numbers, \(x\) and \(2x\), are removed, and the mean of the remaining numbers is 14. What is \(x\)?",
    [r"\(8\)", r"\(12\)", r"\(16\)", r"\(18\)", r"\(24\)", r"\(32\)"], "C",
    r"Original total \(= 300\). 18 numbers remain with total \(18 \times 14 = 252\). So \(3x = 48\) and \(x = 16\). (Dividing by 19 or using 20 for the remaining count are the common slips.)")

add("M1E-10", "m1", 1, "Trigonometry: area and cosine rule",
    r"In triangle \(ABC\), \(AB = 6\), \(AC = 4\) and angle \(BAC = 60^\circ\). What is the perpendicular distance from \(A\) to the line \(BC\)?",
    [r"\(\dfrac{6\sqrt{21}}{7}\)", r"\(\dfrac{3\sqrt{21}}{7}\)", r"\(2\sqrt{7}\)", r"\(3\sqrt{3}\)", r"\(\dfrac{6\sqrt{3}}{7}\)", r"\(\sqrt{21}\)", r"\(\dfrac{12\sqrt{3}}{7}\)"], "A",
    r"\(BC^2 = 36 + 16 - 2 \cdot 6 \cdot 4 \cdot \tfrac12 = 28\), so \(BC = 2\sqrt{7}\). Area \(= \tfrac12 \cdot 6 \cdot 4 \sin 60^\circ = 6\sqrt{3}\). Also area \(= \tfrac12 \cdot BC \cdot h\), so \(h = \dfrac{12\sqrt{3}}{2\sqrt{7}} = \dfrac{6\sqrt{3}}{\sqrt{7}} = \dfrac{6\sqrt{21}}{7}\).")

# ---------------------------------------------------------------- Maths 2, ESAT level 1
add("M2E-01", "m2", 1, "Quadratics: discriminant and tangency",
    r"The line \(y = kx\) is a tangent to the curve \(y = x^2 - 2x + 4\). What are all the possible values of \(k\)?",
    [r"\(2\) only", r"\(-6\) only", r"\(2\) and \(-6\)", r"\(-2\) and \(6\)", r"\(4\) and \(-4\)", r"\(6\) only", r"\(2\) and \(6\)"], "C",
    r"\(x^2 - (2 + k)x + 4 = 0\) must have a repeated root: \((2 + k)^2 = 16 \Rightarrow 2 + k = \pm 4 \Rightarrow k = 2\) or \(k = -6\).")

add("M2E-02", "m2", 1, "Exponentials: hidden quadratics",
    r"What is the sum of the real solutions of \(9^x - 4 \cdot 3^{x+1} + 27 = 0\)?",
    [r"\(0\)", r"\(1\)", r"\(2\)", r"\(3\)", r"\(4\)", r"\(12\)"], "D",
    r"Let \(t = 3^x\): \(t^2 - 12t + 27 = 0 \Rightarrow t = 3\) or \(9\), so \(x = 1\) or \(2\). Sum \(= 3\). (12 is the sum of the \(t\) values.)")

add("M2E-03", "m2", 1, "Trigonometric equations",
    r"What is the sum of all the solutions of \(2\cos^2 x + 3\sin x = 3\) in the interval \(0 \le x \le 2\pi\)?",
    [r"\(\dfrac{\pi}{2}\)", r"\(\pi\)", r"\(\dfrac{7\pi}{6}\)", r"\(\dfrac{3\pi}{2}\)", r"\(2\pi\)", r"\(\dfrac{5\pi}{2}\)", r"\(3\pi\)"], "D",
    r"Use \(\cos^2 x = 1 - \sin^2 x\): \(2\sin^2 x - 3\sin x + 1 = 0 \Rightarrow \sin x = 1\) or \(\tfrac12\). Solutions \(\tfrac{\pi}{2}, \tfrac{\pi}{6}, \tfrac{5\pi}{6}\), with sum \(\tfrac{3\pi}{2}\).")

add("M2E-04", "m2", 1, "Differentiation: optimisation",
    r"A closed cylinder has volume \(16\pi\text{ cm}^3\). What is the smallest possible total surface area, in \(\text{cm}^2\)?",
    [r"\(12\pi\)", r"\(16\pi\)", r"\(20\pi\)", r"\(24\pi\)", r"\(28\pi\)", r"\(32\pi\)", r"\(48\pi\)"], "D",
    r"\(h = \tfrac{16}{r^2}\), so \(S = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \tfrac{32\pi}{r}\). \(S' = 4\pi r - \tfrac{32\pi}{r^2} = 0 \Rightarrow r^3 = 8 \Rightarrow r = 2\), \(h = 4\). \(S = 8\pi + 16\pi = 24\pi\).")

add("M2E-05", "m2", 1, "Integration: area below the axis",
    r"What is the total area of the regions enclosed by the curve \(y = x^2 - 4x + 3\), the \(x\)-axis and the lines \(x = 0\) and \(x = 3\)?",
    [r"\(0\)", r"\(\dfrac43\)", r"\(2\)", r"\(\dfrac83\)", r"\(\dfrac{10}{3}\)", r"\(4\)", r"\(\dfrac{16}{3}\)"], "D",
    r"The curve crosses the axis at \(x = 1\) and \(x = 3\). With \(F(x) = \tfrac{x^3}{3} - 2x^2 + 3x\): \(\int_0^1 = \tfrac43\) (above), \(\int_1^3 = 0 - \tfrac43 = -\tfrac43\) (below). Total area \(= \tfrac43 + \tfrac43 = \tfrac83\). Integrating straight from 0 to 3 gives 0: the trap.")

add("M2E-06", "m2", 1, "Logarithms",
    r"Given that \(\log_a b = 3\), what is \(\log_b (a^2 b)\)?",
    [r"\(\dfrac23\)", r"\(\dfrac35\)", r"\(\dfrac53\)", r"\(\dfrac73\)", r"\(6\)", r"\(7\)", r"\(9\)"], "C",
    r"\(b = a^3\), so \(a = b^{1/3}\) and \(a^2 b = b^{2/3} \cdot b = b^{5/3}\). Hence \(\log_b(a^2b) = \tfrac53\). (7 is \(\log_a(a^2b)\).)")

add("M2E-07", "m2", 1, "Arithmetic series",
    r"An arithmetic series has sum of its first 10 terms equal to 145 and sum of its first 20 terms equal to 590. What is the sum of the 21st to 30th terms inclusive?",
    [r"\(445\)", r"\(590\)", r"\(735\)", r"\(745\)", r"\(755\)", r"\(845\)", r"\(1335\)"], "D",
    r"\(5(2a + 9d) = 145\) and \(10(2a + 19d) = 590\) give \(2a + 9d = 29\), \(2a + 19d = 59\), so \(d = 3\), \(a = 1\). \(S_{30} = 15(2 + 87) = 1335\), and \(1335 - 590 = 745\).")

add("M2E-08", "m2", 1, "Graph transformations",
    r"The curve \(y = f(x)\) has a single stationary point, a maximum at \((2, 5)\). Which describes the stationary point of \(y = 3 - 2f(x + 1)\)?",
    [r"maximum at \((1, -7)\)", r"minimum at \((1, -7)\)", r"minimum at \((3, -7)\)", r"maximum at \((3, 13)\)", r"minimum at \((1, 13)\)", r"maximum at \((1, 13)\)", r"minimum at \((-1, -7)\)", r"maximum at \((-1, -7)\)"], "B",
    r"\(f(x+1)\) shifts left by 1: maximum at \((1, 5)\). Multiplying by \(-2\) stretches and reflects it: minimum at \((1, -10)\). Adding 3: minimum at \((1, -7)\).")

add("M2E-09", "m2", 1, "Binomial expansion",
    r"What is the coefficient of \(x^2\) in the expansion of \((1 + 2x)^5(1 - x)^3\)?",
    [r"\(-13\)", r"\(3\)", r"\(7\)", r"\(13\)", r"\(37\)", r"\(43\)", r"\(73\)"], "D",
    r"\((1 + 2x)^5 = 1 + 10x + 40x^2 + \dots\) and \((1 - x)^3 = 1 - 3x + 3x^2 - x^3\). The \(x^2\) coefficient is \(40 \cdot 1 + 10 \cdot (-3) + 1 \cdot 3 = 13\).")

add("M2E-10", "m2", 1, "Circles: chords",
    r"The line \(y = x + 1\) cuts the circle \((x - 2)^2 + (y - 1)^2 = 10\) at two points. What is the length of the chord joining them?",
    [r"\(\sqrt{2}\)", r"\(2\sqrt{2}\)", r"\(4\)", r"\(4\sqrt{2}\)", r"\(2\sqrt{5}\)", r"\(2\sqrt{10}\)", r"\(8\)"], "D",
    r"Distance from centre \((2, 1)\) to \(x - y + 1 = 0\) is \(\tfrac{|2 - 1 + 1|}{\sqrt{2}} = \sqrt{2}\). Half-chord \(= \sqrt{10 - 2} = 2\sqrt{2}\), so the chord is \(4\sqrt{2}\). (Or solve: the points are \((-1, 0)\) and \((3, 4)\).)")

# ---------------------------------------------------------------- Physics, ESAT level 1
add("PE-01", "phys", 1, "Energy: springs and gravity",
    r"A spring of stiffness \(k\) is compressed by a distance \(x\) and used to launch a ball of mass \(m\) vertically upwards. Assume all the elastic energy becomes kinetic energy of the ball, and ignore air resistance and the height gained while the spring extends. How high does the ball rise above its launch point?",
    [r"\(\dfrac{kx^2}{2mg}\)", r"\(\dfrac{kx}{mg}\)", r"\(\dfrac{kx^2}{mg}\)", r"\(\dfrac{2kx^2}{mg}\)", r"\(\dfrac{kx^2}{2m}\)", r"\(\sqrt{\dfrac{kx^2}{2mg}}\)", r"\(\dfrac{mg}{kx^2}\)"], "A",
    r"\(\tfrac12 kx^2 = mgh \Rightarrow h = \dfrac{kx^2}{2mg}\). Check units: \(\text{N m}^{-1} \times \text{m}^2 / \text{N} = \text{m}\).")

add("PE-02", "phys", 1, "Circuits: switches and power",
    r"A 12 V battery of negligible internal resistance is connected in series with a \(4\,\Omega\) resistor and a \(6\,\Omega\) resistor. A \(3\,\Omega\) resistor in series with a switch is connected in parallel with the \(6\,\Omega\) resistor. The switch is initially open. By what factor does the power supplied by the battery change when the switch is closed?",
    [r"\(\dfrac35\)", r"\(1\)", r"\(\dfrac32\)", r"\(\dfrac53\)", r"\(2\)", r"\(\dfrac52\)", r"\(\dfrac{10}{3}\)"], "D",
    r"Open: \(R = 10\,\Omega\), \(P = V^2/R = 14.4\) W. Closed: \(6 \parallel 3 = 2\,\Omega\), \(R = 6\,\Omega\), \(P = 24\) W. Factor \(= \tfrac{10}{6} = \tfrac53\). (With fixed \(V\), \(P \propto 1/R\).)")

add("PE-03", "phys", 1, "Energy: projectiles",
    r"A stone is thrown with speed \(u\) at an angle \(\theta\) above the horizontal from the top of a cliff of height \(H\). Ignoring air resistance, with what speed does it hit the ground below?",
    [r"\(\sqrt{u^2 + 2gH}\)", r"\(u + \sqrt{2gH}\)", r"\(\sqrt{u^2\cos^2\theta + 2gH}\)", r"\(\sqrt{u^2\sin^2\theta + 2gH}\)", r"\(\sqrt{2gH}\)", r"\(\sqrt{u^2 - 2gH}\)", r"\(u^2 + 2gH\)"], "A",
    r"Energy conservation: \(\tfrac12 mv^2 = \tfrac12 mu^2 + mgH\), so \(v = \sqrt{u^2 + 2gH}\), independent of \(\theta\). (The options with \(\theta\) use only one velocity component, but kinetic energy depends on the full speed.)")

add("PE-04", "phys", 1, "Radioactivity: two isotopes",
    r"A sample contains two radioactive isotopes, P (half-life 2 hours) and Q (half-life 6 hours). Initially there are 8 times as many P nuclei as Q nuclei. After how long are there equal numbers of P and Q nuclei?",
    [r"3 hours", r"6 hours", r"8 hours", r"9 hours", r"12 hours", r"18 hours", r"They never become equal"], "D",
    r"\(8 \cdot 2^{-t/2} = 2^{-t/6} \Rightarrow 3 - \tfrac{t}{2} = -\tfrac{t}{6} \Rightarrow \tfrac{t}{3} = 3 \Rightarrow t = 9\) h. Check: after 9 h P has fallen by \(2^{4.5}\), Q by \(2^{1.5}\), a relative change of \(2^3 = 8\).")

add("PE-05", "phys", 1, "Momentum and energy: ballistic pendulum",
    r"A bullet of mass \(m\) travelling horizontally at speed \(u\) embeds itself in a block of mass \(M\) hanging at rest from a long string. To what maximum height above its starting position does the block rise?",
    [r"\(\dfrac{m^2u^2}{2g(m+M)^2}\)", r"\(\dfrac{mu^2}{2gM}\)", r"\(\dfrac{u^2}{2g}\)", r"\(\dfrac{m^2u^2}{2gM^2}\)", r"\(\dfrac{mu^2}{2g(m+M)}\)", r"\(\dfrac{m^2u^2}{g(m+M)^2}\)", r"\(\dfrac{(m+M)u^2}{2gm}\)"], "A",
    r"Momentum (not energy) is conserved in the collision: \(v = \tfrac{mu}{m+M}\). Then energy is conserved during the swing: \(h = \tfrac{v^2}{2g} = \dfrac{m^2u^2}{2g(m+M)^2}\). Using energy conservation across the collision gives \(\tfrac{mu^2}{2g(m+M)}\): wrong, as the collision is inelastic.")

add("PE-06", "phys", 1, "Waves: refraction",
    r"Light of wavelength 600 nm in air enters glass of refractive index 1.5. The speed of light in air is \(3.0 \times 10^8\text{ m s}^{-1}\). Which of the following statements is/are correct?<br>1. The frequency of the light in the glass is \(\tfrac23\) of its frequency in air.<br>2. The wavelength of the light in the glass is 400 nm.<br>3. The speed of the light in the glass is \(2.0 \times 10^8\text{ m s}^{-1}\).",
    STMT8, "G",
    r"Frequency is set by the source and does not change, so 1 is false. \(v = c/n = 2.0 \times 10^8\text{ m s}^{-1}\) (3 true), and \(\lambda = v/f\) falls by the same factor: \(600/1.5 = 400\) nm (2 true).")

add("PE-07", "phys", 1, "Electricity: resistivity and power",
    r"Wires X and Y are made of the same metal. Y is twice as long as X and has twice the diameter. They are connected in parallel across the same supply. What is \(\dfrac{\text{power dissipated in Y}}{\text{power dissipated in X}}\)?",
    [r"\(\dfrac18\)", r"\(\dfrac14\)", r"\(\dfrac12\)", r"\(1\)", r"\(2\)", r"\(4\)", r"\(8\)"], "E",
    r"\(R = \rho L/A\), and doubling the diameter quadruples \(A\): \(R_Y = \tfrac{2}{4}R_X = \tfrac12 R_X\). In parallel \(V\) is the same, so \(P = V^2/R\) and \(P_Y/P_X = 2\). (In series the answer would be \(\tfrac12\).)")

add("PE-08", "phys", 1, "Thermal physics: latent heat",
    r"A 200 W heater is used to turn 0.20 kg of ice at \(-10^\circ\text{C}\) into water at \(20^\circ\text{C}\). Specific heat capacity of ice \(= 2000\text{ J kg}^{-1}\text{K}^{-1}\); of water \(= 4200\text{ J kg}^{-1}\text{K}^{-1}\); specific latent heat of fusion of ice \(= 3.3 \times 10^5\text{ J kg}^{-1}\). Assuming no energy losses, how long does this take?",
    [r"\(104\text{ s}\)", r"\(330\text{ s}\)", r"\(350\text{ s}\)", r"\(414\text{ s}\)", r"\(434\text{ s}\)", r"\(454\text{ s}\)"], "E",
    r"Warm ice: \(0.2 \times 2000 \times 10 = 4000\) J. Melt: \(0.2 \times 3.3 \times 10^5 = 66\,000\) J. Warm water: \(0.2 \times 4200 \times 20 = 16\,800\) J. Total \(86\,800\) J, and \(86\,800 / 200 = 434\) s. The distractors each leave out one stage.")

add("PE-09", "phys", 1, "Moments",
    r"A uniform beam of weight \(W\) and length \(L\) rests horizontally on two supports, one at each end. A load of weight \(2W\) is placed a distance \(\tfrac{L}{4}\) from the left-hand end. What is the ratio (force from left support) : (force from right support)?",
    [r"\(1 : 1\)", r"\(1 : 2\)", r"\(3 : 2\)", r"\(5 : 3\)", r"\(2 : 1\)", r"\(7 : 5\)", r"\(3 : 1\)"], "E",
    r"Moments about the right support: \(F_L \cdot L = W \cdot \tfrac{L}{2} + 2W \cdot \tfrac{3L}{4} = 2WL\), so \(F_L = 2W\). Total upward force \(= 3W\), so \(F_R = W\). Ratio \(2 : 1\).")

add("PE-10", "phys", 1, "Electricity: power transmission",
    r"10 kW of electrical power is transmitted to a village through cables of total resistance \(4.0\,\Omega\). What percentage of the transmitted power is lost as heat in the cables if the transmission voltage is (i) 1.0 kV and (ii) 10 kV?",
    [r"(i) 4%, (ii) 0.4%", r"(i) 4%, (ii) 0.04%", r"(i) 0.4%, (ii) 0.04%", r"(i) 40%, (ii) 4%", r"(i) 4%, (ii) 4%", r"(i) 0.04%, (ii) 4%"], "B",
    r"\(I = P/V\): 10 A at 1 kV, 1 A at 10 kV. Loss \(= I^2R\): 400 W (4%) and 4 W (0.04%). Raising \(V\) by 10 cuts the loss by \(10^2\).")

# ---------------------------------------------------------------- Chemistry, ESAT level 1
add("CE-01", "chem", 1, "Moles: ions in solution",
    r"How many moles of ions in total are present in \(250\text{ cm}^3\) of \(0.40\text{ mol dm}^{-3}\) aluminium sulfate solution, \(\text{Al}_2(\text{SO}_4)_3(\text{aq})\)? Assume it is fully dissociated.",
    [r"\(0.10\)", r"\(0.20\)", r"\(0.30\)", r"\(0.40\)", r"\(0.50\)", r"\(0.70\)", r"\(2.0\)"], "E",
    r"\(n = 0.40 \times 0.250 = 0.10\) mol of \(\text{Al}_2(\text{SO}_4)_3\). Each formula unit gives \(2\text{Al}^{3+} + 3\text{SO}_4^{2-}\), i.e. 5 ions, so \(0.50\) mol of ions.")

add("CE-02", "chem", 1, "Moles: percentage purity",
    r"An iron ore contains 80% iron(III) oxide, \(\text{Fe}_2\text{O}_3\), by mass. What is the minimum mass of ore needed to produce 5.6 tonnes of iron? (\(A_r\): Fe = 56, O = 16)",
    [r"\(6.4\) t", r"\(7.0\) t", r"\(8.0\) t", r"\(10\) t", r"\(12.5\) t", r"\(16\) t", r"\(20\) t"], "D",
    r"5.6 t Fe \(= 5.6 \times 10^6 / 56 = 1.0 \times 10^5\) mol, needing \(5.0 \times 10^4\) mol \(\text{Fe}_2\text{O}_3\) (\(M_r = 160\)), i.e. \(8.0 \times 10^6\) g \(= 8.0\) t. As the ore is 80% oxide: \(8.0 / 0.80 = 10\) t. (20 t forgets the 2 Fe per formula; 6.4 t multiplies by 0.8 instead of dividing.)")

add("CE-03", "chem", 1, "Redox titrations",
    r"In acid solution, manganate(VII) ions oxidise iron(II) ions:<br>\(\text{MnO}_4^- + 8\text{H}^+ + 5\text{Fe}^{2+} \rightarrow \text{Mn}^{2+} + 5\text{Fe}^{3+} + 4\text{H}_2\text{O}\)<br>What volume of \(0.020\text{ mol dm}^{-3}\) potassium manganate(VII) reacts exactly with \(25.0\text{ cm}^3\) of \(0.10\text{ mol dm}^{-3}\) iron(II) sulfate?",
    [r"\(5.0\text{ cm}^3\)", r"\(12.5\text{ cm}^3\)", r"\(25.0\text{ cm}^3\)", r"\(50.0\text{ cm}^3\)", r"\(62.5\text{ cm}^3\)", r"\(125\text{ cm}^3\)"], "C",
    r"\(n(\text{Fe}^{2+}) = 0.10 \times 0.0250 = 2.5 \times 10^{-3}\) mol, so \(n(\text{MnO}_4^-) = 5.0 \times 10^{-4}\) mol. \(V = 5.0 \times 10^{-4} / 0.020 = 0.025\text{ dm}^3 = 25.0\text{ cm}^3\). (125 cm³ ignores the 1 : 5 ratio.)")

add("CE-04", "chem", 1, "Acids: strong and weak",
    r"Equal volumes of \(0.10\text{ mol dm}^{-3}\) hydrochloric acid and \(0.10\text{ mol dm}^{-3}\) ethanoic acid are each added to an excess of magnesium ribbon. Which of the following statements is/are correct?<br>1. The same total volume of hydrogen is eventually produced in each case.<br>2. The initial rate of reaction is the same in each case.<br>3. The hydrochloric acid has the lower pH.",
    STMT8, "F",
    r"Both contain 0.10 mol dm⁻³ of acid that can eventually react, so the same amount of \(\text{H}_2\) forms (1 true). Ethanoic acid is weak, so \([\text{H}^+]\) is much lower: slower initial rate (2 false) and higher pH (3 true).")

add("CE-05", "chem", 1, "Organic: structural isomers",
    r"How many structural isomers have the molecular formula \(\text{C}_4\text{H}_9\text{Br}\)?",
    [r"\(2\)", r"\(3\)", r"\(4\)", r"\(5\)", r"\(6\)"], "C",
    r"Straight chain: 1-bromobutane, 2-bromobutane. Branched chain: 1-bromo-2-methylpropane, 2-bromo-2-methylpropane. Total 4. (2-bromobutane also has two optical isomers, but these are stereoisomers, not structural isomers.)")

add("CE-06", "chem", 1, "Energetics: bond enthalpies",
    r"Bond enthalpies (\(\text{kJ mol}^{-1}\)): H–H 436, Cl–Cl 242, H–Cl 431.<br>What is the enthalpy change for the formation of <b>one mole</b> of hydrogen chloride from hydrogen and chlorine?",
    [r"\(-431\text{ kJ}\)", r"\(-247\text{ kJ}\)", r"\(-184\text{ kJ}\)", r"\(-92\text{ kJ}\)", r"\(+92\text{ kJ}\)", r"\(+184\text{ kJ}\)", r"\(+247\text{ kJ}\)"], "D",
    r"\(\text{H}_2 + \text{Cl}_2 \rightarrow 2\text{HCl}\): bonds broken \(436 + 242 = 678\), bonds made \(2 \times 431 = 862\), \(\Delta H = 678 - 862 = -184\) kJ for 2 mol. Per mole of HCl: \(-92\) kJ.")

add("CE-07", "chem", 1, "Rates and equilibrium",
    r"\(2\text{SO}_2(\text{g}) + \text{O}_2(\text{g}) \rightleftharpoons 2\text{SO}_3(\text{g})\), \(\Delta H < 0\).<br>The temperature of the equilibrium mixture is raised at constant pressure. What happens to the rate of the forward reaction and to the equilibrium yield of \(\text{SO}_3\)?",
    [r"rate increases; yield increases", r"rate increases; yield decreases", r"rate increases; yield unchanged", r"rate decreases; yield increases", r"rate decreases; yield decreases", r"rate unchanged; yield decreases"], "B",
    r"Higher temperature always increases rate (more collisions exceed the activation energy). The forward reaction is exothermic, so the equilibrium shifts left and the yield of \(\text{SO}_3\) falls.")

add("CE-08", "chem", 1, "Atomic structure: ionic radii",
    r"Which of the following ions has the same electron configuration as an argon atom <b>and</b> the smallest radius?",
    [r"\(\text{S}^{2-}\)", r"\(\text{Cl}^-\)", r"\(\text{K}^+\)", r"\(\text{Ca}^{2+}\)", r"\(\text{Na}^+\)", r"\(\text{Mg}^{2+}\)"], "D",
    r"\(\text{S}^{2-}, \text{Cl}^-, \text{K}^+, \text{Ca}^{2+}\) all have 18 electrons (Ar configuration). With the same electrons, more protons pull them in more tightly, so \(\text{Ca}^{2+}\) (20 protons) is smallest. \(\text{Na}^+\) and \(\text{Mg}^{2+}\) are smaller still, but have the neon configuration.")

add("CE-09", "chem", 1, "Moles: limiting reagent",
    r"2.4 g of magnesium is added to \(100\text{ cm}^3\) of \(1.0\text{ mol dm}^{-3}\) hydrochloric acid. What volume of hydrogen is produced at room temperature and pressure? (\(A_r\): Mg = 24; 1 mol of gas occupies \(24\text{ dm}^3\) at RTP)",
    [r"\(0.12\text{ dm}^3\)", r"\(0.60\text{ dm}^3\)", r"\(1.2\text{ dm}^3\)", r"\(2.0\text{ dm}^3\)", r"\(2.4\text{ dm}^3\)", r"\(4.8\text{ dm}^3\)"], "C",
    r"\(\text{Mg} + 2\text{HCl} \rightarrow \text{MgCl}_2 + \text{H}_2\). Mg: 0.10 mol; HCl: 0.10 mol, which would need only 0.05 mol Mg, so HCl is limiting. \(\text{H}_2 = 0.050\) mol \(= 1.2\text{ dm}^3\). (2.4 dm³ assumes Mg is limiting.)")

add("CE-10", "chem", 1, "Moles: water of crystallisation",
    r"2.46 g of hydrated magnesium sulfate, \(\text{MgSO}_4 \cdot x\text{H}_2\text{O}\), is heated to constant mass, leaving 1.20 g of anhydrous \(\text{MgSO}_4\). What is \(x\)? (\(M_r\): \(\text{MgSO}_4 = 120\), \(\text{H}_2\text{O} = 18\))",
    [r"\(4\)", r"\(5\)", r"\(6\)", r"\(7\)", r"\(8\)", r"\(10\)"], "D",
    r"Water lost \(= 1.26\) g \(= 0.070\) mol. \(\text{MgSO}_4 = 1.20/120 = 0.010\) mol. \(x = 0.070/0.010 = 7\).")

# ---------------------------------------------------------------- Biology, ESAT level 1
add("BE-01", "bio", 1, "Ecology: relationships",
    r"Cleaner wrasse are small fish that eat parasites living on the skin of larger fish. The larger fish do not eat the wrasse. Which correctly describes (i) the relationship between the wrasse and the larger fish and (ii) the relationship between the wrasse and the parasites?",
    [r"(i) mutualism; (ii) predation", r"(i) parasitism; (ii) mutualism", r"(i) commensalism; (ii) predation", r"(i) mutualism; (ii) parasitism", r"(i) competition; (ii) predation", r"(i) predation; (ii) mutualism"], "A",
    r"Both the wrasse (food) and the larger fish (parasite removal) benefit: mutualism. The wrasse kills and eats the parasites: predation.")

add("BE-02", "bio", 1, "Ecology: energy transfer",
    r"The table shows energy values for grass and rabbits in a field over one year.<table class='data'><tr><th></th><th>Energy / kJ</th></tr><tr><td>Gross primary production of grass</td><td>20 000</td></tr><tr><td>Respiration by grass</td><td>12 000</td></tr><tr><td>Energy in grass eaten by rabbits</td><td>2 000</td></tr><tr><td>Energy in rabbit faeces</td><td>800</td></tr><tr><td>Respiration by rabbits</td><td>1 000</td></tr></table>Which of the following statements is/are correct?<br>1. The net primary production of the grass is 40% of its gross primary production.<br>2. Rabbits eat 25% of the net primary production of the grass.<br>3. 1200 kJ is available for growth of the rabbits.",
    STMT8, "E",
    r"NPP \(= 20\,000 - 12\,000 = 8000\) kJ, which is 40% of GPP (1 true). \(2000 / 8000 = 25\%\) (2 true). Rabbit growth \(=\) eaten \(-\) faeces \(-\) respiration \(= 2000 - 800 - 1000 = 200\) kJ, not 1200 (3 false: 1200 is what's absorbed, before respiration).")

add("BE-03", "bio", 1, "Plant transport: potometer",
    r"A bubble potometer has a capillary tube of internal radius 1.0 mm. The air bubble moves 15 mm in 5.0 minutes. Which row correctly gives what the potometer measures directly and the rate?",
    [r"water uptake; \(3\pi\text{ mm}^3\text{ min}^{-1}\)", r"water uptake; \(15\pi\text{ mm}^3\text{ min}^{-1}\)", r"transpiration; \(6\pi\text{ mm}^3\text{ min}^{-1}\)", r"water uptake; \(6\pi\text{ mm}^3\text{ min}^{-1}\)", r"translocation; \(3\pi\text{ mm}^3\text{ min}^{-1}\)", r"transpiration; \(15\pi\text{ mm}^3\text{ min}^{-1}\)"], "A",
    r"Volume \(= \pi r^2 l = \pi \times 1^2 \times 15 = 15\pi\text{ mm}^3\) in 5 min, i.e. \(3\pi\text{ mm}^3\text{ min}^{-1}\). A potometer measures water uptake by the shoot; this approximates transpiration, but some water is used in photosynthesis or kept by cells. \(15\pi\) forgets to divide by the time; \(6\pi\) uses \(2\pi r l\) instead of \(\pi r^2 l\).")

add("BE-04", "bio", 1, "Genetics: dihybrid crosses",
    r"In a plant, purple flowers (P) are dominant to white (p) and tall stems (T) are dominant to short (t). The two genes are on different chromosomes. A plant of genotype PpTt is crossed with one of genotype Pptt. What fraction of the offspring is expected to have purple flowers and short stems?",
    [r"\(\dfrac{1}{16}\)", r"\(\dfrac{3}{16}\)", r"\(\dfrac14\)", r"\(\dfrac38\)", r"\(\dfrac12\)", r"\(\dfrac{9}{16}\)", r"\(\dfrac34\)"], "D",
    r"Independent genes: \(P(\text{purple}) = \tfrac34\) (Pp × Pp), \(P(\text{short}) = \tfrac12\) (Tt × tt). Product \(= \tfrac38\).")

add("BE-05", "bio", 1, "Genetics: inheritance patterns",
    r"Two parents who do not have a particular genetic condition have a daughter who has it. Which of the following statements is/are correct?<br>1. The condition cannot be caused by an X-linked recessive allele.<br>2. Both parents must be heterozygous for the gene.<br>3. Any son of the affected daughter will also have the condition.",
    STMT8, "E",
    r"An affected child of two unaffected parents means the allele is recessive. If it were X-linked recessive, the daughter would need an affected allele from her father, who would then have the condition. So it is autosomal recessive (1 true), and both parents must be carriers (2 true). Her sons get one allele from her, but their other allele comes from their father, so they need not be affected (3 false).")

add("BE-06", "bio", 1, "Enzymes: rate data",
    r"The table shows the initial rate of an enzyme-catalysed reaction at different substrate concentrations, with enzyme concentration and temperature kept constant.<table class='data'><tr><th>Substrate concentration / arbitrary units</th><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><th>Initial rate / arbitrary units</th><td>2.0</td><td>4.0</td><td>6.0</td><td>7.0</td><td>7.5</td><td>7.5</td></tr></table>Which of the following statements is/are correct?<br>1. At a substrate concentration of 1, substrate concentration limits the rate.<br>2. At a substrate concentration of 6, almost all active sites are occupied at any moment.<br>3. Doubling the enzyme concentration would increase the rate at a substrate concentration of 6.",
    STMT8, "H",
    r"At low concentration the rate rises in proportion to substrate: substrate is limiting (1 true). The plateau means the enzymes are saturated (2 true), so enzyme concentration now limits the rate and adding more enzyme raises it (3 true).")

add("BE-07", "bio", 1, "Respiration: interpreting data",
    r"Yeast was grown in a sealed flask of glucose solution. The table shows measurements over 32 hours (arbitrary units).<table class='data'><tr><th>Time / h</th><td>0</td><td>8</td><td>16</td><td>24</td><td>32</td></tr><tr><th>Oxygen</th><td>20</td><td>10</td><td>2</td><td>0</td><td>0</td></tr><tr><th>Ethanol</th><td>0</td><td>0</td><td>1</td><td>4</td><td>8</td></tr><tr><th>Glucose</th><td>100</td><td>90</td><td>70</td><td>45</td><td>25</td></tr></table>Which of the following statements is/are correct?<br>1. Between 0 and 8 hours the yeast respired aerobically only.<br>2. The rate of glucose use was greatest between 24 and 32 hours.<br>3. Ethanol was produced only once oxygen had run out completely.",
    STMT8, "B",
    r"1: no ethanol forms while oxygen falls, consistent with aerobic respiration only. True. 2: glucose falls by 10, 20, 25 and 20 in successive 8-hour periods, so the rate is greatest from 16 to 24 h. False. 3: ethanol appears by 16 h, when 2 units of oxygen remain. False.")

add("BE-08", "bio", 1, "Circulation: cardiac output",
    r"At rest, an athlete has a heart rate of 56 beats per minute and a cardiac output of \(5.6\text{ dm}^3\text{ min}^{-1}\). During exercise the heart rate rises to 160 beats per minute and the stroke volume increases by 50%. What are the resting stroke volume and the cardiac output during exercise?",
    [r"\(100\text{ cm}^3\); \(16\text{ dm}^3\text{ min}^{-1}\)", r"\(100\text{ cm}^3\); \(24\text{ dm}^3\text{ min}^{-1}\)", r"\(10\text{ cm}^3\); \(2.4\text{ dm}^3\text{ min}^{-1}\)", r"\(150\text{ cm}^3\); \(24\text{ dm}^3\text{ min}^{-1}\)", r"\(100\text{ cm}^3\); \(8.4\text{ dm}^3\text{ min}^{-1}\)", r"\(1.0\text{ dm}^3\); \(240\text{ dm}^3\text{ min}^{-1}\)"], "B",
    r"Stroke volume \(= 5600\text{ cm}^3 / 56 = 100\text{ cm}^3\). During exercise: \(150\text{ cm}^3 \times 160 = 24\,000\text{ cm}^3 = 24\text{ dm}^3\text{ min}^{-1}\). (16 forgets the stroke-volume increase; 8.4 forgets the heart-rate increase.)")

add("BE-09", "bio", 1, "Cells: prokaryotes and eukaryotes",
    r"Which of the following are found in <b>both</b> prokaryotic and eukaryotic cells?<br>1. ribosomes &nbsp; 2. cell membrane &nbsp; 3. nucleus &nbsp; 4. mitochondria &nbsp; 5. DNA",
    [r"1 and 2 only", r"1, 2 and 5 only", r"2 and 5 only", r"1, 2, 4 and 5 only", r"1, 2, 3 and 5 only", r"2, 3 and 5 only", r"all five"], "B",
    r"Prokaryotes have ribosomes (smaller, 70S), a cell membrane and DNA (in a loop, not in a nucleus). They have no nucleus and no membrane-bound organelles such as mitochondria.")

add("BE-10", "bio", 1, "Homeostasis: water balance",
    r"A person drinks a large volume of water. Which row shows the changes that follow?",
    [r"ADH secretion decreases; collecting ducts become less permeable to water; urine volume increases",
     r"ADH secretion increases; collecting ducts become more permeable to water; urine volume decreases",
     r"ADH secretion decreases; collecting ducts become more permeable to water; urine volume increases",
     r"ADH secretion increases; collecting ducts become less permeable to water; urine volume increases",
     r"ADH secretion decreases; collecting ducts become less permeable to water; urine volume decreases",
     r"ADH secretion unchanged; collecting ducts become less permeable to water; urine volume increases"], "A",
    r"Blood water potential rises and the hypothalamus detects this, so the pituitary releases less ADH. Collecting ducts become less permeable, less water is reabsorbed, and a larger volume of dilute urine is produced.")
