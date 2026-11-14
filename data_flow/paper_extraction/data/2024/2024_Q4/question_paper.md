# NEET (UG) 2024 · Code Q4

200 questions · source `NEET_Papers/2024/Set_Q4/NEET_2024_Question_Paper_Q4.pdf` · every image a CDN link (0 without one) · 53 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Electrostatics

A thin spherical shell is charged by some source. The potential difference between the two points $C$ and $P$ (in V) shown in the figure is: (Take $\dfrac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}$ SI units)

![printed figure: Charged thin spherical shell of radius R = 3 cm with centre C and point P on the surface](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q001_15148465_13112026.png?v=15148465d922)

*Charged thin spherical shell of radius R = 3 cm with centre C and point P on the surface*

![drawn: Charged thin spherical shell of radius R = 3 cm with centre C and point P on the surface](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q001_question_cc5f9ddd_13112026.svg?v=cc5f9ddda34b)  
*drawn by code/lib/physics_figure.py*

- (1) $3 \times 10^{5}$
- (2) $1 \times 10^{5}$
- (3) $0.5 \times 10^{5}$
- **(4)** Zero

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For uniformly charged spherical shell,
2. $V = \frac{kq}{R}$ (For $r \le R$)
3. $\therefore V_C = V_P$
4. $V_C - V_P = \text{Zero}$

**Solved independently** (answer withheld)

1. Inside a charged conducting/thin spherical shell $E = 0$, so the potential is the same everywhere inside and equals the surface value.
2. $V_C = \frac{1}{4\pi\varepsilon_0}\frac{q}{R} = \frac{9\times10^{9}\times10^{-6}}{0.03} = 3\times10^{5}\,\text{V}$.
3. $P$ lies on the shell, so $V_P = \frac{1}{4\pi\varepsilon_0}\frac{q}{R} = 3\times10^{5}\,\text{V}$.
4. $V_C - V_P = 0$, which is option $4$.

**Subtopic:** Electrostatic Potential Throughout the Volume of a Conductor · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q001_0660e712_13112026.png?v=0660e712503c)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q001_e1025bd8_13112026.png?v=e1025bd80bdd)

---

## Q2

Physics · Semiconductor Electronics

The output ($Y$) of the given logic gate is similar to the output of an/a

![printed figure: NAND with inputs tied to A and NOR with inputs tied to B, both outputs feeding a NOR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q002_11d141cf_13112026.png?v=11d141cf0804)

*NAND with inputs tied to A and NOR with inputs tied to B, both outputs feeding a NOR gate giving Y*

![drawn: NAND with inputs tied to A and NOR with inputs tied to B, both outputs feeding a NOR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q002_question_d25b708f_13112026.svg?v=d25b708fc8d8)  
*drawn by code/lib/physics_figure.py*

- (1) NAND gate
- (2) NOR gate
- (3) OR gate
- **(4)** AND gate

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $Y_1 = \overline{A \cdot A} = \bar{A}$
2. $Y_2 = \overline{B + B} = \bar{B}$
3. $Y = \overline{Y_1 + Y_2}$
4. $= \overline{\bar{A} + \bar{B}} = \bar{\bar{A}} \cdot \bar{\bar{B}}$
5. $= A.B$ is similar to output of AND Gate

**Solved independently** (answer withheld)

1. A NAND gate with both inputs tied to $A$ gives $\overline{A \cdot A} = \overline{A}$.
2. A NOR gate with both inputs tied to $B$ gives $\overline{B + B} = \overline{B}$.
3. The final NOR gate gives $Y = \overline{\overline{A} + \overline{B}}$.
4. By De Morgan's theorem, $\overline{\overline{A} + \overline{B}} = A \cdot B$, which is an AND gate, option $4$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q002_27118e6c_13112026.png?v=27118e6c1883)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q002_338b3eed_13112026.png?v=338b3eed2776)

---

## Q3

Physics · Wave Optics

If the monochromatic source in Young’s double slit experiment is replaced by white light, then

- (1) Interference pattern will disappear
- (2) There will be a central dark fringe surrounded by a few coloured fringes
- **(3)** There will be a central bright white fringe surrounded by a few coloured fringes
- (4) All bright fringes will be of equal width

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. At central point on screen, path difference is zero for all wavelength.
2. So, central bright fringe is white and other fringes depend on wavelength as $\beta = \frac{\lambda D}{d}$.
3. Therefore, other fringes will be coloured.

**Solved independently** (answer withheld)

1. At the central point the path difference is $\Delta x = 0$ for every wavelength $\lambda$.
2. So every colour has a maximum there, and their overlap gives a central bright white fringe.
3. Fringe width $\beta = \frac{\lambda D}{d}$ differs for each $\lambda$, so away from the centre the maxima separate into a few coloured fringes, which is option $3$.

**Subtopic:** Young's Double-Slit Experiment (YDSE) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q003_1d265f99_13112026.png?v=1d265f995ae0)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q003_6cd88125_13112026.png?v=6cd8812510a9)

---

## Q4

Physics · Units and Measurements

In a vernier callipers, $(N + 1)$ divisions of vernier scale coincide with $N$ divisions of main scale. If 1 MSD represents $0.1\,\mathrm{mm}$, the vernier constant (in $\mathrm{cm}$) is:

- (1) $\frac{1}{10N}$
- **(2)** $\frac{1}{100(N+1)}$
- (3) $100N$
- (4) $10(N + 1)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $V.C = \mathrm{MSD} - \mathrm{VSD}$ ...(1)
2. given : $(N + 1)\,\mathrm{VSD} = N\,\mathrm{MSD}$
3. $\mathrm{VSD} = \left(\frac{N}{N+1}\right)\mathrm{MSD}$ ...(2)
4. From (1) and (2)
5. $V.C = (\mathrm{MSD}) - \frac{N}{N+1}(\mathrm{MSD})$
6. $= \mathrm{MSD}\left(1 - \frac{N}{N+1}\right) = \frac{\mathrm{MSD}}{N+1}$
7. $= \frac{0.01}{N+1} = \frac{1}{100(N+1)}$

**Solved independently** (answer withheld)

1. Since $(N+1)$ VSD $= N$ MSD, $1\,\text{VSD} = \frac{N}{N+1}\,\text{MSD}$.
2. $VC = 1\,\text{MSD} - 1\,\text{VSD} = \left(1 - \frac{N}{N+1}\right)\text{MSD} = \frac{1}{N+1}\,\text{MSD}$.
3. $1\,\text{MSD} = 0.1\,\mathrm{mm} = 0.01\,\mathrm{cm} = \frac{1}{100}\,\mathrm{cm}$.
4. $VC = \frac{1}{100(N+1)}\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q004_e92e36e4_13112026.png?v=e92e36e44e29)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q004_23361eee_13112026.png?v=23361eeeec10)

---

## Q5

Physics · Mechanical Properties of Solids

The maximum elongation of a steel wire of $1\,\mathrm{m}$ length if the elastic limit of steel and its Young’s modulus, respectively, are $8 \times 10^{8}\,\mathrm{N\,m^{-2}}$ and $2 \times 10^{11}\,\mathrm{N\,m^{-2}}$, is:

- **(1)** $4\,\mathrm{mm}$
- (2) $0.4\,\mathrm{mm}$
- (3) $40\,\mathrm{mm}$
- (4) $8\,\mathrm{mm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In the case for maximum elongation,
2. Stress = Elastic limit
3. $\delta_{\mathrm{max}} = \frac{\sigma_{\mathrm{elastic}} \times L}{\text{Young's modulus}} = \frac{8 \times 10^{8} \times 1}{2 \times 10^{11}} = 4 \times 10^{-3}$
4. $= 4\,\mathrm{mm}$
5. i.e. maximum elongation is $4\,\mathrm{mm}$

**Solved independently** (answer withheld)

1. Maximum stress the wire can take elastically is the elastic limit, $\sigma = 8 \times 10^{8}\,\mathrm{N\,m^{-2}}$.
2. Maximum strain $= \frac{\sigma}{Y} = \frac{8 \times 10^{8}}{2 \times 10^{11}} = 4 \times 10^{-3}$.
3. $\Delta L = \text{strain} \times L = 4 \times 10^{-3} \times 1\,\mathrm{m} = 4 \times 10^{-3}\,\mathrm{m} = 4\,\mathrm{mm}$, which is option $1$.

**Subtopic:** Hooke's Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q005_d6ffabff_13112026.png?v=d6ffabfff655)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q005_1762bcc7_13112026.png?v=1762bcc7fa25)

---

## Q6

Physics · Rotational Motion

The moment of inertia of a thin rod about an axis passing through its mid point and perpendicular to the rod is $2400\,\mathrm{g\,cm^{2}}$. The length of the $400\,\mathrm{g}$ rod is nearly:

- **(1)** $8.5\,\mathrm{cm}$
- (2) $17.5\,\mathrm{cm}$
- (3) $20.7\,\mathrm{cm}$
- (4) $72.0\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Moment of inertia of rod $= I = \frac{m\ell^{2}}{12}$
2. $\Rightarrow 2400 = 400\frac{\ell^{2}}{12}$
3. $\Rightarrow 72 = \ell^{2}$
4. $\Rightarrow \ell = \sqrt{72} = 8.48\,\mathrm{cm} \simeq 8.5\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. For a thin rod about a perpendicular axis through its midpoint, $I = \frac{ML^{2}}{12}$.
2. $L^{2} = \frac{12I}{M} = \frac{12 \times 2400\,\mathrm{g\,cm^{2}}}{400\,\mathrm{g}} = 72\,\mathrm{cm^{2}}$.
3. $L = \sqrt{72}\,\mathrm{cm} \approx 8.49\,\mathrm{cm} \approx 8.5\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Moment of Inertia of a Uniform Rod · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q006_b3484cbf_13112026.png?v=b3484cbf25c3)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q006_a1490a4e_13112026.png?v=a1490a4ea197)

---

## Q7

Physics · Magnetic Effect of Electric Current

A tightly wound 100 turns coil of radius $10\,\mathrm{cm}$ carries a current of $7\,\mathrm{A}$. The magnitude of the magnetic field at the centre of the coil is (Take permeability of free space as $4\pi \times 10^{-7}$ SI units):

- (1) $44\,\mathrm{mT}$
- (2) $4.4\,\mathrm{T}$
- **(3)** $4.4\,\mathrm{mT}$
- (4) $44\,\mathrm{T}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The magnitude of magnetic field due to circular coil of $N$ turns is given by
2. $B_C = \frac{\mu_0 i N}{2R}$
3. $= \frac{4\pi \times 10^{-7} \times 7 \times 100}{2 \times 0.1}$
4. $= 4.4 \times 10^{-3}\,\mathrm{T} = 4.4\,\mathrm{mT}$

**Solved independently** (answer withheld)

1. Field at the centre of a tightly wound circular coil: $B = \frac{\mu_0 N I}{2R}$.
2. $B = \frac{4\pi \times 10^{-7} \times 100 \times 7}{2 \times 0.1} = 4\pi \times 10^{-7} \times 3500$.
3. $B = 1.4\pi \times 10^{-3}\,\mathrm{T} \approx 4.4 \times 10^{-3}\,\mathrm{T} = 4.4\,\mathrm{mT}$, which is option $3$.

**Subtopic:** Magnetic Field on the Axis of a Circular Current Loop · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 4)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q007_de31ee8b_13112026.png?v=de31ee8beb11)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q007_62ee9b0a_13112026.png?v=62ee9b0acb24)

---

## Q8

Physics · Work, Energy and Power

At any instant of time $t$, the displacement of any particle is given by $2t - 1$ (SI unit) under the influence of force of $5\,\mathrm{N}$. The value of instantaneous power is (in SI unit):

- **(1)** $10$
- (2) $5$
- (3) $7$
- (4) $6$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $x = 2t - 1$
2. $v = \frac{dx}{dt} = 2\,\mathrm{m\,s^{-1}}$
3. $P = F.\,v$
4. $= 2 \times 5 = 10\,\mathrm{W}$

**Solved independently** (answer withheld)

1. Velocity is the time derivative of displacement: $v = \frac{dx}{dt} = \frac{d}{dt}(2t - 1) = 2\,\mathrm{m/s}$.
2. Instantaneous power is $P = F v$.
3. $P = 5\,\mathrm{N} \times 2\,\mathrm{m/s} = 10\,\mathrm{W}$, which is option $1$.

**Subtopic:** Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q008_dba68ee1_13112026.png?v=dba68ee19e94)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q008_a9c371da_13112026.png?v=a9c371dabe2e)

---

## Q9

Physics · Work, Energy and Power

Two bodies $A$ and $B$ of same mass undergo completely inelastic one dimensional collision. The body $A$ moves with velocity $v_1$ while body $B$ is at rest before collision. The velocity of the system after collision is $v_2$. The ratio $v_1 : v_2$ is

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $4 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Before collision $\Rightarrow$
2. It undergoes completely inelastic collision
3. Using conservation of linear momentum
4. Initial momentum = Final momentum
5. $\Rightarrow mv_1 = mv_2 + mv_2$
6. $\Rightarrow mv_1 = 2mv_2$
7. $\Rightarrow \frac{v_1}{v_2} = \frac{2}{1}$

**Solved independently** (answer withheld)

1. In a completely inelastic collision the bodies stick together, and linear momentum is conserved.
2. $m v_1 + m \cdot 0 = (m + m) v_2$.
3. $v_2 = \frac{v_1}{2}$.
4. $v_1 : v_2 = 2 : 1$, which is option $2$.

**Subtopic:** Problems on Inelastic Collision · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 4)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q009_f6aa4423_13112026.png?v=f6aa442300e7)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q009_318df2cb_13112026.png?v=318df2cb3c93)

---

## Q10

Physics · Laws of Motion

A horizontal force $10\,\mathrm{N}$ is applied to a block $A$ as shown in figure. The mass of blocks $A$ and $B$ are $2\,\mathrm{kg}$ and $3\,\mathrm{kg}$ respectively. The blocks slide over a frictionless surface. The force exerted by block $A$ on block $B$ is :

![printed figure: Force F = 10 N pushes block A against block B on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q010_c00f87be_13112026.png?v=c00f87be7178)

*Force F = 10 N pushes block A against block B on a frictionless floor*

![drawn: Force F = 10 N pushes block A against block B on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q010_question_8505b8cd_13112026.svg?v=8505b8cdc941)  
*drawn by code/lib/physics_figure.py*

- (1) Zero
- (2) $4\,\mathrm{N}$
- **(3)** $6\,\mathrm{N}$
- (4) $10\,\mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $F = (M_1 + M_2)a$
2. $a = \frac{10}{2+3} = 2\,\mathrm{m\,s^{-2}}$
3. $F' = M_2(2) = 3 \times 2\,\mathrm{N} = 6\,\mathrm{N}$

**Solved independently** (answer withheld)

1. Both blocks move together on the frictionless surface, so $a = \frac{F}{m_A + m_B} = \frac{10}{2+3} = 2\,\mathrm{m/s^2}$.
2. The only horizontal force on $B$ is the contact force from $A$: $N = m_B a$.
3. $N = 3 \times 2 = 6\,\mathrm{N}$, which is option $3$.

**Subtopic:** Block Problem · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q010_9b921be9_13112026.png?v=9b921be98cfb)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q010_e377ddf8_13112026.png?v=e377ddf86ab3)

---

## Q11

Physics · Gravitation

The mass of a planet is $\frac{1}{10}^{\text{th}}$ that of the earth and its diameter is half that of the earth. The acceleration due to gravity on that planet is:

- (1) $19.6\,\mathrm{m\,s^{-2}}$
- (2) $9.8\,\mathrm{m\,s^{-2}}$
- (3) $4.9\,\mathrm{m\,s^{-2}}$
- **(4)** $3.92\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $g' = \frac{GM'}{R'^{2}} = \frac{GM}{10\left(\frac{R}{2}\right)^{2}}$
2. $= \frac{4}{10}\frac{GM}{R^{2}} = 0.4 \times 9.8$
3. $= 3.92\,\mathrm{m\,s^{-2}}$

**Solved independently** (answer withheld)

1. Surface gravity is $g = \frac{GM}{R^2}$.
2. For the planet, $M' = \frac{M}{10}$ and $R' = \frac{R}{2}$ (diameter halved).
3. $g' = \frac{G(M/10)}{(R/2)^2} = \frac{4}{10}\frac{GM}{R^2} = 0.4\,g$.
4. $g' = 0.4 \times 9.8 = 3.92\,\mathrm{m\,s^{-2}}$, which is option $4$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 5)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q011_a6831cac_13112026.png?v=a6831cac96b9)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q011_03efa39a_13112026.png?v=03efa39aedfa)

---

## Q12

Physics · Semiconductor Electronics

Consider the following statements A and B and identify the correct answer:

![printed figure: I-V axes with quadrants I to IV](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q012_da345c03_13112026.png?v=da345c03d3d0)

*I-V axes with quadrants I to IV*

![drawn: I-V axes with quadrants I to IV](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q012_question_2f86aa69_13112026.svg?v=2f86aa69bb36)  
*drawn by code/lib/physics_figure.py*

- (A) For a solar-cell, the I-V characteristics lies in the IV quadrant of the given graph.
- (B) In a reverse biased $pn$ junction diode, the current measured in ($\mu\mathrm{A}$), is due to majority charge carriers.

- **(1)** A is correct but B is incorrect
- (2) A is incorrect but B is correct
- (3) Both A and B are correct
- (4) Both A and B are incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A: Solar cell characteristics
2. B: In reverse biased $pn$ junction diode, the current measured in ($\mu\mathrm{A}$), is due to minority charge carrier.

**Solved independently** (answer withheld)

1. A solar cell supplies power: open-circuit voltage $V > 0$ while short-circuit current $I < 0$, so its $I$-$V$ characteristic lies in quadrant $\mathrm{IV}$; statement A is correct.
2. In reverse bias the small current ($\mu\mathrm{A}$) is the drift of minority carriers across the junction, not majority carriers; statement B is incorrect.
3. A correct, B incorrect, which is option $1$.

**Subtopic:** Special Purpose PN Junction Diodes, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q012_962a6d02_13112026.png?v=962a6d028909)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q012_be35cdb2_13112026.png?v=be35cdb291fc)

---

## Q13

Physics · Ray Optics

A light ray enters through a right angled prism at point $P$ with the angle of incidence $30^\circ$ as shown in figure. It travels through the prism parallel to its base $BC$ and emerges along the face $AC$. The refractive index of the prism is:

![printed figure: Ray entering a right-angled prism ABC at P, travelling parallel to BC and emerging along AC](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q013_1d44b960_13112026.png?v=1d44b960c0e3)

*Ray entering a right-angled prism ABC at P, travelling parallel to BC and emerging along AC*

![drawn: Ray entering a right-angled prism ABC at P, travelling parallel to BC and emerging along AC](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q013_question_61d88771_13112026.svg?v=61d887711f89)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{\sqrt{5}}{4}$
- **(2)** $\frac{\sqrt{5}}{2}$
- (3) $\frac{\sqrt{3}}{4}$
- (4) $\frac{\sqrt{3}}{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $A = 90^\circ$
2. In prism, $r_1 + c = A$
3. $r_1 = 90^\circ - c$ \quad ...(1)
4. $\sin c = \frac{1}{\mu} \Rightarrow \cos c = \frac{\sqrt{\mu^2 - 1}}{\mu}$
5. $\Rightarrow$ Apply Snell's law, on incidence surface
6. $1 \cdot \sin 30^\circ = \mu \sin(r_1) \Rightarrow 1 \times \frac{1}{2} = \mu \times \sin(90^\circ - c)$
7. $\frac{1}{2} = \mu \times \frac{\sqrt{\mu^2 - 1}}{\mu}$
8. On squaring $\frac{1}{4} = \mu^2 - 1$
9. $\Rightarrow \mu^2 = \frac{5}{4} \Rightarrow \mu = \frac{\sqrt{5}}{2}$

**Solved independently** (answer withheld)

1. The prism angle at $A$ is $90^\circ$, so the refraction angles inside satisfy $r_1 + r_2 = A = 90^\circ$.
2. Snell's law at $P$: $\sin 30^\circ = \mu \sin r_1 \Rightarrow \sin r_1 = \frac{1}{2\mu}$.
3. The ray emerges along face $AC$ (grazing), so at that face $r_2 = \theta_c$ with $\sin r_2 = \frac{1}{\mu}$.
4. Since $r_2 = 90^\circ - r_1$, $\cos r_1 = \frac{1}{\mu}$.
5. $\sin^2 r_1 + \cos^2 r_1 = 1 \Rightarrow \frac{1}{4\mu^2} + \frac{1}{\mu^2} = 1 \Rightarrow \mu^2 = \frac{5}{4}$.
6. $\mu = \frac{\sqrt{5}}{2}$, which is option $2$.

**Subtopic:** Prism, Total Internal Reflection (TIR) · **Difficulty:** easy (4 steps)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q013_8fd0e051_13112026.png?v=8fd0e051b14f)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q013_75ed46a4_13112026.png?v=75ed46a47355)

---

## Q14

Physics · Modern Physics

> ⚠ Statement II (atoms emit their characteristic spectrum) is near-verbatim NCERT Class 12 "Atoms", which makes both statements true (option 1); read strictly, an atom emits its characteristic spectrum only when excited, which makes Statement II false and gives the booklet's key (3). Two blind solves chose 1 (one noting 3 as the strict reading) and an audit backed 3, so the wording, not the solver, decides it. Same question as 2024_S1 q020. (Carried from 2024_Q2 q001, the same question; option numbers converted to this booklet.)

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below.

- (Statement I) Atoms are electrically neutral as they contain equal number of positive and negative charges.
- (Statement II) Atoms of each element are stable and emit their characteristic spectrum.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Statement I is true as atoms are electrically neutral because they contain equal number of positive and negative charges.
2. Statement II is wrong as atom of most of the elements are stable and emit characteristic spectrum. But this statement is not true for every atom.

**Solved independently** (answer withheld)

1. Statement I: a neutral atom has $Z$ protons and $Z$ electrons, so net charge $= Ze - Ze = 0$; Statement I is correct.
2. Statement II: an atom emits radiation only when an electron goes from a higher level to a lower one, $h\nu = E_2 - E_1$, which needs prior excitation.
3. An atom that is stable in its ground state does not emit, so 'stable and emit their characteristic spectrum' is incorrect as a general claim.
4. Statement I correct, Statement II incorrect, which is option $3$.

**Subtopic:** Alpha-Particle Scattering and Rutherford Nuclear Model of the Atom and Thomson's Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q014_4d8a5d0e_13112026.png?v=4d8a5d0e8c26)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q014_ae8c9848_13112026.png?v=ae8c9848f33d)

---

## Q15

Physics · Mechanical Properties of Fluids

A thin flat circular disc of radius $4.5\,\mathrm{cm}$ is placed gently over the surface of water. If surface tension of water is $0.07\,\mathrm{N\,m^{-1}}$, then the excess force required to take it away from the surface is

- **(1)** $19.8\,\mathrm{mN}$
- (2) $198\,\mathrm{N}$
- (3) $1.98\,\mathrm{mN}$
- (4) $99\,\mathrm{N}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Excess force $= T \times 2\pi R$
2. $= \frac{7}{100} \times 2 \times 3.14 \times \frac{4.5}{100}$
3. $= 197.82 \times 10^{-4}$
4. $= 19.8 \times 10^{-3}\,\mathrm{N}$
5. $= 19.8\,\mathrm{mN}$

**Solved independently** (answer withheld)

1. The excess force equals surface tension acting along the circumference of the thin disc: $F = T \cdot 2\pi r$.
2. $2\pi r = 2\pi \times 0.045\,\mathrm{m} \approx 0.2827\,\mathrm{m}$.
3. $F = 0.07 \times 0.2827 \approx 0.0198\,\mathrm{N} = 19.8\,\mathrm{mN}$, which is option $1$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q015_ca67c1c1_13112026.png?v=ca67c1c11e18)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q015_c956dfbe_13112026.png?v=c956dfbe234c)

---

## Q16

Physics · Electromagnetic Induction

In the above diagram, a strong bar magnet is moving towards solenoid-2 from solenoid-1. The direction of induced current in solenoid-1 and that in solenoid-2, respectively, are through the directions:

![printed figure: A bar magnet moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q016_a0b70358_13112026.png?v=a0b703585140)

*A bar magnet moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)*

![drawn: A bar magnet moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q016_question_bc36e6ae_13112026.svg?v=bc36e6ae1c8b)  
*drawn by code/lib/physics_figure.py*

- **(1)** $AB$ and $DC$
- (2) $BA$ and $CD$
- (3) $AB$ and $CD$
- (4) $BA$ and $DC$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. North of magnet is moving away from solenoid $1$ so end $B$ of solenoid $1$ is South and as south of magnet is approaching solenoid $2$ so end $C$ of solenoid $2$ is South.

**Solved independently** (answer withheld)

1. The magnet moves to the right with its $N$ pole facing solenoid-1 and its $S$ pole facing solenoid-2.
2. In solenoid-1 the $N$ pole recedes, so by Lenz's law the right (near) end of solenoid-1 becomes an $S$ pole to oppose the decrease in flux.
3. In solenoid-2 the $S$ pole approaches, so by Lenz's law the left (near) end of solenoid-2 becomes an $S$ pole to oppose the increase in flux.
4. An $S$ pole on the right end of solenoid-1 needs current clockwise when viewed from the right; with the wire rising on the front face from terminal $A$, this current flows $A \to B$.
5. Both solenoids are wound the same way, but solenoid-2 has its $S$ pole on the left (opposite magnetisation), so its current flows from $D \to C$.
6. Hence the currents are $AB$ and $DC$, which is option $1$.

**Subtopic:** Lenz's Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q016_a4c92964_13112026.png?v=a4c9296464ac)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q016_efba8a0c_13112026.png?v=efba8a0cd436)

---

## Q17

Physics · Kinematics

A particle moving with uniform speed in a circular path maintains:

- (1) Constant velocity
- (2) Constant acceleration
- (3) Constant velocity but varying acceleration
- **(4)** Varying velocity and varying acceleration

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A particle moving with uniform speed in a circular path maintains varying velocity and varying acceleration.
2. It is because direction of both velocity as well as acceleration will change continuously.

**Solved independently** (answer withheld)

1. Speed $|\vec v|$ is constant, but $\vec v$ is tangential and its direction changes continuously, so velocity varies.
2. Acceleration $a = \frac{v^2}{r}$ is constant in magnitude but always points towards the centre, so its direction changes and $\vec a$ varies.
3. Both velocity and acceleration vary, which is option $4$.

**Subtopic:** Uniform Circular Motion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q017_6b4820e8_13112026.png?v=6b4820e88b2d)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q017_1c30d46c_13112026.png?v=1c30d46c7554)

---

## Q18

Physics · Modern Physics

Match List I with List II.

| List-I | | List-II | |
|---|---|---|---|
| A | $n_2 = 3$ to $n_1 = 2$ | I | $410.2$ |
| B | $n_2 = 4$ to $n_1 = 2$ | II | $434.1$ |
| C | $n_2 = 5$ to $n_1 = 2$ | III | $656.3$ |
| D | $n_2 = 6$ to $n_1 = 2$ | IV | $486.1$ |

- (1) A-II, B-I, C-IV, D-III
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-IV, B-III, C-I, D-II
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Energy difference $\Delta E = \frac{hc}{\lambda}$
2. $\therefore \lambda \propto \frac{1}{\Delta E}$
3. $(\Delta E)_{6-2} > (\Delta E)_{5-2} > (\Delta E)_{4-2} > (\Delta E)_{3-2}$
4. $\lambda_{6-2} < \lambda_{5-2} < \lambda_{4-2} < \lambda_{3-2}$
5. A-III, B-IV, C-II, D-I

**Solved independently** (answer withheld)

1. Balmer series: $\frac{1}{\lambda} = R_H\left(\frac{1}{2^2} - \frac{1}{n_2^2}\right)$, so wavelength decreases as $n_2$ increases.
2. $n_2 = 3 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{5}{36}$, $\lambda \approx 656.3\,\text{nm}$ (A-III).
3. $n_2 = 4 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{3}{16}$, $\lambda \approx 486.1\,\text{nm}$ (B-IV).
4. $n_2 = 5 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{21}{100}$, $\lambda \approx 434.1\,\text{nm}$ (C-II).
5. $n_2 = 6 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{2}{9}$, $\lambda \approx 410.2\,\text{nm}$ (D-I).
6. A-III, B-IV, C-II, D-I is option $2$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q018_fb559ad1_13112026.png?v=fb559ad16e9a)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q018_0534b414_13112026.png?v=0534b41444b3)

---

## Q19

Physics · Units and Measurements

The quantities which have the same dimensions as those of solid angle are:

- **(1)** strain and angle
- (2) stress and angle
- (3) strain and arc
- (4) angular speed and stress

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Solid angle $d\Omega = \frac{dA}{r^2}$ has dimensions $[\mathrm{M^0L^0T^0}]$
2. Strain $= \frac{\Delta l}{l}$ has dimensions $[\mathrm{M^0L^0T^0}]$
3. Angle measured in radians is also dimensionless $[\mathrm{M^0L^0T^0}]$
4. $\theta = \frac{l}{r}$

**Solved independently** (answer withheld)

1. Solid angle $\Omega = \frac{A}{r^2}$, so $[\Omega] = \frac{[L^2]}{[L^2]} = [M^0 L^0 T^0]$ (dimensionless).
2. Strain $= \frac{\Delta l}{l}$, so $[\text{strain}] = [M^0 L^0 T^0]$.
3. Plane angle $\theta = \frac{s}{r}$, so $[\theta] = [M^0 L^0 T^0]$.
4. Stress $= \frac{F}{A}$ has $[M L^{-1} T^{-2}]$, angular speed has $[T^{-1}]$ and arc has $[L]$, so options $4$, $2$ and $3$ fail.
5. Only strain and angle are dimensionless like solid angle, which is option $1$.

**Subtopic:** Dimensional Formulae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q019_e6347b77_13112026.png?v=e6347b777174)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q019_5dc79381_13112026.png?v=5dc793811ad2)

---

## Q20

Physics · Wave Optics

An unpolarised light beam strikes a glass surface at Brewster's angle. Then

- (1) The reflected light will be partially polarised.
- (2) The refracted light will be completely polarised.
- (3) Both the reflected and refracted light will be completely polarised.
- **(4)** The reflected light will be completely polarised but the refracted light will be partially polarised.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. According to Brewster's law, reflected rays are completely polarized and refracted rays are partially polarized.

**Solved independently** (answer withheld)

1. At Brewster's angle $i_B$ with $\tan i_B = \mu$, the reflected ray is completely plane polarised and the refracted ray is partially polarised, so option $4$.

**Subtopic:** Brewster's Law · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 9)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q020_44d7514b_13112026.png?v=44d7514b943a)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q020_ab0c001c_13112026.png?v=ab0c001cfdb2)

---

## Q21

Physics · Electrostatics

Given below are two statements: one is labelled as **Assertion A** and the other is labelled as **Reason R**. In the light of the above statements, choose the **correct** answer from the options given below:

- (A) The potential $(V)$ at any axial point, at $2\,\mathrm{m}$ distance $(r)$ from the centre of the dipole of dipole moment vector $\vec{P}$ of magnitude, $4 \times 10^{-6}\,\mathrm{C\,m}$, is $\pm 9 \times 10^{3}\,V$. (Take $\dfrac{1}{4\pi \epsilon_0} = 9 \times 10^{9}$ SI units)
- (R) $V = \pm \dfrac{2P}{4\pi \epsilon_0 r^2}$, where $r$ is the distance of any axial point, situated at $2\,\mathrm{m}$ from the centre of the dipole.

- (1) Both A and R are true and R is the correct explanation of A.
- (2) Both A and R are true and R is NOT the correct explanation of A.
- **(3)** A is true but R is false.
- (4) A is false but R is true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The potential $V$ at any point, at distance $r$ from centre of dipole $= \frac{KP\cos\theta}{r^2}$
2. At axial point where $\theta = 0^\circ$, $V = \frac{KP}{r^2} = \frac{9 \times 10^{9} \times 4 \times 10^{-6}}{2^2} = 9 \times 10^{3}\ \mathrm{V}$
3. At axial point where $\theta = 180^\circ$, $V = \frac{-KP}{r^2} = -9 \times 10^{3}\ \mathrm{V}$

**Solved independently** (answer withheld)

1. For a short dipole, potential at an axial point is $V = \pm \frac{1}{4\pi\epsilon_0}\frac{P}{r^2}$.
2. $V = \pm \frac{9\times10^{9} \times 4\times10^{-6}}{2^2}$.
3. $V = \pm \frac{36\times10^{3}}{4} = \pm 9\times10^{3}\,\mathrm{V}$, so Assertion A is true.
4. Reason R uses $V = \pm \frac{2P}{4\pi\epsilon_0 r^2}$, which has an extra factor $2$ (that factor belongs to the axial field $E = \frac{2P}{4\pi\epsilon_0 r^3}$), so R is false.
5. A true, R false, which is option $3$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q021_b80ceb7c_13112026.png?v=b80ceb7cbe5c)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q021_2bafb5e9_13112026.png?v=2bafb5e97914)

---

## Q22

Physics · Rotational Motion

A wheel of a bullock cart is rolling on a level road as shown in the figure below. If its linear speed is $v$ in the direction shown, which one of the following options is correct ($P$ and $Q$ are any highest and lowest points on the wheel, respectively)?

![printed figure: A spoked wheel rolling on a level road with velocity v; P at the top, Q at the bottom](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q022_b42cd947_13112026.png?v=b42cd9477a71)

*A spoked wheel rolling on a level road with velocity v; P at the top, Q at the bottom*

![drawn: A spoked wheel rolling on a level road with velocity v; P at the top, Q at the bottom](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q022_question_a5ff65eb_13112026.svg?v=a5ff65eb54a2)  
*drawn by code/lib/physics_figure.py*

- (1) Point $P$ moves slower than point $Q$
- **(2)** Point $P$ moves faster than point $Q$
- (3) Both the points $P$ and $Q$ move with equal speed
- (4) Point $P$ has zero speed

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In the case of pure rolling,
2. The topmost point will have velocity $2v$ while point $Q$ i.e. lowest point will have zero velocity.
3. Hence point $P$ moves faster than point $Q$.

**Solved independently** (answer withheld)

1. Rolling without slipping on a level road gives $v = \omega R$.
2. Top point: $v_P = v + \omega R = 2v$.
3. Lowest (contact) point: $v_Q = v - \omega R = 0$.
4. $v_P = 2v > v_Q = 0$, so $P$ moves faster than $Q$, which is option $2$.

**Subtopic:** Rolling Motion · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 10)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q022_fd34d6c6_13112026.png?v=fd34d6c681cf)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q022_bd47a9aa_13112026.png?v=bd47a9aa97ab)

---

## Q23

Physics · Oscillations

If $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,\mathrm{m}$ represents the motion of a particle executing simple harmonic motion, the amplitude and time period of motion, respectively, are

- (1) $5\,\mathrm{cm}$, $2\,\mathrm{s}$
- **(2)** $5\,\mathrm{m}$, $2\,\mathrm{s}$
- (3) $5\,\mathrm{cm}$, $1\,\mathrm{s}$
- (4) $5\,\mathrm{m}$, $1\,\mathrm{s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,\mathrm{m}$
2. Amplitude $= 5\,\mathrm{m}$
3. $\omega = \pi = \frac{2\pi}{T}$
4. $T = \frac{2\pi}{\pi} = 2\,\mathrm{s}$

**Solved independently** (answer withheld)

1. Compare with $x = A\sin(\omega t + \phi)$: $A = 5\,\mathrm{m}$ and $\omega = \pi\,\mathrm{rad\,s^{-1}}$.
2. $T = \frac{2\pi}{\omega} = \frac{2\pi}{\pi} = 2\,\mathrm{s}$.
3. Amplitude $5\,\mathrm{m}$ and period $2\,\mathrm{s}$, which is option $2$.

**Subtopic:** Calculate Time Period of SHM, Calculate Amplitude of SHM · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 10)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q023_62e1791c_13112026.png?v=62e1791cda1a)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q023_c8d74a3b_13112026.png?v=c8d74a3bcaee)

---

## Q24

Physics · Semiconductor Electronics

A logic circuit provides the output $Y$ as per the following truth table :

The expression for the output $Y$ is :

![printed figure: Truth table with inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q024_fc3bf73b_13112026.svg?v=fc3bf73bdd69)

*Truth table with inputs A, B and output Y*

![drawn: Truth table with inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q024_question_8ffb3803_13112026.svg?v=8ffb3803e398)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $A.B+\overline{A}$
- (2) $A.\overline{B}+\overline{A}$
- **(3)** $\overline{B}$
- (4) $B$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. According to given truth table, output is independent on value of $A$
2. $\therefore$ Output $Y = \overline{B}$

**Solved independently** (answer withheld)

1. Truth table rows $(A,B,Y)$: $(0,0,1),(0,1,0),(1,0,1),(1,1,0)$.
2. $Y = 1$ only when $B = 0$, and $Y = 0$ whenever $B = 1$, regardless of $A$.
3. Hence $Y = \overline{B}$.
4. Check option $2$: at $A=0, B=1$, $A\cdot\overline{B} + \overline{A} = 1 \neq 0$, so it fails; option $1$ at $A=1,B=1$ gives $1 \neq 0$, so it fails.
5. $Y = \overline{B}$ is option $3$.

**Subtopic:** Logic Gates · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q024_ccc558cd_13112026.png?v=ccc558cd8edf)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q024_e9020351_13112026.png?v=e9020351d31d)

---

## Q25

Physics · Modern Physics

If $c$ is the velocity of light in free space, the correct statements about photon among the following are:
Choose the correct answer from the options given below:

- (A) The energy of a photon is $E = h\nu$.
- (B) The velocity of a photon is $c$.
- (C) The momentum of a photon, $p = \dfrac{h\nu}{c}$.
- (D) In a photon-electron collision, both total energy and total momentum are conserved.
- (E) Photon possesses positive charge.

- (1) A and B only
- **(2)** A, B, C and D only
- (3) A, C and D only
- (4) A, B, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (A) If $c$ is the velocity of light
2. so, $E = h\nu$ (Energy of photon)
3. (B) Velocity of photon is equal to velocity of light i.e. $c$.
4. (C) $\lambda = \frac{h}{p}$
5. $p = \frac{h}{\lambda}$
6. $p = \frac{h\nu}{c}$
7. (D) In photon-electron collision both total energy and total momentum are conserved.

**Solved independently** (answer withheld)

1. Statement A: photon energy is $E = h\nu$, which is true.
2. Statement B: a photon travels at speed $c$ in free space, which is true.
3. Statement C: photon momentum $p = \frac{E}{c} = \frac{h\nu}{c}$, which is true.
4. Statement D: in a photon-electron collision, total energy and total momentum are conserved, which is true.
5. Statement E: a photon is electrically neutral, so it carries no positive charge; E is false.
6. The true set is A, B, C and D, which is option $2$.

**Subtopic:** Photon Energy and Number of Photons · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q025_5806e636_13112026.png?v=5806e63691f3)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q025_65b9088d_13112026.png?v=65b9088d303e)

---

## Q26

Physics · Laws of Motion

A bob is whirled in a horizontal plane by means of a string with an initial speed of $\omega$ rpm. The tension in the string is $T$. If speed becomes $2\omega$ while keeping the same radius, the tension in the string becomes:

- (1) $T$
- **(2)** $4T$
- (3) $\frac{T}{4}$
- (4) $\sqrt{2}T$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $T = m\ell\omega^{2}$
2. $T' = m\ell(2\omega)^{2}$
3. $T' = 4T$

**Solved independently** (answer withheld)

1. The string tension provides the centripetal force: $T = m\omega^2 r$.
2. With the same radius and angular speed $2\omega$: $T' = m(2\omega)^2 r = 4m\omega^2 r$.
3. $T' = 4T$, which is option $2$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 12)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q026_4c969163_13112026.png?v=4c96916347ca)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q026_d9a248ed_13112026.png?v=d9a248edbb20)

---

## Q27

Physics · Current Electricity

The terminal voltage of the battery, whose emf is $10\,\mathrm{V}$ and internal resistance $1\,\Omega$, when connected through an external resistance of $4\,\Omega$ as shown in the figure is:

![printed figure: A 10 V cell with internal resistance 1 Ω (dashed box) connected across an external 4 Ω resistor](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q027_3f40fe7c_13112026.png?v=3f40fe7c58b4)

*A 10 V cell with internal resistance 1 Ω (dashed box) connected across an external 4 Ω resistor*

![drawn: A 10 V cell with internal resistance 1 Ω (dashed box) connected across an external 4 Ω resistor](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q027_question_898137f4_13112026.svg?v=898137f4d637)  
*drawn by code/lib/physics_figure.py*

- (1) $4\,\mathrm{V}$
- (2) $6\,\mathrm{V}$
- **(3)** $8\,\mathrm{V}$
- (4) $10\,\mathrm{V}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Current in circuit $i = \frac{10}{4+1} = 2\,\mathrm{A}$
2. Terminal voltage $= E - iR$
3. $= 10 - 2 \times 1 = 8\,\mathrm{V}$

**Solved independently** (answer withheld)

1. The figure shows the battery discharging through the external resistor, with $R = 4\,\Omega$ in series with $r = 1\,\Omega$.
2. $I = \frac{E}{R + r} = \frac{10}{4 + 1} = 2\,\mathrm{A}$.
3. $V = E - Ir = 10 - 2 \times 1 = 8\,\mathrm{V}$.
4. Check: $V = IR = 2 \times 4 = 8\,\mathrm{V}$, which is option $3$.

**Subtopic:** Terminal Potential Difference · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q027_631d2eba_13112026.png?v=631d2eba60ca)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q027_a939b35b_13112026.png?v=a939b35b17f9)

---

## Q28

Physics · Magnetic Effect of Electric Current

In a uniform magnetic field of $0.049\,\mathrm{T}$, a magnetic needle performs 20 complete oscillations in $5$ seconds as shown. The moment of inertia of the needle is $9.8 \times 10^{-6}\,\mathrm{kg\,m^2}$. If the magnitude of magnetic moment of the needle is $x \times 10^{-5}\,\mathrm{A\,m^2}$, then the value of '$x$' is :

![printed figure: Magnetic needle hung by a thread from a ceiling in a uniform field B](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q028_11e55485_13112026.png?v=11e55485502b)

*Magnetic needle hung by a thread from a ceiling in a uniform field B*

![drawn: Magnetic needle hung by a thread from a ceiling in a uniform field B](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q028_question_a753c72a_13112026.svg?v=a753c72ab078)  
*drawn by code/lib/physics_figure.py*

- (1) $5\pi^2$
- (2) $128\pi^2$
- (3) $50\pi^2$
- **(4)** $1280\pi^2$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Time period of Oscillation, $T = 2\pi\sqrt{\frac{I}{MB}}$
2. $\Rightarrow \frac{1}{4} = 2\pi\sqrt{\frac{9.8 \times 10^{-6}}{M \times 0.049}}$
3. $\Rightarrow \frac{1}{16} = 4\pi^{2} \times \frac{9.8 \times 10^{-6}}{M \times 49 \times 10^{-3}}$
4. $\Rightarrow M = \frac{4\pi^{2} \times 9.8 \times 10^{-6}}{49 \times 10^{-3}} \times 16$
5. $= \frac{4\pi^{2} \times 9.8 \times 16 \times 10^{-3}}{49}$
6. $= 12.8\pi^{2} \times 10^{-3} \times 10^{-2} \times 10^{2} = 1280\pi^{2} \times 10^{-5}\,\mathrm{A\,m^{2}}$

**Solved independently** (answer withheld)

1. Time period: $T = \frac{5\,\mathrm{s}}{20} = 0.25\,\mathrm{s}$.
2. For an oscillating magnetic needle, $T = 2\pi\sqrt{\frac{I}{MB}}$.
3. Rearranging: $M = \frac{4\pi^2 I}{B T^2}$.
4. $B T^2 = 0.049 \times 0.0625 = 3.0625 \times 10^{-3}$.
5. $\frac{I}{BT^2} = \frac{9.8 \times 10^{-6}}{3.0625 \times 10^{-3}} = 3.2 \times 10^{-3}$.
6. $M = 4\pi^2 \times 3.2 \times 10^{-3} = 12.8\pi^2 \times 10^{-3} = 1280\pi^2 \times 10^{-5}\,\mathrm{Am^2}$.
7. So $x = 1280\pi^2$, which is option $4$.

**Subtopic:** The Dipole in a Uniform Magnetic Field · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 12)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q028_dd24a4c4_13112026.png?v=dd24a4c44a9c)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q028_7fa6aa22_13112026.png?v=7fa6aa220d84)

---

## Q29

Physics · Current Electricity

A wire of length '$l$' and resistance $100\,\Omega$ is divided into 10 equal parts. The first 5 parts are connected in series while the next 5 parts are connected in parallel. The two combinations are again connected in series. The resistance of this final combination is:

- (1) $26\,\Omega$
- **(2)** $52\,\Omega$
- (3) $55\,\Omega$
- (4) $60\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Divided into $10$ parts
2. $R = \frac{\rho l}{A}$
3. $R' = \frac{\rho l}{10A} = \frac{R}{10}$
4. $R_S = 5 \times \frac{R}{10}$ [series]
5. $R_S = 50$
6. $R_P = \frac{R}{50}$ [parallel]
7. $R_{\mathrm{eq}} = R_S + R_P$
8. $= 52\,\Omega$

**Solved independently** (answer withheld)

1. Dividing the wire into 10 equal parts gives each part $r = \frac{100\,\Omega}{10} = 10\,\Omega$.
2. Five parts in series: $R_s = 5r = 5 \times 10\,\Omega = 50\,\Omega$.
3. Five parts in parallel: $R_p = \frac{r}{5} = \frac{10\,\Omega}{5} = 2\,\Omega$.
4. The two combinations in series: $R = R_s + R_p = 50\,\Omega + 2\,\Omega = 52\,\Omega$, which is option $2$.

**Subtopic:** Combination of Resistors · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 13)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q029_2afab118_13112026.png?v=2afab1187e79)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q029_68f7ca65_13112026.png?v=68f7ca6516ef)

---

## Q30

Physics · Magnetic Effect of Electric Current

Match List-I with List-II.
List-I (Material) | List-II (Susceptibility ($\chi$))
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| A | Diamagnetic | I | $\chi = 0$ |
| B | Ferromagnetic | II | $0 > \chi \geq -1$ |
| C | Paramagnetic | III | $\chi >> 1$ |
| D | Non-magnetic | IV | $0 < \chi < \varepsilon$ (a small positive number) |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-II, B-I, C-III, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (Material) | (Susceptibility ($\chi$))
2. Diamagnetic | (II) $0 > \chi \geq -1$
3. Ferromagnetic | (III) $\chi >> 1$
4. Paramagnetic | (IV) $0 < \chi < \varepsilon$
5. Non-magnetic | (I) $\chi = 0$

**Solved independently** (answer withheld)

1. Diamagnetic materials have a small negative susceptibility, $-1 \leq \chi < 0$, so A matches II.
2. Ferromagnetic materials have a very large positive susceptibility, $\chi \gg 1$, so B matches III.
3. Paramagnetic materials have a small positive susceptibility, $0 < \chi < \varepsilon$, so C matches IV.
4. Non-magnetic materials have $\chi = 0$, so D matches I.
5. A-II, B-III, C-IV, D-I is option $1$.

**Subtopic:** Magnetism and Matter · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 13)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q030_d262a206_13112026.png?v=d262a206f51a)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q030_4f52016d_13112026.png?v=4f52016db07c)

---

## Q31

Physics · Modern Physics

$\mathrm{{}^{290}_{82}X \xrightarrow{\alpha} Y \xrightarrow{e^{+}} Z \xrightarrow{\beta^{-}} P \xrightarrow{e^{-}} Q}$
In the nuclear emission stated above, the mass number and atomic number of the product $Q$ respectively, are

- (1) 280, 81
- (2) 286, 80
- (3) 288, 82
- **(4)** 286, 81

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{{}^{290}_{82}X \xrightarrow{\alpha} {}^{286}_{80}Y \xrightarrow{e^{+}} {}^{286}_{79}Z \xrightarrow{\beta^{-}} {}^{286}_{80}P \xrightarrow{e^{-}} {}^{286}_{81}Q}$
2. $A \rightarrow 286$
3. $Z = 81$

**Solved independently** (answer withheld)

1. $\alpha$ decay: $A = 290 - 4 = 286$, $Z = 82 - 2 = 80$, so $Y = {}^{286}_{80}Y$.
2. Positron ($e^{+}$) emission: $A$ unchanged, $Z = 80 - 1 = 79$, so $Z = {}^{286}_{79}Z$.
3. $\beta^{-}$ emission: $A$ unchanged, $Z = 79 + 1 = 80$, so $P = {}^{286}_{80}P$.
4. Electron ($e^{-}$) emission is another $\beta^{-}$ decay: $Z = 80 + 1 = 81$, so $Q = {}^{286}_{81}Q$.
5. Mass number $286$, atomic number $81$, which is option $4$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 14)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q031_af2668cf_13112026.png?v=af2668cfe68a)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q031_38397119_13112026.png?v=38397119ac59)

---

## Q32

Physics · Modern Physics

The graph which shows the variation of $\left(\frac{1}{\lambda^2}\right)$ and its kinetic energy, $E$ is (where $\lambda$ is de Broglie wavelength of a free particle):

- (1) ![printed figure: Graph of 1/lambda^2 against E: curve through origin, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q032_option_1_378d4222_13112026.png?v=378d4222e538) *Graph of 1/lambda^2 against E: curve through origin, concave upward* ![drawn: Graph of 1/lambda^2 against E: curve through origin, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q032_option_1_acf331a8_13112026.svg?v=acf331a8081b)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Graph of 1/lambda^2 against E: a falling curve concave up](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q032_option_2_1a25782c_13112026.png?v=1a25782cc862) *Graph of 1/lambda^2 against E: a falling curve concave up* ![drawn: Graph of 1/lambda^2 against E: a falling curve concave up](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q032_option_2_cda60d6e_13112026.svg?v=cda60d6e5713)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: 1/lambda^2 versus E: a curve rising from O, concave down](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q032_option_3_ad606854_13112026.png?v=ad606854bf2f) *1/lambda^2 versus E: a curve rising from O, concave down* ![drawn: 1/lambda^2 versus E: a curve rising from O, concave down](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q032_option_3_a75a6a0f_13112026.svg?v=a75a6a0f7d68)  
*drawn by code/lib/physics_figure.py*
- **(4)** ![printed figure: Graph of 1/lambda^2 against E: straight line through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q032_option_4_5daa2bde_13112026.png?v=5daa2bdedc56) *Graph of 1/lambda^2 against E: straight line through the origin* ![drawn: Graph of 1/lambda^2 against E: straight line through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q032_option_4_6b8191e3_13112026.svg?v=6b8191e3f2b2)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. de-Broglie wavelength $\lambda = \frac{h}{P} = \frac{h}{mv} = \frac{h}{\sqrt{2\,mE}}$ where $E = \frac{1}{2}mv^{2}$
2. Squaring both sides,
3. $\lambda^{2} = \frac{h^{2}}{4m^{2}E}$
4. $\Rightarrow \frac{1}{\lambda^{2}} = (\text{constant})\,E$
5. Graph passes through origin with constant slope.

**Solved independently** (answer withheld)

1. For a free particle, $p = \sqrt{2mE}$, so $\lambda = \frac{h}{\sqrt{2mE}}$.
2. Squaring and inverting: $\frac{1}{\lambda^2} = \frac{2m}{h^2}E$.
3. $\frac{1}{\lambda^2} \propto E$, a straight line through the origin, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q032_b06c055b_13112026.png?v=b06c055b5fe1)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q032_4417d73c_13112026.png?v=4417d73c15bb)

---

## Q33

Physics · Alternating Current

In an ideal transformer, the turns ratio is $\frac{N_P}{N_S} = \frac{1}{2}$. The ratio $V_S : V_P$ is equal to (the symbols carry their usual meaning) :

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $1 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to transformer ratio,
2. $\frac{V_S}{V_P} = \frac{N_S}{N_P} = 2 : 1$

**Solved independently** (answer withheld)

1. For an ideal transformer, $\frac{V_S}{V_P} = \frac{N_S}{N_P}$.
2. Given $\frac{N_P}{N_S} = \frac{1}{2}$, so $\frac{N_S}{N_P} = 2$.
3. $V_S : V_P = 2 : 1$, which is option $2$.

**Subtopic:** Transformer · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q033_bffe2604_13112026.png?v=bffe2604282a)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q033_0f21cfda_13112026.png?v=0f21cfda9f63)

---

## Q34

Physics · Thermodynamics

A thermodynamic system is taken through the cycle $abcda$. The work done by the gas along the path $bc$ is:

![printed figure: P-V cycle abcda: rectangle between 100 and 300 kPa, 100 and 400 cm^3](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q034_bc9d21a6_13112026.png?v=bc9d21a65d4e)

*P-V cycle abcda: rectangle between 100 and 300 kPa, 100 and 400 cm^3*

![drawn: P-V cycle abcda: rectangle between 100 and 300 kPa, 100 and 400 cm^3](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q034_question_f0085bd5_13112026.svg?v=f0085bd51119)  
*drawn by code/lib/physics_figure.py*

- **(1)** Zero
- (2) $30\,\mathrm{J}$
- (3) $-90\,\mathrm{J}$
- (4) $-60\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Path $bc$ is an isochoric process.
2. $\therefore$ Work done by gas along path $bc$ is zero.

**Solved independently** (answer withheld)

1. From the figure, $b$ and $c$ both lie at $V = 400\,\mathrm{cm^3}$; only $P$ changes from $100\,\mathrm{kPa}$ to $300\,\mathrm{kPa}$.
2. Along $bc$, $dV = 0$, so $W_{bc} = \int P\,dV = 0$, which is option $1$.

**Subtopic:** Isochoric Process · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q034_f12bc54f_13112026.png?v=f12bc54fa0e7)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q034_35cb75fe_13112026.png?v=35cb75fe7da6)

---

## Q35

Physics · Capacitance

In the following circuit, the equivalent capacitance between terminal $A$ and terminal $B$ is :

![printed figure: Five 2 uF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q035_45189f4f_13112026.png?v=45189f4fc0b8)

*Five 2 uF capacitors in a bridge between terminals A and B*

![drawn: Five 2 uF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q035_question_ee573476_13112026.svg?v=ee573476e5da)  
*drawn by code/lib/physics_figure.py*

- **(1)** $2\,\mu\mathrm{F}$
- (2) $1\,\mu\mathrm{F}$
- (3) $0.5\,\mu\mathrm{F}$
- (4) $4\,\mu\mathrm{F}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Given circuit is balanced Wheatstone bridge
2. $C_{AB} = 1 + 1 = 2\,\mu\mathrm{F}$

**Solved independently** (answer withheld)

1. The circuit is a Wheatstone bridge: $A$ to the top and bottom middle nodes through $2\,\mu F$ each, those nodes to $B$ through $2\,\mu F$ each, and a $2\,\mu F$ capacitor joining the two middle nodes.
2. Balance condition: $\frac{C_1}{C_2} = \frac{2}{2} = \frac{C_3}{C_4} = \frac{2}{2}$, so the middle nodes are at equal potential and the middle capacitor holds no charge.
3. Each branch is two $2\,\mu F$ capacitors in series: $C_s = \frac{2 \times 2}{2 + 2} = 1\,\mu F$.
4. The two branches are in parallel: $C_{AB} = 1 + 1 = 2\,\mu F$, which is option $1$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q035_6a0685f0_13112026.png?v=6a0685f005fb)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q035_4ca09036_13112026.png?v=4ca09036f189)

---

## Q36

Physics · Capacitance

If the plates of a parallel plate capacitor connected to a battery are moved close to each other, then
Choose the most appropriate answer from the options given below:

- (A) the charge stored in it, increases.
- (B) the energy stored in it, decreases.
- (C) its capacitance increases.
- (D) the ratio of charge to its potential remains the same.
- (E) the product of charge and voltage increases.

- (1) A, B and E only
- **(2)** A, C and E only
- (3) B, D and E only
- (4) A, B and C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Given $V' = V = \text{Constant}$
2. (i) $C' = \frac{\varepsilon_0 A}{d'}, C = \frac{\varepsilon_0 A}{d}$
3. $d' < d$
4. $C' > C$
5. Hence, final capacitance greater than initial capacitance,
6. (ii) $U' = \frac{1}{2}C'V^{2}$
7. $U = \frac{1}{2}CV^{2}$
8. $U' > U$
9. Hence final energy is greater than initial energy
10. (iii) $\frac{Q'}{V'} = C'$ and $\frac{Q}{V} = C$
11. $\frac{Q'}{V'} \neq \frac{Q}{V}$
12. (iv) Product of charge and voltage
13. $X' = Q'V = C'V^{2}$
14. $X = QV = CV^{2}$
15. $X' > X$

**Solved independently** (answer withheld)

1. The capacitor stays connected to the battery, so $V$ is constant.
2. $C = \frac{\varepsilon_0 A}{d}$; decreasing $d$ makes $C$ increase, so C is true.
3. $Q = CV$ increases with $C$ at constant $V$, so A is true.
4. $U = \frac{1}{2}CV^2$ increases, so B (energy decreases) is false.
5. $\frac{Q}{V} = C$ changes (increases), so D is false.
6. $QV = CV^2$ increases, so E is true.
7. True statements are A, C and E, which is option $2$.

**Subtopic:** The Parallel Plate Capacitor, Energy Stored in a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q036_2d0dc803_13112026.png?v=2d0dc8032c48)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q036_7216e6da_13112026.png?v=7216e6da32f9)

---

## Q37

Physics · Alternating Current

A $10\,\mu\mathrm{F}$ capacitor is connected to a $210\,\mathrm{V}$, $50\,\mathrm{Hz}$ source as shown in figure. The peak current in the circuit is nearly ($\pi = 3.14$):

![printed figure: A capacitor C = 10 uF across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q037_0e403b59_13112026.png?v=0e403b595f89)

*A capacitor C = 10 uF across a 210 V, 50 Hz AC source in one loop*

![drawn: A capacitor C = 10 uF across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q037_question_f176f680_13112026.svg?v=f176f6808665)  
*drawn by code/lib/physics_figure.py*

- (1) $0.58\,\mathrm{A}$
- **(2)** $0.93\,\mathrm{A}$
- (3) $1.20\,\mathrm{A}$
- (4) $0.35\,\mathrm{A}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Capacitive Reactance $X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} = \frac{1}{2 \times 3.14 \times 50 \times 10 \times 10^{-6}}$
2. $= \frac{1000}{3.14}$
3. $V_{\mathrm{rms}} = 210\,\mathrm{V}$
4. $i_{\mathrm{rms}} = \frac{V_{\mathrm{rms}}}{X_C} = \frac{210}{X_C}$
5. Peak current $= \sqrt{2} i_{\mathrm{rms}} = \sqrt{2} \times \frac{210}{1000} \times 3.14 = 0.932$
6. $\simeq 0.93\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Capacitive reactance: $X_C = \frac{1}{2\pi f C} = \frac{1}{2 \times 3.14 \times 50 \times 10 \times 10^{-6}} = \frac{1}{3.14 \times 10^{-3}} \approx 318.5\,\Omega$.
2. The 210 V is the rms value, so $I_{rms} = \frac{V_{rms}}{X_C} = \frac{210}{318.5} \approx 0.659\,\mathrm{A}$.
3. Peak current $I_0 = \sqrt{2}\, I_{rms} = 1.414 \times 0.659 \approx 0.93\,\mathrm{A}$, which is option $2$.

**Subtopic:** AC Voltage Applied to a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q037_24b43d5a_13112026.png?v=24b43d5a199b)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q037_6642d332_13112026.png?v=6642d3326bfd)

---

## Q38

Physics · Units and Measurements

A force defined by $F = \alpha t^{2} + \beta t$ acts on a particle at a given time $t$. The factor which is dimensionless, if $\alpha$ and $\beta$ are constants, is:

- (1) $\beta t/\alpha$
- **(2)** $\alpha t/\beta$
- (3) $\alpha\beta t$
- (4) $\alpha\beta/t$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. From principle of homogeneity
2. $[F] = [\alpha t^{2}] = [\beta t]$
3. $[\alpha] = \frac{[F]}{[t^{2}]}$ and $[\beta] = \frac{[F]}{[t]}$
4. $\therefore\ [\alpha]\,[t] = [\beta]$
5. $\therefore\ \frac{\alpha t}{\beta} =$ dimensionless

**Solved independently** (answer withheld)

1. Each term must have the dimensions of force: $[\alpha t^{2}] = [F]$, so $[\alpha] = [F]\,T^{-2}$.
2. Likewise $[\beta t] = [F]$, so $[\beta] = [F]\,T^{-1}$.
3. $\left[\frac{\alpha t}{\beta}\right] = \frac{[F]\,T^{-2}\cdot T}{[F]\,T^{-1}} = 1$, dimensionless, which is option $2$.

**Subtopic:** Homogeneity of Dimensions in an Equation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q038_441d4ae4_13112026.png?v=441d4ae4f6fc)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q038_0b57cafc_13112026.png?v=0b57cafc5334)

---

## Q39

Physics · Thermodynamics

The following graph represents the $T$-$V$ curves of an ideal gas (where $T$ is the temperature and $V$ the volume) at three pressures $P_1$, $P_2$ and $P_3$ compared with those of Charles’s law represented as dotted lines. Then the correct relation is:

![printed figure: T-V curves of an ideal gas at pressures P1, P2, P3 with dashed Charles's law lines](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q039_2b146617_13112026.png?v=2b1466174218)

*T-V curves of an ideal gas at pressures P1, P2, P3 with dashed Charles's law lines*

![drawn: T-V curves of an ideal gas at pressures P1, P2, P3 with dashed Charles's law lines](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q039_question_66b31418_13112026.svg?v=66b314180250)  
*drawn by code/lib/physics_figure.py*

- (1) $P_3 > P_2 > P_1$
- (2) $P_1 > P_3 > P_2$
- (3) $P_2 > P_1 > P_3$
- **(4)** $P_1 > P_2 > P_3$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. At same temperature, curve with higher volume corresponds to lower pressure.
2. $V_3 > V_2 > V_1$
3. $\Rightarrow P_1 > P_2 > P_3$
4. (We draw a straight line parallel to volume axis to get this)

**Solved independently** (answer withheld)

1. Ideal gas law: $PV = nRT \Rightarrow T = \frac{P}{nR}V$.
2. At constant $P$, the $T$-$V$ (Charles's law) line has slope $\frac{P}{nR}$, so a steeper line means a higher pressure.
3. From the figure, the $P_1$ line is steepest, then $P_2$, and $P_3$ is flattest.
4. Hence $P_1 > P_2 > P_3$, which is option $4$.

**Subtopic:** Gas Laws, Problems on Different Graphs of P, V, and T · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q039_137893dd_13112026.png?v=137893dd73e5)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q039_a3e5281b_13112026.png?v=a3e5281b8b15)

---

## Q40

Physics · Magnetic Effect of Electric Current

An iron bar of length $L$ has magnetic moment $M$. It is bent at the middle of its length such that the two arms make an angle $60^\circ$ with each other. The magnetic moment of this new magnet is :

- (1) $M$
- **(2)** $\frac{M}{2}$
- (3) $2M$
- (4) $\frac{M}{\sqrt{3}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $M = ml.$
2. $\Delta l = 2\frac{l}{2}\sin 30^\circ$
3. $= \frac{l}{2}$
4. $M' = ml/2$
5. $= M/2$

**Solved independently** (answer withheld)

1. Original moment: $M = m L$, where $m$ is the pole strength.
2. Bending at the middle gives two arms of length $\frac{L}{2}$ with $60^\circ$ between them.
3. The two arms and the line joining the poles form an equilateral triangle, so the pole separation is $\frac{L}{2}$.
4. $M' = m \cdot \frac{L}{2} = \frac{M}{2}$, which is option $2$.

**Subtopic:** Permanent Magnet and the Bar Magnet · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q040_7da18181_13112026.png?v=7da18181f19b)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q040_b8f06db3_13112026.png?v=b8f06db3da2c)

---

## Q41

Physics · Electromagnetic Waves

A parallel plate capacitor is charged by connecting it to a battery through a resistor. If $I$ is the current in the circuit, then in the gap between the plates:

- (1) There is no current
- **(2)** Displacement current of magnitude equal to $I$ flows in the same direction as $I$
- (3) Displacement current of magnitude equal to $I$ flows in a direction opposite to that of $I$
- (4) Displacement current of magnitude greater than $I$ flows but can be in any direction

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to modified Ampere's law
2. $\oint B.\,dl = \mu_0(I_C + I_D)$
3. For Loop $L_1$ $\quad I_C \neq 0$ and $I_D = 0$
4. For Loop $L_2$ $\quad I_C = 0$ and $I_D \neq 0$
5. Due to KCL $\quad I_C = I_D$

**Solved independently** (answer withheld)

1. In the gap, $E = \frac{q}{\varepsilon_0 A}$, so $\Phi_E = EA = \frac{q}{\varepsilon_0}$.
2. $I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \frac{dq}{dt} = I$.
3. While charging, $E$ grows in the direction of conduction current flow, so $I_d$ is in the same direction as $I$: option $2$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 18)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q041_a1ad8c9f_13112026.png?v=a1ad8c9f6474)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q041_427aced4_13112026.png?v=427aced4115b)

---

## Q42

Physics · Mechanical Properties of Solids

A metallic bar of Young’s modulus, $0.5 \times 10^{11}\,\mathrm{N\,m^{-2}}$ and coefficient of linear thermal expansion $10^{-5}\,{}^{\circ}\mathrm{C}^{-1}$, length $1\,\mathrm{m}$ and area of cross-section $10^{-3}\,\mathrm{m^{2}}$ is heated from $0^{\circ}\mathrm{C}$ to $100^{\circ}\mathrm{C}$ without expansion or bending. The compressive force developed in it is :

- (1) $5 \times 10^{3}\,\mathrm{N}$
- **(2)** $50 \times 10^{3}\,\mathrm{N}$
- (3) $100 \times 10^{3}\,\mathrm{N}$
- (4) $2 \times 10^{3}\,\mathrm{N}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Thermal strain $=$ Longitudinal strain $= \alpha\,\Delta T$
2. $\Rightarrow$ Longitudinal strain, $\delta = 10^{-5} \times 10^{2} = 10^{-3}$
3. $\Rightarrow$ Compressive stress $= \delta \times$ Young's Modulus
4. $= 10^{-3} \times 0.5 \times 10^{11}$
5. $= 0.5 \times 10^{8}$
6. $\Rightarrow$ Compressive force $= 0.5 \times 10^{8} \times 10^{-3} = 0.5 \times 10^{5}$
7. $= 5 \times 10^{4} \times \frac{10}{10} = 50 \times 10^{3}\,\mathrm{N}$

**Solved independently** (answer withheld)

1. Prevented expansion gives thermal strain $\varepsilon = \alpha \Delta T = 10^{-5} \times 100 = 10^{-3}$.
2. Stress $\sigma = Y \varepsilon = 0.5 \times 10^{11} \times 10^{-3} = 0.5 \times 10^{8}\,\mathrm{N\,m^{-2}}$.
3. $F = \sigma A = 0.5 \times 10^{8} \times 10^{-3} = 5 \times 10^{4}\,\mathrm{N} = 50 \times 10^{3}\,\mathrm{N}$, which is option $2$.

**Subtopic:** Thermal Stress and Strain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q042_296c4d2e_13112026.png?v=296c4d2e8953)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q042_2d70119e_13112026.png?v=2d70119e7464)

---

## Q43

Physics · Current Electricity

> ⚠ The independent solve found no printed option exactly right ("which no option gives"); its pick (1) is the closest fit, so treat this question as possibly misprinted.

> ⚠ With the printed arm values (10, 10, 15 and 5 ohm) no circuit balances for an ideal diode. The booklet keys (1) and its own solution balances it only by giving the forward-biased diode a "dynamic resistance" R_D = 10 ohm (10/15 = 10/(5 + R_D)), a value the question never states. Another reading takes a reverse-biased diode as an open arm. The key is the same question's key in every 2024 booklet code.

Choose the correct circuit which can achieve the bridge balance.

- **(1)** ![printed figure: Option 1: Wheatstone bridge with 10, 10, 15 and 5 ohm arms, diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q043_option_1_2ed47791_13112026.png?v=2ed47791384b) *Option 1: Wheatstone bridge with 10, 10, 15 and 5 ohm arms, diode D in the 5 ohm arm, galvanometer G, cell E and key K* ![drawn: Option 1: Wheatstone bridge with 10, 10, 15 and 5 ohm arms, diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q043_option_1_fc2ccd75_13112026.svg?v=fc2ccd751d86)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and 5 ohm arms, diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q043_option_2_554e752f_13112026.png?v=554e752fe168) *Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and 5 ohm arms, diode D in the 5 ohm arm, galvanometer G, cell E and key K* ![drawn: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and 5 ohm arms, diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q043_option_2_c6e27e7d_13112026.svg?v=c6e27e7d2833)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Wheatstone bridge: 10 ohm, 10 ohm, 15 ohm arms, diode D in parallel with 5 ohm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q043_option_3_884cd9b2_13112026.png?v=884cd9b25a1f) *Wheatstone bridge: 10 ohm, 10 ohm, 15 ohm arms, diode D in parallel with 5 ohm, galvanometer G, cell E and key K* ![drawn: Wheatstone bridge: 10 ohm, 10 ohm, 15 ohm arms, diode D in parallel with 5 ohm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q043_option_3_bb9d8a38_13112026.svg?v=bb9d8a38705a)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Wheatstone bridge with galvanometer G between the junctions and diode D in series with 5 ohm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q043_option_4_db0568ac_13112026.png?v=db0568ac52ec) *Wheatstone bridge with galvanometer G between the junctions and diode D in series with 5 ohm, cell E and key K* ![drawn: Wheatstone bridge with galvanometer G between the junctions and diode D in series with 5 ohm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q043_option_4_cc2fdb0b_13112026.svg?v=cc2fdb0b3bcf)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In option (1),
2. $\frac{10}{15} = \frac{10}{5 + R_D}$
3. The diode can conduct and have resistance $R_D = 10\,\Omega$ because diode have dynamic resistance. In that case bridge will be balanced.

**Solved independently** (answer withheld)

1. Wheatstone bridge balance condition: $\frac{P}{Q} = \frac{R}{S}$, with $P = 10\,\Omega$, $Q = 10\,\Omega$ (top arms), $R = 15\,\Omega$, $S$ = lower-right arm.
2. Balance requires $S = \frac{QR}{P} = \frac{10 \times 15}{10} = 15\,\Omega$.
3. Taking the cell's long plate on the left, current enters the bridge at the left node and leaves at the right node, so it flows through the lower-right arm towards the right node.
4. Option 1: the diode points in the direction of current, so it is forward biased (ideal, $R_D = 0$) in series with $5\,\Omega$, so $S = 5\,\Omega$.
5. Options 2 and 4: the diode is reverse biased in series, so $S \to \infty$ and the arm is open; no balance is possible.
6. Option 3: the diode is forward biased in parallel with $5\,\Omega$ and shorts it, so $S = 0$; no balance is possible.
7. None gives $S = 15\,\Omega$; option $1$ is the only circuit with a conducting finite arm, so it is the best choice.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 19)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q043_0c285010_13112026.png?v=0c285010e5e1)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q043_ce0ce833_13112026.png?v=ce0ce833342d)

---

## Q44

Physics · Kinematics

The velocity $(v)$ – time $(t)$ plot of the motion of a body is shown below: The acceleration $(a)$ – time $(t)$ graph that best suits this motion is :

![printed figure: Velocity-time graph: zero, uniform rise, constant, uniform fall to zero](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q044_25a518a3_13112026.png?v=25a518a3ce03)

*Velocity-time graph: zero, uniform rise, constant, uniform fall to zero*

![drawn: Velocity-time graph: zero, uniform rise, constant, uniform fall to zero](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q044_question_435e7d60_13112026.svg?v=435e7d602dad)  
*drawn by code/lib/physics_figure.py*

- (1) ![printed figure: Option (1): a-t graph, trapezoidal pulse of acceleration above the time axis](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q044_option_1_afc52151_13112026.png?v=afc521515463) *Option (1): a-t graph, trapezoidal pulse of acceleration above the time axis* ![drawn: Option (1): a-t graph, trapezoidal pulse of acceleration above the time axis](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q044_option_1_fd8aa8c8_13112026.svg?v=fd8aa8c8ef5d)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q044_option_2_68c2bb05_13112026.png?v=68c2bb052be6) *Acceleration-time graph: zero, then rising linearly, then constant* ![drawn: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q044_option_2_9bb6e764_13112026.svg?v=9bb6e764a074)  
*drawn by code/lib/physics_figure.py*
- **(3)** ![printed figure: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q044_option_3_40374041_13112026.png?v=40374041a94c) *Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse* ![drawn: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q044_option_3_36e78d27_13112026.svg?v=36e78d27b62c)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Option 4: a-t graph, zero then a negative constant step, then zero, then a linearly rising acceleration](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q044_option_4_4d0281a8_13112026.png?v=4d0281a862a0) *Option 4: a-t graph, zero then a negative constant step, then zero, then a linearly rising acceleration* ![drawn: Option 4: a-t graph, zero then a negative constant step, then zero, then a linearly rising acceleration](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q044_option_4_b08a5788_13112026.svg?v=b08a5788ecd7)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Initially, the body has zero velocity and zero slope. Hence the acceleration would be zero initially. After that, the slope of $v$-$t$ curve is constant and positive.
2. After some time, velocity becomes constant and acceleration is zero.
3. After that, the slope of $v$-$t$ curve is constant and negative.

**Solved independently** (answer withheld)

1. Acceleration is the slope of the $v$-$t$ graph: $a = \frac{dv}{dt}$.
2. Initially $v = 0$ and constant, so $a = 0$.
3. On the rising straight segment the slope is constant and positive, so $a = +\text{const}$ (a positive rectangle).
4. On the flat segment $v$ is constant, so $a = 0$.
5. On the falling straight segment the slope is constant and negative, so $a = -\text{const}$ (a negative rectangle), then $a = 0$ after $v$ returns to $0$.
6. Positive block, zero, negative block matches option $3$.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 20)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q044_b2c26aff_13112026.png?v=b2c26affc243)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q044_327f9c26_13112026.png?v=327f9c261a05)

---

## Q45

Physics · Ray Optics

A small telescope has an objective of focal length $140\,\mathrm{cm}$ and an eye piece of focal length $5.0\,\mathrm{cm}$. The magnifying power of telescope for viewing a distant object is:

- (1) $34$
- **(2)** $28$
- (3) $17$
- (4) $32$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $f_0 = 140\,\mathrm{cm}$ and $f_e = 5\,\mathrm{cm}$
2. For distant object,
3. $m = \frac{f_0}{f_e} = \frac{140}{5} = 28$

**Solved independently** (answer withheld)

1. For a distant object viewed in normal adjustment, the magnifying power of a telescope is $m = \frac{f_o}{f_e}$.
2. $m = \frac{140\,\mathrm{cm}}{5.0\,\mathrm{cm}} = 28$, which is option $2$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 20)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q045_5d8f3714_13112026.png?v=5d8f3714c222)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q045_418d3a19_13112026.png?v=418d3a19408b)

---

## Q46

Physics · Gravitation

The minimum energy required to launch a satellite of mass $m$ from the surface of earth of mass $M$ and radius $R$ in a circular orbit at an altitude of $2R$ from the surface of the earth is:

- **(1)** $\frac{5GmM}{6R}$
- (2) $\frac{2GmM}{3R}$
- (3) $\frac{GmM}{2R}$
- (4) $\frac{GmM}{3R}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Apply energy conservation,
2. $U_i + K_i = U_f + K_f$
3. $\Rightarrow -\frac{GMm}{R} + K_i = -\frac{GMm}{3R} + \frac{1}{2}mv^{2}$
4. $\Rightarrow -\frac{GMm}{R} + K_i = -\frac{GMm}{3R} + \frac{1}{2} \times m \times \frac{GM}{3R}$
5. $\Rightarrow K_i = -\frac{1}{6}\frac{GMm}{R} + \frac{GMm}{R}$
6. $K_i = \frac{5}{6}\frac{GMm}{R}$

**Solved independently** (answer withheld)

1. Orbit radius from the centre: $r = R + 2R = 3R$.
2. Total energy in circular orbit: $E_{orbit} = -\frac{GMm}{2r} = -\frac{GMm}{6R}$.
3. Energy at rest on the surface: $E_{surface} = -\frac{GMm}{R}$.
4. $E_{min} = E_{orbit} - E_{surface} = -\frac{GMm}{6R} + \frac{GMm}{R} = \frac{5GMm}{6R}$, which is option $1$.

**Subtopic:** Motion of a Satellite · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 21)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q046_67561f50_13112026.png?v=67561f504acf)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q046_11993ee6_13112026.png?v=11993ee6a7c6)

---

## Q47

Physics · Oscillations

If the mass of the bob in a simple pendulum is increased to thrice its original mass and its length is made half its original length, then the new time period of oscillation is $\frac{x}{2}$ times its original time period. Then the value of $x$ is:

- (1) $\sqrt{3}$
- **(2)** $\sqrt{2}$
- (3) $2\sqrt{3}$
- (4) $4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $T' = 2\pi\sqrt{\frac{\ell'}{g}}$ where $\ell' = \frac{\ell}{2}$
2. $T = 2\pi\sqrt{\frac{\ell}{g}}$
3. $T' = \frac{x}{2}T$
4. $2\pi\sqrt{\frac{\ell}{2g}} = \frac{x}{2}2\pi\sqrt{\frac{\ell}{g}}$
5. $\frac{1}{\sqrt{2}} = \frac{x}{2} \Rightarrow x = \sqrt{2}$

**Solved independently** (answer withheld)

1. $T = 2\pi\sqrt{\frac{l}{g}}$ is independent of the bob's mass, so tripling the mass has no effect.
2. $T' = 2\pi\sqrt{\frac{l/2}{g}} = \frac{T}{\sqrt{2}}$.
3. $\frac{T}{\sqrt{2}} = \frac{\sqrt{2}}{2}T = \frac{x}{2}T \Rightarrow x = \sqrt{2}$, which is option $2$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 21)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q047_7aaf372a_13112026.png?v=7aaf372a976e)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q047_c88b8e35_13112026.png?v=c88b8e352f86)

---

## Q48

Physics · Electromagnetic Induction

A sheet is placed on a horizontal surface in front of a strong magnetic pole. A force is needed to: Choose the correct statement(s) from the options given below:

- (A) hold the sheet there if it is magnetic.
- (B) hold the sheet there if it is non-magnetic.
- (C) move the sheet away from the pole with uniform velocity if it is conducting.
- (D) move the sheet away from the pole with uniform velocity if it is both, non-conducting and non-polar.

- (1) B and D only
- **(2)** A and C only
- (3) A, C and D only
- (4) C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A. A magnetic pole will repel or attract magnetic sheet so force is need.
2. B. If sheet is non-magnetic, no force needed.
3. C. If it is conducting, then there will be addy current in sheet, which opposes the motion. So forces is needed move sheet with uniform speed.
4. D. The non-conducting and non-polar sheet do not interact with magnetic field of magnet.

**Solved independently** (answer withheld)

1. A magnetic sheet is attracted by the strong pole, so a force $\vec F_{\text{hold}} = -\vec F_{\text{mag}}$ is needed to hold it: A is true.
2. A non-magnetic sheet feels no magnetic force at rest, so $\vec F_{\text{net}} = 0$ without any applied force: B is false.
3. A conducting sheet moving in the non-uniform field has changing flux $\frac{d\Phi}{dt} \neq 0$, so eddy currents are induced.
4. By Lenz's law the eddy currents oppose the motion, so an applied force is needed to keep $v$ uniform: C is true.
5. A non-conducting, non-polar sheet has no induced currents and no magnetic force, so uniform velocity needs $F = 0$: D is false.
6. True statements are $A$ and $C$, which is option $2$.

**Subtopic:** Eddy Currents · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 21)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q048_5b791cd4_13112026.png?v=5b791cd4c26e)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q048_ef7c5804_13112026.png?v=ef7c58047235)

---

## Q49

Physics · Current Electricity

Two heaters A and B have power rating of $1\,\mathrm{kW}$ and $2\,\mathrm{kW}$, respectively. Those two are first connected in series and then in parallel to a fixed power source. The ratio of power outputs for these two cases is:

- (1) $1:1$
- **(2)** $2:9$
- (3) $1:2$
- (4) $2:3$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Power Consumed $= P = \frac{V^{2}}{R}$
2. $\frac{P_A}{P_B} = \frac{R_B}{R_A}$
3. $R_A = 2R_B$
4. For Series Combination
5. $P_S = \frac{V^{2}}{3R_B}$
6. For Parallel Combination
7. $P_P = \frac{3V^{2}}{2R_B}$
8. $\frac{P_S}{P_P} = \frac{2}{9}$

**Solved independently** (answer withheld)

1. With a fixed source voltage $V$, each heater has $R = \frac{V^2}{P}$, so $R_A = \frac{V^2}{1\,\mathrm{kW}}$ and $R_B = \frac{V^2}{2\,\mathrm{kW}}$.
2. In series, $\frac{1}{P_s} = \frac{1}{P_A} + \frac{1}{P_B} = \frac{1}{1} + \frac{1}{2} = \frac{3}{2}$, so $P_s = \frac{2}{3}\,\mathrm{kW}$.
3. In parallel, $P_p = P_A + P_B = 1 + 2 = 3\,\mathrm{kW}$.
4. $\frac{P_s}{P_p} = \frac{2/3}{3} = \frac{2}{9}$, i.e. $2:9$, which is option $2$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q049_1aa66468_13112026.png?v=1aa664684705)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q049_b0bb3476_13112026.png?v=b0bb34766928)

---

## Q50

Physics · Electromagnetic Waves

The property which is not of an electromagnetic wave travelling in free space is that:

- (1) They are transverse in nature
- (2) The energy density in electric field is equal to energy density in magnetic field
- (3) They travel with a speed equal to $\frac{1}{\sqrt{\mu_0\varepsilon_0}}$
- **(4)** They originate from charges moving with uniform speed

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The EM waves originate from an accelerating charge.
2. The charge moving with uniform velocity produces steady state magnetic field.

**Solved independently** (answer withheld)

1. Charges moving with uniform velocity produce steady currents and static fields; only accelerated or oscillating charges radiate EM waves, so statement 1 is false.
2. EM waves are transverse ($\vec E \perp \vec B \perp \vec k$), $u_E = \frac{1}{2}\varepsilon_0 E^2 = \frac{B^2}{2\mu_0} = u_B$, and $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, so options 1, 2, 3 are true; the answer is option $4$.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q050_f718c22a_13112026.png?v=f718c22a95e7)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q050_b1b53724_13112026.png?v=b1b53724b6e4)

---

## Q51

Chemistry · inorganic · The p–Block Elements

Among Group 16 elements, which one does NOT show $-2$ oxidation state?

- (1) $\mathrm{O}$
- (2) $\mathrm{Se}$
- (3) $\mathrm{Te}$
- **(4)** $\mathrm{Po}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Oxygen shows $-2$, $-1$, $+1$ and $+2$ oxidation states
2. Selenium shows $-2$, $+2$, $+4$ and $+6$ oxidation states
3. Tellurium shows $-2$, $+2$, $+4$ and $+6$ oxidation states
4. Polonium shows $+2$ and $+4$ oxidation states

**Solved independently** (answer withheld)

1. Down Group 16, stability of the $-2$ oxidation state decreases as metallic character increases; $\mathrm{O}$, $\mathrm{Se}$ and $\mathrm{Te}$ show $-2$, while $\mathrm{Po}$ hardly shows it, so the answer is option $4$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q051_25cb9fef_13112026.png?v=25cb9fef05b9)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q051_d8ce2566_13112026.png?v=d8ce2566e143)

---

## Q52

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.
List I (Molecule)
List II (Number and types of bond/s between two carbon atoms)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | ethane | I | one $\sigma$-bond and two $\pi$-bonds |
| B | ethene | II | two $\pi$-bonds |
| C | carbon molecule, $\mathrm{C_2}$ | III | one $\sigma$-bond |
| D | ethyne | IV | one $\sigma$-bond and one $\pi$-bond |

- (1) A-I, B-IV, C-II, D-III
- (2) A-IV, B-III, C-II, D-I
- **(3)** A-III, B-IV, C-II, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) Ethane: one $(\mathrm{C-C})$ $\sigma$ bond
2. (B) Ethene: one $(\mathrm{C-C})$ $\sigma$ and one $(\mathrm{C-C})$ $\pi$ bond
3. (C) $\mathrm{C_2}$: two $(\mathrm{C-C})$ $\pi$ bonds
4. (D) Ethyne $\mathrm{H-C\equiv C-H}$: two $(\mathrm{C-C})$ $\pi$ bonds and one $(\mathrm{C-C})$ $\sigma$ bond

**Solved independently** (answer withheld)

1. Ethane $\mathrm{C_2H_6}$ has a C$-$C single bond: one $\sigma$-bond, so A$-$III.
2. Ethene $\mathrm{C_2H_4}$ has a C$=$C double bond: one $\sigma$ and one $\pi$-bond, so B$-$IV.
3. In $\mathrm{C_2}$ (MO configuration $\sigma 1s^2\,\sigma^*1s^2\,\sigma 2s^2\,\sigma^*2s^2\,(\pi 2p_x^2 = \pi 2p_y^2)$), the bond order 2 comes from two $\pi$-bonds, so C$-$II.
4. Ethyne $\mathrm{C_2H_2}$ has a C$\equiv$C triple bond: one $\sigma$ and two $\pi$-bonds, so D$-$I.
5. A$-$III, B$-$IV, C$-$II, D$-$I is option $3$.

**Subtopic:** Molecular Orbital Theory, Orbital Overlap Concept · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q052_2383e10b_13112026.png?v=2383e10b6fe2)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q052_07444619_13112026.png?v=074446196ed6)

---

## Q53

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Fehling’s solution ‘A’ is

- **(1)** aqueous copper sulphate
- (2) alkaline copper sulphate
- (3) alkaline solution of sodium potassium tartrate (Rochelle’s salt)
- (4) aqueous sodium citrate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Fehling solution ‘A’ = Aqueous copper sulphate
2. Fehling solution ‘B’ = Alkaline sodium potassium tartrate (Rochelle salt)

**Solved independently** (answer withheld)

1. Fehling's reagent is prepared by mixing Fehling A (aqueous $\mathrm{CuSO_4}$) with Fehling B (alkaline sodium potassium tartrate), so Fehling A is option $1$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 24)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q053_b2a26d86_13112026.png?v=b2a26d8602a8)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q053_66fcb3a8_13112026.png?v=66fcb3a8ca24)

---

## Q54

Chemistry · physical · Electrochemistry

Match List I with List II.
List I (Conversion) | List II (Number of Faraday required)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | 1 mol of $\mathrm{H_2O}$ to $\mathrm{O_2}$ | I | $3\,\mathrm{F}$ |
| B | 1 mol of $\mathrm{MnO_4^-}$ to $\mathrm{Mn^{2+}}$ | II | $2\,\mathrm{F}$ |
| C | 1.5 mol of Ca from molten $\mathrm{CaCl_2}$ | III | $1\,\mathrm{F}$ |
| D | 1 mol of FeO to $\mathrm{Fe_2O_3}$ | IV | $5\,\mathrm{F}$ |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-I, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $4\mathrm{OH^-} \rightarrow 2\mathrm{H_2O} + \mathrm{O_2} + 4e^-$
2. for $2$ mole of $\mathrm{H_2O}$ = $4\,\mathrm{F}$ charge is required
3. for $1$ mole of $\mathrm{H_2O}$ = $\frac{4\,\mathrm{F}}{2} = 2\,\mathrm{F}$ required
4. $\overset{+7}{\mathrm{Mn}}\mathrm{O_4^-} \rightarrow \overset{+2}{\mathrm{Mn}}{}^{2+}$
5. for $1$ mole $\mathrm{MnO_4^-}$ $5\,\mathrm{F}$ charge is required
6. $\mathrm{Ca^{2+}} \xrightarrow{+2e^-} \mathrm{Ca}$
7. For $1$ mole $\mathrm{Ca^{2+}}$ ion required = $2\,\mathrm{F}$
8. $1.5$ mole $\mathrm{Ca^{2+}}$ ion required = $\frac{2}{1} \times 1.5 = 3\,\mathrm{F}$
9. $\overset{+2}{\mathrm{Fe}}\mathrm{O} \rightarrow \overset{+3}{\mathrm{Fe}}\mathrm{{}_2O_3}$
10. for $1$ mole $\mathrm{FeO}$, $1\,\mathrm{F}$ charge is required.

**Solved independently** (answer withheld)

1. A: $\mathrm{H_2O \rightarrow \tfrac{1}{2}O_2 + 2H^+ + 2e^-}$, oxygen goes from $-2$ to $0$, so $2\,\mathrm{F}$ per mol (II).
2. B: $\mathrm{MnO_4^- + 8H^+ + 5e^- \rightarrow Mn^{2+} + 4H_2O}$, Mn goes from $+7$ to $+2$, so $5\,\mathrm{F}$ (IV).
3. C: $\mathrm{Ca^{2+} + 2e^- \rightarrow Ca}$, so $1.5 \times 2 = 3\,\mathrm{F}$ (I).
4. D: In FeO Fe is $+2$, in $\mathrm{Fe_2O_3}$ Fe is $+3$, so $1\,\mathrm{F}$ per mol FeO (III).
5. A-II, B-IV, C-I, D-III matches option $1$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q054_584e6b0e_13112026.png?v=584e6b0ee7df)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q054_12d88937_13112026.png?v=12d88937b3fe)

---

## Q55

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the correct reagents that would bring about the following transformation.

![printed figure: prop-2-en-1-ylcyclohexane (cyclohexyl–CH₂–CH=CH₂) → 3-cyclohexylpropanal (cyclohexyl–CH₂–CH₂–CHO)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q055_994c62d9_13112026.png?v=994c62d9b6ab)

*prop-2-en-1-ylcyclohexane (cyclohexyl–CH₂–CH=CH₂) → 3-cyclohexylpropanal (cyclohexyl–CH₂–CH₂–CHO)*

![drawn: prop-2-en-1-ylcyclohexane (cyclohexyl–CH₂–CH=CH₂) → 3-cyclohexylpropanal (cyclohexyl–CH₂–CH₂–CHO)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q055_question_4ad0072e_13112026.svg?v=4ad0072e529b)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: prop-2-en-1-ylcyclohexane `C=CCC1CCCCC1` ![prop-2-en-1-ylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q055_question_s1_19da39bf_13112026.svg?v=19da39bfbc83); 3-cyclohexylpropanal `O=CCCC1CCCCC1` ![3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q055_question_s2_d5fc3230_13112026.svg?v=d5fc32301153)

- (1) (i) $\mathrm{H_2O/H^+}$ (ii) $\mathrm{CrO_3}$
- **(2)** (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2}/\overset{\ominus}{\mathrm{O}}\mathrm{H}$ (iii) PCC
- (3) (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2}/\overset{\ominus}{\mathrm{O}}\mathrm{H}$ (iii) alk.$\mathrm{KMnO_4}$ (iv) $\mathrm{H_3O^{\oplus}}$
- (4) (i) $\mathrm{H_2O/H^+}$ (ii) PCC

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Mechanism :

**Solved independently** (answer withheld)

1. The product has $\mathrm{-CHO}$ on the terminal carbon, so the terminal alkene carbon must become a primary alcohol (anti-Markovnikov addition of water).
2. $\mathrm{H_2O/H^+}$ adds water by Markovnikov's rule, giving the secondary alcohol $\mathrm{C_6H_{11}CH_2CH(OH)CH_3}$, which would oxidise to a ketone; options $4$ and $1$ are ruled out.
3. $\mathrm{BH_3}$ then $\mathrm{H_2O_2/OH^-}$ gives $\mathrm{C_6H_{11}CH_2CH_2CH_2OH}$ (anti-Markovnikov).
4. PCC oxidises a primary alcohol only to the aldehyde: $\mathrm{C_6H_{11}CH_2CH_2CHO}$, which is option $2$.
5. Alkaline $\mathrm{KMnO_4}$ then $\mathrm{H_3O^+}$ would give the carboxylic acid, so option $3$ is wrong.

**Subtopic:** Preparation of Aldehydes · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 25)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q055_0357c134_13112026.png?v=0357c1341552)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q055_031f4a08_13112026.png?v=031f4a084808)

---

## Q56

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Intramolecular hydrogen bonding is present in

- **(1)** 2-nitrophenol `O=[N+]([O-])c1ccccc1O` ![2-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q056_option_1_s1_af8d6416_13112026.svg?v=af8d641635dd)
- (2) 4-nitrophenol `O=[N+]([O-])c1ccc(O)cc1` ![4-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q056_option_2_s1_061f32a8_13112026.svg?v=061f32a8ba54)
- (3) 3-nitrophenol `O=[N+]([O-])c1cccc(O)c1` ![3-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q056_option_3_s1_683e3fc0_13112026.svg?v=683e3fc063ee)
- (4) $\mathrm{HF}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In o-nitrophenol intramolecular H-bonding is present.

**Solved independently** (answer withheld)

1. Option $1$ is $o$-nitrophenol: $-\mathrm{OH}$ and $-\mathrm{NO_2}$ are on adjacent carbons, so $\mathrm{O-H\cdots O}$ closes a six-membered ring within the molecule (intramolecular H-bond).
2. Options $2$ ($p$-nitrophenol) and $3$ ($m$-nitrophenol) have the groups too far apart, and $\mathrm{HF}$ (option $4$) has one H-bonding site per molecule, so these show only intermolecular H-bonding.
3. Hence intramolecular hydrogen bonding is present in option $1$.

**Subtopic:** Hydrogen Bonding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q056_d587afb3_13112026.png?v=d587afb38d63)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q056_65a713aa_13112026.png?v=65a713aa4fab)

---

## Q57

Chemistry · physical · Chemical Kinetics

Activation energy of any chemical reaction can be calculated if one knows the value of

- (1) rate constant at standard temperature
- (2) probability of collision
- (3) orientation of reactant molecules during collision
- **(4)** rate constant at two different temperatures

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. To calculate value of $E_a$
2. Equation used is
3. $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$
4. Hence $E_a$ can be calculated if value of rate constant $k$ is known at two different temperatures $T_1$ and $T_2$.

**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$, with two unknowns $A$ and $E_a$.
2. Taking the ratio at two temperatures eliminates $A$: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. So $E_a = \frac{2.303\,R\,T_1 T_2 \log(k_2/k_1)}{T_2 - T_1}$ needs $k$ at two different temperatures, which is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q057_f06eedd1_13112026.png?v=f06eedd1dc5d)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q057_0a79789e_13112026.png?v=0a79789e1cca)

---

## Q58

Chemistry · inorganic · Coordination Compounds – Practice

Match List I with List II.
List I (Complex)
List II (Type of isomerism)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ | I | Solvate isomerism |
| B | $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ | II | Linkage isomerism |
| C | $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ | III | Ionization isomerism |
| D | $\mathrm{[Co(H_2O)_6]Cl_3}$ | IV | Coordination isomerism |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-I, B-III, C-IV, D-II
- (3) A-I, B-IV, C-III, D-II
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A. $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ — II. Linkage isomerism due to ‘N’ and ‘O’ linkage by $\mathrm{NO_2}$
2. B. $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ — III. Ionization isomerism
3. C. $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ — IV. Coordination isomerism
4. D. $\mathrm{[Co(H_2O)_6]Cl_3}$ — I. Solvate isomerism

**Solved independently** (answer withheld)

1. A: $\mathrm{NO_2^-}$ is ambidentate (binds through N or O), so $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ shows linkage isomerism: A-II.
2. B: $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ and $\mathrm{[Co(NH_3)_5Br]SO_4}$ give different ions in solution, so ionization isomerism: B-III.
3. C: both cation and anion are complexes, so ligands can interchange, e.g. $\mathrm{[Cr(NH_3)_6][Co(CN)_6]}$: coordination isomerism, C-IV.
4. D: $\mathrm{H_2O}$ can be a ligand or lattice water, e.g. $\mathrm{[Co(H_2O)_5Cl]Cl_2\cdot H_2O}$: solvate (hydrate) isomerism, D-I.
5. A-II, B-III, C-IV, D-I is option $1$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 26)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q058_4f166d24_13112026.png?v=4f166d242f27)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q058_65a48864_13112026.png?v=65a48864ab39)

---

## Q59

Chemistry · physical · Basic Concepts of Chemistry

$1\,\mathrm{g}$ of sodium hydroxide was treated with $25\,\mathrm{mL}$ of $0.75\,\mathrm{M}$ $\mathrm{HCl}$ solution, the mass of sodium hydroxide left unreacted is equal to

- (1) $750\,\mathrm{mg}$
- **(2)** $250\,\mathrm{mg}$
- (3) Zero mg
- (4) $200\,\mathrm{mg}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{M} = \frac{\mathrm{W} \times 1000}{\mathrm{M_2} \times \mathrm{V}\,(\text{in mL})}$
2. $\mathrm{W} = \frac{\mathrm{M} \times \mathrm{M_2} \times \mathrm{V}\,(\text{in mL})}{1000} = \frac{0.75 \times 36.5 \times 25}{1000}$
3. $= 0.684\,\mathrm{g}$ (Mass of $\mathrm{HCl}$)
4. $\underset{36.5\,\mathrm{g}}{\mathrm{HCl}} + \underset{40\,\mathrm{g}}{\mathrm{NaOH}} \longrightarrow \mathrm{HCl} + \mathrm{NaOH}$
5. $36.5\,\mathrm{g}$ $\mathrm{HCl}$ reacts with $\mathrm{NaOH} = 40\,\mathrm{g}$
6. $0.684\,\mathrm{g}$ $\mathrm{HCl}$ reacts with $\mathrm{NaOH} = \frac{40}{36.5} \times 0.684 \simeq 0.750\,\mathrm{g}$
7. Amount of $\mathrm{NaOH}$ left $= 1\,\mathrm{g} - 0.750\,\mathrm{g} = 0.250\,\mathrm{g} = 250\,\mathrm{mg}$

**Solved independently** (answer withheld)

1. $n_{\mathrm{NaOH}} = \frac{1\,\mathrm{g}}{40\,\mathrm{g\,mol^{-1}}} = 0.025\,\mathrm{mol}$.
2. $n_{\mathrm{HCl}} = 0.025\,\mathrm{L} \times 0.75\,\mathrm{M} = 0.01875\,\mathrm{mol}$.
3. $\mathrm{NaOH} + \mathrm{HCl} \rightarrow \mathrm{NaCl} + \mathrm{H_2O}$ reacts $1:1$, so HCl is limiting.
4. Unreacted $n_{\mathrm{NaOH}} = 0.025 - 0.01875 = 0.00625\,\mathrm{mol}$.
5. Mass left $= 0.00625 \times 40 = 0.25\,\mathrm{g} = 250\,\mathrm{mg}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q059_cd711509_13112026.png?v=cd71150998f2)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q059_11e3a7dc_13112026.png?v=11e3a7dc5bff)

---

## Q60

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of electronegativity:
$\mathrm{N}$, $\mathrm{O}$, $\mathrm{F}$, $\mathrm{C}$, $\mathrm{Si}$
Choose the correct answer from the options given below:

- **(1)** $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$
- (2) $\mathrm{Si} < \mathrm{C} < \mathrm{O} < \mathrm{N} < \mathrm{F}$
- (3) $\mathrm{O} < \mathrm{F} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$
- (4) $\mathrm{F} < \mathrm{O} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Electronegativity increases across the period on moving left to right. It decreases on moving down the group.
2. The correct option is $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$

**Solved independently** (answer withheld)

1. Across period 2, electronegativity increases left to right: $\mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$.
2. Down group 14, electronegativity decreases, so $\mathrm{Si} < \mathrm{C}$.
3. Combined order: $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$, which is option $1$.

**Subtopic:** Trends in Chemical Properties – Electronegativity and Electron Affinity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q060_5815e09a_13112026.png?v=5815e09a4506)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q060_66d853d8_13112026.png?v=66d853d87239)

---

## Q61

Chemistry · physical · Thermodynamics

Match List I with List II.
List-I (Process)
List-II (Conditions)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Isothermal process | I | No heat exchange |
| B | Isochoric process | II | Carried out at constant temperature |
| C | Isobaric process | III | Carried out at constant volume |
| D | Adiabatic process | IV | Carried out at constant pressure |

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- (3) A-I, B-II, C-III, D-IV
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (A) Isothermal process $\Rightarrow$ Temperature is constant throughout the process
2. (B) Isochoric process $\Rightarrow$ Volume is constant throughout the process
3. (C) Isobaric process $\Rightarrow$ Pressure is constant throughout the process
4. (D) Adiabatic process $\Rightarrow$ No exchange of heat $(q)$ between system and surrounding

**Solved independently** (answer withheld)

1. Isothermal process is carried out at constant temperature: $A \to II$.
2. Isochoric process is carried out at constant volume: $B \to III$.
3. Isobaric process is carried out at constant pressure: $C \to IV$.
4. Adiabatic process involves no heat exchange ($\Delta Q = 0$): $D \to I$.
5. The matching $A\text{-}II, B\text{-}III, C\text{-}IV, D\text{-}I$ is option $4$.

**Subtopic:** Thermodynamic Processes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q061_c0fa4e3b_13112026.png?v=c0fa4e3bf365)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q061_b7dd74a5_13112026.png?v=b7dd74a56970)

---

## Q62

Chemistry · organic · Alcohols, Phenols and Ethers

Which one of the following alcohols reacts instantaneously with Lucas reagent?

- (1) $\mathrm{CH_3-CH_2-CH_2-CH_2OH}$
- (2) butan-2-ol `CCC(C)O` ![butan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q062_option_2_s1_246d1e4e_13112026.svg?v=246d1e4e3f48) — $\mathrm{CH_3-CH_2-CH(CH_3)-OH}$
- (3) 2-methylpropan-1-ol `CC(C)CO` ![2-methylpropan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q062_option_3_s1_44b6a2e7_13112026.svg?v=44b6a2e7f8a5) — $\mathrm{CH_3-CH(CH_3)-CH_2OH}$
- **(4)** 2-methylpropan-2-ol `CC(C)(C)O` ![2-methylpropan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q062_option_4_s1_51170735_13112026.svg?v=51170735efa7) — $\mathrm{CH_3-C(CH_3)_2-OH}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Tertiary alcohols react instantaneously with Lucas reagent and gives immediate turbidity.
2. In case of tertiary alcohols, they form halides easily with Lucas reagent (conc. $\mathrm{HCl}$ and $\mathrm{ZnCl_2}$)

**Solved independently** (answer withheld)

1. Lucas reagent (conc. $\mathrm{HCl} + \mathrm{ZnCl_2}$) reacts via an $S_N1$ carbocation, so the rate order is $3^\circ > 2^\circ > 1^\circ$; only $3^\circ$ alcohols give turbidity immediately.
2. Classify: option $3$ $\mathrm{(CH_3)_2CHCH_2OH}$ is $1^\circ$, option $4$ $\mathrm{(CH_3)_3COH}$ is $3^\circ$, option $1$ $\mathrm{CH_3(CH_2)_3OH}$ is $1^\circ$, option $2$ $\mathrm{CH_3CH_2CH(OH)CH_3}$ is $2^\circ$.
3. The only tertiary alcohol, $\mathrm{(CH_3)_3COH}$, reacts instantaneously, which is option $4$.

**Subtopic:** Test of Alcohol · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 28)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q062_a440c60e_13112026.png?v=a440c60ef716)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q062_6080d114_13112026.png?v=6080d1144a32)

---

## Q63

Chemistry · physical · Structure of Atom

The energy of an electron in the ground state $(n = 1)$ for $\mathrm{He^{+}}$ ion is $-x\,\mathrm{J}$, then that for an electron in $n = 2$ state for $\mathrm{Be^{3+}}$ ion in J is

- **(1)** $-x$
- (2) $-\frac{x}{9}$
- (3) $-4x$
- (4) $-\frac{4}{9}x$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $E_n = -R_H\left(\frac{Z^2}{n^2}\right)\,\mathrm{J}$
2. For $\mathrm{He^{+}}$ $(n = 1)$,
3. $E_n = -x = -R_H\left(\frac{2^2}{1^2}\right) = -4R_H$
4. $\therefore\quad R_H = \frac{x}{4}$
5. For $\mathrm{Be^{3+}}$ $(n = 2)$,
6. $E_n = -R_H\left(\frac{Z^2}{n^2}\right)\,\mathrm{J}$
7. $= -\frac{x}{4}\times\left(\frac{4\times 4}{2\times 2}\right) = -x\,\mathrm{J}$

**Solved independently** (answer withheld)

1. For hydrogen-like species $E_n = -k\frac{Z^2}{n^2}$.
2. For $\mathrm{He^{+}}$, $n=1$: $E = -k\frac{2^2}{1^2} = -4k = -x$, so $k = \frac{x}{4}$.
3. For $\mathrm{Be^{3+}}$, $n=2$: $E = -k\frac{4^2}{2^2} = -4k$.
4. $-4k = -4 \times \frac{x}{4} = -x$, which is option $1$.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q063_75b30fbd_13112026.png?v=75b30fbd5327)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q063_3cfef9bd_13112026.png?v=3cfef9bdbe44)

---

## Q64

Chemistry · organic · Haloalkanes and Haloarenes

The compound that will undergo $\mathrm{S_N1}$ reaction with the fastest rate is

- (1) (bromomethyl)cyclohexane `BrCC1CCCCC1` ![(bromomethyl)cyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_1_s1_3db34c76_13112026.svg?v=3db34c76f38e)
- (2) bromocyclohexane `BrC1CCCCC1` ![bromocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_2_s1_35c4a4b9_13112026.svg?v=35c4a4b9cb53)
- (3) bromobenzene `Brc1ccccc1` ![bromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_3_s1_61d2ed9e_13112026.svg?v=61d2ed9ebe04)
- **(4)** (1-bromoethyl)benzene `CC(Br)c1ccccc1` ![(1-bromoethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q064_option_4_s1_ef3a803b_13112026.svg?v=ef3a803b5361)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Reactivity towards $\mathrm{S_N1}$ depends upon stability of carbocation.
2. Order of stability is
3. Hence
4. is most reactive

**Solved independently** (answer withheld)

1. $\mathrm{S_N1}$ rate depends on the stability of the carbocation formed in the slow ionisation step.
2. Option $1$, $\mathrm{C_6H_{11}CH_2Br}$, gives a primary carbocation $\mathrm{C_6H_{11}CH_2^+}$, which is very unstable.
3. Option $2$, $\mathrm{C_6H_{11}Br}$, gives a secondary cyclohexyl carbocation, stabilised only by hyperconjugation and $+I$ effect.
4. Option $3$, $\mathrm{C_6H_5Br}$, would give a phenyl cation; the $sp^2$ C$-$Br bond has partial double-bond character, so aryl halides do not undergo $\mathrm{S_N1}$.
5. Option $4$, $\mathrm{C_6H_5CH(Br)CH_3}$, gives the secondary benzylic carbocation $\mathrm{C_6H_5\overset{+}{C}HCH_3}$, delocalised into the ring by resonance.
6. The benzylic cation is the most stable, so option $4$ reacts fastest by $\mathrm{S_N1}$.

**Subtopic:** Reactions of Haloalkanes – Nucleophilic Substitution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q064_96b1b97b_13112026.png?v=96b1b97b2ed3)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q064_2b45b9c1_13112026.png?v=2b45b9c1df53)

---

## Q65

Chemistry · physical · Solutions

The Henry’s law constant ($K_H$) values of three gases (A, B, C) in water are $145$, $2 \times 10^{-5}$ and $35\,\mathrm{kbar}$, respectively. The solubility of these gases in water follow the order:

- (1) B > A > C
- **(2)** B > C > A
- (3) A > C > B
- (4) A > B > C

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Value of Henry’s law constant $\propto \frac{1}{\text{Solubility of gas}}$
2. Higher the value of $K_H$ at a given pressure, lower is the solubility of the gas in the liquid.
3. $K_H$ value of gases (given) : $A > C > B$
4. $\therefore$ Order of solubility of gases in water : $B > C > A$

**Solved independently** (answer withheld)

1. Henry's law: $p = K_\mathrm{H}\,x$, so at a given pressure $x = \frac{p}{K_\mathrm{H}}$ and solubility $\propto \frac{1}{K_\mathrm{H}}$.
2. Order of constants: $K_\mathrm{H}(B) = 2\times10^{-5} < K_\mathrm{H}(C) = 35 < K_\mathrm{H}(A) = 145\,\mathrm{kbar}$.
3. Hence solubility order is $B > C > A$, which is option $2$.

**Subtopic:** Solubility of a Gas in a Liquid · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q065_076e4b56_13112026.png?v=076e4b566b3e)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q065_f4d472c1_13112026.png?v=f4d472c1943e)

---

## Q66

Chemistry · physical · Chemical Kinetics

Which plot of $\ln k$ vs $\frac{1}{T}$ is consistent with Arrhenius equation?

- (1) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): straight line with positive slope, crossing the axes just below the origin](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q066_option_1_a03f378b_13112026.png?v=a03f378bb57d) *graph of ln k (y-axis) vs 1/T (x-axis): straight line with positive slope, crossing the axes just below the origin*
- (2) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): straight line with positive slope and a positive intercept on the ln k axis](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q066_option_2_23dedabf_13112026.png?v=23dedabf521c) *graph of ln k (y-axis) vs 1/T (x-axis): straight line with positive slope and a positive intercept on the ln k axis*
- (3) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): straight line with positive slope passing through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q066_option_3_55924621_13112026.png?v=559246219a46) *graph of ln k (y-axis) vs 1/T (x-axis): straight line with positive slope passing through the origin*
- **(4)** ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): straight line with negative slope, starting at a positive intercept on the ln k axis and meeting the 1/T axis](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q066_option_4_af654b3e_13112026.png?v=af654b3ed651) *graph of ln k (y-axis) vs 1/T (x-axis): straight line with negative slope, starting at a positive intercept on the ln k axis and meeting the 1/T axis*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The Arrhenius equation is given as
2. $k = Ae^{-\frac{E_a}{RT}}$
3. $\therefore\ \ln k = \ln A - \frac{E_a}{RT}$
4. $\ln k$ v/s $\frac{1}{T}$ gives a straight line graph with slope $= -\frac{E_a}{R}$ and intercept $= \ln A$

**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$.
2. Taking logs: $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$.
3. This is linear in $\frac{1}{T}$ with slope $-\frac{E_a}{R} < 0$ and intercept $\ln A$ on the $\ln k$ axis.
4. Options 1, 2 and 3 show positive slopes; only option $4$ shows a falling straight line with a positive intercept, so the answer is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q066_5c833951_13112026.png?v=5c833951381e)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q066_39153234_13112026.png?v=391532340935)

---

## Q67

Chemistry · physical · Chemical Equilibrium

In which of the following equilibria, $K_p$ and $K_c$ are NOT equal?

- **(1)** $\mathrm{PCl_{5(g)} \rightleftharpoons PCl_{3(g)} + Cl_{2(g)}}$
- (2) $\mathrm{H_{2(g)} + I_{2(g)} \rightleftharpoons 2HI_{(g)}}$
- (3) $\mathrm{CO_{(g)} + H_2O_{(g)} \rightleftharpoons CO_{2(g)} + H_{2(g)}}$
- (4) $\mathrm{2BrCl_{(g)} \rightleftharpoons Br_{2(g)} + Cl_{2(g)}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $K_p = K_c (RT)^{\Delta n_g}$
2. for $K_p \neq K_c$,
3. $\Delta n_g \neq 0$
4. $\Delta n_g = n_p - n_r$
5. (1) $\Delta n_g = 2 - 1 = 1$
6. (2) $\Delta n_g = 2 - 2 = 0$
7. (3) $\Delta n_g = 2 - 2 = 0$
8. (4) $\Delta n_g = 2 - 2 = 0$

**Solved independently** (answer withheld)

1. $K_p = K_c (RT)^{\Delta n_g}$, so $K_p \neq K_c$ only when $\Delta n_g \neq 0$.
2. Option 4: $\Delta n_g = (1+1) - 2 = 0$.
3. Option 1: $\Delta n_g = (1+1) - 1 = 1$.
4. Option 2: $\Delta n_g = 2 - (1+1) = 0$.
5. Option 3: $\Delta n_g = (1+1) - (1+1) = 0$.
6. Only option $1$ has $\Delta n_g \neq 0$, so $K_p = K_c RT \neq K_c$.

**Subtopic:** Homogeneous and Heterogeneous Equilibria · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 30)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q067_b56a0dc2_13112026.png?v=b56a0dc250d7)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q067_b44c788d_13112026.png?v=b44c788d253a)

---

## Q68

Chemistry · organic · Hydrocarbons

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The boiling point of three isomeric pentanes follows the order n-pentane $>$ isopentane $>$ neopentane
- (Statement II) When branching increases, the molecule attains a shape of sphere. This results in smaller surface area for contact, due to which the intermolecular forces between the spherical molecules are weak, thereby lowering the boiling point.

- **(1)** Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- (3) Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Both statement I and statement II are correct.
2. Boiling point of n-pentane $= 309\,\mathrm{K}$
3. isopentane $= 301\,\mathrm{K}$
4. neopentane $= 282.5$
5. As branching increases molecules attain the shape of a sphere results in smaller area of contact thus weak intermolecular forces between spherical molecules, which are overcome at relatively lower temperature.
6. Leading to decrease in boiling point.

**Solved independently** (answer withheld)

1. Statement I: b.p. of n-pentane ($309\,K$) $>$ isopentane ($301\,K$) $>$ neopentane ($282.5\,K$), so Statement I is correct.
2. Statement II: more branching makes the molecule nearly spherical, reducing contact surface area and weakening van der Waals forces, which lowers the boiling point; Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Physical Properties of Alkanes, Alkenes and Alkynes · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 31)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q068_42018e51_13112026.png?v=42018e514dcc)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q068_969a63ea_13112026.png?v=969a63ea13e2)

---

## Q69

Chemistry · organic · Biomolecules

The reagents with which glucose does not react to give the corresponding tests/products are
Choose the correct options from the given below:

- (A) Tollen’s reagent
- (B) Schiff’s reagent
- (C) $\mathrm{HCN}$
- (D) $\mathrm{NH_2OH}$
- (E) $\mathrm{NaHSO_3}$

- (1) B and C
- (2) A and D
- **(3)** B and E
- (4) E and D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Despite having the aldehyde group glucose does not give Schiff’s test and it does not form the hydrogen sulphite addition product with $\mathrm{NaHSO_3}$.

**Solved independently** (answer withheld)

1. Glucose reduces Tollens' reagent (silver mirror), so $\text{A}$ reacts.
2. Glucose adds $\mathrm{HCN}$ to give a cyanohydrin, so $\text{C}$ reacts.
3. Glucose condenses with $\mathrm{NH_2OH}$ to give an oxime, so $\text{D}$ reacts.
4. Despite having a $\mathrm{-CHO}$ group, glucose does not give Schiff's test and does not form the $\mathrm{NaHSO_3}$ addition product (evidence for its cyclic structure), so $\text{B}$ and $\text{E}$ do not react.
5. Non-reacting reagents are $\text{B}$ and $\text{E}$, which is option $3$.

**Subtopic:** Structure and Reactions of Glucose · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q069_88dc1cb6_13112026.png?v=88dc1cb64e78)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q069_42419128_13112026.png?v=424191282cd1)

---

## Q70

Chemistry · physical · Thermodynamics

In which of the following processes entropy increases?
Choose the correct answer from the options given below:

- (A) A liquid evaporates to vapour.
- (B) Temperature of a crystalline solid lowered from $130\,\mathrm{K}$ to $0\,\mathrm{K}$.
- (C) $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$
- (D) $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$

- (1) A and C
- (2) A, B and D
- **(3)** A, C and D
- (4) C and D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. When a liquid evaporates to vapour entropy increases.
2. $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$
3. Number of gaseous product molecules increases so entropy increases.
4. $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$
5. $1$ mole $\mathrm{Cl_{2(g)}}$ form $2$ mol $\mathrm{Cl_{(g)}}$. So entropy increases.

**Solved independently** (answer withheld)

1. A: evaporation changes liquid to vapour, so disorder increases and $\Delta S > 0$.
2. B: cooling a crystalline solid from $130\,\mathrm{K}$ to $0\,\mathrm{K}$ reduces molecular motion, so $\Delta S < 0$.
3. C: $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$ gives $\Delta n_g = +2$, so $\Delta S > 0$.
4. D: $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$ gives $\Delta n_g = +1$, so $\Delta S > 0$.
5. Entropy increases in A, C and D, which is option $3$.

**Subtopic:** Entropy, Second Law & Third Law · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 32)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q070_3c8fd1ff_13112026.png?v=3c8fd1ffd07d)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q070_278fd8c4_13112026.png?v=278fd8c42000)

---

## Q71

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List I with List II.
List I (Reaction)
List II (Reagents/Condition)
Choose the correct answer from the options given below:

![printed figure: List I: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → benzophenone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate. List II: I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q071_7f86aa41_13112026.svg?v=7f86aa4158c5)

*List I: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → benzophenone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate. List II: I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$*

![drawn: List I: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → benzophenone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate. List II: I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_e0632f42_13112026.svg?v=e0632f42048e)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: cyclohexylidenecyclohexane `C1CCC(=C2CCCCC2)CC1` ![cyclohexylidenecyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s1_957a6cb4_13112026.svg?v=957a6cb425a6); cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s2_ecae2398_13112026.svg?v=ecae2398c700); benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s3_dbf27a87_13112026.svg?v=dbf27a872e50); benzophenone `O=C(c1ccccc1)c1ccccc1` ![benzophenone](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s4_4a6ed161_13112026.svg?v=4a6ed161623c); cyclohexanol `OC1CCCCC1` ![cyclohexanol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s5_b130dcca_13112026.svg?v=b130dccaeb49); cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s6_ecae2398_13112026.svg?v=ecae2398c700); ethylbenzene `CCc1ccccc1` ![ethylbenzene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s7_c3cd0ee9_13112026.svg?v=c3cd0ee97328); potassium benzoate `O=C([O-])c1ccccc1.[K+]` ![potassium benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s8_d32e872f_13112026.svg?v=d32e872ffccb); benzoyl chloride `O=C(Cl)c1ccccc1` ![benzoyl chloride](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q071_question_s9_56febcfe_13112026.svg?v=56febcfef378)

| List-I | | List-II | |
|---|---|---|---|
| A | [reaction drawn as structures; see figure] | I | [structure drawn; see figure] Cl/Anhyd. $\mathrm{AlCl_3}$ |
| B | [reaction drawn as structures; see figure] | II | $\mathrm{CrO_3}$ |
| C | [reaction drawn as structures; see figure] | III | $\mathrm{KMnO_4/KOH}$, $\Delta$ |
| D | [reaction drawn as structures; see figure] | IV | (i) $\mathrm{O_3}$ (ii) $\mathrm{Zn\text{-}H_2O}$ |

- (1) A-IV, B-I, C-III, D-II
- (2) A-III, B-I, C-II, D-IV
- **(3)** A-IV, B-I, C-II, D-III
- (4) A-I, B-IV, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A)
2. It is reductive ozonolysis
3. (B)
4. It is Friedel-Crafts acylation reaction.
5. (C)
6. Secondary alcohols are oxidised to ketones by $\mathrm{CrO_3}$
7. (D)

**Solved independently** (answer withheld)

1. A: ozonolysis $\mathrm{(i)\,O_3\ (ii)\,Zn\text{-}H_2O}$ cleaves the $\mathrm{C=C}$ of cyclohexylidenecyclohexane into two cyclohexanone molecules, so A-IV.
2. B: Friedel-Crafts acylation of benzene with $\mathrm{C_6H_5COCl}$/anhyd. $\mathrm{AlCl_3}$ gives benzophenone $\mathrm{C_6H_5COC_6H_5}$, so B-I.
3. C: $\mathrm{CrO_3}$ oxidises the secondary alcohol cyclohexanol to cyclohexanone, so C-II.
4. D: hot alkaline $\mathrm{KMnO_4}$ oxidises the whole ethyl side chain to $\mathrm{-COOK}$, giving potassium benzoate, so D-III.
5. A-IV, B-I, C-II, D-III matches option $3$.

**Subtopic:** Preparation of Ketones, Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q071_6c4f29c0_13112026.png?v=6c4f29c0d9dd)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q071_9b87d11c_13112026.png?v=9b87d11c6f26)

---

## Q72

Chemistry · inorganic · The p–Block Elements

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) The boiling point of hydrides of Group 16 elements follow the order $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
- (Statement II) On the basis of molecular mass, $\mathrm{H_2O}$ is expected to have lower boiling point than the other members of the group but due to the presence of extensive H-bonding in $\mathrm{H_2O}$, it has higher boiling point.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Statement I is correct, because boiling point of hydrides of group $16$ follows the order
2. $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
3. Statement II due to intermolecular H-bonding $\mathrm{H_2O}$ shows higher boiling point than respective hydrides of group $16$.
4. (Both Statement are true)
5. Order from $\mathrm{H_2Te}$ to $\mathrm{H_2S}$ is due to decreasing molar mass.

**Solved independently** (answer withheld)

1. Among $\mathrm{H_2S, H_2Se, H_2Te}$ boiling point rises with molar mass (van der Waals forces): $\mathrm{H_2Te > H_2Se > H_2S}$.
2. $\mathrm{H_2O}$ has the lowest molar mass but extensive intermolecular H-bonding, so its boiling point is the highest: $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$, so Statement I is true.
3. Statement II correctly gives the reason (lower expected b.p. by mass, higher actual b.p. due to H-bonding), so it is true; both true is option $1$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q072_e870f259_13112026.png?v=e870f259cdf7)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q072_3a895638_13112026.png?v=3a89563887a8)

---

## Q73

Chemistry · physical · Chemical Equilibrium

For the reaction $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$. At a given time, the composition of reaction mixture is: $[\mathrm{A}] = [\mathrm{B}] = [\mathrm{C}] = 2 \times 10^{-3}\,\mathrm{M}$. Then, which of the following is correct?

- (1) Reaction is at equilibrium.
- (2) Reaction has a tendency to go in forward direction.
- **(3)** Reaction has a tendency to go in backward direction.
- (4) Reaction has gone to completion in forward direction.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$
2. At a given time t, $Q_C$ is to be calculated and been compared with $K_C$.
3. $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^2} = \frac{(2 \times 10^{-3})(2 \times 10^{-3})}{(2 \times 10^{-3})^2}$
4. $Q_C = 1$
5. As $Q_C > K_C$, so reaction has a tendency to move backward.

**Solved independently** (answer withheld)

1. $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^2}$.
2. $Q_C = \frac{(2\times10^{-3})(2\times10^{-3})}{(2\times10^{-3})^2} = 1$.
3. $Q_C = 1 > K_C = 4\times10^{-3}$, so the reaction has a tendency to go in the backward direction, which is option $3$.

**Subtopic:** Predicting the Extent and Direction of a Reaction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q073_54cb4d33_13112026.png?v=54cb4d33a374)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q073_e46ff8fd_13112026.png?v=e46ff8fd8443)

---

## Q74

Chemistry · physical · Structure of Atom

Match List I with List II
List I (Quantum Number) | List II (Information provided)
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | $m_l$ | I | Shape of orbital |
| B | $m_s$ | II | Size of orbital |
| C | $l$ | III | Orientation of orbital |
| D | $n$ | IV | Orientation of spin of electron |

- (1) A-I, B-III, C-II, D-IV
- **(2)** A-III, B-IV, C-I, D-II
- (3) A-III, B-IV, C-II, D-I
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Magnetic quantum number $m_l$ informs about orientation of orbital.
2. Spin quantum number $m_s$ informs about orientation of spin of electron.
3. Azimuthal quantum number $(l)$ informs about shape of orbital
4. Principal quantum number $(n)$ informs about size of orbital

**Solved independently** (answer withheld)

1. $m_l$ (magnetic quantum number) gives the orientation of the orbital: A-III; $m_s$ gives the orientation of electron spin: B-IV; $l$ (azimuthal) gives the shape of the orbital: C-I; $n$ (principal) gives the size of the orbital: D-II; so A-III, B-IV, C-I, D-II is option $2$.

**Subtopic:** Quantum Numbers · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q074_779a5aec_13112026.png?v=779a5aec0ffe)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q074_d8b87974_13112026.png?v=d8b879741ac5)

---

## Q75

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

A compound with a molecular formula of $\mathrm{C_6H_{14}}$ has two tertiary carbons. Its IUPAC name is :

- (1) n-hexane
- (2) 2-methylpentane
- **(3)** 2,3-dimethylbutane
- (4) 2,2-dimethylbutane

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{CH_3-CH_2-CH_2-CH_2-CH_2-CH_3}$ has no tertiary carbon (n-Hexane)
2. has only one tertiary carbon (2-Methylpentane)
3. has two tertiary carbon. (2, 3-Dimethylbutane)
4. has no tertiary carbon (2, 2-Dimethylbutane)

**Solved independently** (answer withheld)

1. A tertiary carbon is bonded to exactly three other carbons.
2. $\mathrm{CH_3-CH(CH_3)-CH(CH_3)-CH_3}$ (2,3-dimethylbutane, $\mathrm{C_6H_{14}}$): $C_2$ and $C_3$ are each bonded to three carbons, so it has $2$ tertiary carbons.
3. 2-methylpentane has $1$ tertiary carbon ($C_2$); 2,2-dimethylbutane has $0$ (its $C_2$ is quaternary); n-hexane has $0$.
4. Only 2,3-dimethylbutane has two tertiary carbons, which is option $3$.

**Subtopic:** Acyclic or Open Chain Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q075_1eb686d6_13112026.png?v=1eb686d644c6)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q075_19a583ed_13112026.png?v=19a583ed4502)

---

## Q76

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

On heating, some solid substances change from solid to vapour state without passing through liquid state. The technique used for the purification of such solid substances based on the above principle is known as

- (1) Crystallization
- **(2)** Sublimation
- (3) Distillation
- (4) Chromatography

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (1) Crystallization : It is based on difference in the solubilities of the compound and impurities in a suitable solvent.
2. (2) Sublimation : It is the purification technique based on principle that on heating, some solid substances change from solid to vapour state without passing through liquid state.
3. (3) Distillation : It is used to separate volatile liquids from non-volatile impurities and the liquids having sufficient difference in their boiling point.
4. (4) Chromatography : It is based on separation by using stationary and mobile phase.

**Solved independently** (answer withheld)

1. A solid passing directly to vapour on heating, skipping the liquid state, is sublimation, so the purification technique is sublimation, option $2$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q076_08ebde81_13112026.png?v=08ebde81fc64)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q076_6c0aaaeb_13112026.png?v=6c0aaaeb1b55)

---

## Q77

Chemistry · organic · General Organic Chemistry

The most stable carbocation among the following is :

- (1) 2-methylpentan-3-ylium `CC[CH+]C(C)C` ![2-methylpentan-3-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_1_s1_8a3210fb_13112026.svg?v=8a3210fb1a2a)
- (2) 4-methylpentan-2-ylium `C[CH+]CC(C)C` ![4-methylpentan-2-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_2_s1_34ac5544_13112026.svg?v=34ac5544f031)
- (3) cyclopentylmethylium `[CH2+]C1CCCC1` ![cyclopentylmethylium](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_3_s1_8adbcb30_13112026.svg?v=8adbcb30ef6b)
- **(4)** 1-methylcyclohexylium `C[C+]1CCCCC1` ![1-methylcyclohexylium](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q077_option_4_s1_6a144549_13112026.svg?v=6a1445496db4)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The stability of carbocation can be described by the hyperconjugation.
2. Greater the extent of hyperconjugation, more is the stability of carbocation.
3. (1) $\rightarrow 3\,\alpha\text{-H}$
4. (2) $\rightarrow 5\,\alpha\text{-H}$
5. (3) $\rightarrow 1\,\alpha\text{-H}$
6. (4) $\rightarrow 7\,\alpha\text{-H}$
7. Stability order of carbocations $= (4) > (2) > (1) > (3)$

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{CH_3CH_2\overset{+}{C}HCH(CH_3)_2}$ has the positive carbon bonded to two carbons, so it is a $2^\circ$ carbocation.
2. Option 2: $\mathrm{CH_3\overset{+}{C}HCH_2CH(CH_3)_2}$ has the positive carbon bonded to two carbons, so it is a $2^\circ$ carbocation.
3. Option 3: $\mathrm{C_5H_9\overset{+}{C}H_2}$ (cyclopentylmethyl) has the positive carbon bonded to one carbon, so it is a $1^\circ$ carbocation.
4. Option 4: the ring carbon bearing $\mathrm{CH_3}$ and the $+$ charge is bonded to three carbons, so it is a $3^\circ$ carbocation.
5. Carbocation stability by hyperconjugation and $+I$ effect: $3^\circ > 2^\circ > 1^\circ$, so the most stable is option $4$.

**Subtopic:** Hyperconjugation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q077_ac63b578_13112026.png?v=ac63b5788b5f)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q077_0caf18a4_13112026.png?v=0caf18a4caf6)

---

## Q78

Chemistry · organic · Amines

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Aniline does not undergo Friedel-Crafts alkylation reaction.
- (Statement II) Aniline cannot be prepared through Gabriel synthesis.

- **(1)** Both statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is correct but Statement II is false
- (4) Statement I is incorrect but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Aniline does not undergo Friedel-Crafts alkylation reaction due to salt formation with aluminium chloride, the Lewis acid, which is used as a catalyst.
2. Aniline (aromatic primary amine) cannot be prepared by Gabriel phthalimide synthesis because aryl halides do not undergo nucleophilic substitution with anion formed by phthalimide.

**Solved independently** (answer withheld)

1. Statement I: aniline (a Lewis base) reacts with the Lewis acid catalyst $\mathrm{AlCl_3}$ to form a salt, so the ring is deactivated and Friedel-Crafts alkylation does not occur; Statement I is true.
2. Statement II: Gabriel synthesis needs $S_N2$ attack of potassium phthalimide on an alkyl halide; aryl halides do not undergo this substitution, so aniline (a primary aromatic amine) cannot be made this way; Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions), Methods of Preparation of Amines · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q078_ee731f47_13112026.png?v=ee731f47224f)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q078_90a14ed0_13112026.png?v=90a14ed0e8e1)

---

## Q79

Chemistry · physical · Redox Reactions

Which reaction is NOT a redox reaction?

- (1) $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$
- (2) $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$
- (3) $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$
- **(4)** $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (1) $\mathrm{Zn^{0} + \overset{+2}{Cu}SO_4 \longrightarrow \overset{+2}{Zn}SO_4 + Cu^{0}}$, Redox reaction
2. (2) $\mathrm{K\overset{+5}{Cl}O_3 + I_2^{0} \longrightarrow 2K\overset{+5}{I}O_3 + Cl_2^{0}}$, Redox reaction
3. (3) $\mathrm{H_2^{0} + Cl_2^{0} \longrightarrow 2\overset{+1}{H}Cl^{-1}}$, Redox reaction
4. (4) $\mathrm{\overset{+2}{Ba}Cl_2^{-1} + \overset{+1}{Na_2}SO_4^{-2} \longrightarrow \overset{+2}{Ba}SO_4 + 2\overset{+1}{Na}Cl^{-1}}$
5. This is not a redox reaction as there is no change in oxidation state.

**Solved independently** (answer withheld)

1. In $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$ the oxidation states stay $\mathrm{Ba}=+2$, $\mathrm{Cl}=-1$, $\mathrm{Na}=+1$, $\mathrm{S}=+6$, $\mathrm{O}=-2$ on both sides, so it is not redox.
2. In $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$, $\mathrm{Zn}: 0 \rightarrow +2$ and $\mathrm{Cu}: +2 \rightarrow 0$, so it is redox.
3. In $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$, $\mathrm{I}: 0 \rightarrow +5$ and $\mathrm{Cl}: +5 \rightarrow 0$, so it is redox.
4. In $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$, $\mathrm{H}: 0 \rightarrow +1$ and $\mathrm{Cl}: 0 \rightarrow -1$, so it is redox.
5. Only option $4$ is not a redox reaction.

**Subtopic:** Oxidation Number · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q079_85303a7d_13112026.png?v=85303a7d25a1)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q079_e3e2bd3a_13112026.png?v=e3e2bd3a938d)

---

## Q80

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.
List I (Compound) | List II (Shape/geometry)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{NH_3}$ | I | Trigonal Pyramidal |
| B | $\mathrm{BrF_5}$ | II | Square Planar |
| C | $\mathrm{XeF_4}$ | III | Octahedral |
| D | $\mathrm{SF_6}$ | IV | Square Pyramidal |

- **(1)** A-I, B-IV, C-II, D-III
- (2) A-II, B-IV, C-III, D-I
- (3) A-III, B-IV, C-I, D-II
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{NH_3} \Rightarrow$ $sp^{3}$ hybridised with $1$ lone pair.
2. Structure will be Trigonal Pyramidal.
3. $\mathrm{BrF_5} \Rightarrow$ $sp^{3}d^{2}$ hybridised with $1$ lone pair.
4. Structure will be Square Pyramidal.
5. $\mathrm{XeF_4} \Rightarrow$ $sp^{3}d^{2}$ with two lone pairs.
6. Structure will be Square Planar.
7. $\mathrm{SF_6} \Rightarrow$ $sp^{3}d^{2}$ with no lone pair.
8. Structure will be Octahedral.
9. A-I, B-IV, C-II, D-III

**Solved independently** (answer withheld)

1. $\mathrm{NH_3}$: 3 bond pairs + 1 lone pair on N, so trigonal pyramidal: A-I.
2. $\mathrm{BrF_5}$: 5 bond pairs + 1 lone pair on Br, so square pyramidal: B-IV.
3. $\mathrm{XeF_4}$: 4 bond pairs + 2 lone pairs on Xe, so square planar: C-II.
4. $\mathrm{SF_6}$: 6 bond pairs, no lone pair on S, so octahedral: D-III.
5. A-I, B-IV, C-II, D-III is option $1$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q080_8fff7e31_13112026.png?v=8fff7e319671)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q080_db6e8408_13112026.png?v=db6e840821d0)

---

## Q81

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of first ionization enthalpy:
$\mathrm{Li}$, $\mathrm{Be}$, $\mathrm{B}$, $\mathrm{C}$, $\mathrm{N}$
Choose the correct answer from the options given below:

- (1) $\mathrm{Li} < \mathrm{Be} < \mathrm{B} < \mathrm{C} < \mathrm{N}$
- **(2)** $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$
- (3) $\mathrm{Li} < \mathrm{Be} < \mathrm{C} < \mathrm{B} < \mathrm{N}$
- (4) $\mathrm{Li} < \mathrm{Be} < \mathrm{N} < \mathrm{B} < \mathrm{C}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Increasing order of first ionization enthalpy is $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$

**Solved independently** (answer withheld)

1. Across period 2, first ionization enthalpy generally increases with increasing nuclear charge, so $\mathrm{Li}$ is lowest and $\mathrm{N}$ is highest among these.
2. $\mathrm{Be}$ ($1s^2 2s^2$) has a fully filled, more penetrating $2s$ orbital, while $\mathrm{B}$ ($1s^2 2s^2 2p^1$) loses a $2p$ electron that is shielded by $2s$, so $\Delta_i H_1(\mathrm{B}) < \Delta_i H_1(\mathrm{Be})$.
3. $\mathrm{C} < \mathrm{N}$ since $\mathrm{N}$ has a stable half-filled $2p^3$ configuration and higher nuclear charge.
4. Order: $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$, which is option $2$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 37)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q081_a0c382d9_13112026.png?v=a0c382d9294a)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q081_a13cc273_13112026.png?v=a13cc2734805)

---

## Q82

Chemistry · inorganic · The D- and F-Block Elements – Practice

‘Spin only’ magnetic moment is same for which of the following ions? Choose the most appropriate answer from the options given below.

- (A) $\mathrm{Ti^{3+}}$
- (B) $\mathrm{Cr^{2+}}$
- (C) $\mathrm{Mn^{2+}}$
- (D) $\mathrm{Fe^{2+}}$
- (E) $\mathrm{Sc^{3+}}$

- **(1)** B and D only
- (2) A and E only
- (3) B and C only
- (4) A and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ions | No. of unpaired electrons | Configuration
2. $\mathrm{Ti^{3+}}$ | $1$ | $3d^{1}$
3. $\mathrm{Cr^{2+}}$ | $4$ | $3d^{4}$
4. $\mathrm{Mn^{2+}}$ | $5$ | $3d^{5}$
5. $\mathrm{Fe^{2+}}$ | $4$ | $3d^{6}$
6. $\mathrm{Sc^{3+}}$ | $0$ | $3d^{0}$
7. Spin only magnetic moment is given by $\sqrt{n(n+2)}\,\mathrm{BM}$
8. $\therefore$ $\mathrm{Cr^{2+}}$ and $\mathrm{Fe^{2+}}$ will have same spin only magnetic moment.

**Solved independently** (answer withheld)

1. Spin-only moment $\mu = \sqrt{n(n+2)}\,\text{BM}$ depends only on the number of unpaired electrons $n$.
2. $\mathrm{Ti^{3+}}$: $3d^1$, $n=1$.
3. $\mathrm{Cr^{2+}}$: $3d^4$, $n=4$.
4. $\mathrm{Mn^{2+}}$: $3d^5$, $n=5$.
5. $\mathrm{Fe^{2+}}$: $3d^6$, $n=4$.
6. $\mathrm{Sc^{3+}}$: $3d^0$, $n=0$.
7. Only $\mathrm{Cr^{2+}}$ and $\mathrm{Fe^{2+}}$ share $n=4$, giving $\mu = \sqrt{24} \approx 4.90\,\text{BM}$ each, i.e. B and D, which is option $1$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q082_a42b6575_13112026.png?v=a42b6575b7e3)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q082_5beb9df8_13112026.png?v=5beb9df81018)

---

## Q83

Chemistry · inorganic · The D- and F-Block Elements – Practice

The $E^\circ$ value for the $\mathrm{Mn^{3+}/Mn^{2+}}$ couple is more positive than that of $\mathrm{Cr^{3+}/Cr^{2+}}$ or $\mathrm{Fe^{3+}/Fe^{2+}}$ due to change of

- (1) $d^{5}$ to $d^{4}$ configuration
- (2) $d^{5}$ to $d^{2}$ configuration
- **(3)** $d^{4}$ to $d^{5}$ configuration
- (4) $d^{3}$ to $d^{5}$ configuration

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $E^\circ_{\mathrm{Mn^{3+}/Mn^{2+}}} > E^\circ_{\mathrm{Cr^{3+}/Cr^{2+}}}$ or $E^\circ_{\mathrm{Fe^{3+}/Fe^{2+}}}$
2. Electronic configuration of $\mathrm{Mn^{3+}} = [\mathrm{Ar}]3d^{4}$
3. Electronic configuration of $\mathrm{Mn^{2+}} = [\mathrm{Ar}]3d^{5}$
4. Electronic configuration of $\mathrm{Cr^{3+}} = [\mathrm{Ar}]3d^{3}$
5. Electronic configuration of $\mathrm{Cr^{2+}} = [\mathrm{Ar}]3d^{4}$
6. As $\mathrm{Mn^{3+}}$ from $d^{4}$ configuration goes to more stable $d^{5}$ configuration (Half filled), due to more exchange energy in $d^{5}$ configuration.

**Solved independently** (answer withheld)

1. $\mathrm{Mn^{3+}}$ is $[\mathrm{Ar}]\,3d^{4}$ and $\mathrm{Mn^{2+}}$ is $[\mathrm{Ar}]\,3d^{5}$.
2. Reduction $\mathrm{Mn^{3+}} + e^- \rightarrow \mathrm{Mn^{2+}}$ changes $d^{4}$ to the half-filled, extra-stable $d^{5}$, so $E^\circ$ is strongly positive.
3. The change is $d^{4} \rightarrow d^{5}$, which is option $3$.

**Subtopic:** Trends of Electrode Potentials · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q083_555687f9_13112026.png?v=555687f973b3)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q083_41559e34_13112026.png?v=41559e34575b)

---

## Q84

Chemistry · physical · Basic Concepts of Chemistry

The highest number of helium atoms is in

- **(1)** $4\,\mathrm{mol}$ of helium
- (2) $4\,\mathrm{u}$ of helium
- (3) $4\,\mathrm{g}$ of helium
- (4) $2.271098\,\mathrm{L}$ of helium at STP

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (1) $4\,\mathrm{mol}$ of $\mathrm{He} = 4\,N_A$ $\mathrm{He}$ atoms
2. (2) $4\,\mathrm{u}$ of $\mathrm{He} = \frac{4\,\mathrm{u}}{4\,\mathrm{u}} = 1$ $\mathrm{He}$ atom
3. (3) $4\,\mathrm{g}$ of Helium $= \frac{4\,\mathrm{g}}{4\,\mathrm{g}}$ mole $= 1$ mole $= N_A$ $\mathrm{He}$ atom
4. (4) $2.2710982$ of $\mathrm{He}$ at STP $= \frac{2.271}{22.710982}$ mole
5. $= 0.1$ mole
6. $= 0.1\,N_A$ $\mathrm{He}$ atom

**Solved independently** (answer withheld)

1. Option 4: molar volume at STP is $22.71098\,\mathrm{L\,mol^{-1}}$, so $n = \frac{2.271098}{22.71098} = 0.1\,\mathrm{mol}$.
2. Option 1: $n = 4\,\mathrm{mol}$, i.e. $4N_A$ atoms.
3. Option 2: mass of one He atom is $4\,\mathrm{u}$, so $4\,\mathrm{u}$ is $1$ atom.
4. Option 3: $n = \frac{4\,\mathrm{g}}{4\,\mathrm{g\,mol^{-1}}} = 1\,\mathrm{mol}$, i.e. $N_A$ atoms.
5. Largest is $4\,\mathrm{mol}$, which is option $1$.

**Subtopic:** Mole Concept · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 38)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q084_c29192e0_13112026.png?v=c29192e0e435)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q084_6241cd50_13112026.png?v=6241cd50e4fc)

---

## Q85

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Both $\mathrm{[Co(NH_3)_6]^{3+}}$ and $\mathrm{[CoF_6]^{3-}}$ complexes are octahedral but differ in their magnetic behaviour.
- (Statement II) $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic whereas $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{Co^{3+}}$ ion is having $3d^{6}$ configuration.
2. Electronic configuration of $\mathrm{Co^{3+}}$ :
3. In presence of $\mathrm{NH_3}$ ligand, pairing of electrons takes place and it becomes diamagnetic complex ion.
4. In presence of $\mathrm{NH_3}$ ligand :
5. $\therefore$ $\mathrm{[Co(NH_3)_6]^{3+}}$ is octahedral with $d^{2}sp^{3}$ hybridisation and it is diamagnetic in nature.
6. In case of $\mathrm{[CoF_6]^{3-}}$, $\mathrm{Co}$ is in $+3$ oxidation state and it is having $3d^{6}$ configuration.
7. In presence of weak field $\mathrm{F^{-}}$ ligand, pairing does not take place.
8. In presence of $\mathrm{F^{-}}$ ligands :
9. $\therefore$ In $\mathrm{[CoF_6]^{3-}}$, $\mathrm{Co^{3+}}$ is $sp^{3}d^{2}$ hybridised with four unpaired electrons, so it is paramagnetic in nature.

**Solved independently** (answer withheld)

1. In both complexes cobalt is $\mathrm{Co^{3+}}$, configuration $3d^6$, with coordination number 6, so both are octahedral.
2. $\mathrm{NH_3}$ is a strong-field ligand: pairing gives $t_{2g}^6 e_g^0$ (inner-orbital $d^2sp^3$), 0 unpaired electrons, so $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic.
3. $\mathrm{F^-}$ is a weak-field ligand: $t_{2g}^4 e_g^2$ (outer-orbital $sp^3d^2$), 4 unpaired electrons, so $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.
4. Hence Statement I (same geometry, different magnetism) and Statement II are both true, which is option $1$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 39)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q085_ffe69f3d_13112026.png?v=ffe69f3dfe94)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q085_71a09ee1_13112026.png?v=71a09ee1ebaa)

---

## Q86

Chemistry · inorganic · The D- and F-Block Elements – Practice

The pair of lanthanoid ions which are diamagnetic is

- **(1)** $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$
- (2) $\mathrm{Ce^{3+}}$ and $\mathrm{Eu^{2+}}$
- (3) $\mathrm{Gd^{3+}}$ and $\mathrm{Eu^{3+}}$
- (4) $\mathrm{Pm^{3+}}$ and $\mathrm{Sm^{3+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Magnetic moment $\mu = \sqrt{n(n+2)}$
2. $n \rightarrow$ number of unpaired electron
3. $\mathrm{Ce^{4+}} \Rightarrow (\mathrm{Xe})\,4f^{0}$
4. $\mu = 0$ Diamagnetic
5. $\mathrm{Yb^{2+}} \Rightarrow (\mathrm{Xe})\,4f^{14}$
6. $\mu = 0$ Diamagnetic
7. $\mathrm{Ce^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{1}$
8. $\mu = \sqrt{3}$ Paramagnetic
9. $\mathrm{Eu^{2+}} \Rightarrow (\mathrm{Xe})\,4f^{7}$
10. $\mu = \sqrt{63}$ Paramagnetic
11. $\mathrm{Gd^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{7}$
12. $\mu = \sqrt{63}$ Paramagnetic
13. $\mathrm{Eu^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{6}$
14. $\mu = \sqrt{48}$ Paramagnetic
15. $\mathrm{Pm^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{4}$
16. $\mu = \sqrt{24}$ Paramagnetic
17. $\mathrm{Sm^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{5}$
18. $\mu = \sqrt{35}$ Paramagnetic
19. Hence $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$ are only diamagnetic.

**Solved independently** (answer withheld)

1. A diamagnetic ion has no unpaired electrons, so it needs a $4f^0$ or $4f^{14}$ configuration.
2. $\mathrm{Ce}$ ($Z=58$): $\mathrm{Ce^{4+}} = [\mathrm{Xe}]4f^0$, which has 0 unpaired electrons.
3. $\mathrm{Yb}$ ($Z=70$): $\mathrm{Yb^{2+}} = [\mathrm{Xe}]4f^{14}$, which has 0 unpaired electrons.
4. $\mathrm{Pm^{3+}}\,(4f^4)$, $\mathrm{Sm^{3+}}\,(4f^5)$, $\mathrm{Ce^{3+}}\,(4f^1)$, $\mathrm{Eu^{2+}}\,(4f^7)$, $\mathrm{Gd^{3+}}\,(4f^7)$ and $\mathrm{Eu^{3+}}\,(4f^6)$ all have unpaired electrons, so they are paramagnetic.
5. Only the pair $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$ is diamagnetic, which is option $1$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q086_5b3ba9ee_13112026.png?v=5b3ba9ee4b5e)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q086_ab042c4f_13112026.png?v=ab042c4fbc1f)

---

## Q87

Chemistry · inorganic · Principles Related to Practical Chemistry

Given below are certain cations. Using inorganic qualitative analysis, arrange them in increasing group number from 0 to VI.

Choose the correct answer from the options given below.

- (A) $\mathrm{Al^{3+}}$
- (B) $\mathrm{Cu^{2+}}$
- (C) $\mathrm{Ba^{2+}}$
- (D) $\mathrm{Co^{2+}}$
- (E) $\mathrm{Mg^{2+}}$

- **(1)** B, A, D, C, E
- (2) B, C, A, D, E
- (3) E, C, D, B, A
- (4) E, A, B, C, D

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct order of group number of ions is $\underset{(\mathrm{B})}{\mathrm{Cu^{2+}}} < \underset{(\mathrm{A})}{\mathrm{Al^{3+}}} < \underset{(\mathrm{D})}{\mathrm{Co^{2+}}} < \underset{(\mathrm{C})}{\mathrm{Ba^{2+}}} < \underset{(\mathrm{E})}{\mathrm{Mg^{2+}}}$
2. $\therefore$ The correct order is B, A, D, C, E

**Solved independently** (answer withheld)

1. $\mathrm{Cu^{2+}}$ is precipitated as sulphide by $\mathrm{H_2S}$ in dilute HCl, so it is group II.
2. $\mathrm{Al^{3+}}$ is precipitated as hydroxide by $\mathrm{NH_4OH}$ in presence of $\mathrm{NH_4Cl}$, so it is group III.
3. $\mathrm{Co^{2+}}$ is precipitated as sulphide by $\mathrm{H_2S}$ in ammoniacal medium, so it is group IV.
4. $\mathrm{Ba^{2+}}$ is precipitated as carbonate by $\mathrm{(NH_4)_2CO_3}$, so it is group V.
5. $\mathrm{Mg^{2+}}$ remains for group VI.
6. Increasing order: B (II), A (III), D (IV), C (V), E (VI), which is option $1$.

**Subtopic:** Group Analysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 40)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q087_979324d4_13112026.png?v=979324d4a26b)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q087_24fee33b_13112026.png?v=24fee33b8661)

---

## Q88

Chemistry · organic · Haloalkanes and Haloarenes

Major products A and B formed in the following reaction sequence, are

![printed figure: 2-methylcyclohexan-1-ol →(PBr₃) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q088_a9168565_13112026.png?v=a91685654b9f)

*2-methylcyclohexan-1-ol →[PBr₃] A (major) →[alc. KOH, Δ] B (major)*

![drawn: 2-methylcyclohexan-1-ol →(PBr₃) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_question_b3ba0357_13112026.svg?v=b3ba0357421f)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2-methylcyclohexan-1-ol `CC1CCCCC1O` ![2-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_question_s1_79eed43b_13112026.svg?v=79eed43b0c22)

- **(1)** 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_1_s1_2d1efb40_13112026.svg?v=2d1efb40eae4); 1-methylcyclohex-1-ene `CC1=CCCCC1` ![1-methylcyclohex-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_1_s2_ba57c26b_13112026.svg?v=ba57c26b570b) — A =, B =
- (2) 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_2_s1_2d1efb40_13112026.svg?v=2d1efb40eae4); 4-methylcyclohex-1-ene `CC1CC=CCC1` ![4-methylcyclohex-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_2_s2_9c0f57d1_13112026.svg?v=9c0f57d13d75) — A =, B =
- (3) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_3_s1_bbec4cde_13112026.svg?v=bbec4cde35ec); 6-methylcyclohex-2-en-1-ol `CC1CCC=CC1O` ![6-methylcyclohex-2-en-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_3_s2_844b7d62_13112026.svg?v=844b7d628c94) — A =, B =
- (4) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_4_s1_bbec4cde_13112026.svg?v=bbec4cde35ec); 2-methylcyclohexan-1-one `CC1CCCCC1=O` ![2-methylcyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q088_option_4_s2_7eaab55c_13112026.svg?v=7eaab55cfa65) — A =, B =

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{PBr_3}$ converts the alcohol to an alkyl bromide: $\mathrm{R{-}OH} \rightarrow \mathrm{R{-}Br}$, so A is 1-bromo-2-methylcyclohexane.
2. Alcoholic $\mathrm{KOH}$ with heat causes $\beta$-elimination of $\mathrm{HBr}$ from A.
3. Two $\beta$-carbons are available; removing H from the carbon bearing $\mathrm{CH_3}$ gives the more substituted (trisubstituted) alkene, favoured by Saytzeff rule.
4. So B is 1-methylcyclohexene, matching option $1$.

**Subtopic:** Reactions of Haloalkanes – Elimination Reactions, Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q088_592ee5c1_13112026.png?v=592ee5c10da7)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q088_4d4e315f_13112026.png?v=4d4e315fd450)

---

## Q89

Chemistry · physical · Thermodynamics

The work done during reversible isothermal expansion of one mole of hydrogen gas at $25^\circ\mathrm{C}$ from pressure of $20$ atmosphere to $10$ atmosphere is (Given $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$)

- (1) $0$ calorie
- **(2)** $-413.14$ calories
- (3) $413.14$ calories
- (4) $100$ calories

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $W_{\mathrm{rev,\,iso}} = -2.303\,nRT\log\frac{P_i}{P_f}$
2. $= -2.303 \times 1 \times 2 \times 298 \times \log 2$
3. $= -2.303 \times 1 \times 2 \times 298 \times 0.3$
4. $= -413.14$ calories

**Solved independently** (answer withheld)

1. For reversible isothermal expansion of an ideal gas, $W = -2.303\,nRT\log\frac{P_1}{P_2}$.
2. $T = 25 + 273 = 298\,\mathrm{K}$, $n = 1$, $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$, $\frac{P_1}{P_2} = \frac{20}{10} = 2$.
3. $W = -2.303 \times 1 \times 2.0 \times 298 \times \log 2 = -1372.59 \times 0.3010$.
4. $W \approx -413.1\,\mathrm{cal}$, which matches option $2$ ($-413.14$ calories).

**Subtopic:** Pressure–Volume Work for Isothermal Reversible Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q089_1a35b918_13112026.png?v=1a35b918682c)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q089_e5fec772_13112026.png?v=e5fec772fa10)

---

## Q90

Chemistry · organic · Amines

Identify the major product C formed in the following reaction sequence: $\mathrm{CH_3-CH_2-CH_2-I \xrightarrow{NaCN} A \xrightarrow[\text{Partial hydrolysis}]{OH^-} B \xrightarrow[Br_2]{NaOH} \underset{(major)}{C}}$

- **(1)** propylamine
- (2) butylamine
- (3) butanamide
- (4) $\alpha$–bromobutanoic acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Step-I is $\mathrm{S_N}$ reaction with $\overset{\ominus}{\mathrm{C}}\mathrm{N}$ nucleophile.
2. Step-II will give amide.
3. Step-III is Hoffmann bromamide degradation reaction.

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2I} + \mathrm{NaCN} \rightarrow \mathrm{CH_3CH_2CH_2CN}$ (A, butanenitrile) by $S_N2$ substitution.
2. Partial hydrolysis: $\mathrm{CH_3CH_2CH_2CN} \xrightarrow{\mathrm{OH^-}} \mathrm{CH_3CH_2CH_2CONH_2}$ (B, butanamide).
3. Hofmann bromamide degradation: $\mathrm{CH_3CH_2CH_2CONH_2} + \mathrm{Br_2} + 4\mathrm{NaOH} \rightarrow \mathrm{CH_3CH_2CH_2NH_2} + \mathrm{Na_2CO_3} + 2\mathrm{NaBr} + 2\mathrm{H_2O}$.
4. C is $\mathrm{CH_3CH_2CH_2NH_2}$, propylamine, which is option $1$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 42)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q090_177094f5_13112026.png?v=177094f59bf9)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q090_2bdc80c6_13112026.png?v=2bdc80c6c48d)

---

## Q91

Chemistry · organic · Haloalkanes and Haloarenes

The products A and B obtained in the following reactions, respectively, are
$\mathrm{3ROH + PCl_3 \rightarrow 3RCl + A}$
$\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + B}$

- (1) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_3}$
- (2) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_4}$
- (3) $\mathrm{H_3PO_4}$ and $\mathrm{POCl_3}$
- **(4)** $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. These reactions are preparation of haloalkanes from alcohols.
2. $\mathrm{3ROH + PCl_3 \longrightarrow 3RCl + \underset{(A)}{H_3PO_3}}$
3. $\mathrm{ROH + PCl_5 \longrightarrow RCl + HCl + \underset{(B)}{POCl_3}}$
4. A and B are $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$ respectively.

**Solved independently** (answer withheld)

1. $\mathrm{3ROH + PCl_3 \rightarrow 3RCl + H_3PO_3}$, so $A = \mathrm{H_3PO_3}$.
2. $\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + POCl_3}$, so $B = \mathrm{POCl_3}$.
3. $A, B = \mathrm{H_3PO_3}, \mathrm{POCl_3}$, which is option $4$.

**Subtopic:** Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q091_fde42249_13112026.png?v=fde422495d37)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q091_8c24653e_13112026.png?v=8c24653e85c7)

---

## Q92

Chemistry · physical · Electrochemistry

Mass in grams of copper deposited by passing $9.6487\,\mathrm{A}$ current through a voltmeter containing copper sulphate solution for $100$ seconds is (Given : Molar mass of $\mathrm{Cu}$ : $63\,\mathrm{g\,mol^{-1}}$, $1\,\mathrm{F} = 96487\,\mathrm{C}$)

- (1) $3.15\,\mathrm{g}$
- **(2)** $0.315\,\mathrm{g}$
- (3) $31.5\,\mathrm{g}$
- (4) $0.0315\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Cu^{2+}(aq)} + 2e^{-} \rightarrow \mathrm{Cu(s)}$
2. Mass of $\mathrm{Cu}$ deposited $(w) = \frac{M \times i \times t}{nF}$
3. $= \frac{63 \times 9.6487 \times 100}{2 \times 96487}$
4. $= 0.315\,\mathrm{g}$

**Solved independently** (answer withheld)

1. $Q = It = 9.6487\,\mathrm{A} \times 100\,\mathrm{s} = 964.87\,\mathrm{C}$.
2. $\frac{964.87}{96487} = 0.01\,\mathrm{F}$.
3. $\mathrm{Cu^{2+}} + 2e^- \rightarrow \mathrm{Cu}$, so $n_{\mathrm{Cu}} = \frac{0.01}{2} = 0.005\,\mathrm{mol}$.
4. $m = 0.005 \times 63 = 0.315\,\mathrm{g}$, which is option $2$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 43)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q092_17cc2705_13112026.png?v=17cc2705fc6d)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q092_7db5bbca_13112026.png?v=7db5bbca093b)

---

## Q93

Chemistry · physical · Basic Concepts of Chemistry

A compound X contains $32\%$ of A, $20\%$ of B and remaining percentage of C. Then, the empirical formula of X is :
(Given atomic masses of $\mathrm{A} = 64$; $\mathrm{B} = 40$; $\mathrm{C} = 32\,\mathrm{u}$)

- (1) $\mathrm{A_2BC_2}$
- **(2)** $\mathrm{ABC_3}$
- (3) $\mathrm{AB_2C_2}$
- (4) $\mathrm{ABC_4}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. So, empirical formula of $X = \begin{matrix} \mathrm{A} & : & \mathrm{B} & : & \mathrm{C} \\ 1 & : & 1 & : & 3 \end{matrix}$
2. $\therefore$ The correct empirical formula of compound X is $\mathrm{ABC_3}$

**Solved independently** (answer withheld)

1. Percentage of C $= 100 - 32 - 20 = 48\%$.
2. Moles in 100 g: $n_A = \frac{32}{64} = 0.5$, $n_B = \frac{20}{40} = 0.5$, $n_C = \frac{48}{32} = 1.5$.
3. Divide by the smallest ($0.5$): $A:B:C = 1:1:3$.
4. Empirical formula $= \mathrm{ABC_3}$, which is option $2$.

**Subtopic:** Empirical and Molecular Formula · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 43)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q093_dd72db6b_13112026.png?v=dd72db6bdefc)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q093_1b46afc0_13112026.png?v=1b46afc0408f)

---

## Q94

Chemistry · inorganic · Principles Related to Practical Chemistry

During the preparation of Mohr’s salt solution (Ferrous ammonium sulphate), which of the following acid is added to prevent hydrolysis of $\mathrm{Fe^{2+}}$ ion?

- (1) dilute hydrochloric acid
- (2) concentrated sulphuric acid
- (3) dilute nitric acid
- **(4)** dilute sulphuric acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. During the preparation of Mohr’s salt, dilute sulphuric acid is added to prevent the hydrolysis of $\mathrm{Fe^{2+}}$ ion.

**Solved independently** (answer withheld)

1. Adding dilute $\mathrm{H_2SO_4}$ supplies $\mathrm{H^+}$ and the common $\mathrm{SO_4^{2-}}$ ion, suppressing $\mathrm{Fe^{2+}}$ hydrolysis without oxidising it, while $\mathrm{HNO_3}$ and concentrated $\mathrm{H_2SO_4}$ are oxidising and $\mathrm{HCl}$ adds foreign $\mathrm{Cl^-}$, so the answer is option $4$.

**Subtopic:** Titration · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 43)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q094_efb1cb05_13112026.png?v=efb1cb0598dd)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q094_1984f2c4_13112026.png?v=1984f2c4a9d3)

---

## Q95

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the correct answer.

- (1) Three resonance structures can be drawn for ozone
- (2) $\mathrm{BF_3}$ has non-zero dipole moment
- (3) Dipole moment of $\mathrm{NF_3}$ is greater than that of $\mathrm{NH_3}$
- **(4)** Three canonical forms can be drawn for $\mathrm{CO_3^{2-}}$ ion

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (1) In ozone; there are two resonating structures.
2. (2) $\mathrm{BF_3}$ i.e., ; Dipole moment $= 0$
3. (3) $(0.80 \times 10^{-30}\,\mathrm{Cm})$ $<$ $(4.90 \times 10^{-30}\,\mathrm{Cm})$
4. (4) (3 canonical forms)

**Solved independently** (answer withheld)

1. In $\mathrm{CO_3^{2-}}$ the $\mathrm{C=O}$ double bond can sit on any of the three O atoms, giving three canonical forms, so statement 1 is true.
2. Ozone $\mathrm{O_3}$ has only two resonance structures, so statement 2 is false.
3. $\mathrm{BF_3}$ is trigonal planar and the three $\mathrm{B-F}$ bond dipoles cancel, so $\mu = 0$; statement 3 is false.
4. In $\mathrm{NH_3}$ the lone-pair moment adds to the $\mathrm{N-H}$ bond moments, while in $\mathrm{NF_3}$ it opposes the $\mathrm{N-F}$ bond moments, so $\mu(\mathrm{NH_3}) > \mu(\mathrm{NF_3})$; statement 4 is false.
5. Only statement 1 is correct, which is option $4$.

**Subtopic:** Bond Parameters, Dipole Moment · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 44)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q095_69427e7b_13112026.png?v=69427e7b8b38)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q095_f25e1023_13112026.png?v=f25e102335b8)

---

## Q96

Chemistry · physical · Chemical Kinetics

The rate of a reaction quadruples when temperature changes from $27^\circ\mathrm{C}$ to $57^\circ\mathrm{C}$. Calculate the energy of activation. Given $R = 8.314\,\mathrm{J\,K^{-1}\,mol^{-1}}$, $\log 4 = 0.6021$

- **(1)** $38.04\,\mathrm{kJ/mol}$
- (2) $380.4\,\mathrm{kJ/mol}$
- (3) $3.80\,\mathrm{kJ/mol}$
- (4) $3804\,\mathrm{kJ/mol}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$
2. $\log\left(\frac{4}{1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{300} - \frac{1}{330}\right)$
3. $E_a = \frac{(\log(4)) \times 2.303 \times 8.314 \times 300 \times 330}{30}$
4. $= 3.804 \times 10^{4}\,\mathrm{J/mol}$
5. $= 38.04\,\mathrm{kJ/mol}$

**Solved independently** (answer withheld)

1. Convert temperatures: $T_1 = 27 + 273 = 300\,\mathrm{K}$, $T_2 = 57 + 273 = 330\,\mathrm{K}$.
2. Arrhenius two-temperature form: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. Substitute $\frac{k_2}{k_1} = 4$: $0.6021 = \frac{E_a}{2.303 \times 8.314} \times \frac{30}{300 \times 330}$.
4. Rearrange: $E_a = 2.303 \times 8.314 \times 0.6021 \times \frac{99000}{30} = 11.5285 \times 3300$.
5. $E_a \approx 38044\,\mathrm{J\,mol^{-1}} = 38.04\,\mathrm{kJ\,mol^{-1}}$, which is option $1$.

**Subtopic:** Arrhenius Equation · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 44)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q096_2bd1e61e_13112026.png?v=2bd1e61e5957)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q096_92b0c0b0_13112026.png?v=92b0c0b0e78c)

---

## Q97

Chemistry · organic · Hydrocarbons

For the given reaction:
‘P’ is

![printed figure: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q097_085c86e0_13112026.png?v=085c86e0b3e6)

*1,2-dicyclohexylethene →[$\ce{KMnO4/H+}$] 'P' (major product)*

![drawn: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q097_question_d670de2f_13112026.svg?v=d670de2f74e0)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1,2-dicyclohexylethene `C(=CC1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethene](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q097_question_s1_69169cd1_13112026.svg?v=69169cd1c645)

- (1) cyclohexanecarbaldehyde `O=CC1CCCCC1` ![cyclohexanecarbaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_1_s1_79f04f91_13112026.svg?v=79f04f918b83) — $\mathrm{-CHO}$
- **(2)** cyclohexanecarboxylic acid `O=C(O)C1CCCCC1` ![cyclohexanecarboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_2_s1_5fc26872_13112026.svg?v=5fc268722cd9) — $\mathrm{-COOH}$
- (3) 1,2-dicyclohexylethane-1,2-diol `OC(C1CCCCC1)C(O)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-diol](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_3_s1_97a497f5_13112026.svg?v=97a497f5ed27) — $\mathrm{-CH(OH)-CH(OH)-}$
- (4) 1,2-dicyclohexylethane-1,2-dione `O=C(C(=O)C1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-dione](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_drawn/q097_option_4_s1_a3dbbe83_13112026.svg?v=a3dbbe83efdc) — $\mathrm{-C(=O)-C(=O)-}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The reactant is 1,2-dicyclohexylethene, $\mathrm{C_6H_{11}-CH=CH-C_6H_{11}}$.
2. Acidic $\mathrm{KMnO_4}$ is a strong oxidant that cleaves the $\mathrm{C=C}$ bond (oxidative cleavage).
3. Each alkene carbon carries one H, so it is first converted to $\mathrm{-CHO}$ and then further oxidised to $\mathrm{-COOH}$.
4. The symmetric alkene gives two molecules of $\mathrm{C_6H_{11}-COOH}$ (cyclohexanecarboxylic acid), which is option $2$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q097_f8b86994_13112026.png?v=f8b8699484b2)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q097_67c3c703_13112026.png?v=67c3c7035d49)

---

## Q98

Chemistry · physical · Solutions

The plot of osmotic pressure ($\Pi$) vs concentration ($\mathrm{mol\,L^{-1}}$) for a solution gives a straight line with slope $25.73\,\mathrm{L\,bar\,mol^{-1}}$. The temperature at which the osmotic pressure measurement is done is (Use $R = 0.083\,\mathrm{L\,bar\,mol^{-1}\,K^{-1}}$)

- **(1)** $37^{\circ}\mathrm{C}$
- (2) $310^{\circ}\mathrm{C}$
- (3) $25.73^{\circ}\mathrm{C}$
- (4) $12.05^{\circ}\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\Pi = \mathrm{CRT}$
2. Slope $= \mathrm{RT}$
3. $25.73 = 0.083 \times \mathrm{T}$
4. $\mathrm{T} = \frac{25.73}{0.083} = 309.47 \approx 310\,\mathrm{K}$
5. $\therefore$ Temperature in $^{\circ}\mathrm{C} = 310 - 273$
6. $= 37^{\circ}\mathrm{C}$

**Solved independently** (answer withheld)

1. From $\Pi = CRT$, a plot of $\Pi$ vs $C$ is a straight line with slope $RT$.
2. $RT = 25.73\,\mathrm{L\,bar\,mol^{-1}}$, so $T = \frac{25.73}{0.083} = 310\,\mathrm{K}$.
3. $310\,\mathrm{K} - 273 = 37\,^{\circ}\mathrm{C}$, which is option $1$.

**Subtopic:** Osmosis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 45)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q098_201edaaf_13112026.png?v=201edaafe896)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q098_20879416_13112026.png?v=2087941645ac)

---

## Q99

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below.

- (Statement I) $\mathrm{[Co(NH_3)_6]^{3+}}$ is a homoleptic complex whereas $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ is a heteroleptic complex.
- (Statement II) Complex $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligands but $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has more than one kind of ligands.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{[Co(NH_3)_6]^{3+}}$ is a homoleptic complex as only one type of ligands ($\mathrm{NH_3}$) is coordinated with $\mathrm{Co^{3+}}$ ion.
2. While $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ is a heteroleptic complex in which $\mathrm{Co^{3+}}$ ion is ligated with more than one type of ligands, i.e., $\mathrm{NH_3}$ and $\mathrm{Cl^{-}}$.

**Solved independently** (answer withheld)

1. $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligand ($\mathrm{NH_3}$), so it is homoleptic.
2. $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has two kinds of ligands ($\mathrm{NH_3}$ and $\mathrm{Cl^-}$), so it is heteroleptic; Statement I is true.
3. Statement II states exactly these ligand facts, so it is true; both true is option $1$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q099_44f4e1d2_13112026.png?v=44f4e1d27a88)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q099_b026728e_13112026.png?v=b026728ea870)

---

## Q100

Chemistry · physical · Chemical Equilibrium

Consider the following reaction in a sealed vessel at equilibrium with concentrations of $\mathrm{N_2} = 3.0 \times 10^{-3}\,\mathrm{M}$, $\mathrm{O_2} = 4.2 \times 10^{-3}\,\mathrm{M}$ and $\mathrm{NO} = 2.8 \times 10^{-3}\,\mathrm{M}$.
$\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$
If $0.1\,\mathrm{mol\,L^{-1}}$ of $\mathrm{NO_{(g)}}$ is taken in a closed vessel, what will be degree of dissociation $(\alpha)$ of $\mathrm{NO_{(g)}}$ at equilibrium?

- (1) $0.00889$
- (2) $0.0889$
- (3) $0.8889$
- **(4)** $0.717$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$
2. $K_c = \frac{[\mathrm{N_2}][\mathrm{O_2}]}{[\mathrm{NO}]^2}$
3. $= \frac{3 \times 10^{-3} \times 4.2 \times 10^{-3}}{2.8 \times 10^{-3} \times 2.8 \times 10^{-3}}$
4. $= 1.607$
5. $\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$
6. $t = 0$: $0.1$, $0$, $0$
7. $0.1 - 0.1\alpha$, $0.05\alpha$, $0.05\alpha$
8. $K_c = \frac{0.05\alpha \times 0.05\alpha}{(0.1 - 0.1\alpha)^2}$
9. $K_c = \frac{0.05\alpha \times 0.05\alpha}{0.01(1 - \alpha)^2}$
10. $1.607 = \frac{(0.05)^2\alpha^2}{0.01(1 - \alpha)^2}$
11. $\frac{\alpha^2}{(1 - \alpha)^2} = \frac{1.607 \times (0.1)^2}{(0.05)^2}$
12. $\frac{\alpha}{1 - \alpha} = \frac{1.27 \times 0.1}{0.05}$
13. $\frac{\alpha}{1 - \alpha} = 2.54$
14. $\alpha = 2.54 - 2.54\alpha$
15. $3.54\alpha = 2.54$
16. $\alpha = \frac{2.54}{3.54} = 0.717$

**Solved independently** (answer withheld)

1. $K_c = \frac{[\mathrm{N_2}][\mathrm{O_2}]}{[\mathrm{NO}]^2} = \frac{(3.0\times10^{-3})(4.2\times10^{-3})}{(2.8\times10^{-3})^2}$.
2. $K_c = \frac{12.6\times10^{-6}}{7.84\times10^{-6}} = 1.607$.
3. Starting with $0.1\,\mathrm{M}$ NO and degree of dissociation $\alpha$: $[\mathrm{NO}] = 0.1(1-\alpha)$, $[\mathrm{N_2}] = [\mathrm{O_2}] = 0.05\alpha$.
4. $K_c = \frac{(0.05\alpha)^2}{(0.1(1-\alpha))^2} = \left(\frac{0.5\alpha}{1-\alpha}\right)^2 = 1.607$.
5. $\frac{0.5\alpha}{1-\alpha} = \sqrt{1.607} = 1.268$.
6. $0.5\alpha = 1.268 - 1.268\alpha \Rightarrow \alpha = \frac{1.268}{1.768} = 0.717$, which is option $4$.

**Subtopic:** Calculating Equilibrium Concentrations · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 46)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q100_cc5e7e53_13112026.png?v=cc5e7e531a84)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q100_ae546b71_13112026.png?v=ae546b71a267)

---

## Q101

Biology · botany · Plant Growth and Development

Auxin is used by gardeners to prepare weed-free lawns. But no damage is caused to grass as auxin

- (1) promotes apical dominance.
- (2) promotes abscission of mature leaves only.
- **(3)** does not affect mature monocotyledonous plants.
- (4) can help in cell division in grasses, to produce growth.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Auxin does not affect mature monocot plants.
2. In monocots, especially grasses show limited translocation and cause rapid degradation of external auxin.

**Solved independently** (answer withheld)

1. Synthetic auxins like $2,4\text{-D}$ are selective herbicides that kill dicot weeds but do not affect mature monocotyledonous plants such as grass, which is option $3$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q101_21eb749a_13112026.png?v=21eb749ac333)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q101_a5c7a9f2_13112026.png?v=a5c7a9f2eff8)

---

## Q102

Biology · botany · Photosynthesis in Higher Plants

How many molecules of ATP and NADPH are required for every molecule of $\mathrm{CO_2}$ fixed in the Calvin cycle?

- (1) 2 molecules of ATP and 3 molecules of NADPH
- (2) 2 molecules of ATP and 2 molecules of NADPH
- (3) 3 molecules of ATP and 3 molecules of NADPH
- **(4)** 3 molecules of ATP and 2 molecules of NADPH

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For fixation of $1$ molecule of $\mathrm{CO_2}$ in Calvin cycle $3$ $\mathrm{ATP}$ molecules and $2$ $\mathrm{NADPH}$ molecules are required.

**Solved independently** (answer withheld)

1. Reduction of 2 molecules of 3-PGA formed per $\mathrm{CO_2}$ uses $2\,\mathrm{ATP} + 2\,\mathrm{NADPH}$; regeneration of RuBP uses $1\,\mathrm{ATP}$, so per $\mathrm{CO_2}$ fixed: $3\,\mathrm{ATP} + 2\,\mathrm{NADPH}$, which is option $4$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 47)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q102_d73527e0_13112026.png?v=d73527e01cd3)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q102_ca13c5e4_13112026.png?v=ca13c5e4325f)

---

## Q103

Biology · botany · Anatomy of Flowering Plants

In the given figure, which component has thin outer walls and highly thickened inner walls?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q103_7d46b6e1_13112026.png?v=7d46b6e1f21f)

- **(1)** C
- (2) D
- (3) A
- (4) B

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Guard cells of stomata have thin outer wall and highly thickened inner walls.

**Solved independently** (answer withheld)

1. The figure shows a stoma: $A$ = epidermal cell, $B$ = subsidiary cell, $C$ = bean-shaped guard cell, $D$ = stomatal pore.
2. As NCERT teaches, guard cells have thin outer walls and highly thickened inner walls (towards the pore), so the answer is $C$, which is option $1$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 47)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q103_3a894d82_13112026.png?v=3a894d82ab97)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q103_67ae6025_13112026.png?v=67ae6025dc8e)

---

## Q104

Biology · botany · Cell: The Unit of Life

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Nucleolus | I | Site of formation of glycolipid |
| B | Centriole | II | Organization like the cartwheel |
| C | Leucoplasts | III | Site for active ribosomal RNA synthesis |
| D | Golgi apparatus | IV | For storing nutrients |

- **(1)** A-III, B-II, C-IV, D-I
- (2) A-II, B-III, C-I, D-IV
- (3) A-III, B-IV, C-II, D-I
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Nucleolus is a site for active ribosomal RNA synthesis
2. Both the centrioles in a centrosome lie perpendicular to each other in which each has an organisation like the cartwheel.
3. Leucoplasts are the colourless plastids of varied shapes and sizes with stored nutrients.
4. Golgi apparatus is the important site for formation of glycoproteins and glycolipids.

**Solved independently** (answer withheld)

1. Nucleolus is the site of active ribosomal RNA synthesis $\Rightarrow$ A-III.
2. Centriole shows a cartwheel organization of nine triplet fibrils $\Rightarrow$ B-II.
3. Leucoplasts (amyloplasts, elaioplasts, aleuroplasts) store starch, oils and proteins $\Rightarrow$ C-IV.
4. Golgi apparatus is the site of formation of glycoproteins and glycolipids $\Rightarrow$ D-I.
5. Combination A-III, B-II, C-IV, D-I corresponds to option $1$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 47)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q104_287d1917_13112026.png?v=287d1917b3cf)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q104_74ecc94c_13112026.png?v=74ecc94c7554)

---

## Q105

Biology · botany · Morphology of Flowering Plants

Identify the type of flowers based on the position of calyx, corolla and androecium with respect to the ovary from the given figures (a) and (b)

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q105_0f69ed2e_13112026.png?v=0f69ed2e6668)

- (1) (a) Epigynous; (b) Hypogynous
- (2) (a) Hypogynous; (b) Epigynous
- (3) (a) Perigynous; (b) Epigynous
- **(4)** (a) Perigynous; (b) Perigynous

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. If gynoecium is situated in the centre and other parts of the flower are located on the rim of the thalamus almost at the same level, it is called perigynous.
2. Both diagram shows perigynous condition.

**Solved independently** (answer withheld)

1. In figure (a) the thalamus grows up as a cup around the ovary; the ovary is not fused with the cup wall.
2. The sepals, petals and stamens of (a) arise from the rim of the cup, roughly at the level of the ovary, so (a) is perigynous.
3. In figure (b) the thalamus is a shallower cup; the ovary again sits free in its centre and the other floral parts arise from its rim at about the ovary's level, so (b) is perigynous.
4. Neither figure shows parts below a superior ovary on a flat/convex thalamus (hypogynous) or parts above an ovary fused with the thalamus (epigynous), so the answer is (a) Perigynous; (b) Perigynous, option $4$.

**Subtopic:** Position of the Ovary · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q105_82334355_13112026.png?v=82334355fb1f)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q105_b47d593b_13112026.png?v=b47d593b6263)

---

## Q106

Biology · botany · Biological Classification

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Rhizopus | I | Mushroom |
| B | Ustilago | II | Smut fungus |
| C | Puccinia | III | Bread mould |
| D | Agaricus | IV | Rust fungus |

- **(1)** A-III, B-II, C-IV, D-I
- (2) A-I, B-III, C-II, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Rhizopus is a bread mould fungus.
2. Ustilago is a smut fungi.
3. Puccinia is known as rust fungi.
4. Agaricus is commonly called mushroom.
5. A-III
6. B-II
7. C-IV
8. D-I

**Solved independently** (answer withheld)

1. Rhizopus is the common bread mould, so A–III.
2. Ustilago causes smut disease of cereals, so B–II.
3. Puccinia is the rust fungus of wheat, so C–IV.
4. Agaricus is the edible mushroom, so D–I.
5. The combination A-III, B-II, C-IV, D-I is option $1$.

**Subtopic:** Basidiomycetes, Phycomycetes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q106_38ea22d4_13112026.png?v=38ea22d45814)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q106_f70d9db4_13112026.png?v=f70d9db435bb)

---

## Q107

Biology · botany · Morphology of Flowering Plants

Which of the following is an example of actinomorphic flower?

- **(1)** Datura
- (2) Cassia
- (3) Pisum
- (4) Sesbania

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Datura shows actinomorphic flower.
2. In Cassia, Pisum and Sesbania, zygomorphic flowers are seen.

**Solved independently** (answer withheld)

1. NCERT lists mustard, Datura and chilli as actinomorphic, while pea (Pisum), Sesbania (bean-type papilionaceous flowers) and Cassia are zygomorphic, so the answer is option $1$ (Datura).

**Subtopic:** The Flower · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q107_fda10a45_13112026.png?v=fda10a45b17a)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q107_3a5a0cfb_13112026.png?v=3a5a0cfb8661)

---

## Q108

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the set of **correct** statements:
Choose the correct answer from the options given below.

- (A) The flowers of *Vallisneria* are colourful and produce nectar.
- (B) The flowers of water lily are not pollinated by water.
- (C) In most of water-pollinated species, the pollen grains are protected from wetting.
- (D) Pollen grains of some hydrophytes are long and ribbon like.
- (E) In some hydrophytes, the pollen grains are carried passively inside water.

- (1) C, D and E only
- (2) A, B, C and D only
- (3) A, C, D and E only
- **(4)** B, C, D and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Flowers of *Vallisneria* are not colourful and do not produce nectar.
2. Waterlily is pollinated by insect or wind.
3. In water-pollinated species, pollen grains are protected from wetting by a mucilaginous covering.
4. In some hydrophytes such as *Vallisneria* pollen grains are carried passively by water current.

**Solved independently** (answer withheld)

1. Statement A: water-pollinated flowers such as $Vallisneria$ are not colourful and do not produce nectar, so A is false.
2. Statement B: water lily emerges above water and is pollinated by insects or wind, not water, so B is true.
3. Statement C: in most water-pollinated species pollen grains are protected from wetting by a mucilaginous covering, so C is true.
4. Statement D: in some hydrophytes such as seagrasses, pollen grains are long and ribbon-like, so D is true.
5. Statement E: in some hydrophytes such as seagrasses, pollen grains are carried passively inside water, so E is true.
6. True set is B, C, D and E, which is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q108_ea6833f1_13112026.png?v=ea6833f18674)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q108_806bf268_13112026.png?v=806bf2685760)

---

## Q109

Biology · botany · Principles of Inheritance and Variation

A pink flowered Snapdragon plant was crossed with a red flowered Snapdragon plant. What type of phenotype/s is/are expected in the progeny?

- (1) Only red flowered plants
- **(2)** Red flowered as well as pink flowered plants
- (3) Only pink flowered plants
- (4) Red, Pink as well as white flowered plants

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Pink colour flower in snapdragon have genotype $\mathbf{Rr}$
2. Red flowered snapdragon have genotype $\mathbf{RR}$ when they both are crossed
3. So the progeny that we get are red and pink flowered plants only

**Solved independently** (answer withheld)

1. Flower colour in snapdragon shows incomplete dominance: $RR$ = red, $Rr$ = pink, $rr$ = white.
2. Cross: $Rr \times RR$ gives gametes $R, r$ and $R$.
3. Progeny: $\frac{1}{2} RR$ (red) $+ \frac{1}{2} Rr$ (pink), which is option $2$.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q109_db68e303_13112026.png?v=db68e3030d46)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q109_d936def9_13112026.png?v=d936def9a6aa)

---

## Q110

Biology · botany · Plant Growth and Development

Formation of interfascicular cambium from fully developed parenchyma cells is an example for

- (1) Differentiation
- (2) Redifferentiation
- **(3)** Dedifferentiation
- (4) Maturation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The phenomenon of formation of interfascicular cambium from fully differentiated parenchyma cells is called dedifferentiation.

**Solved independently** (answer withheld)

1. Fully differentiated parenchyma cells regaining the ability to divide to form interfascicular cambium is $\text{dedifferentiation}$, which is option $3$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 50)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q110_922cf332_13112026.png?v=922cf332e04a)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q110_3143984c_13112026.png?v=3143984ce6c3)

---

## Q111

Biology · botany · Principles of Inheritance and Variation

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Two or more alternative forms of a gene | I | Back cross |
| B | Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent | II | Ploidy |
| C | Cross of $\mathrm{F_1}$ progeny with any of the parents | III | Allele |
| D | Number of chromosome sets in plant | IV | Test cross |

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-I, C-III, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. Two or more alternative forms of gene are called alleles.
2. B. Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent is a test cross.
3. C. Cross of $\mathrm{F_1}$ progeny with any of the parents is a back cross.
4. D. Number of chromosome sets in plant is called ploidy.

**Solved independently** (answer withheld)

1. Two or more alternative forms of a gene are alleles: $A \rightarrow III$.
2. A cross of $\mathrm{F_1}$ with the homozygous recessive parent is a test cross: $B \rightarrow IV$.
3. A cross of $\mathrm{F_1}$ with any of the parents is a back cross: $C \rightarrow I$.
4. The number of chromosome sets in a plant is its ploidy: $D \rightarrow II$, so the match is A-III, B-IV, C-I, D-II, which is option $3$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 50)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q111_407b4798_13112026.png?v=407b4798d438)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q111_41628e94_13112026.png?v=41628e940b3c)

---

## Q112

Biology · botany · Photosynthesis in Higher Plants

Which of the following are required for the dark reaction of photosynthesis? Choose the correct answer from the options given below:

- (A) Light
- (B) Chlorophyll
- (C) $\mathrm{CO_2}$
- (D) ATP
- (E) NADPH

- (1) A, B and C only
- (2) B, C and D only
- **(3)** C, D and E only
- (4) D and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For dark reaction of photosynthesis there are the requirement of
2. $\mathrm{CO_2}$
3. ATP
4. NADPH

**Solved independently** (answer withheld)

1. The dark reaction is the Calvin cycle, the biosynthetic phase of photosynthesis.
2. It fixes $\mathrm{CO_2}$ (C) through RuBisCO into carbohydrate.
3. Reduction of $\mathrm{CO_2}$ uses ATP (D) and NADPH (E) made in the light reaction.
4. Light (A) and chlorophyll (B) are needed only in the light reaction, not directly in the dark reaction.
5. So the required set is C, D and E only, which is option $3$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q112_9f149c3e_13112026.png?v=9f149c3ed440)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q112_974aecda_13112026.png?v=974aecda4bd5)

---

## Q113

Biology · botany · Cell Cycle and Cell Division

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Chromosomes become gradually visible under light microscope during leptotene stage.
- (Statement II) The beginning of diplotene stage is recognized by dissolution of synaptonemal complex.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. During leptotene stage the chromosomes become gradually visible under the light microscope.
2. The beginning of diplotene is recognised by the dissolution of the synaptonemal complex and the tendency of the recombined homologous chromosomes of the bivalents to separate from each other except at the site of crossover.
3. Thus both statement I and II are correct.

**Solved independently** (answer withheld)

1. Statement I: in leptotene, chromosomes become gradually visible under the light microscope, so Statement I is true.
2. Statement II: the beginning of diplotene is recognised by dissolution of the synaptonemal complex, so Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q113_85536f1e_13112026.png?v=85536f1eeaf1)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q113_605a8ef4_13112026.png?v=605a8ef4f9ea)

---

## Q114

Biology · botany · Cell Cycle and Cell Division

Spindle fibers attach to kinetochores of chromosomes during

- (1) Prophase
- **(2)** Metaphase
- (3) Anaphase
- (4) Telophase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spindle fibers attach to kinetochores of chromosome in metaphase stage.

**Solved independently** (answer withheld)

1. NCERT (Cell Cycle and Cell Division) states that the complete disintegration of the nuclear envelope marks the start of metaphase, when spindle fibres attach to the kinetochores of chromosomes, so the answer is option $2$ (Metaphase).

**Subtopic:** Prophase and Metaphase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q114_f963303a_13112026.png?v=f963303a0a24)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q114_c6c1de14_13112026.png?v=c6c1de140db5)

---

## Q115

Biology · botany · Biotechnology: Principles and Processes

What is the fate of a piece of DNA carrying only gene of interest which is transferred into an alien organism? Choose the correct answer from the options given below:

- (A) The piece of DNA would be able to multiply itself independently in the progeny cells of the organism.
- (B) It may get integrated into the genome of the recipient.
- (C) It may multiply and be inherited along with the host DNA.
- (D) The alien piece of DNA is not an integral part of chromosome.
- (E) It shows ability to replicate.

- (1) A and B only
- (2) D and E only
- **(3)** B and C only
- (4) A and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because
2. The fate of a piece of DNA carrying only gene of interest which is transferred into an alien organism are:
3. (B) It may get integrated into the genome of the recipient
4. (C) It may multiply and be inherited along with the host DNA
5. $\Rightarrow$ This piece of DNA would not be able to multiply itself in the progeny cells of the organism but when gets integrated into the genome of the recipient, it may multiply and be inherited along with the host DNA.

**Solved independently** (answer withheld)

1. A piece of DNA with only the gene of interest has no origin of replication ($ori$), so it cannot replicate on its own: statements $A$ and $E$ are false.
2. Such alien DNA may get integrated into the recipient genome: statement $B$ is true.
3. Once integrated, it multiplies and is inherited along with the host DNA: statement $C$ is true, and $D$ (not an integral part of the chromosome) is false.
4. So the correct set is $B$ and $C$ only, which is option $3$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 51)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q115_3b51fa10_13112026.png?v=3b51fa10c91c)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q115_20625f10_13112026.png?v=20625f100c4f)

---

## Q116

Biology · botany · Molecular Basis of Inheritance

The lactose present in the growth medium of bacteria is transported to the cell by the action of

- (1) Beta-galactosidase
- (2) Acetylase
- **(3)** Permease
- (4) Polymerase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The $y$ gene $lac$ operon codes for permease enzyme, which increase the permeability of cell to $\beta$-galactosides.
2. So, the lactose present in the growth medium of bacteria is transported into the cell by the action of permease.

**Solved independently** (answer withheld)

1. In the $lac$ operon, the $y$ gene codes for permease, which raises the cell's permeability to $\beta$-galactosides and so carries lactose into the cell; this is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 52)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q116_bd03659f_13112026.png?v=bd03659f9596)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q116_d314e589_13112026.png?v=d314e5899f50)

---

## Q117

Biology · botany · Anatomy of Flowering Plants

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Parenchyma is living but collenchyma is dead tissue.
- (Statement II) Gymnosperms lack xylem vessels but presence of xylem vessels is the characteristic of angiosperms.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- **(4)** Statement I is false but Statement II is true

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Collenchyma is also living tissue.
2. Gymnosperm lack xylem vessels but presence of xylem vessels is the characteristic of angiosperm.

**Solved independently** (answer withheld)

1. Parenchyma and collenchyma are both living simple tissues (only sclerenchyma is dead), so Statement I is false.
2. Per NCERT, gymnosperms lack vessels in their xylem, and the presence of vessels is a characteristic feature of angiosperms, so Statement II is true.
3. Statement I false and Statement II true matches option $4$.

**Subtopic:** Permanent Tissue, Complex Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q117_7cbc171d_13112026.png?v=7cbc171d73c4)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q117_1a6ed69a_13112026.png?v=1a6ed69a90e8)

---

## Q118

Biology · botany · Biological Classification

Which one of the following is not a criterion for classification of fungi?

- (1) Morphology of mycelium
- **(2)** Mode of nutrition
- (3) Mode of spore formation
- (4) Fruiting body

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The morphology of the mycelium, mode of spore formation and fruiting bodies form the basis for the division of the kingdom fungi into various classes.

**Solved independently** (answer withheld)

1. NCERT states fungi are divided into classes based on morphology of the mycelium, mode of spore formation and fruiting bodies, so mode of nutrition (option $2$) is not a criterion.

**Subtopic:** Kingdom Fungi · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q118_0a98d288_13112026.png?v=0a98d288c542)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q118_72e28d46_13112026.png?v=72e28d46e07c)

---

## Q119

Biology · botany · Principles of Inheritance and Variation

In a plant, black seed color (BB/Bb) is dominant over white seed color (bb). In order to find out the genotype of the black seed plant, with which of the following genotype will you cross it?

- (1) BB
- **(2)** bb
- (3) Bb
- (4) BB/Bb

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. To determine the genotype of a black seed colour at $\mathrm{F_2}$, the black seed from $\mathrm{F_2}$ is crossed with the white seed colour. This is called a test cross.
2. $\therefore$ To determine the genotype of (BB/Bb) black seed we need to cross them with white seed i.e. bb.

**Solved independently** (answer withheld)

1. To find an unknown dominant genotype, perform a test cross with the homozygous recessive parent, $bb$.
2. If the plant is $BB$: $BB \times bb \rightarrow$ all $Bb$ (black seeds).
3. If the plant is $Bb$: $Bb \times bb \rightarrow 1\,Bb : 1\,bb$ (black : white), so the cross is with $bb$, option $2$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q119_f8812208_13112026.png?v=f88122080e49)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q119_76046386_13112026.png?v=760463867b71)

---

## Q120

Biology · botany · Biodiversity and Conservation

Tropical regions show greatest level of species richness because
Choose the correct answer from the options given below.

- (A) Tropical latitudes have remained relatively undisturbed for millions of years, hence more time was available for species diversification.
- (B) Tropical environments are more seasonal.
- (C) More solar energy is available in tropics.
- (D) Constant environments promote niche specialization.
- (E) Tropical environments are constant and predictable.

- **(1)** A, C, D and E only
- (2) A and B only
- (3) A, B and E only
- (4) A, B and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Only statement B is incorrect because tropical environments unlike temperate ones, are less seasonal, relatively more constant and predictable.
2. Thus statements A, C, D and E are correct.

**Solved independently** (answer withheld)

1. A is true: tropical latitudes stayed relatively undisturbed for millions of years, giving more time for diversification.
2. B is false: tropical environments are less seasonal, not more.
3. C is true: more solar energy is available in the tropics, supporting higher productivity.
4. D is true: constant environments promote niche specialization.
5. E is true: tropical environments are relatively constant and predictable.
6. True set is $\{A, C, D, E\}$, which is option $1$.

**Subtopic:** Latitudinal Gradients · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 53)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q120_a5ddc9a1_13112026.png?v=a5ddc9a14d69)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q120_0275bdef_13112026.png?v=0275bdefeeb0)

---

## Q121

Biology · botany · Biodiversity and Conservation

These are regarded as major causes of biodiversity loss: Choose the correct option:

- (A) Over exploitation
- (B) Co-extinction
- (C) Mutation
- (D) Habitat loss and fragmentation
- (E) Migration

- (1) A, C and D only
- (2) A, B, C and D only
- (3) A, B and E only
- **(4)** A, B and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Major causes of biodiversity losses are
2. (1) Habitat loss and fragmentation
3. (2) Over-exploitation
4. (3) Alien species invasions
5. (4) Co-extinctions
6. Hence correct option is A, B and D only.

**Solved independently** (answer withheld)

1. NCERT lists the four major causes of biodiversity loss (the 'Evil Quartet') as habitat loss and fragmentation, over-exploitation, alien species invasions and co-extinctions, so $A$, $B$ and $D$ are causes while mutation ($C$) and migration ($E$) are not, giving option $4$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q121_e6b64d19_13112026.png?v=e6b64d196c54)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q121_acf0ea25_13112026.png?v=acf0ea25a09d)

---

## Q122

Biology · botany · Molecular Basis of Inheritance

A transcription unit in DNA is defined primarily by the three regions in DNA and these are with respect to upstream and down stream end;

- (1) Repressor, Operator gene, Structural gene
- (2) Structural gene, Transposons, Operator gene
- (3) Inducer, Repressor, Structural gene
- **(4)** Promotor, Structural gene, Terminator

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A transcription unit of DNA is defined primarily by the three regions in the DNA:
2. (i) A promoter
3. (ii) The structural gene
4. (iii) A terminator
5. The promoter is said to be located towards $5'$-end (upstream) of the structural gene (the reference is made with respect to the polarity of coding strand)
6. The terminator is located towards $3'$-end (downstream) of the coding strand.

**Solved independently** (answer withheld)

1. A transcription unit in DNA is defined by three regions: the promoter at the upstream end, the structural gene in the middle, and the terminator at the downstream end, which matches option $4$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q122_077dc480_13112026.png?v=077dc4806363)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q122_1fb1c05c_13112026.png?v=1fb1c05c45b3)

---

## Q123

Biology · botany · Biotechnology: Principles and Processes

Hind II always cuts DNA molecules at a particular point called recognition sequence and it consists of:

- (1) $8\,\mathrm{bp}$
- **(2)** $6\,\mathrm{bp}$
- (3) $4\,\mathrm{bp}$
- (4) $10\,\mathrm{bp}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option $(2)$.
2. The first restriction endonuclease – $\textit{Hin}\mathrm{d}$ II, whose functioning depends on a specific DNA nucleotide sequence was isolated.
3. It was found that $\textit{Hin}\mathrm{d}$ II always cut DNA molecules at a particular point by recognising sequence of six base pairs.
4. Option $(1)$, $(3)$ and $(4)$ are incorrect because they have either more than $6$ or less than $6\,\mathrm{bp}$.

**Solved independently** (answer withheld)

1. Per NCERT, Hind II always cuts DNA at a particular point by recognising a specific sequence of $6$ base pairs, which is option $2$ ($6\,\mathrm{bp}$).

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 54)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q123_b895a9b9_13112026.png?v=b895a9b972b9)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q123_0f294a78_13112026.png?v=0f294a788ff6)

---

## Q124

Biology · botany · Biomolecules

The cofactor of the enzyme carboxypeptidase is:

- **(1)** Zinc
- (2) Niacin
- (3) Flavin
- (4) Haem

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as the cofactor of the enzyme carboxypeptidase is zinc.
2. Niacin is associated with coenzyme NAD and NADP.
3. Option (4) is incorrect as haem is the prosthetic group in peroxidase and catalase.

**Solved independently** (answer withheld)

1. Carboxypeptidase is a proteolytic metalloenzyme whose essential cofactor is the metal ion $\mathrm{Zn^{2+}}$, so the answer is option $1$ (Zinc).

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 54)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q124_fe8ff8bf_13112026.png?v=fe8ff8bffca4)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q124_df05a201_13112026.png?v=df05a201d48c)

---

## Q125

Biology · botany · Microbes in Human Welfare

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Clostridium butylicum | I | Ethanol |
| B | Saccharomyces cerevisiae | II | Streptokinase |
| C | Trichoderma polysporum | III | Butyric acid |
| D | Streptococcus sp. | IV | Cyclosporin-A |

- (1) A-III, B-I, C-II, D-IV
- (2) A-II, B-IV, C-III, D-I
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-IV, B-I, C-III, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. Clostridium butylicum — Butyric acid
2. B. Saccharomyces cerevisiae — Ethanol
3. C. Trichoderma polysporum — Cyclosporin-A
4. D. Streptococcus sp. — Streptokinase

**Solved independently** (answer withheld)

1. $A$: Clostridium butylicum produces butyric acid $\Rightarrow A\text{-}III$; $B$: Saccharomyces cerevisiae produces ethanol $\Rightarrow B\text{-}I$.
2. $C$: Trichoderma polysporum produces cyclosporin-A $\Rightarrow C\text{-}IV$; $D$: Streptococcus produces streptokinase $\Rightarrow D\text{-}II$.
3. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ matches option $3$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 55)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q125_8a8dbd1c_13112026.png?v=8a8dbd1cd534)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q125_fd4cc15a_13112026.png?v=fd4cc15a276d)

---

## Q126

Biology · botany · Biodiversity and Conservation

List of endangered species was released by

- (1) GEAC
- (2) WWF
- (3) FOAM
- **(4)** IUCN

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. List of endangered species was released by – IUCN.

**Solved independently** (answer withheld)

1. The IUCN (International Union for Conservation of Nature) publishes the Red List of threatened species, so the list of endangered species is released by IUCN, option $4$.

**Subtopic:** Loss of Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q126_70200157_13112026.png?v=702001576eff)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q126_d56cb53f_13112026.png?v=d56cb53f8b71)

---

## Q127

Biology · botany · Biodiversity and Conservation

> ⚠ The question describes ex-situ conservation (threatened species taken out of their natural habitat and protected in a special setting), but no option says "ex-situ conservation". The booklet keys "Biodiversity conservation" as the umbrella term, and its own solution names ex-situ conservation "a type of biodiversity conservation". The keyed option is defensible only as the broad category; the precise answer is missing from the options. Same question as 2024_Q3 q110 and 2024_S1 q118. (Carried from 2024_Q2 q117, the same question; option numbers converted to this booklet.)

The type of conservation in which the threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called

- (1) in-situ conservation
- **(2)** Biodiversity conservation
- (3) Semi-conservative method
- (4) Sustainable development

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The type of conservation in which threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called ex-situ conservation which is a type of biodiversity conservation.

**Solved independently** (answer withheld)

1. Taking threatened species out of their natural habitat and protecting them in a special setting is ex-situ conservation.
2. Option $1$ (in-situ) means protection within the natural habitat, so it is wrong; options $4$ and $3$ are unrelated terms.
3. Ex-situ is not offered, so the broad term in option $2$, Biodiversity conservation, is the best available choice.

**Subtopic:** Ex Situ Conservation · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 55)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q127_cea07c8c_13112026.png?v=cea07c8cf4d4)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q127_dc5384f2_13112026.png?v=dc5384f24616)

---

## Q128

Biology · botany · Strategies for Enhancement in Food Production

The capacity to generate a whole plant from any cell of the plant is called:

- **(1)** Totipotency
- (2) Micropropagation
- (3) Differentiation
- (4) Somatic hybridization

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Totipotency is defined as the capacity to generate a whole plant from any cell of the plant.

**Solved independently** (answer withheld)

1. The ability of a single plant cell (explant) to give rise to a whole plant is defined as totipotency, which is option $1$.

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q128_7c35151b_13112026.png?v=7c35151b4a14)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q128_a5ae034c_13112026.png?v=a5ae034c7b06)

---

## Q129

Biology · botany · Organisms and Populations

The equation of Verhulst-Pearl logistic growth is $\frac{dN}{dt} = rN\left[\frac{K-N}{K}\right]$. From this equation, K indicates:

- (1) Intrinsic rate of natural increase
- (2) Biotic potential
- **(3)** Carrying capacity
- (4) Population density

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In the equation $\frac{dN}{dt} = rN\left(\frac{K - N}{K}\right)$, $K$ represents carrying capacity.

**Solved independently** (answer withheld)

1. In $\frac{dN}{dt} = rN\left[\frac{K - N}{K}\right]$, $N$ is population density, $r$ is the intrinsic rate of natural increase and $K$ is the carrying capacity, which is option $3$.

**Subtopic:** Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q129_1a8586cf_13112026.png?v=1a8586cf071a)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q129_f52b9f58_13112026.png?v=f52b9f58aa12)

---

## Q130

Biology · botany · Anatomy of Flowering Plants

Bulliform cells are responsible for

- **(1)** Inward curling of leaves in monocots.
- (2) Protecting the plant from salt stress.
- (3) Increased photosynthesis in monocots.
- (4) Providing large spaces for storage of sugars.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In grasses, certain adaxial epidermal cells along the veins modify themselves into large, empty, colourless cells.
2. These are called bulliform cells.
3. When the bulliform cells in the leaves have absorbed water and are turgid, the leaf surface is exposed.
4. When they are flaccid due to water stress, they make the leaves curl inwards to minimise water loss.

**Solved independently** (answer withheld)

1. Bulliform cells are large, empty, colourless epidermal cells of monocot (grass) leaves; when they become flaccid from water loss the leaf curls inward, which is option $1$.

**Subtopic:** Dicotyledonous and Monocotyledonous Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q130_e6a764f5_13112026.png?v=e6a764f5a726)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q130_bf69a226_13112026.png?v=bf69a22692c0)

---

## Q131

Biology · botany · Biomolecules

Lecithin, a small molecular weight organic compound found in living tissues, is an example of:

- (1) Amino acids
- **(2)** Phospholipids
- (3) Glycerides
- (4) Carbohydrates

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2).
2. Some lipids have phosphorous and a phosphorylated organic compound in them. These are phospholipids.
3. They are found in cell membrane.
4. Lecithin is one example.
5. Option (3) is incorrect as glycerides are another group of lipids in which both glycerol and fatty acids are present.
6. Option (1) and (2) are incorrect as amino acids and carbohydrates are separate groups of biomolecules.

**Solved independently** (answer withheld)

1. Lecithin is a lipid carrying a phosphorylated organic compound (choline), so it is a phospholipid, which is option $2$.

**Subtopic:** Lipids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 56)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q131_f7c96d40_13112026.png?v=f7c96d4018f4)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q131_7b9fab4a_13112026.png?v=7b9fab4a5738)

---

## Q132

Biology · botany · Biomolecules

Inhibition of Succinic dehydrogenase enzyme by malonate is a classical example of:

- (1) Cofactor inhibition
- (2) Feedback inhibition
- **(3)** Competitive inhibition
- (4) Enzyme activation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because malonate shows close structural similarity with the substrate and it competes with the substrate for the substrate binding site of the enzyme succinic dehydrogenase.
2. Option (1), (2) and (4) are incorrect as enzyme activation, co-factor inhibition are not showing structural similarity with substrate.

**Solved independently** (answer withheld)

1. Malonate closely resembles succinate in structure and binds the active site of succinic dehydrogenase in place of the substrate, which is competitive inhibition (option $3$).

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q132_b9192be1_13112026.png?v=b9192be1c36b)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q132_7ae6314b_13112026.png?v=7ae6314be285)

---

## Q133

Biology · botany · Biotechnology and Its Applications

> ⚠ Statement II is false (the protoxin is activated by the ALKALINE pH of the insect gut, not acidic). Statement I says Bt toxins are "coded by a gene cry IAc": the toxins are coded by several cry genes (cryIAc and cryIIAb against cotton bollworms, cryIAb against corn borer), so read strictly it is false and gives option 2; the booklet keys (3), reading it as true. The blind solve chose 4. Same question and same key as 2024_S1 q125 and 2024_Q3 q108. (Carried from 2024_Q2 q102, the same question; option numbers converted to this booklet.)

> ⚠ The independent solve chose (2); the booklet prints (3).

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Bt toxins are insect group specific and coded by a gene cry IAc.
- (Statement II) Bt toxin exists as inactive protoxin in B. thuringiensis. However, after ingestion by the insect the inactive protoxin gets converted into active form due to acidic pH of the insect gut.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (2) · differs

**Publisher's solution**

1. The correct answer is option (3) as specific Bt toxin genes were isolated from Bacillus thuringiensis and incorporated into the several crop plants such as cotton.
2. The choice of genes depends upon the crop and the targeted pest as most Bt toxins are insect-group specific.
3. The toxin is coded by a gene named cry.
4. There are a number of them, for example, the proteins encoded by the genes cry IAc and cry IIAb control the cotton bollworms, that of cry IAb controls corn borer.

**Solved independently** (answer withheld)

1. Bt toxin proteins are coded by several genes named $cry$ (e.g. $cryIAc$, $cryIIAb$ for cotton bollworms, $cryIAb$ for corn borer); they are not coded by the single gene $cryIAc$, so Statement I is false.
2. The Bt toxin exists as an inactive protoxin and is converted to the active toxin by the alkaline pH of the insect gut, not an acidic pH, so Statement II is false.
3. Both statements are false, which is option $2$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 57)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q133_36377f4d_13112026.png?v=36377f4d8ee2)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q133_50bb1ef3_13112026.png?v=50bb1ef3ac3d)

---

## Q134

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the part of the seed from the given figure which is destined to form root when the seed germinates.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q134_3d4be8d8_13112026.png?v=3d4be8d855de)

- (1) A
- (2) B
- **(3)** C
- (4) D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Radicle is destined to form root.
2. In the given diagram ‘C’ represent radicle

**Solved independently** (answer withheld)

1. The figure is a monocot (maize-type) seed in L.S.: endosperm above, embryo axis at the lower side; the upper sheath A is the coleoptile, B is the plumule, C is the radicle inside the lower sheath D (coleorhiza), so the radicle $C$, which forms the root, is option $3$.

**Subtopic:** Embryo and Seed · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 57)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q134_feb9ee20_13112026.png?v=feb9ee2092be)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q134_daf867a7_13112026.png?v=daf867a76f32)

---

## Q135

Biology · botany · Principles of Inheritance and Variation

Which one of the following can be explained on the basis of Mendel's Law of Dominance?
Choose the correct answer from the options given below:

- (A) Out of one pair of factors one is dominant and the other is recessive.
- (B) Alleles do not show any expression and both the characters appear as such in $\mathrm{F_2}$ generation.
- (C) Factors occur in pairs in normal diploid plants.
- (D) The discrete unit controlling a particular character is called factor.
- (E) The expression of only one of the parental characters is found in a monohybrid cross.

- (1) A, B and C only
- **(2)** A, C, D and E only
- (3) B, C and D only
- (4) A, B, C, D and E

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to Law of Dominance
2. (1) Characters are controlled by discrete units called factors
3. (2) Factors occur in pairs
4. (3) In a dissimilar pair of factors one member of the pair dominates (dominant) the other recessive
5. The law of dominance is used to explain the expression of only one of the parental characters in a monohybrid cross.
6. Law of segregation is based on the fact that the alleles do not show any expression and both the characters are recovered as such in $\mathrm{F_2}$ generation

**Solved independently** (answer withheld)

1. Per NCERT, the Law of Dominance states: characters are controlled by discrete units called factors, so $D$ is true.
2. Factors occur in pairs, so $C$ is true.
3. In a dissimilar pair of factors one member dominates (dominant) and the other does not (recessive), so $A$ is true.
4. The law explains expression of only one parental character in the $\mathrm{F_1}$ of a monohybrid cross, so $E$ is true.
5. $B$ (alleles show no expression, both characters appear as such) does not follow from dominance, so $B$ is false.
6. Correct set is $A, C, D$ and $E$ only, which is option $2$.

**Subtopic:** Principles of Laws of Inheritance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q135_91433f3c_13112026.png?v=91433f3ccb82)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q135_8e2989ba_13112026.png?v=8e2989ba2e86)

---

## Q136

Biology · botany · Respiration in Plants

Match List I with List II

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Citric acid cycle | I | Cytoplasm |
| B | Glycolysis | II | Mitochondrial matrix |
| C | Electron transport system | III | Intermembrane space of mitochondria |
| D | Proton gradient | IV | Inner mitochondrial membrane |

- (1) A-I, B-II, C-III, D-IV
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-III, B-IV, C-I, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Citric acid cycle occurs in mitochondrial matrix.
2. Glycolysis occurs in cytosol in most of the organism.
3. Electron transport system is present in the inner mitochondrial membrane.
4. Proton gradient is formed across the intermembrane space of mitochondria.

**Solved independently** (answer withheld)

1. Citric acid cycle (A) occurs in the mitochondrial matrix, so $A \rightarrow II$.
2. Glycolysis (B) occurs in the cytoplasm, so $B \rightarrow I$.
3. Electron transport system (C) is located in the inner mitochondrial membrane, so $C \rightarrow IV$.
4. Protons are pumped into the intermembrane space, creating the proton gradient there, so $D \rightarrow III$.
5. $A$-II, $B$-I, $C$-IV, $D$-III matches option $2$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle, Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 58)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q136_87b2d87b_13112026.png?v=87b2d87b7919)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q136_0d1ddff4_13112026.png?v=0d1ddff4d663)

---

## Q137

Biology · botany · Biodiversity and Conservation

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Robert May | I | Species-Area relationship |
| B | Alexander von Humboldt | II | Long term ecosystem experiment using out door plots |
| C | Paul Ehrlich | III | Global species diversity at about 7 million |
| D | David Tilman | IV | Rivet popper hypothesis |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-III, B-I, C-IV, D-II
- (3) A-I, B-III, C-II, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Robert May places the global species diversity at about 7 million.
2. Alexander von Humboldt gave species-area relationship.
3. Paul Ehrlich used an analogy “Rivet popper hypothesis” to explain the role of species in the ecosystem.
4. David Tilman performed long term ecosystem experiments using out door plots.

**Solved independently** (answer withheld)

1. Robert May estimated global species diversity at about $7$ million, so A-III.
2. Alexander von Humboldt described the species-area relationship, so B-I.
3. Paul Ehrlich proposed the rivet popper hypothesis, so C-IV.
4. David Tilman conducted long-term ecosystem experiments using outdoor plots, so D-II.
5. A-III, B-I, C-IV, D-II matches option $2$.

**Subtopic:** The Importance of Species Diversity to the Ecosystem, Species–Area Relationships · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 59)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q137_34d30049_13112026.png?v=34d300498411)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q137_c8761d02_13112026.png?v=c8761d0262b5)

---

## Q138

Biology · botany · Ecosystem

> ⚠ The question asks for the GPP (Gross Primary Productivity) of the THIRD trophic level, but primary productivity is defined only for producers (the first level). Read as "energy reaching level 3" with the 10% rule, 100x gives 10x at level 2 and x at level 3 (option 2); the booklet keys 10x (option 3), reading it as what level 3 takes in from level 2. Same question as 2024_S1 q147 and 2024_Q3 q143. (Carried from 2024_Q2 q141, the same question; option numbers converted to this booklet.)

> ⚠ The independent solve chose (2); the booklet prints (3).

In an ecosystem if the Net Primary Productivity (NPP) of first trophic level is $100x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, what would be the GPP (Gross Primary Productivity) of the third trophic level of the same ecosystem?

- (1) $\frac{x}{10}\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- (2) $x\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- **(3)** $10x\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- (4) $\frac{100x}{3x}\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$

**Answer** — booklet: (3) · independent solve: (2) · differs

**Publisher's solution**

1. NPP at first trophic level would be the GPP for second trophic level.
2. NPP at second trophic level would be GPP for third trophic level.
3. Therefore, $100x\,(\mathrm{kcal/m^{2}/yr})$ would be GPP at second trophic level and $100x \times 10\%\,(\mathrm{kcal/m^{2}/yr})$ \textit{i.e.}, $10x\,(\mathrm{kcal/m^{2}/yr})$ energy would be GPP at third trophic level.

**Solved independently** (answer withheld)

1. Apply the 10% law: only about $10\%$ of energy at one trophic level is transferred to the next.
2. Energy reaching the second trophic level $= 0.1 \times 100x = 10x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$.
3. Energy reaching the third trophic level $= 0.1 \times 10x = x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, which is option $2$.

**Subtopic:** Energy Flow, Productivity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q138_d546ee63_13112026.png?v=d546ee63d2bd)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q138_e8cbf711_13112026.png?v=e8cbf7113aa9)

---

## Q139

Biology · botany · Plant Kingdom

Read the following statements and choose the set of correct statements: In the members of Phaeophyceae, Choose the correct answer from the options given below:

- (A) Asexual reproduction occurs usually by biflagellate zoospores.
- (B) Sexual reproduction is by oogamous method only.
- (C) Stored food is in the form of carbohydrates which is either mannitol or laminarin.
- (D) The major pigments found are chlorophyll a, c and carotenoids and xanthophyll.
- (E) Vegetative cells have a cellulosic wall, usually covered on the outside by gelatinous coating of algin.

- (1) A, B, C and D only
- (2) B, C, D and E only
- **(3)** A, C, D and E only
- (4) A, B, C and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In members of Phaeophyceae sexual reproduction is by oogamous, isogamous or anisogamous methods.
2. Therefore correct set of statements are A, C, D and E.

**Solved independently** (answer withheld)

1. A: asexual reproduction in brown algae is usually by pear-shaped biflagellate zoospores, so A is true.
2. B: sexual reproduction may be isogamous, anisogamous or oogamous, so 'oogamous only' makes B false.
3. C: reserve food is complex carbohydrate as laminarin or mannitol, so C is true.
4. D: pigments are chlorophyll $a$, $c$, carotenoids and xanthophylls (fucoxanthin), so D is true.
5. E: the cellulosic wall is usually covered outside by a gelatinous coating of algin, so E is true.
6. Correct set is A, C, D and E only, which is option $3$.

**Subtopic:** Phaeophyceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q139_3f84f373_13112026.png?v=3f84f373cce7)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q139_d47160dd_13112026.png?v=d47160ddfdd7)

---

## Q140

Biology · botany · Plant Growth and Development

Spraying sugarcane crop with which of the following plant growth regulators, increases the length of stem, thus, increasing the yield?

- (1) Auxin
- **(2)** Gibberellin
- (3) Cytokinin
- (4) Abscisic acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sugarcanes store carbohydrate as sugar in their stems.
2. Spraying sugarcane crop with gibberellins increases the length of the stem, thus increasing the yield.

**Solved independently** (answer withheld)

1. Spraying sugarcane with gibberellins elongates the stem (internodes), raising the yield, so the answer is option $2$ (Gibberellin).

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q140_2941c0fe_13112026.png?v=2941c0fe0376)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q140_f1379cf0_13112026.png?v=f1379cf09534)

---

## Q141

Biology · botany · Morphology of Flowering Plants

Match List I with List II
List I (Types of Stamens) | List II (Example)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Monoadelphous | I | Citrus |
| B | Diadelphous | II | Pea |
| C | Polyadelphous | III | Lily |
| D | Epiphyllous | IV | China-rose |

- **(1)** A-IV, B-II, C-I, D-III
- (2) A-IV, B-I, C-II, D-III
- (3) A-I, B-II, C-IV, D-III
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In China rose monoadelphous androecium is present.
2. Diadelphous androecium is found in pea plant.
3. Polyadelphous androecium is found in citrus.
4. Epiphyllous androecium is found in lily.

**Solved independently** (answer withheld)

1. Monoadelphous stamens (one bundle) occur in China-rose, so $A \rightarrow IV$.
2. Diadelphous stamens (two bundles) occur in pea, so $B \rightarrow II$.
3. Polyadelphous stamens (more than two bundles) occur in Citrus, so $C \rightarrow I$.
4. Epiphyllous stamens (attached to perianth) occur in lily, so $D \rightarrow III$.
5. $A$-IV, $B$-II, $C$-I, $D$-III matches option $1$.

**Subtopic:** Androecium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q141_012f9b9b_13112026.png?v=012f9b9ba747)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q141_fa33945f_13112026.png?v=fa33945f9c83)

---

## Q142

Biology · botany · Molecular Basis of Inheritance

Which of the following statement is correct regarding the process of replication in \textit{E.coli}?

- (1) The DNA dependent DNA polymerase catalyses polymerization in one direction that is $3' \rightarrow 5'$
- (2) The DNA dependent RNA polymerase catalyses polymerization in one direction, that is $5' \rightarrow 3'$
- (3) The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ as well as $3' \rightarrow 5'$ direction
- **(4)** The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ direction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In Prokaryotes, like \textit{E.coli} during replication, the DNA dependent DNA polymerase catalyse polymerization only in one direction, that is $5' \rightarrow 3'$

**Solved independently** (answer withheld)

1. DNA replication in \textit{E. coli} is catalysed by DNA-dependent DNA polymerase, which adds nucleotides only in the $5' \rightarrow 3'$ direction, so option $4$ is correct; options $1$ and $3$ give wrong directions and option $2$ names the transcription enzyme.

**Subtopic:** The Machinery and the Enzymes of Replication · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 60)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q142_1c9c9a32_13112026.png?v=1c9c9a3220b7)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q142_2ee4c4ff_13112026.png?v=2ee4c4ff9d88)

---

## Q143

Biology · botany · Respiration in Plants

Identify the step in tricarboxylic acid cycle, which does not involve oxidation of substrate.

- (1) Malic acid $\rightarrow$ Oxaloacetic acid
- (2) Succinic acid $\rightarrow$ Malic acid
- **(3)** Succinyl-CoA $\rightarrow$ Succinic acid
- (4) Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Oxidation involves the loss of electrons (often as part of hydrogen) from a molecule, leaving to an increase in its oxidation state.
2. This process is typically associated with the transfer of electrons to an electron acceptor which is reduced in the process.
3. The conversion of succinyl CoA to succinic acid does not involve oxidation of substrate.

**Solved independently** (answer withheld)

1. Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid is an oxidative decarboxylation producing $NADH + H^+$, so it is an oxidation.
2. Malic acid $\rightarrow$ Oxaloacetic acid is a dehydrogenation producing $NADH + H^+$, so it is an oxidation.
3. Succinic acid $\rightarrow$ Malic acid (via fumarate) involves the dehydrogenation producing $FADH_2$, so it is an oxidation.
4. Succinyl-CoA $\rightarrow$ Succinic acid releases CoA and forms $GTP$ (substrate-level phosphorylation) with no electron carrier reduced, so it is not an oxidation: option $3$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 61)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q143_5bc45ef9_13112026.png?v=5bc45ef93c8d)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q143_1b33c9fa_13112026.png?v=1b33c9fa831e)

---

## Q144

Biology · botany · Molecular Basis of Inheritance

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Frederick Griffith | I | Genetic code |
| B | Francois Jacob & Jacque Monod | II | Semi-conservative mode of DNA replication |
| C | Har Gobind Khorana | III | Transformation |
| D | Meselson & Stahl | IV | *Lac* operon |

- (1) A-III, B-II, C-I, D-IV
- **(2)** A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-IV, D-I
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Frederick Griffith series of experiment witness miraculous transformation in the bacteria.
2. The elucidation of *Lac* operon was a result of a close association between geneticist, Francois Jacob and a biochemist, Jacques Monod.
3. Meselson and Stahl gave semi-conservative mode of DNA replication.
4. Har Gobind Khorana developed chemical method to define combination of bases in genetic code.

**Solved independently** (answer withheld)

1. Griffith discovered transformation ($A \to III$), Jacob and Monod proposed the lac operon ($B \to IV$), Khorana helped decipher the genetic code ($C \to I$), and Meselson and Stahl proved semi-conservative DNA replication ($D \to II$), so the match is option $2$.

**Subtopic:** The Lac Operon, Experimental Proof that DNA is Semiconservative · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 61)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q144_a3ab13a6_13112026.png?v=a3ab13a6e6aa)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q144_b0468b11_13112026.png?v=b0468b114075)

---

## Q145

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the correct description about the given figure:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q145_020c99c7_13112026.png?v=020c99c7651d)

- **(1)** Wind pollinated plant inflorescence showing flowers with well exposed stamens.
- (2) Water pollinated flowers showing stamens with mucilaginous covering.
- (3) Cleistogamous flowers showing autogamy.
- (4) Compact inflorescence showing complete autogamy

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The given diagram shows a wind pollinated plant showing compact inflorescence and well exposed stamens.
2. Stamens are exposed so complete autogamy does not occur.

**Solved independently** (answer withheld)

1. The figure shows a compact elongated inflorescence axis with numerous long filaments bearing anthers hanging freely on all sides, i.e. well-exposed stamens; this is the adaptation of wind-pollinated plants for easy dispersal of pollen by air currents, so the description is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q145_2abf3f94_13112026.png?v=2abf3f947647)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q145_453b7a4f_13112026.png?v=453b7a4f1c8f)

---

## Q146

Biology · botany · Cell: The Unit of Life

The DNA present in chloroplast is:

- (1) Linear, double stranded
- **(2)** Circular, double stranded
- (3) Linear, single stranded
- (4) Circular, single stranded

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The DNA present in chloroplast is circular double stranded.

**Solved independently** (answer withheld)

1. Chloroplast DNA, like prokaryotic DNA, is a naked, circular, double-stranded molecule, which is option $2$.

**Subtopic:** Plastids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 62)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q146_88586d53_13112026.png?v=88586d5349d2)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q146_3fe10eba_13112026.png?v=3fe10ebaf6ed)

---

## Q147

Biology · botany · Photosynthesis in Higher Plants

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) In $\mathrm{C_3}$ plants, some $\mathrm{O_2}$ binds to RuBisCO, hence $\mathrm{CO_2}$ fixation is decreased.
- (Statement II) In $\mathrm{C_4}$ plants, mesophyll cells show very little photorespiration while bundle sheath cells do not show photorespiration.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In $\mathrm{C_3}$ plant, some $\mathrm{O_2}$ bind to RuBisCO, and hence $\mathrm{CO_2}$ fixation is decreased.
2. Statement II is incorrect, photorespiration does not occur in $\mathrm{C_4}$ plants as they lack RuBisCO in mesophyll.
3. Hence statement I is the only correct option.

**Solved independently** (answer withheld)

1. In $\mathrm{C_3}$ plants RuBisCO also binds $\mathrm{O_2}$ (oxygenase activity), causing photorespiration and lowering $\mathrm{CO_2}$ fixation, so Statement I is true.
2. In $\mathrm{C_4}$ plants mesophyll cells fix $\mathrm{CO_2}$ with PEP carboxylase and lack RuBisCO, so they cannot photorespire at all; the claim of 'very little photorespiration' there is wrong, so Statement II is false.
3. Statement I true, Statement II false, which is option $3$.

**Subtopic:** Photorespiration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 62)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q147_8f8a5bc3_13112026.png?v=8f8a5bc3ac3f)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q147_4eefebe7_13112026.png?v=4eefebe7a224)

---

## Q148

Biology · botany · Biomolecules

Match List-I with List-II
Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | GLUT-4 | I | Hormone |
| B | Insulin | II | Enzyme |
| C | Trypsin | III | Intercellular ground substance |
| D | Collagen | IV | Enables glucose transport into cells |

- **(1)** A-IV, B-I, C-II, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-II, B-III, C-IV, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1)
2. A. GLUT-4 — IV. Enables glucose transport into cells
3. B. Insulin — I. Hormone
4. C. Trypsin — II. Enzyme
5. D. Collagen — III. Intercellular ground substance

**Solved independently** (answer withheld)

1. $\text{GLUT-4}$ is a transporter that enables glucose transport into cells, so $A \to IV$.
2. Insulin is a peptide hormone, so $B \to I$.
3. Trypsin is a digestive enzyme, so $C \to II$.
4. Collagen is a protein of the intercellular ground substance, so $D \to III$.
5. $A\text{-}IV,\ B\text{-}I,\ C\text{-}II,\ D\text{-}III$ matches option $1$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q148_4feb18a5_13112026.png?v=4feb18a55ff2)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q148_8ed830d9_13112026.png?v=8ed830d901b0)

---

## Q149

Biology · botany · Morphology of Flowering Plants

Match List I with List II
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Rose | I | Twisted aestivation |
| B | Pea | II | Perigynous flower |
| C | Cotton | III | Drupe |
| D | Mango | IV | Marginal placentation |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Rose have half-inferior ovary, thus it is known as Perigynous flower.
2. In Pea, the placenta form a ridge along the ventral suture of the ovary and ovules are borne on this ridge forming two rows.
3. In Cotton, twisted aestivation is present.
4. In Mango, fruit is drupe.

**Solved independently** (answer withheld)

1. Rose (A) has a perigynous flower (hypanthium), so $A \to II$.
2. Pea (B) has marginal placentation (monocarpellary ovary), so $B \to IV$.
3. Cotton (C) shows twisted aestivation, so $C \to I$.
4. Mango (D) fruit is a drupe, so $D \to III$.
5. $A$-II, $B$-IV, $C$-I, $D$-III matches option $1$.

**Subtopic:** The Flower, The Fruit · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q149_ee6a5dca_13112026.png?v=ee6a5dca3c44)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q149_c17612eb_13112026.png?v=c17612eb79e0)

---

## Q150

Biology · botany · Strategies for Enhancement in Food Production

Which of the following are fused in somatic hybridization involving two varieties of plants?

- (1) Callus
- (2) Somatic embryos
- **(3)** Protoplasts
- (4) Pollens

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Protoplast of two varieties of plants are fused in somatic hybridization.

**Solved independently** (answer withheld)

1. In somatic hybridization, cell walls are digested away and the isolated protoplasts of two varieties are fused to give a somatic hybrid, so the answer is option $3$ (Protoplasts).

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q150_1fc0e4c9_13112026.png?v=1fc0e4c9eb75)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q150_d0816d6b_13112026.png?v=d0816d6be347)

---

## Q151

Biology · zoology · Animal Kingdom

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pleurobrachia | I | Mollusca |
| B | Radula | II | Ctenophora |
| C | Stomochord | III | Osteichthyes |
| D | Air bladder | IV | Hemichordata |

- (1) A-IV, B-II, C-III, D-I
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-II, B-IV, C-I, D-III
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. A. Pleurobrachia – is a member of phylum Ctenophora.
3. B. Radula – is a rasping feeding organ present in phylum Mollusca.
4. C. Stomochord – Rudimentary structure similar to notochord found in the collar region of members of phylum Hemichordata.
5. D. Air bladder – is found in Osteichthyes which provides them buoyancy.

**Solved independently** (answer withheld)

1. Pleurobrachia is a comb jelly, so $A \rightarrow II$ (Ctenophora).
2. Radula is the file-like rasping feeding organ of molluscs, so $B \rightarrow I$ (Mollusca).
3. Stomochord is the rudimentary notochord-like structure in the proboscis of hemichordates, so $C \rightarrow IV$ (Hemichordata).
4. Air bladder regulates buoyancy in bony fishes, so $D \rightarrow III$ (Osteichthyes).
5. $A\text{-}II, B\text{-}I, C\text{-}IV, D\text{-}III$ matches option $2$.

**Subtopic:** Classification of Animals · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 64)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q151_9176ff30_13112026.png?v=9176ff3036a1)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q151_f1d66d9b_13112026.png?v=f1d66d9b3dcb)

---

## Q152

Biology · zoology · Cell Cycle and Cell Division

Following are the stages of cell division : Choose the correct sequence of stages from the options given below :

- (A) Gap 2 phase
- (B) Cytokinesis
- (C) Synthesis phase
- (D) Karyokinesis
- (E) Gap 1 phase

- (1) C-E-D-A-B
- (2) E-B-D-A-C
- (3) B-D-E-A-C
- **(4)** E-C-A-D-B

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct sequence of stages of cell division is
2. Gap 1 phase (E) $\rightarrow$ Synthesis phase (C) $\rightarrow$ Gap 2 phase (A)
3. $\rightarrow$ Karyokinesis (D) $\rightarrow$ Cytokinesis (B)
4. The correct sequence will be $\rightarrow \mathrm{E} \rightarrow \mathrm{C} \rightarrow \mathrm{A} \rightarrow \mathrm{D} \rightarrow \mathrm{B}$

**Solved independently** (answer withheld)

1. Interphase runs in the order $G_1 \rightarrow S \rightarrow G_2$, i.e. $E \rightarrow C \rightarrow A$.
2. The M phase follows: karyokinesis (nuclear division, $D$) comes before cytokinesis (cytoplasmic division, $B$).
3. Full sequence $E-C-A-D-B$, which is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q152_ef320418_13112026.png?v=ef320418e9ea)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q152_bc3ea216_13112026.png?v=bc3ea21661b8)

---

## Q153

Biology · zoology · Human Health and Disease

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Common cold | I | Plasmodium |
| B | Haemozoin | II | Typhoid |
| C | Widal test | III | Rhinoviruses |
| D | Allergy | IV | Dust mites |

- (1) A-II, B-IV, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- **(3)** A-III, B-I, C-II, D-IV
- (4) A-IV, B-II, C-III, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because
2. Common cold is caused by Rhinoviruses
3. Haemozoin is released in blood due to ruptured RBCs after Plasmodium infection.
4. Widal test is used to confirm the typhoid fever.
5. Allergy is caused due to dust mites.

**Solved independently** (answer withheld)

1. Common cold is caused by Rhinoviruses, so $A \to III$.
2. Haemozoin is the toxin released by Plasmodium, so $B \to I$.
3. Widal test confirms typhoid, so $C \to II$.
4. Dust mites are a common allergen, so $D \to IV$.
5. $A\text{-}III, B\text{-}I, C\text{-}II, D\text{-}IV$ is option $3$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 65)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q153_74b9a82f_13112026.png?v=74b9a82ff8d6)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q153_80792168_13112026.png?v=807921684e50)

---

## Q154

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Typhoid | I | Fungus |
| B | Leishmaniasis | II | Nematode |
| C | Ringworm | III | Protozoa |
| D | Filariasis | IV | Bacteria |

- (1) A-I, B-III, C-II, D-IV
- **(2)** A-IV, B-III, C-I, D-II
- (3) A-III, B-I, C-IV, D-II
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. Typhoid – Caused by Salmonella typhimurium (Bacteria)
3. Leishmaniasis – Caused by protozoan i.e., Leishmania donovani
4. Ringworm – Caused by fungi belonging to the genera Microsporum, Trichophyton and Epidermophyton
5. Filariasis – Caused by Wuchereria bancrofti and Wuchereria malayi (Nematode)

**Solved independently** (answer withheld)

1. Typhoid is caused by the bacterium $Salmonella\ typhi$, so A-IV.
2. Leishmaniasis is caused by the protozoan $Leishmania$, so B-III.
3. Ringworm is caused by fungi ($Microsporum$, $Trichophyton$, $Epidermophyton$), so C-I.
4. Filariasis is caused by the nematodes $Wuchereria$ ($W.\ bancrofti$, $W.\ malayi$), so D-II.
5. The match A-IV, B-III, C-I, D-II is option $2$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q154_90163656_13112026.png?v=90163656bdcc)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q154_b3985250_13112026.png?v=b39852506481)

---

## Q155

Biology · zoology · Evolution

The flippers of the Penguins and Dolphins are the example of the

- (1) Adaptive radiation
- (2) Natural selection
- **(3)** Convergent evolution
- (4) Divergent evolution

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3), because the flippers of the Penguins and Dolphins perform similar function but they are not anatomically similar structures.
2. This is example of analogous structures.
3. Option (1) is incorrect as adaptive radiation is the process of evolution of different species in a given geographical area starting from a point and literally radiating to the other areas of geography.
4. Option (2) is incorrect as natural selection is a key mechanism of evolution.
5. Option (4) is incorrect as divergent evolution results in the formation of homologous structures.

**Solved independently** (answer withheld)

1. Penguin flippers (modified bird wings) and dolphin flippers (modified mammal forelimbs) do the same job, swimming, but come from different lineages, so they are analogous structures, which show convergent evolution: option $3$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q155_cc3b435d_13112026.png?v=cc3b435d706a)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q155_947014d9_13112026.png?v=947014d977e4)

---

## Q156

Biology · zoology · Body Fluids and Circulation

Following are the stages of pathway for conduction of an action potential through the heart
Choose the correct sequence of pathway from the options given below

- (A) AV bundle
- (B) Purkinje fibres
- (C) AV node
- (D) Bundle branches
- (E) SA node

- **(1)** E-C-A-D-B
- (2) A-E-C-B-D
- (3) B-D-E-C-A
- (4) E-A-D-B-C

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1) because the correct pathway of conduction of action potential is
2. SA $\rightarrow$ AV node $\rightarrow$ AV bundle $\rightarrow$ Bundle branches $\rightarrow$ Purkinje fibres

**Solved independently** (answer withheld)

1. The action potential originates at the SA node ($E$), passes to the AV node ($C$), then the AV bundle ($A$), the bundle branches ($D$) and the Purkinje fibres ($B$), giving $E\text{-}C\text{-}A\text{-}D\text{-}B$, which is option $1$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q156_56bec159_13112026.png?v=56bec159259d)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q156_15946d99_13112026.png?v=15946d99422b)

---

## Q157

Biology · zoology · Biotechnology: Principles and Processes

Which of the following statements is incorrect?

- (1) A bio-reactor provides optimal growth conditions for achieving the desired product
- (2) Most commonly used bio-reactors are of stirring type
- **(3)** Bio-reactors are used to produce small scale bacterial cultures
- (4) Bio-reactors have an agitator system, an oxygen delivery system and foam control system

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3)
2. The statement (3) is incorrect because bioreactors are used for processing of large volumes ($100$ – $1000$ litres) of culture.
3. Small volume cultures cannot yield appreciable quantities of products.
4. To produce in large quantities the development of bioreactors is required.

**Solved independently** (answer withheld)

1. Bioreactors are large vessels (about $100$ to $1000$ litres) in which raw materials are biologically converted to products, so they are used for large-scale, not small-scale, cultures; statement $4$ is incorrect while statements $1$, $2$ and $3$ are correct, giving option $3$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 66)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q157_41266856_13112026.png?v=412668565caa)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q157_378e2223_13112026.png?v=378e2223923f)

---

## Q158

Biology · zoology · Human Reproduction

Which of the following is not a component of Fallopian tube?

- **(1)** Uterine fundus
- (2) Isthmus
- (3) Infundibulum
- (4) Ampulla

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as uterine fundus is the upper, dome-shaped part of the uterus, above the opening of fallopian tubes.
2. Option (2) is incorrect as isthmus is the last and narrow part of the oviduct that links to the uterus.
3. Option (3) is incorrect as infundibulum is the part of oviduct which is closer to the ovary.
4. Option (4) is incorrect as ampulla is the wider part of the oviduct.

**Solved independently** (answer withheld)

1. The Fallopian tube (oviduct) has three parts: infundibulum (with fimbriae), ampulla and isthmus; the uterine fundus is the upper dome of the uterus, so option $1$ is not a component.

**Subtopic:** The Female Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q158_45dbbe6f_13112026.png?v=45dbbe6f50d9)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q158_8fc6e763_13112026.png?v=8fc6e7631891)

---

## Q159

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements : In the light of the above statements, choose the correct answer from the option given below :

- (Statement I) In the nephron, the descending limb of loop of Henle is impermeable to water and permeable to electrolytes.
- (Statement II) The proximal convoluted tubule is lined by simple columnar brush border epithelium and increases the surface area for reabsorption.

- (1) Both Statement I and Statement II are true
- **(2)** Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2) because
2. Statement I is false as the descending limb of loop of Henle is permeable to water and almost impermeable to electrolytes.
3. Statement II is false as proximal convoluted tubule is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption.

**Solved independently** (answer withheld)

1. Statement I: NCERT states the descending limb of loop of Henle is permeable to water but almost impermeable to electrolytes, so Statement I (impermeable to water, permeable to electrolytes) is false.
2. Statement II: NCERT states the PCT is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption; the statement says simple columnar, so Statement II is false.
3. Both statements are false, which is option $2$.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 67)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q159_25e712d7_13112026.png?v=25e712d7ec41)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q159_9f248789_13112026.png?v=9f248789cc49)

---

## Q160

Biology · zoology · Evolution

Which one of the following factors will not affect the Hardy-Weinberg equilibrium?

- (1) Genetic recombination
- (2) Genetic drift
- (3) Gene migration
- **(4)** Constant gene pool

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as a constant gene pool will not disturb the Hardy-Weinberg equilibrium.
2. Option (1), (2) & (3) will affect the equilibrium leading to evolution.

**Solved independently** (answer withheld)

1. NCERT lists five factors affecting Hardy-Weinberg equilibrium: gene migration (gene flow), genetic drift, mutation, genetic recombination and natural selection; a constant gene pool is the equilibrium state itself, so option $4$ does not affect it.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q160_fc50e54a_13112026.png?v=fc50e54ae629)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q160_99d145ee_13112026.png?v=99d145ee2ded)

---

## Q161

Biology · zoology · Chemical Coordination and Integration

Which of the following is not a steroid hormone?

- (1) Cortisol
- (2) Testosterone
- (3) Progesterone
- **(4)** Glucagon

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as glucagon is a proteinaceous hormone secreted from pancreas.
2. Options (1), (2) and (3) are not correct as they are steroid in nature.

**Solved independently** (answer withheld)

1. Glucagon is a peptide (polypeptide) hormone secreted by the $\alpha$-cells of the islets of Langerhans, whereas cortisol, testosterone and progesterone are cholesterol-derived steroid hormones, so the answer is option $4$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q161_f94ae096_13112026.png?v=f94ae096d154)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q161_ab93f990_13112026.png?v=ab93f990edc3)

---

## Q162

Biology · zoology · Reproductive Health

Match List I with List II
Choose the correct answer from the option given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Non-medicated IUD | I | Multiload 375 |
| B | Copper releasing IUD | II | Progestogens |
| C | Hormone releasing IUD | III | Lippes loop |
| D | Implants | IV | LNG-20 |

- (1) A-III, B-I, C-II, D-IV
- (2) A-I, B-III, C-IV, D-II
- (3) A-IV, B-I, C-II, D-III
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because
2. Lippes loop is a non-medicated IUD.
3. Multiload 375 is a copper releasing IUD.
4. LNG -20 is a hormone releasing IUD.
5. Progestogens are used as implants.

**Solved independently** (answer withheld)

1. Non-medicated IUD is the Lippes loop, so $A \rightarrow III$.
2. Copper releasing IUD is Multiload 375, so $B \rightarrow I$.
3. Hormone releasing IUD is LNG-20, so $C \rightarrow IV$.
4. Implants contain progestogens (alone or with estrogen), so $D \rightarrow II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ is option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 67)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q162_1c2400c8_13112026.png?v=1c2400c832d0)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q162_71e0e3d3_13112026.png?v=71e0e3d3280a)

---

## Q163

Biology · zoology · Structural Organisation in Animals

In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on

- (1) $5^{\text{th}}$ segment
- **(2)** $10^{\text{th}}$ segment
- (3) $8^{\text{th}}$ and $9^{\text{th}}$ segment
- (4) $11^{\text{th}}$ segment

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2), because in both sexes of cockroach, $10^{\text{th}}$ segment bears a pair of jointed filamentous structures called anal cerci.
2. Options (1), (3) and (4) are incorrect because $5^{\text{th}}$, $8^{\text{th}}$ and $9^{\text{th}}$ segments do not bear such structures.
3. In adult cockroaches only $10^{\text{th}}$ segments are present in abdomen.
4. $11^{\text{th}}$ abdominal segment is absent.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Structural Organisation in Animals) states that in both sexes the $10^{\mathrm{th}}$ segment bears a pair of jointed filamentous anal cerci, which is option $2$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 68)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q163_aa315242_13112026.png?v=aa315242340f)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q163_c6953c42_13112026.png?v=c6953c421153)

---

## Q164

Biology · zoology · Breathing and Exchange of Gases

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Expiratory capacity | I | Expiratory reserve volume + Tidal volume + Inspiratory reserve volume |
| B | Functional residual capacity | II | Tidal volume + Expiratory reserve volume |
| C | Vital capacity | III | Tidal volume + Inspiratory reserve volume |
| D | Inspiratory capacity | IV | Expiratory reserve volume + Residual volume |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-III, B-II, C-IV, D-I
- (3) A-II, B-I, C-IV, D-III
- (4) A-I, B-III, C-II, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Expiratory capacity = Tidal volume + Expiratory reserve volume
2. Functional residual capacity = Expiratory reserve volume + Residual volume
3. Vital capacity = Expiratory reserve volume + Tidal volume + Inspiratory reserve volume
4. Inspiratory capacity = Tidal volume + Inspiratory reserve volume

**Solved independently** (answer withheld)

1. Expiratory capacity $= TV + ERV$, so A matches II.
2. Functional residual capacity $= ERV + RV$, so B matches IV.
3. Vital capacity $= ERV + TV + IRV$, so C matches I.
4. Inspiratory capacity $= TV + IRV$, so D matches III.
5. A-II, B-IV, C-I, D-III is option $1$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 68)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q164_0e2b592e_13112026.png?v=0e2b592e8c56)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q164_49993932_13112026.png?v=49993932622e)

---

## Q165

Biology · zoology · Neural Control and Coordination

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pons | I | Provides additional space for Neurons, regulates posture and balance. |
| B | Hypothalamus | II | Controls respiration and gastric secretions. |
| C | Medulla | III | Connects different regions of the brain. |
| D | Cerebellum | IV | Neuro secretory cells |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-I, B-III, C-II, D-IV
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. A. Pons – Part of hindbrain, it connects different regions of the brain.
3. B. Hypothalamus – Also have neuro secretory cells which secrete hormones.
4. C. Medulla oblongata – Part of hindbrain which controls respiration and gastric secretions.
5. D. Cerebellum – Part of hindbrain with convoluted surface which provides additional space for neurons, also regulates posture and balance.

**Solved independently** (answer withheld)

1. Pons consists of fibre tracts that interconnect different regions of the brain, so $A \to III$.
2. Hypothalamus contains neurosecretory cells that secrete hypothalamic hormones, so $B \to IV$.
3. Medulla contains centres controlling respiration, cardiovascular reflexes and gastric secretions, so $C \to II$.
4. Cerebellum has a highly convoluted surface giving additional space for neurons and regulates posture and balance, so $D \to I$.
5. $A-III,\ B-IV,\ C-II,\ D-I$ matches option $2$.

**Subtopic:** Hindbrain, Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q165_8064d1ef_13112026.png?v=8064d1efff8d)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q165_a8e5c724_13112026.png?v=a8e5c7245d02)

---

## Q166

Biology · zoology · Human Reproduction

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) The presence or absence of hymen is not a reliable indicator of virginity.
- (Statement II) The hymen is torn during the first coitus only.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) because the presence or absence of hymen is not a reliable indicator of virginity because hymen can also be broken by a sudden jolt, insertion of a vaginal tampon, active participation in some sports and in some women the hymen persists even after coitus.

**Solved independently** (answer withheld)

1. Statement I: the hymen may be torn by a sudden fall or jolt, tampon insertion, or active sports such as horse riding and cycling, and in some women it persists even after coitus, so its presence or absence is not a reliable indicator of virginity; Statement I is true.
2. Statement II: because the hymen can be torn by these other causes, it is not torn during the first coitus only; Statement II is false.
3. Statement I true and Statement II false matches option $3$.

**Subtopic:** Female External Genitalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 69)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q166_79c4d700_13112026.png?v=79c4d700ac0c)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q166_474fe23c_13112026.png?v=474fe23c9f9f)

---

## Q167

Biology · zoology · Biotechnology: Principles and Processes

The following diagram showing restriction sites in E. coli cloning vector pBR322. Find the role of ‘X’ and ‘Y’ genes :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q167_58f17fa7_13112026.png?v=58f17fa778c5)

- (1) The gene ‘X’  is responsible for resistance to antibiotics and ‘Y’ for protein involved in the replication of Plasmid.
- **(2)** The gene ‘X’ is responsible for controlling the copy number of the linked DNA and ‘Y’ for protein involved in the replication of Plasmid.
- (3) The gene ‘X’ is for protein involved in replication of Plasmid and ‘Y’ for resistance to antibiotics.
- (4) Gene ’X’ is responsible for recognitions sites and ‘Y’ is responsible for antibiotic resistance.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2), because
2. ‘X’ in the given diagram is ori while ‘Y’ is rop.
3. ‘X’ which is ori is responsible for controlling the copy number of the linked DNA and ‘Y’ which is rop codes for protein involved in the replication of plasmid.
4. Options (1), (3) and (4) are incorrect as ‘X’ and ‘Y’ are not related to these functions.

**Solved independently** (answer withheld)

1. In pBR322, $amp^R$ carries the PstI and PvuI sites and $tet^R$ carries the BamHI and SalI sites, so neither X nor Y is an antibiotic-resistance gene.
2. X is at the bottom-left of the map, where $ori$ sits; $ori$ controls the copy number of the linked DNA.
3. Y is next to the PvuII site, where $rop$ sits; $rop$ codes for proteins involved in plasmid replication.
4. So X = $ori$ and Y = $rop$, which is option $2$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 69)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q167_db9cd512_13112026.png?v=db9cd51251e9)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q167_c7bf8a44_13112026.png?v=c7bf8a44aa03)

---

## Q168

Biology · zoology · Molecular Basis of Inheritance

Which one is the correct product of DNA dependent RNA polymerase to the given template? 3’TACATGGCAAATATCCATTCA5’

- **(1)** 5’AUGUACCGUUUAUAGGUAAGU3’
- (2) 5’AUGUAAAGUUUAUAGGUAAGU3’
- (3) 5’AUGUACCGUUUAUAGGGAAGU3’
- (4) 5’ATGTACCGTTTATAGGTAAGT3’

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Template DNA is :
2. 3’TACATGGCAAATATCCATTCA5’
3. 5’AUGUACCGUUUAUAGGUAAGU3’ m-RNA

**Solved independently** (answer withheld)

1. DNA-dependent RNA polymerase synthesises RNA complementary and antiparallel to the template strand, reading $3'\to5'$ and building $5'\to3'$, using U instead of T.
2. Complementing $3'$-TACATGGCAAATATCCATTCA-$5'$ base by base gives $5'$-AUGUACCGUUUAUAGGUAAGU-$3'$.
3. Option 4 contains T (DNA), option 2 has AAAG in place of CCG, option 3 has GGG in place of GGU; only option $1$ matches exactly.

**Subtopic:** Transcription · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q168_8b055c03_13112026.png?v=8b055c03fa53)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q168_b201689c_13112026.png?v=b201689c2255)

---

## Q169

Biology · zoology · Locomotion and Movement

Which of the following are Autoimmune disorders?
Choose the most appropriate answer from the options given below:

- (A) Myasthenia gravis
- (B) Rheumatoid arthritis
- (C) Gout
- (D) Muscular dystrophy
- (E) Systemic Lupus Erythematosus (SLE)

- (1) A, B & D only
- **(2)** A, B & E only
- (3) B, C & E only
- (4) C, D & E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as Myasthenia gravis, Rheumatoid arthritis and Systemic Lupus Erythematosus (SLE) are autoimmune disorders.
2. Muscular dystrophy is a genetic disorder which progressively affects the skeletal muscles.
3. Gout is the inflammation of joints due to deposition of uric acid crystals.
4. Option (1), (3) and (4) are not the correct answer because all of them are not autoimmune disorders.

**Solved independently** (answer withheld)

1. Myasthenia gravis (A), rheumatoid arthritis (B) and SLE (E) are autoimmune disorders; gout (C) is due to uric acid crystal deposition and muscular dystrophy (D) is a genetic degenerative disorder, so the set is A, B & E, which is option $2$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q169_49925b63_13112026.png?v=49925b634637)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q169_7cbbcce2_13112026.png?v=7cbbcce225d4)

---

## Q170

Biology · zoology · Animal Kingdom

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pterophyllum | I | Hag fish |
| B | Myxine | II | Saw fish |
| C | Pristis | III | Angel fish |
| D | Exocoetus | IV | Flying fish |

- (1) A-II, B-I, C-III, D-IV
- **(2)** A-III, B-I, C-II, D-IV
- (3) A-IV, B-I, C-II, D-III
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct option is option no. (2) as
2. Pterophyllum is the scientific name for Angel fish.
3. Myxine is the scientific name for Hag fish.
4. Pristis is the scientific name for Saw fish.
5. Exocoetus is the scientific name for Flying fish.

**Solved independently** (answer withheld)

1. $\text{Pterophyllum}$ is the angel fish, so $A \to III$.
2. $\text{Myxine}$ is the hag fish, so $B \to I$.
3. $\text{Pristis}$ is the saw fish, so $C \to II$.
4. $\text{Exocoetus}$ is the flying fish, so $D \to IV$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}II,\ D\text{-}IV$ matches option $2$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q170_8ea76acf_13112026.png?v=8ea76acfc40c)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q170_f685c09c_13112026.png?v=f685c09cfe2d)

---

## Q171

Biology · zoology · Chemical Coordination and Integration

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) FSH acts upon ovarian follicles in female and Leydig cells in male.
- (Reason R) Growing ovarian follicles secrete estrogen in female while interstitial cells secrete androgen in male human being.

- (1) Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the correct explanation of A
- (3) A is true but R is false
- **(4)** A is false but R is true

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as FSH is a gonadotropin affects ovarian follicles in females and causes their growth but in males LH affects Leydig cells leading to secretion of androgens.
2. Growing ovarian follicles secrete estrogen in females while interstitial cells secrete androgen in male human being.
3. Hence, Assertion is false and Reason is true.

**Solved independently** (answer withheld)

1. In males, FSH acts on Sertoli cells, while LH acts on Leydig cells; so Assertion A is false.
2. Growing ovarian follicles secrete estrogen and interstitial (Leydig) cells secrete androgens; so Reason R is true.
3. A false, R true, which is option $4$.

**Subtopic:** The Pituitary Gland, Gonads · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 71)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q171_6239a1c6_13112026.png?v=6239a1c6ec93)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q171_6dc72487_13112026.png?v=6dc7248731df)

---

## Q172

Biology · zoology · Biomolecules

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Lipase | I | Peptide bond |
| B | Nuclease | II | Ester bond |
| C | Protease | III | Glycosidic bond |
| D | Amylase | IV | Phosphodiester bond |

- (1) A-IV, B-II, C-III, D-I
- (2) A-III, B-II, C-I, D-IV
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-IV, B-I, C-III, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. A. Lipase – Digests ester bond found in lipids.
3. B. Nuclease – Helps in digestion of phosphodiester bonds found in nucleic acids.
4. C. Protease – Helps in digestion of peptide bond found in proteins.
5. D. Amylase – Digests/breaks the glycosidic bonds found in carbohydrates i.e., digest starch into smaller molecules, ultimately yielding maltose, which in turn is cleaved into two glucose molecules by maltase.

**Solved independently** (answer withheld)

1. Lipase hydrolyses lipids by breaking the $\text{ester bond}$, so $A \to II$.
2. Nuclease hydrolyses nucleic acids by breaking the $\text{phosphodiester bond}$, so $B \to IV$.
3. Protease hydrolyses proteins by breaking the $\text{peptide bond}$, so $C \to I$.
4. Amylase hydrolyses starch by breaking the $\text{glycosidic bond}$, so $D \to III$.
5. $A\text{-}II,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}III$ matches option $3$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 71)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q172_5ff622bf_13112026.png?v=5ff622bf163f)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q172_a40ea29c_13112026.png?v=a40ea29c8858)

---

## Q173

Biology · zoology · Cell: The Unit of Life

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Axoneme | I | Centriole |
| B | Cartwheel pattern | II | Cilia and flagella |
| C | Crista | III | Chromosome |
| D | Satellite | IV | Mitochondria |

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- (3) A-II, B-IV, C-I, D-III
- **(4)** A-II, B-I, C-IV, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Axoneme is seen in cilia and flagella
2. Centriole shows cartwheel appearance
3. Crista is found in mitochondria
4. Satellite is present in chromosomes

**Solved independently** (answer withheld)

1. Axoneme is the microtubule core of cilia and flagella, so $A \rightarrow II$.
2. The centriole shows a cartwheel arrangement of peripheral triplet fibrils, so $B \rightarrow I$.
3. Cristae are infoldings of the inner mitochondrial membrane, so $C \rightarrow IV$.
4. A satellite is a small fragment beyond the secondary constriction of some chromosomes, so $D \rightarrow III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ is option $4$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 71)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q173_745b5a68_13112026.png?v=745b5a68d810)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q173_32d6b7d4_13112026.png?v=32d6b7d4eb7e)

---

## Q174

Biology · zoology · Cell Cycle and Cell Division

Match List I with List II :
Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
|  | List I (Sub Phases of Prophase I) |  | List II (Specific Characters) |
| A | Diakinesis | I | Synaptonemal complex formation |
| B | Pachytene | II | Completion of terminalisation of chiasmata |
| C | Zygotene | III | Chromosomes look like thin threads |
| D | Leptotene | IV | Appearance of recombination nodules |

- (1) A-IV, B-II, C-III, D-I
- (2) A-I, B-II, C-IV, D-III
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) Diakinesis – Completion of terminalisation of chiasmata
2. (B) Pachytene – Appearance of recombination nodules
3. (C) Zygotene – Synaptonemal complex formation
4. (D) Leptotene – Chromosomes look like thin threads
5. A-II, B-IV, C-I, D-III

**Solved independently** (answer withheld)

1. Diakinesis (A) is marked by completion of terminalisation of chiasmata, so $A \to II$.
2. Pachytene (B) shows the appearance of recombination nodules, so $B \to IV$.
3. Zygotene (C) is when the synaptonemal complex forms during synapsis, so $C \to I$.
4. Leptotene (D) has chromosomes that look like thin threads, so $D \to III$.
5. The match A-II, B-IV, C-I, D-III is option $3$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 72)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q174_76d6133b_13112026.png?v=76d6133b9602)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q174_1ce2d4b4_13112026.png?v=1ce2d4b497ed)

---

## Q175

Biology · zoology · Animal Kingdom

Consider the following statements :
Choose the correct answer from the options given below :

- (A) Annelids are true coelomates
- (B) Poriferans are pseudocoelomates
- (C) Aschelminthes are acoelomates
- (D) Platyhelminthes are pseudocoelomates

- (1) B only
- **(2)** A only
- (3) C only
- (4) D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2), because annelids are true coelomate animals.
2. Options (1), (3) and (4) are incorrect because poriferans are acoelomates, aschelminths are pseudocoelomates and platyhelminthes are acoelomates.

**Solved independently** (answer withheld)

1. Statement A: Annelids have a true coelom lined by mesoderm, so $A$ is true.
2. Statement B: Poriferans are cellular-level animals with no coelom, not pseudocoelomates, so $B$ is false.
3. Statement C: Aschelminthes have a pseudocoelom, not an acoelomate body, so $C$ is false.
4. Statement D: Platyhelminthes are acoelomates, not pseudocoelomates, so $D$ is false.
5. Only $A$ is correct, which is option $2$ (A only).

**Subtopic:** Basis of Classification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q175_6c567781_13112026.png?v=6c567781d25c)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q175_4a947beb_13112026.png?v=4a947bebc9a5)

---

## Q176

Biology · zoology · Biotechnology and Its Applications

Match List I with List II :
Choose the correct answer form the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\alpha$ –I antitrypsin | I | Cotton bollworm |
| B | Cry IAb | II | ADA deficiency |
| C | Cry IAc | III | Emphysema |
| D | Enzyme replacement therapy | IV | Corn borer |

- (1) A-II, B-I, C-IV, D-III
- (2) A-III, B-I, C-II, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. $\alpha$– I antitrypsin $\rightarrow$ Is used for treatment of Emphysema
3. $\textit{Cry}$ I Ab gene $\rightarrow$ Controls corn borer
4. $\textit{Cry}$ I Ac gene $\rightarrow$ Controls cotton bollworms
5. Enzyme replacement therapy $\rightarrow$ Can be used as treatment option in ADA deficiency.

**Solved independently** (answer withheld)

1. $\alpha$-1 antitrypsin is used to treat emphysema, so A-III.
2. The cryIAb gene product controls the corn borer, so B-IV.
3. The cryIAc gene product controls the cotton bollworm, so C-I.
4. Enzyme replacement therapy (giving ADA) treats ADA deficiency, so D-II.
5. A-III, B-IV, C-I, D-II matches option $3$.

**Subtopic:** Pest Resistant Plants and Bt Cotton, Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 72)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q176_0c0f1368_13112026.png?v=0c0f1368db86)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q176_a7f9d734_13112026.png?v=a7f9d7346cbc)

---

## Q177

Biology · zoology · Locomotion and Movement

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Fibrous joints | I | Adjacent vertebrae, limited movement |
| B | Cartilaginous joints | II | Humerus and Pectoral girdle, rotational movement |
| C | Hinge joints | III | Skull, don’t allow any movement |
| D | Ball and socket joints | IV | Knee, help in locomotion |

- (1) A-IV, B-II, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- (3) A-II, B-III, C-I, D-IV
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) as
2. Fibrous joints do not allow any movement. This type of joint is shown by the flat skull bones which fuse end-to-end with the help of dense fibrous connective tissues in the form of sutures.
3. Cartilaginous joint is present between the adjacent vertebrae in the vertebral column and this permits limited movements.
4. Hinge joint is a type of synovial joint present in knee, help in locomotion
5. Ball and socket joint is also a type of synovial joint present between humerus and pectoral girdle and allows rotational movement.

**Solved independently** (answer withheld)

1. Fibrous joints (A) are the sutures of the skull bones, which allow no movement, so A-III.
2. Cartilaginous joints (B) join adjacent vertebrae and permit limited movement, so B-I.
3. Hinge joints (C) occur at the knee and help in locomotion, so C-IV.
4. Ball and socket joints (D) are between the humerus and pectoral girdle, giving rotational movement, so D-II.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}II$ matches option $4$.

**Subtopic:** Joints · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 73)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q177_a7974885_13112026.png?v=a7974885f837)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q177_a5b64826_13112026.png?v=a5b648268830)

---

## Q178

Biology · zoology · Structural Organisation in Animals

Three types of muscles are given as a, b and c. Identify the correct matching pair along with their location in human body: Name of muscle/location

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q178_b1688be6_13112026.png?v=b1688be672dd)

- (1) (a) Smooth - Toes (b) Skeletal – Legs (c) Cardiac – Heart
- **(2)** (a) Skeletal - Triceps (b) Smooth – Stomach (c) Cardiac – Heart
- (3) (a) Skeletal - Biceps (b) Involuntary – Intestine (c) Smooth – Heart
- (4) (a) Involuntary – Nose tip (b) Skeletal – Bone (c) Cardiac – Heart

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. Figure (a) represents skeletal muscle fibres which are closely attached to skeletal bones. In a typical muscle such as triceps and biceps, striated muscle fibres are bundled together in a parallel fashion.
3. Figure (b) represents smooth muscle fibres which are present in the wall of internal organs such as the blood vessels, stomach and intestine.
4. Figure (c) represents cardiac muscle fibres which are exclusively present in the heart.

**Solved independently** (answer withheld)

1. Figure (a) shows long cylindrical, striated, unbranched fibres: skeletal muscle, found attached to bones, e.g. triceps.
2. Figure (b) shows spindle-shaped, unstriated fibres with a single central nucleus: smooth muscle, found in walls of visceral organs such as the stomach.
3. Figure (c) shows striated, branched fibres joined to each other: cardiac muscle, found only in the heart.
4. Option $3$ wrongly places smooth muscle in the heart, option $4$ calls (a) involuntary at the nose tip, option $1$ puts smooth muscle in toes; only option $2$ (Skeletal – Triceps, Smooth – Stomach, Cardiac – Heart) matches, so the answer is option $2$.

**Subtopic:** Muscle Tissue and Neural Tissue · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 73)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q178_ae7f8455_13112026.png?v=ae7f8455489d)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q178_b198be15_13112026.png?v=b198be15654c)

---

## Q179

Biology · zoology · Principles of Inheritance and Variation

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Down’s syndrome | I | $11^{\text{th}}$ chromosome |
| B | $\alpha$-Thalassemia | II | ‘X’ chromosome |
| C | $\beta$-Thalassemia | III | $21^{\text{st}}$ chromosome |
| D | Klinefelter’s syndrome | IV | $16^{\text{th}}$ chromosome |

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-III, C-IV, D-I
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Down’s syndrome is due to presence of an additional copy of chromosome number $21$.
2. Klinefelter’s syndrome is caused due to presence of an additional copy of $\mathrm{X}$-chromosome.
3. $\alpha$-Thalassemia is controlled by two closely linked genes on chromosome $16$ of each parent.
4. $\beta$-Thalassemia is controlled by a single gene HBB on chromosome $11$ of each parent.

**Solved independently** (answer withheld)

1. Down's syndrome is trisomy of chromosome $21$, so A-III.
2. $\alpha$-Thalassemia is controlled by genes HBA1 and HBA2 on chromosome $16$, so B-IV.
3. $\beta$-Thalassemia is controlled by the HBB gene on chromosome $11$, so C-I.
4. Klinefelter's syndrome is $47$, XXY (an extra X chromosome), so D-II.
5. A-III, B-IV, C-I, D-II is option $3$.

**Subtopic:** Thalassemia, Chromosomal Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q179_fb41132e_13112026.png?v=fb41132ed895)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q179_2dee2004_13112026.png?v=2dee20043ed9)

---

## Q180

Biology · zoology · Breathing and Exchange of Gases

Which of the following factors are favourable for the formation of oxyhaemoglobin in alveoli?

- (1) High $p\mathrm{O_2}$ and High $p\mathrm{CO_2}$
- **(2)** High $p\mathrm{O_2}$ and Lesser $\mathrm{H^+}$ concentration
- (3) Low $p\mathrm{CO_2}$ and High $\mathrm{H^+}$ concentration
- (4) Low $p\mathrm{CO_2}$ and High temperature

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as
2. Conditions favourable for formation of oxyhaemoglobin in alveoli are high $p\mathrm{O_2}$, less $\mathrm{H^+}$ concentration low $p\mathrm{CO_2}$ and low temperature.
3. Option (1), (3) and (4) are not correct as they do not favour the formation of oxyhaemoglobin.

**Solved independently** (answer withheld)

1. Oxyhaemoglobin formation is favoured by high $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, lesser $\mathrm{H^+}$ concentration and lower temperature (conditions in the alveoli).
2. Option 4 has high temperature, option 1 has high $\mathrm{pCO_2}$ and option 3 has high $\mathrm{H^+}$, each of which is unfavourable.
3. Option $2$ (high $\mathrm{pO_2}$ and lesser $\mathrm{H^+}$) has both factors favourable, so the answer is option $2$.

**Subtopic:** Transport of Gases · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 74)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q180_8a74470e_13112026.png?v=8a74470eedad)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q180_72100dd8_13112026.png?v=72100dd88ebe)

---

## Q181

Biology · zoology · Evolution

Given below are some stages of human evolution. Arrange them in correct sequence. (Past to Recent) Choose the correct sequence of human evolution from the options given below:

- (A) Homo habilis
- (B) Homo sapiens
- (C) Homo neanderthalensis
- (D) Homo erectus

- (1) D-A-C-B
- (2) B-A-D-C
- (3) C-B-D-A
- **(4)** A-D-C-B

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because the correct sequence of stages of human evolution from past to recent is
2. Homo habilis $\rightarrow$ Homo erectus $\rightarrow$ Homo neanderthalensis $\rightarrow$ Homo sapiens

**Solved independently** (answer withheld)

1. Order the stages from past to recent as $\text{A (H. habilis)} \rightarrow \text{D (H. erectus)} \rightarrow \text{C (H. neanderthalensis)} \rightarrow \text{B (H. sapiens)}$, i.e. A-D-C-B, which is option $4$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 75)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q181_2ab4ea3a_13112026.png?v=2ab4ea3a4b70)

Publisher's solution, as printed:

![printed solution 181](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q181_8c6d1f72_13112026.png?v=8c6d1f72ba28)

---

## Q182

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cocaine | I | Effective sedative in surgery |
| B | Heroin | II | Cannabis sativa |
| C | Morphine | III | Erythroxylum |
| D | Marijuana | IV | Papaver somniferum |

- (1) A-IV, B-III, C-I, D-II
- (2) A-I, B-III, C-II, D-IV
- (3) A-II, B-I, C-III, D-IV
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct option is (4) as
2. A. Cocaine – Obtained from plant Erythroxylum coca, stimulating action on CNS.
3. B. Heroin – Formed by the acetylation of morphine which is obtained from plant Papaver somniferum.
4. C. Morphine – Obtained from Papaver somniferum, is an effective sedative in surgery.
5. D. Marijuana – Obtained from Cannabis sativa, produces hallucinogenic effect and affects cardiovascular system of the body.

**Solved independently** (answer withheld)

1. Cocaine is obtained from the coca plant $Erythroxylum\ coca$, so $A \to III$.
2. Heroin (diacetylmorphine) is derived from morphine, which comes from the poppy $Papaver\ somniferum$, so $B \to IV$.
3. Morphine is a very effective sedative and painkiller used in surgery, so $C \to I$.
4. Marijuana is obtained from the inflorescences of $Cannabis\ sativa$, so $D \to II$.
5. $A\text{-}III, B\text{-}IV, C\text{-}I, D\text{-}II$ matches option $4$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 75)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q182_9896e975_13112026.png?v=9896e975e01c)

Publisher's solution, as printed:

![printed solution 182](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q182_92c1621e_13112026.png?v=92c1621e2d8f)

---

## Q183

Biology · zoology · Human Health and Disease

Given below are two statements: One is labelled as Assertion A and the other is labelled as Reason R: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby.
- (Reason R) Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

- **(1)** Both A and R are correct and R is the correct explanation of A
- (2) Both A and R are correct but R is NOT the correct explanation of A
- (3) A is correct but R is not correct
- (4) A is not correct but R is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1)
2. Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby as colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

**Solved independently** (answer withheld)

1. Assertion A is true: NCERT states that breast-feeding during the initial period of infant growth is recommended by doctors for bringing up a healthy baby.
2. Reason R is true: colostrum contains several antibodies (IgA) absolutely essential to develop resistance for the newborn, and this passive immunity is the reason breast-feeding is recommended, so R explains A, giving option $1$.

**Subtopic:** Active and Passive Immunity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 75)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q183_9a0eac55_13112026.png?v=9a0eac55b91e)

Publisher's solution, as printed:

![printed solution 183](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q183_b10941a6_13112026.png?v=b10941a6c279)

---

## Q184

Biology · zoology · Reproductive Health

Which of the following is not a natural/traditional contraceptive method?

- (1) Coitus interruptus
- (2) Periodic abstinence
- (3) Lactational amenorrhea
- **(4)** Vaults

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as
2. Vault is a barrier method of contraception which is made of rubber that is inserted into the female reproductive tract to cover the cervix during the coitus.
3. Option (1) is incorrect as coitus interruptus is a natural method of contraception in which male partner withdraws his penis from the vagina just before ejaculation so as to avoid insemination.
4. Option (2) is incorrect as periodic abstinence is also a natural method of contraception in which couples avoid coitus during the fertile period.
5. Option (3) is incorrect as lactational amenorrhea is also a natural method of contraception which is based on the fact that ovulation and therefore the cycle do not occur during the period of intense lactational following parturition.

**Solved independently** (answer withheld)

1. Coitus interruptus, periodic abstinence and lactational amenorrhea are natural/traditional methods, while vaults are a barrier method, so the answer is option $4$.

**Subtopic:** Natural Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 76)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q184_f2a6479f_13112026.png?v=f2a6479f4dba)

Publisher's solution, as printed:

![printed solution 184](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q184_243b6ffc_13112026.png?v=243b6ffce6fe)

---

## Q185

Biology · zoology · Biotechnology: Principles and Processes

The “Ti plasmid” of Agrobacterium tumefaciens stands for

- (1) Tumour inhibiting plasmid
- (2) Tumor independent plasmid
- **(3)** Tumor inducing plasmid
- (4) Temperature independent plasmid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as Ti plasmid of Agrobacterium tumefaciens is tumor inducing plasmid, containing T-DNA which causes tumor in several dicot plants.
2. Options (1), (2) and (4) are not correct.

**Solved independently** (answer withheld)

1. The Ti plasmid of $Agrobacterium\ tumefaciens$ causes tumours (crown gall) in dicot plants, so Ti = Tumor inducing, which is option $3$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 76)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q185_8f0a5364_13112026.png?v=8f0a53641ba1)

Publisher's solution, as printed:

![printed solution 185](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q185_a2ed8a1f_13112026.png?v=a2ed8a1fb86c)

---

## Q186

Biology · zoology · Chemical Coordination and Integration

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Exophthalmic goiter | I | Excess secretion of cortisol, moon face & hypergylcemia. |
| B | Acromegaly | II | Hypo-secretion of thyroid hormone and stunted growth. |
| C | Cushing’s syndrome | III | Hyper secretion of thyroid hormone & protruding eye balls. |
| D | Cretinism | IV | Excessive secretion of growth hormone. |

- (1) A-I, B-III, C-II, D-IV
- (2) A-IV, B-II, C-I, D-III
- (3) A-III, B-IV, C-II, D-I
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) as
2. (A) Exophthalmic goiter — (III) Hyper secretion of thyroid hormone and characterized by protruding eye balls
3. (B) Acromegaly — (IV) Excessive secretion of growth hormone
4. (C) Cushing’s syndrome — (I) Excess secretion of cortisol, moon face and hyperglycaemia
5. (D) Cretinism — (II) Hypo-secretion of thyroid hormone and characterized by stunted growth

**Solved independently** (answer withheld)

1. Exophthalmic goiter (Graves' disease) is hypersecretion of thyroid hormone with protruding eyeballs: $A \to III$.
2. Acromegaly results from excessive secretion of growth hormone in adults: $B \to IV$.
3. Cushing's syndrome results from excess cortisol, giving moon face and hyperglycemia: $C \to I$.
4. Cretinism results from hyposecretion of thyroid hormone, with stunted growth: $D \to II$.
5. $A\text{-}III, B\text{-}IV, C\text{-}I, D\text{-}II$ matches option $4$.

**Subtopic:** Endocrine Disorders · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 76)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q186_13fc8115_13112026.png?v=13fc8115aaa7)

Publisher's solution, as printed:

![printed solution 186](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q186_fb22199c_13112026.png?v=fb22199c0259)

---

## Q187

Biology · zoology · Cell: The Unit of Life

> ⚠ The booklet prints "choose the mis appropriate answer" (read: most appropriate) and "as compared chloroplast" (read: as compared to chloroplast). Statement II is the disputed one: the booklet keys (3), Statement II incorrect; the blind solve chose (1), both correct (the inner mitochondrial membrane is the less permeable one). Same question and same key as 2024_S1 q191 and 2024_Q3 q199. (Carried from 2024_Q2 q190, the same question; option numbers converted to this booklet.)

> ⚠ The independent solve chose (1); the booklet prints (3).

Given below are two statements: In the light of the above statements, choose the mis appropriate answer from the options given below:

- (Statement I) Mitochondria and chloroplasts both double membranes bound organelles.
- (Statement II) Inner membrane of mitochondria is relatively less permeable, as compared chloroplast.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (1) · differs

**Publisher's solution**

1. Both mitochondria and chloroplasts are double membrane bound cell organelles.
2. Transport of ions occurs across the inner membrane of mitochondria.
3. The inner membrane of chloroplast is impermeable to ions and metabolites.
4. Therefore, it is said that inner membrane of mitochondria is relatively more permeable to that of chloroplast.

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts each have an outer and an inner membrane, so Statement I is correct.
2. The inner mitochondrial membrane is highly selective (most solutes need specific carriers), so it is relatively less permeable; Statement II is taken as correct.
3. Both statements correct $\Rightarrow$ option $1$.

**Subtopic:** Mitochondria, Plastids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 77)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q187_5b3a34af_13112026.png?v=5b3a34af80c0)

Publisher's solution, as printed:

![printed solution 187](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q187_6cddf3b8_13112026.png?v=6cddf3b82fc9)

---

## Q188

Biology · zoology · Biomolecules

Regarding catalytic cycle of an enzyme action, select the correct sequential steps :
Choose the correct answer from the options given below :

- (A) Substrate enzyme complex formation.
- (B) Free enzyme ready to bind with another substrate.
- (C) Release of products.
- (D) Chemical bonds of the substrate broken.
- (E) Substrate binding to active site.

- **(1)** E, A, D, C, B
- (2) A, E, B, D, C
- (3) B, A, C, D, E
- (4) E, D, C, B, A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) which is E, A, D, C, B.
2. The catalytic cycle of an enzyme action can be described in the following steps.
3. (1) First, the substrate binds to the active site of the enzyme, fitting into the active site.
4. (2) The binding of the substrate induces the enzyme to alter its shape, fitting more tightly around the substrate.
5. (3) The active site of the enzyme, now in close proximity of the substrate breaks the chemical bonds of the substrate and the new enzyme-product complex is formed.
6. (4) The enzyme releases the products of the reaction and the free enzyme is ready to bind to another molecule of the substrate and run through the catalytic cycle once again.
7. Options (2), (3) and (4) are incorrect as the steps mentioned are in the wrong sequence.

**Solved independently** (answer withheld)

1. The substrate first binds to the active site of the enzyme: step $E$.
2. Binding forms the enzyme-substrate complex: step $A$.
3. Within the complex the chemical bonds of the substrate are broken: step $D$.
4. The products are released from the active site: step $C$.
5. The free enzyme is then ready to bind another substrate: step $B$.
6. The sequence $E \rightarrow A \rightarrow D \rightarrow C \rightarrow B$ is option $1$.

**Subtopic:** Enzymes and Chemical Reactions · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 77)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q188_9f378121_13112026.png?v=9f378121eb1f)

Publisher's solution, as printed:

![printed solution 188](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q188_83cc94e8_13112026.png?v=83cc94e8307f)

---

## Q189

Biology · zoology · Structural Organisation in Animals

Match List I with List II related to digestive system of cockroach.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | The structures used for storing of food | I | Gizzard |
| B | Ring of 6-8 blind tubules at junction of foregut and midgut. | II | Gastric Caeca |
| C | Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut. | III | Malpighian tubules |
| D | The structures used for grinding the food. | IV | Crop |

- **(1)** A-IV, B-II, C-III, D-I
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as
2. The structure used for griding the food particles – Gizzard
3. The structure used for storing of food – Crop
4. Ring of 6-8 blind tubules at junction of foregut and midgut which assists in secretion of digestive juices – Gastric Caeca
5. Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut which assists in elimination of nitrogenous wastes – Malpighian tubules

**Solved independently** (answer withheld)

1. Food storage in cockroach is done by the crop, so $A \to IV$.
2. The ring of 6-8 blind tubules at the foregut-midgut junction is the gastric caeca, so $B \to II$.
3. The ring of 100-150 yellow filaments at the midgut-hindgut junction is the Malpighian tubules, so $C \to III$.
4. Grinding of food is done by the gizzard (proventriculus), so $D \to I$.
5. $A$-IV, $B$-II, $C$-III, $D$-I is option $1$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 78)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q189_3c3992bc_13112026.png?v=3c3992bceb19)

Publisher's solution, as printed:

![printed solution 189](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q189_18019b2f_13112026.png?v=18019b2f0c89)

---

## Q190

Biology · zoology · Animal Kingdom

The following are the statements about non-chordates:
Choose the most appropriate answer from the options given below:

- (A) Pharynx is perforated by gill slits.
- (B) Notochord is absent.
- (C) Central nervous system is dorsal.
- (D) Heart is dorsal if present.
- (E) Post anal tail is absent.

- (1) A & C only
- (2) A, B & D only
- **(3)** B, D & E only
- (4) B, C & D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) as the features of non-chordates among the given statements are:
2. B. Notochord is absent.
3. D. Heart is dorsal if present.
4. E. Post anal tail is absent.
5. Statements A and C are features of chordates.
6. Hence, option (3) is correct and options (1), (2) and (4) are incorrect.

**Solved independently** (answer withheld)

1. A: pharyngeal gill slits are absent in non-chordates, so A is false.
2. B: notochord is absent in non-chordates, so B is true.
3. C: the central nervous system of non-chordates is ventral, solid and double, so C is false.
4. D: the heart of non-chordates, if present, is dorsal, so D is true.
5. E: a post-anal tail is absent in non-chordates, so E is true.
6. True statements are $B$, $D$ and $E$, which is option $3$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 78)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q190_5e3c2ac6_13112026.png?v=5e3c2ac6bc26)

Publisher's solution, as printed:

![printed solution 190](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q190_6923277d_13112026.png?v=6923277d61e0)

---

## Q191

Biology · zoology · Excretory Products and Their Elimination

Choose the correct statement given below regarding juxta medullary nephron.

- (1) Juxta medullary nephrons are located in the columns of Bertini.
- (2) Renal corpuscle of juxta medullary nephron lies in the outer portion of the renal medulla.
- **(3)** Loop of Henle of juxta medullary nephron runs deep into medulla.
- (4) Juxta medullary nephrons outnumber the cortical nephrons.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no, (3) because the length of loop of Henle of juxta medullary nephron is longer than the length of loop of Henle of cortical nephron and runs deep into medulla.
2. Option (1) is incorrect as juxta medullary nephron are not present in columns of Bertini.
3. Option (2) is incorrect because renal corpuscle of juxta medullary nephron lies in inner cortical region.
4. Option (4) is incorrect as juxta medullary nephrons are lesser in number than cortical nephrons.

**Solved independently** (answer withheld)

1. Cortical nephrons outnumber juxtamedullary ones, their corpuscles lie in the inner cortex rather than the medulla or the columns of Bertini, and their long loops of Henle run deep into the medulla, so option $3$ is correct.

**Subtopic:** Human Excretory System · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 78)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q191_57a2cd27_13112026.png?v=57a2cd276ec0)

Publisher's solution, as printed:

![printed solution 191](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q191_0bb576e0_13112026.png?v=0bb576e0aef6)

---

## Q192

Biology · zoology · Neural Control and Coordination

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The cerebral hemispheres are connected by nerve tract known as corpus callosum.
- (Statement II) The brain stem consists of the medulla oblongata, pons and cerebrum.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as statement I is correct but statement II is incorrect.
2. In human brain, a deep cleft divides the cerebrum longitudinally into two halves, which are termed as the left and right cerebral hemispheres.
3. The cerebral hemispheres are connected by a tract of nerve fibres called corpus callosum.
4. Three major regions make up the brain stem i.e. mid brain, pons and medulla oblongata.
5. Cerebrum is a part of forebrain which does not form brain stem.
6. Options (1), (2) and (4) are incorrect.

**Solved independently** (answer withheld)

1. Statement I: the two cerebral hemispheres are connected by a tract of nerve fibres called the corpus callosum, so Statement I is correct.
2. Statement II: the brain stem is formed by the midbrain, pons and medulla oblongata; the cerebrum is part of the forebrain, so Statement II is incorrect.
3. I correct and II incorrect matches option $3$.

**Subtopic:** Forebrain, Hindbrain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 79)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q192_f5f6c3ca_13112026.png?v=f5f6c3ca5bae)

Publisher's solution, as printed:

![printed solution 192](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q192_0499df2d_13112026.png?v=0499df2d6091)

---

## Q193

Biology · zoology · Body Fluids and Circulation

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | P wave | I | Heart muscles are electrically silent. |
| B | QRS complex | II | Depolarisation of ventricles. |
| C | T wave | III | Depolarisation of atria. |
| D | T-P gap | IV | Repolarisation of ventricles. |

- (1) A-I, B-III, C-IV, D-II
- **(2)** A-III, B-II, C-IV, D-I
- (3) A-II, B-III, C-I, D-IV
- (4) A-IV, B-II, C-I, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2) as
2. A. P wave - III. Depolarisation of atria.
3. B. QRS complex - II. Depolarisation of ventricles.
4. C. T wave - IV. Repolarisation of ventricles.
5. D. T-P gap - I. Heart muscles are electrically silent.

**Solved independently** (answer withheld)

1. P wave $\rightarrow$ depolarisation of atria (III); QRS complex $\rightarrow$ depolarisation of ventricles (II); T wave $\rightarrow$ repolarisation of ventricles (IV); T-P gap $\rightarrow$ heart muscles electrically silent (I); so A-III, B-II, C-IV, D-I, which is option $2$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 79)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q193_e89b3cc7_13112026.png?v=e89b3cc76372)

Publisher's solution, as printed:

![printed solution 193](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q193_f3b74452_13112026.png?v=f3b7445231ba)

---

## Q194

Biology · zoology · Evolution

Match List I with List II:
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Mesozoic Era | I | Lower invertebrates |
| B | Proterozoic Era | II | Fish & Amphibia |
| C | Cenozoic Era | III | Birds & Reptiles |
| D | Paleozoic Era | IV | Mammals |

- (1) A-II, B-I, C-III, D-IV
- (2) A-III, B-I, C-II, D-IV
- (3) A-I, B-II, C-IV, D-III
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4)
2. (A) Mesozoic Era – (III) Birds & Reptiles
3. (B) Proterozoic Era – (I) Lower invertebrates
4. (C) Cenozoic Era – (IV) Mammals
5. (D) Paleozoic Era – (II) Fish & Amphibia

**Solved independently** (answer withheld)

1. Mesozoic Era (A) is the age of reptiles, with birds arising in it: $A \to III$.
2. Proterozoic Era (B) holds only lower invertebrates: $B \to I$.
3. Cenozoic Era (C) is the age of mammals: $C \to IV$.
4. Paleozoic Era (D) sees fishes and amphibians: $D \to II$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}II$ is option $4$.

**Subtopic:** Brief Account of Evolution · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 80)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q194_516021ae_13112026.png?v=516021aeb70d)

Publisher's solution, as printed:

![printed solution 194](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q194_ea414658_13112026.png?v=ea414658bda5)

---

## Q195

Biology · zoology · Principles of Inheritance and Variation

As per ABO blood grouping system, the blood group of father is $\mathrm{B^{+}}$, mother is $\mathrm{A^{+}}$ and child is $\mathrm{O^{+}}$. Their respective genotype can be
Choose the most appropriate answer from the options given below :

- (A) $\mathrm{I^{B}i/I^{A}i/ii}$
- (B) $\mathrm{I^{B}I^{B}/I^{A}I^{A}/ii}$
- (C) $\mathrm{I^{A}I^{B}/iI^{A}/I^{B}i}$
- (D) $\mathrm{I^{A}i/I^{B}i/I^{A}i}$
- (E) $\mathrm{iI^{B}/iI^{A}/I^{A}I^{B}}$

- **(1)** A only
- (2) B only
- (3) C & B only
- (4) D & E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Genotype of father with blood group $\mathrm{B^{+}} = \mathrm{I^{B}i/iI^{B}}$
2. Genotype of mother with blood group $\mathrm{A^{+}} = \mathrm{I^{A}i/iI^{A}}$
3. Genotype of child with blood group $\mathrm{O^{+}} = \mathrm{ii}$
4. Hence only ‘A’ is correct.

**Solved independently** (answer withheld)

1. Blood group O is only possible with genotype $ii$, so the child is $ii$ and got one $i$ allele from each parent.
2. So the father (group B) must be $I^{B}i$ and the mother (group A) must be $I^{A}i$.
3. Statement A ($I^{B}i/I^{A}i/ii$) matches. B fails because homozygous parents cannot have an $ii$ child, and C, D and E give the wrong phenotypes.
4. Only A is correct, which is option $1$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 80)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q195_4e1332e9_13112026.png?v=4e1332e9db70)

Publisher's solution, as printed:

![printed solution 195](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q195_fa0c9cd3_13112026.png?v=fa0c9cd3f5c5)

---

## Q196

Biology · zoology · Organisms and Populations

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Gause's competitive exclusion principle states that two closely related species competing for different resources cannot exist indefinitely.
- (Statement II) According to Gause's principle, during competition, the inferior will be eliminated. This may be true if resources are limiting.

- (1) Both Statement I and Statement II are true.
- (2) Both Statement I and Statement II are false.
- (3) Statement I is true but Statement II is false.
- **(4)** Statement I is false but Statement II is true.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Gause's competitive exclusion principle states that two closely related species competing for the same resources cannot exist indefinitely and the competitively inferior one will be eliminated eventually.
2. This may be true if resources are limiting.

**Solved independently** (answer withheld)

1. Gause's competitive exclusion principle: two closely related species competing for the same resources cannot coexist indefinitely; Statement I says 'different resources', so it is false.
2. Under the principle the competitively inferior species is eliminated, which holds when resources are limiting; Statement II is true.
3. Statement I false, Statement II true, which is option $4$.

**Subtopic:** Competition · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 80)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q196_429d149a_13112026.png?v=429d149a4ac4)

Publisher's solution, as printed:

![printed solution 196](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q196_30728b5c_13112026.png?v=30728b5ce8ab)

---

## Q197

Biology · zoology · Human Health and Disease

Given below are two statements : In the light of above statements, choose the most appropriate answer from the options given below :

- (Statement I) Bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
- (Statement II) Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes.

- **(1)** Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- (3) Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as both statements I and II are correct.
2. In humans, the bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
3. Both bone-marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes.
4. Options (2), (3) and (4) are incorrect.

**Solved independently** (answer withheld)

1. Statement I: bone marrow is the main (primary) lymphoid organ where all blood cells, including lymphocytes, are formed, so it is correct.
2. Statement II: as NCERT teaches, both bone marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes, so it is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 81)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q197_0e15663d_13112026.png?v=0e15663d6cb3)

Publisher's solution, as printed:

![printed solution 197](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q197_73e3543e_13112026.png?v=73e3543e5dd2)

---

## Q198

Biology · zoology · Structural Organisation in Animals

Match List I with List II: Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Unicellular glandular epithelium | I | Salivary glands |
| B | Compound epithelium | II | Pancreas |
| C | Multicellular glandular epithelium | III | Goblet cells of alimentary canal |
| D | Endocrine glandular epithelium | IV | Moist surface of buccal cavity |

- (1) A-II, B-I, C-III, D-IV
- (2) A-IV, B-III, C-I, D-II
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) as
2. A. Unicellular glandular epithelium — (III) Goblet cells of alimentary canal
3. B. Compound epithelium — (IV) Lines moist surface of buccal cavity
4. C. Multicellular glandular epithelium — (I) Salivary glands
5. D. Endocrine glandular epithelium — (II) Pancreas

**Solved independently** (answer withheld)

1. Unicellular glandular epithelium consists of isolated cells such as the goblet cells of the alimentary canal: $A \rightarrow III$.
2. Compound epithelium covers the moist surface of the buccal cavity: $B \rightarrow IV$.
3. Multicellular glandular epithelium forms clusters of cells, as in the salivary glands: $C \rightarrow I$.
4. Among the remaining choices the pancreas has endocrine function (islets of Langerhans): $D \rightarrow II$.
5. $A\text{-}III,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}II$ matches option $3$.

**Subtopic:** Animal Tissues: Epithelial Tissue · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 81)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q198_5fd217c8_13112026.png?v=5fd217c86e5e)

Publisher's solution, as printed:

![printed solution 198](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q198_71cec7a6_13112026.png?v=71cec7a6a3ba)

---

## Q199

Biology · zoology · Molecular Basis of Inheritance

Match List I with List II: Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | RNA polymerase III | I | snRNPs |
| B | Termination of transcription | II | Promotor |
| C | Splicing of Exons | III | Rho factor |
| D | TATA box | IV | SnRNAs, tRNA |

- (1) A-II, B-IV, C-I, D-III
- (2) A-III, B-II, C-IV, D-I
- (3) A-III, B-IV, C-I, D-II
- **(4)** A-IV, B-III, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In eukaryotes, RNA polymerase III codes for snRNAs, tRNA and 5s rRNA.
2. Splicing of exons is performed by snRNPs.
3. TATA box is present in promoter region of transcription unit.
4. Rho factor is responsible for termination of transcription.

**Solved independently** (answer withheld)

1. RNA polymerase III transcribes $\text{tRNA}$, $5S\,\text{rRNA}$ and $\text{snRNAs}$, so $A \to IV$.
2. Rho factor causes termination of transcription in prokaryotes, so $B \to III$.
3. Splicing of exons is carried out by the spliceosome made of $\text{snRNPs}$, so $C \to I$.
4. The TATA box is part of the promoter, so $D \to II$.
5. $A\text{-}IV,\ B\text{-}III,\ C\text{-}I,\ D\text{-}II$ is option $4$.

**Subtopic:** Transcription · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 82)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q199_2a5cc33d_13112026.png?v=2a5cc33dda25)

Publisher's solution, as printed:

![printed solution 199](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q199_e0c019a1_13112026.png?v=e0c019a1812f)

---

## Q200

Biology · zoology · Human Reproduction

Identify the correct option (A), (B), (C), (D) with respect to spermatogenesis.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/figures_agent/q200_f19fdf5f_13112026.png?v=f19fdf5fbbc7)

- **(1)** FSH, Leydig cells, Sertoli cells, spermiogenesis.
- (2) ICSH, Interstitial cells, Leydig cells, spermiogenesis.
- (3) FSH, Sertoli cells, Leydig cells, spermatogenesis.
- (4) ICSH, Leydig cells, Sertoli cells, spermatogenesis.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as
2. (A) is $\mathrm{FSH}$ which is a pituitary hormone.
3. (B) is Leydig cells which are found in the interstitial space outside of the seminiferous tubules.
4. (C) is Sertoli cells are found inside the seminiferous tubules.
5. (D) is Spermiogenesis which is a process that helps in transformation of spermatids into spermatozoa.

**Solved independently** (answer withheld)

1. GnRH stimulates release of LH and FSH, so (A) $=$ FSH.
2. LH acts on Leydig cells to stimulate androgen synthesis, so (B) $=$ Leydig cells.
3. FSH acts on Sertoli cells, so (C) $=$ Sertoli cells.
4. Sertoli cells secrete factors that help spermiogenesis (spermatids to sperm), so (D) $=$ spermiogenesis.
5. FSH, Leydig cells, Sertoli cells, spermiogenesis matches option $1$.

**Subtopic:** Male Gametogenesis (Spermatogenesis), Hormonal Regulation of Reproduction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 82)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/crops/q200_8fa6873e_13112026.png?v=8fa6873e54bf)

Publisher's solution, as printed:

![printed solution 200](https://d30lmobgrc5gb8.cloudfront.net/general/13112026/neet_papers/2024/2024_Q4/solutions/q200_8e78d187_13112026.png?v=8e78d1876af5)

