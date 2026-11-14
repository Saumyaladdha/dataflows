# NEET (UG) 2024 · Code S1

200 questions · source `NEET_Papers/2024/Set_S1/NEET_2024_Question_Paper_S1.pdf` · every image a CDN link (0 without one) · 98 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Laws of Motion

A bob is whirled in a horizontal plane by means of a string with an initial speed of $\omega$ rpm. The tension in the string is $T$. If speed becomes $2\omega$ while keeping the same radius, the tension in the string becomes:

- (1) $\sqrt{2}T$
- (2) $T$
- **(3)** $4T$
- (4) $\frac{T}{4}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Bob m whirled on a string of length l about a pivot with angular speed omega; tension T acts towards the pivot](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q001_sol_1_95aa3050_03112026.png?v=95aa30501151)

*Bob m whirled on a string of length l about a pivot with angular speed omega; tension T acts towards the pivot*

![drawn: Bob m whirled on a string of length l about a pivot with angular speed omega; tension T acts towards the pivot](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q001_solution_1_a7bff9ab_04112026.svg?v=a7bff9ab78e5)  
*drawn by code/lib/physics_figure.py*

1. $T = m\ell\omega^{2}$

![printed figure: Bob m on a string of length l whirled about a pivot at 2ω, tension T' along the string towards the pivot](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q001_sol_2_0549aafb_03112026.png?v=0549aafb56b9)

*Bob m on a string of length l whirled about a pivot at 2ω, tension T' along the string towards the pivot*

![drawn: Bob m on a string of length l whirled about a pivot at 2ω, tension T' along the string towards the pivot](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q001_solution_2_ae28c5cf_04112026.svg?v=ae28c5cf8164)  
*drawn by code/lib/physics_figure.py*

2. $T' = m\ell(2\omega)^{2}$
3. $T' = 4T$

**Solved independently** (answer withheld)

1. The string tension provides the centripetal force: $T = m\omega^2 r$.
2. With the same radius and angular speed $2\omega$: $T' = m(2\omega)^2 r = 4m\omega^2 r$.
3. $T' = 4T$, which is option $3$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q001_4ebdaac6_03112026.png?v=4ebdaac64e74)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q001_ff50ec16_03112026.png?v=ff50ec1671f5)

---

## Q2

Physics · Current Electricity

A wire of length ‘$l$’ and resistance $100\,\Omega$ is divided into 10 equal parts. The first 5 parts are connected in series while the next 5 parts are connected in parallel. The two combinations are again connected in series. The resistance of this final combination is:

- (1) $60\,\Omega$
- (2) $26\,\Omega$
- **(3)** $52\,\Omega$
- (4) $55\,\Omega$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: A wire with its length l marked by a double-headed arrow](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q002_sol_1_47d2ac89_03112026.png?v=47d2ac89c0bb)

*A wire with its length l marked by a double-headed arrow*

![drawn: A wire with its length l marked by a double-headed arrow](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q002_solution_1_41878819_04112026.svg?v=4187881948bf)  
*drawn by code/lib/physics_figure.py*

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
4. The two combinations in series: $R = R_s + R_p = 50\,\Omega + 2\,\Omega = 52\,\Omega$, which is option $3$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q002_9b7a7f78_03112026.png?v=9b7a7f781476)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q002_98e8621e_03112026.png?v=98e8621e5221)

---

## Q3

Physics · Thermodynamics

A thermodynamic system is taken through the cycle $abcda$. The work done by the gas along the path $bc$ is:

![printed figure: P-V cycle abcda: a rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q003_2938d371_04112026.png?v=2938d37118d3)

*P-V cycle abcda: a rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3*

![drawn: P-V cycle abcda: a rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q003_question_6f28b645_04112026.svg?v=6f28b64503a5)  
*drawn by code/lib/physics_figure.py*

- (1) $-60\,\mathrm{J}$
- **(2)** Zero
- (3) $30\,\mathrm{J}$
- (4) $-90\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Path $bc$ is an isochoric process.
2. $\therefore$ Work done by gas along path $bc$ is zero.

**Solved independently** (answer withheld)

1. From the figure, $b$ and $c$ both lie at $V = 400\,\mathrm{cm^3}$; only $P$ changes from $100\,\mathrm{kPa}$ to $300\,\mathrm{kPa}$.
2. Along $bc$, $dV = 0$, so $W_{bc} = \int P\,dV = 0$, which is option $2$.

**Subtopic:** Isochoric Process · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q003_11f5cd68_03112026.png?v=11f5cd6830be)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q003_70298c41_03112026.png?v=70298c41d7dd)

---

## Q4

Physics · Semiconductor Electronics

A logic circuit provides the output $Y$ as per the following truth table : The expression for the output $Y$ is :

![printed figure: Truth table with inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q004_9c0baa10_03112026.svg?v=9c0baa10a68c)

*Truth table with inputs A, B and output Y*

![drawn: Truth table with inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q004_question_f4ec2abe_04112026.svg?v=f4ec2abeabe3)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $B$
- (2) $A.B+\overline{A}$
- (3) $A.\overline{B}+\overline{A}$
- **(4)** $\overline{B}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Truth table with inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q004_sol_1_28bbc000_03112026.svg?v=28bbc0009178)

*Truth table with inputs A, B and output Y*

![drawn: Truth table with inputs A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_drawn/q004_solution_1_0a99e0c8_03112026.svg?v=0a99e0c8b542)  
*drawn on the booklet's geometry, checked against its figure spec*

1. According to given truth table, output is independent on value of $A$
2. $\therefore$ Output $Y = \overline{B}$

**Solved independently** (answer withheld)

1. Truth table rows $(A,B,Y)$: $(0,0,1),(0,1,0),(1,0,1),(1,1,0)$.
2. $Y = 1$ only when $B = 0$, and $Y = 0$ whenever $B = 1$, regardless of $A$.
3. Hence $Y = \overline{B}$.
4. Check option $3$: at $A=0, B=1$, $A\cdot\overline{B} + \overline{A} = 1 \neq 0$, so it fails; option $2$ at $A=1,B=1$ gives $1 \neq 0$, so it fails.
5. $Y = \overline{B}$ is option $4$.

**Subtopic:** Logic Gates · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q004_c806837b_03112026.png?v=c806837b4acc)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q004_d58bcdb3_03112026.png?v=d58bcdb34578)

---

## Q5

Physics · Modern Physics

The graph which shows the variation of $\left(\frac{1}{\lambda^2}\right)$ and its kinetic energy, $E$ is (where $\lambda$ is de Broglie wavelength of a free particle):

- **(1)** ![printed figure: Graph of 1/lambda^2 against E: a straight line through the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q005_option_1_d17af294_04112026.png?v=d17af2947983) *Graph of 1/lambda^2 against E: a straight line through the origin O* ![drawn: Graph of 1/lambda^2 against E: a straight line through the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q005_option_1_8f66987e_04112026.svg?v=8f66987e94ce)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Graph of 1/lambda^2 against E: a curve from the origin, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q005_option_2_6fb53c23_04112026.png?v=6fb53c23c880) *Graph of 1/lambda^2 against E: a curve from the origin, concave upward* ![drawn: Graph of 1/lambda^2 against E: a curve from the origin, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q005_option_2_d1df4a2f_04112026.svg?v=d1df4a2f1305)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Option (3): 1/lambda^2 against E falling as a hyperbola-like curve](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q005_option_3_3148494c_04112026.png?v=3148494cee5c) *Option (3): 1/lambda^2 against E falling as a hyperbola-like curve* ![drawn: Option (3): 1/lambda^2 against E falling as a hyperbola-like curve](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q005_option_3_76ce4029_04112026.svg?v=76ce40292ba6)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Graph of 1/lambda^2 against E: a concave-down curve rising from the origin](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q005_option_4_59d1bfa5_04112026.png?v=59d1bfa5b2a6) *Graph of 1/lambda^2 against E: a concave-down curve rising from the origin* ![drawn: Graph of 1/lambda^2 against E: a concave-down curve rising from the origin](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q005_option_4_e4ad976d_04112026.svg?v=e4ad976dbf4e)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. de-Broglie wavelength $\lambda = \frac{h}{P} = \frac{h}{mv} = \frac{h}{\sqrt{2\,mE}}$ where $E = \frac{1}{2}mv^{2}$
2. Squaring both sides,
3. $\lambda^{2} = \frac{h^{2}}{4m^{2}E}$
4. $\Rightarrow \frac{1}{\lambda^{2}} = (\text{constant})\,E$
5. Graph passes through origin with constant slope.

**Solved independently** (answer withheld)

1. For a free particle, $p = \sqrt{2mE}$, so $\lambda = \frac{h}{\sqrt{2mE}}$.
2. Squaring and inverting: $\frac{1}{\lambda^2} = \frac{2mE}{h^2}$.
3. $\frac{1}{\lambda^2} \propto E$, a straight line through the origin, which is option $1$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q005_152c40b3_03112026.png?v=152c40b37f54)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q005_85aa050b_03112026.png?v=85aa050bd928)

---

## Q6

Physics · Modern Physics

If $c$ is the velocity of light in free space, the correct statements about photon among the following are: Choose the correct answer from the options given below:

- (A) The energy of a photon is $E = h\nu$.
- (B) The velocity of a photon is $c$.
- (C) The momentum of a photon, $p = \frac{h\nu}{c}$.
- (D) In a photon-electron collision, both total energy and total momentum are conserved.
- (E) Photon possesses positive charge.

- (1) A, B, D and E only
- (2) A and B only
- **(3)** A, B, C and D only
- (4) A, C and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) If $c$ is the velocity of light
2. so, $E = h\nu$ (Energy of photon)
3. (B) Velocity of photon is equal to velocity of light i.e. $c$.
4. (C) $\lambda = \frac{h}{p}$
5. $p = \frac{h}{\lambda}$
6. $p = \frac{h\nu}{c}$
7. (D) In photon-electron collision both total energy and total momentum are conserved.

**Solved independently** (answer withheld)

1. Statement A: a photon's energy is $E = h\nu$, so A is true.
2. Statement B: a photon travels at $c$ in free space, so B is true.
3. Statement C: momentum $p = \frac{E}{c} = \frac{h\nu}{c}$, so C is true.
4. Statement D: in a photon-electron collision total energy and total momentum are conserved, so D is true.
5. Statement E: a photon carries no charge, so E is false.
6. True set is A, B, C and D, which is option $3$.

**Subtopic:** Photon Energy and Number of Photons · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q006_195b410e_03112026.png?v=195b410e7dc2)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q006_bbf61599_03112026.png?v=bbf6159938e8)

---

## Q7

Physics · Gravitation

The mass of a planet is $\frac{1}{10}$ th that of the earth and its diameter is half that of the earth. The acceleration due to gravity on that planet is:

- **(1)** $3.92\,\mathrm{m\,s^{-2}}$
- (2) $19.6\,\mathrm{m\,s^{-2}}$
- (3) $9.8\,\mathrm{m\,s^{-2}}$
- (4) $4.9\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $g' = \frac{GM'}{R'^{2}} = \frac{GM}{10\left(\frac{R}{2}\right)^{2}}$
2. $= \frac{4}{10}\frac{GM}{R^{2}} = 0.4 \times 9.8$
3. $= 3.92\,\mathrm{m\,s^{-2}}$

**Solved independently** (answer withheld)

1. Surface gravity is $g = \frac{GM}{R^2}$.
2. For the planet, $M' = \frac{M}{10}$ and $R' = \frac{R}{2}$ (diameter halved).
3. $g' = \frac{G(M/10)}{(R/2)^2} = \frac{4}{10}\frac{GM}{R^2} = 0.4\,g$.
4. $g' = 0.4 \times 9.8 = 3.92\,\mathrm{m\,s^{-2}}$, which is option $1$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q007_cdddccd8_03112026.png?v=cdddccd8b169)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q007_89f4a4c2_03112026.png?v=89f4a4c2977f)

---

## Q8

Physics · Units and Measurements

In a vernier callipers, $(N + 1)$ divisions of vernier scale coincide with $N$ divisions of main scale. If 1 MSD represents $0.1\,\mathrm{mm}$, the vernier constant (in cm) is:

- (1) $10(N + 1)$
- (2) $\dfrac{1}{10N}$
- **(3)** $\dfrac{1}{100(N + 1)}$
- (4) $100N$

**Answer** — booklet: (3) · independent solve: (3) · agree

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
4. $VC = \frac{1}{100(N+1)}\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q008_b5991da0_03112026.png?v=b5991da05dbc)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q008_a735c970_03112026.png?v=a735c970b892)

---

## Q9

Physics · Alternating Current

In an ideal transformer, the turns ratio is $\frac{N_P}{N_S} = \frac{1}{2}$. The ratio $V_S : V_P$ is equal to (the symbols carry their usual meaning) :

- (1) $1 : 4$
- (2) $1 : 2$
- **(3)** $2 : 1$
- (4) $1 : 1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. According to transformer ratio,
2. $\frac{V_S}{V_P} = \frac{N_S}{N_P} = 2 : 1$

**Solved independently** (answer withheld)

1. For an ideal transformer, $\frac{V_S}{V_P} = \frac{N_S}{N_P}$.
2. Given $\frac{N_P}{N_S} = \frac{1}{2}$, so $\frac{N_S}{N_P} = 2$.
3. $V_S : V_P = 2 : 1$, which is option $3$.

**Subtopic:** Transformer · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q009_da68e977_03112026.png?v=da68e9772d81)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q009_af6f992b_03112026.png?v=af6f992baa6b)

---

## Q10

Physics · Work, Energy and Power

At any instant of time $t$, the displacement of any particle is given by $2t - 1$ (SI unit) under the influence of force of $5\,\mathrm{N}$. The value of instantaneous power is (in SI unit):

- (1) $6$
- **(2)** $10$
- (3) $5$
- (4) $7$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $x = 2t - 1$
2. $v = \frac{dx}{dt} = 2\,\mathrm{m\,s^{-1}}$
3. $P = F.\,v$
4. $= 2 \times 5 = 10\,\mathrm{W}$

**Solved independently** (answer withheld)

1. Velocity is the time derivative of displacement: $v = \frac{dx}{dt} = \frac{d}{dt}(2t - 1) = 2\,\mathrm{m/s}$.
2. Instantaneous power is $P = F v$.
3. $P = 5\,\mathrm{N} \times 2\,\mathrm{m/s} = 10\,\mathrm{W}$, which is option $2$.

**Subtopic:** Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q010_72b747a9_03112026.png?v=72b747a94385)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q010_1aefb9ee_03112026.png?v=1aefb9ee3b65)

---

## Q11

Physics · Mechanical Properties of Fluids

A thin flat circular disc of radius $4.5\,\mathrm{cm}$ is placed gently over the surface of water. If surface tension of water is $0.07\,\mathrm{N\,m^{-1}}$, then the excess force required to take it away from the surface is

- (1) $99\,\mathrm{N}$
- **(2)** $19.8\,\mathrm{mN}$
- (3) $198\,\mathrm{N}$
- (4) $1.98\,\mathrm{mN}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: A hatched circular disc on water with surface tension T acting upward along its rim](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q011_sol_1_38bf2f6d_03112026.png?v=38bf2f6d2790)

*A hatched circular disc on water with surface tension T acting upward along its rim*

![drawn: A hatched circular disc on water with surface tension T acting upward along its rim](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q011_solution_1_7a74febb_04112026.svg?v=7a74febb6255)  
*drawn by code/lib/physics_figure.py*

1. Excess force $= T \times 2\pi R$
2. $= \frac{7}{100} \times 2 \times 3.14 \times \frac{4.5}{100}$
3. $= 197.82 \times 10^{-4}$
4. $= 19.8 \times 10^{-3}\,\mathrm{N}$
5. $= 19.8\,\mathrm{mN}$

**Solved independently** (answer withheld)

1. The extra force needed is surface tension acting along the contact line, i.e. the disc's circumference: $F = T \cdot 2\pi r$.
2. $r = 4.5\,\mathrm{cm} = 0.045\,\mathrm{m}$, $T = 0.07\,\mathrm{N\,m^{-1}}$.
3. $F = 0.07 \times 2\pi \times 0.045 = 0.07 \times 0.2827 \approx 0.0198\,\mathrm{N}$.
4. $0.0198\,\mathrm{N} = 19.8\,\mathrm{mN}$, which is option $2$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q011_49d0bc9f_03112026.png?v=49d0bc9f3229)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q011_fbfcea1e_03112026.png?v=fbfcea1e4ce5)

---

## Q12

Physics · Rotational Motion

A wheel of a bullock cart is rolling on a level road as shown in the figure below. If its linear speed is $v$ in the direction shown, which one of the following options is correct ($P$ and $Q$ are any highest and lowest points on the wheel, respectively)?

![printed figure: A spoked wheel rolling on level ground with velocity v; P at top, Q at contact point](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q012_9b5c4a7d_04112026.png?v=9b5c4a7d3b76)

*A spoked wheel rolling on level ground with velocity v; P at top, Q at contact point*

![drawn: A spoked wheel rolling on level ground with velocity v; P at top, Q at contact point](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q012_question_ef4de6e9_04112026.svg?v=ef4de6e9d264)  
*drawn by code/lib/physics_figure.py*

- (1) Point $P$ has zero speed
- (2) Point $P$ moves slower than point $Q$
- **(3)** Point $P$ moves faster than point $Q$
- (4) Both the points $P$ and $Q$ move with equal speed

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In the case of pure rolling,

![printed figure: Rolling wheel: top point P moves at 2v, centre at v, contact point Q on the ground](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q012_sol_1_1f35ba8e_03112026.png?v=1f35ba8e2adb)

*Rolling wheel: top point P moves at 2v, centre at v, contact point Q on the ground*

![drawn: Rolling wheel: top point P moves at 2v, centre at v, contact point Q on the ground](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q012_solution_1_0a973c92_04112026.svg?v=0a973c920ec6)  
*drawn by code/lib/physics_figure.py*

2. The topmost point will have velocity $2v$ while point $Q$ i.e. lowest point will have zero velocity.
3. Hence point $P$ moves faster than point $Q$.

**Solved independently** (answer withheld)

1. Rolling without slipping on a level road gives $v = \omega R$.
2. Top point: $v_P = v + \omega R = 2v$.
3. Lowest (contact) point: $v_Q = v - \omega R = 0$.
4. $v_P = 2v > v_Q = 0$, so $P$ moves faster than $Q$, which is option $3$.

**Subtopic:** Rolling Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q012_c4a74718_03112026.png?v=c4a74718b340)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q012_2ef069ca_03112026.png?v=2ef069ca32c0)

---

## Q13

Physics · Electrostatics

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) The potential ($V$) at any axial point, at $2\,\mathrm{m}$ distance ($r$) from the centre of the dipole of dipole moment vector $\vec{P}$ of magnitude, $4 \times 10^{-6}\,\mathrm{C\,m}$, is $\pm 9 \times 10^{3}\,V$. (Take $\frac{1}{4\pi \epsilon_0} = 9 \times 10^{9}$ SI units)
- (Reason R) $V = \pm \frac{2P}{4\pi \epsilon_0 r^2}$, where $r$ is the distance of any axial point, situated at $2\,\mathrm{m}$ from the centre of the dipole.

- (1) A is false but R is true.
- (2) Both A and R are true and R is the correct explanation of A.
- (3) Both A and R are true and R is NOT the correct explanation of A.
- **(4)** A is true but R is false.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The potential $V$ at any point, at distance $r$ from centre of dipole $= \frac{KP\cos\theta}{r^{2}}$
2. At axial point where $\theta = 0^{\circ}$, $V = \frac{KP}{r^{2}} = \frac{9 \times 10^{9} \times 4 \times 10^{-6}}{2^{2}} = 9 \times 10^{3}\,\mathrm{V}$
3. At axial point where $\theta = 180^{\circ}$, $V = \frac{-KP}{r^{2}} = -9 \times 10^{3}\,\mathrm{V}$

**Solved independently** (answer withheld)

1. For a short dipole, potential at an axial point is $V = \pm \frac{1}{4\pi\epsilon_0}\frac{P}{r^2}$.
2. $V = \pm \frac{9\times10^{9} \times 4\times10^{-6}}{2^2}$.
3. $V = \pm \frac{36\times10^{3}}{4} = \pm 9\times10^{3}\,\mathrm{V}$, so Assertion A is true.
4. Reason R uses $V = \pm \frac{2P}{4\pi\epsilon_0 r^2}$, which has an extra factor $2$ (that factor belongs to the axial field $E = \frac{2P}{4\pi\epsilon_0 r^3}$), so R is false.
5. A true, R false, which is option $4$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q013_6d267abe_03112026.png?v=6d267abe63ae)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q013_d2090633_03112026.png?v=d2090633f802)

---

## Q14

Physics · Oscillations

If $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,\mathrm{m}$ represents the motion of a particle executing simple harmonic motion, the amplitude and time period of motion, respectively, are

- (1) $5\,\mathrm{m}$, $1\,\mathrm{s}$
- (2) $5\,\mathrm{cm}$, $2\,\mathrm{s}$
- **(3)** $5\,\mathrm{m}$, $2\,\mathrm{s}$
- (4) $5\,\mathrm{cm}$, $1\,\mathrm{s}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,\mathrm{m}$
2. Amplitude $= 5\,\mathrm{m}$
3. $\omega = \pi = \frac{2\pi}{T}$
4. $T = \frac{2\pi}{\pi} = 2\,\mathrm{s}$

**Solved independently** (answer withheld)

1. Compare with $x = A\sin(\omega t + \phi)$: $A = 5\,\mathrm{m}$ and $\omega = \pi\,\mathrm{rad\,s^{-1}}$.
2. $T = \frac{2\pi}{\omega} = \frac{2\pi}{\pi} = 2\,\mathrm{s}$.
3. Amplitude $5\,\mathrm{m}$ and period $2\,\mathrm{s}$, which is option $3$.

**Subtopic:** Calculate Time Period of SHM, Calculate Amplitude of SHM · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q014_c4fc8d7d_03112026.png?v=c4fc8d7d832d)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q014_5b66fedf_03112026.png?v=5b66fedf32f4)

---

## Q15

Physics · Wave Optics

An unpolarised light beam strikes a glass surface at Brewster's angle. Then

- **(1)** The reflected light will be completely polarised but the refracted light will be partially polarised.
- (2) The reflected light will be partially polarised.
- (3) The refracted light will be completely polarised.
- (4) Both the reflected and refracted light will be completely polarised.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Unpolarised light incident at Brewster's angle: reflected, refracted rays with polarisation marks](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q015_sol_1_5ed2db8b_03112026.png?v=5ed2db8b327c)

*Unpolarised light incident at Brewster's angle: reflected, refracted rays with polarisation marks*

![drawn: Unpolarised light incident at Brewster's angle: reflected, refracted rays with polarisation marks](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q015_solution_1_3b99caf5_04112026.svg?v=3b99caf58f38)  
*drawn by code/lib/physics_figure.py*

1. According to Brewster's law, reflected rays are completely polarized and refracted rays are partially polarized.

**Solved independently** (answer withheld)

1. At Brewster's angle $i_B$ with $\tan i_B = \mu$, the reflected ray is completely plane polarised and the refracted ray is partially polarised, so option $1$.

**Subtopic:** Brewster's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q015_ebc8a073_03112026.png?v=ebc8a073b183)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q015_683ecbb6_03112026.png?v=683ecbb690bb)

---

## Q16

Physics · Units and Measurements

The quantities which have the same dimensions as those of solid angle are:

- (1) angular speed and stress
- **(2)** strain and angle
- (3) stress and angle
- (4) strain and arc

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Solid angle $d\Omega = \frac{dA}{r^{2}}$ has dimensions $[\mathrm{M^{0}L^{0}T^{0}}]$
2. Strain $= \frac{\Delta l}{l}$ has dimensions $[\mathrm{M^{0}L^{0}T^{0}}]$
3. Angle measured in radians is also dimensionless $[\mathrm{M^{0}L^{0}T^{0}}]$
4. $\theta = \frac{l}{r}$

**Solved independently** (answer withheld)

1. Solid angle $\Omega = \frac{A}{r^2}$, so $[\Omega] = \frac{[L^2]}{[L^2]} = [M^0 L^0 T^0]$ (dimensionless).
2. Strain $= \frac{\Delta l}{l}$, so $[\text{strain}] = [M^0 L^0 T^0]$.
3. Plane angle $\theta = \frac{s}{r}$, so $[\theta] = [M^0 L^0 T^0]$.
4. Stress $= \frac{F}{A}$ has $[M L^{-1} T^{-2}]$, angular speed has $[T^{-1}]$ and arc has $[L]$, so options $1$, $3$ and $4$ fail.
5. Only strain and angle are dimensionless like solid angle, which is option $2$.

**Subtopic:** Dimensional Formulae · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q016_7f2a5d2d_03112026.png?v=7f2a5d2d3d8a)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q016_1e5001eb_03112026.png?v=1e5001eb7565)

---

## Q17

Physics · Magnetic Effect of Electric Current

In a uniform magnetic field of $0.049\,\mathrm{T}$, a magnetic needle performs 20 complete oscillations in $5$ seconds as shown. The moment of inertia of the needle is $9.8 \times 10^{-6}\,\mathrm{kg\,m^2}$. If the magnitude of magnetic moment of the needle is $x \times 10^{-5}\,\mathrm{Am^2}$, then the value of '$x$' is :

![printed figure: A magnetic needle NS hung by a thread from a fixed support in a uniform field B](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q017_df699485_03112026.png?v=df6994856f3e)

*A magnetic needle NS hung by a thread from a fixed support in a uniform field B*

![drawn: A magnetic needle NS hung by a thread from a fixed support in a uniform field B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q017_question_e4b33b92_04112026.svg?v=e4b33b920317)  
*drawn by code/lib/physics_figure.py*

- **(1)** $1280\pi^2$
- (2) $5\pi^2$
- (3) $128\pi^2$
- (4) $50\pi^2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Time period of Oscillation, $T = 2\pi\sqrt{\frac{I}{MB}}$
2. $\Rightarrow \frac{1}{4} = 2\pi\sqrt{\frac{9.8\times10^{-6}}{M\times0.049}}$
3. $\Rightarrow \frac{1}{16} = 4\pi^{2}\times\frac{9.8\times10^{-6}}{M\times49\times10^{-3}}$
4. $\Rightarrow M = \frac{4\pi^{2}\times9.8\times10^{-6}}{49\times10^{-3}}\times16$
5. $= \frac{4\pi^{2}\times9.8\times16\times10^{-3}}{49}$
6. $= 12.8\pi^{2}\times10^{-3}\times10^{-2}\times10^{2}$
7. $= 1280\pi^{2}\times10^{-5}\,\mathrm{Am^{2}}$

**Solved independently** (answer withheld)

1. Time period: $T = \frac{5\,\mathrm{s}}{20} = 0.25\,\mathrm{s}$.
2. For an oscillating magnetic needle, $T = 2\pi\sqrt{\frac{I}{MB}}$.
3. Rearranging: $M = \frac{4\pi^2 I}{B T^2}$.
4. $B T^2 = 0.049 \times 0.0625 = 3.0625 \times 10^{-3}$.
5. $\frac{I}{BT^2} = \frac{9.8 \times 10^{-6}}{3.0625 \times 10^{-3}} = 3.2 \times 10^{-3}$.
6. $M = 4\pi^2 \times 3.2 \times 10^{-3} = 12.8\pi^2 \times 10^{-3} = 1280\pi^2 \times 10^{-5}\,\mathrm{Am^2}$.
7. So $x = 1280\pi^2$, which is option $1$.

**Subtopic:** The Dipole in a Uniform Magnetic Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q017_1513bae0_03112026.png?v=1513bae05114)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q017_99bb2cf6_03112026.png?v=99bb2cf6cc4e)

---

## Q18

Physics · Electrostatics

A thin spherical shell is charged by some source. The potential difference between the two points $C$ and $P$ (in V) shown in the figure is: (Take $\frac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}$ SI units)

![printed figure: Charged thin spherical shell of radius R with centre C and point P on the shell](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q018_41a34a41_04112026.png?v=41a34a41b762)

*Charged thin spherical shell of radius R with centre C and point P on the shell*

![drawn: Charged thin spherical shell of radius R with centre C and point P on the shell](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q018_question_06b41955_04112026.svg?v=06b419557ff6)  
*drawn by code/lib/physics_figure.py*

- **(1)** Zero
- (2) $3 \times 10^{5}$
- (3) $1 \times 10^{5}$
- (4) $0.5 \times 10^{5}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For uniformly charged spherical shell,
2. $V = \frac{kq}{R}$ (For $r \leq R$)
3. $\therefore\ V_C = V_P$
4. $V_C - V_P =$ Zero

**Solved independently** (answer withheld)

1. Inside a charged conducting/thin spherical shell $E = 0$, so the potential is the same everywhere inside and equals the surface value.
2. $V_C = \frac{1}{4\pi\varepsilon_0}\frac{q}{R} = \frac{9\times10^{9}\times10^{-6}}{0.03} = 3\times10^{5}\,\text{V}$.
3. $P$ lies on the shell, so $V_P = \frac{1}{4\pi\varepsilon_0}\frac{q}{R} = 3\times10^{5}\,\text{V}$.
4. $V_C - V_P = 0$, which is option $1$.

**Subtopic:** Electrostatic Potential Throughout the Volume of a Conductor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q018_a70b45e5_03112026.png?v=a70b45e58db3)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q018_d3931302_03112026.png?v=d39313029dde)

---

## Q19

Physics · Rotational Motion

The moment of inertia of a thin rod about an axis passing through its mid point and perpendicular to the rod is $2400\,\mathrm{g\,cm^{2}}$. The length of the $400\,\mathrm{g}$ rod is nearly:

- (1) $72.0\,\mathrm{cm}$
- **(2)** $8.5\,\mathrm{cm}$
- (3) $17.5\,\mathrm{cm}$
- (4) $20.7\,\mathrm{cm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Moment of inertia of rod $= I = \frac{m\ell^{2}}{12}$
2. $\Rightarrow 2400 = 400\frac{\ell^{2}}{12}$
3. $\Rightarrow 72 = \ell^{2}$
4. $\Rightarrow \ell = \sqrt{72} = 8.48\,\mathrm{cm} \simeq 8.5\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. For a thin rod about a perpendicular axis through its midpoint, $I = \frac{ML^{2}}{12}$.
2. $L^{2} = \frac{12I}{M} = \frac{12 \times 2400\,\mathrm{g\,cm^{2}}}{400\,\mathrm{g}} = 72\,\mathrm{cm^{2}}$.
3. $L = \sqrt{72}\,\mathrm{cm} \approx 8.49\,\mathrm{cm} \approx 8.5\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Moment of Inertia of a Uniform Rod · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 9)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q019_489c9a9e_03112026.png?v=489c9a9e6b96)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q019_bd14714c_03112026.png?v=bd14714cd463)

---

## Q20

Physics · Modern Physics

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below.

- (Statement I) Atoms are electrically neutral as they contain equal number of positive and negative charges.
- (Statement II) Atoms of each element are stable and emit their characteristic spectrum.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Statement I is true as atoms are electrically neutral because they contain equal number of positive and negative charges.
2. Statement II is wrong as atom of most of the elements are stable and emit characteristic spectrum.
3. But this statement is not true for every atom.

**Solved independently** (answer withheld)

1. Statement I: a neutral atom has $Z$ protons and $Z$ electrons, so net charge $= Ze - Ze = 0$; Statement I is correct.
2. Statement II: an atom emits radiation only when an electron goes from a higher level to a lower one, $h\nu = E_2 - E_1$, which needs prior excitation.
3. An atom that is stable in its ground state does not emit, so 'stable and emit their characteristic spectrum' is incorrect as a general claim.
4. Statement I correct, Statement II incorrect, which is option $4$.

**Subtopic:** Alpha-Particle Scattering and Rutherford Nuclear Model of the Atom and Thomson's Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q020_e5670120_03112026.png?v=e5670120e4a5)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q020_17ba5942_03112026.png?v=17ba5942df88)

---

## Q21

Physics · Modern Physics

Match List I with List II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $n_2 = 3$ to $n_1 = 2$ | I | $410.2$ |
| B | $n_2 = 4$ to $n_1 = 2$ | II | $434.1$ |
| C | $n_2 = 5$ to $n_1 = 2$ | III | $656.3$ |
| D | $n_2 = 6$ to $n_1 = 2$ | IV | $486.1$ |

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-I, C-IV, D-III
- **(3)** A-III, B-IV, C-II, D-I
- (4) A-IV, B-III, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Energy difference $\Delta E = \frac{hc}{\lambda}$
2. $\therefore \lambda \propto \frac{1}{\Delta E}$
3. $(\Delta E)_{6-2} > (\Delta E)_{5-2} > (\Delta E)_{4-2} > (\Delta E)_{3-2}$
4. $\lambda_{6-2} < \lambda_{5-2} < \lambda_{4-2} < \lambda_{3-2}$
5. A-III, B-IV, C-II, D-I

**Solved independently** (answer withheld)

1. All transitions end at $n_1 = 2$, so they are Balmer lines with $\frac{1}{\lambda} = R\left(\frac{1}{2^2} - \frac{1}{n_2^2}\right)$.
2. A larger $n_2$ gives a larger energy gap, hence a shorter wavelength.
3. $n_2 = 3$: $\frac{1}{\lambda} = R\cdot\frac{5}{36}$, $\lambda = \frac{36}{5 \times 1.097\times10^{7}}\,\text{m} \approx 656.3\,\text{nm}$, so A-III.
4. $n_2 = 4$: $\lambda = \frac{16}{3R} \approx 486.1\,\text{nm}$, so B-IV.
5. $n_2 = 5$: $\lambda = \frac{100}{21R} \approx 434.1\,\text{nm}$, so C-II.
6. $n_2 = 6$: $\lambda = \frac{36}{8R} = \frac{9}{2R} \approx 410.2\,\text{nm}$, so D-I.
7. A-III, B-IV, C-II, D-I is option $3$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q021_7d4bd22e_03112026.png?v=7d4bd22e90ea)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q021_2eb2739c_03112026.png?v=2eb2739c4434)

---

## Q22

Physics · Magnetic Effect of Electric Current

Match List-I with List-II. List-I (Material) List-II (Susceptibility ($\chi$)) Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| A | Diamagnetic | I | $\chi = 0$ |
| B | Ferromagnetic | II | $0 > \chi \geq -1$ |
| C | Paramagnetic | III | $\chi >> 1$ |
| D | Non-magnetic | IV | $0 < \chi < \varepsilon$ (a small positive number) |

- (1) A-IV, B-III, C-II, D-I
- **(2)** A-II, B-III, C-IV, D-I
- (3) A-II, B-I, C-III, D-IV
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (Material) | (Susceptibility ($\chi$))
2. Diamagnetic | (II) | $0 > \chi \geq -1$
3. Ferromagnetic | (III) | $\chi >> 1$
4. Paramagnetic | (IV) | $0 < \chi < \varepsilon$
5. Non-magnetic | (I) | $\chi = 0$

**Solved independently** (answer withheld)

1. Diamagnetic materials have a small negative susceptibility, $-1 \leq \chi < 0$, so A matches II.
2. Ferromagnetic materials have a very large positive susceptibility, $\chi \gg 1$, so B matches III.
3. Paramagnetic materials have a small positive susceptibility, $0 < \chi < \varepsilon$, so C matches IV.
4. Non-magnetic materials have $\chi = 0$, so D matches I.
5. A-II, B-III, C-IV, D-I is option $2$.

**Subtopic:** Magnetism and Matter · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q022_e5973ccf_03112026.png?v=e5973ccf6c90)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q022_e87a5194_03112026.png?v=e87a519417f6)

---

## Q23

Physics · Semiconductor Electronics

Consider the following statements A and B and identify the correct answer:

![printed figure: I-V axes with the four quadrants (I) to (IV) marked](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q023_0dd5a28c_03112026.png?v=0dd5a28ca73f)

*I-V axes with the four quadrants (I) to (IV) marked*

![drawn: I-V axes with the four quadrants (I) to (IV) marked](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q023_question_ffc4eccf_04112026.svg?v=ffc4eccf8860)  
*drawn by code/lib/physics_figure.py*

- (A) For a solar-cell, the I-V characteristics lies in the IV quadrant of the given graph.
- (B) In a reverse biased $pn$ junction diode, the current measured in ($\mu\mathrm{A}$), is due to majority charge carriers.

- (1) Both A and B are incorrect
- **(2)** A is correct but B is incorrect
- (3) A is incorrect but B is correct
- (4) Both A and B are correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A: Solar cell characteristics

![printed figure: Solar cell I-V characteristic in the fourth quadrant, from I_SC on the current axis to V_OC on the voltage axis](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q023_sol_1_44eb5ec1_03112026.png?v=44eb5ec122bd)

*Solar cell I-V characteristic in the fourth quadrant, from I_SC on the current axis to V_OC on the voltage axis*

![drawn: Solar cell I-V characteristic in the fourth quadrant, from I_SC on the current axis to V_OC on the voltage axis](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q023_solution_1_a2fe7ef6_04112026.svg?v=a2fe7ef6d292)  
*drawn by code/lib/physics_figure.py*

2. B: In reverse biased $pn$ junction diode, the current measured in ($\mu\mathrm{A}$), is due to minority charge carrier.

**Solved independently** (answer withheld)

1. A solar cell supplies power: open-circuit voltage $V > 0$ while short-circuit current $I < 0$, so its $I$-$V$ characteristic lies in quadrant $\mathrm{IV}$; statement A is correct.
2. In reverse bias the small current ($\mu\mathrm{A}$) is the drift of minority carriers across the junction, not majority carriers; statement B is incorrect.
3. A correct, B incorrect, which is option $2$.

**Subtopic:** Special Purpose PN Junction Diodes, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q023_21d5849b_03112026.png?v=21d5849bea48)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q023_965332c2_03112026.png?v=965332c275cd)

---

## Q24

Physics · Wave Optics

If the monochromatic source in Young’s double slit experiment is replaced by white light, then

- (1) All bright fringes will be of equal width
- (2) Interference pattern will disappear
- (3) There will be a central dark fringe surrounded by a few coloured fringes
- **(4)** There will be a central bright white fringe surrounded by a few coloured fringes

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. At central point on screen, path difference is zero for all wavelength.
2. So, central bright fringe is white and other fringes depend on wavelength as $\beta = \frac{\lambda D}{d}$.
3. Therefore, other fringes will be coloured.

**Solved independently** (answer withheld)

1. At the central point the path difference is $\Delta x = 0$ for every wavelength $\lambda$.
2. So every colour has a maximum there, and their overlap gives a central bright white fringe.
3. Fringe width $\beta = \frac{\lambda D}{d}$ differs for each $\lambda$, so away from the centre the maxima separate into a few coloured fringes, which is option $4$.

**Subtopic:** Young's Double-Slit Experiment (YDSE) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q024_31d495a6_03112026.png?v=31d495a63997)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q024_214e76ce_03112026.png?v=214e76cea0aa)

---

## Q25

Physics · Ray Optics

A light ray enters through a right angled prism at point $P$ with the angle of incidence $30^\circ$ as shown in figure. It travels through the prism parallel to its base $BC$ and emerges along the face $AC$. The refractive index of the prism is:

![printed figure: Right-angled prism ABC: ray incident at P at 30 degrees to the normal, travels parallel to BC and emerges along face AC](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q025_aef5da70_03112026.png?v=aef5da7072e5)

*Right-angled prism ABC: ray incident at P at 30 degrees to the normal, travels parallel to BC and emerges along face AC*

![drawn: Right-angled prism ABC: ray incident at P at 30 degrees to the normal, travels parallel to BC and emerges along face AC](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q025_question_b3740dc3_04112026.svg?v=b3740dc3f0b6)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{\sqrt{3}}{2}$
- (2) $\frac{\sqrt{5}}{4}$
- **(3)** $\frac{\sqrt{5}}{2}$
- (4) $\frac{\sqrt{3}}{4}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Ray through a right-angled prism: incidence 30 deg, refraction r1, critical angle c at the second face](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q025_sol_1_7a1197fd_03112026.png?v=7a1197fd2fe3)

*Ray through a right-angled prism: incidence 30 deg, refraction r1, critical angle c at the second face*

![drawn: Ray through a right-angled prism: incidence 30 deg, refraction r1, critical angle c at the second face](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q025_solution_1_dade22ec_04112026.svg?v=dade22ec2d09)  
*drawn by code/lib/physics_figure.py*

1. $A = 90^\circ$
2. In prism, $r_1 + c = A$
3. $r_1 = 90^\circ - c$ $\quad\ldots(1)$
4. $\sin c = \frac{1}{\mu} \Rightarrow \cos c = \frac{\sqrt{\mu^2 - 1}}{\mu}$
5. $\Rightarrow$ Apply Snell's law, on incidence surface
6. $1\cdot\sin 30^\circ = \mu\sin(r_1) \Rightarrow 1\times\frac{1}{2} = \mu\times\sin(90^\circ - c)$
7. $\frac{1}{2} = \mu\times\frac{\sqrt{\mu^2 - 1}}{\mu}$
8. On squaring $\frac{1}{4} = \mu^2 - 1$
9. $\Rightarrow \mu^2 = \frac{5}{4} \Rightarrow \mu = \frac{\sqrt{5}}{2}$

**Solved independently** (answer withheld)

1. The prism angle at $A$ is $90^\circ$, so the refraction angles inside satisfy $r_1 + r_2 = A = 90^\circ$.
2. Snell's law at $P$: $\sin 30^\circ = \mu \sin r_1 \Rightarrow \sin r_1 = \frac{1}{2\mu}$.
3. The ray emerges along face $AC$ (grazing), so at that face $r_2 = \theta_c$ with $\sin r_2 = \frac{1}{\mu}$.
4. Since $r_2 = 90^\circ - r_1$, $\cos r_1 = \frac{1}{\mu}$.
5. $\sin^2 r_1 + \cos^2 r_1 = 1 \Rightarrow \frac{1}{4\mu^2} + \frac{1}{\mu^2} = 1 \Rightarrow \mu^2 = \frac{5}{4}$.
6. $\mu = \frac{\sqrt{5}}{2}$, which is option $3$.

**Subtopic:** Prism, Total Internal Reflection (TIR) · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 11)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q025_72221cc0_03112026.png?v=72221cc0c14d)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q025_9b2d8fcc_03112026.png?v=9b2d8fccceb1)

---

## Q26

Physics · Current Electricity

The terminal voltage of the battery, whose emf is $10\,\mathrm{V}$ and internal resistance $1\,\Omega$, when connected through an external resistance of $4\,\Omega$ as shown in the figure is:

![printed figure: A 10 V cell with internal resistance 1 ohm (dashed box) connected across an external 4 ohm resistor](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q026_946bde51_04112026.png?v=946bde518501)

*A 10 V cell with internal resistance 1 ohm (dashed box) connected across an external 4 ohm resistor*

![drawn: A 10 V cell with internal resistance 1 ohm (dashed box) connected across an external 4 ohm resistor](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q026_question_03bd5e35_04112026.svg?v=03bd5e35f439)  
*drawn by code/lib/physics_figure.py*

- (1) $10\,\mathrm{V}$
- (2) $4\,\mathrm{V}$
- (3) $6\,\mathrm{V}$
- **(4)** $8\,\mathrm{V}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: A 10 V cell with 1 ohm internal resistance in series with a 4 ohm resistor, current i](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q026_sol_1_aaf7cd9f_03112026.png?v=aaf7cd9f25bd)

*A 10 V cell with 1 ohm internal resistance in series with a 4 ohm resistor, current i*

![drawn: A 10 V cell with 1 ohm internal resistance in series with a 4 ohm resistor, current i](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q026_solution_1_22dd6e1e_04112026.svg?v=22dd6e1e308d)  
*drawn by code/lib/physics_figure.py*

1. Current in circuit $i = \frac{10}{4+1} = 2\,\mathrm{A}$
2. Terminal voltage $= E - iR$
3. $= 10 - 2 \times 1 = 8\,\mathrm{V}$

**Solved independently** (answer withheld)

1. The figure shows the battery discharging through the external resistor, with $R = 4\,\Omega$ in series with $r = 1\,\Omega$.
2. $I = \frac{E}{R + r} = \frac{10}{4 + 1} = 2\,\mathrm{A}$.
3. $V = E - Ir = 10 - 2 \times 1 = 8\,\mathrm{V}$.
4. Check: $V = IR = 2 \times 4 = 8\,\mathrm{V}$, which is option $4$.

**Subtopic:** Terminal Potential Difference · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q026_652debb0_03112026.png?v=652debb09026)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q026_560b7e2b_03112026.png?v=560b7e2bc726)

---

## Q27

Physics · Laws of Motion

A horizontal force $10\,\mathrm{N}$ is applied to a block $A$ as shown in figure. The mass of blocks $A$ and $B$ are $2\,\mathrm{kg}$ and $3\,\mathrm{kg}$ respectively. The blocks slide over a frictionless surface. The force exerted by block $A$ on block $B$ is :

![printed figure: Horizontal force F = 10 N pushes block A (2 kg) against block B (3 kg) on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q027_e3b95f86_03112026.png?v=e3b95f86f9ed)

*Horizontal force F = 10 N pushes block A (2 kg) against block B (3 kg) on a frictionless floor*

![drawn: Horizontal force F = 10 N pushes block A (2 kg) against block B (3 kg) on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q027_question_0e4cc221_04112026.svg?v=0e4cc221b5f8)  
*drawn by code/lib/physics_figure.py*

- (1) $10\,\mathrm{N}$
- (2) Zero
- (3) $4\,\mathrm{N}$
- **(4)** $6\,\mathrm{N}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $F = (M_1 + M_2)a$
2. $a = \frac{10}{2 + 3} = 2\,\mathrm{m\,s^{-2}}$
3. $F' = M_2(2) = 3 \times 2\,\mathrm{N} = 6\,\mathrm{N}$

**Solved independently** (answer withheld)

1. Both blocks move together on the frictionless surface, so $a = \frac{F}{m_A + m_B} = \frac{10}{2+3} = 2\,\mathrm{m/s^2}$.
2. The only horizontal force on $B$ is the contact force from $A$: $N = m_B a$.
3. $N = 3 \times 2 = 6\,\mathrm{N}$, which is option $4$.

**Subtopic:** Block Problem · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q027_d62df091_03112026.png?v=d62df091fa7e)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q027_35863a3e_03112026.png?v=35863a3ead92)

---

## Q28

Physics · Work, Energy and Power

Two bodies $A$ and $B$ of same mass undergo completely inelastic one dimensional collision. The body $A$ moves with velocity $v_1$ while body $B$ is at rest before collision. The velocity of the system after collision is $v_2$. The ratio $v_1 : v_2$ is

- (1) $1 : 4$
- (2) $1 : 2$
- **(3)** $2 : 1$
- (4) $4 : 1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Before collision $\Rightarrow$

![printed figure: Body A moving with velocity v1 towards body B at rest](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q028_sol_1_7d39f5aa_03112026.png?v=7d39f5aa9865)

*Body A moving with velocity v1 towards body B at rest*

![drawn: Body A moving with velocity v1 towards body B at rest](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q028_solution_1_5a47e557_04112026.svg?v=5a47e55754b9)  
*drawn by code/lib/physics_figure.py*

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
4. $v_1 : v_2 = 2 : 1$, which is option $3$.

**Subtopic:** Problems on Inelastic Collision · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q028_99462e37_03112026.png?v=99462e3753d3)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q028_0100b4e4_03112026.png?v=0100b4e40411)

---

## Q29

Physics · Semiconductor Electronics

The output $(Y)$ of the given logic gate is similar to the output of an/a

![printed figure: NAND gate (inputs tied, fed by A) and NOR gate (inputs tied, fed by B) driving a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q029_8261e980_03112026.png?v=8261e9809ee7)

*NAND gate (inputs tied, fed by A) and NOR gate (inputs tied, fed by B) driving a NOR gate with output Y*

![drawn: NAND gate (inputs tied, fed by A) and NOR gate (inputs tied, fed by B) driving a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q029_question_9ead08fa_04112026.svg?v=9ead08fa8720)  
*drawn by code/lib/physics_figure.py*

- **(1)** AND gate
- (2) NAND gate
- (3) NOR gate
- (4) OR gate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: NAND gate with both inputs tied to A (output Y1) and NOR gate with both inputs tied to B (output Y2), feeding a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q029_sol_1_3fdd039b_03112026.png?v=3fdd039bffe3)

*NAND gate with both inputs tied to A (output Y1) and NOR gate with both inputs tied to B (output Y2), feeding a NOR gate with output Y*

![drawn: NAND gate with both inputs tied to A (output Y1) and NOR gate with both inputs tied to B (output Y2), feeding a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q029_solution_1_1935ed14_04112026.svg?v=1935ed148214)  
*drawn by code/lib/physics_figure.py*

1. $Y_1 = \overline{A \cdot A}$
2. $= \overline{A}$
3. $Y_2 = \overline{B + B}$
4. $= \overline{B}$
5. $Y = \overline{Y_1 + Y_2}$
6. $= \overline{\overline{A} + \overline{B}}$
7. $= \overline{\overline{A}} \cdot \overline{\overline{B}}$
8. $= A.B$ is similar to output of AND Gate

**Solved independently** (answer withheld)

1. A NAND gate with both inputs tied to $A$ gives $\overline{A \cdot A} = \overline{A}$.
2. A NOR gate with both inputs tied to $B$ gives $\overline{B + B} = \overline{B}$.
3. The final NOR gate gives $Y = \overline{\overline{A} + \overline{B}}$.
4. By De Morgan's theorem, $\overline{\overline{A} + \overline{B}} = A \cdot B$, which is an AND gate, option $1$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q029_935551e1_03112026.png?v=935551e129b8)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q029_09c4098b_03112026.png?v=09c4098be0ec)

---

## Q30

Physics · Capacitance

In the following circuit, the equivalent capacitance between terminal $A$ and terminal $B$ is :

![printed figure: Five 2 uF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q030_f4856db3_04112026.png?v=f4856db34bca)

*Five 2 uF capacitors in a bridge between terminals A and B*

![drawn: Five 2 uF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q030_question_26acdcfa_04112026.svg?v=26acdcfa0028)  
*drawn by code/lib/physics_figure.py*

- (1) $4\,\mu\mathrm{F}$
- **(2)** $2\,\mu\mathrm{F}$
- (3) $1\,\mu\mathrm{F}$
- (4) $0.5\,\mu\mathrm{F}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Five 2 μF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q030_sol_1_1527d1e0_03112026.png?v=1527d1e08ecb)

*Five 2 μF capacitors in a bridge between terminals A and B*

![drawn: Five 2 μF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q030_solution_1_4236c0b4_04112026.svg?v=4236c0b47dc8)  
*drawn by code/lib/physics_figure.py*

1. Given circuit is balanced Wheatstone bridge

![printed figure: Two branches between A and B, each with two 2 uF capacitors in series](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q030_sol_2_98addef4_03112026.png?v=98addef4d10a)

*Two branches between A and B, each with two 2 uF capacitors in series*

![drawn: Two branches between A and B, each with two 2 uF capacitors in series](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q030_solution_2_d41304f9_04112026.svg?v=d41304f9afb2)  
*drawn by code/lib/physics_figure.py*

2. $C_{AB} = 1 + 1$
3. $= 2\,\mu\mathrm{F}$

**Solved independently** (answer withheld)

1. The circuit is a Wheatstone bridge: $A$ to the top and bottom middle nodes through $2\,\mu F$ each, those nodes to $B$ through $2\,\mu F$ each, and a $2\,\mu F$ capacitor joining the two middle nodes.
2. Balance condition: $\frac{C_1}{C_2} = \frac{2}{2} = \frac{C_3}{C_4} = \frac{2}{2}$, so the middle nodes are at equal potential and the middle capacitor holds no charge.
3. Each branch is two $2\,\mu F$ capacitors in series: $C_s = \frac{2 \times 2}{2 + 2} = 1\,\mu F$.
4. The two branches are in parallel: $C_{AB} = 1 + 1 = 2\,\mu F$, which is option $2$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q030_f06f0363_03112026.png?v=f06f0363bdaf)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q030_1961f59e_03112026.png?v=1961f59e8b17)

---

## Q31

Physics · Kinematics

A particle moving with uniform speed in a circular path maintains:

- **(1)** Varying velocity and varying acceleration
- (2) Constant velocity
- (3) Constant acceleration
- (4) Constant velocity but varying acceleration

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A particle moving with uniform speed in a circular path maintains varying velocity and varying acceleration.
2. It is because direction of both velocity as well as acceleration will change continuously.

**Solved independently** (answer withheld)

1. Speed $|\vec v|$ is constant, but $\vec v$ is tangential and its direction changes continuously, so velocity varies.
2. Acceleration $a = \frac{v^2}{r}$ is constant in magnitude but always points towards the centre, so its direction changes and $\vec a$ varies.
3. Both velocity and acceleration vary, which is option $1$.

**Subtopic:** Uniform Circular Motion · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 14)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q031_ddbd3a31_03112026.png?v=ddbd3a310d40)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q031_3a7ee71b_03112026.png?v=3a7ee71b45e6)

---

## Q32

Physics · Mechanical Properties of Solids

The maximum elongation of a steel wire of $1\,\mathrm{m}$ length if the elastic limit of steel and its Young’s modulus, respectively, are $8 \times 10^{8}\,\mathrm{N\,m^{-2}}$ and $2 \times 10^{11}\,\mathrm{N\,m^{-2}}$, is:

- (1) $8\,\mathrm{mm}$
- **(2)** $4\,\mathrm{mm}$
- (3) $0.4\,\mathrm{mm}$
- (4) $40\,\mathrm{mm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In the case for maximum elongation,
2. Stress = Elastic limit
3. $\delta_{\mathrm{max}} = \frac{\sigma_{\mathrm{elastic}} \times L}{\text{Young's modulus}} = \frac{8 \times 10^{8} \times 1}{2 \times 10^{11}} = 4 \times 10^{-3}$
4. $= 4\,\mathrm{mm}$
5. i.e. maximum elongation is $4\,\mathrm{mm}$

**Solved independently** (answer withheld)

1. Maximum stress the wire can take elastically is the elastic limit, $\sigma = 8 \times 10^{8}\,\mathrm{N\,m^{-2}}$.
2. Maximum strain $= \frac{\sigma}{Y} = \frac{8 \times 10^{8}}{2 \times 10^{11}} = 4 \times 10^{-3}$.
3. $\Delta L = \text{strain} \times L = 4 \times 10^{-3} \times 1\,\mathrm{m} = 4 \times 10^{-3}\,\mathrm{m} = 4\,\mathrm{mm}$, which is option $2$.

**Subtopic:** Hooke's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q032_ae09ee5b_03112026.png?v=ae09ee5b6cf8)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q032_9b907010_03112026.png?v=9b9070105143)

---

## Q33

Physics · Modern Physics

$^{290}_{82}X \xrightarrow{\alpha} Y \xrightarrow{e^{+}} Z \xrightarrow{\beta^{-}} P \xrightarrow{e^{-}} Q$
In the nuclear emission stated above, the mass number and atomic number of the product $Q$ respectively, are

- **(1)** 286, 81
- (2) 280, 81
- (3) 286, 80
- (4) 288, 82

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $^{290}_{82}X \xrightarrow{\alpha} {}^{286}_{80}Y \xrightarrow{e^{+}} {}^{286}_{79}Z \xrightarrow{\beta^{-}} {}^{286}_{80}P \xrightarrow{e^{-}} {}^{286}_{81}Q$
2. $A \rightarrow 286$
3. $Z = 81$

**Solved independently** (answer withheld)

1. $\alpha$ decay: $A = 290 - 4 = 286$, $Z = 82 - 2 = 80$, so $Y = {}^{286}_{80}Y$.
2. Positron ($e^{+}$) emission: $A$ unchanged, $Z = 80 - 1 = 79$, so $Z = {}^{286}_{79}Z$.
3. $\beta^{-}$ emission: $A$ unchanged, $Z = 79 + 1 = 80$, so $P = {}^{286}_{80}P$.
4. Electron ($e^{-}$) emission is another $\beta^{-}$ decay: $Z = 80 + 1 = 81$, so $Q = {}^{286}_{81}Q$.
5. Mass number $286$, atomic number $81$, which is option $1$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q033_05a9a725_03112026.png?v=05a9a72511d1)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q033_b806c343_03112026.png?v=b806c34314c6)

---

## Q34

Physics · Electromagnetic Induction

In the above diagram, a strong bar magnet is moving towards solenoid-2 from solenoid-1. The direction of induced current in solenoid-1 and that in solenoid-2, respectively, are through the directions:

![printed figure: Bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q034_76d5b7a2_04112026.png?v=76d5b7a2ff59)

*Bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)*

![drawn: Bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q034_question_604afcfc_04112026.svg?v=604afcfceea6)  
*drawn by code/lib/physics_figure.py*

- (1) $BA$ and $DC$
- **(2)** $AB$ and $DC$
- (3) $BA$ and $CD$
- (4) $AB$ and $CD$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Bar magnet moving with velocity v from solenoid-1 towards solenoid-2, with induced current directions marked on the turns](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q034_sol_1_c94f0ab2_03112026.png?v=c94f0ab20b55)

*Bar magnet moving with velocity v from solenoid-1 towards solenoid-2, with induced current directions marked on the turns*

![drawn: Bar magnet moving with velocity v from solenoid-1 towards solenoid-2, with induced current directions marked on the turns](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q034_solution_1_efe9596d_04112026.svg?v=efe9596ded81)  
*drawn by code/lib/physics_figure.py*

1. North of magnet is moving away from solenoid 1 so end $B$ of solenoid 1 is South and as south of magnet is approaching solenoid 2 so end $C$ of solenoid 2 is South.

**Solved independently** (answer withheld)

1. The magnet moves to the right with its $N$ pole facing solenoid-1 and its $S$ pole facing solenoid-2.
2. In solenoid-1 the $N$ pole recedes, so by Lenz's law the right (near) end of solenoid-1 becomes an $S$ pole to oppose the decrease in flux.
3. In solenoid-2 the $S$ pole approaches, so by Lenz's law the left (near) end of solenoid-2 becomes an $S$ pole to oppose the increase in flux.
4. An $S$ pole on the right end of solenoid-1 needs current clockwise when viewed from the right; with the wire rising on the front face from terminal $A$, this current flows $A \to B$.
5. Both solenoids are wound the same way, but solenoid-2 has its $S$ pole on the left (opposite magnetisation), so its current flows from $D \to C$.
6. Hence the currents are $AB$ and $DC$, which is option $2$.

**Subtopic:** Lenz's Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q034_391ac0db_03112026.png?v=391ac0dba974)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q034_4354692d_03112026.png?v=4354692dc252)

---

## Q35

Physics · Magnetic Effect of Electric Current

A tightly wound $100$ turns coil of radius $10\,\mathrm{cm}$ carries a current of $7\,\mathrm{A}$. The magnitude of the magnetic field at the centre of the coil is (Take permeability of free space as $4\pi \times 10^{-7}$ SI units):

- (1) $44\,\mathrm{T}$
- (2) $44\,\mathrm{mT}$
- (3) $4.4\,\mathrm{T}$
- **(4)** $4.4\,\mathrm{mT}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The magnitude of magnetic field due to circular coil of $N$ turns is given by
2. $B_C = \frac{\mu_0 i N}{2R}$
3. $= \frac{4\pi \times 10^{-7} \times 7 \times 100}{2 \times 0.1}$
4. $= 4.4 \times 10^{-3}\,\mathrm{T}$
5. $= 4.4\,\mathrm{mT}$

**Solved independently** (answer withheld)

1. Field at the centre of a tightly wound circular coil: $B = \frac{\mu_0 N I}{2R}$.
2. Substitute $N = 100$, $I = 7\,\mathrm{A}$, $R = 0.1\,\mathrm{m}$: $B = \frac{4\pi \times 10^{-7} \times 100 \times 7}{2 \times 0.1}$.
3. $B = 4\pi \times 10^{-7} \times 3500 = 1.4\pi \times 10^{-3}\,\mathrm{T}$.
4. $B \approx 4.4 \times 10^{-3}\,\mathrm{T} = 4.4\,\mathrm{mT}$, which is option $4$.

**Subtopic:** Magnetic Field on the Axis of a Circular Current Loop · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q035_cfbba2e2_03112026.png?v=cfbba2e2e027)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q035_36c955c4_03112026.png?v=36c955c4da24)

---

## Q36

Physics · Electromagnetic Waves

The property which is not of an electromagnetic wave travelling in free space is that:

- **(1)** They originate from charges moving with uniform speed
- (2) They are transverse in nature
- (3) The energy density in electric field is equal to energy density in magnetic field
- (4) They travel with a speed equal to $\dfrac{1}{\sqrt{\mu_0 \varepsilon_0}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The EM waves originate from an accelerating charge.
2. The charge moving with uniform velocity produces steady state magnetic field.

**Solved independently** (answer withheld)

1. Charges moving with uniform velocity produce steady currents and static fields; only accelerated or oscillating charges radiate EM waves, so statement 1 is false.
2. EM waves are transverse ($\vec E \perp \vec B \perp \vec k$), $u_E = \frac{1}{2}\varepsilon_0 E^2 = \frac{B^2}{2\mu_0} = u_B$, and $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, so options 2, 3, 4 are true; the answer is option $1$.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q036_bab1786a_03112026.png?v=bab1786ade9f)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q036_41d8d5a1_03112026.png?v=41d8d5a190fa)

---

## Q37

Physics · Kinematics

The velocity $(v)$ – time $(t)$ plot of the motion of a body is shown below: The acceleration $(a)$ – time $(t)$ graph that best suits this motion is :

![printed figure: Velocity-time graph: v rises linearly from zero, stays constant, then falls linearly to zero](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q037_0a78284d_04112026.png?v=0a78284d248a)

*Velocity-time graph: v rises linearly from zero, stays constant, then falls linearly to zero*

![drawn: Velocity-time graph: v rises linearly from zero, stays constant, then falls linearly to zero](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q037_question_630c5b9b_04112026.svg?v=630c5b9b0a7c)  
*drawn by code/lib/physics_figure.py*

- (1) ![printed figure: Acceleration-time graph: zero, then a negative constant rectangle, then a rising straight line](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q037_option_1_58f19ba4_04112026.png?v=58f19ba41574) *Acceleration-time graph: zero, then a negative constant rectangle, then a rising straight line* ![drawn: Acceleration-time graph: zero, then a negative constant rectangle, then a rising straight line](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q037_option_1_623184b7_04112026.svg?v=623184b71419)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Option (2): a-t graph, zero then a trapezoidal positive pulse then zero](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q037_option_2_f0b198f0_04112026.png?v=f0b198f07324) *Option (2): a-t graph, zero then a trapezoidal positive pulse then zero* ![drawn: Option (2): a-t graph, zero then a trapezoidal positive pulse then zero](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q037_option_2_4051f1f0_04112026.svg?v=4051f1f099e8)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q037_option_3_5e91efd4_04112026.png?v=5e91efd4d283) *Acceleration-time graph: zero, then rising linearly, then constant* ![drawn: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q037_option_3_5aef142f_04112026.svg?v=5aef142f3b26)  
*drawn by code/lib/physics_figure.py*
- **(4)** ![printed figure: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q037_option_4_8611b337_04112026.png?v=8611b337dd04) *Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse* ![drawn: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q037_option_4_e5018438_04112026.svg?v=e50184385acd)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Initially, the body has zero velocity and zero slope.
2. Hence the acceleration would be zero initially.
3. After that, the slope of $v$-$t$ curve is constant and positive.
4. After some time, velocity becomes constant and acceleration is zero.
5. After that, the slope of $v$-$t$ curve is constant and negative.

![printed figure: Acceleration-time graph: a positive rectangular pulse followed by an equal negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q037_sol_1_34569d17_03112026.png?v=34569d17e3f8)

*Acceleration-time graph: a positive rectangular pulse followed by an equal negative rectangular pulse*

![drawn: Acceleration-time graph: a positive rectangular pulse followed by an equal negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q037_solution_1_d9f9da5d_04112026.svg?v=d9f9da5d922e)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. Acceleration is the slope of the $v$-$t$ graph: $a = \frac{dv}{dt}$.
2. Initially $v = 0$ and constant, so $a = 0$.
3. Next $v$ rises linearly, so $a = \frac{\Delta v}{\Delta t} > 0$ and constant: a positive rectangular pulse.
4. Then $v$ is constant, so $a = 0$.
5. Finally $v$ falls linearly to zero, so $a < 0$ and constant: a negative rectangular pulse.
6. Only option $4$ shows $a = 0$, then a positive constant, then $0$, then a negative constant.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q037_fcdfeac6_03112026.png?v=fcdfeac6aa8a)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q037_4d6da939_03112026.png?v=4d6da93936b4)

---

## Q38

Physics · Alternating Current

A $10\,\mu\mathrm{F}$ capacitor is connected to a $210\,\mathrm{V}$, $50\,\mathrm{Hz}$ source as shown in figure. The peak current in the circuit is nearly $(\pi = 3.14)$:

![printed figure: A capacitor C = 10 uF across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q038_a055b034_04112026.png?v=a055b034bb96)

*A capacitor C = 10 uF across a 210 V, 50 Hz AC source in one loop*

![drawn: A capacitor C = 10 uF across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q038_question_a103779e_04112026.svg?v=a103779e1955)  
*drawn by code/lib/physics_figure.py*

- (1) $0.35\,\mathrm{A}$
- (2) $0.58\,\mathrm{A}$
- **(3)** $0.93\,\mathrm{A}$
- (4) $1.20\,\mathrm{A}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Capacitive Reactance $X_C = \frac{1}{\omega C} = \frac{1}{2\pi fC} = \frac{1}{2\times 3.14\times 50\times 10\times 10^{-6}}$
2. $= \frac{1000}{3.14}$
3. $V_{\mathrm{rms}} = 210\,\mathrm{V}$
4. $i_{\mathrm{rms}} = \frac{V_{\mathrm{rms}}}{X_C} = \frac{210}{X_C}$
5. Peak current $= \sqrt{2}i_{\mathrm{rms}} = \sqrt{2}\times\frac{210}{1000}\times 3.14 = 0.932$
6. $\simeq 0.93\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Capacitive reactance: $X_C = \frac{1}{2\pi f C} = \frac{1}{2 \times 3.14 \times 50 \times 10 \times 10^{-6}} = \frac{1}{3.14 \times 10^{-3}} \approx 318.5\,\Omega$.
2. The 210 V is the rms value, so $I_{rms} = \frac{V_{rms}}{X_C} = \frac{210}{318.5} \approx 0.659\,\mathrm{A}$.
3. Peak current $I_0 = \sqrt{2}\, I_{rms} = 1.414 \times 0.659 \approx 0.93\,\mathrm{A}$, which is option $3$.

**Subtopic:** AC Voltage Applied to a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q038_2eff076d_03112026.png?v=2eff076dbd06)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q038_0cb606bf_03112026.png?v=0cb606bffbc2)

---

## Q39

Physics · Thermodynamics

The following graph represents the $T$-$V$ curves of an ideal gas (where $T$ is the temperature and $V$ the volume) at three pressures $P_1$, $P_2$ and $P_3$ compared with those of Charles's law represented as dotted lines. Then the correct relation is:

![printed figure: T-V curves of an ideal gas at pressures P1, P2, P3 with Charles's law dotted lines](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q039_f23f57bd_03112026.png?v=f23f57bd688f)

*T-V curves of an ideal gas at pressures P1, P2, P3 with Charles's law dotted lines*

![drawn: T-V curves of an ideal gas at pressures P1, P2, P3 with Charles's law dotted lines](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q039_question_468955f7_04112026.svg?v=468955f7c4c2)  
*drawn by code/lib/physics_figure.py*

- **(1)** $P_1 > P_2 > P_3$
- (2) $P_3 > P_2 > P_1$
- (3) $P_1 > P_3 > P_2$
- (4) $P_2 > P_1 > P_3$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. At same temperature, curve with higher volume corresponds to lower pressure.
2. $V_3 > V_2 > V_1$
3. $\Rightarrow P_1 > P_2 > P_3$
4. (We draw a straight line parallel to volume axis to get this)

**Solved independently** (answer withheld)

1. Ideal gas law: $PV = nRT \Rightarrow T = \frac{P}{nR}V$.
2. At constant $P$, the $T$-$V$ (Charles's law) line has slope $\frac{P}{nR}$, so a steeper line means a higher pressure.
3. From the figure, the $P_1$ line is steepest, then $P_2$, and $P_3$ is flattest.
4. Hence $P_1 > P_2 > P_3$, which is option $1$.

**Subtopic:** Gas Laws, Problems on Different Graphs of P, V, and T · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q039_e927baaf_03112026.png?v=e927baaf7f81)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q039_62909146_03112026.png?v=62909146887e)

---

## Q40

Physics · Current Electricity

> ⚠ The independent solve found no printed option exactly right ("No option gives $S = 15\,\Omega$, and options 1 and 3 are electrically equivalent, so no single option can be chosen"); its pick (unsure) is the closest fit, so treat this question as possibly misprinted.

> ⚠ Diode in a Wheatstone bridge: the booklet keys option (2), balancing 10/15 = 10/(5 + R_D) with the diode's dynamic resistance R_D = 10 ohm, as its printed solution says. An ideal-diode reading (R_D = 0 or open) balances no option exactly, which is why the blind solve stays unsure. Same question as 2024_Q2 q046, 2024_Q3 q042, 2024_Q4 q043, 2024_Q5 q036, 2024_Q6 q045 and 2024_T3 q039.

> ⚠ The independent solve chose (unsure); the booklet prints (2).

Choose the correct circuit which can achieve the bridge balance.

- (1) ![printed figure: Wheatstone bridge: 10 ohm, 10 ohm upper arms, 15 ohm lower-left, 5 ohm with diode D lower-right, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q040_option_1_2a368e8a_04112026.png?v=2a368e8a5a34) *Wheatstone bridge: 10 ohm, 10 ohm upper arms, 15 ohm lower-left, 5 ohm with diode D lower-right, galvanometer G, cell E and key K* ![drawn: Wheatstone bridge: 10 ohm, 10 ohm upper arms, 15 ohm lower-left, 5 ohm with diode D lower-right, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q040_option_1_fdb89fc9_04112026.svg?v=fdb89fc98a16)  
*drawn by code/lib/physics_figure.py*
- **(2)** ![printed figure: Wheatstone bridge 10, 10, 15 and 5 ohm with diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q040_option_2_97be0538_04112026.png?v=97be0538acf4) *Wheatstone bridge 10, 10, 15 and 5 ohm with diode D in the 5 ohm arm, galvanometer G, cell E and key K* ![drawn: Wheatstone bridge 10, 10, 15 and 5 ohm with diode D in the 5 ohm arm, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q040_option_2_cf29c26e_04112026.svg?v=cf29c26e9edd)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm, 5 ohm arms, galvanometer G, a diode D in the 5 ohm arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q040_option_3_ae536e5f_04112026.png?v=ae536e5fa127) *Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm, 5 ohm arms, galvanometer G, a diode D in the 5 ohm arm, cell E and key K* ![drawn: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm, 5 ohm arms, galvanometer G, a diode D in the 5 ohm arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q040_option_3_132a0dae_04112026.svg?v=132a0daead87)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Bridge: 10 ohm, 10 ohm, 15 ohm arms, galvanometer G across, diode D in parallel with 5 ohm in fourth arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q040_option_4_3df86bcc_04112026.png?v=3df86bccb88e) *Bridge: 10 ohm, 10 ohm, 15 ohm arms, galvanometer G across, diode D in parallel with 5 ohm in fourth arm, cell E and key K* ![drawn: Bridge: 10 ohm, 10 ohm, 15 ohm arms, galvanometer G across, diode D in parallel with 5 ohm in fourth arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q040_option_4_5460e860_04112026.svg?v=5460e86016c0)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (2) · independent solve: (unsure) · ai_unsure

**Publisher's solution**

1. In option (2),
2. $\frac{10}{15} = \frac{10}{5 + R_D}$
3. The diode can conduct and have resistance $R_D = 10\,\Omega$ because diode have dynamic resistance. In that case bridge will be balanced.

**Solved independently** (answer withheld)

1. Arms: top-left $P = 10\,\Omega$, top-right $Q = 10\,\Omega$, bottom-left $R = 15\,\Omega$, bottom-right $S$ = $5\,\Omega$ with diode $D$; galvanometer between top and bottom nodes.
2. Balance needs $\frac{P}{Q} = \frac{R}{S} \Rightarrow \frac{10}{10} = \frac{15}{S} \Rightarrow S = 15\,\Omega$.
3. Option 1: positive terminal on the right, series diode forward only from bottom node to right node, so it is reverse biased and $S \to \infty$.
4. Option 2: positive terminal on the left, same diode direction, so it is forward biased and $S = 5\,\Omega$; $\frac{10}{10} \ne \frac{15}{5}$.
5. Option 3: positive terminal on the left, diode forward only from right node to bottom node, so it is reverse biased and $S \to \infty$ (same as option 1).
6. Option 4: diode in parallel with $5\,\Omega$, so $S = 0$ (forward) or $S = 5\,\Omega$ (reverse); neither equals $15\,\Omega$.
7. No option gives $S = 15\,\Omega$, and options 1 and 3 are electrically equivalent, so no single option can be chosen.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 17)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q040_ef760322_03112026.png?v=ef7603224f57)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q040_53f75be1_03112026.png?v=53f75be1c4a3)

---

## Q41

Physics · Current Electricity

Two heaters A and B have power rating of $1\,\mathrm{kW}$ and $2\,\mathrm{kW}$, respectively. Those two are first connected in series and then in parallel to a fixed power source. The ratio of power outputs for these two cases is:

- (1) $2:3$
- (2) $1:1$
- **(3)** $2:9$
- (4) $1:2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Power Consumed = $P = \frac{V^{2}}{R}$
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
4. $\frac{P_s}{P_p} = \frac{2/3}{3} = \frac{2}{9}$, i.e. $2:9$, which is option $3$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q041_b66376a1_03112026.png?v=b66376a1b0d4)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q041_4cecee92_03112026.png?v=4cecee923656)

---

## Q42

Physics · Capacitance

If the plates of a parallel plate capacitor connected to a battery are moved close to each other, then
Choose the most appropriate answer from the options given below:

- (A) the charge stored in it, increases.
- (B) the energy stored in it, decreases.
- (C) its capacitance increases.
- (D) the ratio of charge to its potential remains the same.
- (E) the product of charge and voltage increases.

- (1) A, B and C only
- (2) A, B and E only
- **(3)** A, C and E only
- (4) B, D and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

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
7. True statements are A, C and E, which is option $3$.

**Subtopic:** The Parallel Plate Capacitor, Energy Stored in a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q042_a85ade4d_03112026.png?v=a85ade4d541c)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q042_cbd593bd_03112026.png?v=cbd593bd5788)

---

## Q43

Physics · Units and Measurements

A force defined by $F = \alpha t^{2} + \beta t$ acts on a particle at a given time $t$. The factor which is dimensionless, if $\alpha$ and $\beta$ are constants, is:

- (1) $\alpha\beta/t$
- (2) $\beta t/\alpha$
- **(3)** $\alpha t/\beta$
- (4) $\alpha\beta t$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. From principle of homogeneity
2. $[F] = [\alpha t^{2}] = [\beta t]$
3. $[\alpha] = \frac{[F]}{[t^{2}]}$ and $[\beta] = \frac{[F]}{[t]}$
4. $\therefore\ [\alpha]\,[t] = [\beta]$
5. $\therefore\ \frac{\alpha t}{\beta} =$ dimensionless

**Solved independently** (answer withheld)

1. Each term must have the dimensions of force: $[\alpha t^{2}] = [F]$, so $[\alpha] = [F]\,T^{-2}$.
2. Likewise $[\beta t] = [F]$, so $[\beta] = [F]\,T^{-1}$.
3. $\left[\frac{\alpha t}{\beta}\right] = \frac{[F]\,T^{-2}\cdot T}{[F]\,T^{-1}} = 1$, dimensionless, which is option $3$.

**Subtopic:** Homogeneity of Dimensions in an Equation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q043_881524e9_03112026.png?v=881524e95e01)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q043_908d1a3b_03112026.png?v=908d1a3bff17)

---

## Q44

Physics · Gravitation

The minimum energy required to launch a satellite of mass $m$ from the surface of earth of mass $M$ and radius $R$ in a circular orbit at an altitude of $2R$ from the surface of the earth is:

- (1) $\frac{GmM}{3R}$
- **(2)** $\frac{5GmM}{6R}$
- (3) $\frac{2GmM}{3R}$
- (4) $\frac{GmM}{2R}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Apply energy conservation,
2. $U_i + K_i = U_f + K_f$
3. $\Rightarrow -\frac{GMm}{R} + K_i = -\frac{GMm}{3R} + \frac{1}{2}mv^2$
4. $\Rightarrow -\frac{GMm}{R} + K_i = -\frac{GMm}{3R} + \frac{1}{2} \times m \times \frac{GM}{3R}$
5. $\Rightarrow K_i = -\frac{1}{6}\frac{GMm}{R} + \frac{GMm}{R}$
6. $K_i = \frac{5}{6}\frac{GMm}{R}$

**Solved independently** (answer withheld)

1. Orbit radius from the centre: $r = R + 2R = 3R$.
2. Total energy in circular orbit: $E_{orbit} = -\frac{GMm}{2r} = -\frac{GMm}{6R}$.
3. Energy at rest on the surface: $E_{surface} = -\frac{GMm}{R}$.
4. $E_{min} = E_{orbit} - E_{surface} = -\frac{GMm}{6R} + \frac{GMm}{R} = \frac{5GMm}{6R}$, which is option $2$.

**Subtopic:** Motion of a Satellite · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q044_9ee05ab3_03112026.png?v=9ee05ab3addb)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q044_7b43f1a0_03112026.png?v=7b43f1a03ff5)

---

## Q45

Physics · Mechanical Properties of Solids

A metallic bar of Young’s modulus, $0.5 \times 10^{11}\,\mathrm{N\,m^{-2}}$ and coefficient of linear thermal expansion $10^{-5}\,^{\circ}\mathrm{C}^{-1}$, length $1\,\mathrm{m}$ and area of cross-section $10^{-3}\,\mathrm{m^2}$ is heated from $0^{\circ}\mathrm{C}$ to $100^{\circ}\mathrm{C}$ without expansion or bending. The compressive force developed in it is :

- (1) $2 \times 10^{3}\,\mathrm{N}$
- (2) $5 \times 10^{3}\,\mathrm{N}$
- **(3)** $50 \times 10^{3}\,\mathrm{N}$
- (4) $100 \times 10^{3}\,\mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Thermal strain $=$ Longitudinal strain $= \alpha\,\Delta T$
2. $\Rightarrow$ Longitudinal strain, $\delta = 10^{-5} \times 10^{2} = 10^{-3}$
3. $\Rightarrow$ Compressive stress $= \delta \times$ Young's Modulus
4. $= 10^{-3} \times 0.5 \times 10^{11}$
5. $= 0.5 \times 10^{8}$
6. $\Rightarrow$ Compressive force $= 0.5 \times 10^{8} \times 10^{-3} = 0.5 \times 10^{5}$
7. $= 5 \times 10^{4} \times \frac{10}{10}$
8. $= 50 \times 10^{3}\,\mathrm{N}$

**Solved independently** (answer withheld)

1. Prevented expansion gives thermal strain $\varepsilon = \alpha \Delta T = 10^{-5} \times 100 = 10^{-3}$.
2. Stress $\sigma = Y \varepsilon = 0.5 \times 10^{11} \times 10^{-3} = 0.5 \times 10^{8}\,\mathrm{N\,m^{-2}}$.
3. $F = \sigma A = 0.5 \times 10^{8} \times 10^{-3} = 5 \times 10^{4}\,\mathrm{N} = 50 \times 10^{3}\,\mathrm{N}$, which is option $3$.

**Subtopic:** Thermal Stress and Strain · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q045_763e2ed5_03112026.png?v=763e2ed5bfa6)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q045_3e715259_03112026.png?v=3e71525903b8)

---

## Q46

Physics · Electromagnetic Waves

A parallel plate capacitor is charged by connecting it to a battery through a resistor. If $I$ is the current in the circuit, then in the gap between the plates:

- (1) Displacement current of magnitude greater than $I$ flows but can be in any direction
- (2) There is no current
- **(3)** Displacement current of magnitude equal to $I$ flows in the same direction as $I$
- (4) Displacement current of magnitude equal to $I$ flows in a direction opposite to that of $I$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Capacitor plates with Amperian loop L1 around the wire and loop L2 in the gap](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q046_sol_1_b705e690_03112026.png?v=b705e690e3d2)

*Capacitor plates with Amperian loop L1 around the wire and loop L2 in the gap*

![drawn: Capacitor plates with Amperian loop L1 around the wire and loop L2 in the gap](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q046_solution_1_8ac27998_04112026.svg?v=8ac27998e2cb)  
*drawn by code/lib/physics_figure.py*

1. According to modified Ampere’s law
2. $\oint B.\,dl = \mu_0(I_C + I_D)$
3. For Loop $L_1$ $\quad I_C \neq 0$ and $I_D = 0$
4. For Loop $L_2$ $\quad I_C = 0$ and $I_D \neq 0$
5. Due to KCL $\quad I_C = I_D$

**Solved independently** (answer withheld)

1. In the gap, $E = \frac{q}{\varepsilon_0 A}$, so $\Phi_E = EA = \frac{q}{\varepsilon_0}$.
2. $I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \frac{dq}{dt} = I$.
3. While charging, $E$ grows in the direction of conduction current flow, so $I_d$ is in the same direction as $I$: option $3$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q046_8bf20e5a_03112026.png?v=8bf20e5a736a)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q046_723697b1_03112026.png?v=723697b1c984)

---

## Q47

Physics · Electromagnetic Induction

A sheet is placed on a horizontal surface in front of a strong magnetic pole. A force is needed to:
Choose the correct statement(s) from the options given below:

- (A) hold the sheet there if it is magnetic.
- (B) hold the sheet there if it is non-magnetic.
- (C) move the sheet away from the pole with uniform velocity if it is conducting.
- (D) move the sheet away from the pole with uniform velocity if it is both, non-conducting and non-polar.

- (1) C only
- (2) B and D only
- **(3)** A and C only
- (4) A, C and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

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
6. True statements are $A$ and $C$, which is option $3$.

**Subtopic:** Eddy Currents · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q047_3a37ecad_03112026.png?v=3a37ecad1668)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q047_4921d99d_03112026.png?v=4921d99d2ec0)

---

## Q48

Physics · Oscillations

If the mass of the bob in a simple pendulum is increased to thrice its original mass and its length is made half its original length, then the new time period of oscillation is $\frac{x}{2}$ times its original time period. Then the value of $x$ is:

- (1) $4$
- (2) $\sqrt{3}$
- **(3)** $\sqrt{2}$
- (4) $2\sqrt{3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $T' = 2\pi\sqrt{\frac{\ell'}{g}}$ where $\ell' = \frac{\ell}{2}$
2. $T = 2\pi\sqrt{\frac{\ell}{g}}$
3. $T' = \frac{x}{2}T$
4. $2\pi\sqrt{\frac{\ell}{2g}} = \frac{x}{2}2\pi\sqrt{\frac{\ell}{g}}$
5. $\frac{1}{\sqrt{2}} = \frac{x}{2} \Rightarrow x = \sqrt{2}$

**Solved independently** (answer withheld)

1. $T = 2\pi\sqrt{\frac{l}{g}}$ is independent of the bob's mass, so tripling the mass has no effect.
2. $T' = 2\pi\sqrt{\frac{l/2}{g}} = \frac{T}{\sqrt{2}}$.
3. $\frac{T}{\sqrt{2}} = \frac{\sqrt{2}}{2}T = \frac{x}{2}T \Rightarrow x = \sqrt{2}$, which is option $3$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q048_8d0b066c_03112026.png?v=8d0b066cd9a3)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q048_5b330173_03112026.png?v=5b3301736907)

---

## Q49

Physics · Magnetic Effect of Electric Current

An iron bar of length $L$ has magnetic moment $M$. It is bent at the middle of its length such that the two arms make an angle $60^\circ$ with each other. The magnetic moment of this new magnet is :

- (1) $\frac{M}{\sqrt{3}}$
- (2) $M$
- **(3)** $\frac{M}{2}$
- (4) $2M$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Straight iron bar of length l before bending](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q049_sol_1_d05b2381_03112026.png?v=d05b2381cd1e)

*Straight iron bar of length l before bending*

![drawn: Straight iron bar of length l before bending](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q049_solution_1_24a829e5_04112026.svg?v=24a829e5bb75)  
*drawn by code/lib/physics_figure.py*

1. $M = ml.$

![printed figure: Bar bent at its middle: two arms of length l/2 at 60 degrees, free ends separated by delta l](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q049_sol_2_14bfc1c9_03112026.png?v=14bfc1c9e448)

*Bar bent at its middle: two arms of length l/2 at 60 degrees, free ends separated by delta l*

![drawn: Bar bent at its middle: two arms of length l/2 at 60 degrees, free ends separated by delta l](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q049_solution_2_8f9a7184_04112026.svg?v=8f9a718459a8)  
*drawn by code/lib/physics_figure.py*

2. $\Delta l = 2\frac{l}{2}\sin 30^\circ$
3. $= \frac{l}{2}$
4. $M' = ml/2$
5. $= M/2$

**Solved independently** (answer withheld)

1. Original moment: $M = m L$, where $m$ is the pole strength.
2. Bending at the middle gives two arms of length $\frac{L}{2}$ with $60^\circ$ between them.
3. The two arms and the line joining the poles form an equilateral triangle, so the pole separation is $\frac{L}{2}$.
4. $M' = m \cdot \frac{L}{2} = \frac{M}{2}$, which is option $3$.

**Subtopic:** Permanent Magnet and the Bar Magnet · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q049_411223e6_03112026.png?v=411223e6bed6)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q049_732ebdb4_03112026.png?v=732ebdb4838b)

---

## Q50

Physics · Ray Optics

A small telescope has an objective of focal length $140\,\mathrm{cm}$ and an eye piece of focal length $5.0\,\mathrm{cm}$. The magnifying power of telescope for viewing a distant object is:

- (1) $32$
- (2) $34$
- **(3)** $28$
- (4) $17$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $f_0 = 140\,\mathrm{cm}$ and $f_e = 5\,\mathrm{cm}$
2. For distant object,
3. $m = \frac{f_0}{f_e} = \frac{140}{5} = 28$

**Solved independently** (answer withheld)

1. For a distant object viewed in normal adjustment, the magnifying power of a telescope is $m = \frac{f_o}{f_e}$.
2. $m = \frac{140\,\mathrm{cm}}{5.0\,\mathrm{cm}} = 28$, which is option $3$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 21)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q050_92ea038c_03112026.png?v=92ea038c448e)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q050_ab017b01_03112026.png?v=ab017b0190f6)

---

## Q51

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the correct reagents that would bring about the following transformation.

![printed figure: allylcyclohexane → 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q051_7ae1f23f_03112026.png?v=7ae1f23f22ee)

*allylcyclohexane → 3-cyclohexylpropanal*

![drawn: allylcyclohexane → 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q051_question_4ad0072e_04112026.svg?v=4ad0072e529b)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: allylcyclohexane `C=CCC1CCCCC1` ![allylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q051_question_s1_19da39bf_04112026.svg?v=19da39bfbc83); 3-cyclohexylpropanal `O=CCCC1CCCCC1` ![3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q051_question_s2_d5fc3230_04112026.svg?v=d5fc32301153)

- (1) (i) $\mathrm{H_2O/H^+}$ (ii) PCC
- (2) (i) $\mathrm{H_2O/H^+}$ (ii) $\mathrm{CrO_3}$
- **(3)** (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2}/\overset{\ominus}{\mathrm{O}}\mathrm{H}$ (iii) PCC
- (4) (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2}/\overset{\ominus}{\mathrm{O}}\mathrm{H}$ (iii) alk.$\mathrm{KMnO_4}$ (iv) $\mathrm{H_3O^{\oplus}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: I. allylcyclohexane →((i) BH₃ (ii) H₂O₂/OH⁻ (iii) PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q051_sol_1_e158ac0b_03112026.png?v=e158ac0beac8)

*I. allylcyclohexane →[(i) BH₃ (ii) H₂O₂/OH⁻ (iii) PCC] 3-cyclohexylpropanal*

![drawn: I. allylcyclohexane →((i) BH₃ (ii) H₂O₂/OH⁻ (iii) PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q051_solution_1_b046c75d_04112026.svg?v=b046c75df267)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Mechanism :

![printed figure: allylcyclohexane + $\ce{(H-BH2)3}$ → (3-cyclohexylpropyl)borane (H and BH₂ drawn on adjacent carbons); (3-cyclohexylpropyl)borane →(allylcyclohexane) bis(3-cyclohexylpropyl)borane; bis(3-cyclohexylpropyl)borane →(allylcyclohexane) tris(3-cyclohexylpropyl)borane; tris(3-cyclohexylpropyl)borane →(H₂O; 3H₂O₂, OH⁻) 3 3-cyclohexylpropan-1-ol; 3-cyclohexylpropan-1-ol →(PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q051_sol_2_261a9c9c_03112026.png?v=261a9c9ceda2)

*allylcyclohexane + $\ce{(H-BH2)3}$ → (3-cyclohexylpropyl)borane (H and BH₂ drawn on adjacent carbons); (3-cyclohexylpropyl)borane →[allylcyclohexane] bis(3-cyclohexylpropyl)borane; bis(3-cyclohexylpropyl)borane →[allylcyclohexane] tris(3-cyclohexylpropyl)borane; tris(3-cyclohexylpropyl)borane →[H₂O; 3H₂O₂, OH⁻] 3 3-cyclohexylpropan-1-ol; 3-cyclohexylpropan-1-ol →[PCC] 3-cyclohexylpropanal*

![drawn: allylcyclohexane + $\ce{(H-BH2)3}$ → (3-cyclohexylpropyl)borane (H and BH₂ drawn on adjacent carbons); (3-cyclohexylpropyl)borane →(allylcyclohexane) bis(3-cyclohexylpropyl)borane; bis(3-cyclohexylpropyl)borane →(allylcyclohexane) tris(3-cyclohexylpropyl)borane; tris(3-cyclohexylpropyl)borane →(H₂O; 3H₂O₂, OH⁻) 3 3-cyclohexylpropan-1-ol; 3-cyclohexylpropan-1-ol →(PCC) 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q051_solution_2_b3f100ae_04112026.svg?v=b3f100ae525f)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. The product has $\mathrm{-CHO}$ on the terminal carbon, so the terminal alkene carbon must become a primary alcohol (anti-Markovnikov addition of water).
2. $\mathrm{H_2O/H^+}$ adds water by Markovnikov's rule, giving the secondary alcohol $\mathrm{C_6H_{11}CH_2CH(OH)CH_3}$, which would oxidise to a ketone; options $1$ and $2$ are ruled out.
3. $\mathrm{BH_3}$ then $\mathrm{H_2O_2/OH^-}$ gives $\mathrm{C_6H_{11}CH_2CH_2CH_2OH}$ (anti-Markovnikov).
4. PCC oxidises a primary alcohol only to the aldehyde: $\mathrm{C_6H_{11}CH_2CH_2CHO}$, which is option $3$.
5. Alkaline $\mathrm{KMnO_4}$ then $\mathrm{H_3O^+}$ would give the carboxylic acid, so option $4$ is wrong.

**Subtopic:** Preparation of Aldehydes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q051_b663aac6_03112026.png?v=b663aac68703)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q051_a860a8d1_03112026.png?v=a860a8d14777)

---

## Q52

Chemistry · organic · Haloalkanes and Haloarenes

The compound that will undergo $\mathrm{S_N1}$ reaction with the fastest rate is

- **(1)** (1-bromoethyl)benzene `CC(Br)c1ccccc1` ![(1-bromoethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q052_option_1_s1_ef3a803b_04112026.svg?v=ef3a803b5361)
- (2) (bromomethyl)cyclohexane `BrCC1CCCCC1` ![(bromomethyl)cyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q052_option_2_s1_3db34c76_04112026.svg?v=3db34c76f38e)
- (3) bromocyclohexane `BrC1CCCCC1` ![bromocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q052_option_3_s1_35c4a4b9_04112026.svg?v=35c4a4b9cb53)
- (4) bromobenzene `Brc1ccccc1` ![bromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q052_option_4_s1_61d2ed9e_04112026.svg?v=61d2ed9ebe04)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Reactivity towards $\mathrm{S_N1}$ depends upon stability of carbocation.
2. Order of stability is

![printed figure: 1-phenylethyl cation > cyclohexyl cation > cyclohexylmethyl cation > phenyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q052_sol_1_fc0af3e2_03112026.png?v=fc0af3e23a77)

*1-phenylethyl cation > cyclohexyl cation > cyclohexylmethyl cation > phenyl cation*

![drawn: 1-phenylethyl cation > cyclohexyl cation > cyclohexylmethyl cation > phenyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q052_solution_1_a0e30856_04112026.svg?v=a0e30856b5e9)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. Hence

![printed figure: (1-bromoethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q052_sol_2_615740f5_03112026.png?v=615740f5b56e)

*(1-bromoethyl)benzene*

![drawn: (1-bromoethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q052_solution_2_c3366f27_04112026.svg?v=c3366f2703ed)  
*drawn by RDKit (code/lib/chem_cards.py)*

4. is most reactive

**Solved independently** (answer withheld)

1. The $\mathrm{S_N1}$ rate depends on how stable the carbocation formed in the slow ionisation step is.
2. Option $1$, $\mathrm{C_6H_5CH(Br)CH_3}$, gives $\mathrm{C_6H_5\overset{+}{C}HCH_3}$, a secondary benzylic carbocation stabilised by resonance with the ring.
3. Option $3$, bromocyclohexane, gives a secondary cyclohexyl carbocation with no resonance stabilisation.
4. Option $2$, $\mathrm{C_6H_{11}CH_2Br}$, would give a primary carbocation, which is poorly stabilised.
5. Option $4$, bromobenzene, is an aryl halide: the $\mathrm{C-Br}$ bond has partial double-bond character and a phenyl cation is very unstable, so it does not undergo $\mathrm{S_N1}$.
6. Order of rate: $1 > 3 > 2 > 4$, so the fastest is option $1$.

**Subtopic:** Reactions of Haloalkanes – Nucleophilic Substitution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q052_bfa42ca0_03112026.png?v=bfa42ca0fc5d)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q052_be44ec8f_03112026.png?v=be44ec8fcf87)

---

## Q53

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

- (1) A-III, B-IV, C-I, D-II
- (2) A-I, B-IV, C-II, D-III
- (3) A-IV, B-III, C-II, D-I
- **(4)** A-III, B-IV, C-II, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (A) Ethane: one $(\mathrm{C-C})$ $\sigma$ bond

![printed figure: ethane](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q053_sol_1_29481016_03112026.png?v=294810161650)

*ethane*

![drawn: ethane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q053_solution_1_6ee0c318_04112026.svg?v=6ee0c3182288)  
*drawn by RDKit (code/lib/chem_cards.py)*

2. (B) Ethene: one $(\mathrm{C-C})$ $\sigma$ and one $(\mathrm{C-C})$ $\pi$ bond

![printed figure: ethene](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q053_sol_2_139032c1_03112026.png?v=139032c1d01d)

*ethene*

![drawn: ethene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q053_solution_2_bcd44f8a_04112026.svg?v=bcd44f8a0a60)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. (C) $\mathrm{C_2}$: two $(\mathrm{C-C})$ $\pi$ bonds
4. (D) Ethyne $\mathrm{H-C\equiv C-H}$: two $(\mathrm{C-C})$ $\pi$ bonds and one $(\mathrm{C-C})$ $\sigma$ bond

**Solved independently** (answer withheld)

1. Ethane $\mathrm{C_2H_6}$ has a C$-$C single bond: one $\sigma$-bond, so A$-$III.
2. Ethene $\mathrm{C_2H_4}$ has a C$=$C double bond: one $\sigma$ and one $\pi$-bond, so B$-$IV.
3. In $\mathrm{C_2}$ (MO configuration $\sigma 1s^2\,\sigma^*1s^2\,\sigma 2s^2\,\sigma^*2s^2\,(\pi 2p_x^2 = \pi 2p_y^2)$), the bond order 2 comes from two $\pi$-bonds, so C$-$II.
4. Ethyne $\mathrm{C_2H_2}$ has a C$\equiv$C triple bond: one $\sigma$ and two $\pi$-bonds, so D$-$I.
5. A$-$III, B$-$IV, C$-$II, D$-$I is option $4$.

**Subtopic:** Molecular Orbital Theory, Orbital Overlap Concept · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 23)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q053_b1d7b3e6_03112026.png?v=b1d7b3e631ad)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q053_958b9913_03112026.png?v=958b99135ef7)

---

## Q54

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements :
In the light of the above statements, choose the correct answer from the options given below:

- (I) Both $\mathrm{[Co(NH_3)_6]^{3+}}$ and $\mathrm{[CoF_6]^{3-}}$ complexes are octahedral but differ in their magnetic behaviour.
- (II) $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic whereas $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.

- (1) Statement I is false but Statement II is true
- **(2)** Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{Co^{3+}}$ ion is having $3d^{6}$ configuration.
2. Electronic configuration of $\mathrm{Co^{3+}}$ :

![printed figure: orbital-box diagram: 3d subshell with one paired and four unpaired electrons (6 electrons), empty 4s and empty 4p boxes](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q054_sol_1_cb09cbc6_03112026.png?v=cb09cbc6883c)

*orbital-box diagram: 3d subshell with one paired and four unpaired electrons (6 electrons), empty 4s and empty 4p boxes*

3. In presence of $\mathrm{NH_3}$ ligand, pairing of electrons takes place and it becomes diamagnetic complex ion.
4. In presence of $\mathrm{NH_3}$ ligand :

![printed figure: orbital-box diagram: 3d subshell with three paired electron boxes and two empty boxes (6 electrons), empty 4s and empty 4p boxes](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q054_sol_2_a99f059d_03112026.png?v=a99f059dc996)

*orbital-box diagram: 3d subshell with three paired electron boxes and two empty boxes (6 electrons), empty 4s and empty 4p boxes*

5. $\therefore$ $\mathrm{[Co(NH_3)_6]^{3+}}$ is octahedral with $d^{2}sp^{3}$ hybridisation and it is diamagnetic in nature.
6. In case of $\mathrm{[CoF_6]^{3-}}$, $\mathrm{Co}$ is in $+3$ oxidation state and it is having $3d^{6}$ configuration.
7. In presence of weak field $\mathrm{F^{-}}$ ligand, pairing does not take place.
8. In presence of $\mathrm{F^{-}}$ ligands :

![printed figure: orbital-box diagram: 3d subshell with one paired and four unpaired electrons, then empty 4s, 4p and 4d boxes, with 4s, 4p and two 4d boxes enclosed in a rectangle (hybridisation)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q054_sol_3_2dd93253_03112026.png?v=2dd93253a3ed)

*orbital-box diagram: 3d subshell with one paired and four unpaired electrons, then empty 4s, 4p and 4d boxes, with 4s, 4p and two 4d boxes enclosed in a rectangle (hybridisation)*

9. $\therefore$ In $\mathrm{[CoF_6]^{3-}}$, $\mathrm{Co^{3+}}$ is $sp^{3}d^{2}$ hybridised with four unpaired electrons, so it is paramagnetic in nature.

**Solved independently** (answer withheld)

1. In both complexes cobalt is $\mathrm{Co^{3+}}$, configuration $3d^6$, with coordination number 6, so both are octahedral.
2. $\mathrm{NH_3}$ is a strong-field ligand: pairing gives $t_{2g}^6 e_g^0$ (inner-orbital $d^2sp^3$), 0 unpaired electrons, so $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic.
3. $\mathrm{F^-}$ is a weak-field ligand: $t_{2g}^4 e_g^2$ (outer-orbital $sp^3d^2$), 4 unpaired electrons, so $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.
4. Hence Statement I (same geometry, different magnetism) and Statement II are both true, which is option $2$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q054_5813693d_03112026.png?v=5813693dc564)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q054_9cecc916_03112026.png?v=9cecc916c691)

---

## Q55

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{NH_3}$ | I | Trigonal Pyramidal |
| B | $\mathrm{BrF_5}$ | II | Square Planar |
| C | $\mathrm{XeF_4}$ | III | Octahedral |
| D | $\mathrm{SF_6}$ | IV | Square Pyramidal |

- (1) A-II, B-III, C-IV, D-I
- **(2)** A-I, B-IV, C-II, D-III
- (3) A-II, B-IV, C-III, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

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

1. $\mathrm{NH_3}$: N has 3 bond pairs and 1 lone pair ($sp^3$), so its shape is trigonal pyramidal: A-I.
2. $\mathrm{BrF_5}$: Br has 5 bond pairs and 1 lone pair ($sp^3d^2$), so its shape is square pyramidal: B-IV.
3. $\mathrm{XeF_4}$: Xe has 4 bond pairs and 2 lone pairs ($sp^3d^2$), so its shape is square planar: C-II.
4. $\mathrm{SF_6}$: S has 6 bond pairs and 0 lone pairs ($sp^3d^2$), so its shape is octahedral: D-III.
5. A-I, B-IV, C-II, D-III matches option $2$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q055_b36b9736_03112026.png?v=b36b9736f627)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q055_f09c935d_03112026.png?v=f09c935d059d)

---

## Q56

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of first ionization enthalpy:
$\mathrm{Li}$, $\mathrm{Be}$, $\mathrm{B}$, $\mathrm{C}$, $\mathrm{N}$
Choose the correct answer from the options given below:

- (1) $\mathrm{Li} < \mathrm{Be} < \mathrm{N} < \mathrm{B} < \mathrm{C}$
- (2) $\mathrm{Li} < \mathrm{Be} < \mathrm{B} < \mathrm{C} < \mathrm{N}$
- **(3)** $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$
- (4) $\mathrm{Li} < \mathrm{Be} < \mathrm{C} < \mathrm{B} < \mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Increasing order of first ionization enthalpy is $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$

![printed figure: table of first ionization enthalpy ($\Delta_i H$/kJ mol$^{-1}$) by element: Li 520; Be 899; B 801; C 1086; N 1402](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q056_sol_1_0f5995f5_03112026.png?v=0f5995f5b03b)

*table of first ionization enthalpy ($\Delta_i H$/kJ mol$^{-1}$) by element: Li 520; Be 899; B 801; C 1086; N 1402*


**Solved independently** (answer withheld)

1. Across period 2, first ionization enthalpy generally increases with increasing nuclear charge, so $\mathrm{Li}$ is lowest and $\mathrm{N}$ is highest among these.
2. $\mathrm{Be}$ ($1s^2 2s^2$) has a fully filled, more penetrating $2s$ orbital, while $\mathrm{B}$ ($1s^2 2s^2 2p^1$) loses a $2p$ electron that is shielded by $2s$, so $\Delta_i H_1(\mathrm{B}) < \Delta_i H_1(\mathrm{Be})$.
3. $\mathrm{C} < \mathrm{N}$ since $\mathrm{N}$ has a stable half-filled $2p^3$ configuration and higher nuclear charge.
4. Order: $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$, which is option $3$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q056_cfda09d5_03112026.png?v=cfda09d54334)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q056_63ac62cc_03112026.png?v=63ac62cc79df)

---

## Q57

Chemistry · organic · Biomolecules

The reagents with which glucose does not react to give the corresponding tests/products are
Choose the correct options from the given below:

- (A) Tollen’s reagent
- (B) Schiff’s reagent
- (C) $\mathrm{HCN}$
- (D) $\mathrm{NH_2OH}$
- (E) $\mathrm{NaHSO_3}$

- (1) E and D
- (2) B and C
- (3) A and D
- **(4)** B and E

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Despite having the aldehyde group glucose does not give Schiff’s test and it does not form the hydrogen sulphite addition product with $\mathrm{NaHSO_3}$.

**Solved independently** (answer withheld)

1. Glucose reduces Tollens' reagent (silver mirror), so $\text{A}$ reacts.
2. Glucose adds $\mathrm{HCN}$ to give a cyanohydrin, so $\text{C}$ reacts.
3. Glucose condenses with $\mathrm{NH_2OH}$ to give an oxime, so $\text{D}$ reacts.
4. Despite having a $\mathrm{-CHO}$ group, glucose does not give Schiff's test and does not form the $\mathrm{NaHSO_3}$ addition product (evidence for its cyclic structure), so $\text{B}$ and $\text{E}$ do not react.
5. Non-reacting reagents are $\text{B}$ and $\text{E}$, which is option $4$.

**Subtopic:** Structure and Reactions of Glucose · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q057_e4a52656_03112026.png?v=e4a526563e66)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q057_983e3a14_03112026.png?v=983e3a14d591)

---

## Q58

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

- (1) A-II, B-I, C-IV, D-III
- (2) A-I, B-III, C-II, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Magnetic quantum number $m_l$ informs about orientation of orbital.
2. Spin quantum number $m_s$ informs about orientation of spin of electron.
3. Azimuthal quantum number $(l)$ informs about shape of orbital
4. Principal quantum number $(n)$ informs about size of orbital

**Solved independently** (answer withheld)

1. $m_l$ (magnetic quantum number) gives the orientation of the orbital: A-III; $m_s$ gives the orientation of electron spin: B-IV; $l$ (azimuthal) gives the shape of the orbital: C-I; $n$ (principal) gives the size of the orbital: D-II; so A-III, B-IV, C-I, D-II is option $3$.

**Subtopic:** Quantum Numbers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q058_53505140_03112026.png?v=535051409a2d)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q058_797b30ca_03112026.png?v=797b30ca9f81)

---

## Q59

Chemistry · physical · Basic Concepts of Chemistry

The highest number of helium atoms is in

- (1) $2.271098\,\mathrm{L}$ of helium at STP
- **(2)** $4\,\mathrm{mol}$ of helium
- (3) $4\,\mathrm{u}$ of helium
- (4) $4\,\mathrm{g}$ of helium

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (1) $2.2710982$ of He at STP $= \frac{2.271}{22.710982}$ mole
2. $= 0.1$ mole
3. $= 0.1\,N_A$ He atom
4. (2) $4\,\mathrm{mol}$ of He $= 4\,N_A$ He atoms
5. (3) $4\,\mathrm{u}$ of He $= \frac{4\,\mathrm{u}}{4\,\mathrm{u}} = 1$ He atom
6. (4) $4\,\mathrm{g}$ of Helium $= \frac{4\,\mathrm{g}}{4\,\mathrm{g}}$ mole $= 1$ mole $= N_A$ He atom

**Solved independently** (answer withheld)

1. Option 1: molar volume at STP is $22.71098\,\mathrm{L\,mol^{-1}}$, so $n = \frac{2.271098}{22.71098} = 0.1\,\mathrm{mol}$.
2. Option 2: $n = 4\,\mathrm{mol}$, i.e. $4N_A$ atoms.
3. Option 3: mass of one He atom is $4\,\mathrm{u}$, so $4\,\mathrm{u}$ is $1$ atom.
4. Option 4: $n = \frac{4\,\mathrm{g}}{4\,\mathrm{g\,mol^{-1}}} = 1\,\mathrm{mol}$, i.e. $N_A$ atoms.
5. Largest is $4\,\mathrm{mol}$, which is option $2$.

**Subtopic:** Mole Concept · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q059_ff96ca0b_03112026.png?v=ff96ca0b88ca)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q059_a0942d58_03112026.png?v=a0942d58a058)

---

## Q60

Chemistry · physical · Redox Reactions

Which reaction is NOT a redox reaction?

- **(1)** $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$
- (2) $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$
- (3) $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$
- (4) $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (1) $\mathrm{\overset{+2}{Ba}Cl_2^{-1} + \overset{+1}{Na_2}SO_4^{-2} \longrightarrow \overset{+2}{Ba}SO_4 + 2\overset{+1}{Na}Cl^{-1}}$
2. This is not a redox reaction as there is no change in oxidation state.
3. (2) $\mathrm{Zn^{0} + \overset{+2}{Cu}SO_4 \longrightarrow \overset{+2}{Zn}SO_4 + Cu^{0}}$, Redox reaction

![printed figure: (2) zinc (oxidation state 0) + copper(II) sulfate (Cu +2) → zinc sulfate (Zn +2) + copper (oxidation state 0), Redox reaction; bracket arrows: Reduction (Cu +2 → Cu 0), Oxidation (Zn 0 → Zn +2); $\ce{Zn + CuSO4 -> ZnSO4 + Cu}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q060_sol_1_30af7656_03112026.png?v=30af76565d45)

*(2) zinc (oxidation state 0) + copper(II) sulfate (Cu +2) → zinc sulfate (Zn +2) + copper (oxidation state 0), Redox reaction; bracket arrows: Reduction (Cu +2 → Cu 0), Oxidation (Zn 0 → Zn +2); $\ce{Zn + CuSO4 -> ZnSO4 + Cu}$*

4. (3) $\mathrm{K\overset{+5}{Cl}O_3 + I_2^{0} \longrightarrow 2K\overset{+5}{I}O_3 + Cl_2^{0}}$, Redox reaction

![printed figure: (3) potassium chlorate (Cl +5) + iodine (oxidation state 0) → 2 potassium iodate (I +5) + chlorine (oxidation state 0), Redox reaction; bracket arrows: Reduction (Cl +5 → Cl 0), Oxidation (I 0 → I +5); $\ce{KClO3 + I2 -> 2KIO3 + Cl2}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q060_sol_2_52f04ffa_03112026.png?v=52f04ffae3e5)

*(3) potassium chlorate (Cl +5) + iodine (oxidation state 0) → 2 potassium iodate (I +5) + chlorine (oxidation state 0), Redox reaction; bracket arrows: Reduction (Cl +5 → Cl 0), Oxidation (I 0 → I +5); $\ce{KClO3 + I2 -> 2KIO3 + Cl2}$*

![drawn: (3) potassium chlorate (Cl +5) + iodine (oxidation state 0) → 2 potassium iodate (I +5) + chlorine (oxidation state 0), Redox reaction; bracket arrows: Reduction (Cl +5 → Cl 0), Oxidation (I 0 → I +5); $\ce{KClO3 + I2 -> 2KIO3 + Cl2}$](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q060_solution_2_0cea716b_04112026.svg?v=0cea716bae87)  
*drawn by RDKit (code/lib/chem_cards.py)*

5. (4) $\mathrm{H_2^{0} + Cl_2^{0} \longrightarrow 2\overset{+1}{H}Cl^{-1}}$, Redox reaction

![printed figure: (4) hydrogen (oxidation state 0) + chlorine (oxidation state 0) → 2 hydrogen chloride (H +1, Cl −1), Redox reaction; bracket arrows: Reduction (Cl 0 → Cl −1), Oxidation (H 0 → H +1); $\ce{H2 + Cl2 -> 2HCl}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q060_sol_3_28a5539e_03112026.png?v=28a5539eb911)

*(4) hydrogen (oxidation state 0) + chlorine (oxidation state 0) → 2 hydrogen chloride (H +1, Cl −1), Redox reaction; bracket arrows: Reduction (Cl 0 → Cl −1), Oxidation (H 0 → H +1); $\ce{H2 + Cl2 -> 2HCl}$*

![drawn: (4) hydrogen (oxidation state 0) + chlorine (oxidation state 0) → 2 hydrogen chloride (H +1, Cl −1), Redox reaction; bracket arrows: Reduction (Cl 0 → Cl −1), Oxidation (H 0 → H +1); $\ce{H2 + Cl2 -> 2HCl}$](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q060_solution_3_a1f33a87_04112026.svg?v=a1f33a87ce38)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. In $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$ the oxidation states stay $\mathrm{Ba}=+2$, $\mathrm{Cl}=-1$, $\mathrm{Na}=+1$, $\mathrm{S}=+6$, $\mathrm{O}=-2$ on both sides, so it is not redox.
2. In $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$, $\mathrm{Zn}: 0 \rightarrow +2$ and $\mathrm{Cu}: +2 \rightarrow 0$, so it is redox.
3. In $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$, $\mathrm{I}: 0 \rightarrow +5$ and $\mathrm{Cl}: +5 \rightarrow 0$, so it is redox.
4. In $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$, $\mathrm{H}: 0 \rightarrow +1$ and $\mathrm{Cl}: 0 \rightarrow -1$, so it is redox.
5. Only option $1$ is not a redox reaction.

**Subtopic:** Oxidation Number · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q060_c405d4a3_03112026.png?v=c405d4a3e1a7)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q060_76618710_03112026.png?v=7661871061dc)

---

## Q61

Chemistry · inorganic · The p–Block Elements

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) The boiling point of hydrides of Group 16 elements follow the order $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
- (Statement II) On the basis of molecular mass, $\mathrm{H_2O}$ is expected to have lower boiling point than the other members of the group but due to the presence of extensive H-bonding in $\mathrm{H_2O}$, it has higher boiling point.

- (1) Statement I is false but Statement II is true
- **(2)** Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Statement I is correct, because boiling point of hydrides of group 16 follows the order
2. $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
3. Statement II due to intermolecular H-bonding $\mathrm{H_2O}$ shows higher boiling point than respective hydrides of group 16.
4. (Both Statement are true)
5. Order from $\mathrm{H_2Te}$ to $\mathrm{H_2S}$ is due to decreasing molar mass.

**Solved independently** (answer withheld)

1. Among $\mathrm{H_2S, H_2Se, H_2Te}$ boiling point rises with molar mass (van der Waals forces): $\mathrm{H_2Te > H_2Se > H_2S}$.
2. $\mathrm{H_2O}$ has the lowest molar mass but extensive intermolecular H-bonding, so its boiling point is the highest: $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$, so Statement I is true.
3. Statement II correctly gives the reason (lower expected b.p. by mass, higher actual b.p. due to H-bonding), so it is true; both true is option $2$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q061_e33450b8_03112026.png?v=e33450b84323)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q061_78f75eff_03112026.png?v=78f75eff027a)

---

## Q62

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of electronegativity:
$\mathrm{N}$, $\mathrm{O}$, $\mathrm{F}$, $\mathrm{C}$, $\mathrm{Si}$
Choose the correct answer from the options given below:

- (1) $\mathrm{F} < \mathrm{O} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$
- **(2)** $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$
- (3) $\mathrm{Si} < \mathrm{C} < \mathrm{O} < \mathrm{N} < \mathrm{F}$
- (4) $\mathrm{O} < \mathrm{F} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Electronegativity increases across the period on moving left to right.
2. It decreases on moving down the group.
3. The correct option is $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$

**Solved independently** (answer withheld)

1. Across period 2, electronegativity increases left to right: $\mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$.
2. Down group 14, electronegativity decreases, so $\mathrm{Si} < \mathrm{C}$.
3. Combined order: $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$, which is option $2$.

**Subtopic:** Trends in Chemical Properties – Electronegativity and Electron Affinity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q062_8768ee02_03112026.png?v=8768ee026c7f)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q062_296f96be_03112026.png?v=296f96be1420)

---

## Q63

Chemistry · physical · Thermodynamics

Match List I with List II.
List-I (Process) | List-II (Conditions)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Isothermal process | I | No heat exchange |
| B | Isochoric process | II | Carried out at constant temperature |
| C | Isobaric process | III | Carried out at constant volume |
| D | Adiabatic process | IV | Carried out at constant pressure |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-IV, B-III, C-II, D-I
- (3) A-IV, B-II, C-III, D-I
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

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
5. The matching $A\text{-}II, B\text{-}III, C\text{-}IV, D\text{-}I$ is option $1$.

**Subtopic:** Thermodynamic Processes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q063_a9310aef_03112026.png?v=a9310aeffb1a)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q063_6434aa54_03112026.png?v=6434aa5425ac)

---

## Q64

Chemistry · physical · Structure of Atom

The energy of an electron in the ground state ($n = 1$) for $\mathrm{He^{+}}$ ion is $-x\,\mathrm{J}$, then that for an electron in $n = 2$ state for $\mathrm{Be^{3+}}$ ion in J is

- (1) $-\frac{4}{9}x$
- **(2)** $-x$
- (3) $-\frac{x}{9}$
- (4) $-4x$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $E_n = -R_H\left(\frac{Z^2}{n^2}\right)\,\mathrm{J}$
2. For $\mathrm{He^{+}}$ $(n = 1)$,
3. $E_n = -x = -R_H\left(\frac{2^2}{1^2}\right) = -4R_H$
4. $\therefore\ R_H = \frac{x}{4}$
5. For $\mathrm{Be^{3+}}$ $(n = 2)$,
6. $E_n = -R_H\left(\frac{Z^2}{n^2}\right)\,\mathrm{J}$
7. $= -\frac{x}{4}\times\left(\frac{4\times 4}{2\times 2}\right) = -x\,\mathrm{J}$

**Solved independently** (answer withheld)

1. For hydrogen-like species $E_n = -k\frac{Z^2}{n^2}$.
2. For $\mathrm{He^{+}}$, $n=1$: $E = -k\frac{2^2}{1^2} = -4k = -x$, so $k = \frac{x}{4}$.
3. For $\mathrm{Be^{3+}}$, $n=2$: $E = -k\frac{4^2}{2^2} = -4k$.
4. $-4k = -4 \times \frac{x}{4} = -x$, which is option $2$.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q064_45f2c74c_03112026.png?v=45f2c74cdf15)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q064_7fe37357_03112026.png?v=7fe3735794dd)

---

## Q65

Chemistry · physical · Electrochemistry

Match List I with List II.
List I (Conversion)
List II (Number of Faraday required)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | 1 mol of $\mathrm{H_2O}$ to $\mathrm{O_2}$ | I | $3\,\mathrm{F}$ |
| B | 1 mol of $\mathrm{MnO_4^-}$ to $\mathrm{Mn^{2+}}$ | II | $2\,\mathrm{F}$ |
| C | 1.5 mol of $\mathrm{Ca}$ from molten $\mathrm{CaCl_2}$ | III | $1\,\mathrm{F}$ |
| D | 1 mol of $\mathrm{FeO}$ to $\mathrm{Fe_2O_3}$ | IV | $5\,\mathrm{F}$ |

- (1) A-III, B-IV, C-II, D-I
- **(2)** A-II, B-IV, C-I, D-III
- (3) A-III, B-IV, C-I, D-II
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $4\mathrm{OH^-} \rightarrow 2\mathrm{H_2O} + \mathrm{O_2} + 4e^-$
2. for $2$ mole of $\mathrm{H_2O}$ = $4\mathrm{F}$ charge is required
3. for $1$ mole of $\mathrm{H_2O}$ = $\frac{4\mathrm{F}}{2}$ = $2\mathrm{F}$ required
4. $\overset{+7}{\mathrm{Mn}}\mathrm{O_4^-} \rightarrow \overset{+2}{\mathrm{Mn}}{}^{2+}$
5. for $1$ mole $\mathrm{MnO_4^-}$ $5\mathrm{F}$ charge is required
6. $\mathrm{Ca^{2+}} \xrightarrow{+2e^-} \mathrm{Ca}$
7. For $1$ mole $\mathrm{Ca^{2+}}$ ion required = $2\mathrm{F}$
8. $1.5$ mole $\mathrm{Ca^{2+}}$ ion required = $\frac{2}{1} \times 1.5$ = $3\mathrm{F}$
9. $\overset{+2}{\mathrm{Fe}}\mathrm{O} \rightarrow \overset{+3}{\mathrm{Fe}}\mathrm{_2O_3}$
10. for $1$ mole $\mathrm{FeO}$, $1\mathrm{F}$ charge is required.

**Solved independently** (answer withheld)

1. A: $\mathrm{H_2O} \rightarrow \frac{1}{2}\mathrm{O_2} + 2\mathrm{H^+} + 2e^-$, oxygen goes from $-2$ to $0$, so $2\,\mathrm{F}$ per mol (II).
2. B: $\mathrm{MnO_4^-} + 8\mathrm{H^+} + 5e^- \rightarrow \mathrm{Mn^{2+}} + 4\mathrm{H_2O}$, Mn goes from $+7$ to $+2$, so $5\,\mathrm{F}$ (IV).
3. C: $\mathrm{Ca^{2+}} + 2e^- \rightarrow \mathrm{Ca}$, so $1.5 \times 2 = 3\,\mathrm{F}$ (I).
4. D: In $\mathrm{FeO} \rightarrow \frac{1}{2}\mathrm{Fe_2O_3}$, Fe goes from $+2$ to $+3$, so $1\,\mathrm{F}$ per mol (III).
5. A-II, B-IV, C-I, D-III matches option $2$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q065_be543688_03112026.png?v=be543688b3cc)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q065_4b778b70_03112026.png?v=4b778b7000e2)

---

## Q66

Chemistry · physical · Basic Concepts of Chemistry

$1\,\mathrm{gram}$ of sodium hydroxide was treated with $25\,\mathrm{mL}$ of $0.75\,\mathrm{M}$ $\mathrm{HCl}$ solution, the mass of sodium hydroxide left unreacted is equal to

- (1) $200\,\mathrm{mg}$
- (2) $750\,\mathrm{mg}$
- **(3)** $250\,\mathrm{mg}$
- (4) Zero $\mathrm{mg}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{M} = \frac{\mathrm{W} \times 1000}{\mathrm{M_2} \times \mathrm{V}\ (\text{in mL})}$
2. $\mathrm{W} = \frac{\mathrm{M} \times \mathrm{M_2} \times \mathrm{V}\ (\text{in mL})}{1000} = \frac{0.75 \times 36.5 \times 25}{1000}$
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
5. Mass left $= 0.00625 \times 40 = 0.25\,\mathrm{g} = 250\,\mathrm{mg}$, which is option $3$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q066_1f55699d_03112026.png?v=1f55699dd540)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q066_9a13ec9f_03112026.png?v=9a13ec9f6a52)

---

## Q67

Chemistry · organic · General Organic Chemistry

The most stable carbocation among the following is :

- **(1)** 1-methylcyclohexyl cation `C[C+]1CCCCC1` ![1-methylcyclohexyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_option_1_s1_6a144549_04112026.svg?v=6a1445496db4)
- (2) 2-methylpentan-3-yl cation `CC[CH+]C(C)C` ![2-methylpentan-3-yl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_option_2_s1_8a3210fb_04112026.svg?v=8a3210fb1a2a)
- (3) 4-methylpentan-2-yl cation `C[CH+]CC(C)C` ![4-methylpentan-2-yl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_option_3_s1_34ac5544_04112026.svg?v=34ac5544f031)
- (4) cyclopentylmethyl cation `[CH2+]C1CCCC1` ![cyclopentylmethyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_option_4_s1_8adbcb30_04112026.svg?v=8adbcb30ef6b)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The stability of carbocation can be described by the hyperconjugation.
2. Greater the extent of hyperconjugation, more is the stability of carbocation.

![printed figure: 1-methylcyclohexyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q067_sol_1_0db126d5_03112026.png?v=0db126d5e5af)

*1-methylcyclohexyl cation*

![drawn: 1-methylcyclohexyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_solution_1_20493a7e_04112026.svg?v=20493a7e5b96)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. (1) $\rightarrow 7\ \alpha\text{-H}$

![printed figure: 2-methylpentan-3-yl cation](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q067_sol_2_0403efa6_03112026.png?v=0403efa60fb0)

*2-methylpentan-3-yl cation*

![drawn: 2-methylpentan-3-yl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_solution_2_094b4cb1_04112026.svg?v=094b4cb13fe8)  
*drawn by RDKit (code/lib/chem_cards.py)*

4. (2) $\rightarrow 3\ \alpha\text{-H}$

![printed figure: 4-methylpentan-2-yl cation](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q067_sol_3_3dd186ad_03112026.png?v=3dd186ad4792)

*4-methylpentan-2-yl cation*

![drawn: 4-methylpentan-2-yl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_solution_3_a4d5fa37_04112026.svg?v=a4d5fa372e67)  
*drawn by RDKit (code/lib/chem_cards.py)*

5. (3) $\rightarrow 5\ \alpha\text{-H}$

![printed figure: cyclopentylmethyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q067_sol_4_edcae7d6_03112026.png?v=edcae7d6fb72)

*cyclopentylmethyl cation*

![drawn: cyclopentylmethyl cation](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q067_solution_4_1d61fc69_04112026.svg?v=1d61fc6974b9)  
*drawn by RDKit (code/lib/chem_cards.py)*

6. (4) $\rightarrow 1\ \alpha\text{-H}$
7. Stability order of carbocations = (1) > (3) > (2) > (4)

**Solved independently** (answer withheld)

1. Option 1: the positive carbon of the ring also carries $\mathrm{CH_3}$ and two ring carbons, so it is a $3^\circ$ carbocation.
2. Option 2: $\mathrm{CH_3CH_2\overset{+}{C}HCH(CH_3)_2}$ has the positive carbon bonded to two carbons, so it is $2^\circ$.
3. Option 3: $\mathrm{CH_3\overset{+}{C}HCH_2CH(CH_3)_2}$ is also $2^\circ$.
4. Option 4: $\mathrm{C_5H_9\overset{+}{C}H_2}$ is a $1^\circ$ carbocation.
5. Stability order by hyperconjugation and $+I$ effect is $3^\circ > 2^\circ > 1^\circ$, so the most stable is option $1$.

**Subtopic:** Hyperconjugation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q067_9b8b23e4_03112026.png?v=9b8b23e45d6e)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q067_c9980e9c_03112026.png?v=c9980e9c6081)

---

## Q68

Chemistry · physical · Chemical Equilibrium

In which of the following equilibria, $K_p$ and $K_c$ are NOT equal?

- (1) $\mathrm{2BrCl_{(g)} \rightleftharpoons Br_{2(g)} + Cl_{2(g)}}$
- **(2)** $\mathrm{PCl_{5(g)} \rightleftharpoons PCl_{3(g)} + Cl_{2(g)}}$
- (3) $\mathrm{H_{2(g)} + I_{2(g)} \rightleftharpoons 2HI_{(g)}}$
- (4) $\mathrm{CO_{(g)} + H_2O_{(g)} \rightleftharpoons CO_{2(g)} + H_{2(g)}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $K_p = K_c (RT)^{\Delta n_g}$
2. for $K_p \neq K_c$,
3. $\Delta n_g \neq 0$
4. $\Delta n_g = n_p - n_r$
5. (1) $\Delta n_g = 2 - 2 = 0$
6. (2) $\Delta n_g = 2 - 1 = 1$
7. (3) $\Delta n_g = 2 - 2 = 0$
8. (4) $\Delta n_g = 2 - 2 = 0$

**Solved independently** (answer withheld)

1. $K_p = K_c (RT)^{\Delta n_g}$, so $K_p \neq K_c$ only when $\Delta n_g \neq 0$.
2. Option 1: $\Delta n_g = (1+1) - 2 = 0$.
3. Option 2: $\Delta n_g = (1+1) - 1 = 1$.
4. Option 3: $\Delta n_g = 2 - (1+1) = 0$.
5. Option 4: $\Delta n_g = (1+1) - (1+1) = 0$.
6. Only option $2$ has $\Delta n_g \neq 0$, so $K_p = K_c RT \neq K_c$.

**Subtopic:** Homogeneous and Heterogeneous Equilibria · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q068_c7fac88b_03112026.png?v=c7fac88b38f0)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q068_6e87a831_03112026.png?v=6e87a831f1ba)

---

## Q69

Chemistry · inorganic · The D- and F-Block Elements – Practice

The $E^\circ$ value for the $\mathrm{Mn^{3+}/Mn^{2+}}$ couple is more positive than that of $\mathrm{Cr^{3+}/Cr^{2+}}$ or $\mathrm{Fe^{3+}/Fe^{2+}}$ due to change of

- (1) $d^{3}$ to $d^{5}$ configuration
- (2) $d^{5}$ to $d^{4}$ configuration
- (3) $d^{5}$ to $d^{2}$ configuration
- **(4)** $d^{4}$ to $d^{5}$ configuration

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $E^{\circ}_{\mathrm{Mn^{3+}/Mn^{2+}}} > E^{\circ}_{\mathrm{Cr^{3+}/Cr^{2+}}}$ or $E^{\circ}_{\mathrm{Fe^{3+}/Fe^{2+}}}$
2. Electronic configuration of $\mathrm{Mn^{3+}} = [\mathrm{Ar}]3d^{4}$
3. Electronic configuration of $\mathrm{Mn^{2+}} = [\mathrm{Ar}]3d^{5}$
4. Electronic configuration of $\mathrm{Cr^{3+}} = [\mathrm{Ar}]3d^{3}$
5. Electronic configuration of $\mathrm{Cr^{2+}} = [\mathrm{Ar}]3d^{4}$
6. As $\mathrm{Mn^{3+}}$ from $d^{4}$ configuration goes to more stable $d^{5}$ configuration (Half filled), due to more exchange energy in $d^{5}$ configuration.

**Solved independently** (answer withheld)

1. $\mathrm{Mn^{3+}}$ is $[\mathrm{Ar}]\,3d^{4}$ and $\mathrm{Mn^{2+}}$ is $[\mathrm{Ar}]\,3d^{5}$.
2. Reduction $\mathrm{Mn^{3+}} + e^- \rightarrow \mathrm{Mn^{2+}}$ changes $d^{4}$ to the half-filled, extra-stable $d^{5}$, so $E^\circ$ is strongly positive.
3. The change is $d^{4} \rightarrow d^{5}$, which is option $4$.

**Subtopic:** Trends of Electrode Potentials · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q069_f5d23230_03112026.png?v=f5d232308137)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q069_4dfdc6da_03112026.png?v=4dfdc6da105d)

---

## Q70

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Fehling’s solution ‘A’ is

- (1) aqueous sodium citrate
- **(2)** aqueous copper sulphate
- (3) alkaline copper sulphate
- (4) alkaline solution of sodium potassium tartrate (Rochelle’s salt)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Fehling solution ‘A’ = Aqueous copper sulphate
2. Fehling solution ‘B’ = Alkaline sodium potassium tartrate (Rochelle salt)

**Solved independently** (answer withheld)

1. Fehling's reagent is prepared by mixing Fehling A (aqueous $\mathrm{CuSO_4}$) with Fehling B (alkaline sodium potassium tartrate), so Fehling A is option $2$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 29)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q070_5a1241cd_03112026.png?v=5a1241cd8d44)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q070_fbb9d5b8_03112026.png?v=fbb9d5b8c4d4)

---

## Q71

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List I with List II. List I (Reaction) List II (Reagents/Condition) Choose the correct answer from the options given below:

![printed figure: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → diphenylmethanone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q071_efb471a7_04112026.png?v=efb471a70182)

*A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → diphenylmethanone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$*

![drawn: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → diphenylmethanone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_0d251026_04112026.svg?v=0d2510266d7f)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: cyclohexylidenecyclohexane `C1CCC(=C2CCCCC2)CC1` ![cyclohexylidenecyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s1_957a6cb4_04112026.svg?v=957a6cb425a6); cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s2_ecae2398_04112026.svg?v=ecae2398c700); benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s3_dbf27a87_04112026.svg?v=dbf27a872e50); diphenylmethanone `O=C(c1ccccc1)c1ccccc1` ![diphenylmethanone](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s4_4a6ed161_04112026.svg?v=4a6ed161623c); cyclohexanol `OC1CCCCC1` ![cyclohexanol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s5_b130dcca_04112026.svg?v=b130dccaeb49); cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s6_ecae2398_04112026.svg?v=ecae2398c700); ethylbenzene `CCc1ccccc1` ![ethylbenzene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s7_c3cd0ee9_04112026.svg?v=c3cd0ee97328); potassium benzoate `O=C([O-])c1ccccc1.[K+]` ![potassium benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s8_d32e872f_04112026.svg?v=d32e872ffccb); benzoyl chloride `O=C(Cl)c1ccccc1` ![benzoyl chloride](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_question_s9_56febcfe_04112026.svg?v=56febcfef378)

| List-I | | List-II | |
|---|---|---|---|
| A | [reaction drawn as structures; see figure] | I | [structure; see figure] Cl/Anhyd. $\mathrm{AlCl_3}$ |
| B | [reaction drawn as structures; see figure] | II | $\mathrm{CrO_3}$ |
| C | [reaction drawn as structures; see figure] | III | $\mathrm{KMnO_4/KOH}$, $\Delta$ |
| D | [reaction drawn as structures; see figure] | IV | (i) $\mathrm{O_3}$ (ii) $\mathrm{Zn\text{-}H_2O}$ |

- (1) A-I, B-IV, C-II, D-III
- (2) A-IV, B-I, C-III, D-II
- (3) A-III, B-I, C-II, D-IV
- **(4)** A-IV, B-I, C-II, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: (A) cyclohexylidenecyclohexane →((i) $\ce{O3}$; (ii) Zn-$\ce{H2O}$) 2 cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q071_sol_1_a1e79cab_03112026.png?v=a1e79cab127a)

*(A) cyclohexylidenecyclohexane →[(i) $\ce{O3}$; (ii) Zn-$\ce{H2O}$] 2 cyclohexanone*

![drawn: (A) cyclohexylidenecyclohexane →((i) $\ce{O3}$; (ii) Zn-$\ce{H2O}$) 2 cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_solution_1_d6bab421_04112026.svg?v=d6bab4212d1e)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. It is reductive ozonolysis

![printed figure: (B) benzene →(benzoyl chloride/Anhyd. $\ce{AlCl3}$) diphenylmethanone](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q071_sol_2_a5b70ba7_03112026.png?v=a5b70ba7d721)

*(B) benzene →[benzoyl chloride/Anhyd. $\ce{AlCl3}$] diphenylmethanone*

![drawn: (B) benzene →(benzoyl chloride/Anhyd. $\ce{AlCl3}$) diphenylmethanone](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_solution_2_f44e74fe_04112026.svg?v=f44e74fe20c5)  
*drawn by RDKit (code/lib/chem_cards.py)*

2. It is Friedel-Crafts acylation reaction.

![printed figure: (C) cyclohexanol →($\ce{CrO3}$) cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q071_sol_3_847534ee_03112026.png?v=847534ee335f)

*(C) cyclohexanol →[$\ce{CrO3}$] cyclohexanone*

![drawn: (C) cyclohexanol →($\ce{CrO3}$) cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_solution_3_ed8865a0_04112026.svg?v=ed8865a0b203)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. Secondary alcohols are oxidised to ketones by $\mathrm{CrO_3}$

![printed figure: (D) ethylbenzene →($\ce{KMnO4}$; KOH, Δ) potassium benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q071_sol_4_6791b67c_03112026.png?v=6791b67c6c1b)

*(D) ethylbenzene →[$\ce{KMnO4}$; KOH, Δ] potassium benzoate*

![drawn: (D) ethylbenzene →($\ce{KMnO4}$; KOH, Δ) potassium benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q071_solution_4_46428010_04112026.svg?v=46428010ded1)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. A: ozonolysis of the $C=C$ in cyclohexylidenecyclohexane with $\mathrm{O_3}$ then $\mathrm{Zn\text{-}H_2O}$ gives $2$ cyclohexanone, so A-IV.
2. B: benzene with $\mathrm{C_6H_5COCl}$/anhyd. $\mathrm{AlCl_3}$ (Friedel-Crafts acylation) gives benzophenone, so B-I.
3. C: $\mathrm{CrO_3}$ oxidises the secondary alcohol cyclohexanol to cyclohexanone, so C-II.
4. D: $\mathrm{KMnO_4/KOH}$, $\Delta$ oxidises the side chain of ethylbenzene to $\mathrm{C_6H_5COOK}$, so D-III.
5. A-IV, B-I, C-II, D-III matches option $4$.

**Subtopic:** Preparation of Ketones, Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q071_4b7637b2_03112026.png?v=4b7637b2cde7)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q071_1e678328_03112026.png?v=1e678328043d)

---

## Q72

Chemistry · physical · Thermodynamics

In which of the following processes entropy increases? Choose the correct answer from the options given below:

- (A) A liquid evaporates to vapour.
- (B) Temperature of a crystalline solid lowered from $130\,\mathrm{K}$ to $0\,\mathrm{K}$.
- (C) $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$
- (D) $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$

- (1) C and D
- (2) A and C
- (3) A, B and D
- **(4)** A, C and D

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. When a liquid evaporates to vapour entropy increases.
2. $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$
3. Number of gaseous product molecules increases so entropy increases.
4. $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$
5. 1 mole $\mathrm{Cl_{2(g)}}$ form 2 mol $\mathrm{Cl_{(g)}}$. So entropy increases.

**Solved independently** (answer withheld)

1. A: evaporation changes liquid to vapour, so disorder increases and $\Delta S > 0$.
2. B: cooling a crystalline solid from $130\,\mathrm{K}$ to $0\,\mathrm{K}$ reduces molecular motion, so $\Delta S < 0$.
3. C: $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$ gives $\Delta n_g = +2$, so $\Delta S > 0$.
4. D: $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$ gives $\Delta n_g = +1$, so $\Delta S > 0$.
5. Entropy increases in A, C and D, which is option $4$.

**Subtopic:** Entropy, Second Law & Third Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q072_ecc25f9a_03112026.png?v=ecc25f9ae0bb)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q072_ddd756b6_03112026.png?v=ddd756b60f8a)

---

## Q73

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

A compound with a molecular formula of $\mathrm{C_6H_{14}}$ has two tertiary carbons. Its IUPAC name is :

- (1) 2,2-dimethylbutane
- (2) n-hexane
- (3) 2-methylpentane
- **(4)** 2,3-dimethylbutane

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{CH_3 - CH_2 - CH_2 - CH_2 - CH_2 - CH_3}$ has no tertiary carbon
2. (n-Hexane)

![printed figure: 2-methylpentane, carbons numbered 5, 4, 3, 2, 1 from left to right with the methyl branch on C-2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q073_sol_1_61759097_03112026.png?v=617590974924)

*2-methylpentane, carbons numbered 5, 4, 3, 2, 1 from left to right with the methyl branch on C-2*

![drawn: 2-methylpentane, carbons numbered 5, 4, 3, 2, 1 from left to right with the methyl branch on C-2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q073_solution_1_5c95d1e4_04112026.svg?v=5c95d1e49218)  
*drawn by RDKit (code/lib/chem_cards.py)*

3. has only one tertiary carbon
4. (2-Methylpentane)

![printed figure: 2,3-dimethylbutane, carbons numbered 1, 2, 3, 4 from left to right with methyl branches on C-2 and C-3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q073_sol_2_9ac72b8f_03112026.png?v=9ac72b8f6d2e)

*2,3-dimethylbutane, carbons numbered 1, 2, 3, 4 from left to right with methyl branches on C-2 and C-3*

![drawn: 2,3-dimethylbutane, carbons numbered 1, 2, 3, 4 from left to right with methyl branches on C-2 and C-3](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q073_solution_2_eadd440c_04112026.svg?v=eadd440c56d7)  
*drawn by RDKit (code/lib/chem_cards.py)*

5. has two tertiary carbon.
6. (2, 3-Dimethylbutane)

![printed figure: 2,2-dimethylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q073_sol_3_60538104_03112026.png?v=60538104e71b)

*2,2-dimethylbutane*

![drawn: 2,2-dimethylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q073_solution_3_a70235ca_04112026.svg?v=a70235ca8fe5)  
*drawn by RDKit (code/lib/chem_cards.py)*

7. has no tertiary carbon
8. (2, 2-Dimethylbutane)

**Solved independently** (answer withheld)

1. A tertiary carbon is bonded to exactly three other carbons.
2. $\mathrm{CH_3-CH(CH_3)-CH(CH_3)-CH_3}$ (2,3-dimethylbutane, $\mathrm{C_6H_{14}}$): $C_2$ and $C_3$ are each bonded to three carbons, so it has $2$ tertiary carbons.
3. 2-methylpentane has $1$ tertiary carbon ($C_2$); 2,2-dimethylbutane has $0$ (its $C_2$ is quaternary); n-hexane has $0$.
4. Only 2,3-dimethylbutane has two tertiary carbons, which is option $4$.

**Subtopic:** Acyclic or Open Chain Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q073_70bce8fa_03112026.png?v=70bce8fa0cc1)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q073_e94d5ef0_03112026.png?v=e94d5ef09780)

---

## Q74

Chemistry · physical · Chemical Equilibrium

For the reaction $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$. At a given time, the composition of reaction mixture is: $[\mathrm{A}] = [\mathrm{B}] = [\mathrm{C}] = 2 \times 10^{-3}\,\mathrm{M}$. Then, which of the following is correct?

- (1) Reaction has gone to completion in forward direction.
- (2) Reaction is at equilibrium.
- (3) Reaction has a tendency to go in forward direction.
- **(4)** Reaction has a tendency to go in backward direction.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$
2. At a given time t, $Q_C$ is to be calculated and been compared with $K_C$.
3. $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^2} = \frac{(2 \times 10^{-3})(2 \times 10^{-3})}{(2 \times 10^{-3})^2}$
4. $Q_C = 1$
5. As $Q_C > K_C$, so reaction has a tendency to move backward.

**Solved independently** (answer withheld)

1. $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^2}$.
2. $Q_C = \frac{(2\times10^{-3})(2\times10^{-3})}{(2\times10^{-3})^2} = 1$.
3. $Q_C = 1 > K_C = 4\times10^{-3}$, so the reaction has a tendency to go in the backward direction, which is option $4$.

**Subtopic:** Predicting the Extent and Direction of a Reaction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q074_e88a840e_03112026.png?v=e88a840ef11a)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q074_72c9610e_03112026.png?v=72c9610e5f14)

---

## Q75

Chemistry · organic · Hydrocarbons

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The boiling point of three isomeric pentanes follows the order n-pentane $>$ isopentane $>$ neopentane
- (Statement II) When branching increases, the molecule attains a shape of sphere. This results in smaller surface area for contact, due to which the intermolecular forces between the spherical molecules are weak, thereby lowering the boiling point.

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

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
3. Both statements are correct, which is option $2$.

**Subtopic:** Physical Properties of Alkanes, Alkenes and Alkynes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q075_cf54b70d_03112026.png?v=cf54b70d0b59)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q075_fb8c58b1_03112026.png?v=fb8c58b14782)

---

## Q76

Chemistry · organic · Alcohols, Phenols and Ethers

Which one of the following alcohols reacts instantaneously with Lucas reagent?

- **(1)** 2-methylpropan-2-ol `CC(C)(C)O` ![2-methylpropan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q076_option_1_s1_51170735_04112026.svg?v=51170735efa7)
- (2) $\mathrm{CH_3-CH_2-CH_2-CH_2OH}$
- (3) butan-2-ol `CCC(C)O` ![butan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q076_option_3_s1_246d1e4e_04112026.svg?v=246d1e4e3f48)
- (4) 2-methylpropan-1-ol `CC(C)CO` ![2-methylpropan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q076_option_4_s1_44b6a2e7_04112026.svg?v=44b6a2e7f8a5)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Tertiary alcohols react instantaneously with Lucas reagent and gives immediate turbidity.
2. In case of tertiary alcohols, they form halides easily with Lucas reagent (conc. $\mathrm{HCl}$ and $\mathrm{ZnCl_2}$)

**Solved independently** (answer withheld)

1. Lucas reagent (conc. $\mathrm{HCl} + \mathrm{ZnCl_2}$) reacts via a carbocation, so the rate order is $3^\circ > 2^\circ > 1^\circ$; only $3^\circ$ alcohols give turbidity immediately.
2. Option 1, $\mathrm{(CH_3)_3C-OH}$, is a $3^\circ$ alcohol.
3. Option 2, $\mathrm{CH_3CH_2CH_2CH_2OH}$, and option 4, $\mathrm{(CH_3)_2CH-CH_2OH}$, are $1^\circ$ alcohols; option 3, $\mathrm{CH_3CH_2CH(OH)CH_3}$, is $2^\circ$.
4. So the alcohol that reacts instantaneously is $\mathrm{(CH_3)_3C-OH}$, option $1$.

**Subtopic:** Test of Alcohol · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q076_5778a224_03112026.png?v=5778a224e515)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q076_4dbb3d90_03112026.png?v=4dbb3d90fde6)

---

## Q77

Chemistry · physical · Solutions

The Henry’s law constant ($K_\mathrm{H}$) values of three gases (A, B, C) in water are 145, $2 \times 10^{-5}$ and $35\,\mathrm{kbar}$, respectively. The solubility of these gases in water follow the order:

- (1) A > B > C
- (2) B > A > C
- **(3)** B > C > A
- (4) A > C > B

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Value of Henry’s law constant $\propto \frac{1}{\text{Solubility of gas}}$
2. Higher the value of $K_\mathrm{H}$ at a given pressure, lower is the solubility of the gas in the liquid.
3. $K_\mathrm{H}$ value of gases (given) : $A > C > B$
4. $\therefore$ Order of solubility of gases in water : $B > C > A$

**Solved independently** (answer withheld)

1. Henry's law: $p = K_\mathrm{H}\,x$, so at a given pressure $x = \frac{p}{K_\mathrm{H}}$ and solubility $\propto \frac{1}{K_\mathrm{H}}$.
2. Order of constants: $K_\mathrm{H}(B) = 2\times10^{-5} < K_\mathrm{H}(C) = 35 < K_\mathrm{H}(A) = 145\,\mathrm{kbar}$.
3. Hence solubility order is $B > C > A$, which is option $3$.

**Subtopic:** Solubility of a Gas in a Liquid · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 32)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q077_98c7e560_03112026.png?v=98c7e560362e)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q077_9bf35ae4_03112026.png?v=9bf35ae4be55)

---

## Q78

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

On heating, some solid substances change from solid to vapour state without passing through liquid state. The technique used for the purification of such solid substances based on the above principle is known as

- (1) Chromatography
- (2) Crystallization
- **(3)** Sublimation
- (4) Distillation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (1) Chromatography : It is based on separation by using stationary and mobile phase.
2. (2) Crystallization : It is based on difference in the solubilities of the compound and impurities in a suitable solvent.
3. (3) Sublimation : It is the purification technique based on principle that on heating, some solid substances change from solid to vapour state without passing through liquid state.
4. (4) Distillation : It is used to separate volatile liquids from non-volatile impurities and the liquids having sufficient difference in their boiling point.

**Solved independently** (answer withheld)

1. A solid passing directly to vapour on heating, skipping the liquid state, is sublimation, so the purification technique is sublimation, option $3$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q078_8aa60c29_03112026.png?v=8aa60c295259)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q078_73ef7f08_03112026.png?v=73ef7f08b468)

---

## Q79

Chemistry · inorganic · Coordination Compounds – Practice

Match List I with List II.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
|  | List I (Complex) |  | List II (Type of isomerism) |
| A | $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ | I | Solvate isomerism |
| B | $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ | II | Linkage isomerism |
| C | $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ | III | Ionization isomerism |
| D | $\mathrm{[Co(H_2O)_6]Cl_3}$ | IV | Coordination isomerism |

- (1) A-II, B-IV, C-III, D-I
- **(2)** A-II, B-III, C-IV, D-I
- (3) A-I, B-III, C-IV, D-II
- (4) A-I, B-IV, C-III, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A. $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ — II. Linkage isomerism due to ‘N’ and ‘O’ linkage by $\mathrm{NO_2}$
2. B. $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ — III. Ionization isomerism
3. C. $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ — IV. Coordination isomerism
4. D. $\mathrm{[Co(H_2O)_6]Cl_3}$ — I. Solvate isomerism

**Solved independently** (answer withheld)

1. $\mathrm{NO_2^-}$ in $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ is ambidentate (N- or O-bonded), so A shows linkage isomerism: A-II.
2. In $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ the $\mathrm{SO_4^{2-}}$ and $\mathrm{Br^-}$ can swap between coordination sphere and counter-ion, so B shows ionization isomerism: B-III.
3. $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ has complex cation and complex anion that can exchange ligands, so C shows coordination isomerism: C-IV.
4. In $\mathrm{[Co(H_2O)_6]Cl_3}$ water can be coordinated or lattice water, so D shows solvate (hydrate) isomerism: D-I.
5. A-II, B-III, C-IV, D-I is option $2$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q079_836988ef_03112026.png?v=836988ef022c)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q079_682ac24f_03112026.png?v=682ac24f2b48)

---

## Q80

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Intramolecular hydrogen bonding is present in

- (1) $\mathrm{HF}$
- **(2)** 2-nitrophenol `O=[N+]([O-])c1ccccc1O` ![2-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q080_option_2_s1_af8d6416_04112026.svg?v=af8d641635dd)
- (3) 4-nitrophenol `O=[N+]([O-])c1ccc(O)cc1` ![4-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q080_option_3_s1_061f32a8_04112026.svg?v=061f32a8ba54)
- (4) 3-nitrophenol `O=[N+]([O-])c1cccc(O)c1` ![3-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q080_option_4_s1_683e3fc0_04112026.svg?v=683e3fc063ee)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In o-nitrophenol intramolecular H-bonding is present.

![printed figure: 2-nitrophenol with a dotted intramolecular hydrogen bond from the OH hydrogen to a nitro oxygen, labelled H-bonding](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q080_sol_1_52177da3_03112026.png?v=52177da34198)

*2-nitrophenol with a dotted intramolecular hydrogen bond from the OH hydrogen to a nitro oxygen, labelled H-bonding*

![drawn: 2-nitrophenol with a dotted intramolecular hydrogen bond from the OH hydrogen to a nitro oxygen, labelled H-bonding](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q080_solution_1_90862b83_04112026.svg?v=90862b837506)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. HF forms hydrogen bonds only between separate molecules (intermolecular), so option $1$ is out.
2. In o-nitrophenol (option $2$) the $-\mathrm{OH}$ and $-\mathrm{NO_2}$ groups are on adjacent carbons, close enough for $\mathrm{O{-}H \cdots O{=}N}$ to form a six-membered ring within the molecule: intramolecular H-bonding.
3. In p-nitrophenol (option $3$) and m-nitrophenol (option $4$) the groups are too far apart, so their H-bonding is intermolecular. The answer is option $2$.

**Subtopic:** Hydrogen Bonding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q080_858ee914_03112026.png?v=858ee914b38d)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q080_1cd1338d_03112026.png?v=1cd1338dfc4c)

---

## Q81

Chemistry · organic · Amines

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Aniline does not undergo Friedel-Crafts alkylation reaction.
- (Statement II) Aniline cannot be prepared through Gabriel synthesis.

- (1) Statement I is incorrect but Statement II is true
- **(2)** Both statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- (4) Statement I is correct but Statement II is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Aniline does not undergo Friedel-Crafts alkylation reaction due to salt formation with aluminium chloride, the Lewis acid, which is used as a catalyst.
2. Aniline (aromatic primary amine) cannot be prepared by Gabriel phthalimide synthesis because aryl halides do not undergo nucleophilic substitution with anion formed by phthalimide.

**Solved independently** (answer withheld)

1. Statement I: aniline (a Lewis base) reacts with the Lewis acid catalyst $\mathrm{AlCl_3}$ to form a salt, so the ring is deactivated and Friedel-Crafts alkylation does not occur; Statement I is true.
2. Statement II: Gabriel synthesis needs $S_N2$ attack of potassium phthalimide on an alkyl halide; aryl halides do not undergo this substitution, so aniline (a primary aromatic amine) cannot be made this way; Statement II is true.
3. Both statements are true, which is option $2$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions), Methods of Preparation of Amines · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q081_3090b4ae_03112026.png?v=3090b4aef13b)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q081_95d40b62_03112026.png?v=95d40b625d40)

---

## Q82

Chemistry · inorganic · The p–Block Elements

Among Group 16 elements, which one does NOT show $-2$ oxidation state?

- **(1)** $\mathrm{Po}$
- (2) $\mathrm{O}$
- (3) $\mathrm{Se}$
- (4) $\mathrm{Te}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Oxygen shows $-2$, $-1$, $+1$ and $+2$ oxidation states
2. Selenium shows $-2$, $+2$, $+4$ and $+6$ oxidation states
3. Tellurium shows $-2$, $+2$, $+4$ and $+6$ oxidation states
4. Polonium shows $+2$ and $+4$ oxidation states

**Solved independently** (answer withheld)

1. Down Group 16, stability of the $-2$ oxidation state decreases as metallic character increases; $\mathrm{O}$, $\mathrm{Se}$ and $\mathrm{Te}$ show $-2$, while $\mathrm{Po}$ hardly shows it, so the answer is option $1$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q082_173295fb_03112026.png?v=173295fbf8b6)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q082_388772de_03112026.png?v=388772de7d74)

---

## Q83

Chemistry · physical · Chemical Kinetics

Activation energy of any chemical reaction can be calculated if one knows the value of

- **(1)** rate constant at two different temperatures
- (2) rate constant at standard temperature
- (3) probability of collision
- (4) orientation of reactant molecules during collision

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. To calculate value of $E_{a}$
2. Equation used is $\log\left(\frac{k_{2}}{k_{1}}\right) = \frac{E_{a}}{2.303R}\left(\frac{1}{T_{1}} - \frac{1}{T_{2}}\right)$
3. Hence $E_{a}$ can be calculated if value of rate constant $k$ is known at two different temperatures $T_{1}$ and $T_{2}$.

**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$, with two unknowns $A$ and $E_a$.
2. Taking the ratio at two temperatures eliminates $A$: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. So $E_a = \frac{2.303\,R\,T_1 T_2 \log(k_2/k_1)}{T_2 - T_1}$ needs $k$ at two different temperatures, which is option $1$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q083_d565cf92_03112026.png?v=d565cf9280c4)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q083_7df52383_03112026.png?v=7df523836c56)

---

## Q84

Chemistry · inorganic · The D- and F-Block Elements – Practice

‘Spin only’ magnetic moment is same for which of the following ions? Choose the most appropriate answer from the options given below.

- (A) $\mathrm{Ti^{3+}}$
- (B) $\mathrm{Cr^{2+}}$
- (C) $\mathrm{Mn^{2+}}$
- (D) $\mathrm{Fe^{2+}}$
- (E) $\mathrm{Sc^{3+}}$

- (1) A and D only
- **(2)** B and D only
- (3) A and E only
- (4) B and C only

**Answer** — booklet: (2) · independent solve: (2) · agree

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
7. Only $\mathrm{Cr^{2+}}$ and $\mathrm{Fe^{2+}}$ share $n=4$, giving $\mu = \sqrt{24} \approx 4.90\,\text{BM}$ each, i.e. B and D, which is option $2$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q084_5b181e89_03112026.png?v=5b181e890a05)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q084_15720dbe_03112026.png?v=15720dbe64ff)

---

## Q85

Chemistry · physical · Chemical Kinetics

Which plot of $\ln k$ vs $\frac{1}{T}$ is consistent with Arrhenius equation?

- **(1)** ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with negative slope, starting at a positive intercept on the ln k axis and falling to meet the 1/T axis](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q085_option_1_78818527_03112026.png?v=788185277f95) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with negative slope, starting at a positive intercept on the ln k axis and falling to meet the 1/T axis*
- (2) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope, starting slightly below the origin and rising](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q085_option_2_6035b29f_03112026.png?v=6035b29f45e3) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope, starting slightly below the origin and rising*
- (3) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope, starting at a positive intercept on the ln k axis and rising](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q085_option_3_717d8011_03112026.png?v=717d8011e8e1) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope, starting at a positive intercept on the ln k axis and rising*
- (4) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope passing through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q085_option_4_4b90600d_03112026.png?v=4b90600d9aa1) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope passing through the origin*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The Arrhenius equation is given as
2. $k = Ae^{-\frac{E_a}{RT}}$
3. $\therefore \quad \ln k = \ln A - \frac{E_a}{RT}$
4. $\ln k$ v/s $\frac{1}{T}$ gives a straight line graph with slope $= -\frac{E_a}{R}$ and intercept $= \ln A$

![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with negative slope; the intercept on the ln k axis is labelled 'Intercept = ln A' and the line is labelled 'Slope = $-\frac{E_a}{R}$'](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q085_sol_1_d85c8cc2_03112026.png?v=d85c8cc221f9)

*graph of ln k (y-axis) vs 1/T (x-axis): a straight line with negative slope; the intercept on the ln k axis is labelled 'Intercept = ln A' and the line is labelled 'Slope = $-\frac{E_a}{R}$'*


**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$.
2. Taking logs: $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$.
3. A plot of $\ln k$ vs $\frac{1}{T}$ is a straight line with slope $-\frac{E_a}{R} < 0$ and intercept $\ln A$ on the $\ln k$ axis.
4. Only option $1$ shows a straight line falling from a positive intercept, so the answer is option $1$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q085_f9111b71_03112026.png?v=f9111b71b2eb)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q085_63594076_03112026.png?v=6359407608a7)

---

## Q86

Chemistry · inorganic · Principles Related to Practical Chemistry

Given below are certain cations. Using inorganic qualitative analysis, arrange them in increasing group number from 0 to VI.
Choose the correct answer from the options given below.

- (A) $\mathrm{Al^{3+}}$
- (B) $\mathrm{Cu^{2+}}$
- (C) $\mathrm{Ba^{2+}}$
- (D) $\mathrm{Co^{2+}}$
- (E) $\mathrm{Mg^{2+}}$

- (1) E, A, B, C, D
- **(2)** B, A, D, C, E
- (3) B, C, A, D, E
- (4) E, C, D, B, A

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: table of groups and cations: Group-II $\ce{Cu^2+}$; Group-III $\ce{Al^3+}$; Group-IV $\ce{Co^2+}$; Group-V $\ce{Ba^2+}$; Group-VI $\ce{Mg^2+}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q086_sol_1_257282b1_03112026.png?v=257282b19961)

*table of groups and cations: Group-II $\ce{Cu^2+}$; Group-III $\ce{Al^3+}$; Group-IV $\ce{Co^2+}$; Group-V $\ce{Ba^2+}$; Group-VI $\ce{Mg^2+}$*

1. The correct order of group number of ions is $\underset{(\mathrm{B})}{\mathrm{Cu^{2+}}} < \underset{(\mathrm{A})}{\mathrm{Al^{3+}}} < \underset{(\mathrm{D})}{\mathrm{Co^{2+}}} < \underset{(\mathrm{C})}{\mathrm{Ba^{2+}}} < \underset{(\mathrm{E})}{\mathrm{Mg^{2+}}}$
2. $\therefore$ The correct order is B, A, D, C, E

**Solved independently** (answer withheld)

1. $\mathrm{Cu^{2+}}$ is precipitated as sulphide by $\mathrm{H_2S}$ in dilute HCl, so it is group II.
2. $\mathrm{Al^{3+}}$ is precipitated as hydroxide by $\mathrm{NH_4OH}$ in presence of $\mathrm{NH_4Cl}$, so it is group III.
3. $\mathrm{Co^{2+}}$ is precipitated as sulphide by $\mathrm{H_2S}$ in ammoniacal medium, so it is group IV.
4. $\mathrm{Ba^{2+}}$ is precipitated as carbonate by $\mathrm{(NH_4)_2CO_3}$, so it is group V.
5. $\mathrm{Mg^{2+}}$ remains for group VI.
6. Increasing order: B (II), A (III), D (IV), C (V), E (VI), which is option $2$.

**Subtopic:** Group Analysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q086_4e757cf2_03112026.png?v=4e757cf2a983)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q086_775df639_03112026.png?v=775df639b3be)

---

## Q87

Chemistry · physical · Solutions

The plot of osmotic pressure ($\Pi$) vs concentration ($\mathrm{mol\,L^{-1}}$) for a solution gives a straight line with slope $25.73\,\mathrm{L\,bar\,mol^{-1}}$. The temperature at which the osmotic pressure measurement is done is (Use $R = 0.083\,\mathrm{L\,bar\,mol^{-1}\,K^{-1}}$)

- (1) $12.05\,^{\circ}\mathrm{C}$
- **(2)** $37\,^{\circ}\mathrm{C}$
- (3) $310\,^{\circ}\mathrm{C}$
- (4) $25.73\,^{\circ}\mathrm{C}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\Pi = \mathrm{CRT}$
2. Slope $= \mathrm{RT}$
3. $25.73 = 0.083 \times \mathrm{T}$
4. $\mathrm{T} = \frac{25.73}{0.083} = 309.47 \approx 310\,\mathrm{K}$
5. $\therefore$ Temperature in $^{\circ}\mathrm{C} = 310 - 273$
6. $= 37\,^{\circ}\mathrm{C}$

**Solved independently** (answer withheld)

1. From $\Pi = CRT$, a plot of $\Pi$ vs $C$ is a straight line with slope $RT$.
2. $RT = 25.73\,\mathrm{L\,bar\,mol^{-1}}$, so $T = \frac{25.73}{0.083} = 310\,\mathrm{K}$.
3. $310\,\mathrm{K} - 273 = 37\,^{\circ}\mathrm{C}$, which is option $2$.

**Subtopic:** Osmosis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q087_a8274fe7_03112026.png?v=a8274fe726e1)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q087_07fd1073_03112026.png?v=07fd10735c18)

---

## Q88

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the correct answer.

- **(1)** Three canonical forms can be drawn for $\mathrm{CO_3^{2-}}$ ion
- (2) Three resonance structures can be drawn for ozone
- (3) $\mathrm{BF_3}$ has non-zero dipole moment
- (4) Dipole moment of $\mathrm{NF_3}$ is greater than that of $\mathrm{NH_3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (1) (3 canonical forms)

![printed figure: carbonate ↔ carbonate ↔ carbonate (three resonance structures of $\ce{CO3^2-}$)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q088_sol_1_b52faa68_03112026.png?v=b52faa689d5a)

*carbonate ↔ carbonate ↔ carbonate (three resonance structures of $\ce{CO3^2-}$)*

![drawn: carbonate ↔ carbonate ↔ carbonate (three resonance structures of $\ce{CO3^2-}$)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q088_solution_1_28e533cf_04112026.svg?v=28e533cf460e)  
*drawn by RDKit (code/lib/chem_cards.py)*

2. (2) In ozone; there are two resonating structures.
3. (3) $\mathrm{BF_3}$ i.e., ; Dipole moment $= 0$

![printed figure: boron trifluoride with δ+ on B and δ− on each F, bond-dipole arrows pointing from B to each F](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q088_sol_2_e8efb9ad_03112026.png?v=e8efb9ad7af0)

*boron trifluoride with δ+ on B and δ− on each F, bond-dipole arrows pointing from B to each F*

![drawn: boron trifluoride with δ+ on B and δ− on each F, bond-dipole arrows pointing from B to each F](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q088_solution_2_6c191419_04112026.svg?v=6c19141930ea)  
*drawn by RDKit (code/lib/chem_cards.py)*

4. (4)

![printed figure: nitrogen trifluoride (0.80 × 10⁻³⁰ Cm) < ammonia (4.90 × 10⁻³⁰ Cm); each drawn with a lone pair on N and bond-dipole arrows](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q088_sol_3_76500289_03112026.png?v=765002894762)

*nitrogen trifluoride (0.80 × 10⁻³⁰ Cm) < ammonia (4.90 × 10⁻³⁰ Cm); each drawn with a lone pair on N and bond-dipole arrows*

![drawn: nitrogen trifluoride (0.80 × 10⁻³⁰ Cm) < ammonia (4.90 × 10⁻³⁰ Cm); each drawn with a lone pair on N and bond-dipole arrows](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q088_solution_3_c2ddcf12_04112026.svg?v=c2ddcf1251d7)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. In $\mathrm{CO_3^{2-}}$ the $\mathrm{C=O}$ double bond can sit on any of the three O atoms, giving three canonical forms, so statement 1 is true.
2. Ozone $\mathrm{O_3}$ has only two resonance structures, so statement 2 is false.
3. $\mathrm{BF_3}$ is trigonal planar and the three $\mathrm{B-F}$ bond dipoles cancel, so $\mu = 0$; statement 3 is false.
4. In $\mathrm{NH_3}$ the lone-pair moment adds to the $\mathrm{N-H}$ bond moments, while in $\mathrm{NF_3}$ it opposes the $\mathrm{N-F}$ bond moments, so $\mu(\mathrm{NH_3}) > \mu(\mathrm{NF_3})$; statement 4 is false.
5. Only statement 1 is correct, which is option $1$.

**Subtopic:** Bond Parameters, Dipole Moment · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q088_558c2ddb_03112026.png?v=558c2ddb60b0)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q088_bdc2fe27_03112026.png?v=bdc2fe27fd71)

---

## Q89

Chemistry · physical · Basic Concepts of Chemistry

A compound X contains $32\%$ of A, $20\%$ of B and remaining percentage of C. Then, the empirical formula of X is : (Given atomic masses of A $= 64$; B $= 40$; C $= 32\,\mathrm{u}$)

- (1) $\mathrm{ABC_4}$
- (2) $\mathrm{A_2BC_2}$
- **(3)** $\mathrm{ABC_3}$
- (4) $\mathrm{AB_2C_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Element A: mass percentage $32\%$; no. of moles $\frac{32}{64} = \frac{1}{2}$; no. of moles/smallest number $\frac{1}{2} \times 2$; simplest whole number $= 1$
2. Element B: mass percentage $20\%$; no. of moles $\frac{20}{40} = \frac{1}{2}$; no. of moles/smallest number $\frac{1}{2} \times 2$; simplest whole number $= 1$
3. Element C: mass percentage $48\%$; no. of moles $\frac{48}{32} = \frac{3}{2}$; no. of moles/smallest number $\frac{3}{2} \times 2$; simplest whole number $= 3$
4. So, empirical formula of $X = \begin{matrix} \mathrm{A} & : & \mathrm{B} & : & \mathrm{C} \\ 1 & : & 1 & : & 3 \end{matrix}$
5. $\therefore$ The correct empirical formula of compound X is $\mathrm{ABC_3}$

**Solved independently** (answer withheld)

1. Percentage of C $= 100 - 32 - 20 = 48\%$.
2. Moles in 100 g: $n_A = \frac{32}{64} = 0.5$, $n_B = \frac{20}{40} = 0.5$, $n_C = \frac{48}{32} = 1.5$.
3. Divide by the smallest ($0.5$): $A:B:C = 1:1:3$.
4. Empirical formula $= \mathrm{ABC_3}$, which is option $3$.

**Subtopic:** Empirical and Molecular Formula · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q089_e7bd3bad_03112026.png?v=e7bd3bad8370)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q089_01c1c2ce_03112026.png?v=01c1c2cea5a5)

---

## Q90

Chemistry · organic · Haloalkanes and Haloarenes

Major products A and B formed in the following reaction sequence, are

![printed figure: 2-methylcyclohexan-1-ol →(PBr₃) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q090_89db2594_04112026.png?v=89db25940ae8)

*2-methylcyclohexan-1-ol →[PBr₃] A (major) →[alc. KOH, Δ] B (major)*

![drawn: 2-methylcyclohexan-1-ol →(PBr₃) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_question_b3ba0357_04112026.svg?v=b3ba0357421f)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2-methylcyclohexan-1-ol `CC1CCCCC1O` ![2-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_question_s1_79eed43b_04112026.svg?v=79eed43b0c22)

- (1) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_1_s1_bbec4cde_04112026.svg?v=bbec4cde35ec); 2-methylcyclohexan-1-one `CC1CCCCC1=O` ![2-methylcyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_1_s2_7eaab55c_04112026.svg?v=7eaab55cfa65) — A =, B =
- **(2)** 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_2_s1_2d1efb40_04112026.svg?v=2d1efb40eae4); 1-methylcyclohexene `CC1=CCCCC1` ![1-methylcyclohexene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_2_s2_ba57c26b_04112026.svg?v=ba57c26b570b) — A =, B =
- (3) 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_3_s1_2d1efb40_04112026.svg?v=2d1efb40eae4); 4-methylcyclohexene `CC1CC=CCC1` ![4-methylcyclohexene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_3_s2_9c0f57d1_04112026.svg?v=9c0f57d13d75) — A =, B =
- (4) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_4_s1_bbec4cde_04112026.svg?v=bbec4cde35ec); 6-methylcyclohex-2-en-1-ol `CC1CCC=CC1O` ![6-methylcyclohex-2-en-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_option_4_s2_844b7d62_04112026.svg?v=844b7d628c94) — A =, B =

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: 2-methylcyclohexan-1-ol →(PBr₃) 1-bromo-2-methylcyclohexane (A) major; (A) → 1-methylcyclohexene (B) major](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q090_sol_1_53e62053_03112026.png?v=53e62053cf32)

*2-methylcyclohexan-1-ol →[PBr₃] 1-bromo-2-methylcyclohexane (A) major; (A) → 1-methylcyclohexene (B) major*

![drawn: 2-methylcyclohexan-1-ol →(PBr₃) 1-bromo-2-methylcyclohexane (A) major; (A) → 1-methylcyclohexene (B) major](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q090_solution_1_5c3cb65e_04112026.svg?v=5c3cb65e944a)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. $\mathrm{PBr_3}$ converts the secondary alcohol to the alkyl bromide: 2-methylcyclohexan-1-ol $\rightarrow$ 1-bromo-2-methylcyclohexane $= A$.
2. Alcoholic $\mathrm{KOH}$ with heat causes $\beta$-elimination of $\mathrm{HBr}$ from $A$.
3. By Saytzeff's rule the more substituted alkene forms, i.e. the double bond goes towards the $\mathrm{CH_3}$-bearing carbon: $B = $ 1-methylcyclohexene.
4. $A$ = 1-bromo-2-methylcyclohexane and $B$ = 1-methylcyclohexene match option $2$.

**Subtopic:** Reactions of Haloalkanes – Elimination Reactions, Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 37)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q090_8a6a226f_03112026.png?v=8a6a226f8eeb)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q090_18d00e9c_03112026.png?v=18d00e9cd12c)

---

## Q91

Chemistry · organic · Amines

Identify the major product C formed in the following reaction sequence: $\mathrm{CH_3-CH_2-CH_2-I} \xrightarrow{\mathrm{NaCN}} \mathrm{A} \xrightarrow[\text{Partial hydrolysis}]{\mathrm{OH^-}} \mathrm{B} \xrightarrow[\mathrm{Br_2}]{\mathrm{NaOH}} \underset{\text{(major)}}{\mathrm{C}}$

- (1) $\alpha$–bromobutanoic acid
- **(2)** propylamine
- (3) butylamine
- (4) butanamide

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: 1-iodopropane →(NaCN) butanenitrile (A) →(Partial hydrolysis) butanamide (B); (B) →(NaOH/$\ce{Br2}$) propan-1-amine (C) (Propyl amine)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q091_sol_1_3d9db47a_03112026.png?v=3d9db47a312d)

*1-iodopropane →[NaCN] butanenitrile (A) →[Partial hydrolysis] butanamide (B); (B) →[NaOH/$\ce{Br2}$] propan-1-amine (C) (Propyl amine)*

![drawn: 1-iodopropane →(NaCN) butanenitrile (A) →(Partial hydrolysis) butanamide (B); (B) →(NaOH/$\ce{Br2}$) propan-1-amine (C) (Propyl amine)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q091_solution_1_3963c085_04112026.svg?v=3963c0855c2a)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Step-I is $\mathrm{S_N}$ reaction with $\overset{\ominus}{\mathrm{C}}\mathrm{N}$ nucleophile.
2. Step-II will give amide.
3. Step-III is Hoffmann bromamide degradation reaction.

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2I} + \mathrm{NaCN} \rightarrow \mathrm{CH_3CH_2CH_2CN}$ (A, butanenitrile) by $S_N2$ substitution.
2. Partial hydrolysis: $\mathrm{CH_3CH_2CH_2CN} \xrightarrow{\mathrm{OH^-}} \mathrm{CH_3CH_2CH_2CONH_2}$ (B, butanamide).
3. Hofmann bromamide degradation: $\mathrm{CH_3CH_2CH_2CONH_2} + \mathrm{Br_2} + 4\mathrm{NaOH} \rightarrow \mathrm{CH_3CH_2CH_2NH_2} + \mathrm{Na_2CO_3} + 2\mathrm{NaBr} + 2\mathrm{H_2O}$.
4. C is $\mathrm{CH_3CH_2CH_2NH_2}$, propylamine, which is option $2$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 38)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q091_417f45e3_03112026.png?v=417f45e356dc)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q091_f45211e1_03112026.png?v=f45211e106c9)

---

## Q92

Chemistry · physical · Chemical Equilibrium

Consider the following reaction in a sealed vessel at equilibrium with concentrations of $\mathrm{N_2} = 3.0 \times 10^{-3}\,\mathrm{M}$, $\mathrm{O_2} = 4.2 \times 10^{-3}\,\mathrm{M}$ and $\mathrm{NO} = 2.8 \times 10^{-3}\,\mathrm{M}$. $\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$ If $0.1\,\mathrm{mol\,L^{-1}}$ of $\mathrm{NO_{(g)}}$ is taken in a closed vessel, what will be degree of dissociation ($\alpha$) of $\mathrm{NO_{(g)}}$ at equilibrium?

- **(1)** $0.717$
- (2) $0.00889$
- (3) $0.0889$
- (4) $0.8889$

**Answer** — booklet: (1) · independent solve: (1) · agree

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
10. $1.607 = \frac{(0.05)^2 \alpha^2}{0.01(1 - \alpha)^2}$
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
6. $0.5\alpha = 1.268 - 1.268\alpha \Rightarrow \alpha = \frac{1.268}{1.768} = 0.717$, which is option $1$.

**Subtopic:** Calculating Equilibrium Concentrations · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 38)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q092_73606470_03112026.png?v=736064706f51)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q092_23cbf10f_03112026.png?v=23cbf10f5a19)

---

## Q93

Chemistry · organic · Haloalkanes and Haloarenes

The products A and B obtained in the following reactions, respectively, are
$\mathrm{3ROH + PCl_3 \rightarrow 3RCl + A}$
$\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + B}$

- **(1)** $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$
- (2) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_3}$
- (3) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_4}$
- (4) $\mathrm{H_3PO_4}$ and $\mathrm{POCl_3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. These reactions are preparation of haloalkanes from alcohols.
2. $\mathrm{3ROH + PCl_3 \longrightarrow 3RCl + \underset{(A)}{H_3PO_3}}$
3. $\mathrm{ROH + PCl_5 \longrightarrow RCl + HCl + \underset{(B)}{POCl_3}}$
4. A and B are $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$ respectively.

**Solved independently** (answer withheld)

1. $\mathrm{3ROH + PCl_3 \rightarrow 3RCl + H_3PO_3}$, so $A = \mathrm{H_3PO_3}$.
2. $\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + POCl_3}$, so $B = \mathrm{POCl_3}$.
3. $A, B = \mathrm{H_3PO_3}, \mathrm{POCl_3}$, which is option $1$.

**Subtopic:** Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q093_39064100_03112026.png?v=390641005163)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q093_f19976c6_03112026.png?v=f19976c64921)

---

## Q94

Chemistry · inorganic · The D- and F-Block Elements – Practice

The pair of lanthanoid ions which are diamagnetic is

- (1) $\mathrm{Pm^{3+}}$ and $\mathrm{Sm^{3+}}$
- **(2)** $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$
- (3) $\mathrm{Ce^{3+}}$ and $\mathrm{Eu^{2+}}$
- (4) $\mathrm{Gd^{3+}}$ and $\mathrm{Eu^{3+}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Magnetic moment $\mu = \sqrt{n(n+2)}$
2. $n \rightarrow$ number of unpaired electron
3. $\mathrm{Ce^{4+}} \Rightarrow (\mathrm{Xe})\,4f^{0}$
4. $\mu = 0$ Diamagnetic

![printed figure: orbital-box diagram of seven boxes, each with a paired up-down arrow pair (fully filled f subshell)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_1_eace69c4_03112026.png?v=eace69c40c40)

*orbital-box diagram of seven boxes, each with a paired up-down arrow pair (fully filled f subshell)*

5. $\mathrm{Yb^{2+}} \Rightarrow (\mathrm{Xe})\,4f^{14}$
6. $\mu = 0$ Diamagnetic

![printed figure: orbital-box diagram of seven boxes, the first with one up arrow and the other six empty](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_2_e540438a_03112026.png?v=e540438a0e48)

*orbital-box diagram of seven boxes, the first with one up arrow and the other six empty*

7. $\mathrm{Ce^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{1}$
8. $\mu = \sqrt{3}$ Paramagnetic

![printed figure: orbital-box diagram of seven boxes, each with one up arrow](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_3_e592cec4_03112026.png?v=e592cec474d3)

*orbital-box diagram of seven boxes, each with one up arrow*

9. $\mathrm{Eu^{2+}} \Rightarrow (\mathrm{Xe})\,4f^{7}$
10. $\mu = \sqrt{63}$ Paramagnetic

![printed figure: orbital-box diagram of five boxes, each with one up arrow](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_4_8172d792_03112026.png?v=8172d7923e66)

*orbital-box diagram of five boxes, each with one up arrow*

11. $\mathrm{Gd^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{7}$
12. $\mu = \sqrt{63}$ Paramagnetic

![printed figure: orbital-box diagram of five boxes, each with one up arrow](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_5_3659ff91_03112026.png?v=3659ff919e1b)

*orbital-box diagram of five boxes, each with one up arrow*

13. $\mathrm{Eu^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{6}$
14. $\mu = \sqrt{48}$ Paramagnetic

![printed figure: orbital-box diagram of five boxes, the first four each with one up arrow and the fifth empty](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_6_1fc29e16_03112026.png?v=1fc29e162f0d)

*orbital-box diagram of five boxes, the first four each with one up arrow and the fifth empty*

15. $\mathrm{Pm^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{4}$
16. $\mu = \sqrt{24}$ Paramagnetic

![printed figure: orbital-box diagram of five boxes, each with one up arrow](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q094_sol_7_99be0b20_03112026.png?v=99be0b20fb0e)

*orbital-box diagram of five boxes, each with one up arrow*

17. $\mathrm{Sm^{3+}} \Rightarrow (\mathrm{Xe})\,4f^{5}$
18. $\mu = \sqrt{35}$ Paramagnetic
19. Hence $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$ are only diamagnetic.

**Solved independently** (answer withheld)

1. A diamagnetic ion has no unpaired electrons, so it needs a $4f^0$ or $4f^{14}$ configuration.
2. $\mathrm{Ce}$ ($Z=58$): $\mathrm{Ce^{4+}} = [\mathrm{Xe}]4f^0$, which has 0 unpaired electrons.
3. $\mathrm{Yb}$ ($Z=70$): $\mathrm{Yb^{2+}} = [\mathrm{Xe}]4f^{14}$, which has 0 unpaired electrons.
4. $\mathrm{Pm^{3+}}\,(4f^4)$, $\mathrm{Sm^{3+}}\,(4f^5)$, $\mathrm{Ce^{3+}}\,(4f^1)$, $\mathrm{Eu^{2+}}\,(4f^7)$, $\mathrm{Gd^{3+}}\,(4f^7)$ and $\mathrm{Eu^{3+}}\,(4f^6)$ all have unpaired electrons, so they are paramagnetic.
5. Only the pair $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$ is diamagnetic, which is option $2$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q094_e3c1caee_03112026.png?v=e3c1caeef2f8)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q094_8a96e39c_03112026.png?v=8a96e39c9d49)

---

## Q95

Chemistry · physical · Chemical Kinetics

The rate of a reaction quadruples when temperature changes from $27^\circ\mathrm{C}$ to $57^\circ\mathrm{C}$. Calculate the energy of activation. Given $R = 8.314\,\mathrm{J\,K^{-1}\,mol^{-1}}$, $\log 4 = 0.6021$

- (1) $3804\,\mathrm{kJ/mol}$
- **(2)** $38.04\,\mathrm{kJ/mol}$
- (3) $380.4\,\mathrm{kJ/mol}$
- (4) $3.80\,\mathrm{kJ/mol}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\log\left(\frac{k_2}{k_1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$
2. $\log\left(\frac{4}{1}\right) = \frac{E_a}{2.303R}\left(\frac{1}{300} - \frac{1}{330}\right)$
3. $E_a = \frac{(\log(4)) \times 2.303 \times 8.314 \times 300 \times 330}{30}$
4. $= 3.804 \times 10^{4}\,\mathrm{J/mol}$
5. $= 38.04\,\mathrm{kJ/mol}$

**Solved independently** (answer withheld)

1. $T_1 = 27 + 273 = 300\,\mathrm{K}$, $T_2 = 57 + 273 = 330\,\mathrm{K}$, $\frac{k_2}{k_1} = 4$.
2. $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. $0.6021 = \frac{E_a}{2.303 \times 8.314} \times \frac{30}{300 \times 330} = \frac{E_a}{2.303 \times 8.314 \times 3300}$.
4. $E_a = 0.6021 \times 2.303 \times 8.314 \times 3300 \approx 38044\,\mathrm{J\,mol^{-1}}$.
5. $E_a \approx 38.04\,\mathrm{kJ\,mol^{-1}}$, which is option $2$.

**Subtopic:** Arrhenius Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 40)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/crops/q095_3ee31610_04112026.png?v=3ee316105683)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q095_cb2f7509_03112026.png?v=cb2f7509dd3c)

---

## Q96

Chemistry · organic · Hydrocarbons

For the given reaction: [reaction scheme: see figure_bbox; reagent $\mathrm{KMnO_4/H^+}$, product 'P' (major product)] 'P' is

![printed figure: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q096_81ef4845_04112026.png?v=81ef48454fe7)

*1,2-dicyclohexylethene →[$\ce{KMnO4/H+}$] 'P' (major product)*

![drawn: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_question_677728a1_04112026.svg?v=677728a1e81a)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1,2-dicyclohexylethene `C(=CC1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethene](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_question_s1_bc3abcb5_04112026.svg?v=bc3abcb5ca8e)

- (1) 1,2-dicyclohexylethane-1,2-dione `O=C(C(=O)C1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-dione](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_option_1_s1_a3dbbe83_04112026.svg?v=a3dbbe83efdc) — ring$-\overset{\mathrm{O}}{\overset{\|}{\mathrm{C}}}-\overset{\mathrm{O}}{\overset{\|}{\mathrm{C}}}-$ring
- (2) cyclohexanecarbaldehyde `O=CC1CCCCC1` ![cyclohexanecarbaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_option_2_s1_79f04f91_04112026.svg?v=79f04f918b83) — ring$-\mathrm{CHO}$
- **(3)** cyclohexanecarboxylic acid `O=C(O)C1CCCCC1` ![cyclohexanecarboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_option_3_s1_5fc26872_04112026.svg?v=5fc268722cd9) — ring$-\mathrm{COOH}$
- (4) 1,2-dicyclohexylethane-1,2-diol `OC(C1CCCCC1)C(O)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-diol](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_option_4_s1_63689f37_04112026.svg?v=63689f374fd9) — ring$-\underset{}{\overset{\mathrm{OH}}{\overset{|}{\mathrm{CH}}}}-\overset{\mathrm{OH}}{\overset{|}{\mathrm{CH}}}-$ring

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: I. (E)-1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 2 cyclohexanecarboxylic acid (Major product)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q096_sol_1_bf34db34_03112026.png?v=bf34db34f787)

*I. (E)-1,2-dicyclohexylethene →[$\ce{KMnO4/H+}$] 2 cyclohexanecarboxylic acid (Major product)*

![drawn: I. (E)-1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 2 cyclohexanecarboxylic acid (Major product)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_drawn/q096_solution_1_cfea80c9_04112026.svg?v=cfea80c9615f)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. The substrate is $\mathrm{C_6H_{11}{-}CH{=}CH{-}C_6H_{11}}$, a symmetric 1,2-disubstituted alkene.
2. Hot acidic $\mathrm{KMnO_4}$ cleaves the $\mathrm{C{=}C}$ bond completely (oxidative cleavage), not stopping at the diol.
3. Each $\mathrm{{=}CH{-}R}$ fragment becomes $\mathrm{R{-}CHO}$, which is further oxidised under these conditions to $\mathrm{R{-}COOH}$.
4. Both halves give $\mathrm{C_6H_{11}{-}COOH}$ (cyclohexanecarboxylic acid), which is option $3$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 40)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/crops/q096_0b641f67_04112026.png?v=0b641f671e8f)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q096_c371028a_03112026.png?v=c371028a3a1a)

---

## Q97

Chemistry · inorganic · Principles Related to Practical Chemistry

During the preparation of Mohr’s salt solution (Ferrous ammonium sulphate), which of the following acid is added to prevent hydrolysis of $\mathrm{Fe^{2+}}$ ion?

- **(1)** dilute sulphuric acid
- (2) dilute hydrochloric acid
- (3) concentrated sulphuric acid
- (4) dilute nitric acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. During the preparation of Mohr’s salt, dilute sulphuric acid is added to prevent the hydrolysis of $\mathrm{Fe^{2+}}$ ion.

**Solved independently** (answer withheld)

1. Adding dilute $\mathrm{H_2SO_4}$ supplies $\mathrm{H^+}$ and the common $\mathrm{SO_4^{2-}}$ ion, suppressing $\mathrm{Fe^{2+}}$ hydrolysis without oxidising it, while $\mathrm{HNO_3}$ and concentrated $\mathrm{H_2SO_4}$ are oxidising and $\mathrm{HCl}$ adds foreign $\mathrm{Cl^-}$, so the answer is option $1$.

**Subtopic:** Titration · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 41)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q097_932cf10a_03112026.png?v=932cf10aff0b)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q097_70be23d2_03112026.png?v=70be23d20171)

---

## Q98

Chemistry · physical · Thermodynamics

The work done during reversible isothermal expansion of one mole of hydrogen gas at $25^\circ\mathrm{C}$ from pressure of $20$ atmosphere to $10$ atmosphere is (Given $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$)

- (1) $100$ calories
- (2) $0$ calorie
- **(3)** $-413.14$ calories
- (4) $413.14$ calories

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $W_{\mathrm{rev,\,iso}} = -2.303\,nRT\log\frac{P_i}{P_f}$
2. $= -2.303 \times 1 \times 2 \times 298 \times \log 2$
3. $= -2.303 \times 1 \times 2 \times 298 \times 0.3$
4. $= -413.14$ calories

**Solved independently** (answer withheld)

1. For reversible isothermal expansion of an ideal gas, $w = -2.303\,nRT\log\frac{P_1}{P_2}$.
2. $T = 25 + 273 = 298\,\mathrm{K}$, $n = 1$, $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$, $\frac{P_1}{P_2} = \frac{20}{10} = 2$.
3. $2.303 \times 1 \times 2.0 \times 298 = 1372.588$.
4. $w = -1372.588 \times \log 2 = -1372.588 \times 0.3010 = -413.14\,\mathrm{cal}$, which is option $3$.

**Subtopic:** Pressure–Volume Work for Isothermal Reversible Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q098_13b8f086_03112026.png?v=13b8f0869128)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q098_59cf31bb_03112026.png?v=59cf31bb2766)

---

## Q99

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below.

- (Statement I) $\mathrm{[Co(NH_3)_6]^{3+}}$ is a homoleptic complex whereas $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ is a heteroleptic complex.
- (Statement II) Complex $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligands but $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has more than one kind of ligands.

- (1) Statement I is false but Statement II is true
- **(2)** Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{[Co(NH_3)_6]^{3+}}$ is a homoleptic complex as only one type of ligands ($\mathrm{NH_3}$) is coordinated with $\mathrm{Co^{3+}}$ ion.
2. While $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ is a heteroleptic complex in which $\mathrm{Co^{3+}}$ ion is ligated with more than one type of ligands, i.e., $\mathrm{NH_3}$ and $\mathrm{Cl^{-}}$.

**Solved independently** (answer withheld)

1. $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligand ($\mathrm{NH_3}$), so it is homoleptic.
2. $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has two kinds of ligands ($\mathrm{NH_3}$ and $\mathrm{Cl^-}$), so it is heteroleptic; Statement I is true.
3. Statement II states exactly these ligand facts, so it is true; both true is option $2$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q099_36e8d6fd_03112026.png?v=36e8d6fddc9d)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q099_49b0f9e9_03112026.png?v=49b0f9e91909)

---

## Q100

Chemistry · physical · Electrochemistry

Mass in grams of copper deposited by passing $9.6487\,\mathrm{A}$ current through a voltmeter containing copper sulphate solution for $100$ seconds is (Given : Molar mass of $\mathrm{Cu}$ : $63\,\mathrm{g\,mol^{-1}}$, $1\,\mathrm{F} = 96487\,\mathrm{C}$)

- (1) $0.0315\,\mathrm{g}$
- (2) $3.15\,\mathrm{g}$
- **(3)** $0.315\,\mathrm{g}$
- (4) $31.5\,\mathrm{g}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{Cu^{2+}(aq) + 2e^{-} \rightarrow Cu(s)}$
2. Mass of $\mathrm{Cu}$ deposited $(w) = \frac{M \times i \times t}{nF}$
3. $= \frac{63 \times 9.6487 \times 100}{2 \times 96487}$
4. $= 0.315\,\mathrm{g}$

**Solved independently** (answer withheld)

1. $Q = It = 9.6487\,\mathrm{A} \times 100\,\mathrm{s} = 964.87\,\mathrm{C}$.
2. $\frac{964.87}{96487} = 0.01\,\mathrm{F}$.
3. $\mathrm{Cu^{2+}} + 2e^- \rightarrow \mathrm{Cu}$, so $n(\mathrm{Cu}) = \frac{0.01}{2} = 0.005\,\mathrm{mol}$.
4. $m = 0.005 \times 63 = 0.315\,\mathrm{g}$, which is option $3$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 41)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q100_abc104b9_03112026.png?v=abc104b95cb6)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q100_1a4d8da6_03112026.png?v=1a4d8da6a06d)

---

## Q101

Biology · botany · Biomolecules

Lecithin, a small molecular weight organic compound found in living tissues, is an example of:

- (1) Carbohydrates
- (2) Amino acids
- **(3)** Phospholipids
- (4) Glycerides

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3).
2. Some lipids have phosphorous and a phosphorylated organic compound in them. These are phospholipids. They are found in cell membrane. Lecithin is one example.
3. Option (4) is incorrect as glycerides are another group of lipids in which both glycerol and fatty acids are present.
4. Option (1) and (2) are incorrect as carbohydrates and amino acids are separate groups of biomolecules.

**Solved independently** (answer withheld)

1. Lecithin is a lipid carrying a phosphorylated organic compound (choline), so it is a phospholipid, which is option $3$.

**Subtopic:** Lipids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q101_f840ee1f_03112026.png?v=f840ee1f37ee)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q101_a6a47ac4_03112026.png?v=a6a47ac479bb)

---

## Q102

Biology · botany · Biodiversity and Conservation

These are regarded as major causes of biodiversity loss: Choose the correct option:

- (A) Over exploitation
- (B) Co-extinction
- (C) Mutation
- (D) Habitat loss and fragmentation
- (E) Migration

- **(1)** A, B and D only
- (2) A, C and D only
- (3) A, B, C and D only
- (4) A, B and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Major causes of biodiversity losses are
2. (1) Co-extinctions
3. (2) Habitat loss and fragmentation
4. (3) Over-exploitation
5. (4) Alien species invasions
6. Hence correct option is A, B and D only.

**Solved independently** (answer withheld)

1. NCERT lists the four major causes of biodiversity loss (the 'Evil Quartet') as habitat loss and fragmentation, over-exploitation, alien species invasions and co-extinctions, so $A$, $B$ and $D$ are causes while mutation ($C$) and migration ($E$) are not, giving option $1$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q102_e9efc430_03112026.png?v=e9efc43067d6)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q102_c320125b_03112026.png?v=c320125bfe9d)

---

## Q103

Biology · botany · Principles of Inheritance and Variation

In a plant, black seed color (BB/Bb) is dominant over white seed color (bb). In order to find out the genotype of the black seed plant, with which of the following genotype will you cross it?

- (1) BB/Bb
- (2) BB
- **(3)** bb
- (4) Bb

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. To determine the genotype of a black seed colour at $\mathrm{F_2}$, the black seed from $\mathrm{F_2}$ is crossed with the white seed colour.
2. This is called a test cross.
3. $\therefore$ To determine the genotype of (BB/Bb) black seed we need to cross them with white seed i.e. bb.

**Solved independently** (answer withheld)

1. To find the unknown genotype of a dominant-phenotype plant, perform a test cross with the homozygous recessive parent $bb$.
2. If the plant is $BB$: $BB \times bb \rightarrow$ all $Bb$ (black); if $Bb$: $Bb \times bb \rightarrow 1\,Bb : 1\,bb$ (black : white).
3. So the cross is with $bb$, which is option $3$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q103_4690dc91_03112026.png?v=4690dc9156ec)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q103_98fb37cf_03112026.png?v=98fb37cf2cbf)

---

## Q104

Biology · botany · Molecular Basis of Inheritance

A transcription unit in DNA is defined primarily by the three regions in DNA and these are with respect to upstream and down stream end;

- **(1)** Promotor, Structural gene, Terminator
- (2) Repressor, Operator gene, Structural gene
- (3) Structural gene, Transposons, Operator gene
- (4) Inducer, Repressor, Structural gene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A transcription unit of DNA is defined primarily by the three regions in the DNA:
2. (i) A promoter
3. (ii) The structural gene
4. (iii) A terminator
5. The promoter is said to be located towards $5'$-end (upstream) of the structural gene (the reference is made with respect to the polarity of coding strand)
6. The terminator is located towards $3'$-end (downstream) of the coding strand.

**Solved independently** (answer withheld)

1. A transcription unit in DNA is defined by three regions: the promoter at the upstream end, the structural gene in the middle, and the terminator at the downstream end, which matches option $1$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q104_115d36da_03112026.png?v=115d36da2dae)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q104_df0987c4_03112026.png?v=df0987c48d7d)

---

## Q105

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the set of correct statements: Choose the correct answer from the options given below.

- (A) The flowers of Vallisneria are colourful and produce nectar.
- (B) The flowers of water lily are not pollinated by water.
- (C) In most of water-pollinated species, the pollen grains are protected from wetting.
- (D) Pollen grains of some hydrophytes are long and ribbon like.
- (E) In some hydrophytes, the pollen grains are carried passively inside water.

- **(1)** B, C, D and E only
- (2) C, D and E only
- (3) A, B, C and D only
- (4) A, C, D and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Flowers of Vallisneria are not colourful and do not produce nectar.
2. Waterlily is pollinated by insect or wind.
3. In water-pollinated species, pollen grains are protected from wetting by a mucilaginous covering.
4. In some hydrophytes such as Vallisneria pollen grains are carried passively by water current.

**Solved independently** (answer withheld)

1. Statement A: water-pollinated flowers such as $Vallisneria$ are not colourful and do not produce nectar, so A is false.
2. Statement B: water lily emerges above water and is pollinated by insects or wind, not water, so B is true.
3. Statement C: in most water-pollinated species pollen grains are protected from wetting by a mucilaginous covering, so C is true.
4. Statement D: in some hydrophytes such as seagrasses, pollen grains are long and ribbon-like, so D is true.
5. Statement E: in some hydrophytes such as seagrasses, pollen grains are carried passively inside water, so E is true.
6. True set is B, C, D and E, which is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 43)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q105_708f4ec4_03112026.png?v=708f4ec4db43)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q105_4cd75f5a_03112026.png?v=4cd75f5aec28)

---

## Q106

Biology · botany · Anatomy of Flowering Plants

Bulliform cells are responsible for

- (1) Providing large spaces for storage of sugars.
- **(2)** Inward curling of leaves in monocots.
- (3) Protecting the plant from salt stress.
- (4) Increased photosynthesis in monocots.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In grasses, certain adaxial epidermal cells along the veins modify themselves into large, empty, colourless cells.
2. These are called bulliform cells.
3. When the bulliform cells in the leaves have absorbed water and are turgid, the leaf surface is exposed.
4. When they are flaccid due to water stress, they make the leaves curl inwards to minimise water loss.

**Solved independently** (answer withheld)

1. Bulliform cells are large, empty, colourless epidermal cells of monocot (grass) leaves; when they become flaccid from water loss the leaf curls inward, which is option $2$.

**Subtopic:** Dicotyledonous and Monocotyledonous Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q106_5c62a3bd_03112026.png?v=5c62a3bddb3a)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q106_e0978af0_03112026.png?v=e0978af0957a)

---

## Q107

Biology · botany · Biological Classification

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Rhizopus | I | Mushroom |
| B | Ustilago | II | Smut fungus |
| C | Puccinia | III | Bread mould |
| D | Agaricus | IV | Rust fungus |

- (1) A-IV, B-III, C-II, D-I
- **(2)** A-III, B-II, C-IV, D-I
- (3) A-I, B-III, C-II, D-IV
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

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
5. The combination A-III, B-II, C-IV, D-I is option $2$.

**Subtopic:** Basidiomycetes, Phycomycetes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q107_b9535fda_03112026.png?v=b9535fda1144)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q107_2f4314a7_03112026.png?v=2f4314a74200)

---

## Q108

Biology · botany · Cell Cycle and Cell Division

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Chromosomes become gradually visible under light microscope during leptotene stage.
- (Statement II) The beginning of diplotene stage is recognized by dissolution of synaptonemal complex.

- (1) Statement I is false but Statement II is true
- **(2)** Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. During leptotene stage the chromosomes become gradually visible under the light microscope.
2. The beginning of diplotene is recognised by the dissolution of the synaptonemal complex and the tendency of the recombined homologous chromosomes of the bivalents to separate from each other except at the site of crossover.
3. Thus both statement I and II are correct.

**Solved independently** (answer withheld)

1. Statement I: in leptotene, chromosomes become gradually visible under the light microscope, so Statement I is true.
2. Statement II: the beginning of diplotene is recognised by dissolution of the synaptonemal complex, so Statement II is true.
3. Both statements are true, which is option $2$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 44)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q108_d282f6d8_03112026.png?v=d282f6d8ac56)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q108_94ff190a_03112026.png?v=94ff190a63ee)

---

## Q109

Biology · botany · Microbes in Human Welfare

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Clostridium butylicum | I | Ethanol |
| B | Saccharomyces cerevisiae | II | Streptokinase |
| C | Trichoderma polysporum | III | Butyric acid |
| D | Streptococcus sp. | IV | Cyclosporin-A |

- (1) A-IV, B-I, C-III, D-II
- (2) A-III, B-I, C-II, D-IV
- (3) A-II, B-IV, C-III, D-I
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. Clostridium butylicum — Butyric acid
2. B. Saccharomyces cerevisiae — Ethanol
3. C. Trichoderma polysporum — Cyclosporin-A
4. D. Streptococcus sp. — Streptokinase

**Solved independently** (answer withheld)

1. $A$: Clostridium butylicum produces butyric acid $\Rightarrow A\text{-}III$; $B$: Saccharomyces cerevisiae produces ethanol $\Rightarrow B\text{-}I$.
2. $C$: Trichoderma polysporum produces cyclosporin-A $\Rightarrow C\text{-}IV$; $D$: Streptococcus produces streptokinase $\Rightarrow D\text{-}II$.
3. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ matches option $4$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q109_9ff868d6_03112026.png?v=9ff868d602e0)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q109_d9130f3a_03112026.png?v=d9130f3af055)

---

## Q110

Biology · botany · Biomolecules

The cofactor of the enzyme carboxypeptidase is:

- (1) Haem
- **(2)** Zinc
- (3) Niacin
- (4) Flavin

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as the cofactor of the enzyme carboxypeptidase is zinc.
2. Niacin is associated with coenzyme NAD and NADP.
3. Option (1) is incorrect as haem is the prosthetic group in peroxidase and catalase.

**Solved independently** (answer withheld)

1. Carboxypeptidase is a proteolytic metalloenzyme whose essential cofactor is the metal ion $\mathrm{Zn^{2+}}$, so the answer is option $2$ (Zinc).

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q110_f2afd1eb_03112026.png?v=f2afd1eb119a)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q110_55c06b9f_03112026.png?v=55c06b9f0ecb)

---

## Q111

Biology · botany · Anatomy of Flowering Plants

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Parenchyma is living but collenchyma is dead tissue.
- (Statement II) Gymnosperms lack xylem vessels but presence of xylem vessels is the characteristic of angiosperms.

- **(1)** Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Collenchyma is also living tissue.
2. Gymnosperm lack xylem vessels but presence of xylem vessels is the characteristic of angiosperm.

**Solved independently** (answer withheld)

1. Parenchyma and collenchyma are both living simple tissues (only sclerenchyma is dead), so Statement I is false.
2. Per NCERT, gymnosperms lack vessels in their xylem, and the presence of vessels is a characteristic feature of angiosperms, so Statement II is true.
3. Statement I false and Statement II true matches option $1$.

**Subtopic:** Permanent Tissue, Complex Tissue · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 45)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q111_5363cff9_03112026.png?v=5363cff9ac64)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q111_4e2559c3_03112026.png?v=4e2559c3c74d)

---

## Q112

Biology · botany · Morphology of Flowering Plants

Identify the type of flowers based on the position of calyx, corolla and androecium with respect to the ovary from the given figures (a) and (b)

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q112_51569f37_04112026.png?v=51569f37182b)

- **(1)** (a) Perigynous; (b) Perigynous
- (2) (a) Epigynous; (b) Hypogynous
- (3) (a) Hypogynous; (b) Epigynous
- (4) (a) Perigynous; (b) Epigynous

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. If gynoecium is situated in the centre and other parts of the flower are located on the rim of the thalamus almost at the same level, it is called perigynous.
2. Both diagram shows perigynous condition.

**Solved independently** (answer withheld)

1. In figure (a) the thalamus grows up as a cup around the ovary; the ovary is not fused with the cup wall.
2. The sepals, petals and stamens of (a) arise from the rim of the cup, roughly at the level of the ovary, so (a) is perigynous.
3. In figure (b) the thalamus is a shallower cup; the ovary again sits free in its centre and the other floral parts arise from its rim at about the ovary's level, so (b) is perigynous.
4. Neither figure shows parts below a superior ovary on a flat/convex thalamus (hypogynous) or parts above an ovary fused with the thalamus (epigynous), so the answer is (a) Perigynous; (b) Perigynous, option $1$.

**Subtopic:** Position of the Ovary · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 46)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q112_82e465c1_03112026.png?v=82e465c1a76a)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q112_8c6f128f_03112026.png?v=8c6f128fe7cc)

---

## Q113

Biology · botany · Organisms and Populations

The equation of Verhulst-Pearl logistic growth is $\frac{dN}{dt} = rN\left[\frac{K - N}{K}\right]$. From this equation, $K$ indicates:

- (1) Population density
- (2) Intrinsic rate of natural increase
- (3) Biotic potential
- **(4)** Carrying capacity

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In the equation $\frac{dN}{dt} = rN\left(\frac{K - N}{K}\right)$, $K$ represents carrying capacity.

**Solved independently** (answer withheld)

1. In $\frac{dN}{dt} = rN\left[\frac{K - N}{K}\right]$, $N$ is population density, $r$ is the intrinsic rate of natural increase and $K$ is the carrying capacity, which is option $4$.

**Subtopic:** Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q113_ab33d95c_03112026.png?v=ab33d95c294c)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q113_09620847_03112026.png?v=09620847bbed)

---

## Q114

Biology · botany · Photosynthesis in Higher Plants

How many molecules of ATP and NADPH are required for every molecule of $\mathrm{CO_2}$ fixed in the Calvin cycle?

- **(1)** 3 molecules of ATP and 2 molecules of NADPH
- (2) 2 molecules of ATP and 3 molecules of NADPH
- (3) 2 molecules of ATP and 2 molecules of NADPH
- (4) 3 molecules of ATP and 3 molecules of NADPH

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For fixation of $1$ molecule of $\mathrm{CO_2}$ in Calvin cycle $3$ $\mathrm{ATP}$ molecules and $2$ $\mathrm{NADPH}$ molecules are required.

**Solved independently** (answer withheld)

1. Reduction of 2 molecules of 3-PGA formed per $\mathrm{CO_2}$ uses $2\,\mathrm{ATP} + 2\,\mathrm{NADPH}$; regeneration of RuBP uses $1\,\mathrm{ATP}$, so per $\mathrm{CO_2}$ fixed: $3\,\mathrm{ATP} + 2\,\mathrm{NADPH}$, which is option $1$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 46)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q114_0c1f6a51_03112026.png?v=0c1f6a518065)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q114_1022a35a_03112026.png?v=1022a35a3249)

---

## Q115

Biology · botany · Photosynthesis in Higher Plants

Which of the following are required for the dark reaction of photosynthesis? Choose the correct answer from the options given below:

- (A) Light
- (B) Chlorophyll
- (C) $\mathrm{CO_2}$
- (D) ATP
- (E) NADPH

- (1) D and E only
- (2) A, B and C only
- (3) B, C and D only
- **(4)** C, D and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

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
5. So the required set is C, D and E only, which is option $4$.

**Subtopic:** The Calvin Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q115_31e10470_03112026.png?v=31e10470ec66)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q115_aecb2c0e_03112026.png?v=aecb2c0e313c)

---

## Q116

Biology · botany · Biotechnology: Principles and Processes

What is the fate of a piece of DNA carrying only gene of interest which is transferred into an alien organism? Choose the correct answer from the options given below:

- (A) The piece of DNA would be able to multiply itself independently in the progeny cells of the organism.
- (B) It may get integrated into the genome of the recipient.
- (C) It may multiply and be inherited along with the host DNA.
- (D) The alien piece of DNA is not an integral part of chromosome.
- (E) It shows ability to replicate.

- (1) A and E only
- (2) A and B only
- (3) D and E only
- **(4)** B and C only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because
2. The fate of a piece of DNA carrying only gene of interest which is transferred into an alien organism are:
3. (B) It may get integrated into the genome of the recipient
4. (C) It may multiply and be inherited along with the host DNA
5. $\Rightarrow$ This piece of DNA would not be able to multiply itself in the progeny cells of the organism but when gets integrated into the genome of the recipient, it may multiply and be inherited along with the host DNA.

**Solved independently** (answer withheld)

1. A piece of DNA with only the gene of interest has no origin of replication ($ori$), so it cannot replicate on its own: statements $A$ and $E$ are false.
2. Such alien DNA may get integrated into the recipient genome: statement $B$ is true.
3. Once integrated, it multiplies and is inherited along with the host DNA: statement $C$ is true, and $D$ (not an integral part of the chromosome) is false.
4. So the correct set is $B$ and $C$ only, which is option $4$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 47)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q116_74884f68_03112026.png?v=74884f680ad1)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q116_9e520a90_03112026.png?v=9e520a9051cb)

---

## Q117

Biology · botany · Plant Growth and Development

Formation of interfascicular cambium from fully developed parenchyma cells is an example for

- (1) Maturation
- (2) Differentiation
- (3) Redifferentiation
- **(4)** Dedifferentiation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The phenomenon of formation of interfascicular cambium from fully differentiated parenchyma cells is called dedifferentiation.

**Solved independently** (answer withheld)

1. Fully differentiated parenchyma cells regaining the ability to divide to form interfascicular cambium is $\text{dedifferentiation}$, which is option $4$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 47)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q117_a61b745c_03112026.png?v=a61b745c5a4e)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q117_0e417258_03112026.png?v=0e417258befb)

---

## Q118

Biology · botany · Biodiversity and Conservation

> ⚠ The question describes ex-situ conservation (threatened species taken out of their natural habitat and protected in a special setting), but no option says "ex-situ conservation". The booklet keys "Biodiversity conservation" as the umbrella term, and its own solution names ex-situ conservation "a type of biodiversity conservation". The keyed option is defensible only as the broad category; the precise answer is missing from the options. Same question as 2024_Q3 q110 and 2024_S1 q118.

The type of conservation in which the threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called

- (1) Sustainable development
- (2) in-situ conservation
- **(3)** Biodiversity conservation
- (4) Semi-conservative method

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The type of conservation in which threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called ex-situ conservation which is a type of biodiversity conservation.

**Solved independently** (answer withheld)

1. Taking threatened species out of their natural habitat and protecting them in a special setting is ex-situ conservation.
2. Option $2$ (in-situ) means protection within the natural habitat, so it is wrong; options $1$ and $4$ are unrelated terms.
3. Ex-situ is not offered, so the broad term in option $3$, Biodiversity conservation, is the best available choice.

**Subtopic:** Ex Situ Conservation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q118_4658749d_03112026.png?v=4658749d07e0)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q118_a8d9d119_03112026.png?v=a8d9d1191b23)

---

## Q119

Biology · botany · Morphology of Flowering Plants

Which of the following is an example of actinomorphic flower?

- (1) Sesbania
- **(2)** Datura
- (3) Cassia
- (4) Pisum

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Datura shows actinomorphic flower.
2. In Cassia, Pisum and Sesbania, zygomorphic flowers are seen.

**Solved independently** (answer withheld)

1. NCERT lists mustard, Datura and chilli as actinomorphic, while pea (Pisum), Sesbania (bean-type papilionaceous flowers) and Cassia are zygomorphic, so the answer is option $2$ (Datura).

**Subtopic:** The Flower · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q119_186390a3_03112026.png?v=186390a3b5b0)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q119_2c64711a_03112026.png?v=2c64711af516)

---

## Q120

Biology · botany · Strategies for Enhancement in Food Production

The capacity to generate a whole plant from any cell of the plant is called:

- (1) Somatic hybridization
- **(2)** Totipotency
- (3) Micropropagation
- (4) Differentiation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Totipotency is defined as the capacity to generate a whole plant from any cell of the plant.

**Solved independently** (answer withheld)

1. The ability of a single plant cell (explant) to give rise to a whole plant is defined as totipotency, which is option $2$.

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q120_953a66cd_03112026.png?v=953a66cd2bcc)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q120_6e9856b8_03112026.png?v=6e9856b8cabd)

---

## Q121

Biology · botany · Principles of Inheritance and Variation

Which one of the following can be explained on the basis of Mendel's Law of Dominance?
Choose the correct answer from the options given below:

- (A) Out of one pair of factors one is dominant and the other is recessive.
- (B) Alleles do not show any expression and both the characters appear as such in $\mathrm{F_2}$ generation.
- (C) Factors occur in pairs in normal diploid plants.
- (D) The discrete unit controlling a particular character is called factor.
- (E) The expression of only one of the parental characters is found in a monohybrid cross.

- (1) A, B, C, D and E
- (2) A, B and C only
- **(3)** A, C, D and E only
- (4) B, C and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

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
6. Correct set is $A, C, D$ and $E$ only, which is option $3$.

**Subtopic:** Principles of Laws of Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 48)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q121_db0a10eb_03112026.png?v=db0a10eb8d77)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q121_fa0a649b_03112026.png?v=fa0a649b03ee)

---

## Q122

Biology · botany · Cell Cycle and Cell Division

Spindle fibers attach to kinetochores of chromosomes during

- (1) Telophase
- (2) Prophase
- **(3)** Metaphase
- (4) Anaphase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Spindle fibers attach to kinetochores of chromosome in metaphase stage.

**Solved independently** (answer withheld)

1. NCERT (Cell Cycle and Cell Division) states that the complete disintegration of the nuclear envelope marks the start of metaphase, when spindle fibres attach to the kinetochores of chromosomes, so the answer is option $3$ (Metaphase).

**Subtopic:** Prophase and Metaphase · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 49)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q122_c61eec3f_03112026.png?v=c61eec3fd465)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q122_9506f1b3_03112026.png?v=9506f1b3cf9b)

---

## Q123

Biology · botany · Biomolecules

Inhibition of Succinic dehydrogenase enzyme by malonate is a classical example of:

- (1) Enzyme activation
- (2) Cofactor inhibition
- (3) Feedback inhibition
- **(4)** Competitive inhibition

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because malonate shows close structural similarity with the substrate and it competes with the substrate for the substrate binding site of the enzyme succinic dehydrogenase.
2. Option (1), (2) and (3) are incorrect as enzyme activation, co-factor inhibition are not showing structural similarity with substrate.

**Solved independently** (answer withheld)

1. Malonate closely resembles succinate in structure and binds the active site of succinic dehydrogenase in place of the substrate, which is competitive inhibition (option $4$).

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q123_5dbffc66_03112026.png?v=5dbffc6649f8)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q123_07ca80bb_03112026.png?v=07ca80bbec21)

---

## Q124

Biology · botany · Biotechnology: Principles and Processes

Hind II always cuts DNA molecules at a particular point called recognition sequence and it consists of:

- (1) $10\,\mathrm{bp}$
- (2) $8\,\mathrm{bp}$
- **(3)** $6\,\mathrm{bp}$
- (4) $4\,\mathrm{bp}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3).
2. The first restriction endonuclease – \textit{Hin}d II, whose functioning depends on a specific DNA nucleotide sequence was isolated.
3. It was found that \textit{Hin}d II always cut DNA molecules at a particular point by recognising sequence of six base pairs.
4. Option (1), (2) and (4) are incorrect because they have either more than $6$ or less than $6\,\mathrm{bp}$.

**Solved independently** (answer withheld)

1. Per NCERT, Hind II always cuts DNA at a particular point by recognising a specific sequence of $6$ base pairs, which is option $3$ ($6\,\mathrm{bp}$).

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q124_82dee98b_03112026.png?v=82dee98b12ee)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q124_a65b3986_03112026.png?v=a65b39860330)

---

## Q125

Biology · botany · Biotechnology and Its Applications

> ⚠ Statement II is false (the Bt protoxin is activated by the ALKALINE pH of the insect gut, not acidic). Statement I says Bt toxins are "coded by a gene cry IAc": several cry genes code them (cryIAc, cryIIAb, cryIAb), so read strictly it is false and gives option (3), which the blind solve chose; the booklet keys option (4), reading cry IAc as an example. Same question as 2024_Q3 q108, 2024_T3 q131, 2024_Q2 q102, 2024_Q4 q133.

> ⚠ The independent solve chose (3); the booklet prints (4).

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Bt toxins are insect group specific and coded by a gene cry IAc.
- (Statement II) Bt toxin exists as inactive protoxin in B. thuringiensis. However, after ingestion by the insect the inactive protoxin gets converted into active form due to acidic pH of the insect gut.

- (1) Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- **(4)** Statement I is true but Statement II is false

**Answer** — booklet: (4) · independent solve: (3) · differs

**Publisher's solution**

1. The correct answer is option (4) as specific Bt toxin genes were isolated from Bacillus thuringiensis and incorporated into the several crop plants such as cotton.
2. The choice of genes depends upon the crop and the targeted pest as most Bt toxins are insect-group specific.
3. The toxin is coded by a gene named cry.
4. There are a number of them, for example, the proteins encoded by the genes cry IAc and cry IIAb control the cotton bollworms, that of cry IAb controls corn borer.

**Solved independently** (answer withheld)

1. Bt toxin proteins are coded by several genes named $cry$ (e.g. $cryIAc$, $cryIIAb$ for cotton bollworms, $cryIAb$ for corn borer); they are not coded by the single gene $cryIAc$, so Statement I is false.
2. The Bt toxin exists as an inactive protoxin and is converted to the active toxin by the alkaline pH of the insect gut, not an acidic pH, so Statement II is false.
3. Both statements are false, which is option $3$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q125_6a5e802c_03112026.png?v=6a5e802c39c0)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q125_8271c626_03112026.png?v=8271c6266530)

---

## Q126

Biology · botany · Cell: The Unit of Life

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Nucleolus | I | Site of formation of glycolipid |
| B | Centriole | II | Organization like the cartwheel |
| C | Leucoplasts | III | Site for active ribosomal RNA synthesis |
| D | Golgi apparatus | IV | For storing nutrients |

- (1) A-I, B-II, C-III, D-IV
- **(2)** A-III, B-II, C-IV, D-I
- (3) A-II, B-III, C-I, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

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
5. Combination A-III, B-II, C-IV, D-I corresponds to option $2$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q126_08ec865a_03112026.png?v=08ec865aa494)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q126_f1f157c0_03112026.png?v=f1f157c04a71)

---

## Q127

Biology · botany · Principles of Inheritance and Variation

A pink flowered Snapdragon plant was crossed with a red flowered Snapdragon plant. What type of phenotype/s is/are expected in the progeny?

- (1) Red, Pink as well as white flowered plants
- (2) Only red flowered plants
- **(3)** Red flowered as well as pink flowered plants
- (4) Only pink flowered plants

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pink colour flower in snapdragon have genotype $\mathrm{Rr}$
2. Red flowered snapdragon have genotype $\mathrm{RR}$ when they both are crossed

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q127_sol_1_930f738d_03112026.svg?v=930f738db529)

3. Phenotype Red : Pink : White $\;2\quad 2\quad 0$
4. So the progeny that we get are red and pink flowered plants only

**Solved independently** (answer withheld)

1. Flower colour in snapdragon shows incomplete dominance: $RR$ = red, $Rr$ = pink, $rr$ = white.
2. Cross: $Rr \times RR$ gives gametes $R, r$ and $R$.
3. Progeny: $\frac{1}{2} RR$ (red) $+ \frac{1}{2} Rr$ (pink), which is option $3$.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q127_b37b12f5_03112026.png?v=b37b12f5b1d2)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q127_dd9cf800_03112026.png?v=dd9cf8005b9d)

---

## Q128

Biology · botany · Biodiversity and Conservation

List of endangered species was released by

- **(1)** IUCN
- (2) GEAC
- (3) WWF
- (4) FOAM

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. List of endangered species was released by – IUCN.

**Solved independently** (answer withheld)

1. The IUCN (International Union for Conservation of Nature) publishes the Red List of threatened species, so the list of endangered species is released by IUCN, option $1$.

**Subtopic:** Loss of Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q128_c4dde24e_03112026.png?v=c4dde24e36de)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q128_b0b2b33d_03112026.png?v=b0b2b33d0c1e)

---

## Q129

Biology · botany · Biodiversity and Conservation

Tropical regions show greatest level of species richness because
Choose the correct answer from the options given below.

- (A) Tropical latitudes have remained relatively undisturbed for millions of years, hence more time was available for species diversification.
- (B) Tropical environments are more seasonal.
- (C) More solar energy is available in tropics.
- (D) Constant environments promote niche specialization.
- (E) Tropical environments are constant and predictable.

- (1) A, B and D only
- **(2)** A, C, D and E only
- (3) A and B only
- (4) A, B and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Only statement B is incorrect because tropical environments unlike temperate ones, are less seasonal, relatively more constant and predictable.
2. Thus statements A, C, D and E are correct.

**Solved independently** (answer withheld)

1. A is true: tropical latitudes stayed relatively undisturbed for millions of years, giving more time for diversification.
2. B is false: tropical environments are less seasonal, not more.
3. C is true: more solar energy is available in the tropics, supporting higher productivity.
4. D is true: constant environments promote niche specialization.
5. E is true: tropical environments are relatively constant and predictable.
6. True set is $\{A, C, D, E\}$, which is option $2$.

**Subtopic:** Latitudinal Gradients · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 51)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q129_04f45bd4_03112026.png?v=04f45bd4d58c)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q129_44a0c4b4_03112026.png?v=44a0c4b4ab2c)

---

## Q130

Biology · botany · Biological Classification

Which one of the following is not a criterion for classification of fungi?

- (1) Fruiting body
- (2) Morphology of mycelium
- **(3)** Mode of nutrition
- (4) Mode of spore formation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The morphology of the mycelium, mode of spore formation and fruiting bodies form the basis for the division of the kingdom fungi into various classes.

**Solved independently** (answer withheld)

1. NCERT states fungi are divided into classes based on morphology of the mycelium, mode of spore formation and fruiting bodies, so mode of nutrition (option $3$) is not a criterion.

**Subtopic:** Kingdom Fungi · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q130_8a9f2c93_03112026.png?v=8a9f2c932be6)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q130_09be3cc7_03112026.png?v=09be3cc7167e)

---

## Q131

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the part of the seed from the given figure which is destined to form root when the seed germinates.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q131_a8edbfa6_03112026.png?v=a8edbfa670aa)

- (1) D
- (2) A
- (3) B
- **(4)** C

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Radicle is destined to form root.
2. In the given diagram ‘C’ represent radicle

**Solved independently** (answer withheld)

1. The figure is a monocot (maize-type) seed in L.S.: endosperm above, embryo axis at the lower side; the upper sheath A is the coleoptile, B is the plumule, C is the radicle inside the lower sheath D (coleorhiza), so the radicle $C$, which forms the root, is option $4$.

**Subtopic:** Embryo and Seed · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q131_af9cf404_03112026.png?v=af9cf4045118)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q131_710db32b_03112026.png?v=710db32b4b7b)

---

## Q132

Biology · botany · Molecular Basis of Inheritance

The lactose present in the growth medium of bacteria is transported to the cell by the action of

- (1) Polymerase
- (2) Beta-galactosidase
- (3) Acetylase
- **(4)** Permease

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The $y$ gene $lac$ operon codes for permease enzyme, which increase the permeability of cell to $\beta$-galactosides.
2. So, the lactose present in the growth medium of bacteria is transported into the cell by the action of permease.

**Solved independently** (answer withheld)

1. In the $lac$ operon, the $y$ gene codes for permease, which raises the cell's permeability to $\beta$-galactosides and so carries lactose into the cell; this is option $4$.

**Subtopic:** The Lac Operon · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 52)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q132_67062f24_03112026.png?v=67062f2435e9)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q132_f9eb3c24_03112026.png?v=f9eb3c2455cd)

---

## Q133

Biology · botany · Plant Growth and Development

Auxin is used by gardeners to prepare weed-free lawns. But no damage is caused to grass as auxin

- (1) can help in cell division in grasses, to produce growth.
- (2) promotes apical dominance.
- (3) promotes abscission of mature leaves only.
- **(4)** does not affect mature monocotyledonous plants.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Auxin does not affect mature monocot plants.
2. In monocots, especially grasses show limited translocation and cause rapid degradation of external auxin.

**Solved independently** (answer withheld)

1. Synthetic auxins like $2,4\text{-D}$ are selective herbicides that kill dicot weeds but do not affect mature monocotyledonous plants such as grass, which is option $4$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q133_9bd74c62_03112026.png?v=9bd74c6238e4)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q133_f3a47520_03112026.png?v=f3a4752001c6)

---

## Q134

Biology · botany · Anatomy of Flowering Plants

In the given figure, which component has thin outer walls and highly thickened inner walls?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q134_71db99a6_04112026.png?v=71db99a6a2ae)

- (1) B
- **(2)** C
- (3) D
- (4) A

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Guard cells of stomata have thin outer wall and highly thickened inner walls.

**Solved independently** (answer withheld)

1. The figure shows a stoma: $A$ = epidermal cell, $B$ = subsidiary cell, $C$ = bean-shaped guard cell, $D$ = stomatal pore.
2. As NCERT teaches, guard cells have thin outer walls and highly thickened inner walls (towards the pore), so the answer is $C$, which is option $2$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q134_835c8a15_03112026.png?v=835c8a151f57)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q134_bd48e3a1_03112026.png?v=bd48e3a13742)

---

## Q135

Biology · botany · Principles of Inheritance and Variation

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Two or more alternative forms of a gene | I | Back cross |
| B | Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent | II | Ploidy |
| C | Cross of $\mathrm{F_1}$ progeny with any of the parents | III | Allele |
| D | Number of chromosome sets in plant | IV | Test cross |

- (1) A-IV, B-III, C-II, D-I
- (2) A-I, B-II, C-III, D-IV
- (3) A-II, B-I, C-III, D-IV
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. Two or more alternative forms of gene are called alleles.
2. B. Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent is a test cross.
3. C. Cross of $\mathrm{F_1}$ progeny with any of the parents is a back cross.
4. D. Number of chromosome sets in plant is called ploidy.

**Solved independently** (answer withheld)

1. Two or more alternative forms of a gene are alleles: $A \rightarrow III$.
2. A cross of $\mathrm{F_1}$ with the homozygous recessive parent is a test cross: $B \rightarrow IV$.
3. A cross of $\mathrm{F_1}$ with any of the parents is a back cross: $C \rightarrow I$.
4. The number of chromosome sets in a plant is its ploidy: $D \rightarrow II$, so the match is A-III, B-IV, C-I, D-II, which is option $4$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q135_75224dae_03112026.png?v=75224dae9698)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q135_0e551101_03112026.png?v=0e551101da2c)

---

## Q136

Biology · botany · Morphology of Flowering Plants

Match List I with List II
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Rose | I | Twisted aestivation |
| B | Pea | II | Perigynous flower |
| C | Cotton | III | Drupe |
| D | Mango | IV | Marginal placentation |

- (1) A-II, B-III, C-IV, D-I
- **(2)** A-II, B-IV, C-I, D-III
- (3) A-I, B-II, C-III, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

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
5. $A$-II, $B$-IV, $C$-I, $D$-III matches option $2$.

**Subtopic:** The Flower, The Fruit · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q136_4e95c44a_03112026.png?v=4e95c44aa33f)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q136_06f34d13_03112026.png?v=06f34d134e29)

---

## Q137

Biology · botany · Photosynthesis in Higher Plants

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) In $\mathrm{C_3}$ plants, some $\mathrm{O_2}$ binds to RuBisCO, hence $\mathrm{CO_2}$ fixation is decreased.
- (Statement II) In $\mathrm{C_4}$ plants, mesophyll cells show very little photorespiration while bundle sheath cells do not show photorespiration.

- (1) Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- **(4)** Statement I is true but Statement II is false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In $\mathrm{C_3}$ plant, some $\mathrm{O_2}$ bind to RuBisCO, and hence $\mathrm{CO_2}$ fixation is decreased.
2. Statement II is incorrect, photorespiration does not occur in $\mathrm{C_4}$ plants as they lack RuBisCO in mesophyll.
3. Hence statement I is the only correct option.

**Solved independently** (answer withheld)

1. In $\mathrm{C_3}$ plants RuBisCO also binds $\mathrm{O_2}$ (oxygenase activity), causing photorespiration and lowering $\mathrm{CO_2}$ fixation, so Statement I is true.
2. In $\mathrm{C_4}$ plants mesophyll cells fix $\mathrm{CO_2}$ with PEP carboxylase and lack RuBisCO, so they cannot photorespire at all; the claim of 'very little photorespiration' there is wrong, so Statement II is false.
3. Statement I true, Statement II false, which is option $4$.

**Subtopic:** Photorespiration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 53)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q137_dc14824f_03112026.png?v=dc14824ff38f)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q137_ccdf996a_03112026.png?v=ccdf996a51a8)

---

## Q138

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the correct description about the given figure:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q138_a6d9a68c_03112026.png?v=a6d9a68c666e)

- (1) Compact inflorescence showing complete autogamy
- **(2)** Wind pollinated plant inflorescence showing flowers with well exposed stamens.
- (3) Water pollinated flowers showing stamens with mucilaginous covering.
- (4) Cleistogamous flowers showing autogamy.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The given diagram shows a wind pollinated plant showing compact inflorescence and well exposed stamens.
2. Stamens are exposed so complete autogamy does not occur.

**Solved independently** (answer withheld)

1. The figure shows a compact elongated inflorescence axis with numerous long filaments bearing anthers hanging freely on all sides, i.e. well-exposed stamens; this is the adaptation of wind-pollinated plants for easy dispersal of pollen by air currents, so the description is option $2$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q138_ab167cf8_03112026.png?v=ab167cf87ade)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q138_d818329f_03112026.png?v=d818329f1e24)

---

## Q139

Biology · botany · Plant Kingdom

Read the following statements and choose the set of correct statements: In the members of Phaeophyceae, Choose the correct answer from the options given below:

- (A) Asexual reproduction occurs usually by biflagellate zoospores.
- (B) Sexual reproduction is by oogamous method only.
- (C) Stored food is in the form of carbohydrates which is either mannitol or laminarin.
- (D) The major pigments found are chlorophyll a, c and carotenoids and xanthophyll.
- (E) Vegetative cells have a cellulosic wall, usually covered on the outside by gelatinous coating of algin.

- (1) A, B, C and E only
- (2) A, B, C and D only
- (3) B, C, D and E only
- **(4)** A, C, D and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In members of Phaeophyceae sexual reproduction is by oogamous, isogamous or anisogamous methods.
2. Therefore correct set of statements are A, C, D and E.

**Solved independently** (answer withheld)

1. A: asexual reproduction in brown algae is usually by pear-shaped biflagellate zoospores, so A is true.
2. B: sexual reproduction may be isogamous, anisogamous or oogamous, so 'oogamous only' makes B false.
3. C: reserve food is complex carbohydrate as laminarin or mannitol, so C is true.
4. D: pigments are chlorophyll $a$, $c$, carotenoids and xanthophylls (fucoxanthin), so D is true.
5. E: the cellulosic wall is usually covered outside by a gelatinous coating of algin, so E is true.
6. Correct set is A, C, D and E only, which is option $4$.

**Subtopic:** Phaeophyceae · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 54)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q139_0c521f26_03112026.png?v=0c521f26f86f)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q139_37368e13_03112026.png?v=37368e13de43)

---

## Q140

Biology · botany · Respiration in Plants

Identify the step in tricarboxylic acid cycle, which does not involve oxidation of substrate.

- (1) Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid
- (2) Malic acid $\rightarrow$ Oxaloacetic acid
- (3) Succinic acid $\rightarrow$ Malic acid
- **(4)** Succinyl-CoA $\rightarrow$ Succinic acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Oxidation involves the loss of electrons (often as part of hydrogen) from a molecule, leaving to an increase in its oxidation state.
2. This process is typically associated with the transfer of electrons to an electron acceptor which is reduced in the process.
3. The conversion of succinyl CoA to succinic acid does not involve oxidation of substrate.

**Solved independently** (answer withheld)

1. Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid is an oxidative decarboxylation producing $NADH + H^+$, so it is an oxidation.
2. Malic acid $\rightarrow$ Oxaloacetic acid is a dehydrogenation producing $NADH + H^+$, so it is an oxidation.
3. Succinic acid $\rightarrow$ Malic acid (via fumarate) involves the dehydrogenation producing $FADH_2$, so it is an oxidation.
4. Succinyl-CoA $\rightarrow$ Succinic acid releases CoA and forms $GTP$ (substrate-level phosphorylation) with no electron carrier reduced, so it is not an oxidation: option $4$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q140_003a2233_03112026.png?v=003a2233fccb)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q140_d6fa0e10_03112026.png?v=d6fa0e1017d6)

---

## Q141

Biology · botany · Biodiversity and Conservation

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Robert May | I | Species-Area relationship |
| B | Alexander von Humboldt | II | Long term ecosystem experiment using out door plots |
| C | Paul Ehrlich | III | Global species diversity at about 7 million |
| D | David Tilman | IV | Rivet popper hypothesis |

- (1) A-III, B-IV, C-II, D-I
- (2) A-II, B-III, C-I, D-IV
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-I, B-III, C-II, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Robert May places the global species diversity at about $7$ million.
2. Alexander von Humboldt gave species-area relationship.
3. Paul Ehrlich used an analogy “Rivet popper hypothesis” to explain the role of species in the ecosystem.
4. David Tilman performed long term ecosystem experiments using out door plots.

**Solved independently** (answer withheld)

1. Robert May estimated global species diversity at about $7$ million, so A-III.
2. Alexander von Humboldt described the species-area relationship, so B-I.
3. Paul Ehrlich proposed the rivet popper hypothesis, so C-IV.
4. David Tilman conducted long-term ecosystem experiments using outdoor plots, so D-II.
5. A-III, B-I, C-IV, D-II matches option $3$.

**Subtopic:** The Importance of Species Diversity to the Ecosystem, Species–Area Relationships · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 55)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q141_cb8eb643_03112026.png?v=cb8eb643c4cf)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q141_10ee520d_03112026.png?v=10ee520daac2)

---

## Q142

Biology · botany · Molecular Basis of Inheritance

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Frederick Griffith | I | Genetic code |
| B | Francois Jacob & Jacque Monod | II | Semi-conservative mode of DNA replication |
| C | Har Gobind Khorana | III | Transformation |
| D | Meselson & Stahl | IV | Lac operon |

- (1) A-IV, B-I, C-II, D-III
- (2) A-III, B-II, C-I, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Frederick Griffith series of experiment witness miraculous transformation in the bacteria.
2. The elucidation of Lac operon was a result of a close association between geneticist, Francois Jacob and a biochemist, Jacques Monod.
3. Meselson and Stahl gave semi-conservative mode of DNA replication.
4. Har Gobind Khorana developed chemical method to define combination of bases in genetic code.

**Solved independently** (answer withheld)

1. Griffith discovered transformation ($A \to III$), Jacob and Monod proposed the lac operon ($B \to IV$), Khorana helped decipher the genetic code ($C \to I$), and Meselson and Stahl proved semi-conservative DNA replication ($D \to II$), so the match is option $3$.

**Subtopic:** The Lac Operon, Experimental Proof that DNA is Semiconservative · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q142_a81ea497_03112026.png?v=a81ea4976bed)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q142_cb7fca02_03112026.png?v=cb7fca0240ee)

---

## Q143

Biology · botany · Strategies for Enhancement in Food Production

Which of the following are fused in somatic hybridization involving two varieties of plants?

- (1) Pollens
- (2) Callus
- (3) Somatic embryos
- **(4)** Protoplasts

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Protoplast of two varieties of plants are fused in somatic hybridization.

**Solved independently** (answer withheld)

1. In somatic hybridization, cell walls are digested away and the isolated protoplasts of two varieties are fused to give a somatic hybrid, so the answer is option $4$ (Protoplasts).

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q143_cbe52e5c_03112026.png?v=cbe52e5c3d4d)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q143_a4ae5f04_03112026.png?v=a4ae5f041df6)

---

## Q144

Biology · botany · Cell: The Unit of Life

The DNA present in chloroplast is:

- (1) Circular, single stranded
- (2) Linear, double stranded
- **(3)** Circular, double stranded
- (4) Linear, single stranded

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The DNA present in chloroplast is circular double stranded.

**Solved independently** (answer withheld)

1. Chloroplast DNA, like prokaryotic DNA, is a naked, circular, double-stranded molecule, which is option $3$.

**Subtopic:** Plastids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q144_2eb8fe06_03112026.png?v=2eb8fe06db99)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q144_7bf0a757_03112026.png?v=7bf0a75770d2)

---

## Q145

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

- (1) A-III, B-I, C-IV, D-II
- **(2)** A-IV, B-II, C-I, D-III
- (3) A-IV, B-I, C-II, D-III
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

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
5. $A$-IV, $B$-II, $C$-I, $D$-III matches option $2$.

**Subtopic:** Androecium · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 56)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q145_b12e3dae_03112026.png?v=b12e3dae0226)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q145_e47dfdcd_03112026.png?v=e47dfdcd3138)

---

## Q146

Biology · botany · Molecular Basis of Inheritance

Which of the following statement is correct regarding the process of replication in \textit{E.coli}?

- **(1)** The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ direction
- (2) The DNA dependent DNA polymerase catalyses polymerization in one direction that is $3' \rightarrow 5'$
- (3) The DNA dependent RNA polymerase catalyses polymerization in one direction, that is $5' \rightarrow 3'$
- (4) The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ as well as $3' \rightarrow 5'$ direction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In Prokaryotes, like \textit{E.coli} during replication, the DNA dependent DNA polymerase catalyse polymerization only in one direction, that is $5' \rightarrow 3'$

**Solved independently** (answer withheld)

1. DNA replication in \textit{E. coli} is catalysed by DNA-dependent DNA polymerase, which adds nucleotides only in the $5' \rightarrow 3'$ direction, so option $1$ is correct; options $2$ and $4$ give wrong directions and option $3$ names the transcription enzyme.

**Subtopic:** The Machinery and the Enzymes of Replication · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 56)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q146_548a6bc2_03112026.png?v=548a6bc2e33b)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q146_a35fcf6b_03112026.png?v=a35fcf6ba235)

---

## Q147

Biology · botany · Ecosystem

> ⚠ The question asks for the GPP of the THIRD trophic level, but primary productivity is defined for producers. Read as energy reaching level 3 with the 10% rule, 100x gives x (option 3, the blind solve's pick); the booklet keys 10x (option 4), taking NPP of level 2 as the GPP of level 3. Two audits disagree. Same question as 2024_Q3 q143, 2024_T3 q146, 2024_Q2 q141, 2024_Q4 q138.

> ⚠ The independent solve chose (3); the booklet prints (4).

In an ecosystem if the Net Primary Productivity (NPP) of first trophic level is $100x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, what would be the GPP (Gross Primary Productivity) of the third trophic level of the same ecosystem?

- (1) $\frac{100x}{3x}\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- (2) $\frac{x}{10}\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- (3) $x\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$
- **(4)** $10x\left(\mathrm{kcal\,m^{-2}}\right)\mathrm{yr^{-1}}$

**Answer** — booklet: (4) · independent solve: (3) · differs

**Publisher's solution**

1. NPP at first trophic level would be the GPP for second trophic level.
2. NPP at second trophic level would be GPP for third trophic level.
3. Therefore, $100x\,(\mathrm{kcal/m^{2}/yr})$ would be GPP at second trophic level and $100x \times 10\%\,(\mathrm{kcal/m^{2}/yr})$ i.e., $10x\,(\mathrm{kcal/m^{2}/yr})$ energy would be GPP at third trophic level.

**Solved independently** (answer withheld)

1. Apply the 10% law: only about $10\%$ of energy at one trophic level is transferred to the next.
2. Energy reaching the second trophic level $= 0.1 \times 100x = 10x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$.
3. Energy reaching the third trophic level $= 0.1 \times 10x = x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, which is option $3$.

**Subtopic:** Energy Flow, Productivity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 56)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q147_14ca76a2_03112026.png?v=14ca76a2c820)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q147_ed28b13b_03112026.png?v=ed28b13b2ed6)

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

- (1) A-III, B-IV, C-I, D-II
- **(2)** A-IV, B-I, C-II, D-III
- (3) A-I, B-II, C-III, D-IV
- (4) A-II, B-III, C-IV, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2)
2. A. GLUT-4    IV. Enables glucose transport into cells
3. B. Insulin    I. Hormone
4. C. Trypsin    II. Enzyme
5. D. Collagen    III. Intercellular ground substance

**Solved independently** (answer withheld)

1. $\text{GLUT-4}$ is a transporter that enables glucose transport into cells, so $A \to IV$.
2. Insulin is a peptide hormone, so $B \to I$.
3. Trypsin is a digestive enzyme, so $C \to II$.
4. Collagen is a protein of the intercellular ground substance, so $D \to III$.
5. $A\text{-}IV,\ B\text{-}I,\ C\text{-}II,\ D\text{-}III$ matches option $2$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q148_5bacab36_03112026.png?v=5bacab3637ea)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q148_bbdba775_03112026.png?v=bbdba7754efa)

---

## Q149

Biology · botany · Respiration in Plants

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Citric acid cycle | I | Cytoplasm |
| B | Glycolysis | II | Mitochondrial matrix |
| C | Electron transport system | III | Intermembrane space of mitochondria |
| D | Proton gradient | IV | Inner mitochondrial membrane |

- (1) A-IV, B-III, C-II, D-I
- (2) A-I, B-II, C-III, D-IV
- **(3)** A-II, B-I, C-IV, D-III
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

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
5. $A$-II, $B$-I, $C$-IV, $D$-III matches option $3$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle, Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q149_0ae8ba40_03112026.png?v=0ae8ba4021fa)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q149_fe1e5fb1_03112026.png?v=fe1e5fb1f401)

---

## Q150

Biology · botany · Plant Growth and Development

Spraying sugarcane crop with which of the following plant growth regulators, increases the length of stem, thus, increasing the yield?

- (1) Abscisic acid
- (2) Auxin
- **(3)** Gibberellin
- (4) Cytokinin

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Sugarcanes store carbohydrate as sugar in their stems.
2. Spraying sugarcane crop with gibberellins increases the length of the stem, thus increasing the yield.

**Solved independently** (answer withheld)

1. Spraying sugarcane with gibberellins elongates the stem (internodes), raising the yield, so the answer is option $3$ (Gibberellin).

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q150_99aa53f5_03112026.png?v=99aa53f569c8)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q150_3408bd4d_03112026.png?v=3408bd4df33d)

---

## Q151

Biology · zoology · Breathing and Exchange of Gases

Which of the following factors are favourable for the formation of oxyhaemoglobin in alveoli?

- (1) Low $\mathrm{pCO_2}$ and High temperature
- (2) High $\mathrm{pO_2}$ and High $\mathrm{pCO_2}$
- **(3)** High $\mathrm{pO_2}$ and Lesser $\mathrm{H^+}$ concentration
- (4) Low $\mathrm{pCO_2}$ and High $\mathrm{H^+}$ concentration

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. Conditions favourable for formation of oxyhaemoglobin in alveoli are high $\mathrm{pO_2}$, less $\mathrm{H^+}$ concentration low $\mathrm{pCO_2}$ and low temperature.
3. Option (1), (2) and (4) are not correct as they do not favour the formation of oxyhaemoglobin.

**Solved independently** (answer withheld)

1. Oxyhaemoglobin formation is favoured by high $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, lesser $\mathrm{H^+}$ concentration and lower temperature (conditions in the alveoli).
2. Option 1 has high temperature, option 2 has high $\mathrm{pCO_2}$ and option 4 has high $\mathrm{H^+}$, each of which is unfavourable.
3. Option $3$ (high $\mathrm{pO_2}$ and lesser $\mathrm{H^+}$) has both factors favourable, so the answer is option $3$.

**Subtopic:** Transport of Gases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q151_d7427350_03112026.png?v=d74273501d1d)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q151_db285aad_03112026.png?v=db285aada47b)

---

## Q152

Biology · zoology · Cell Cycle and Cell Division

Following are the stages of cell division : Choose the correct sequence of stages from the options given below :

- (A) Gap 2 phase
- (B) Cytokinesis
- (C) Synthesis phase
- (D) Karyokinesis
- (E) Gap 1 phase

- **(1)** E-C-A-D-B
- (2) C-E-D-A-B
- (3) E-B-D-A-C
- (4) B-D-E-A-C

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct sequence of stages of cell division is
2. Gap 1 phase (E) $\rightarrow$ Synthesis phase (C) $\rightarrow$ Gap 2 phase (A) $\rightarrow$ Karyokinesis (D) $\rightarrow$ Cytokinesis (B)
3. The correct sequence will be $\rightarrow \mathrm{E} \rightarrow \mathrm{C} \rightarrow \mathrm{A} \rightarrow \mathrm{D} \rightarrow \mathrm{B}$

**Solved independently** (answer withheld)

1. Interphase runs in the order $G_1 \rightarrow S \rightarrow G_2$, i.e. $E \rightarrow C \rightarrow A$.
2. The M phase follows: karyokinesis (nuclear division, $D$) comes before cytokinesis (cytoplasmic division, $B$).
3. Full sequence $E-C-A-D-B$, which is option $1$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q152_98be179c_03112026.png?v=98be179c8a01)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q152_258cd541_03112026.png?v=258cd541e10c)

---

## Q153

Biology · zoology · Structural Organisation in Animals

In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on

- (1) $11^{\mathrm{th}}$ segment
- (2) $5^{\mathrm{th}}$ segment
- **(3)** $10^{\mathrm{th}}$ segment
- (4) $8^{\mathrm{th}}$ and $9^{\mathrm{th}}$ segment

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3), because in both sexes of cockroach, $10^{\mathrm{th}}$ segment bears a pair of jointed filamentous structures called anal cerci.
2. Options (1), (2) and (4) are incorrect because $5^{\mathrm{th}}$, $8^{\mathrm{th}}$ and $9^{\mathrm{th}}$ segments do not bear such structures.
3. In adult cockroaches only $10^{\mathrm{th}}$ segments are present in abdomen.
4. $11^{\mathrm{th}}$ abdominal segment is absent.

**Solved independently** (answer withheld)

1. NCERT Class 11 (Structural Organisation in Animals) states that in both sexes the $10^{\mathrm{th}}$ segment bears a pair of jointed filamentous anal cerci, which is option $3$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 58)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q153_1d9c3abe_03112026.png?v=1d9c3abe58af)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q153_a2c68234_03112026.png?v=a2c682342110)

---

## Q154

Biology · zoology · Animal Kingdom

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pleurobrachia | I | Mollusca |
| B | Radula | II | Ctenophora |
| C | Stomochord | III | Osteichthyes |
| D | Air bladder | IV | Hemichordata |

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- **(3)** A-II, B-I, C-IV, D-III
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. A. Pleurobrachia – is a member of phylum Ctenophora.
3. B. Radula – is a rasping feeding organ present in phylum Mollusca.
4. C. Stomochord – Rudimentary structure similar to notochord found in the collar region of members of phylum Hemichordata.
5. D. Air bladder – is found in Osteichthyes which provides them buoyancy.

**Solved independently** (answer withheld)

1. Pleurobrachia is a comb jelly, so $A \rightarrow II$ (Ctenophora).
2. Radula is the file-like rasping feeding organ of molluscs, so $B \rightarrow I$ (Mollusca).
3. Stomochord is the rudimentary notochord-like structure in the proboscis of hemichordates, so $C \rightarrow IV$ (Hemichordata).
4. Air bladder regulates buoyancy in bony fishes, so $D \rightarrow III$ (Osteichthyes).
5. $A\text{-}II, B\text{-}I, C\text{-}IV, D\text{-}III$ matches option $3$.

**Subtopic:** Classification of Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q154_306c0433_03112026.png?v=306c04334e6e)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q154_e8c1fd36_03112026.png?v=e8c1fd36ec69)

---

## Q155

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Typhoid | I | Fungus |
| B | Leishmaniasis | II | Nematode |
| C | Ringworm | III | Protozoa |
| D | Filariasis | IV | Bacteria |

- (1) A-II, B-IV, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- **(3)** A-IV, B-III, C-I, D-II
- (4) A-III, B-I, C-IV, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. Typhoid – Caused by Salmonella typhimurium (Bacteria)
3. Leishmaniasis – Caused by protozoan i.e., Leishmania donovani
4. Ringworm – Caused by fungi belonging to the genera Microsporum, Trichophyton and Epidermophyton
5. Filariasis – Caused by Wuchereria bancrofti and Wuchereria malayi (Nematode)

**Solved independently** (answer withheld)

1. Typhoid is caused by the bacterium $Salmonella\ typhi$, so A-IV.
2. Leishmaniasis is caused by the protozoan $Leishmania$, so B-III.
3. Ringworm is caused by fungi ($Microsporum$, $Trichophyton$, $Epidermophyton$), so C-I.
4. Filariasis is caused by the nematodes $Wuchereria$ ($W.\ bancrofti$, $W.\ malayi$), so D-II.
5. The match A-IV, B-III, C-I, D-II is option $3$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q155_db564fb2_03112026.png?v=db564fb253a8)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q155_adb89d22_03112026.png?v=adb89d221955)

---

## Q156

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cocaine | I | Effective sedative in surgery |
| B | Heroin | II | Cannabis sativa |
| C | Morphine | III | Erythroxylum |
| D | Marijuana | IV | Papaver somniferum |

- **(1)** A-III, B-IV, C-I, D-II
- (2) A-IV, B-III, C-I, D-II
- (3) A-I, B-III, C-II, D-IV
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct option is (1) as
2. A. Cocaine – Obtained from plant Erythroxylum coca, stimulating action on CNS.
3. B. Heroin – Formed by the acetylation of morphine which is obtained from plant Papaver somniferum.
4. C. Morphine – Obtained from Papaver somniferum, is an effective sedative in surgery.
5. D. Marijuana – Obtained from Cannabis sativa, produces hallucinogenic effect and affects cardiovascular system of the body.

**Solved independently** (answer withheld)

1. Cocaine is obtained from the coca plant $Erythroxylum\ coca$, so $A \to III$.
2. Heroin (diacetylmorphine) is derived from morphine, which comes from the poppy $Papaver\ somniferum$, so $B \to IV$.
3. Morphine is a very effective sedative and painkiller used in surgery, so $C \to I$.
4. Marijuana is obtained from the inflorescences of $Cannabis\ sativa$, so $D \to II$.
5. $A\text{-}III, B\text{-}IV, C\text{-}I, D\text{-}II$ matches option $1$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q156_aec68996_03112026.png?v=aec6899645cc)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q156_c9e7b607_03112026.png?v=c9e7b6073144)

---

## Q157

Biology · zoology · Structural Organisation in Animals

> ⚠ The booklet prints answer (3), but option (3) calls muscle (c) smooth, while its own printed solution says figure (c) is cardiac muscle, found only in the heart. Option (4) is the only option whose three pairs are all correct, so (4) is the correct answer; the printed key is kept as printed. Four-file audit, 2026-11-04.

> ⚠ The independent solve chose (4); the booklet prints (3).

Three types of muscles are given as a, b and c. Identify the correct matching pair along with their location in human body:
Name of muscle/location

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q157_00e69915_04112026.png?v=00e6991536b4)

- (1) (a) Involuntary – Nose tip (b) Skeletal – Bone (c) Cardiac – Heart
- (2) (a) Smooth - Toes (b) Skeletal – Legs (c) Cardiac – Heart
- **(3)** (a) Skeletal - Triceps (b) Smooth – Stomach (c) Smooth – Heart
- (4) (a) Skeletal - Biceps (b) Involuntary – Intestine (c) Cardiac – Heart

**Answer** — booklet: (3) · independent solve: (4) · differs

**Publisher's solution**

1. The correct answer is option (3) as
2. Figure (a) represents skeletal muscle fibres which are closely attached to skeletal bones.
3. In a typical muscle such as triceps and biceps, striated muscle fibres are bundled together in a parallel fashion.
4. Figure (b) represents smooth muscle fibres which are present in the wall of internal organs such as the blood vessels, stomach and intestine.
5. Figure (c) represents cardiac muscle fibres which are exclusively present in the heart.

**Solved independently** (answer withheld)

1. Figure (a) shows long, cylindrical, unbranched, striated fibres: skeletal muscle, e.g. biceps.
2. Figure (b) shows spindle-shaped, unstriated fibres with single nuclei: smooth (involuntary) muscle, e.g. intestine wall.
3. Figure (c) shows branched, striated fibres joined to each other: cardiac muscle, found in the heart.
4. Option 1 calls (a) involuntary and (b) skeletal; option 2 calls (a) smooth; option 3 calls (c) smooth. Only option $4$ fits all three.

**Subtopic:** Muscle Tissue and Neural Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q157_51697d5f_03112026.png?v=51697d5f38c2)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q157_9305265d_03112026.png?v=9305265d05f4)

---

## Q158

Biology · zoology · Neural Control and Coordination

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pons | I | Provides additional space for Neurons, regulates posture and balance. |
| B | Hypothalamus | II | Controls respiration and gastric secretions. |
| C | Medulla | III | Connects different regions of the brain. |
| D | Cerebellum | IV | Neuro secretory cells |

- (1) A-II, B-I, C-III, D-IV
- (2) A-II, B-III, C-I, D-IV
- **(3)** A-III, B-IV, C-II, D-I
- (4) A-I, B-III, C-II, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as
2. A. Pons – Part of hindbrain, it connects different regions of the brain.
3. B. Hypothalamus – Also have neuro secretory cells which secrete hormones.
4. C. Medulla oblongata – Part of hindbrain which controls respiration and gastric secretions.
5. D. Cerebellum – Part of hindbrain with convoluted surface which provides additional space for neurons, also regulates posture and balance.

**Solved independently** (answer withheld)

1. Pons consists of fibre tracts that interconnect different regions of the brain, so $A \to III$.
2. Hypothalamus contains neurosecretory cells that secrete hypothalamic hormones, so $B \to IV$.
3. Medulla contains centres controlling respiration, cardiovascular reflexes and gastric secretions, so $C \to II$.
4. Cerebellum has a highly convoluted surface giving additional space for neurons and regulates posture and balance, so $D \to I$.
5. $A-III,\ B-IV,\ C-II,\ D-I$ matches option $3$.

**Subtopic:** Hindbrain, Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q158_692c63a3_03112026.png?v=692c63a3e003)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q158_9f845231_03112026.png?v=9f8452313bda)

---

## Q159

Biology · zoology · Biotechnology and Its Applications

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | $\alpha$ –I antitrypsin | I | Cotton bollworm |
| B | Cry IAb | II | ADA deficiency |
| C | Cry IAc | III | Emphysema |
| D | Enzyme replacement therapy | IV | Corn borer |

- (1) A-II, B-IV, C-I, D-III
- (2) A-II, B-I, C-IV, D-III
- (3) A-III, B-I, C-II, D-IV
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as
2. $\alpha$– I antitrypsin $\rightarrow$ Is used for treatment of Emphysema
3. $\textit{Cry}$ I Ab gene $\rightarrow$ Controls corn borer
4. $\textit{Cry}$ I Ac gene $\rightarrow$ Controls cotton bollworms
5. Enzyme replacement therapy $\rightarrow$ Can be used as treatment option in ADA deficiency.

**Solved independently** (answer withheld)

1. $\alpha$-1 antitrypsin (made in transgenic animals) is used to treat emphysema: A-III.
2. The protein coded by $cry\,IAb$ controls the corn borer: B-IV.
3. The proteins coded by $cry\,IAc$ and $cry\,IIAb$ control cotton bollworms: C-I.
4. Enzyme replacement therapy (giving ADA) is used for ADA deficiency: D-II.
5. A-III, B-IV, C-I, D-II matches option $4$.

**Subtopic:** Pest Resistant Plants and Bt Cotton, Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q159_3d369333_03112026.png?v=3d36933399a3)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q159_18b5c130_03112026.png?v=18b5c130d80f)

---

## Q160

Biology · zoology · Evolution

Given below are some stages of human evolution. Arrange them in correct sequence. (Past to Recent) Choose the correct sequence of human evolution from the options given below:

- (A) Homo habilis
- (B) Homo sapiens
- (C) Homo neanderthalensis
- (D) Homo erectus

- **(1)** A-D-C-B
- (2) D-A-C-B
- (3) B-A-D-C
- (4) C-B-D-A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1) because the correct sequence of stages of human evolution from past to recent is
2. Homo habilis $\rightarrow$ Homo erectus $\rightarrow$ Homo neanderthalensis $\rightarrow$ Homo sapiens

**Solved independently** (answer withheld)

1. Order the stages from past to recent as $\text{A (H. habilis)} \rightarrow \text{D (H. erectus)} \rightarrow \text{C (H. neanderthalensis)} \rightarrow \text{B (H. sapiens)}$, i.e. A-D-C-B, which is option $1$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 62)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q160_c3bd6131_03112026.png?v=c3bd6131d429)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q160_4a115072_03112026.png?v=4a115072eb1d)

---

## Q161

Biology · zoology · Human Reproduction

Which of the following is not a component of Fallopian tube?

- (1) Ampulla
- **(2)** Uterine fundus
- (3) Isthmus
- (4) Infundibulum

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) as uterine fundus is the upper, dome-shaped part of the uterus, above the opening of fallopian tubes.
2. Option (3) is incorrect as isthmus is the last and narrow part of the oviduct that links to the uterus.
3. Option (4) is incorrect as infundibulum is the part of oviduct which is closer to the ovary.
4. Option (1) is incorrect as ampulla is the wider part of the oviduct.

**Solved independently** (answer withheld)

1. The Fallopian tube (oviduct) has three parts: infundibulum (with fimbriae), ampulla and isthmus; the uterine fundus is the upper dome of the uterus, so option $2$ is not a component.

**Subtopic:** The Female Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q161_1ff81b9a_03112026.png?v=1ff81b9a48f5)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q161_37dc32ee_03112026.png?v=37dc32ee11eb)

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

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-III, B-I, C-II, D-IV
- (3) A-I, B-III, C-IV, D-II
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Correct answer is option (1) because
2. Lippes loop is a non-medicated IUD.
3. Multiload 375 is a copper releasing IUD.
4. LNG -20 is a hormone releasing IUD.
5. Progestogens are used as implants.

**Solved independently** (answer withheld)

1. Non-medicated IUD is the Lippes loop, so $A \rightarrow III$.
2. Copper releasing IUD is Multiload 375, so $B \rightarrow I$.
3. Hormone releasing IUD is LNG-20, so $C \rightarrow IV$.
4. Implants contain progestogens (alone or with estrogen), so $D \rightarrow II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ is option $1$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 62)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q162_28ecd002_03112026.png?v=28ecd002beca)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q162_141ad26e_03112026.png?v=141ad26e0db0)

---

## Q163

Biology · zoology · Reproductive Health

Which of the following is not a natural/traditional contraceptive method?

- **(1)** Vaults
- (2) Coitus interruptus
- (3) Periodic abstinence
- (4) Lactational amenorrhea

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as
2. Vault is a barrier method of contraception which is made of rubber that is inserted into the female reproductive tract to cover the cervix during the coitus.
3. Option (2) is incorrect as coitus interruptus is a natural method of contraception in which male partner withdraws his penis from the vagina just before ejaculation so as to avoid insemination.
4. Option (3) is incorrect as periodic abstinence is also a natural method of contraception in which couples avoid coitus during the fertile period.
5. Option (4) is incorrect as lactational amenorrhea is also a natural method of contraception which is based on the fact that ovulation and therefore the cycle do not occur during the period of intense lactational following parturition.

**Solved independently** (answer withheld)

1. Coitus interruptus, periodic abstinence and lactational amenorrhea are natural/traditional methods, while vaults are a barrier method, so the answer is option $1$.

**Subtopic:** Natural Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q163_16baa12a_03112026.png?v=16baa12acdee)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q163_62c369e0_03112026.png?v=62c369e01037)

---

## Q164

Biology · zoology · Animal Kingdom

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pterophyllum | I | Hag fish |
| B | Myxine | II | Saw fish |
| C | Pristis | III | Angel fish |
| D | Exocoetus | IV | Flying fish |

- (1) A-III, B-II, C-I, D-IV
- (2) A-II, B-I, C-III, D-IV
- **(3)** A-III, B-I, C-II, D-IV
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct option is option no. (3) as
2. Pterophyllum is the scientific name for Angel fish.
3. Myxine is the scientific name for Hag fish.
4. Pristis is the scientific name for Saw fish.
5. Exocoetus is the scientific name for Flying fish.

**Solved independently** (answer withheld)

1. $\text{Pterophyllum}$ is the angel fish, so $A \to III$.
2. $\text{Myxine}$ is the hag fish, so $B \to I$.
3. $\text{Pristis}$ is the saw fish, so $C \to II$.
4. $\text{Exocoetus}$ is the flying fish, so $D \to IV$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}II,\ D\text{-}IV$ matches option $3$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q164_fabba8bb_03112026.png?v=fabba8bb1701)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q164_efc45071_03112026.png?v=efc450718759)

---

## Q165

Biology · zoology · Evolution

The flippers of the Penguins and Dolphins are the example of the

- (1) Divergent evolution
- (2) Adaptive radiation
- (3) Natural selection
- **(4)** Convergent evolution

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4), because the flippers of the Penguins and Dolphins perform similar function but they are not anatomically similar structures.
2. This is example of analogous structures.
3. Option (2) is incorrect as adaptive radiation is the process of evolution of different species in a given geographical area starting from a point and literally radiating to the other areas of geography.
4. Option (3) is incorrect as natural selection is a key mechanism of evolution.
5. Option (1) is incorrect as divergent evolution results in the formation of homologous structures.

**Solved independently** (answer withheld)

1. Penguin flippers (modified bird wings) and dolphin flippers (modified mammal forelimbs) do the same job, swimming, but come from different lineages, so they are analogous structures, which show convergent evolution: option $4$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 63)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q165_8398fb69_03112026.png?v=8398fb69bdb8)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q165_dc50706e_03112026.png?v=dc50706e0152)

---

## Q166

Biology · zoology · Chemical Coordination and Integration

Which of the following is not a steroid hormone?

- **(1)** Glucagon
- (2) Cortisol
- (3) Testosterone
- (4) Progesterone

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as glucagon is a proteinaceous hormone secreted from pancreas.
2. Options (2), (3) and (4) are not correct as they are steroid in nature.

**Solved independently** (answer withheld)

1. Glucagon is a peptide (polypeptide) hormone secreted by the $\alpha$-cells of the islets of Langerhans, whereas cortisol, testosterone and progesterone are cholesterol-derived steroid hormones, so the answer is option $1$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q166_a309038f_03112026.png?v=a309038f1aeb)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q166_06afc1b9_03112026.png?v=06afc1b9ab48)

---

## Q167

Biology · zoology · Principles of Inheritance and Variation

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Down’s syndrome | I | $11^{\text{th}}$ chromosome |
| B | $\alpha$-Thalassemia | II | ‘X’ chromosome |
| C | $\beta$-Thalassemia | III | $21^{\text{st}}$ chromosome |
| D | Klinefelter’s syndrome | IV | $16^{\text{th}}$ chromosome |

- (1) A-IV, B-I, C-II, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-II, B-III, C-IV, D-I
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Down’s syndrome is due to presence of an additional copy of chromosome number $21$.
2. Klinefelter’s syndrome is caused due to presence of an additional copy of X-chromosome.
3. $\alpha$-Thalassemia is controlled by two closely linked genes on chromosome $16$ of each parent.
4. $\beta$-Thalassemia is controlled by a single gene HBB on chromosome $11$ of each parent.

**Solved independently** (answer withheld)

1. Down's syndrome is trisomy of the $21^{\text{st}}$ chromosome, so A-III.
2. $\alpha$-Thalassemia is controlled by genes HBA1 and HBA2 on the $16^{\text{th}}$ chromosome, so B-IV.
3. $\beta$-Thalassemia is controlled by the HBB gene on the $11^{\text{th}}$ chromosome, so C-I.
4. Klinefelter's syndrome (XXY) involves an extra 'X' chromosome, so D-II.
5. A-III, B-IV, C-I, D-II matches option $4$.

**Subtopic:** Chromosomal Disorders, Thalassemia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q167_1bc6b48d_03112026.png?v=1bc6b48dedda)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q167_8b9ef3ed_03112026.png?v=8b9ef3ed5ec7)

---

## Q168

Biology · zoology · Human Health and Disease

Given below are two statements: One is labelled as Assertion A and the other is labelled as Reason R: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby.
- (Reason R) Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

- (1) A is not correct but R is correct
- **(2)** Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are correct but R is NOT the correct explanation of A
- (4) A is correct but R is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2)
2. Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby as colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

**Solved independently** (answer withheld)

1. Assertion A is true: NCERT states that breast-feeding during the initial period of infant growth is recommended by doctors for bringing up a healthy baby.
2. Reason R is true: colostrum contains several antibodies (IgA) absolutely essential to develop resistance for the newborn, and this passive immunity is the reason breast-feeding is recommended, so R explains A, giving option $2$.

**Subtopic:** Active and Passive Immunity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 64)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q168_b6ad6291_03112026.png?v=b6ad6291f01c)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q168_227873b9_03112026.png?v=227873b9c495)

---

## Q169

Biology · zoology · Breathing and Exchange of Gases

Match List I with List II :

| List-I | | List-II | |
|---|---|---|---|
| A | Expiratory capacity | I | Expiratory reserve volume + Tidal volume + Inspiratory reserve volume |
| B | Functional residual capacity | II | Tidal volume + Expiratory reserve volume |
| C | Vital capacity | III | Tidal volume + Inspiratory reserve volume |
| D | Inspiratory capacity | IV | Expiratory reserve volume + Residual volume |

- (1) A-I, B-III, C-II, D-IV
- **(2)** A-II, B-IV, C-I, D-III
- (3) A-III, B-II, C-IV, D-I
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Expiratory capacity = Tidal volume + Expiratory reserve volume
2. Functional residual capacity = Expiratory reserve volume + Residual volume
3. Vital capacity = Expiratory reserve volume + Tidal volume + Inspiratory reserve volume
4. Inspiratory capacity = Tidal volume + Inspiratory reserve volume

**Solved independently** (answer withheld)

1. Expiratory capacity $EC = TV + ERV$, so A matches II.
2. Functional residual capacity $FRC = ERV + RV$, so B matches IV.
3. Vital capacity $VC = ERV + TV + IRV$, so C matches I.
4. Inspiratory capacity $IC = TV + IRV$, so D matches III.
5. A-II, B-IV, C-I, D-III is option $2$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q169_d636ca06_03112026.png?v=d636ca06dd64)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q169_72c822e9_03112026.png?v=72c822e9cdba)

---

## Q170

Biology · zoology · Cell Cycle and Cell Division

Match List I with List II : List I (Sub Phases of Prophase I) List II (Specific Characters) Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| A | Diakinesis | I | Synaptonemal complex formation |
| B | Pachytene | II | Completion of terminalisation of chiasmata |
| C | Zygotene | III | Chromosomes look like thin threads |
| D | Leptotene | IV | Appearance of recombination nodules |

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- (3) A-I, B-II, C-IV, D-III
- **(4)** A-II, B-IV, C-I, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (A) Diakinesis – Completion of terminalisation of chiasmata
2. (B) Pachytene – Appearance of recombination nodules
3. (C) Zygotene – Synaptonemal complex formation
4. (D) Leptotene – Chromosomes look like thin threads
5. A-II, B-IV, C-I, D-III

**Solved independently** (answer withheld)

1. Diakinesis (A) is marked by the completion of terminalisation of chiasmata, so $A \rightarrow II$.
2. Pachytene (B) shows the appearance of recombination nodules, the sites of crossing over, so $B \rightarrow IV$.
3. Zygotene (C) is when homologues pair and the synaptonemal complex forms, so $C \rightarrow I$.
4. Leptotene (D) is when chromosomes become visible as thin threads, so $D \rightarrow III$.
5. The match $A\text{-}II,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}III$ is option $4$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q170_d75e8a5f_03112026.png?v=d75e8a5f7019)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q170_07387040_03112026.png?v=073870409938)

---

## Q171

Biology · zoology · Chemical Coordination and Integration

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R : In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) FSH acts upon ovarian follicles in female and Leydig cells in male.
- (Reason R) Growing ovarian follicles secrete estrogen in female while interstitial cells secrete androgen in male human being.

- **(1)** A is false but R is true
- (2) Both A and R are true and R is the correct explanation of A
- (3) Both A and R are true but R is NOT the correct explanation of A
- (4) A is true but R is false

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as FSH is a gonadotropin affects ovarian follicles in females and causes their growth but in males LH affects Leydig cells leading to secretion of androgens.
2. Growing ovarian follicles secrete estrogen in females while interstitial cells secrete androgen in male human being.
3. Hence, Assertion is false and Reason is true.

**Solved independently** (answer withheld)

1. In males, FSH acts on Sertoli cells, while LH acts on Leydig cells; so Assertion A is false.
2. Growing ovarian follicles secrete estrogen and interstitial (Leydig) cells secrete androgens; so Reason R is true.
3. A false, R true, which is option $1$.

**Subtopic:** The Pituitary Gland, Gonads · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 65)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q171_d3c89eb9_03112026.png?v=d3c89eb9e0e3)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q171_60e30b76_03112026.png?v=60e30b76edd8)

---

## Q172

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) The presence or absence of hymen is not a reliable indicator of virginity.
- (Statement II) The hymen is torn during the first coitus only.

- (1) Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- **(4)** Statement I is true but Statement II is false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) because the presence or absence of hymen is not a reliable indicator of virginity because hymen can also be broken by a sudden jolt, insertion of a vaginal tampon, active participation in some sports and in some women the hymen persists even after coitus.

**Solved independently** (answer withheld)

1. Statement I: the hymen may be torn by a sudden fall or jolt, tampon insertion, or active sports such as horse riding and cycling, and in some women it persists even after coitus, so its presence or absence is not a reliable indicator of virginity; Statement I is true.
2. Statement II: because the hymen can be torn by these other causes, it is not torn during the first coitus only; Statement II is false.
3. Statement I true and Statement II false matches option $4$.

**Subtopic:** Female External Genitalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q172_aca368e8_03112026.png?v=aca368e83277)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q172_2d28b5b3_03112026.png?v=2d28b5b3d308)

---

## Q173

Biology · zoology · Locomotion and Movement

Which of the following are Autoimmune disorders? Choose the most appropriate answer from the options given below:

- (A) Myasthenia gravis
- (B) Rheumatoid arthritis
- (C) Gout
- (D) Muscular dystrophy
- (E) Systemic Lupus Erythematosus (SLE)

- (1) C, D & E only
- (2) A, B & D only
- **(3)** A, B & E only
- (4) B, C & E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option (3) as Myasthenia gravis, Rheumatoid arthritis and Systemic Lupus Erythematosus (SLE) are autoimmune disorders.
2. Muscular dystrophy is a genetic disorder which progressively affects the skeletal muscles.
3. Gout is the inflammation of joints due to deposition of uric acid crystals.
4. Option (1), (2) and (4) are not the correct answer because all of them are not autoimmune disorders.

**Solved independently** (answer withheld)

1. Myasthenia gravis (A), rheumatoid arthritis (B) and SLE (E) are autoimmune disorders; gout (C) is due to uric acid crystal deposition and muscular dystrophy (D) is a genetic degenerative disorder, so the set is A, B & E, which is option $3$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 66)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q173_f1a9f41f_03112026.png?v=f1a9f41f6dd5)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q173_84411fba_03112026.png?v=84411fbaf658)

---

## Q174

Biology · zoology · Animal Kingdom

Consider the following statements :
Choose the correct answer from the options given below :

- (A) Annelids are true coelomates
- (B) Poriferans are pseudocoelomates
- (C) Aschelminthes are acoelomates
- (D) Platyhelminthes are pseudocoelomates

- (1) D only
- (2) B only
- **(3)** A only
- (4) C only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3), because annelids are true coelomate animals.
2. Options (1), (2) and (4) are incorrect because poriferans are acoelomates, aschelminths are pseudocoelomates and platyhelminthes are acoelomates.

**Solved independently** (answer withheld)

1. Statement A: Annelids have a true coelom lined by mesoderm, so $A$ is true.
2. Statement B: Poriferans are cellular-level animals with no coelom, not pseudocoelomates, so $B$ is false.
3. Statement C: Aschelminthes have a pseudocoelom, not an acoelomate body, so $C$ is false.
4. Statement D: Platyhelminthes are acoelomates, not pseudocoelomates, so $D$ is false.
5. Only $A$ is correct, which is option $3$ (A only).

**Subtopic:** Basis of Classification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q174_c9647e06_03112026.png?v=c9647e0648ca)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q174_27f7b082_03112026.png?v=27f7b08273d4)

---

## Q175

Biology · zoology · Molecular Basis of Inheritance

Which one is the correct product of DNA dependent RNA polymerase to the given template? 3’TACATGGCAAATATCCATTCA5’

- (1) 5’ATGTACCGTTTATAGGTAAGT3’
- **(2)** 5’AUGUACCGUUUAUAGGUAAGU3’
- (3) 5’AUGUAAAGUUUAUAGGUAAGU3’
- (4) 5’AUGUACCGUUUAUAGGGAAGU3’

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Template DNA is :
2. 3’TACATGGCAAATATCCATTCA5’
3. 5’AUGUACCGUUUAUAGGUAAGU3’ m-RNA

**Solved independently** (answer withheld)

1. DNA-dependent RNA polymerase synthesises RNA complementary and antiparallel to the template strand, reading $3'\to5'$ and building $5'\to3'$, using U instead of T.
2. Complementing $3'$-TACATGGCAAATATCCATTCA-$5'$ base by base gives $5'$-AUGUACCGUUUAUAGGUAAGU-$3'$.
3. Option 1 contains T (DNA), option 3 has AAAG in place of CCG, option 4 has GGG in place of GGU; only option $2$ matches exactly.

**Subtopic:** Transcription · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 67)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q175_996abde9_03112026.png?v=996abde924fe)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q175_52e7c9cf_03112026.png?v=52e7c9cf9abe)

---

## Q176

Biology · zoology · Evolution

Which one of the following factors will not affect the Hardy-Weinberg equilibrium?

- **(1)** Constant gene pool
- (2) Genetic recombination
- (3) Genetic drift
- (4) Gene migration

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option (1) as a constant gene pool will not disturb the Hardy-Weinberg equilibrium.
2. Option (3), (4) & (5) will affect the equilibrium leading to evolution.

**Solved independently** (answer withheld)

1. NCERT lists five factors affecting Hardy-Weinberg equilibrium: gene migration (gene flow), genetic drift, mutation, genetic recombination and natural selection; a constant gene pool is the equilibrium state itself, so option $1$ does not affect it.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q176_debe3778_03112026.png?v=debe377882fc)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q176_5b223d42_03112026.png?v=5b223d42d2b6)

---

## Q177

Biology · zoology · Biotechnology: Principles and Processes

The “Ti plasmid” of Agrobacterium tumefaciens stands for

- (1) Temperature independent plasmid
- (2) Tumour inhibiting plasmid
- (3) Tumor independent plasmid
- **(4)** Tumor inducing plasmid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as Ti plasmid of Agrobacterium tumefaciens is tumor inducing plasmid, containing T-DNA which causes tumor in several dicot plants.
2. Options (1), (2) and (3) are not correct.

**Solved independently** (answer withheld)

1. The Ti plasmid of $Agrobacterium\ tumefaciens$ causes tumours (crown gall) in dicot plants, so Ti = Tumor inducing, which is option $4$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q177_dbdb9afa_03112026.png?v=dbdb9afa9642)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q177_03600cd2_03112026.png?v=03600cd2049f)

---

## Q178

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements : In the light of the above statements, choose the correct answer from the option given below :

- (Statement I) In the nephron, the descending limb of loop of Henle is impermeable to water and permeable to electrolytes.
- (Statement II) The proximal convoluted tubule is lined by simple columnar brush border epithelium and increases the surface area for reabsorption.

- (1) Statement I is false but Statement II is true
- (2) Both Statement I and Statement II are true
- **(3)** Both Statement I and Statement II are false
- (4) Statement I is true but Statement II is false

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3) because
2. Statement I is false as the descending limb of loop of Henle is permeable to water and almost impermeable to electrolytes.
3. Statement II is false as proximal convoluted tubule is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption.

**Solved independently** (answer withheld)

1. Statement I: NCERT states the descending limb of loop of Henle is permeable to water but almost impermeable to electrolytes, so Statement I (impermeable to water, permeable to electrolytes) is false.
2. Statement II: NCERT states the PCT is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption; the statement says simple columnar, so Statement II is false.
3. Both statements are false, which is option $3$.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 67)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q178_88a22a0e_03112026.png?v=88a22a0ec4db)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q178_85b828f7_03112026.png?v=85b828f720e9)

---

## Q179

Biology · zoology · Biomolecules

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Lipase | I | Peptide bond |
| B | Nuclease | II | Ester bond |
| C | Protease | III | Glycosidic bond |
| D | Amylase | IV | Phosphodiester bond |

- (1) A-IV, B-I, C-III, D-II
- (2) A-IV, B-II, C-III, D-I
- (3) A-III, B-II, C-I, D-IV
- **(4)** A-II, B-IV, C-I, D-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as
2. A. Lipase – Digests ester bond found in lipids.
3. B. Nuclease – Helps in digestion of phosphodiester bonds found in nucleic acids.
4. C. Protease – Helps in digestion of peptide bond found in proteins.
5. D. Amylase – Digests/breaks the glycosidic bonds found in carbohydrates i.e., digest starch into smaller molecules, ultimately yielding maltose, which in turn is cleaved into two glucose molecules by maltase.

**Solved independently** (answer withheld)

1. Lipase hydrolyses lipids by breaking the $\text{ester bond}$, so $A \to II$.
2. Nuclease hydrolyses nucleic acids by breaking the $\text{phosphodiester bond}$, so $B \to IV$.
3. Protease hydrolyses proteins by breaking the $\text{peptide bond}$, so $C \to I$.
4. Amylase hydrolyses starch by breaking the $\text{glycosidic bond}$, so $D \to III$.
5. $A\text{-}II,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}III$ matches option $4$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q179_6361f7c7_03112026.png?v=6361f7c70527)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q179_efada8eb_03112026.png?v=efada8ebc57e)

---

## Q180

Biology · zoology · Locomotion and Movement

Match List I with List II : Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Fibrous joints | I | Adjacent vertebrae, limited movement |
| B | Cartilaginous joints | II | Humerus and Pectoral girdle, rotational movement |
| C | Hinge joints | III | Skull, don’t allow any movement |
| D | Ball and socket joints | IV | Knee, help in locomotion |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-IV, B-II, C-III, D-I
- (3) A-I, B-III, C-II, D-IV
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1) as
2. Fibrous joints do not allow any movement. This type of joint is shown by the flat skull bones which fuse end-to-end with the help of dense fibrous connective tissues in the form of sutures.
3. Cartilaginous joint is present between the adjacent vertebrae in the vertebral column and this permits limited movements.
4. Hinge joint is a type of synovial joint present in knee, help in locomotion
5. Ball and socket joint is also a type of synovial joint present between humerus and pectoral girdle and allows rotational movement.

**Solved independently** (answer withheld)

1. Fibrous joints (A) join the flat skull bones as sutures and allow no movement, so $A \to III$.
2. Cartilaginous joints (B) join adjacent vertebrae and allow limited movement, so $B \to I$.
3. Hinge joints (C) occur at the knee and help in locomotion, so $C \to IV$.
4. Ball and socket joints (D) occur between the humerus and pectoral girdle and allow rotational movement, so $D \to II$.
5. $A-III, B-I, C-IV, D-II$ is option $1$.

**Subtopic:** Joints · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q180_6067f511_03112026.png?v=6067f5116323)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q180_e35c1aba_03112026.png?v=e35c1aba405a)

---

## Q181

Biology · zoology · Body Fluids and Circulation

Following are the stages of pathway for conduction of an action potential through the heart
Choose the correct sequence of pathway from the options given below

- (A) AV bundle
- (B) Purkinje fibres
- (C) AV node
- (D) Bundle branches
- (E) SA node

- (1) E-A-D-B-C
- **(2)** E-C-A-D-B
- (3) A-E-C-B-D
- (4) B-D-E-C-A

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct answer is option (2) because the correct pathway of conduction of action potential is
2. SA $\rightarrow$ AV node $\rightarrow$ AV bundle $\rightarrow$ Bundle branches $\rightarrow$ Purkinje fibres

**Solved independently** (answer withheld)

1. The action potential originates at the SA node ($E$), passes to the AV node ($C$), then the AV bundle ($A$), the bundle branches ($D$) and the Purkinje fibres ($B$), giving $E\text{-}C\text{-}A\text{-}D\text{-}B$, which is option $2$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q181_53f1ddc5_03112026.png?v=53f1ddc5fb25)

Publisher's solution, as printed:

![printed solution 181](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q181_8aba91fb_03112026.png?v=8aba91fb1651)

---

## Q182

Biology · zoology · Biotechnology: Principles and Processes

Which of the following statements is incorrect?

- (1) Bio-reactors have an agitator system, an oxygen delivery system and foam control system
- (2) A bio-reactor provides optimal growth conditions for achieving the desired product
- (3) Most commonly used bio-reactors are of stirring type
- **(4)** Bio-reactors are used to produce small scale bacterial cultures

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4)
2. The statement (4) is incorrect because bioreactors are used for processing of large volumes ($100 - 1000$ litres) of culture.
3. Small volume cultures cannot yield appreciable quantities of products.
4. To produce in large quantities the development of bioreactors is required.

**Solved independently** (answer withheld)

1. Bioreactors are large vessels (about $100$ to $1000$ litres) in which raw materials are biologically converted to products, so they are used for large-scale, not small-scale, cultures; statement $4$ is incorrect while statements $1$, $2$ and $3$ are correct, giving option $4$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q182_a72f12cd_03112026.png?v=a72f12cd8578)

Publisher's solution, as printed:

![printed solution 182](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q182_87432c90_03112026.png?v=87432c90c52a)

---

## Q183

Biology · zoology · Biotechnology: Principles and Processes

The following diagram showing restriction sites in E. coli cloning vector pBR322. Find the role of ‘X’ and ‘Y’ genes :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2024/2024_S1/figures_agent/q183_6cc2e17c_04112026.png?v=6cc2e17cf4f6)

- (1) Gene ’X’ is responsible for recognitions sites and ‘Y’ is responsible for antibiotic resistance.
- (2) The gene ‘X’  is responsible for resistance to antibiotics and ‘Y’ for protein involved in the replication of Plasmid.
- **(3)** The gene ‘X’ is responsible for controlling the copy number of the linked DNA and ‘Y’ for protein involved in the replication of Plasmid.
- (4) The gene ‘X’ is for protein involved in replication of Plasmid and ‘Y’ for resistance to antibiotics.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Correct answer is option (3), because
2. ‘X’ in the given diagram is ori while ‘Y’ is rop.
3. ‘X’ which is ori is responsible for controlling the copy number of the linked DNA and ‘Y’ which is rop codes for protein involved in the replication of plasmid.
4. Options (1), (2) and (4) are incorrect as ‘X’ and ‘Y’ are not related to these functions.

**Solved independently** (answer withheld)

1. In pBR322, $amp^R$ carries the PstI and PvuI sites and $tet^R$ carries the BamHI and SalI sites, so neither X nor Y is an antibiotic-resistance gene.
2. X is at the bottom-left of the map, where $ori$ sits; $ori$ controls the copy number of the linked DNA.
3. Y is next to the PvuII site, where $rop$ sits; $rop$ codes for proteins involved in plasmid replication.
4. So X = $ori$ and Y = $rop$, which is option $3$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 69)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q183_9e256fab_03112026.png?v=9e256fabb288)

Publisher's solution, as printed:

![printed solution 183](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q183_d492b8ce_03112026.png?v=d492b8ce3297)

---

## Q184

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Common cold | I | Plasmodium |
| B | Haemozoin | II | Typhoid |
| C | Widal test | III | Rhinoviruses |
| D | Allergy | IV | Dust mites |

- (1) A-IV, B-II, C-III, D-I
- (2) A-II, B-IV, C-III, D-I
- (3) A-I, B-III, C-II, D-IV
- **(4)** A-III, B-I, C-II, D-IV

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct answer is option (4) because
2. Common cold is caused by Rhinoviruses
3. Haemozoin is released in blood due to ruptured RBCs after Plasmodium infection.
4. Widal test is used to confirm the typhoid fever.
5. Allergy is caused due to dust mites.

**Solved independently** (answer withheld)

1. Common cold is caused by Rhinoviruses, so $A \to III$.
2. Haemozoin is the toxin released by Plasmodium, so $B \to I$.
3. Widal test confirms typhoid, so $C \to II$.
4. Dust mites are a common allergen, so $D \to IV$.
5. $A\text{-}III, B\text{-}I, C\text{-}II, D\text{-}IV$ is option $4$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q184_7ec1f3a2_03112026.png?v=7ec1f3a2d03b)

Publisher's solution, as printed:

![printed solution 184](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q184_0582b8c7_03112026.png?v=0582b8c74b50)

---

## Q185

Biology · zoology · Cell: The Unit of Life

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Axoneme | I | Centriole |
| B | Cartwheel pattern | II | Cilia and flagella |
| C | Crista | III | Chromosome |
| D | Satellite | IV | Mitochondria |

- **(1)** A-II, B-I, C-IV, D-III
- (2) A-IV, B-III, C-II, D-I
- (3) A-IV, B-II, C-III, D-I
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

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
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ is option $1$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q185_a19c1438_03112026.png?v=a19c1438f2b2)

Publisher's solution, as printed:

![printed solution 185](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q185_0b5553c8_03112026.png?v=0b5553c8baa3)

---

## Q186

Biology · zoology · Animal Kingdom

The following are the statements about non-chordates: Choose the most appropriate answer from the options given below:

- (A) Pharynx is perforated by gill slits.
- (B) Notochord is absent.
- (C) Central nervous system is dorsal.
- (D) Heart is dorsal if present.
- (E) Post anal tail is absent.

- (1) B, C & D only
- (2) A & C only
- (3) A, B & D only
- **(4)** B, D & E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) as the features of non-chordates among the given statements are:
2. B. Notochord is absent.
3. D. Heart is dorsal if present.
4. E. Post anal tail is absent.
5. Statements A and C are features of chordates.
6. Hence, option (4) is correct and options (1), (2) and (3) are incorrect.

**Solved independently** (answer withheld)

1. A: pharyngeal gill slits are absent in non-chordates, so A is false.
2. B: notochord is absent in non-chordates, so B is true.
3. C: the central nervous system of non-chordates is ventral, solid and double, so C is false.
4. D: the heart of non-chordates, if present, is dorsal, so D is true.
5. E: a post-anal tail is absent in non-chordates, so E is true.
6. True statements are $B$, $D$ and $E$, which is option $4$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 70)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q186_b1f52b91_03112026.png?v=b1f52b91d4dc)

Publisher's solution, as printed:

![printed solution 186](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q186_8a56eafa_03112026.png?v=8a56eafa1081)

---

## Q187

Biology · zoology · Principles of Inheritance and Variation

As per ABO blood grouping system, the blood group of father is $\mathrm{B^{+}}$, mother is $\mathrm{A^{+}}$ and child is $\mathrm{O^{+}}$. Their respective genotype can be
Choose the most appropriate answer from the options given below :

- (A) $\mathrm{I^{B}i/I^{A}i/ii}$
- (B) $\mathrm{I^{B}I^{B}/I^{A}I^{A}/ii}$
- (C) $\mathrm{I^{A}I^{B}/iI^{A}/I^{B}i}$
- (D) $\mathrm{I^{A}i/I^{B}i/I^{A}i}$
- (E) $\mathrm{iI^{B}/iI^{A}/I^{A}I^{B}}$

- (1) D & E only
- **(2)** A only
- (3) B only
- (4) C & B only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Genotype of father with blood group $\mathrm{B^{+}}$ = $\mathrm{I^{B}i/iI^{B}}$
2. Genotype of mother with blood group $\mathrm{A^{+}}$ = $\mathrm{I^{A}i/iI^{A}}$
3. Genotype of child with blood group $\mathrm{O^{+}}$ = $\mathrm{ii}$
4. Hence only ‘A’ is correct.

**Solved independently** (answer withheld)

1. Blood group O is only possible with genotype $ii$, so the child is $ii$ and got one $i$ allele from each parent.
2. So the father (group B) must be $I^{B}i$ and the mother (group A) must be $I^{A}i$.
3. Statement A ($I^{B}i/I^{A}i/ii$) matches. B fails because homozygous parents cannot have an $ii$ child, and C, D and E give the wrong phenotypes.
4. Only A is correct, which is option $2$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 71)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q187_272b06ca_03112026.png?v=272b06ca5ab6)

Publisher's solution, as printed:

![printed solution 187](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q187_62757928_03112026.png?v=62757928ffaf)

---

## Q188

Biology · zoology · Evolution

Match List I with List II:
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Mesozoic Era | I | Lower invertebrates |
| B | Proterozoic Era | II | Fish & Amphibia |
| C | Cenozoic Era | III | Birds & Reptiles |
| D | Paleozoic Era | IV | Mammals |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-II, B-I, C-III, D-IV
- (3) A-III, B-I, C-II, D-IV
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correct answer is option no. (1)
2. (A) Mesozoic Era – (III) Birds & Reptiles
3. (B) Proterozoic Era – (I) Lower invertebrates
4. (C) Cenozoic Era – (IV) Mammals
5. (D) Paleozoic Era – (II) Fish & Amphibia

**Solved independently** (answer withheld)

1. Mesozoic Era (A) is the age of reptiles, with birds arising in it: $A \to III$.
2. Proterozoic Era (B) holds only lower invertebrates: $B \to I$.
3. Cenozoic Era (C) is the age of mammals: $C \to IV$.
4. Paleozoic Era (D) sees fishes and amphibians: $D \to II$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}II$ is option $1$.

**Subtopic:** Brief Account of Evolution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 71)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q188_50f2bce4_03112026.png?v=50f2bce4ca9d)

Publisher's solution, as printed:

![printed solution 188](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q188_44c177e4_03112026.png?v=44c177e42614)

---

## Q189

Biology · zoology · Body Fluids and Circulation

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | P wave | I | Heart muscles are electrically silent. |
| B | QRS complex | II | Depolarisation of ventricles. |
| C | T wave | III | Depolarisation of atria. |
| D | T-P gap | IV | Repolarisation of ventricles. |

- (1) A-IV, B-II, C-I, D-III
- (2) A-I, B-III, C-IV, D-II
- **(3)** A-III, B-II, C-IV, D-I
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The correct answer is option no. (3) as
2. A. P wave - III. Depolarisation of atria.
3. B. QRS complex - II. Depolarisation of ventricles.
4. C. T wave - IV. Repolarisation of ventricles.
5. D. T-P gap - I. Heart muscles are electrically silent.

**Solved independently** (answer withheld)

1. P wave $\rightarrow$ depolarisation of atria (III); QRS complex $\rightarrow$ depolarisation of ventricles (II); T wave $\rightarrow$ repolarisation of ventricles (IV); T-P gap $\rightarrow$ heart muscles electrically silent (I); so A-III, B-II, C-IV, D-I, which is option $3$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q189_0e461514_03112026.png?v=0e461514f4e3)

Publisher's solution, as printed:

![printed solution 189](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q189_24a1fe25_03112026.png?v=24a1fe251d13)

---

## Q190

Biology · zoology · Chemical Coordination and Integration

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Exophthalmic goiter | I | Excess secretion of cortisol, moon face & hypergylcemia. |
| B | Acromegaly | II | Hypo-secretion of thyroid hormone and stunted growth. |
| C | Cushing’s syndrome | III | Hyper secretion of thyroid hormone & protruding eye balls. |
| D | Cretinism | IV | Excessive secretion of growth hormone. |

- **(1)** A-III, B-IV, C-I, D-II
- (2) A-I, B-III, C-II, D-IV
- (3) A-IV, B-II, C-I, D-III
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

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
5. $A\text{-}III, B\text{-}IV, C\text{-}I, D\text{-}II$ matches option $1$.

**Subtopic:** Endocrine Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 72)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q190_9803d8da_03112026.png?v=9803d8da10f2)

Publisher's solution, as printed:

![printed solution 190](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q190_9c793de0_03112026.png?v=9c793de08da9)

---

## Q191

Biology · zoology · Cell: The Unit of Life

> ⚠ The booklet prints "choose the mis appropriate answer" (read: most appropriate) and "as compared chloroplast" (read: as compared to chloroplast). The wording is kept as printed. Four-file audit, 2026-11-04.

> ⚠ The independent solve chose (2); the booklet prints (4).

Given below are two statements:
In the light of the above statements, choose the mis appropriate answer from the options given below:

- (Statement I) Mitochondria and chloroplasts both double membranes bound organelles.
- (Statement II) Inner membrane of mitochondria is relatively less permeable, as compared chloroplast.

- (1) Statement I is incorrect but Statement II is correct.
- (2) Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- **(4)** Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (4) · independent solve: (2) · differs

**Publisher's solution**

1. Both mitochondria and chloroplasts are double membrane bound cell organelles.
2. Transport of ions occurs across the inner membrane of mitochondria.
3. The inner membrane of chloroplast is impermeable to ions and metabolites.
4. Therefore, it is said that inner membrane of mitochondria is relatively more permeable to that of chloroplast.

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts each have an outer and an inner membrane, so Statement I is correct.
2. The inner mitochondrial membrane is highly selective (most solutes need specific carriers), so it is relatively less permeable; Statement II is taken as correct.
3. Both statements correct $\Rightarrow$ option $2$.

**Subtopic:** Mitochondria, Plastids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 72)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q191_b0816416_03112026.png?v=b0816416f11b)

Publisher's solution, as printed:

![printed solution 191](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q191_ba93802d_03112026.png?v=ba93802d623c)

---

## Q192

Biology · zoology · Biomolecules

Regarding catalytic cycle of an enzyme action, select the correct sequential steps : Choose the correct answer from the options given below :

- (A) Substrate enzyme complex formation.
- (B) Free enzyme ready to bind with another substrate.
- (C) Release of products.
- (D) Chemical bonds of the substrate broken.
- (E) Substrate binding to active site.

- (1) E, D, C, B, A
- **(2)** E, A, D, C, B
- (3) A, E, B, D, C
- (4) B, A, C, D, E

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option (2) which is E, A, D, C, B.
2. The catalytic cycle of an enzyme action can be described in the following steps.
3. (1) The enzyme releases the products of the reaction and the free enzyme is ready to bind to another molecule of the substrate and run through the catalytic cycle once again.
4. (2) First, the substrate binds to the active site of the enzyme, fitting into the active site.
5. (3) The binding of the substrate induces the enzyme to alter its shape, fitting more tightly around the substrate.
6. (4) The active site of the enzyme, now in close proximity of the substrate breaks the chemical bonds of the substrate and the new enzyme-product complex is formed.
7. Options (1), (3) and (4) are incorrect as the steps mentioned are in the wrong sequence.

**Solved independently** (answer withheld)

1. The substrate first binds to the active site of the enzyme: step $E$.
2. Binding forms the enzyme-substrate complex: step $A$.
3. Within the complex the chemical bonds of the substrate are broken: step $D$.
4. The products are released from the active site: step $C$.
5. The free enzyme is then ready to bind another substrate: step $B$.
6. The sequence $E \rightarrow A \rightarrow D \rightarrow C \rightarrow B$ is option $2$.

**Subtopic:** Enzymes and Chemical Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q192_11617084_03112026.png?v=11617084ac61)

Publisher's solution, as printed:

![printed solution 192](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q192_2391074c_03112026.png?v=2391074cb095)

---

## Q193

Biology · zoology · Structural Organisation in Animals

Match List I with List II: Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Unicellular glandular epithelium | I | Salivary glands |
| B | Compound epithelium | II | Pancreas |
| C | Multicellular glandular epithelium | III | Goblet cells of alimentary canal |
| D | Endocrine glandular epithelium | IV | Moist surface of buccal cavity |

- (1) A-II, B-I, C-IV, D-III
- (2) A-II, B-I, C-III, D-IV
- (3) A-IV, B-III, C-I, D-II
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no. (4) as
2. A. Unicellular glandular epithelium — (III) Goblet cells of alimentary canal
3. B. Compound epithelium — (IV) Lines moist surface of buccal cavity
4. C. Multicellular glandular epithelium — (I) Salivary glands
5. D. Endocrine glandular epithelium — (II) Pancreas

**Solved independently** (answer withheld)

1. Unicellular glandular epithelium consists of isolated cells such as the goblet cells of the alimentary canal: $A \rightarrow III$.
2. Compound epithelium covers the moist surface of the buccal cavity: $B \rightarrow IV$.
3. Multicellular glandular epithelium forms clusters of cells, as in the salivary glands: $C \rightarrow I$.
4. Among the remaining choices the pancreas has endocrine function (islets of Langerhans): $D \rightarrow II$.
5. $A\text{-}III,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}II$ matches option $4$.

**Subtopic:** Animal Tissues: Epithelial Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q193_2bae1cfd_03112026.png?v=2bae1cfd4a6c)

Publisher's solution, as printed:

![printed solution 193](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q193_8e5aeb48_03112026.png?v=8e5aeb481237)

---

## Q194

Biology · zoology · Excretory Products and Their Elimination

Choose the correct statement given below regarding juxta medullary nephron.

- (1) Juxta medullary nephrons outnumber the cortical nephrons.
- (2) Juxta medullary nephrons are located in the columns of Bertini.
- (3) Renal corpuscle of juxta medullary nephron lies in the outer portion of the renal medulla.
- **(4)** Loop of Henle of juxta medullary nephron runs deep into medulla.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option no, (4) because the length of loop of Henle of juxta medullary nephron is longer than the length of loop of Henle of cortical nephron and runs deep into medulla.
2. Option (1) is incorrect as juxta medullary nephrons are lesser in number than cortical nephrons.
3. Option (2) is incorrect as juxta medullary nephron are not present in columns of Bertini.
4. Option (3) is incorrect because renal corpuscle of juxta medullary nephron lies in inner cortical region.

**Solved independently** (answer withheld)

1. Cortical nephrons outnumber juxtamedullary ones, their corpuscles lie in the inner cortex rather than the medulla or the columns of Bertini, and their long loops of Henle run deep into the medulla, so option $4$ is correct.

**Subtopic:** Human Excretory System · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 74)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q194_01912867_03112026.png?v=019128675129)

Publisher's solution, as printed:

![printed solution 194](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q194_3aad0df6_03112026.png?v=3aad0df68b44)

---

## Q195

Biology · zoology · Human Health and Disease

Given below are two statements :
In the light of above statements, choose the most appropriate answer from the options given below :

- (Statement I) Bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
- (Statement II) Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes.

- (1) Statement I is incorrect but Statement II is correct.
- **(2)** Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- (4) Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2) as both statements I and II are correct.
2. In humans, the bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
3. Both bone-marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes.
4. Options (1), (3) and (4) are incorrect.

**Solved independently** (answer withheld)

1. Statement I: bone marrow is the main (primary) lymphoid organ where all blood cells, including lymphocytes, are formed, so it is correct.
2. Statement II: as NCERT teaches, both bone marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes, so it is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 74)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q195_0e1c0638_03112026.png?v=0e1c06385d9e)

Publisher's solution, as printed:

![printed solution 195](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q195_d680053c_03112026.png?v=d680053c29fd)

---

## Q196

Biology · zoology · Structural Organisation in Animals

Match List I with List II related to digestive system of cockroach. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | The structures used for storing of food | I | Gizzard |
| B | Ring of 6-8 blind tubules at junction of foregut and midgut. | II | Gastric Caeca |
| C | Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut. | III | Malpighian tubules |
| D | The structures used for grinding the food. | IV | Crop |

- (1) A-III, B-II, C-IV, D-I
- **(2)** A-IV, B-II, C-III, D-I
- (3) A-I, B-II, C-III, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2) as
2. The structure used for griding the food particles – Gizzard
3. The structure used for storing of food – Crop
4. Ring of 6-8 blind tubules at junction of foregut and midgut which assists in secretion of digestive juices – Gastric Caeca
5. Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut which assists in elimination of nitrogenous wastes – Malpighian tubules

**Solved independently** (answer withheld)

1. Food storage in cockroach is done by the crop, so $A \to IV$.
2. The ring of 6-8 blind tubules at the foregut-midgut junction is the gastric caeca, so $B \to II$.
3. The ring of 100-150 yellow filaments at the midgut-hindgut junction is the Malpighian tubules, so $C \to III$.
4. Grinding of food is done by the gizzard (proventriculus), so $D \to I$.
5. $A$-IV, $B$-II, $C$-III, $D$-I is option $2$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 74)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q196_0320774d_03112026.png?v=0320774d3dd8)

Publisher's solution, as printed:

![printed solution 196](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q196_52d5a3b6_03112026.png?v=52d5a3b6d217)

---

## Q197

Biology · zoology · Neural Control and Coordination

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The cerebral hemispheres are connected by nerve tract known as corpus callosum.
- (Statement II) The brain stem consists of the medulla oblongata, pons and cerebrum.

- (1) Statement I is incorrect but Statement II is correct.
- (2) Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- **(4)** Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct answer is option (4) as statement I is correct but statement II is incorrect.
2. In human brain, a deep cleft divides the cerebrum longitudinally into two halves, which are termed as the left and right cerebral hemispheres.
3. The cerebral hemispheres are connected by a tract of nerve fibres called corpus callosum.
4. Three major regions make up the brain stem i.e. mid brain, pons and medulla oblongata.
5. Cerebrum is a part of forebrain which does not form brain stem.
6. Options (1), (2) and (3) are incorrect.

**Solved independently** (answer withheld)

1. Statement I: the two cerebral hemispheres are connected by a tract of nerve fibres called the corpus callosum, so Statement I is correct.
2. Statement II: the brain stem is formed by the midbrain, pons and medulla oblongata; the cerebrum is part of the forebrain, so Statement II is incorrect.
3. I correct and II incorrect matches option $4$.

**Subtopic:** Forebrain, Hindbrain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 75)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q197_ce4df751_03112026.png?v=ce4df7514926)

Publisher's solution, as printed:

![printed solution 197](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q197_ed2439f2_03112026.png?v=ed2439f26a30)

---

## Q198

Biology · zoology · Organisms and Populations

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below :

- (Statement I) Gause's competitive exclusion principle states that two closely related species competing for different resources cannot exist indefinitely.
- (Statement II) According to Gause's principle, during competition, the inferior will be eliminated. This may be true if resources are limiting.

- **(1)** Statement I is false but Statement II is true.
- (2) Both Statement I and Statement II are true.
- (3) Both Statement I and Statement II are false.
- (4) Statement I is true but Statement II is false.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Gause's competitive exclusion principle states that two closely related species competing for the same resources cannot exist indefinitely and the competitively inferior one will be eliminated eventually.
2. This may be true if resources are limiting.

**Solved independently** (answer withheld)

1. Gause's competitive exclusion principle: two closely related species competing for the same resources cannot coexist indefinitely; Statement I says 'different resources', so it is false.
2. Under the principle the competitively inferior species is eliminated, which holds when resources are limiting; Statement II is true.
3. Statement I false, Statement II true, which is option $1$.

**Subtopic:** Competition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 75)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q198_3caefa8d_03112026.png?v=3caefa8d07de)

Publisher's solution, as printed:

![printed solution 198](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q198_ebb88cef_03112026.png?v=ebb88cefdf98)

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

- **(1)** A-IV, B-III, C-I, D-II
- (2) A-II, B-IV, C-I, D-III
- (3) A-III, B-II, C-IV, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

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
5. $A\text{-}IV,\ B\text{-}III,\ C\text{-}I,\ D\text{-}II$ is option $1$.

**Subtopic:** Transcription · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 75)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q199_2f27e823_03112026.png?v=2f27e8235f53)

Publisher's solution, as printed:

![printed solution 199](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q199_c0d0e1ef_03112026.png?v=c0d0e1efa6a5)

---

## Q200

Biology · zoology · Human Reproduction

Identify the correct option (A), (B), (C), (D) with respect to spermatogenesis.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q200_33dd680a_03112026.png?v=33dd680a3e06)

- (1) ICSH, Leydig cells, Sertoli cells, spermatogenesis.
- **(2)** FSH, Leydig cells, Sertoli cells, spermiogenesis.
- (3) ICSH, Interstitial cells, Leydig cells, spermiogenesis.
- (4) FSH, Sertoli cells, Leydig cells, spermatogenesis.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct answer is option no. (2) as

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/figures_agent/q200_sol_1_68073cb7_03112026.png?v=68073cb7b003)

2. (A) is FSH which is a pituitary hormone.
3. (B) is Leydig cells which are found in the interstitial space outside of the seminiferous tubules.
4. (C) is Sertoli cells are found inside the seminiferous tubules.
5. (D) is Spermiogenesis which is a process that helps in transformation of spermatids into spermatozoa.

**Solved independently** (answer withheld)

1. GnRH stimulates release of LH and FSH, so (A) $=$ FSH.
2. LH acts on Leydig cells to stimulate androgen synthesis, so (B) $=$ Leydig cells.
3. FSH acts on Sertoli cells, so (C) $=$ Sertoli cells.
4. Sertoli cells secrete factors that help spermiogenesis (spermatids to sperm), so (D) $=$ spermiogenesis.
5. FSH, Leydig cells, Sertoli cells, spermiogenesis matches option $2$.

**Subtopic:** Male Gametogenesis (Spermatogenesis), Hormonal Regulation of Reproduction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 76)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q200_640335cb_03112026.png?v=640335cbe0c4)

Publisher's solution, as printed:

![printed solution 200](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q200_f72b3d7a_03112026.png?v=f72b3d7a8417)

