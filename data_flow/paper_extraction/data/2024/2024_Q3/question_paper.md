# NEET (UG) 2024 · Code Q3

200 questions · source `NEET_Papers/2024/Set_Q3/NEET_2024_Question_Paper_Q3.pdf` · every image a CDN link (0 without one) · 53 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Units and Measurements

In a vernier calipers, $(N + 1)$ divisions of vernier scale coincide with $N$ divisions of main scale. If 1 MSD represents $0.1\,\mathrm{mm}$, the vernier constant (in cm) is:

- (1) $\dfrac{1}{10N}$
- **(2)** $\dfrac{1}{100(N+1)}$
- (3) $100N$
- (4) $10(N + 1)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Since $(N+1)$ VSD $= N$ MSD, $1\,\text{VSD} = \frac{N}{N+1}\,\text{MSD}$.
2. $VC = 1\,\text{MSD} - 1\,\text{VSD} = \left(1 - \frac{N}{N+1}\right)\text{MSD} = \frac{1}{N+1}\,\text{MSD}$.
3. $1\,\text{MSD} = 0.1\,\mathrm{mm} = 0.01\,\mathrm{cm} = \frac{1}{100}\,\mathrm{cm}$.
4. $VC = \frac{1}{100(N+1)}\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q001_0d8e7efb_12112026.png?v=0d8e7efb6ffa)

---

## Q2

Physics · Wave Optics

If the monochromatic source in Young’s double slit experiment is replaced by white light, then

- (1) Interference pattern will disappear.
- (2) There will be a central dark fringe surrounded by a few coloured fringes.
- **(3)** There will be a central bright white fringe surrounded by a few coloured fringes.
- (4) All bright fringes will be of equal width.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. At the central point the path difference is $\Delta x = 0$ for every wavelength $\lambda$.
2. So every colour has a maximum there, and their overlap gives a central bright white fringe.
3. Fringe width $\beta = \frac{\lambda D}{d}$ differs for each $\lambda$, so away from the centre the maxima separate into a few coloured fringes, which is option $3$.

**Subtopic:** Young's Double-Slit Experiment (YDSE) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q002_f07a20a0_12112026.png?v=f07a20a0ac9e)

---

## Q3

Physics · Semiconductor Electronics

A logic circuit provides the output $Y$ as per the following truth table : The expression for the output $Y$ is :

![printed figure: Truth table of A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q003_809decf2_12112026.svg?v=809decf25af5)

*Truth table of A, B and output Y*

![drawn: Truth table of A, B and output Y](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_drawn/q003_question_8d29c2f6_12112026.svg?v=8d29c2f60ace)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $A.B+\bar{A}$
- (2) $A.\bar{B}+\bar{A}$
- **(3)** $\bar{B}$
- (4) $B$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. From the table, $Y=1$ for $(A,B)=(0,0)$ and $(1,0)$, i.e. whenever $B=0$.
2. $Y=0$ for $(0,1)$ and $(1,1)$, i.e. whenever $B=1$, so $Y$ does not depend on $A$.
3. Hence $Y=\bar{B}$.
4. Check option $2$: $A\cdot\bar{B}+\bar{A}$ at $A=0,B=1$ gives $1$, but the table gives $0$, so it fails; option $3$ is correct.

**Subtopic:** Logic Gates · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q003_26fc599c_12112026.png?v=26fc599c62f8)

---

## Q4

Physics · Current Electricity

The terminal voltage of the battery, whose emf is $10\,\mathrm{V}$ and internal resistance $1\,\Omega$, when connected through an external resistance of $4\,\Omega$ as shown in the figure is:

![printed figure: A 10 V cell with internal resistance 1 Ω (dashed box) driving current through an external 4 Ω resistor](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q004_c10a8ee1_12112026.png?v=c10a8ee1631f)

*A 10 V cell with internal resistance 1 Ω (dashed box) driving current through an external 4 Ω resistor*

![drawn: A 10 V cell with internal resistance 1 Ω (dashed box) driving current through an external 4 Ω resistor](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q004_question_fce34508_14112026.svg?v=fce3450820ef)  
*drawn by code/lib/physics_figure.py*

- (1) $4\,\mathrm{V}$
- (2) $6\,\mathrm{V}$
- **(3)** $8\,\mathrm{V}$
- (4) $10\,\mathrm{V}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The figure shows the battery discharging through the external resistor, with $R = 4\,\Omega$ in series with $r = 1\,\Omega$.
2. $I = \frac{E}{R + r} = \frac{10}{4 + 1} = 2\,\mathrm{A}$.
3. $V = E - Ir = 10 - 2 \times 1 = 8\,\mathrm{V}$.
4. Check: $V = IR = 2 \times 4 = 8\,\mathrm{V}$, which is option $3$.

**Subtopic:** Terminal Potential Difference · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q004_a450145e_12112026.png?v=a450145ed7f6)

---

## Q5

Physics · Magnetic Effect of Electric Current

In a uniform magnetic field of $0.049\,\mathrm{T}$, a magnetic needle performs 20 complete oscillations in $5$ seconds as shown. The moment of inertia of the needle is $9.8 \times 10^{-6}\,\mathrm{kg\,m^{2}}$. If the magnitude of magnetic moment of the needle is $x \times 10^{-5}\,\mathrm{A\,m^{2}}$, then the value of '$x$' is :

![printed figure: A magnetic needle hung by a thread from a ceiling in a uniform horizontal field B](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q005_73225d39_12112026.png?v=73225d3927c4)

*A magnetic needle hung by a thread from a ceiling in a uniform horizontal field B*

![drawn: A magnetic needle hung by a thread from a ceiling in a uniform horizontal field B](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q005_question_d0faec80_14112026.svg?v=d0faec80b487)  
*drawn by code/lib/physics_figure.py*

- (1) $5\pi^{2}$
- (2) $128\pi^{2}$
- (3) $50\pi^{2}$
- **(4)** $1280\pi^{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Time period: $T = \frac{5\,\mathrm{s}}{20} = 0.25\,\mathrm{s}$.
2. For an oscillating magnetic needle, $T = 2\pi\sqrt{\frac{I}{MB}}$.
3. Rearranging: $M = \frac{4\pi^2 I}{B T^2}$.
4. $B T^2 = 0.049 \times 0.0625 = 3.0625 \times 10^{-3}$.
5. $\frac{I}{BT^2} = \frac{9.8 \times 10^{-6}}{3.0625 \times 10^{-3}} = 3.2 \times 10^{-3}$.
6. $M = 4\pi^2 \times 3.2 \times 10^{-3} = 12.8\pi^2 \times 10^{-3} = 1280\pi^2 \times 10^{-5}\,\mathrm{Am^2}$.
7. So $x = 1280\pi^2$, which is option $4$.

**Subtopic:** The Dipole in a Uniform Magnetic Field · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q005_8ea94ac2_12112026.png?v=8ea94ac26f3b)

---

## Q6

Physics · Current Electricity

A wire of length '$l$' and resistance $100\,\Omega$ is divided into 10 equal parts. The first 5 parts are connected in series while the next 5 parts are connected in parallel. The two combinations are again connected in series. The resistance of this final combination is:

- (1) $26\,\Omega$
- **(2)** $52\,\Omega$
- (3) $55\,\Omega$
- (4) $60\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Dividing the wire into 10 equal parts gives each part $r = \frac{100\,\Omega}{10} = 10\,\Omega$.
2. Five parts in series: $R_s = 5r = 5 \times 10\,\Omega = 50\,\Omega$.
3. Five parts in parallel: $R_p = \frac{r}{5} = \frac{10\,\Omega}{5} = 2\,\Omega$.
4. The two combinations in series: $R = R_s + R_p = 50\,\Omega + 2\,\Omega = 52\,\Omega$, which is option $2$.

**Subtopic:** Combination of Resistors · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q006_51e2fa08_12112026.png?v=51e2fa0803c6)

---

## Q7

Physics · Laws of Motion

A horizontal force $10\,\mathrm{N}$ is applied to a block $A$ as shown in figure. The mass of blocks $A$ and $B$ are $2\,\mathrm{kg}$ and $3\,\mathrm{kg}$ respectively. The blocks slide over a frictionless surface. The force exerted by block $A$ on block $B$ is :

![printed figure: Horizontal force F = 10 N pushing block A (2 kg) against block B (3 kg) on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q007_5d5b7cf0_12112026.png?v=5d5b7cf085ce)

*Horizontal force F = 10 N pushing block A (2 kg) against block B (3 kg) on a frictionless floor*

![drawn: Horizontal force F = 10 N pushing block A (2 kg) against block B (3 kg) on a frictionless floor](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q007_question_1f5d3f00_14112026.svg?v=1f5d3f00c2cd)  
*drawn by code/lib/physics_figure.py*

- (1) Zero
- (2) $4\,\mathrm{N}$
- **(3)** $6\,\mathrm{N}$
- (4) $10\,\mathrm{N}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Both blocks move together on the frictionless surface, so $a = \frac{F}{m_A + m_B} = \frac{10}{2+3} = 2\,\mathrm{m/s^2}$.
2. The only horizontal force on $B$ is the contact force from $A$: $N = m_B a$.
3. $N = 3 \times 2 = 6\,\mathrm{N}$, which is option $3$.

**Subtopic:** Block Problem · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q007_c088125a_12112026.png?v=c088125ab73a)

---

## Q8

Physics · Magnetic Effect of Electric Current

A tightly wound 100 turns coil of radius $10\,\mathrm{cm}$ carries a current of $7\,\mathrm{A}$. The magnitude of the magnetic field at the centre of the coil is (Take permeability of free space as $4\pi \times 10^{-7}$ SI units):

- (1) $44\,\mathrm{mT}$
- (2) $4.4\,\mathrm{T}$
- **(3)** $4.4\,\mathrm{mT}$
- (4) $44\,\mathrm{T}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For a tightly wound circular coil of $N$ turns, the field at the centre is $B = \frac{\mu_0 N I}{2R}$.
2. Substitute $N = 100$, $I = 7\,\mathrm{A}$, $R = 0.1\,\mathrm{m}$: $B = \frac{4\pi \times 10^{-7} \times 100 \times 7}{2 \times 0.1}$.
3. $B = 4\pi \times 10^{-7} \times 3500 = 1.4\pi \times 10^{-3}\,\mathrm{T}$.
4. $1.4\pi \times 10^{-3} \approx 4.4 \times 10^{-3}\,\mathrm{T} = 4.4\,\mathrm{mT}$, which is option $3$.

**Subtopic:** Magnetic Field on the Axis of a Circular Current Loop · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q008_ba965480_12112026.png?v=ba965480092b)

---

## Q9

Physics · Alternating Current

In an ideal transformer, the turns ratio is $\frac{N_P}{N_S} = \frac{1}{2}$. The ratio $V_S : V_P$ is equal to (the symbols carry their usual meaning) :

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $1 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For an ideal transformer, $\frac{V_S}{V_P} = \frac{N_S}{N_P}$.
2. Given $\frac{N_P}{N_S} = \frac{1}{2}$, so $\frac{N_S}{N_P} = 2$.
3. $V_S : V_P = 2 : 1$, which is option $2$.

**Subtopic:** Transformer · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q009_4b0e4039_12112026.png?v=4b0e4039aa10)

---

## Q10

Physics · Modern Physics

The graph which shows the variation of $\left(\frac{1}{\lambda^2}\right)$ and its kinetic energy, $E$ is (where $\lambda$ is de Broglie wavelength of a free particle):

- (1) ![printed figure: 1/lambda^2 against E: a curve rising from O, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q010_option_1_3a588cb5_12112026.png?v=3a588cb5c55d) *1/lambda^2 against E: a curve rising from O, concave upward* ![drawn: 1/lambda^2 against E: a curve rising from O, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q010_option_1_e4b7179d_14112026.svg?v=e4b7179d9a9a)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Graph of 1/lambda^2 against E: a curve falling steeply then flattening (hyperbola-like)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q010_option_2_39d16ee1_12112026.png?v=39d16ee10bab) *Graph of 1/lambda^2 against E: a curve falling steeply then flattening (hyperbola-like)* ![drawn: Graph of 1/lambda^2 against E: a curve falling steeply then flattening (hyperbola-like)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q010_option_2_6582c27d_14112026.svg?v=6582c27dd60b)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Graph of 1/lambda^2 against E: a curve rising from the origin and flattening (concave down)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q010_option_3_33e12b4b_12112026.png?v=33e12b4b8f87) *Graph of 1/lambda^2 against E: a curve rising from the origin and flattening (concave down)* ![drawn: Graph of 1/lambda^2 against E: a curve rising from the origin and flattening (concave down)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q010_option_3_7fd45dec_14112026.svg?v=7fd45dec3078)  
*drawn by code/lib/physics_figure.py*
- **(4)** ![printed figure: Straight line through the origin: 1/lambda^2 against E](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q010_option_4_b26bef4a_12112026.png?v=b26bef4a0a46) *Straight line through the origin: 1/lambda^2 against E* ![drawn: Straight line through the origin: 1/lambda^2 against E](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q010_option_4_639371a3_14112026.svg?v=639371a3ba23)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For a free particle, $p = \sqrt{2mE}$.
2. de Broglie: $\lambda = \frac{h}{p} = \frac{h}{\sqrt{2mE}}$.
3. Squaring and inverting: $\frac{1}{\lambda^2} = \frac{2m}{h^2}E$.
4. So $\frac{1}{\lambda^2} \propto E$, a straight line through the origin, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 4)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q010_8c5669e1_12112026.png?v=8c5669e1a95b)

---

## Q11

Physics · Modern Physics

> ⚠ Statement II (atoms emit their characteristic spectrum) is near-verbatim NCERT Class 12 "Atoms", which makes both statements true (option 1); read strictly, an atom emits its characteristic spectrum only when excited, which makes Statement II false and gives the booklet's key (3). Two blind solves chose 1 (one noting 3 as the strict reading) and an audit backed 3, so the wording, not the solver, decides it. Same question as 2024_S1 q020.

> ⚠ The independent solve chose (1); the booklet prints (3).

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below.

- (Statement I) Atoms are electrically neutral as they contain equal number of positive and negative charges.
- (Statement II) Atoms of each element are stable and emit their characteristic spectrum.

- (1) Both Statement I and Statement II are correct
- (2) Both Statement I and Statement II are incorrect
- **(3)** Statement I is correct but Statement II is incorrect
- (4) Statement I is incorrect but Statement II is correct

**Answer** — booklet: (3) · independent solve: (1) · differs

**Solved independently** (answer withheld)

1. Statement I: an atom has equal total positive charge $(+Ze)$ and negative charge $(-Ze)$, so net charge $= 0$; true.
2. Statement II: NCERT Class 12 (Atoms, introduction) lists as known facts that atoms of each element are stable and emit their characteristic spectrum; true as taught.
3. Both statements correct, which is option $1$.

**Subtopic:** Alpha-Particle Scattering and Rutherford Nuclear Model of the Atom and Thomson's Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q011_9af260f7_12112026.png?v=9af260f7fab3)

---

## Q12

Physics · Laws of Motion

A bob is whirled in a horizontal plane by means of a string with an initial speed of $\omega$ rpm. The tension in the string is $T$. If speed becomes $2\omega$ while keeping the same radius, the tension in the string becomes:

- (1) $T$
- **(2)** $4T$
- (3) $\frac{T}{4}$
- (4) $\sqrt{2}T$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The string tension provides the centripetal force: $T = m\omega^2 r$.
2. With the same radius and angular speed $2\omega$: $T' = m(2\omega)^2 r = 4m\omega^2 r$.
3. $T' = 4T$, which is option $2$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q012_6e38c97b_12112026.png?v=6e38c97b919a)

---

## Q13

Physics · Semiconductor Electronics

Consider the following statements A and B and identify the correct answer:

![printed figure: V-I axes with four quadrants labelled (I) to (IV)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q013_6c87ac8f_12112026.png?v=6c87ac8f5474)

*V-I axes with four quadrants labelled (I) to (IV)*

![drawn: V-I axes with four quadrants labelled (I) to (IV)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q013_question_e01ab55d_14112026.svg?v=e01ab55df709)  
*drawn by code/lib/physics_figure.py*

- (A) For a solar-cell, the I-V characteristics lies in the IV quadrant of the given graph.
- (B) In a reverse biased $pn$ junction diode, the current measured in ($\mu\mathrm{A}$), is due to majority charge carriers.

- **(1)** A is correct but B is incorrect
- (2) A is incorrect but B is correct
- (3) Both A and B are correct
- (4) Both A and B are incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A solar cell supplies power: open-circuit voltage $V > 0$ while short-circuit current $I < 0$, so its $I$-$V$ characteristic lies in quadrant $\mathrm{IV}$; statement A is correct.
2. In reverse bias the small current ($\mu\mathrm{A}$) is the drift of minority carriers across the junction, not majority carriers; statement B is incorrect.
3. A correct, B incorrect, which is option $1$.

**Subtopic:** Special Purpose PN Junction Diodes, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q013_18aa33cc_12112026.png?v=18aa33cc4a03)

---

## Q14

Physics · Thermodynamics

A thermodynamic system is taken through the cycle $abcda$. The work done by the gas along the path $bc$ is:

![printed figure: P-V cycle abcda: rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q014_69876370_12112026.png?v=69876370dd30)

*P-V cycle abcda: rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3*

![drawn: P-V cycle abcda: rectangle between 100 kPa and 300 kPa, 100 cm3 and 400 cm3](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q014_question_e6bd464a_14112026.svg?v=e6bd464a80e5)  
*drawn by code/lib/physics_figure.py*

- **(1)** Zero
- (2) $30\,\mathrm{J}$
- (3) $-90\,\mathrm{J}$
- (4) $-60\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. From the figure, $b$ and $c$ both lie at $V = 400\,\mathrm{cm^3}$; only $P$ changes from $100\,\mathrm{kPa}$ to $300\,\mathrm{kPa}$.
2. Along $bc$, $dV = 0$, so $W_{bc} = \int P\,dV = 0$, which is option $1$.

**Subtopic:** Isochoric Process · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q014_745def0d_12112026.png?v=745def0d5a97)

---

## Q15

Physics · Electrostatics

A thin spherical shell is charged by some source. The potential difference between the two points $C$ and $P$ (in V) shown in the figure is:
(Take $\frac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}$ SI units)

![printed figure: Charged thin spherical shell of radius R with centre C and point P on the shell](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q015_eee62460_12112026.png?v=eee6246037bd)

*Charged thin spherical shell of radius R with centre C and point P on the shell*

![drawn: Charged thin spherical shell of radius R with centre C and point P on the shell](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q015_question_0ada7dfa_14112026.svg?v=0ada7dfa934c)  
*drawn by code/lib/physics_figure.py*

- (1) $3 \times 10^{5}$
- (2) $1 \times 10^{5}$
- (3) $0.5 \times 10^{5}$
- **(4)** Zero

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Inside a charged conducting/thin spherical shell $E = 0$, so the potential is the same everywhere inside and equals the surface value.
2. $V_C = \frac{1}{4\pi\varepsilon_0}\frac{q}{R} = \frac{9\times10^{9}\times10^{-6}}{0.03} = 3\times10^{5}\,\text{V}$.
3. $P$ lies on the shell, so $V_P = \frac{1}{4\pi\varepsilon_0}\frac{q}{R} = 3\times10^{5}\,\text{V}$.
4. $V_C - V_P = 0$, which is option $4$.

**Subtopic:** Electrostatic Potential Throughout the Volume of a Conductor · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 5)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q015_0ed6ec80_12112026.png?v=0ed6ec806121)

---

## Q16

Physics · Rotational Motion

The moment of inertia of a thin rod about an axis passing through its mid point and perpendicular to the rod is $2400\,\mathrm{g\,cm^{2}}$. The length of the $400\,\mathrm{g}$ rod is nearly:

- **(1)** $8.5\,\mathrm{cm}$
- (2) $17.5\,\mathrm{cm}$
- (3) $20.7\,\mathrm{cm}$
- (4) $72.0\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For a thin rod about a perpendicular axis through its midpoint, $I = \frac{ML^{2}}{12}$.
2. $L^{2} = \frac{12I}{M} = \frac{12 \times 2400\,\mathrm{g\,cm^{2}}}{400\,\mathrm{g}} = 72\,\mathrm{cm^{2}}$.
3. $L = \sqrt{72}\,\mathrm{cm} \approx 8.49\,\mathrm{cm} \approx 8.5\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Moment of Inertia of a Uniform Rod · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q016_75f1ac9a_12112026.png?v=75f1ac9adb03)

---

## Q17

Physics · Kinematics

A particle moving with uniform speed in a circular path maintains:

- (1) Constant velocity
- (2) Constant acceleration
- (3) Constant velocity but varying acceleration
- **(4)** Varying velocity and varying acceleration

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Speed $|\vec v|$ is constant, but $\vec v$ is tangential and its direction changes continuously, so velocity varies.
2. Acceleration $a = \frac{v^2}{r}$ is constant in magnitude but always points towards the centre, so its direction changes and $\vec a$ varies.
3. Both velocity and acceleration vary, which is option $4$.

**Subtopic:** Uniform Circular Motion · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 5)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q017_3a5892d7_12112026.png?v=3a5892d76d69)

---

## Q18

Physics · Modern Physics

If $c$ is the velocity of light in free space, the correct statements about photon among the following are:

- (A) The energy of a photon is $E = h\nu$.
- (B) The velocity of a photon is $c$.
- (C) The momentum of a photon, $p = \frac{h\nu}{c}$.
- (D) In a photon-electron collision, both total energy and total momentum are conserved.
- (E) Photon possesses positive charge.

- (1) A and B only
- **(2)** A, B, C and D only
- (3) A, C and D only
- (4) A, B, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement A: a photon's energy is $E = h\nu$, so A is true.
2. Statement B: a photon travels at $c$ in free space, so B is true.
3. Statement C: momentum $p = \frac{E}{c} = \frac{h\nu}{c}$, so C is true.
4. Statement D: in a photon-electron collision total energy and total momentum are conserved, so D is true.
5. Statement E: a photon carries no charge, so E is false.
6. True set is A, B, C and D, which is option $2$.

**Subtopic:** Photon Energy and Number of Photons · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 6)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q018_18f26c4a_12112026.png?v=18f26c4ae54c)

---

## Q19

Physics · Work, Energy and Power

At any instant of time $t$, the displacement of any particle is given by $2t - 1$ (SI unit) under the influence of force of $5\,N$. The value of instantaneous power is (in SI unit):

- **(1)** $10$
- (2) $5$
- (3) $7$
- (4) $6$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Velocity is the time derivative of displacement: $v = \frac{dx}{dt} = \frac{d}{dt}(2t - 1) = 2\,\mathrm{m/s}$.
2. Instantaneous power is $P = F v$.
3. $P = 5\,\mathrm{N} \times 2\,\mathrm{m/s} = 10\,\mathrm{W}$, which is option $1$.

**Subtopic:** Power · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 6)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q019_e78e32e8_12112026.png?v=e78e32e8cae9)

---

## Q20

Physics · Ray Optics

A light ray enters through a right angled prism at point $P$ with the angle of incidence $30^\circ$ as shown in figure. It travels through the prism parallel to its base $BC$ and emerges along the face $AC$. The refractive index of the prism is :

![printed figure: A ray enters right-angled prism ABC at P on face AB at 30 degrees incidence, travels parallel to base BC and emerges along face AC](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q020_7734b68d_12112026.png?v=7734b68d3558)

*A ray enters right-angled prism ABC at P on face AB at 30 degrees incidence, travels parallel to base BC and emerges along face AC*

![drawn: A ray enters right-angled prism ABC at P on face AB at 30 degrees incidence, travels parallel to base BC and emerges along face AC](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q020_question_06c11cce_14112026.svg?v=06c11cce604c)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{\sqrt{5}}{4}$
- **(2)** $\frac{\sqrt{5}}{2}$
- (3) $\frac{\sqrt{3}}{4}$
- (4) $\frac{\sqrt{3}}{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The prism angle at $A$ is $90^\circ$, so the refraction angles inside satisfy $r_1 + r_2 = A = 90^\circ$.
2. Snell's law at $P$: $\sin 30^\circ = \mu \sin r_1 \Rightarrow \sin r_1 = \frac{1}{2\mu}$.
3. The ray emerges along face $AC$ (grazing), so at that face $r_2 = \theta_c$ with $\sin r_2 = \frac{1}{\mu}$.
4. Since $r_2 = 90^\circ - r_1$, $\cos r_1 = \frac{1}{\mu}$.
5. $\sin^2 r_1 + \cos^2 r_1 = 1 \Rightarrow \frac{1}{4\mu^2} + \frac{1}{\mu^2} = 1 \Rightarrow \mu^2 = \frac{5}{4}$.
6. $\mu = \frac{\sqrt{5}}{2}$, which is option $2$.

**Subtopic:** Prism, Total Internal Reflection (TIR) · **Difficulty:** easy (4 steps)

**Printed in the booklet** (page 6)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q020_6832e640_12112026.png?v=6832e640a435)

---

## Q21

Physics · Capacitance

In the following circuit, the equivalent capacitance between terminal $A$ and terminal $B$ is :

![printed figure: Five 2 uF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q021_5fef7751_12112026.png?v=5fef7751f76f)

*Five 2 uF capacitors in a bridge between terminals A and B*

![drawn: Five 2 uF capacitors in a bridge between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q021_question_2d40dc38_14112026.svg?v=2d40dc382485)  
*drawn by code/lib/physics_figure.py*

- **(1)** $2\,\mu\mathrm{F}$
- (2) $1\,\mu\mathrm{F}$
- (3) $0.5\,\mu\mathrm{F}$
- (4) $4\,\mu\mathrm{F}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The circuit is a Wheatstone bridge: $A$ to the top and bottom middle nodes through $2\,\mu F$ each, those nodes to $B$ through $2\,\mu F$ each, and a $2\,\mu F$ capacitor joining the two middle nodes.
2. Balance condition: $\frac{C_1}{C_2} = \frac{2}{2} = \frac{C_3}{C_4} = \frac{2}{2}$, so the middle nodes are at equal potential and the middle capacitor holds no charge.
3. Each branch is two $2\,\mu F$ capacitors in series: $C_s = \frac{2 \times 2}{2 + 2} = 1\,\mu F$.
4. The two branches are in parallel: $C_{AB} = 1 + 1 = 2\,\mu F$, which is option $1$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q021_40a03a53_12112026.png?v=40a03a5346a2)

---

## Q22

Physics · Units and Measurements

The quantities which have the same dimensions as those of solid angle are :

- **(1)** strain and angle
- (2) stress and angle
- (3) strain and arc
- (4) angular speed and stress

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Solid angle $\Omega = \frac{A}{r^2}$, so $[\Omega] = \frac{[L^2]}{[L^2]} = [M^0 L^0 T^0]$ (dimensionless).
2. Strain $= \frac{\Delta l}{l}$, so $[\text{strain}] = [M^0 L^0 T^0]$.
3. Plane angle $\theta = \frac{s}{r}$, so $[\theta] = [M^0 L^0 T^0]$.
4. Stress $= \frac{F}{A}$ has $[M L^{-1} T^{-2}]$, angular speed has $[T^{-1}]$ and arc has $[L]$, so options $4$, $2$ and $3$ fail.
5. Only strain and angle are dimensionless like solid angle, which is option $1$.

**Subtopic:** Dimensional Formulae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q022_b4064827_12112026.png?v=b40648272b57)

---

## Q23

Physics · Mechanical Properties of Solids

The maximum elongation of a steel wire of $1\,\mathrm{m}$ length if the elastic limit of steel and its Young’s modulus, respectively, are $8 \times 10^{8}\,\mathrm{N\,m^{-2}}$ and $2 \times 10^{11}\,\mathrm{N\,m^{-2}}$, is:

- **(1)** $4\,\mathrm{mm}$
- (2) $0.4\,\mathrm{mm}$
- (3) $40\,\mathrm{mm}$
- (4) $8\,\mathrm{mm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Maximum stress the wire can take elastically is the elastic limit, $\sigma = 8 \times 10^{8}\,\mathrm{N\,m^{-2}}$.
2. Maximum strain $= \frac{\sigma}{Y} = \frac{8 \times 10^{8}}{2 \times 10^{11}} = 4 \times 10^{-3}$.
3. $\Delta L = \text{strain} \times L = 4 \times 10^{-3} \times 1\,\mathrm{m} = 4 \times 10^{-3}\,\mathrm{m} = 4\,\mathrm{mm}$, which is option $1$.

**Subtopic:** Hooke's Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q023_cf5ab485_12112026.png?v=cf5ab4858d88)

---

## Q24

Physics · Electromagnetic Induction

In the above diagram, a strong bar magnet is moving towards solenoid-2 from solenoid-1. The direction of induced current in solenoid-1 and that in solenoid-2, respectively, are through the directions:

![printed figure: A bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q024_18c9ec63_12112026.png?v=18c9ec63b274)

*A bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)*

![drawn: A bar magnet N-S moving with velocity v from solenoid-1 (ends A, B) towards solenoid-2 (ends C, D)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q024_question_104012a5_14112026.svg?v=104012a50985)  
*drawn by code/lib/physics_figure.py*

- **(1)** $AB$ and $DC$
- (2) $BA$ and $CD$
- (3) $AB$ and $CD$
- (4) $BA$ and $DC$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The magnet moves to the right with its $N$ pole facing solenoid-1 and its $S$ pole facing solenoid-2.
2. In solenoid-1 the $N$ pole recedes, so by Lenz's law the right (near) end of solenoid-1 becomes an $S$ pole to oppose the decrease in flux.
3. In solenoid-2 the $S$ pole approaches, so by Lenz's law the left (near) end of solenoid-2 becomes an $S$ pole to oppose the increase in flux.
4. An $S$ pole on the right end of solenoid-1 needs current clockwise when viewed from the right; with the wire rising on the front face from terminal $A$, this current flows $A \to B$.
5. Both solenoids are wound the same way, but solenoid-2 has its $S$ pole on the left (opposite magnetisation), so its current flows from $D \to C$.
6. Hence the currents are $AB$ and $DC$, which is option $1$.

**Subtopic:** Lenz's Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 7)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q024_7458fa51_12112026.png?v=7458fa51dfe1)

---

## Q25

Physics · Gravitation

The mass of a planet is $\frac{1}{10}^{\text{th}}$ that of the earth and its diameter is half that of the earth. The acceleration due to gravity on that planet is:

- (1) $19.6\,\mathrm{m\,s^{-2}}$
- (2) $9.8\,\mathrm{m\,s^{-2}}$
- (3) $4.9\,\mathrm{m\,s^{-2}}$
- **(4)** $3.92\,\mathrm{m\,s^{-2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Surface gravity is $g = \frac{GM}{R^2}$.
2. For the planet, $M' = \frac{M}{10}$ and $R' = \frac{R}{2}$ (diameter halved).
3. $g' = \frac{G(M/10)}{(R/2)^2} = \frac{4}{10}\frac{GM}{R^2} = 0.4\,g$.
4. $g' = 0.4 \times 9.8 = 3.92\,\mathrm{m\,s^{-2}}$, which is option $4$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 7)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q025_29f74b21_12112026.png?v=29f74b21215d)

---

## Q26

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

**Solved independently** (answer withheld)

1. Balmer series: $\frac{1}{\lambda} = R_H\left(\frac{1}{2^2} - \frac{1}{n_2^2}\right)$, so wavelength decreases as $n_2$ increases.
2. $n_2 = 3 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{5}{36}$, $\lambda \approx 656.3\,\text{nm}$ (A-III).
3. $n_2 = 4 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{3}{16}$, $\lambda \approx 486.1\,\text{nm}$ (B-IV).
4. $n_2 = 5 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{21}{100}$, $\lambda \approx 434.1\,\text{nm}$ (C-II).
5. $n_2 = 6 \to 2$: $\frac{1}{\lambda} = R_H \cdot \frac{2}{9}$, $\lambda \approx 410.2\,\text{nm}$ (D-I).
6. A-III, B-IV, C-II, D-I is option $2$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q026_6d61470f_12112026.png?v=6d61470f33f1)

---

## Q27

Physics · Wave Optics

An unpolarised light beam strikes a glass surface at Brewster's angle. Then

- (1) The reflected light will be partially polarised.
- (2) The refracted light will be completely polarised.
- (3) Both the reflected and refracted light will be completely polarised.
- **(4)** The reflected light will be completely polarised but the refracted light will be partially polarised.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. At Brewster's angle $i_B$ with $\tan i_B = \mu$, the reflected ray is completely plane polarised and the refracted ray is partially polarised, so option $4$.

**Subtopic:** Brewster's Law · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 8)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q027_2e4e7f92_12112026.png?v=2e4e7f921276)

---

## Q28

Physics · Magnetic Effect of Electric Current

Match List-I with List-II. Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
|  | (Material) |  | (Susceptibility ($\chi$)) |
| A | Diamagnetic | I | $\chi = 0$ |
| B | Ferromagnetic | II | $0 > \chi \geq -1$ |
| C | Paramagnetic | III | $\chi >> 1$ |
| D | Non-magnetic | IV | $0 < \chi < \varepsilon$ (a small positive number) |

- **(1)** A-II, B-III, C-IV, D-I
- (2) A-II, B-I, C-III, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Diamagnetic materials have a small negative susceptibility, $-1 \leq \chi < 0$, so A matches II.
2. Ferromagnetic materials have a very large positive susceptibility, $\chi \gg 1$, so B matches III.
3. Paramagnetic materials have a small positive susceptibility, $0 < \chi < \varepsilon$, so C matches IV.
4. Non-magnetic materials have $\chi = 0$, so D matches I.
5. A-II, B-III, C-IV, D-I is option $1$.

**Subtopic:** Magnetism and Matter · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 8)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q028_b1fa294c_12112026.png?v=b1fa294cfdd8)

---

## Q29

Physics · Work, Energy and Power

Two bodies $A$ and $B$ of same mass undergo completely inelastic one dimensional collision. The body $A$ moves with velocity $v_1$ while body $B$ is at rest before collision. The velocity of the system after collision is $v_2$. The ratio $v_1 : v_2$ is

- (1) $1 : 2$
- **(2)** $2 : 1$
- (3) $4 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In a completely inelastic collision the bodies stick together, and linear momentum is conserved.
2. $m v_1 + m \cdot 0 = (m + m) v_2$.
3. $v_2 = \frac{v_1}{2}$.
4. $v_1 : v_2 = 2 : 1$, which is option $2$.

**Subtopic:** Problems on Inelastic Collision · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 8)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q029_cdd34209_12112026.png?v=cdd3420973e2)

---

## Q30

Physics · Modern Physics

$\mathrm{{}^{290}_{82}X \xrightarrow{\alpha} Y \xrightarrow{e^{+}} Z \xrightarrow{\beta^{-}} P \xrightarrow{e^{-}} Q}$
In the nuclear emission stated above, the mass number and atomic number of the product $Q$ respectively, are

- (1) 280, 81
- (2) 286, 80
- (3) 288, 82
- **(4)** 286, 81

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\alpha$ decay: $A = 290 - 4 = 286$, $Z = 82 - 2 = 80$, so $Y = {}^{286}_{80}Y$.
2. Positron ($e^{+}$) emission: $A$ unchanged, $Z = 80 - 1 = 79$, so $Z = {}^{286}_{79}Z$.
3. $\beta^{-}$ emission: $A$ unchanged, $Z = 79 + 1 = 80$, so $P = {}^{286}_{80}P$.
4. Electron ($e^{-}$) emission is another $\beta^{-}$ decay: $Z = 80 + 1 = 81$, so $Q = {}^{286}_{81}Q$.
5. Mass number $286$, atomic number $81$, which is option $4$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 8)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q030_e224044e_12112026.png?v=e224044eaf1a)

---

## Q31

Physics · Oscillations

If $x = 5\sin\left(\pi t + \frac{\pi}{3}\right)\,m$ represents the motion of a particle executing simple harmonic motion, the amplitude and time period of motion, respectively, are

- (1) $5\,\mathrm{cm}$, $2\,\mathrm{s}$
- **(2)** $5\,\mathrm{m}$, $2\,\mathrm{s}$
- (3) $5\,\mathrm{cm}$, $1\,\mathrm{s}$
- (4) $5\,\mathrm{m}$, $1\,\mathrm{s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Compare with $x = A\sin(\omega t + \phi)$: $A = 5\,\mathrm{m}$ and $\omega = \pi\,\mathrm{rad\,s^{-1}}$.
2. $T = \frac{2\pi}{\omega} = \frac{2\pi}{\pi} = 2\,\mathrm{s}$.
3. Amplitude $5\,\mathrm{m}$ and period $2\,\mathrm{s}$, which is option $2$.

**Subtopic:** Calculate Time Period of SHM, Calculate Amplitude of SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q031_0b142852_12112026.png?v=0b142852acc8)

---

## Q32

Physics · Mechanical Properties of Fluids

A thin flat circular disc of radius $4.5\,\mathrm{cm}$ is placed gently over the surface of water. If surface tension of water is $0.07\,\mathrm{N\,m^{-1}}$, then the excess force required to take it away from the surface is

- **(1)** $19.8\,\mathrm{mN}$
- (2) $198\,\mathrm{N}$
- (3) $1.98\,\mathrm{mN}$
- (4) $99\,\mathrm{N}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The extra force needed equals the surface tension force along the contact line, which is the disc's circumference: $F = T \cdot 2\pi r$.
2. $2\pi r = 2\pi \times 0.045\,\mathrm{m} = 0.2827\,\mathrm{m}$.
3. $F = 0.07 \times 0.2827 = 0.01979\,\mathrm{N} \approx 19.8\,\mathrm{mN}$, which is option $1$.

**Subtopic:** Surface Tension and Surface Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q032_12181cb2_12112026.png?v=12181cb206ab)

---

## Q33

Physics · Semiconductor Electronics

The output ($Y$) of the given logic gate is similar to the output of an/a

![printed figure: NAND gate with tied inputs A and NOR gate with tied inputs B feeding a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q033_026624cb_12112026.png?v=026624cb09a7)

*NAND gate with tied inputs A and NOR gate with tied inputs B feeding a NOR gate with output Y*

![drawn: NAND gate with tied inputs A and NOR gate with tied inputs B feeding a NOR gate with output Y](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q033_question_b457e0bd_14112026.svg?v=b457e0bd5d59)  
*drawn by code/lib/physics_figure.py*

- (1) NAND gate
- (2) NOR gate
- (3) OR gate
- **(4)** AND gate

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A NAND gate with both inputs tied to $A$ gives $\overline{A \cdot A} = \overline{A}$.
2. A NOR gate with both inputs tied to $B$ gives $\overline{B + B} = \overline{B}$.
3. The final NOR gate gives $Y = \overline{\overline{A} + \overline{B}}$.
4. By De Morgan's theorem, $\overline{\overline{A} + \overline{B}} = A \cdot B$, which is an AND gate, option $4$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q033_8e173f74_12112026.png?v=8e173f74bc33)

---

## Q34

Physics · Electrostatics

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the correct answer from the options given below:

- (Assertion A) The potential ($V$) at any axial point, at $2\,\mathrm{m}$ distance ($r$) from the centre of the dipole of dipole moment vector $\vec{P}$ of magnitude, $4 \times 10^{-6}\,\mathrm{C\,m}$, is $\pm 9 \times 10^{3}\,V$. (Take $\frac{1}{4\pi \epsilon_0} = 9 \times 10^{9}$ SI units)
- (Reason R) $V = \pm \frac{2P}{4\pi \epsilon_0 r^2}$, where $r$ is the distance of any axial point, situated at $2\,\mathrm{m}$ from the centre of the dipole.

- (1) Both A and R are true and R is the correct explanation of A.
- (2) Both A and R are true and R is NOT the correct explanation of A.
- **(3)** A is true but R is false.
- (4) A is false but R is true.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For a short dipole, potential at an axial point is $V = \pm \frac{1}{4\pi\epsilon_0}\frac{P}{r^2}$.
2. $V = \pm \frac{9\times10^{9} \times 4\times10^{-6}}{2^2}$.
3. $V = \pm \frac{36\times10^{3}}{4} = \pm 9\times10^{3}\,\mathrm{V}$, so Assertion A is true.
4. Reason R uses $V = \pm \frac{2P}{4\pi\epsilon_0 r^2}$, which has an extra factor $2$ (that factor belongs to the axial field $E = \frac{2P}{4\pi\epsilon_0 r^3}$), so R is false.
5. A true, R false, which is option $3$.

**Subtopic:** Potential Due to an Electric Dipole · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 9)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q034_ea78e474_12112026.png?v=ea78e47466a8)

---

## Q35

Physics · Rotational Motion

A wheel of a bullock cart is rolling on a level road as shown in the figure below. If its linear speed is $\nu$ in the direction shown, which one of the following options is correct ($P$ and $Q$ are any highest and lowest points on the wheel, respectively)?

![printed figure: A spoked wheel rolling on a level road with velocity v; P at the top, Q at the bottom](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q035_ebab2566_12112026.png?v=ebab256681b3)

*A spoked wheel rolling on a level road with velocity v; P at the top, Q at the bottom*

![drawn: A spoked wheel rolling on a level road with velocity v; P at the top, Q at the bottom](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q035_question_551f9358_14112026.svg?v=551f93582f35)  
*drawn by code/lib/physics_figure.py*

- (1) Point $P$ moves slower than point $Q$
- **(2)** Point $P$ moves faster than point $Q$
- (3) Both the points $P$ and $Q$ move with equal speed
- (4) Point $P$ has zero speed

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Rolling without slipping on a level road gives $v = \omega R$.
2. Top point: $v_P = v + \omega R = 2v$.
3. Lowest (contact) point: $v_Q = v - \omega R = 0$.
4. $v_P = 2v > v_Q = 0$, so $P$ moves faster than $Q$, which is option $2$.

**Subtopic:** Rolling Motion · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 9)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q035_1d7f3980_12112026.png?v=1d7f39808e0a)

---

## Q36

Physics · Electromagnetic Waves

A parallel plate capacitor is charged by connecting it to a battery through a resistor. If $I$ is the current in the circuit, then in the gap between the plates:

- (1) There is no current
- **(2)** Displacement current of magnitude equal to $I$ flows in the same direction as $I$
- (3) Displacement current of magnitude equal to $I$ flows in a direction opposite to that of $I$
- (4) Displacement current of magnitude greater than $I$ flows but can be in any direction

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In the gap, $E = \frac{q}{\varepsilon_0 A}$, so $\Phi_E = EA = \frac{q}{\varepsilon_0}$.
2. $I_d = \varepsilon_0 \frac{d\Phi_E}{dt} = \frac{dq}{dt} = I$.
3. While charging, $E$ grows in the direction of conduction current flow, so $I_d$ is in the same direction as $I$: option $2$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 10)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q036_7eb1c51f_12112026.png?v=7eb1c51f1c9b)

---

## Q37

Physics · Electromagnetic Waves

The property which is not of an electromagnetic wave travelling in free space is that:

- (1) They are transverse in nature
- (2) The energy density in electric field is equal to energy density magnetic field
- (3) They travel with a speed equal to $\frac{1}{\sqrt{\mu_0 \varepsilon_0}}$
- **(4)** They originate from charges moving with uniform speed

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Charges moving with uniform velocity produce steady currents and static fields; only accelerated or oscillating charges radiate EM waves, so statement 1 is false.
2. EM waves are transverse ($\vec E \perp \vec B \perp \vec k$), $u_E = \frac{1}{2}\varepsilon_0 E^2 = \frac{B^2}{2\mu_0} = u_B$, and $c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}$, so options 1, 2, 3 are true; the answer is option $4$.

**Subtopic:** Electromagnetic Waves and Their Characteristics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 10)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q037_173fc6b8_12112026.png?v=173fc6b8c5a6)

---

## Q38

Physics · Ray Optics

A small telescope has an objective of focal length $140\,\mathrm{cm}$ and an eye piece of focal length $5.0\,\mathrm{cm}$. The magnifying power of telescope for viewing a distant object is:

- (1) $34$
- **(2)** $28$
- (3) $17$
- (4) $32$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For a distant object viewed in normal adjustment, the magnifying power of a telescope is $m = \frac{f_o}{f_e}$.
2. $m = \frac{140\,\mathrm{cm}}{5.0\,\mathrm{cm}} = 28$, which is option $2$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 10)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q038_18cb76a2_12112026.png?v=18cb76a21f97)

---

## Q39

Physics · Current Electricity

Two heaters A and B have power rating of $1\,\mathrm{kW}$ and $2\,\mathrm{kW}$, respectively. Those two are first connected in series and then in parallel to a fixed power source. The ratio of power outputs for these two cases is:

- (1) $1 : 1$
- **(2)** $2 : 9$
- (3) $1 : 2$
- (4) $2 : 3$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. At the rated voltage $V$, each heater has resistance $R = \frac{V^2}{P}$, so $R_A = \frac{V^2}{1\,\mathrm{kW}}$ and $R_B = \frac{V^2}{2\,\mathrm{kW}}$.
2. In series, $R_s = R_A + R_B$, so $P_s = \frac{V^2}{R_A + R_B} = \frac{1}{\frac{1}{1} + \frac{1}{2}}\,\mathrm{kW} = \frac{2}{3}\,\mathrm{kW}$.
3. In parallel, each heater gets the full voltage, so $P_p = 1 + 2 = 3\,\mathrm{kW}$.
4. $\frac{P_s}{P_p} = \frac{2/3}{3} = \frac{2}{9}$, so the ratio is $2 : 9$, which is option $2$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q039_c5ff2eba_12112026.png?v=c5ff2ebaaead)

---

## Q40

Physics · Thermodynamics

The following graph represents the T-V curves of an ideal gas (where $T$ is the temperature and $V$ the volume) at three pressures $P_1$, $P_2$ and $P_3$ compared with those of Charles’s law represented as dotted lines. Then the correct relation is:

![printed figure: T-V curves of an ideal gas at pressures P1, P2, P3 with dotted Charles's law lines](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q040_51717f62_12112026.png?v=51717f628fdb)

*T-V curves of an ideal gas at pressures P1, P2, P3 with dotted Charles's law lines*

![drawn: T-V curves of an ideal gas at pressures P1, P2, P3 with dotted Charles's law lines](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q040_question_221d860d_14112026.svg?v=221d860d3542)  
*drawn by code/lib/physics_figure.py*

- (1) $P_3 > P_2 > P_1$
- (2) $P_1 > P_3 > P_2$
- (3) $P_2 > P_1 > P_3$
- **(4)** $P_1 > P_2 > P_3$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Ideal gas law: $PV = nRT \Rightarrow T = \frac{P}{nR}V$.
2. At constant $P$, the $T$-$V$ (Charles's law) line has slope $\frac{P}{nR}$, so a steeper line means a higher pressure.
3. From the figure, the $P_1$ line is steepest, then $P_2$, and $P_3$ is flattest.
4. Hence $P_1 > P_2 > P_3$, which is option $4$.

**Subtopic:** Gas Laws, Problems on Different Graphs of P, V, and T · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q040_0ba540a6_12112026.png?v=0ba540a6e361)

---

## Q41

Physics · Kinematics

The velocity $(v)$ – time $(t)$ plot of the motion of a body is shown below: The acceleration $(a)$ – time $(t)$ graph that best suits this motion is :

![printed figure: Velocity-time graph: trapezoid (rise, constant, fall)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q041_7e9f46b4_12112026.png?v=7e9f46b4a05e)

*Velocity-time graph: trapezoid (rise, constant, fall)*

![drawn: Velocity-time graph: trapezoid (rise, constant, fall)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q041_question_a7efad6b_14112026.svg?v=a7efad6b6186)  
*drawn by code/lib/physics_figure.py*

- (1) ![printed figure: Acceleration-time graph: a raised trapezoidal pulse above the t-axis](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q041_option_1_b85ca383_12112026.png?v=b85ca383c4d2) *Acceleration-time graph: a raised trapezoidal pulse above the t-axis* ![drawn: Acceleration-time graph: a raised trapezoidal pulse above the t-axis](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q041_option_1_d8a340ff_14112026.svg?v=d8a340ffa959)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q041_option_2_d0cb8fe0_12112026.png?v=d0cb8fe01e74) *Acceleration-time graph: zero, then rising linearly, then constant* ![drawn: Acceleration-time graph: zero, then rising linearly, then constant](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q041_option_2_3b40d710_14112026.svg?v=3b40d71055bd)  
*drawn by code/lib/physics_figure.py*
- **(3)** ![printed figure: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q041_option_3_75ca86f7_12112026.png?v=75ca86f78dd2) *Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse* ![drawn: Acceleration-time graph: a positive rectangular pulse followed by a negative rectangular pulse](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q041_option_3_883865b0_14112026.svg?v=883865b0dfd3)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Option 4: a-t graph, zero, then a negative rectangular pulse, then a rising straight line](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q041_option_4_1f6a456c_12112026.png?v=1f6a456c3eeb) *Option 4: a-t graph, zero, then a negative rectangular pulse, then a rising straight line* ![drawn: Option 4: a-t graph, zero, then a negative rectangular pulse, then a rising straight line](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q041_option_4_6c247a11_14112026.svg?v=6c247a11bf02)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Acceleration is the slope of the $v$-$t$ graph: $a = \frac{dv}{dt}$.
2. Initial segment with $v = 0$ is flat, so $a = 0$.
3. Rising straight line has constant positive slope, so $a = +\text{const}$ (positive rectangle).
4. Horizontal segment has zero slope, so $a = 0$.
5. Falling straight line has constant negative slope, so $a = -\text{const}$ (negative rectangle).
6. The sequence $0, +a, 0, -a$ matches option $3$.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q041_6f6191cf_12112026.png?v=6f6191cf7e80)

---

## Q42

Physics · Current Electricity

> ⚠ With the printed arm values (10, 10, 15 and 5 ohm) no circuit balances for an ideal diode. The booklet keys (1) and its own solution balances it only by giving the forward-biased diode a "dynamic resistance" R_D = 10 ohm (10/15 = 10/(5 + R_D)), a value the question never states. Another reading takes a reverse-biased diode as an open arm. The key is the same question's key in every 2024 booklet code.

Choose the correct circuit which can achieve the bridge balance.

- **(1)** ![printed figure: Wheatstone bridge: 10 ohm, 10 ohm, 15 ohm, 5 ohm with diode D, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q042_option_1_0c9238f6_12112026.png?v=0c9238f65e34) *Wheatstone bridge: 10 ohm, 10 ohm, 15 ohm, 5 ohm with diode D, galvanometer G, cell E and key K* ![drawn: Wheatstone bridge: 10 ohm, 10 ohm, 15 ohm, 5 ohm with diode D, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q042_option_1_7698f31d_14112026.svg?v=7698f31d0c0f)  
*drawn by code/lib/physics_figure.py* — [circuit diagram]
- (2) ![printed figure: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and diode plus 5 ohm arms, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q042_option_2_64882aa7_12112026.png?v=64882aa7c5ed) *Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and diode plus 5 ohm arms, galvanometer G, cell E and key K* ![drawn: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm and diode plus 5 ohm arms, galvanometer G, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q042_option_2_142c6096_14112026.svg?v=142c60969b3f)  
*drawn by code/lib/physics_figure.py* — [circuit diagram]
- (3) ![printed figure: Bridge with 10 Ω, 10 Ω, 15 Ω arms, galvanometer G, and a diode D in parallel with 5 Ω; cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q042_option_3_671a2be5_12112026.png?v=671a2be520b7) *Bridge with 10 Ω, 10 Ω, 15 Ω arms, galvanometer G, and a diode D in parallel with 5 Ω; cell E and key K* ![drawn: Bridge with 10 Ω, 10 Ω, 15 Ω arms, galvanometer G, and a diode D in parallel with 5 Ω; cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q042_option_3_b4e6684f_14112026.svg?v=b4e6684f3aa2)  
*drawn by code/lib/physics_figure.py* — [circuit diagram]
- (4) ![printed figure: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm, 5 ohm, galvanometer G across the middle, diode D in the lower-right arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q042_option_4_17bd4e10_12112026.png?v=17bd4e1088f0) *Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm, 5 ohm, galvanometer G across the middle, diode D in the lower-right arm, cell E and key K* ![drawn: Wheatstone bridge with 10 ohm, 10 ohm, 15 ohm, 5 ohm, galvanometer G across the middle, diode D in the lower-right arm, cell E and key K](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q042_option_4_93be500c_14112026.svg?v=93be500cb56e)  
*drawn by code/lib/physics_figure.py* — [circuit diagram]

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Arms: $P = 10\,\Omega$ (top-left), $Q = 10\,\Omega$ (top-right), $R = 15\,\Omega$ (bottom-left), $S$ = bottom-right arm containing $5\,\Omega$ and diode $D$.
2. Balance condition: $\frac{P}{Q} = \frac{R}{S} \Rightarrow \frac{10}{10} = \frac{15}{S} \Rightarrow S = 15\,\Omega$.
3. So the bottom-right arm must conduct and have resistance $15\,\Omega$: $5 + r_D = 15 \Rightarrow r_D = 10\,\Omega$, i.e. a forward-biased diode in series with $5\,\Omega$.
4. In options 1, 2, 3 the long plate (positive) of $E$ is on the left, so current flows left node $\to$ bottom node $\to$ right node in the lower arms; in option 4 the battery is reversed.
5. Option 1: diode points from the bottom node toward the right node, so it is forward biased and in series with $5\,\Omega$; balance is possible with $r_D = 10\,\Omega$.
6. Option 2: diode points the other way, so it is reverse biased; the arm is open and current flows through $G$ via the $15\,\Omega$ arm, no balance.
7. Option 4: diode as in option 1 but battery reversed, so it is reverse biased; no balance.
8. Option 3: diode in parallel with $5\,\Omega$ gives $S \le 5\,\Omega \ne 15\,\Omega$; no balance.
9. Hence the answer is option $1$.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 11)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q042_60edd79e_12112026.png?v=60edd79e2a09)

---

## Q43

Physics · Oscillations

If the mass of the bob in a simple pendulum is increased to thrice its original mass and its length is made half its original length, then the new time period of oscillation is $\frac{x}{2}$ times its original time period. Then the value of $x$ is:

- (1) $\sqrt{3}$
- **(2)** $\sqrt{2}$
- (3) $2\sqrt{3}$
- (4) $4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $T = 2\pi\sqrt{\frac{l}{g}}$ is independent of the bob's mass, so tripling the mass has no effect.
2. $T' = 2\pi\sqrt{\frac{l/2}{g}} = \frac{T}{\sqrt{2}}$.
3. $\frac{T}{\sqrt{2}} = \frac{\sqrt{2}}{2}T = \frac{x}{2}T \Rightarrow x = \sqrt{2}$, which is option $2$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 11)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q043_f7f3ea15_12112026.png?v=f7f3ea155e65)

---

## Q44

Physics · Gravitation

The minimum energy required to launch a satellite of mass $m$ from the surface of earth of mass $M$ and radius $R$ in a circular orbit at an altitude of $2R$ from the surface of the earth is:

- **(1)** $\frac{5GmM}{6R}$
- (2) $\frac{2GmM}{3R}$
- (3) $\frac{GmM}{2R}$
- (4) $\frac{GmM}{3R}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Orbit radius from the centre: $r = R + 2R = 3R$.
2. Total energy in circular orbit: $E_{orbit} = -\frac{GMm}{2r} = -\frac{GMm}{6R}$.
3. Energy at rest on the surface: $E_{surface} = -\frac{GMm}{R}$.
4. $E_{min} = E_{orbit} - E_{surface} = -\frac{GMm}{6R} + \frac{GMm}{R} = \frac{5GMm}{6R}$, which is option $1$.

**Subtopic:** Motion of a Satellite · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 12)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q044_13d64378_12112026.png?v=13d64378f11a)

---

## Q45

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

**Solved independently** (answer withheld)

1. A magnetic sheet is attracted by the strong pole, so a force $\vec F_{\text{hold}} = -\vec F_{\text{mag}}$ is needed to hold it: A is true.
2. A non-magnetic sheet feels no magnetic force at rest, so $\vec F_{\text{net}} = 0$ without any applied force: B is false.
3. A conducting sheet moving in the non-uniform field has changing flux $\frac{d\Phi}{dt} \neq 0$, so eddy currents are induced.
4. By Lenz's law the eddy currents oppose the motion, so an applied force is needed to keep $v$ uniform: C is true.
5. A non-conducting, non-polar sheet has no induced currents and no magnetic force, so uniform velocity needs $F = 0$: D is false.
6. True statements are $A$ and $C$, which is option $2$.

**Subtopic:** Eddy Currents · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q045_d1de21fc_12112026.png?v=d1de21fcbb8f)

---

## Q46

Physics · Alternating Current

A $10\,\mu\mathrm{F}$ capacitor is connected to a $210\,\mathrm{V}$, $50\,\mathrm{Hz}$ source as shown in figure. The peak current in the circuit is nearly ($\pi = 3.14$):

![printed figure: A 10 uF capacitor C connected across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q046_5f32f509_12112026.png?v=5f32f5091d09)

*A 10 uF capacitor C connected across a 210 V, 50 Hz AC source in one loop*

![drawn: A 10 uF capacitor C connected across a 210 V, 50 Hz AC source in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q046_question_8e37b3fe_14112026.svg?v=8e37b3fe07fa)  
*drawn by code/lib/physics_figure.py*

- (1) $0.58\,\mathrm{A}$
- **(2)** $0.93\,\mathrm{A}$
- (3) $1.20\,\mathrm{A}$
- (4) $0.35\,\mathrm{A}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Capacitive reactance: $X_C = \frac{1}{2\pi f C} = \frac{1}{2 \times 3.14 \times 50 \times 10 \times 10^{-6}} = \frac{1}{3.14 \times 10^{-3}} \approx 318.5\,\Omega$.
2. The 210 V is the rms value, so $I_{rms} = \frac{V_{rms}}{X_C} = \frac{210}{318.5} \approx 0.659\,\mathrm{A}$.
3. Peak current $I_0 = \sqrt{2}\, I_{rms} = 1.414 \times 0.659 \approx 0.93\,\mathrm{A}$, which is option $2$.

**Subtopic:** AC Voltage Applied to a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q046_55a6f107_12112026.png?v=55a6f107029c)

---

## Q47

Physics · Mechanical Properties of Solids

A metallic bar of Young’s modulus, $0.5 \times 10^{11}\,\mathrm{N\,m^{-2}}$ and coefficient of linear thermal expansion $10^{-5}\,{}^{\circ}\mathrm{C}^{-1}$, length $1\,\mathrm{m}$ and area of cross-section $10^{-3}\,\mathrm{m^2}$ is heated from $0^{\circ}\mathrm{C}$ to $100^{\circ}\mathrm{C}$ without expansion or bending. The compressive force developed in it is :

- (1) $5 \times 10^{3}\,\mathrm{N}$
- **(2)** $50 \times 10^{3}\,\mathrm{N}$
- (3) $100 \times 10^{3}\,\mathrm{N}$
- (4) $2 \times 10^{3}\,\mathrm{N}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Prevented expansion gives thermal strain $\varepsilon = \alpha \Delta T = 10^{-5} \times 100 = 10^{-3}$.
2. Stress $\sigma = Y \varepsilon = 0.5 \times 10^{11} \times 10^{-3} = 0.5 \times 10^{8}\,\mathrm{N\,m^{-2}}$.
3. $F = \sigma A = 0.5 \times 10^{8} \times 10^{-3} = 5 \times 10^{4}\,\mathrm{N} = 50 \times 10^{3}\,\mathrm{N}$, which is option $2$.

**Subtopic:** Thermal Stress and Strain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q047_3509e768_12112026.png?v=3509e768b70b)

---

## Q48

Physics · Magnetic Effect of Electric Current

An iron bar of length $L$ has magnetic moment $M$. It is bent at the middle of its length such that the two arms make an angle $60^\circ$ with each other. The magnetic moment of this new magnet is :

- (1) $M$
- **(2)** $\frac{M}{2}$
- (3) $2M$
- (4) $\frac{M}{\sqrt{3}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Original moment: $M = m L$, where $m$ is the pole strength.
2. Bending at the middle gives two arms of length $\frac{L}{2}$ with $60^\circ$ between them.
3. The two arms and the line joining the poles form an equilateral triangle, so the pole separation is $\frac{L}{2}$.
4. $M' = m \cdot \frac{L}{2} = \frac{M}{2}$, which is option $2$.

**Subtopic:** Permanent Magnet and the Bar Magnet · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q048_16121831_12112026.png?v=1612183153e5)

---

## Q49

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

**Solved independently** (answer withheld)

1. The capacitor stays connected to the battery, so $V$ is constant.
2. $C = \frac{\varepsilon_0 A}{d}$; decreasing $d$ makes $C$ increase, so C is true.
3. $Q = CV$ increases with $C$ at constant $V$, so A is true.
4. $U = \frac{1}{2}CV^2$ increases, so B (energy decreases) is false.
5. $\frac{Q}{V} = C$ changes (increases), so D is false.
6. $QV = CV^2$ increases, so E is true.
7. True statements are A, C and E, which is option $2$.

**Subtopic:** The Parallel Plate Capacitor, Energy Stored in a Capacitor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q049_0d739ede_12112026.png?v=0d739ede0aa6)

---

## Q50

Physics · Units and Measurements

A force defined by $F = \alpha t^{2} + \beta t$ acts on a particle at a given time $t$. The factor which is dimensionless, if $\alpha$ and $\beta$ are constants, is:

- (1) $\beta t/\alpha$
- **(2)** $\alpha t/\beta$
- (3) $\alpha\beta t$
- (4) $\alpha\beta/t$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Each term must have the dimensions of force: $[\alpha t^{2}] = [F]$, so $[\alpha] = [F]\,T^{-2}$.
2. Likewise $[\beta t] = [F]$, so $[\beta] = [F]\,T^{-1}$.
3. $\left[\frac{\alpha t}{\beta}\right] = \frac{[F]\,T^{-2}\cdot T}{[F]\,T^{-1}} = 1$, dimensionless, which is option $2$.

**Subtopic:** Homogeneity of Dimensions in an Equation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q050_0d52220e_12112026.png?v=0d52220ed429)

---

## Q51

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.
List I (Molecule) | List II (Number and types of bond/s between two carbon atoms)
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | ethane | I | one $\sigma$-bond and two $\pi$-bonds |
| B | ethene | II | two $\pi$-bonds |
| C | carbon molecule, $\mathrm{C_2}$ | III | one $\sigma$-bonds |
| D | ethyne | IV | one $\sigma$-bond and one $\pi$-bond |

- (1) A-I, B-IV, C-II, D-III
- (2) A-IV, B-III, C-II, D-I
- **(3)** A-III, B-IV, C-II, D-I
- (4) A-III, B-IV, C-I, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Ethane has a $\mathrm{C-C}$ single bond: one $\sigma$-bond, so A-III.
2. Ethene has a $\mathrm{C=C}$ double bond: one $\sigma$-bond and one $\pi$-bond, so B-IV.
3. In $\mathrm{C_2}$ (MO configuration $\sigma 1s^2\,\sigma^*1s^2\,\sigma 2s^2\,\sigma^*2s^2\,(\pi 2p_x^2 = \pi 2p_y^2)$), bond order $2$ comes from two $\pi$-bonds, so C-II.
4. Ethyne has a $\mathrm{C\equiv C}$ triple bond: one $\sigma$-bond and two $\pi$-bonds, so D-I.
5. A-III, B-IV, C-II, D-I matches option $3$.

**Subtopic:** Molecular Orbital Theory, Orbital Overlap Concept · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q051_a54404ab_12112026.png?v=a54404aba500)

---

## Q52

Chemistry · physical · Solutions

The Henry's law constant ($K_{\mathrm{H}}$) values of three gases (A, B, C) in water are $145$, $2 \times 10^{-5}$ and $35\,\mathrm{kbar}$, respectively. The solubility of these gases in water follow the order:

- (1) B $>$ A $>$ C
- **(2)** B $>$ C $>$ A
- (3) A $>$ C $>$ B
- (4) A $>$ B $>$ C

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Henry's law: $p = K_\mathrm{H}\,x$, so at a given pressure $x = \frac{p}{K_\mathrm{H}}$ and solubility $\propto \frac{1}{K_\mathrm{H}}$.
2. Order of constants: $K_\mathrm{H}(B) = 2\times10^{-5} < K_\mathrm{H}(C) = 35 < K_\mathrm{H}(A) = 145\,\mathrm{kbar}$.
3. Hence solubility order is $B > C > A$, which is option $2$.

**Subtopic:** Solubility of a Gas in a Liquid · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 14)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q052_86ba9afd_12112026.png?v=86ba9afd5bd2)

---

## Q53

Chemistry · inorganic · The p–Block Elements

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) The boiling point of hydrides of Group 16 elements follow the order $\mathrm{H_2O} > \mathrm{H_2Te} > \mathrm{H_2Se} > \mathrm{H_2S}$.
- (Statement II) On the basis of molecular mass, $\mathrm{H_2O}$ is expected to have lower boiling point than the other members of the group but due to the presence of extensive H-bonding in $\mathrm{H_2O}$, it has higher boiling point.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Among $\mathrm{H_2S}$, $\mathrm{H_2Se}$, $\mathrm{H_2Te}$ boiling point rises with molecular mass (stronger van der Waals forces): $\mathrm{H_2Te} > \mathrm{H_2Se} > \mathrm{H_2S}$.
2. $\mathrm{H_2O}$ has the highest boiling point ($373\,\mathrm{K}$) because of extensive intermolecular hydrogen bonding, so the order $\mathrm{H_2O} > \mathrm{H_2Te} > \mathrm{H_2Se} > \mathrm{H_2S}$ holds and Statement I is true.
3. By molecular mass alone $\mathrm{H_2O}$ (lightest) would be expected to boil lowest; H-bonding explains its higher boiling point, so Statement II is true.
4. Both statements are true, which is option $1$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q053_308f3680_12112026.png?v=308f36800172)

---

## Q54

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Intramolecular hydrogen bonding is present in

- **(1)** 2-nitrophenol `O=[N+]([O-])c1ccccc1O` ![2-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q054_option_1_s1_af8d6416_14112026.svg?v=af8d641635dd)
- (2) 4-nitrophenol `O=[N+]([O-])c1ccc(O)cc1` ![4-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q054_option_2_s1_061f32a8_14112026.svg?v=061f32a8ba54)
- (3) 3-nitrophenol `O=[N+]([O-])c1cccc(O)c1` ![3-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q054_option_3_s1_683e3fc0_14112026.svg?v=683e3fc063ee)
- (4) $\mathrm{HF}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Intramolecular hydrogen bonding needs the H-bond donor ($-\mathrm{OH}$) and acceptor ($-\mathrm{NO_2}$) close together in the same molecule.
2. In option $1$ (o-nitrophenol) the $-\mathrm{OH}$ and $-\mathrm{NO_2}$ are on adjacent carbons, giving an $\mathrm{O{-}H\cdots O{=}N}$ six-membered ring: intramolecular H-bond.
3. In options $2$ (p-nitrophenol) and $3$ (m-nitrophenol) the groups are too far apart, so only intermolecular H-bonding occurs.
4. $\mathrm{HF}$ (option $4$) forms intermolecular $\mathrm{H{-}F\cdots H{-}F}$ chains, not intramolecular bonds, so the answer is option $1$.

**Subtopic:** Hydrogen Bonding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q054_c92bd25c_12112026.png?v=c92bd25c35ab)

---

## Q55

Chemistry · organic · Hydrocarbons

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The boiling point of three isomeric pentanes follows the order n-pentane $>$ isopentane $>$ neopentane
- (Statement II) When branching increases, the molecule attains a shape of sphere. This results in smaller surface area for contact, due to which the intermolecular forces between the spherical molecules are weak, thereby lowering the boiling point.

- **(1)** Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- (3) Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: b.p. of n-pentane ($309\,K$) $>$ isopentane ($301\,K$) $>$ neopentane ($282.5\,K$), so Statement I is correct.
2. Statement II: more branching makes the molecule nearly spherical, reducing contact surface area and weakening van der Waals forces, which lowers the boiling point; Statement II is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Physical Properties of Alkanes, Alkenes and Alkynes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q055_82f24bea_12112026.png?v=82f24bea1ba6)

---

## Q56

Chemistry · organic · Haloalkanes and Haloarenes

The compound that will undergo $\mathrm{S_N1}$ reaction with the fastest rate is

- (1) (bromomethyl)cyclohexane `BrCC1CCCCC1` ![(bromomethyl)cyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q056_option_1_s1_3db34c76_14112026.svg?v=3db34c76f38e)
- (2) bromocyclohexane `BrC1CCCCC1` ![bromocyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q056_option_2_s1_35c4a4b9_14112026.svg?v=35c4a4b9cb53)
- (3) bromobenzene `Brc1ccccc1` ![bromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q056_option_3_s1_61d2ed9e_14112026.svg?v=61d2ed9ebe04)
- **(4)** (1-bromoethyl)benzene `CC(Br)c1ccccc1` ![(1-bromoethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q056_option_4_s1_ef3a803b_14112026.svg?v=ef3a803b5361)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\mathrm{S_N1}$ rate depends on the stability of the carbocation formed in the slow ionisation step.
2. Option 1 ($\mathrm{C_6H_{11}CH_2Br}$) gives a primary carbocation $\mathrm{C_6H_{11}CH_2^+}$, which is poorly stabilised.
3. Option 2 (bromocyclohexane) gives a secondary cyclohexyl carbocation, stabilised only by hyperconjugation and $+I$ effect.
4. Option 3 (bromobenzene) would give an aryl cation on an $sp^2$ carbon; the C-Br bond has partial double-bond character, so it does not undergo $\mathrm{S_N1}$.
5. Option 4 ($\mathrm{C_6H_5CH(Br)CH_3}$) gives the secondary benzylic cation $\mathrm{C_6H_5\overset{+}{C}HCH_3}$, delocalised into the ring by resonance and also stabilised by hyperconjugation from $\mathrm{CH_3}$.
6. Stability order $4 > 2 > 1 > 3$, so option $4$ reacts fastest.

**Subtopic:** Reactions of Haloalkanes – Nucleophilic Substitution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q056_9ac14e8c_12112026.png?v=9ac14e8cade3)

---

## Q57

Chemistry · organic · Alcohols, Phenols and Ethers

Which one of the following alcohols reacts instantaneously with Lucas reagent?

- (1) $\mathrm{CH_3-CH_2-CH_2-CH_2OH}$
- (2) butan-2-ol `CCC(C)O` ![butan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q057_option_2_s1_246d1e4e_14112026.svg?v=246d1e4e3f48) — $\mathrm{CH_3-CH_2-CH(CH_3)-OH}$
- (3) 2-methylpropan-1-ol `CC(C)CO` ![2-methylpropan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q057_option_3_s1_44b6a2e7_14112026.svg?v=44b6a2e7f8a5) — $\mathrm{CH_3-CH(CH_3)-CH_2OH}$
- **(4)** 2-methylpropan-2-ol `CC(C)(C)O` ![2-methylpropan-2-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q057_option_4_s1_51170735_14112026.svg?v=51170735efa7) — $\mathrm{CH_3-C(CH_3)_2-OH}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Lucas reagent (conc. $\mathrm{HCl} + \mathrm{ZnCl_2}$) reacts via a carbocation, so the rate order is $3^\circ > 2^\circ > 1^\circ$ alcohol.
2. Option $1$ ($\mathrm{CH_3CH_2CH_2CH_2OH}$) and option $3$ ($\mathrm{(CH_3)_2CHCH_2OH}$) are $1^\circ$; option $2$ (butan-2-ol) is $2^\circ$.
3. Option $4$, $\mathrm{(CH_3)_3C-OH}$, is $3^\circ$ and gives turbidity instantly, so the answer is option $4$.

**Subtopic:** Test of Alcohol · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 16)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q057_5ab59232_12112026.png?v=5ab592327b25)

---

## Q58

Chemistry · physical · Basic Concepts of Chemistry

$1\,\mathrm{gram}$ of sodium hydroxide was treated with $25\,\mathrm{mL}$ of $0.75\,\mathrm{M}$ $\mathrm{HCl}$ solution, the mass of sodium hydroxide left unreacted is equal to

- (1) $750\,\mathrm{mg}$
- **(2)** $250\,\mathrm{mg}$
- (3) Zero $\mathrm{mg}$
- (4) $200\,\mathrm{mg}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $n_{\mathrm{NaOH}} = \frac{1\,\mathrm{g}}{40\,\mathrm{g\,mol^{-1}}} = 0.025\,\mathrm{mol}$.
2. $n_{\mathrm{HCl}} = 0.025\,\mathrm{L} \times 0.75\,\mathrm{M} = 0.01875\,\mathrm{mol}$.
3. $\mathrm{NaOH} + \mathrm{HCl} \rightarrow \mathrm{NaCl} + \mathrm{H_2O}$ reacts $1:1$, so HCl is limiting.
4. Unreacted $n_{\mathrm{NaOH}} = 0.025 - 0.01875 = 0.00625\,\mathrm{mol}$.
5. Mass left $= 0.00625 \times 40 = 0.25\,\mathrm{g} = 250\,\mathrm{mg}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 16)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q058_b69e1bf8_12112026.png?v=b69e1bf8ffad)

---

## Q59

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of first ionization enthalpy: $\mathrm{Li}$, $\mathrm{Be}$, $\mathrm{B}$, $\mathrm{C}$, $\mathrm{N}$ Chose the correct answer from the options given below:

- (1) $\mathrm{Li} < \mathrm{Be} < \mathrm{B} < \mathrm{C} < \mathrm{N}$
- **(2)** $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$
- (3) $\mathrm{Li} < \mathrm{Be} < \mathrm{C} < \mathrm{B} < \mathrm{N}$
- (4) $\mathrm{Li} < \mathrm{Be} < \mathrm{N} < \mathrm{B} < \mathrm{C}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Across period 2, first ionization enthalpy generally increases with increasing nuclear charge, so $\mathrm{Li}$ is lowest and $\mathrm{N}$ is highest among these.
2. $\mathrm{Be}$ ($1s^2 2s^2$) has a fully filled, more penetrating $2s$ orbital, while $\mathrm{B}$ ($1s^2 2s^2 2p^1$) loses a $2p$ electron that is shielded by $2s$, so $\Delta_i H_1(\mathrm{B}) < \Delta_i H_1(\mathrm{Be})$.
3. $\mathrm{C} < \mathrm{N}$ since $\mathrm{N}$ has a stable half-filled $2p^3$ configuration and higher nuclear charge.
4. Order: $\mathrm{Li} < \mathrm{B} < \mathrm{Be} < \mathrm{C} < \mathrm{N}$, which is option $2$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q059_02ab182a_12112026.png?v=02ab182a9a8d)

---

## Q60

Chemistry · organic · General Organic Chemistry

The most stable carbocation among the following is :

- (1) 2-methylpentan-3-ylium `CC[CH+]C(C)C` ![2-methylpentan-3-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q060_option_1_s1_8a3210fb_14112026.svg?v=8a3210fb1a2a)
- (2) 4-methylpentan-2-ylium `C[CH+]CC(C)C` ![4-methylpentan-2-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q060_option_2_s1_34ac5544_14112026.svg?v=34ac5544f031)
- (3) cyclopentylmethylium `[CH2+]C1CCCC1` ![cyclopentylmethylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q060_option_3_s1_8adbcb30_14112026.svg?v=8adbcb30ef6b)
- **(4)** 1-methylcyclohexylium `C[C+]1CCCCC1` ![1-methylcyclohexylium](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q060_option_4_s1_6a144549_14112026.svg?v=6a1445496db4)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{CH_3CH_2\overset{+}{C}H-CH(CH_3)_2}$ has the positive carbon bonded to two carbons, a $2^\circ$ carbocation.
2. Option 2: $\mathrm{CH_3\overset{+}{C}H-CH_2-CH(CH_3)_2}$ is also a $2^\circ$ carbocation.
3. Option 3: $\mathrm{C_5H_9-\overset{+}{C}H_2}$ (cyclopentylmethyl) is a $1^\circ$ carbocation.
4. Option 4: the positive carbon of the ring also carries $\mathrm{CH_3}$, so it is bonded to three carbons, a $3^\circ$ carbocation.
5. Stability order $3^\circ > 2^\circ > 1^\circ$ (more hyperconjugation and $+I$), so option $4$ is the most stable.

**Subtopic:** Hyperconjugation · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 16)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q060_ef34a61a_12112026.png?v=ef34a61a7bc1)

---

## Q61

Chemistry · physical · Chemical Kinetics

Activation energy of any chemical reaction can be calculated if one knows the value of

- (1) rate constant at standard temperature
- (2) probability of collision
- (3) orientation of reactant molecules during collision
- **(4)** rate constant at two different temperatures

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$, with two unknowns $A$ and $E_a$.
2. Taking the ratio at two temperatures eliminates $A$: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. So $E_a = \frac{2.303\,R\,T_1 T_2 \log(k_2/k_1)}{T_2 - T_1}$ needs $k$ at two different temperatures, which is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 17)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q061_33975afb_12112026.png?v=33975afbaa4c)

---

## Q62

Chemistry · organic · Amines

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Aniline does not undergo Friedel-Crafts alkylation reaction.
- (Statement II) Aniline cannot be prepared through Gabriel synthesis.

- **(1)** Both statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is correct but Statement II is false
- (4) Statement I is incorrect but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Aniline's $-\mathrm{NH_2}$ is a Lewis base and reacts with the Lewis acid $\mathrm{AlCl_3}$ to form a salt, putting a positive charge on N that deactivates the ring, so aniline does not undergo Friedel-Crafts alkylation: Statement I is true.
2. Gabriel synthesis needs the phthalimide anion to attack an alkyl halide by nucleophilic substitution; aryl halides do not undergo this substitution, so aromatic primary amines such as aniline cannot be prepared this way: Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions), Methods of Preparation of Amines · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q062_af29081e_12112026.png?v=af29081e93f1)

---

## Q63

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Arrange the following elements in increasing order of electronegativity: $\mathrm{N}$, $\mathrm{O}$, $\mathrm{F}$, $\mathrm{C}$, $\mathrm{Si}$ Choose the correct answer from the options given below:

- **(1)** $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$
- (2) $\mathrm{Si} < \mathrm{C} < \mathrm{O} < \mathrm{N} < \mathrm{F}$
- (3) $\mathrm{O} < \mathrm{F} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$
- (4) $\mathrm{F} < \mathrm{O} < \mathrm{N} < \mathrm{C} < \mathrm{Si}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Across period 2, electronegativity increases left to right: $\mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$.
2. Down group 14, electronegativity decreases, so $\mathrm{Si} < \mathrm{C}$.
3. Combined order: $\mathrm{Si} < \mathrm{C} < \mathrm{N} < \mathrm{O} < \mathrm{F}$, which is option $1$.

**Subtopic:** Trends in Chemical Properties – Electronegativity and Electron Affinity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 17)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q063_3e6481a9_12112026.png?v=3e6481a93e07)

---

## Q64

Chemistry · physical · Electrochemistry

Match List I with List II.
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $1$ mol of $\mathrm{H_2O}$ to $\mathrm{O_2}$ | I | $3\,\mathrm{F}$ |
| B | $1$ mol of $\mathrm{MnO_4^-}$ to $\mathrm{Mn^{2+}}$ | II | $2\,\mathrm{F}$ |
| C | $1.5$ mol of Ca from molten $\mathrm{CaCl_2}$ | III | $1\,\mathrm{F}$ |
| D | $1$ mol of FeO to $\mathrm{Fe_2O_3}$ | IV | $5\,\mathrm{F}$ |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-I, D-IV
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A: $\mathrm{H_2O \rightarrow \tfrac{1}{2}O_2 + 2H^+ + 2e^-}$; oxygen goes from $-2$ to $0$, so $1$ mol needs $2\,\mathrm{F}$ (II).
2. B: In $\mathrm{MnO_4^-}$ Mn is $+7$; going to $\mathrm{Mn^{2+}}$ gains $5e^-$, so $1$ mol needs $5\,\mathrm{F}$ (IV).
3. C: $\mathrm{Ca^{2+} + 2e^- \rightarrow Ca}$, so $1.5$ mol needs $1.5 \times 2 = 3\,\mathrm{F}$ (I).
4. D: Fe in FeO is $+2$ and in $\mathrm{Fe_2O_3}$ is $+3$; $1$ mol loses $1e^-$ per Fe, so $1\,\mathrm{F}$ (III).
5. Match A-II, B-IV, C-I, D-III, which is option $1$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q064_37fe017c_12112026.png?v=37fe017cf83b)

---

## Q65

Chemistry · inorganic · Coordination Compounds – Practice

Match List I with List II.
List I (Complex) | List II (Type of isomerism)
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

**Solved independently** (answer withheld)

1. A: $\mathrm{NO_2^-}$ is ambidentate (binds through N or O), so $\mathrm{[Co(NH_3)_5(NO_2)]Cl_2}$ shows linkage isomerism: A-II.
2. B: $\mathrm{[Co(NH_3)_5(SO_4)]Br}$ and $\mathrm{[Co(NH_3)_5Br]SO_4}$ give different ions in solution, so ionization isomerism: B-III.
3. C: ligands can interchange between the two metal centres, $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ vs $\mathrm{[Cr(NH_3)_6][Co(CN)_6]}$, so coordination isomerism: C-IV.
4. D: water can be a ligand or lattice water, $\mathrm{[Co(H_2O)_6]Cl_3}$ vs $\mathrm{[Co(H_2O)_5Cl]Cl_2\cdot H_2O}$, so solvate (hydrate) isomerism: D-I.
5. A-II, B-III, C-IV, D-I matches option $1$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 18)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q065_640fc63c_12112026.png?v=640fc63c24d5)

---

## Q66

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II.

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

**Solved independently** (answer withheld)

1. $\mathrm{NH_3}$: 3 bond pairs + 1 lone pair on N, so it is trigonal pyramidal: A-I.
2. $\mathrm{BrF_5}$: 5 bond pairs + 1 lone pair on Br, so it is square pyramidal: B-IV.
3. $\mathrm{XeF_4}$: 4 bond pairs + 2 lone pairs on Xe, so it is square planar: C-II.
4. $\mathrm{SF_6}$: 6 bond pairs, no lone pair on S, so it is octahedral: D-III.
5. A-I, B-IV, C-II, D-III is option $1$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q066_b9c13379_12112026.png?v=b9c13379bff4)

---

## Q67

Chemistry · physical · Chemical Kinetics

Which plot of $\ln k$ vs $\frac{1}{T}$ is consistent with Arrhenius equation?

- (1) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope, starting slightly below the x-axis near the origin and rising to the upper right](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q067_option_1_ed20add2_12112026.png?v=ed20add23ba6) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope, starting slightly below the x-axis near the origin and rising to the upper right* — [graph: $\ln k$ vs $\frac{1}{T}$]
- (2) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope and a positive y-intercept, rising to the upper right](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q067_option_2_654c2f16_12112026.png?v=654c2f168e87) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope and a positive y-intercept, rising to the upper right* — [graph: $\ln k$ vs $\frac{1}{T}$]
- (3) ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope passing through the origin](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q067_option_3_8a56b608_12112026.png?v=8a56b6088716) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with positive slope passing through the origin* — [graph: $\ln k$ vs $\frac{1}{T}$]
- **(4)** ![printed figure: graph of ln k (y-axis) vs 1/T (x-axis): a straight line with negative slope, starting at a positive y-intercept and falling to meet the x-axis](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q067_option_4_04b7d768_12112026.png?v=04b7d7683446) *graph of ln k (y-axis) vs 1/T (x-axis): a straight line with negative slope, starting at a positive y-intercept and falling to meet the x-axis* — [graph: $\ln k$ vs $\frac{1}{T}$]

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Arrhenius equation: $k = A e^{-E_a/RT}$.
2. Taking logs: $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$.
3. This is linear in $\frac{1}{T}$ with slope $-\frac{E_a}{R} < 0$ and intercept $\ln A$ on the $\ln k$ axis.
4. Options $1$, $2$ and $3$ have positive slopes; only option $4$ shows a line falling from a positive intercept, so the answer is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 18)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q067_e4d52c3d_12112026.png?v=e4d52c3d0329)

---

## Q68

Chemistry · physical · Structure of Atom

The energy of an electron in the ground state $(n = 1)$ for $\mathrm{He^{+}}$ ion is $-x\,\mathrm{J}$, then that for an electron in $n = 2$ state for $\mathrm{Be^{3+}}$ ion in J is

- **(1)** $-x$
- (2) $-\dfrac{x}{9}$
- (3) $-4x$
- (4) $-\dfrac{4}{9}x$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For hydrogen-like species $E_n = -k\frac{Z^2}{n^2}$.
2. For $\mathrm{He^{+}}$, $n=1$: $E = -k\frac{2^2}{1^2} = -4k = -x$, so $k = \frac{x}{4}$.
3. For $\mathrm{Be^{3+}}$, $n=2$: $E = -k\frac{4^2}{2^2} = -4k$.
4. $-4k = -4 \times \frac{x}{4} = -x$, which is option $1$.

**Subtopic:** Bohr’s Model for Hydrogen Atom · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q068_837d271d_12112026.png?v=837d271db953)

---

## Q69

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

**Solved independently** (answer withheld)

1. A: evaporation changes liquid to vapour, so disorder increases and $\Delta S > 0$.
2. B: cooling a crystalline solid from $130\,\mathrm{K}$ to $0\,\mathrm{K}$ reduces molecular motion, so $\Delta S < 0$.
3. C: $\mathrm{2NaHCO_{3(s)} \rightarrow Na_2CO_{3(s)} + CO_{2(g)} + H_2O_{(g)}}$ gives $\Delta n_g = +2$, so $\Delta S > 0$.
4. D: $\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$ gives $\Delta n_g = +1$, so $\Delta S > 0$.
5. Entropy increases in A, C and D, which is option $3$.

**Subtopic:** Entropy, Second Law & Third Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q069_f48f27e5_12112026.png?v=f48f27e51fb7)

---

## Q70

Chemistry · physical · Redox Reactions

Which reaction is NOT a redox reaction?

- (1) $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$
- (2) $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$
- (3) $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$
- **(4)** $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In $\mathrm{BaCl_2 + Na_2SO_4 \rightarrow BaSO_4 + 2NaCl}$ the oxidation states stay $\mathrm{Ba}=+2$, $\mathrm{Cl}=-1$, $\mathrm{Na}=+1$, $\mathrm{S}=+6$, $\mathrm{O}=-2$ on both sides, so it is not redox.
2. In $\mathrm{Zn + CuSO_4 \rightarrow ZnSO_4 + Cu}$, $\mathrm{Zn}: 0 \rightarrow +2$ and $\mathrm{Cu}: +2 \rightarrow 0$, so it is redox.
3. In $\mathrm{2KClO_3 + I_2 \rightarrow 2KIO_3 + Cl_2}$, $\mathrm{I}: 0 \rightarrow +5$ and $\mathrm{Cl}: +5 \rightarrow 0$, so it is redox.
4. In $\mathrm{H_2 + Cl_2 \rightarrow 2HCl}$, $\mathrm{H}: 0 \rightarrow +1$ and $\mathrm{Cl}: 0 \rightarrow -1$, so it is redox.
5. Only option $4$ is not a redox reaction.

**Subtopic:** Oxidation Number · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q070_056d9c88_12112026.png?v=056d9c883ebf)

---

## Q71

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

**Solved independently** (answer withheld)

1. $m_l$ (magnetic quantum number) gives the orientation of the orbital: A-III; $m_s$ gives the orientation of electron spin: B-IV; $l$ (azimuthal) gives the shape of the orbital: C-I; $n$ (principal) gives the size of the orbital: D-II; so A-III, B-IV, C-I, D-II is option $2$.

**Subtopic:** Quantum Numbers · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q071_a93fe01e_12112026.png?v=a93fe01ecc24)

---

## Q72

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

**Solved independently** (answer withheld)

1. Spin-only moment $\mu = \sqrt{n(n+2)}\,\text{BM}$ depends only on the number of unpaired electrons $n$.
2. $\mathrm{Ti^{3+}}$: $3d^1$, $n=1$.
3. $\mathrm{Cr^{2+}}$: $3d^4$, $n=4$.
4. $\mathrm{Mn^{2+}}$: $3d^5$, $n=5$.
5. $\mathrm{Fe^{2+}}$: $3d^6$, $n=4$.
6. $\mathrm{Sc^{3+}}$: $3d^0$, $n=0$.
7. Only $\mathrm{Cr^{2+}}$ and $\mathrm{Fe^{2+}}$ share $n=4$, giving $\mu = \sqrt{24} \approx 4.90\,\text{BM}$ each, i.e. B and D, which is option $1$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q072_7221afd5_12112026.png?v=7221afd53231)

---

## Q73

Chemistry · physical · Basic Concepts of Chemistry

The highest number of helium atoms is in

- **(1)** $4\,\mathrm{mol}$ of helium
- (2) $4\,\mathrm{u}$ of helium
- (3) $4\,\mathrm{g}$ of helium
- (4) $2.271098\,\mathrm{L}$ of helium at STP

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Option 4: molar volume at STP is $22.71098\,\mathrm{L\,mol^{-1}}$, so $n = \frac{2.271098}{22.71098} = 0.1\,\mathrm{mol}$.
2. Option 1: $n = 4\,\mathrm{mol}$, i.e. $4N_A$ atoms.
3. Option 2: mass of one He atom is $4\,\mathrm{u}$, so $4\,\mathrm{u}$ is $1$ atom.
4. Option 3: $n = \frac{4\,\mathrm{g}}{4\,\mathrm{g\,mol^{-1}}} = 1\,\mathrm{mol}$, i.e. $N_A$ atoms.
5. Largest is $4\,\mathrm{mol}$, which is option $1$.

**Subtopic:** Mole Concept · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 20)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q073_2aced039_12112026.png?v=2aced039e697)

---

## Q74

Chemistry · inorganic · The p–Block Elements

Among Group 16 elements, which one does NOT show $-2$ oxidation state?

- (1) $\mathrm{O}$
- (2) $\mathrm{Se}$
- (3) $\mathrm{Te}$
- **(4)** $\mathrm{Po}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Down Group 16, stability of the $-2$ oxidation state decreases as metallic character increases; $\mathrm{O}$, $\mathrm{Se}$ and $\mathrm{Te}$ show $-2$, while $\mathrm{Po}$ hardly shows it, so the answer is option $4$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 20)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q074_369dca2c_12112026.png?v=369dca2c6f61)

---

## Q75

Chemistry · inorganic · The D- and F-Block Elements – Practice

The $E^\circ$ value for the $\mathrm{Mn^{3+}/Mn^{2+}}$ couple is more positive than that of $\mathrm{Cr^{3+}/Cr^{2+}}$ or $\mathrm{Fe^{3+}/Fe^{2+}}$ due to change of

- (1) $d^{5}$ to $d^{4}$ configuration
- (2) $d^{5}$ to $d^{2}$ configuration
- **(3)** $d^{4}$ to $d^{5}$ configuration
- (4) $d^{3}$ to $d^{5}$ configuration

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\mathrm{Mn^{3+}}$ is $[\mathrm{Ar}]\,3d^{4}$ and $\mathrm{Mn^{2+}}$ is $[\mathrm{Ar}]\,3d^{5}$.
2. Reduction $\mathrm{Mn^{3+}} + e^- \rightarrow \mathrm{Mn^{2+}}$ changes $d^{4}$ to the half-filled, extra-stable $d^{5}$, so $E^\circ$ is strongly positive.
3. The change is $d^{4} \rightarrow d^{5}$, which is option $3$.

**Subtopic:** Trends of Electrode Potentials · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q075_74a80bb5_12112026.png?v=74a80bb58224)

---

## Q76

Chemistry · organic · Biomolecules

The reagents with which glucose does **not** react to give the corresponding tests/products are
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

**Solved independently** (answer withheld)

1. Glucose reduces Tollens' reagent (silver mirror), so $\text{A}$ reacts.
2. Glucose adds $\mathrm{HCN}$ to give a cyanohydrin, so $\text{C}$ reacts.
3. Glucose condenses with $\mathrm{NH_2OH}$ to give an oxime, so $\text{D}$ reacts.
4. Despite having a $\mathrm{-CHO}$ group, glucose does not give Schiff's test and does not form the $\mathrm{NaHSO_3}$ addition product (evidence for its cyclic structure), so $\text{B}$ and $\text{E}$ do not react.
5. Non-reacting reagents are $\text{B}$ and $\text{E}$, which is option $3$.

**Subtopic:** Structure and Reactions of Glucose · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q076_c2312ba7_12112026.png?v=c2312ba7dc62)

---

## Q77

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Identify the correct reagents that would bring about the following transformation.

![printed figure: allylcyclohexane → 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q077_6cd2374c_12112026.png?v=6cd2374c4149)

*allylcyclohexane → 3-cyclohexylpropanal*

![drawn: allylcyclohexane → 3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q077_question_4ad0072e_14112026.svg?v=4ad0072e529b)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: allylcyclohexane `C=CCC1CCCCC1` ![allylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q077_question_s1_19da39bf_14112026.svg?v=19da39bfbc83); 3-cyclohexylpropanal `O=CCCC1CCCCC1` ![3-cyclohexylpropanal](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q077_question_s2_d5fc3230_14112026.svg?v=d5fc32301153)

- (1) (i) $\mathrm{H_2O/H^+}$ (ii) $\mathrm{CrO_3}$
- **(2)** (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2/\overset{\ominus}{O}H}$ (iii) PCC
- (3) (i) $\mathrm{BH_3}$ (ii) $\mathrm{H_2O_2/\overset{\ominus}{O}H}$ (iii) alk.$\mathrm{KMnO_4}$ (iv) $\mathrm{H_3O^{\oplus}}$
- (4) (i) $\mathrm{H_2O/H^+}$ (ii) PCC

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The product has $\mathrm{-CHO}$ on the terminal carbon, so the terminal alkene carbon must become a primary alcohol (anti-Markovnikov addition of water).
2. $\mathrm{H_2O/H^+}$ adds water by Markovnikov's rule, giving the secondary alcohol $\mathrm{C_6H_{11}CH_2CH(OH)CH_3}$, which would oxidise to a ketone; options $4$ and $1$ are ruled out.
3. $\mathrm{BH_3}$ then $\mathrm{H_2O_2/OH^-}$ gives $\mathrm{C_6H_{11}CH_2CH_2CH_2OH}$ (anti-Markovnikov).
4. PCC oxidises a primary alcohol only to the aldehyde: $\mathrm{C_6H_{11}CH_2CH_2CHO}$, which is option $2$.
5. Alkaline $\mathrm{KMnO_4}$ then $\mathrm{H_3O^+}$ would give the carboxylic acid, so option $3$ is wrong.

**Subtopic:** Preparation of Aldehydes · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 21)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q077_06afc42f_12112026.png?v=06afc42ffc71)

---

## Q78

Chemistry · physical · Chemical Equilibrium

In which of the following equilibria, $K_p$ and $K_c$ are NOT equal?

- **(1)** $\mathrm{PCl_{5(g)} \rightleftharpoons PCl_{3(g)} + Cl_{2(g)}}$
- (2) $\mathrm{H_{2(g)} + I_{2(g)} \rightleftharpoons 2HI_{(g)}}$
- (3) $\mathrm{CO_{(g)} + H_2O_{(g)} \rightleftharpoons CO_{2(g)} + H_{2(g)}}$
- (4) $\mathrm{2BrCl_{(g)} \rightleftharpoons Br_{2(g)} + Cl_{2(g)}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $K_p = K_c (RT)^{\Delta n_g}$, so $K_p \neq K_c$ only when $\Delta n_g \neq 0$.
2. Option 4: $\Delta n_g = (1+1) - 2 = 0$.
3. Option 1: $\Delta n_g = (1+1) - 1 = 1$.
4. Option 2: $\Delta n_g = 2 - (1+1) = 0$.
5. Option 3: $\Delta n_g = (1+1) - (1+1) = 0$.
6. Only option $1$ has $\Delta n_g \neq 0$, so $K_p = K_c RT \neq K_c$.

**Subtopic:** Homogeneous and Heterogeneous Equilibria · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 22)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q078_70cc096d_12112026.png?v=70cc096d6ec2)

---

## Q79

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

A compound with a molecular formula of $\mathrm{C_6H_{14}}$ has two tertiary carbons. Its IUPAC name is :

- (1) n-hexane
- (2) 2-methylpentane
- **(3)** 2,3-dimethylbutane
- (4) 2,2-dimethylbutane

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A tertiary carbon is bonded to exactly three other carbons.
2. $\mathrm{CH_3-CH(CH_3)-CH(CH_3)-CH_3}$ (2,3-dimethylbutane, $\mathrm{C_6H_{14}}$): $C_2$ and $C_3$ are each bonded to three carbons, so it has $2$ tertiary carbons.
3. 2-methylpentane has $1$ tertiary carbon ($C_2$); 2,2-dimethylbutane has $0$ (its $C_2$ is quaternary); n-hexane has $0$.
4. Only 2,3-dimethylbutane has two tertiary carbons, which is option $3$.

**Subtopic:** Acyclic or Open Chain Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q079_b3ca69d6_12112026.png?v=b3ca69d6c2df)

---

## Q80

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Fehling’s solution ‘A’ is

- **(1)** aqueous copper sulphate
- (2) alkaline copper sulphate
- (3) alkaline solution of sodium potassium tartrate (Rochelle’s salt)
- (4) aqueous sodium citrate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Fehling's reagent is prepared by mixing Fehling A (aqueous $\mathrm{CuSO_4}$) with Fehling B (alkaline sodium potassium tartrate), so Fehling A is option $1$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 22)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q080_6b7bb1b4_12112026.png?v=6b7bb1b426e3)

---

## Q81

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

- (1) A-IV, B-III, C-II, D-I
- (2) A-IV, B-II, C-III, D-I
- (3) A-I, B-II, C-III, D-IV
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Isothermal process is carried out at constant temperature: $A \to II$.
2. Isochoric process is carried out at constant volume: $B \to III$.
3. Isobaric process is carried out at constant pressure: $C \to IV$.
4. Adiabatic process involves no heat exchange ($\Delta Q = 0$): $D \to I$.
5. The matching $A\text{-}II, B\text{-}III, C\text{-}IV, D\text{-}I$ is option $4$.

**Subtopic:** Thermodynamic Processes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q081_dad0e89a_12112026.png?v=dad0e89a3bc8)

---

## Q82

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements : In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Both $\mathrm{[Co(NH_3)_6]^{3+}}$ and $\mathrm{[CoF_6]^{3-}}$ complexes are octahedral but differ in their magnetic behaviour.
- (Statement II) $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic whereas $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In both complexes cobalt is $\mathrm{Co^{3+}}$, configuration $3d^6$, with coordination number 6, so both are octahedral.
2. $\mathrm{NH_3}$ is a strong-field ligand: pairing gives $t_{2g}^6 e_g^0$ (inner-orbital $d^2sp^3$), 0 unpaired electrons, so $\mathrm{[Co(NH_3)_6]^{3+}}$ is diamagnetic.
3. $\mathrm{F^-}$ is a weak-field ligand: $t_{2g}^4 e_g^2$ (outer-orbital $sp^3d^2$), 4 unpaired electrons, so $\mathrm{[CoF_6]^{3-}}$ is paramagnetic.
4. Hence Statement I (same geometry, different magnetism) and Statement II are both true, which is option $1$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q082_f8201f0c_12112026.png?v=f8201f0c17ce)

---

## Q83

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

On heating, some solid substances change from solid to vapour state without passing through liquid state. The technique used for the purification of such solid substances based on the above principle is known as

- (1) Crystallization
- **(2)** Sublimation
- (3) Distillation
- (4) Chromatography

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A solid passing directly to vapour on heating, skipping the liquid state, is sublimation, so the purification technique is sublimation, option $2$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q083_99578aba_12112026.png?v=99578aba793e)

---

## Q84

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List I with List II. Choose the correct answer from the options given below:

![printed figure: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → benzophenone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q084_3ecb5ac6_12112026.svg?v=3ecb5ac65c8c)

*A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → benzophenone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$*

![drawn: A. cyclohexylidenecyclohexane → 2 cyclohexanone; B. benzene → benzophenone; C. cyclohexanol → cyclohexanone; D. ethylbenzene → potassium benzoate; I. benzoyl chloride/Anhyd. $\ce{AlCl3}$; II. $\ce{CrO3}$; III. $\ce{KMnO4}$/KOH, Δ; IV. (i) $\ce{O3}$](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_76036843_14112026.svg?v=760368434dc9)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: cyclohexylidenecyclohexane `C1CCC(=C2CCCCC2)CC1` ![cyclohexylidenecyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s1_957a6cb4_14112026.svg?v=957a6cb425a6); cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s2_ecae2398_14112026.svg?v=ecae2398c700); benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s3_dbf27a87_14112026.svg?v=dbf27a872e50); benzophenone `O=C(c1ccccc1)c1ccccc1` ![benzophenone](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s4_4a6ed161_14112026.svg?v=4a6ed161623c); cyclohexanol `OC1CCCCC1` ![cyclohexanol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s5_b130dcca_14112026.svg?v=b130dccaeb49); cyclohexanone `O=C1CCCCC1` ![cyclohexanone](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s6_ecae2398_14112026.svg?v=ecae2398c700); ethylbenzene `CCc1ccccc1` ![ethylbenzene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s7_c3cd0ee9_14112026.svg?v=c3cd0ee97328); potassium benzoate `O=C([O][K])c1ccccc1` ![potassium benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s8_7b68beea_14112026.svg?v=7b68beea7498); benzoyl chloride `O=C(Cl)c1ccccc1` ![benzoyl chloride](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q084_question_s9_56febcfe_14112026.svg?v=56febcfef378)

| List-I | | List-II | |
|---|---|---|---|
| A | [structure: reaction drawn in figure] | I | [structure: acyl chloride drawn in figure] $\mathrm{Cl}$/Anhyd. $\mathrm{AlCl_3}$ |
| B | [structure: reaction drawn in figure] | II | $\mathrm{CrO_3}$ |
| C | [structure: reaction drawn in figure] | III | $\mathrm{KMnO_4/KOH},\ \Delta$ |
| D | [structure: reaction drawn in figure] | IV | (i) $\mathrm{O_3}$ (ii) $\mathrm{Zn\text{-}H_2O}$ |

- (1) A-IV, B-I, C-III, D-II
- (2) A-III, B-I, C-II, D-IV
- **(3)** A-IV, B-I, C-II, D-III
- (4) A-I, B-IV, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A: ozonolysis $(\mathrm{O_3}$ then $\mathrm{Zn/H_2O})$ cleaves the $\mathrm{C=C}$ of cyclohexylidenecyclohexane into $2$ cyclohexanone, so A-IV.
2. B: Friedel-Crafts acylation of benzene with $\mathrm{C_6H_5COCl}$/anhyd. $\mathrm{AlCl_3}$ gives benzophenone $\mathrm{C_6H_5COC_6H_5}$, so B-I.
3. C: $\mathrm{CrO_3}$ oxidises the secondary alcohol cyclohexanol to cyclohexanone, so C-II.
4. D: $\mathrm{KMnO_4/KOH},\ \Delta$ oxidises the whole ethyl side chain to $\mathrm{-COOK}$, giving potassium benzoate, so D-III.
5. A-IV, B-I, C-II, D-III matches option $3$.

**Subtopic:** Preparation of Ketones, Methods of Preparation of Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q084_065d48c5_12112026.png?v=065d48c53196)

---

## Q85

Chemistry · physical · Chemical Equilibrium

For the reaction $\mathrm{2A \rightleftharpoons B + C}$, $K_C = 4 \times 10^{-3}$. At a given time, the composition of reaction mixture is: $[\mathrm{A}] = [\mathrm{B}] = [\mathrm{C}] = 2 \times 10^{-3}\,\mathrm{M}$. Then, which of the following is correct?

- (1) Reaction is at equilibrium.
- (2) Reaction has a tendency to go in forward direction.
- **(3)** Reaction has a tendency to go in backward direction.
- (4) Reaction has gone to completion in forward direction.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $Q_C = \frac{[\mathrm{B}][\mathrm{C}]}{[\mathrm{A}]^2}$.
2. $Q_C = \frac{(2\times10^{-3})(2\times10^{-3})}{(2\times10^{-3})^2} = 1$.
3. $Q_C = 1 > K_C = 4\times10^{-3}$, so the reaction has a tendency to go in the backward direction, which is option $3$.

**Subtopic:** Predicting the Extent and Direction of a Reaction · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q085_b6d8b945_12112026.png?v=b6d8b9454a45)

---

## Q86

Chemistry · inorganic · The D- and F-Block Elements – Practice

The pair of lanthanoid ions which are diamagnetic is

- **(1)** $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$
- (2) $\mathrm{Ce^{3+}}$ and $\mathrm{Eu^{2+}}$
- (3) $\mathrm{Gd^{3+}}$ and $\mathrm{Eu^{3+}}$
- (4) $\mathrm{Pm^{3+}}$ and $\mathrm{Sm^{3+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A diamagnetic ion has no unpaired electrons, so it needs a $4f^0$ or $4f^{14}$ configuration.
2. $\mathrm{Ce}$ ($Z=58$): $\mathrm{Ce^{4+}} = [\mathrm{Xe}]4f^0$, which has 0 unpaired electrons.
3. $\mathrm{Yb}$ ($Z=70$): $\mathrm{Yb^{2+}} = [\mathrm{Xe}]4f^{14}$, which has 0 unpaired electrons.
4. $\mathrm{Pm^{3+}}\,(4f^4)$, $\mathrm{Sm^{3+}}\,(4f^5)$, $\mathrm{Ce^{3+}}\,(4f^1)$, $\mathrm{Eu^{2+}}\,(4f^7)$, $\mathrm{Gd^{3+}}\,(4f^7)$ and $\mathrm{Eu^{3+}}\,(4f^6)$ all have unpaired electrons, so they are paramagnetic.
5. Only the pair $\mathrm{Ce^{4+}}$ and $\mathrm{Yb^{2+}}$ is diamagnetic, which is option $1$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q086_41bf4294_12112026.png?v=41bf429488bb)

---

## Q87

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

**Solved independently** (answer withheld)

1. $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligand ($\mathrm{NH_3}$), so it is homoleptic.
2. $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has two kinds of ligands ($\mathrm{NH_3}$ and $\mathrm{Cl^-}$), so it is heteroleptic; Statement I is true.
3. Statement II states exactly these ligand facts, so it is true; both true is option $1$.

**Subtopic:** Terminologies of Coordination Compounds · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 24)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q087_a534f176_12112026.png?v=a534f1767253)

---

## Q88

Chemistry · physical · Electrochemistry

Mass in grams of copper deposited by passing $9.6487\,\mathrm{A}$ current through a voltmeter containing copper sulphate solution for $100$ seconds is (Given : Molar mass of $\mathrm{Cu}$ : $63\,\mathrm{g\,mol^{-1}}$, $1\,\mathrm{F} = 96487\,\mathrm{C}$)

- (1) $3.15\,\mathrm{g}$
- **(2)** $0.315\,\mathrm{g}$
- (3) $31.5\,\mathrm{g}$
- (4) $0.0315\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $Q = It = 9.6487\,\mathrm{A} \times 100\,\mathrm{s} = 964.87\,\mathrm{C}$.
2. $\frac{964.87}{96487} = 0.01\,\mathrm{F}$.
3. $\mathrm{Cu^{2+}} + 2e^- \rightarrow \mathrm{Cu}$, so moles of Cu $= \frac{0.01}{2} = 0.005\,\mathrm{mol}$.
4. $m = 0.005 \times 63 = 0.315\,\mathrm{g}$, which is option $2$.

**Subtopic:** Faraday’s Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q088_c9b29543_12112026.png?v=c9b29543bbb2)

---

## Q89

Chemistry · organic · Hydrocarbons

For the given reaction: [reaction figure: cyclohexyl-CH=CH-cyclohexyl $\xrightarrow{\mathrm{KMnO_4/H^+}}$ 'P' (major product)] 'P' is

![printed figure: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q089_d9dcc97a_12112026.png?v=d9dcc97a2365)

*1,2-dicyclohexylethene →[$\ce{KMnO4/H+}$] 'P' (major product)*

![drawn: 1,2-dicyclohexylethene →($\ce{KMnO4/H+}$) 'P' (major product)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q089_question_d670de2f_14112026.svg?v=d670de2f74e0)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1,2-dicyclohexylethene `C(=CC1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q089_question_s1_69169cd1_14112026.svg?v=69169cd1c645)

- (1) cyclohexanecarbaldehyde `O=CC1CCCCC1` ![cyclohexanecarbaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q089_option_1_s1_79f04f91_14112026.svg?v=79f04f918b83) — $\mathrm{C_6H_{11}{-}CHO}$ (structure: cyclohexane ring attached to CHO)
- **(2)** cyclohexanecarboxylic acid `O=C(O)C1CCCCC1` ![cyclohexanecarboxylic acid](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q089_option_2_s1_5fc26872_14112026.svg?v=5fc268722cd9) — $\mathrm{C_6H_{11}{-}COOH}$ (structure: cyclohexane ring attached to COOH)
- (3) 1,2-dicyclohexylethane-1,2-diol `OC(C1CCCCC1)C(O)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-diol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q089_option_3_s1_63689f37_14112026.svg?v=63689f374fd9) — $\mathrm{C_6H_{11}{-}CH(OH){-}CH(OH){-}C_6H_{11}}$ (structure)
- (4) 1,2-dicyclohexylethane-1,2-dione `O=C(C(=O)C1CCCCC1)C1CCCCC1` ![1,2-dicyclohexylethane-1,2-dione](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q089_option_4_s1_a3dbbe83_14112026.svg?v=a3dbbe83efdc) — $\mathrm{C_6H_{11}{-}CO{-}CO{-}C_6H_{11}}$ (structure)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Acidic $\mathrm{KMnO_4}$ is a strong oxidant that cleaves the $\mathrm{C=C}$ bond of an alkene.
2. Each alkene carbon here is $\mathrm{=CH-}$ (bearing one H), so on cleavage it is oxidised first to $\mathrm{-CHO}$ and then further to $\mathrm{-COOH}$.
3. $\mathrm{C_6H_{11}{-}CH{=}CH{-}C_6H_{11} \xrightarrow{KMnO_4/H^+} 2\,C_6H_{11}{-}COOH}$, which is option $2$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q089_20d3bbac_12112026.png?v=20d3bbac07db)

---

## Q90

Chemistry · organic · Haloalkanes and Haloarenes

The products A and B obtained in the following reactions, respectively, are
$\mathrm{3ROH + PCl_3 \rightarrow RCl + A}$
$\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + B}$

- (1) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_3}$
- (2) $\mathrm{POCl_3}$ and $\mathrm{H_3PO_4}$
- (3) $\mathrm{H_3PO_4}$ and $\mathrm{POCl_3}$
- **(4)** $\mathrm{H_3PO_3}$ and $\mathrm{POCl_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\mathrm{3ROH + PCl_3 \rightarrow 3RCl + H_3PO_3}$, so $A = \mathrm{H_3PO_3}$.
2. $\mathrm{ROH + PCl_5 \rightarrow RCl + HCl + POCl_3}$, so $B = \mathrm{POCl_3}$.
3. $A, B = \mathrm{H_3PO_3}, \mathrm{POCl_3}$, which is option $4$.

**Subtopic:** Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q090_d491c8bc_12112026.png?v=d491c8bc5ffa)

---

## Q91

Chemistry · physical · Chemical Kinetics

The rate of a reaction quadruples when temperature changes from $27^\circ\mathrm{C}$ to $57^\circ\mathrm{C}$. Calculate the energy of activation. Given $R = 8.314\,\mathrm{J\,K^{-1}\,mol^{-1}}$, $\log 4 = 0.6021$

- **(1)** $38.04\,\mathrm{kJ/mol}$
- (2) $380.4\,\mathrm{kJ/mol}$
- (3) $3.80\,\mathrm{kJ/mol}$
- (4) $3804\,\mathrm{kJ/mol}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Convert temperatures: $T_1 = 27 + 273 = 300\,\mathrm{K}$, $T_2 = 57 + 273 = 330\,\mathrm{K}$.
2. Arrhenius two-temperature form: $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2 - T_1}{T_1 T_2}\right)$.
3. Rate quadruples, so $\log\frac{k_2}{k_1} = \log 4 = 0.6021$.
4. $\frac{T_2 - T_1}{T_1 T_2} = \frac{30}{300 \times 330} = \frac{1}{3300}\,\mathrm{K^{-1}}$.
5. $E_a = 0.6021 \times 2.303 \times 8.314 \times 3300\,\mathrm{J\,mol^{-1}}$.
6. $E_a \approx 38044\,\mathrm{J\,mol^{-1}} = 38.04\,\mathrm{kJ\,mol^{-1}}$, which is option $1$.

**Subtopic:** Arrhenius Equation · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 25)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q091_ab57e64e_12112026.png?v=ab57e64e3051)

---

## Q92

Chemistry · inorganic · Principles Related to Practical Chemistry

During the preparation of Mohr’s salt solution (Ferrous ammonium sulphate), which of the following acid is added to prevent hydrolysis of $\mathrm{Fe^{2+}}$ ion?

- (1) dilute hydrochloric acid
- (2) concentrated sulphuric acid
- (3) dilute nitric acid
- **(4)** dilute sulphuric acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Adding dilute $\mathrm{H_2SO_4}$ supplies $\mathrm{H^+}$ and the common $\mathrm{SO_4^{2-}}$ ion, suppressing $\mathrm{Fe^{2+}}$ hydrolysis without oxidising it, while $\mathrm{HNO_3}$ and concentrated $\mathrm{H_2SO_4}$ are oxidising and $\mathrm{HCl}$ adds foreign $\mathrm{Cl^-}$, so the answer is option $4$.

**Subtopic:** Titration · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q092_43244f54_12112026.png?v=43244f54a230)

---

## Q93

Chemistry · organic · Haloalkanes and Haloarenes

Major products A and B formed in the following reaction sequence, are

![printed figure: 2-methylcyclohexan-1-ol →($\ce{PBr3}$) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q093_7ca149f5_12112026.png?v=7ca149f5b200)

*2-methylcyclohexan-1-ol →[$\ce{PBr3}$] A (major) →[alc. KOH, Δ] B (major)*

![drawn: 2-methylcyclohexan-1-ol →($\ce{PBr3}$) A (major) →(alc. KOH, Δ) B (major)](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_question_b3ba0357_14112026.svg?v=b3ba0357421f)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2-methylcyclohexan-1-ol `CC1CCCCC1O` ![2-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_question_s1_79eed43b_14112026.svg?v=79eed43b0c22)

- **(1)** 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_1_s1_2d1efb40_14112026.svg?v=2d1efb40eae4); 1-methylcyclohex-1-ene `CC1=CCCCC1` ![1-methylcyclohex-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_1_s2_ba57c26b_14112026.svg?v=ba57c26b570b) — A =, B =
- (2) 1-bromo-2-methylcyclohexane `CC1CCCCC1Br` ![1-bromo-2-methylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_2_s1_2d1efb40_14112026.svg?v=2d1efb40eae4); 4-methylcyclohex-1-ene `CC1CC=CCC1` ![4-methylcyclohex-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_2_s2_5d2336c6_14112026.svg?v=5d2336c68684) — A =, B =
- (3) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_3_s1_bbec4cde_14112026.svg?v=bbec4cde35ec); 6-methylcyclohex-2-en-1-ol `CC1CCC=CC1O` ![6-methylcyclohex-2-en-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_3_s2_844b7d62_14112026.svg?v=844b7d628c94) — A =, B =
- (4) 2-bromo-6-methylcyclohexan-1-ol `CC1CCCC(Br)C1O` ![2-bromo-6-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_4_s1_bbec4cde_14112026.svg?v=bbec4cde35ec); 2-methylcyclohexan-1-one `CC1CCCCC1=O` ![2-methylcyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/14112026/neet_papers/2024/2024_Q3/figures_drawn/q093_option_4_s2_7eaab55c_14112026.svg?v=7eaab55cfa65) — A =, B =

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{PBr_3}$ converts the secondary alcohol to the alkyl bromide: $\mathrm{R{-}OH} \xrightarrow{PBr_3} \mathrm{R{-}Br}$, so A is 1-bromo-2-methylcyclohexane.
2. Alcoholic $\mathrm{KOH}$ with heat causes $\beta$-elimination of $\mathrm{HBr}$ from A.
3. By Saytzeff's rule the H is lost from the more substituted $\beta$-carbon (the one bearing $\mathrm{CH_3}$), giving the trisubstituted alkene.
4. B is 1-methylcyclohexene, matching option $1$; option $2$ shows a disubstituted alkene not conjugated to the methyl carbon, and options $3$, $4$ wrongly keep OH in A.

**Subtopic:** Reactions of Haloalkanes – Elimination Reactions, Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q093_2ef8949e_12112026.png?v=2ef8949e16a2)

---

## Q94

Chemistry · physical · Solutions

The plot of osmotic pressure ($\Pi$) vs concentration ($\mathrm{mol\,L^{-1}}$) for a solution gives a straight line with slope $25.73\,\mathrm{L\,bar\,mol^{-1}}$. The temperature at which the osmotic pressure measurement is done is (Use $R = 0.083\,\mathrm{L\,bar\,mol^{-1}\,K^{-1}}$)

- **(1)** $37^\circ\mathrm{C}$
- (2) $310^\circ\mathrm{C}$
- (3) $25.73^\circ\mathrm{C}$
- (4) $12.05^\circ\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. From $\Pi = CRT$, a plot of $\Pi$ vs $C$ is a straight line with slope $RT$.
2. $RT = 25.73\,\mathrm{L\,bar\,mol^{-1}}$, so $T = \frac{25.73}{0.083} = 310\,\mathrm{K}$.
3. $310\,\mathrm{K} - 273 = 37\,^{\circ}\mathrm{C}$, which is option $1$.

**Subtopic:** Osmosis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q094_e2d3e0e2_12112026.png?v=e2d3e0e25691)

---

## Q95

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the correct answer.

- (1) Three resonance structures can be drawn for ozone
- (2) $\mathrm{BF_3}$ has non-zero dipole moment
- (3) Dipole moment of $\mathrm{NF_3}$ is greater than that of $\mathrm{NH_3}$
- **(4)** Three canonical forms can be drawn for $\mathrm{CO_3^{2-}}$ ion

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In $\mathrm{CO_3^{2-}}$ the $\mathrm{C=O}$ double bond can sit on any of the three O atoms, giving three canonical forms, so statement 1 is true.
2. Ozone $\mathrm{O_3}$ has only two resonance structures, so statement 2 is false.
3. $\mathrm{BF_3}$ is trigonal planar and the three $\mathrm{B-F}$ bond dipoles cancel, so $\mu = 0$; statement 3 is false.
4. In $\mathrm{NH_3}$ the lone-pair moment adds to the $\mathrm{N-H}$ bond moments, while in $\mathrm{NF_3}$ it opposes the $\mathrm{N-F}$ bond moments, so $\mu(\mathrm{NH_3}) > \mu(\mathrm{NF_3})$; statement 4 is false.
5. Only statement 1 is correct, which is option $4$.

**Subtopic:** Bond Parameters, Dipole Moment · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 26)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q095_2568237b_12112026.png?v=2568237bb810)

---

## Q96

Chemistry · organic · Amines

Identify the major product C formed in the following reaction sequence: $\mathrm{CH_3-CH_2-CH_2-I \xrightarrow{NaCN} A \xrightarrow[\text{Partial hydrolysis}]{OH^-} B \xrightarrow[Br_2]{NaOH} \underset{(\text{major})}{C}}$

- **(1)** propylamine
- (2) butylamine
- (3) butanamide
- (4) $\alpha$–bromobutanoic acid

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2I} + \mathrm{NaCN} \rightarrow \mathrm{CH_3CH_2CH_2CN}$ (A, butanenitrile) by $S_N2$ substitution.
2. Partial hydrolysis: $\mathrm{CH_3CH_2CH_2CN} \xrightarrow{\mathrm{OH^-}} \mathrm{CH_3CH_2CH_2CONH_2}$ (B, butanamide).
3. Hofmann bromamide degradation: $\mathrm{CH_3CH_2CH_2CONH_2} + \mathrm{Br_2} + 4\mathrm{NaOH} \rightarrow \mathrm{CH_3CH_2CH_2NH_2} + \mathrm{Na_2CO_3} + 2\mathrm{NaBr} + 2\mathrm{H_2O}$.
4. C is $\mathrm{CH_3CH_2CH_2NH_2}$, propylamine, which is option $1$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q096_d0ee6fcf_12112026.png?v=d0ee6fcfdbd6)

---

## Q97

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

**Solved independently** (answer withheld)

1. $\mathrm{Cu^{2+}}$ is precipitated as sulphide by $\mathrm{H_2S}$ in dilute HCl, so it is group II.
2. $\mathrm{Al^{3+}}$ is precipitated as hydroxide by $\mathrm{NH_4OH}$ in presence of $\mathrm{NH_4Cl}$, so it is group III.
3. $\mathrm{Co^{2+}}$ is precipitated as sulphide by $\mathrm{H_2S}$ in ammoniacal medium, so it is group IV.
4. $\mathrm{Ba^{2+}}$ is precipitated as carbonate by $\mathrm{(NH_4)_2CO_3}$, so it is group V.
5. $\mathrm{Mg^{2+}}$ remains for group VI.
6. Increasing order: B (II), A (III), D (IV), C (V), E (VI), which is option $1$.

**Subtopic:** Group Analysis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q097_b58d0866_12112026.png?v=b58d0866bebc)

---

## Q98

Chemistry · physical · Thermodynamics

The work done during reversible isothermal expansion of one mole of hydrogen gas at $25^\circ\mathrm{C}$ from pressure of $20$ atmosphere to $10$ atmosphere is (Given $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$)

- (1) $0$ calorie
- **(2)** $-413.14$ calories
- (3) $413.14$ calories
- (4) $100$ calories

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For reversible isothermal expansion of an ideal gas, $W = -2.303\,nRT\log\frac{P_1}{P_2}$.
2. Substitute $n = 1$, $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$, $T = 298\,\mathrm{K}$, $\frac{P_1}{P_2} = \frac{20}{10} = 2$.
3. $W = -2.303 \times 1 \times 2.0 \times 298 \times \log 2 = -2.303 \times 596 \times 0.3010$.
4. $W \approx -413.1\,\mathrm{cal}$, negative because work is done by the gas on expansion, which is option $2$ ($-413.14$ calories).

**Subtopic:** Pressure–Volume Work for Isothermal Reversible Process · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q098_f883a53b_12112026.png?v=f883a53bcbed)

---

## Q99

Chemistry · physical · Chemical Equilibrium

Consider the following reaction in a sealed vessel at equilibrium with concentrations of $\mathrm{N_2} = 3.0 \times 10^{-3}\,\mathrm{M}$, $\mathrm{O_2} = 4.2 \times 10^{-3}\,\mathrm{M}$ and $\mathrm{NO} = 2.8 \times 10^{-3}\,\mathrm{M}$. $\mathrm{2NO_{(g)} \rightleftharpoons N_{2(g)} + O_{2(g)}}$ If $0.1\,\mathrm{mol\,L^{-1}}$ of $\mathrm{NO_{(g)}}$ is taken in a closed vessel, what will be degree of dissociation $(\alpha)$ of $\mathrm{NO_{(g)}}$ at equilibrium?

- (1) $0.00889$
- (2) $0.0889$
- (3) $0.8889$
- **(4)** $0.717$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $K_c = \frac{[\mathrm{N_2}][\mathrm{O_2}]}{[\mathrm{NO}]^2} = \frac{(3.0\times10^{-3})(4.2\times10^{-3})}{(2.8\times10^{-3})^2}$.
2. $K_c = \frac{12.6\times10^{-6}}{7.84\times10^{-6}} = 1.607$.
3. Starting with $0.1\,\mathrm{M}$ NO and degree of dissociation $\alpha$: $[\mathrm{NO}] = 0.1(1-\alpha)$, $[\mathrm{N_2}] = [\mathrm{O_2}] = 0.05\alpha$.
4. $K_c = \frac{(0.05\alpha)^2}{(0.1(1-\alpha))^2} = \left(\frac{0.5\alpha}{1-\alpha}\right)^2 = 1.607$.
5. $\frac{0.5\alpha}{1-\alpha} = \sqrt{1.607} = 1.268$.
6. $0.5\alpha = 1.268 - 1.268\alpha \Rightarrow \alpha = \frac{1.268}{1.768} = 0.717$, which is option $4$.

**Subtopic:** Calculating Equilibrium Concentrations · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 27)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q099_371318a7_12112026.png?v=371318a76341)

---

## Q100

Chemistry · physical · Basic Concepts of Chemistry

A compound X contains $32\%$ of A, $20\%$ of B and remaining percentage of C. Then, the empirical formula of X is : (Given atomic masses of $\mathrm{A} = 64$; $\mathrm{B} = 40$; $\mathrm{C} = 32\,\mathrm{u}$)

- (1) $\mathrm{A_2BC_2}$
- **(2)** $\mathrm{ABC_3}$
- (3) $\mathrm{AB_2C_2}$
- (4) $\mathrm{ABC_4}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Percentage of C $= 100 - 32 - 20 = 48\%$.
2. Moles in 100 g: $n_A = \frac{32}{64} = 0.5$, $n_B = \frac{20}{40} = 0.5$, $n_C = \frac{48}{32} = 1.5$.
3. Divide by the smallest ($0.5$): $A:B:C = 1:1:3$.
4. Empirical formula $= \mathrm{ABC_3}$, which is option $2$.

**Subtopic:** Empirical and Molecular Formula · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q100_db9683d2_12112026.png?v=db9683d2f89c)

---

## Q101

Biology · botany · Biomolecules

Lecithin, a small molecular weight organic compound found in living tissues, is an example of:

- (1) Amino acids
- **(2)** Phospholipids
- (3) Glycerides
- (4) Carbohydrates

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Lecithin is a lipid carrying a phosphorylated organic compound (choline), so it is a phospholipid, which is option $2$.

**Subtopic:** Lipids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q101_98abb3ba_12112026.png?v=98abb3ba934c)

---

## Q102

Biology · botany · Photosynthesis in Higher Plants

How many molecules of ATP and NADPH are required for every molecule of $\mathrm{CO_2}$ fixed in the Calvin cycle?

- (1) 2 molecules of ATP and 3 molecules of NADPH
- (2) 2 molecules of ATP and 2 molecules of NADPH
- (3) 3 molecules of ATP and 3 molecules of NADPH
- **(4)** 3 molecules of ATP and 2 molecules of NADPH

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Reduction of 2 molecules of 3-PGA formed per $\mathrm{CO_2}$ uses $2\,\mathrm{ATP} + 2\,\mathrm{NADPH}$; regeneration of RuBP uses $1\,\mathrm{ATP}$, so per $\mathrm{CO_2}$ fixed: $3\,\mathrm{ATP} + 2\,\mathrm{NADPH}$, which is option $4$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q102_8686b4d4_12112026.png?v=8686b4d44c9d)

---

## Q103

Biology · botany · Biotechnology: Principles and Processes

Hind II always cuts DNA molecules at a particular point called recognition sequence and it consists of:

- (1) $8\,\mathrm{bp}$
- **(2)** $6\,\mathrm{bp}$
- (3) $4\,\mathrm{bp}$
- (4) $10\,\mathrm{bp}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Per NCERT, Hind II always cuts DNA at a particular point by recognising a specific sequence of $6$ base pairs, which is option $2$ ($6\,\mathrm{bp}$).

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q103_083cf7db_12112026.png?v=083cf7db603b)

---

## Q104

Biology · botany · Anatomy of Flowering Plants

In the given figure, which component has thin outer walls and highly thickened inner walls?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q104_c11ad387_12112026.png?v=c11ad38742d6)

- **(1)** C
- (2) D
- (3) A
- (4) B

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The figure shows a stoma: $A$ = epidermal cell, $B$ = subsidiary cell, $C$ = bean-shaped guard cell, $D$ = stomatal pore.
2. As NCERT teaches, guard cells have thin outer walls and highly thickened inner walls (towards the pore), so the answer is $C$, which is option $1$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q104_21b90cf5_12112026.png?v=21b90cf5b8b2)

---

## Q105

Biology · botany · Biomolecules

The cofactor of the enzyme carboxypeptidase is :

- **(1)** Zinc
- (2) Niacin
- (3) Flavin
- (4) Haem

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Carboxypeptidase is a proteolytic metalloenzyme whose essential cofactor is the metal ion $\mathrm{Zn^{2+}}$, so the answer is option $1$ (Zinc).

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q105_3b9351c2_12112026.png?v=3b9351c2ddd5)

---

## Q106

Biology · botany · Strategies for Enhancement in Food Production

The capacity to generate a whole plant from any cell of the plant is called:

- **(1)** Totipotency
- (2) Micropropagation
- (3) Differentiation
- (4) Somatic hybridization

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The ability of a single plant cell (explant) to give rise to a whole plant is defined as totipotency, which is option $1$.

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q106_4e7b0f16_12112026.png?v=4e7b0f1696f7)

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

- **(1)** A-III, B-II, C-IV, D-I
- (2) A-I, B-III, C-II, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Rhizopus is the common bread mould, so A–III.
2. Ustilago causes smut disease of cereals, so B–II.
3. Puccinia is the rust fungus of wheat, so C–IV.
4. Agaricus is the edible mushroom, so D–I.
5. The combination A-III, B-II, C-IV, D-I is option $1$.

**Subtopic:** Basidiomycetes, Phycomycetes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q107_87cec71c_12112026.png?v=87cec71c3385)

---

## Q108

Biology · botany · Biotechnology and Its Applications

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

**Solved independently** (answer withheld)

1. Bt toxin proteins are coded by several genes named $cry$ (e.g. $cryIAc$, $cryIIAb$ for cotton bollworms, $cryIAb$ for corn borer); they are not coded by the single gene $cryIAc$, so Statement I is false.
2. The Bt toxin exists as an inactive protoxin and is converted to the active toxin by the alkaline pH of the insect gut, not an acidic pH, so Statement II is false.
3. Both statements are false, which is option $2$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 29)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q108_98d6b832_12112026.png?v=98d6b832bb9e)

---

## Q109

Biology · botany · Morphology of Flowering Plants

Which of the following is an example of actinomorphic flower?

- **(1)** Datura
- (2) Cassia
- (3) Pisum
- (4) Sesbania

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT lists mustard, Datura and chilli as actinomorphic, while pea (Pisum), Sesbania (bean-type papilionaceous flowers) and Cassia are zygomorphic, so the answer is option $1$ (Datura).

**Subtopic:** The Flower · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q109_3caccc98_12112026.png?v=3caccc98a199)

---

## Q110

Biology · botany · Biodiversity and Conservation

> ⚠ The question describes ex-situ conservation (threatened species taken out of their natural habitat and protected in a special setting), but no option says "ex-situ conservation". The booklet keys "Biodiversity conservation" as the umbrella term, and its own solution names ex-situ conservation "a type of biodiversity conservation". The keyed option is defensible only as the broad category; the precise answer is missing from the options. Same question as 2024_T3 q102 and 2024_S1 q118.

The type of conservation in which the threatened species are taken out from their natural habitat and placed in special setting where they can be protected and given special care is called;

- (1) in-situ conservation
- **(2)** Biodiversity conservation
- (3) Semi-conservative method
- (4) Sustainable development

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Taking threatened species out of their natural habitat and protecting them in a special setting is ex-situ conservation.
2. Option $1$ (in-situ) means protection within the natural habitat, so it is wrong; options $4$ and $3$ are unrelated terms.
3. Ex-situ is not offered, so the broad term in option $2$, Biodiversity conservation, is the best available choice.

**Subtopic:** Ex Situ Conservation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q110_434c2eea_12112026.png?v=434c2eea8de3)

---

## Q111

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the set of correct statement: Choose the correct answer from the options given below.

- (A) The flowers of \textit{Vallisneria} are colourful and produce nectar.
- (B) The flowers of waterlily are not pollinated by water.
- (C) In most of water-pollinated species, the pollen grains are protected from wetting.
- (D) Pollen grains of some hydrophytes are long and ribbon like.
- (E) In some hydrophytes, the pollen grains are carried passively inside water.

- (1) C, D and E only
- (2) A, B, C and D only
- (3) A, C, D and E only
- **(4)** B, C, D and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement A: water-pollinated flowers such as $Vallisneria$ are not colourful and do not produce nectar, so A is false.
2. Statement B: water lily emerges above water and is pollinated by insects or wind, not water, so B is true.
3. Statement C: in most water-pollinated species pollen grains are protected from wetting by a mucilaginous covering, so C is true.
4. Statement D: in some hydrophytes such as seagrasses, pollen grains are long and ribbon-like, so D is true.
5. Statement E: in some hydrophytes such as seagrasses, pollen grains are carried passively inside water, so E is true.
6. True set is B, C, D and E, which is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 30)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q111_5d75ee21_12112026.png?v=5d75ee21bfd8)

---

## Q112

Biology · botany · Molecular Basis of Inheritance

The lactose present in the growth medium of bacteria is transported to the cell by the action of

- (1) Beta-galactosidase
- (2) Acetylase
- **(3)** Permease
- (4) Polymerase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the $lac$ operon, the $y$ gene codes for permease, which raises the cell's permeability to $\beta$-galactosides and so carries lactose into the cell; this is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 30)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q112_8fa842b9_12112026.png?v=8fa842b9bed6)

---

## Q113

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

**Solved independently** (answer withheld)

1. $A$: Clostridium butylicum produces butyric acid $\Rightarrow A\text{-}III$; $B$: Saccharomyces cerevisiae produces ethanol $\Rightarrow B\text{-}I$.
2. $C$: Trichoderma polysporum produces cyclosporin-A $\Rightarrow C\text{-}IV$; $D$: Streptococcus produces streptokinase $\Rightarrow D\text{-}II$.
3. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ matches option $3$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q113_706d18b0_12112026.png?v=706d18b001cc)

---

## Q114

Biology · botany · Organisms and Populations

The equation of Verhulst-Pearl logistic growth is $\frac{dN}{dt} = rN\left[\frac{K-N}{K}\right]$.
From this equation, K indicates:

- (1) Intrinsic rate of natural increase
- (2) Biotic potential
- **(3)** Carrying capacity
- (4) Population density

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In $\frac{dN}{dt} = rN\left[\frac{K - N}{K}\right]$, $N$ is population density, $r$ is the intrinsic rate of natural increase and $K$ is the carrying capacity, which is option $3$.

**Subtopic:** Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q114_543d33af_12112026.png?v=543d33afb5be)

---

## Q115

Biology · botany · Plant Growth and Development

Auxin is used by gardeners to prepare weed-free lawns. But no damage is caused to grass as auxin

- (1) promotes apical dominance.
- (2) promotes abscission of mature leaves only.
- **(3)** does not affect mature monocotyledonous plants.
- (4) can help in cell division in grasses, to produce growth.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Synthetic auxins like $2,4\text{-D}$ are selective herbicides that kill dicot weeds but do not affect mature monocotyledonous plants such as grass, which is option $3$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q115_64ce0e58_12112026.png?v=64ce0e582998)

---

## Q116

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the part of the seed from the given figure which is destined to form root when the seed germinates.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q116_2e380f01_12112026.png?v=2e380f011e55)

- (1) A
- (2) B
- **(3)** C
- (4) D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The figure is a monocot (maize-type) seed in L.S.: endosperm above, embryo axis at the lower side; the upper sheath A is the coleoptile, B is the plumule, C is the radicle inside the lower sheath D (coleorhiza), so the radicle $C$, which forms the root, is option $3$.

**Subtopic:** Embryo and Seed · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q116_58627da3_12112026.png?v=58627da3d338)

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

**Solved independently** (answer withheld)

1. Collenchyma cells are living (with protoplasm), so Statement I is false.
2. Xylem vessels are absent in gymnosperms and are characteristic of angiosperms, so Statement II is true; this matches option $4$.

**Subtopic:** Permanent Tissue, Complex Tissue · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q117_10268612_12112026.png?v=10268612a657)

---

## Q118

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

**Solved independently** (answer withheld)

1. NCERT lists the four major causes of biodiversity loss (the 'Evil Quartet') as habitat loss and fragmentation, over-exploitation, alien species invasions and co-extinctions, so $A$, $B$ and $D$ are causes while mutation ($C$) and migration ($E$) are not, giving option $4$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q118_33b5bd69_12112026.png?v=33b5bd697e59)

---

## Q119

Biology · botany · Biological Classification

Which one of the following is not a criterion for classification of fungi?

- (1) Morphology of mycelium
- **(2)** Mode of nutrition
- (3) Mode of spore formation
- (4) Fruiting body

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT states fungi are divided into classes based on morphology of the mycelium, mode of spore formation and fruiting bodies, so mode of nutrition (option $2$) is not a criterion.

**Subtopic:** Kingdom Fungi · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 32)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q119_ce9f4b83_12112026.png?v=ce9f4b8364c1)

---

## Q120

Biology · botany · Morphology of Flowering Plants

Identify the type of flowers based on the position of calyx, corolla and androecium with respect to the ovary from the given figures (a) and (b)

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q120_a464d241_12112026.png?v=a464d2415f98)

- (1) (a) Epigynous; (b) Hypogynous
- (2) (a) Hypogynous; (b) Epigynous
- (3) (a) Perigynous; (b) Epigynous
- **(4)** (a) Perigynous; (b) Perigynous

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In figure (a) the thalamus grows up as a cup around the ovary; the ovary is not fused with the cup wall.
2. The sepals, petals and stamens of (a) arise from the rim of the cup, roughly at the level of the ovary, so (a) is perigynous.
3. In figure (b) the thalamus is a shallower cup; the ovary again sits free in its centre and the other floral parts arise from its rim at about the ovary's level, so (b) is perigynous.
4. Neither figure shows parts below a superior ovary on a flat/convex thalamus (hypogynous) or parts above an ovary fused with the thalamus (epigynous), so the answer is (a) Perigynous; (b) Perigynous, option $4$.

**Subtopic:** Position of the Ovary · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q120_f04c02c8_12112026.png?v=f04c02c84fa7)

---

## Q121

Biology · botany · Biodiversity and Conservation

List of endangered species was released by-

- (1) GEAC
- (2) WWF
- (3) FOAM
- **(4)** IUCN

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The IUCN (International Union for Conservation of Nature) publishes the Red List of threatened species, so the list of endangered species is released by IUCN, option $4$.

**Subtopic:** Loss of Biodiversity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q121_f67f8652_12112026.png?v=f67f86521e97)

---

## Q122

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

**Solved independently** (answer withheld)

1. A piece of DNA with only the gene of interest has no origin of replication ($ori$), so it cannot replicate on its own: statements $A$ and $E$ are false.
2. Such alien DNA may get integrated into the recipient genome: statement $B$ is true.
3. Once integrated, it multiplies and is inherited along with the host DNA: statement $C$ is true, and $D$ (not an integral part of the chromosome) is false.
4. So the correct set is $B$ and $C$ only, which is option $3$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q122_33b8460e_12112026.png?v=33b8460e36d7)

---

## Q123

Biology · botany · Principles of Inheritance and Variation

Which one of the following can be explained on the basis of Mendel's Law of Dominance? Choose the correct answer from the options given below:

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

**Solved independently** (answer withheld)

1. Per NCERT, the Law of Dominance states: characters are controlled by discrete units called factors, so $D$ is true.
2. Factors occur in pairs, so $C$ is true.
3. In a dissimilar pair of factors one member dominates (dominant) and the other does not (recessive), so $A$ is true.
4. The law explains expression of only one parental character in the $\mathrm{F_1}$ of a monohybrid cross, so $E$ is true.
5. $B$ (alleles show no expression, both characters appear as such) does not follow from dominance, so $B$ is false.
6. Correct set is $A, C, D$ and $E$ only, which is option $2$.

**Subtopic:** Principles of Laws of Inheritance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q123_364a8709_12112026.png?v=364a8709ca11)

---

## Q124

Biology · botany · Biomolecules

Inhibition of Succinic dehydrogenase enzyme by malonate is a classical example of:

- (1) Cofactor inhibition
- (2) Feedback inhibition
- **(3)** Competitive inhibition
- (4) Enzyme activation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Malonate closely resembles succinate in structure and binds the active site of succinic dehydrogenase in place of the substrate, which is competitive inhibition (option $3$).

**Subtopic:** Factors Affecting Enzyme Activity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q124_e447d534_12112026.png?v=e447d5347785)

---

## Q125

Biology · botany · Plant Growth and Development

Formation of interfascicular cambium from fully developed parenchyma cells is an example for

- (1) Differentiation
- (2) Redifferentiation
- **(3)** Dedifferentiation
- (4) Maturation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Fully differentiated parenchyma cells regaining the ability to divide to form interfascicular cambium is $\text{dedifferentiation}$, which is option $3$.

**Subtopic:** Differentiation and Dedifferentiation and Redifferentiation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 33)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q125_70940503_12112026.png?v=709405032ff9)

---

## Q126

Biology · botany · Cell Cycle and Cell Division

Spindle fibers attach to kinetochores of chromosomes during

- (1) Prophase
- **(2)** Metaphase
- (3) Anaphase
- (4) Telophase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT (Cell Cycle and Cell Division) states that the complete disintegration of the nuclear envelope marks the start of metaphase, when spindle fibres attach to the kinetochores of chromosomes, so the answer is option $2$ (Metaphase).

**Subtopic:** Prophase and Metaphase · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q126_63d0623d_12112026.png?v=63d0623dad3e)

---

## Q127

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

**Solved independently** (answer withheld)

1. A is true: tropical latitudes stayed relatively undisturbed for millions of years, giving more time for diversification.
2. B is false: tropical environments are less seasonal, not more.
3. C is true: more solar energy is available in the tropics, supporting higher productivity.
4. D is true: constant environments promote niche specialization.
5. E is true: tropical environments are relatively constant and predictable.
6. True set is $\{A, C, D, E\}$, which is option $1$.

**Subtopic:** Latitudinal Gradients · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q127_5cb29c35_12112026.png?v=5cb29c35e7c3)

---

## Q128

Biology · botany · Cell Cycle and Cell Division

Given below are two statements:
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Chromosomes become gradually visible under light microscope during leptotene stage.
- (Statement II) The beginning of diplotene stage is recognized by dissolution of synaptonemal complex.

- **(1)** Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: in leptotene, chromosomes become gradually visible under the light microscope, so Statement I is true.
2. Statement II: the beginning of diplotene is recognised by dissolution of the synaptonemal complex, so Statement II is true.
3. Both statements are true, which is option $1$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q128_3d0852dd_12112026.png?v=3d0852ddc334)

---

## Q129

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

**Solved independently** (answer withheld)

1. Nucleolus is the site of active ribosomal RNA synthesis $\Rightarrow$ A-III.
2. Centriole shows a cartwheel organization of nine triplet fibrils $\Rightarrow$ B-II.
3. Leucoplasts (amyloplasts, elaioplasts, aleuroplasts) store starch, oils and proteins $\Rightarrow$ C-IV.
4. Golgi apparatus is the site of formation of glycoproteins and glycolipids $\Rightarrow$ D-I.
5. Combination A-III, B-II, C-IV, D-I corresponds to option $1$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q129_6427cdfd_12112026.png?v=6427cdfdc673)

---

## Q130

Biology · botany · Anatomy of Flowering Plants

Bulliform cells are responsible for

- **(1)** Inward curling of leaves in monocots.
- (2) Protecting the plant from salt stress.
- (3) Increased photosynthesis in monocots.
- (4) Providing large spaces for storage of sugars.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Bulliform cells are large, empty, colourless epidermal cells of monocot (grass) leaves; when they become flaccid from water loss the leaf curls inward, which is option $1$.

**Subtopic:** Dicotyledonous and Monocotyledonous Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q130_3a8af500_12112026.png?v=3a8af500a8bb)

---

## Q131

Biology · botany · Principles of Inheritance and Variation

A pink flowered Snapdragon plant was crossed with a red flowered Snapdragon plant. What type of phenotype/s is/are expected in the progeny?

- (1) Only red flowered plants
- **(2)** Red flowered as well as pink flowered plants
- (3) Only pink flowered plants
- (4) Red, Pink as well as white flowered plants

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Flower colour in snapdragon shows incomplete dominance: $RR$ = red, $Rr$ = pink, $rr$ = white.
2. Cross: $Rr \times RR$ gives gametes $R, r$ and $R$.
3. Progeny: $\frac{1}{2} RR$ (red) $+ \frac{1}{2} Rr$ (pink), which is option $2$.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q131_ab4506a2_12112026.png?v=ab4506a212da)

---

## Q132

Biology · botany · Molecular Basis of Inheritance

A transcription unit in DNA is defined primarily by the three regions in DNA and these are with respect to upstream and down stream end;

- (1) Repressor, Operator gene, Structural gene
- (2) Structural gene, Transposons, Operator gene
- (3) Inducer, Repressor, Structural gene
- **(4)** Promotor, Structural gene, Terminator

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A transcription unit in DNA is defined by three regions: the promoter at the upstream end, the structural gene in the middle, and the terminator at the downstream end, which matches option $4$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q132_34f6bfab_12112026.png?v=34f6bfab8c35)

---

## Q133

Biology · botany · Principles of Inheritance and Variation

In a plant, black seed color (BB/Bb) is dominant over white seed color (bb). In order to find out the genotype of the black seed plant, with which of the following genotype will be cross it?

- (1) BB
- **(2)** bb
- (3) Bb
- (4) BB/Bb

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. To find the unknown genotype of a dominant-phenotype plant, cross it with the homozygous recessive parent ($bb$) — a test cross.
2. If the progeny are all black, the plant is $BB$; if black and white appear $1:1$, it is $Bb$. So the cross is with $bb$, option $2$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q133_19fe70a9_12112026.png?v=19fe70a93c1d)

---

## Q134

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

**Solved independently** (answer withheld)

1. The dark reaction is the Calvin cycle, the biosynthetic phase of photosynthesis.
2. It fixes $\mathrm{CO_2}$ (C) through RuBisCO into carbohydrate.
3. Reduction of $\mathrm{CO_2}$ uses ATP (D) and NADPH (E) made in the light reaction.
4. Light (A) and chlorophyll (B) are needed only in the light reaction, not directly in the dark reaction.
5. So the required set is C, D and E only, which is option $3$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 35)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q134_d722ac82_12112026.png?v=d722ac82585f)

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

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-I, C-III, D-IV
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Two or more alternative forms of a gene are alleles: $A \rightarrow III$.
2. A cross of $\mathrm{F_1}$ with the homozygous recessive parent is a test cross: $B \rightarrow IV$.
3. A cross of $\mathrm{F_1}$ with any of the parents is a back cross: $C \rightarrow I$.
4. The number of chromosome sets in a plant is its ploidy: $D \rightarrow II$, so the match is A-III, B-IV, C-I, D-II, which is option $3$.

**Subtopic:** Test Cross & Back Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q135_c4bcc9eb_12112026.png?v=c4bcc9eb0bfc)

---

## Q136

Biology · botany · Cell: The Unit of Life

The DNA present in chloroplast is:

- (1) Linear, double stranded
- **(2)** Circular, double stranded
- (3) Linear, single stranded
- (4) Circular, single stranded

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Chloroplast DNA, like prokaryotic DNA, is a naked, circular, double-stranded molecule, which is option $2$.

**Subtopic:** Plastids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 36)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q136_1bdef101_12112026.png?v=1bdef1012041)

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

**Solved independently** (answer withheld)

1. Robert May estimated global species diversity at about $7$ million, so A-III.
2. Alexander von Humboldt described the species-area relationship, so B-I.
3. Paul Ehrlich proposed the rivet popper hypothesis, so C-IV.
4. David Tilman conducted long-term ecosystem experiments using outdoor plots, so D-II.
5. A-III, B-I, C-IV, D-II matches option $2$.

**Subtopic:** The Importance of Species Diversity to the Ecosystem, Species–Area Relationships · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q137_155ab7ab_12112026.png?v=155ab7abe067)

---

## Q138

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

**Solved independently** (answer withheld)

1. Rose (A) has a perigynous flower (hypanthium), so $A \to II$.
2. Pea (B) has marginal placentation (monocarpellary ovary), so $B \to IV$.
3. Cotton (C) shows twisted aestivation, so $C \to I$.
4. Mango (D) fruit is a drupe, so $D \to III$.
5. $A$-II, $B$-IV, $C$-I, $D$-III matches option $1$.

**Subtopic:** The Flower, The Fruit · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 37)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q138_fe8320dd_12112026.png?v=fe8320dd17f0)

---

## Q139

Biology · botany · Molecular Basis of Inheritance

Which of the following statement is correct regarding the process of replication in \textit{E.coli}?

- (1) The DNA dependent DNA polymerase catalyses polymerization in one direction that is $3' \rightarrow 5'$
- (2) The DNA dependent RNA polymerase catalyses polymerization in one direction, that is $5' \rightarrow 3'$
- (3) The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ as well as $3' \rightarrow 5'$ direction
- **(4)** The DNA dependent DNA polymerase catalyses polymerization in $5' \rightarrow 3'$ direction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. DNA replication in \textit{E. coli} is catalysed by DNA-dependent DNA polymerase, which adds nucleotides only in the $5' \rightarrow 3'$ direction, so option $4$ is correct; options $1$ and $3$ give wrong directions and option $2$ names the transcription enzyme.

**Subtopic:** The Machinery and the Enzymes of Replication · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 37)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q139_e5a65284_12112026.png?v=e5a65284d513)

---

## Q140

Biology · botany · Sexual Reproduction in Flowering Plants

Identify the correct description about the given figure:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q140_9f371118_12112026.png?v=9f37111840ca)

- **(1)** Wind pollinated plant inflorescence showing flowers with well exposed stamens.
- (2) Water pollinated flowers showing stamens with mucilaginous covering.
- (3) Cleistogamous flowers showing autogamy.
- (4) Compact inflorescence showing complete autogamy

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The figure shows a compact elongated inflorescence axis with numerous long filaments bearing anthers hanging freely on all sides, i.e. well-exposed stamens; this is the adaptation of wind-pollinated plants for easy dispersal of pollen by air currents, so the description is option $1$.

**Subtopic:** Agents of Pollination · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 37)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q140_3d3a8841_12112026.png?v=3d3a8841a99a)

---

## Q141

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

**Solved independently** (answer withheld)

1. Citric acid cycle (A) occurs in the mitochondrial matrix, so $A \rightarrow II$.
2. Glycolysis (B) occurs in the cytoplasm, so $B \rightarrow I$.
3. Electron transport system (C) is located in the inner mitochondrial membrane, so $C \rightarrow IV$.
4. Protons are pumped into the intermembrane space, creating the proton gradient there, so $D \rightarrow III$.
5. $A$-II, $B$-I, $C$-IV, $D$-III matches option $2$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle, Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 38)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q141_71236581_12112026.png?v=71236581e4f9)

---

## Q142

Biology · botany · Plant Kingdom

Read the following statements and choose the set of correct statements:
In the members of Phaeophyceae,
Choose the correct answer from the options given below:

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

**Solved independently** (answer withheld)

1. A: asexual reproduction in brown algae is usually by pear-shaped biflagellate zoospores, so A is true.
2. B: sexual reproduction may be isogamous, anisogamous or oogamous, so 'oogamous only' makes B false.
3. C: reserve food is complex carbohydrate as laminarin or mannitol, so C is true.
4. D: pigments are chlorophyll $a$, $c$, carotenoids and xanthophylls (fucoxanthin), so D is true.
5. E: the cellulosic wall is usually covered outside by a gelatinous coating of algin, so E is true.
6. Correct set is A, C, D and E only, which is option $3$.

**Subtopic:** Phaeophyceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q142_c1d22139_12112026.png?v=c1d221397998)

---

## Q143

Biology · botany · Ecosystem

> ⚠ The question asks for the GPP (Gross Primary Productivity) of the THIRD trophic level, but primary productivity is defined only for producers (the first level). Read as "energy reaching level 3" with the 10% rule, 100x gives 10x at level 2 and x at level 3 (option 2); the booklet keys 10x (option 3), reading it as what level 3 takes in from level 2. Two independent audits came to opposite answers, so the wording, not the solver, is the problem. Same question as 2024_S1 q147.

> ⚠ The independent solve chose (2); the booklet prints (3).

In an ecosystem if the Net Primary Productivity (NPP) of first trophic level is $100x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, what would be the GPP (Gross Primary Productivity) of the third trophic level of the same ecosystem?

- (1) $\frac{x}{10}(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$
- (2) $x(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$
- **(3)** $10x(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$
- (4) $\frac{100x}{3x}(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$

**Answer** — booklet: (3) · independent solve: (2) · differs

**Solved independently** (answer withheld)

1. Apply the 10% law: only about $10\%$ of energy at one trophic level is transferred to the next.
2. Energy reaching the second trophic level $= 0.1 \times 100x = 10x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$.
3. Energy reaching the third trophic level $= 0.1 \times 10x = x\,(\mathrm{kcal\,m^{-2}})\,\mathrm{yr^{-1}}$, which is option $2$.

**Subtopic:** Energy Flow, Productivity · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 38)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q143_be7624fb_12112026.png?v=be7624fb2301)

---

## Q144

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

**Solved independently** (answer withheld)

1. $\text{GLUT-4}$ is a transporter that enables glucose transport into cells, so $A \to IV$.
2. Insulin is a peptide hormone, so $B \to I$.
3. Trypsin is a digestive enzyme, so $C \to II$.
4. Collagen is a protein of the intercellular ground substance, so $D \to III$.
5. $A\text{-}IV,\ B\text{-}I,\ C\text{-}II,\ D\text{-}III$ matches option $1$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q144_1dc472f3_12112026.png?v=1dc472f30100)

---

## Q145

Biology · botany · Respiration in Plants

Identify the step in tricarboxylic acid cycle, which does not involve oxidation of substrate.

- (1) Malic acid $\rightarrow$ Oxaloacetic acid
- (2) Succinic acid $\rightarrow$ Malic acid
- **(3)** Succinyl-CoA $\rightarrow$ Succinic acid
- (4) Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Isocitrate $\rightarrow$ $\alpha$-ketoglutaric acid is an oxidative decarboxylation producing $NADH + H^+$, so it is an oxidation.
2. Malic acid $\rightarrow$ Oxaloacetic acid is a dehydrogenation producing $NADH + H^+$, so it is an oxidation.
3. Succinic acid $\rightarrow$ Malic acid (via fumarate) involves the dehydrogenation producing $FADH_2$, so it is an oxidation.
4. Succinyl-CoA $\rightarrow$ Succinic acid releases CoA and forms $GTP$ (substrate-level phosphorylation) with no electron carrier reduced, so it is not an oxidation: option $3$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q145_1202a3cf_12112026.png?v=1202a3cfe136)

---

## Q146

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

**Solved independently** (answer withheld)

1. In $\mathrm{C_3}$ plants RuBisCO also binds $\mathrm{O_2}$ (oxygenase activity), causing photorespiration and lowering $\mathrm{CO_2}$ fixation, so Statement I is true.
2. In $\mathrm{C_4}$ plants mesophyll cells fix $\mathrm{CO_2}$ with PEP carboxylase and lack RuBisCO, so they cannot photorespire at all; the claim of 'very little photorespiration' there is wrong, so Statement II is false.
3. Statement I true, Statement II false, which is option $3$.

**Subtopic:** Photorespiration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q146_8144d4f4_12112026.png?v=8144d4f4bf76)

---

## Q147

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

**Solved independently** (answer withheld)

1. Monoadelphous stamens (one bundle) occur in China-rose, so $A \rightarrow IV$.
2. Diadelphous stamens (two bundles) occur in pea, so $B \rightarrow II$.
3. Polyadelphous stamens (more than two bundles) occur in Citrus, so $C \rightarrow I$.
4. Epiphyllous stamens (attached to perianth) occur in lily, so $D \rightarrow III$.
5. $A$-IV, $B$-II, $C$-I, $D$-III matches option $1$.

**Subtopic:** Androecium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 39)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q147_77f68a61_12112026.png?v=77f68a618be8)

---

## Q148

Biology · botany · Molecular Basis of Inheritance

Match List I with List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Frederick Griffith | I | Genetic code |
| B | Francois Jacob & Jacque | II | Semi-conservative mode of DNA replication |
| C | Har Gobind Khorana | III | Transformation |
| D | Meselson & Stahl | IV | Lac operon |

- (1) A-III, B-II, C-I, D-IV
- **(2)** A-III, B-IV, C-I, D-II
- (3) A-II, B-III, C-IV, D-I
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Griffith discovered transformation ($A \to III$), Jacob and Monod proposed the lac operon ($B \to IV$), Khorana helped decipher the genetic code ($C \to I$), and Meselson and Stahl proved semi-conservative DNA replication ($D \to II$), so the match is option $2$.

**Subtopic:** The Lac Operon, Experimental Proof that DNA is Semiconservative · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q148_5c1314eb_12112026.png?v=5c1314eb13ce)

---

## Q149

Biology · botany · Strategies for Enhancement in Food Production

Which of the following are fused in somatic hybridization involving two varieties of plants?

- (1) Callus
- (2) Somatic embryos
- **(3)** Protoplasts
- (4) Pollens

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In somatic hybridization, cell walls are digested away and the isolated protoplasts of two varieties are fused to give a somatic hybrid, so the answer is option $3$ (Protoplasts).

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q149_87c9d594_12112026.png?v=87c9d5949edd)

---

## Q150

Biology · botany · Plant Growth and Development

Spraying sugarcane crop with which of the following plant growth regulators, increases the length of stem, thus, increasing the yield?

- (1) Auxin
- **(2)** Gibberellin
- (3) Cytokinin
- (4) Abscisic acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Spraying sugarcane with gibberellins elongates the stem (internodes), raising the yield, so the answer is option $2$ (Gibberellin).

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 40)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q150_eed6fba6_12112026.png?v=eed6fba61167)

---

## Q151

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

**Solved independently** (answer withheld)

1. The action potential originates at the SA node ($E$), passes to the AV node ($C$), then the AV bundle ($A$), the bundle branches ($D$) and the Purkinje fibres ($B$), giving $E\text{-}C\text{-}A\text{-}D\text{-}B$, which is option $1$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q151_e2573e58_12112026.png?v=e2573e58c0fd)

---

## Q152

Biology · zoology · Structural Organisation in Animals

In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on

- (1) $5^{\mathrm{th}}$ segment
- **(2)** $10^{\mathrm{th}}$ segment
- (3) $8^{\mathrm{th}}$ and $9^{\mathrm{th}}$ segment
- (4) $11^{\mathrm{th}}$ segment

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT Class 11 (Structural Organisation in Animals) states that in both sexes the $10^{\mathrm{th}}$ segment bears a pair of jointed filamentous anal cerci, which is option $2$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 41)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q152_1eacc218_12112026.png?v=1eacc21831b1)

---

## Q153

Biology · zoology · Evolution

The flippers of the Penguins and Dolphins are the example of the

- (1) Adaptive radiation
- (2) Natural selection
- **(3)** Convergent evolution
- (4) Divergent evolution

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Penguin flippers (modified bird wings) and dolphin flippers (modified mammal forelimbs) do the same job, swimming, but come from different lineages, so they are analogous structures, which show convergent evolution: option $3$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 41)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q153_5781c8da_12112026.png?v=5781c8dad16e)

---

## Q154

Biology · zoology · Human Reproduction

Which of the following is not a component of Fallopian tube?

- **(1)** Uterine fundus
- (2) Isthmus
- (3) Infundibulum
- (4) Ampulla

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The Fallopian tube (oviduct) has three parts: infundibulum (with fimbriae), ampulla and isthmus; the uterine fundus is the upper dome of the uterus, so option $1$ is not a component.

**Subtopic:** The Female Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q154_d6a0836a_12112026.png?v=d6a0836ac03a)

---

## Q155

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

**Solved independently** (answer withheld)

1. Order the stages from past to recent as $\text{A (H. habilis)} \rightarrow \text{D (H. erectus)} \rightarrow \text{C (H. neanderthalensis)} \rightarrow \text{B (H. sapiens)}$, i.e. A-D-C-B, which is option $4$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 41)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q155_9e28a797_12112026.png?v=9e28a7977f9f)

---

## Q156

Biology · zoology · Chemical Coordination and Integration

Which of the following is not a steroid hormone?

- (1) Cortisol
- (2) Testosterone
- (3) Progesterone
- **(4)** Glucagon

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Glucagon is a peptide (polypeptide) hormone secreted by the $\alpha$-cells of the islets of Langerhans, whereas cortisol, testosterone and progesterone are cholesterol-derived steroid hormones, so the answer is option $4$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q156_d5f21880_12112026.png?v=d5f21880e165)

---

## Q157

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

**Solved independently** (answer withheld)

1. $\alpha$-1 antitrypsin is used to treat emphysema, so A-III.
2. The cryIAb gene product controls the corn borer, so B-IV.
3. The cryIAc gene product controls the cotton bollworm, so C-I.
4. Enzyme replacement therapy (giving ADA) treats ADA deficiency, so D-II.
5. A-III, B-IV, C-I, D-II matches option $3$.

**Subtopic:** Pest Resistant Plants and Bt Cotton, Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 42)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q157_eb0dc83d_12112026.png?v=eb0dc83deabf)

---

## Q158

Biology · zoology · Cell Cycle and Cell Division

Following are the stages of cell division :
Choose the correct sequence of stages from the options given below :

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

**Solved independently** (answer withheld)

1. Interphase runs in the order $G_1 \rightarrow S \rightarrow G_2$, i.e. $E \rightarrow C \rightarrow A$.
2. The M phase follows: karyokinesis (nuclear division, $D$) comes before cytokinesis (cytoplasmic division, $B$).
3. Full sequence $E-C-A-D-B$, which is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q158_575f3d08_12112026.png?v=575f3d0892ab)

---

## Q159

Biology · zoology · Evolution

Which one of the following factors will not affect the Hardy-Weinberg equilibrium?

- (1) Genetic recombination
- (2) Genetic drift
- (3) Gene migration
- **(4)** Constant gene pool

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT lists five factors affecting Hardy-Weinberg equilibrium: gene migration (gene flow), genetic drift, mutation, genetic recombination and natural selection; a constant gene pool is the equilibrium state itself, so option $4$ does not affect it.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q159_464bb81f_12112026.png?v=464bb81f0263)

---

## Q160

Biology · zoology · Locomotion and Movement

Which of the following are Autoimmune disorders?
Choose the most appropriate answer from the options given below:

- (A) Myasthenia gravis
- (B) Rheumatoid arthritis
- (C) Gout
- (D) Muscular dystrophy
- (E) Systemic Lupus Erythematosus (SLE)

- (1) A, B & D only
- **(2)** B & E only
- (3) B, C & E only
- (4) C, D & E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Rheumatoid arthritis ($B$) and SLE ($E$) are autoimmune disorders.
2. Gout ($C$) is caused by uric acid crystal deposition in joints, so it is not autoimmune.
3. Muscular dystrophy ($D$) is a genetic degeneration of skeletal muscle, so it is not autoimmune.
4. Myasthenia gravis ($A$) is also autoimmune (antibodies against acetylcholine receptors at the neuromuscular junction).
5. Options $1$, $3$ and $4$ each include $C$ or $D$, so they are wrong; option $2$ (B & E only) is the only option with all members autoimmune.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 43)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q160_523aafc1_12112026.png?v=523aafc144ba)

---

## Q161

Biology · zoology · Human Health and Disease

Match List I with List II : Choose the correct answer from the options given below:

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

**Solved independently** (answer withheld)

1. Typhoid is caused by the bacterium $Salmonella\ typhi$, so A-IV.
2. Leishmaniasis is caused by the protozoan $Leishmania$, so B-III.
3. Ringworm is caused by fungi ($Microsporum$, $Trichophyton$, $Epidermophyton$), so C-I.
4. Filariasis is caused by the nematodes $Wuchereria$ ($W.\ bancrofti$, $W.\ malayi$), so D-II.
5. The match A-IV, B-III, C-I, D-II is option $2$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 43)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q161_3fe3c364_12112026.png?v=3fe3c36430fd)

---

## Q162

Biology · zoology · Breathing and Exchange of Gases

Match List I with List II
Choose the correct answer from the options given below :

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

**Solved independently** (answer withheld)

1. Expiratory capacity $EC = TV + ERV$, so A matches II.
2. Functional residual capacity $FRC = ERV + RV$, so B matches IV.
3. Vital capacity $VC = ERV + TV + IRV$, so C matches I.
4. Inspiratory capacity $IC = TV + IRV$, so D matches III.
5. A-II, B-IV, C-I, D-III is option $1$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 43)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q162_2f774b35_12112026.png?v=2f774b3577ed)

---

## Q163

Biology · zoology · Principles of Inheritance and Variation

Match List I with List II

| List-I | | List-II | |
|---|---|---|---|
| A | Down’s syndrome | I | $11^{\text{th}}$ chormosome |
| B | $\alpha$-Thalassemia | II | ‘X’ chromosome |
| C | $\beta$-Thalassemia | III | $21^{\text{st}}$ chromosome |
| D | Klinefelter’s syndrome | IV | $16^{\text{th}}$ chromosome |

- (1) A-I, B-II, C-III, D-IV
- (2) A-II, B-III, C-IV, D-I
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-I, C-II, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Down's syndrome is trisomy of the $21^{\text{st}}$ chromosome, so A-III.
2. $\alpha$-Thalassemia is controlled by genes HBA1 and HBA2 on the $16^{\text{th}}$ chromosome, so B-IV.
3. $\beta$-Thalassemia is controlled by the HBB gene on the $11^{\text{th}}$ chromosome, so C-I.
4. Klinefelter's syndrome (XXY) involves an extra 'X' chromosome, so D-II.
5. A-III, B-IV, C-I, D-II matches option $3$.

**Subtopic:** Chromosomal Disorders, Thalassemia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q163_4f39f09a_12112026.png?v=4f39f09add51)

---

## Q164

Biology · zoology · Chemical Coordination and Integration

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R :
In the light of the above statements, choose the correct answer from the options given below :

- (Assertion A) FSH acts upon ovarian follicles in female and Leydig cells in male.
- (Reason R) Growing ovarian follicles secrete estrogen in female while interstitial cells secrete androgen in male human being.

- (1) Both A and R are true and R is the correct explanation of A
- (2) Both A and R are true but R is NOT the correct explanation of A
- (3) A is true but R is false
- **(4)** A is false but R is true

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In males, FSH acts on Sertoli cells, while LH acts on Leydig cells; so Assertion A is false.
2. Growing ovarian follicles secrete estrogen and interstitial (Leydig) cells secrete androgens; so Reason R is true.
3. A false, R true, which is option $4$.

**Subtopic:** The Pituitary Gland, Gonads · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 44)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q164_bf4c0ce8_12112026.png?v=bf4c0ce8ea34)

---

## Q165

Biology · zoology · Animal Kingdom

Match List I with List II :
Choose the correct answer from the options given below

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

**Solved independently** (answer withheld)

1. Pleurobrachia is a comb jelly, so $A \rightarrow II$ (Ctenophora).
2. Radula is the file-like rasping feeding organ of molluscs, so $B \rightarrow I$ (Mollusca).
3. Stomochord is the rudimentary notochord-like structure in the proboscis of hemichordates, so $C \rightarrow IV$ (Hemichordata).
4. Air bladder regulates buoyancy in bony fishes, so $D \rightarrow III$ (Osteichthyes).
5. $A\text{-}II, B\text{-}I, C\text{-}IV, D\text{-}III$ matches option $2$.

**Subtopic:** Classification of Animals · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 44)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q165_75ebdb7d_12112026.png?v=75ebdb7dfec1)

---

## Q166

Biology · zoology · Cell Cycle and Cell Division

Match List I with List II

Choose the correct answer from the options given below

| List-I | | List-II | |
|---|---|---|---|
| List I | (Sub Phases of Prophase I) | List II | (Specific characters) |
| A | Diakinesis | I | Synaptonemal complex formation |
| B | Pachytene | II | Completion of terminalisation of chiasmata |
| C | Zygotene | III | Chromosomes look like thin threads |
| D | Leptotene | IV | Appearance of recombination nodules |

- (1) A-IV, B-II, C-III, D-I
- (2) A-I, B-II, C-IV, D-III
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Diakinesis (A) is marked by completion of terminalisation of chiasmata, so $A \rightarrow II$.
2. Pachytene (B) is marked by the appearance of recombination nodules, so $B \rightarrow IV$.
3. Zygotene (C) is marked by synapsis with synaptonemal complex formation, so $C \rightarrow I$.
4. Leptotene (D) chromosomes appear as thin threads, so $D \rightarrow III$.
5. $A-II, B-IV, C-I, D-III$ matches option $3$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 45)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q166_84c44c81_12112026.png?v=84c44c811db5)

---

## Q167

Biology · zoology · Biotechnology: Principles and Processes

The “Ti plasmid” of Agrobacterium tumefaciens stands for

- (1) Tumour inhibiting plasmid
- (2) Tumor independent plasmid
- **(3)** Tumor inducing plasmid
- (4) Temperature independent plasmid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The Ti plasmid of $Agrobacterium\ tumefaciens$ causes tumours (crown gall) in dicot plants, so Ti = Tumor inducing, which is option $3$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q167_715d1a01_12112026.png?v=715d1a01129f)

---

## Q168

Biology · zoology · Human Health and Disease

Match List I with List II :

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cocaine | I | Effective sedative in surgery |
| B | Heroin | II | Connabis sativa |
| C | Morphine | III | Erythroxylum |
| D | Marijuana | IV | Papaver somniferum |

- (1) A-IV, B-III, C-I, D-II
- (2) A-I, B-III, C-II, D-IV
- (3) A-II, B-I, C-III, D-IV
- **(4)** A-III, B-IV, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Cocaine is obtained from the coca plant $Erythroxylum\ coca$, so $A \to III$.
2. Heroin (diacetylmorphine) is derived from morphine, which comes from the poppy $Papaver\ somniferum$, so $B \to IV$.
3. Morphine is a very effective sedative and painkiller used in surgery, so $C \to I$.
4. Marijuana is obtained from the inflorescences of $Cannabis\ sativa$, so $D \to II$.
5. $A\text{-}III, B\text{-}IV, C\text{-}I, D\text{-}II$ matches option $4$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 45)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q168_0174a9ba_12112026.png?v=0174a9ba019b)

---

## Q169

Biology · zoology · Molecular Basis of Inheritance

Which one is the correct product of DNA dependent RNA polymerase to the given template? 3’TACATGGCAAATATCCATTCA5’

- **(1)** 5’AUGUACCGUUUAUAGGUAAGU3’
- (2) 5’AUGUAAAGUUUAUAGGUAAGU3’
- (3) 5’AUGUACCGUUUAUAGGGAAGU3’
- (4) 5’ATGTACCGTTTATAGGTAAGT3’

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. DNA-dependent RNA polymerase synthesises RNA complementary and antiparallel to the template strand, reading $3'\to5'$ and building $5'\to3'$, using U instead of T.
2. Complementing $3'$-TACATGGCAAATATCCATTCA-$5'$ base by base gives $5'$-AUGUACCGUUUAUAGGUAAGU-$3'$.
3. Option 4 contains T (DNA), option 2 has AAAG in place of CCG, option 3 has GGG in place of GGU; only option $1$ matches exactly.

**Subtopic:** Transcription · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 46)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q169_70add112_12112026.png?v=70add1122ff3)

---

## Q170

Biology · zoology · Neural Control and Coordination

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pons | I | Provides additional space for Neurons, regulates posture and balance. |
| B | Hypothalamus | II | Controls respiration and gastric secretions. |
| C | Medulla | III | Connects different regions of the brain. |
| D | Cerebellum | IV | Neurosecretory cells |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-I, B-III, C-II, D-IV
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Pons consists of fibre tracts that interconnect different regions of the brain, so $A \to III$.
2. Hypothalamus contains neurosecretory cells that secrete hypothalamic hormones, so $B \to IV$.
3. Medulla contains centres controlling respiration, cardiovascular reflexes and gastric secretions, so $C \to II$.
4. Cerebellum has a highly convoluted surface giving additional space for neurons and regulates posture and balance, so $D \to I$.
5. $A-III,\ B-IV,\ C-II,\ D-I$ matches option $2$.

**Subtopic:** Hindbrain, Forebrain · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 46)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q170_1223e365_12112026.png?v=1223e365c493)

---

## Q171

Biology · zoology · Biomolecules

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Lipase | I. | Peptide bond |
| B. | Nuclease | II. | Ester bond |
| C. | Protease | III. | Glycosidic bond |
| D. | Amylase | IV | Phosphodiester bond |

- (1) A-IV, B-II, C-III, D-I
- (2) A-III, B-II, C-I, D-IV
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-IV, B-I, C-III, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Lipase hydrolyses lipids by breaking the $\text{ester bond}$, so $A \to II$.
2. Nuclease hydrolyses nucleic acids by breaking the $\text{phosphodiester bond}$, so $B \to IV$.
3. Protease hydrolyses proteins by breaking the $\text{peptide bond}$, so $C \to I$.
4. Amylase hydrolyses starch by breaking the $\text{glycosidic bond}$, so $D \to III$.
5. $A\text{-}II,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}III$ matches option $3$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q171_788c7e8c_12112026.png?v=788c7e8c0d16)

---

## Q172

Biology · zoology · Reproductive Health

Which of the following is not a natural/traditional contraceptive method?

- (1) Coitus interruptus
- (2) Periodic abstinence
- (3) Lactational amenorrhea
- **(4)** Vaults

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Coitus interruptus, periodic abstinence and lactational amenorrhea are natural/traditional methods, while vaults are a barrier method, so the answer is option $4$.

**Subtopic:** Natural Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q172_7869c994_12112026.png?v=7869c994011a)

---

## Q173

Biology · zoology · Structural Organisation in Animals

Three types of muscles are given as a, b and c. Identify the correct matching pair along with their location in human body: Name of muscle/location

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q173_6b11b08e_12112026.png?v=6b11b08e4ad0)

- (1) (a) Smooth - Toes (b) Skeletal – Legs (c) Cardiac – Heart
- **(2)** (a) Skeletal - Triceps (b) Smooth – Stomach (c) Cardiac – Heart
- (3) (a) Skeletal - Biceps (b) Involuntary – Intestine (c) Smooth – Heart
- (4) (a) Involuntary – Nose tip (b) Skeletal – Bone (c) Cardiac – Heart

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Figure $(a)$ shows long, cylindrical, unbranched striated fibres with many peripheral nuclei, so it is skeletal muscle, found attached to bones, e.g. the triceps.
2. Figure $(b)$ shows spindle-shaped, unstriated cells with one central nucleus each, so it is smooth (involuntary) muscle, found in the walls of visceral organs such as the stomach.
3. Figure $(c)$ shows striated, branched fibres joined to one another, so it is cardiac muscle, found only in the heart.
4. Option $3$ fails because it calls $(c)$ smooth muscle in the heart, and options $1$ and $4$ give wrong locations for $(a)$ (smooth muscle in the toes, involuntary muscle in the nose tip). This leaves option $2$.

**Subtopic:** Muscle Tissue and Neural Tissue · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 47)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q173_20c9b6ee_12112026.png?v=20c9b6eeb62f)

---

## Q174

Biology · zoology · Biotechnology: Principles and Processes

Which of the following statements is incorrect?

- (1) A bio-reactor provides optimal growth conditions for achieving the desired product
- (2) Most commonly used bio-reactors are of stirring type
- **(3)** Bio-reactors are used to produce small scale bacterial cultures
- (4) Bio-reactors have an agitator system, an oxygen delivery system foam control system

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Bioreactors are large vessels (about $100$ to $1000$ litres) in which raw materials are biologically converted to products, so they are used for large-scale, not small-scale, cultures; statement $4$ is incorrect while statements $1$, $2$ and $3$ are correct, giving option $3$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q174_9fe38118_12112026.png?v=9fe38118590b)

---

## Q175

Biology · zoology · Human Health and Disease

Given below are two statements: One is labelled as Assertion A and the other is labelled as Reason R: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) Breast-feeding during initial period of infant growth is recommended by doctors for bringing a healthy baby.
- (Reason R) Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby.

- **(1)** Both A and R are correct and R is the correct explanation of A
- (2) Both A and R are correct but R is NOT the correct explanation of A
- (3) A is correct but R is not correct
- (4) A is not correct but R is correct

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Assertion A is true: NCERT states that breast-feeding during the initial period of infant growth is recommended by doctors for bringing up a healthy baby.
2. Reason R is true: colostrum contains several antibodies (IgA) absolutely essential to develop resistance for the newborn, and this passive immunity is the reason breast-feeding is recommended, so R explains A, giving option $1$.

**Subtopic:** Active and Passive Immunity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 48)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q175_7c8fbb83_12112026.png?v=7c8fbb83d394)

---

## Q176

Biology · zoology · Breathing and Exchange of Gases

Which of the following factors are favourable for the formation of oxyhaemoglobin in alveoli?

- (1) High $p\mathrm{O_2}$ and High $p\mathrm{CO_2}$
- **(2)** High $p\mathrm{O_2}$ and Lesser $\mathrm{H^+}$ concentration
- (3) Low $p\mathrm{CO_2}$ and High $\mathrm{H^+}$ concentration
- (4) Low $p\mathrm{CO_2}$ and High temperature

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Oxyhaemoglobin formation is favoured by high $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, lesser $\mathrm{H^+}$ concentration and lower temperature (conditions in the alveoli).
2. Option 4 has high temperature, option 1 has high $\mathrm{pCO_2}$ and option 3 has high $\mathrm{H^+}$, each of which is unfavourable.
3. Option $2$ (high $\mathrm{pO_2}$ and lesser $\mathrm{H^+}$) has both factors favourable, so the answer is option $2$.

**Subtopic:** Transport of Gases · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 48)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q176_ce4c1af9_12112026.png?v=ce4c1af90491)

---

## Q177

Biology · zoology · Human Health and Disease

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Common cold | I | *Plasmodium* |
| B | Haemozoin | II | Typhoid |
| C | Widal test | III | Rhinoviruses |
| D | Allergy | IV | Dust mites |

- (1) A-II, B-IV, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- **(3)** A-III, B-I, C-II, D-IV
- (4) A-IV, B-II, C-III, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Common cold is caused by Rhinoviruses, so $A \to III$.
2. Haemozoin is the toxin released by Plasmodium, so $B \to I$.
3. Widal test confirms typhoid, so $C \to II$.
4. Dust mites are a common allergen, so $D \to IV$.
5. $A\text{-}III, B\text{-}I, C\text{-}II, D\text{-}IV$ is option $3$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q177_8b356f59_12112026.png?v=8b356f59e301)

---

## Q178

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

**Solved independently** (answer withheld)

1. Statement A: Annelids have a true coelom lined by mesoderm, so $A$ is true.
2. Statement B: Poriferans are cellular-level animals with no coelom, not pseudocoelomates, so $B$ is false.
3. Statement C: Aschelminthes have a pseudocoelom, not an acoelomate body, so $C$ is false.
4. Statement D: Platyhelminthes are acoelomates, not pseudocoelomates, so $D$ is false.
5. Only $A$ is correct, which is option $2$ (A only).

**Subtopic:** Basis of Classification · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 48)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q178_fa31725d_12112026.png?v=fa31725de6bd)

---

## Q179

Biology · zoology · Reproductive Health

Match List I with List II
Choose the correct answer from the option given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Non-medicated IUD | I | Multiload 375 |
| B | Copper releasing IUD | II | Progestogens |
| C | Hormone releasing IUD | III | Lipper loop |
| D | Implants | IV | LNG-20 |

- (1) A-III, B-I, C-II, D-IV
- (2) A-I, B-III, C-IV, D-II
- (3) A-IV, B-I, C-II, D-III
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Non-medicated IUD is the Lippes loop, so $A \rightarrow III$.
2. Copper releasing IUD is Multiload 375, so $B \rightarrow I$.
3. Hormone releasing IUD is LNG-20, so $C \rightarrow IV$.
4. Implants contain progestogens (alone or with estrogen), so $D \rightarrow II$.
5. $A\text{-}III, B\text{-}I, C\text{-}IV, D\text{-}II$ is option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q179_0c37e1b7_12112026.png?v=0c37e1b76d77)

---

## Q180

Biology · zoology · Excretory Products and Their Elimination

Given below are two statements :
In the light of the above statements, choose the correct answer from the option given below :

- (Statement I) In the nephron, the descending limb of loop of Henle is impermeable to water and permeable to electrolytes.
- (Statement II) The proximal convoluted tubule is lined by simple columnar brush border epithelium and increases the surface area for reabsorption.

- (1) Both statement I and Statement II are true
- **(2)** Both statement I and Statement II are false
- (3) Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement I: NCERT states the descending limb of loop of Henle is permeable to water but almost impermeable to electrolytes, so Statement I (impermeable to water, permeable to electrolytes) is false.
2. Statement II: NCERT states the PCT is lined by simple cuboidal brush border epithelium which increases the surface area for reabsorption; the statement says simple columnar, so Statement II is false.
3. Both statements are false, which is option $2$.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 49)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q180_f95c4fa9_12112026.png?v=f95c4fa927d6)

---

## Q181

Biology · zoology · Biotechnology: Principles and Processes

The following diagram shown restriction sites in $E.$ coli cloning vector pBR322. Find the role of ‘X’ and ‘Y’ gens :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q181_5589b09f_12112026.png?v=5589b09f2aa1)

- (1) The gene ‘X’  is responsible for resistance to antibiotics and ‘Y’ for protein involved in the replication of Plasmid.
- **(2)** The gene ‘X’ is responsible for controlling the copy number of the linked DNA and ‘Y’ for protein involved in the replication of Plasmid.
- (3) The gene ‘X’ is for protein involved in replication of Plasmid and ‘Y’ for resistance to antibiotics.
- (4) Gene ’X’ is responsible for recognitions sites and ‘Y’ is responsible for antibiotic resistance

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In pBR322, $amp^R$ carries the PstI and PvuI sites and $tet^R$ carries the BamHI and SalI sites, so neither X nor Y is an antibiotic-resistance gene.
2. X is at the bottom-left of the map, where $ori$ sits; $ori$ controls the copy number of the linked DNA.
3. Y is next to the PvuII site, where $rop$ sits; $rop$ codes for proteins involved in plasmid replication.
4. So X = $ori$ and Y = $rop$, which is option $2$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 49)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q181_539b256f_12112026.png?v=539b256f29df)

---

## Q182

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

**Solved independently** (answer withheld)

1. Axoneme is the microtubule core of cilia and flagella, so $A \rightarrow II$.
2. The centriole shows a cartwheel arrangement of peripheral triplet fibrils, so $B \rightarrow I$.
3. Cristae are infoldings of the inner mitochondrial membrane, so $C \rightarrow IV$.
4. A satellite is a small fragment beyond the secondary constriction of some chromosomes, so $D \rightarrow III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ is option $4$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 50)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q182_1fb7bb8f_12112026.png?v=1fb7bb8f1b79)

---

## Q183

Biology · zoology · Animal Kingdom

Match List I with List II :
Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Pterophyllum | I | Hag fish |
| B | Myxine | II | Saw fish |
| C | Pristis | III | Angel fish |
| D | Exocoetus | IV | Flying fish |

- (1) A-II, B-I, C-IIII, D-IV
- **(2)** A-III, B-I, C-II, D-IV
- (3) A-IV, B-I, C-II, D-III
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\text{Pterophyllum}$ is the angel fish, so $A \to III$.
2. $\text{Myxine}$ is the hag fish, so $B \to I$.
3. $\text{Pristis}$ is the saw fish, so $C \to II$.
4. $\text{Exocoetus}$ is the flying fish, so $D \to IV$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}II,\ D\text{-}IV$ matches option $2$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q183_bbdcbb45_12112026.png?v=bbdcbb456a29)

---

## Q184

Biology · zoology · Locomotion and Movement

Match List I with List II : Choose the correct answer from the options given below :

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

**Solved independently** (answer withheld)

1. Fibrous joints (A) join the flat skull bones as sutures and allow no movement, so $A \to III$.
2. Cartilaginous joints (B) join adjacent vertebrae and allow limited movement, so $B \to I$.
3. Hinge joints (C) occur at the knee and help in locomotion, so $C \to IV$.
4. Ball and socket joints (D) occur between the humerus and pectoral girdle and allow rotational movement, so $D \to II$.
5. $A-III, B-I, C-IV, D-II$ is option $4$.

**Subtopic:** Joints · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q184_1303bf79_12112026.png?v=1303bf79cbd5)

---

## Q185

Biology · zoology · Human Reproduction

Given below are two statements:
In the light of the above above statements, choose the correct answer from the options given below :

- (Statement I) The presence or absence of hymen is not a reliable indicator of virginity.
- (Statement II) The hymen is torn during the first coitus only.

- (1) Both Statement I and Statement II are true
- (2) Both Statement I and Statement II are false
- **(3)** Statement I is true but Statement II is false
- (4) Statement I is false but Statement II is true

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT says the hymen can be torn by a sudden fall or jolt, by inserting a vaginal tampon, or during active sports such as horseback riding or cycling, and in some women it persists even after coitus. So Statement I is true and Statement II is false, which is option $3$.

**Subtopic:** Female External Genitalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q185_1f4c59c6_12112026.png?v=1f4c59c69d4a)

---

## Q186

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

**Solved independently** (answer withheld)

1. Gause's competitive exclusion principle (NCERT): two closely related species competing for the same resources cannot coexist indefinitely; Statement I says 'different resources', so it is false, while Statement II restates NCERT's wording that the competitively inferior one will be eliminated, which may be true if resources are limiting, so it is true; this is option $4$.

**Subtopic:** Competition · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q186_ff3ea6bb_12112026.png?v=ff3ea6bb1733)

---

## Q187

Biology · zoology · Structural Organisation in Animals

Match List I with List II related to digestive system of cockroach.

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | The structures used for storing of food. | I | Gizzard |
| B | Ring of 6-8 blind tubules at junction of foregut and midgut. | II | Gastric Caeca |
| C | Ring of 100-150 yellow coloured thin filaments at junction of midgut and hindgut. | III | Malpighian tubules |
| D | The structures used for grinding the food. | IV | Crop |

- **(1)** A-IV, B-II, C-III, D-I
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-II, C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Food storage in cockroach is done by the crop, so $A \to IV$.
2. The ring of 6-8 blind tubules at the foregut-midgut junction is the gastric caeca, so $B \to II$.
3. The ring of 100-150 yellow filaments at the midgut-hindgut junction is the Malpighian tubules, so $C \to III$.
4. Grinding of food is done by the gizzard (proventriculus), so $D \to I$.
5. $A$-IV, $B$-II, $C$-III, $D$-I is option $1$.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q187_5004c966_12112026.png?v=5004c96680d8)

---

## Q188

Biology · zoology · Animal Kingdom

The following are the statements about non-chordates: Choose the most appropriate answer from the options given below:

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

**Solved independently** (answer withheld)

1. A: pharyngeal gill slits are absent in non-chordates, so A is false.
2. B: notochord is absent in non-chordates, so B is true.
3. C: the central nervous system of non-chordates is ventral, solid and double, so C is false.
4. D: the heart of non-chordates, if present, is dorsal, so D is true.
5. E: a post-anal tail is absent in non-chordates, so E is true.
6. True statements are $B$, $D$ and $E$, which is option $3$.

**Subtopic:** Phylum – Chordata · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q188_b7278ad8_12112026.png?v=b7278ad8bda4)

---

## Q189

Biology · zoology · Excretory Products and Their Elimination

Choose the correct statement given below regarding juxta medullary nephron.

- (1) Juxta medullary nephrons are located in the columns of Bertini.
- (2) Renal corpuscle of juxta medullary nephron lies in the outer portion of the renal medulla.
- **(3)** Loop of Henle of juxta medullary nephron runs deep into medulla.
- (4) Juxta medullary nephrons outnumber the cortical nephrons.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Cortical nephrons outnumber juxtamedullary ones, their corpuscles lie in the inner cortex rather than the medulla or the columns of Bertini, and their long loops of Henle run deep into the medulla, so option $3$ is correct.

**Subtopic:** Human Excretory System · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 52)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q189_3f469b6d_12112026.png?v=3f469b6d8924)

---

## Q190

Biology · zoology · Neural Control and Coordination

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The cerebral hemispheres are connected by nerve tract known as corpus callosum.
- (Statement II) The brain stem consists of the medulla oblongata, pons and cerebrum.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Statement I: the two cerebral hemispheres are connected by a tract of nerve fibres called the corpus callosum, so Statement I is correct.
2. Statement II: the brain stem is formed by the midbrain, pons and medulla oblongata; the cerebrum is part of the forebrain, so Statement II is incorrect.
3. I correct and II incorrect matches option $3$.

**Subtopic:** Forebrain, Hindbrain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 52)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q190_35d66882_12112026.png?v=35d66882df6f)

---

## Q191

Biology · zoology · Human Health and Disease

Given below are two statements : In the light of above statements, choose the most appropriate answer from the options given below :

- (Statement I) Bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
- (Statement II) Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes.

- **(1)** Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- (3) Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: bone marrow is the main lymphoid organ where all blood cells, including lymphocytes, are produced, so it is correct.
2. Statement II: NCERT states that bone marrow and thymus provide micro-environments for the development and maturation of T-lymphocytes, so it is correct.
3. Both statements are correct, which is option $1$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 53)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q191_e63706e2_12112026.png?v=e63706e224b9)

---

## Q192

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

**Solved independently** (answer withheld)

1. The substrate first binds to the active site of the enzyme: step $E$.
2. Binding forms the enzyme-substrate complex: step $A$.
3. Within the complex the chemical bonds of the substrate are broken: step $D$.
4. The products are released from the active site: step $C$.
5. The free enzyme is then ready to bind another substrate: step $B$.
6. The sequence $E \rightarrow A \rightarrow D \rightarrow C \rightarrow B$ is option $1$.

**Subtopic:** Enzymes and Chemical Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q192_92c4e014_12112026.png?v=92c4e014e612)

---

## Q193

Biology · zoology · Human Reproduction

Identify the correct option (A), (B), (C), (D) with respect to spermatogenesis.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/figures_agent/q193_6113e1f7_12112026.png?v=6113e1f7fbd2)

- **(1)** FSH, Leydig cells, Sertoli cells, Spermiogenesis.
- (2) ICSH, Interstitial cells, Leydig cells, spermiogenesis.
- (3) FSH, Sertoli cells, Leydig cells, spermatogenesis.
- (4) ICSH, Leydig cells, Sertoli cells, spermatogenesis.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. GnRH stimulates release of LH and FSH, so (A) $=$ FSH.
2. LH acts on Leydig cells to stimulate androgen synthesis, so (B) $=$ Leydig cells.
3. FSH acts on Sertoli cells, so (C) $=$ Sertoli cells.
4. Sertoli cells secrete factors that help spermiogenesis (spermatids to sperm), so (D) $=$ spermiogenesis.
5. FSH, Leydig cells, Sertoli cells, spermiogenesis matches option $1$.

**Subtopic:** Male Gametogenesis (Spermatogenesis), Hormonal Regulation of Reproduction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 53)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q193_52f4f7d3_12112026.png?v=52f4f7d3ba4f)

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

**Solved independently** (answer withheld)

1. Mesozoic Era (A) is the age of reptiles, with birds arising in it: $A \to III$.
2. Proterozoic Era (B) holds only lower invertebrates: $B \to I$.
3. Cenozoic Era (C) is the age of mammals: $C \to IV$.
4. Paleozoic Era (D) sees fishes and amphibians: $D \to II$.
5. $A\text{-}III,\ B\text{-}I,\ C\text{-}IV,\ D\text{-}II$ is option $4$.

**Subtopic:** Brief Account of Evolution · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 54)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q194_82cb7d0c_12112026.png?v=82cb7d0c7a7e)

---

## Q195

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

**Solved independently** (answer withheld)

1. Unicellular glandular epithelium consists of isolated cells such as the goblet cells of the alimentary canal: $A \rightarrow III$.
2. Compound epithelium covers the moist surface of the buccal cavity: $B \rightarrow IV$.
3. Multicellular glandular epithelium forms clusters of cells, as in the salivary glands: $C \rightarrow I$.
4. Among the remaining choices the pancreas has endocrine function (islets of Langerhans): $D \rightarrow II$.
5. $A\text{-}III,\ B\text{-}IV,\ C\text{-}I,\ D\text{-}II$ matches option $3$.

**Subtopic:** Animal Tissues: Epithelial Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q195_7f8fc413_12112026.png?v=7f8fc4137327)

---

## Q196

Biology · zoology · Molecular Basis of Inheritance

Match List I with List II:

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

**Solved independently** (answer withheld)

1. RNA polymerase III transcribes tRNA, 5S rRNA and snRNAs, so $A \rightarrow IV$.
2. In prokaryotes, termination of transcription is brought about by the Rho factor, so $B \rightarrow III$.
3. Splicing of exons (removal of introns) is carried out by snRNPs of the spliceosome, so $C \rightarrow I$.
4. The TATA box is part of the promoter, so $D \rightarrow II$.
5. $A\text{-}IV,\ B\text{-}III,\ C\text{-}I,\ D\text{-}II$ matches option $4$.

**Subtopic:** Transcription · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 54)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q196_fbba8b22_12112026.png?v=fbba8b22e9d3)

---

## Q197

Biology · zoology · Principles of Inheritance and Variation

As per ABO blood grouping system, the blood group of father is $\mathrm{B^{+}}$, mother is $\mathrm{A^{+}}$ and child is $\mathrm{O^{+}}$. Their respective genotype can be Choose the most appropriate answer from the options given below :

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

**Solved independently** (answer withheld)

1. Blood group O is only possible with genotype $ii$, so the child is $ii$ and got one $i$ allele from each parent.
2. So the father (group B) must be $I^{B}i$ and the mother (group A) must be $I^{A}i$.
3. Statement A ($I^{B}i/I^{A}i/ii$) matches. B fails because homozygous parents cannot have an $ii$ child, and C, D and E give the wrong phenotypes.
4. Only A is correct, which is option $1$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q197_78199b63_12112026.png?v=78199b6372a7)

---

## Q198

Biology · zoology · Cell: The Unit of Life

> ⚠ The booklet prints the SAME question twice: q198 and q199 both read "Statement I: Mitochondria and chloroplasts both double membranes bound organelles. Statement II: Inner membrane of mitochondria is relatively less permeable, as compared chloroplast." with identical options, but q198 is keyed (2) and q199 (3). q199's key matches 2024_S1 q191 ("Statement I is correct but Statement II is incorrect"), so q199 is the real question and q198 is a misprint: the question that belonged at q198 was not printed, and its key (2) cannot be checked against anything printed. Treat q198 as unusable.

> ⚠ The independent solve chose (1); the booklet prints (2).

Given below are two statements:
In the light of the above statements, choose the mis appropriate answer from the options given below

- (Statement I) Mitochondria and chloroplasts both double membranes bound organelles.
- (Statement II) Inner membrane of mitochondria is relatively less permeable, as compared chloroplast.

- (1) Both Statement I and Statement II are correct.
- **(2)** Both Statement I and Statement II are incorrect.
- (3) Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (2) · independent solve: (1) · differs

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts each have an outer and an inner membrane, so Statement I is correct.
2. The inner mitochondrial membrane is highly selective (most solutes need specific carriers), so it is relatively less permeable; Statement II is taken as correct.
3. Both statements correct $\Rightarrow$ option $1$.

**Subtopic:** Mitochondria, Plastids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q198_3adb100f_12112026.png?v=3adb100f4d9b)

---

## Q199

Biology · zoology · Cell: The Unit of Life

> ⚠ The booklet prints this question twice (as q198 and q199) with identical text and options but different keys: q198 (2), q199 (3). It also prints "choose the mis appropriate answer" (read: most appropriate) and "as compared chloroplast" (read: as compared to chloroplast). q199's key (3) matches 2024_S1 q191, so this is the real question; see the note on q198.

> ⚠ The independent solve chose (1); the booklet prints (3).

Given below are two statements:
In the light of the above statements, choose the mis appropriate answer from the options given below

- (Statement I) Mitochondria and chloroplasts both double membranes bound organelles.
- (Statement II) Inner membrane of mitochondria is relatively less permeable, as compared chloroplast.

- (1) Both Statement I and Statement II are correct.
- (2) Both Statement I and Statement II are incorrect.
- **(3)** Statement I is correct but Statement II is incorrect.
- (4) Statement I is incorrect but Statement II is correct.

**Answer** — booklet: (3) · independent solve: (1) · differs

**Solved independently** (answer withheld)

1. Mitochondria and chloroplasts are both bounded by an outer and an inner membrane, so Statement I is correct.
2. The inner mitochondrial membrane is a highly impermeable membrane (ions and metabolites cross only via specific carriers), so it is relatively less permeable; Statement II is taken as correct.
3. Both statements correct, which is option $1$.

**Subtopic:** Mitochondria, Plastids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q199_b7ea1ff1_12112026.png?v=b7ea1ff1fbe3)

---

## Q200

Biology · zoology · Chemical Coordination and Integration

Match List I with List II :
Choose the correct answer from the options given below

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

**Solved independently** (answer withheld)

1. Exophthalmic goiter (Graves' disease) is hypersecretion of thyroid hormone with protruding eyeballs: $A \to III$.
2. Acromegaly results from excessive secretion of growth hormone in adults: $B \to IV$.
3. Cushing's syndrome results from excess cortisol, giving moon face and hyperglycemia: $C \to I$.
4. Cretinism results from hyposecretion of thyroid hormone, with stunted growth: $D \to II$.
5. $A\text{-}III, B\text{-}IV, C\text{-}I, D\text{-}II$ matches option $4$.

**Subtopic:** Endocrine Disorders · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 56)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/12112026/neet_papers/2024/2024_Q3/crops/q200_f8ce580c_12112026.png?v=f8ce580ccf59)

