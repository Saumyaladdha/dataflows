# NEET (UG) 2025 · Code 47

180 questions · source `NEET_Papers/2025/Set_Code_47/Answers-and-Solutions_NEET-2025_Code-47-PCB.pdf` · every image a CDN link (0 without one) · 1 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Current Electricity

The current passing through the battery in the given circuit, is:

![printed figure: Resistor network ABCDEF with a 5 V battery and series resistors on the outer loop](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q001_77044c03_12112026.png?v=77044c035c03)

*Resistor network ABCDEF with a 5 V battery and series resistors on the outer loop*

- (1) $1.5\,\mathrm{A}$
- (2) $2.0\,\mathrm{A}$
- **(3)** $0.5\,\mathrm{A}$
- (4) $2.5\,\mathrm{A}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\therefore$ its equivalent $R' = \frac{4\times 8}{12} = \frac{8}{3}\,\Omega$
2. Circuit can be redrawn as
3. $R_{\mathrm{eq}} = \frac{8}{3} + \frac{1}{3} + 1.5 + 5.5$
4. $= 10\,\Omega$
5. $i = \frac{V}{R_{\mathrm{eq}}} = \frac{5}{10} = 0.5\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Points $A$ and $F$ are joined by a plain wire, as are $C$ and $D$, so $F \equiv A$ and $C \equiv D$.
2. Between $B$ and $E$: $R_{BA} = 5\,\Omega$, $R_{AE} = 3\,\Omega$, $R_{BD} = 2.5\,\Omega$, $R_{DE} = 1.5\,\Omega$, with $6\,\Omega$ across $A$–$D$.
3. $\frac{R_{BA}}{R_{AE}} = \frac{5}{3}$ and $\frac{R_{BD}}{R_{DE}} = \frac{2.5}{1.5} = \frac{5}{3}$, so the bridge is balanced and the $6\,\Omega$ carries no current.
4. $R_{BE} = \frac{(5+3)(2.5+1.5)}{(5+3)+(2.5+1.5)} = \frac{8 \times 4}{12} = \frac{8}{3}\,\Omega$.
5. The battery branch has $1.5 + 5.5 + \frac{1}{3} = \frac{22}{3}\,\Omega$ in series with $R_{BE}$, so $R_{total} = \frac{8}{3} + \frac{22}{3} = 10\,\Omega$.
6. $I = \frac{5\,\mathrm{V}}{10\,\Omega} = 0.5\,\mathrm{A}$, which is option $3$.

**Subtopic:** Combination of Resistors · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q001_dfbf454e_12112026.png?v=dfbf454ec3d2)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q001_eb574ac5_12112026.png?v=eb574ac57861)

---

## Q2

Physics · Electromagnetic Waves

The electric field in a plane electromagnetic wave is given by $E_z = 60\cos(5x + 1.5 \times 10^{9}\,t)\,\mathrm{V/m}$. Then expression for the corresponding magnetic field is (here subscripts denote the direction of the field) :

- (1) $B_y = 60\sin(5x + 1.5 \times 10^{9}\,t)\,\mathrm{T}$
- **(2)** $B_y = 2 \times 10^{-7}\cos(5x + 1.5 \times 10^{9}\,t)\,\mathrm{T}$
- (3) $B_x = 2 \times 10^{-7}\cos(5x + 1.5 \times 10^{9}\,t)\,\mathrm{T}$
- (4) $B_z = 60\cos(5x + 1.5 \times 10^{9}\,t)\,\mathrm{T}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In electromagnetic wave, $E$ and $B$ are in same phase and $B_0 = \frac{E_0}{c}$; their planes are perpendicular to each other.
2. $\therefore\ B_y = \frac{60}{c}\cos(5x + 1.5 \times 10^{9}t)\,\mathrm{T}$
3. $= \frac{60}{3 \times 10^{8}}\cos(5x + 1.5 \times 10^{9}t)\,\mathrm{T}$
4. $B_y = 2 \times 10^{-7}\cos(5x + 1.5 \times 10^{9}t)\,\mathrm{T}$

**Solved independently** (answer withheld)

1. Wave speed: $v = \frac{\omega}{k} = \frac{1.5 \times 10^{9}}{5} = 3 \times 10^{8}\,\mathrm{m/s} = c$.
2. The phase $(5x + \omega t)$ means the wave travels along $-\hat{x}$.
3. $\vec{B}$ must be perpendicular to both $\vec{E}$ ($\hat{z}$) and the propagation direction ($\hat{x}$), so $\vec{B}$ lies along $\hat{y}$; check: $\hat{z} \times \hat{y} = -\hat{x}$, consistent with propagation.
4. $B_0 = \frac{E_0}{c} = \frac{60}{3 \times 10^{8}} = 2 \times 10^{-7}\,\mathrm{T}$.
5. $B_y = 2 \times 10^{-7}\cos(5x + 1.5 \times 10^{9}\,t)\,\mathrm{T}$, which is option $2$.

**Subtopic:** Relation Between E, B, and Speed of Light, Transverse Nature of Electromagnetic Waves · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q002_92c715ec_12112026.png?v=92c715ec5fa4)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q002_298732fb_12112026.png?v=298732fb54aa)

---

## Q3

Physics · Waves

A pipe open at both ends has a fundamental frequency $f$ in air. The pipe is now dipped vertically in a water drum to half of its length. The fundamental frequency of the air column is now equal to:

- (1) $2f$
- (2) $\frac{f}{2}$
- **(3)** $f$
- (4) $\frac{3f}{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Fundamental frequency of open pipe (at both ends) $f = \frac{v}{2L}$ $\ldots$(i)
2. Now immersed in water open pipe behaves as closed pipe.
3. $f' = \frac{v}{4\left(\frac{L}{2}\right)} = \frac{v}{2L}$ $\ldots$(ii)
4. $f = f'$

**Solved independently** (answer withheld)

1. For a pipe open at both ends, $f = \frac{v}{2L}$.
2. Dipping half the pipe in water leaves an air column of length $\frac{L}{2}$ closed at one end by the water surface.
3. For a closed pipe, $f' = \frac{v}{4l} = \frac{v}{4(L/2)} = \frac{v}{2L}$.
4. $f' = f$, which is option $3$.

**Subtopic:** Organ Pipe · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q003_3cf0320e_12112026.png?v=3cf0320e1535)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q003_927b02ac_12112026.png?v=927b02ac50bb)

---

## Q4

Physics · Magnetic Effect of Electric Current

An electron (mass $9 \times 10^{-31}\,\mathrm{kg}$ and charge $1.6 \times 10^{-19}\,\mathrm{C}$) moving with speed $c/100$ ($c$ = speed of light) is injected into a magnetic field $\vec{B}$ of magnitude $9 \times 10^{-4}\,\mathrm{T}$ perpendicular to its direction of motion. We wish to apply an uniform electric field $\vec{E}$ together with the magnetic field so that the electron does not deflect from its path. Then (speed of light $c = 3 \times 10^{8}\,\mathrm{m\,s^{-1}}$)

- (1) $\vec{E}$ is parallel to $\vec{B}$ and its magnitude is $27 \times 10^{4}\,\mathrm{V\,m^{-1}}$
- (2) $\vec{E}$ is perpendicular to $\vec{B}$ and its magnitude is $27 \times 10^{4}\,\mathrm{V\,m^{-1}}$
- **(3)** $\vec{E}$ is perpendicular to $\vec{B}$ and its magnitude is $27 \times 10^{2}\,\mathrm{V\,m^{-1}}$
- (4) $\vec{E}$ is parallel to $\vec{B}$ and its magnitude is $27 \times 10^{2}\,\mathrm{V\,m^{-1}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For no deflection of electron, $\vec{F}_B = \vec{F}_E$
2. $-e(\vec{v} \times \vec{B}) = -e\vec{E}$
3. $\Rightarrow \vec{E} = \vec{v} \times \vec{B} \Rightarrow \vec{E} \perp \vec{B}$
4. $E = vB = \frac{c}{100} \times 9 \times 10^{-4}$
5. $= \frac{3 \times 10^{8}}{100} \times 9 \times 10^{-4}$
6. $= 27 \times 10^{2}\,\mathrm{V\,m^{-1}}$

**Solved independently** (answer withheld)

1. For no deflection the electric force must cancel the magnetic force: $qE = qvB$, so $E = vB$, with $\vec{E}$ perpendicular to both $\vec{v}$ and $\vec{B}$.
2. $v = \frac{c}{100} = \frac{3 \times 10^{8}}{100} = 3 \times 10^{6}\,\mathrm{m\,s^{-1}}$.
3. $E = vB = 3 \times 10^{6} \times 9 \times 10^{-4} = 2.7 \times 10^{3}\,\mathrm{V\,m^{-1}} = 27 \times 10^{2}\,\mathrm{V\,m^{-1}}$.
4. $\vec{E} \perp \vec{B}$ with magnitude $27 \times 10^{2}\,\mathrm{V\,m^{-1}}$, which is option $3$.

**Subtopic:** Motion in Combined Electric and Magnetic Field · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q004_f2ee07c9_12112026.png?v=f2ee07c922cc)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q004_119cddc0_12112026.png?v=119cddc036d9)

---

## Q5

Physics · Ray Optics

In a certain camera, a combination of four similar thin convex lenses are arranged axially in contact. Then the power of the combination and the total magnification in comparison to the power ($p$) and magnification ($m$) for each lens will be, respectively

- (1) $p^{4}$ and $m^{4}$
- (2) $4p$ and $4m$
- (3) $p^{4}$ and $4m$
- **(4)** $4p$ and $m^{4}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For series combination of lens
2. $p_{\mathrm{eff}} = p_{1} + p_{2} + p_{3} + p_{4} = 4p$
3. $m_{\mathrm{eff}} = m_{1} \times m_{2} \times m_{3} \times m_{4} = m^{4}$

**Solved independently** (answer withheld)

1. For thin lenses in contact, the powers add: $P = p_1 + p_2 + p_3 + p_4$.
2. With four similar lenses, $P = 4p$.
3. In a lens combination, the total magnification is the product of the individual magnifications: $M = m_1 m_2 m_3 m_4$.
4. With four similar lenses, $M = m^{4}$, so the answer is $4p$ and $m^{4}$, which is option $4$.

**Subtopic:** Combination of Thin Lenses in Contact · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q005_6bb955d5_12112026.png?v=6bb955d5af05)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q005_ca6d1049_12112026.png?v=ca6d10497c87)

---

## Q6

Physics · Magnetic Effect of Electric Current

A $2\,\mathrm{amp}$ current is flowing through two different small circular copper coils having radii ratio $1:2$. The ratio of their respective magnetic moments will be

- (1) $4:1$
- **(2)** $1:4$
- (3) $1:2$
- (4) $2:1$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Magnetic moment of current carrying circular loop $= IA$
2. $M = IA$
3. $M \propto A \quad [I\text{–Same}]$
4. $\frac{M_1}{M_2} = \frac{A_1}{A_2} = \frac{\pi r_1^2}{\pi r_2^2} = \left(\frac{1}{2}\right)^2 = \frac{1}{4}$

**Solved independently** (answer withheld)

1. For a circular coil carrying current $I$, the magnetic moment is $m = I A = I\pi r^2$.
2. The current is the same ($2\,\mathrm{A}$) in both coils, so $\frac{m_1}{m_2} = \frac{r_1^2}{r_2^2}$.
3. $\frac{m_1}{m_2} = \left(\frac{1}{2}\right)^2 = \frac{1}{4}$, i.e. $1:4$, which is option $2$.

**Subtopic:** Current Carrying Loop as a Magnetic Dipole · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q006_78215d14_12112026.png?v=78215d148b26)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q006_6b7dcf3d_12112026.png?v=6b7dcf3d1842)

---

## Q7

Physics · Current Electricity

A constant voltage of $50\,\mathrm{V}$ is maintained between the points $A$ and $B$ of the circuit shown in the figure. The current through the branch $CD$ of the circuit is:

![printed figure: Bridge of 1, 2, 3, 4 ohm resistors with branch CD, fed by 50 V between A and B](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q007_5be5ea60_12112026.png?v=5be5ea6088ec)

*Bridge of 1, 2, 3, 4 ohm resistors with branch CD, fed by 50 V between A and B*

- (1) $3.0\,\mathrm{A}$
- (2) $1.5\,\mathrm{A}$
- **(3)** $2.0\,\mathrm{A}$
- (4) $2.5\,\mathrm{A}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $R_{AB} = (1\,\Omega/3\,\Omega)$ in series with $(2\,\Omega/4\,\Omega)$
2. $= \frac{3\times 1}{3+1} + \frac{2\times 4}{2+4}$
3. $= \frac{3}{4} + \frac{8}{6} = \frac{9+16}{12} = \frac{25}{12}\,\Omega$
4. Now total current through cell
5. $I = \frac{50}{25/12} = 24\,\mathrm{A}$
6. $I_{1\Omega} = \frac{3}{4}\times 24 = 18\,\mathrm{A}$, $I_{3\Omega} = \frac{1}{4}\times 24 = 6\,\mathrm{A}$
7. $I_{2\Omega} = \frac{4}{6}\times 24 = 16\,\mathrm{A}$, $I_{4\Omega} = \frac{2}{6}\times 24 = 8\,\mathrm{A}$
8. Using junction rule at $C$, $I_{CD} = 18 - 16 = 2\,\mathrm{A}$ (From $C$ to $D$)

**Solved independently** (answer withheld)

1. Branch $CD$ is a resistance-free wire, so $C$ and $D$ are at the same potential: $1\,\Omega \parallel 3\,\Omega$ is in series with $2\,\Omega \parallel 4\,\Omega$.
2. $R_1 = \frac{1 \times 3}{1+3} = 0.75\,\Omega$.
3. $R_2 = \frac{2 \times 4}{2+4} = \frac{4}{3}\,\Omega$.
4. $R = 0.75 + \frac{4}{3} = \frac{25}{12}\,\Omega$.
5. $I = \frac{50}{25/12} = 24\,\mathrm{A}$.
6. $V_{AC} = 24 \times 0.75 = 18\,\mathrm{V}$, so $I_{1\Omega} = \frac{18}{1} = 18\,\mathrm{A}$.
7. $V_{CB} = 50 - 18 = 32\,\mathrm{V}$, so $I_{2\Omega} = \frac{32}{2} = 16\,\mathrm{A}$.
8. At node $C$: $I_{CD} = 18 - 16 = 2.0\,\mathrm{A}$, which is option $3$.

**Subtopic:** Kirchhoff's Laws of Current Distribution, Combination of Resistors · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 4)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q007_740b816a_12112026.png?v=740b816ae330)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q007_0b1a6dd5_12112026.png?v=0b1a6dd52adf)

---

## Q8

Physics · Thermodynamics

Two gases $A$ and $B$ are filled at the same pressure in separate cylinders with movable pistons of radius $r_A$ and $r_B$, respectively. On supplying an equal amount of heat to both the systems reversibly under constant pressure, the pistons of gas $A$ and $B$ are displaced by $16\,\mathrm{cm}$ and $9\,\mathrm{cm}$, respectively. If the change in their internal energy is the same, then the ratio $\frac{r_A}{r_B}$ is equal to

- (1) $\frac{\sqrt{3}}{2}$
- (2) $\frac{4}{3}$
- **(3)** $\frac{3}{4}$
- (4) $\frac{2}{\sqrt{3}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Using first law of thermodynamics
2. $\Delta Q = \Delta U + P\Delta V$
3. $\Delta Q$ is same
4. $\Delta U$ is also same
5. $W_A = W_B$
6. $\therefore\ (P\Delta V)_A = (P\Delta V)_B$
7. $P$ is also same
8. $\therefore\ A_A d_A = A_B d_B$
9. $\pi r_A^2 d_A = \pi r_B^2 d_B$
10. $\frac{r_A}{r_B} = \left(\frac{dB}{dA}\right)^{\frac{1}{2}} = \left(\frac{9}{16}\right)^{\frac{1}{2}}$
11. $= \frac{3}{4}$

**Solved independently** (answer withheld)

1. First law: $Q = \Delta U + W$. Since $Q$ and $\Delta U$ are equal for both gases, $W_A = W_B$.
2. At constant pressure $W = P\,\Delta V = P\,\pi r^2 d$, where $d$ is the piston displacement.
3. $P\,\pi r_A^2 (16) = P\,\pi r_B^2 (9)$, so $\left(\frac{r_A}{r_B}\right)^2 = \frac{9}{16}$.
4. $\frac{r_A}{r_B} = \frac{3}{4}$, which is option $3$.

**Subtopic:** Isobaric Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q008_cac15ca4_12112026.png?v=cac15ca4de38)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q008_d41e3392_12112026.png?v=d41e3392bbbe)

---

## Q9

Physics · Thermodynamics

A container has two chambers of volumes $V_1 = 2$ litres and $V_2 = 3$ litres separated by a partition made of a thermal insulator. The chambers contain $n_1 = 5$ and $n_2 = 4$ moles of ideal gas at pressures $p_1 = 1\,\mathrm{atm}$ and $p_2 = 2\,\mathrm{atm}$, respectively. When the partition is removed, the mixture attains an equilibrium pressure of

- (1) $1.8\,\mathrm{atm}$
- (2) $1.3\,\mathrm{atm}$
- **(3)** $1.6\,\mathrm{atm}$
- (4) $1.4\,\mathrm{atm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $P_1V_1 + P_2V_2 = P(V_1 + V_2)$
2. $1(2) + 2(3) = P(2 + 3)$
3. $\frac{8}{5} = P$
4. $\Rightarrow 1.6\,\mathrm{atm}$

**Solved independently** (answer withheld)

1. No heat or work exchange with surroundings, so the total internal energy is conserved: $U_1 + U_2 = U$.
2. For an ideal gas $U = \frac{f}{2} nRT = \frac{f}{2} pV$, so $p_1V_1 + p_2V_2 = p(V_1 + V_2)$.
3. $p_1V_1 + p_2V_2 = 1\times 2 + 2\times 3 = 8\,\mathrm{atm\,L}$.
4. $p = \frac{8}{2+3} = 1.6\,\mathrm{atm}$, which is option $3$.

**Subtopic:** Ideal Gas Equation · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 6)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q009_fdb25315_12112026.png?v=fdb25315dd8b)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q009_30ceb3cd_12112026.png?v=30ceb3cd2bd4)

---

## Q10

Physics · Gravitation

The radius of Martian orbit around the Sun is about 4 times the radius of the orbit of Mercury. The Martian year is 687 Earth days. Then which of the following is the length of 1 year on Mercury?

- (1) 124 earth days
- **(2)** 88 earth days
- (3) 225 earth days
- (4) 172 earth days

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Applying Kepler's $3^{\mathrm{rd}}$ law : $T^{2} \propto R^{3}$
2. Radius of Martian orbit, $R' = 4R$
3. $\left(\frac{T'}{T}\right)^{2} = \left(\frac{R'}{R}\right)^{3} = \left(\frac{4R}{R}\right)^{3} = 4^{3} = 64 \Rightarrow \frac{T'}{T} = 8$
4. $\therefore$ Length of 1 year on Mercury $= T = \frac{T'}{8} = \frac{687}{8} = 85.88$ days

**Solved independently** (answer withheld)

1. By Kepler's third law, $T^2 \propto r^3$, so $T \propto r^{3/2}$.
2. $\frac{T_{Mars}}{T_{Mercury}} = \left(\frac{r_{Mars}}{r_{Mercury}}\right)^{3/2} = 4^{3/2} = 8$.
3. $T_{Mercury} = \frac{687}{8} \approx 85.9$ earth days.
4. The closest option is $88$ earth days, which is option $2$.

**Subtopic:** Kepler's Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q010_22bfbc45_12112026.png?v=22bfbc4504e7)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q010_89d34549_12112026.png?v=89d34549e58f)

---

## Q11

Physics · Alternating Current

To an ac power supply of $220\,\mathrm{V}$ at $50\,\mathrm{Hz}$, a resistor of $20\,\Omega$, a capacitor of reactance $25\,\Omega$ and an inductor of reactance $45\,\Omega$ are connected in series. The corresponding current in the circuit and the phase angle between the current and the voltage is, respectively

- (1) $15.6\,\mathrm{A}$ and $45^\circ$
- (2) $7.8\,\mathrm{A}$ and $30^\circ$
- **(3)** $7.8\,\mathrm{A}$ and $45^\circ$
- (4) $15.6\,\mathrm{A}$ and $30^\circ$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $X_L = 45\,\mathrm{W}$, $X_C = 25\,\mathrm{W}$, $R = 20\,\mathrm{W}$
2. $I = \frac{220}{\sqrt{(X_L - X_C)^2 + R^2}} = \frac{220}{\sqrt{(45 - 25)^2 + 20^2}}$
3. $= \frac{220}{2\sqrt{2}} = \frac{11}{\sqrt{2}} = 7.779\,\mathrm{A}$
4. $\tan\phi = \frac{X_L - X_C}{R} = \frac{45 - 25}{20} = 1$
5. $f = 45^\circ$

**Solved independently** (answer withheld)

1. Net reactance: $X = X_L - X_C = 45 - 25 = 20\,\Omega$.
2. Impedance: $Z = \sqrt{R^2 + X^2} = \sqrt{20^2 + 20^2} = 20\sqrt{2} \approx 28.28\,\Omega$.
3. Current: $I = \frac{V}{Z} = \frac{220}{28.28} \approx 7.8\,\mathrm{A}$.
4. Phase angle: $\tan\phi = \frac{X}{R} = \frac{20}{20} = 1 \Rightarrow \phi = 45^\circ$.
5. $7.8\,\mathrm{A}$ and $45^\circ$ is option $3$.

**Subtopic:** RLC Circuit · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 6)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q011_08d10f28_12112026.png?v=08d10f2853db)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q011_f2f8ebb9_12112026.png?v=f2f8ebb9e98a)

---

## Q12

Physics · Current Electricity

A wire of resistance $R$ is cut into 8 equal pieces. From these pieces two equivalent resistances are made by adding four of these together in parallel. Then these two sets are added in series. The net effective resistance of the combination is:

- (1) $\frac{R}{8}$
- (2) $\frac{R}{64}$
- (3) $\frac{R}{32}$
- **(4)** $\frac{R}{16}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. After being cut into $8$ equal pieces,
2. $\Rightarrow$ Resistance of each piece $= R' = \frac{R}{8}$
3. Each set has $4$ pieces in parallel combination
4. $\Rightarrow$ Resistance of each set $= R'' = \frac{R'}{4} = \frac{R}{32}$
5. Both sets are connected in series
6. $\therefore\ R_{eq} = R'' + R'' = 2 \times \frac{R}{32} = \frac{R}{16}$

**Solved independently** (answer withheld)

1. Cutting into 8 equal pieces gives each piece $r = \frac{R}{8}$.
2. Four pieces in parallel: $R_p = \frac{r}{4} = \frac{R}{32}$.
3. Two such sets in series: $R_{net} = 2 \times \frac{R}{32} = \frac{R}{16}$, which is option $4$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q012_c2dde982_12112026.png?v=c2dde98200e8)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q012_5ced29f6_12112026.png?v=5ced29f6ac3e)

---

## Q13

Physics · Semiconductor Electronics

The output ($Y$) of the given logic implementation is similar to the output of an/a _____ gate.

![printed figure: A NOR gate (inputs A, B) and a NAND gate (inputs B, A) feeding an AND gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q013_c8498c87_12112026.png?v=c8498c87f65c)

*A NOR gate (inputs A, B) and a NAND gate (inputs B, A) feeding an AND gate with output Y*

- **(1)** NOR
- (2) AND
- (3) NAND
- (4) OR

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $Y_1 = \overline{A + B}$
2. $Y_2 = \overline{A \cdot B}$
3. $Y = Y_1 \cdot Y_2$
4. $= \overline{A + B} \cdot \overline{A \cdot B}$
5. $= \overline{(A + B) + A \cdot B}$
6. $= \overline{A + B(1 + A)}$
7. $= \overline{A + B}$ NOR gate

**Solved independently** (answer withheld)

1. The upper gate is a NOR gate: its output is $\overline{A+B} = \bar{A}\bar{B}$.
2. The lower gate is a NAND gate: its output is $\overline{AB} = \bar{A}+\bar{B}$.
3. The final gate is an AND gate: $Y = \bar{A}\bar{B}\,(\bar{A}+\bar{B})$.
4. Expanding: $Y = \bar{A}\bar{B} + \bar{A}\bar{B} = \bar{A}\bar{B} = \overline{A+B}$.
5. Truth table check: $Y = 1$ only for $A = B = 0$, so $Y$ is the NOR output, option $1$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q013_d1a7a612_12112026.png?v=d1a7a6126bc7)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q013_9cd0fbf1_12112026.png?v=9cd0fbf1ab6b)

---

## Q14

Physics · Electrostatics

Two identical charged conducting spheres $A$ and $B$ have their centres separated by a certain distance. Charge on each sphere is $q$ and the force of repulsion between them is $F$. A third identical uncharged conducting sphere is brought in contact with sphere $A$ first and then with $B$ and finally removed from both. New force of repulsion between spheres $A$ and $B$ (Radii of $A$ and $B$ are negligible compared to the distance of separation so that for calculating force between them they can be considered as point charges) is best given as:

- **(1)** $\frac{3F}{8}$
- (2) $\frac{3F}{5}$
- (3) $\frac{2F}{3}$
- (4) $\frac{F}{2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $F = \frac{Kqq}{r^{2}}$
2. $F' = \frac{K\frac{q}{2}\frac{3q}{4}}{r^{2}}$
3. $F' = \frac{3F}{8}$

**Solved independently** (answer withheld)

1. Initially $F = \frac{k q^2}{r^2}$.
2. Identical sphere $C$ touches $A$: charge shares equally, $q_A = q_C = \frac{q + 0}{2} = \frac{q}{2}$.
3. $C$ then touches $B$: $q_B = q_C' = \frac{q + q/2}{2} = \frac{3q}{4}$.
4. $F' = \frac{k (q/2)(3q/4)}{r^2} = \frac{3}{8}\frac{k q^2}{r^2} = \frac{3F}{8}$, which is option $1$.

**Subtopic:** Coulomb's Law, Common Potential and Redistribution of Charge Between Connected Conductors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q014_07978e4f_12112026.png?v=07978e4f53b8)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q014_43900ab9_12112026.png?v=43900ab95685)

---

## Q15

Physics · Units and Measurements

Consider the diameter of a spherical object being measured with the help of a Vernier callipers. Suppose its 10 Vernier Scale Divisions (V.S.D.) are equal to its 9 Main Scale Divisions (M.S.D.). The least division in the M.S. is $0.1\,\mathrm{cm}$ and the zero of V.S. is at $x = 0.1\,\mathrm{cm}$ when the jaws of Vernier callipers are closed.
If the main scale reading for the diameter is $M = 5\,\mathrm{cm}$ and the number of coinciding vernier division is 8, the measured diameter after zero error correction, is

- (1) $5.00\,\mathrm{cm}$
- (2) $5.18\,\mathrm{cm}$
- (3) $5.08\,\mathrm{cm}$
- **(4)** $4.98\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Least count $= 1\,\mathrm{MSD} - 1\,\mathrm{VSD}$
2. $= 1\,\mathrm{MSD} - \frac{9}{10}\,\mathrm{MSD} = \frac{1}{10}\,\mathrm{MSD}$
3. $= \frac{1}{10} \times 0.1\,\mathrm{cm} = 0.01\,\mathrm{cm}$
4. Zero error $= +0.1\,\mathrm{cm}$
5. Main scale reading $= 5\,\mathrm{cm}$
6. Vernier scale reading $= 8 \times 0.01 = 0.08\,\mathrm{cm}$
7. Final measurement of diameter
8. $= 5 + 0.08 - 0.1 = 4.98\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. $10\,\text{VSD} = 9\,\text{MSD}$, so $1\,\text{VSD} = \frac{9}{10}\,\text{MSD}$.
2. $\text{LC} = 1\,\text{MSD} - 1\,\text{VSD} = \frac{1}{10}\times 0.1\,\mathrm{cm} = 0.01\,\mathrm{cm}$.
3. Observed reading $= M + n\,\text{LC} = 5 + 8\times 0.01 = 5.08\,\mathrm{cm}$.
4. With jaws closed the vernier zero is at $x = +0.1\,\mathrm{cm}$, so the zero error is $+0.1\,\mathrm{cm}$.
5. Corrected diameter $= 5.08 - 0.10 = 4.98\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 8)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q015_328ab7f5_12112026.png?v=328ab7f50d48)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q015_cd33fd39_12112026.png?v=cd33fd398a8b)

---

## Q16

Physics · Kinematics

In some appropriate units, time ($t$) and position ($x$) relation of a moving particle is given by $t = x^{2} + x$. The acceleration of the particle is

- (1) $+\frac{2}{2x+1}$
- (2) $-\frac{2}{(x+2)^{3}}$
- **(3)** $-\frac{2}{(2x+1)^{3}}$
- (4) $+\frac{2}{(x+1)^{3}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $t = x^{2} + x$
2. $\frac{dt}{dx} = 2x + 1$
3. $v = \frac{dx}{dt} = \frac{1}{(2x+1)}$
4. $\frac{dv}{dx} = \frac{-2}{(2x+1)^{2}}$
5. $a = v\frac{dv}{dx} = \frac{1}{(2x+1)}\left[\frac{-2}{(2x+1)^{2}}\right]$
6. $= -\frac{2}{(2x+1)^{3}}$

**Solved independently** (answer withheld)

1. Differentiate $t = x^2 + x$ with respect to $x$: $\frac{dt}{dx} = 2x + 1$.
2. So $v = \frac{dx}{dt} = \frac{1}{2x+1}$.
3. $\frac{dv}{dx} = -\frac{2}{(2x+1)^2}$.
4. $a = v\frac{dv}{dx} = \frac{1}{2x+1}\cdot\left(-\frac{2}{(2x+1)^2}\right) = -\frac{2}{(2x+1)^3}$, which is option $3$.

**Subtopic:** Instantaneous Acceleration · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 8)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q016_f31e1ea0_12112026.png?v=f31e1ea026a8)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q016_86e279b5_12112026.png?v=86e279b54723)

---

## Q17

Physics · Modern Physics

Which of the following options represent the variation of photoelectric current with property of light shown on the $x$-axis?

![printed figure: Four graphs A-D of photoelectric current against intensity or frequency of light](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q017_25d7167a_12112026.png?v=25d7167aee54)

*Four graphs A-D of photoelectric current against intensity or frequency of light*

- (A) [graph]
- (B) [graph]
- (C) [graph]
- (D) [graph]

- (1) B and D
- **(2)** A only
- (3) A and C
- (4) A and D

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Photoelectric current is directly proportional to intensity of light.

**Solved independently** (answer withheld)

1. Above threshold, the number of photoelectrons per second is proportional to the number of incident photons, so $i \propto I$: a straight line through the origin, as in graph A. Graph A is correct.
2. Graph B shows $i$ constant with intensity, which contradicts $i \propto I$. Graph B is wrong.
3. No photoemission occurs for $\nu < \nu_0$, so $i = 0$ below threshold; graph C starts rising from $\nu = 0$, so graph C is wrong.
4. For $\nu > \nu_0$ the photocurrent depends on photon number (intensity), not on $\nu$; increasing $\nu$ raises only $K_{max} = h\nu - \phi_0$. A linear rise of $i$ with $\nu$ (graph D) is not supported, so graph D is wrong.
5. Only A is correct, which is option $2$.

**Subtopic:** Photoelectric Effect · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 9)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q017_1d0a0977_12112026.png?v=1d0a0977ec90)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q017_972a7bf7_12112026.png?v=972a7bf76278)

---

## Q18

Physics · Modern Physics

A particle of mass $m$ is moving around the origin with a constant force $F$ pulling it towards the origin. If Bohr model is used to describe its motion, the radius of the $n^{\text{th}}$ orbit and the particle’s speed $\nu$ in the orbit depend on $n$ as

- (1) $r \propto n^{4/3};\ \nu \propto n^{-1/3}$
- (2) $r \propto n^{1/3};\ \nu \propto n^{1/3}$
- (3) $r \propto n^{1/3};\ \nu \propto n^{2/3}$
- **(4)** $r \propto n^{2/3};\ \nu \propto n^{1/3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Given, force is constant
2. $F = \frac{mv^{2}}{r}$
3. $\Rightarrow \frac{v^{2}}{r} = \text{constant}$
4. $\Rightarrow r \propto v^{2}$ ...(1)
5. & $L = mvr = \frac{nh}{2\pi}$ ...(2)
6. $\Rightarrow$ on solving equation (1) and equation (2)
7. $\nu \propto n^{1/3}$ and $r \propto n^{2/3}$

**Solved independently** (answer withheld)

1. The constant central force supplies the centripetal force: $\frac{mv^2}{r} = F$, so $v^2 = \frac{Fr}{m}$.
2. Bohr quantisation: $mvr = \frac{nh}{2\pi}$, so $v = \frac{nh}{2\pi m r}$.
3. Substitute: $\frac{n^2h^2}{4\pi^2 m^2 r^2} = \frac{Fr}{m}$, so $r^3 = \frac{n^2h^2}{4\pi^2 m F}$.
4. Hence $r \propto n^{2/3}$.
5. $v \propto r^{1/2} \propto n^{1/3}$, which is option $4$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 9)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q018_446bf8ed_12112026.png?v=446bf8ed77f6)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q018_66362f04_12112026.png?v=66362f049ed0)

---

## Q19

Physics · Work, Energy and Power

A bob of heavy mass $m$ is suspended by a light string of length $l$. The bob is given a horizontal velocity $v_0$ as shown in figure. If the string gets slack at some point $P$ making an angle $\theta$ from the horizontal, the ratio of the speed $v$ of the bob at point $P$ to its initial speed $v_0$ is:

![printed figure: Bob m on a string of length l about O, given horizontal velocity v0 at the bottom; string slackens at P at angle theta above the horizontal](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q019_990bb05c_12112026.png?v=990bb05c5188)

*Bob m on a string of length l about O, given horizontal velocity v0 at the bottom; string slackens at P at angle theta above the horizontal*

- **(1)** $\left(\dfrac{\sin\theta}{2+3\sin\theta}\right)^{\frac{1}{2}}$
- (2) $(\sin\theta)^{\frac{1}{2}}$
- (3) $\left(\dfrac{1}{2+3\sin\theta}\right)^{\frac{1}{2}}$
- (4) $\left(\dfrac{\cos\theta}{2+3\sin\theta}\right)^{\frac{1}{2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. At Point $P$, $mg\sin\theta = \frac{mv^2}{l}$ ...(1)
2. By conservation of mechanical energy at point $P \in Q$
3. $\frac{1}{2}mv_0^2 = \frac{1}{2}mv^2 + mg(l + l\sin\theta)$
4. $\frac{v_0^2}{2} = \frac{v^2}{2} + gl(1 + \sin\theta)$
5. Put $gl = \frac{v^2}{\sin\theta}$ using (1)
6. $\frac{v_0^2}{2} = \frac{v^2}{2} + \frac{v^2}{\sin\theta}(1 + \sin\theta)$
7. $\frac{v_0^2}{2} = \frac{v^2}{2} + \frac{v^2}{\sin\theta} + v^2$
8. $\frac{v_0^2}{2} = \frac{3}{2}v^2 + \frac{2v^2}{2\sin\theta}$
9. $v_0^2 = v^2\left[3 + \frac{2}{\sin\theta}\right]$
10. $\frac{v}{v_0} = \left(\frac{\sin\theta}{3\sin\theta + 2}\right)^{\frac{1}{2}}$

**Solved independently** (answer withheld)

1. From the figure, $P$ is at angle $\theta$ above the horizontal through $O$, so its height above the lowest point is $h = l + l\sin\theta$.
2. At $P$ the radial component of gravity toward $O$ is $mg\sin\theta$, so $T + mg\sin\theta = \frac{mv^2}{l}$.
3. The string goes slack when $T = 0$: $v^2 = gl\sin\theta$.
4. Energy conservation: $v_0^2 = v^2 + 2gl(1+\sin\theta)$.
5. Substituting: $v_0^2 = gl\sin\theta + 2gl + 2gl\sin\theta = gl(2+3\sin\theta)$.
6. $\frac{v}{v_0} = \left(\frac{\sin\theta}{2+3\sin\theta}\right)^{1/2}$, which is option $1$.

**Subtopic:** Motion in a Vertical Circular Motion · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q019_19aa2b3b_12112026.png?v=19aa2b3b1c62)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q019_12424965_12112026.png?v=1242496547c9)

---

## Q20

Physics · Semiconductor Electronics

A full wave rectifier circuit with diodes ($D_1$) and ($D_2$) is shown in the figure. If input supply voltage $V_{in} = 220\sin(100\pi t)$ volt, then at $t = 15\,\mathrm{msec}$

![printed figure: Centre-tap full wave rectifier with diodes D1, D2 and load RL](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q020_92677bd1_12112026.png?v=92677bd15a79)

*Centre-tap full wave rectifier with diodes D1, D2 and load RL*

- (1) $D_1$ and $D_2$ both are reverse biased
- (2) $D_1$ is forward biased, $D_2$ is reverse biased
- **(3)** $D_1$ is reverse biased, $D_2$ is forward biased.
- (4) $D_1$ and $D_2$ both are forward biased

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $V_{in} = 220\sin(100\pi t)$ volt
2. $t = 15\,\mathrm{ms}$
3. $t = 0.015\,\mathrm{s}$
4. $\omega = 100\pi$
5. $\frac{2\pi}{T} = 100\pi$
6. $T = \frac{1}{50}\,\mathrm{s}$
7. $T = 0.02\,\mathrm{s}$
8. $\therefore\ t = \frac{3T}{4}$
9. i.e. negative half cycle.
10. So now negative half cycle is fed to circuit making $D_1$ as reverse biased and $D_2$ as forward biased.

**Solved independently** (answer withheld)

1. $\omega t = 100\pi \times 15\times10^{-3} = 1.5\pi$.
2. $V_{in} = 220\sin(1.5\pi) = -220\,\mathrm{V}$, so the input is in its negative half cycle.
3. In the negative half cycle the secondary end feeding $D_1$ is at lower potential than the centre tap, so $D_1$ is reverse biased.
4. The secondary end feeding $D_2$ is at higher potential than the centre tap, so $D_2$ is forward biased, which is option $3$.

**Subtopic:** Use of PN Junction Diode as Rectifier · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 11)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q020_044d86a3_12112026.png?v=044d86a31974)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q020_0f7c10f0_12112026.png?v=0f7c10f0987b)

---

## Q21

Physics · Mechanical Properties of Fluids

A balloon is made of a material of surface tension $S$ and its inflation outlet (from where gas is filled in it) has small area $A$. It is filled with a gas of density $\rho$ and takes a spherical shape of radius $R$. When the gas is allowed to flow freely out of it, its radius $r$ changes from $R$ to 0 (zero) in time $T$. If the speed $v(r)$ of gas coming out of the balloon depends on $r$ as $r^{a}$ and $T \propto S^{\alpha} A^{\beta} \rho^{\gamma} R^{\delta}$ then

- (1) $a=\frac{1}{2}, \alpha=\frac{1}{2}, \beta=-\frac{1}{2}, \gamma=\frac{1}{2}, \delta=\frac{7}{2}$
- (2) $a=\frac{1}{2}, \alpha=\frac{1}{2}, \beta=-1, \gamma=+1, \delta=\frac{3}{2}$
- (3) $a=-\frac{1}{2}, \alpha=-\frac{1}{2}, \beta=-1, \gamma=-\frac{1}{2}, \delta=\frac{5}{2}$
- **(4)** $a=-\frac{1}{2}, \alpha=-\frac{1}{2}, \beta=-1, \gamma=\frac{1}{2}, \delta=\frac{7}{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $T \propto S^{\alpha}A^{\beta}\rho^{\gamma}R^{\delta}$
2. $\mathrm{M^{0}L^{0}T^{1}} = K(\mathrm{MT^{-2}})^{\alpha}(L^{2})^{\beta}(\mathrm{ML^{-3}})^{\gamma}\mathrm{L}^{\delta}$
3. $\mathrm{M^{0}L^{0}T^{1}} = K[\mathrm{M}^{\alpha + \gamma}\mathrm{L}^{2\beta - 3\gamma + \delta}\mathrm{T}^{-2\alpha}]$
4. $-2\alpha = 1 \quad \alpha = -\frac{1}{2}$
5. $\alpha + \gamma = 0 \quad \gamma = \frac{1}{2}$
6. $2\beta - 3\gamma + \delta = 0$
7. $2\beta - 3\left(\frac{1}{2}\right) + \delta = 0$
8. By hit and trial (using option (1))
9. Put $\beta = -1$
10. $2(-1) - \frac{3}{2} + \delta = 0 \quad \therefore \delta = \frac{7}{2}$

**Solved independently** (answer withheld)

1. Excess pressure inside the balloon due to surface tension is $\Delta P = \frac{kS}{r}$ (with $k = 2$ or $4$, a constant).
2. Bernoulli at the outlet: $\frac{1}{2}\rho v^2 = \frac{kS}{r}$, so $v = \sqrt{\frac{2kS}{\rho r}} \propto r^{-1/2}$, giving $a = -\frac{1}{2}$.
3. Volume outflow rate: $\frac{d}{dt}\left(\frac{4}{3}\pi r^3\right) = -Av$, i.e. $4\pi r^2 \frac{dr}{dt} = -A\sqrt{\frac{2kS}{\rho r}}$.
4. Separate variables: $dt = -\frac{4\pi}{A}\sqrt{\frac{\rho}{2kS}}\, r^{5/2}\, dr$.
5. Integrate $r$ from $R$ to $0$: $T = \frac{4\pi}{A}\sqrt{\frac{\rho}{2kS}} \cdot \frac{2}{7} R^{7/2}$.
6. Hence $T \propto S^{-1/2} A^{-1} \rho^{1/2} R^{7/2}$: $\alpha = -\frac{1}{2}, \beta = -1, \gamma = \frac{1}{2}, \delta = \frac{7}{2}$, which is option $4$.

**Subtopic:** Excess Pressure on Curved Surface (General Case, Drop, Soap Bubbles, Air Bubbles), Equation of Continuity and Bernoulli's Equation · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 11)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q021_9c94c8a4_12112026.png?v=9c94c8a4cd59)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q021_ac982d5c_12112026.png?v=ac982d5c28f9)

---

## Q22

Physics · Ray Optics

A microscope has an objective of focal length $2\,\mathrm{cm}$, eyepiece of focal length $4\,\mathrm{cm}$ and the tube length of $40\,\mathrm{cm}$. If the distance of distinct vision of eye is $25\,\mathrm{cm}$, the magnification in the microscope is

- (1) $250$
- (2) $100$
- **(3)** $125$
- (4) $150$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $m = \frac{L}{f_o} \times \frac{D}{f_e}$
2. $= \frac{40}{2} \times \frac{25}{4}$
3. $m = 125$

**Solved independently** (answer withheld)

1. For a compound microscope with the final image at infinity, $m = \frac{L}{f_o}\cdot\frac{D}{f_e}$.
2. $\frac{L}{f_o} = \frac{40}{2} = 20$.
3. $\frac{D}{f_e} = \frac{25}{4} = 6.25$.
4. $m = 20 \times 6.25 = 125$, which is option $3$.

**Subtopic:** Resolving and Magnifying Power of Microscope · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q022_f3342194_12112026.png?v=f3342194ab4f)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q022_3cf565f9_12112026.png?v=3cf565f922ca)

---

## Q23

Physics · Oscillations

Two identical point masses $P$ and $Q$, suspended from two separate massless springs of spring constants $k_1$ and $k_2$, respectively, oscillate vertically. If their maximum speeds are the same, the ratio $(A_Q/A_P)$ of the amplitude $A_Q$ of mass $Q$ to the amplitude $A_P$ of mass $P$ is

- **(1)** $\sqrt{\frac{k_1}{k_2}}$
- (2) $\frac{k_2}{k_1}$
- (3) $\frac{k_1}{k_2}$
- (4) $\sqrt{\frac{k_2}{k_1}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Maximum velocity $V = A\omega$
2. $v_P = v_Q$
3. $A_P\omega_P = A_Q\omega_Q$
4. $\frac{A_Q}{A_P} = \frac{\omega_P}{\omega_Q}$ $\left(\omega = \sqrt{\frac{k}{m}}\right)$
5. $= \sqrt{\frac{k_P}{m_P}\frac{m_Q}{k_Q}}$
6. $= \sqrt{\frac{k_1}{k_2}}$

**Solved independently** (answer withheld)

1. For SHM, $v_{max} = A\omega$ with $\omega = \sqrt{\frac{k}{m}}$.
2. Equal maximum speeds and equal masses: $A_P\sqrt{\frac{k_1}{m}} = A_Q\sqrt{\frac{k_2}{m}}$.
3. $\frac{A_Q}{A_P} = \sqrt{\frac{k_1}{k_2}}$, which is option $1$.

**Subtopic:** Speed in SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q023_d4ee8047_12112026.png?v=d4ee80472539)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q023_fd7de6c3_12112026.png?v=fd7de6c31aad)

---

## Q24

Physics · Electromagnetic Waves

A parallel plate capacitor made of circular plates is being charged such that the surface charge density on its plates is increasing at a constant rate with time. The magnetic field arising due to displacement current is:

- (1) Zero between the plates and non-zero outside
- (2) Zero at all places
- (3) Constant between the plates and zero outside the plates
- **(4)** Non-zero everywhere with maximum at the imaginary cylindrical surface connecting peripheries of the plates

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Let the surface charge density be $\sigma = \frac{q}{A}$
2. Given $\frac{d\sigma}{dt} = \text{constant}$
3. $\therefore \frac{d}{dt}\left(\frac{q}{A}\right) = \text{constant} \Rightarrow \frac{I}{A}i = \text{constant}$
4. It means displacement current is constant.
5. This system will act like a cylindrical wire.
6. The graph of magnetic field $(B)$ vs $r$ is

**Solved independently** (answer withheld)

1. Since $\sigma$ increases at a constant rate, $E = \sigma/\varepsilon_0$ gives $\frac{dE}{dt} = \frac{1}{\varepsilon_0}\frac{d\sigma}{dt} = $ constant, so the displacement current density $j_d = \varepsilon_0 \frac{dE}{dt} = \frac{d\sigma}{dt}$ is uniform and non-zero between the plates.
2. Inside ($r<R$), Ampere-Maxwell law: $B(2\pi r) = \mu_0 j_d \pi r^2 \Rightarrow B = \frac{\mu_0 j_d r}{2}$, increasing with $r$.
3. Outside ($r>R$): $B(2\pi r) = \mu_0 j_d \pi R^2 \Rightarrow B = \frac{\mu_0 j_d R^2}{2r}$, decreasing with $r$ but non-zero.
4. $B$ is maximum at $r = R$, the cylindrical surface joining the plate peripheries, and non-zero elsewhere, which is option $4$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 12)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q024_84344994_12112026.png?v=843449943902)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q024_54717922_12112026.png?v=54717922d224)

---

## Q25

Physics · Electrostatics

An electric dipole with dipole moment $5 \times 10^{-6}\,\mathrm{C\,m}$ is aligned with the direction of a uniform electric field of magnitude $4 \times 10^{5}\,\mathrm{N/C}$. The dipole is then rotated through an angle of $60^\circ$ with respect to the electric field. The change in the potential energy of the dipole is:

- (1) $1.5\,\mathrm{J}$
- (2) $0.8\,\mathrm{J}$
- **(3)** $1.0\,\mathrm{J}$
- (4) $1.2\,\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Given
2. $|\vec{P}| = 5 \times 10^{-6}\,\mathrm{C\,m}$
3. $|\vec{E}| = 4 \times 10^{5}\,\mathrm{N/C}$
4. $\theta_i = 0^\circ$ and $\theta_f = 60^\circ$
5. $\Delta U = U_f - U_i$
6. $= -PE\cos\theta_f + PE\cos\theta_i$
7. $= PE[\cos\theta_i - \cos\theta_f)$
8. $= 5 \times 10^{-6} \times 4 \times 10^{5} \left[1 - \frac{1}{2}\right)$
9. $= 10 \times 10^{-6} \times 10^{5} = 1\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Potential energy of a dipole in a uniform field is $U = -pE\cos\theta$.
2. $\Delta U = U_{60^\circ} - U_{0^\circ} = pE(\cos 0^\circ - \cos 60^\circ) = pE(1 - \tfrac{1}{2})$.
3. $pE = (5 \times 10^{-6})(4 \times 10^{5}) = 2\,\mathrm{J}$.
4. $\Delta U = 2 \times 0.5 = 1.0\,\mathrm{J}$, which is option $3$.

**Subtopic:** Potential Energy of Dipole in Uniform Electric Field · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 13)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q025_9dcf5281_12112026.png?v=9dcf52817ea5)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q025_24baf1b4_12112026.png?v=24baf1b415b6)

---

## Q26

Physics · Laws of Motion

There are two inclined surfaces of equal length ($L$) and same angle of inclination $45^\circ$ with the horizontal. One of them is rough and the other is perfectly smooth. A given body takes 2 times as much time to slide down on rough surface than on the smooth surface. The coefficient of kinetic friction ($\mu_k$) between the object and the rough surface is close to

- **(1)** $0.75$
- (2) $0.25$
- (3) $0.40$
- (4) $0.5$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $t_{\mathrm{rough}} = 2t_{\mathrm{smooth}}$
2. $a_{\mathrm{smooth}} = g\sin\theta$
3. $t \propto \frac{1}{\sqrt{a}} \Rightarrow t_{\mathrm{smooth}} \propto \frac{1}{\sqrt{g\sin\theta}}$
4. $a_{\mathrm{rough}} = g\sin\theta - \mu_k g\cos\theta$
5. $\frac{t_{\mathrm{rough}}}{t_{\mathrm{smooth}}} = \frac{\sqrt{\sin\theta}}{\sqrt{\sin\theta - \mu_k\cos\theta}} = 2$
6. Squaring both sides
7. $\frac{\sin\theta}{\sin\theta - \mu_k\cos\theta} = 4 \Rightarrow \frac{\frac{1}{\sqrt{2}}}{\frac{1}{\sqrt{2}} - \mu_k \times \frac{1}{\sqrt{2}}} = 4$
8. $\Rightarrow 1 - \mu_k = \frac{1}{4}$
9. $\mu_k = \frac{3}{4}$
10. $= 0.75$

**Solved independently** (answer withheld)

1. Starting from rest over the same length, $L = \frac{1}{2} a t^2$, so $a \propto \frac{1}{t^2}$.
2. With $t_r = 2 t_s$, $a_r = \frac{a_s}{4}$.
3. Smooth incline: $a_s = g\sin 45^\circ$; rough incline: $a_r = g(\sin 45^\circ - \mu_k \cos 45^\circ)$.
4. $g(\sin 45^\circ - \mu_k \cos 45^\circ) = \frac{g \sin 45^\circ}{4}$, and since $\sin 45^\circ = \cos 45^\circ$, $1 - \mu_k = \frac{1}{4}$.
5. $\mu_k = 0.75$, which is option $1$.

**Subtopic:** Kinetic Friction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q026_617a8fa6_12112026.png?v=617a8fa60123)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q026_8d67f8ef_12112026.png?v=8d67f8ef7ec3)

---

## Q27

Physics · Modern Physics

De-Broglie wavelength of an electron orbiting in the $n = 2$ state of hydrogen atom is close to (Given Bohr radius $= 0.052\,\mathrm{nm}$)

- (1) $2.67\,\mathrm{nm}$
- (2) $0.067\,\mathrm{nm}$
- **(3)** $0.67\,\mathrm{nm}$
- (4) $1.67\,\mathrm{nm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $r = 0.052\,n^{2}$
2. For $n = 2$
3. $r = 0.052 \times 4$
4. $= 0.208\,\mathrm{nm}$
5. $Mvr = \frac{nh}{2\pi}$
6. $\lambda = \frac{h}{Mv} = \pi r$
7. $= 3.14 \times 0.208\,\mathrm{nm}$
8. $= 0.65317\,\mathrm{nm}$
9. $\approx 0.67\,\mathrm{nm}$

**Solved independently** (answer withheld)

1. Bohr quantisation: $2\pi r_n = n\lambda$, so $\lambda = \frac{2\pi r_n}{n}$.
2. $r_n = n^2 a_0$, so $r_2 = 4 \times 0.052\,\mathrm{nm} = 0.208\,\mathrm{nm}$.
3. $\lambda = \frac{2\pi (0.208)}{2} = \pi \times 0.208 \approx 0.653\,\mathrm{nm}$.
4. $0.653\,\mathrm{nm}$ is closest to $0.67\,\mathrm{nm}$, which is option $3$.

**Subtopic:** de Broglie's Explanation of Bohr's Quantization Postulate · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q027_ac66ce9a_12112026.png?v=ac66ce9a9aad)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q027_9d6e2cda_12112026.png?v=9d6e2cda851d)

---

## Q28

Physics · Rotational Motion

The Sun rotates around its centre once in $27$ days. What will be the period of revolution if the Sun were to expand to twice its present radius without any external influence? Assume the Sun to be a sphere of uniform density.

- **(1)** $108$ days
- (2) $100$ days
- (3) $105$ days
- (4) $115$ days

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Assuming the Sun to be a solid sphere, $I = \frac{2}{5}mR^{2}$
2. Using conservation of angular momentum, $I'\omega' = I\omega$
3. $\Rightarrow \frac{2}{5}m(2R)^{2} \times \frac{2\pi}{T'} = \frac{2}{5}mR^{2} \times \frac{2\pi}{T}$
4. $\Rightarrow T' = 4T = 4 \times 27 = 108$ days

**Solved independently** (answer withheld)

1. No external torque, so angular momentum is conserved: $I_1\omega_1 = I_2\omega_2$.
2. For a uniform sphere $I = \frac{2}{5}MR^2$, so $I \propto R^2$ at constant mass.
3. Since $\omega = \frac{2\pi}{T}$, conservation gives $\frac{I_1}{T_1} = \frac{I_2}{T_2}$, so $T_2 = T_1\frac{I_2}{I_1} = T_1\left(\frac{R_2}{R_1}\right)^2$.
4. $T_2 = 27 \times 2^2 = 108$ days, which is option $1$.

**Subtopic:** Conservation of Angular Momentum · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 14)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q028_44c025ef_12112026.png?v=44c025ef9a58)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q028_61fd2742_12112026.png?v=61fd27426412)

---

## Q29

Physics · Units and Measurements

A physical quantity $P$ is related to four observations $a$, $b$, $c$ and $d$ as follows: $P = a^3 b^2 / c\sqrt{d}$ The percentage errors of measurement in $a$, $b$, $c$ and $d$ are $1\%$, $3\%$, $2\%$, and $4\%$ respectively. The percentage error in the quantity $P$ is

- (1) $15\%$
- (2) $10\%$
- (3) $2\%$
- **(4)** $13\%$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Maximum $\%$ error in $P = \frac{\Delta P}{P} \times 100 = 3\left(\frac{\Delta a}{a} \times 100\right) + 2\left(\frac{\Delta b}{b} \times 100\right) + \left(\frac{\Delta c}{c} \times 100\right) + \frac{1}{2}\left(\frac{\Delta d}{d} \times 100\right)$
2. $= 3 \times (1) + 2 \times (3) + (2) + \frac{1}{2} \times (4)$
3. $= 13\%$

**Solved independently** (answer withheld)

1. For $P = \frac{a^3 b^2}{c\sqrt{d}}$, maximum relative error is $\frac{\Delta P}{P} = 3\frac{\Delta a}{a} + 2\frac{\Delta b}{b} + \frac{\Delta c}{c} + \frac{1}{2}\frac{\Delta d}{d}$.
2. $3 \times 1\% = 3\%$, $2 \times 3\% = 6\%$, $1 \times 2\% = 2\%$, $\frac{1}{2} \times 4\% = 2\%$.
3. $3\% + 6\% + 2\% + 2\% = 13\%$, which is option $4$.

**Subtopic:** Errors in Measurement · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q029_0b1198c0_12112026.png?v=0b1198c086bf)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q029_a8f7289f_12112026.png?v=a8f7289f260c)

---

## Q30

Physics · Capacitance

The plates of a parallel plate capacitor are separated by $d$. Two slabs of different dielectric constant $K_1$ and $K_2$ with thickness $\frac{3}{8}d$ and $\frac{d}{2}$, respectively are inserted in the capacitor. Due to this, the capacitance becomes two times larger than when there is nothing between the plates. If $K_1 = 1.25\,K_2$, the value of $K_1$ is:

- (1) $1.33$
- **(2)** $2.66$
- (3) $2.33$
- (4) $1.60$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Using $C_{eq} = \frac{\varepsilon_0 A}{\frac{t_1}{K_1} + \frac{t_2}{K_2} + \frac{t_3}{K_3}}$
2. here $C_0 = \frac{\varepsilon_0 A}{d}, t_1 = \frac{3d}{8}, t_2 = \frac{d}{2}, t_3 = \frac{d}{8}$
3. $K_1 = K_1,\ K_2 = \frac{K_1}{1.25}$ and $K_3 = 1$
4. Given $C_{eq} = 2C_0$
5. $\Rightarrow 2C_0 = \frac{\varepsilon_0 A}{\frac{3d}{8K_1} + \frac{d \times 1.25}{2K_1} + \frac{d}{8}}$
6. $\Rightarrow \frac{2\varepsilon_0 A}{d} = \frac{\varepsilon_0 A}{\frac{3d}{8K_1} + \frac{d}{2K_1} \times \frac{5}{4} + \frac{d}{8}}$
7. $\Rightarrow 2 = \frac{1}{\frac{3}{8K_1} + \frac{5}{8K_1} + \frac{1}{8}} \Rightarrow K_1 = \frac{8}{3} = 2.66$

**Solved independently** (answer withheld)

1. Remaining air gap: $d - \frac{3d}{8} - \frac{d}{2} = \frac{d}{8}$.
2. Layers are in series: $C = \frac{\varepsilon_0 A}{\frac{d}{8} + \frac{3d}{8K_1} + \frac{d}{2K_2}}$.
3. Set $C = 2C_0 = \frac{2\varepsilon_0 A}{d}$: $\frac{d}{8} + \frac{3d}{8K_1} + \frac{d}{2K_2} = \frac{d}{2}$, so $\frac{3}{8K_1} + \frac{1}{2K_2} = \frac{3}{8}$.
4. $K_2 = \frac{K_1}{1.25} = 0.8K_1$, so $\frac{1}{2K_2} = \frac{0.625}{K_1}$.
5. $\frac{0.375}{K_1} + \frac{0.625}{K_1} = \frac{1}{K_1} = \frac{3}{8}$.
6. $K_1 = \frac{8}{3} \approx 2.66$, which is option $2$.

**Subtopic:** Effect of Dielectric on Capacitance · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q030_dded5e94_12112026.png?v=dded5e942abc)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q030_5dc91b91_12112026.png?v=5dc91b9134d7)

---

## Q31

Physics · Laws of Motion

A ball of mass $0.5\,\mathrm{kg}$ is dropped from a height of $40\,\mathrm{m}$. The ball hits the ground and rises to a height of $10\,\mathrm{m}$. The impulse imparted to the ball during its collision with the ground is (Take $g = 9.8\,\mathrm{m/s^2}$)

- (1) $84\,\mathrm{NS}$
- **(2)** $21\,\mathrm{NS}$
- (3) $7\,\mathrm{NS}$
- (4) $0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $v_1 = \sqrt{2gh_1}$
2. $= \sqrt{2 \times 9.8 \times 40}$
3. $v_1 = \sqrt{784} = 28\,\mathrm{m\,s^{-1}}$
4. and $v_2 = \sqrt{2gh_2} = \sqrt{2 \times 9.8 \times 10}$
5. $= \sqrt{196} = 14\,\mathrm{m\,s^{-1}}$
6. Impulse $= \Delta\vec{p} = m(\vec{v}_f - \vec{v}_i) = m(\vec{v}_2 - \vec{v}_1)$
7. $= \frac{1}{2}(14 - (-28))$
8. $= 21\,\mathrm{NS}$

**Solved independently** (answer withheld)

1. Speed just before impact: $v_1 = \sqrt{2gh_1} = \sqrt{2 \times 9.8 \times 40} = \sqrt{784} = 28\,\mathrm{m/s}$ downward.
2. Speed just after impact: $v_2 = \sqrt{2gh_2} = \sqrt{2 \times 9.8 \times 10} = \sqrt{196} = 14\,\mathrm{m/s}$ upward.
3. Velocity reverses direction, so impulse magnitude $J = m(v_2 + v_1)$.
4. $J = 0.5 \times (14 + 28) = 21\,\mathrm{N\,s}$, which is option $2$.

**Subtopic:** Impulse–Momentum Theorem · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q031_783e740d_12112026.png?v=783e740d002c)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q031_7c9c115f_12112026.png?v=7c9c115f9074)

---

## Q32

Physics · Kinematics

Two cities $X$ and $Y$ are connected by a regular bus service with a bus leaving in either direction every $T$ min. A girl is driving scooty with a speed of $60\,\mathrm{km/h}$ in the direction $X$ to $Y$ notices that a bus goes past her every $30$ minutes in the direction of her motion, and every $10$ minutes in the opposite direction. Choose the correct option for the period $T$ of the bus service and the speed (assumed constant) of the buses.

- **(1)** $15\,\mathrm{min}$, $120\,\mathrm{km/h}$
- (2) $9\,\mathrm{min}$, $40\,\mathrm{km/h}$
- (3) $25\,\mathrm{min}$, $100\,\mathrm{km/h}$
- (4) $10\,\mathrm{min}$, $90\,\mathrm{km/h}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $X \rightarrow Y$
2. Let velocity of bus $= v\,\mathrm{km/hr}$
3. Relative velocity of bus w.r.t. scooty $= (v - 60)$
4. Distance between 2 consecutive buses $= vT$
5. $(v - 60)30 = vT$ ...(i)
6. $Y \rightarrow X$
7. $(v + 60)10 = vT$ ...(ii)
8. Equating (1) and (2)
9. $(v - 60)30 = (v + 60)10$
10. $\therefore\ v = 120\,\mathrm{km/hr}$
11. $T = 15\,\mathrm{min}$

**Solved independently** (answer withheld)

1. Buses leave every $T$, so the spacing between buses moving the same way is $d = vT$.
2. Buses going the same way overtake her at relative speed $v-60$: $d = (v-60)\times\frac{1}{2}$.
3. Buses coming the other way meet her at relative speed $v+60$: $d = (v+60)\times\frac{1}{6}$.
4. Equating: $3(v-60) = v+60 \Rightarrow v = 120\,\mathrm{km/h}$.
5. $d = (120-60)\times\frac{1}{2} = 30\,\mathrm{km}$.
6. $T = \frac{d}{v} = \frac{30}{120}\,\mathrm{h} = 15\,\mathrm{min}$, which is option $1$.

**Subtopic:** Relative Motion in 1D · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 16)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q032_30552141_12112026.png?v=305521418c1f)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q032_617a531d_12112026.png?v=617a531d6a00)

---

## Q33

Physics · Thermodynamics

An oxygen cylinder of volume $30$ litre has $18.20$ moles of oxygen. After some oxygen is withdrawn from the cylinder, its gauge pressure drops to $11$ atmospheric pressures at temperature $27^\circ\mathrm{C}$. The mass of the oxygen withdrawn from the cylinder is nearly equal to:
[Given, $R = \frac{100}{12}\,\mathrm{J\,mol^{-1}\,K^{-1}}$, and molecular mass of $\mathrm{O_2} = 32$, $1\,\mathrm{atm}$ pressure $= 1.01 \times 10^{5}\,\mathrm{N/m}$]

- (1) $0.156\,\mathrm{kg}$
- (2) $0.125\,\mathrm{kg}$
- (3) $0.144\,\mathrm{kg}$
- **(4)** $0.116\,\mathrm{kg}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Number of moles left
2. $n = \frac{PV}{RT} = \frac{12 \times 1.01 \times 10^{5}\,\mathrm{N/m^{2}} \times 30 \times 10^{-3}\,\mathrm{m^{3}}}{\frac{100}{12} \times 300}$
3. $n = \frac{12 \times 1.01 \times 12}{10} = 14.54$ moles
4. Moles removed $= 18.2 - 14.54$
5. $= 3.656$ moles
6. Mass removed $= 3.656 \times 32 = 116.99\,\mathrm{g} = 0.116\,\mathrm{kg}$

**Solved independently** (answer withheld)

1. Gauge pressure excludes atmospheric pressure, so $P_{abs} = 11 + 1 = 12\,\mathrm{atm}$.
2. $P_{abs} = 12 \times 1.01 \times 10^{5} = 1.212 \times 10^{6}\,\mathrm{Pa}$, and $V = 30\,\mathrm{L} = 0.030\,\mathrm{m^3}$, $T = 300\,\mathrm{K}$.
3. $n_{left} = \frac{PV}{RT} = \frac{1.212 \times 10^{6} \times 0.030}{\frac{100}{12} \times 300} = \frac{36360}{2500} = 14.544\,\mathrm{mol}$.
4. $n_{withdrawn} = 18.20 - 14.544 = 3.656\,\mathrm{mol}$.
5. $m = 3.656 \times 32\,\mathrm{g} \approx 117\,\mathrm{g} \approx 0.116\,\mathrm{kg}$, which is option $4$.

**Subtopic:** Ideal Gas Equation · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 16)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q033_7a1f6ca5_12112026.png?v=7a1f6ca53105)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q033_222e7422_12112026.png?v=222e7422496d)

---

## Q34

Physics · Electromagnetic Induction

$AB$ is a part of an electrical circuit (see figure). The potential difference “$V_A - V_B$”, at the instant when current $i = 2\,\mathrm{A}$ and is increasing at a rate of $1\,\mathrm{amp/second}$ is:

![printed figure: Circuit segment AB: inductor 1 H, cell 5 V and resistor 2 ohm in series, current i from A](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q034_9fe5a93d_12112026.png?v=9fe5a93dbf83)

*Circuit segment AB: inductor 1 H, cell 5 V and resistor 2 ohm in series, current i from A*

- **(1)** $10\,\mathrm{volt}$
- (2) $5\,\mathrm{volt}$
- (3) $6\,\mathrm{volt}$
- (4) $9\,\mathrm{volt}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Given, $I = 2\,\mathrm{A}$ and $\frac{di}{dt} = +1\,\mathrm{A/s}$
2. $V_A - L\frac{di}{dt} - 5 - i \times 2 = V_B$
3. $\Rightarrow V_A - 1 \times 1 - 5 - 2 \times 2 = V_B$
4. $\Rightarrow V_A - V_B = 10\,\mathrm{volt}$

**Solved independently** (answer withheld)

1. Across the inductor in the direction of current: drop $L\frac{di}{dt} = 1\,\mathrm{H} \times 1\,\mathrm{A/s} = 1\,\mathrm{V}$.
2. The battery's longer (positive) plate faces $A$, so going from $A$ towards $B$ the potential falls by $5\,\mathrm{V}$.
3. Across the resistor: drop $iR = 2\,\mathrm{A} \times 2\,\Omega = 4\,\mathrm{V}$.
4. $V_A - V_B = 1 + 5 + 4 = 10\,\mathrm{V}$, which is option $1$.

**Subtopic:** Self Induction · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 17)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q034_4d788d93_12112026.png?v=4d788d931814)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q034_c9e04239_12112026.png?v=c9e04239b19c)

---

## Q35

Physics · Oscillations

In an oscillating spring mass system, a spring is connected to a box filled with sand. As the box oscillates, sand leaks slowly out of the box vertically so that the average frequency $\omega(t)$ and average amplitude $A(t)$ of the system change with time $t$. Which one of the following options schematically depicts these changes correctly?

- (1) ![printed figure: Option (1): omega(t) and A(t) both decrease with time t](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q035_option_1_16673fdf_12112026.png?v=16673fdfb3ce) *Option (1): omega(t) and A(t) both decrease with time t*
- (2) ![printed figure: Option (2): omega(t) rises and levels off, A(t) stays constant](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q035_option_2_2ac0b42f_12112026.png?v=2ac0b42f84b5) *Option (2): omega(t) rises and levels off, A(t) stays constant*
- **(3)** ![printed figure: Option (3): omega(t) rises and levels off; A(t) falls and levels off](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q035_option_3_428bbe72_12112026.png?v=428bbe72dc95) *Option (3): omega(t) rises and levels off; A(t) falls and levels off*
- (4) ![printed figure: Option 4: omega(t) and A(t) both rise with t and level off](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q035_option_4_a964753a_12112026.png?v=a964753ab40e) *Option 4: omega(t) and A(t) both rise with t and level off*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. At any point of time, time period is given by
2. $T = 2\pi\sqrt{\frac{m}{k}}$
3. Here $m$ is decreasing, so time period $T$ will be decreasing
4. Since $\omega = \frac{2\pi}{T}$
5. Hence as mass leaks, $\omega$ will increase
6. Now, at any instant
7. $mg = kx_0$
8. So, equilibrium length $x_0 = \frac{mg}{k}$, where $m$ is decreasing
9. So, equilibrium length will decrease.
10. So, amplitude also go on decreasing.

**Solved independently** (answer withheld)

1. The angular frequency is $\omega = \sqrt{\frac{k}{m}}$.
2. Sand leaks out, so $m$ decreases with time and $\omega(t)$ increases.
3. Sand leaves vertically relative to the box, so it carries the box's horizontal velocity $v$; the box's own velocity is unchanged at that instant.
4. The leaking sand carries away kinetic energy $\frac{1}{2}\Delta m\, v^2$, so the oscillator energy $E = \frac{1}{2}kA^2$ decreases on average.
5. Hence $A(t)$ decreases while $\omega(t)$ increases, which is option $3$.

**Subtopic:** Calculate Angular Frequency of SHM, Calculate Amplitude of SHM · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 17)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q035_fca1fa73_12112026.png?v=fca1fa73996a)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q035_1b1052b1_12112026.png?v=1b1052b12acc)

---

## Q36

Physics · Magnetic Effect of Electric Current

A model for quantized motion of an electron in a uniform magnetic field $B$ states that the flux passing through the orbit of the electron is $n(hle)$ where $n$ is an integer, $h$ is Planck's constant and $e$ is the magnitude of electron's charge. According to the model, the magnetic moment of an electron in its lowest energy state will be ($m$ is the mass of the electron)

- (1) $\frac{heB}{2\pi m}$
- (2) $\frac{he}{\pi m}$
- **(3)** $\frac{he}{2\pi m}$
- (4) $\frac{heB}{\pi m}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Magnetic force $= \frac{mv^{2}}{r}$
2. $evB = \frac{mv^{2}}{r}$
3. $v = \frac{eBr}{m}$
4. $\phi = BA$
5. $\frac{nh}{e} = B\pi r^{2}$
6. $Br^{2} = \frac{nh}{e\pi}$
7. $\mu = IA$
8. $= \frac{e}{T}\pi r^{2}$
9. $= \frac{e \times v}{2\pi r}\pi r^{2}$
10. $\mu = \frac{evr}{2}$
11. $= \frac{1}{2}e \times \frac{eBr}{m}r$
12. $\mu = \frac{1}{2}e^{2}\frac{Br^{2}}{m}$
13. $\mu = \frac{1}{2}e^{2}\frac{nh}{e\pi m}$
14. $\mu = \frac{neh}{2\pi m}$
15. for $n = 1$
16. $\mu = \frac{eh}{2\pi m}$

**Solved independently** (answer withheld)

1. Lowest energy state means $n = 1$, so $B\pi r^2 = \frac{h}{e}$.
2. $r^2 = \frac{h}{\pi e B}$.
3. Circular motion in the field: $\frac{mv^2}{r} = evB \Rightarrow v = \frac{eBr}{m}$.
4. Current of the orbit: $I = \frac{e v}{2\pi r}$.
5. Magnetic moment: $\mu = I \pi r^2 = \frac{e v r}{2}$.
6. Substitute $v$: $\mu = \frac{e^2 B r^2}{2m}$.
7. Substitute $r^2$: $\mu = \frac{e^2 B}{2m}\cdot\frac{h}{\pi e B} = \frac{he}{2\pi m}$, which is option $3$.

**Subtopic:** Magnetic Dipole Moment of a Revolving Electron, Motion in a Magnetic Field · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 18)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q036_47d71d1a_12112026.png?v=47d71d1a17f5)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q036_e7879c30_12112026.png?v=e7879c30f87b)

---

## Q37

Physics · Gravitation

A body weighs $48\,\mathrm{N}$ on the surface of the earth. The gravitational force experienced by the body due to the earth at a height equal to one-third the radius of the earth from its surface is :

- (1) $36\,\mathrm{N}$
- (2) $16\,\mathrm{N}$
- **(3)** $27\,\mathrm{N}$
- (4) $32\,\mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $W = mg$ and $g = \frac{GM}{R^2}$, $g_h = \frac{GM}{(R+h)^2}$
2. $\Rightarrow \frac{W_h}{W} = \frac{mg_h}{mg} = \frac{g_h}{g} = \frac{R^2}{(R+h)^2}$ $\left(h = \frac{R}{3}\right)$
3. $\Rightarrow \frac{W_h}{W} = \frac{R^2}{\left(R + \frac{R}{3}\right)^2} = \frac{R^2}{\left(\frac{4R}{3}\right)^2} = \frac{9}{16}$
4. $\Rightarrow W_h = \frac{9}{16}W = \frac{9}{16} \times 48$ $[W = 48\,\mathrm{N}]$
5. $= 27\,\mathrm{N}$

**Solved independently** (answer withheld)

1. Gravitational force varies as $F \propto \frac{1}{r^2}$, where $r$ is the distance from the earth's centre.
2. At height $h = \frac{R}{3}$, $r = R + \frac{R}{3} = \frac{4R}{3}$.
3. $F' = F\left(\frac{R}{4R/3}\right)^2 = 48 \times \left(\frac{3}{4}\right)^2 = 48 \times \frac{9}{16}$.
4. $F' = 27\,\mathrm{N}$, which is option $3$.

**Subtopic:** Variation in g Due to Height and Rotation · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 19)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q037_c614b25c_12112026.png?v=c614b25c23a2)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q037_bbe13c7c_12112026.png?v=bbe13c7c35a5)

---

## Q38

Physics · Mechanical Properties of Fluids

Consider a water tank shown in the figure. It has one wall at $x = L$ and can be taken to be very wide in the $z$ direction. When filled with a liquid of surface tension $S$ and density $\rho$, the liquid surface makes angle $\theta_0$ ($\theta_0 << 1$) with the $x$-axis at $x = L$. If $y(x)$ is the height of the surface then the equation for $y(x)$ is: (take $\theta(x) = \sin\theta(x) = \tan\theta(x) = \frac{dy}{dx}$, $g$ is the acceleration due to gravity)

![printed figure: Liquid surface y(x) in a tank rising to meet the wall at x = L at angle θ0 with the horizontal](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q038_7955217d_12112026.png?v=7955217dc2dd)

*Liquid surface y(x) in a tank rising to meet the wall at x = L at angle θ0 with the horizontal*

- (1) $\frac{dy}{dx} = \sqrt{\frac{\rho g}{S}}\,x$
- (2) $\frac{d^2y}{dx^2} = \frac{\rho g}{S}\,x$
- **(3)** $\frac{d^2y}{dx^2} = \frac{\rho g}{S}\,y$
- (4) $\frac{d^2y}{dx^2} = \sqrt{\frac{\rho g}{S}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $ROC$ = Radius of curvature at point $A$
2. Curvature $= \frac{1}{ROC} = \frac{\left|\frac{d^2y}{dx^2}\right|}{\left(1+\left(\frac{dy}{dx}\right)^2\right)^{\frac{3}{2}}} = \frac{\left|\frac{d^2y}{dx^2}\right|}{(1+0)^{\frac{3}{2}}} = \frac{d^2y}{dx^2}$ $\left[\because \frac{dy}{dx} = \tan\theta \simeq 0\right]$
3. $\Delta P = S \times$ curvature
4. $\Rightarrow \rho g y = S\frac{d^2y}{dx^2}$
5. $\therefore \frac{d^2y}{dx^2} = \frac{\rho g y}{S}$

**Solved independently** (answer withheld)

1. Take a thin strip of the surface between $x$ and $x+dx$, unit width in $z$.
2. Net vertical surface-tension force on the strip: $S[\sin\theta(x+dx) - \sin\theta(x)] = S\frac{d\theta}{dx}dx = S\frac{d^2y}{dx^2}dx$, using $\sin\theta = \frac{dy}{dx}$.
3. The pressure difference across the surface at height $y$ (measured from the flat level) is hydrostatic: $\Delta P = \rho g y$, giving force $\rho g y\,dx$.
4. Equating: $S\frac{d^2y}{dx^2} = \rho g y \Rightarrow \frac{d^2y}{dx^2} = \frac{\rho g}{S}y$, which is option $3$.

**Subtopic:** Excess Pressure on Curved Surface (General Case, Drop, Soap Bubbles, Air Bubbles), Surface Tension and Surface Energy · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 19)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q038_0a5f34d8_12112026.png?v=0a5f34d83655)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q038_5e2558ca_12112026.png?v=5e2558ca3b9e)

---

## Q39

Physics · Wave Optics

The intensity of transmitted light when a polaroid sheet, placed between two crossed polaroids at $22.5^{\circ}$ from the polarization axis of one of the polaroids, is ($I_0$ is the intensity of polarised light after passing through the first polaroid):

- (1) $\frac{I_0}{16}$
- (2) $\frac{I_0}{2}$
- (3) $\frac{I_0}{4}$
- **(4)** $\frac{I_0}{8}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $I_1 = I_0 \cos^2\left(\frac{45}{2}\right)$
2. $I_2 = I_1 \cos^2\left(90 - \frac{45}{2}\right)$
3. $= I_0 \cos^2\left(\frac{45}{2}\right)\sin^2\left(\frac{45}{2}\right)$
4. $= \frac{I_0}{4}\left(4\cos^2\left(\frac{45}{2}\right)\sin^2\left(\frac{45}{2}\right)\right)$
5. $= \frac{I_0}{4}\sin^2 45^{\circ} = \frac{I_0}{8}$

**Solved independently** (answer withheld)

1. Crossed polaroids are at $90^{\circ}$, so the middle sheet makes $22.5^{\circ}$ with the first and $90^{\circ} - 22.5^{\circ} = 67.5^{\circ}$ with the second.
2. After the middle sheet, by Malus's law: $I_1 = I_0 \cos^2 22.5^{\circ}$.
3. After the second crossed polaroid: $I = I_1 \cos^2 67.5^{\circ} = I_0 \cos^2 22.5^{\circ} \sin^2 22.5^{\circ}$.
4. $\cos\theta \sin\theta = \frac{1}{2}\sin 2\theta$, so $I = \frac{I_0}{4}\sin^2 45^{\circ}$.
5. $I = \frac{I_0}{4} \times \frac{1}{2} = \frac{I_0}{8}$, which is option $4$.

**Subtopic:** Polaroids · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 20)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q039_0e42c748_12112026.png?v=0e42c7485794)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q039_1223a0df_12112026.png?v=1223a0dfb906)

---

## Q40

Physics · Modern Physics

A photon and an electron (mass $m$) have the same energy $E$. The ratio $(\lambda_{\mathrm{photon}}/\lambda_{\mathrm{electron}})$ of their de Broglie wavelengths is: ($c$ is the speed of light)

- (1) $\frac{1}{c}\sqrt{E/2m}$
- (2) $\sqrt{E/2m}$
- (3) $c\sqrt{2mE}$
- **(4)** $c\sqrt{\frac{2m}{E}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For photon, $E = \frac{hc}{\lambda_{\mathrm{Ph}}} \Rightarrow \lambda_{\mathrm{Ph}} = \frac{hc}{E}$
2. For electron, $p$ = momentum and $E = \frac{p^{2}}{2m} = \left(\frac{h}{\lambda_{e}}\right)^{2} \times \frac{1}{2m}$
3. $\Rightarrow \lambda_{e} = \frac{h}{\sqrt{2mE}}$
4. $\therefore \frac{\lambda_{\mathrm{Ph}}}{\lambda_{e}} = \frac{\frac{hc}{E}}{\frac{h}{\sqrt{2mE}}} = c\sqrt{\frac{2m}{E}}$

**Solved independently** (answer withheld)

1. For the photon, $E = \frac{hc}{\lambda_p}$, so $\lambda_p = \frac{hc}{E}$.
2. For the electron (non-relativistic), $p = \sqrt{2mE}$, so $\lambda_e = \frac{h}{\sqrt{2mE}}$.
3. $\frac{\lambda_p}{\lambda_e} = \frac{hc}{E} \cdot \frac{\sqrt{2mE}}{h} = \frac{c\sqrt{2mE}}{E}$.
4. $\frac{c\sqrt{2mE}}{E} = c\sqrt{\frac{2m}{E}}$, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q040_d9ac86d2_12112026.png?v=d9ac86d2a48d)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q040_9147b9b4_12112026.png?v=9147b9b423b4)

---

## Q41

Physics · Wave Optics

An unpolarized light beam travelling in air is incident on a medium of refractive index $1.73$ at Brewster’s angle. Then

- (1) Transmitted light is completely polarized with angle of refraction close to $30^\circ$
- **(2)** Reflected light is completely polarized and the angle of reflection is close to $60^\circ$
- (3) Reflected light is partially polarized and the angle of reflection is close to $30^\circ$
- (4) Both reflected and transmitted light are perfectly polarized with angles of reflection and refraction close to $60^\circ$ and $30^\circ$, respectively

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Using Brewster law
2. $\mu = \tan\theta_P$
3. $\Rightarrow 1.73 = \tan\theta_P$
4. $\Rightarrow \sqrt{3} = \tan\theta_P$
5. $\Rightarrow \theta_P = 60^\circ$
6. At this polarising angle, reflected light is perfectly polarized and transmitted light is partially polarised.

**Solved independently** (answer withheld)

1. Brewster's law: $\tan i_B = \mu = 1.73 \approx \sqrt{3}$.
2. $i_B = \tan^{-1}\sqrt{3} = 60^\circ$, so the angle of reflection is $60^\circ$.
3. At Brewster's angle the reflected and refracted rays are perpendicular, so $r = 90^\circ - 60^\circ = 30^\circ$.
4. The reflected light is completely (plane) polarized, while the transmitted light is only partially polarized, so options $1$, $3$ and $4$ fail.
5. Reflected light completely polarized with angle of reflection $60^\circ$ is option $2$.

**Subtopic:** Brewster's Law, Polarization by Reflection and Refraction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q041_79d5ef1b_12112026.png?v=79d5ef1ba2a8)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q041_b1b26e96_12112026.png?v=b1b26e9625d8)

---

## Q42

Physics · Rotational Motion

A uniform rod of mass $20\,\mathrm{kg}$ and length $5\,\mathrm{m}$ leans against a smooth vertical wall making an angle of $60^\circ$ with it. The other end rests on a rough horizontal floor. The friction force that the floor exerts on the rod is (Take $g = 10\,\mathrm{m/s^2}$)

- (1) $200\sqrt{3}\,\mathrm{N}$
- (2) $100\,\mathrm{N}$
- **(3)** $100\sqrt{3}\,\mathrm{N}$
- (4) $200\,\mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For translational equilibrium
2. $N_1 = Mg$
3. $N_2 = f$
4. For rotational equilibrium
5. Torque about $A$, $Mg\frac{L}{2}\cos\theta = N_2 L\sin\theta$
6. $\frac{Mg}{2}\cot\theta = N_2 = f$
7. $\frac{Mg}{2}\cot 30^\circ = f$
8. $\frac{Mg}{2}\sqrt{3} = N_2$
9. $100\sqrt{3} = f$

**Solved independently** (answer withheld)

1. The rod makes $\theta = 60^\circ$ with the vertical wall; the wall is smooth, so it exerts only a horizontal normal force $N_w$ at the top.
2. Horizontal equilibrium: the floor friction $f = N_w$.
3. Torque about the floor contact: $N_w \, L\cos 60^\circ = mg \, \frac{L}{2}\sin 60^\circ$.
4. $N_w = \frac{mg}{2}\tan 60^\circ = \frac{20 \times 10}{2}\sqrt{3} = 100\sqrt{3}\,\mathrm{N}$.
5. $f = 100\sqrt{3}\,\mathrm{N}$, which is option $3$.

**Subtopic:** Equilibrium of a Rigid Body · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 21)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q042_63f231c3_12112026.png?v=63f231c39d63)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q042_a4426f43_12112026.png?v=a4426f43f207)

---

## Q43

Physics · Thermal Properties of Matter

Three identical heat conducting rods are connected in series as shown in the figure. The rods on the sides have thermal conductivity $2K$ while that in the middle has thermal conductivity $K$. The left end of the combination is maintained at temperature $3T$ and the right end at $T$. The rods are thermally insulated from outside. In steady state, temperature at the left junction is $T_1$ and that at the right junction is $T_2$. The ratio $T_1/T_2$ is

![printed figure: Three equal rods 2K, K, 2K in series between walls at 3T and T, junctions T1 and T2](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q043_3abb92fd_12112026.png?v=3abb92fde3a5)

*Three equal rods 2K, K, 2K in series between walls at 3T and T, junctions T1 and T2*

- (1) $\frac{5}{4}$
- (2) $\frac{3}{2}$
- (3) $\frac{4}{3}$
- **(4)** $\frac{5}{3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In series, $R_{\mathrm{eq.}} = R_1 + R_2 + R_3$
2. $= \frac{l}{2KA} + \frac{l}{KA} + \frac{l}{2KA}$
3. $= \frac{4l}{2KA}$
4. $R_{\mathrm{eq.}} = \frac{2l}{KA}$
5. In series rate of heat flow is same
6. $\therefore \frac{3T - T_1}{R_1} = \frac{3T - T}{R_{\mathrm{eq.}}}$
7. $\frac{(3T - T_1)2KA}{l} = \frac{(2T)KA}{2l}$
8. $\Rightarrow 6T - 2T_1 = T$
9. $\Rightarrow 2T_1 = 5T$
10. $\Rightarrow T_1 = \frac{5T}{2}$ ...(1)
11. Now, equate heat flow rate in $3^{\mathrm{rd}}$ section & total section
12. $\frac{T_2 - T}{R_3} = \frac{3T - T}{R_{\mathrm{eq.}}}$
13. $\Rightarrow \frac{(T_2 - T)(2KA)}{l} = \frac{2T(KA)}{2l}$
14. $\Rightarrow 2T_2 - 2T = T$
15. $\Rightarrow T_2 = \frac{3T}{2}$ ...(2)
16. By equation (1) and equation (2)
17. $\frac{T_1}{T_2} = \frac{5T \times 2}{2 \times 3T} = \frac{5}{3}$

**Solved independently** (answer withheld)

1. Thermal resistance of a rod is $R_{th} = \frac{L}{kA}$, so with $R = \frac{L}{KA}$ the side rods have $\frac{L}{2KA} = \frac{R}{2}$ and the middle rod has $R$.
2. Total series resistance $R_{tot} = \frac{R}{2} + R + \frac{R}{2} = 2R$.
3. Heat current $H = \frac{3T - T}{2R} = \frac{T}{R}$.
4. $T_1 = 3T - H\cdot\frac{R}{2} = 3T - \frac{T}{2} = \frac{5T}{2}$.
5. $T_2 = T + H\cdot\frac{R}{2} = T + \frac{T}{2} = \frac{3T}{2}$.
6. $\frac{T_1}{T_2} = \frac{5T/2}{3T/2} = \frac{5}{3}$, which is option $4$.

**Subtopic:** Connection of Rods · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q043_f05d2d9c_12112026.png?v=f05d2d9cb7a2)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q043_6179c148_12112026.png?v=6179c148c8cf)

---

## Q44

Physics · Work, Energy and Power

The kinetic energies of two similar cars $A$ and $B$ are $100\,\mathrm{J}$ and $225\,\mathrm{J}$ respectively. On applying breaks, car $A$ stops after $1000\,\mathrm{m}$ and car $B$ stops after $1500\,\mathrm{m}$. If $F_A$ and $F_B$ are the forces applied by the breaks on cars $A$ and $B$ respectively, then the ratio of $\frac{F_A}{F_B}$ is

- (1) $\frac{1}{2}$
- (2) $\frac{3}{2}$
- **(3)** $\frac{2}{3}$
- (4) $\frac{1}{3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. By work-energy theorem,
2. $FS = \Delta K \cdot E$
3. $\Rightarrow -FS = k_f - k_i$
4. $\Rightarrow FS = k_i - k_f$
5. $\Rightarrow \frac{F_A}{F_B} = \frac{k_A}{k_B} \times \frac{S_B}{S_A}$
6. $= \frac{100}{225} \times \frac{1500}{1000}$
7. $= \frac{150}{225} = \frac{2}{3}$

**Solved independently** (answer withheld)

1. By the work-energy theorem the braking work equals the kinetic energy lost: $F d = K$, so $F = \frac{K}{d}$.
2. $F_A = \frac{100\,\mathrm{J}}{1000\,\mathrm{m}} = 0.1\,\mathrm{N}$.
3. $F_B = \frac{225\,\mathrm{J}}{1500\,\mathrm{m}} = 0.15\,\mathrm{N}$.
4. $\frac{F_A}{F_B} = \frac{0.1}{0.15} = \frac{2}{3}$, which is option $3$.

**Subtopic:** Work–Energy Theorem · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q044_3f0de4f6_12112026.png?v=3f0de4f64f41)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q044_44ac2689_12112026.png?v=44ac268968da)

---

## Q45

Physics · Rotational Motion

A sphere of radius $R$ is cut from a larger solid sphere of radius $2R$ as shown in the figure. The ratio of the moment of inertia of the smaller sphere to that of the rest part of the sphere about the $Y$-axis is:

![printed figure: A solid sphere of radius 2R with a sphere of radius R cut out, touching its rim on the X-axis](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q045_9e735597_12112026.png?v=9e7355975ad2)

*A solid sphere of radius 2R with a sphere of radius R cut out, touching its rim on the X-axis*

- (1) $\frac{7}{64}$
- (2) $\frac{7}{8}$
- (3) $\frac{7}{40}$
- **(4)** $\frac{7}{57}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For larger solid sphere about diameter $Y$-axis,
2. $I_{\mathrm{whole}} = \frac{2}{5}M(2R)^{2} = \frac{8}{5}MR^{2}$
3. Density of sphere is uniform
4. $\Rightarrow \frac{M}{V_{\mathrm{whole}}} = \frac{M_{\mathrm{smaller}}}{V_{\mathrm{smaller}}} \Rightarrow \frac{M}{\frac{4}{3}\pi(2R)^{3}} = \frac{M'}{\frac{4}{3}\pi R^{3}}$
5. $\Rightarrow M' = \frac{M}{8}$
6. Using parallel axis theorem for smaller sphere,
7. $I' = I_{\mathrm{cm}} + M'R^{2} = \frac{2}{5}\frac{MR^{2}}{8} + \frac{MR^{2}}{8} = \frac{7}{40}MR^{2}$
8. $\therefore\ \text{Ratio} = \frac{I_{\mathrm{smaller}}}{I_{\mathrm{remaining}}} = \frac{I'}{I_{\mathrm{whole}} - I'} = \frac{\frac{7}{40}MR^{2}}{\left(\frac{8}{5} - \frac{7}{40}\right)MR^{2}} = \frac{7}{64 - 7} = \frac{7}{57}$

**Solved independently** (answer withheld)

1. Mass scales as $r^3$, so if the small sphere has mass $m$, the full sphere of radius $2R$ has mass $8m$.
2. $I_{full} = \frac{2}{5}(8m)(2R)^2 = \frac{64}{5}mR^2$ about the Y-axis through its centre.
3. From the figure the small sphere's centre is at distance $R$ from the Y-axis, so by the parallel axis theorem $I_{small} = \frac{2}{5}mR^2 + mR^2 = \frac{7}{5}mR^2$.
4. $I_{rest} = I_{full} - I_{small} = \frac{64}{5}mR^2 - \frac{7}{5}mR^2 = \frac{57}{5}mR^2$.
5. $\frac{I_{small}}{I_{rest}} = \frac{7}{57}$, which is option $4$.

**Subtopic:** Moment of Inertia of a Sphere, Parallel Axis and Perpendicular Axis Theorem · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 24)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q045_47dd1864_12112026.png?v=47dd18648521)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q045_3a81d3b9_12112026.png?v=3a81d3b96d51)

---

## Q46

Chemistry · physical · Electrochemistry

If the molar conductivity ($\Lambda_\mathrm{m}$) of a $0.050\,\mathrm{mol\,L^{-1}}$ solution of a monobasic weak acid is $90\,\mathrm{S\,cm^{2}\,mol^{-1}}$, its extent (degree) of dissociation will be [Assume $\Lambda_{+}^{\circ} = 349.6\,\mathrm{S\,cm^{2}\,mol^{-1}}$ and $\Lambda_{-}^{\circ} = 50.4\,\mathrm{S\,cm^{2}\,mol^{-1}}$.]

- (1) $0.215$
- (2) $0.115$
- (3) $0.125$
- **(4)** $0.225$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Degree of dissociation ($\alpha$) is given as
2. $\alpha = \frac{\Lambda_\mathrm{m}}{\Lambda_\mathrm{m}^{\circ}}$
3. $\Lambda_\mathrm{m}^{\circ} = \Lambda_{+}^{\circ} + \Lambda_{-}^{\circ}$
4. $= 349.6 + 50.4$
5. $= 400\,\mathrm{S\,cm^{2}\,mol^{-1}}$
6. $\alpha = \frac{\Lambda_\mathrm{m}}{\Lambda_\mathrm{m}^{\circ}} = \frac{90}{400} = 0.225$

**Solved independently** (answer withheld)

1. By Kohlrausch's law, $\Lambda_\mathrm{m}^{\circ} = \Lambda_{+}^{\circ} + \Lambda_{-}^{\circ} = 349.6 + 50.4 = 400\,\mathrm{S\,cm^{2}\,mol^{-1}}$.
2. Degree of dissociation $\alpha = \frac{\Lambda_\mathrm{m}}{\Lambda_\mathrm{m}^{\circ}} = \frac{90}{400}$.
3. $\alpha = 0.225$, which is option $4$.

**Subtopic:** Applications of Kohlrausch Law · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 25)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q046_2b7c12ce_12112026.png?v=2b7c12ce65dc)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q046_f804a0fd_12112026.png?v=f804a0fd9c5f)

---

## Q47

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) A hypothetical diatomic molecule with bond order zero is quite stable.
- (Statement II) As bond order increases, the bond length increases.

- (1) Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- **(3)** Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A positive bond order means a stable molecule while a negative or zero bond order means an unstable molecule.
2. When  bond order increases, the bond length decreases.

**Solved independently** (answer withheld)

1. A bond order of $0$ means $N_b = N_a$, so there is no net bonding and the molecule is not stable; Statement I is false.
2. Bond length is inversely related to bond order ($\text{bond length} \propto \frac{1}{\text{bond order}}$), so it decreases as bond order increases; Statement II is false.
3. Both statements are false, which is option $3$.

**Subtopic:** Molecular Orbital Theory, Bond Parameters · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q047_b59b9913_12112026.png?v=b59b9913f7c9)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q047_7b92f1e4_12112026.png?v=7b92f1e421fe)

---

## Q48

Chemistry · physical · Structure of Atom

The ratio of the wavelengths of the light absorbed by a Hydrogen atom when it undergoes $n = 2 \rightarrow n = 3$ and $n = 4 \rightarrow n = 6$ transitions, respectively, is

- **(1)** $\frac{1}{4}$
- (2) $\frac{1}{36}$
- (3) $\frac{1}{16}$
- (4) $\frac{1}{9}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\Delta E = \frac{hc}{\lambda} = E_{\mathrm{final}} - E_{\mathrm{initial}}$ $\left(E_n = \frac{-R_H}{n^2}\right)$
2. $\Delta E_{2\rightarrow 3} = \frac{hc}{\lambda_{2\rightarrow 3}} = E_3 - E_2 = \frac{-R_H}{3^2} - \left(\frac{-R_H}{2^2}\right)$
3. $= R_H\left(\frac{1}{4} - \frac{1}{9}\right)$
4. $= R_H \times \frac{5}{36}$
5. $\therefore \lambda_{2\rightarrow 3} = \frac{hc \cdot 36}{R_H \cdot 5}$
6. $\Delta E_{4\rightarrow 6} = E_6 - E_4 = \frac{-R_H}{36} + \frac{R_H}{16} = \frac{R_H \times 20}{36 \times 16}$
7. $\frac{hc}{\lambda_{4\rightarrow 6}} = \frac{R_H \times 20}{36 \times 16}$
8. $\lambda_{4\rightarrow 6} = \frac{hc \times 36 \times 16}{R_H \cdot 20}$
9. $\frac{\lambda_{2\rightarrow 3}}{\lambda_{4\rightarrow 6}} = \frac{\frac{hc \cdot 36}{R_H \cdot 5}}{\frac{hc \times 36 \times 16}{R_H \cdot 20}}$
10. $= \frac{1}{4}$

**Solved independently** (answer withheld)

1. Rydberg formula: $\frac{1}{\lambda} = R\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$.
2. For $2 \rightarrow 3$: $\frac{1}{\lambda_1} = R\left(\frac{1}{4} - \frac{1}{9}\right) = \frac{5R}{36}$.
3. For $4 \rightarrow 6$: $\frac{1}{\lambda_2} = R\left(\frac{1}{16} - \frac{1}{36}\right) = \frac{5R}{144}$.
4. $\frac{\lambda_1}{\lambda_2} = \frac{5R/144}{5R/36} = \frac{36}{144} = \frac{1}{4}$, which is option $1$.

**Subtopic:** Hydrogen Spectrum and Spectral Series · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q048_06cbcec5_12112026.png?v=06cbcec5fbbf)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q048_674acc0f_12112026.png?v=674acc0f1b98)

---

## Q49

Chemistry · inorganic · Coordination Compounds – Practice

The correct order of the wavelength of light absorbed by the following complexes is, Choose the correct answer from the options given below:

- (A) $\mathrm{[Co(NH_3)_6]^{3+}}$
- (B) $\mathrm{[Co(CN)_6]^{3-}}$
- (C) $\mathrm{[Cu(H_2O)_4]^{2+}}$
- (D) $\mathrm{[Ti(H_2O)_6]^{3+}}$

- (1) C $<$ A $<$ D $<$ B
- (2) B $<$ D $<$ A $<$ C
- **(3)** B $<$ A $<$ D $<$ C
- (4) C $<$ D $<$ A $<$ B

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\lambda \propto \frac{1}{\text{strength of ligand}}$
2. $\lambda \propto \frac{1}{\text{splitting}}$
3. A. $\mathrm{[Co(NH_3)_6]^{3+}}$ ; $475\,\mathrm{nm}$
4. B. $\mathrm{[Co(CN)_6]^{3-}}$ ; $310\,\mathrm{nm}$
5. C. $\mathrm{[Cu(H_2O)_4]^{2+}}$ ; $600\,\mathrm{nm}$
6. D. $\mathrm{[Ti(H_2O)_6]^{3+}}$ ; $498\,\mathrm{nm}$
7. Order of $\lambda$ = C $>$ D $>$ A $>$ B

**Solved independently** (answer withheld)

1. The absorbed wavelength is inversely related to the crystal-field splitting: $\lambda \propto \frac{1}{\Delta_o}$.
2. $\mathrm{CN^-}$ is a stronger-field ligand than $\mathrm{NH_3}$, and both complexes have $\mathrm{Co^{3+}}$, so $\Delta_B > \Delta_A$.
3. $\mathrm{Ti^{3+}}$ with the weak-field ligand $\mathrm{H_2O}$ has a smaller $\Delta$ than the $\mathrm{Co^{3+}}$ ammine complex ($\lambda_{max} \approx 500$ nm, violet colour), so $\Delta_A > \Delta_D$.
4. $\mathrm{Cu^{2+}}$ (+2 charge) with $\mathrm{H_2O}$ has the smallest $\Delta$ and absorbs in the red/orange region ($\lambda > 600$ nm, blue colour), so $\Delta_D > \Delta_C$.
5. So $\lambda$: $B < A < D < C$, which is option $3$.

**Subtopic:** Colour in Coordination Compounds, Crystal Field Theory and Its Limitations · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 26)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q049_67583245_12112026.png?v=6758324536f4)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q049_1d74bc19_12112026.png?v=1d74bc1955c0)

---

## Q50

Chemistry · physical · Chemical Kinetics

If the rate constant of a reaction is $0.03\,\mathrm{s^{-1}}$, how much time does it take for $7.2\,\mathrm{mol\,L^{-1}}$ concentration of the reactant to get reduced to $0.9\,\mathrm{mol\,L^{-1}}$? (Given: $\log 2 = 0.301$)

- (1) $21.0\,\mathrm{s}$
- **(2)** $69.3\,\mathrm{s}$
- (3) $23.1\,\mathrm{s}$
- (4) $210\,\mathrm{s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $k = 0.03\,\mathrm{s^{-1}}$
2. $t = \frac{2.303}{k}\log\frac{a}{a - x}$
3. $= \frac{2.303}{0.03}\log\frac{7.2}{0.9}$
4. $= \frac{2.303}{0.03}\log 8$
5. $= \frac{2.303}{0.03} \times 3 \times \log 2$
6. $= \frac{2.303}{0.03} \times 3 \times 0.301$
7. $= 69.3\,\mathrm{s}$

**Solved independently** (answer withheld)

1. The unit of $k$ is $\mathrm{s^{-1}}$, so the reaction is first order.
2. $t = \frac{2.303}{k}\log\frac{[R]_0}{[R]} = \frac{2.303}{0.03}\log\frac{7.2}{0.9}$.
3. $\frac{7.2}{0.9} = 8$, so $\log 8 = 3\log 2 = 3 \times 0.301 = 0.903$.
4. $t = 76.77 \times 0.903 \approx 69.3\,\mathrm{s}$, which is option $2$.

**Subtopic:** First Order Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q050_b0e0da2b_12112026.png?v=b0e0da2bae85)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q050_e4c13ba8_12112026.png?v=e4c13ba8269e)

---

## Q51

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

Match List I with List II

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{CHCl_3 + C_6H_5NH_2}$ | I | Distillation under reduced pressure |
| B | Crude oil in petroleum industry | II | Steam distillation |
| C | Glycerol from spent-lye | III | Fractional distillation |
| D | Aniline - water | IV | Simple distillation |

- (1) A-III, B-IV, C-II, D-I
- **(2)** A-IV, B-III, C-I, D-II
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (Method of separation)
2. (A) $\mathrm{CHCl_3 + C_6H_5NH_2}$ — Simple distillation
3. (B) Crude oil in petroleum industry — Fractional distillation
4. (C) Glycerol from spent-lye — Distillation under reduced pressure
5. (D) Aniline - water — Steam Distillation

**Solved independently** (answer withheld)

1. $\mathrm{CHCl_3}$ (b.p. 334 K) and $\mathrm{C_6H_5NH_2}$ (b.p. 457 K) have widely different boiling points, so they are separated by simple distillation: A-IV.
2. Crude oil components have close boiling points, so the petroleum industry uses fractional distillation: B-III.
3. Glycerol decomposes at its boiling point, so it is recovered from spent-lye by distillation under reduced pressure: C-I.
4. Aniline is steam volatile and immiscible with water, so aniline-water is separated by steam distillation: D-II.
5. A-IV, B-III, C-I, D-II is option $2$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q051_a0bdc762_12112026.png?v=a0bdc7629159)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q051_b5cd5b2b_12112026.png?v=b5cd5b2b8ab0)

---

## Q52

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The major product of the following reaction is

![printed figure: 4-oxo-4-phenylbutanenitrile →((i) $\ce{CH3MgBr}$ (excess); (ii) $\ce{H3O+}$)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q052_959acc9f_12112026.png?v=959acc9ff395)

*4-oxo-4-phenylbutanenitrile →[(i) $\ce{CH3MgBr}$ (excess); (ii) $\ce{H3O+}$]*

Structures: 4-oxo-4-phenylbutanenitrile `N#CCCC(=O)c1ccccc1`

- (1) 1-phenylpentane-1,4-dione `CC(=O)CCC(=O)c1ccccc1`
- (2) 4-hydroxy-4-phenylpentanenitrile `CC(O)(CCC#N)c1ccccc1`
- **(3)** 5-hydroxy-5-phenylhexan-2-one `CC(=O)CCC(C)(O)c1ccccc1`
- (4) 2-methyl-5-phenylhexane-2,5-diol `CC(C)(O)CCC(C)(O)c1ccccc1`

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\mathrm{CH_3MgBr}$ adds to the ketone: $\mathrm{PhC(=O)R} \rightarrow \mathrm{Ph(CH_3)C(OMgBr)R}$.
2. $\mathrm{CH_3MgBr}$ adds once to the nitrile: $\mathrm{R'C{\equiv}N} \rightarrow \mathrm{R'C(CH_3){=}NMgBr}$; the negatively charged imine salt does not add a second Grignard.
3. Acid work-up protonates the alkoxide to $\mathrm{-C(OH)(CH_3)Ph}$.
4. Acid work-up hydrolyses the imine: $\mathrm{R'C(CH_3){=}NH} + \mathrm{H_2O} \rightarrow \mathrm{R'COCH_3} + \mathrm{NH_3}$.
5. Product $\mathrm{Ph(CH_3)C(OH)CH_2CH_2COCH_3}$ is option $3$.

**Subtopic:** Nucleophilic Addition Reactions, Preparation of Ketones · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 28)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q052_1dc461c7_12112026.png?v=1dc461c7cf8d)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q052_6379489e_12112026.png?v=6379489ed3e4)

---

## Q53

Chemistry · organic · Isomerism in Organic Compounds

Which one of the following compounds can exist as cis-trans isomers?

- **(1)** 1, 2-Dimethylcyclohexane
- (2) Pent-1-ene
- (3) 2-Methylhex-2-ene
- (4) 1, 1-Dimethylcyclopropane

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cis-trans isomers shown by :
2. Condition: Restricted rotation around double bond
3. Or
4. Different group around double bond

**Solved independently** (answer withheld)

1. Cis-trans isomerism needs two different groups on each of the two carbons whose rotation is restricted (a $C=C$ or ring carbons).
2. Pent-1-ene: $CH_2=CH-CH_2CH_2CH_3$; $C_1$ carries two $H$, so no cis-trans isomers.
3. 2-Methylhex-2-ene: $(CH_3)_2C=CH-CH_2CH_2CH_3$; $C_2$ carries two $CH_3$, so no cis-trans isomers.
4. 1,1-Dimethylcyclopropane: both $CH_3$ are on the same ring carbon, so no cis-trans isomers.
5. 1,2-Dimethylcyclohexane: the $CH_3$ groups are on adjacent ring carbons and can be on the same or opposite faces, giving cis and trans forms; this is option $1$.

**Subtopic:** Geometrical Isomerism · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q053_b26d7743_12112026.png?v=b26d77436642)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q053_2ef73a60_12112026.png?v=2ef73a600809)

---

## Q54

Chemistry · physical · Basic Concepts of Chemistry

Among the following, choose the ones with equal number of atoms.
Choose the correct answer from the options given below :

- (A) $212\,\mathrm{g}$ of $\mathrm{Na_2CO_3(s)}$ [molar mass $= 106\,\mathrm{g}$]
- (B) $248\,\mathrm{g}$ of $\mathrm{Na_2O(s)}$ [molar mass $= 62\,\mathrm{g}$]
- (C) $240\,\mathrm{g}$ of $\mathrm{NaOH(s)}$ [molar mass $= 40\,\mathrm{g}$]
- (D) $12\,\mathrm{g}$ of $\mathrm{H_2(g)}$ [molar mass $= 2\,\mathrm{g}$]
- (E) $220\,\mathrm{g}$ of $\mathrm{CO_2(g)}$ [molar mass $= 44\,\mathrm{g}$]

- (1) B, D, and E only
- (2) A, B, and C only
- **(3)** A, B, and D only
- (4) B, C, and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Number of atoms $= \frac{\text{given mass}}{\text{molar mass}} \times \text{atomicity} \times N_A$
2. A. $\frac{212}{106} \times 6 \times N_A = 12\,N_A$
3. B. $\frac{248}{62} \times 3 \times N_A = 12\,N_A$
4. C. $\frac{240}{40} \times 3 \times N_A = 18\,N_A$
5. D. $\frac{12}{2} \times N_A \times 2 = 12\,N_A$
6. E. $\frac{220}{44} \times N_A \times 3 = 15\,N_A$
7. A, B and D have same number of atoms

**Solved independently** (answer withheld)

1. A: $n = \frac{212}{106} = 2$ mol of $\mathrm{Na_2CO_3}$, 6 atoms each, so $2 \times 6 = 12$ mol atoms.
2. B: $n = \frac{248}{62} = 4$ mol of $\mathrm{Na_2O}$, 3 atoms each, so $4 \times 3 = 12$ mol atoms.
3. C: $n = \frac{240}{40} = 6$ mol of $\mathrm{NaOH}$, 3 atoms each, so $6 \times 3 = 18$ mol atoms.
4. D: $n = \frac{12}{2} = 6$ mol of $\mathrm{H_2}$, 2 atoms each, so $6 \times 2 = 12$ mol atoms.
5. E: $n = \frac{220}{44} = 5$ mol of $\mathrm{CO_2}$, 3 atoms each, so $5 \times 3 = 15$ mol atoms.
6. A, B and D each have $12 N_A$ atoms, which is option $3$.

**Subtopic:** Mole Concept · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q054_d20fcda7_12112026.png?v=d20fcda7ed50)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q054_cda778ab_12112026.png?v=cda778ab4848)

---

## Q55

Chemistry · organic · General Organic Chemistry

Among the given compounds I-III, the correct order of bond dissociation energy of $\mathrm{C{-}H}$ bond marked with $*$ is :

![printed figure: I benzene (C-H marked *); II ethynylbenzene (terminal alkyne C-H marked *); III cyclopropene (sp3 CH2 C-H marked *)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q055_662027fc_12112026.png?v=662027fca86d)

*I benzene (C-H marked *); II ethynylbenzene (terminal alkyne C-H marked *); III cyclopropene (sp3 CH2 C-H marked *)*

Structures: benzene `c1ccccc1`; ethynylbenzene `C#Cc1ccccc1`; cyclopropene `C1=CC1`

- (1) $\mathrm{II > III > I}$
- **(2)** $\mathrm{II > I > III}$
- (3) $\mathrm{I > II > III}$
- (4) $\mathrm{III > II > I}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. I. carbon of this bond is $sp^{2}$ hybridised
2. II. carbon of this bond is $sp$ hybridised
3. III. carbon of this bond is $sp^{3}$ hybridised
4. Higher the percentage s character, stronger is $\mathrm{C{-}H}$ bond. Correct order of bond dissociation energy of $\mathrm{C{-}H}$ bond:
5. $\mathrm{II > I > III}$

**Solved independently** (answer withheld)

1. In I the marked $\mathrm{C{-}H}$ is on an aromatic ring carbon, which is $sp^2$ ($33\%$ s-character).
2. In II the marked $\mathrm{C{-}H}$ is on a terminal alkyne carbon, which is $sp$ ($50\%$ s-character).
3. In III the marked $\mathrm{C{-}H}$ is on the $\mathrm{CH_2}$ of cyclopropene, which is $sp^3$ ($25\%$ s-character) and allylic to the $\mathrm{C{=}C}$.
4. Higher s-character gives a shorter, stronger $\mathrm{C{-}H}$ bond, so bond dissociation energy follows $sp > sp^2 > sp^3$.
5. Hence $\mathrm{II > I > III}$, which is option $2$.

**Subtopic:** Resonance Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q055_d9041377_12112026.png?v=d9041377573c)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q055_52af779b_12112026.png?v=52af779bd1e1)

---

## Q56

Chemistry · physical · Thermodynamics

The standard heat of formation, in $\mathrm{kcal/mol}$ of $\mathrm{Ba^{2+}}$ is : [Given : standard heat of formation of $\mathrm{SO_4^{2-}}$ ion (aq) $= -216\,\mathrm{kcal/mol}$, standard heat of crystallisation of $\mathrm{BaSO_4(s)} = -4.5\,\mathrm{kcal/mol}$, standard heat of formation of $\mathrm{BaSO_4(s)} = -349\,\mathrm{kcal/mol}$]

- (1) $+220.5$
- **(2)** $-128.5$
- (3) $-133.0$
- (4) $+133.0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{S} + 2\mathrm{O_2} + 2e^{-} \longrightarrow \mathrm{SO_4^{2-}}$ $\quad \Delta H_f = -216\,\mathrm{kcal/mol}$ $\quad \ldots(1)$
2. $\mathrm{Ba^{2+}}(g) + \mathrm{SO_4^{2-}}(g) \longrightarrow \mathrm{BaSO_4}(s)$ $\quad \Delta H_{\text{crystallisation}} = -4.5\,\mathrm{kcal/mol}$ $\quad \ldots(2)$
3. $\mathrm{Ba} + \mathrm{S} + 2\mathrm{O_2} \longrightarrow \mathrm{BaSO_4}(s)$ $\quad \Delta H_{f(\mathrm{BaSO_4})} = -349\,\mathrm{kcal/mol}$ $\quad \ldots(3)$
4. $\mathrm{Ba}(s) \longrightarrow \mathrm{Ba^{2+}}(g) + 2e^{-}$ $\quad \ldots(4)$
5. From equation (1),(2) and (3) we get equation (4). Applying equation (3) – (1) – (2)
6. So, $-349 - (-4.5) - (-216)$
7. So $-349 + 4.5 + 216$
8. $= -349 + 220.5$
9. $= -128.5\,\mathrm{kcal/mol}$

**Solved independently** (answer withheld)

1. Crystallisation reaction: $\mathrm{Ba^{2+}(aq) + SO_4^{2-}(aq) \rightarrow BaSO_4(s)}$, $\Delta H_{cryst} = -4.5\,\mathrm{kcal/mol}$.
2. $\Delta H_{cryst} = \Delta H_f(\mathrm{BaSO_4}) - [\Delta H_f(\mathrm{Ba^{2+}}) + \Delta H_f(\mathrm{SO_4^{2-}})]$.
3. $-4.5 = -349 - (x - 216)$, so $x - 216 = -344.5$.
4. $x = -128.5\,\mathrm{kcal/mol}$, which is option $2$.

**Subtopic:** Standard Enthalpy of Formation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q056_c3f00e45_12112026.png?v=c3f00e458dab)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q056_ef376445_12112026.png?v=ef3764454652)

---

## Q57

Chemistry · physical · Redox Reactions

Consider the following compounds :
$\mathrm{\underline{K}O_2}$, $\mathrm{H_2\underline{O}_2}$ and $\mathrm{H_2\underline{S}O_4}$
The oxidation state of the underlined elements in them are, respectively,

- (1) $+4$, $-4$, and $+6$
- **(2)** $+1$, $-1$, and $+6$
- (3) $+2$, $-2$, and $+6$
- (4) $+1$, $-2$, and $+4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{KO_2}$ $\rightarrow$ Alkali metal always shows $+1$ oxidation state. Therefore oxidation state of $\mathrm{K}$ is $+1$.
2. $\mathrm{H_2O_2}$ $\rightarrow$
3. Oxidation state of oxygen in $\mathrm{H_2O_2}$ is $-1$.
4. $\mathrm{H_2SO_4}$ $\rightarrow$
5. Oxidation state of sulphur in $\mathrm{H_2SO_4}$ is $+6$.

**Solved independently** (answer withheld)

1. $\mathrm{K}$ is an alkali metal, so in $\mathrm{KO_2}$ (superoxide) its oxidation state is $+1$.
2. In $\mathrm{H_2O_2}$: $2(+1) + 2x = 0 \Rightarrow x = -1$.
3. In $\mathrm{H_2SO_4}$: $2(+1) + y + 4(-2) = 0 \Rightarrow y = +6$.
4. The set $+1, -1, +6$ is option $2$.

**Subtopic:** Oxidation Number · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q057_697929b9_12112026.png?v=697929b9751c)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q057_94ddd59f_12112026.png?v=94ddd59f8a40)

---

## Q58

Chemistry · inorganic · Coordination Compounds – Practice

Out of the following complex compounds, which of the compound will be having the minimum conductance in solution?

- (1) $\mathrm{[Co(NH_3)_5Cl]Cl}$
- **(2)** $\mathrm{[Co(NH_3)_3Cl_3]}$
- **(3)** $\mathrm{[Co(NH_3)_4Cl_2]}$
- (4) $\mathrm{[Co(NH_3)_6]Cl_3}$

**Answer** — booklet: (2, 3) · independent solve: (2) · agree

**Publisher's solution**

1. Conductance of any complex depends on the following factor.
2. (1) Number of ions produced by complex.
3. (2) If number of ions are same then we will check charge on complex unit.
4. (1) $\mathrm{[Co(NH_3)_5Cl]Cl \rightarrow [Co(NH_3)_5Cl]^{+} + Cl^{-}}$
5. (2) $\mathrm{[Co^{+3}(NH_3)_3Cl_3]}$ and (3) $\mathrm{[Co^{+2}(NH_3)_4Cl_2]}$: Both complex units have no charge. Therefore both complex units have same conductance.
6. (4) $\mathrm{[Co(NH_3)_6]Cl_3 \rightarrow [Co(NH_3)_6]^{+3} + 3Cl^{-}}$

**Solved independently** (answer withheld)

1. Conductance of a complex in solution depends on the number of ions it gives on dissociation.
2. $\mathrm{[Co(NH_3)_5Cl]Cl \rightarrow [Co(NH_3)_5Cl]^{2+} + Cl^-}$: 2 ions.
3. $\mathrm{[Co(NH_3)_3Cl_3]}$ is neutral (Co$^{3+}$ with 3 Cl$^-$ in the coordination sphere): 0 ions.
4. $\mathrm{[Co(NH_3)_4Cl_2]}$ as printed is also neutral (0 ions), though the usual Co(III) series member is $\mathrm{[Co(NH_3)_4Cl_2]Cl}$ with 2 ions.
5. $\mathrm{[Co(NH_3)_6]Cl_3 \rightarrow [Co(NH_3)_6]^{3+} + 3Cl^-}$: 4 ions.
6. Minimum conductance is for the non-electrolyte $\mathrm{[Co(NH_3)_3Cl_3]}$, option $2$.

**Subtopic:** Werner’s Theory and Applications of Coordination Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q058_686c19e8_12112026.png?v=686c19e890e1)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q058_19d8deb7_12112026.png?v=19d8deb78f28)

---

## Q59

Chemistry · organic · Hydrocarbons

Which one of the following reactions does NOT give benzene as the product?

- **(1)** benzenediazonium chloride `N#[N+]c1ccccc1.[Cl-]` — $\mathrm{C_6H_5{-}\overset{\oplus}{N}{\equiv}N\,\overset{\ominus}{Cl}} \xrightarrow[\text{warm}]{\mathrm{H_2O}}$
- (2) sodium benzoate `O=C([O][Na])c1ccccc1` — $\mathrm{C_6H_5{-}\overset{O}{\overset{\|}{C}}{-}ONa} \xrightarrow[\Delta]{\text{sodalime}}$
- (3) hexane `CCCCCC` — n-hexane $\xrightarrow[773\,\mathrm{K},\ 10-20\,\mathrm{atm}]{\mathrm{Mo_2O_3}}$
- (4) ethyne `C#C` — $\mathrm{H{-}C{\equiv}C{-}H} \xrightarrow[\text{at } 873\,\mathrm{K}]{\text{red hot Iron Tube}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. 1.
2. 2.
3. 3.
4. 4.

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{C_6H_5N_2^+Cl^- + H_2O \xrightarrow{\text{warm}} C_6H_5OH + N_2 + HCl}$, which gives phenol, not benzene.
2. Option 2: decarboxylation with soda lime, $\mathrm{C_6H_5COONa + NaOH \xrightarrow[\Delta]{CaO} C_6H_6 + Na_2CO_3}$, which gives benzene.
3. Option 3: aromatisation of n-hexane over $\mathrm{Mo_2O_3}$ at $773\,\mathrm{K}$ and $10$-$20\,\mathrm{atm}$ gives benzene.
4. Option 4: cyclic polymerisation, $\mathrm{3\,HC{\equiv}CH \xrightarrow{\text{red hot Fe},\ 873\,K} C_6H_6}$, which gives benzene.
5. Only option $1$ does not give benzene.

**Subtopic:** Chemical and Physical Properties of Benzene · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q059_ceea05c3_12112026.png?v=ceea05c31150)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q059_fe69c64a_12112026.png?v=fe69c64a5cfe)

---

## Q60

Chemistry · inorganic · Coordination Compounds – Practice

Which of the following are paramagnetic?
Choose the correct answer from the options given below :

- (A) $\mathrm{[NiCl_4]^{2-}}$
- (B) $\mathrm{Ni(CO)_4}$
- (C) $\mathrm{[Ni(CN)_4]^{2-}}$
- (D) $\mathrm{[Ni(H_2O)_6]^{2+}}$
- (E) $\mathrm{Ni(PPh_3)_4}$

- (1) A, D and E only
- (2) A and C only
- (3) B and E only
- **(4)** A and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. $\mathrm{[NiCl_4]^{2-}}$; $\mathrm{Ni^{+2}}$; $3d^{8}$; $sp^{3}$ hybridisation; $2$ unpaired electrons; paramagnetic
2. B. $\mathrm{Ni(CO)_4}$; $\mathrm{Ni}$; $3d^{8}\,4s^{2}$; $sp^{3}$ hybridisation; Zero unpaired electron; diamagnetic
3. C. $\mathrm{[Ni(CN)_4]^{2-}}$; $\mathrm{Ni^{+2}}$; $3d^{8}$; $dsp^{2}$ hybridisation; Zero unpaired electron; diamagnetic
4. D. $\mathrm{[Ni(H_2O)_6]^{2+}}$; $\mathrm{Ni^{2+}}$, $3d^{8}$; $sp^{3}d^{2}$ hybridisation; Two unpaired electron; paramagnetic
5. E. $\mathrm{Ni(PPh_3)_4}$; $\mathrm{Ni}$; $3d^{8}\,4s^{2}$, $sp^{3}$ hybridisation; zero unpaired electron; Diamagnetic

**Solved independently** (answer withheld)

1. A: $\mathrm{[NiCl_4]^{2-}}$ has $\mathrm{Ni^{2+}}$ ($3d^8$); weak-field $\mathrm{Cl^-}$ gives $sp^3$ tetrahedral with 2 unpaired electrons, so paramagnetic.
2. B: $\mathrm{Ni(CO)_4}$ has $\mathrm{Ni(0)}$, configured as $3d^{10}$ with $sp^3$ hybridisation; 0 unpaired electrons, so diamagnetic.
3. C: $\mathrm{[Ni(CN)_4]^{2-}}$ has $\mathrm{Ni^{2+}}$ ($3d^8$); strong-field $\mathrm{CN^-}$ pairs the electrons, giving $dsp^2$ square planar with 0 unpaired electrons, so diamagnetic.
4. D: $\mathrm{[Ni(H_2O)_6]^{2+}}$ has $\mathrm{Ni^{2+}}$ ($3d^8$) octahedral ($sp^3d^2$); $t_{2g}^6 e_g^2$ leaves 2 unpaired electrons, so paramagnetic.
5. E: $\mathrm{Ni(PPh_3)_4}$ has $\mathrm{Ni(0)}$, $3d^{10}$; 0 unpaired electrons, so diamagnetic.
6. Paramagnetic species are A and D only, which is option $4$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 31)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q060_64f9a47e_12112026.png?v=64f9a47e2e02)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q060_1f3b8e1e_12112026.png?v=1f3b8e1e4112)

---

## Q61

Chemistry · organic · Hydrocarbons

Which one of the following compounds does not decolourize bromine water?

- (1) aniline `Nc1ccccc1` — $-\mathrm{NH_2}$
- **(2)** cyclohexane `C1CCCCC1`
- (3) phenol `Oc1ccccc1` — $-\mathrm{OH}$
- (4) styrene `C=Cc1ccccc1` — $-\mathrm{CH=CH_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Test for unsaturation i.e. Bromine water Reddish orange colour of bromine solution in $\mathrm{CCl_4}$ will discharge when bromine adds to an unsaturation site.

**Solved independently** (answer withheld)

1. Aniline ($\mathrm{C_6H_5NH_2}$): the strongly activating $-\mathrm{NH_2}$ group gives 2,4,6-tribromoaniline with bromine water, so it decolourizes it.
2. Phenol ($\mathrm{C_6H_5OH}$): the activating $-\mathrm{OH}$ group gives 2,4,6-tribromophenol with bromine water, so it decolourizes it.
3. Styrene ($\mathrm{C_6H_5CH{=}CH_2}$): $\mathrm{Br_2}$ adds across the $\mathrm{C{=}C}$ bond, so it decolourizes bromine water.
4. Option 2 is drawn as a plain hexagon with no ring circle or double bonds, so it is cyclohexane ($\mathrm{C_6H_{12}}$). It is saturated and does not react, so it does not decolourize bromine water: option $2$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q061_fd054328_12112026.png?v=fd0543285006)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q061_73cd5b0a_12112026.png?v=73cd5b0a4275)

---

## Q62

Chemistry · inorganic · The D- and F-Block Elements – Practice

Match List-I with List-II. Choose the correct answer from the options given below :

![printed figure: Match-the-list table. List-I: A. Haber process; B. Wacker oxidation; C. Wilkinson catalyst; D Ziegler catalyst. List-II: I. Fe catalyst; II. $\ce{PdCl2}$; III. $\ce{((PPh3)3RhCl)}$; IV. $\ce{TiCl4}$ with $\ce{Al(CH3)3}$](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q062_b664cdc9_12112026.svg?v=b664cdc9bd94)

*Match-the-list table. List-I: A. Haber process; B. Wacker oxidation; C. Wilkinson catalyst; D Ziegler catalyst. List-II: I. Fe catalyst; II. $\ce{PdCl2}$; III. $\ce{[(PPh3)3RhCl]}$; IV. $\ce{TiCl4}$ with $\ce{Al(CH3)3}$*

| List-I | | List-II | |
|---|---|---|---|
| A | Haber process | I | $\mathrm{Fe}$ catalyst |
| B | Wacker oxidation | II | $\mathrm{PdCl_2}$ |
| C | Wilkinson catalyst | III | $\mathrm{[(PPh_3)_3RhCl]}$ |
| D | Ziegler catalyst | IV | $\mathrm{TiCl_4}$ with $\mathrm{Al(CH_3)_3}$ |

- (1) A-I, B-IV, C-III, D-II
- (2) A-I, B-II, C-IV, D-III
- (3) A-II, B-III, C-I, D-IV
- **(4)** A-I, B-II, C-III, D-IV

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Process — Catalyst used
2. A. Haber process — I. $\mathrm{Fe}$ catalyst
3. B. Wacker oxidation — II. $\mathrm{PdCl_2}$
4. C. Wilkinson catalyst — III. $\mathrm{[(PPh_3)_3RhCl]}$
5. D Ziegler catalyst — IV. $\mathrm{TiCl_4}$ with $\mathrm{Al(CH_3)_3}$

**Solved independently** (answer withheld)

1. Haber process ($\mathrm{N_2 + 3H_2 \rightarrow 2NH_3}$) uses an iron catalyst, so A-I.
2. Wacker oxidation of ethene to ethanal uses $\mathrm{PdCl_2}$, so B-II.
3. Wilkinson catalyst is $\mathrm{[(PPh_3)_3RhCl]}$, so C-III.
4. Ziegler catalyst is $\mathrm{TiCl_4}$ with an alkylaluminium such as $\mathrm{Al(CH_3)_3}$, so D-IV.
5. A-I, B-II, C-III, D-IV matches option $4$.

**Subtopic:** Applications of d-Block and f-Block Elements · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 32)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q062_bd9d571d_12112026.png?v=bd9d571dd90f)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q062_1953127f_12112026.png?v=1953127ff6ec)

---

## Q63

Chemistry · organic · Biomolecules

Match List-I with List-II.
List-I (Name of Vitamin) | List-II (Deficiency disease)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Vitamin $\mathrm{B_{12}}$ | I | Cheilosis |
| B | Vitamin D | II | Convulsions |
| C | Vitamin $\mathrm{B_{2}}$ | III | Rickets |
| D | Vitamin $\mathrm{B_{6}}$ | IV | Pernicious anaemia |

- (1) A-IV, B-III, C-II, D-I
- (2) A-I, B-III, C-II, D-IV
- **(3)** A-IV, B-III, C-I, D-II
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. Vitamin $\mathrm{B_{12}}$ — Pernicious anaemia
2. B. Vitamin D — Rickets
3. C. Vitamin $\mathrm{B_{2}}$ — Cheilosis
4. D. Vitamin $\mathrm{B_{6}}$ — Convulsions

**Solved independently** (answer withheld)

1. Vitamin $\mathrm{B_{12}}$ deficiency causes pernicious anaemia, so A-IV.
2. Vitamin D deficiency causes rickets, so B-III.
3. Vitamin $\mathrm{B_{2}}$ (riboflavin) deficiency causes cheilosis, so C-I.
4. Vitamin $\mathrm{B_{6}}$ (pyridoxine) deficiency causes convulsions, so D-II.
5. A-IV, B-III, C-I, D-II is option $3$.

**Subtopic:** Vitamins Classification and Uses · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q063_b0b5bc78_12112026.png?v=b0b5bc781810)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q063_997d455b_12112026.png?v=997d455b1aa5)

---

## Q64

Chemistry · inorganic · The D- and F-Block Elements – Practice

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Ferromagnetism is considered as an extreme form of paramagnetism.
- (Statement II) The number of unpaired electrons in a $\mathrm{Cr^{2+}}$ ion ($Z = 24$) is the same as that of a $\mathrm{Nd^{3+}}$ ion ($Z = 60$).

- (1) Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- **(4)** Statement I is true but Statement II is false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Substances which are attracted very strongly in applied magnetic field are termed as ferromagnetic. Infact, ferromagnetism is an extreme form of paramagnetism.
2. Hence statement I is correct.
3. $\mathrm{Cr^{2+}} = 3d^{4}4s^{0}$
4. Unpaired electrons $= 4$
5. $\mathrm{Nd^{3+}} = 4f^{3}\,6s^{0}$
6. Unpaired electrons $= 3$
7. Hence, Statement II is incorrect

**Solved independently** (answer withheld)

1. Ferromagnetic substances are strongly attracted because their unpaired spins align cooperatively into domains; this is treated as an extreme form of paramagnetism, so Statement I is true.
2. $\mathrm{Cr}\,(Z=24): [\mathrm{Ar}]\,3d^5 4s^1 \Rightarrow \mathrm{Cr^{2+}}: [\mathrm{Ar}]\,3d^4$, giving $4$ unpaired electrons.
3. $\mathrm{Nd}\,(Z=60): [\mathrm{Xe}]\,4f^4 6s^2 \Rightarrow \mathrm{Nd^{3+}}: [\mathrm{Xe}]\,4f^3$, giving $3$ unpaired electrons.
4. $4 \neq 3$, so Statement II is false; I true and II false is option $4$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q064_16899154_12112026.png?v=168991545383)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q064_bfc2967b_12112026.png?v=bfc2967be394)

---

## Q65

Chemistry · physical · Chemical Kinetics

If the half-life ($t_{1/2}$) for a first order reaction is $1$ minute, then the time required for $99.9\%$ completion of the reaction is closest to :

- **(1)** $10$ minutes
- (2) $2$ minutes
- (3) $4$ minutes
- (4) $5$ minutes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For $1^{\text{st}}$ order reaction
2. $kt = 2.303\log\frac{A_0}{A_t}$ $\quad A_0$ = initial concentration
3. $A_t$ = Final concentration
4. $t_{99.9\%} = 10\,t_{1/2}$
5. $t_{99.9\%} = 10 \times 1$ minute $= 10$ minutes

**Solved independently** (answer withheld)

1. For a first order reaction $k = \frac{0.693}{t_{1/2}} = \frac{0.693}{1\,\text{min}} = 0.693\,\text{min}^{-1}$.
2. For $99.9\%$ completion, $\frac{[A]_0}{[A]} = \frac{100}{0.1} = 1000$.
3. $t = \frac{2.303}{k}\log 1000 = \frac{2.303 \times 3}{0.693}\,\text{min}$.
4. $t \approx 9.97\,\text{min} \approx 10\,\text{min}$, which is option $1$.

**Subtopic:** First Order Reactions, Half-Life of a Reaction · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 34)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q065_b8de52cb_12112026.png?v=b8de52cbf6f8)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q065_69fe2aa4_12112026.png?v=69fe2aa43591)

---

## Q66

Chemistry · organic · Amines

The correct order of decreasing basic strength of the given amines is:

- (1) benzenamine $>$ ethanamine $>$ N-methylaniline $>$ N-ethylethanamine
- (2) N-methylaniline $>$ benzenamine $>$ ethanamine $>$ N-ethylethanamine
- (3) N-ethylethanamine $>$ ethanamine $>$ benzenamine $>$ N-methylaniline
- **(4)** N-ethylethanamine $>$ ethanamine $>$ N-methylaniline $>$ benzenamine

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Lower is the value of $\mathrm{p}K_{b}$, higher is the basicity
2. Also aliphatic amines are stronger bases than aromatic amines.
3. $\mathrm{p}K_{b}$ : Benzenamine $>$ N-Methylaniline $>$ Ethanamine $>$ N-Ethylethanamine
4. Basic strength : N-Ethylethanamine $>$ Ethanamine $>$ N-Methylaniline $>$ Benzenamine

**Solved independently** (answer withheld)

1. Aliphatic amines are stronger bases than aryl amines because in aryl amines the N lone pair is delocalised into the ring, so $\text{N-ethylethanamine}$ and $\text{ethanamine}$ come before $\text{N-methylaniline}$ and $\text{benzenamine}$.
2. In aqueous solution $(C_2H_5)_2NH$ ($pK_b = 3.00$) is more basic than $C_2H_5NH_2$ ($pK_b = 3.29$), so $\text{N-ethylethanamine} > \text{ethanamine}$.
3. The $+I$ effect of $-CH_3$ makes $C_6H_5NHCH_3$ ($pK_b = 9.30$) more basic than $C_6H_5NH_2$ ($pK_b = 9.38$), so $\text{N-methylaniline} > \text{benzenamine}$.
4. Order: $\text{N-ethylethanamine} > \text{ethanamine} > \text{N-methylaniline} > \text{benzenamine}$, which is option $4$.

**Subtopic:** Chemical Reactions of Amines (Basicity, Alkylation and Acylation) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q066_a24bd58b_12112026.png?v=a24bd58bd93a)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q066_e88b824b_12112026.png?v=e88b824b4703)

---

## Q67

Chemistry · inorganic · Principles Related to Practical Chemistry

Match List I with List II
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{Co^{2+}}$ | I | Group-I |
| B | $\mathrm{Mg^{2+}}$ | II | Group-III |
| C | $\mathrm{Pb^{2+}}$ | III | Group-IV |
| D | $\mathrm{Al^{3+}}$ | IV | Group-VI |

- (1) A-III, B-II, C-I, D-IV
- (2) A-III, B-IV, C-II, D-I
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ion — Group number in Cation Analysis
2. A. $\mathrm{Co^{2+}}$ — Group-IV
3. B. $\mathrm{Mg^{2+}}$ — Group-VI
4. C. $\mathrm{Pb^{2+}}$ — Group-I
5. D. $\mathrm{Al^{3+}}$ — Group-III

**Solved independently** (answer withheld)

1. $\mathrm{Co^{2+}}$ is precipitated as $\mathrm{CoS}$ by $\mathrm{H_2S}$ in ammoniacal medium, so it is a Group-IV cation: A-III.
2. $\mathrm{Mg^{2+}}$ is not precipitated in Groups I to V and is detected as $\mathrm{Mg(NH_4)PO_4}$ in Group-VI: B-IV.
3. $\mathrm{Pb^{2+}}$ is precipitated as $\mathrm{PbCl_2}$ by dilute $\mathrm{HCl}$, so it is a Group-I cation: C-I.
4. $\mathrm{Al^{3+}}$ is precipitated as $\mathrm{Al(OH)_3}$ by $\mathrm{NH_4OH}$ in presence of $\mathrm{NH_4Cl}$, so it is a Group-III cation: D-II.
5. The match A-III, B-IV, C-I, D-II is option $3$.

**Subtopic:** Group Analysis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q067_451e610a_12112026.png?v=451e610a8ede)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q067_31ec98bb_12112026.png?v=31ec98bb7733)

---

## Q68

Chemistry · physical · Ionic Equilibrium

Phosphoric acid ionizes in three steps with their ionization constant values $K_{a_1}$, $K_{a_2}$ and $K_{a_3}$, respectively, while $K$ is the overall ionization constant. Which of the following statements are true? Choose the correct answer from the options given below :

- (A) $\log K = \log K_{a_1} + \log K_{a_2} + \log K_{a_3}$
- (B) $\mathrm{H_3PO_4}$ is a stronger acid than $\mathrm{H_2PO_4^-}$ and $\mathrm{HPO_4^{2-}}$
- (C) $K_{a_1} > K_{a_2} > K_{a_3}$
- (D) $K_{a_1} = \dfrac{K_{a_3} + K_{a_2}}{2}$

- **(1)** A, B and C only
- (2) A and B only
- (3) A and C only
- (4) B, C and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{H_3PO_4}$ is a stronger acid than $\mathrm{H_2PO_4^-}$ and $\mathrm{HPO_4^{2-}}$
2. $\mathrm{H_3PO_4(aq) \rightleftharpoons H^+(aq) + H_2PO_4^-(aq)}$ $\quad K_{a_1} = 7.5 \times 10^{-3}$
3. $\mathrm{H_2PO_4^-(aq) \rightleftharpoons H^+(aq) + HPO_4^{2-}(aq)}$ $\quad K_{a_2} = 6.2 \times 10^{-8}$
4. $\mathrm{HPO_4^{2-}(aq) \rightleftharpoons H^+(aq) + PO_4^{3-}(aq)}$ $\quad K_{a_3} = 1.7 \times 10^{-12}$
5. $K_{a_1} > K_{a_2} > K_{a_3}$
6. $\log K = \log K_{a_1} + \log K_{a_2} + \log K_{a_3}$
7. Ans. (A), (B) and (C) only

**Solved independently** (answer withheld)

1. Overall equilibrium is the sum of the three steps, so $K = K_{a_1} K_{a_2} K_{a_3}$.
2. Taking logs, $\log K = \log K_{a_1} + \log K_{a_2} + \log K_{a_3}$, so A is true.
3. Removing $\mathrm{H^+}$ from an increasingly negative species is harder, so $K_{a_1} > K_{a_2} > K_{a_3}$; C is true.
4. Hence $\mathrm{H_3PO_4}$ is a stronger acid than $\mathrm{H_2PO_4^-}$ and $\mathrm{HPO_4^{2-}}$; B is true.
5. $K_{a_1} = \frac{K_{a_2} + K_{a_3}}{2}$ is impossible since $K_{a_1} \gg K_{a_2}, K_{a_3}$; D is false.
6. True statements are A, B and C, which is option $1$.

**Subtopic:** Di- and Polybasic Acids and Bases · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q068_e083bd41_12112026.png?v=e083bd416346)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q068_01a3622c_12112026.png?v=01a3622c539c)

---

## Q69

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Which of the following statements are true?
Choose the correct answer from the options given below :

- (A) Unlike Ga that has a very high melting point, Cs has a very low melting point.
- (B) On Pauling scale, the electronegativity values of N and Cl are not the same.
- (C) $\mathrm{Ar}$, $\mathrm{K^{+}}$, $\mathrm{Cl^{-}}$, $\mathrm{Ca^{2+}}$, and $\mathrm{S^{2-}}$ are all isoelectronic species.
- (D) The correct order of the first ionization enthalpies of Na, Mg, Al, and Si is $\mathrm{Si} > \mathrm{Al} > \mathrm{Mg} > \mathrm{Na}$.
- (E) The atomic radius of Cs is greater than that of Li and Rb.

- (1) A, C, and E only
- (2) A, B, and E only
- **(3)** C and E only
- (4) C and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Both $\mathrm{Ga}$ and $\mathrm{Cs}$ have low melting points.
2. Element | Melting point/$\mathrm{K}$
3. $\mathrm{Ga}$ | $303$
4. $\mathrm{Cs}$ | $302$
5. On Pauling scale, the electronegativity value of $\mathrm{N}$ and $\mathrm{Cl}$ have same ($3.0$).
6. $\mathrm{Ar}$, $\mathrm{K^{+}}$, $\mathrm{Cl^{-}}$, $\mathrm{Ca^{2+}}$ and $\mathrm{S^{2-}}$ have $18$ electrons. So these are isoelectronic species.
7. The correct order of first ionization enthalpy is $\mathrm{Si} > \mathrm{Mg} > \mathrm{Al} > \mathrm{Na}$
8. First ionisation enthalpy of $\mathrm{Mg}$ is higher than $\mathrm{Al}$ because the penetration of a $3s$-electron to the nucleus is more than that of a $2p$-electron.
9. Generally down the group atomic radii increases
10. Atom | Atomic radius/$\mathrm{pm}$
11. $\mathrm{Li}$ | $152$
12. $\mathrm{Rb}$ | $244$
13. $\mathrm{CS}$ | $262$

**Solved independently** (answer withheld)

1. Statement A: $\mathrm{Ga}$ itself has a very low melting point ($\approx 303\,\mathrm{K}$), so A is false.
2. Statement B: on the Pauling scale $\chi(\mathrm{N}) = 3.0 = \chi(\mathrm{Cl})$, so B is false.
3. Statement C: $\mathrm{Ar}, \mathrm{K^{+}}, \mathrm{Cl^{-}}, \mathrm{Ca^{2+}}, \mathrm{S^{2-}}$ each have $18$ electrons, so C is true.
4. Statement D: $\mathrm{Mg}$ ($3s^2$, filled subshell) has higher $\Delta_i H_1$ than $\mathrm{Al}$ ($3p^1$), so the order is $\mathrm{Si} > \mathrm{Mg} > \mathrm{Al} > \mathrm{Na}$ and D is false.
5. Statement E: atomic radius increases down group 1, so $r(\mathrm{Cs}) > r(\mathrm{Rb}) > r(\mathrm{Li})$ and E is true.
6. True statements are C and E only, which is option $3$.

**Subtopic:** Trends in Chemical Properties – Atomic and Ionic Radius · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 35)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q069_8450b727_12112026.png?v=8450b727ebdc)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q069_09964320_12112026.png?v=099643202589)

---

## Q70

Chemistry · inorganic · The p–Block Elements

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) Like nitrogen that can form ammonia, arsenic can form arsine.
- (Statement II) Antimony cannot form antimony pentoxide.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. All the elements of group $15$ form hydrides of $\mathrm{EH_3}$ type. Nitrogen forms ammonia ($\mathrm{NH_3}$) while Arsenic forms Arsine ($\mathrm{AsH_3}$)
2. All the elements of group $15$ form two types of oxides : $\mathrm{E_2O_3}$ and $\mathrm{E_2O_5}$
3. Antimony forms antimony pentoxide $\mathrm{Sb_2O_5}$
4. Hence, statement I is correct and statement II is incorrect

**Solved independently** (answer withheld)

1. All group 15 elements form hydrides of the type $EH_3$, so like $NH_3$, arsenic forms arsine $AsH_3$; Statement I is correct.
2. Group 15 elements form oxides $E_2O_3$ and $E_2O_5$; antimony forms antimony pentoxide $Sb_2O_5$, so Statement II is incorrect.
3. Statement I correct, Statement II incorrect gives option $4$.

**Subtopic:** General Properties & Trends of Group 15 (Nitrogen Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q070_3f66ead3_12112026.png?v=3f66ead3e501)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q070_bc64aec2_12112026.png?v=bc64aec260ca)

---

## Q71

Chemistry · physical · Solutions

Which of the following aqueous solution will exhibit highest boiling point?

- (1) $0.015\,\mathrm{M}$ $\mathrm{C_6H_{12}O_6}$
- (2) $0.01\,\mathrm{M}$ Urea
- (3) $0.01\,\mathrm{M}$ $\mathrm{KNO_3}$
- **(4)** $0.01\,\mathrm{M}$ $\mathrm{Na_2SO_4}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\Delta T_b = iK_b \times m$
2. $\Delta T_b \propto i \times m$
3. By considering molarity same as molality
4. (1) $0.015\,\mathrm{M}$ $\mathrm{C_6H_{12}O_6}$ $\quad i \times m = 1 \times 0.015 = 0.015$
5. (2) $0.01\,\mathrm{M}$ Urea $\quad i \times m = 1 \times 0.01 = 0.01$
6. (3) $0.01\,\mathrm{M}$ $\mathrm{KNO_3}$ $\quad i \times m = 2 \times 0.01 = 0.02$
7. (4) $0.01\,\mathrm{M}$ $\mathrm{Na_2SO_4}$ $\quad i \times m = 3 \times 0.01 = 0.03$
8. $T_b' = T_b^{*} + \Delta T_b$
9. Higher the value of $(i \times m)$ more will be the boiling point.

**Solved independently** (answer withheld)

1. Elevation in boiling point is colligative: $\Delta T_b = i K_b m$, so compare $i \times m$.
2. Glucose is a non-electrolyte: $i \times m = 1 \times 0.015 = 0.015$.
3. Urea is a non-electrolyte: $i \times m = 1 \times 0.01 = 0.01$.
4. $\mathrm{KNO_3} \rightarrow \mathrm{K^+} + \mathrm{NO_3^-}$, $i = 2$: $i \times m = 2 \times 0.01 = 0.02$.
5. $\mathrm{Na_2SO_4} \rightarrow 2\mathrm{Na^+} + \mathrm{SO_4^{2-}}$, $i = 3$: $i \times m = 3 \times 0.01 = 0.03$.
6. $0.03$ is the largest, so $\mathrm{Na_2SO_4}$ has the highest boiling point, which is option $4$.

**Subtopic:** Elevation of Boiling Point, Van’t Hoff Factor · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q071_dbc5d6c6_12112026.png?v=dbc5d6c65990)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q071_0c07a5ca_12112026.png?v=0c07a5ca295f)

---

## Q72

Chemistry · organic · Amines

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement-I) Benzenediazonium salt is prepared by the reaction of aniline with nitrous acid at $273 - 278\,\mathrm{K}$. It decomposes easily in the dry state.
- (Statement-II) Insertion of iodine into the benzene ring is difficult and hence iodobenzene is prepared through the reaction of benzenediazonium salt with $\mathrm{KI}$.

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Benzene diazonium chloride is prepared by the reaction of aniline with nitrous acid at $273\text{-}278\,\mathrm{K}$.
2. Nitrous acid is produced in the reaction mixture by reaction of $\mathrm{NaNO_2}$ with $\mathrm{HCl}$.
3. $\mathrm{C_6H_5NH_2 + NaNO_2 + 2HCl \xrightarrow{273\,-\,278\,K} C_6H_5\overset{+}{N_2}\overset{-}{Cl} + NaCl + 2H_2O}$
4. Benzene diazonium chloride decomposes easily in the dry state
5. Iodobenzene is prepared by shaking benzene diazonium salt with $\mathrm{KI}$ because direct insertion of iodine into benzene ring is difficult

**Solved independently** (answer withheld)

1. Statement I: aniline reacts with nitrous acid ($\mathrm{NaNO_2 + HCl}$) at $273$-$278\,\mathrm{K}$ to give benzenediazonium chloride, which is unstable and decomposes easily in the dry state, so Statement I is correct.
2. Statement II: direct iodination of benzene is reversible and difficult, so iodobenzene is made by treating benzenediazonium salt with $\mathrm{KI}$, so Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Diazotization and Its Method of Preparation, Chemical Reactions of Diazonium Salts and Coupling Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q072_036df667_12112026.png?v=036df667bbee)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q072_9b4a4a88_12112026.png?v=9b4a4a8863d1)

---

## Q73

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the suitable reagent for the following conversion.

![printed figure: methyl benzoate → benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q073_87b67a47_12112026.png?v=87b67a4704b1)

*methyl benzoate → benzaldehyde*

Structures: methyl benzoate `COC(=O)c1ccccc1`; benzaldehyde `O=Cc1ccccc1`

- (1) $\mathrm{H_2/Pd\text{-}BaSO_4}$
- (2) (i) $\mathrm{LiAlH_4}$, (ii) $\mathrm{H^+/H_2O}$
- **(3)** (i) $\mathrm{AlH(iBu)_2}$, (ii) $\mathrm{H_2O}$
- (4) (i) $\mathrm{NaBH_4}$, (ii) $\mathrm{H^+/H_2O}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Esters are reduced to aldehydes with $\mathrm{DIBAL\text{-}H}$

**Solved independently** (answer withheld)

1. The conversion is $\mathrm{C_6H_5COOCH_3} \rightarrow \mathrm{C_6H_5CHO}$, a partial reduction of an ester to an aldehyde.
2. $\mathrm{H_2/Pd\text{-}BaSO_4}$ (Rosenmund) reduces acid chlorides, not esters, so option $1$ fails.
3. $\mathrm{LiAlH_4}$ reduces the ester fully to $\mathrm{C_6H_5CH_2OH}$, so option $2$ fails; $\mathrm{NaBH_4}$ does not readily reduce esters, so option $4$ fails.
4. $\mathrm{AlH(iBu)_2}$ (DIBAL-H) then $\mathrm{H_2O}$ gives $\mathrm{C_6H_5COOCH_3} \rightarrow \mathrm{C_6H_5CHO} + \mathrm{CH_3OH}$, which is option $3$.

**Subtopic:** Preparation of Aldehydes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 37)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q073_6fe22b5b_12112026.png?v=6fe22b5b9f61)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q073_4cd0b5cd_12112026.png?v=4cd0b5cd5b04)

---

## Q74

Chemistry · organic · Haloalkanes and Haloarenes

Given below are two statements : one is labelled as Assertion (A) and the other is labelled as Reason (R).
In the light of the above statements, choose the correct answer from the options given below:

![printed figure: Assertion (A) : 1-iodobutane undergoes $\mathrm{S_N2}$ reaction faster than 1-chlorobutane.](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q074_835a9475_12112026.svg?v=835a9475fa00)

*Assertion (A) : 1-iodobutane undergoes $\mathrm{S_N2}$ reaction faster than 1-chlorobutane.*

![drawn: Assertion (A) : 1-iodobutane undergoes $\mathrm{S_N2}$ reaction faster than 1-chlorobutane.](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_drawn/q074_question_8440f810_12112026.svg?v=8440f81089b6)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1-iodobutane `CCCCI` ![1-iodobutane](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_drawn/q074_question_s1_11a81756_12112026.svg?v=11a81756ad9a); 1-chlorobutane `CCCCCl` ![1-chlorobutane](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_drawn/q074_question_s2_f87d4b46_12112026.svg?v=f87d4b46b2b7)

- (A) [structure 1] undergoes $\mathrm{S_N2}$ reaction faster than [structure 2].
- (R) Iodine is a better leaving group because of its large size.

- (1) A is false but R is true
- **(2)** Both A and R are true and R is the correct explanation of A
- (3) Both A and R are true but R is not the correct explanation of A
- (4) A is true but R is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rate of $\mathrm{S_N2}$ reaction of [structure 1] is faster than [structure 2].
2. Because iodine is a good leaving group due to large size of iodine. Which stabilises the $\mathrm{I^{-}}$ ion.

**Solved independently** (answer withheld)

1. The figure shows two primary alkyl halides with the same carbon chain: $\mathrm{R{-}I}$ and $\mathrm{R{-}Cl}$.
2. In an $\mathrm{S_N2}$ reaction the rate depends on how easily the $\mathrm{C{-}X}$ bond breaks, i.e. on the leaving group.
3. Iodine is larger than chlorine, so the $\mathrm{C{-}I}$ bond is weaker and $\mathrm{I^-}$ is a better leaving group than $\mathrm{Cl^-}$.
4. Hence $\mathrm{R{-}I}$ reacts faster than $\mathrm{R{-}Cl}$: A is true, R is true and R explains A, which is option $2$.

**Subtopic:** Reactions of Haloalkanes – Nucleophilic Substitution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 38)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q074_6e4cee5e_12112026.png?v=6e4cee5e05da)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q074_ba8f027e_12112026.png?v=ba8f027e1d8b)

---

## Q75

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The correct order of decreasing acidity of the following aliphatic acids is

- (1) $\mathrm{HCOOH > (CH_3)_3CCOOH > (CH_3)_2CHCOOH > CH_3COOH}$
- (2) $\mathrm{(CH_3)_3CCOOH > (CH_3)_2CHCOOH > CH_3COOH > HCOOH}$
- (3) $\mathrm{CH_3COOH > (CH_3)_2CHCOOH > (CH_3)_3CCOOH > HCOOH}$
- **(4)** $\mathrm{HCOOH > CH_3COOH > (CH_3)_2CHCOOH > (CH_3)_3CCOOH}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Electron donating group decreases the acidity of carboxylic acids.
2. So correct order is
3. $\mathrm{HCOOH > CH_3COOH > (CH_3)_2CHCOOH > (CH_3)_3CCOOH}$

**Solved independently** (answer withheld)

1. Acid strength depends on the stability of the carboxylate ion $\mathrm{RCOO^-}$.
2. Alkyl groups have a $+I$ effect that increases electron density on $\mathrm{COO^-}$ and destabilises it.
3. The $+I$ effect increases as $\mathrm{H < CH_3 < (CH_3)_2CH < (CH_3)_3C}$.
4. So acidity is $\mathrm{HCOOH > CH_3COOH > (CH_3)_2CHCOOH > (CH_3)_3CCOOH}$, which is option $4$.

**Subtopic:** Acidity of Carboxylic Acids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q075_c3f075f6_12112026.png?v=c3f075f60d08)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q075_093171b2_12112026.png?v=093171b216bf)

---

## Q76

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

Which one of the following reactions does NOT belong to “Lassaigne’s test”?

- **(1)** $\mathrm{2CuO + C \xrightarrow[\Delta]{} 2Cu + CO_2}$
- (2) $\mathrm{Na + C + N \xrightarrow[\Delta]{} NaCN}$
- (3) $\mathrm{2Na + S \xrightarrow[\Delta]{} Na_2S}$
- (4) $\mathrm{Na + X \xrightarrow[\Delta]{} + NaX}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Nitrogen, sulphur, halogens and phosphorus present in an organic compound are detected by “Lassaigne’s test”.
2. $\mathrm{Na + C + N \xrightarrow{\Delta} NaCN}$
3. $\mathrm{2Na + S \xrightarrow{\Delta} Na_2S}$
4. $\mathrm{Na + X \xrightarrow{\Delta} NaX}$ $(\mathrm{X = Cl, Br, I})$

**Solved independently** (answer withheld)

1. In Lassaigne's test the organic compound is fused with sodium metal, which converts N, S and halogens into ionic sodium salts.
2. $\mathrm{Na + C + N \xrightarrow{\Delta} NaCN}$, $\mathrm{2Na + S \xrightarrow{\Delta} Na_2S}$ and $\mathrm{Na + X \xrightarrow{\Delta} NaX}$ are all sodium fusion reactions.
3. $\mathrm{2CuO + C \xrightarrow{\Delta} 2Cu + CO_2}$ is the copper(II) oxide test for carbon (and hydrogen), not part of Lassaigne's test, so the answer is option $1$.

**Subtopic:** Detection of Elements · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 38)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q076_3893976d_12112026.png?v=3893976d8a88)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q076_bb025906_12112026.png?v=bb025906050c)

---

## Q77

Chemistry · organic · Isomerism in Organic Compounds

How many products (including stereoisomers) are expected from monochlorination of the following compound?

![printed figure: 2-methylbutane, $\ce{(CH3)2CH-CH2-CH3}$](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q077_581db4b5_12112026.png?v=581db4b5548e)

*2-methylbutane, $\ce{(CH3)2CH-CH2-CH3}$*

Structures: 2-methylbutane `CCC(C)C`

- **(1)** $6$
- (2) $2$
- (3) $3$
- (4) $5$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Possible monochlorination products :
2. One isomer
3. Two isomers due to presence of chiral carbon
4. One isomer
5. Two isomers due to chiral carbon
6. Total $6$ isomers

**Solved independently** (answer withheld)

1. The compound is 2-methylbutane, $(CH_3)_2CH-CH_2-CH_3$, with four kinds of H: the two equivalent $CH_3$ on C2, the C2 $H$, the $CH_2$ H, and the terminal $CH_3$.
2. Chlorinating a C2 methyl gives $ClCH_2-CH(CH_3)-CH_2CH_3$; C2 becomes a stereocentre, so $2$ enantiomers.
3. Chlorinating C2-H gives $(CH_3)_2CCl-CH_2CH_3$, achiral: $1$ product.
4. Chlorinating the $CH_2$ gives $(CH_3)_2CH-CHCl-CH_3$; C3 is a stereocentre, so $2$ enantiomers.
5. Chlorinating the terminal $CH_3$ gives $(CH_3)_2CH-CH_2-CH_2Cl$, achiral: $1$ product.
6. Total $= 2 + 1 + 2 + 1 = 6$, which is option $1$.

**Subtopic:** Position Isomerism, Optical Isomerism · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 39)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q077_7ec42830_12112026.png?v=7ec42830e7ef)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q077_3305583c_12112026.png?v=3305583c2728)

---

## Q78

Chemistry · organic · Biomolecules

Sugar ‘X’
‘X’ is :

- (A) is found in honey
- (B) is a keto sugar
- (C) exists in $\alpha$ and $\beta$ – anomeric forms.
- (D) Is laevorotatory.

- (1) Sucrose
- (2) D-Glucose
- **(3)** D-Fructose
- (4) Maltose

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. D-Fructose is found in honey and is a keto sugar.

**Solved independently** (answer withheld)

1. Statement B (keto sugar) rules out D-glucose (an aldose) and maltose (glucose units only); sucrose is a non-reducing disaccharide, not a keto sugar.
2. D-Fructose is a ketohexose found in honey, forms $\alpha$ and $\beta$ anomers, and is laevorotatory, satisfying A, B, C and D.
3. So $X$ = D-Fructose, which is option $3$.

**Subtopic:** Structure and Reactions of Fructose · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q078_62f120bd_12112026.png?v=62f120bd371e)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q078_f3577fab_12112026.png?v=f3577fab7ac1)

---

## Q79

Chemistry · physical · Basic Concepts of Chemistry

Dalton’s Atomic theory could not explain which of the following?

- **(1)** Law of gaseous volume
- (2) Law of conservation of mass
- (3) Law of constant proportion
- (4) Law of multiple proportion

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Dalton’s theory could explain the laws of chemical combination.
2. However, it could not explain the laws of gaseous volumes.

**Solved independently** (answer withheld)

1. Dalton's atomic theory accounts for the laws of conservation of mass, constant proportions and multiple proportions, but it could not explain Gay-Lussac's law of gaseous volumes, so the answer is option $1$.

**Subtopic:** Dalton’s Atomic Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q079_d9dc4f75_12112026.png?v=d9dc4f752fb3)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q079_676e22df_12112026.png?v=676e22df4194)

---

## Q80

Chemistry · physical · Chemical Equilibrium

Higher yield of NO in $\mathrm{N_2(g) + O_2(g) \rightleftharpoons 2NO(g)}$ can be obtained at [$\Delta H$ of the reaction $= +180.7\,\mathrm{kJ\,mol^{-1}}$] Choose the correct answer from the options given below :

- (A) Higher temperature
- (B) Lower temperature
- (C) Higher concentration of $\mathrm{N_2}$
- (D) Higher concentration of $\mathrm{O_2}$

- **(1)** A, C, D only
- (2) A, D only
- (3) B, C only
- (4) B, C, D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Yield of the product generally depends on
2. • Temperature
3. • Concentration of reactant(s) and product(s)
4. • Pressure
5. As this is an endothermic reaction ($\Delta H = +180.7\,\mathrm{kJ\,mol^{-1}}$), so, increase in temperature will shift equilibrium in forward direction to increase yield of $\mathrm{NO}$.
6. Increase in concentration of reactants ($\mathrm{N_2}$ and $\mathrm{O_2}$) also shifts the equilibrium in forward direction and increase the yield of $\mathrm{NO}$.
7. Hence, (A), (C) and (D) only will increase yield of $\mathrm{NO}$.

**Solved independently** (answer withheld)

1. $\Delta H = +180.7\,\mathrm{kJ\,mol^{-1}} > 0$, so the forward reaction is endothermic.
2. By Le Chatelier's principle, raising temperature favours the endothermic forward reaction, so higher temperature increases NO yield: A true, B false.
3. Increasing $[\mathrm{N_2}]$ shifts the equilibrium towards products: C true.
4. Increasing $[\mathrm{O_2}]$ likewise shifts the equilibrium towards products: D true.
5. A, C and D are correct, which is option $1$.

**Subtopic:** Le Chatelier's Principle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q080_2c19a47c_12112026.png?v=2c19a47ccf99)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q080_64dbc565_12112026.png?v=64dbc565de14)

---

## Q81

Chemistry · inorganic · The p–Block Elements

Match List-I with List-II

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{XeO_3}$ | I | $sp^3d$; linear |
| B | $\mathrm{XeF_2}$ | II | $sp^3$; pyramidal |
| C | $\mathrm{XeOF_4}$ | III | $sp^3d^3$; distorted octahedral |
| D | $\mathrm{XeF_6}$ | IV | $sp^3d^2$; square pyramidal |

- (1) A-IV, B-II, C-I, D-III
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-II, B-I, C-III, D-IV
- (4) A-IV, B-II, C-III, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Molecule | Hybridisation | Shape
2. $sp^{3}$ | Pyramidal
3. $sp^{3}d$ | Linear
4. $sp^{3}d^{2}$ | Square Pyramidal
5. $sp^{3}d^{3}$ | Distorted Octahedral

**Solved independently** (answer withheld)

1. $\mathrm{XeO_3}$: 3 bond pairs + 1 lone pair = 4 electron domains, so $sp^3$ and pyramidal: A-II.
2. $\mathrm{XeF_2}$: 2 bond pairs + 3 lone pairs = 5 domains, so $sp^3d$ and linear: B-I.
3. $\mathrm{XeOF_4}$: 5 bond pairs + 1 lone pair = 6 domains, so $sp^3d^2$ and square pyramidal: C-IV.
4. $\mathrm{XeF_6}$: 6 bond pairs + 1 lone pair = 7 domains, so $sp^3d^3$ and distorted octahedral: D-III.
5. A-II, B-I, C-IV, D-III matches option $2$.

**Subtopic:** Important Compounds of Xenon · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 40)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q081_185cfebf_12112026.png?v=185cfebf7a66)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q081_1c9a5130_12112026.png?v=1c9a5130c8f4)

---

## Q82

Chemistry · physical · Solutions

Match List-I with List-II
List-I (Example) | List-II (Type of Solution)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Humidity | I | Solid in solid |
| B | Alloys | II | Liquid in gas |
| C | Amalgams | III | Solid in gas |
| D | Smoke | IV | Liquid in solid |

- (1) A-III, B-II, C-I, D-IV
- (2) A-II, B-IV, C-I,D-III
- **(3)** A-II, B-I, C-IV, D-III
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Humidity is a solution of liquid in gas
2. Alloy is a solution of solid in solid
3. Amalgam is a solution of liquid in solid
4. Smoke is a solution of solid in gas

**Solved independently** (answer withheld)

1. Humidity is water (liquid) dispersed in air (gas), so $A \rightarrow II$ (liquid in gas).
2. Alloys (e.g. copper dissolved in gold) are solid in solid, so $B \rightarrow I$.
3. Amalgams (e.g. mercury in sodium) are liquid in solid, so $C \rightarrow IV$.
4. Smoke is solid particles in air, so $D \rightarrow III$ (solid in gas).
5. $A\text{-}II,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}III$ matches option $3$.

**Subtopic:** Types of Solutions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q082_d091318c_12112026.png?v=d091318c46c9)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q082_0ac90ce5_12112026.png?v=0ac90ce5e543)

---

## Q83

Chemistry · physical · Structure of Atom

Energy and radius of first Bohr orbit of $\mathrm{He^{+}}$ and $\mathrm{Li^{2+}}$ are [Given $R_{\mathrm{H}} = 2.18 \times 10^{-18}\,\mathrm{J}$, $a_{0} = 52.9\,\mathrm{pm}$]

- (1) $E_{n}(\mathrm{Li^{2+}}) = -8.72 \times 10^{-16}\,\mathrm{J}$; $r_{n}(\mathrm{Li^{2+}}) = 17.6\,\mathrm{pm}$ $E_{n}(\mathrm{He^{+}}) = -19.62 \times 10^{-16}\,\mathrm{J}$; $r_{n}(\mathrm{He^{+}}) = 17.6\,\mathrm{pm}$
- **(2)** $E_{n}(\mathrm{Li^{2+}}) = -19.62 \times 10^{-18}\,\mathrm{J}$; $r_{n}(\mathrm{Li^{2+}}) = 17.6\,\mathrm{pm}$ $E_{n}(\mathrm{He^{+}}) = -8.72 \times 10^{-18}\,\mathrm{J}$; $r_{n}(\mathrm{He^{+}}) = 26.4\,\mathrm{pm}$
- (3) $E_{n}(\mathrm{Li^{2+}}) = -8.72 \times 10^{-18}\,\mathrm{J}$; $r_{n}(\mathrm{Li^{2+}}) = 26.4\,\mathrm{pm}$ $E_{n}(\mathrm{He^{+}}) = -19.62 \times 10^{-18}\,\mathrm{J}$; $r_{n}(\mathrm{He^{+}}) = 17.6\,\mathrm{pm}$
- (4) $E_{n}(\mathrm{Li^{2+}}) = -19.62 \times 10^{-16}\,\mathrm{J}$; $r_{n}(\mathrm{Li^{2+}}) = 17.6\,\mathrm{pm}$ $E_{n}(\mathrm{He^{+}}) = -8.72 \times 10^{-16}\,\mathrm{J}$; $r_{n}(\mathrm{He^{+}}) = 26.4\,\mathrm{pm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $E_{n} = \frac{-2.18 \times 10^{-18} \times z^{2}}{n^{2}}\,\mathrm{J}$; $r_{n} = \frac{52.9 \times n^{2}}{z}\,\mathrm{pm}$
2. For $\mathrm{He^{+}}$
3. $E_{\mathrm{He^{+}}} = -2.18 \times 10^{-18} \times 4 = -8.72 \times 10^{-18}\,\mathrm{J}$
4. $r_{\mathrm{He^{+}}} = \frac{52.9 \times 1}{2} = 26.45\,\mathrm{pm}$
5. For $\mathrm{Li^{2+}}$
6. $E_{\mathrm{Li^{2+}}} = -2.18 \times 10^{-18} \times 9 = 19.62 \times 10^{-18}\,\mathrm{J}$
7. $r_{\mathrm{Li^{2+}}} = \frac{52.9 \times 1}{3} = 17.63\,\mathrm{pm}$

**Solved independently** (answer withheld)

1. For a hydrogen-like ion, $E_n = -R_H \frac{Z^2}{n^2}$ and $r_n = \frac{a_0 n^2}{Z}$; here $n = 1$.
2. $\mathrm{He^{+}}$ ($Z=2$): $E_1 = -2.18 \times 10^{-18} \times 4 = -8.72 \times 10^{-18}\,\mathrm{J}$.
3. $\mathrm{He^{+}}$: $r_1 = \frac{52.9}{2} = 26.45 \approx 26.4\,\mathrm{pm}$.
4. $\mathrm{Li^{2+}}$ ($Z=3$): $E_1 = -2.18 \times 10^{-18} \times 9 = -19.62 \times 10^{-18}\,\mathrm{J}$.
5. $\mathrm{Li^{2+}}$: $r_1 = \frac{52.9}{3} = 17.63 \approx 17.6\,\mathrm{pm}$.
6. These match option $2$.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q083_f2b209f5_12112026.png?v=f2b209f5edaf)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q083_e0c7c47e_12112026.png?v=e0c7c47e0085)

---

## Q84

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Which among the following electronic configurations belong to main group elements? Choose the correct answer from the option given below :

- (A) $\mathrm{[Ne]3s^{1}}$
- (B) $\mathrm{[Ar]3d^{3}4s^{2}}$
- (C) $\mathrm{[Kr]4d^{10}\,5s^{2}5p^{5}}$
- (D) $\mathrm{[Ar]3d^{10}4s^{1}}$
- (E) $\mathrm{[Rn]5f^{0}6d^{2}7s^{2}}$

- (1) A, C and D only
- (2) B and E only
- **(3)** A and C only
- (4) D and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) $\mathrm{[Ne]3s^{1}}$; $\mathrm{Na}$ (s-block)
2. (B) $\mathrm{[Ar]3d^{3}4s^{2}}$; $\mathrm{V}$ (d-block)
3. (C) $\mathrm{[Kr]4d^{10}5s^{2}5p^{5}}$; $\mathrm{I}$ (p-block)
4. (D) $\mathrm{[Ar]3d^{10}4s^{1}}$; $\mathrm{Cu}$ (d-block)
5. (E) $\mathrm{[Rn]5f^{0}6d^{2}7s^{2}}$; $\mathrm{Th}$ (f-block)
6. Main group elements (A and C only)

**Solved independently** (answer withheld)

1. Main group elements are the s-block and p-block elements.
2. $\mathrm{[Ne]3s^{1}}$ is Na, an s-block element, so A is main group.
3. $\mathrm{[Ar]3d^{3}4s^{2}}$ is V, a d-block element, so B is not.
4. $\mathrm{[Kr]4d^{10}5s^{2}5p^{5}}$ is I, a p-block element, so C is main group.
5. $\mathrm{[Ar]3d^{10}4s^{1}}$ is Cu (group 11), a d-block element, so D is not.
6. $\mathrm{[Rn]5f^{0}6d^{2}7s^{2}}$ is Th, an f-block element, so E is not.
7. Main group: A and C only, which is option $3$.

**Subtopic:** Electronic Configurations · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q084_d810ebc5_12112026.png?v=d810ebc524c9)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q084_d9085607_12112026.png?v=d90856073c29)

---

## Q85

Chemistry · physical · Thermodynamics

$\mathrm{C(s) + 2H_2(g) \rightarrow CH_4(g)}$; $\Delta H = -74.8\,\mathrm{kJ\,mol^{-1}}$. Which of the following diagrams gives an accurate representation of the above reaction? [R $\rightarrow$ reactants; P $\rightarrow$ products]

- (1) ![printed figure: energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at low energy, a hump, P higher than R; a double arrow labelled 74.8 spans from R level up to P level](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q085_option_1_eaaa69bc_12112026.png?v=eaaa69bc9755) *energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at low energy, a hump, P higher than R; a double arrow labelled 74.8 spans from R level up to P level*
- **(2)** ![printed figure: energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at higher energy, a hump, P lower than R; a double arrow labelled 74.8 spans from R level down to P level](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q085_option_2_2004aefa_12112026.png?v=2004aefad9bf) *energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at higher energy, a hump, P lower than R; a double arrow labelled 74.8 spans from R level down to P level*
- (3) ![printed figure: energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at low energy, a hump, P higher than R; a double arrow labelled 74.8 spans from the top of the hump down to P level](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q085_option_3_ab14ac79_12112026.png?v=ab14ac793918) *energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at low energy, a hump, P higher than R; a double arrow labelled 74.8 spans from the top of the hump down to P level*
- (4) ![printed figure: energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at higher energy, a hump, P lower than R; a double arrow labelled 74.8 spans from the top of the hump down to R level](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q085_option_4_eda8aa01_12112026.png?v=eda8aa015514) *energy profile diagram (Energy (kJ mol⁻¹) vs Reaction progress): R at higher energy, a hump, P lower than R; a double arrow labelled 74.8 spans from the top of the hump down to R level*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\Delta H = -74.8\,\mathrm{kJ\,mol^{-1}}$, it is an exothermic reaction.
2. So, accurate representation is

**Solved independently** (answer withheld)

1. $\Delta H = H_P - H_R = -74.8\,\mathrm{kJ\,mol^{-1}} < 0$, so the reaction is exothermic and $P$ lies below $R$.
2. Options $1$ and $3$ show $P$ above $R$ (endothermic), so they are wrong.
3. Option $4$ marks $74.8$ from the energy peak down to $P$, which is not $\Delta H$.
4. Option $2$ marks $74.8$ as the gap between $R$ and the lower $P$, matching $\Delta H$, so the answer is option $2$.

**Subtopic:** Standard Enthalpy of Reactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 43)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q085_e513172c_12112026.png?v=e513172c6b5c)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q085_b55cdc98_12112026.png?v=b55cdc98ccc4)

---

## Q86

Chemistry · organic · Amines

Predict the major product ‘P’ in the following sequence of reactions-

![printed figure: 1-methylcyclopentene →((i) HBr, benzoyl peroxide (ii) KCN (iii) Na (Hg)/C₂H₅OH) P (Major)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q086_6d12625d_12112026.png?v=6d12625d0ebc)

*1-methylcyclopentene →[(i) HBr, benzoyl peroxide (ii) KCN (iii) Na (Hg)/C₂H₅OH] P (Major)*

Structures: 1-methylcyclopentene `CC1=CCCC1`

- (1) 1-isocyano-1-methylcyclopentane `[C-]#[N+]C1(C)CCCC1`
- **(2)** (2-methylcyclopentyl)methanamine `CC1CCCC1CN`
- (3) (1-methylcyclopentyl)methanamine `CC1(CN)CCCC1`
- (4) 1-isocyano-2-methylcyclopentane `[C-]#[N+]C1CCCC1C`

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. With benzoyl peroxide, HBr adds anti-Markovnikov to 1-methylcyclopentene: Br goes to $C_2$ and H to $C_1$, giving 1-bromo-2-methylcyclopentane.
2. $KCN$ substitutes Br by $S_N2$ (C-attack of the ambident cyanide), giving 2-methylcyclopentane-1-carbonitrile ($R-C\equiv N$).
3. $Na(Hg)/C_2H_5OH$ (Mendius reduction) reduces $R-C\equiv N \rightarrow R-CH_2NH_2$.
4. P is 2-methylcyclopentylmethanamine: $CH_3$ and $CH_2NH_2$ on adjacent ring carbons, which is option $2$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 44)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q086_51a757c8_12112026.png?v=51a757c8d922)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q086_608b37cf_12112026.png?v=608b37cf748a)

---

## Q87

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the correct orders against the property mentioned
Choose the correct answer from the options given below:

- (A) $\mathrm{H_2O} > \mathrm{NH_3} > \mathrm{CHCl_3}$ – dipole moment
- (B) $\mathrm{XeF_4} > \mathrm{XeO_3} > \mathrm{XeF_2}$ – number of lone pairs on central atom
- (C) $\mathrm{O{-}H} > \mathrm{C{-}H} > \mathrm{N{-}O}$ – bond length
- (D) $\mathrm{N_2} > \mathrm{O_2} > \mathrm{H_2}$ – bond enthalpy

- (1) B, C only
- **(2)** A, D only
- (3) B, D only
- (4) A, C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A. $\mu\,(\mathrm{D})$: $\mathrm{H_2O}$ $1.85$
2. $\mathrm{NH_3}$ $1.47$
3. $\mathrm{CHCl_3}$ $1.04$
4. B. $\mathrm{XeF_4}$ : $2$ lone pairs of electron
5. $\mathrm{XeO_3}$ : $1$ lone pair of electron
6. $\mathrm{XeF_2}$ : $3$ lone pairs of electron
7. C. Order of Bond length :- $\mathrm{N{-}O} > \mathrm{C{-}H} > \mathrm{O{-}H}$
8. D. $\mathrm{N_2}$ Bond order is $3$
9. $\mathrm{H_2}$ Bond order is $1$
10. $\mathrm{O_2}$ Bond order is $2$

**Solved independently** (answer withheld)

1. Dipole moments: $\mu(\mathrm{H_2O}) \approx 1.85\,\mathrm{D} > \mu(\mathrm{NH_3}) \approx 1.47\,\mathrm{D} > \mu(\mathrm{CHCl_3}) \approx 1.04\,\mathrm{D}$, so A is correct.
2. Lone pairs on Xe: $\mathrm{XeF_4} = 2$, $\mathrm{XeO_3} = 1$, $\mathrm{XeF_2} = 3$; the order $2 > 1 > 3$ is not decreasing, so B is incorrect.
3. Bond lengths: $\mathrm{O{-}H} \approx 96\,\mathrm{pm} < \mathrm{C{-}H} \approx 109\,\mathrm{pm} < \mathrm{N{-}O}$, so C is incorrect.
4. Bond enthalpies: $\mathrm{N_2}\ (946) > \mathrm{O_2}\ (498) > \mathrm{H_2}\ (436)\,\mathrm{kJ\,mol^{-1}}$, so D is correct.
5. Correct statements are A and D only, which is option $2$.

**Subtopic:** Bond Parameters, Dipole Moment · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 44)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q087_56755fd1_12112026.png?v=56755fd14375)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q087_d8d539e8_12112026.png?v=d8d539e88367)

---

## Q88

Chemistry · organic · Isomerism in Organic Compounds

Total number of possible isomers (both structural as well as stereoisomers) of cyclic ethers of molecular formula $\mathrm{C_4H_8O}$ is :

- (1) 11
- (2) 6
- (3) 8
- **(4)** 10

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For cyclic ethers $\mathrm{O}$ should be in ring $*$ carbon here is chiral

**Solved independently** (answer withheld)

1. Five-membered ring: tetrahydrofuran, $1$ isomer.
2. Four-membered rings: 2-methyloxetane is chiral ($2$ enantiomers) and 3-methyloxetane is achiral ($1$), giving $3$.
3. Three-membered rings: ethyloxirane is chiral ($2$) and 2,2-dimethyloxirane is achiral ($1$).
4. 2,3-Dimethyloxirane: cis is meso ($1$) and trans is a chiral pair ($2$), giving $3$.
5. Oxiranes total $2 + 1 + 3 = 6$.
6. Total $= 1 + 3 + 6 = 10$, which is option $4$.

**Subtopic:** Optical Isomerism, Geometrical Isomerism · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 45)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q088_7662786b_12112026.png?v=7662786b1408)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q088_92ca527d_12112026.png?v=92ca527dc7ce)

---

## Q89

Chemistry · physical · Chemical Equilibrium

For the reaction $\mathrm{A(g) \rightleftharpoons 2B(g)}$, the backward reaction rate constant is higher than the forward reaction rate constant by a factor of $2500$, at $1000\,\mathrm{K}$. [Given : $R = 0.0831\,\mathrm{L\,atm\,mol^{-1}\,K^{-1}}$] $K_P$ for the reaction at $1000\,\mathrm{K}$ is

- (1) $0.021$
- (2) $83.1$
- (3) $2.077 \times 10^{5}$
- **(4)** $0.033$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $K_C = \frac{k_f}{k_b} = \frac{1}{2500}$
2. $K_P = K_C(RT)^{\Delta n_g}$ \quad $(\Delta n_g = 2 - 1 = 1)$
3. $= \frac{1}{2500} \times 0.0831 \times 1000$
4. $= 0.033$

**Solved independently** (answer withheld)

1. $K_c = \frac{k_f}{k_b} = \frac{1}{2500} = 4 \times 10^{-4}$.
2. $\Delta n_g = 2 - 1 = 1$.
3. $RT = 0.0831 \times 1000 = 83.1$.
4. $K_P = K_c (RT)^{\Delta n_g} = 4 \times 10^{-4} \times 83.1 = 0.0332 \approx 0.033$, which is option $4$.

**Subtopic:** Law of Chemical Equilibrium, Homogeneous and Heterogeneous Equilibria · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 46)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q089_ca7a1a81_12112026.png?v=ca7a1a81c29a)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q089_3407f4de_12112026.png?v=3407f4dec1ef)

---

## Q90

Chemistry · physical · Solutions

$5$ moles of liquid X and $10$ moles of liquid Y make a solution having a vapour pressure of $70\,\mathrm{torr}$. The vapour pressures of pure X and Y are $63\,\mathrm{torr}$ and $78\,\mathrm{torr}$ respectively. Which of the following is true regarding the described solution?

- (1) The solution has volume greater than the sum of individual volumes.
- (2) The solution shows positive deviation.
- **(3)** The solution shows negative deviation.
- (4) The solution is ideal.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $P_{\mathrm{total}} = X_x P_x^{\circ} + X_y P_y^{\circ}$
2. $= \frac{5}{15} \times 63 + \frac{10}{15} \times 78$
3. $= 21 + 52$
4. $= 73\,\mathrm{torr}$
5. Observed total pressure of solution is $70\,\mathrm{torr}$.
6. It is less than calculated total pressure.
7. Hence, it shows negative deviation.

**Solved independently** (answer withheld)

1. Total moles $= 5 + 10 = 15$, so $x_X = \frac{5}{15} = \frac{1}{3}$ and $x_Y = \frac{10}{15} = \frac{2}{3}$.
2. By Raoult's law, $P_{ideal} = x_X P_X^0 + x_Y P_Y^0 = \frac{1}{3}(63) + \frac{2}{3}(78)$.
3. $P_{ideal} = 21 + 52 = 73\,\mathrm{torr}$.
4. Observed $P = 70\,\mathrm{torr} < 73\,\mathrm{torr}$, so the solution shows negative deviation from Raoult's law, which is option $3$.

**Subtopic:** Ideal and Nonideal Solutions · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 46)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q090_47de2c61_12112026.png?v=47de2c614841)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q090_ba0f43db_12112026.png?v=ba0f43dba722)

---

## Q91

Biology · botany · Ecosystem

Which of the following is the unit of productivity of an Ecosystem?

- **(1)** $(\mathrm{KCal\,m^{-2}})\,\mathrm{yr^{-1}}$
- (2) $\mathrm{gm^{-2}}$
- (3) $\mathrm{KCal\,m^{-2}}$
- (4) $\mathrm{KCal\,m^{-3}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The rate of biomass production is called productivity.
2. It is expressed in terms of $\mathrm{g\,m^{-2}\,yr^{-1}}$ or $(\mathrm{KCal\,m^{-2}})\,\mathrm{yr^{-1}}$ to compare the productivity of different ecosystems.

**Solved independently** (answer withheld)

1. Productivity is the rate of biomass or energy production per unit area over a time period, so its unit needs area and time: $(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, which is option $1$; options $2$, $3$ and $4$ have no time term.

**Subtopic:** Productivity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 47)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q091_f4dd345e_12112026.png?v=f4dd345e0b28)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q091_475b4ece_12112026.png?v=475b4ece86fa)

---

## Q92

Biology · zoology · Human Reproduction

The first menstruation is called :

- (1) Ovulation
- (2) Menopause
- **(3)** Menarche
- (4) Diapause

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The first menstruation begins at puberty and is called menarche.
2. Ovulation is the process that deals with the release of secondary oocyte from the mature Graafian follicle.
3. In human beings, menstrual cycles ceases around $50$ years of age; that is termed as menopause.
4. Diapause is a state of dormancy or developmental arrest in an organism.

**Solved independently** (answer withheld)

1. The first menstruation, which begins at puberty, is called menarche, which is option $3$.

**Subtopic:** Menstrual Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q092_d8fab440_12112026.png?v=d8fab440494b)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q092_934ab60a_12112026.png?v=934ab60ac155)

---

## Q93

Biology · zoology · Animal Kingdom

Given below are two statements: one is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the correct answer from the options given below:

- Assertion (A) All vertebrates are chordates but all chordates are not vertebrate.
- Reason (R) The members of subphylum vertebrata possess notochord during the embryonic period, the notochord is replaced by cartilaginous or bony vertebral column in adults.

- (1) (A) is false but (R) is true
- **(2)** Both (A) and (R) are true and (R) is the correct explanation of (A)
- (3) Both (A) and (R) are true but (R) is not the correct explanation of (A)
- (4) (A) is true but (R) is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Both (A) and (R) are true and (R) is the correct explanation of (A).
2. The members of subphylum vertebrata possess notochord during the embryonic period. The notochord is replaced by a cartilaginous or bony vertebral column in the adult.
3. Thus, all vertebrates are chordates but all chordates are not vertebrates.

**Solved independently** (answer withheld)

1. Assertion (A) is true: every vertebrate has a notochord at some stage, so it is a chordate, but urochordates and cephalochordates are chordates without a vertebral column.
2. Reason (R) is true: in vertebrates the embryonic notochord is replaced by a cartilaginous or bony vertebral column in adults.
3. R gives the feature that makes a chordate a vertebrate, so R correctly explains A, which is option $2$.

**Subtopic:** Phylum – Chordata · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 47)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q093_2e21d154_12112026.png?v=2e21d154e37b)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q093_f987d1f0_12112026.png?v=f987d1f051ea)

---

## Q94

Biology · both · Principles of Inheritance and Variation

Genes R and Y follow independent assortment. If RRYY produce round yellow seeds and rryy produce wrinkled green seeds, what will be the phenotypic ratio of the F2 generation?

- (1) Phenotypic ratio - $9 : 7$
- (2) Phenotypic ratio - $1 : 2 : 1$
- (3) Phenotypic ratio - $3 : 1$
- **(4)** Phenotypic ratio - $9 : 3 : 3 : 1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A classical dihybrid cross performed by Mendel involves.
2. A cross which was made between a pure round yellow seeded pea plant (RRYY) with wrinkled green seeded plant (rryy).
3. Yellow colour is dominant over green and round seed shape over wrinkled seed shape.
4. Phenotypic ratio in F2 generation

**Solved independently** (answer withheld)

1. Cross $RRYY \times rryy$ gives F1 all $RrYy$ (round yellow).
2. Selfing $RrYy$ with independent assortment: each gene segregates $3:1$ in phenotype.
3. Combined ratio $(3:1)\times(3:1) = 9:3:3:1$, which is option $4$.

**Subtopic:** Inheritance of Two Genes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q094_4a44e86b_12112026.png?v=4a44e86b4c53)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q094_3f3f7006_12112026.png?v=3f3f70068c73)

---

## Q95

Biology · both · Biotechnology: Principles and Processes

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) The DNA fragments extracted from gel electrophoresis can be used in construction of recombinant DNA.
- (Statement II) Smaller size DNA fragments are observed near anode while larger fragments are found near the wells in an agarose gel.

- (1) Statement I is incorrect but statement II is correct
- **(2)** Both statement I and statement II are correct
- (3) Both statement I and statement II are incorrect
- (4) Statement I is correct but statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The cutting of DNA by restriction endonucleases results in the fragments of DNA.
2. These fragments can be separated by a technique known as gel electrophoresis.
3. The separated bands of DNA are cut out from the agarose gel and extracted from the gel piece.
4. This step is known as elution.
5. The DNA fragments purified in this way are used in constructing rDNA by joining them with cloning vectors.
6. In gel electrophoresis, the DNA fragments separate (resolve) according to their size through sieving effect provided by the agarose gel.
7. Hence, the smaller  the fragment size, the farther it moves from cathode towards anode.

**Solved independently** (answer withheld)

1. Statement I: separated DNA bands are cut out of the agarose gel and extracted (elution), and these purified fragments are used to construct recombinant DNA, so Statement I is correct.
2. Statement II: DNA is negatively charged and moves toward the anode; the gel sieves the fragments, so smaller ones move further (nearer the anode) and larger ones stay near the wells. Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q095_2e9039d7_12112026.png?v=2e9039d74992)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q095_b4e392a4_12112026.png?v=b4e392a43e82)

---

## Q96

Biology · both · Cell Cycle and Cell Division

What is the main function of the spindle fibers during mitosis?

- (1) To regulate cell growth
- **(2)** To separate the chromosomes
- (3) To synthesize new DNA
- (4) To repair damaged DNA

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. During mitosis, spindle fibre get attach to the kinetochores of the chromosome and help in the separation of the chromosome.

**Solved independently** (answer withheld)

1. Spindle fibres attach to the kinetochores of chromosomes and, in anaphase, pull the sister chromatids to opposite poles, so their function is to separate the chromosomes (option $2$).

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q096_4f3b107d_12112026.png?v=4f3b107d70de)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q096_36c0eba8_12112026.png?v=36c0eba8ef57)

---

## Q97

Biology · botany · Sexual Reproduction in Flowering Plants

How many meiotic and mitotic divisions need to occur for the development of a mature female gametophyte from the megaspore mother cell in an angiosperm plant?

- (1) No Meiosis and 2 Mitosis
- (2) 2 Meiosis and 3 Mitosis
- (3) 1 Meiosis and 2 Mitosis
- **(4)** 1 Meiosis and 3 Mitosis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Development of a mature female gametophyte, i.e., embryo sac from a megaspore mother cell in an angiosperm plant requires $1$ meiotic and $3$ mitotic divisions.

**Solved independently** (answer withheld)

1. The megaspore mother cell divides by $1$ meiosis to form a tetrad of $4$ megaspores, of which $1$ is functional.
2. The functional megaspore nucleus divides mitotically: $1 \to 2 \to 4 \to 8$ nuclei, i.e. $3$ mitotic divisions.
3. Total: $1$ meiosis and $3$ mitosis, which is option $4$.

**Subtopic:** Megasporangium (Ovule) and Embryo Sac, Megasporogenesis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q097_8bb49cc7_12112026.png?v=8bb49cc7b517)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q097_a194181c_12112026.png?v=a194181c5730)

---

## Q98

Biology · zoology · Human Health and Disease

Identify the statement that is NOT correct.

- (1) Constant region of heavy and light chains are located at C-terminus of antibody molecules
- (2) Each antibody has two light and two heavy chains.
- (3) The heavy and light chains are held together by disulfide bonds.
- **(4)** Antigen binding site is located at C-terminal region of antibody molecules.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Each antibody molecule has four peptide chains, two small called light chains and two longer called heavy chains.
2. Hence, an antibody is represented as $\mathrm{H_2L_2}$.
3. In an antibody molecule, antigen binding site is located at N-terminal region.

**Solved independently** (answer withheld)

1. An antibody is $H_2L_2$: two heavy and two light chains, held together by disulfide bonds, so statements $2$ and $3$ are correct.
2. The constant regions of both chains lie toward the C-terminus, so statement $1$ is correct.
3. The antigen binding site is formed by the variable regions at the N-terminus, so statement $4$ is NOT correct, which is option $4$.

**Subtopic:** Acquired Immunity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q098_f39ea7f1_12112026.png?v=f39ea7f1c867)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q098_6c4328a1_12112026.png?v=6c4328a1b06f)

---

## Q99

Biology · zoology · Human Reproduction

Consider the following :

- (A) The reductive division for the human female gametogenesis starts earlier than that of the male gametogenesis.
- (B) The gap between the first meiotic division and the second meiotic division is much shorter for males compared to females.
- (C) The first polar body is associated with the formation of the primary oocyte.
- (D) Luteinizing Hormone (LH) surge leads to disintegration of the endometrium and onset of menstrual bleeding.

- (1) B and C are true
- **(2)** A and B are true
- (3) A and C are true
- (4) B and D are true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Statements A and B are true while statements C and D are false.
2. The first polar body is associated with the formation of the secondary oocyte LH surge leads to ovulation.
3. Decreased levels of progesterone during late luteal phase leads to degeneration of the endometrium and onset of menstrual bleeding.

**Solved independently** (answer withheld)

1. Statement A: oogonia enter meiosis I (reductive division) during fetal life, while spermatogonia begin meiosis only at puberty, so $A$ is true.
2. Statement B: secondary spermatocytes complete meiosis II almost immediately, whereas the secondary oocyte stays arrested until ovulation/fertilisation, so $B$ is true.
3. Statement C: the first polar body is released when the primary oocyte completes meiosis I, forming the secondary oocyte, so $C$ is false.
4. Statement D: the LH surge induces ovulation; menstruation results from degeneration of the corpus luteum and fall in progesterone, so $D$ is false.
5. Only $A$ and $B$ are true, which is option $2$.

**Subtopic:** Female Gametogenesis (Oogenesis), Male Gametogenesis (Spermatogenesis) · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 49)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q099_1f63674f_12112026.png?v=1f63674f16df)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q099_a508e4aa_12112026.png?v=a508e4aaaf82)

---

## Q100

Biology · botany · Sexual Reproduction in Flowering Plants

> ⚠ A is NCERT verbatim. NCERT says the tapetum nourishes the developing POLLEN GRAINS; R says it nourishes the developing MICROSPORE MOTHER CELLS. The key (4, A true but R false) reads R as false on that word; the blind solve took R as a loose restatement of NCERT and chose (2). The publisher's own solution explains A with R's idea ("increases the efficiency of nourishing the developing pollen grains"), so the key rests only on that one word.

> ⚠ The independent solve chose (2); the booklet prints (4).

Given below are two statements : One is labelled as Assertion (A) and other is labelled as Reason (R). In light of the above statements, choose the most appropriate answer from the options given below:

- Assertion (A) Cells of the tapetum possess dense cytoplasm and generally have more than one nucleus.
- Reason (R) Presence of more than one nucleus in the tapetum increases the efficiency of nourishing the developing microspore mother cells.

- (1) A is false but R is true
- (2) Both A and R are true and R is the correct explanation of A
- (3) Both A and R are true but R is NOT the correct explanation of A
- **(4)** A is true but R is false

**Answer** — booklet: (4) · independent solve: (2) · differs

**Publisher's solution**

1. Cell of the tapetum possess dense cytoplasm and generally have more than one nucleus because the presence of more than one nucleus in the tapetal cells increases the efficiency of nourishing the develpoing pollen grains.

**Solved independently** (answer withheld)

1. Assertion: the tapetum (innermost anther wall layer) has cells with dense cytoplasm and generally more than one nucleus, so $A$ is true.
2. Reason: the tapetum's function is to nourish the developing microsporocytes and pollen grains; more nuclei increase its metabolic and nutritive capacity, so $R$ is true.
3. $R$ gives the functional basis of the multinucleate condition stated in $A$, so $R$ explains $A$: option $2$.

**Subtopic:** Microsporangium and Microsporogenesis · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 49)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q100_e6ceef1d_12112026.png?v=e6ceef1df30c)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q100_10419563_12112026.png?v=104195634852)

---

## Q101

Biology · both · Biotechnology: Principles and Processes

The blue and white selectable markers have been developed which differentiate recombinant colonies from non-recombinant colonies on the basis of their ability to produce colour in the presence of a chromogenic substrate. Given below are two statements about this method: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The blue coloured colonies have DNA insert in the plasmid and they are identified as recombinant colonies.
- (Statement II) The colonies without blue colour have DNA insert in the plasmid and are identified as recombinant colonies.

- **(1)** Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Statement I is incorrect but statement II is correct as a recombinant DNA is inserted within the coding sequence of an enzyme, $\beta$-galactosidase.
2. This results into inactivation of the gene for synthesis of this enzyme.
3. Thus, presence of insert results into insertional inactivation of the $\beta$-galactosidase gene and the colonies do not produce any colour and identified as recombinant colonies.
4. Whereas non-recombinant transformants will produce blue colour in presence of chromogenic substrate.

**Solved independently** (answer withheld)

1. The DNA insert is ligated within the coding sequence of the $\beta$-galactosidase gene, causing insertional inactivation.
2. Recombinant colonies therefore cannot act on the chromogenic substrate and give no blue colour (white colonies).
3. Non-recombinant colonies have an intact $\beta$-galactosidase gene and produce blue colonies, so Statement I is incorrect.
4. Colonies without blue colour carry the insert and are recombinants, so Statement II is correct; this is option $1$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 50)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q101_235cad1b_12112026.png?v=235cad1b0654)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q101_0e5594ef_12112026.png?v=0e5594ef4f85)

---

## Q102

Biology · botany · Plant Kingdom

In bryophytes, the gemmae help in which one of the following?

- (1) Gaseous exchange
- (2) Sexual reproduction
- **(3)** Asexual reproduction
- (4) Nutrient absorption

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Gemmae are green, multicellular, asexual buds which develop in small receptacles called gemma cups and help in asexual reproduction in bryophytes.

**Solved independently** (answer withheld)

1. Gemmae are green, multicellular asexual buds formed in gemma cups on the thallus of liverworts such as $Marchantia$; they detach and germinate into new individuals, so they serve asexual reproduction (option $3$).

**Subtopic:** Liverworts · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 50)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q102_953610ab_12112026.png?v=953610abb4b5)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q102_261d9747_12112026.png?v=261d9747a335)

---

## Q103

Biology · both · Biomolecules

Match List I with List II: Choose the option with all correct matches.

| List-I | | List-II | |
|---|---|---|---|
| A | Adenosine | I | Nitrogen base |
| B | Adenylic acid | II | Nucleotide |
| C | Adenine | III | Nucleoside |
| D | Alanine | IV | Amino acid |

- (1) A-II, B-III, C-I, D-IV
- (2) A-III, B-IV, C-II, D-I
- (3) A-III, B-II, C-IV, D-I
- **(4)** A-III, B-II, C-I, D-IV

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is A-III, B-II, C-I, D-IV
2. Adenosine – It is a nucleoside which is composed of nitrogen base and sugar only.
3. Adenylic acid – It is a nucleotide which is composed of nitrogen base, sugar and a phosphate group is esterified to the sugar.
4. Adenine – Nitrogen base (Purine)
5. Alanine – An amino acid that contains a methyl group as the ‘R’ group.

**Solved independently** (answer withheld)

1. Adenosine = adenine + ribose sugar, so it is a nucleoside: $A \rightarrow III$.
2. Adenylic acid = adenosine + phosphate, so it is a nucleotide: $B \rightarrow II$.
3. Adenine is a purine nitrogen base: $C \rightarrow I$.
4. Alanine is an amino acid: $D \rightarrow IV$.
5. The match $A-III, B-II, C-I, D-IV$ is option $4$.

**Subtopic:** Nucleic Acid · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q103_ff111eb9_12112026.png?v=ff111eb97d75)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q103_12516788_12112026.png?v=12516788cb3f)

---

## Q104

Biology · both · Principles of Inheritance and Variation

With the help of given pedigree, find out the probability for the birth of a child having no disease and being a carrier (has the disease mutation in one allele of the gene) in $\mathrm{F_3}$ generation.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q104_cb922232_12112026.png?v=cb922232321a)

- (1) Zero
- **(2)** $1/4$
- (3) $1/2$
- (4) $1/8$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. As in the $\mathrm{F_1}$ generation the carrier female and non-affected (normal, not carrier) had affected male child that means the genetic disorder is sex-linked recessive.
2. The consanguineous mating between female ($\mathrm{X^{c}X}$) and male ($\mathrm{X^{c}Y}$)
3. Out of $4$ child only one is carrier i.e. $\frac{1}{4}$.

**Solved independently** (answer withheld)

1. Only females are shown as carriers and the affected F0 mother has carrier daughters, so the trait is X-linked recessive.
2. The F2 parents are a carrier female $X^AX^a$ and an affected male $X^aY$.
3. Cross: $X^AX^a \times X^aY \rightarrow X^AX^a,\ X^aX^a,\ X^AY,\ X^aY$, each with probability $\frac{1}{4}$.
4. Only $X^AX^a$ is free of disease and a carrier, so $P = \frac{1}{4}$, which is option $2$.

**Subtopic:** Pedigree Analysis · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 51)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q104_e7142f5c_12112026.png?v=e7142f5c8f9c)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q104_65b091cd_12112026.png?v=65b091cdb0d0)

---

## Q105

Biology · zoology · Chemical Coordination and Integration

Consider the following statements regarding function of adrenal medullary hormones : Choose the correct answer from the options given below :

- (A) It causes pupilary constriction.
- (B) It is a hyperglycemic hormone.
- (C) It causes piloerection.
- (D) It increases strength of heart contraction.

- (1) D only
- (2) C and D only
- **(3)** B, C and D only
- (4) A, C and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Adrenal medulla secretes two hormones called adrenaline or epinephrine and noradrenaline or norepinephrine (also called emergency hormones).
2. Both the hormones -
3. Cause pupillary dilation (not constriction)
4. Stimulate breakdown of glycogen resulting in increased concentration of glucose in blood i.e., cause hyperglycemia.
5. Cause piloerection (raising of hair).
6. Increase strength of heart contraction i.e., heartbeat.

**Solved independently** (answer withheld)

1. Catecholamines (emergency hormones) cause pupillary dilation, so statement A (constriction) is false.
2. They stimulate glycogenolysis and raise blood glucose, so they are hyperglycemic: B is true.
3. They cause piloerection (raising of hairs): C is true.
4. They increase heart beat and the strength of heart contraction: D is true.
5. True statements are B, C and D, which is option $3$.

**Subtopic:** Adrenal Gland · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 51)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q105_1fdbdceb_12112026.png?v=1fdbdceb8eee)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q105_2fc51bd3_12112026.png?v=2fc51bd3ce3d)

---

## Q106

Biology · botany · Morphology of Flowering Plants

Which of the following is an example of a zygomorphic flower?

- (1) Chilli
- (2) Petunia
- (3) Datura
- **(4)** Pea

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Zygomorphic flowers can be divided into two equal halves by only a single vertical plane and shows bilateral symmetry.
2. Pea possess zygomorphic flowers.
3. Chilli, Petunia and Datura possess actinomorphic flowers.

**Solved independently** (answer withheld)

1. NCERT: zygomorphic flowers (one plane of symmetry) include pea, gulmohur, bean, cassia; actinomorphic include mustard, datura, chilli. Petunia (Solanaceae) is also actinomorphic, so pea is option $4$.

**Subtopic:** The Flower · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q106_78bf9181_12112026.png?v=78bf91818e52)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q106_18c3bb54_12112026.png?v=18c3bb542f01)

---

## Q107

Biology · both · Molecular Basis of Inheritance

Who proposed that the genetic code for amino acids should be made up of three nucleotides?

- (1) Franklin Stahl
- **(2)** George Gamow
- (3) Francis Crick
- (4) Jacque Monod

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. George Gamow, a physicist proposed that genetic code for amino acids should be made up of three nucleotides.

**Solved independently** (answer withheld)

1. NCERT states that George Gamow proposed the code must be a combination of three nucleotides, since $4^2 = 16 < 20$ while $4^3 = 64 \geq 20$ amino acids, which is option $2$.

**Subtopic:** Genetic Code and Its Features · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 52)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q107_0e89e2ef_12112026.png?v=0e89e2ef5c42)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q107_65b5e835_12112026.png?v=65b5e8356e80)

---

## Q108

Biology · botany · Ecosystem

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) In ecosystem, there is unidirectional flow of energy of sun from producers to consumers.
- (Statement II) Ecosystems are exempted from $2^{\text{nd}}$ law of thermodynamics.

- (1) Statement I is incorrect but statement II is correct
- (2) Both statement I and statement II are correct
- (3) Both statement I and statement II are incorrect
- **(4)** Statement I is correct but statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sun is the only source of energy for all ecosystems on Earth, except for deep sea-hydro-thermal ecosystem.
2. The energy flow is unidirectional from the sun to producers and then to consumers.
3. Ecosystems are not exempted from the second law of thermodynamics. They need a constant supply of energy to synthesise the molecules they require to counteract the universal tendency towards increasing disorderliness.

**Solved independently** (answer withheld)

1. Statement I: energy from the sun flows one way, producers to consumers, so it is correct.
2. Statement II: ecosystems obey the $2^{\text{nd}}$ law of thermodynamics and need a constant energy supply, so it is incorrect.
3. I correct, II incorrect, which is option $4$.

**Subtopic:** Energy Flow · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q108_db70212d_12112026.png?v=db70212d4a64)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q108_fb62eff1_12112026.png?v=fb62eff157af)

---

## Q109

Biology · both · Evolution

Sweet potato and potato represent a certain type of evolution. Select the correct combination of terms to explain the evolution.

- (1) Analogy, divergent
- **(2)** Analogy, convergent
- (3) Homology, divergent
- (4) Homology, convergent

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sweet potato is a root modification while potato is a stem modification but both of them have same function.
2. Analogous structures are not anatomically similar structures though they perform similar functions.
3. Analogous structures are the result of convergent evolution.
4. Homologous organs are anatomically similar but they do not perform similar function.
5. Homologous organs are the result of divergent evolution.

**Solved independently** (answer withheld)

1. Sweet potato is a modified root and potato is a modified stem tuber; both store food, so they have the same function but different origins. Such organs are analogous, and analogy comes from convergent evolution, which is option $2$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 53)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q109_b1ecfaf4_12112026.png?v=b1ecfaf47eb0)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q109_dd778337_12112026.png?v=dd7783373ade)

---

## Q110

Biology · zoology · Animal Kingdom

All living members of the class Cyclostomata are :

- **(1)** Ectoparasite
- (2) Free living
- (3) Endoparasite
- (4) Symbiotic

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. All living members of class Cyclostomata are ectoparasites.

**Solved independently** (answer withheld)

1. NCERT Class 11 states that all living members of class Cyclostomata are ectoparasites on some fishes, so the answer is option $1$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 53)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q110_c5fb6e7b_12112026.png?v=c5fb6e7b20df)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q110_8ade79a0_12112026.png?v=8ade79a05485)

---

## Q111

Biology · both · Molecular Basis of Inheritance

Histones are enriched with -

- (1) Phenylalanine & Arginine
- **(2)** Lysine & Arginine
- (3) Leucine & Lysine
- (4) Phenylalanine & Leucine

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In eukaryotes, packaging of DNA is much more complex. There is a set of positively charged, basic proteins called histones.
2. Histones are organised to form a unit of light molecules called histone octamer.
3. They are rich in the basic amino acid residues lysine and arginine.

**Solved independently** (answer withheld)

1. Histones are positively charged because they are rich in the basic amino acids lysine and arginine, which is option $2$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q111_f40771f9_12112026.png?v=f40771f9243b)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q111_39c744cc_12112026.png?v=39c744cc04ad)

---

## Q112

Biology · botany · Organisms and Populations

Which one of the following equations represents the Verhulst-Pearl Logistic Growth of population?

- (1) $\dfrac{dN}{dt}=N\left(\dfrac{r-K}{K}\right)$
- (2) $\dfrac{dN}{dt}=r\left(\dfrac{K-N}{K}\right)$
- **(3)** $\dfrac{dN}{dt}=rN\left(\dfrac{K-N}{K}\right)$
- (4) $\dfrac{dN}{dt}=rN\left(\dfrac{N-K}{N}\right)$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Logistic growth is described by Verhulst-Pearl logistic growth equation $\frac{dN}{dt} = rN\left(\frac{K - N}{K}\right)$.

**Solved independently** (answer withheld)

1. The Verhulst-Pearl logistic growth equation is $\frac{dN}{dt} = rN\left(\frac{K-N}{K}\right)$, where $r$ is the intrinsic rate of natural increase and $K$ is the carrying capacity; this matches option $3$.

**Subtopic:** Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q112_d2be1384_12112026.png?v=d2be138441b2)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q112_6ec62d7c_12112026.png?v=6ec62d7c100d)

---

## Q113

Biology · both · Cell: The Unit of Life

> ⚠ Both A and R are true (NCERT, Golgi apparatus). Whether R (cis-to-trans flow of vesicles) is the correct explanation of A (packaging and delivery) is a judgement call: the key says no (3), the blind solve said yes (2). The publisher's solution gives no reason beyond saying it does not explain A.

> ⚠ The independent solve chose (2); the booklet prints (3).

Given below are two statements : one is labelled as Assertion (A), and the other is labelled as Reason (R). In the light of the above statements, choose the correct answer from the options given below :

- Assertion (A) The primary function of the Golgi apparatus is to package the materials made by the endoplasmic reticulum and deliver it to intracellular targets and outside the cell.
- Reason (R) Vesicles containing materials made by the endoplasmic reticulum fuse with the cis face of the Golgi apparatus, and they are modified and released from the trans face of the Golgi apparatus.

- (1) A is false but R is true
- (2) Both A and R are true and R is the correct explanation of A
- **(3)** Both A and R are true but R is not the correct explanation of A
- (4) A is true but R is false

**Answer** — booklet: (3) · independent solve: (2) · differs

**Publisher's solution**

1. The primary function of Golgi apparatus is to package the materials made by endoplasmic reticulum and deliver it to intracellular targets and outside the cell, this statement is correct and the reason statement is also correct.
2. Golgi apparatus remains in close association with endoplasmic reticulum.
3. Here, assertion and reason statements both are correct but reason is not correctly explaining assertion.

**Solved independently** (answer withheld)

1. Assertion (A): NCERT states the Golgi apparatus principally packages materials made by the ER and delivers them to intracellular targets and outside the cell, so $A$ is true.
2. Reason (R): ER vesicles fuse with the cis (forming) face; their contents are modified in the cisternae and released from the trans (maturing) face, so $R$ is true.
3. R gives the route by which the Golgi receives, processes and dispatches ER products, i.e. the mechanism of the packaging function in A, so $R$ explains $A$: option $2$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 54)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q113_324b8862_12112026.png?v=324b88627734)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q113_a8de8527_12112026.png?v=a8de85273d91)

---

## Q114

Biology · botany · Photosynthesis in Higher Plants

Which of the following statements about RuBisCO is true?

- **(1)** It catalyzes the carboxylation of RuBP
- (2) It is active only in the dark
- (3) It has higher affinity for oxygen than carbon dioxide
- (4) It is an enzyme involved in the photolysis of water

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Carboxylation is the most crucial step of the Calvin cycle where $\mathrm{CO_2}$ is utilised for the carboxylation of RuBP.
2. This reaction is catalysed by enzyme RuBP carboxylase.
3. Since this enzyme also has an oxygenase activity, RuBisCO has higher affinity for carbon dioxide than oxygen.

**Solved independently** (answer withheld)

1. RuBisCO fixes $\mathrm{CO_2}$ by carboxylating RuBP: $\mathrm{RuBP + CO_2 \rightarrow 2\,PGA}$, so option $1$ is true; it is not dark-only, has higher affinity for $\mathrm{CO_2}$ than $\mathrm{O_2}$, and photolysis of water is done by the PS II water-splitting complex, so options $2$, $3$, $4$ are false.

**Subtopic:** The Calvin Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q114_7fa5bc70_12112026.png?v=7fa5bc700058)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q114_c6de9e87_12112026.png?v=c6de9e87c36e)

---

## Q115

Biology · zoology · Chemical Coordination and Integration

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Progesterone | I | Pars intermedia |
| B | Relaxin | II | Ovary |
| C | Melanocyte stimulating hormone | III | Adrenal Medulla |
| D | Catecholamines | IV | Corpus luteum |

- (1) A-III, B-II, C-IV, D-I
- **(2)** A-IV, B-II, C-I, D-III
- (3) A-IV, B-II, C-III, D-I
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is [A-IV, B-II, C-I, D-III]
2. Progesterone – A steroidal hormone which is secreted by the corpus luteum
3. Relaxin – A proteinaceous hormone which is secreted by the ovaries in the later stage of pregnancy
4. Melanocyte stimulating hormone – A proteinaceous hormone released by the pars intermedia
5. Catecholamines – An amino-acid derived hormone released from the adrenal medulla during emergency conditions

**Solved independently** (answer withheld)

1. Progesterone (A) is secreted mainly by the corpus luteum, so $A \to IV$.
2. Relaxin (B) is secreted by the ovary in later pregnancy, so $B \to II$.
3. Melanocyte stimulating hormone (C) is secreted by the pars intermedia of the pituitary, so $C \to I$.
4. Catecholamines (D) are secreted by the adrenal medulla, so $D \to III$.
5. $A$-$IV$, $B$-$II$, $C$-$I$, $D$-$III$ matches option $2$.

**Subtopic:** Endocrine Glands and Hormones and System of Human Endocrine · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 54)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q115_08e62fbb_12112026.png?v=08e62fbbd4aa)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q115_11202f2f_12112026.png?v=11202f2f73be)

---

## Q116

Biology · both · Biomolecules

The protein portion of an enzyme is called:

- (1) Prosthetic group
- (2) Cofactor
- (3) Coenzyme
- **(4)** Apoenzyme

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. There are number of cases in which non-protein constituents called co-factors are bound to the enzyme to make the enzyme catalytically active.
2. In these instances, the protein portion of the enzymes is called the apoenzyme.
3. Three kinds of co-factors are identified prosthetic groups, co-enzymes and metal ions.
4. Prosthetic groups are organic compounds and they are tightly bound with apoenzyme.
5. Co-enzymes are also organic compounds but their association with apoenzyme is only transient.

**Solved independently** (answer withheld)

1. A holoenzyme consists of a protein part, the $\text{apoenzyme}$, plus a non-protein $\text{cofactor}$ (prosthetic group, coenzyme or metal ion), so the protein portion is the apoenzyme, option $4$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q116_591841df_12112026.png?v=591841df518c)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q116_309272fd_12112026.png?v=309272fdcb0b)

---

## Q117

Biology · both · Biotechnology: Principles and Processes

Which of the following enzyme(s) are NOT essential for gene cloning?
Choose the correct answer from the options given below:

- (A) Restriction enzymes
- (B) DNA ligase
- (C) DNA mutase
- (D) DNA recombinase
- (E) DNA polymerase

- (1) B and C only
- **(2)** C and D only
- (3) A and B only
- (4) D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Gene cloning is a process where a specific gene or DNA sequence is isolated and replicated, creating multiple identical copies.
2. In gene cloning, restriction enzymes, DNA ligase and DNA polymerase are primarily used.

**Solved independently** (answer withheld)

1. Restriction enzymes (A) cut DNA at specific sites, so they are essential for cloning.
2. DNA ligase (B) joins the insert to the vector, so it is essential.
3. DNA polymerase (E) amplifies the gene of interest (PCR), which NCERT lists as a tool of recombinant DNA technology.
4. DNA mutase (C) and DNA recombinase (D) are not among the essential cloning enzymes, so the answer is C and D only, option $2$.

**Subtopic:** Tools of Recombinant DNA Technology · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q117_9f728e15_12112026.png?v=9f728e152a1a)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q117_26a91a22_12112026.png?v=26a91a22cbf3)

---

## Q118

Biology · zoology · Human Health and Disease

Which of the following type of immunity is present at the time of birth and is a non-specific type of defence in the human body?

- (1) Humoral Immunity
- (2) Acquired Immunity
- **(3)** Innate Immunity
- (4) Cell-mediated Immunity

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Innate immunity is non-specific type of defence, that is present at the time of birth.
2. This is accomplished by providing different types of barriers to the entry of the foreign agents into our body.
3. Acquired immunity is pathogen specific, characterised by memory cells.
4. Immune response mediated by B-lymphocytes is humoral immunity and other immune response mediated by T-lymphocytes is called cell-mediated immunity.

**Solved independently** (answer withheld)

1. Innate immunity is present at the time of birth and gives non-specific defence, while acquired immunity (humoral and cell-mediated) is pathogen-specific, so the answer is option $3$.

**Subtopic:** Innate Immunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q118_c9cb6672_12112026.png?v=c9cb66723aed)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q118_62d2dde1_12112026.png?v=62d2dde170d5)

---

## Q119

Biology · both · Molecular Basis of Inheritance

Which factor is important for termination of transcription?

- (1) $\gamma$ (gamma)
- (2) $\alpha$ (alpha)
- (3) $\sigma$ (sigma)
- **(4)** $\rho$ (rho)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In prokaryotes the RNA polymerase is only capable of catalysing the process of elongation.
2. It associates transiently with initiation factor ($\sigma$) and termination factor ($\rho$) to initiate and terminate the transcription respectively.

**Solved independently** (answer withheld)

1. NCERT: RNA polymerase associates transiently with $\sigma$ factor for initiation and with $\rho$ (rho) factor for termination of transcription, so the answer is option $4$.

**Subtopic:** Transcription · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 56)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q119_614f5bfa_12112026.png?v=614f5bfa64d7)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q119_fe444153_12112026.png?v=fe444153b950)

---

## Q120

Biology · zoology · Chemical Coordination and Integration

Which of the following hormones released from the pituitary is actually synthesized in the hypothalamus?

- (1) Adrenocorticotropic hormone (ACTH)
- (2) Luteinizing hormone (LH)
- **(3)** Anti-diuretic hormone (ADH)
- (4) Follicle-stimulating hormone (FSH)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Neurohypophysis i.e., posterior pituitary (Pars nervosa) stores and releases two hormones called oxytocin and vasopressin (Also called ADH i.e., antidiuretic hormone) which are actually synthesised by hypothalamus and are transported axonally to neurohypophysis.
2. The pars distalis (anterior pituitary) produces follicle stimulating hormone (FSH), adrenocorticotropic hormone (ACTH) and luteinizing hormone (LH).

**Solved independently** (answer withheld)

1. The neurohypophysis (posterior pituitary) only stores and releases oxytocin and vasopressin (ADH), which are synthesized in the hypothalamus; ACTH, LH and FSH are synthesized in the adenohypophysis, so the answer is option $3$.

**Subtopic:** The Pituitary Gland, The Hypothalamus · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q120_32f9bb4a_12112026.png?v=32f9bb4a155a)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q120_84d96e97_12112026.png?v=84d96e97406e)

---

## Q121

Biology · botany · Microbes in Human Welfare

Which of the following microbes is NOT involved in the preparation of household products? Choose the correct answer from the options given below:

- (A) Aspergillus niger
- (B) Lactobacillus
- (C) Trichoderma polysporum
- (D) Saccharomyces cerevisiae
- (E) Propionibacterium sharmanii

- (1) C and E only
- (2) A and B only
- **(3)** A and C only
- (4) C and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Lactobacillus is used for production of curd.
2. Saccharomyces cerevisiae is used for the fermentation of palm sap to obtain toddy drink.
3. Propionibacterium sharmanii is used for production of swiss cheese.
4. Aspergillus niger is used for the commercial production of citric acid.
5. Trichoderma polysporum is used for the production of cyclosporin A and also act as a biocontrol agent.
6. A, C are used in industrial production of citric acid and cyclosporin-A.

**Solved independently** (answer withheld)

1. Household products per NCERT: Lactobacillus makes curd (B), Saccharomyces cerevisiae makes bread dough rise (D), Propionibacterium sharmanii gives Swiss cheese its holes (E).
2. Aspergillus niger (A) is used industrially for citric acid production, not household products.
3. Trichoderma polysporum (C) is used industrially to produce the immunosuppressant cyclosporin A, not household products.
4. So the microbes not involved are A and C only, which is option $3$.

**Subtopic:** Microbes in Household Products · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q121_429da41f_12112026.png?v=429da41f89ed)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q121_dc096242_12112026.png?v=dc096242fc45)

---

## Q122

Biology · botany · Organisms and Populations

> ⚠ Statement I (fig is a "non-vegetarian" fruit) is a popular claim, not science, so it is incorrect. Statement II describes fig-wasp mutualism as in NCERT, but says the fig FRUIT gets pollinated; the publisher marks it incorrect on that word (the inflorescence/flower is pollinated) and keys (3), both incorrect. The blind solve read II as the NCERT mutualism example and chose (1).

> ⚠ The independent solve chose (1); the booklet prints (3).

Given below are two statements :
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) Fig fruit is a non-vegetarian fruit as it has enclosed fig wasps in it.
- (Statement II) Fig wasp and fig tree exhibit mutual relationship as fig wasp completes its life cycle in fig fruit and fig fruit gets pollinated by fig wasp.

- (1) Statement I is incorrect but statement II is correct
- (2) Both statement I and statement II are correct
- **(3)** Both statement I and statement II are incorrect
- (4) Statement I is correct but statement II is incorrect

**Answer** — booklet: (3) · independent solve: (1) · differs

**Publisher's solution**

1. Fig fruit is a vegetarian fruit as it only gets pollinated by wasp.
2. Fig tree and fig wasps shows mutualism in which both species are benefitted.
3. So, statement I is incorrect.
4. Statement II is also not correct as fig inflorescence/flower gets pollinated by fig wasp.

**Solved independently** (answer withheld)

1. Statement II: NCERT cites the fig-wasp pair as mutualism: the female wasp pollinates the fig inflorescence while using the fruit for egg laying and larval development, so Statement II is correct.
2. Statement I: a fig is a plant fruit; the presence of wasps inside does not make it a 'non-vegetarian fruit', so this is not a valid biological statement and Statement I is incorrect.
3. Statement I incorrect and Statement II correct matches option $1$.

**Subtopic:** Mutualism · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 57)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q122_d0467e02_12112026.png?v=d0467e02b6dc)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q122_5558df55_12112026.png?v=5558df55ee3f)

---

## Q123

Biology · zoology · Animal Kingdom

Role of the water vascular system in Echinoderms is :
Choose the correct answer from the options given below :

- (A) Respiration and Locomotion
- (B) Excretion and Locomotion
- (C) Capture and transport of food
- (D) Digestion and Respiration
- (E) Digestion and Excretion

- (1) B, D and E Only
- (2) A and B Only
- **(3)** A and C Only
- (4) B and C Only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Water vascular system in Echinoderms helps in locomotion, capture and transport of food and respiration.
2. Excretory system is absent in echinoderms. Excretion takes place through general body surface.

**Solved independently** (answer withheld)

1. NCERT states the water vascular system of echinoderms helps in locomotion, capture and transport of food, and respiration, so A and C are correct while B, D and E (excretion, digestion) are not; this is option $3$ (A and C Only).

**Subtopic:** Phylum – Echinodermata and Hemichordata · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 57)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q123_6da82a76_12112026.png?v=6da82a76b9e9)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q123_28dbab81_12112026.png?v=28dbab8180db)

---

## Q124

Biology · zoology · Human Health and Disease

After maturation, in primary lymphoid organs, the lymphocytes migrate for interaction with antigens to secondary lymphoid organ(s) / tissue(s) like
Choose the correct answer from the options given below

- (A) thymus
- (B) bone marrow
- (C) spleen
- (D) lymph nodes
- (E) Peyer’s patches

- **(1)** C, D, E only
- (2) B, C, D only
- (3) A, B, C only
- (4) E, A, B only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The primary lymphoid organs are bone marrow and thymus where immature lymphocytes differentiate into antigen-sensitive lymphocytes.
2. After maturation, the lymphocytes migrate into secondary lymphoid organs like spleen, lymph nodes, Peyer’s patches of small intestine and appendix.
3. These secondary lymphoid organ provide the sites for interaction of lymphocytes with the antigen.

**Solved independently** (answer withheld)

1. Thymus (A) and bone marrow (B) are primary lymphoid organs, where lymphocytes mature, so they are excluded.
2. Spleen (C), lymph nodes (D) and Peyer's patches (E, MALT) are secondary lymphoid organs/tissues where mature lymphocytes interact with antigens.
3. So the set is $C, D, E$ only, which is option $1$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 57)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q124_1371eaf5_12112026.png?v=1371eaf5b6c4)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q124_68030cd1_12112026.png?v=68030cd1ae17)

---

## Q125

Biology · botany · Biodiversity and Conservation

Match List I with List II: Choose the option with all correct matches.

| List-I | | List-II | |
|---|---|---|---|
| A | The Evil Quartet | I | Cryopreservation |
| B | Ex situ conservation | II | Alien species invasion |
| C | Lantana camara | III | Causes of biodiversity losses |
| D | Dodo | IV | Extinction |

- (1) A-III, B-II, C-IV, D-I
- (2) A-III, B-II, C-I, D-IV
- **(3)** A-III, B-I, C-II, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The Evil Quartet – Causes of biodiversity losses
2. Ex situ conservation – Cryopreservation
3. Lantana camara – Alien species invasion
4. Dodo – Extinction

**Solved independently** (answer withheld)

1. The Evil Quartet names the four major causes of biodiversity loss, so $A \rightarrow III$.
2. Cryopreservation of gametes is an ex situ conservation method, so $B \rightarrow I$.
3. \textit{Lantana camara} is an alien species invasion example, so $C \rightarrow II$.
4. The Dodo of Mauritius is an example of extinction, so $D \rightarrow IV$.
5. $A-III, B-I, C-II, D-IV$ is option $3$.

**Subtopic:** Causes of Biodiversity Losses, Ex Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q125_fa0f4543_12112026.png?v=fa0f454365f5)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q125_e0ec44fd_12112026.png?v=e0ec44fd82fb)

---

## Q126

Biology · botany · Plant Growth and Development

Read the following statements on plant growth and development.

Choose the option with all correct statements.

- (A) Parthenocarpy can be induced by auxins.
- (B) Plant growth regulators can be involved in promotion as well as inhibition of growth.
- (C) Dedifferentiation is a pre-requisite for re-differentiation.
- (D) Abscisic acid is a plant growth promoter.
- (E) Apical dominance promotes the growth of lateral buds.

- (1) B, D, E only
- **(2)** A, B, C only
- (3) A, C, E only
- (4) A, D, E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. ABA is a plant growth inhibitor and an inhibitor of plant metabolism.
2. Apical dominance promotes growth of apical bud.
3. Statements A, B and C are correct.

**Solved independently** (answer withheld)

1. $A$: auxins induce parthenocarpy, so $A$ is true.
2. $B$: plant growth regulators include promoters and inhibitors, so $B$ is true.
3. $C$: redifferentiation is the change undergone by dedifferentiated cells, so dedifferentiation must come first and $C$ is true.
4. $D$: abscisic acid is a growth inhibitor, so $D$ is false.
5. $E$: apical dominance suppresses the growth of lateral buds, so $E$ is false.
6. True set $\{A, B, C\}$ matches option $2$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins, Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q126_5bac4a38_12112026.png?v=5bac4a385fca)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q126_66fc5ae7_12112026.png?v=66fc5ae7b4bf)

---

## Q127

Biology · botany · Plant Kingdom

Match List-I with List-II. Choose the option with all correct matches.

| List-I | | List-II | |
|---|---|---|---|
| A | Pteridophyte | I | Salvia |
| B | Bryophyte | II | Ginkgo |
| C | Angiosperm | III | Polytrichum |
| D | Gymnosperm | IV | Salvinia |

- (1) A-IV, B-III, C-II, D-I
- (2) A-III, B-IV, C-II, D-I
- **(3)** A-IV, B-III, C-I, D-II
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pteridophyte - Salvinia
2. Bryophyte - Polytrichum
3. Angiosperm - Salvia
4. Gymnosperm - Ginkgo

**Solved independently** (answer withheld)

1. Pteridophyte (A): $Salvinia$ is a water fern, so $A \to IV$.
2. Bryophyte (B): $Polytrichum$ is a moss, so $B \to III$.
3. Angiosperm (C): $Salvia$ is a flowering plant, so $C \to I$.
4. Gymnosperm (D): $Ginkgo$ is a gymnosperm, so $D \to II$.
5. $A$-IV, $B$-III, $C$-I, $D$-II matches option $3$.

**Subtopic:** Pteridophytes, Gymnosperms · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q127_07e168dc_12112026.png?v=07e168dcf804)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q127_bffa82d0_12112026.png?v=bffa82d0240b)

---

## Q128

Biology · both · Biotechnology and Its Applications

Why can’t insulin be given orally to diabetic patients?

- (1) Its bioavailability will be increased
- (2) Human body will elicit strong immune response
- **(3)** It will be digested in Gastro-Intestinal (GI) tract
- (4) Because of structural variation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Insulin can’t be administered orally to diabetic patients as being the proteinaceous molecule, it will be digested in gastro-intestinal tract.

**Solved independently** (answer withheld)

1. Insulin is a polypeptide hormone, so if taken orally it would be broken down by proteases in the gastro-intestinal tract; hence it is injected, which is option $3$.

**Subtopic:** Genetically Engineered Insulin · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q128_feb4fb0b_12112026.png?v=feb4fb0b5398)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q128_3e3d1b36_12112026.png?v=3e3d1b36c4f3)

---

## Q129

Biology · botany · Plant Kingdom

Which one of the following is the characteristic feature of gymnosperms?

- (1) Gymnosperms have flowers for reproduction
- (2) Seeds are enclosed in fruits
- **(3)** Seeds are naked
- (4) Seeds are absent

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The gymnosperms (Gymnos : naked, sperma seed) are plants in which the ovules are not enclosed by an ovary wall and remains exposed, both before and after fertilization.
2. The seeds that develop post-fertilization, are not covered, i.e., naked.

**Solved independently** (answer withheld)

1. Gymnosperms (gymnos = naked, sperma = seed) have ovules that are not enclosed by an ovary wall, so after fertilisation the seeds stay exposed: seeds are naked, option $3$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q129_9721f088_12112026.png?v=9721f08877f4)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q129_34c60d01_12112026.png?v=34c60d01227e)

---

## Q130

Biology · zoology · Structural Organisation in Animals

Frogs respire in water by skin and buccal cavity and on land by skin, buccal cavity and lungs. Choose the **correct** answer from the following :

- (1) The statement is false for both the environment
- (2) The statement is true for water but false for land
- (3) The statement is true for both the environment
- **(4)** The statement is false for water but true for land

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In water, frogs respire through skin and not through buccal cavity i.e., undergo cutaneous respiration only.
2. On land, the buccal cavity, skin and lungs act as respiratory organs i.e., undergo buccopharyngeal , cutaneous and pulmonary respiration.

**Solved independently** (answer withheld)

1. In water, the frog's skin is the only respiratory organ (cutaneous respiration), so the claim of skin and buccal cavity in water is false.
2. On land, the buccal cavity, skin and lungs all act as respiratory organs, so that part of the statement is true.
3. False for water, true for land matches option $4$.

**Subtopic:** Anatomy of Frog · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q130_b0d11b3e_12112026.png?v=b0d11b3e6cda)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q130_8c6d2dca_12112026.png?v=8c6d2dca2faa)

---

## Q131

Biology · both · Biotechnology and Its Applications

Silencing of specific mRNA is possible via RNAi because of

- (1) Non-complementary ssRNA
- **(2)** Complementary dsRNA
- (3) Inhibitory ssRNA
- (4) Complementary tRNA

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. RNAi (RNA interference) takes place in all eukaryotic organisms as a method of cellular defense.
2. This method involves silencing of a specific mRNA due to a complementary dsRNA molecule that binds to and prevents translation of the mRNA.

**Solved independently** (answer withheld)

1. In RNA interference, a complementary $\text{dsRNA}$ binds to the specific mRNA and stops its translation, so the answer is option $2$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q131_2cca1007_12112026.png?v=2cca100707ed)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q131_389cdae2_12112026.png?v=389cdae294a2)

---

## Q132

Biology · zoology · Human Reproduction

Twins are born to a family that lives next door to you. The twins are a boy and a girl. Which of the following must be true?

- (1) They have $75\%$ identical genetic content.
- (2) They are monozygotic twins.
- **(3)** They are fraternal twins.
- (4) They were conceived through in vitro fertilization.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Fraternal twins or dizygotic twins are $2$ separate fertilized eggs, they usually develop $2$ separate amniotic sacs, placentas and supporting structures.
2. If twins are a boy and a girl, this indicates they are fraternal twins.

**Solved independently** (answer withheld)

1. Monozygotic twins arise from a single zygote, so they carry the same sex chromosomes and are always the same sex.
2. The twins here are a boy ($XY$) and a girl ($XX$), so they cannot come from one zygote; option $2$ is ruled out.
3. Hence they developed from two separately fertilised ova, i.e. they are fraternal (dizygotic) twins, which is option $3$; they share about $50\%$ genes like ordinary siblings (not $75\%$), and IVF is not required.

**Subtopic:** Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q132_40812b4b_12112026.png?v=40812b4b9638)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q132_b967fe02_12112026.png?v=b967fe025a1c)

---

## Q133

Biology · botany · Sexual Reproduction in Flowering Plants

Match List I with List II :
Choose the option with all correct matches.

| List-I | | List-II | |
|---|---|---|---|
| A | Scutellum | I | Persistent nucellus |
| B | Non-albuminous seed | II | Cotyledon of Monocot seed |
| C | Epiblast | III | Groundnut |
| D | Perisperm | IV | Rudimentary cotyledon |

- (1) A-II, B- IV, C-III, D-I
- **(2)** A-II, B- III, C-IV, D-I
- (3) A-IV, B- III, C-II, D-I
- (4) A-IV, B- III, C-I, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Scutellum is cotyledon of monocot seed.
2. Groundnut seed is non-albuminous seed.
3. Epiblast is rudimentary cotyledon in monocot seed.
4. Perisperm is persistent nucellus.

**Solved independently** (answer withheld)

1. Scutellum is the single cotyledon of the monocot (grass) embryo, so A-II.
2. Groundnut has no residual endosperm, so it is a non-albuminous seed: B-III.
3. Epiblast is a rudimentary second cotyledon in some grasses: C-IV.
4. Perisperm is the residual, persistent nucellus (e.g. black pepper, beet): D-I.
5. The match A-II, B-III, C-IV, D-I is option $2$.

**Subtopic:** Embryo and Seed · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q133_d2334bb5_12112026.png?v=d2334bb5aa88)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q133_a421c1bf_12112026.png?v=a421c1bf74b8)

---

## Q134

Biology · zoology · Structural Organisation in Animals

In frog, the Renal portal system is a special venous connection that acts to link :

- **(1)** Kidney and lower part of body
- (2) Liver and intestine
- (3) Liver and kidney
- (4) Kidney and intestine

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In frogs, special venous connection between liver and intestine as well as the kidney and lower parts of the body are present in frogs.
2. The former is called hepatic portal system and the latter is called renal portal system.

**Solved independently** (answer withheld)

1. In frog, the hepatic portal system links the liver and intestine, while the renal portal system links the kidney and the lower parts of the body, so the answer is option $1$.

**Subtopic:** Anatomy of Frog · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 60)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q134_eab656dd_12112026.png?v=eab656ddd506)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q134_2d648515_12112026.png?v=2d648515ed9f)

---

## Q135

Biology · zoology · Chemical Coordination and Integration

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Heart | I | Erythropoietin |
| B | Kidney | II | Aldosterone |
| C | Gastro-intestinal tract | III | Atrial natriuretic factor |
| D | Adrenal Cortex | IV | Secretin |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-II, B-I, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-I, B-III, C-IV, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Organ Name - Hormone Secreted
2. Heart - Atrial natriuretic factor
3. Kidney - Erythropoietin
4. Gastro-intestinal tract - Secretin
5. Adrenal cortex - Aldosterone

**Solved independently** (answer withheld)

1. Heart (atrial wall) secretes atrial natriuretic factor: A-III.
2. Kidney (juxtaglomerular cells) secretes erythropoietin: B-I.
3. Gastro-intestinal tract (duodenum) secretes secretin: C-IV.
4. Adrenal cortex secretes the mineralocorticoid aldosterone: D-II.
5. A-III, B-I, C-IV, D-II is option $1$.

**Subtopic:** Hormones of Heart, Kidney and Gastrointestinal Tract · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 61)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q135_768d5d88_12112026.png?v=768d5d8834ad)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q135_9b9c7527_12112026.png?v=9b9c7527dde9)

---

## Q136

Biology · zoology · Body Fluids and Circulation

Cardiac activities of the heart are regulated by: Choose the correct answer from the options given below :

- (A) Nodal tissue
- (B) A special neural centre in the medulla oblongata
- (C) Adrenal medullary hormones
- (D) Adrenal cortical hormones

- (1) A, B and D Only
- **(2)** A, B and C Only
- (3) A, B, C and D
- (4) A, C and D Only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Normal cardiac activities of the heart are regulated intrinsically, i.e., auto regulated by specialised muscles (nodal tissue), hence the heart is called myogenic.
2. A special neural centre in the medulla oblongata can moderate the cardiac function through autonomic nervous system.
3. Sympathetic nervous system can increase the rate of heartbeat, ventricular contraction and thereby cardiac output.
4. Parasympathetic neural signals decrease the rate of heartbeat, speed of conduction of action potential and thereby the cardiac output.
5. Adrenal medullary hormones can also increase the cardiac output.

**Solved independently** (answer withheld)

1. Normal cardiac activity is regulated intrinsically (auto-regulated) by the specialised nodal tissue, so $A$ is correct.
2. A special neural centre in the medulla oblongata moderates cardiac function through the autonomic nervous system, so $B$ is correct.
3. Adrenal medullary hormones (adrenaline, noradrenaline) increase heart rate and cardiac output, so $C$ is correct.
4. Adrenal cortical hormones are not described as regulators of cardiac activity, so $D$ is incorrect.
5. $A, B$ and $C$ only, which is option $2$.

**Subtopic:** Regulation of Cardiac Activity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 61)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q136_d7704342_12112026.png?v=d77043421746)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q136_ae7bc2ae_12112026.png?v=ae7bc2aeb7d0)

---

## Q137

Biology · botany · Microbes in Human Welfare

Streptokinase produced by bacterium Streptococcus is used for

- **(1)** Removing clots from blood vessels
- (2) Curd production
- (3) Ethanol production
- (4) Liver disease treatment

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Streptokinase produced by the bacterium Streptococcus and modified by genetic engineering is used as a ‘clot buster’ for removing clots from blood vessels of patients who have undergone myocardial infarction leading to heart attack.
2. Curd production is done by Lactobacillus and ethanol production is done by Saccharomyces.

**Solved independently** (answer withheld)

1. Streptokinase (from Streptococcus, modified by genetic engineering) is a clot buster that dissolves clots in blood vessels, so the answer is option $1$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q137_adbdbab9_12112026.png?v=adbdbab9399b)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q137_ee87c2d6_12112026.png?v=ee87c2d68c13)

---

## Q138

Biology · botany · Organisms and Populations

Who is known as the father of Ecology in India?

- (1) Birbal Sahni
- (2) S.R. Kashyap
- **(3)** Ramdeo Misra
- (4) Ram Udar

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ramdeo Misra is known as the father of Ecology in India.

**Solved independently** (answer withheld)

1. NCERT Class 12 (Organisms and Populations) names Ramdeo Misra as the Father of Ecology in India, so the answer is option $3$.

**Subtopic:** Introduction of Organisms, Populations and Their Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q138_500eeaad_12112026.png?v=500eeaadcc35)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q138_c44272e9_12112026.png?v=c44272e94259)

---

## Q139

Biology · botany · Sexual Reproduction in Flowering Plants

Given below are two statements : One is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the correct answer from the options given below :

- Assertion (A) A typical unfertilised, angiosperm embryo sac at maturity is 8 nucleate and 7-celled.
- Reason (R) The egg apparatus has 2 polar nuclei.

- (1) A is false but R is true
- (2) Both A and R are true and R is the correct explanation of A
- (3) Both A and R are true but R is NOT the correct explanation of A
- **(4)** A is true but R is false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A typical Angiosperm embryo sac, at maturity is $7$-celled and $8$ nucleate.
2. Polar nuclei are situated below the egg apparatus in the large central cell.
3. Three cells are grouped together at micropylar end and constitute the egg apparatus.
4. Hence, A is true but R is false.

**Solved independently** (answer withheld)

1. A mature angiosperm embryo sac has 3 antipodals, 2 synergids, 1 egg cell and 1 central cell with 2 polar nuclei: $8$ nuclei in $7$ cells, so A is true.
2. The egg apparatus consists of the egg cell and $2$ synergids; the $2$ polar nuclei belong to the central cell, so R is false.
3. A is true but R is false, which is option $4$.

**Subtopic:** Megasporangium (Ovule) and Embryo Sac · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 62)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q139_3ca35981_12112026.png?v=3ca35981785e)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q139_a4eb4ea6_12112026.png?v=a4eb4ea6a7df)

---

## Q140

Biology · zoology · Human Health and Disease

Neoplastic characteristics of cells refer to :
Choose the correct answer from the options given below:

- (A) A mass of proliferating cell
- (B) Rapid growth of cells
- (C) Invasion and damage to the surrounding tissue
- (D) Those confined to original location

- (1) B, C, D only
- (2) A, B only
- **(3)** A, B, C only
- (4) A, B, D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer will include : A, B and C only.
2. A neoplasm is a general term for any abnormal growth of tissue.
3. Neoplastic characteristics of cells refer to
4. (1) A mass of proliferating cell.
5. (2) Rapid growth of cells.
6. (3) Invasion and damage to the surrounding tissue.
7. Cancer specifically refers to malignant neoplasms, which are cancerous and invasive.
8. Benign tumours remain confined to their original location. Thus, D is not included in the answer.
9. The malignant tumours, on the other hand are a mass of proliferating cells called neoplastic or tumour cells.
10. These cells grow very rapidly, invading and damaging the surrounding normal tissues.

**Solved independently** (answer withheld)

1. Neoplastic (malignant) tumours are masses of proliferating cells that grow rapidly, so A and B are true.
2. Malignant cells invade and damage the surrounding normal tissue, so C is true.
3. Remaining confined to the original location is a feature of benign tumours, so D is false.
4. Hence A, B, C only, which is option $3$.

**Subtopic:** Cancer · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 62)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q140_a748b118_12112026.png?v=a748b118ac46)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q140_354e5fe8_12112026.png?v=354e5fe8fe69)

---

## Q141

Biology · botany · Plant Kingdom

Given below are the stages in the life cycle of pteridophytes. Arrange the following stages in the correct sequence. Choose the correct answer from the options given below:

- (A) Prothallus stage
- (B) Meiosis in spore mother cells
- (C) Fertilisation
- (D) Formation of archegonia and antheridia in gametophyte.
- (E) Transfer of antherozoids to the archegonia in presence of water.

- (1) E, D, C, B, A
- **(2)** B, A, D, E, C
- (3) B, A, E, C, D
- (4) D, E, C, A, B

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In a pteridophytes life cycle, the correct sequence of stages will be given as follows:
2. B $\rightarrow$ Meiosis in spore mother cells
3. A $\rightarrow$ Prothallus stage
4. D $\rightarrow$ Formation of archegonia and antheridia in gametophyte
5. E $\rightarrow$ Transfer of antherozoids to the archegonia in presence of water
6. C $\rightarrow$ Fertilisation will occur
7. So, the correct sequence is B $\rightarrow$ A $\rightarrow$ D $\rightarrow$ E $\rightarrow$ C

**Solved independently** (answer withheld)

1. Meiosis in spore mother cells of the sporophyte produces spores: stage $B$ comes first.
2. Spores germinate into the gametophyte, the prothallus: stage $A$.
3. The prothallus bears antheridia and archegonia: stage $D$.
4. Antherozoids are transferred to archegonia in the presence of water: stage $E$.
5. Fertilisation follows: stage $C$. Sequence $B, A, D, E, C$ is option $2$.

**Subtopic:** Pteridophytes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 63)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q141_16d7f908_12112026.png?v=16d7f9081e81)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q141_61722a55_12112026.png?v=61722a55bf37)

---

## Q142

Biology · botany · Sexual Reproduction in Flowering Plants

Given below are two statements : One is labelled as Assertion (A) and the other is labelled as Reason (R). In the light of the above statements, choose the correct answer from the options given below:

- Assertion (A) Both wind and water pollinated flowers are not very colourful and do not produce nectar.
- Reason (R) The flowers produce enormous amount of pollen grains in wind and water pollinated flowers.

- (1) A is false but R is true
- (2) Both A and R are true and R is the correct explanation of A
- **(3)** Both A and R are true but R is NOT the correct explanation of A
- (4) A is true but R is false

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Both wind and water pollinated flowers are not very colourful and do not produce nectar, this is because they rely on wind and water to carry their pollen.
2. Wind and water pollinated flower do not need to attract insect, so they did not evolve to produce bright coloured flower.

**Solved independently** (answer withheld)

1. Assertion (A): wind- and water-pollinated flowers do not need to attract animal pollinators, so they are not very colourful and do not produce nectar; A is true.
2. Reason (R): such flowers produce enormous numbers of pollen grains to compensate for pollen wastage during abiotic transfer; R is true.
3. The absence of colour and nectar is explained by the absence of animal pollinators, not by the large pollen output, so R is not the correct explanation of A: option $3$.

**Subtopic:** Agents of Pollination · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 63)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q142_95b48836_12112026.png?v=95b4883619c3)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q142_a06a6094_12112026.png?v=a06a6094313f)

---

## Q143

Biology · both · Biomolecules

Which one of the following enzymes contains ‘Haem’ as the prosthetic group?

- **(1)** Catalase
- (2) RuBisCo
- (3) Carbonic anhydrase
- (4) Succinate dehydrogenase

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In peroxidase and catalase, which catalyze the breakdown of hydrogen peroxide to water and oxygen, haem is the prosthetic group and it is part of the active site of the enzymes.
2. Zinc is the cofactor in enzyme carbonic anhydrase.
3. RuBisCo is the most abundant protein in whole of the biosphere.
4. Succinate is the substrate of enzyme succinic dehydrogenase.

**Solved independently** (answer withheld)

1. NCERT lists haem as the prosthetic group of peroxidase and catalase, which break down $H_2O_2$; the other enzymes use $Zn^{2+}$, $Mg^{2+}$ or FAD, so the answer is option $1$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 64)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q143_a2c39df1_12112026.png?v=a2c39df10703)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q143_1d6ad258_12112026.png?v=1d6ad258cfce)

---

## Q144

Biology

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Emphysema | I | Rapid spasms in muscle due to low $\mathrm{Ca^{++}}$ in body fluid |
| B | Angina Pectoris | II | Damaged alveolar walls and decreased respiratory surface |
| C | Glomerulonephritis | III | Acute chest pain when not enough oxygen is reaching to heart muscle |
| D | Tetany | IV | Inflammation of glomeruli of kidney |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-III, B-I, C-IV, D-II
- (3) A-III, B-I, C-II, D-IV
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Emphysema - Damaged alveolar walls and decreased respiratory surface
2. Angina pectoris - Acute chest pain when not enough oxygen is reaching to heart muscle
3. Glomerulonephritis - Inflammation of glomeruli of kidney
4. Tetany - Rapid spasms in muscle due to low $\mathrm{Ca^{++}}$ in body fluid

**Solved independently** (answer withheld)

1. Emphysema: alveolar walls are damaged, decreasing respiratory surface, so $A \rightarrow II$.
2. Angina pectoris: acute chest pain when not enough oxygen reaches heart muscle, so $B \rightarrow III$.
3. Glomerulonephritis: inflammation of glomeruli of kidney, so $C \rightarrow IV$.
4. Tetany: rapid muscle spasms due to low $\mathrm{Ca^{++}}$ in body fluid, so $D \rightarrow I$.
5. $A-II, B-III, C-IV, D-I$ matches option $1$.

**Subtopic:** — · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 64)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q144_db7aa729_12112026.png?v=db7aa729c5ca)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q144_a685bc07_12112026.png?v=a685bc07d0ee)

---

## Q145

Biology · botany · Anatomy of Flowering Plants

Find the statement that is NOT correct with regard to the structure of monocot stem.

- (1) Phloem parenchyma is absent.
- **(2)** Hypodermis is parenchymatous.
- (3) Vascular bundles are scattered.
- (4) Vascular bundles are conjoint and closed.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In monocot stem, hypodermis is sclerenchymatous.

**Solved independently** (answer withheld)

1. Per NCERT, the monocot stem has a sclerenchymatous hypodermis, scattered conjoint closed vascular bundles and no phloem parenchyma, so the incorrect statement is that the hypodermis is parenchymatous, option $2$.

**Subtopic:** Dicotyledonous and Monocotyledonous Stem · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 64)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q145_c86d5eb9_12112026.png?v=c86d5eb9d700)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q145_b47cbdcc_12112026.png?v=b47cbdcc0330)

---

## Q146

Biology · zoology · Structural Organisation in Animals

Which of the following statement is correct about location of the male frog copulatory pad?

- **(1)** First digit of the fore limb
- (2) First and Second digit of fore limb
- (3) First digit of hind limb
- (4) Second digit of fore limb

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In male frogs, copulatory pad is present on the first digit of the forelimbs which are absent in female frogs.

**Solved independently** (answer withheld)

1. In male frogs the copulatory (nuptial) pad lies on the first digit of the fore limb, which is option $1$.

**Subtopic:** Morphology of Frog · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 65)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q146_2479a14a_12112026.png?v=2479a14a08ae)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q146_33dd412d_12112026.png?v=33dd412d0037)

---

## Q147

Biology · botany · Ecosystem

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The primary source of energy in an ecosystem is solar energy.
- (Statement II) The rate of production of organic matter during photosynthesis in an ecosystem is called net primary productivity (NPP).

- (1) Statement I is incorrect but statement II is correct
- (2) Both statement I and statement II are correct
- (3) Both statement I and statement II are incorrect
- **(4)** Statement I is correct but statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Primary source of energy in the ecosystem is solar energy.
2. Gross primary productivity of an ecosystem is the rate of production of organic matter during photosynthesis.
3. Hence, statement I is correct but statement II is incorrect.

**Solved independently** (answer withheld)

1. Statement I: solar energy is the only/primary source of energy for nearly all ecosystems, so Statement I is correct.
2. Statement II: the rate of production of organic matter during photosynthesis is gross primary productivity (GPP), while $NPP = GPP - R$, so Statement II is incorrect.
3. I correct, II incorrect corresponds to option $4$.

**Subtopic:** Productivity, Energy Flow · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q147_78e76fbb_12112026.png?v=78e76fbb483b)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q147_286fe628_12112026.png?v=286fe628c433)

---

## Q148

Biology · both · Biotechnology: Principles and Processes

Identify the part of a bio-reactor which is used as a foam braker from the given figure.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q148_a045838f_12112026.png?v=a045838f5b94)

- **(1)** C
- (2) A
- (3) B
- (4) D

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\therefore$ Part labelled as C is foam breaker.

**Solved independently** (answer withheld)

1. In the NCERT stirred-tank bioreactor, the foam breaker is the disc on the agitator shaft at the top of the vessel, above the culture broth and just below the motor; in the figure this is label $C$ (B = motor, A = flat-bladed impeller, D = bottom line), which is option $1$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 65)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q148_57711e4d_12112026.png?v=57711e4d99e8)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q148_629bdbaf_12112026.png?v=629bdbafa1be)

---

## Q149

Biology · both · Biotechnology: Principles and Processes

Polymerase chain reaction (PCR) amplifies DNA following the equation.

- (1) $2\mathrm{N}^{2}$
- (2) $\mathrm{N}^{2}$
- **(3)** $2^{n}$
- (4) $2n + 1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. PCR i.e., polymerase chain reaction amplifies DNA as per the equation $2^{n}$, where ‘$n$’ refers to number of cycles.
2. Thus, say, if $3$ PCR cycles will run, then $2^{3}$ i.e., $2 \times 2 \times 2 \Rightarrow 8$ DNA fragments will be formed.

**Solved independently** (answer withheld)

1. Each PCR cycle (denaturation, annealing, extension) doubles the number of DNA molecules.
2. After $n$ cycles, one template gives $1 \times 2 \times 2 \cdots = 2^{n}$ copies, which is option $3$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q149_a9b4b4c4_12112026.png?v=a9b4b4c4552b)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q149_84239aad_12112026.png?v=84239aad4a38)

---

## Q150

Biology · zoology · Human Reproduction

Match List - I with List - II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Head | I | Enzymes |
| B | Middle piece | II | Sperm motility |
| C | Acrosome | III | Energy |
| D | Tail | IV | Genetic material |

- (1) A-III, B-II, C-I, D-IV
- **(2)** A-IV, B-III, C-I, D-II
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The sperm head contains elongated nucleus which possesses the genetic material.
2. The middle piece possesses numerous mitochondria, which produce energy for movement.
3. Acrosome is a cap-like structure filled with enzymes that help in fertilization of ovum.
4. The tail of sperm facilitates sperm motility essential for fertilisation.

**Solved independently** (answer withheld)

1. The sperm head contains the haploid nucleus, so A (Head) matches IV (Genetic material).
2. The middle piece has many mitochondria that produce energy, so B matches III (Energy).
3. The acrosome is a cap filled with enzymes that help in fertilisation, so C matches I (Enzymes).
4. The tail drives sperm motility, so D matches II (Sperm motility).
5. $A\text{-}IV,\ B\text{-}III,\ C\text{-}I,\ D\text{-}II$ is option $2$.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 66)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q150_dd463136_12112026.png?v=dd4631364611)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q150_89b6f356_12112026.png?v=89b6f3565424)

---

## Q151

Biology · botany · Morphology of Flowering Plants

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) In a floral formula $\oplus$ stands for zygomorphic nature of the flower, and $\underline{\mathrm{G}}$ stands for inferior ovary.
- (Statement II) In a floral formula $\oplus$ stands for actinomorphic nature of the flower and $\underline{\mathrm{G}}$ stands for superior ovary.

- **(1)** Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The floral formula symbol $\oplus$ is used for actinomorphic flower, while $\%$ is used for zygomorphic flower.
2. The symbol $\mathrm{G}$ represents gynoecium and $\underline{\mathrm{G}}$ symbol represent superior ovary, while inferior ovary is represented by $\bar{\mathrm{G}}$.
3. Thus, statement I is incorrect and Statement II is correct.

**Solved independently** (answer withheld)

1. In NCERT floral formulae, $\oplus$ stands for actinomorphic and $\%$ for zygomorphic, so the first half of Statement I is false.
2. $\underline{\mathrm{G}}$ (line below G) stands for a superior ovary and $\overline{\mathrm{G}}$ for an inferior ovary, so the second half of Statement I is also false.
3. Both halves of Statement II ($\oplus$ = actinomorphic, $\underline{\mathrm{G}}$ = superior ovary) are correct.
4. Statement I is incorrect and Statement II is correct, which is option $1$.

**Subtopic:** Semi-Technical Description of a Typical Flowering Plant · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 66)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q151_d8211dc7_12112026.png?v=d8211dc73066)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q151_e151a8fb_12112026.png?v=e151a8fb130b)

---

## Q152

Biology · both · Cell: The Unit of Life

From the statements given below choose the correct option :

- (A) The eukaryotic ribosomes are $80\mathrm{S}$ and prokaryotic ribosomes are $70\mathrm{S}$.
- (B) Each ribosome has two sub-units.
- (C) The two sub-units of $80\mathrm{S}$ ribosome are $60\mathrm{S}$ and $40\mathrm{S}$ while that of $70\mathrm{S}$ are $50\mathrm{S}$ and $30\mathrm{S}$.
- (D) The two sub-units of $80\mathrm{S}$ ribosome are $60\mathrm{S}$ and $20\mathrm{S}$ and that of $70\mathrm{S}$ are $50\mathrm{S}$ and $20\mathrm{S}$.
- (E) The two sub-units of $80\mathrm{S}$ are $60\mathrm{S}$ and $30\mathrm{S}$ and that of $70\mathrm{S}$ are $50\mathrm{S}$ and $30\mathrm{S}$.

- (1) B, D, E are true
- **(2)** A, B, C are true
- (3) A, B, D are true
- (4) A, B, E are true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The eukaryotic ribosomes are $80\mathrm{S}$ and prokaryotic ribosomes are $70\mathrm{S}$ type.
2. Each ribosome has two sub-units.
3. The two sub-units of $80\mathrm{S}$ ribosome are $60\mathrm{S}$ and $40\mathrm{S}$ while that of $70\mathrm{S}$ are $50\mathrm{S}$ and $30\mathrm{S}$.

**Solved independently** (answer withheld)

1. A is true: eukaryotic ribosomes are $80\mathrm{S}$ and prokaryotic ribosomes are $70\mathrm{S}$.
2. B is true: each ribosome is made of a large and a small sub-unit.
3. C is true: $80\mathrm{S} = 60\mathrm{S} + 40\mathrm{S}$ and $70\mathrm{S} = 50\mathrm{S} + 30\mathrm{S}$.
4. D is false ($20\mathrm{S}$ sub-units are wrong) and E is false (the small sub-unit of $80\mathrm{S}$ is $40\mathrm{S}$, not $30\mathrm{S}$).
5. A, B and C are true, which is option $2$.

**Subtopic:** Ribosomes And Cytoskeleton · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 66)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q152_3221795c_12112026.png?v=3221795c833b)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q152_3b07a055_12112026.png?v=3b07a05527bd)

---

## Q153

Biology · botany · Biological Classification

Each of the following characteristics represent a Kingdom proposed by Whittaker. Arrange the following in increasing order of complexity of body organization. Choose the correct answer from the options given below :

- (A) Multicellular heterotrophs with cell wall made of chitin.
- (B) Heterotrophs with tissue/organ/organ system level of body organization.
- (C) Prokaryotes with cell wall made of polysaccharides and amino acids.
- (D) Eukaryotic autotrophs with tissue/organ level of body organization.
- (E) Eukaryotes with cellular body organization.

- (1) C, E, A, B, D
- (2) A, C, E, B, D
- **(3)** C, E, A, D, B
- (4) A, C, E, D, B

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Increasing order of complexity of body organisation in the kingdom given by R.H. Whittaker is as follows-
2. C. Monera-Prokaryotes with cell wall made up of polysaccharide.
3. E. Protista - Unicellular eukaryotes.
4. A. Fungi -Multicellular heterotrophic with cell wall made up of chitin.
5. D. Plantae - Eukaryotes autotrophs with tissue body organisation.
6. B. Animalia - Heterotrophs with tissue organ/system of body organisation
7. Correct sequence is C, E, A, D, B.

**Solved independently** (answer withheld)

1. Identify the kingdoms: $C$ = Monera, $E$ = Protista, $A$ = Fungi, $D$ = Plantae, $B$ = Animalia.
2. Body organization per Whittaker (NCERT table): Monera and Protista are cellular, Fungi multicellular/loose tissue, Plantae tissue/organ, Animalia tissue/organ/organ system.
3. Monera (prokaryotic) is simpler than Protista (eukaryotic), so the order is $C < E < A < D < B$.
4. $C, E, A, D, B$ is option $3$.

**Subtopic:** Five-Kingdom Classification & Characteristics · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 67)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q153_960660dd_12112026.png?v=960660dd866e)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q153_dedaca72_12112026.png?v=dedaca72f324)

---

## Q154

Biology · botany · Plant Kingdom

The correct sequence of events in the life cycle of bryophytes is

- (A) Fusion of antherozoid with egg.
- (B) Attachment of gametophyte to substratum.
- (C) Reduction division to produce haploid spores.
- (D) Formation of sporophyte.
- (E) Release of antherozoids into water.
- Choose the correct answer from the options given below :

- (1) D, E, A, B, C
- (2) D, E, A, C, B
- (3) B, E, A, C, D
- **(4)** B, E, A, D, C

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct sequence of events in the life cycle of bryophytes is
2. Attachment of gametophyte to substratum.
3. Release of antherozoids into water.
4. Fusion of antherozoid with egg.
5. Formation of sporophyte.
6. Reduction division to produce haploid spores.

**Solved independently** (answer withheld)

1. The dominant haploid gametophyte is attached to the substratum by rhizoids: $B$.
2. Antherozoids are released into water and swim to the archegonium: $E$.
3. An antherozoid fuses with the egg to form the zygote: $A$.
4. The zygote develops into the sporophyte, which stays attached to the gametophyte: $D$.
5. Spore mother cells in the capsule undergo reduction division to form haploid spores: $C$.
6. Sequence $B, E, A, D, C$ is option $4$.

**Subtopic:** Bryophytes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 67)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q154_45bf20b2_12112026.png?v=45bf20b2fd02)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q154_9180f19b_12112026.png?v=9180f19b503d)

---

## Q155

Biology · zoology · Human Health and Disease

Which are correct: Choose the correct answer from the options given below:

- (A) Computed tomography and magnetic resonance imaging detect cancers of internal organs.
- (B) Chemotherapeutics drugs are used to kill non-cancerous cells.
- (C) $\alpha$ -interferon activate the cancer patients’ immune system and helps in destroying the tumour.
- (D) Chemotherapeutic drugs are biological response modifiers.
- (E) In the case of leukaemia blood cell counts are decreased.

- **(1)** A and C only
- (2) B and D only
- (3) D and E only
- (4) C and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Statements A and C are correct while statements B, D and E are incorrect.
2. Chemotherapeutic drugs are used to kill cancerous cells.
3. In case of leukaemia, blood cell counts are increased.
4. $\alpha$-interferons are biological response modifiers.

**Solved independently** (answer withheld)

1. $A$: CT and MRI are used to detect cancers of internal organs, so $A$ is true.
2. $B$: chemotherapeutic drugs kill cancerous cells, not non-cancerous cells, so $B$ is false.
3. $C$: $\alpha$-interferon activates the patient's immune system and helps destroy the tumour, so $C$ is true.
4. $D$: biological response modifiers are substances like $\alpha$-interferon, not chemotherapeutic drugs, so $D$ is false.
5. $E$: in leukaemia blood cell counts are increased, not decreased, so $E$ is false.
6. Only $A$ and $C$ are correct, which is option $1$.

**Subtopic:** Cancer · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 68)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q155_e6180f65_12112026.png?v=e6180f650dd8)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q155_e2683ef0_12112026.png?v=e2683ef0ce4c)

---

## Q156

Biology · both · Biomolecules

Name the class of enzyme that usually catalyze the following reaction : $\mathrm{S - G + S^{\#} \rightarrow S + S^{\#} - G}$ Where, $\mathrm{G} \rightarrow$ a group other than hydrogen $\mathrm{S} \rightarrow$ a substrate $\mathrm{S^{\#}} \rightarrow$ another substrate

- (1) Ligase
- (2) Hydrolase
- (3) Lyase
- **(4)** Transferase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Enzymes catalysing a transfer of $\mathrm{G}$ group, (other than hydrogen) between a pair of substrates, $\mathrm{S}$ and $\mathrm{S'}$ are known as transferases.
2. $\mathrm{S - G + S^{\#} \rightarrow S + S^{\#} - G}$
3. Ligases catalyse the linking together of $2$ compounds such as $\mathrm{C - O}$, $\mathrm{C - S}$, $\mathrm{C - N}$ bonds \textit{etc}
4. Lyases catalyse removal of groups from substrates by mechanisms other than hydrolysis leaving double bonds
5. Hydrolases are enzymes that catalyse hydrolysis of ester, ether, peptide , glycosidic, $\mathrm{C - C}$, $\mathrm{C}$ – halide or $\mathrm{P - N}$ bonds.

**Solved independently** (answer withheld)

1. The group $\mathrm{G}$ (not hydrogen) moves from substrate $\mathrm{S}$ to substrate $\mathrm{S^{\#}}$: $\mathrm{S-G + S^{\#} \rightarrow S + S^{\#}-G}$, which is the reaction of transferases, option $4$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q156_c0509b0b_12112026.png?v=c0509b0bfbc1)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q156_375c8db1_12112026.png?v=375c8db17345)

---

## Q157

Biology · zoology · Human Reproduction

Find the correct statement :
Choose the correct answer from the options given below :

- (A) In human pregnancy, the major organ systems are formed at the end of 12 weeks.
- (B) In human pregnancy the major organ systems are formed at the end of 8 weeks.
- (C) In human pregnancy heart is formed after one month of gestation.
- (D) In human pregnancy, limbs and digits develop by the end of second month.
- (E) In human pregnancy the appearance of hair is usually observed in the fifth month.

- **(1)** A, C, D and E only
- (2) A and E only
- (3) B and C only
- (4) B, C, D and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In a human female’s pregnancy.
2. By the end of $12$ weeks ($1^{\text{st}}$ trimester), most of major organ systems are formed (not by end of $8$ weeks).
3. After one month of pregnancy, the embryo’s heart is formed.
4. By the end of second month of pregnancy, the foetus develops limbs and digits.
5. The first movements of foetus and appearance of hair on head are usually observed during the fifth month.

**Solved independently** (answer withheld)

1. NCERT states that by the end of $12$ weeks (first trimester) most major organ systems are formed, so A is true and B is false.
2. After one month of pregnancy the embryo's heart is formed, so C is true.
3. By the end of the second month the foetus develops limbs and digits, so D is true.
4. During the fifth month the first movements and the appearance of hair on the head are usually observed, so E is true.
5. The correct set is A, C, D and E only, which is option $1$.

**Subtopic:** Implantation and Embryonic Development · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 69)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q157_4f77c5eb_12112026.png?v=4f77c5eb55e3)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q157_3570c64b_12112026.png?v=3570c64b4caa)

---

## Q158

Biology · botany · Microbes in Human Welfare

Which of the following is an example of non-distilled alcoholic beverage produced by yeast?

- (1) Rum
- (2) Whisky
- (3) Brandy
- **(4)** Beer

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Wine and beer are produced without distillation whereas whisky, brandy and rum are produced by distillation of fermented broth.

**Solved independently** (answer withheld)

1. Per NCERT (Microbes in Human Welfare), wine and beer are made without distillation, whereas whisky, brandy and rum are made by distilling the fermented broth, so the answer is Beer, option $4$.

**Subtopic:** Microbes in Industrial Products (Fermented Beverages) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q158_91f9f2a4_12112026.png?v=91f9f2a41b03)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q158_19c65b18_12112026.png?v=19c65b1881e6)

---

## Q159

Biology · both · Molecular Basis of Inheritance

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) In the RNA world, RNA is considered the first genetic material evolved to carry out essential life processes. RNA acts as a genetic material and also as a catalyst for some important biochemical reactions in living systems. Being reactive, RNA is unstable.
- (Statement II) DNA evolved from RNA and is a more stable genetic material. Its double helical strands being complementary, resist changes by evolving repairing mechanism.

- (1) Statement I is incorrect but statement II is correct
- **(2)** Both statement I and statement II are correct
- (3) Both statement I and statement II are incorrect
- (4) Statement I is correct but statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In RNA world, RNA was the first genetic material as there are enough evidences to suggest that essential life processes (such as metabolism, translation, splicing, etc) evolved around RNA.
2. RNA used to act as a genetic material as well as catalyst (there are some important biochemical reaction in living systems that are catalysed by RNA catalysts not by protein enzymes) so, statement I is correct statement II is also correct as DNA being double stranded and having complementary strands further resists changes by evolving a process of repair.

**Solved independently** (answer withheld)

1. Statement I: per NCERT, RNA was the first genetic material, acts both as genetic material and as a catalyst, and being reactive is unstable, so Statement I is correct.
2. Statement II: per NCERT, DNA evolved from RNA with chemical modifications making it more stable; its complementary double-helical strands resist changes by evolving a repair process, so Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 69)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q159_666a0224_12112026.png?v=666a0224f43b)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q159_08bf6745_12112026.png?v=08bf67450bec)

---

## Q160

Biology · both · Molecular Basis of Inheritance

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) Transfer RNAs and ribosomal RNA do not interact with mRNA.
- (Statement II) RNA interference (RNAi) takes place in all eukaryotic organisms as a method of cellular defence.

- **(1)** Statement I is incorrect but statement II is correct
- (2) Both statement I and statement II are correct
- (3) Both statement I and statement II are incorrect
- (4) Statement I is correct but statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Both transfer RNAs and ribosomal RNA interact with mRNA.
2. RNA interference (RNAi) takes place in all eukaryotic organisms as a method of cellular defence.

**Solved independently** (answer withheld)

1. During translation, the tRNA anticodon pairs with the mRNA codon and rRNA in the ribosome binds the mRNA, so Statement I is incorrect.
2. NCERT (Biotechnology and its Applications) states that RNAi takes place in all eukaryotic organisms as a method of cellular defence, so Statement II is correct.
3. Statement I incorrect and Statement II correct matches option $1$.

**Subtopic:** Translation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q160_82d068cd_12112026.png?v=82d068cd04a6)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q160_bf52222a_12112026.png?v=bf52222a6c70)

---

## Q161

Biology · zoology · Excretory Products and Their Elimination

Which of the following diagrams is correct with regard to the proximal (P) and distal (D) tubule of the Nephron.

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q161_option_1_0cc5bab8_12112026.png?v=0cc5bab822cd)
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q161_option_2_df757cc1_12112026.png?v=df757cc12ee0)
- **(3)** ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q161_option_3_e423e42c_12112026.png?v=e423e42c66bd)
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q161_option_4_ec52af5d_12112026.png?v=ec52af5dd001)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. During urine formation, the tubular cells secrete substances like $\mathrm{H^{+}}$, $\mathrm{K^{+}}$ and ammonia into the filtrate.
2. Tubular secretion is also an important step in urine formation as it helps in the maintenance of ionic and acid base balance of body fluids.
3. PCT $\rightarrow$ Selective secretion of $\mathrm{H^{+}}$, ammonia and $\mathrm{K^{+}}$ into the filtrate.
4. DCT $\rightarrow$ Capable of reabsorption of $\mathrm{HCO_3^{-}}$ and selective secretion of $\mathrm{H^{+}}$, $\mathrm{K^{+}}$ and $\mathrm{NH_3}$.

**Solved independently** (answer withheld)

1. In each diagram, arrows leaving the lumen upward show reabsorption and arrows entering the lumen from below show secretion.
2. Proximal tubule (NCERT): reabsorbs $\mathrm{HCO_3^-}$, $\mathrm{NaCl}$ and $\mathrm{H_2O}$; secretes $\mathrm{H^+}$ and $\mathrm{NH_3}$.
3. Distal tubule (NCERT): reabsorbs $\mathrm{NaCl}$, $\mathrm{H_2O}$ and $\mathrm{HCO_3^-}$; secretes $\mathrm{K^+}$ and $\mathrm{H^+}$.
4. Options 1 and 2 show $\mathrm{H_2O}$ secreted into the proximal tubule, and option 4 shows $\mathrm{NaCl}$ secreted into the distal tubule, so they are wrong.
5. Option 3 matches both tubules, so the answer is option $3$.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 70)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q161_9e83f720_12112026.png?v=9e83f7208d77)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q161_92dc7ce2_12112026.png?v=92dc7ce2a898)

---

## Q162

Biology · both · Principles of Inheritance and Variation

What is the pattern of inheritance for polygenic trait?

- (1) X-linked recessive inheritance pattern
- (2) Mendelian inheritance pattern
- **(3)** Non-mendelian inheritance pattern
- (4) Autosomal dominant pattern

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Polygenic inheritance refers to the inheritance of a trait controlled by two or more genes.
2. When human disorders are determined by mutation in the single gene then they are transmitted to the offspring as per Mendelian principle.
3. Polygenic trait shows non-Mendelian inheritance pattern.

**Solved independently** (answer withheld)

1. A polygenic trait is controlled by several genes with additive effects, giving continuous variation that does not follow simple Mendelian ratios, so its inheritance pattern is non-Mendelian, which is option $3$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 70)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q162_f705a090_12112026.png?v=f705a0904e34)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q162_8884fc55_12112026.png?v=8884fc550380)

---

## Q163

Biology · botany · Morphology of Flowering Plants

In the seeds of cereals, the outer covering of endosperm separates the embryo by a protein-rich layer called :

- **(1)** Aleurone layer
- (2) Coleoptile
- (3) Coleorhiza
- (4) Integument

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In monocot seeds, the outer covering of endosperm separates the embryo by a proteinous layer called aleurone layer.

**Solved independently** (answer withheld)

1. In cereal seeds such as maize, the outer covering of the endosperm that separates it from the embryo is a protein-rich layer called the aleurone layer, which is option $1$.

**Subtopic:** The Seed · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 71)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q163_1d0a3d8b_12112026.png?v=1d0a3d8bfe5f)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q163_b6b67d42_12112026.png?v=b6b67d42abd8)

---

## Q164

Biology · botany · Photosynthesis in Higher Plants

Match List I with List II: Choose the option with all correct matches.

| List-I | | List-II | |
|---|---|---|---|
| A | Chlorophyll a | I | Yellow-green |
| B | Chlorophyll b | II | Yellow |
| C | Xanthophylls | III | Blue-green |
| D | Carotenoids | IV | Yellow to Yellow-orange |

- (1) A-I, B-IV, C-III, D-II
- (2) A-III, B-IV, C-II, D-I
- **(3)** A-III, B-I, C-II, D-IV
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A chromatographic separation of the leaf pigments shows that the colour that we see in leaves is not due to single pigment but due to four pigments.
2. Chlorophyll a – Bright or blue-green in the chromatogram
3. Chlorophyll b – Yellow-green
4. Xanthophylls – Yellow
5. Carotenoids – Yellow to Yellow-orange

**Solved independently** (answer withheld)

1. In NCERT chromatography of leaf pigments, chlorophyll $a$ is bright or blue-green, so $A \to III$.
2. Chlorophyll $b$ is yellow-green, so $B \to I$.
3. Xanthophylls are yellow, so $C \to II$.
4. Carotenoids are yellow to yellow-orange, so $D \to IV$.
5. $A$-III, $B$-I, $C$-II, $D$-IV matches option $3$.

**Subtopic:** Pigments and Its Types · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 71)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q164_6e6704ed_12112026.png?v=6e6704ed7317)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q164_ff858478_12112026.png?v=ff858478a40a)

---

## Q165

Biology · both · Biotechnology and Its Applications

Which of the following genetically engineered organisms was used by Eli Lilly to prepare human insulin?

- (1) Phage
- **(2)** Bacterium
- (3) Yeast
- (4) Virus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is bacterium.
2. In 1983, Eli Lilly, an American company, prepared two DNA sequences corresponding to ‘A’ and ‘B’ chains of human insulin and introduced them in plasmids of $\textit{E.coli}$ (a gram negative bacterium) to produce insulin chains.

**Solved independently** (answer withheld)

1. Eli Lilly introduced the DNA sequences for insulin chains A and B into plasmids of $E.\ coli$, a bacterium, to produce human insulin, which is option $2$.

**Subtopic:** Genetically Engineered Insulin · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 71)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q165_5b4663ac_12112026.png?v=5b4663acc5f2)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q165_26bc3118_12112026.png?v=26bc3118360d)

---

## Q166

Biology · both · Molecular Basis of Inheritance

Which of the following are the post-transcriptional events in an eukaryotic cell?
Choose the correct answer from the options given below :

- (A) Transport of pre-mRNA to cytoplasm prior to splicing.
- (B) Removal of introns and joining of exons.
- (C) Addition of methyl group at $5'$ end of hnRNA.
- (D) Addition of adenine residues at $3'$ end of hnRNA.
- (E) Base pairing of two complementary RNAs.

- (1) C, D, E only
- (2) A, B, C only
- **(3)** B, C, D only
- (4) B, C, E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The process of copying genetic information from one strand of the DNA into RNA is known as transcription. It occurs in the cytoplasm with the help of transcripting enzyme.
2. Transport of pre-mRNA to cytoplasm prior to splicing is a part of transcription.
3. The primary transcript is converted into functional mRNA after post transcriptional processing involves $3$ steps as follows-
4. Modification of $5'$ end by capping,
5. Tailing,
6. Splicing.
7. Base pairing of two complementary RNA is not on event of post-transcription.
8. Hence, statements B, C, D are post-transcriptional modification events in eukaryotic cell.

**Solved independently** (answer withheld)

1. Statement A is false: hnRNA is spliced in the nucleus and only the processed mRNA is transported to the cytoplasm.
2. Statement B is true: splicing removes introns and joins exons.
3. Statement C is true: capping adds methyl guanosine triphosphate at the $5'$ end of hnRNA.
4. Statement D is true: tailing adds $200$-$300$ adenylate residues at the $3'$ end of hnRNA.
5. Statement E is false: base pairing of complementary RNAs is not a post-transcriptional processing step.
6. So the correct set is B, C, D only, which is option $3$.

**Subtopic:** Transcription · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 72)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q166_ff388f22_12112026.png?v=ff388f227e1a)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q166_9a5bca1b_12112026.png?v=9a5bca1b29c1)

---

## Q167

Biology · both · Cell: The Unit of Life

Match List-I with List- II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Centromere | I | Mitochondrion |
| B | Cilium | II | Cell division |
| C | Cristae | III | Cell movement |
| D | Cell membrane | IV | Phospholipid Bilayer |

- **(1)** A-II, B-III, C-I, D-IV
- (2) A-I, B-II, C-III, D-IV
- (3) A-II, B-I, C-IV, D-III
- (4) A-IV, B-II, C-III, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Centromere - Helps in cell division
2. Cilium - Helps in cell movement
3. Cristae - Finger like structures of mitochondria
4. Cell membrane - Is a phospholipid bilayer

**Solved independently** (answer withheld)

1. Centromere holds sister chromatids and attaches to spindle fibres, so A matches II (Cell division); cilium drives cell movement, so B matches III; cristae are infoldings of the inner mitochondrial membrane, so C matches I; the cell membrane is a phospholipid bilayer, so D matches IV. This gives A-II, B-III, C-I, D-IV, which is option $1$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q167_f7bf51c2_12112026.png?v=f7bf51c22817)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q167_aa97d208_12112026.png?v=aa97d2086ab6)

---

## Q168

Biology · both · Molecular Basis of Inheritance

Match List I with List II:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Alfred Hershey and Martha Chase | I | Streptococcus pneumoniae |
| B | Euchromatin | II | Densely packed and dark-stained |
| C | Frederick Griffith | III | Loosely packed and light-stained |
| D | Heterochromatin | IV | DNA as genetic material confirmation |

- (1) A-III, B-II, C-IV, D-I
- (2) A-II, B-IV, C-I, D-III
- (3) A-IV, B-II, C-I, D-III
- **(4)** A-IV, B-III, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The unequivocal proof that DNA is the genetic material came from the experiment of Alfred Hershey and Martha Chase.
2. Euchromatin are lightly stained region with loosely packed chromatin fibre.
3. Frederick Griffith performed series of experiments by selecting the different strains of Streptococcus pneumoniae.
4. Heterochromatin are darkly stained region with tightly packed chromatin fibre.

**Solved independently** (answer withheld)

1. Hershey and Chase used bacteriophages to confirm that DNA is the genetic material, so $A \to IV$.
2. Euchromatin is loosely packed chromatin that stains light, so $B \to III$.
3. Griffith's transformation experiment used $Streptococcus\ pneumoniae$, so $C \to I$.
4. Heterochromatin is densely packed chromatin that stains dark, so $D \to II$.
5. $A$-$IV$, $B$-$III$, $C$-$I$, $D$-$II$ matches option $4$.

**Subtopic:** The Search for Genetic Material, Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 73)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q168_56c67b88_12112026.png?v=56c67b88389c)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q168_ff7045b4_12112026.png?v=ff7045b48d6a)

---

## Q169

Biology · both · Molecular Basis of Inheritance

Which chromosome in the human genome has the highest number of genes?

- (1) Chromosome 10
- (2) Chromosome X
- (3) Chromosome Y
- **(4)** Chromosome 1

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In human genome, Chromosome $1$ has the highest number of genes, i.e., $2968$.

**Solved independently** (answer withheld)

1. NCERT states chromosome $1$ has the most genes ($2968$) and chromosome $Y$ the fewest ($231$), so the answer is option $4$.

**Subtopic:** Human Genome Project · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 73)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q169_138edb17_12112026.png?v=138edb1770b5)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q169_a3e1e4d2_12112026.png?v=a3e1e4d2751e)

---

## Q170

Biology · zoology · Reproductive Health

What are the potential drawbacks in adoption of the IVF method? Choose the correct answer from the options given below:

- (A) High fatality risk to mother
- (B) Expensive instruments and reagents
- (C) Husband/wife necessary for being donors
- (D) Less adoption of orphans
- (E) Not available in India
- (F) Possibility that the early embryo does not survive

- (1) A, B, C, E, F only
- **(2)** B, D, F only
- (3) A, C, D, F only
- (4) A, B, C, D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Statements B, D and F are correct while statements A, C and E are incorrect.
2. Husband/wife is not necessary for being donors. IVF is available ins India.

**Solved independently** (answer withheld)

1. Statement A is false: IVF does not carry a high fatality risk to the mother.
2. Statement B is true: IVF needs expensive instruments and reagents (NCERT: very expensive, specialised facilities).
3. Statement C is false: gametes may come from donors, not necessarily husband/wife.
4. Statement D is true: preference for own biological child via ART reduces adoption of orphans.
5. Statement E is false: IVF facilities are available in India.
6. Statement F is true: the early embryo may fail to survive or implant.
7. True set $= \{B, D, F\}$, which is option $2$.

**Subtopic:** Infertility and In-Vitro Fertilisation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 73)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q170_0777782a_12112026.png?v=0777782a57ec)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q170_9d8fa165_12112026.png?v=9d8fa165cb22)

---

## Q171

Biology · botany · Biodiversity and Conservation

Which one of the following is an example of ex-situ conservation?

- (1) Protected areas
- (2) National Park
- (3) Wildlife Sanctuary
- **(4)** Zoos and botanical gardens

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Zoological parks (Zoos), botanical gardens and wildlife safari parks are examples of ex-situ conservation.
2. Sacred groves, biosphere reserves, national parks and wildlife sanctuaries are examples of in-situ conservation.

**Solved independently** (answer withheld)

1. Ex-situ conservation protects threatened species away from their natural habitat (e.g. zoos, botanical gardens, seed banks), while protected areas, national parks and wildlife sanctuaries are in-situ, so the answer is option $4$.

**Subtopic:** Ex Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q171_cc4ff098_12112026.png?v=cc4ff0989675)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q171_5e840c56_12112026.png?v=5e840c561318)

---

## Q172

Biology · both · Cell: The Unit of Life

A specialised membranous structure in a prokaryotic cell which helps in cell well wall formation, DNA replication and respiration is

- (1) Endoplasmic Reticulum
- **(2)** Mesosome
- (3) Chromatophores
- (4) Cristae

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Mesosome is membranous extension in bacterial cell that helps in cell wall formation, DNA replication and contains enzymes for respiration.

**Solved independently** (answer withheld)

1. In prokaryotes the plasma membrane infolds to form the mesosome, which helps in cell wall formation, DNA replication and respiration, so the answer is option $2$.

**Subtopic:** Prokaryotic Cells And Its Modification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q172_72b05418_12112026.png?v=72b05418ff92)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q172_a2ce05d2_12112026.png?v=a2ce05d211e7)

---

## Q173

Biology · both · Biotechnology: Principles and Processes

In the above represented plasmid, an alien piece of DNA is inserted at EcoRI site. Which of the following strategies will be chosen to select the recombinant colonies?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/figures_agent/q173_562ba8e3_12112026.png?v=562ba8e371f2)

- (1) Blue color colonies grown on ampicillin plates can be selected.
- (2) Using ampicillin & tetracycline containing medium plate.
- (3) Blue color colonies will be selected.
- **(4)** White color colonies will be selected.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is that white-colored colonies will be selected.
2. Since an alien piece of DNA is being inserted at $\textit{Eco}\mathrm{RI}$ site, the gene $\beta$-galactosidase present here will undergo insertional inactivation.
3. This gene is responsible for producing blue-colored colonies, but since it has been insertionally inactivated, white colored colonies will be produced.
4. Ampicillin and tetracycline resistance genes present in the given DNA will remain intact. Thus, the given DNA will show $\mathrm{amp}^{\mathrm{R}}$ and $\mathrm{tet}^{\mathrm{R}}$.

**Solved independently** (answer withheld)

1. In the figure the EcoRI site lies inside the $\beta$-galactosidase coding region, while $amp^R$ and $tet^R$ are untouched.
2. Inserting alien DNA at EcoRI causes insertional inactivation of $\beta$-galactosidase.
3. With a chromogenic substrate, colonies with active $\beta$-galactosidase (non-recombinants) turn blue; recombinants lacking it stay white.
4. Ampicillin and tetracycline resistance remain intact in both recombinants and non-recombinants, so antibiotic plates (options $1$, $2$) cannot separate them.
5. Hence white colonies are selected as recombinants, which is option $4$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 74)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q173_fc3f7001_12112026.png?v=fc3f7001db1e)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q173_b3cf0325_12112026.png?v=b3cf032516d5)

---

## Q174

Biology · zoology · Structural Organisation in Animals

What is the name of the blood vessel that carries deoxygenated blood from the body to the heart in a frog?

- **(1)** Vena cava
- (2) Aorta
- (3) Pulmonary artery
- (4) Pulmonary vein

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Frog’s heart is a muscular structure with three chambers.
2. It receives deoxygenated blood from body parts through the major veins called vena cava.
3. Vena cava carries deoxygenated blood.
4. Aorta and pulmonary vein carries oxygenated blood.
5. Whereas, pulmonary artery will carry deoxygenated blood towards the lungs.

**Solved independently** (answer withheld)

1. In the frog, the vena cavae collect deoxygenated blood from the body and bring it to the sinus venosus and right atrium, so the answer is option $1$ (Vena cava).

**Subtopic:** Anatomy of Frog · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 75)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q174_84f1464f_12112026.png?v=84f1464f4031)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q174_f79adcd0_12112026.png?v=f79adcd0e5e9)

---

## Q175

Biology · botany · Microbes in Human Welfare

Which of following organisms cannot fix nitrogen? Choose the correct answer from the options given below:

- (A) Azotobacter
- (B) Oscillatoria
- (C) Anabaena
- (D) Volvox
- (E) Nostoc

- (1) E only
- (2) A only
- **(3)** D only
- (4) B only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Azotobacter, Oscillatoria, Anabaena and Nostoc can fix nitrogen but Volvox cannot fix nitrogen.

**Solved independently** (answer withheld)

1. Azotobacter (A) is a free-living aerobic nitrogen-fixing bacterium.
2. Anabaena (C) and Nostoc (E) are cyanobacteria that fix nitrogen in heterocysts; Oscillatoria (B) is a cyanobacterium also counted as a nitrogen fixer.
3. Volvox (D) is a eukaryotic green alga (Chlorophyceae) and lacks nitrogenase, so it cannot fix nitrogen.
4. Hence the answer is D only, which is option $3$.

**Subtopic:** Microbes as Biofertilisers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 75)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q175_1b41ab3f_12112026.png?v=1b41ab3ffebe)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q175_b25004e9_12112026.png?v=b25004e967f1)

---

## Q176

Biology · zoology · Animal Kingdom

While trying to find out the characteristic of a newly found animal, a researcher did the histology of adult animal and observed a cavity with presence of mesodermal tissue towards the body wall but no mesodermal tissue was observed towards the alimentary canal. What could be the possible coelome of that animal?

- (1) Spongocoelomate
- (2) Acoelomate
- **(3)** Pseudocoelomate
- (4) Schizocoelomate

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In pseudocoelomates, the body cavity is not entirely lined with mesoderm, instead, mesodermal tissue is present along the body wall but not towards the gut.
2. Schizocoelomates are animals whose coelom or body cavity develops middle from a split in the mesoderm, the middle germ layer of the embryo.
3. In acoelomates, coelom is absent.
4. Spongocoel is a central cavity found in Sponges.

**Solved independently** (answer withheld)

1. In a pseudocoelomate the body cavity is not fully lined by mesoderm: mesoderm lies against the body wall but not around the alimentary canal, so the animal is a pseudocoelomate (option $3$).

**Subtopic:** Basis of Classification · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 75)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q176_0ba436ba_12112026.png?v=0ba436ba6cac)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q176_a59bcca6_12112026.png?v=a59bcca67389)

---

## Q177

Biology · both · Biomolecules

Which one of the following statements refers to Reductionist Biology?

- (1) Behavioural approach to study and understand living organisms
- **(2)** Physico-chemical approach to study and understand living organisms
- (3) Physiological approach to study and understand living organisms
- (4) Chemical approach to study and understand living organisms

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The physico-chemical approach to study and understand living organisms is called ‘Reductionist Biology’.

**Solved independently** (answer withheld)

1. Reductionist biology explains life processes by breaking organisms down into molecules and applying the concepts and techniques of physics and chemistry, i.e. a physico-chemical approach, which is option $2$.

**Subtopic:** Chemical Constituents Of Living Cells · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 75)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q177_3022a2bf_12112026.png?v=3022a2bfd43e)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q177_4b4d2552_12112026.png?v=4b4d2552895c)

---

## Q178

Biology · botany · Organisms and Populations

Epiphytes that are growing on a mango branch is an example of which of the following?

- (1) Amensalism
- **(2)** Commensalism
- (3) Mutualism
- (4) Predation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Commensalism is the type of interaction in which one-species benefits and another is neither harmed nor benefited.
2. An orchid growing as an epiphyte on a mango branch is an example of commensalism.

**Solved independently** (answer withheld)

1. An orchid-like epiphyte growing on a mango branch gains support and access to light ($+$), while the mango tree is neither harmed nor benefited ($0$); a $(+,0)$ interaction is commensalism, which is option $2$.

**Subtopic:** Commensalism and Ammensalism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 76)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q178_442bb37a_12112026.png?v=442bb37a937b)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q178_4e0bddf7_12112026.png?v=4e0bddf7f495)

---

## Q179

Biology · botany · Plant Growth and Development

Which one of the following phytohormones promotes nutrient mobilization which helps in the delay of leaf senescence in plants?

- **(1)** Cytokinin
- (2) Ethylene
- (3) Abscisic acid
- (4) Gibberellin

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cytokinins help to overcome apical dominance.
2. They promote nutrient mobilisation which helps in the delay of leaf senescence.

**Solved independently** (answer withheld)

1. Cytokinins help produce new leaves and chloroplasts and promote nutrient mobilisation, which delays leaf senescence, so the answer is option $1$ (Cytokinin).

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 76)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q179_d260bb29_12112026.png?v=d260bb29f9e3)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q179_e0bc60e6_12112026.png?v=e0bc60e6ad70)

---

## Q180

Biology · botany · Respiration in Plants

The complex II of mitochondrial electron transport chain is also known as

- (1) NADH dehydrogenase
- (2) Cytochrome $\mathrm{bc_1}$
- **(3)** Succinate dehydrogenase
- (4) Cytochrome c oxidase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Complex II of mitochondrial electron transport chain is also known as succinate dehydrogenase.
2. Cytochrome c oxidase (complex IV), NADH dehydrogenase (complex I), cytochrome $\mathrm{bc_1}$ (complex III).

**Solved independently** (answer withheld)

1. In the mitochondrial ETC, complex I is NADH dehydrogenase, complex II is succinate dehydrogenase, complex III is cytochrome $\mathrm{bc_1}$ and complex IV is cytochrome c oxidase, so complex II is option $3$.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 76)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/crops/q180_c9593184_12112026.png?v=c95931842b23)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2025/2025_47/solutions/q180_c0ff8a21_12112026.png?v=c0ff8a2177dc)

