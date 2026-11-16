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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The string tension in a horizontal circle is the centripetal force, so at fixed radius it grows as the square of the angular speed
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The square is applied to the speed ratio written old-over-new, $\left(\frac{\omega}{2\omega}\right)^2=\frac{1}{4}$, so the tension comes out as $\frac{T}{4}$ when the same square the other way up gives $4T$.
- **Why:** This question requires scaling the tension by the square of the speed at a fixed radius, demonstrated by 'If speed becomes $2\omega$ while keeping the same radius' and by options that are all multiples of $T$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Ten equal parts of a wire carry a tenth of its resistance each; in series they add, and $n$ equal parts in parallel give one part's resistance divided by $n$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The parallel rule $\frac{R}{n}$ is applied to the five parts taken together, $\frac{50}{5}=10\,\Omega$, instead of to one part, $\frac{10}{5}=2\,\Omega$, so the two blocks add to $60\,\Omega$ rather than $52\,\Omega$.
- **Why:** This question requires combining five equal parts in series with five in parallel and then adding the two blocks, demonstrated by 'The two combinations are again connected in series'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Work is the area under the path on a P-V diagram, so a vertical (constant-volume) leg does no work
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $-60\,\mathrm{J}$ is the work for the whole loop $abcda$ — $+30\,\mathrm{J}$ along $ab$ and $-90\,\mathrm{J}$ along $cd$ — and the stem's opening sentence names that cycle.
- **Why:** This question requires reading from the printed P-V figure that $bc$ is the constant-volume leg, demonstrated by 'The work done by the gas along the path $bc$' with $b$ and $c$ both drawn at $V=400\,\mathrm{cm^3}$.
- **Note:** The figure was supplied with the packet as a drawn spec and a printed PNG: $a$ and $b$ sit at $100\,\mathrm{kPa}$, $c$ and $d$ at $300\,\mathrm{kPa}$, with volumes $100$ and $400\,\mathrm{cm^3}$, which is consistent with the printed key.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Turning a truth table into a Boolean expression: here Y does not move with A at all and is the complement of B, so the circuit is a NOT gate on B
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The Y column moves only when B moves, so a student who stops at "Y is controlled by B" writes $Y=B$; lined up row by row the two columns are opposites, B reading 0, 1, 0, 1 against Y reading 1, 0, 1, 0, so the bar is the entire answer.
- **Why:** This question requires reading the supplied truth table and naming the Boolean expression that reproduces its output column, demonstrated by the stem "A logic circuit provides the output $Y$ as per the following truth table" with the rows 0 0 - 1, 0 1 - 0, 1 0 - 1, 1 1 - 0 printed nowhere but in the table itself.
- **Note:** E1 called this plain_mcq, which is right for the option set, but the printed shape has a table laid over it; on the retired E1 list that is the table_based overlay, and this step's qtype axis has no slot for an overlay, so it is recorded as mcq. This is not the rulebook 5.0 missing-figure case: the figure spec carried all 15 cell and header labels with print_match passing, so the full table was readable at this step and the trap is auditable. Key checked by evaluating every option on all four rows: only $\overline{B}$ matches 1, 0, 1, 0, so option 4 stands as printed.
<!--/ecat-->

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
2. Squaring and inverting: $\frac{1}{\lambda^2} = \frac{2m}{h^2}E$.
3. $\frac{1}{\lambda^2} \propto E$, a straight line through the origin, which is option $1$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q005_152c40b3_03112026.png?v=152c40b37f54)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q005_85aa050b_03112026.png?v=85aa050bd928)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** For a free particle $p=\sqrt{2mE}$, so $\frac{1}{\lambda^2}=\frac{2mE}{h^2}$ is a straight line through the origin against kinetic energy
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  $\frac{1}{\lambda}=\frac{\sqrt{2mE}}{h}$ is reached correctly and then sketched as it stands — a $\sqrt{E}$ curve that rises and bends over — because the square that makes the plotted quantity $\frac{1}{\lambda^2}$ is left off.
- **Why:** This question requires turning $\lambda=\frac{h}{\sqrt{2mE}}$ into the shape of $\frac{1}{\lambda^2}$ against $E$ and matching it to a drawn curve, demonstrated by the four options being graphs of $1/\lambda^2$ against $E$ of which one is 'a straight line through the origin'.
- **Note:** E1 recorded `statement_options` on '15 full-statement options', which does not match the page: the options are drawings, arriving as '[drawn option] Graph of 1/lambda^2 against E ...'. The printed shape is four graphs as options, which `category_retired.qtype` maps (`graph_options`) onto `mcq`, so `mcq` is recorded here.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The photon's stated properties: energy $E=h\nu$, speed $c$, momentum $p=h\nu/c$, zero charge, and conservation of both energy and momentum in a photon-electron collision
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student who reaches for $p=mv$ has nothing to put in it for a massless photon, so statement C is struck out and D's momentum conservation goes with it. What is left, A and B, is true but stops two statements short of the key, whose $p=h\nu/c$ is the same quantity as $p=h/\lambda$.
- **Why:** This question requires judging five printed claims against the properties stated for the photon, demonstrated by statement E, 'Photon possesses positive charge.', which is settled by a stated property and not by any computation.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Surface gravity is $g=\frac{GM}{R^2}$, so the mass enters once and the radius enters squared
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  $g\propto R$, the equal-density result, is used in place of $g=\frac{GM}{R^2}$, so halving the radius halves $9.8$ to $4.9\,\mathrm{m\,s^{-2}}$ and the given mass of $\frac{1}{10}$ never enters the sum.
- **Why:** This question requires combining a mass factor of $\frac{1}{10}$ with a radius factor of $\frac{1}{2}$ inside $g=\frac{GM}{R^2}$, demonstrated by 'its diameter is half that of the earth' and options printed as values in $\mathrm{m\,s^{-2}}$ rather than as multiples of $g$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The vernier constant is one main-scale division divided by the number of vernier divisions, which here is $N+1$, then converted to centimetres
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The familiar bench calliper is carried in rather than the stem's: least count $=\frac{1\,\mathrm{MSD}}{N}$ with $1\,\mathrm{MSD}=1\,\mathrm{mm}$ gives $\frac{1}{10N}$ cm, where the stem's own data give $\frac{0.1\,\mathrm{mm}}{N+1}=\frac{1}{100(N+1)}$ cm.
- **Why:** This question requires the vernier constant as $1\,\mathrm{MSD}-1\,\mathrm{VSD}$ with the division count the stem supplies, demonstrated by '$(N + 1)$ divisions of vernier scale coincide with $N$ divisions of main scale' together with '1 MSD represents $0.1\,\mathrm{mm}$'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Ideal transformer: the voltage divides in the same ratio as the turns, so $V_S/V_P = N_S/N_P$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The stem prints the turns ratio as $\frac{N_P}{N_S}=\frac{1}{2}$, and a student who carries 'voltage ratio equals turns ratio' copies the printed $1:2$ straight across, while the question asks for $V_S:V_P$, which is the other way round.
- **Why:** This question requires the ideal-transformer turns-to-voltage proportionality read in the direction asked, demonstrated by the stem printing $\frac{N_P}{N_S}=\frac{1}{2}$ and then asking for 'The ratio $V_S : V_P$'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Instantaneous power is force times instantaneous velocity, and the velocity is the slope of the displacement-time expression
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Differentiating $2t-1$ term by term and carrying the $-1$ through gives $v=2-1=1\,\mathrm{m\,s^{-1}}$, so $P=5\times1=5$ W instead of $5\times2=10$ W.
- **Why:** This question requires a number computed from the stem's own data, demonstrated by 'the displacement of any particle is given by $2t - 1$' and 'force of $5\,\mathrm{N}$' having to be combined as $P=Fv$.
- **Note:** The stem's displacement is linear in $t$, so the particle moves at constant velocity while a $5\,\mathrm{N}$ force acts; that is consistent only if an equal opposing force is present, which the stem does not mention. The key follows $P=Fv$ and is tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Pulling a flat disc off a liquid surface needs force = surface tension $\times$ length of the contact line, which for a disc is one circle of $2\pi r$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Converting $4.5\,\mathrm{cm}$ by dividing by 1000 instead of 100 puts $r=0.0045\,\mathrm{m}$ into $F=T(2\pi r)$ and returns $1.98\,\mathrm{mN}$, exactly a tenth of the right value.
- **Why:** This question requires a number computed from the stem's measurements, demonstrated by 'radius $4.5\,\mathrm{cm}$' and 'surface tension of water is $0.07\,\mathrm{N\,m^{-1}}$' with options printed across both N and mN.
- **Note:** The key corresponds to a single contact line, $F=T(2\pi r)=19.8\,\mathrm{mN}$, which is what a thin flat disc lying on the surface gives; a two-surface reading $4\pi rT$ would give $39.6\,\mathrm{mN}$ and is not among the options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In rolling without slipping the contact point is instantaneously at rest and the topmost point moves at $2v$
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  'One point of a rolling wheel is instantaneously at rest' is the fact this topic is remembered by, and a student who holds the fact without holding that the point is the one touching the road pins the zero onto the top point $P$.
- **Why:** This question requires the rolling constraint applied to two named points with no quantity produced, demonstrated by the options being bare comparisons such as 'Point $P$ moves faster than point $Q$'.
- **Note:** The stem itself fixes which letter is which, with '$P$ and $Q$ are any highest and lowest points on the wheel, respectively', so the tag does not depend on reading the figure. The figure spec is consistent with that once its coordinates are read with $y$ increasing upward: the ground line and the contact label $Q$ sit together, and $P$ sits past the top of the circle.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The axial potential of a short dipole is $V = \pm\frac{P}{4\pi\epsilon_0 r^2}$; the factor 2 belongs to the axial field, not to the potential
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The factor 2 sits in the axial field $E = \frac{2P}{4\pi\epsilon_0 r^3}$, so R's $\pm\frac{2P}{4\pi\epsilon_0 r^2}$ reads as the standard axial dipole result, and A's $\pm 9\times 10^3$ V checks out on its own, so both are marked true with R explaining A.
- **Why:** This question requires substituting the stem's numbers into the axial dipole potential and then checking the printed relation term by term, demonstrated by R printing $V = \pm\frac{2P}{4\pi\epsilon_0 r^2}$ while A's $\pm 9\times 10^3$ V follows from the same $P = 4\times 10^{-6}$ C m and $r = 2$ m only without the factor 2.
- **Note:** The key as printed, option 4, agrees with the arithmetic: $9\times 10^9 \times 4\times 10^{-6}/4 = 9\times 10^3$ V makes A true, and R's extra factor 2 would give $1.8\times 10^4$ V. `negative_words_seen` lists NOT and FALSE, but both come from the standard A/R option wording, not from the task.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In $x=A\sin(\omega t+\phi)$ the amplitude is $A$ in the unit printed with $x$, and the time period is $2\pi/\omega$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The computed half comes out right, $T=2\pi/\pi=2\,\mathrm{s}$, and the read-off half is lost: the unit 'm' sits outside the bracket, and a student used to amplitudes quoted in centimetres writes $5\,\mathrm{cm}$, so the whole pair scores nothing.
- **Why:** This question requires two values read and computed from the printed equation, demonstrated by 'the amplitude and time period of motion, respectively, are' with every option pairing a length with a time.
- **Note:** E1 records this as `multi_part_respectively`, which on the current axis is `two_part`; the printed shape agrees, since each option carries an amplitude and a period that must both hold.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** At Brewster's angle the reflected beam is completely polarised while the transmitted beam stays partially polarised
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  'At Brewster's angle the light is completely polarised' is the half of the rule that sticks, and with no beam attached to it the student grants it to both beams; the reflected half of this option is right and the refracted half is not.
- **Why:** This question requires the statement the textbook makes about Brewster's angle, demonstrated by the stem supplying only 'strikes a glass surface at Brewster's angle. Then' with no quantity to find and no new case to apply a rule to.
- **Note:** E1 records this as `statement_options`, a shape the current `qtype` axis has no value for; under the rule that long sentences as options do not make a question `statements`, with no lettered block printed and no instruction to judge statements, it is recorded as `mcq`.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A solid angle is an area divided by a radius squared, so it is dimensionless, and only quantities that are themselves ratios of like quantities match it
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Angle is correctly seen as dimensionless and stress is taken for the dimensionless member of the stress-strain pair, so the half that is right vouches for the half that is not; stress is $ML^{-1}T^{-2}$.
- **Why:** This question requires the dimensional formula of each named quantity to be worked out and set against a dimensionless solid angle, demonstrated by 'the quantities which have the same dimensions as those of solid angle' with each option offering two quantities to be accepted together.
- **Note:** E1 recorded plain_mcq, but each option is a pair of quantities accepted or rejected whole ('strain and angle'), which is the rulebook's pair_options shape, so the printed shape is recorded as two_part. Options 3 and 4 are both half-right pairs; option 3 is named as the trap because its failing member, stress, is the look-alike of the right member, strain, while option 4's 'arc' needs a looser association to reach.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A magnetic needle oscillating in a uniform field has $T = 2\pi\sqrt{I/mB}$, rearranged to give the magnetic moment
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The period is taken as oscillations over time, $20/5 = 4$ s, instead of time over oscillations, $5/20 = 0.25$ s, and the same correct formula then gives $m = 4\pi^2 I/(T^2 B) = 5\pi^2 \times 10^{-5}\,\mathrm{Am^2}$, which is printed.
- **Why:** This question requires the oscillation formula rearranged for the magnetic moment and evaluated on the printed data, demonstrated by 'if the magnitude of magnetic moment of the needle is $x \times 10^{-5}\,\mathrm{Am^2}$, then the value of $x$ is'.
- **Note:** The figure shows the needle hung in the uniform field and supplies no measurement; every number needed is in the stem, so the question is not figure-gated.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A charged conductor is an equipotential: the potential on its surface and everywhere inside it is the same, so two such points differ by zero
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $kq/R = 9\times10^{9} \times 10^{-6}/0.03 = 3\times10^{5}$ V is the one number the printed data yields, and it is the potential of the shell itself, not the difference between two points that share it.
- **Why:** This question requires the equipotential property of a charged conductor applied to a point at the centre and a point on the shell, demonstrated by 'the potential difference between the two points $C$ and $P$' with the supplied $\frac{1}{4\pi\varepsilon_0}$ never needed to answer it.
- **Note:** Tagged apply_rule rather than calculate because no quantity is produced: the figure's $q = 1\,\mu\mathrm{C}$ and $R = 3$ cm and the stem's constant are all unused once the equipotential rule is applied.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Moment of inertia of a uniform rod about its midpoint, $I = ML^2/12$, rearranged for the length
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $L^2 = 12I/M = 12 \times 2400/400 = 72$, and 72 is printed as a length in centimetres, so the number reached one step early is sitting in the options and the square root is never taken.
- **Why:** This question requires $I = ML^2/12$ solved for $L$ on the printed numbers, demonstrated by 'the moment of inertia ... is $2400\,\mathrm{g\,cm^{2}}$' and 'the length of the $400\,\mathrm{g}$ rod is nearly'.
<!--/ecat-->

## Q20

Physics · Modern Physics

Given below are two statements:
Statement I: Atoms are electrically neutral as they contain equal number of positive and negative charges.
Statement II: Atoms of each element are stable and emit their characteristic spectrum.
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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Atoms are neutral because their positive and negative charges balance, but a characteristic line spectrum comes out only after the atom is excited - an atom sitting in its stable state radiates nothing
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Both sentences read like lines out of the chapter's own account of the atom, so Statement II's 'stable and emit their characteristic spectrum' is ticked off as recalled text instead of checked. Emission needs the atom excited first, so stability and emission cannot be held together the way the statement joins them.
- **Why:** This question requires each printed claim about the atom to be graded against what the chapter states, demonstrated by Statement II, 'Atoms of each element are stable and emit their characteristic spectrum', which is the clause the printed key grades incorrect while Statement I is left standing.
- **Note:** Tagged as printed, with the key kept (§7). The stem supplies no ground for grading Statement II incorrect, and two readings are open to a reviewer: that emission requires the atom to be excited, so stability and emission cannot be asserted together, or that the atoms of radioactive elements are not stable. The trap route is written on the first reading because it is the one the statement's own wording ('stable and emit') sets up; a reviewer preferring the second reading would keep the same label and option and change only the route. Flagged arguable_key because Statement II is close to the chapter's own listed facts about atoms, so option 2 is defensible on a reasonable reading and the key rests on the finer reading of 'stable'. E1's statement_i_ii matches the printed shape - exactly two labelled statements and four verdict options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Balmer lines: the larger the jump down to $n_1 = 2$, the larger the energy gap, so the shorter the wavelength -- $656.3$ nm for $n_2 = 3$ falling to $410.2$ nm for $n_2 = 6$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Reading a bigger jump as a longer wavelength puts the shortest line on $n_2 = 3$ and the longest on $n_2 = 6$, and pairing the two lists off straight down the page in that belief gives A-I, B-II, C-III, D-IV.
- **Why:** This question requires the direction of the Rydberg relation applied to each listed transition rather than any stored number, demonstrated by List II printing the four wavelengths already -- $410.2$, $434.1$, $656.3$, $486.1$ -- so that ordering them against "$n_2 = 3$ to $n_1 = 2$" through "$n_2 = 6$ to $n_1 = 2$" fixes every row with nothing computed.
- **Note:** List II prints the wavelengths as bare numbers with no unit; they are the Balmer wavelengths in nm. The missing unit does not affect the pairing, so the record is tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Magnetic susceptibility sorts materials: small and negative for a diamagnet, small and positive for a paramagnet, very large for a ferromagnet, zero for a non-magnetic material
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Diamagnetic and paramagnetic are separated only by the sign of $\chi$, and hanging the minus sign on the paramagnet puts the small positive range on A and $0 > \chi \geq -1$ on C, which is option 1 exactly.
- **Why:** This question requires the susceptibility range the textbook tabulates against each class of material, demonstrated by List II's printed bounds "$0 < \chi < \varepsilon$ (a small positive number)" and "$0 > \chi \geq -1$", which are read off the table rather than produced by any relation.
- **Note:** The stem arrives with the two column headers run together on one line, "List-I (Material) List-II (Susceptibility ($\chi$))"; both lists and all four options are present, so the record is complete and is tagged as printed. "Non-magnetic" paired with $\chi = 0$ is the paper's own fourth class, not a re-reading of the key.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The microampere current in a reverse biased junction is the drift of thermally generated minority carriers, and a solar cell's I-V curve sits in the fourth quadrant because it delivers power
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The carrier sentence a student brings from the forward-bias paragraph is that the diode's current is carried by majority carriers, and it sits a few lines from the reverse-bias case, so it is carried across and B reads as correct. Reverse bias pulls those carriers away from the junction; what is left in the microampere range is minority-carrier drift, which is why it saturates.
- **Why:** This question requires deciding which carrier type the microampere reverse current belongs to, demonstrated by statement B, 'In a reverse biased $pn$ junction diode, the current measured in ($\mu\mathrm{A}$), is due to majority charge carriers.' On the trap axis I applied the unlike-words test from §5.1: replace the two carrier names with two words that do not resemble each other and the pull stands, because what carries the student is the forward-bias sentence printed beside the reverse-bias one, so the label is nearby_fact rather than look_alike_term.
- **Note:** E1_question_type is plain_mcq by the 16-default, but the printed shape is two lettered statements, A and B, with the four verdict options, so qtype is recorded as statements. The figure supplies only the quadrant numbering; its labels run in the usual sense even though the I axis is drawn downward, so the two printed claims decide the answer and asks is fact_line rather than read_diagram.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** At the centre of a double-slit pattern the path difference is zero for every wavelength, so white light gives a white centre, while fringe width $\beta = \lambda D/d$ differs with colour and the outer fringes colour and then wash out
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The 'few coloured fringes' half of this option is exactly what white light does, and that correct half carries the 'central dark fringe' with it; a dark centre comes from reasoning that all the colours overlapping at the centre must cancel.
- **Why:** This question requires what a named experiment shows when one condition of it is changed, demonstrated by 'if the monochromatic source in Young's double slit experiment is replaced by white light, then' with each option a rival description of the observed pattern.
- **Note:** E1 recorded statement_options, which is the rulebook's E1 shape for content living entirely in the four options. On the current qtype axis, `statements` is reserved for a stem that asks statements to be judged or prints a lettered list, and neither is printed here, so the shape is recorded as mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ray that emerges along a face left the glass at the critical angle; with the internal ray parallel to the base of a right-angled prism the two face angles are complementary, which reduces the problem to $n^2 = 1 + \sin^2 i$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The physics finishes correctly at $n^2 = 1 + \sin^2 30^\circ = 5/4$, and then $\sqrt{5/4}$ is written as $\frac{\sqrt5}{4}$, with the root taken on the numerator only, which is a printed option.
- **Why:** This question requires the critical-angle condition combined with the prism geometry and evaluated to a number, demonstrated by 'it travels through the prism parallel to its base $BC$ and emerges along the face $AC$' with the angle of incidence printed as $30^\circ$.
- **Note:** The supplied figure confirms the right angle at $A$ and the internal ray drawn parallel to $BC$, which the stem also states in words, so the figure corroborates rather than carries the question.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Terminal voltage is the emf less the drop across the cell's own internal resistance, $V=\varepsilon-Ir$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The cell is labelled $10\,\mathrm{V}$ in the stem and in the figure, so a student who reads the emf as the terminal reading reports it unchanged. That reading is the right one only with nothing connected; with the printed $4\,\Omega$ in place, $2\,\mathrm{A}$ flows and $1\,\Omega$ of internal resistance takes $2\,\mathrm{V}$ away.
- **Why:** This question requires computing the terminal voltage from the emf and the internal drop, demonstrated by the stem's 'emf is $10\,\mathrm{V}$ and internal resistance $1\,\Omega$, when connected through an external resistance of $4\,\Omega$' and by all four options being voltages.
- **Note:** The figure spec was supplied and agrees with the stem (cell $10\,\mathrm{V}$ with $1\,\Omega$ in the dashed box, $4\,\Omega$ in the loop), so the stem alone carries every number needed. Trap label chosen as condition_missed over formula_misused because option 1 is the correct reading once the printed external connection is dropped, which is the evidence that label asks for.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Contact force between two blocks pushed together: get the common acceleration from the whole system, then apply $F=ma$ to the block the contact force alone pushes
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $10\,\mathrm{N}$ is true of the arrow in the figure — it is the force applied to $A$ — and a student who takes a push to arrive at the second block undiminished reports that same number for the contact force. $4\,\mathrm{N}$ of it is spent accelerating $A$'s own $2\,\mathrm{kg}$, leaving $6\,\mathrm{N}$ for $B$.
- **Why:** This question requires computing the contact force on the isolated rear block, demonstrated by the stem asking for 'The force exerted by block $A$ on block $B$' while printing one applied force and both masses.
- **Note:** E1 returned multi_part_respectively, but the 'respectively' in this stem only distributes the two masses ('$2\,\mathrm{kg}$ and $3\,\mathrm{kg}$ respectively'); the answer is a single force, so the printed shape is a plain mcq and that is what is recorded.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Momentum is conserved in a perfectly inelastic collision, so equal masses sticking together move at half the incoming speed
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Momentum gives $v_2=v_1/2$, and a student who copies that fraction straight into the answer prints the halving in the wrong order. The stem asks for $v_1:v_2$, which is $2:1$.
- **Why:** This question requires applying momentum conservation and then reporting the result as a ratio in the printed order, demonstrated by the four options being the orderings '$1:4$', '$1:2$', '$2:1$', '$4:1$' of a single halving.
- **Note:** The retired vocabulary would have called option 2 inverted_ratio; under §5.1 that device belongs to the reversed family, which is what is recorded.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A two-input gate with its inputs tied together acts as an inverter, and the output bubbles decide the function: $\overline{\bar A+\bar B}=A\cdot B$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Each of the first two gates has its inputs tied, so they hand $\bar A$ and $\bar B$ to the last gate; a student who then reads that last gate from its OR body and not from its output bubble writes $Y=\bar A+\bar B$, which is $\overline{A\cdot B}$ — a NAND.
- **Why:** This question requires applying the gate truth tables to the network as drawn, demonstrated by the stem's 'The output $(Y)$ of the given logic gate is similar to the output of an/a' with four gate names as the options.
- **Note:** The figure was supplied as a readable spec (tied-input NAND fed by $A$, tied-input NOR fed by $B$, both into a bubbled OR giving $Y$), so §5.1's figure-not-supplied case does not apply. asks is apply_rule rather than read_diagram because the figure only supplies the network; the decision is the Boolean reduction, and no quantity is produced. Trap label is formula_misused rather than arithmetic_slip because the student uses the OR table where the NOR table applies, and there is no arithmetic in the question.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A bridge of five equal capacitors is balanced, so the bridge capacitor carries no charge and the two series arms simply add in parallel
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The middle capacitor is drawn between the two junctions, so a student who has not tested the bridge for balance counts it as one more path from $A$ to $B$ and adds its $2\,\mu\mathrm{F}$ in parallel with the $2\,\mu\mathrm{F}$ of the two arms, giving $4\,\mu\mathrm{F}$. Being balanced, it holds no charge at all.
- **Why:** This question requires reducing a five-capacitor bridge to one equivalent value, demonstrated by the stem's 'the equivalent capacitance between terminal $A$ and terminal $B$' and the figure's five equal $2\,\mu\mathrm{F}$ arms.
- **Note:** The figure spec and netlist were supplied ($C_1$: A-P, $C_2$: P-B, $C_3$: P-Q, $C_4$: A-Q, $C_5$: Q-B, all $2\,\mu\mathrm{F}$), which is what makes the balance checkable; the stem by itself carries no values.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Uniform speed fixes only a magnitude: in circular motion both the velocity and the centripetal acceleration keep changing direction
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who holds the taught line that the centripetal acceleration keeps turning towards the centre, and who reads the stem's 'uniform speed' as a constant velocity, finds both of those sentences in one option. The acceleration half is right; the velocity half fails, because the velocity lies along the tangent and turns with the particle.
- **Why:** This question requires holding speed apart from velocity and a fixed magnitude apart from a fixed vector, demonstrated by the stem's 'uniform speed' set against option 2's 'Constant velocity' and option 3's 'Constant acceleration'.
- **Note:** half_right is used on option 4 under the two-or-more-parts rule: 'Constant velocity but varying acceleration' carries two claims and only the second holds. asks is compare rather than apply_rule because the four options cross constant against varying for two neighbouring quantities, and the work is telling those quantities apart; compare here sits on a plain mcq, not on a pairing shape.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The elastic limit is the largest stress the wire can carry, and strain $=$ stress $/$ Young's modulus, so the greatest elongation is that strain times the wire's length.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Dividing $8\times10^{8}$ by $10^{11}$ and letting the 2 of $2\times10^{11}$ fall out of the mantissa carries the stem's own digit 8 into the answer: $8\times10^{-3}\,$m, the printed $8\,$mm.
- **Why:** This question requires a number computed from the two printed constants, demonstrated by the stem supplying '$8 \times 10^{8}\,\mathrm{N\,m^{-2}}$ and $2 \times 10^{11}\,\mathrm{N\,m^{-2}}$' while each option prints a single length.
- **Note:** E1's pattern read the stem's 'respectively' as a multi-part answer and returned multi_part_respectively, which maps to two_part. The word attaches to the two given constants, not to the answer, which is one length, so the shape recorded here is mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In alpha emission the mass number falls by 4 and the atomic number by 2; in positron emission the mass number is unchanged and the atomic number falls by 1; in nuclear electron emission the mass number is unchanged and the atomic number rises by 1.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The chain prints four arrows but only three lettered intermediates, and the last arrow $e^{-}$ repeats what $\beta^{-}$ has already done, so reading it as an electron leaving the atom rather than the nucleus stops the count at $P$ — 286 and 80, one $Z+1$ short of $Q$.
- **Why:** This question requires the mass number and the atomic number to be carried through four printed decay arrows, demonstrated by the stem asking for 'the mass number and atomic number of the product $Q$ respectively' with each option printing a pair of numbers.
- **Note:** E1's pattern fired on the text arrows and returned reaction_scheme, which maps to mcq, but each option is a pair judged whole, so the shape recorded here is two_part. One thing for a reviewer: the final arrow $e^{-}$ duplicates the earlier $\beta^{-}$, and only the emission reading reaches a printed option — electron capture would give 286, 79, which is not on the list. The key as printed agrees with the emission reading, and is followed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Lenz's law: the induced current opposes the change in flux, so the coil the magnet is leaving attracts it while the coil it approaches repels it, and the two currents circulate oppositely.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Settling solenoid-1 first and then giving solenoid-2 the same circulation sense — the coils are drawn alike and one magnet passes both — prints CD where Lenz's law needs DC, because the approaching S pole has to be pushed away while the departing N pole has to be held back.
- **Why:** This question requires Lenz's law applied to two coils whose flux changes run opposite ways, demonstrated by the stem asking for 'the direction of induced current in solenoid-1 and that in solenoid-2, respectively'.
- **Note:** E1's pattern returned plain_mcq, which maps to mcq; each option is a pair of senses judged whole, so the shape recorded here is two_part. The figure was supplied, as a printed PNG and a draw spec showing two identically wound coils with A and B on solenoid-1, C and D on solenoid-2, and the magnet's N face towards solenoid-1 moving right. The mapping from the letters to a circulation sense was not re-derived from the drawing, so the routes above are written as reversals of the printed key rather than as absolute senses. All four options are a grid over two independent senses, which is why each wrong cell carries a route and none is filler.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The field at the centre of a tightly wound circular coil is $B = \mu_0 N I / 2R$, with the radius in metres.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Converting the $10\,$cm radius with the millimetre factor gives $R = 0.01\,$m, and $4\pi\times10^{-7}\times700/0.02 = 4.4\times10^{-2}\,$T, which is the printed $44\,$mT.
- **Why:** This question requires a field computed from the coil's turns, current and radius, demonstrated by the stem giving '$100$ turns coil of radius $10\,\mathrm{cm}$ carries a current of $7\,\mathrm{A}$' together with the permeability to put into it.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Electromagnetic waves are radiated by accelerating charges; a charge moving with uniform speed radiates nothing.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Comparing the field magnitudes instead of the energy-density expressions makes the equality look false: $E = cB$ puts $E$ some $3\times10^{8}$ times above $B$, so the electric field seems to hold the energy, and a true property is offered as the one an electromagnetic wave lacks.
- **Why:** This question requires one printed property of electromagnetic waves to be graded false, demonstrated by the option 'They originate from charges moving with uniform speed' standing against the three true properties printed beside it.
- **Note:** E1's pattern returned statement_options, which maps to statements; no lettered block is printed, and the task is to grade four whole property claims, with the polarity word NOT in the stem itself. The falsity of the key turns on one word — 'uniform', where the source has accelerated charges as the origin of radiation.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Acceleration is the slope of the velocity-time graph, so straight segments of $v$ become constant blocks of $a$ and a steady speed means zero acceleration.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The trapezoid is the curve the stem has already printed, and taking the acceleration to follow the speed — largest where the body is fastest — redraws that shape on the $a$-$t$ axes, which answers what the velocity does rather than what the acceleration does.
- **Why:** This question requires the velocity graph's slope translated into an acceleration graph, demonstrated by the stem's 'The acceleration $(a)$ – time $(t)$ graph that best suits this motion' with four drawn graphs as the options.
- **Note:** E1's pattern returned statement_options because the drawn options arrive as one-line descriptions of the drawings; the four options are graphs, so the printed shape is graph_options, which maps to mcq. The '[drawn option] …' text describes a real printed drawing and was treated as a readable option, not as missing data. Option 4's description names a positive block followed by a negative block, with the zero stretches before and between them implied, which is what the drawn $v$-$t$ graph's slope gives.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Capacitive reactance $X_C=\frac{1}{2\pi fC}$ fixes the rms current, and the peak current is $\sqrt{2}$ times the rms value
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Every named slip on $I_0=\sqrt{2}\,V_{rms}\,(2\pi fC)$ was computed against the printed options: with $X_C=318.5\,\Omega$ the rms current is $0.66$ A and the peak $0.93$ A, dividing by $\sqrt{2}$ instead of multiplying gives $0.47$ A, using $\pi f$ for $2\pi f$ gives $0.33$ A rms and $0.47$ A peak, multiplying by $2$ instead of $\sqrt{2}$ gives $1.32$ A, and reading $C$ as $1\,\mu$F gives $0.093$ A; the printed wrong options are $0.35$, $0.58$ and $1.20$ A, so no route lands on one of them
- **Why:** This question requires the capacitive reactance to be computed from the printed data and converted into a peak current, demonstrated by the stem's "The peak current in the circuit is nearly $(\pi = 3.14)$" set against $10\,\mu\mathrm{F}$, $210\,\mathrm{V}$ and $50\,\mathrm{Hz}$.
- **Note:** The key follows from the printed data: $X_C = 1/(314 \times 10^{-5}) = 318.5\,\Omega$, $I_{rms} = 0.66$ A, $I_0 = 0.93$ A. The figure adds nothing beyond the stem, which already names C, V and f. The three wrong values are a numerical spread rather than engineered slips, which is why the trap axis records no_trap instead of a forced arithmetic route.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** On a plot of $T$ against $V$ an ideal gas gives a line of slope $P/nR$, so the steeper line belongs to the higher pressure
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  On the Charles's-law plot as NCERT draws it, $V$ against $T$, the slope is $nR/P$ and the steeper line is the lower pressure; carried straight onto these axes, where $T$ is plotted against $V$ and the slope is $P/nR$, that rule reverses the order and gives $P_3 > P_2 > P_1$.
- **Why:** This question requires the slopes of three printed curves to be read against the ideal-gas relation, demonstrated by the stem's "$T$-$V$ curves of an ideal gas … at three pressures $P_1$, $P_2$ and $P_3$" with options that are orderings of those three labels.
- **Note:** In the stored drawing $T$ runs down the page (its axis arrow points downward) and $V$ runs to the right, with the origin at the top left; the steepest solid curve carries the $P_1$ label, which is what the printed key rests on.
<!--/ecat-->

## Q40

Physics · Current Electricity

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

1. Top arms are $10\,\Omega$ and $10\,\Omega$, so balance needs the two bottom arms equal: $\frac{10}{10} = \frac{15}{S} \Rightarrow S = 15\,\Omega$.
2. Options 1-3: diode in series with $5\,\Omega$; forward bias gives $S = 5\,\Omega \neq 15\,\Omega$.
3. Reverse bias makes that arm open; then current flows $15\,\Omega \to G \to 10\,\Omega$, so $I_G \neq 0$ and the bridge is not balanced.
4. Option 4: diode in parallel with $5\,\Omega$ gives $S = 0$ (forward) or $S = 5\,\Omega$ (reverse), neither equal to $15\,\Omega$.
5. No option satisfies $S = 15\,\Omega$ as the values are read, so the answer is unsure.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 17)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q040_ef760322_03112026.png?v=ef7603224f57)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q040_53f75be1_03112026.png?v=53f75be1c4a3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A Wheatstone bridge balances only when the two arm ratios are equal, and an ideal diode makes its arm a short circuit when forward biased and an open branch when reverse biased
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn circuits, and the descriptions supplied to this step give all four the same arms — 10, 10, 15 and 5 ohm with a diode D, a galvanometer, a cell and a key — without the diode's orientation or terminal, which is the feature that decides whether its arm is a short or an open
- **Why:** This question requires the bridge-balance condition applied to an arm whose resistance depends on the diode's bias, demonstrated by the stem's "Choose the correct circuit which can achieve the bridge balance" with four drawings that carry the same four arm values and move only the diode.
- **Note:** E1_question_type reads statement_options on the ground of "15 full-statement options", but the four options are drawn circuits, not statements; recorded as mcq with drawn options. What a reviewer holding the printed drawings should check: with 10, 10, 15 and 5 ohm in the four arms no arrangement satisfies $P/Q = R/S$ (every pairing of those values gives $1$ against $3$, $\tfrac{2}{3}$ against $2$, or $1.5$ against $0.5$), so balance can only come from the diode turning one arm into a short when forward biased or into an open branch when reverse biased. The trap to expect is a drawing whose diode bias leaves the arm resistance untouched, so the ratios stay unequal; it could not be confirmed from the option text, so no option is tagged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On one fixed supply voltage the outputs of two rated heaters combine reciprocally in series and add in parallel
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The series step gives $P_s = \frac{P_AP_B}{P_A+P_B} = \frac{2}{3}$ kW, and $2:3$ is that fraction printed as a ratio; clearing it against the parallel output needs both terms multiplied by $3$, giving $2:9$, and multiplying only the first term leaves $2:3$.
- **Why:** This question requires the series and the parallel output of two rated heaters on one supply to be computed and divided, demonstrated by "Those two are first connected in series and then in parallel to a fixed power source" with four options that are ratios.
- **Note:** "A fixed power source" has to be read as a fixed supply voltage for the key to follow, since the two connections draw different power; the phrase itself is what makes $1:1$ reachable.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A capacitor held at constant voltage by a battery: reducing the plate separation raises $C$, and with $V$ fixed it raises $Q$, $QV$ and the stored energy $\tfrac{1}{2}CV^2$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Pushing the plates closer raises $C$, and the energy formula with $C$ in the denominator, $U=Q^2/2C$, then says the stored energy falls, so B is accepted and E, which is twice that energy, is dropped with it. That formula belongs to an isolated capacitor; the plates here stay 'connected to a battery', so $V$ is the fixed quantity and $U=\tfrac{1}{2}CV^2$ rises.
- **Why:** This question requires applying the capacitor relations with the potential difference held fixed, demonstrated by the stem's 'connected to a battery' together with statement D, 'the ratio of charge to its potential remains the same.', and no numerical quantity is asked for.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Every term added into a force must itself have the dimensions of force, which fixes $[\alpha]$ and $[\beta]$ and so the one combination of them that is dimensionless
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  $[\beta]/[\alpha] = T$, so the $t$ has to divide rather than multiply; written the other way round as $\beta t/\alpha$ the combination carries $T^2$ instead of cancelling.
- **Why:** This question requires dimensional homogeneity applied to a printed equation and then tested on four given combinations, demonstrated by "The factor which is dimensionless, if $\alpha$ and $\beta$ are constants" set on $F = \alpha t^{2} + \beta t$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Launch energy is the difference of total energies: $-\frac{GMm}{R}$ at rest on the surface and $-\frac{GMm}{2r}$ in a circular orbit of radius $r$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Taking the change in potential energy alone, $-\frac{GMm}{3R} + \frac{GMm}{R} = \frac{2GmM}{3R}$, drops the kinetic-energy term the satellite must carry to stay in the circular orbit.
- **Why:** This question requires the total energy at rest on the surface to be subtracted from the total energy in the orbit, demonstrated by "The minimum energy required to launch a satellite … in a circular orbit at an altitude of $2R$ from the surface" with four symbolic options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Thermal stress in a clamped bar: blocking the expansion forces a strain $\alpha\Delta T$ on the bar, so the compressive force is $F = YA\alpha\Delta T$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The modulus is printed as $0.5 \times 10^{11}$, and carrying it as the familiar round $10^{11}$ doubles the whole product: $10^{11} \times 10^{-3} \times 10^{-5} \times 100 = 100 \times 10^{3}$ N, exactly the printed option.
- **Why:** This question requires the clamped-bar thermal-stress relation applied to the printed numbers, demonstrated by "heated from $0^{\circ}\mathrm{C}$ to $100^{\circ}\mathrm{C}$ without expansion or bending" together with the printed $Y$, $\alpha$ and area of cross-section.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Displacement current: the growing electric flux between charging plates carries the current across the gap, equal in size to the conduction current and in the same sense, so the current is unbroken round the circuit
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Induced quantities are filed under "opposes the change" — Lenz's law, back emf — so the magnitude is kept and the arrow flipped. But $i_d = \varepsilon_0 \frac{d\Phi_E}{dt}$ grows with the field the arriving charge is building, so it runs along $I$.
- **Why:** This question requires the Ampere-Maxwell rule applied to the gap of a charging capacitor with no quantity computed, demonstrated by the options separating "magnitude equal to $I$ flows in the same direction as $I$" from "equal to $I$ flows in a direction opposite".
- **Note:** E1_question_type is the retired `statement_options`. No lettered statement block is printed and the stem is a single trailing instruction, so under brief rule 1 long sentences as options do not make this `statements`; the current-vocabulary shape is `mcq`.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A strong pole attracts a ferromagnetic sheet at rest, while eddy-current drag opposes a sheet moved near the pole only when the sheet can carry an induced current
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Eddy-current drag is what makes a force necessary in C, and a student who keeps the drag but not the property it needs reads D - the same motion with the material conditions negated - as needing a force too. Eddy currents need a conducting path, and D's own words remove it, so that sheet can be moved at uniform velocity with nothing opposing it.
- **Why:** This question requires applying the magnetic-attraction and eddy-current rules to four cases that differ only in the material condition written into each, demonstrated by statement D, 'move the sheet away from the pole with uniform velocity if it is both, non-conducting and non-polar.', which is C with its condition negated.
- **Note:** D is tagged false as the printed key has it, at the level this chapter works at, where a non-conducting, non-polar sheet is treated as magnetically inert. The key is not re-judged here.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The period of a simple pendulum, $T = 2\pi\sqrt{L/g}$, is set by length and $g$ alone; the bob's mass cancels out of the equation of motion
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  A student holding $T \propto \sqrt{m}$ needs nothing else from the stem: the mass triples, so $T' = \sqrt{3}\,T$, and matching that against $T' = \frac{x}{2}T$ reads off $x = 2\sqrt{3}$.
- **Why:** This question requires how many times the period changes when the length is halved, demonstrated by "the new time period of oscillation is $\frac{x}{2}$ times its original time period", with the tripled mass absent from $T = 2\pi\sqrt{L/g}$.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A bar magnet's moment is pole strength times the straight-line separation of its poles, so bending the bar shortens that separation and cuts the moment
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $M$ is true of the magnet the stem started with, and bending removes no iron and demagnetises nothing, so a student who treats the moment as that unchanged material property hands the stem's own $M$ straight back. The moment is pole strength times pole separation, and the bent bar's poles sit only $L/2$ apart.
- **Why:** This question requires the new pole separation worked out from the bend and multiplied by the unchanged pole strength, demonstrated by "bent at the middle of its length such that the two arms make an angle $60^{\circ}$ with each other".
- **Note:** Option 2 is the stem's own printed value, the device the retired per-option list called `copied_from_stem`; its live family under section 5.1 is `answers_other_question`, since $M$ is true of the magnet before the bend and answers that question rather than the one asked.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A telescope in normal adjustment magnifies by $f_o/f_e$; the extra factor $\left(1+\frac{f_e}{D}\right)$ belongs only to the case where the final image is held at the near point
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $34$ is the correct answer to the other half of this standard pair of parts: with the final image brought to the least distance of distinct vision, $M = \frac{f_o}{f_e}\left(1+\frac{f_e}{D}\right) = 28 \times 1.2 = 33.6 \approx 34$. The stem asks only for the magnifying power for a distant object, where the second factor is absent and $M = 140/5 = 28$.
- **Why:** This question requires the magnifying power computed from the two printed focal lengths, demonstrated by "an objective of focal length $140\,\mathrm{cm}$ and an eye piece of focal length $5.0\,\mathrm{cm}$" with bare numbers as the four options.
- **Note:** The stem does not state the adjustment in words; the key of 28 reads "for viewing a distant object" as normal adjustment, which is the usual convention, while option 2's 34 is the value when the final image is at $25\,\mathrm{cm}$. Tagged as printed. `old_ncert_answer` was ruled out because no printed value has been altered, so the two numbers that label requires cannot both be named; 34 answers a different part of the same question, which is `answers_other_question`.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A terminal aldehyde needs the OH put on the end carbon by hydroboration-oxidation and then a mild oxidant such as PCC, because alkaline $\mathrm{KMnO_4}$ or $\mathrm{CrO_3}$ carries a primary alcohol past the aldehyde to the acid
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Steps (i) and (ii) are the hydroboration-oxidation that does put OH on the end carbon, so two of the four reagents match the key exactly; alk. $\mathrm{KMnO_4}$ then $\mathrm{H_3O^{\oplus}}$ carries 3-cyclohexylpropan-1-ol on to 3-cyclohexylpropanoic acid instead of stopping at the printed aldehyde.
- **Why:** This question requires the reagent sequence that effects a printed conversion, demonstrated by the stem 'Identify the correct reagents that would bring about the following transformation.' with numbered reagent lists as the four options.
- **Note:** The transformation lives in the figure, which the packet supplies as text ('allylcyclohexane → 3-cyclohexylpropanal') and as reaction SMILES 'C=CCC1CCCCC1>>O=CCCC1CCCCC1', so the question is complete enough to rate. Worth recording why the trap sits on 4 rather than on 1: options 1 and 2 differ only in the oxidant, and acting on the secondary alcohol that acid hydration gives, PCC and $\mathrm{CrO_3}$ both end at the same ketone, so the regiochemical error does not single out one option, whereas option 4 shares the key's first two steps and fails on one reagent.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The $\mathrm{S_N1}$ rate follows the stability of the carbocation that forms, and the benzylic cation from (1-bromoethyl)benzene is delocalised into the ring while a plain cyclohexyl cation is not and an aryl halide cannot ionise at all
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Bromocyclohexane is a secondary halide and genuinely does ionise, so ranking the four only by how many carbons sit on the C-Br carbon makes it the winner once the primary and the aryl halide are struck out; it undergoes $\mathrm{S_N1}$, but the stem asks for the fastest, and the resonance term the benzylic cation enjoys was never counted.
- **Why:** This question requires a known rule - $\mathrm{S_N1}$ rate follows carbocation stability - applied to four drawn halides, demonstrated by the stem 'The compound that will undergo $\mathrm{S_N1}$ reaction with the fastest rate is', which prints no numbers and names no reagent.
- **Note:** The four options arrive as '[drawn option] <name>', that is drawn structures described in words, and were read as real options. The printed shape is the retired `structure_options`, which maps to qtype `mcq` through category_retired.qtype, the same value E1's `plain_mcq` maps to. `read_diagram` was ruled out for `asks` because the drawings only print four nameable compounds; the work is the stability rule applied to them. Trap label reached through category_retired.trap_v2 `not_the_superlative` → `answers_other_question`, which is what the superlative stem 'fastest' creates.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Counting the $\sigma$ and $\pi$ bonds between two carbons: hybridisation settles ethane, ethene and ethyne, while the C$_2$ molecule is settled by its molecular-orbital filling, which puts both bonding pairs in $\pi$ orbitals
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  C$_2$ is two carbons bonded to nothing else, so the acetylene core is the picture reached for and the count comes out as one $\sigma$ and two $\pi$; the MO filling for C$_2$ is $\sigma_{2s}^2\sigma_{2s}^{*2}\pi_{2p}^4$, whose bond order of 2 is carried by two $\pi$ bonds with no net $\sigma$, and entry I belongs to ethyne instead.
- **Why:** This question requires the $\sigma$/$\pi$ count derived for each named species from its bonding model, demonstrated by List I placing 'carbon molecule, $C_2$' beside the three hydrocarbons, where no hybridisation picture exists and the entry 'two $\pi$-bonds' can come only from the molecular-orbital filling.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Ligand field strength, not shape, fixes the spin state: NH$_3$ pairs all six d electrons of Co(III) while F$^-$ leaves four unpaired, so two octahedral complexes of the same ion differ in magnetism
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Fluoride is the most electronegative ligand in the pair, so a student who ranks field strength by electronegativity makes $\mathrm{[CoF_6]^{3-}}$ the low-spin one and reads Statement II's assignment as the wrong way round, which leaves Statement I true and Statement II false.
- **Why:** This question requires the ligand field rule applied to a $d^6$ Co(III) centre, demonstrated by Statement I granting both complexes are 'octahedral but differ in their magnetic behaviour' while no criterion is printed anywhere in the question, so the student must supply that NH$_3$ is strong field and F$^-$ weak.
- **Note:** stem_en as stored carries only the two instruction lines; the two statements sit in the statements array, so the printed shape is complete and no source damage is involved.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** VSEPR: the shape names only the bonded atoms, while the lone pairs still occupy positions in the electron-pair geometry
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  XeF$_4$'s four bond pairs and two lone pairs make six electron domains pointing at the corners of an octahedron, so 'Octahedral' is a true description of the arrangement of its electron pairs, which is not what the pairing asks; the two lone pairs sit opposite each other and leave the four fluorines square planar.
- **Why:** This question requires VSEPR applied to each formula, demonstrated by List II printing 'Octahedral' and 'Square Planar' as separate entries, so the six electron pairs of XeF$_4$ must be held apart from the shape its four fluorines take.
- **Note:** List II is untitled in our record (the stem prints no 'List II (Shape)' header), so 'Octahedral' for XeF$_4$ is defensible if the lists are read as electron-pair geometries; the pairing is still forced, because SF$_6$ can take no other entry. Tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** First ionisation enthalpy rises across period 2 but dips at boron, whose lone 2p electron is easier to remove than beryllium's paired 2s electron, so B sits below Be
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Applying 'ionisation enthalpy increases across a period' straight through the stem's own list gives $\mathrm{Li} < \mathrm{Be} < \mathrm{B} < \mathrm{C} < \mathrm{N}$; the one place that general rule does not hold in this row is the Be-B step, where B at $801\,\mathrm{kJ\,mol^{-1}}$ falls below Be at $899$.
- **Why:** This question requires the five elements put into a sequence, demonstrated by the stem 'Arrange the following elements in increasing order of first ionization enthalpy'.
- **Note:** Trap label reached by taking the §5.2 name `ignores_exception` - the option is exactly what the general rule predicts and this row is the exception to it - to its live family `condition_missed` through category_retired.trap_v2. E1 gave `arrange_in_order`, which maps to qtype `mcq`.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Glucose's aldehyde group is locked up as a cyclic hemiacetal, so it still gives the silver mirror, the oxime and the cyanohydrin but fails Schiff's test and the $\mathrm{NaHSO_3}$ addition
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  $\mathrm{NaHSO_3}$ is the member of the exception pair a student holds securely, and the other remembered no-reaction line in the same paragraph is hydroxylamine giving nothing; drop the word pentaacetate from that line and $\mathrm{NH_2OH}$ joins $\mathrm{NaHSO_3}$. Free glucose does form the oxime, so only E of this pair belongs.
- **Why:** This question requires the reagent-by-reagent reactivity of glucose as the chapter prints it, demonstrated by the stem asking for the reagents 'with which glucose does not react to give the corresponding tests/products' across five named reagents.
- **Note:** E1's retired `list_of_statements` maps onto `statements`; the lettered items A-E are reagents rather than claims, but the printed shape is still a lettered block the options select a subset from. The negation ('does not react') sits in the task, which is what `negative_words_seen: NOT` records. Key (4) checks out: B and E are the two exceptions.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What each quantum number tells you about an orbital: $n$ its size, $l$ its shape, $m_l$ its orientation in space, $m_s$ the orientation of the electron's spin
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  'Shape of orbital' and 'Size of orbital' are printed in the same four-word frame with one near-twin word between them, so the pair can be attached to $l$ and $n$ the wrong way round once the two subscripted rows have been settled.
- **Why:** This question requires the line stated for each quantum number, demonstrated by List II printing 'Shape of orbital' and 'Size of orbital' as the entries that must be attached to $l$ and $n$, with nothing in the stem to derive either from.
- **Note:** Applied the rulebook's swap test: replace 'Size of orbital' with an unlike phrase such as 'mean distance of the electron from the nucleus' and the hesitation between the two entries largely goes, so the resemblance of the printed terms is doing the work. Adjacency in the quantum-number paragraph also holds, and by the tie-break the likeness wins.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Comparing atom counts means converting every quantity to moles: $4\,\mathrm{mol}$ is four times Avogadro's number, $4\,\mathrm{g}$ of He and $22.711\,\mathrm{L}$ at STP are one mole each, and $4\,\mathrm{u}$ is a single atom
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $4\,\mathrm{g}$ of helium is the chapter's anchor for one mole, $6.022\times10^{23}$ atoms, so the option that reproduces that remembered line is picked; it is true, but the stem asks which holds the highest count and $4\,\mathrm{mol}$ holds $4\times6.022\times10^{23}=2.4\times10^{24}$ atoms.
- **Why:** This question requires each quantity converted into a number of atoms before the four can be compared at all, demonstrated by options that print the same element in four different units - '$2.271098\,\mathrm{L}$ of helium at STP', '$4\,\mathrm{mol}$ of helium', '$4\,\mathrm{u}$ of helium' and '$4\,\mathrm{g}$ of helium'.
- **Note:** Trap label follows category_retired.trap_v2 `not_the_superlative` → `answers_other_question`: option 4 is a true statement of what one mole of helium is, set against a stem that asks for the highest count. `calculate` was chosen over `compare` because nothing can be compared until each option is converted to moles.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A reaction is redox only when some atom's oxidation number changes, so $\mathrm{BaCl_2+Na_2SO_4}$ is a partner exchange with nothing changed, while the halogen trade between $\mathrm{KClO_3}$ and $\mathrm{I_2}$ takes Cl from $+5$ to $0$ and I from $0$ to $+5$
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  K stays $+1$ and each O stays $-2$ on both sides of $\mathrm{2KClO_3+I_2\rightarrow 2KIO_3+Cl_2}$, so an oxidation-number check run on those atoms, plus the surviving $\mathrm{XO_3}$ skeleton, reads as a partner swap; the atoms this reaction turns on are the halogens, where Cl falls $+5\rightarrow 0$ and I rises $0\rightarrow +5$.
- **Why:** This question requires the oxidation-number rules applied to four printed equations, demonstrated by the stem 'Which reaction is NOT a redox reaction?' with whole balanced equations as the options.
- **Note:** E1_question_type is null because the options are reactions; the printed shape is the retired `reaction_options`, which maps to qtype `mcq` through category_retired.qtype. The task itself is negated ('NOT a redox reaction'), which is what makes the three redox equations the candidate traps rather than the key.
<!--/ecat-->

## Q61

Chemistry · inorganic · The p–Block Elements

Given below are two statements:
Statement I: The boiling point of hydrides of Group 16 elements follow the order $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$.
Statement II: On the basis of molecular mass, $\mathrm{H_2O}$ is expected to have lower boiling point than the other members of the group but due to the presence of extensive H-bonding in $\mathrm{H_2O}$, it has higher boiling point.
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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Boiling point of the Group 16 hydrides rises with molecular mass down the group, and hydrogen bonding alone lifts water above all of them
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Thermal stability of the Group 16 hydrides does fall down the group, so a student who carries that direction over to boiling point reads the printed $\mathrm{H_2O > H_2Te > H_2Se > H_2S}$ as backwards and marks Statement I false, while Statement II, which repeats the textbook sentence word for word, is ticked true.
- **Why:** This question requires the reason the textbook gives for water breaking the mass-driven trend, demonstrated by Statement II printing 'due to the presence of extensive H-bonding in $\mathrm{H_2O}$, it has higher boiling point' as the thing to be judged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Electronegativity rises across a period and falls down a group, with no break anywhere in this set, so the Pauling order runs Si $1.8$ < C $2.5$ < N $3.0$ < O $3.5$ < F $4.0$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  $\mathrm{F}<\mathrm{O}<\mathrm{N}<\mathrm{C}<\mathrm{Si}$ is the rehearsed sequence F, O, N, C, Si written out with the inequality signs left as they stand, so writing down the descending list and not re-reading the word 'increasing' lands here; it is the key's order element for element, backwards.
- **Why:** This question requires the five elements put into a sequence, demonstrated by the stem 'Arrange the following elements in increasing order of electronegativity' followed by 'Choose the correct answer from the options given below'.
- **Note:** E1 gave `arrange_in_order`, which maps to qtype `mcq`. Unlike q056 this row carries no exception for an option to reproduce, so the pull here is the direction of the inequality and option 1 is the key reversed element for element.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each iso- name says which variable is held fixed — temperature, volume or pressure — while adiabatic holds out the heat, not the temperature
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Isothermal, isochoric and isobaric share the whole of their printed shape except the stem that carries the meaning, so reading 'isobaric' as the temperature one hands isothermal the constant-pressure line and isobaric the constant-temperature line while the other two rows stay put.
- **Why:** This question requires the stated definition of each process, demonstrated by List II being those definitions verbatim — 'Carried out at constant temperature', 'Carried out at constant volume', 'Carried out at constant pressure' — so the pairing turns on what each name holds fixed and nothing is computed.
- **Note:** Applied the swap test: print 'constant-pressure process' in place of 'Isobaric process' and nothing is left to confuse it with isothermal, so the likeness of the iso- family, not its position in the table, carries the student.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Bohr energy goes as $Z^2/n^2$, so two one-electron species with the same $Z/n$ sit at the same energy
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Carrying only the $Z^2$ part of $E_n = -13.6\,Z^2/n^2$, the charge doubling from 2 to 4 multiplies the energy by 4 and the $1/n^2$ is left at 1, turning $-x$ into $-4x$.
- **Why:** This question requires the $Z^2/n^2$ scaling of the Bohr energy read as a factor, demonstrated by every option being a multiple of the printed $-x$ rather than a value in joules.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Faraday count = moles named in the stem $\times$ electrons transferred per formula unit, where the electron count is the change in oxidation state, not the oxidation state itself
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Fe$_2$O$_3$ carries two irons, so balancing 2Fe$^{2+}$ $\to$ 2Fe$^{3+}$ + 2e$^-$ reads off 2 F; the stem names 1 mol of FeO, which supplies only one of those two irons, so the charge required is 1 F.
- **Why:** This question requires a Faraday count computed row by row, demonstrated by List I printing the amounts '1 mol' and '1.5 mol of Ca from molten CaCl2', which must be multiplied by the electrons per formula unit to land on 1 F, 2 F, 3 F or 5 F.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a 1:1 neutralisation the reagent with fewer moles is used up, and what survives is the mole difference of the other one
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $25\,\mathrm{mL}$ of $0.75\,\mathrm{M}$ HCl is $18.75\,\mathrm{mmol}$, which consumes $18.75 \times 40 = 750\,\mathrm{mg}$ of NaOH — the mass that reacted, where the stem asked for the mass left.
- **Why:** This question requires a limiting-reagent subtraction worked from the stem's own numbers, demonstrated by '1 gram of sodium hydroxide' set against '25 mL of 0.75 M HCl' with masses as the options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A carbocation is stabilised by the alkyl groups bonded to the charged carbon itself, so tertiary beats secondary beats primary
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  In 2-methylpentan-3-yl the branch sits on C2, next door to the charged C3, so counting substituents one carbon away from the charge reads the centre as tertiary when only two alkyl groups are bonded to it.
- **Why:** This question requires the carbocation stability order applied to four skeletons it has not ranked before, demonstrated by 'The most stable carbocation among the following is' with no criterion printed and the substitution at the charged carbon the only thing separating the drawings.
- **Note:** The pattern classifier recorded statement_options, but the four options are drawn structures rather than statements; the printed shape is structure_options, which the retired-value map carries onto qtype mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $K_p = K_c(RT)^{\Delta n}$, so the two are equal only where the reaction leaves the number of gaseous moles unchanged
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Reading '$\mathrm{2BrCl}$ gives $\mathrm{Br_2 + Cl_2}$' as one molecule splitting into two drops the coefficient 2 and yields $\Delta n = +1$, where the balanced equation holds 2 moles of gas on each side.
- **Why:** This question requires $K_p = K_c(RT)^{\Delta n}$ applied to each printed equilibrium, demonstrated by four balanced equations carrying (g) labels and no numbers to compute.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Mn³⁺ is $d^4$ and Mn²⁺ is $d^5$, so reducing Mn³⁺ hands back the extra-stable half-filled shell and drives $E^\circ$ positive
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  An $E^\circ$ value describes the reduction Mn³⁺ → Mn²⁺, which runs $d^4 \rightarrow d^5$; attaching the remembered half-filled $d^5$ to the ion written first in the couple prints the same two configurations backwards.
- **Why:** This question requires the reason the book gives for the Mn³⁺/Mn²⁺ potential standing out, demonstrated by the stem's 'due to change of' and options that are configuration changes rather than potentials.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Fehling's reagent is made up at the bench from two solutions: A is aqueous copper sulphate, B is alkaline sodium potassium tartrate
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Solution B's composition is printed in the same line as A's, so holding the pair without the letters puts the fuller, named half — alkaline sodium potassium tartrate — against A.
- **Why:** This question requires what is in a named bench reagent, demonstrated by "Fehling's solution 'A' is" and four options that are reagent compositions.
- **Note:** On nearby_fact against look_alike_term I applied the swap test: replace 'sodium potassium tartrate' with two unlike words and the pull survives, because what carries the student is that the option is the other half of the A/B pair printed beside the answer, not any resemblance between the names. asks is experiment rather than fact_line because the rulebook files 'what is in a named reagent' under practical_procedure, which the retired-value map carries onto experiment.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Which reagent effects which conversion: ozonolysis cleaves a C=C to two carbonyls, CrO$_3$ takes a secondary alcohol to the ketone, hot alkaline KMnO$_4$ oxidises a benzylic side chain to the carboxylate salt, and benzoyl chloride with anhydrous AlCl$_3$ acylates an arene
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  CrO$_3$ is the strong chromium oxidant and a benzylic side chain is oxidisable, so ethylbenzene is paired with CrO$_3$; the product printed for that row is potassium benzoate, and the potassium can only come from the KOH that reagent III carries.
- **Why:** This question requires the reagent that effects each printed conversion, demonstrated by List I being four substrate-to-product arrows and List II four reagent sets, with the ethylbenzene row ending in 'potassium benzoate' and only one entry supplying KOH.
- **Note:** List I is printed as drawn structures; our record resolves them from the figure caption and the drawn species list, which both read A cyclohexylidenecyclohexane to 2 cyclohexanone, B benzene to diphenylmethanone, C cyclohexanol to cyclohexanone, D ethylbenzene to potassium benzoate, so the question is complete. One internal disagreement: the figure note says entry IV was visible only as '(i) O3' in the crop, while list_ii records '(i) O3 (ii) Zn-H2O'. The pairing is unaffected, since both workups give ketones from a tetrasubstituted alkene. Reported, not repaired.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Entropy rises when a process creates more freedom - a move into the gas phase or more moles of gas - and falls as a crystal is cooled towards 0 K
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  0 K is where the one entropy fact attached to temperature lives, so the cooling step is ticked as an entropy change without its direction being read. Cooling a perfect crystal to 0 K drives $S$ to zero, which is a decrease, and the stem asks only for increases.
- **Why:** This question requires the entropy rule applied to four fresh cases with no number produced, demonstrated by 'In which of the following processes entropy increases?' set over items as unlike as 'A liquid evaporates to vapour.' and '$\mathrm{Cl_{2(g)} \rightarrow 2Cl_{(g)}}$'.
- **Note:** E1's retired `list_of_statements` maps onto `statements`. The whole catch sits on item B, which appears in only one option, so the trap is named on the direction of $\Delta S$ rather than on the option being partly correct; option 3 also drops C, and that second move is carried as a second bad step on the same route.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The degree of a carbon atom is decided by how many other carbons it is bonded to: three carbons make it tertiary, four make it quaternary
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A carbon carrying two methyl groups is read as tertiary, but in 2,2-dimethylbutane that carbon holds four carbons and is quaternary, the next degree up in the same primary/secondary/tertiary/quaternary scheme.
- **Why:** This question requires the definition of a tertiary carbon applied to each named isomer, demonstrated by 'has two tertiary carbons' being the only criterion printed and all four options being $\mathrm{C_6H_{14}}$ isomers.
- **Note:** nearby_fact over look_alike_term: swapped the two degree names for two unlike words and the trap survives, because what carries the student is the adjacent member of the primary/secondary/tertiary/quaternary scheme, not any resemblance between the words 'tertiary' and 'quaternary'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Reaction quotient against equilibrium constant: work out $Q_C$ for the mixture in hand and compare it with $K_C$, since $Q_C > K_C$ drives the reaction backward
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Equilibrium is read off the equality of the three printed concentrations instead of from $Q_C = K_C$, and here $Q_C = 1$ against $K_C = 4 \times 10^{-3}$.
- **Why:** This question requires $Q_C$ computed from the printed concentrations and compared with the printed constant, demonstrated by the stem supplying '$K_C = 4 \times 10^{-3}$' alongside '$[\mathrm{A}] = [\mathrm{B}] = [\mathrm{C}] = 2 \times 10^{-3}\,\mathrm{M}$'.
- **Note:** qtype follows E1's statement_options, mapped through the retired list to statements: no lettered block is printed and each option is a full claim graded for correctness by 'which of the following is correct?'. asks is calculate rather than apply_rule because a quantity, $Q_C = 1$, must be produced from the stem's numbers before the direction rule can be used at all.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Among isomeric alkanes, branching rounds the molecule, cuts the surface available for contact and so lowers the boiling point
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The companion physical-property fact for branched isomers runs the other way, the near-spherical isomer packing best in the solid and melting highest, so a student who reaches for the melting-point picture reads n-pentane $>$ isopentane $>$ neopentane as wrong and marks Statement I incorrect while ticking Statement II's textbook sentence correct.
- **Why:** This question requires the taught reason for branching lowering boiling point, demonstrated by Statement II printing 'smaller surface area for contact, due to which the intermolecular forces between the spherical molecules are weak, thereby lowering the boiling point'. On the trap axis I applied the swap test: replace melting point with any unlike quantity taught beside boiling point and the pull survives, because position in the same lesson rather than resemblance between the words carries the student, so nearby_fact and not look_alike_term.
- **Note:** stem_en as stored carries only the two instruction lines; both statements sit in the statements array.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Lucas test: the alcohol that clouds at once is the one giving the most stable carbocation, so tertiary is immediate, secondary takes about five minutes and primary needs heating
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Butan-2-ol does react with Lucas reagent and give turbidity, so dropping the stem's 'instantaneously' makes it a right answer, when a secondary alcohol in fact takes about five minutes.
- **Why:** This question requires the Lucas reagent's reactivity order mapped onto four drawn alcohols, demonstrated by 'reacts instantaneously with Lucas reagent' and by all four options being $\mathrm{C_4H_{10}O}$ isomers differing only in where the OH sits.
- **Note:** Options 1, 3 and 4 are printed as drawn structures and arrive described in words; they were read as real options. Drawn-structure options still map to qtype mcq, so E1's plain_mcq is not contradicted. `experiment` was considered for asks because Lucas is a bench test, but the stem asks neither about a setup nor about what an observation means, and a reactivity comparison resting on carbocation stability is what the retired map sends to `reaction`.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Henry's law: at a fixed temperature a gas dissolves less as its $K_\mathrm{H}$ rises, so the smallest constant belongs to the most soluble gas
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Reading $K_\mathrm{H}$ as a measure of solubility ranks the gases straight down the printed constants, $145 > 35 > 2 \times 10^{-5}$, giving A > C > B, which is the key's B > C > A turned end to end.
- **Why:** This question requires three gases ranked by the reciprocal of their Henry's law constants, demonstrated by the stem printing '145, $2 \times 10^{-5}$ and $35\,\mathrm{kbar}$, respectively' and asking that 'the solubility of these gases in water follow the order'.
- **Note:** E1's pattern called this statement_options on 'full-statement options', but the printed options are orderings (A > B > C), not claims to be graded; the printed shape is a ranking question, which the current qtype list folds into mcq through retired arrange_in_order, and the ordering is recorded on the asks axis as `order`.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sublimation: a solid that passes straight into vapour on heating is purified by subliming it and recondensing the vapour, with no liquid stage in between
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Distillation is the purification that works by vaporising and recondensing, so reading only 'change ... to vapour state' reaches it, while the clause 'without passing through liquid state' is the one thing distillation cannot satisfy.
- **Why:** This question requires the purification technique the textbook ties to a named phase change, demonstrated by the stem's 'change from solid to vapour state without passing through liquid state' and its asking what the technique 'is known as'.
- **Note:** `experiment` was considered for asks because all four options are bench techniques, but the stem asks for the name attached to a printed principle and supplies no setup, data or observation to interpret, so the ask is a stated fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The isomerism types of coordination compounds are told apart by what moves: the donor atom of an ambidentate ligand (linkage), a counter-ion across the coordination sphere (ionisation), solvent in or out of the sphere (solvate), and ligand sets between two complex ions (coordination)
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  $\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$ is the one formula here that splits into two ions, so the name carrying the word ionization attaches to it, and the sulfate complex is left with coordination isomerism, the entry NCERT prints beside it in the same list of types.
- **Why:** This question requires each printed formula to be tested against the defining criterion of an isomerism type rather than the pairing to be recalled whole, demonstrated by '$\mathrm{[Co(NH_3)_6][Cr(CN)_6]}$' and '$\mathrm{[Co(NH_3)_5(SO_4)]Br}$', which separate only on whether both ions are complex or a single counter-ion crosses the coordination sphere.
- **Note:** E1's match_the_lists maps onto qtype match_columns; two printed columns and a pairing-code answer, so the pattern agrees with the printed shape. asks is set by what each row demands, not by the pairing, so compare was ruled out. All four formulae are also the worked examples NCERT prints for these four types, so a pure recall route (fact_line) reaches the answer too; apply_rule is recorded because the criterion that decides each row is readable off the printed formula. Trap axis: the look-alike test was applied first and fails, since 'ionization' and 'coordination' share no form; the wrong name is the entry printed beside the right one in the same NCERT list of isomerism types, so nearby_fact. Options 1 and 3 are each a single swapped pair and option 4 is both swaps, which leaves no filler option on this question. Key checks out as printed: option 2 reads A-II, B-III, C-IV, D-I.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An intramolecular hydrogen bond needs the donor H and the acceptor inside one molecule and within reach of each other, which on a benzene ring only the ortho arrangement allows
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  4-nitrophenol is the isomer carried as the hydrogen-bonding example, but the bonding it is named for is intermolecular: the para nitro group sits across the ring from the OH and cannot reach it.
- **Why:** This question requires the proximity condition for an intramolecular hydrogen bond applied to three ring isomers, demonstrated by 'Intramolecular hydrogen bonding is present in' being the only thing that separates the 2-, 3- and 4-nitrophenol options.
- **Note:** Options 2, 3 and 4 are printed as drawn structures and arrive described in words; they were read as real options, and drawn-structure options still map to qtype mcq. `nearby_fact` was ruled out on option 3 because the question that option does answer can be named, which nitrophenol shows intermolecular hydrogen bonding, and that is what `answers_other_question` is for.
<!--/ecat-->

## Q81

Chemistry · organic · Amines

Given below are two statements:
Statement I : Aniline does not undergo Friedel-Crafts alkylation reaction.
Statement II : Aniline cannot be prepared through Gabriel synthesis.
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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Aniline's amino lone pair binds the Lewis acid catalyst and kills Friedel-Crafts alkylation, and Gabriel synthesis needs an alkyl halide, so it cannot deliver an aryl amine
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Gabriel phthalimide synthesis is carried as the clean route to primary amines and aniline is a primary amine, so a student who applies the rule without its halide condition judges Statement II false while keeping the well-drilled Statement I true.
- **Why:** This question requires knowing what two named reactions do to one substrate, demonstrated by Statement I 'Aniline does not undergo Friedel-Crafts alkylation reaction.' and Statement II 'Aniline cannot be prepared through Gabriel synthesis.'
- **Note:** On the trap axis the device matches the retired 5.2 name ignores_exception (the option is right for the general rule and this case is its exception). Following 5.0 I took it to its live 5.1 family, condition_missed, since the rule is applied where its condition, an alkyl halide, does not hold; formula_misused was ruled out because the rule itself is remembered correctly and only its scope is not. Separately, the printed options mix wordings: option 1 reads 'incorrect ... true' and option 4 'correct ... false', while options 2 and 3 use true/false. That is printing variance and does not change the four verdicts.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The $-2$ oxidation state of group 16 grows harder to reach down the group as metallic character rises, and polonium hardly shows it at all.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Oxygen is the group-16 member carried as 'the exception' because it has no d orbitals and so cannot reach $+6$; that remembered exception is about the $+6$ state, not the $-2$ state the stem names.
- **Why:** This question requires the stated fact about which group-16 member fails to reach the $-2$ state, demonstrated by 'Among Group 16 elements, which one does NOT show $-2$ oxidation state?' over four bare element symbols with no criterion printed to apply.
- **Note:** Option 2 was weighed as nearby_fact as well, since oxygen's exception is printed in the same section as the polonium line. answers_other_question was taken because what carries a student there is a true claim about a different oxidation state ($+6$), not the position of the two lines on the page.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The Arrhenius equation holds two unknowns, $A$ and $E_a$, so $E_a$ can be extracted only from rate constants measured at two different temperatures.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Holding $k = Ae^{-E_a/RT}$ as a one-line formula, a student reads one $k$ at one temperature as enough to solve for $E_a$ and forgets that $A$ is unknown too, so a single measurement leaves two unknowns in one equation.
- **Why:** This question requires the Arrhenius relation to be applied to decide what has to be measured, demonstrated by the options naming data rather than values — 'rate constant at two different temperatures'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Spin-only moment $\mu=\sqrt{n(n+2)}$ depends only on the number of unpaired electrons, so two different $d$-counts - $d^4$ and high-spin $d^6$ - can share one moment
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Chromium's half-filled $3d^5$ is the configuration carried about the element, and keeping it for $\mathrm{Cr^{2+}}$ gives five unpaired electrons, matching $\mathrm{Mn^{2+}}$ at $5.92$ BM. The half-filled stability argument settles the neutral atom's configuration, not a dication's, and $\mathrm{Cr^{2+}}$ is $3d^4$.
- **Why:** This question requires each ion's unpaired-electron count turned into a moment and the moments compared, demonstrated by ‘Spin only’ magnetic moment is same for which of the following ions?' asked over five ions whose $d$-counts all differ.
- **Note:** E1's retired `list_of_statements` maps onto `statements`; each option reads 'A and D only', so the subset is accepted whole. Key (2) checks out: $\mathrm{Cr^{2+}}$ $d^4$ and high-spin $\mathrm{Fe^{2+}}$ $d^6$ both carry four unpaired electrons, $\mu=4.90$ BM. `asks` is `calculate` rather than `apply_rule` because a quantity is produced for each ion before the comparison can be made.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Taking logarithms of the Arrhenius equation gives $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$: a straight line of negative slope $-E_a/R$ with intercept $\ln A$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Keeping hold of 'the rate constant rises with temperature', a student draws the line rising and does not notice the axis is $1/T$, which runs the other way, so the slope $-E_a/R$ comes out positive.
- **Why:** This question requires four drawn plots to be read against the logarithmic form of the Arrhenius equation, demonstrated by 'Which plot of $\ln k$ vs $\frac{1}{T}$ is consistent with Arrhenius equation?' with options differing only in slope sign and intercept.
- **Note:** E1's pattern classifier returned statement_options, but the four options are drawn graphs described in words ('[drawn option] graph of ln k (y-axis) vs 1/T (x-axis) ...'), not statements to be judged; the printed shape is graph options, which is recorded as mcq. The drawn-option descriptions were treated as real, readable options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Each cation has a fixed group in the qualitative-analysis scheme, set by the reagent that precipitates it: $\mathrm{H_2S}$ in acid for II, $\mathrm{NH_4OH}$ for III, $\mathrm{H_2S}$ in ammonia for IV, ammonium carbonate for V, and $\mathrm{Mg^{2+}}$ left for VI
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  With the groups assigned correctly - $\mathrm{Cu^{2+}}$ II, $\mathrm{Al^{3+}}$ III, $\mathrm{Co^{2+}}$ IV, $\mathrm{Ba^{2+}}$ V, $\mathrm{Mg^{2+}}$ VI - writing the list from the highest group downwards opens it with $\mathrm{Mg^{2+}}$, and option 4 is the only list that runs that way. The stem fixes the direction as increasing, from 0 to VI.
- **Why:** This question requires each cation filed into its qualitative-analysis group and the five then sequenced, demonstrated by 'arrange them in increasing group number from 0 to VI' with a full ordering printed as each option.
- **Note:** E1 called this `arrange_in_order`, which has no counterpart among the six qtype values; the printed shape is a lettered block A-E with the options selecting an arrangement, so `qtype` is `statements` and the ordering demand is carried on `asks: order`. One honest limit on the trap: option 4 is the only option running downward and its first three places are the exact descending order, but it is not the exact reverse of the key - its last two are B then A where a strict reversal would read A then B - so the pick is completed by matching the opening.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a dilute solution $\Pi = CRT$, so the slope of $\Pi$ against concentration is $RT$: divide the slope by $R$ for the kelvin temperature, then convert to degrees Celsius.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Dividing the slope by $R$ gives $25.73/0.083 = 310$, and the option reading $310\,^{\circ}\mathrm{C}$ takes that as finished — the kelvin figure handed in against a Celsius unit, with the $-273$ never done.
- **Why:** This question requires a number computed from the stem's own data, demonstrated by 'a straight line with slope $25.73\,\mathrm{L\,bar\,mol^{-1}}$' and 'Use $R = 0.083$' having to be divided and the result converted to °C.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Carbonate allows three equivalent canonical forms, and a dipole moment is the vector sum of bond moments and the lone-pair moment rather than a reading of electronegativity differences.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Fluorine is far more electronegative than hydrogen, so comparing the two molecules on bond polarity alone puts $\mathrm{NF_3}$ above $\mathrm{NH_3}$; the order runs the other way because in $\mathrm{NF_3}$ the lone-pair moment opposes the resultant of the three N–F moments while in $\mathrm{NH_3}$ it reinforces them.
- **Why:** This question requires each printed claim to be graded against a stated fact, demonstrated by the stem being only the instruction 'Identify the correct answer.' above four unconnected claims such as 'Three canonical forms can be drawn for $\mathrm{CO_3^{2-}}$ ion'.
- **Note:** apply_rule was ruled out for asks: each option is settled against a line the chapter prints — carbonate's three canonical forms, ozone's two, $\mathrm{BF_3}$'s zero dipole moment, and the $\mathrm{NH_3}$ against $\mathrm{NF_3}$ comparison — rather than by applying a rule to a case not met before.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An empirical formula comes from dividing each element's mass percentage by its atomic mass and reducing those mole numbers to the smallest whole-number ratio.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Treating the percentages as the mole ratio skips the division by atomic mass: $32:20:48$ divided by the smallest figure, 20, gives $1.6:1:2.4$, and rounding both outer figures to 2 prints $\mathrm{A_2BC_2}$.
- **Why:** This question requires mass percentages to be converted into a mole ratio by computation, demonstrated by 'remaining percentage of C' and 'Given atomic masses of A $= 64$; B $= 40$; C $= 32\,\mathrm{u}$' having to be divided into the percentages before the ratio can be read.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** PBr$_3$ swaps the alcohol's OH for Br without touching the ring; alcoholic KOH then eliminates HBr to the more substituted alkene
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked all four options as stored: each carries only the bare text "A =, B =" and the drawn structures are lost, so there is no option content for any route to land on.
- **Why:** This question requires the two products of a printed two-step scheme to be named together, demonstrated by the stem "Major products A and B formed in the following reaction sequence, are" and by every option reading "A =, B =".
- **Note:** Source damage, not a question defect: the stem and the scheme survive in figure_image.text ("2-methylcyclohexan-1-ol →[PBr₃] A (major) →[alc. KOH, Δ] B (major)"), but the four options carry only the labels "A =, B =" and none of the drawn structures, so the four options are indistinguishable as stored. Rulebook §5a: review_status source_incomplete, no trap tag, repair task is to re-extract the option structures from q090.png. E1's pattern said arrange_in_order ("6 arrange/sequence"); nothing here is ordered, and the answer's form is a pair of products, so I record two_part.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hofmann bromamide degradation shortens the chain by one carbon: the amide's carbonyl carbon leaves, so a C$_4$ amide yields a C$_3$ amine
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The chain shortens only in the last step, so carrying B's four carbons straight through gives the C$_4$ amine; butanamide's carbonyl carbon leaves as carbonate and C is the C$_3$ amine, propylamine.
- **Why:** This question requires each printed reagent to be mapped to the transformation it performs until the last product is reached, demonstrated by the three labelled arrows "NaCN", "OH$^-$ / Partial hydrolysis" and "NaOH / Br$_2$" and by the options being single named compounds.
- **Note:** E1's pattern said arrange_in_order ("6 arrange/sequence"); the printed shape is a multi-arrow scheme in the stem with four single-name options, which the rulebook's tie-break settles by the answer's form, so qtype is mcq. Trap axis: butylamine is a lone wrong name, so by rule 5 the choice is nearby_fact or look_alike_term; swapping propylamine/butylamine for two unlike words leaves the trap alive, because what carries the student is the neighbouring preparation method, so nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** $K_c$ is fixed by one equilibrium mixture, then reused with the 2:1:1 stoichiometry to get the degree of dissociation of a fresh 0.1 M charge of NO
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Squaring $2.8\times10^{-3}$ to $7.84\times10^{-7}$ instead of $7.84\times10^{-6}$ turns $K$ from 1.6 into 16, and the same algebra then gives $\alpha/(1-\alpha)=8$, i.e. $\alpha=8/9=0.8889$.
- **Why:** This question requires a number computed from the stem's own concentrations, demonstrated by "If $0.1\,\mathrm{mol\,L^{-1}}$ of NO(g) is taken in a closed vessel, what will be degree of dissociation ($\alpha$)" with four numerical options.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** PCl$_3$ is stripped of all three chlorines by three alcohol molecules and ends as phosphorous acid; PCl$_5$ gives up one chlorine and ends as phosphoryl chloride
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Both printed species are the right ones and only their slots are exchanged: reading the oxychloride as the trichloride's residue puts POCl$_3$ at A, but $3\mathrm{ROH}+\mathrm{PCl_3}$ hands away all three chlorines, leaving H$_3$PO$_3$.
- **Why:** This question requires both phosphorus by-products to be assigned to the right equation at once, demonstrated by "The products A and B obtained in the following reactions, respectively, are" and by each option printing two species.
- **Note:** E1's pattern said plain_mcq by default, but each option is a pair accepted or rejected whole (the rulebook's pair_options, §1), and the stem says "respectively", so I record two_part. Trap axis: option 4 is a two-part option with one part failing, so half_right was available, but the failure has a nameable pull (phosphorous H$_3$PO$_3$ against phosphoric H$_3$PO$_4$) and would have been look_alike_term; I kept the primary trap on option 2 because the stem's "respectively" and its printed 3:1 coefficients make the assignment the live decision, and option 2 holds both correct species with only the slots exchanged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A lanthanoid ion is diamagnetic only at 4f$^0$ or 4f$^{14}$, so the charge on the ion, not the element, decides
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Cerium's empty-f ion is Ce$^{4+}$ and the filled-f ion here is Yb$^{2+}$; storing the elements rather than the charges lands on the ions printed beside them, but Ce$^{3+}$ is 4f$^1$ and Eu$^{2+}$ is 4f$^7$, both paramagnetic.
- **Why:** This question requires the diamagnetism rule to be applied to named ions, demonstrated by "The pair of lanthanoid ions which are diamagnetic is", where each option's charge has to be turned into a 4f count before the rule can decide anything.
- **Note:** E1's pattern said plain_mcq by default; each option is a pair of ions accepted or rejected whole (the rulebook's pair_options), so I record two_part. Trap axis: both items in option 3 are lone wrong names, so by rule 5 the choice is nearby_fact or look_alike_term; swapping the symbols for unlike species leaves the pull intact, because what carries the student is that $+3$ is the characteristic state printed beside the f$^0$ list and Eu$^{2+}$ is the $+2$ ion printed beside Yb$^{2+}$, so nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Two-temperature Arrhenius form: a known rate ratio across 300 K to 330 K fixes the activation energy
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  $\frac{1}{300}-\frac{1}{330}=\frac{30}{99000}=3.03\times10^{-4}$, but with the zero dropped it reads $\frac{30}{9900}=3.03\times10^{-3}$, which divides 11.53 into 3804 J/mol and converts to the printed 3.80 kJ/mol.
- **Why:** This question requires a number computed from the stem's own data, demonstrated by "Calculate the energy of activation. Given $R=8.314\,\mathrm{J\,K^{-1}\,mol^{-1}}$, $\log 4=0.6021$".
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Permanganate has two faces on an alkene: cold, dilute and alkaline it adds two OH groups, hot and acidic it cuts the double bond and oxidises each fragment up to the carboxylic acid
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Baeyer's reagent is the $\mathrm{KMnO_4}$ reaction carried for an alkene, so with $\mathrm{KMnO_4}$ over the arrow one OH is put on each alkene carbon and the glycol ring$-\mathrm{CH(OH)}-\mathrm{CH(OH)}-$ring is taken as 'P'. The printed $\mathrm{H^+}$ is the cleaving condition, which breaks the C$-$C bond instead of hydroxylating it.
- **Why:** This question requires the product of hot acidic permanganate oxidation of a disubstituted alkene, demonstrated by '$\mathrm{KMnO_4/H^+}$' printed over the arrow while the options print the glycol, the aldehyde and the acid side by side.
- **Note:** The printed shape is a reaction scheme in the stem with structures as the four options; the six-value qtype axis has no value for either, so E1's plain_mcq maps to mcq and the shape is recorded here. The options render the cyclohexyl ring as the bare word 'ring' (the figure text names the substrate 1,2-dicyclohexylethene); I checked that the four options stay distinguishable without the ring's identity, since they differ in the oxidation state of the two central carbons, so the abbreviation does not touch the tagging.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Mohr's salt solution is made up in dilute sulphuric acid: the added $\mathrm{H^+}$ pushes back the hydrolysis of $\mathrm{Fe^{2+}}$, and sulphate is the one anion the double salt already contains, so nothing is introduced that could oxidise or tie up the iron
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Dilute hydrochloric acid is the other dilute mineral acid on the same bench list and supplies $\mathrm{H^+}$ just as well, so the rule 'acid suppresses hydrolysis' lands on the acid printed beside the right one. Chloride is a new anion: it is oxidised by the permanganate this solution is titrated against and it complexes iron, which is why the sulphate already in the salt is the one used.
- **Why:** This question requires the acid that the Mohr's salt preparation specifies, demonstrated by the stem's 'which of the following acid is added to prevent hydrolysis of $\mathrm{Fe^{2+}}$ ion' with sulphuric acid printed twice at two strengths. On the trap axis I applied the swap test: 'hydrochloric' does not resemble 'sulphuric' as a word, and it is reachable only because it is the acid printed beside sulphuric in the list of dilute bench acids, so position does the work and the label is nearby_fact rather than look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Reversible isothermal work, $w=-nRT\ln(P_1/P_2)$, where the minus sign records that an expanding gas does work on its surroundings
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  $nRT\ln(P_1/P_2)=1\times 2.0\times 298\times\ln 2=413.14$, and reporting the work done BY the expanding gas as a positive number lands on the printed $+413.14$ calories. In the convention the chapter uses, work done by the system is negative, so the expansion gives $-413.14$ calories.
- **Why:** This question requires the reversible isothermal work computed from the stem's own numbers, demonstrated by 'Given $R = 2.0\,\mathrm{cal\,K^{-1}\,mol^{-1}}$' supplied with the pressures 20 atmosphere and 10 atmosphere.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homoleptic means one kind of ligand and heteroleptic more than one kind; the prefix is the whole distinction
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Homoleptic and heteroleptic differ only in the prefix on a shared stem, so a student carrying the pair the wrong way round reads Statement I's two labels as swapped and marks it false, while Statement II, which states the criterion without using either term, checks out straight off the printed formulas.
- **Why:** This question requires the stated meaning of two coordination terms, demonstrated by Statement II printing the criterion itself, 'Complex $\mathrm{[Co(NH_3)_6]^{3+}}$ has only one kind of ligands but $\mathrm{[Co(NH_3)_4Cl_2]^{+}}$ has more than one kind of ligands.' On the trap axis I applied the swap test: replace homoleptic and heteroleptic with two unlike words and the pull disappears, so the resemblance of the names carries the student and the label is look_alike_term, not nearby_fact.
- **Note:** stem_en as stored carries only the instruction lines; both statements sit in the statements array.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Faraday's first law: mass deposited equals the equivalent weight times the number of faradays passed, and for copper the equivalent weight is $63/2$ g
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The charge passed is $9.6487\times 100=964.87$ C against a faraday of 96487 C, and the two carry the same digit string, so the division is read off as 0.1 faraday instead of 0.01; $31.5\times 0.1$ prints as 3.15 g.
- **Why:** This question requires the mass computed from Faraday's first law, demonstrated by the stem supplying '$9.6487\,\mathrm{A}$', '$100$ seconds', 'Molar mass of $\mathrm{Cu}$ : $63\,\mathrm{g\,mol^{-1}}$' and '$1\,\mathrm{F} = 96487\,\mathrm{C}$'.
- **Note:** The stem reads 'a voltmeter containing copper sulphate solution' where a voltameter (coulometer) is meant; the slip does not change what is computed, so the question is tagged as printed.
<!--/ecat-->

## Q101

Biology · botany · Biomolecules

Lecithin, a small molecular weight organic compound found in living tissues, is an example of:

- (1) Carbohydrates
- (2) Amino acids
- **(3)** Phospholipids
- (4) Glycerides

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solution** — answer (3)

> *Some lipids have phosphorous and a phosphorylated organic compound in them. These are phospholipids. They are found in cell membrane. Lecithin is one example.*
>
> — `BIO11L-CH09-P09`

That line calls lecithin an example of the lipids carrying phosphorous - the phospholipids of the cell membrane. So lecithin is a phospholipid, not a glyceride.

*Figure on the card: a diagram drawn for this solution. Both are lipids built on glycerol; only the phospholipid carries a phosphorus head group, and that is why lecithin is option 3.*

<details><summary>the full reason, and why each other option fails</summary>

Lecithin is a lipid. Lipids are sorted by what is joined to them. Many lipids have glycerol esterified with fatty acids; these are monoglycerides, diglycerides and triglycerides, the fats and oils. Some lipids instead carry phosphorous and a phosphorylated organic compound. Those are the phospholipids, they are found in cell membrane, and lecithin is the example given for them. That phosphorous-containing part is what settles it: lecithin is a phospholipid, so option 3 is correct. Notice the trap in option 4 - glycerides are lipids too, but they are only glycerol plus fatty acids, with no phosphorous and no phosphorylated organic compound.

- **(1)** Carbohydrates are not lipids. Lecithin is named among the lipids, as the example of a lipid carrying phosphorous and a phosphorylated organic compound.
- **(2)** Amino acids are not lipids either. Lecithin has phosphorous and a phosphorylated organic compound in it, which places it with the phospholipids.
- **(4)** Glycerides are the lipids in which fatty acids are esterified with glycerol - the monoglycerides, diglycerides and triglycerides, also called fats and oils. They have no phosphorous and no phosphorylated organic compound, so lecithin does not sit here.

</details>



**NCERT:** Biomolecules (Class XI, Chapter 9) · 9.1 How to Analyse Chemical Composition? · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q101_f840ee1f_03112026.png?v=f840ee1f37ee)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q101_a6a47ac4_03112026.png?v=a6a47ac479bb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lecithin is the textbook phospholipid: a glycerol backbone carrying fatty acids plus a phosphate-choline head, which is what puts it in membranes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who knows lecithin is a fat built on glycerol and fatty acids stops at 'Glycerides', the class printed just before phospholipids in the same lipid passage, and misses that the phosphate head is what names this molecule.
- **Why:** This question requires the class the textbook assigns to a named biomolecule, demonstrated by the stem giving only the name — 'Lecithin, a small molecular weight organic compound found in living tissues, is an example of:' — with four coordinate biomolecule classes as options and no criterion printed to apply.
- **Note:** Lecithin is a phosphoglyceride, so option 4 is not wholly false as chemistry; the key follows the textbook, which names lecithin only as its phospholipid example. Tagged as printed. look_alike_term was ruled out by the swap test: 'glyceride' and 'phospholipid' do not resemble each other, and replacing one with an unlike word leaves the pull intact, because what carries the student is the glycerol backbone being described in the adjacent line.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The four causes the chapter names for biodiversity loss -- habitat loss and fragmentation, over-exploitation, alien species invasion and co-extinction -- and that mutation and migration are not among them
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The chapter names four major causes and only three of them are printed as items, so a student who has stored the count rather than the names fills the fourth slot with Mutation and takes the four-item option.
- **Why:** This question requires the chapter's own list of major causes of biodiversity loss to be checked item by item, demonstrated by 'These are regarded as major causes of biodiversity loss' printed above lettered items that include 'Mutation' and 'Migration'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A test cross reads a dominant plant's hidden allele by crossing it with the homozygous recessive, so each offspring's own colour reports one allele directly
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Holding only 'to find a hidden genotype, cross it back to a parent', a student reaches for the dominant parent BB; but BB x BB and BB x Bb both give nothing but black seeds, so the cross reports nothing.
- **Why:** This question requires a stated rule applied to a named case, demonstrated by 'In order to find out the genotype of the black seed plant, with which of the following genotype will you cross it?', where the options are candidate tester genotypes and no quantity is asked for.
- **Note:** Flagging the key rather than re-judging it: option 4 (Bb) also separates BB from Bb, since white seeds appear only if the unknown is Bb, so the key rests on the textbook definition of a test cross rather than on genetics alone. Tagged as printed, verdict arguable_key.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A transcription unit is promoter, structural gene and terminator, the promoter lying upstream and the terminator downstream of the gene being copied
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The operon map from the regulation section of the same chapter — repressor, operator, structural gene — is the labelled DNA diagram most readily to hand, so a student fits those three labels to 'the three regions'; the unit's own three are promoter, structural gene and terminator.
- **Why:** This question requires the three regions the textbook names for a transcription unit, demonstrated by 'defined primarily by the three regions in DNA and these are with respect to upstream and down stream end', with each option supplying a complete triple that stands or falls whole.
- **Note:** E1 recorded statement_options on 'full-statement options', but the printed options are not statements: each is a set of three region names accepted or rejected whole, which the rulebook calls pair_options in §1. The nearest live qtype for a multi-component answer is two_part, used here; if the retired map sends pair_options elsewhere, this is the field to correct. On the trap axis the promoter/operator near-likeness was considered, but the swap test puts the pull on position: the option transplants a whole triple from the regulation section, so it survives replacing any one of those names with an unlike word — nearby_fact, not look_alike_term. half_right was ruled out because two of the option's three parts fail, so it is not a nearly-complete set.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Water-pollinated flowers are small and unrewarding, their pollen is ribbon-like, mucilage-protected and carried passively in water, and water lily, though aquatic, is pollinated by insects or wind
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Colour and nectar are what the same section states of animal-pollinated flowers one paragraph earlier, so a student who carries that sentence across to Vallisneria accepts A and then has to drop the negatively worded B to fit a four-item option.
- **Why:** This question requires each printed statement about water pollination to be checked against the stated facts, demonstrated by option 4 differing from the key only in taking 'The flowers of Vallisneria are colourful and produce nectar.' for 'The flowers of water lily are not pollinated by water.'
- **Note:** The NOT in negative_words_seen sits inside statement B, not in the task. Likeness test on the trap: replacing Vallisneria and water lily with two unlike plant names leaves the pull intact, because the colour-and-nectar sentence is carried over by its position in the same section, so nearby_fact and not look_alike_term.
<!--/ecat-->

## Q106

Biology · botany · Anatomy of Flowering Plants

Bulliform cells are responsible for

- (1) Providing large spaces for storage of sugars.
- **(2)** Inward curling of leaves in monocots.
- (3) Protecting the plant from salt stress.
- (4) Increased photosynthesis in monocots.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solution** — answer (2)

> *When they are flaccid due to water stress, they make the leaves curl inwards to minimise water loss.*
>
> — `BIO11L-CH06-P19`

The 'they' here is the bulliform cells of a grass leaf: short of water they turn flaccid and the leaf curls inwards. That inward curling is what they do.

*Figure on the card: the printed diagram, with the deciding parts marked. In the monocot half (b), look at the upper (adaxial) epidermis over the vein: the enlarged, empty, colourless bulliform cells that go flaccid under water stress and curl the leaf inwards.*

<details><summary>the full reason, and why each other option fails</summary>

Bulliform cells belong to the grass leaf. Certain adaxial epidermal cells lying along the veins become large, empty and colourless, and these are the bulliform cells. What they do depends on water. When they have absorbed water and are turgid, the leaf is held open and its surface stays exposed. Under water stress they lose that water and turn flaccid, and the leaf curls inwards, so less surface is exposed and water loss is reduced. Grasses are monocots, so this inward curling is how the monocot leaf answers a shortage of water. That is what option 2 states.

- **(1)** These cells are described as large, empty and colourless. The space in them is taken up by water, and it is the absorbing and losing of that water that turns them turgid or flaccid. No storage of sugars is attached to them.
- **(3)** The only stress linked to bulliform cells is water stress, which makes them flaccid. Nothing connects them with salt.
- **(4)** They are colourless cells, so they do not add to photosynthesis. Their action actually curls the leaf inwards, which hides the leaf surface instead of exposing more of it.

</details>



**NCERT:** Anatomy of Flowering Plants (Class XI, Chapter 6) · 6.2.6 Isobilateral (Monocotyledonous) Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q106_5c62a3bd_03112026.png?v=5c62a3bddb3a)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q106_e0978af0_03112026.png?v=e0978af0957a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bulliform cells are the large empty epidermal cells of grass leaves; when they lose water they go flaccid and roll the leaf inward to cut further loss
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The description of bulliform cells as large, empty, colourless cells is printed one line before their function, so a student who stops at the description converts 'large empty cells' into storage space; what fills them is water, and what it buys is the inward curling.
- **Why:** This question requires the function the textbook states for a named cell type, demonstrated by the stem 'Bulliform cells are responsible for' followed by four rival functions with no criterion printed to apply.
- **Note:** E1 recorded statement_options; by the rule that long option sentences do not make a statements question, the printed shape is a plain mcq whose options happen to be full-sentence functions, so qtype is mcq. look_alike_term was ruled out on the primary trap: 'storage of sugars' resembles nothing in the keyed answer, and the pull comes from the adjacent printed description.
<!--/ecat-->

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

**Solution** — answer (2)

> *Some common members are Agaricus (mushroom) (Figure 2.5c), Ustilago (smut) and Puccinia (rust fungus).*
>
> — `BIO11L-CH02-P39`

That line names Agaricus as the mushroom, Ustilago the smut and Puccinia the rust fungus — so B-II, C-IV, D-I. Only option 2 has all three.

<details><summary>the full reason, and why each other option fails</summary>

Three of the four names come from one list of Basidiomycetes: Agaricus is the mushroom, Ustilago the smut and Puccinia the rust fungus. So B-II, C-IV and D-I. That already fixes the answer, because only one option carries all three. Rhizopus is not a basidiomycete at all; it sits with the Phycomycetes, whose mycelium is aseptate and coenocytic, and it is the bread mould. So A-III. Together the match is A-III, B-II, C-IV, D-I, which is option 2. The trap is swapping Agaricus and Puccinia, or sending Rhizopus to the rust-and-smut group.

- **(1)** Calls Rhizopus the rust fungus and Ustilago the bread mould. Rhizopus is the bread mould, placed among the phycomycetes; Puccinia is the rust fungus and Ustilago the smut.
- **(3)** Makes Rhizopus the mushroom and Agaricus the rust fungus. Agaricus is the mushroom and Rhizopus the bread mould, so both ends of this match are wrong.
- **(4)** A-III and B-II are right, but the last two are swapped: Puccinia is the rust fungus and Agaricus the mushroom, not the reverse.

</details>



**NCERT:** Biological Classification (Class XI, Chapter 2) · 2.3.1 Phycomycetes; 2.3.3 Basidiomycetes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q107_b9535fda_03112026.png?v=b9535fda1144)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q107_2f4314a7_03112026.png?v=2f4314a74200)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fungal classes through their stock examples: Rhizopus is the bread mould of Phycomycetes, while Agaricus, Ustilago and Puccinia are the basidiomycete mushroom, smut and rust
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  NCERT prints the three basidiomycete genera with their common names in one breath, so a student who has locked Rhizopus-bread mould and Ustilago-smut can hold mushroom and rust as a leftover set without holding which genus takes which, and option 4 is the code that swaps exactly those two.
- **Why:** This question requires the common name NCERT prints for each named fungal genus, demonstrated by List II being four of those names - 'Bread mould', 'Smut fungus', 'Rust fungus', 'Mushroom' - with no criterion in the stem to apply to anything. Applied the likeness test on the trap: 'Puccinia' and 'Agaricus' do not resemble each other, and replacing them with two unlike words leaves the swap standing, because what carries it is their sitting in one printed basidiomycete list, so nearby_fact and not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each sub-stage of prophase I is recognised by one event: chromosomes become visible at leptotene, the synaptonemal complex forms at zygotene and is dissolved at diplotene
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The synaptonemal complex is met first as the thing zygotene builds, so that association is carried to Statement II and 'diplotene' is read as the wrong stage for it.
- **Why:** This question requires two prophase I sub-stage events to be checked against the lines NCERT prints for each, demonstrated by Statement I naming 'leptotene stage' for chromosomes becoming 'gradually visible under light microscope' and Statement II naming 'dissolution of synaptonemal complex' as the mark of diplotene. The trap is nearby_fact on the swap test: replace 'zygotene' with an unlike word and the pull survives, because what carries the student is the complex being printed beside the stage asked about, not any likeness between the two stage names.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which microbe industry uses for which product: brewer's yeast for ethanol, Clostridium butylicum for butyric acid, Trichoderma polysporum for cyclosporin-A, Streptococcus for streptokinase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Cyclosporin-A and streptokinase are introduced in consecutive sentences of the same bioactive-molecules passage, so a student who recalls both molecules but not which microbe makes which puts streptokinase on the fungus and cyclosporin-A on the bacterium, which is option 2.
- **Why:** This question requires which product NCERT names for each listed microbe, demonstrated by List II reading 'Ethanol', 'Streptokinase', 'Butyric acid', 'Cyclosporin-A' against four organism names. Applied the likeness test on the trap: 'cyclosporin-A' and 'streptokinase' are nothing alike as words and the swap survives replacing them with two unlike terms, because the pull is their being introduced side by side in one passage, so nearby_fact and not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cofactors come in three kinds, and carboxypeptidase's is a metal ion, zinc, rather than an organic prosthetic group or a vitamin-derived coenzyme
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Haem is the cofactor example printed in the same passage, where it is the prosthetic group of peroxidase and catalase, so a student recalling that line brings haem across to carboxypeptidase; carboxypeptidase's cofactor is the metal ion zinc.
- **Why:** This question requires the cofactor the textbook pairs with a named enzyme, demonstrated by 'The cofactor of the enzyme carboxypeptidase is:' with one metal ion set against three organic cofactors drawn from the same passage.
- **Note:** look_alike_term was ruled out by the swap test: haem, zinc, niacin and flavin resemble each other in no way, and the pull survives replacing any of them with another unlike cofactor name, because what carries the student is the passage printing all of these examples together.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parenchyma and collenchyma are both living simple tissues and only sclerenchyma is dead; vessels are the xylem element that marks angiosperms off from gymnosperms
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Dead' belongs to sclerenchyma, the third '-enchyma' in the same taught trio, so a student holding the three names but not the three properties lets Statement I stand and reads both statements as true.
- **Why:** This question requires the living-or-dead status of a named simple tissue plus the vessel contrast between the two seed-plant groups, demonstrated by Statement I's 'Parenchyma is living but collenchyma is dead tissue'. The trap is look_alike_term: on the swap test, exchanging collenchyma and sclerenchyma for two unlike words takes most of the pull away, because the shared '-enchyma' ending is what lets one tissue's property slide onto the other; position holds as well, and §5.1 gives likeness precedence when both do.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Hypogynous, perigynous and epigynous say where calyx, corolla and androecium sit relative to the ovary: below a superior ovary, level with it on a raised thalamus rim, or borne on top of an ovary sunk into the thalamus
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who reads (a) correctly as perigynous expects the second figure to show a different type, since three of the four options pair two unlike names, and so assigns (b) epigynous; the key makes both flowers perigynous, so the half that is right scores nothing.
- **Why:** This question requires two drawn flowers read against the hypogynous-perigynous-epigynous criterion, demonstrated by 'from the given figures (a) and (b)' and by options that must answer both figures at once, '(a) Perigynous; (b) Epigynous'.
- **Note:** The figure is present in the source (sha256 recorded), but my instruction limits me to the input file, so I did not open the image. The trap is therefore built only on the printed option set and the key — three options pair two unlike names, one repeats a name — and on the (a) reading the key implies; no claim is made about what the drawings contain. E1 recorded statement_options, which contradicts the printed shape: the options are two labelled parts answered together, with a figure gating the question, so qtype is two_part and asks is read_diagram.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the logistic equation each symbol is a named quantity: $N$ is population density, $r$ the intrinsic rate of natural increase, and $K$ the carrying capacity the habitat can support
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  $r$ and $K$ stand in the same printed equation, and the sentence under it glosses $r$ as the 'intrinsic rate of natural increase', so a student who stored that phrase without the letter it belongs to attaches it to $K$.
- **Why:** This question requires the name attached to one symbol of a printed relation, demonstrated by the stem supplying the whole equation and asking only what '$K$ indicates'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Per $\mathrm{CO_2}$ fixed the Calvin cycle spends 3 ATP and 2 NADPH: two ATP and both NADPH on reducing the two PGA, the third ATP on regenerating RuBP
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  What gets stored is the pair of figures 3 and 2, not which cofactor takes which, so a student holding '3 and 2 for one $\mathrm{CO_2}$' assigns the larger figure to NADPH and lands on 2 ATP with 3 NADPH.
- **Why:** This question requires the stored per-$\mathrm{CO_2}$ cost of the Calvin cycle, demonstrated by the stem supplying no numbers of its own and asking 'how many molecules of ATP and NADPH are required for every molecule of $\mathrm{CO_2}$ fixed'.
- **Note:** E1's pattern returned statement_options on '15 full-statement options', but each option is a pair of counts rather than a statement to be judged, so the printed shape is a plain MCQ and qtype is recorded as mcq.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The dark reaction fixes $\mathrm{CO_2}$ using the ATP and NADPH handed over by the light reaction, and needs neither light nor chlorophyll of its own
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The stored line is that the biosynthetic phase runs on the ATP and NADPH made in the light reaction, so a student ticks exactly that pair and leaves out $\mathrm{CO_2}$, the carbon the cycle actually fixes.
- **Why:** This question requires the stated requirements of the dark reaction, demonstrated by 'Light' and 'Chlorophyll' being printed as items A and B under 'required for the dark reaction of photosynthesis'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A gene of interest on its own carries no origin of replication, so it cannot multiply by itself; it is kept only by integrating into the host genome and replicating with it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The stem's condition is a piece carrying only the gene of interest, and a student who reads past that word applies the general cloning fact -- recombinant DNA put into a host multiplies there -- and ticks the two statements that say this piece replicates on its own.
- **Why:** This question requires the replication rule to be applied to the case the stem supplies, demonstrated by 'a piece of DNA carrying only gene of interest' in the stem against item A's 'would be able to multiply itself independently in the progeny cells of the organism'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Dedifferentiation is a fully mature, non-dividing cell regaining the power to divide; redifferentiation is the same cell's products losing that power again
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Redifferentiation' and 'dedifferentiation' differ by one syllable and both name something happening to an already mature cell, so a student who holds the pair but not what each prefix does takes the wrong half of the pair.
- **Why:** This question requires the process name attached to a printed textbook example, demonstrated by the stem reproducing that example's own words, 'interfascicular cambium from fully developed parenchyma cells'.
- **Note:** Applied the swap test on the trap axis: replace 'redifferentiation' with a word unlike 'dedifferentiation' and the pull dies, so the likeness and not the position is doing the work, which makes it look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q118

Biology · botany · Biodiversity and Conservation

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex situ conservation takes a threatened species out of its habitat into a zoo, botanical garden, seed bank or cryo-store where it can be given special care
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stem against all four stored options: the stem defines ex situ conservation, option 2 reads 'in-situ conservation', which is the opposite arrangement, and option 3, which the key names, reads 'Biodiversity conservation'. With the keyed option's own text not matching what the stem describes, this record cannot show what pulls a student anywhere.
- **Why:** This question requires the name given to one type of conservation, demonstrated by the stem defining it in full, species 'taken out from their natural habitat and placed in special setting where they can be protected and given special care'.
- **Note:** The stored option set does not support the printed key. The stem defines ex situ conservation, no stored option names it, and the answer line reads 'Answer (4)' style as 'Answer (3)' against option 3 'Biodiversity conservation'. The subtopic field already reads 'Ex Situ Conservation', so option 3's text has most likely lost its printed wording in extraction. Tagged as printed and the key is not re-judged; sent for repair, and no trap is written on an option set this damaged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Actinomorphic flowers can be cut into equal radial halves on any plane; the papilionaceous legumes listed in the same paragraph are zygomorphic
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Cassia is printed as an example in the same symmetry paragraph as Datura, a couple of lines down on the zygomorphic side, so a student who stored the paragraph's genus names without their side answers with a printed example that belongs to the other symmetry.
- **Why:** This question requires membership of a printed example list for one symmetry type, demonstrated by the stem asking for 'an example of actinomorphic flower' while the options are four bare genus names with no floral description supplied to judge.
- **Note:** Applied the swap test: 'Cassia' and 'Datura' resemble each other in no way, and the pull survives because both are example genera printed in the same paragraph, so position is doing the work and the label is nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Totipotency is a single plant cell's capacity to regenerate the whole plant; micropropagation is the technique built on it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Micropropagation is the sentence printed beside totipotency in the tissue-culture section and it is the one that actually turns out whole plants in thousands, so a student who remembers 'whole plants from single cells' reaches for the technique instead of the capacity.
- **Why:** This question requires the term a printed definition sentence names, demonstrated by the stem reproducing that definition, 'the capacity to generate a whole plant from any cell of the plant'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mendel's Law of Dominance: characters are controlled by discrete factors, the factors occur in pairs, one of a dissimilar pair dominates the other, and so a monohybrid cross shows only one parental character
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The second clause of B is true -- both parental characters do reappear in the F2 of a monohybrid cross -- and that true half vouches for the opening clause 'Alleles do not show any expression', so the student accepts B and takes the all-five option.
- **Why:** This question requires the propositions the book assigns to the Law of Dominance to be told apart from a statement that denies dominance, demonstrated by item B's 'Alleles do not show any expression' appearing in every wrong option.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Spindle fibres take hold of the kinetochores at metaphase, once the chromosomes are lined up at the equator; prophase only builds the spindle
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The assembly of the mitotic spindle is printed under prophase, so a student who learnt each stage by its headline event puts the attachment there as well. Assembly and attachment are separate events: the fibres reach the kinetochores only after the chromosomes line up at the equator, which is metaphase.
- **Why:** This question requires the mitotic stage NCERT ties to kinetochore attachment, demonstrated by the stem "Spindle fibers attach to kinetochores of chromosomes during" with four options that are only the four stages and no criterion printed to work from.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A competitive inhibitor resembles the substrate and occupies the active site - malonate standing in for succinate at succinic dehydrogenase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Feedback inhibition is the other inhibition type that comes with a name and a diagram, so a student who has kept the malonate-succinic dehydrogenase pairing but not the reason for it answers with the inhibition they can name. Malonate works by resembling succinate closely enough to sit in the active site, which is competition, not an end product shutting down its own pathway.
- **Why:** This question requires the inhibition type that the printed malonate-succinic dehydrogenase pair is the standard example of, demonstrated by the stem calling it "a classical example of:", which points at the textbook example rather than at any structure or data the stem supplies.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A restriction endonuclease recognises one specific palindromic stretch of DNA; Hind II's recognition sequence is six base pairs long
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The four options are bare base-pair counts spaced around the printed six, and no line in the chapter attaches 10, 8 or 4 to Hind II or to recognition sequences in general, so nothing but the stored number six leads anywhere.
- **Why:** This question requires the stored length of Hind II's recognition sequence, demonstrated by the stem "recognition sequence and it consists of:" followed by four bare base-pair counts with no sequence given to count.
- **Note:** The pattern classifier returned `arrange_in_order`; the printed shape has nothing to sequence - one question and four bare base-pair values - so the shape recorded here is mcq.
<!--/ecat-->

## Q125

Biology · botany · Biotechnology and Its Applications

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Bt protoxin crystals are solubilised into active toxin by the alkaline pH of the insect gut, and the cry gene carried decides which insect group is affected
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A gut that activates a swallowed protein reads as an acid gut, so a student carrying stomach acid over from the digestion chapter lets 'due to acidic pH' pass and takes Statement II for the NCERT sentence it otherwise is.
- **Why:** This question requires the cause NCERT gives for protoxin activation, demonstrated by Statement II's 'the inactive protoxin gets converted into active form due to acidic pH of the insect gut'. The trap is reversed because the printed condition sits at the opposite end of the pH scale from the alkaline gut the text names; nearby_fact is ruled out since 'acidic' is not printed beside it, and condition_missed is ruled out because no rule is applied here - the condition itself is misstated.
- **Note:** Statement I prints the gene as 'cry IAc' with a space inside the name; tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each organelle's own job: the nucleolus makes rRNA, the centriole is the cartwheel of nine triplets, leucoplasts store food, and the Golgi builds glycolipids and glycoproteins
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  The Golgi's taught job is packaging and holding material for delivery, so 'For storing nutrients' reads as a description of it, and with the cartwheel pair kept, option 1 is the only code carrying both.
- **Why:** This question requires the function NCERT attaches to each named organelle, demonstrated by List II being four printed descriptions, 'Site for active ribosomal RNA synthesis' and 'Organization like the cartwheel' among them. Both name tests fail for the trap - Golgi and leucoplast neither resemble each other nor stand beside each other in the chapter, one being in the endomembrane section and the other under plastids - so what is offered is a real storage function placed at the wrong organelle, which is wrong_site_attacked.
- **Note:** wrong_site_attacked is used here for a function moved to the wrong organelle rather than the wrong position in a molecule; §5.2's wrong_site_or_stage ('moves a biological event to the wrong place') is its retired form and names the same device.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Incomplete dominance: the heterozygote itself is pink, so a pink (Rr) x red (RR) cross gives half red and half pink, and white needs two recessive alleles
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Red, pink and white is the phenotype set of the snapdragon cross the textbook prints - the F1 selfing, Rr x Rr, with its 1:2:1 - so a student who recognises "Snapdragon" and recalls that result reports it without working this cross. Here one parent is red RR, so no gamete can supply a second recessive allele and white cannot appear.
- **Why:** This question requires incomplete dominance applied to a cross the book does not print, demonstrated by the stem crossing "A pink flowered Snapdragon plant ... with a red flowered Snapdragon plant", which forces the student to read pink as Rr and work the gametes out rather than recall a result.
- **Note:** half_right was considered for option 1, since it is a three-part set with one part (white) failing, but the pull is not a part-wise slip: the whole set is the correct answer to the printed F1 x F1 cross, which is answers_other_question.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The IUCN Red List is the inventory that catalogues threatened and endangered species
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  WWF is the conservation body whose whole public identity is threatened animals, so a student sorting four acronyms by "which one is about saving species" stops there. The catalogue of endangered species is the IUCN Red List; IUCN is the body that compiles and releases it, while WWF funds and campaigns.
- **Why:** This question requires the body named as the source of the endangered-species list, demonstrated by the stem "List of endangered species was released by" with four organisation acronyms as the options.
- **Note:** Option 4 is stored as "FOAM", which matches no organisation; it is tagged as printed and recorded as filler, with no inference drawn about whether the printing is damaged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Why the tropics hold the most species: long undisturbed evolutionary time, constant and predictable -- that is, less seasonal -- environments that allow niche specialisation, and more solar energy
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The printed explanation says tropical environments are less seasonal and more constant, and a student who has stored that seasonality is the factor without storing which way it runs reads B as that line and keeps A and D beside it.
- **Why:** This question requires the reasons the chapter gives for tropical species richness, demonstrated by the stem 'Tropical regions show greatest level of species richness because' above items B and E, which state opposite things about seasonality.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fungi are classified on mycelium morphology, mode of spore formation and fruiting body; mode of nutrition separates nothing because the whole kingdom is heterotrophic
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Fruiting body is on the printed list of criteria, so it is true of the question "which IS a criterion" and not of the one asked. A student whose recall of the three-item list keeps only mycelium morphology and spore formation treats the third item as the intruder and ticks it, while the item actually missing from the list is mode of nutrition.
- **Why:** This question requires the three printed criteria for classifying fungi, demonstrated by the stem "Which one of the following is not a criterion for classification of fungi?" with "Fruiting body", "Morphology of mycelium" and "Mode of spore formation" being exactly the items of that printed list.
- **Note:** task polarity is negative ("not"), which is what makes the three true criteria reachable; the dropped-negation route touches options 1, 2 and 4, and option 1 carries the trap because it also has the short-list route.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** In a dicot seed the embryonal axis has two ends: the radicle below the cotyledons becomes the root, the plumule above them becomes the shoot
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the options are bare letters and the figure was not supplied to this step
- **Why:** This question requires reading a labelled seed figure and naming the part that becomes the root, demonstrated by the stem 'Identify the part of the seed from the given figure which is destined to form root when the seed germinates' with options that are the bare labels 'D', 'A', 'B', 'C'.
- **Note:** Trap recorded as no_trap under codebook section 5.0, the figure-gated case, and this is our reading limit rather than a finding that nothing pulls. The four options are bare figure labels and the figure is held in the record only as an image reference (figures_agent/2024_S1/q131.png); this step reads the record, so which part each of A, B and D marks cannot be established and no option can be named, which rule 0.4 requires before a trap is tagged. The source is not damaged -- the png carries a path, a CDN url and a sha256 -- so this is not source_incomplete and not source_damage_artifact. For whoever has the printed figure: the route to check is the other end of the embryonal axis, since NCERT prints the plumule immediately beside the radicle in the same seed diagram and the same sentence, which would make it nearby_fact on whichever letter marks the plumule.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The lac operon's y gene makes permease, which carries lactose across the bacterial membrane; beta-galactosidase only splits lactose once it is already inside
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Beta-galactosidase is the enzyme filed under the word 'lactose', so it is reached before the stem's verb 'transported' is weighed; it hydrolyses lactose inside the cell and carries nothing across the membrane.
- **Why:** This question requires the one NCERT line on what each lac operon gene product does, demonstrated by 'transported to the cell by the action of' set against four enzyme names drawn from that same operon.
- **Note:** Trap is nearby_fact, not look_alike_term: swap 'beta-galactosidase' and 'permease' for two unlike words and the trap survives, because what carries the student is that NCERT prints the two products side by side in one sentence, not any resemblance between the names. Not answers_other_question either: the option is a bare name rather than a true claim, and a lone wrong name belongs to the nearby_fact / look_alike_term pair.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Auxin weedicides such as 2,4-D kill broad-leaved dicot weeds but leave mature monocots like lawn grass unaffected
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Apical dominance is the auxin effect printed in the same NCERT list as the weedicide use, so a scan for a true auxin statement stops there; it is true, and it says nothing about why grass survives the spray.
- **Why:** This question requires the reason NCERT gives for grass surviving an auxin weedicide, demonstrated by the stem's connective in 'no damage is caused to grass as auxin' and by option 4's 'does not affect mature monocotyledonous plants.'
- **Note:** answers_other_question over nearby_fact: the option is not a wrong fact at all -- auxin does promote apical dominance -- it is a right fact answering 'what does auxin do' when the stem asked 'why is grass unharmed'. qtype stays mcq on E1's reading: long statements as options do not make a question statements, and the stem carries its own content plus a trailing connective rather than being a bare instruction. negative_words_seen records 'NOT', but it sits in the premise 'no damage is caused' and in option 4's 'does not affect', not in the task.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A guard cell has a thin outer wall and a thickened inner wall, so turgor bows it outward and opens the stoma
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the options are bare letters and the figure was not supplied to this step
- **Why:** This question requires reading a stomatal figure and matching a wall-thickening description to one labelled cell, demonstrated by 'In the given figure, which component has thin outer walls and highly thickened inner walls?' with options that are the bare labels 'B', 'C', 'D', 'A'.
- **Note:** Trap recorded as no_trap under codebook section 5.0, the figure-gated case, for the same reason as q131: the options are bare figure labels, the figure is held only as an image reference (figures_agent/2024_S1/q134.png), and this step reads the record, so no option can be named and rule 0.4 is not satisfiable. The png carries a path, a CDN url and a sha256, so the source is intact -- this is not source_incomplete. For whoever has the printed figure: the route to check is whichever letter marks the ordinary epidermal or subsidiary cell, which NCERT prints flanking the guard cell in the stomatal apparatus diagram.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Genetics vocabulary read strictly: allele and ploidy, and test cross against back cross, where the genotype of the partner is what separates them
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No wrong option shares even one pair with the key, so the confusion the lists invite - the back cross against the test cross - has no code to land on, and any single one of the four definitions held securely selects option 4 on its own.
- **Why:** This question requires the term each printed definition names, demonstrated by List I's 'Cross of $\mathrm{F_1}$ progeny with homozygous recessive parent' standing against List II's 'Test cross' and 'Back cross'. The verdict is no_trap because the key code A-III, B-IV, C-I, D-II shares no pair with any wrong option, so the nested test-cross/back-cross wording is never put in play by a printed code.
- **Note:** no_trap here is a property of the option set, not of the lists: a code swapping only B and C would have been a real trap and is not offered.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Floral and fruit characters of the stock examples: rose is perigynous, pea has marginal placentation, cotton has twisted aestivation, mango is a drupe
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Reading List I's 'Rose' as the China rose of NCERT's twisted-aestivation example list puts twisted aestivation on row A, and option 3 is the only code carrying A-I, so one misread name settles the whole pairing.
- **Why:** This question requires the morphological character NCERT prints for each named plant, demonstrated by List II being 'Twisted aestivation', 'Perigynous flower', 'Drupe', 'Marginal placentation' set against four plant names. Applied the likeness test on the trap: replace 'Rose' with 'Plum', NCERT's other perigynous example, and nothing pulls twisted aestivation onto row A any more, so the resemblance between Rose and China rose is doing the work and the label is look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Photorespiration needs RuBisCO together with O2, so in a C4 leaf only the bundle sheath could photorespire and the CO2 built up around it keeps that very low, while the mesophyll has PEP carboxylase and no RuBisCO at all
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  'C4 plants show very little photorespiration' is the line carried from the chapter, and Statement II prints that line with cell types attached, so checking the familiar phrase and not which cell owns it leaves both statements looking true.
- **Why:** This question requires which cells of a C4 leaf can photorespire, demonstrated by Statement II's 'mesophyll cells show very little photorespiration while bundle sheath cells do not show photorespiration'. The trap is wrong_site_attacked because the event is moved onto the cells that lack RuBisCO; reversed is ruled out since nothing here is an order or a direction - two sites have had their attributes exchanged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Wind-pollinated flowers advertise nothing: they hang out well-exposed stamens and feathery stigmas so that moving air does the carrying
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Water pollination is the paragraph NCERT prints next to wind pollination, and its flowers also push their stamens out, so a student who has ruled out selfing picks the neighbouring agent; the mucilaginous covering NCERT describes belongs to the pollen grains of submerged flowers, not to stamens.
- **Why:** This question requires judging four whole descriptions against a figure, demonstrated by the stem 'Identify the correct description about the given figure:' and by option 2's 'Wind pollinated plant inflorescence showing flowers with well exposed stamens.'
- **Note:** qtype statements on E1's own non-null reading, statement_options (15 full-statement options): no statement block is printed, the stem is a bare instruction and each option is a full description to be judged, which is the case rule 1 admits alongside 'which one of the following statements is correct'. The figure itself is not readable in this step, so the one fact about it used here is the one the printed key certifies -- option 2's 'well exposed stamens' is the accepted description -- and the routes rest on that plus the printed option wording, not on any guess at what the picture shows.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Phaeophyceae diagnostics: chlorophyll a and c with carotenoids and xanthophylls, food stored as mannitol or laminarin, algin coating a cellulosic wall, and sexual reproduction that may be isogamous, anisogamous or oogamous
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Oogamy is the sexual reproduction taught for brown algae, so 'Sexual reproduction is by oogamous method only' reads as the remembered line and the word 'only' goes unweighed. Four statements are then wanted, and the one dropped is A, because 'biflagellate' is the word attached to Chlamydomonas and the green algae.
- **Why:** This question requires the features NCERT states for one algal class, demonstrated by four of the five statements being its printed lines and the fifth reading 'Sexual reproduction is by oogamous method only'; half_right is the label because what fails in B is the exclusivity and not the oogamy, so each wrong set is a four-part answer with one part broken.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Three TCA steps are dehydrogenations that reduce NAD+ or FAD; succinyl-CoA to succinate is the substrate-level phosphorylation that makes GTP while oxidising nothing
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The printed arrow from succinic acid to malic acid spans two reactions, and the second of them, fumarate plus water to malate, oxidises nothing -- so the true 'no oxidation here' verdict is reached one stage late and pinned on the whole arrow, whose first half is the cycle's FADH$_2$ step.
- **Why:** This question requires applying the test for substrate oxidation to four printed conversions of the cycle, demonstrated by the task 'which does not involve oxidation of substrate' set against 'Succinyl-CoA $\rightarrow$ Succinic acid'.
- **Note:** E1_question_type is null -- the four options are printed conversions and no pattern covered that shape. It is carried as mcq rather than new_type, because one question with four answers is what mcq means on this axis and the collapse of the retired reaction_options into it loses nothing; recorded here so the collapse stays visible. half_right was considered for option 3 and ruled out: the option is printed as a single arrow, not as two claims, and rule 2 keeps half_right to options with two or more printed parts. wrong_site_attacked carries it exactly -- a real non-oxidative reaction located at the wrong stage of the cycle. asks is apply_rule rather than fact_line because no single NCERT line settles it: the criterion in 'oxidation of substrate' has to be run over all four conversions.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Who contributed what to biodiversity: Humboldt's species-area relationship, May's estimate of about 7 million species, Ehrlich's rivet popper hypothesis, Tilman's long-term outdoor plots
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Tilman's plots are taught as the result that more species means more productivity and more stability, so the species-richness phrasing pulls his name onto 'Species-Area relationship', and with May's 7 million kept, option 1 is the only code carrying D-I.
- **Why:** This question requires which contribution NCERT attributes to each named ecologist, demonstrated by List II carrying 'Global species diversity at about 7 million' and 'Rivet popper hypothesis' against four personal names. Applied the likeness test on the trap: the four names resemble each other in no way and the swap survives replacing them with unlike words, because what carries it is the four attributions sitting in one printed section, so nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Who is credited with what in molecular genetics: Griffith with transformation, Jacob and Monod with the lac operon, Khorana with the genetic code, Meselson and Stahl with semi-conservative replication
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Options 2 and 3 both read A-III and C-I, so Griffith and Khorana settle nothing and the whole code comes down to which duo owns the lac operon; a student who holds Jacob & Monod and Meselson & Stahl together as the two duos who worked on E. coli takes the crossed arrangement.
- **Why:** This question requires the attribution NCERT prints for each named worker, demonstrated by List II holding 'Transformation' and 'Lac operon' as bare findings with no criterion printed that would let them be worked out.
- **Note:** look_alike_term and nearby_fact were both ruled out on the crossed pair: 'Jacob & Monod' and 'Meselson & Stahl' carry no resemblance to each other, and their findings are not printed side by side, so what is left is the multi-part pairing device the retired vocabulary called wrong_pairing, whose §5.1 family is half_right.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Somatic hybridisation fuses two naked protoplasts — cells whose walls have been digested off — so a hybrid plant is raised without a pollen cross
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Somatic embryos sit in the same tissue-culture passage as protoplast fusion and the stem's own word 'somatic' reappears in the option, so a student holding that passage as a run of 'somatic' techniques stops at the matching phrase. An embryo is a product of culture, not a body that can be fused.
- **Why:** This question requires the stated fact of which body is fused in somatic hybridisation, demonstrated by the stem naming the technique — 'fused in somatic hybridization involving two varieties of plants' — with four coordinate tissue-culture terms as options and no criterion printed to apply.
- **Note:** Likeness test applied: 'somatic embryos' and 'protoplasts' do not resemble each other, so resemblance between the right and wrong name is not the pull; replace the option with another term from the same passage (callus) and the pull survives, so position in the NCERT passage carries the student. Hence nearby_fact, not look_alike_term. The stem's word 'somatic' reappearing in the option is recorded under 'feels'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plastids and mitochondria carry their own naked circular double-stranded genome, of the prokaryotic type, unlike the linear nuclear chromosomes around them
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  'Double stranded' is the half a student holds securely, and the nuclear chromosome's description carries 'linear' along with it. The plastid genome is a closed circle, which is why it is read as a prokaryotic-type genome.
- **Why:** This question requires the stated description of the plastid genome, demonstrated by the stem asking only what 'The DNA present in chloroplast is' and the four options differing solely in shape and strandedness.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stamen cohesion: the prefix counts how many bundles the filaments are fused into, and NCERT fixes one example plant per type
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  A student counting stamens rather than bundles sees Citrus's crowded tuft and gives it the two-bundle name, pushing pea onto the many-bundle name; the two names differ only by prefix, so the swap costs nothing in memory and lands on the one option that keeps china-rose and lily in place.
- **Why:** This question requires the example NCERT prints for each named stamen type, demonstrated by List II being four plant names — 'Citrus', 'Pea', 'Lily', 'China-rose' — that no stated criterion connects to a cohesion type. Swapping 'diadelphous' and 'polyadelphous' for two unlike words kills the pull, so likeness and not position is carrying it.
- **Note:** The column headings arrived folded into stem_en as 'List I (Types of Stamens) | List II (Example)'; the printed shape is still two columns answered by a pairing code.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA polymerase can add a nucleotide only to a free 3'-OH, so every new strand grows 5' to 3' — the single polarity that forces the lagging strand to be made in pieces
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The clause 'catalyses polymerization in one direction, that is $5' \rightarrow 3'$' is true as printed, so a student who screens the options on the direction and not on the enzyme ticks it. The sentence belongs to the transcription enzyme, and the stem asked about replication.
- **Why:** This question requires the stated fact of the direction in which DNA-dependent DNA polymerase works, demonstrated by the stem 'Which of the following statement is correct regarding the process of replication in E.coli?' with four rival full statements differing only in the enzyme named and the direction given.
- **Note:** E1_question_type is null and its reason reads 'options are reactions'; the printed options are four rival statements about replication, not reactions, so the shape recorded here is `statements`, on the stem's 'which of the following statement is correct'.
<!--/ecat-->

## Q147

Biology · botany · Ecosystem

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The ten per cent law: each trophic level passes on about a tenth of the energy it received from the one below
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Taking a tenth at each of the two steps from the first level to the third — $100x \to 10x \to x$ — lands on $x$, one factor of $\frac{1}{10}$ past where the printed key stops.
- **Why:** This question requires a number computed from the stem's own figure by the ten per cent law, demonstrated by the stem supplying 'the Net Primary Productivity (NPP) of first trophic level is $100x$' and asking for a productivity two levels above it.
- **Note:** Key doubt recorded, not acted on. The ten per cent law applied across both level changes gives $100x \to 10x \to x$, which is option 3, while the answer line as printed reads 'Answer (4)', $10x$ — the figure one step up, i.e. the second trophic level's share. Tagged to the printed key per §7, with verdict `arguable_key`. A second looseness feeds the gap: GPP is a producer term, and the stem applies it to the third trophic level where secondary productivity is the standard term, so there is no printed convention fixing whether the $100x$ is the start of the chain or already one transfer into it.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Proteins are filed by the job they do — hormone, enzyme, structural ground substance, membrane glucose transporter
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Insulin is the molecule tied to glucose entering cells, so 'Enables glucose transport into cells' reads as insulin's line; it is true of what insulin brings about, but it is the entry the protein table prints against GLUT-4, and B-IV appears in option 1 alone.
- **Why:** This question requires the function NCERT's protein table prints for each named protein, demonstrated by List II mixing three categories with one function line, 'Enables glucose transport into cells', and printing no criterion for sorting them.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each stage of respiration has its own compartment: glycolysis in the cytoplasm, the citric acid cycle in the matrix, the electron transport system on the inner membrane, protons piled up in the intermembrane space
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked every wrong option against the two sites the chapter states outright: all three move glycolysis inside the mitochondrion and the citric acid cycle out of the matrix. 'Glycolysis — Cytoplasm' and 'Citric acid cycle — Mitochondrial matrix' appear only in the key, so either one of those printed facts strikes out all three at once, and no option keeps a securely held site for a route to rest on.
- **Why:** This question requires the compartment NCERT assigns to each stage of respiration, demonstrated by List II being four locations — 'Cytoplasm', 'Mitochondrial matrix', 'Intermembrane space of mitochondria', 'Inner mitochondrial membrane' — that each stage simply sits in.
- **Note:** Three fillers is the finding here, not a gap: one printed site, glycolysis in the cytoplasm, survives in a single option, so each wrong option needs two stated compartments abandoned together.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gibberellin stretches internodes, so spraying sugarcane lengthens the cane that stores the sugar and the yield rises with it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Auxin is the regulator the same section ties to cell elongation, so a student holding 'elongation is auxin' reads the stem's 'increases the length of stem' straight onto it. The sugarcane spray NCERT names is gibberellin.
- **Why:** This question requires the stated fact of which regulator the sugarcane example uses, demonstrated by the stem reproducing that line almost word for word — 'increases the length of stem, thus, increasing the yield' — with four coordinate regulators as options.
- **Note:** Likeness test applied: 'auxin' and 'gibberellin' do not resemble each other, so resemblance is not the pull. The pull survives for any regulator whose printed role is elongation, because what carries the student is the elongation role sitting beside gibberellin's in the same section. Hence nearby_fact, not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the alveoli — high $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, fewer $\mathrm{H^+}$ and a lower temperature — haemoglobin binds oxygen; all four reverse in the tissues, where it releases it
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  'High $\mathrm{pO_2}$' is the alveolar factor the text lists first and it is printed here as the option's own first clause, so the option opens as the answer. The second clause reverses it, because alveolar $\mathrm{pCO_2}$ is the low one, 40 mm Hg, and high $\mathrm{pCO_2}$ is a tissue-side condition.
- **Why:** This question requires the stated set of alveolar factors, demonstrated by the stem reproducing that sentence — 'factors are favourable for the formation of oxyhaemoglobin in alveoli' — and each option pairing two of the four named factors.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The cell cycle runs Gap 1, then Synthesis, then Gap 2, and M phase closes it with karyokinesis before cytokinesis
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The two orderings a single remembered mistake produces are E-C-A-B-D, from putting cytokinesis before karyokinesis, and E-A-C-D-B, from putting Gap 2 before Synthesis; neither is printed, and each wrong option instead breaks the sequence in two or three places at once.
- **Why:** This question requires the fixed order of the cell cycle stages, demonstrated by the options being orderings of 'Gap 1 phase', 'Synthesis phase', 'Gap 2 phase', 'Karyokinesis' and 'Cytokinesis'; no_trap follows because the two orderings a single remembered mistake yields, E-C-A-B-D and E-A-C-D-B, are not among the four printed strings.
- **Note:** E1 called this arrange_in_order, a retired value with no ordering shape in the current qtype list; the printed shape is a lettered A-to-E block, which rule 1 puts under statements, and the ordering demand is carried by asks: order.
<!--/ecat-->

## Q153

Biology · zoology · Structural Organisation in Animals

In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on

- (1) $11^{\mathrm{th}}$ segment
- (2) $5^{\mathrm{th}}$ segment
- **(3)** $10^{\mathrm{th}}$ segment
- (4) $8^{\mathrm{th}}$ and $9^{\mathrm{th}}$ segment

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solution** — answer (3)

> *The latest NCERT Biology edition does not cover which segment of the cockroach bears the anal cerci.*

Nothing in the current book to quote. The question's own clue is the paired filamentous anal cerci of both sexes: they sit on the tenth segment, so option 3.

*Figure on the card: a diagram drawn for this solution. Count back from the thorax: the abdomen ends at segment 10, and the pair of anal cerci hangs off that last segment.*

<details><summary>the full reason, and why each other option fails</summary>

The question itself hands you the structure: a pair of jointed filamentous structures called anal cerci, present in both sexes. They are carried on the tenth segment, so option 3 is correct. This is a plain position fact about the hind end of the cockroach, where the last segment of the abdomen bears the cerci in male and female alike, which is why the question stresses "in both sexes". The latest NCERT Biology edition carries no line saying which segment bears the anal cerci, so there is nothing in the current book to quote back here. Learn it as a single pairing: anal cerci, both sexes, tenth segment.

- **(1)** The cerci are already the terminal pair of structures, carried on the tenth segment at the hind end of the adult abdomen, so counting on to an eleventh segment goes past where they sit.
- **(2)** The fifth segment lies in the middle of the abdomen and carries no such pair; the cerci are a hind-end feature, which is how the question describes them for both sexes.
- **(4)** The cerci are one pair on one segment, not a pair spread over the eighth and ninth; the question asks for the single segment that bears them.

</details>



**NCERT:** Structural Organisation in Animals (Class XI, Chapter 7) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 58)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q153_1d9c3abe_03112026.png?v=1d9c3abe58af)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q153_a2c68234_03112026.png?v=a2c682342110)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which abdominal segment carries which appendage in the cockroach: anal cerci on the 10th in both sexes, anal styles on the 9th in the male only
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The 9th segment is where the other pair of abdominal appendages, the anal styles, sits, so a recalled segment number with no structure attached to it lands on the one option carrying a 9; the styles are present in males only, and the stem's "In both sexes" is exactly what moves the answer to the 10th.
- **Why:** This question requires the stored fact of which abdominal segment bears the anal cerci, demonstrated by the stem "In both sexes of cockroach, a pair of jointed filamentous structures called anal cerci are present on" followed by four bare segment numbers, with no criterion printed that could be applied instead.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each animal phylum is identified by its own diagnostic structure or example genus — the ctenophore Pleurobrachia, the molluscan radula, the hemichordate stomochord, the bony fish's air bladder
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Pleurobrachia and the air bladder are the two pairs the chapter makes easy and option 4 keeps both, so the code turns on radula against stomochord; 'stomochord' reads as a mouth structure, and the famous mouth structure in the list belongs to Mollusca, so the two get crossed.
- **Why:** This question requires the phylum NCERT attaches to each named structure or genus, demonstrated by List I mixing a genus with three body structures — 'Radula', 'Stomochord', 'Air bladder' — that only the printed diagnostic lines connect to a phylum.
- **Note:** Applied the swap test to the crossed pair: 'radula' and 'stomochord' carry no resemblance to each other and the two phyla are not printed side by side, so look_alike_term and nearby_fact both fail and the device is the multi-part pairing failure, half_right — the same reading as q142.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each human disease is caused by a particular class of pathogen — typhoid by a bacterium, leishmaniasis by a protozoan, ringworm by a fungus, filariasis by a nematode
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Ringworm' carries 'worm' in its name, so the Nematode entry reads as its agent; the disease is fungal, and C-II is printed in option 2 alone, which is what carries the student to the whole code.
- **Why:** This question requires the class of pathogen NCERT names for each disease, demonstrated by List II being four agent groups — 'Fungus', 'Nematode', 'Protozoa', 'Bacteria' — with no feature of any disease printed to deduce the agent from. Replacing 'Ringworm' with 'tinea' kills the pull to Nematode, so the likeness inside the name is doing the work rather than the entry's position in the list.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which plant each drug of abuse is obtained from, plus morphine's use as a post-surgical sedative
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  List II prints the bare genus 'Erythroxylum' without the species word that names cocaine, so the one self-announcing plant left is the poppy and it goes to cocaine while the unfamiliar genus goes to heroin.
- **Why:** This question requires the pairing NCERT prints between each drug of abuse and its source plant, demonstrated by List II holding three plant names — 'Erythroxylum', 'Papaver somniferum', 'Cannabis sativa' — and one clinical line, 'Effective sedative in surgery', with no criterion printed to work any of them out from.
- **Note:** Swap test applied: the two plant names resemble each other not at all, and the wrong one is reachable because NCERT prints it two lines from the right one, so nearby_fact rather than look_alike_term.
<!--/ecat-->

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

**Solution** — answer (4)

> ⚠ **Marked for review.** NCERT supports option 4, but the booklet prints (3). The printed answer is option 3, but NCERT contradicts its third pair: 'As the name suggests, Cardiac muscles are the muscles of heart' and 'Based on appearance, cardiac muscles are striated' (BIO11L-CH17-P10), so 'Smooth - Heart' cannot be right. Option 4 matches all three diagrams to NCERT, which is also what the independent solve gave, so answer_is is written as 4. The publisher's working supports option 3 only by describing figure (c) as cardiac muscle of the heart, which is the opposite of what option 3 states.

> *As the name suggests, Cardiac muscles are the muscles of heart.*
>
> — `BIO11L-CH17-P10`

Heart muscle is cardiac muscle, not smooth muscle. So option 3's third pair is wrong and the printed key fails; option 4 is the match NCERT supports.

*Figure on the card: the printed diagram, with the deciding parts marked. Read each panel for two things only: are the cells striated, and are they branched.*

<details><summary>the full reason, and why each other option fails</summary>

Read the three diagrams against NCERT's three types of muscles: skeletal, visceral and cardiac. Diagram (a) shows striated cells lying side by side, unbranched. These are skeletal muscles, which are attached to skeletal elements, so biceps or triceps fits. Diagram (b) shows cells that do not exhibit any striation and are smooth in appearance. These are the visceral or smooth muscles of the inner walls of hollow visceral organs like the alimentary canal, and they are involuntary, so intestine or stomach fits. Diagram (c) shows striated cells assembled in a branching pattern. These are cardiac muscles, the muscles of heart. Only one option names all three correctly: skeletal-biceps, involuntary-intestine, cardiac-heart.

- **(1)** It calls (a) involuntary. Diagram (a) is striated and unbranched, which NCERT describes as skeletal muscle, and skeletal muscles are voluntary in nature. NCERT also locates skeletal muscle at skeletal elements, not at the nose tip.
- **(2)** It calls (a) smooth. Smooth muscle is the one that does not exhibit any striation, which is diagram (b), not (a). Diagram (a) is striated, so it is skeletal; the toes carry skeletal elements, which is where skeletal muscles attach. Pairs (b) and (c) here are also shifted onto the wrong diagrams.
- **(3)** Its first two pairs are right, but it calls the heart muscle smooth. NCERT says the muscles of heart are the cardiac muscles, and that based on appearance, cardiac muscles are striated, whereas smooth muscle is the nonstriated visceral type. Diagram (c) is striated and branched, so it cannot be smooth muscle.

</details>



**NCERT:** Locomotion and Movement (Class XI, Chapter 17) · 17.2 Muscle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 60)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/crops/q157_51697d5f_03112026.png?v=51697d5f38c2)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2024/2024_S1/solutions/q157_9305265d_03112026.png?v=9305265d05f4)

---

<!--ecat-->
#### Categories

- **Type:** **New type (proposed)** (`new_type`) — a printed shape none of the above describes
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The three muscle types and where each is found in the body: skeletal on the skeleton, smooth in the walls of hollow visceral organs, cardiac in the heart
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stored option cells against the printed key: option 3 is keyed correct yet its third cell reads "Smooth – Heart", while option 4 reads "Cardiac – Heart" and holds in all three cells. The item's own table reached this record only as a figure capture, so the cell text is not confirmed and no route can be read off cells that may not be what the paper printed.
- **Why:** This question requires three muscle-type-to-location assignments to hold at once in a single option, demonstrated by option 3 reading "(a) Skeletal - Triceps (b) Smooth – Stomach (c) Smooth – Heart", where one wrong cell sinks the whole option.
- **Note:** Withheld as source damage, not tagged for a trap. The record's option 3 is the printed key yet its third cell reads "Smooth – Heart", while option 4 reads "(a) Skeletal - Biceps (b) Involuntary – Intestine (c) Cardiac – Heart" and is consistent in all three cells; the two cannot both be as the paper printed them. The stem says "Three types of muscles are given as a, b and c" and the record carries a figure whose `shows` is "question", i.e. the item's own table was captured as an image, so the cell text stored in `options_en` is not confirmed against the printed paper. Per §5a this is `source_damage_artifact` and needs a repair task re-reading the table from the figure; the tag follows the printed key and I am not re-judging it (§7). qtype, asks and concept are recorded because the shape and the demand are legible even with one cell in doubt.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What each part of the brain does: pons connects, medulla holds the respiratory and gastric centres, hypothalamus holds neurosecretory cells, cerebellum governs posture and balance
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Respiratory control is moved one structure along the brain stem, from the medulla to the pons, which then forces the medulla to take the pons's own job of connecting brain regions.
- **Why:** This question requires the function NCERT states for each named brain part, demonstrated by List II quoting those lines directly — 'Controls respiration and gastric secretions' and 'Provides additional space for Neurons, regulates posture and balance'.
- **Note:** All three wrong codes give the cerebellum 'Neuro secretory cells', so the cerebellum's posture-and-balance line alone decides the question; wrong_site_attacked was preferred to nearby_fact because the function in the trap row is real and has been moved to the adjacent structure, which is the site test in §5.1.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each cry gene is named for the one pest it kills, and each therapeutic protein for the one disorder it corrects
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Cry IAb' and 'Cry IAc' differ by one final letter, and a student holding them the other way round — IAb for the bollworm, IAc for the corn borer — finds both of those rows together only in option 2.
- **Why:** This question requires the pest or disorder NCERT ties to each named gene and therapy, demonstrated by List I printing 'Cry IAb' and 'Cry IAc' as separate entries against 'Cotton bollworm' and 'Corn borer' in List II.
- **Note:** Both §5.1 tests were applied to the gene rows: NCERT does print the two targets in one sentence, which is the position route, but replacing 'Cry IAb' and 'Cry IAc' with two unlike names kills the pull, so the likeness wins and the label is look_alike_term. The brief's nearby_fact example covers the other configuration, where a bollworm gene is offered against a corn-borer question.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The hominid line runs Homo habilis, then Homo erectus, then Homo neanderthalensis, then Homo sapiens
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The name 'erectus' carries the upright-posture milestone, so a student dating the line by milestones rather than by the fossil dates puts Homo erectus ahead of Homo habilis. The rest of the string, Homo neanderthalensis then Homo sapiens, is kept, so only the first adjacency fails.
- **Why:** This question requires the printed past-to-recent order of four Homo species, demonstrated by the stem's '(Past to Recent)' and by option 2 'D-A-C-B' transposing Homo habilis and Homo erectus and nothing else; reversed is excluded by the rulebook's own 'not one swapped pair inside a longer order', so a partly-correct ordering is half_right.
- **Note:** E1 called this arrange_in_order, a retired value; the printed lettered block puts it under qtype statements with asks: order.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The parts of the oviduct in order — infundibulum, ampulla, isthmus — against the parts of the uterus it opens into
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Infundibulum, ampulla and isthmus are the three parts of the oviduct named in one run of sentences, so the single recalled line that places one of them in the tube places all three; the key is the only option that carries another organ's name inside it, and no wrong option offers a route of its own.
- **Why:** This question requires the stored membership of the oviduct's parts, demonstrated by the stem "Which of the following is not a component of Fallopian tube?" with three of the four options being the three parts the oviduct is described as having.
- **Note:** "Uterine fundus" is standard anatomy but is not a term used in the female-tract paragraph that supplies the other three options, which is what makes it the identifiable outsider here rather than a fourth tube part.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT's named example for each contraceptive class: Lippes loop, Multiload 375, LNG-20 and the progestogen implant
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A hormone-releasing IUD does release a progestogen, so 'Progestogens' is taken as its partner, and that leaves LNG-20 — itself an intrauterine device — to be called an implant.
- **Why:** This question requires NCERT's named example for each contraceptive class, demonstrated by List I printing the classes — 'Non-medicated IUD', 'Copper releasing IUD', 'Hormone releasing IUD' — against the device names 'Multiload 375', 'Lippes loop' and 'LNG-20' in List II.
- **Note:** compare was considered here, since the three IUD classes in List I are near neighbours, and rejected: each row is settled by recalling which named device NCERT files under the class, not by holding two concepts apart.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which contraceptive methods are filed as natural or traditional — periodic abstinence, coitus interruptus, lactational amenorrhea — against the barrier methods listed next to them
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Coitus interruptus, periodic abstinence and lactational amenorrhea are the three items printed under the natural/traditional heading, so one recalled heading separates the key from all three at once; vaults is printed under the barrier heading beside condoms, diaphragms and cervical caps, and no wrong option has a route that reaches it.
- **Why:** This question requires the stored membership of the natural/traditional contraceptive list, demonstrated by the stem "Which of the following is not a natural/traditional contraceptive method?" with the other three options being the three items that list contains.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The common names NCERT prints beside its example fishes across cyclostomes, cartilaginous and bony fishes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  'Pterophyllum' shares its first syllable with 'Pteropus', NCERT's flying fox, so 'Pter-' reads as flying and Pterophyllum is taken for the flying fish, leaving Exocoetus with angel fish.
- **Why:** This question requires the common name NCERT prints beside each scientific name, demonstrated by List II holding only common names — 'Hag fish', 'Saw fish', 'Angel fish', 'Flying fish' — with no diagnostic feature given to reason from.
- **Note:** Likeness test applied against a name outside the question: the pull is the resemblance between Pterophyllum and Pteropus, and replacing Pterophyllum with an unlike genus kills it, so look_alike_term rather than nearby_fact.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Analogy and convergent evolution: unrelated animals under the same selection pressure arrive at the same body form, while homologous organs diverging from one ancestor is divergent evolution
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Convergent and divergent are taught as one pair of terms in one paragraph and differ by three letters, so holding the flipper example without which half of the pair it illustrates lands on divergent; divergence applies to homologous organs descended from one ancestral structure, and a penguin's forelimb and a dolphin's are not that.
- **Why:** This question requires the stated example-to-term pairing, demonstrated by the stem "The flippers of the Penguins and Dolphins are the example of the" naming the very pair printed as the standard illustration of analogy, with the term itself as the answer.
- **Note:** Swap test applied as §5.1 directs: the wrong term is both printed beside the right one and three letters away from it, and when both hold the likeness wins, so `look_alike_term` rather than `nearby_fact`. Replace "divergent" with an unlike word and the pull on option 1 dies, which is the test for likeness carrying it.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The chemical nature of hormones: cortisol, testosterone and progesterone are steroids, while glucagon belongs with the peptide and protein hormones
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Cortisol, testosterone and progesterone are the names printed in the steroid line itself, so one recalled line strikes out all three wrong options together; glucagon is printed in the peptide-and-protein line beside insulin, and no wrong option carries a route of its own.
- **Why:** This question requires the stored chemical class of four named hormones, demonstrated by the stem "Which of the following is not a steroid hormone?" with three options being names printed in the steroid list and one printed in the protein-and-peptide list.
- **Note:** The one resemblance in this option set, glucagon against glucocorticoid, points at the key rather than at any wrong option, so it supports no trap: a student pulled by it would be pulled towards option 1, which is the printed answer. That is why `look_alike_term` was ruled out and `no_trap` recorded.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which chromosome each disorder sits on: trisomy of the 21st for Down's, the 16th for alpha-thalassemia, the 11th for beta-thalassemia, an extra X for Klinefelter's
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All three wrong codes are rotations of the key that share no row with it, so any one remembered pair — Down's syndrome on the 21st chromosome — strikes out all three, and no code offers the alpha and beta thalassemia rows exchanged with the other two left right.
- **Why:** This question requires the chromosome NCERT assigns to each disorder, demonstrated by List II being four chromosome labels — '21st chromosome', '16th chromosome', '11th chromosome', 'X chromosome' — set against four named disorders with no rule printed to derive them.
- **Note:** The device this question looks built for is the alpha-thalassemia / beta-thalassemia pair, chromosome 16 against 11, but no option prints that exchange with the Down's and Klinefelter's rows intact, so it has nowhere to land; hence no_trap, which is a finding about this option set.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Colostrum, the first milk, carries maternal antibodies that give the newborn passive immunity, and that is the reason early breast-feeding is advised
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 3  
  A student who files breast milk under nutrition reads R's antibodies-and-resistance claim as a separate topic from A's 'bringing a healthy baby', grants both sentences and denies the link; but resistance in the newborn is exactly what the printed advice is given for, and no other reason is printed.
- **Proposed:** `explanation_link_denied` — The option grants both statements and rejects the explanatory link because the Reason looks narrower in topic than the Assertion. No §5.1 value covers a failure in judging the A/R link itself. half_right was ruled out because its 'two or more parts' test is about an option's own factual content; every A/R verdict option is a conjunction of verdicts, so using it here would tag every assertion-reason question half_right and carry no information. answers_other_question was ruled out because option 3 is a verdict, not a true fact answering a different question.
- **Why:** This question requires deciding whether the reason the source gives for early breast-feeding accounts for the recommendation, demonstrated by Reason R printing that reason — 'Colostrum contains several antibodies absolutely essential to develop resistance for the new born baby' — against an Assertion that states only the recommendation, 'Breast-feeding during initial period of infant growth is recommended by doctors'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each lung capacity is a fixed sum of the four respiratory volumes, and residual volume sits inside functional residual capacity, never inside vital capacity
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Vital capacity gets read as all the air the lungs hold, so residual volume is placed inside it, and IV is the only List II entry carrying residual volume, which pushes the three-volume sum onto functional residual capacity.
- **Why:** This question requires the composition NCERT states for each lung capacity, demonstrated by List II printing the sums themselves ('Expiratory reserve volume + Residual volume'), so row A is settled by the one stated sum 'Tidal volume + Expiratory reserve volume' rather than by holding the four capacities against each other.
- **Note:** nearby_fact rather than look_alike_term by the swap test: 'vital capacity' and 'total lung capacity' do not resemble each other, and replacing them with two unlike words leaves the trap intact because what carries the student is the neighbouring printed line that adds residual volume to vital capacity. half_right was ruled out: on a four-row pairing code every wrong option is partly right, so that label would not discriminate here. Key checked pair by pair and it holds.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What marks each sub-phase of prophase I: thin threads in leptotene, synapsis in zygotene, recombination nodules in pachytene, terminalised chiasmata in diakinesis
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  Pachytene is learnt as the crossing-over stage and chiasmata are the crossover points, so 'Completion of terminalisation of chiasmata' is read as the end of crossing over and placed at pachytene instead of diakinesis.
- **Why:** This question requires the marker NCERT attaches to each named sub-phase of prophase I, demonstrated by List II entries such as 'Appearance of recombination nodules' and 'Chromosomes look like thin threads', each of which belongs to one sub-phase on its own line.
- **Note:** wrong_site_attacked rather than nearby_fact because the event in option 3 is a real printed event and only its stage moves, from diakinesis to pachytene, which is the rulebook's 'right event in the wrong place or time' test. asks is fact_line and not order: the answer form is a pairing code and each row is settled by its own printed marker, not by sequencing the sub-phases. The stem carries the two column headings run into the question line ('List I (Sub Phases of Prophase I) List II (Specific Characters)'), a join in extraction that does not change the printed shape. Key checked pair by pair and it holds.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** FSH acts on the ovarian follicle in the female and on Sertoli cells in the male; Leydig (interstitial) cells are LH's target and the source of androgens
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  A's female clause is right and R's 'interstitial cells' echoes A's 'Leydig cells', so a student checks the half that matches and accepts A whole; but FSH's male target is the Sertoli cell, and Leydig cells are where LH acts.
- **Why:** This question requires checking one printed fact before any explanatory link can be weighed, demonstrated by Assertion A reading 'FSH acts upon ovarian follicles in female and Leydig cells in male', whose male half names the wrong target cell, while both clauses of Reason R are stated facts.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The hymen can be torn by causes other than coitus and can stay intact after it, which is why its state reports nothing about virginity
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 2  
  The line carried from the chapter is that the hymen is often torn during first coitus, and Statement II is that line with 'often' replaced by 'only', so checking the content and not the scope leaves both statements marked true.
- **Proposed:** `overclaiming_quantifier` — The option fails on one quantifier and nothing else: drop 'only' from Statement II and it becomes true. half_right is ruled out because Statement II carries a single claim, not two or more parts, and the evidence needed is a counter-example (a fall, a jolt, a tampon) rather than a second failed clause. reversed is ruled out because nothing is inverted - the direction of the claim is right and only its scope is wrong. nearby_fact and look_alike_term are ruled out because no second name is involved. The retired §5.2 list held this device under this name with the counter-example as required evidence; §5.1 has no family for it.
- **Why:** This question requires whether first coitus is the sole cause of a torn hymen, demonstrated by Statement II's 'The hymen is torn during the first coitus only' set against Statement I's 'presence or absence of hymen is not a reliable indicator of virginity'. No live §5.1 value covers an option that fails on a quantifier alone, so new_trap carries the proposal rather than forcing half_right onto a single-clause statement.
- **Note:** Statement II differs from the textbook sentence by one word ('only' for 'often'); that single word is the whole of the item's difficulty.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An autoimmune disorder is one in which the body's own lymphocytes attack its own tissue, which separates myasthenia gravis, rheumatoid arthritis and SLE from gout's uric-acid crystals and muscular dystrophy's genetic degeneration
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Muscular dystrophy is printed in the same disorders list as myasthenia gravis and weakens skeletal muscle the same way, so a student recalling that list rather than each cause carries the neighbour across into the autoimmune set. Its cause is given as progressive genetic degeneration of muscle, not an attack by the body's own antibodies.
- **Why:** This question requires the one line given for each named disorder's cause, demonstrated by 'Gout' and 'Muscular dystrophy' standing in the same printed disorders list as 'Myasthenia gravis'; the test applied was the swap test - replace muscular dystrophy with any unlike disorder name from that same list and the pull survives, because position and not resemblance carries the student, so nearby_fact and not look_alike_term.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Coelom grades: a true mesoderm-lined cavity from annelids onward, a cavity present but unlined in Aschelminthes, and no cavity at all in Platyhelminthes
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Aschelminthes have a cavity that is not a true coelom, and a student who stores that as 'no real coelom' reads 'Aschelminthes are acoelomates' as the line they learnt. The paper has exchanged the two grades between the two worm phyla: Aschelminthes are the pseudocoelomates and Platyhelminthes the acoelomates.
- **Why:** This question requires which coelom grade is assigned to each named phylum, demonstrated by statements C and D being exactly each other's swap - 'Aschelminthes are acoelomates' and 'Platyhelminthes are pseudocoelomates'; look_alike_term was ruled out because no option offers a wrong term, both grades being real names in the printed scheme, and what is inverted is which phylum holds which.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Transcription reads the template strand 3'-to-5' and builds the transcript 5'-to-3' by complementary pairing, with uracil wherever the template carries adenine
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Pairing the printed template base by base gives 5'ATGTACCGTTTATAGGTAAGT3', which is the coding DNA strand and a correct answer to 'write the other strand'; the stem asks for the product of RNA polymerase, which carries U where that strand carries T.
- **Why:** This question requires complementary base pairing and the T-to-U substitution applied to a printed sequence, demonstrated by the stem supplying '3'TACATGGCAAATATCCATTCA5'' and options 1 and 2 carrying the same base order with T against U.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hardy-Weinberg equilibrium holds only while nothing shifts allele frequencies; gene migration, genetic drift, mutation, genetic recombination and natural selection are the five factors NCERT prints as disturbing it
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Genetic recombination is one of the five factors NCERT prints as affecting Hardy-Weinberg equilibrium, so it is a true answer to 'which factor affects it', and the argument that recombination only reshuffles alleles already present leaves p and q looking untouched, which makes it read as the harmless one the negated stem wants.
- **Why:** This question requires the stated membership of NCERT's list of factors that disturb genetic equilibrium, demonstrated by 'Which one of the following factors will not affect the Hardy-Weinberg equilibrium?' set over three options - 'Genetic recombination', 'Genetic drift', 'Gene migration' - that the book prints as members of that list.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ti stands for tumour inducing: the Agrobacterium tumefaciens plasmid delivers T-DNA that turns dicot cells into a crown-gall tumour, and it is disarmed before use as a vector
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  NCERT also says the Ti plasmid has been converted into a cloning vector that is no longer pathogenic, so a student who carries that disarming line into the name reads the plasmid's relation to tumours in the opposite sense and expands the 'i' as inhibiting.
- **Why:** This question requires the stated expansion of an abbreviation NCERT writes out, demonstrated by 'The “Ti plasmid” of Agrobacterium tumefaciens stands for' with three rival expansions of the same two letters. On the trap axis the swap test was applied to option 2: replacing 'inhibiting' with the dissimilar 'suppressing' keeps the pull intact, so the inverted meaning and not the spelling resemblance is doing the work, which rules out look_alike_term.
- **Note:** Options print 'Tumour' and 'Tumor' inconsistently across 2, 3 and 4; the spelling difference carries no part of the trap.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each nephron segment's wall does one job: the descending limb of the loop of Henle passes water and holds back salts, the ascending limb does the reverse, and the PCT's brush-bordered cuboidal lining raises the surface for reabsorption
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The PCT line is reproduced word for word except for the epithelium, and 'columnar' is the term standing next to 'cuboidal' in the taught epithelium list, so a student who has caught the limb error in Statement I passes Statement II as the sentence they know.
- **Why:** This question requires the permeability of the named limb of the loop of Henle and the epithelium NCERT names for the PCT, demonstrated by Statement II's 'simple columnar brush border epithelium'. The trap is nearby_fact on the swap test: put any other member of the epithelium list into that slot and the pull survives, because what carries the student is the whole surrounding sentence being verbatim and the term sitting beside the right one in a taught list, not a likeness between 'columnar' and 'cuboidal'.
- **Note:** Both statements are altered, so two one-error routes exist; the primary trap is placed on option 1 because the epithelium word is the finer alteration, while the descending-limb permeability is the line the chapter drills and is recorded as the option 4 route.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each class of biomolecule is held together by its own linkage, and the hydrolase named after the substrate is the enzyme that breaks that linkage
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The one confusable pairing here is nuclease with 'Ester bond', since the nucleic-acid backbone is a phosphodiester; carried through it gives A-IV, B-II, C-I, D-III, which is not printed, and amylase with 'Glycosidic bond' appears only in the key, so every printed wrong code is struck by that one pair.
- **Why:** This question requires the linkage NCERT names for each class of biomolecule, demonstrated by List II holding only bond names, 'Phosphodiester bond' and 'Glycosidic bond', with no reagent, condition or product printed anywhere in the stem.
- **Note:** asks is fact_line and not reaction: although the List I items are hydrolases, nothing printed asks for a conversion, a product or an agent that effects one, only the bond name tied to each macromolecule class. no_trap is recorded as a finding on the test stated in group_note, not as a gap. Key checked pair by pair and it holds.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Joints are classed by what holds the bones together, and how much movement is allowed follows from that: fibrous none, cartilaginous limited, synovial free
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The one confusable exchange here is fibrous with the vertebrae and cartilaginous with the skull; carried through it gives A-I, B-III, C-IV, D-II, which is not printed, and every printed wrong code instead has to accept a joint type paired with a movement its own definition denies.
- **Why:** This question requires the example and the movement NCERT prints for each joint type, demonstrated by List II carrying both in one entry, 'Skull, don't allow any movement', so each row is answered from one printed line.
- **Note:** No wrong code shares a single pair with the key, so one secure row, hinge with the knee, strikes all three; recorded as no_trap on the test stated in group_note. Key checked pair by pair and it holds.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The heart's conducting route: SA node, then AV node, then AV bundle or bundle of His, then the bundle branches, then the Purkinje fibres
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'AV bundle' and 'AV node' share the AV in their names, so a student who keeps one AV station in the chain runs SA node straight into the AV bundle and is left with the AV node to park at the tail. Their own chain - SA node, AV bundle, bundle branches, Purkinje fibres - sits intact inside E-A-D-B-C, which is why the string reads almost right.
- **Why:** This question requires the printed order of the conducting stations, demonstrated by option 1's 'E-A-D-B-C', which keeps AV bundle, bundle branches and Purkinje fibres in order and strands the AV node at the end; the test applied was the swap test - print 'bundle of His' in place of 'AV bundle' and the pull dies, so the resemblance of the two AV names is doing the work and the label is look_alike_term, not nearby_fact.
- **Note:** E1 called this arrange_in_order, a retired value; the printed lettered block puts it under qtype statements with asks: order.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A bioreactor is the large-volume vessel - 100 to 1000 litres - in which cells convert raw material into product under controlled stirring, aeration, pH and temperature
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Option 1 prints three of the five systems NCERT lists for a bioreactor - agitator, oxygen delivery and foam control - and leaves out the temperature control and pH control systems, so a student checking the sentence against the remembered list of five reads the short list as the incorrect statement. An incomplete list is still a true claim; the sentence the book contradicts is 'small scale' in option 4.
- **Why:** This question requires judging four printed claims about the bioreactor against NCERT's own lines, demonstrated by 'Which of the following statements is incorrect?' over options that are each a full statement, with 'Bio-reactors are used to produce small scale bacterial cultures' the only clause the book contradicts.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** In pBR322 the ori is where replication starts and it sets the copy number of the linked DNA, rop codes the proteins of plasmid replication, and ampR and tetR are the selectable markers
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The second clause of option 2, 'Y for protein involved in the replication of Plasmid', is word for word the clause the key carries for Y, so a student who settles Y first finds the option confirmed and takes the X clause along with it; X is the ori that controls the copy number, not an antibiotic-resistance gene.
- **Why:** This question requires two roles read off a labelled plasmid map and supplied together, demonstrated by 'Find the role of ‘X’ and ‘Y’ genes' with every option stating a role for X and a role for Y.
- **Note:** The pattern classifier returned statement_options, but the stem asks for two things at once - the role of X and the role of Y - and each option supplies both, so the printed shape is two_part; long option sentences alone do not make it statements. The figure is recorded as present with a png path and hash, so the source is not incomplete, but I am restricted to this input file and did not open it: the identities of X and Y are taken from the printed key's own clauses, and the trap above rests only on option 2 sharing the key's Y clause verbatim, not on any figure position.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named disease, diagnostic test or pigment belongs to one causal agent: rhinovirus to the common cold, haemozoin to Plasmodium, the Widal test to typhoid, mites to allergy
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Three rows are settled by one printed line each, so the unfamiliar term haemozoin is then forced; the nearest code, option 3, asks for the common cold to be caused by Plasmodium, against the printed pairing of rhinoviruses with the common cold, and nothing in the stem supports the exchange in either direction.
- **Why:** This question requires the agent NCERT names for each disease, test or pigment, demonstrated by List II being four agents and conditions, 'Rhinoviruses', 'Plasmodium', 'Typhoid', 'Dust mites', with one printed line standing behind each row.
- **Note:** Haemozoin is the only term here a student may not hold, and the pairing code forces it once the other three rows are placed, which is why the question carries no trap rather than a trap on the haemozoin row. Key checked pair by pair and it holds.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which structure each named part belongs to: the axoneme to cilia and flagella, the cartwheel to the centriole, cristae to the mitochondrion, the satellite to the chromosome
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Three rows are settled by single printed lines and the cartwheel row is then forced; the nearest code, option 4, needs cristae to belong to the centriole, and nothing in the source attaches a cartwheel to the mitochondrion, so the exchange it rests on has no printed line behind it.
- **Why:** This question requires which structure owns each named part, demonstrated by List I being parts, 'Cartwheel pattern' and 'Crista', against List II being the four structures that carry them.
- **Note:** 'Satellite' is the chromosome's segment beyond the secondary constriction, and 'cartwheel pattern' the centriole's hub-and-spokes; both are printed in the chapter this question is drawn from. Recorded as no_trap on the test stated in group_note, with option 4 proved rather than assumed. Key checked pair by pair and it holds.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** The non-chordate side of the chordate comparison: no notochord, a ventral solid nerve cord, an unperforated pharynx, a dorsal heart and no post-anal tail
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  D's "Heart is dorsal if present" is true of non-chordates, so the word dorsal is already accepted on that side and C's "Central nervous system is dorsal" reads as more of the same. On the non-chordate side the nerve cord is ventral and solid, so this set carries one false member and also leaves out E.
- **Why:** This question requires sorting five statements onto the two sides of the chordate / non-chordate comparison, demonstrated by "Notochord is absent" and "Central nervous system is dorsal" being the same pair of table rows read from opposite columns.
- **Note:** The stem's instruction line reads only "The following are the statements about non-chordates" with no printed verb telling the student to select the correct ones; the four combination options fix the task, so it is tagged as printed. Nothing is missing from the stem, statements, options or key, so this is not a source-damage case.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** ABO multiple alleles in a family: an O child is $\mathrm{ii}$, so each parent must hand on an $\mathrm{i}$, which only heterozygous A and B parents can do
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Every genotype in B does give the blood group printed against it: $\mathrm{I^{B}I^{B}}$ is B, $\mathrm{I^{A}I^{A}}$ is A and $\mathrm{ii}$ is O, so a student who checks genotype against phenotype and stops there signs the set off. Two homozygous parents can only hand on $\mathrm{I^{A}}$ and $\mathrm{I^{B}}$, so their child would be AB and the three cannot be this family.
- **Why:** This question requires applying the ABO allele rules to a stated family, demonstrated by "the blood group of father is $\mathrm{B^{+}}$, mother is $\mathrm{A^{+}}$ and child is $\mathrm{O^{+}}$" having to be met by genotypes that also pass an $\mathrm{i}$ from each parent.
- **Note:** Statements E and A write the same kind of heterozygote with the alleles in opposite order ($\mathrm{iI^{B}}$ against $\mathrm{I^{B}i}$); order inside a genotype carries no meaning, so that was not treated as a difference between them. The printed key, option 2, follows from the stem as given.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which animal group dominated in each geological era: lower invertebrates in the Proterozoic, fish and amphibia in the Paleozoic, reptiles and birds in the Mesozoic, mammals in the Cenozoic
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student holding the two headline eras, the Mesozoic as the age of reptiles and the Proterozoic as the earliest with lower invertebrates, has only the Cenozoic and Paleozoic left and reads List I's printed order as a timeline, which puts the mammals in the Paleozoic
- **Why:** This question requires the era-by-era fauna NCERT prints in its account of evolution, demonstrated by List I holding four named eras ('Mesozoic Era', 'Proterozoic Era') against List II's faunal headings ('Birds & Reptiles', 'Mammals') with no criterion printed to apply.
- **Note:** B-I is common to three of the four options, so the question effectively turns on the Cenozoic/Paleozoic pair. An `order` reading of `asks` is arguable because the rows are eras in time sequence, but each row is still one line NCERT prints against an era, so fact_line is recorded.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each ECG deflection reports one electrical event: P is atrial depolarisation, QRS ventricular depolarisation, T ventricular repolarisation, and the T-P gap is the electrically silent interval
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  A student secure on 'the T wave is repolarisation of the ventricles' reads the tall QRS as the opening event of the beat and so hangs the atrial depolarisation on it, which leaves the small P wave as the silent stretch
- **Why:** This question requires the stated meaning of each deflection of the ECG, demonstrated by List II carrying the events in the chapter's own words — 'Depolarisation of atria', 'Repolarisation of ventricles', 'Heart muscles are electrically silent.'
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Endocrine disorders read off the hormone: hyper- and hypo-secretion of thyroid hormone give exophthalmic goiter and cretinism, excess growth hormone gives acromegaly, excess cortisol gives Cushing's syndrome
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Every List II entry prints the hormone and the sign together — 'Hyper secretion of thyroid hormone & protruding eye balls', 'Excessive secretion of growth hormone' — so each row is decided by words standing in the option, and no wrong code can be assembled without contradicting one of them
- **Why:** This question requires the hormone-to-disorder lines of the endocrine chapter, demonstrated by each List II entry naming its own hormone and sign — 'Excess secretion of cortisol, moon face & hypergylcemia.'
- **Note:** Recorded as no_trap on the evidence that the List II entries state their own causal hormone, which leaves no wrong pairing with a printed route; this is a finding about the option set, not an absence of checking.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Mitochondria and chloroplasts are both double-membrane organelles, and the "inner membrane is relatively less permeable" line compares an organelle's own two membranes, not one organelle's inner membrane against the other's
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The phrase "the inner membrane is relatively less permeable" belongs to the paragraph that pairs the two organelles, so a reader who recognises the phrase inside Statement II signs the pair off without noticing that the comparison has been re-aimed from one membrane against the other to one organelle against the other.
- **Why:** This question requires the chapter's membrane-permeability line to be held against the organelle it was printed for, demonstrated by Statement II's "Inner membrane of mitochondria is relatively less permeable, as compared chloroplast" while Statement I states only the shared "double membranes bound" property.
- **Note:** OCR damage in the printing: the instruction line reads "choose the mis appropriate answer", Statement I drops the copula ("both double membranes bound organelles") and Statement II drops a preposition ("as compared chloroplast"). Not treated as source_incomplete, because both statements and all four options are present and legible and neither truth value turns on the missing words; the printed key 4 is consistent with "most appropriate", which the other three members of this group print in full. Tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The enzyme catalytic cycle in order: substrate binds the active site, the enzyme-substrate complex forms, the substrate's bonds break, products are released, the free enzyme is ready again
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  "Substrate enzyme complex formation" (A) and "Substrate binding to active site" (E) name the same moment in different words, so a student who reads them as one event has only four distinct steps to order — binding, bonds broken, products released, enzyme free — gets those four in the right order and parks the leftover letter A at the end. The complex is a step of its own that follows the binding, so A sits second and the order is E, A, D, C, B.
- **Why:** This question requires ordering the printed steps of one pathway, demonstrated by "select the correct sequential steps" and by all four options holding the same five statements in different arrangements.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Glandular epithelium is classed by how many cells make the gland — one goblet cell against a cluster as in a salivary gland — and by where the secretion goes, while compound epithelium is the multilayered lining such as the moist buccal surface
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  NCERT's sentence on where compound epithelium is found lists the buccal cavity, the ducts of the salivary glands and the pancreatic ducts together, so a student revising from that one sentence pulls 'Salivary glands' onto the compound row and 'Pancreas' onto the row above it
- **Why:** This question requires NCERT's named example for each epithelial class, demonstrated by List I printing the classes ('Unicellular glandular epithelium', 'Compound epithelium') against List II's examples ('Goblet cells of alimentary canal', 'Moist surface of buccal cavity').
- **Note:** Row B-I is itself defensible on NCERT's own sentence, which names the inner lining of salivary gland ducts as compound epithelium; it is excluded only because 'Salivary glands' is needed as the multicellular gland, so the one-to-one constraint, not the row's falsity, settles it. The printed key stands as a whole code and is tagged as printed.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Every nephron's Malpighian corpuscle lies in the cortex; what makes a nephron juxtamedullary is a long loop of Henle running deep into the medulla
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  'Juxta medullary' reads as 'next to the medulla', so a student who takes the name as a statement of where the nephron sits moves its renal corpuscle across the boundary into the outer medulla; NCERT keeps every Malpighian corpuscle in the cortex and sends only the loop of Henle into the medulla.
- **Why:** This question requires one stated fact about the juxtamedullary nephron, demonstrated by 'Loop of Henle of juxta medullary nephron runs deep into medulla' standing against three options that relocate or re-count the same nephron.
<!--/ecat-->

## Q195

Biology · zoology · Human Health and Disease

Given below are two statements :
Statement I : Bone marrow is the main lymphoid organ where all blood cells including lymphocytes are produced.
Statement II : Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes.
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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bone marrow produces all blood cells including lymphocytes, and bone marrow and thymus BOTH supply the micro-environment in which T-lymphocytes develop and mature
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Statement I, printed directly above, says the marrow is where blood cells are produced, and a reader who turns that into a division of labour — production in the marrow, maturation in the thymus — strikes Statement II for letting the marrow mature T-cells as well.
- **Why:** This question requires the stated fact about which organs supply the micro-environment for T-lymphocyte maturation, demonstrated by Statement II's "Both bone marrow and thymus provide micro environments for the development and maturation of T-lymphocytes."
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The cockroach gut front to back: the crop stores food, the gizzard grinds it, the gastric caeca ring the foregut-midgut junction and the Malpighian tubules the midgut-hindgut junction
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  A student who has the crop and the gizzard secure still has two rows that are both 'a ring of tubules at a gut junction', and carrying across the mammalian caecum, which sits where the small intestine meets the large, puts the gastric caeca at the midgut-hindgut junction and the Malpighian tubules forward
- **Why:** This question requires the name the chapter gives each described part of the cockroach gut, demonstrated by the rows quoting its descriptions — 'Ring of 6-8 blind tubules at junction of foregut and midgut.'
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The brain stem is midbrain, pons and medulla oblongata; the cerebrum is forebrain, and the corpus callosum is the tract joining its two hemispheres
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Two of the three parts Statement II lists, medulla oblongata and pons, are the right ones, and the third slot is filled with cerebrum, a brain part named in the same division of the brain, so a reader who checks the two familiar names signs the list off.
- **Why:** This question requires the stated membership of the brain stem, demonstrated by Statement II's "The brain stem consists of the medulla oblongata, pons and cerebrum."
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gause's competitive exclusion principle is about two closely related species competing for the SAME resources, and the inferior competitor is eliminated only where those resources are limiting
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The principle is carried as a sentence shape ending in "cannot exist indefinitely", and this printing reads "competing for different resources" where the principle says the same resources, so a reader who recognises the shape endorses Statement I and ticks both true.
- **Why:** This question requires the printed definition of Gause's principle to be checked clause by clause, demonstrated by Statement I's "competing for different resources" standing beside Statement II's "This may be true if resources are limiting."
- **Note:** Options are worded true/false here while the other three members of the group use correct/incorrect; the verdict set is the same four, so the shape is unchanged.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The transcription machinery sorted by job: RNA polymerase III transcribes tRNA and snRNAs, rho factor terminates, snRNPs splice out the introns, and the TATA box is a promoter element
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  With splicing-to-snRNPs and TATA-box-to-promoter settled, only 'Rho factor' and 'SnRNAs, tRNA' remain, and rho factor is the machinery term printed beside the RNA polymerases in the same transcription section, so it is attached to the polymerase row and termination takes what is left
- **Why:** This question requires the job the chapter assigns each transcription component, demonstrated by List I printing 'RNA polymerase III' and 'Termination of transcription' against List II's 'SnRNAs, tRNA' and 'Rho factor'.
<!--/ecat-->

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

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Hormonal control of the testis: LH (ICSH) drives the Leydig cells to make androgens, while FSH drives the Sertoli cells, whose secretions carry spermiogenesis, the shaping of spermatids into sperm
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The stem's own last word is 'spermatogenesis', so the closing blank gets that umbrella term instead of spermiogenesis, the spermatid-to-sperm shaping that the Sertoli secretions actually carry. Option 1 keeps Leydig cells then Sertoli cells in NCERT's own sentence order, so two right slots sit beside the ICSH-for-FSH slip in the first.
- **Why:** This question requires four blanks read off the figure to be filled with NCERT's hormone-to-cell-to-stage chain in the testis, all four at once, demonstrated by the stem 'Identify the correct option (A), (B), (C), (D) with respect to spermatogenesis' and by options that each bundle four terms, such as 'FSH, Leydig cells, Sertoli cells, spermiogenesis.', accepted or rejected whole.
- **Note:** Two things about the record. (i) E1_question_type_why says 'statement_options, 15 full-statement options', but no option is a statement: each is a comma-separated set of four terms filling the figure's blanks (A)-(D), which is the rulebook's pair_options shape with a multi_part_respectively answer, so I recorded the shape I can see as two_part - the only ECAT qtype value in the several-blanks-answered-together family - rather than mcq, which would hide that three slots right scores zero. (ii) figure_image.text is null, so the figure's blank positions are not transcribed in my input; the figure itself is recorded as present (sha256 33dd680a..., cdn_url), so this is not source damage, but my slot-to-term assignment is inferred from the four option sets plus the printed key rather than read off the figure. The trap routes were written to be slot-order-independent where possible: option 1 differs from the key only in the two end terms, and option 3 names the same cell type twice, both of which are readable from the options alone. Key checks out against NCERT's lines (FSH to Sertoli cells, factors helping spermiogenesis).
<!--/ecat-->

