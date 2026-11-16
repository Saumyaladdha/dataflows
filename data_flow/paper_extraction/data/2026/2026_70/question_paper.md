# NEET (UG) 2026 · Code 70

180 questions · source `NEET_Papers/2026/Set_70/NEET_2026_Code_70.pdf` · every image a CDN link (0 without one) · 52 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Modern Physics

> ⚠ The paper prints the electron's mass as "1/(4πε₀) = 9 × 10⁻³¹ kg": the label 1/(4πε₀) is misplaced and the value is the mass of the electron (m = 9 × 10⁻³¹ kg). Kept as printed. Four-file audit, 2026-11-04.

A photon and an electron, each of $20\,\mathrm{eV}$ energy, move in free space. The ratio of linear momentum of electron $p_e$ to that of photon $p_{Ph}$, $\dfrac{p_e}{p_{Ph}}$ is : (Take speed of light $= 3 \times 10^{8}\,\mathrm{m\,s^{-1}}$, charge of electron $= -1.6 \times 10^{-19}\,\mathrm{C}$ and mass of electron $\dfrac{1}{4\pi\epsilon_0} = 9 \times 10^{-31}\,\mathrm{kg}$ )

- (1) $275$
- (2) $\dfrac{2}{450}$
- (3) $\dfrac{1}{250}$
- **(4)** $225$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $E = 20\,\mathrm{eV} = 20 \times 1.6 \times 10^{-19} = 3.2 \times 10^{-18}\,\mathrm{J}$.
2. For the electron (non-relativistic), $p_e = \sqrt{2mE} = \sqrt{2 \times 9 \times 10^{-31} \times 3.2 \times 10^{-18}} = \sqrt{5.76 \times 10^{-48}} = 2.4 \times 10^{-24}\,\mathrm{kg\,m\,s^{-1}}$.
3. For the photon, $p_{Ph} = \frac{E}{c} = \frac{3.2 \times 10^{-18}}{3 \times 10^{8}} = 1.067 \times 10^{-26}\,\mathrm{kg\,m\,s^{-1}}$.
4. $\frac{p_e}{p_{Ph}} = \frac{2.4 \times 10^{-24}}{1.067 \times 10^{-26}} = 225$, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves, Photon Energy and Number of Photons · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q001_37a6352f_03112026.png?v=37a6352fb253)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At the same energy a photon carries momentum $E/c$ while an electron carries $\sqrt{2mE}$, so the massive particle's momentum is larger by the factor $c\sqrt{2m/E}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Both momenta come out right and the division is then done the other way up, $p_{Ph}/p_e$, which is exactly $\frac{1}{225}$ and is printed as $\frac{2}{450}$.
- **Why:** This question requires two momenta computed from one energy and then placed in the printed order, demonstrated by 'The ratio of linear momentum of electron $p_e$ to that of photon $p_{Ph}$' sitting beside the supplied $c$, $e$ and electron mass.
- **Note:** Stem debris: the bracket reads 'mass of electron $\frac{1}{4\pi\epsilon_0} = 9 \times 10^{-31}$ kg', pasting the constant label $1/4\pi\epsilon_0$ in front of the electron mass. The value and unit the calculation needs are intact and give the printed key 225, so the question is tagged as printed; the stray symbol is flagged for repair.
<!--/ecat-->

## Q2

Physics · Mechanical Properties of Fluids

Water flows in a streamline motion through a horizontal pipe of circular cross-section as shown in the figure. The pressure difference of water between $P$ and $Q$ is $15\,\mathrm{N\,m^{-2}}$. The area of cross-section at $P$ and $Q$ are $40\,\mathrm{cm^2}$ and $20\,\mathrm{cm^2}$, respectively. The rate of flow of water through the pipe, in $\mathrm{cm^3\,s^{-1}}$, is: [Take density of water $= 1000\,\mathrm{kg\,m^{-3}}$]

![printed figure: Horizontal pipe narrowing from a wide section P to a narrow section Q and widening again, with its axis](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q002_e2d1e83d_03112026.svg?v=e2d1e83de8f7)

*Horizontal pipe narrowing from a wide section P to a narrow section Q and widening again, with its axis*

![drawn: Horizontal pipe narrowing from a wide section P to a narrow section Q and widening again, with its axis](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q002_question_bd44f2a0_04112026.svg?v=bd44f2a062a7)  
*drawn by code/lib/physics_figure.py*

- **(1)** $400$
- (2) $100$
- (3) $200$
- (4) $300$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Continuity: $A_P v_P = A_Q v_Q \Rightarrow v_Q = \frac{40}{20} v_P = 2v_P$.
2. Bernoulli (horizontal pipe): $P_P - P_Q = \frac{1}{2}\rho (v_Q^2 - v_P^2) = \frac{1}{2}\rho (3v_P^2)$.
3. $15 = \frac{1}{2}(1000)(3v_P^2) = 1500\,v_P^2 \Rightarrow v_P^2 = 0.01$.
4. $v_P = 0.1\,\mathrm{m\,s^{-1}} = 10\,\mathrm{cm\,s^{-1}}$.
5. Rate of flow $= A_P v_P = 40\,\mathrm{cm^2} \times 10\,\mathrm{cm\,s^{-1}} = 400\,\mathrm{cm^3\,s^{-1}}$, which is option $1$.

**Subtopic:** Equation of Continuity and Bernoulli's Equation · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q002_a813e028_03112026.png?v=a813e0285e54)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Continuity ties the two speeds through the two areas, Bernoulli turns the pressure drop into the difference of their squares, and the volume flow rate is one number for both sections
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The speed at the wide section comes out as $10\,\mathrm{cm\,s^{-1}}$ and is then multiplied by the narrow area, $20\,\mathrm{cm^2}$ in place of $40\,\mathrm{cm^2}$, giving $200$ where the flow rate is $400$.
- **Why:** This question requires continuity and Bernoulli chained to a single number, demonstrated by 'The rate of flow of water through the pipe, in $\mathrm{cm^3\,s^{-1}}$' being asked from a pressure difference and two areas.
<!--/ecat-->

## Q3

Physics · Rotational Motion

A thin horizontal disc is rotating about a vertical axis passing through its fixed centre $O$. Its angular momentum is $L_A$ and $L_B$ computed about points $A$ and $B$, respectively, with $OB = 2 \times OA$. The value of $\frac{L_A}{L_B}$ is :

![printed figure: Horizontal disc about centre O rotating anticlockwise, with points A and B on a dotted line from O, OB = 2 OA](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q003_afb4d834_03112026.svg?v=afb4d8343482)

*Horizontal disc about centre O rotating anticlockwise, with points A and B on a dotted line from O, OB = 2 OA*

![drawn: Horizontal disc about centre O rotating anticlockwise, with points A and B on a dotted line from O, OB = 2 OA](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q003_question_bd12b888_04112026.svg?v=bd12b888a0a6)  
*drawn by code/lib/physics_figure.py*

- (1) $2$
- (2) $\frac{1}{4}$
- (3) $\frac{1}{2}$
- **(4)** $1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The centre $O$ (the centre of mass) is fixed, so $\vec v_{cm} = 0$ and the total linear momentum $\vec P = M\vec v_{cm} = 0$.
2. About any point $P$: $\vec L_P = \vec L_O + \vec r_{PO} \times \vec P$.
3. With $\vec P = 0$, $\vec L_A = \vec L_B = \vec L_O = I\omega$, independent of $OA$ and $OB$.
4. $\frac{L_A}{L_B} = 1$, which is option $4$.

**Subtopic:** Problems on Angular Momentum · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q003_d26f2c5c_03112026.png?v=d26f2c5ccf27)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** With the disc's centre fixed, $\vec{v}_{cm}=0$, so the $\vec{r}\times M\vec{v}_{cm}$ term vanishes and the angular momentum is the same about every point
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Angular momentum is carried as $L=mvr$, the $r$ in it is read as the distance of the reference point, and $L_A/L_B$ becomes $OA/OB=\tfrac12$.
- **Why:** This question requires knowing by what factor the angular momentum differs when the reference point moves outward, demonstrated by the stem giving only '$OB = 2 \times OA$' and asking for '$\frac{L_A}{L_B}$'.
<!--/ecat-->

## Q4

Physics · Electromagnetic Induction

Consider a long solenoid of length $l$ and radius $r$. If $n$ is the number of turns per unit length and $\mu_0$ is the permeability of free space, the inductance of the solenoid is :

- (1) $2\mu_0 \pi n^2 r^2 l$
- **(2)** $\mu_0 \pi n^2 r^2 l$
- (3) $\mu_0 n^2 r^2 l$
- (4) $(\mu_0 / 2\pi) n^2 r^2 l$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Field inside a long solenoid: $B = \mu_0 n I$.
2. Flux through one turn: $\phi = B A = \mu_0 n I \pi r^2$.
3. Total turns $N = n l$, so flux linkage $N\phi = \mu_0 n^2 \pi r^2 l\, I$.
4. $L = \frac{N\phi}{I} = \mu_0 \pi n^2 r^2 l$, which is option $2$.

**Subtopic:** Self Inductance of Solenoid · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q004_4424a378_03112026.png?v=4424a3787470)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A long solenoid's self-inductance is $L=\mu_0n^2lA$, and for a circular cross-section the area is $\pi r^2$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The standard form $L=\mu_0n^2lA$ is recalled correctly and the cross-section is then entered as $r^2$, so the $\pi$ of $\pi r^2$ never appears.
- **Why:** This question requires the solenoid flux linkage turned into an expression, demonstrated by the options differing only in the numerical factor attached to '$\mu_0 n^2 r^2 l$'.
<!--/ecat-->

## Q5

Physics · Thermal Properties of Matter

The temperature of a metallic sphere of radius $R$ is increased by a small amount $\Delta T$ . If the linear coefficient of thermal expansion of the metal is $\alpha$ , the approximate increase in the volume of the sphere is :

- (1) $6\pi R^{3}\alpha\Delta T$
- (2) $2\pi R^{3}\alpha\Delta T$
- (3) $3\pi R^{3}\alpha\Delta T$
- **(4)** $4\pi R^{3}\alpha\Delta T$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The coefficient of volume expansion is $\gamma = 3\alpha$.
2. The initial volume is $V = \frac{4}{3}\pi R^{3}$.
3. $\Delta V = \gamma V \Delta T = 3\alpha \cdot \frac{4}{3}\pi R^{3} \Delta T$.
4. $\Delta V = 4\pi R^{3}\alpha\Delta T$, which is option $4$.

**Subtopic:** Thermal Expansion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q005_f204ba0b_03112026.png?v=f204ba0b0da0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Volume expansion uses $\gamma=3\alpha$, and the volume it multiplies is the sphere's $\tfrac43\pi R^3$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $\gamma=3\alpha$ is applied correctly and the sphere's volume is written as $\pi R^3$, so the dropped $\tfrac43$ turns $4\pi R^3\alpha\Delta T$ into $3\pi R^3\alpha\Delta T$.
- **Why:** This question requires the volume coefficient and the sphere's volume combined into an expression, demonstrated by 'the approximate increase in the volume of the sphere' with options differing only in the factor on $\pi R^3\alpha\Delta T$.
<!--/ecat-->

## Q6

Physics · Current Electricity

Consider two circuits, (A) and (B), each having two resistors. One of them has a positive temperature coefficient of resistance, $+\alpha$, while the other one has a negative temperature of coefficient, $-\alpha$, as shown in the figure. The current through these circuits are denoted by $I_A$ and $I_B$. At initial temperature, the resistance of the two resistors is $R_0$. As the temperature is increased, the correct option that describes the variation of current in these circuits is :

![printed figure: Circuit (A): cell V with R0(1-αΔT) and R0(1+αΔT) in series; circuit (B): cell V with the two resistors in parallel](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q006_5621d276_03112026.svg?v=5621d2769ddd)

*Circuit (A): cell V with R0(1-αΔT) and R0(1+αΔT) in series; circuit (B): cell V with the two resistors in parallel*

![drawn: Circuit (A): cell V with R0(1-αΔT) and R0(1+αΔT) in series; circuit (B): cell V with the two resistors in parallel](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q006_question_0847a3b7_03112026.svg?v=0847a3b7a281)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) both $I_A$ and $I_B$ remain constant
- **(2)** $I_A$ remains constant while $I_B$ increases
- (3) $I_A$ decreases while $I_B$ increases
- (4) $I_A$ increases while $I_B$ decreases

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Circuit (A) has the two resistors in series: $R_A = R_0(1-\alpha\Delta T) + R_0(1+\alpha\Delta T) = 2R_0$.
2. $R_A$ is independent of $\Delta T$, so $I_A = \frac{V}{2R_0}$ remains constant.
3. Circuit (B) has them in parallel: $R_B = \frac{R_0(1-\alpha\Delta T)\,R_0(1+\alpha\Delta T)}{2R_0} = \frac{R_0}{2}\left(1-\alpha^2\Delta T^2\right)$.
4. $R_B$ decreases as $\Delta T$ increases, so $I_B = \frac{V}{R_B}$ increases, which is option $2$.

**Subtopic:** Temperature Coefficient of Resistance, Combination of Resistors · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 2)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q006_7902d0e9_03112026.png?v=7902d0e9f6b4)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Two resistors with equal and opposite temperature coefficients add to a constant $2R_0$ in series, but combine in parallel to $R_0(1-\alpha^2\Delta T^2)/2$, which falls as the temperature rises
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The $+\alpha\Delta T$ and $-\alpha\Delta T$ really do cancel in the series circuit, and that cancellation is carried across to the parallel circuit, where the two factors multiply instead of adding.
- **Why:** This question requires the temperature law applied to a series and a parallel pair, demonstrated by the figure labelling $R_0(1-\alpha\Delta T)$ and $R_0(1+\alpha\Delta T)$ in series in (A) and the same two in parallel in (B).
- **Note:** E1 called this statement_options from the length of the options; each option is a conjunction about two circuits that must both hold, so the shape recorded here is two_part.
<!--/ecat-->

## Q7

Physics · Modern Physics

A beam of light falls on a metal surface such that photo-electrons are generated. If power of the light source starts to decrease linearly with time $t$, then variation of the photocurrent $I$ and magnitude of the stopping potential $|V|$ with time is best represented by :

- (1) ![printed figure: Option (1): photocurrent I constant with t, and |V| constant with t](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q007_option_1_f536bf6c_03112026.svg?v=f536bf6c22fd) *Option (1): photocurrent I constant with t, and |V| constant with t* ![drawn: Option (1): photocurrent I constant with t, and |V| constant with t](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q007_option_1_0fa3f8f3_04112026.svg?v=0fa3f8f3b43a)  
*drawn by code/lib/physics_figure.py*
- **(2)** ![printed figure: Two graphs vs time t: photocurrent I falls linearly to zero; stopping potential |V| stays constant](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q007_option_2_60b06ced_03112026.svg?v=60b06cedecbd) *Two graphs vs time t: photocurrent I falls linearly to zero; stopping potential |V| stays constant* ![drawn: Two graphs vs time t: photocurrent I falls linearly to zero; stopping potential |V| stays constant](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q007_option_2_b9443610_04112026.svg?v=b94436106dbd)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Option 3: photocurrent I falls linearly to zero with t, and stopping potential magnitude |V| also falls linearly to zero with t](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q007_option_3_dac7980b_03112026.svg?v=dac7980bcacc) *Option 3: photocurrent I falls linearly to zero with t, and stopping potential magnitude |V| also falls linearly to zero with t* ![drawn: Option 3: photocurrent I falls linearly to zero with t, and stopping potential magnitude |V| also falls linearly to zero with t](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q007_option_3_b7ea3f7e_04112026.svg?v=b7ea3f7ea4c0)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Option (4): photocurrent I constant with time t; magnitude of stopping potential |V| falling linearly to zero with t](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q007_option_4_e6ffc393_03112026.svg?v=e6ffc3931703) *Option (4): photocurrent I constant with time t; magnitude of stopping potential |V| falling linearly to zero with t* ![drawn: Option (4): photocurrent I constant with time t; magnitude of stopping potential |V| falling linearly to zero with t](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q007_option_4_09d32b5e_04112026.svg?v=09d32b5eb972)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. At fixed frequency, the number of photons per second is $n = \frac{P}{h\nu}$, so the photocurrent $I \propto P$.
2. $P(t) = P_0 - kt$ decreases linearly, so $I(t)$ decreases linearly with $t$.
3. Stopping potential obeys $e|V| = h\nu - \phi$, which does not depend on $P$, so $|V|$ stays constant.
4. Linearly falling $I$ with constant $|V|$ is the pair of graphs in option $2$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q007_2e8cc2c6_03112026.png?v=2e8cc2c60544)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The photocurrent follows the light's intensity, while the stopping potential is fixed by the frequency and does not move when the power falls
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and not one of them was supplied to this step, so no option could be inspected
- **Why:** This question requires the two photoelectric dependences applied to a source whose power falls with time, demonstrated by 'If power of the light source starts to decrease linearly with time $t$' being the only change the stem makes.
- **Note:** All four options arrive as empty strings because they are graphs; the shape is recorded as mcq since the qtype axis carries no graph value. A reviewer holding the printed panels should check the one in which $|V|$ also slopes down: the stopping potential depends on frequency alone, so the pairing 'I falls, |V| flat' is the answer and 'both fall' is the mechanism to confirm.
<!--/ecat-->

## Q8

Physics · Semiconductor Electronics

An ideal Zener diode with breakdown voltage of $-3\,\mathrm{V}$ is reverse biased with a negative input voltage $V_i = -5\,\mathrm{V}$. The magnitude of voltage difference between points B and A is :

![printed figure: Zener diode, resistor R and a cell in one loop, with points C, B, A on the top wire](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q008_992bd8db_03112026.svg?v=992bd8dbaa53)

*Zener diode, resistor R and a cell in one loop, with points C, B, A on the top wire*

![drawn: Zener diode, resistor R and a cell in one loop, with points C, B, A on the top wire](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q008_question_368490a9_04112026.svg?v=368490a92588)  
*drawn by code/lib/physics_figure.py*

- (1) $0\,\mathrm{V}$
- (2) $3\,\mathrm{V}$
- **(3)** $2\,\mathrm{V}$
- (4) $1\,\mathrm{V}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The Zener (C to B) and resistor $R$ (B to A) are in series across the source of magnitude $|V_i| = 5\,\mathrm{V}$.
2. Since $|V_i| = 5\,\mathrm{V} > |V_Z| = 3\,\mathrm{V}$, the reverse-biased ideal Zener is in breakdown, so $|V_{CB}| = 3\,\mathrm{V}$.
3. By KVL, $|V_{BA}| = |V_i| - |V_Z| = 5 - 3 = 2\,\mathrm{V}$, which is option $3$.

**Subtopic:** Zener Diode · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q008_1f32b00a_03112026.png?v=1f32b00a2382)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A Zener past breakdown holds its own voltage at the breakdown value, so the remainder of the supply appears across the series resistor
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  3 V is a true voltage in this circuit — it is what the Zener holds across C and B — but the stem asks for the drop between B and A, which is the $5-3=2$ V left for the resistor.
- **Why:** This question requires the supply split between a clamped diode and its series resistor, demonstrated by 'The magnitude of voltage difference between points B and A' with R drawn between exactly those two points.
<!--/ecat-->

## Q9

Physics · Mechanical Properties of Fluids

In the measurement of viscosity of liquids using terminal velocity experiment, spherical balls of same radius but having different densities are used. The variation of the terminal velocity ($v$) with the ratio of density of spherical ball ($\sigma$) to density of the liquid ($\rho$), is best represented by:

- (1) ![printed figure: Terminal velocity v against sigma/rho: zero up to 1, then a constant positive value](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q009_option_1_6a86e6d6_03112026.svg?v=6a86e6d6b271) *Terminal velocity v against sigma/rho: zero up to 1, then a constant positive value* ![drawn: Terminal velocity v against sigma/rho: zero up to 1, then a constant positive value](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q009_option_1_84ac18bc_04112026.svg?v=84ac18bc7369)  
*drawn by code/lib/physics_figure.py*
- **(2)** ![printed figure: Terminal velocity v against sigma/rho: zero up to 1, then rising linearly](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q009_option_2_0e343951_03112026.svg?v=0e3439517a8c) *Terminal velocity v against sigma/rho: zero up to 1, then rising linearly* ![drawn: Terminal velocity v against sigma/rho: zero up to 1, then rising linearly](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q009_option_2_cea54424_04112026.svg?v=cea5442475ff)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Graph of v against sigma/rho: a straight line through the origin, dotted up to sigma/rho = 1 and solid beyond it, with a dotted vertical at sigma/rho = 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q009_option_3_963e4296_03112026.svg?v=963e4296f0da) *Graph of v against sigma/rho: a straight line through the origin, dotted up to sigma/rho = 1 and solid beyond it, with a dotted vertical at sigma/rho = 1* ![drawn: Graph of v against sigma/rho: a straight line through the origin, dotted up to sigma/rho = 1 and solid beyond it, with a dotted vertical at sigma/rho = 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q009_option_3_ce810adb_04112026.svg?v=ce810adb50c9)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Terminal velocity v against sigma/rho: a straight line rising from a point beyond 1, dotted below and solid above sigma/rho = 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q009_option_4_8e470be8_03112026.svg?v=8e470be8bf7e) *Terminal velocity v against sigma/rho: a straight line rising from a point beyond 1, dotted below and solid above sigma/rho = 1* ![drawn: Terminal velocity v against sigma/rho: a straight line rising from a point beyond 1, dotted below and solid above sigma/rho = 1](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q009_option_4_e1135208_04112026.svg?v=e1135208537f)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. At terminal velocity, weight = buoyancy + viscous drag: $\frac{4}{3}\pi r^3 \sigma g = \frac{4}{3}\pi r^3 \rho g + 6\pi \eta r v$.
2. $v = \frac{2 r^2 (\sigma - \rho) g}{9\eta}$.
3. Rewrite in terms of the ratio: $v = \frac{2 r^2 \rho g}{9\eta}\left(\frac{\sigma}{\rho} - 1\right)$, with $r$, $\rho$, $\eta$ fixed.
4. So $v$ is a straight line in $\sigma/\rho$ with positive slope, $v = 0$ at $\sigma/\rho = 1$ (ball only falls for $\sigma/\rho > 1$).
5. The graph starting at $\sigma/\rho = 1$ from $v = 0$ and rising linearly is option $2$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q009_2bb71775_03112026.png?v=2bb71775576d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Terminal velocity in Stokes' law goes with $(\sigma-\rho)$, so against $\sigma/\rho$ it is a straight line that crosses zero at $\sigma/\rho=1$ rather than passing through the origin
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and not one of them was supplied to this step, so no option could be inspected
- **Why:** This question requires Stokes' law rewritten in the variable the axes use, demonstrated by 'The variation of the terminal velocity ($v$) with the ratio of density of spherical ball ($\sigma$) to density of the liquid ($\rho$)'.
- **Note:** All four options arrive as empty strings because they are graphs; the shape is recorded as mcq since the qtype axis carries no graph value. A reviewer holding the printed panels should check for a straight line through the origin: $v_t\propto(\sigma/\rho-1)$ has a negative intercept, so the through-the-origin panel is the one reached by dropping the buoyancy term $-\rho$ from $(\sigma-\rho)$.
<!--/ecat-->

## Q10

Physics · Gravitation

Two planets $P_1$ and $P_2$ with equal mass have radii $R_1$ and $R_2$, respectively, where $R_2=\frac{R_1}{2}$. The escape speeds of $P_1$ and $P_2$ are $v_1$ and $v_2$, respectively. Then $\frac{v_2}{v_1}$ is :

- (1) $2$
- (2) $\frac{1}{\sqrt{2}}$
- (3) $1$
- **(4)** $\sqrt{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Escape speed: $v = \sqrt{\frac{2GM}{R}}$.
2. With equal $M$: $\frac{v_2}{v_1} = \sqrt{\frac{R_1}{R_2}}$.
3. $R_2 = \frac{R_1}{2}$ gives $\frac{v_2}{v_1} = \sqrt{2}$, which is option $4$.

**Subtopic:** Escape Velocity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q010_6c53edae_03112026.png?v=6c53edae0c7f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Escape speed is $\sqrt{2GM/R}$, so at equal mass it rises as the radius shrinks, in proportion to $1/\sqrt{R}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The radius is correctly seen to decide the answer and then put on the wrong side of the root: reading $v\propto\sqrt{R}$ gives $\sqrt{R_2/R_1}=\frac{1}{\sqrt2}$ instead of $\sqrt{R_1/R_2}=\sqrt2$.
- **Why:** This question requires the factor by which escape speed changes when the radius is halved at fixed mass, demonstrated by 'where $R_2=\frac{R_1}{2}$' and the request for '$\frac{v_2}{v_1}$'.
<!--/ecat-->

## Q11

Physics · Alternating Current

An ac voltage $V = 220\sin(2\times10^{3}t)$ Volt is applied to a series LCR circuit. Then the current amplitude in this circuit is : (Given : $L = 10\,\mathrm{mH}$, $C = 25\,\mu\mathrm{F}$, $R = 100\,\Omega$)

- (1) $22.0\,\mathrm{A}$
- **(2)** $2.2\,\mathrm{A}$
- (3) $5.5\,\mathrm{A}$
- (4) $11.0\,\mathrm{A}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. From $V = 220\sin(2\times10^{3}t)$: $V_0 = 220\,\mathrm{V}$ and $\omega = 2\times10^{3}\,\mathrm{rad/s}$.
2. $X_L = \omega L = 2\times10^{3} \times 10\times10^{-3} = 20\,\Omega$.
3. $X_C = \frac{1}{\omega C} = \frac{1}{2\times10^{3} \times 25\times10^{-6}} = \frac{1}{0.05} = 20\,\Omega$.
4. $X_L = X_C$, so the circuit is at resonance: $Z = \sqrt{R^2 + (X_L - X_C)^2} = R = 100\,\Omega$.
5. $I_0 = \frac{V_0}{Z} = \frac{220}{100} = 2.2\,\mathrm{A}$, which is option $2$.

**Subtopic:** RLC Circuit, Resonance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q011_b0ba44f2_03112026.png?v=b0ba44f2d3f0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With $X_L=\omega L$ and $X_C=1/\omega C$ equal, the series circuit is at resonance and the impedance is the resistance alone
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Resonance is spotted correctly from $X_L=X_C=20\,\Omega$ and then the surviving 20 $\Omega$ is used as the impedance, giving $220/20=11$ A instead of $220/100=2.2$ A.
- **Why:** This question requires the current amplitude computed from the impedance of a series LCR circuit, demonstrated by 'the current amplitude in this circuit is' with $L$, $C$, $R$ and $\omega$ all supplied.
<!--/ecat-->

## Q12

Physics · Electromagnetic Induction

Two identical inductors are connected in two different configurations $P$ and $Q$, where a time varying current $I(t)$ is flowing, as shown in the figure. The induced emf between points $a$ and $b$ for configuration $P$ is $E_P$ and that for configuration $Q$ is $E_Q$. The ratio $E_P / E_Q$ is : [Neglect the effect of mutual inductance.]

![printed figure: Two identical inductors in series (P) and in parallel (Q) carrying I(t), with points a and b](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q012_62159ba7_03112026.svg?v=62159ba7f3b0)

*Two identical inductors in series (P) and in parallel (Q) carrying I(t), with points a and b*

![drawn: Two identical inductors in series (P) and in parallel (Q) carrying I(t), with points a and b](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q012_question_6fc146fe_04112026.svg?v=6fc146fe5ba0)  
*drawn by code/lib/physics_figure.py*

- **(1)** $2$
- (2) $1/4$
- (3) $1/2$
- (4) $1$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. From the figure, in $P$ the points $a$ and $b$ lie across only the upper inductor, which carries the full current $I(t)$.
2. $E_P = L\frac{dI}{dt}$.
3. In $Q$, $a$ and $b$ lie across the two identical inductors in parallel, so $L_{eq} = \frac{L \cdot L}{L+L} = \frac{L}{2}$, carrying total current $I(t)$.
4. $E_Q = \frac{L}{2}\frac{dI}{dt}$.
5. $\frac{E_P}{E_Q} = \frac{L}{L/2} = 2$, which is option $1$.

**Subtopic:** Coefficient of Self-Inductance of Two Coils in Series and Parallel · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 3)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q012_ae91fa49_03112026.png?v=ae91fa49fea1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Between $a$ and $b$ the series arrangement puts the whole current $I(t)$ through one inductor, while the parallel arrangement sends only $I/2$ through each, so the emf there is half as large
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The emf is written as $L\,dI/dt$ in both figures with the same $I(t)$, so the factor $\tfrac12$ from the current dividing between the two parallel inductors is never applied and the ratio comes out as 1 instead of 2.
- **Why:** This question requires the emf between two marked points in two wirings, demonstrated by '$a$ and $b$' being drawn across one inductor in (P) and across the parallel pair in (Q), with mutual inductance explicitly set aside.
<!--/ecat-->

## Q13

Physics · Capacitance

Three identical capacitors P, Q and S, each of the capacitance C, are connected to a battery of voltage V, as shown in the figure. If the energy stored in the capacitor P and total energy stored in the system are $U_p$ and $U_t$, respectively, then the ratio $U_p / U_t$ is :

![printed figure: Capacitors P and Q in series, that pair in parallel with S, all across a battery V](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q013_0f7cb109_03112026.svg?v=0f7cb10939c4)

*Capacitors P and Q in series, that pair in parallel with S, all across a battery V*

![drawn: Capacitors P and Q in series, that pair in parallel with S, all across a battery V](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q013_question_f3205eee_04112026.svg?v=f3205eee15f9)  
*drawn by code/lib/physics_figure.py*

- **(1)** $1/6$
- (2) $2/3$
- (3) $1/3$
- (4) $1/2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. From the figure, $P$ and $Q$ are in series, and that branch is in parallel with $S$ across the battery $V$.
2. Identical capacitors in series share the voltage equally, so $V_P = V_Q = \frac{V}{2}$.
3. $U_p = \frac{1}{2} C \left(\frac{V}{2}\right)^2 = \frac{CV^2}{8}$.
4. Energy in the $P$-$Q$ branch: $U_{PQ} = \frac{1}{2}\cdot\frac{C}{2} V^2 = \frac{CV^2}{4}$.
5. Energy in $S$: $U_S = \frac{1}{2} C V^2$.
6. $U_t = \frac{CV^2}{4} + \frac{CV^2}{2} = \frac{3CV^2}{4}$.
7. $\frac{U_p}{U_t} = \frac{CV^2/8}{3CV^2/4} = \frac{1}{6}$, which is option $1$.

**Subtopic:** Energy Stored in a Capacitor, Combination of Capacitors · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 3)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q013_5b236d6f_03112026.png?v=5b236d6fd406)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** P and Q in series each take half the battery voltage, so each stores a quarter of what the single parallel capacitor S stores and a sixth of the system's energy
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\frac13$ is a true share of the stored energy — it is what the whole P-and-Q branch holds — but the stem asks for P alone, which is half of that again.
- **Why:** This question requires one capacitor's energy as a fraction of the system's, demonstrated by 'the energy stored in the capacitor P and total energy stored in the system are $U_p$ and $U_t$' with P drawn in series with Q and the pair across S.
<!--/ecat-->

## Q14

Physics · Electromagnetic Induction

A conducting loop of finite resistance lies on the x - y plane. There is a constant magnetic field in the z direction. The area of the loop varies with time t, as $A = A_0(1 + \sin t)$ in appropriate units. The figure that correctly indicates the qualitative behaviour of the power P dissipated in the loop as a function of time is :

- (1) ![printed figure: Power P rising ever faster with time t from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q014_option_1_08834093_03112026.svg?v=08834093c7ed) *Power P rising ever faster with time t from the origin O* ![drawn: Power P rising ever faster with time t from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q014_option_1_0578c4bb_03112026.svg?v=0578c4bba8e2)  
*drawn on the booklet's geometry, checked against its figure spec*
- (2) ![printed figure: P versus t: two equal arches touching the t-axis, with P and an up arrow printed below O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q014_option_2_1e916cda_03112026.svg?v=1e916cda3ee5) *P versus t: two equal arches touching the t-axis, with P and an up arrow printed below O* ![drawn: P versus t: two equal arches touching the t-axis, with P and an up arrow printed below O](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q014_option_2_43cd9f7e_04112026.svg?v=43cd9f7e7737)  
*drawn by code/lib/physics_figure.py*
- **(3)** ![printed figure: P versus t: power falls from a finite value to zero with a cusp, then rises back symmetrically](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q014_option_3_d96071e7_03112026.svg?v=d96071e75ccc) *P versus t: power falls from a finite value to zero with a cusp, then rises back symmetrically* ![drawn: P versus t: power falls from a finite value to zero with a cusp, then rises back symmetrically](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q014_option_3_ec6b4409_04112026.svg?v=ec6b440998e4)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Graph of power P against time t: a horizontal straight line (constant P)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q014_option_4_3a899fc0_03112026.svg?v=3a899fc09048) *Graph of power P against time t: a horizontal straight line (constant P)* ![drawn: Graph of power P against time t: a horizontal straight line (constant P)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q014_option_4_bfec8950_03112026.svg?v=bfec895064dc)  
*drawn on the booklet's geometry, checked against its figure spec*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Flux through the loop: $\phi = B A = B A_0 (1 + \sin t)$.
2. Induced emf: $\varepsilon = -\frac{d\phi}{dt} = -B A_0 \cos t$.
3. Power dissipated: $P = \frac{\varepsilon^2}{R} = \frac{B^2 A_0^2}{R} \cos^2 t$.
4. At $t = 0$, $P = \frac{B^2 A_0^2}{R}$ (maximum, non-zero); at $t = \frac{\pi}{2}$, $P = 0$; then $P$ rises again, and $P \ge 0$ always.
5. Option $1$ (monotonic rise from 0) and option $4$ (constant) are wrong; option $2$ starts at $P = 0$ (that is $\sin^2 t$); option $3$ starts at a non-zero maximum and dips to zero, so the answer is option $3$.

**Subtopic:** Faraday's Law of Electromagnetic Induction, Calculate Thermal Energy Developed · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 4)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q014_0c53d966_03112026.png?v=0c53d96689d3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The emf follows $dA/dt\propto\cos t$, so the dissipated power goes as $\cos^2t$: never negative, and repeating twice as often as the area does
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and not one of them was supplied to this step, so no option could be inspected
- **Why:** This question requires Faraday's law and $P=e^2/R$ applied to a stated area variation, demonstrated by '$A = A_0(1 + \sin t)$' and the request for 'the qualitative behaviour of the power P dissipated in the loop as a function of time'.
- **Note:** All four options arrive as empty strings because they are graphs; the shape is recorded as mcq since the qtype axis carries no graph value. A reviewer holding the printed panels should check two things: a curve that dips below zero, which is the panel reached by plotting the emf $\cos t$ instead of the power, and a curve of period $2\pi$, which is the panel reached by plotting the area rather than its rate of change.
<!--/ecat-->

## Q15

Physics · Thermodynamics

In an adiabatic expansion, the temperature of one mole of an ideal monatomic gas ($\gamma = 5/3$) decreases from $60\,\mathrm{K}$ to $50\,\mathrm{K}$. The work done by the gas in the process is : (Take the universal gas constant as $R = 8.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$)

- (1) $166\,\mathrm{J}$
- (2) $41.5\,\mathrm{J}$
- (3) $83\,\mathrm{J}$
- **(4)** $124.5\,\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For an adiabatic process the work done by the gas is $W = \frac{nR(T_1 - T_2)}{\gamma - 1}$.
2. $\gamma - 1 = \frac{5}{3} - 1 = \frac{2}{3}$.
3. $nR(T_1 - T_2) = 1 \times 8.3 \times (60 - 50) = 83\,\mathrm{J}$.
4. $W = \frac{83}{2/3} = 124.5\,\mathrm{J}$, which is option $4$.

**Subtopic:** Adiabatic Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q015_49613fca_03112026.png?v=49613fca9268)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In an adiabatic change the work done by the gas equals the fall in internal energy, $nC_v\Delta T$, and for a monatomic gas $C_v=\tfrac32R$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The right structure $W=nC\Delta T$ is used with $R$ itself in place of the monatomic $C_v=\tfrac32R$, which gives $8.3\times10=83$ J instead of $124.5$ J.
- **Why:** This question requires the adiabatic work from the temperature fall and the monatomic capacity, demonstrated by 'the temperature of one mole of an ideal monatomic gas ($\gamma = 5/3$) decreases from $60\,\mathrm{K}$ to $50\,\mathrm{K}$'.
<!--/ecat-->

## Q16

Physics · Kinematics

Consider a particle moving along a straight line, whose position as a function of time is given by $s(t) = \alpha t^{2} - \beta t + \gamma$, where $\alpha = 1\,\mathrm{m\,s^{-2}}$, $\beta = 6\,\mathrm{m\,s^{-1}}$ and $\gamma = 5\,\mathrm{m}$. The average speed of the particle, in $\mathrm{m\,s^{-1}}$, from $t = 0$ to $t = 6\,\mathrm{s}$ is:

- (1) $0$
- (2) $12$
- (3) $6$
- **(4)** $3$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. With the given constants, $s(t) = t^{2} - 6t + 5$ (in m).
2. $v = \frac{ds}{dt} = 2t - 6$, which is zero at $t = 3\,\mathrm{s}$, so the particle reverses direction there.
3. $s(0) = 5\,\mathrm{m}$, $s(3) = 9 - 18 + 5 = -4\,\mathrm{m}$, $s(6) = 36 - 36 + 5 = 5\,\mathrm{m}$.
4. Distance $= |s(3) - s(0)| + |s(6) - s(3)| = 9 + 9 = 18\,\mathrm{m}$.
5. Average speed $= \frac{18\,\mathrm{m}}{6\,\mathrm{s}} = 3\,\mathrm{m\,s^{-1}}$, which is option $4$.

**Subtopic:** Average Speed · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 4)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q016_79d1dbdd_03112026.png?v=79d1dbdd5a7f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Average speed divides the path length by the time, so the 9 m travelled before the particle turns at $t=3$ s and the 9 m after it must be added, while average velocity would divide the displacement
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $s(0)=s(6)=5$ m, so the displacement is zero — which is the true average velocity, not the average speed the stem asks for.
- **Why:** This question requires the path length rather than the displacement, demonstrated by 'The average speed of the particle' over an interval whose endpoints both give $s=5\,\mathrm{m}$.
<!--/ecat-->

## Q17

Physics · Electromagnetic Waves

The following table presents the part of the electromagnetic spectrum and their corresponding major applications.

The **correct** option is :

| List-I | | List-II | |
|---|---|---|---|
| P | Microwave | I | For purifying the water |
| Q | UV rays | II | For warming the food |
| R | Gamma rays | III | For AM and FM communication systems |
| S | Radio wave | IV | For treating the Cancer cells |

- (1) P-II, Q-IV, R-III, S-I
- (2) P-I, Q-II, R-III, S-IV
- (3) P-I, Q-IV, R-II, S-III
- **(4)** P-II, Q-I, R-IV, S-III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Microwaves are used in microwave ovens for warming food, so $P \to II$.
2. UV rays kill microorganisms and are used in water purifiers, so $Q \to I$.
3. Gamma rays are used in radiotherapy to destroy cancer cells, so $R \to IV$.
4. Radio waves are used in AM and FM broadcast communication, so $S \to III$.
5. The match $P\text{-}II,\ Q\text{-}I,\ R\text{-}IV,\ S\text{-}III$ is option $4$.

**Subtopic:** Electromagnetic Spectrum · **Difficulty:** easy (4 steps)

**Printed in the booklet** (page 4)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q017_45992fa9_03112026.png?v=45992fa925bd)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each band of the electromagnetic spectrum carries its own taught application: microwaves warm food, UV sterilises water, gamma rays destroy cancer cells, radio waves carry AM and FM
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Option 1 keeps P-II, the one pairing the spectrum table ties to a household appliance, and then gives UV the cancer-cell line that the same table prints one band away, against gamma rays.
- **Why:** This question requires the application the spectrum table states for each named band, demonstrated by 'For AM and FM communication systems' having to be set against 'Radio wave' with no criterion printed from which it could be derived.
- **Note:** On the nearby_fact versus look_alike_term test: replacing 'UV rays' and 'Gamma rays' with two unlike words leaves the trap standing, because what carries the student is the application printed one row away in the same table, not any resemblance between the two names.
<!--/ecat-->

## Q18

Physics · Thermodynamics

An ideal gas is made of polyatomic molecules. Each of the molecules has three translational, three rotational and $f$ number of vibrational modes. If the ratio of heat capacities $\frac{C_p}{C_v}$ of the gas is $\frac{8}{7}$, then the value of $f$ is:

- (1) $1$
- **(2)** $4$
- (3) $3$
- (4) $2$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Each translational and rotational mode contributes 1 degree of freedom; each vibrational mode contributes 2 (kinetic and potential), so $F = 3 + 3 + 2f = 6 + 2f$.
2. For an ideal gas $\gamma = \frac{C_p}{C_v} = 1 + \frac{2}{F}$.
3. $1 + \frac{2}{F} = \frac{8}{7} \Rightarrow \frac{2}{F} = \frac{1}{7} \Rightarrow F = 14$.
4. $6 + 2f = 14 \Rightarrow f = 4$, which is option $2$.

**Subtopic:** Specific Heat Capacity of Monoatomic, Diatomic, and Polyatomic Gases · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q018_4ce62f6e_03112026.png?v=4ce62f6e8b09)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Each translational and rotational mode contributes $\tfrac12R$ to $C_v$ but each vibrational mode contributes a full $R$, so $C_v=(3+f)R$ and $\gamma=(4+f)/(3+f)$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked every mis-count the mode bookkeeping allows: counting each vibrational mode as $\tfrac12R$ gives $f=8$, dropping the rotational modes gives $f=5.5$, and dropping the $\tfrac12$ from every mode gives $f=0.5$ — none of these is printed. The three wrong options are the integers 1, 2 and 3 flanking the answer 4, each corresponding to a $\gamma$ the stem does not state.
- **Why:** This question requires the mode count inverted out of a stated heat-capacity ratio, demonstrated by 'If the ratio of heat capacities $\frac{C_p}{C_v}$ of the gas is $\frac{8}{7}$, then the value of $f$ is'.
- **Note:** The one wrong route this topic reliably produces — treating a vibrational mode like a translational one, worth $\tfrac12R$ — gives $f=8$, and the paper does not print it. That is why the verdict on this question is no_trap rather than a forced label on one of the flanking integers.
<!--/ecat-->

## Q19

Physics · Electrostatics

A unit positive point charge is taken slowly through an infinitesimally thin tube that is inside a charged dielectric sphere of radius $R$, having uniform positive charge density $\rho$, as shown in the figure. The initial and final positions of the charge are marked by $A$ and $B$ at distances $2R$ and $3R$ respectively, from the centre of the sphere. In this process, the magnitude of the total work done on the point charge is $\dfrac{\rho R^2}{n\epsilon_0}$. The value of $n$ is : $\epsilon_0$ is the permittivity of vacuum)

![printed figure: Charged dielectric sphere of radius R with a thin tube; unit charge moved from A (2R) to B (3R)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q019_9e3166d8_03112026.svg?v=9e3166d8c02a)

*Charged dielectric sphere of radius R with a thin tube; unit charge moved from A (2R) to B (3R)*

![drawn: Charged dielectric sphere of radius R with a thin tube; unit charge moved from A (2R) to B (3R)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q019_question_12e646e8_04112026.svg?v=12e646e8d07b)  
*drawn by code/lib/physics_figure.py*

- **(1)** $18$
- (2) $2$
- (3) $6$
- (4) $9$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The field is conservative, so the work depends only on the end points: $W = q(V_B - V_A)$ with $q = 1$.
2. Total charge of the sphere: $Q = \frac{4}{3}\pi R^3 \rho$.
3. Outside the sphere ($r \ge R$): $V(r) = \frac{Q}{4\pi\epsilon_0 r} = \frac{\rho R^3}{3\epsilon_0 r}$.
4. At $A$ ($r = 2R$): $V_A = \frac{\rho R^2}{6\epsilon_0}$.
5. At $B$ ($r = 3R$): $V_B = \frac{\rho R^2}{9\epsilon_0}$.
6. $|W| = |V_B - V_A| = \frac{\rho R^2}{\epsilon_0}\left(\frac{1}{6} - \frac{1}{9}\right) = \frac{\rho R^2}{18\epsilon_0}$.
7. So $n = 18$, which is option $1$.

**Subtopic:** Work Done by Electric Force · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 4)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q019_818b1b2a_03112026.png?v=818b1b2a43bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Outside a uniformly charged sphere $V=\rho R^3/3\epsilon_0 r$, and the work is the charge times the difference of the potentials at $3R$ and $2R$, not the potential at either point
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $\rho R^2/9\epsilon_0$ is a true quantity here — it is the potential at B, the point at $3R$ — but the work needs the difference between B and A, which is $\rho R^2/18\epsilon_0$.
- **Why:** This question requires the potential difference between two outside points of a uniformly charged sphere, demonstrated by 'the initial and final positions of the charge are marked by $A$ and $B$ at distances $2R$ and $3R$ respectively' with the answer asked as $n$ in $\frac{\rho R^2}{n\epsilon_0}$.
- **Note:** The stem carries an unmatched bracket in '$\epsilon_0$ is the permittivity of vacuum)'. It affects nothing in the physics, and the printed key 18 follows from the stem's own numbers, so the question is tagged as printed.
<!--/ecat-->

## Q20

Physics · Magnetic Effect of Electric Current

A current $I_0$ flows through a metallic circular loop of radius $r$ as shown in the figure. Resistance of the segment ABC is half of ADC. Magnitude of magnetic field at the center O of the loop is:

![printed figure: Current I0 enters a circular loop at A and leaves at C; arcs ABC and ADC, centre O, radius r](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q020_1772675e_03112026.svg?v=1772675e131e)

*Current I0 enters a circular loop at A and leaves at C; arcs ABC and ADC, centre O, radius r*

![drawn: Current I0 enters a circular loop at A and leaves at C; arcs ABC and ADC, centre O, radius r](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q020_question_d897f3e9_04112026.svg?v=d897f3e9d9cc)  
*drawn by code/lib/physics_figure.py*

- (1) $\dfrac{\mu_0 I_0}{2\pi r}$
- **(2)** $\dfrac{\mu_0 I_0}{12r}$
- (3) $\dfrac{\mu_0 I_0}{4r}$
- (4) $\dfrac{\mu_0 I_0}{2r}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A and C are diametrically opposite, so $ABC$ and $ADC$ are semicircles in parallel.
2. Since $R_{ABC} = \frac{1}{2}R_{ADC}$, current divides inversely: $I_{ABC} = \frac{2I_0}{3}$, $I_{ADC} = \frac{I_0}{3}$.
3. Field of a semicircular arc at its centre: $B = \frac{\mu_0 i}{4r}$.
4. The two arcs carry current in opposite senses about $O$, so their fields oppose: $B = \frac{\mu_0}{4r}\left(\frac{2I_0}{3} - \frac{I_0}{3}\right)$.
5. The straight leads lie along the line through $O$, so they contribute $0$.
6. $B = \frac{\mu_0 I_0}{12r}$, which is option $2$.

**Subtopic:** Magnetic Field Due to a Current Element, Biot–Savart Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 5)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q020_ae0721f7_03112026.png?v=ae0721f7fbde)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The current divides inversely as the two arc resistances, and the two semicircles carry it in opposite senses round the centre, so their fields subtract
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The split is done right, $\tfrac23I_0$ through ABC and $\tfrac13I_0$ through ADC, and the two arc fields are then added instead of opposed, which restores the full $\mu_0I_0/4r$ of a single semicircle.
- **Why:** This question requires the divided current and the opposing arc fields combined into one expression, demonstrated by 'Resistance of the segment ABC is half of ADC' with the current entering at A and leaving at C.
<!--/ecat-->

## Q21

Physics · Work, Energy and Power

Bob B of mass $m$ at rest is hanging vertically from the ceiling via a massless string of length $10\,\mathrm{m}$, as shown in the figure. Point mass A of mass $m$ travelling horizontally with speed $10\,\mathrm{ms^{-1}}$ hits bob B elastically. The bob B rises $h$ meter after the collision. Taking the acceleration due to gravity $g = 10\,\mathrm{ms^{-2}}$ and neglecting the size of the bob, the value of $h$ is :

![printed figure: Bob B hanging from the ceiling by a string; point mass A moving horizontally at 10 m/s towards B](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q021_42d13fe3_03112026.svg?v=42d13fe3a7c4)

*Bob B hanging from the ceiling by a string; point mass A moving horizontally at 10 m/s towards B*

![drawn: Bob B hanging from the ceiling by a string; point mass A moving horizontally at 10 m/s towards B](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q021_question_db3eb148_04112026.svg?v=db3eb148d6e5)  
*drawn by code/lib/physics_figure.py*

- (1) $2.5$
- (2) $8$
- (3) $7$
- **(4)** $5$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In a head-on elastic collision between equal masses with B at rest, velocities are exchanged, so $v_B = 10\,\mathrm{m\,s^{-1}}$.
2. Check whether B rises above the horizontal: $v_B^2 = 100 < 2gL = 2 \times 10 \times 10 = 200$, so B stops before the string becomes horizontal and the string stays taut.
3. Energy conservation: $\frac{1}{2} m v_B^2 = m g h$.
4. $h = \frac{v_B^2}{2g} = \frac{100}{20} = 5\,\mathrm{m}$, which is option $4$.

**Subtopic:** Problems on Elastic Collision · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q021_f2084e3e_03112026.png?v=f2084e3ee07e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Equal masses in a head-on elastic collision exchange velocities, so the bob leaves with the whole $10\,\mathrm{m\,s^{-1}}$ and rises $v^2/2g$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The collision is read as sharing the kinetic energy equally between the two equal masses, so the bob starts with half of $\tfrac12mv^2$ and rises $v^2/4g=2.5$ m instead of $v^2/2g=5$ m.
- **Why:** This question requires the elastic equal-mass handover followed by an energy balance, demonstrated by 'Point mass A of mass $m$ travelling horizontally with speed $10\,\mathrm{ms^{-1}}$ hits bob B elastically'.
<!--/ecat-->

## Q22

Physics · Electromagnetic Waves

An electromagnetic wave travelling in a lossless dielectric medium having a dielectric constant, $\varepsilon_r = 9$, has the electric field, $E_x = E_0 \sin(kz - 2\pi \times 10^6 t)\ \mathrm{V\,m^{-1}}$ where $E_0$ is the amplitude and $k$ is the wave vector. Among the following options, the incorrect choice is:

- (1) The direction of propagation of the electromagnetic wave is along $+z$
- (2) The speed of the electromagnetic wave inside the medium is $10^8\ \mathrm{m\,s^{-1}}$
- **(3)** The wavelength of the electromagnetic wave inside the medium is $300\ \mathrm{m}$
- **(4)** The magnetic field is given by the relation $B_y = \frac{B_0}{\nu} \sin(kz - 2\pi \times 10^6 t)$ where $\nu$ is the speed of the electromagnetic wave inside the medium

**Answer** — booklet: (3, 4) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The phase $kz - \omega t$ means the wave travels along $+z$, so option $1$ is correct.
2. With $\mu_r = 1$, $v = \frac{c}{\sqrt{\varepsilon_r}} = \frac{3\times 10^8}{\sqrt{9}} = 10^8\ \mathrm{m\,s^{-1}}$, so option $2$ is correct.
3. $\omega = 2\pi \times 10^6\ \mathrm{rad\,s^{-1}}$ gives $f = \frac{\omega}{2\pi} = 10^6\ \mathrm{Hz}$.
4. $\lambda = \frac{v}{f} = \frac{10^8}{10^6} = 100\ \mathrm{m} \neq 300\ \mathrm{m}$, so option $3$ is incorrect.
5. For $E$ along $x$ and propagation along $+z$, $B$ lies along $y$ with $B_y = \frac{E_0}{v}\sin(kz - \omega t)$, which option $4$ intends.
6. The incorrect choice is option $3$.

**Subtopic:** Plane Electromagnetic Waves · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 5)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q022_4b447047_03112026.png?v=4b447047d804)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Inside a dielectric the wave slows to $c/\sqrt{\varepsilon_r}$, and the wavelength that follows from the printed frequency is the one in the medium, not in vacuum
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The dielectric constant is passed over and the speed is taken as $3\times10^{8}\,\mathrm{m\,s^{-1}}$, which makes the true statement 'the speed inside the medium is $10^8\,\mathrm{m\,s^{-1}}$' look like the incorrect one.
- **Why:** This question requires four printed claims about a wave in a medium tested one by one, demonstrated by 'Among the following options, the incorrect choice is' with statements about direction, speed, wavelength and the magnetic field.
- **Note:** accepted_answers holds both 3 and 4, matching the printed 'Answer Key: 3, 4', so no trap or filler is written on either. Both are genuinely defective: 300 m is the vacuum wavelength while the medium's is 100 m, and option 4 writes $B_0/\nu$ where the amplitude relation needs $E_0/\nu$. Only options 1 and 2 are wrong options, which is why this rating accounts for two rather than three.
<!--/ecat-->

## Q23

Physics · Work, Energy and Power

A particle of mass $M$ moves along a horizontal x axis from $x = 0$ to $x = L$. The coefficient of kinetic friction varies as a function of x as $\mu_k(x) = \mu_0 - \alpha x$, where $\mu_0$, $\alpha$ are constants of appropriate dimensions, so that $\mu_k(L) = 0$. The total work done by the frictional force during the motion is $n\mu_0 MgL$, where $g$ is the acceleration due to gravity. The value of n is:

- **(1)** $\frac{1}{2}$
- (2) $3$
- (3) $1$
- (4) $\frac{1}{3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. From $\mu_k(L) = 0$: $\mu_0 - \alpha L = 0 \Rightarrow \alpha = \frac{\mu_0}{L}$.
2. Friction force magnitude at $x$: $f(x) = \mu_k(x) M g = (\mu_0 - \alpha x) M g$.
3. $|W| = \int_0^L (\mu_0 - \alpha x) M g\,dx = M g\left(\mu_0 L - \frac{\alpha L^2}{2}\right)$.
4. Substitute $\alpha = \frac{\mu_0}{L}$: $|W| = M g\left(\mu_0 L - \frac{\mu_0 L}{2}\right) = \frac{1}{2}\mu_0 M g L$.
5. So $n = \frac{1}{2}$ (in magnitude), which is option $1$.

**Subtopic:** Work Done by Variable Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q023_5f05ea74_03112026.png?v=5f05ea745d98)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A coefficient of friction falling linearly from $\mu_0$ to zero has average $\mu_0/2$, so the work against it over the length $L$ is half of $\mu_0MgL$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The constant-friction result $W=\mu MgL$ is used with the starting value $\mu_0$, which ignores that $\mu_k$ falls to zero by $x=L$ and gives $n=1$ instead of $\tfrac12$.
- **Why:** This question requires the work of a force that varies over the path, demonstrated by '$\mu_k(x) = \mu_0 - \alpha x$ ... so that $\mu_k(L) = 0$' with the answer asked as $n$ in $n\mu_0MgL$.
<!--/ecat-->

## Q24

Physics · Ray Optics

Consider three media $P$, $Q$ and $R$ with refractive indices $1$, $1.25$, and $1.5$, respectively. The medium $Q$ having a thickness of $5\,\mathrm{cm}$ is placed between extended media $P$ and $R$ as shown in the figure. An object $O$ is placed at the center of medium $Q$. If viewed from medium $P$ near the normal direction, the apparent depth of $O$ is $h_1$. For similar observation from medium $R$, the apparent depth is $h_2$. The value of $|h_1 - h_2|$, in cm, is:

![printed figure: Medium Q of thickness 5 cm between extended media P (above) and R (below, shaded), object O at the centre of Q](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q024_79cee90d_03112026.svg?v=79cee90d7267)

*Medium Q of thickness 5 cm between extended media P (above) and R (below, shaded), object O at the centre of Q*

![drawn: Medium Q of thickness 5 cm between extended media P (above) and R (below, shaded), object O at the centre of Q](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q024_question_9206e15f_04112026.svg?v=9206e15f3f1d)  
*drawn by code/lib/physics_figure.py*

- (1) $3$
- (2) $0$
- **(3)** $1$
- (4) $2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $O$ is at the centre of $Q$, so its real distance from each interface is $d = \frac{5}{2} = 2.5\,\mathrm{cm}$.
2. Viewed from $P$: $h_1 = d\,\frac{n_P}{n_Q} = 2.5 \times \frac{1}{1.25} = 2\,\mathrm{cm}$.
3. Viewed from $R$: $h_2 = d\,\frac{n_R}{n_Q} = 2.5 \times \frac{1.5}{1.25} = 3\,\mathrm{cm}$.
4. $|h_1 - h_2| = |2 - 3| = 1\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Apparent Depth · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 5)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q024_fb0fe5ef_03112026.png?v=fb0fe5efa0bd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Apparent depth is the real depth times the observer's refractive index over the object medium's, so the same 2.5 cm reads as 2 cm from $n=1$ and 3 cm from $n=1.5$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Apparent depth is carried as 'real depth divided by the index of the medium the object sits in', which leaves the observer's medium out, so both views give the same number and the difference comes out as zero.
- **Why:** This question requires two apparent depths of one object and their difference, demonstrated by 'If viewed from medium $P$ ... the apparent depth of $O$ is $h_1$. For similar observation from medium $R$, the apparent depth is $h_2$'.
<!--/ecat-->

## Q25

Physics · Electrostatics

Consider a fixed uniformly charged insulating sphere with radius $R$ and total charge $+Q$. A point charge $-q$ ($q << Q$) with mass $m$ is released from rest at a distance of $3R$ from the centre of the charged sphere. When the point charge reaches the surface of the sphere, its speed is : ($\epsilon_0$ is the permittivity of vacuum, neglect gravitational forces).

- (1) $\sqrt{\dfrac{Qq}{4\pi\epsilon_0 mR}}$
- (2) $\sqrt{\dfrac{3Qq}{4\pi\epsilon_0 mR}}$
- (3) $\sqrt{\dfrac{2Qq}{3\pi\epsilon_0 mR}}$
- **(4)** $\sqrt{\dfrac{Qq}{3\pi\epsilon_0 mR}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Outside the sphere the potential is $V(r) = \frac{Q}{4\pi\epsilon_0 r}$, so the charge $-q$ has potential energy $U(r) = -\frac{Qq}{4\pi\epsilon_0 r}$.
2. Energy conservation from $r=3R$ (at rest) to $r=R$: $\frac{1}{2}mv^2 = U(3R) - U(R) = \frac{Qq}{4\pi\epsilon_0}\left(\frac{1}{R} - \frac{1}{3R}\right)$.
3. $\frac{1}{2}mv^2 = \frac{Qq}{4\pi\epsilon_0}\cdot\frac{2}{3R} = \frac{Qq}{6\pi\epsilon_0 R}$.
4. $v^2 = \frac{Qq}{3\pi\epsilon_0 mR}$, so $v = \sqrt{\frac{Qq}{3\pi\epsilon_0 mR}}$, which is option $4$.

**Subtopic:** Electrostatic Potential Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q025_143f936f_03112026.png?v=143f936f6030)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The attraction does work $kQq\left(\frac1R-\frac1{3R}\right)$ on the released charge, and all of it appears as kinetic energy at the surface
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The two potential-energy terms are combined with the same sign, $\frac1R+\frac1{3R}=\frac{4}{3R}$ instead of $\frac{2}{3R}$, which doubles $v^2$ to $\frac{2Qq}{3\pi\epsilon_0 mR}$.
- **Why:** This question requires the work of the attraction between two stated radii turned into a speed, demonstrated by 'released from rest at a distance of $3R$ from the centre' and 'When the point charge reaches the surface of the sphere, its speed is'.
<!--/ecat-->

## Q26

Physics · Laws of Motion

A car travels on a circular racetrack of radius $50\,\mathrm{m}$, which is banked at an angle $\theta$. If the car travels at a speed $10\,\mathrm{m\,s^{-1}}$, then the wear and tear on its tyres is minimum. Taking the acceleration due to gravity to be $10\,\mathrm{m\,s^{-2}}$, the value of $\theta$ is:

- (1) $\tan^{-1}\left(2\sqrt{3}\right)$
- **(2)** $\tan^{-1}\left(\frac{1}{5}\right)$
- (3) $\tan^{-1}\left(\frac{2}{5}\right)$
- (4) $\tan^{-1}\left(\sqrt{3}/2\right)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Minimum wear and tear means the banking alone provides the centripetal force, so friction is zero.
2. With no friction, $N\cos\theta = mg$ and $N\sin\theta = \frac{mv^2}{r}$, giving $\tan\theta = \frac{v^2}{rg}$.
3. $\tan\theta = \frac{(10)^2}{50 \times 10} = \frac{100}{500} = \frac{1}{5}$.
4. $\theta = \tan^{-1}\left(\frac{1}{5}\right)$, which is option $2$.

**Subtopic:** Circular Turnings · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q026_03eaa1f4_03112026.png?v=03eaa1f4973d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Minimum wear means friction is not needed, so the bank alone turns the car and $\tan\theta=v^2/rg$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The three printed numbers are 50 m, $10\,\mathrm{m\,s^{-1}}$ and $10\,\mathrm{m\,s^{-2}}$, and $\tan\theta=v^2/rg=100/500=1/5$. No sum, product, quotient or square root of 50, 10 and 10 produces a $\sqrt3$, so options 1 and 4 have no arithmetic route at all; the remaining option is twice the computed ratio and reaching it means halving the 50 m that the stem calls a radius, which is a misreading of a printed word rather than a route a prepared student walks.
- **Why:** This question requires the banking angle for which no friction is needed, demonstrated by 'the wear and tear on its tyres is minimum' alongside the radius, speed and $g$.
- **Note:** Recorded as no_trap deliberately: on this stem the arithmetic is one line and the three wrong options are a surd pair that the printed numbers cannot generate plus a doubling with no source, so naming a trap would mean asserting a route the paper does not supply.
<!--/ecat-->

## Q27

Physics · Center of Mass

A frictionless circular wire of unit radius is fixed on the horizontal plane. Two point particles of unit mass start moving simultaneously from point $A\left(\theta=\frac{\pi}{2}\right)$ with identical uniform angular speeds in opposite directions, and meet again at point $B\left(\theta=\frac{-\pi}{2}\right)$. During this time, which of the following figures schematically represent the magnitude of the total linear momentum $P$ of the system, as a function of $\theta$ ?

![printed figure: Circular wire with points A (top) and B (bottom), two particles moving in opposite directions, angle theta from horizontal](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q027_07905112_03112026.svg?v=0790511269e1)

*Circular wire with points A (top) and B (bottom), two particles moving in opposite directions, angle theta from horizontal*

![drawn: Circular wire with points A (top) and B (bottom), two particles moving in opposite directions, angle theta from horizontal](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q027_question_4283f84f_04112026.svg?v=4283f84fe428)  
*drawn by code/lib/physics_figure.py*

- (1) ![printed figure: Graph of P against theta: a straight line falling from a maximum at pi/2 to zero at -pi/2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q027_option_1_d5596140_03112026.svg?v=d55961402280) *Graph of P against theta: a straight line falling from a maximum at pi/2 to zero at -pi/2* ![drawn: Graph of P against theta: a straight line falling from a maximum at pi/2 to zero at -pi/2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q027_option_1_7c4f3772_04112026.svg?v=7c4f3772f2f4)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Graph of P versus theta: a horizontal line (P constant) from pi/2 to -pi/2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q027_option_2_81f60033_03112026.svg?v=81f60033eaeb) *Graph of P versus theta: a horizontal line (P constant) from pi/2 to -pi/2* ![drawn: Graph of P versus theta: a horizontal line (P constant) from pi/2 to -pi/2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q027_option_2_9fc6bc83_04112026.svg?v=9fc6bc838aa6)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: Graph of P against θ: curve starting high at θ = π/2, falling to zero at a cusp in the middle, rising back to the same height at θ = −π/2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q027_option_3_f506d433_03112026.svg?v=f506d433ea8f) *Graph of P against θ: curve starting high at θ = π/2, falling to zero at a cusp in the middle, rising back to the same height at θ = −π/2* ![drawn: Graph of P against θ: curve starting high at θ = π/2, falling to zero at a cusp in the middle, rising back to the same height at θ = −π/2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q027_option_3_c438be24_04112026.svg?v=c438be24e304)  
*drawn by code/lib/physics_figure.py*
- **(4)** ![printed figure: Graph of P against theta: a single hump rising from zero at pi/2 and falling to zero at -pi/2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q027_option_4_3cd4e1ac_03112026.svg?v=3cd4e1acd25b) *Graph of P against theta: a single hump rising from zero at pi/2 and falling to zero at -pi/2* ![drawn: Graph of P against theta: a single hump rising from zero at pi/2 and falling to zero at -pi/2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q027_option_4_1fa1646d_04112026.svg?v=1fa1646d4fa2)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The particles stay symmetric about the vertical diameter: one at angle $\theta$, the other at $\pi-\theta$.
2. Velocity of the clockwise particle at $\theta$: $\vec v_1 = \omega(\sin\theta, -\cos\theta)$.
3. Velocity of the anticlockwise particle at $\pi-\theta$: $\vec v_2 = \omega(-\sin\theta, -\cos\theta)$.
4. Total momentum $\vec P = m(\vec v_1 + \vec v_2) = (0, -2m\omega\cos\theta)$, so $|P| = 2m\omega|\cos\theta|$.
5. As $\theta$ goes from $\frac{\pi}{2}$ to $-\frac{\pi}{2}$, $|P|$ rises from $0$ to its maximum $2m\omega$ at $\theta = 0$ and falls back to $0$, an arch shape, which is option $4$.

**Subtopic:** Problems on Velocity, Acceleration and Force of Center of Mass · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 6)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q027_9e1fed71_03112026.png?v=9e1fed718fcb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The two particles' velocities are mirror images, so the components across the axis of symmetry cancel and the total momentum is largest when both are at the horizontal and zero where they meet
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and not one of them was supplied to this step, so no option could be inspected
- **Why:** This question requires a vector sum tracked over a motion, demonstrated by 'identical uniform angular speeds in opposite directions' and the request for 'the magnitude of the total linear momentum $P$ of the system, as a function of $\theta$'.
- **Note:** All four options arrive as empty strings because they are graphs; the shape is recorded as mcq since the qtype axis carries no graph value. A reviewer holding the printed panels should check the curve that is zero at $\theta=0$ and maximal at $\theta=\pm\pi/2$: the total momentum is $2mu|\cos\theta|$, so it is maximal at the horizontal and zero at A and B, and the panel with the peaks and zeros interchanged is the mechanism to confirm.
<!--/ecat-->

## Q28

Physics · Semiconductor Electronics

Three identical p-n junction diodes $D_1, D_2$ and $D_3$ are connected across a battery as shown in the figure. If the width of the depletion regions of $D_1, D_2$ and $D_3$ are $W_1, W_2$ and $W_3$, respectively, then the correct option is:

![printed figure: Three diodes D1, D2, D3 with 1 kilo-ohm resistors connected across a 5 V battery](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q028_44b681bb_03112026.svg?v=44b681bb9d9f)

*Three diodes D1, D2, D3 with 1 kilo-ohm resistors connected across a 5 V battery*

![drawn: Three diodes D1, D2, D3 with 1 kilo-ohm resistors connected across a 5 V battery](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q028_question_192a6b37_04112026.svg?v=192a6b37ef92)  
*drawn by code/lib/physics_figure.py*

- (1) $W_2 > W_1 = W_3$
- (2) $W_1 > W_2 > W_3$
- (3) $W_3 = W_1 > W_2$
- **(4)** $W_3 > W_2 > W_1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The battery's long plate (positive) is on the left, so the left junction is at higher potential than the right junction.
2. $D_1$ points from left to right, so its anode is at the higher potential: forward biased, so $W_1$ is less than the unbiased width.
3. $D_3$ points from right to left, so its cathode is at the higher potential: reverse biased, so $W_3$ is greater than the unbiased width.
4. The branch with $D_2$ is broken (open gap), so no voltage acts on $D_2$: it is unbiased and $W_2$ keeps its equilibrium value.
5. Therefore $W_3 > W_2 > W_1$, which is option $4$.

**Subtopic:** PN Junction Diode Under Reverse Bias, PN Junction Diode Under Forward Bias · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 6)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q028_7ca02262_03112026.png?v=7ca02262b756)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Forward bias narrows a junction's depletion region, reverse bias widens it, and a junction with no applied voltage keeps its equilibrium width in between
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The bias rule is carried the wrong way round — forward bias taken to widen the depletion region and reverse bias to narrow it — which prints the correct order backwards, $W_1 > W_2 > W_3$ instead of $W_3 > W_2 > W_1$.
- **Why:** This question requires three depletion widths placed in order from the bias each diode sees, demonstrated by the figure putting $D_1$ and $D_3$ in opposite orientations across the 5 V supply and leaving $D_2$'s branch open.
<!--/ecat-->

## Q29

Physics · Ray Optics

The lens combination as shown in the figure, consists of two lenses, $\mathrm{L_1}$ and $\mathrm{L_2}$, of the focal lengths $+\,10\,\mathrm{cm}$ and $-\,10\,\mathrm{cm}$, respectively. The position of the image formed is :

![printed figure: Object O on the principal axis 30 cm left of convex lens L1, with concave lens L2 3 cm to its right](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q029_1ebcbbd1_03112026.svg?v=1ebcbbd1854d)

*Object O on the principal axis 30 cm left of convex lens L1, with concave lens L2 3 cm to its right*

![drawn: Object O on the principal axis 30 cm left of convex lens L1, with concave lens L2 3 cm to its right](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q029_question_5fe8250d_03112026.svg?v=5fe8250d2514)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $60\,\mathrm{cm}$ to the right of the concave lens
- (2) $20\,\mathrm{cm}$ to the left of the concave lens
- **(3)** $60\,\mathrm{cm}$ to the left of the concave lens
- (4) $30\,\mathrm{cm}$ to the right of the concave lens

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For $L_1$: $u_1 = -30\,\mathrm{cm}$, $f_1 = +10\,\mathrm{cm}$.
2. $\frac{1}{v_1} = \frac{1}{f_1} + \frac{1}{u_1} = \frac{1}{10} - \frac{1}{30} = \frac{1}{15}$, so $v_1 = +15\,\mathrm{cm}$ right of $L_1$.
3. $L_2$ is $3\,\mathrm{cm}$ right of $L_1$, so the image acts as a virtual object at $u_2 = 15 - 3 = +12\,\mathrm{cm}$.
4. $\frac{1}{v_2} = \frac{1}{f_2} + \frac{1}{u_2} = -\frac{1}{10} + \frac{1}{12} = -\frac{1}{60}$.
5. $v_2 = -60\,\mathrm{cm}$, i.e. $60\,\mathrm{cm}$ to the left of the concave lens, which is option $3$.

**Subtopic:** Lens Formula, Position of Equivalent Lens When Two Lenses are Separated by a Distance · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 6)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q029_79584891_03112026.png?v=79584891af2b)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The convex lens forms its image 15 cm behind it, which is 12 cm past the concave lens and so a virtual object for it, and the concave lens throws the final image 60 cm back to the object side
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The arithmetic reaches $v=-60$ cm and the minus sign is then read as a magnitude only, so the image is placed on the far side of the concave lens instead of on the side it actually falls.
- **Why:** This question requires two lens equations chained and the side of the final image named, demonstrated by the options pairing a distance with 'to the right' or 'to the left of the concave lens'.
<!--/ecat-->

## Q30

Physics · Rotational Motion

A solid sphere A of radius $R$ and mass $M$ is attached at a point to a smaller solid sphere B of radius $r < R$ and mass $m < M$. Assume that the line joining their centres lies along the horizontal. The moment of inertia of the system calculated about a vertical axis passing through the centre of A is $I_{A}$ and that calculated about a vertical axis passing through the centre of B is $I_{B}$. The difference $I_{A} - I_{B}$ is:

![printed figure: Sphere A touching smaller sphere B; vertical axis through centre of A (I_A) and through centre of B (I_B)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q030_c741dfe8_03112026.svg?v=c741dfe809cb)

*Sphere A touching smaller sphere B; vertical axis through centre of A (I_A) and through centre of B (I_B)*

![drawn: Sphere A touching smaller sphere B; vertical axis through centre of A (I_A) and through centre of B (I_B)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q030_question_564d1bfa_04112026.svg?v=564d1bfa32cb)  
*drawn by code/lib/physics_figure.py*

- (1) $0$
- (2) $(M - m)(R + r)^{2}$
- **(3)** $(m - M)(R + r)^{2}$
- (4) $(m - M)(R - r)^{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The spheres touch, so the distance between their centres is $d = R + r$.
2. About the axis through A: $I_A = \frac{2}{5}MR^2 + \frac{2}{5}mr^2 + m(R+r)^2$ (parallel-axis theorem for B).
3. About the axis through B: $I_B = \frac{2}{5}MR^2 + \frac{2}{5}mr^2 + M(R+r)^2$ (parallel-axis theorem for A).
4. $I_A - I_B = m(R+r)^2 - M(R+r)^2 = (m - M)(R+r)^2$, which is option $3$.

**Subtopic:** Parallel Axis and Perpendicular Axis Theorem · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q030_303febf9_03112026.png?v=303febf90021)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Each sphere's own $\tfrac25MR^2$ appears in both moments, so the two differ only in which mass is carried off the axis at the centre separation $R+r$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Both moments are built correctly and then subtracted the other way round, giving $(M-m)(R+r)^2$ — the positive version that fits the expectation that the big sphere's axis must give the bigger moment.
- **Why:** This question requires two parallel-axis calculations differenced in the printed order, demonstrated by 'The difference $I_{A} - I_{B}$ is' with both axes vertical and the centres joined horizontally.
<!--/ecat-->

## Q31

Physics · Modern Physics

Consider that an electron is revolving in an excited state of Hydrogen atom with velocity $\sqrt{25.6}\times 10^{5}\,\mathrm{m\,s^{-1}}$. The radius of the orbit is $x\times 10^{-9}\,\mathrm{m}$. The value of $x$ is : (Take the mass of electron to be $9\times 10^{-31}\,\mathrm{kg}$, charge of electron $= -1.6\times 10^{-19}\,\mathrm{C}$ and $\frac{1}{4\pi\epsilon_0} = 9\times 10^{9}\,\mathrm{N\,m^{2}\,C^{-2}}$ ]

- **(1)** 1
- (2) 4
- (3) 3
- (4) 2

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For circular motion of the electron, $\frac{mv^2}{r} = \frac{1}{4\pi\epsilon_0}\frac{e^2}{r^2}$.
2. Rearranging, $r = \frac{1}{4\pi\epsilon_0}\frac{e^2}{mv^2}$.
3. Numerator: $9\times10^{9} \times (1.6\times10^{-19})^2 = 9\times10^{9}\times 2.56\times10^{-38} = 2.304\times10^{-28}$.
4. Denominator: $mv^2 = 9\times10^{-31} \times 25.6\times10^{10} = 2.304\times10^{-19}$.
5. $r = \frac{2.304\times10^{-28}}{2.304\times10^{-19}} = 1\times10^{-9}\,\mathrm{m}$, so $x = 1$, which is option $1$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q031_14fa8ee3_03112026.png?v=14fa8ee3deff)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The Coulomb attraction supplies the centripetal force, so $r=ke^2/mv^2$ and the orbit radius follows from the speed alone
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The radius is found by equating the potential-energy magnitude $ke^2/r$ to the kinetic energy $\tfrac12mv^2$ instead of using the force balance, which doubles the radius to $2\times10^{-9}$ m and gives $x=2$.
- **Why:** This question requires the orbit radius from the orbital speed, demonstrated by 'an electron is revolving in an excited state of Hydrogen atom with velocity $\sqrt{25.6}\times 10^{5}\,\mathrm{m\,s^{-1}}$. The radius of the orbit is $x\times 10^{-9}\,\mathrm{m}$'.
- **Note:** With the rounded constants the stem supplies, the radius $1\times10^{-9}$ m is not $n^2a_0$ for any integer $n$, so the 'excited state' is not an actual Bohr level. The arithmetic the question asks for is unaffected and the printed key follows from it, so the question is tagged as printed.
<!--/ecat-->

## Q32

Physics · Thermodynamics

The mean free path of molecules in an ideal gas A is half that of another ideal gas B. The diameter of the spherical molecules of gas A is twice the diameter of the molecules of B. If number densities of the gases A and B are $n_A$ and $n_B$, respectively, then the correct option is :

- **(1)** $n_A = \frac{1}{2}n_B$
- (2) $n_A = n_B$
- (3) $n_A = 2n_B$
- (4) $n_A = \frac{1}{4}n_B$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Mean free path: $\lambda = \frac{1}{\sqrt{2}\,\pi d^2 n}$.
2. Ratio: $\frac{\lambda_A}{\lambda_B} = \frac{n_B d_B^2}{n_A d_A^2}$.
3. With $d_A = 2d_B$: $\frac{\lambda_A}{\lambda_B} = \frac{n_B}{4 n_A}$.
4. Given $\frac{\lambda_A}{\lambda_B} = \frac{1}{2}$: $\frac{n_B}{4n_A} = \frac{1}{2} \Rightarrow n_A = \frac{1}{2} n_B$, which is option $1$.

**Subtopic:** Mean Free Path, RMS, Average, and Most Probable Speed in Terms of Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q032_fd2f9b1a_03112026.png?v=fd2f9b1a9aa6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Mean free path goes as $1/(d^2n)$, so halving it while the diameter doubles forces the number density down by a factor 2
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The diameter is entered without its square, as $\lambda\propto1/(dn)$, so the doubled diameter accounts for the whole halving of $\lambda$ and the densities come out equal.
- **Why:** This question requires the density ratio that two stated changes force, demonstrated by 'The mean free path of molecules in an ideal gas A is half that of another ideal gas B' together with 'The diameter ... of gas A is twice the diameter of the molecules of B'.
<!--/ecat-->

## Q33

Physics · Oscillations

A cylindrical cork of uniform density floats in a liquid of density $\rho_1$. If the cork is depressed slightly and released, it oscillates harmonically with time period $T$. If the same cork floats in another liquid of density $\rho_2$, then the similar oscillation has time period $2T$. The value of $\rho_2/\rho_1$ is :

- **(1)** $\frac{1}{4}$
- (2) $4$
- (3) $2$
- (4) $\frac{1}{2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. For a depression $x$, the extra buoyant force is the restoring force: $F = -\rho A g x$.
2. So $k = \rho A g$ and $T = 2\pi\sqrt{\frac{m}{\rho A g}}$, giving $T \propto \frac{1}{\sqrt{\rho}}$ (same cork, so $m$ and $A$ are fixed).
3. $\frac{T_2}{T_1} = \sqrt{\frac{\rho_1}{\rho_2}} = 2$.
4. $\frac{\rho_2}{\rho_1} = \frac{1}{4}$, which is option $1$.

**Subtopic:** Calculate Time Period of SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q033_fdb3668d_03112026.png?v=fdb3668d328c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** A floating cork's period is $2\pi\sqrt{L\rho_{cork}/\rho_{liquid}g}$, so it goes as $1/\sqrt{\rho_{liquid}}$ and doubling it needs a liquid a quarter as dense
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The square-root dependence is used but read the wrong way up, as $T\propto\sqrt{\rho}$, so a doubled period is taken to need a liquid four times as dense.
- **Why:** This question requires the factor the liquid density must change by when the period doubles, demonstrated by 'the similar oscillation has time period $2T$' with the same cork in both liquids.
<!--/ecat-->

## Q34

Physics · Waves

For sound waves, if the number of nodes for the $5^{\mathrm{th}}$ harmonic of an open-ended pipe is $n$ and that for the $9^{\mathrm{th}}$ harmonic of the same pipe with one of its ends closed is $m$, the ratio $\frac{n}{m}$ is :

- (1) $\frac{3}{5}$
- (2) $\frac{5}{9}$
- (3) $\frac{9}{5}$
- **(4)** $1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For an open pipe the $p^{\text{th}}$ harmonic has $L = p\frac{\lambda}{2}$ with antinodes at both ends, giving $p$ nodes.
2. So for the $5^{\text{th}}$ harmonic of the open pipe, $n = 5$.
3. For a closed pipe $L = (2k-1)\frac{\lambda}{4}$, with a node at the closed end and an antinode at the open end, giving $k$ nodes.
4. The $9^{\text{th}}$ harmonic means $2k-1 = 9$, so $k = 5$ and $m = 5$.
5. $\frac{n}{m} = \frac{5}{5} = 1$, which is option $4$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q034_c2bbfbb8_03112026.png?v=c2bbfbb8a5c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An open pipe's $p$-th harmonic holds $p$ nodes, while a closed pipe's 9th harmonic is $9\lambda/4$ long and holds five, so both counts come out as 5
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The open pipe's rule 'nodes equal the harmonic number' is carried over to the closed pipe, so the counts are taken as 5 and 9 and the ratio becomes the ratio of the two printed harmonic numbers.
- **Why:** This question requires two node counts from two end conditions, demonstrated by 'the number of nodes for the $5^{\mathrm{th}}$ harmonic of an open-ended pipe is $n$ and that for the $9^{\mathrm{th}}$ harmonic of the same pipe with one of its ends closed is $m$'.
<!--/ecat-->

## Q35

Physics · Modern Physics

Consider the following nuclear reaction : $\mathrm{^{238}U \rightarrow {}^{234}Th + {}^{4}He}$ Take masses of $\mathrm{^{238}U}$, $\mathrm{^{234}Th}$ and $\mathrm{^{4}He}$ as $238.050\,\mathrm{u}$, $234.043\,\mathrm{u}$ and $4.003\,\mathrm{u}$, respectively. The Q value for the reaction, in keV, is : [Given : $1\,\mathrm{u} = 931.5\,\mathrm{MeV}\,c^{-2}$]

- (1) $3740$
- **(2)** $3726$
- (3) $3730$
- (4) $3736$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\Delta m = m_U - (m_{Th} + m_{He}) = 238.050 - (234.043 + 4.003)\,\mathrm{u}$.
2. $\Delta m = 238.050 - 238.046 = 0.004\,\mathrm{u}$.
3. $Q = \Delta m \times 931.5\,\mathrm{MeV/u} = 0.004 \times 931.5 = 3.726\,\mathrm{MeV}$.
4. $3.726\,\mathrm{MeV} = 3726\,\mathrm{keV}$, which is option $2$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q035_06ff4409_03112026.png?v=06ff44098418)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The Q value is the mass defect times the printed conversion: $0.004\,\mathrm{u}\times931.5\,\mathrm{MeV\,u^{-1}}=3.726\,\mathrm{MeV}$, which is 3726 keV
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  3.726 MeV is rounded to three figures as 3.73 MeV before the conversion to keV, and 3.73 MeV is the printed 3730.
- **Why:** This question requires a mass defect converted into an energy, demonstrated by the three printed masses and 'Given : $1\,\mathrm{u} = 931.5\,\mathrm{MeV}\,c^{-2}$' with the answer asked in keV.
<!--/ecat-->

## Q36

Physics · Ray Optics

Which of the following measurements require 'index correction' ?

- (1) Measurement of speed of sound using resonance tube
- (2) Measurement of resistance of a wire using meter bridge
- (3) Measurement of gravitational acceleration using simple pendulum
- **(4)** Measurement of focal length of lenses using optical bench

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. On an optical bench, the distance read from the uprights' scale differs from the true distance between the lens and the object/image pin; this difference is the index error, and the 'index correction' fixes it, so measuring focal length on an optical bench (option $4$) needs it.

**Subtopic:** Lens Formula · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 7)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q036_530e926c_03112026.png?v=530e926c0bd5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Index correction is the optical-bench adjustment for the gap between an index mark and the true position of a lens, mirror or pin
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The resonance-tube experiment is taught with an additive correction of its own, the end correction for the open end, so a student holding 'the resonance tube is the experiment with a correction' reaches for it here.
- **Why:** This question requires which named practical carries a stated correction, demonstrated by "Which of the following measurements require 'index correction' ?" with four experiments as options.
- **Note:** On the nearby_fact against look_alike_term test: swapping 'resonance tube' and 'optical bench' for two unlike words leaves the trap standing, because what carries the student is that the resonance-tube experiment is taught with a correction of its own, not any likeness between the two experiment names. E1 called this statement_options from the option length; the options are named measurements rather than claims to be judged, so the shape recorded is mcq.
<!--/ecat-->

## Q37

Physics · Gravitation

In a solar system, the time-period of revolution of a planet tracing a circular orbit of radius $R$ is proportional to:

- (1) $R^{3}$
- (2) $R^{1/2}$
- **(3)** $R^{3/2}$
- (4) $R^{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Gravity provides the centripetal force: $\frac{GMm}{R^2} = m\omega^2 R = m\frac{4\pi^2}{T^2}R$.
2. Rearranging gives $T^2 = \frac{4\pi^2}{GM}R^3$.
3. Hence $T \propto R^{3/2}$, which is option $3$.

**Subtopic:** Kepler's Law · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q037_83ab5efd_03112026.png?v=83ab5efd169f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Kepler's third law makes $T^2$ proportional to $R^3$, so the period itself goes as $R^{3/2}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The law is recalled correctly as $T^2\propto R^3$ and the square on the left is then left behind, so the $R^3$ is read off as the period's own dependence.
- **Why:** This question requires the power of $R$ that the period scales with, demonstrated by 'the time-period of revolution of a planet tracing a circular orbit of radius $R$ is proportional to'.
<!--/ecat-->

## Q38

Physics · Units and Measurements

Consider that $\sigma_s, k_B, b$ represent Stefan-Boltzmann constant, Boltzmann constant and Wien's displacement law constant, respectively. The dimension of $\sigma_s k_B^{-1} b$ is:

- (1) $[L^{-1}T^{-1}K^{-4}]$
- **(2)** $[L^{-1}T^{-1}K^{-2}]$
- (3) $[L^{-1}K^{-2}]$
- (4) $[L^{-1}T^{-1}K^{-3}]$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\sigma_s = \frac{P}{A T^4} \Rightarrow [\sigma_s] = \frac{[M L^2 T^{-3}]}{[L^2][K^4]} = [M T^{-3} K^{-4}]$.
2. $k_B = \frac{E}{T} \Rightarrow [k_B] = [M L^2 T^{-2} K^{-1}]$, so $[k_B^{-1}] = [M^{-1} L^{-2} T^{2} K]$.
3. $b = \lambda_m T \Rightarrow [b] = [L K]$.
4. $[\sigma_s k_B^{-1}] = [M T^{-3} K^{-4}][M^{-1} L^{-2} T^{2} K] = [L^{-2} T^{-1} K^{-3}]$.
5. $[\sigma_s k_B^{-1} b] = [L^{-2} T^{-1} K^{-3}][L K] = [L^{-1} T^{-1} K^{-2}]$, which is option $2$.

**Subtopic:** Dimensional Formulae · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 7)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q038_08e2f7f3_03112026.png?v=08e2f7f3adcc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The dimensions of a product of constants are got by adding the exponents of its parts, and Wien's constant carries a kelvin because it is defined by $\lambda_{max}T=b$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Wien's constant is recalled as "the wavelength at the peak" and entered as $[L]$, so the only kelvins left are $\sigma_s$'s $K^{-4}$ and the $K^{+1}$ from $k_B^{-1}$, which gives $K^{-3}$ instead of $K^{-2}$
- **Why:** This question requires the dimensional formulae of three named constants to be combined, demonstrated by the stem's "The dimension of $\sigma_s k_B^{-1} b$ is".
<!--/ecat-->

## Q39

Physics · Modern Physics

A ray of light with wavelength $\lambda$ is incident on three different photo-electric cells namely 1, 2 and 3. The threshold wavelength of these photo-electric cells are $\lambda_1$, $\lambda_2$ and $\lambda_3$, respectively and the magnitude of stopping potentials of these cells are $V_1$, $V_2$ and $V_3$, respectively. The relation between $\lambda$ and threshold wavelengths are $\lambda_1 < \lambda$, $\lambda_2 > \lambda$ and $\lambda_3 >> \lambda$. The correct option is:

- (1) $V_1 < V_2, V_3 = 0$
- **(2)** $V_1 = 0, V_2 < V_3$
- (3) $V_1 = 0, V_2 > V_3$
- (4) $V_1 > V_2, V_3 = 0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Photoemission happens only if $\lambda < \lambda_{th}$. For cell 1, $\lambda_1 < \lambda$, so there is no emission and $V_1 = 0$.
2. For cells 2 and 3, $eV_i = hc\left(\frac{1}{\lambda} - \frac{1}{\lambda_i}\right)$.
3. $\lambda_3 \gg \lambda$ and $\lambda_2 > \lambda$ (with $\lambda_3 > \lambda_2$), so $\frac{1}{\lambda_3} < \frac{1}{\lambda_2}$ and therefore $V_3 > V_2$.
4. $V_1 = 0,\ V_2 < V_3$, which is option $2$.

**Subtopic:** Photoelectric Effect · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 7)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q039_4e3556cf_03112026.png?v=4e3556cf0b09)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Photoemission needs the incident wavelength below the threshold wavelength, and since the work function is $hc/\lambda_0$, a longer threshold wavelength means a weaker hold and a larger stopping potential
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Cell 1 is correctly killed, and then the three cells are ranked on the threshold wavelengths themselves, $\lambda_3$ being much the largest and so read as the most tightly bound, which inverts the inequality
- **Why:** This question requires the photoelectric threshold condition and $eV=hc/\lambda-hc/\lambda_0$ applied to three cells, demonstrated by the stem printing "$\lambda_1 < \lambda$, $\lambda_2 > \lambda$ and $\lambda_3 >> \lambda$" and asking for the relation between $V_1$, $V_2$ and $V_3$.
<!--/ecat-->

## Q40

Physics · Units and Measurements

> ⚠ The booklet prints "Answer Key: Drop": NTA dropped this question and gave every candidate its marks, so it has no keyed answer.

One main scale division of a Vernier calliper is equal to $1\,\mathrm{mm}$ and the number of divisions on the Vernier scale is 10. When both the jaws touch each other, the Vernier scale shifts to the left of zero of the main scale in such a way that $4^{\mathrm{th}}$ Vernier division coincides with a division of the main scale. If this Vernier caliper measures the length of a wire to be $1\,\mathrm{cm}$, the actual length of the wire is:

- (1) $1.04\,\mathrm{cm}$
- (2) $0.60\,\mathrm{cm}$
- (3) $0.96\,\mathrm{cm}$
- (4) $1.00\,\mathrm{cm}$

**Answer** — booklet: (none) · independent solve: (1) · unchecked

**Solved independently** (answer withheld)

1. Least count $= \frac{1\,\mathrm{mm}}{10} = 0.1\,\mathrm{mm}$.
2. Vernier zero lies to the left of main-scale zero, so the zero error is negative.
3. Taking the coinciding division directly, zero error $= -4 \times 0.1\,\mathrm{mm} = -0.04\,\mathrm{cm}$.
4. Actual length $=$ measured $-$ zero error $= 1.00 - (-0.04) = 1.04\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 7)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q040_658eceb4_03112026.png?v=658eceb43f07)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A vernier's zero error is read from the coinciding division with the jaws shut and then taken off every reading, its sign set by which side of the main-scale zero the vernier zero sits on
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the answer line reads "Answer Key: Drop" and accepted_answers is empty, so no option can be named wrong by this step; I worked the zero error both conventional ways and they do not agree with each other, which is what the absent key leaves unsettled
- **Why:** This question requires a vernier zero-error correction applied to a measured reading, demonstrated by "the Vernier scale shifts to the left of zero of the main scale in such a way that $4^{\mathrm{th}}$ Vernier division coincides" and "the actual length of the wire is".
- **Note:** No trap is written because the paper's own answer line is "Drop" and the packet carries no accepted answer; I am not supplying one. For a reviewer: least count $=1\,\mathrm{mm}/10=0.1\,\mathrm{mm}$, and with the vernier zero to the LEFT of the main-scale zero and the 4th vernier division coinciding, the two conventions in circulation give zero error $-0.4\,\mathrm{mm}$ (correction $+0.04\,\mathrm{cm}$, actual length $1.04\,\mathrm{cm}$, option 1) and $-(10-4)\times0.1=-0.6\,\mathrm{mm}$ (correction $+0.06\,\mathrm{cm}$, actual length $1.06\,\mathrm{cm}$, which is not printed at all). Option 3 is the same $0.4\,\mathrm{mm}$ applied with the opposite sign and option 2 is $0.6$ read in cm instead of mm. That convention clash is the likely ground for the drop, so the rating carries verdict arguable_key rather than a trap.
<!--/ecat-->

## Q41

Physics · Electrostatics

A point charge $Q$ is placed inside a cavity within a solid isolated conducting sphere. Consider points A, B and C as shown in the figure, where the magnitudes of the electric fields are $E_A$, $E_B$ and $E_C$, respectively. The points B and C are at the same distance from the center of the solid sphere. The correct option is:

![printed figure: Conducting sphere with an off-centre cavity holding charge Q; point A in the cavity, points C and B outside on a line through the centre](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q041_da44cf41_03112026.svg?v=da44cf415a05)

*Conducting sphere with an off-centre cavity holding charge Q; point A in the cavity, points C and B outside on a line through the centre*

![drawn: Conducting sphere with an off-centre cavity holding charge Q; point A in the cavity, points C and B outside on a line through the centre](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q041_question_79a9ea52_04112026.svg?v=79a9ea520469)  
*drawn by code/lib/physics_figure.py*

- (1) $E_A \neq 0,\ E_B < E_C$
- (2) $E_A = 0,\ E_B = E_C$
- **(3)** $E_A \neq 0,\ E_B = E_C$
- (4) $E_A = 0,\ E_B > E_C$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Point A lies inside the cavity alongside $Q$, where the field due to $Q$ and the induced $-Q$ on the cavity wall does not vanish, so $E_A \neq 0$.
2. Charge $+Q$ is induced on the outer surface; the conductor shields the cavity, so this charge spreads uniformly over the outer sphere.
3. Outside the sphere $E = \frac{kQ}{r^2}$ measured from the centre; since $r_B = r_C$, $E_B = E_C$, which is option $3$.

**Subtopic:** Electrostatic Shielding · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 8)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q041_6e26a557_03112026.png?v=6e26a557ac0a)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A charge sitting in a conductor's cavity leaves the cavity field non-zero, while the charge it induces on the spherical outer surface spreads uniformly, so from outside the sphere the field is that of $Q$ at the centre
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The shielding result is held without its condition that the cavity be empty, so A, drawn in the hollow, is given a zero field even though the stem puts a point charge $Q$ inside that cavity
- **Why:** This question requires the cavity-field and outer-surface results for a charged conductor applied to the printed arrangement, demonstrated by "A point charge $Q$ is placed inside a cavity within a solid isolated conducting sphere" and "The points B and C are at the same distance from the center".
- **Note:** The figure spec places A at (262, 97), inside the cavity whose centre is (262, 117) with radius 42, and puts $Q$ at the cavity centre; that placement is what makes $E_A\neq0$ decidable. B and C lie outside the sphere on the dashed line through its centre.
<!--/ecat-->

## Q42

Physics · Modern Physics

In Geiger-Marsden experiment, the number of scattered $\alpha$-particles $N(\theta)$ is plotted as a function of scattering angle $\theta$. Which of the following options represents the correct plot?

- (1) ![printed figure: N(θ) on a log scale against θ from 0 to 180 degrees: a broad hump peaking near 90°](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q042_option_1_9cd7662d_03112026.svg?v=9cd7662de2c8) *N(θ) on a log scale against θ from 0 to 180 degrees: a broad hump peaking near 90°* ![drawn: N(θ) on a log scale against θ from 0 to 180 degrees: a broad hump peaking near 90°](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q042_option_1_8b8d7498_04112026.svg?v=8b8d74985a47)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Option (2): log-scale N(θ) rising as a straight line with scattering angle θ](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q042_option_2_98aa7e0e_03112026.svg?v=98aa7e0ef2e8) *Option (2): log-scale N(θ) rising as a straight line with scattering angle θ* ![drawn: Option (2): log-scale N(θ) rising as a straight line with scattering angle θ](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q042_option_2_b51de10e_04112026.svg?v=b51de10e7317)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: N(theta) on a log scale versus scattering angle theta: flat near 10^7 up to about 60 degrees, then falling to about 10^3 near 175 degrees](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q042_option_3_084cfca0_03112026.svg?v=084cfca0ecc5) *N(theta) on a log scale versus scattering angle theta: flat near 10^7 up to about 60 degrees, then falling to about 10^3 near 175 degrees* ![drawn: N(theta) on a log scale versus scattering angle theta: flat near 10^7 up to about 60 degrees, then falling to about 10^3 near 175 degrees](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q042_option_3_a5144a00_04112026.svg?v=a5144a00fe4a)  
*drawn by code/lib/physics_figure.py*
- **(4)** ![printed figure: N(θ) on a log scale against scattering angle θ: steep fall from 10^7 near 0° flattening to about 10^2 by 180°](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q042_option_4_35acc580_03112026.svg?v=35acc58024a6) *N(θ) on a log scale against scattering angle θ: steep fall from 10^7 near 0° flattening to about 10^2 by 180°* ![drawn: N(θ) on a log scale against scattering angle θ: steep fall from 10^7 near 0° flattening to about 10^2 by 180°](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q042_option_4_3bd8908c_04112026.svg?v=3bd8908c3a35)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Rutherford scattering formula: $N(\theta) \propto \frac{1}{\sin^4(\theta/2)}$.
2. As $\theta \to 0$, $\sin(\theta/2) \to 0$, so $N(\theta)$ is very large; most $\alpha$-particles pass almost undeflected.
3. $N(\theta)$ decreases monotonically with $\theta$; $\frac{N(10^\circ)}{N(180^\circ)} = \frac{1}{\sin^4 5^\circ} \approx 1.7\times 10^4$, and most of this fall happens at small angles, so the curve drops steeply then levels off.
4. Options 1 (peak at $90^\circ$) and 2 (increasing) are wrong; option 3 stays nearly flat at small angles, contrary to the formula; option 4 shows the steep fall and flat tail, so the answer is option $4$.

**Subtopic:** Alpha-Particle Scattering and Rutherford Nuclear Model of the Atom and Thomson's Model · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 8)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q042_32675442_03112026.png?v=32675442cb95)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** In alpha-particle scattering the count falls off steeply and without a bump as the scattering angle grows, going as $1/\sin^4(\theta/2)$, so only a tiny fraction is turned through large angles
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are plots and all four options_en values arrived empty, so no curve can be inspected and no wrong curve named
- **Why:** This question requires the observed angular distribution of a named experiment, demonstrated by "In Geiger-Marsden experiment, the number of scattered $\alpha$-particles $N(\theta)$ is plotted as a function of scattering angle $\theta$".
- **Note:** All four options are empty strings: this is a graph-option question whose option images did not reach this step. Under the codebook's third case (section 5.0) the paper itself is intact, so this is not recorded as source damage, and no trap is written. For a reviewer holding the plots: Rutherford's result is $N(\theta)\propto 1/\sin^4(\theta/2)$, a curve falling steeply and monotonically from small angles and flattening towards $\theta=180^\circ$; the options to check are any plot that rises with $\theta$, any that peaks at an intermediate angle (the Thomson-model expectation of small-angle-only scattering drawn as a hump), and any that falls linearly. E1 returned plain_mcq by its default rule; the shape the stem implies is four graph options, for which the current qtype list has no value, so mcq is recorded.
<!--/ecat-->

## Q43

Physics · Thermodynamics

One mole of an ideal monatomic gas undergoes a cyclic process as shown in the figure. The total heat supplied to the gas is :

![printed figure: Cyclic process abcd on a p-v diagram: rectangle between v = 2 and 5 m^3, p = 100 and 300 N/m^2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q043_696381fc_03112026.svg?v=696381fcd463)

*Cyclic process abcd on a p-v diagram: rectangle between v = 2 and 5 m^3, p = 100 and 300 N/m^2*

![drawn: Cyclic process abcd on a p-v diagram: rectangle between v = 2 and 5 m^3, p = 100 and 300 N/m^2](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q043_question_2f31d901_04112026.svg?v=2f31d901dac9)  
*drawn by code/lib/physics_figure.py*

- (1) $800\,\mathrm{J}$
- (2) $400\,\mathrm{J}$
- (3) $500\,\mathrm{J}$
- **(4)** $600\,\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For a complete cycle $\Delta U = 0$, so $Q_{net} = W_{net}$.
2. The cycle $a \to b \to c \to d \to a$ is clockwise on the $p$-$V$ diagram, so $W_{net}$ is positive and equals the enclosed area.
3. $W_{net} = (300 - 100)\,\mathrm{N\,m^{-2}} \times (5 - 2)\,\mathrm{m^3} = 200 \times 3 = 600\,\mathrm{J}$.
4. $Q_{net} = 600\,\mathrm{J}$, which is option $4$.

**Subtopic:** Polytropic Process and Cyclic Process · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 8)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q043_31b5d0c7_03112026.png?v=31b5d0c70b97)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Round a closed cycle the internal energy comes back to its starting value, so the heat supplied equals the net work, which is the area enclosed on the p-v diagram
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The pressure side of the rectangle is taken as a difference but the volume side as the single label printed at its left edge, so the area comes out $200\times2=400$ J instead of $200\times3=600$ J
- **Why:** This question requires the net work of a closed cycle read as the area of the loop and set equal to the heat, demonstrated by "undergoes a cyclic process as shown in the figure" and "The total heat supplied to the gas is".
- **Note:** The figure spec reads as the rectangle a(2, 300), b(5, 300), c(5, 100), d(2, 100) traversed a-b-c-d-a, with pressures in $\mathrm{N\,m^{-2}}$ and volumes in $\mathrm{m^3}$, so the area is $200\times3=600$ J and the key is consistent. "One mole of an ideal monatomic gas" is not used by the area route.
<!--/ecat-->

## Q44

Physics · Magnetic Effect of Electric Current

Two infinitely long parallel conducting wires $A$ and $B$ carry currents $I$ and $2I$, respectively, in the same direction. The wire $A$ has uniform mass per unit length $\lambda$ and lies on an insulated floor. The wire $B$ is kept fixed at a height $h$ above the floor. The minimum magnitude of $h$ so that the wire $A$ does not rise from the floor is :
[ $g$ is the acceleration due to gravity and $\mu_0$ is the permeability of free space.]

- (1) $\dfrac{4\mu_0 I^2}{\pi\lambda g}$
- (2) $\dfrac{\mu_0 I^2}{2\pi\lambda g}$
- **(3)** $\dfrac{\mu_0 I^2}{\pi\lambda g}$
- (4) $\dfrac{2\mu_0 I^2}{\pi\lambda g}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Currents in the same direction attract, so wire $B$ above pulls wire $A$ upward.
2. Force per unit length on $A$: $\frac{F}{L} = \frac{\mu_0 I (2I)}{2\pi h} = \frac{\mu_0 I^2}{\pi h}$.
3. Weight per unit length of $A$ is $\lambda g$; $A$ does not rise if $\frac{\mu_0 I^2}{\pi h} \le \lambda g$.
4. $h \ge \frac{\mu_0 I^2}{\pi \lambda g}$, so $h_{min} = \frac{\mu_0 I^2}{\pi \lambda g}$, which is option $3$.

**Subtopic:** Force Between Two Parallel Current-Carrying Conductors · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 8)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q044_56edf4fc_03112026.png?v=56edf4fc3c10)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Parallel currents in the same direction attract with $\mu_0 I_1 I_2/2\pi h$ per unit length, and the lower wire stays on the floor only while that upward pull is no bigger than its weight per unit length $\lambda g$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The parallel-wire force is recalled in its equal-current form $\mu_0 I^2/2\pi d$, so wire B's $2I$ never enters the numerator, and balancing against $\lambda g$ returns an $h$ half the right one
- **Why:** This question requires the force per unit length between unequal parallel currents balanced against weight per unit length, demonstrated by "carry currents $I$ and $2I$" and "The minimum magnitude of $h$ so that the wire $A$ does not rise from the floor".
<!--/ecat-->

## Q45

Physics · Oscillations

Consider a spring-mass simple harmonic oscillator in one dimension. The mass of the particle is $m$ kg and the spring constant is $k\,\mathrm{N\,m^{-1}}$. At a given instant, the extension of the spring is $x$ meter and the speed of the particle is $v\,\mathrm{m\,s^{-1}}$. On the $x-v$ plane, if the graph of $v$ as a function of $x$ is a circle, then the correct option is:

- (1) $k=\sqrt{m}$
- (2) $k=\dfrac{1}{m}$
- **(3)** $k=m$
- (4) $k=m^{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Total mechanical energy is conserved: $\frac{1}{2}kx^2 + \frac{1}{2}mv^2 = E$.
2. Multiply by 2: $kx^2 + mv^2 = 2E$, an ellipse in the $x$-$v$ plane.
3. A circle $x^2 + v^2 = r^2$ needs equal coefficients, so $k = m$ (numerically), which is option $3$.

**Subtopic:** Velocity in SHM · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 8)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q045_0ad75ed4_03112026.png?v=0ad75ed49897)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On the $x$-$v$ plane simple harmonic motion traces an ellipse with semi-axes $A$ and $\omega A$, so it closes into a circle only when $\omega=\sqrt{k/m}=1$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The circle condition is correctly reduced to $\omega=1$, and then the spring-mass frequency is recalled as $\sqrt{km}$ rather than $\sqrt{k/m}$, so the condition comes out as $km=1$
- **Why:** This question requires the simple-harmonic velocity-displacement relation imposed as a circle rather than an ellipse, demonstrated by "if the graph of $v$ as a function of $x$ is a circle, then the correct option is".
- **Note:** Inverting the ratio -- using $\sqrt{m/k}$ instead of $\sqrt{k/m}$, or dropping the root altogether -- still returns $k=m$, so every distractor here is reached only by misplacing the root or turning the ratio into a product.
<!--/ecat-->

## Q46

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Consider the following reaction, and choose the correct option.

![printed figure: toluene →(i. $\ce{CrO2Cl2}$, $\ce{CS2}$; ii. $\ce{H3O+}$) P](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q046_2e9dc87f_03112026.svg?v=2e9dc87fa612)

*toluene →[i. $\ce{CrO2Cl2}$, $\ce{CS2}$; ii. $\ce{H3O+}$] P*

![drawn: toluene →(i. $\ce{CrO2Cl2}$, $\ce{CS2}$; ii. $\ce{H3O+}$) P](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q046_question_c5dd8717_03112026.svg?v=c5dd87171041)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: toluene `Cc1ccccc1` ![toluene](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q046_question_s1_914ebbdb_03112026.svg?v=914ebbdb22ca)

- **(1)** Compound $\mathbf{P}$ is obtained by the hydrogenation of benzoyl chloride with $\mathrm{Pd}$ on $\mathrm{BaSO_4}$.
- (2) On treating compound $\mathbf{P}$ with saturated $\mathrm{NaHCO_3}$ solution, brisk effervescence is observed.
- (3) Compound $\mathbf{P}$ can be prepared by treating benzene with anhydrous $\mathrm{AlCl_3}$ and $\mathrm{CH_3COCl}$.
- (4) On treatment with bromine water, compound $\mathbf{P}$ gives a white precipitate.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Toluene with $\mathrm{CrO_2Cl_2}$ in $\mathrm{CS_2}$ followed by $\mathrm{H_3O^+}$ is the Etard reaction, giving benzaldehyde, so $\mathbf{P} = \mathrm{C_6H_5CHO}$.
2. Rosenmund reduction: $\mathrm{C_6H_5COCl} \xrightarrow{\mathrm{H_2,\ Pd/BaSO_4}} \mathrm{C_6H_5CHO}$, so option $1$ is correct.
3. Benzaldehyde is not acidic enough to liberate $\mathrm{CO_2}$ from $\mathrm{NaHCO_3}$, so option $2$ is false.
4. Friedel-Crafts acylation of benzene with $\mathrm{CH_3COCl}/\mathrm{AlCl_3}$ gives acetophenone, not benzaldehyde, so option $3$ is false.
5. The white precipitate with bromine water is the test for phenol (2,4,6-tribromophenol), not benzaldehyde, so option $4$ is false; the answer is option $1$.

**Subtopic:** Preparation of Benzaldehyde · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 9)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q046_ed831102_03112026.png?v=ed8311024382)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** The Etard reaction with $\mathrm{CrO_2Cl_2}$ in $\mathrm{CS_2}$ oxidises toluene's methyl group only as far as the aldehyde, so P is benzaldehyde, which the Rosenmund reduction of benzoyl chloride over $\mathrm{Pd/BaSO_4}$ also gives
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Reading $\mathrm{CrO_2Cl_2}$ as just another oxidising agent takes toluene all the way to benzoic acid, and effervescence with $\mathrm{NaHCO_3}$ is exactly what benzoic acid gives
- **Why:** This question requires the product of the printed reagent sequence and then a reaction claim about it, demonstrated by the scheme's 'i. $\mathrm{CrO_2Cl_2}$, $\mathrm{CS_2}$; ii. $\mathrm{H_3O^+}$' and by option 2 proposing the $\mathrm{NaHCO_3}$ test.
- **Note:** The figure's content is carried in the record as text and as a drawn scheme, so the stem was readable at this step; the product is printed only as the letter P.
<!--/ecat-->

## Q47

Chemistry · inorganic · Coordination Compounds – Practice

The formula of tetraammineaquachloridocobalt(III) chloride is

- **(1)** $\mathrm{[Co(NH_3)_4(H_2O)Cl]Cl_2}$
- (2) $\mathrm{[Co(NH_3)_4Cl_2]\times H_2O}$
- (3) $\mathrm{[Co(NH_3)_4]Cl_3\times H_2O}$
- (4) $\mathrm{[Co(NH_3)_4(H_2O)Cl]Cl}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The name lists the ligands inside the coordination sphere as tetraammine ($4\,\mathrm{NH_3}$), aqua ($\mathrm{H_2O}$) and chlorido ($\mathrm{Cl^-}$), with cobalt in the $+3$ state and chloride as the counter ion.
2. Charge on the complex ion: $+3 + 4(0) + 0 + (-1) = +2$, so the ion is $\mathrm{[Co(NH_3)_4(H_2O)Cl]^{2+}}$.
3. Two $\mathrm{Cl^-}$ counter ions balance it: $\mathrm{[Co(NH_3)_4(H_2O)Cl]Cl_2}$, which is option $1$.

**Subtopic:** IUPAC Nomenclature and Formulae of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q047_a6f1d17c_03112026.png?v=a6f1d17cc175)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The charge on a complex ion is the metal's oxidation state plus its ligands' charges, so cobalt(III) with four ammines, one aqua and one chlorido inside leaves a $2+$ ion needing two chlorides outside
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The coordination sphere is assembled correctly from the name and then the counter ion is copied from the word 'chloride' as a single Cl, leaving the charge unbalanced
- **Why:** This question requires the naming convention turned back into a formula, demonstrated by the name 'tetraammineaquachloridocobalt(III) chloride' carrying both a chlorido ligand and a chloride counter ion.
<!--/ecat-->

## Q48

Chemistry · inorganic · The D- and F-Block Elements – Practice

The lanthanide ion having four unpaired electrons is (Given: Atomic numbers of $\mathrm{Ce} = 58$, $\mathrm{Nd} = 60$, $\mathrm{Tb} = 65$ and $\mathrm{Ho} = 67$)

- **(1)** $\mathrm{Ho^{3+}}$
- (2) $\mathrm{Nd^{3+}}$
- (3) $\mathrm{Ce^{3+}}$
- (4) $\mathrm{Tb^{3+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. A $\mathrm{Ln^{3+}}$ ion has configuration $[\mathrm{Xe}]\,4f^{\,Z-57}$.
2. $\mathrm{Ce^{3+}}$ ($Z=58$): $4f^{1}$, so $1$ unpaired electron.
3. $\mathrm{Nd^{3+}}$ ($Z=60$): $4f^{3}$, so $3$ unpaired electrons.
4. $\mathrm{Tb^{3+}}$ ($Z=65$): $4f^{8}$, so $7-1 = 6$ unpaired electrons.
5. $\mathrm{Ho^{3+}}$ ($Z=67$): $4f^{10}$, so $14-10 = 4$ unpaired electrons.
6. Only $\mathrm{Ho^{3+}}$ has $4$ unpaired electrons, which is option $1$.

**Subtopic:** Electronic Configurations of the d-Block & f-Block · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 9)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q048_540d6a02_03112026.png?v=540d6a02379d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A tripositive lanthanide ion has $4f^{(Z-57)}$, and Hund's rule then fixes the unpaired count: $\mathrm{Ho^{3+}}$ is $4f^{10}$, which is three paired orbitals and four singly occupied ones
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Counting the f electrons of the neutral atom instead of the $3+$ ion makes neodymium $4f^4$, which is four unpaired electrons and looks like the answer the stem asked for
- **Why:** This question requires the f-electron count of a tripositive ion and Hund's rule applied to it, demonstrated by the stem supplying only atomic numbers and asking for 'The lanthanide ion having four unpaired electrons'.
- **Note:** asks is apply_rule rather than calculate because the answer is a named ion, with the electron count as the intermediate step.
<!--/ecat-->

## Q49

Chemistry · physical · Chemical Kinetics

For an elementary chemical reaction, the Arrhenius plot is given below. If the energy of activation is $6.64\,\mathrm{kJ\,mol^{-1}}$ and $\mathrm{R} = 8.3\,\mathrm{J\,K^{-1}\,mol^{-1}}$, the temperature at which the rate constant becomes $\mathrm{e}^{2}\,\mathrm{min^{-1}}$, is:

![printed figure: Arrhenius plot: graph of ln k (y-axis, marked 2, 4, 6, 8) against 1/T (x-axis); a straight line with negative slope starting at ln k = 6 on the y-axis and falling towards the x-axis](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q049_239f6829_03112026.svg?v=239f682921f5)

*Arrhenius plot: graph of ln k (y-axis, marked 2, 4, 6, 8) against 1/T (x-axis); a straight line with negative slope starting at ln k = 6 on the y-axis and falling towards the x-axis*

- (1) $250\,\mathrm{K}$
- (2) $125\,\mathrm{K}$
- (3) $150\,\mathrm{K}$
- **(4)** $200\,\mathrm{K}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The Arrhenius plot follows $\ln k = \ln A - \frac{E_a}{RT}$, so the intercept on the $\ln k$ axis is $\ln A = 6$.
2. For $k = e^{2}\,\mathrm{min^{-1}}$, $\ln k = 2$, so $2 = 6 - \frac{E_a}{RT}$.
3. $\frac{E_a}{RT} = 4$.
4. $T = \frac{E_a}{4R} = \frac{6640}{4 \times 8.3} = \frac{6640}{33.2} = 200\,\mathrm{K}$, which is option $4$.

**Subtopic:** Arrhenius Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q049_7bceb300_03112026.png?v=7bceb300d5bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On an Arrhenius plot of $\ln k$ against $1/T$ the intercept is $\ln A$ and the slope is $-E_a/R$, so the temperature at which $\ln k$ reaches a given value follows from the gap between that value and the intercept
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the routes the numbers allow. With $E_a/R = 6640/8.3 = 800\,\mathrm{K}$ and the intercept at $\ln A = 6$, the answer is $800/(6-2) = 200\,\mathrm{K}$. Dropping the intercept and writing $\ln k = -E_a/RT$ gives $400\,\mathrm{K}$; reading the intercept off the top axis mark as 8 gives $133\,\mathrm{K}$ and as 4 gives $400\,\mathrm{K}$; carrying the $2.303$ of the $\log$ form into the $\ln$ form gives $87\,\mathrm{K}$. The printed 250, 150 and 125 K would need gaps of 3.2, 5.33 and 6.4 in $\ln k$, and no reading of an axis marked 2, 4, 6, 8 supplies any of them, so no named wrong operation reaches a printed option
- **Why:** This question requires the intercept read off the plot and substituted into the Arrhenius equation, demonstrated by the stem giving '$E_a = 6.64\,\mathrm{kJ\,mol^{-1}}$' and asking for the temperature at which the rate constant becomes $\mathrm{e}^2\,\mathrm{min^{-1}}$.
- **Note:** The graph's content reached this step as text, including the intercept at $\ln k = 6$ and the axis marks 2, 4, 6, 8, so the arithmetic above could be checked against the printed options.
<!--/ecat-->

## Q50

Chemistry · inorganic · The D- and F-Block Elements – Practice

The green paramagnetic species formed by heating $\mathrm{KMnO_4}$ at $513\,\mathrm{K}$ is

- (1) $\mathrm{KO_2}$
- **(2)** $\mathrm{K_2MnO_4}$
- (3) $\mathrm{Mn_3O_4}$
- (4) $\mathrm{MnO}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. On heating at $513\,\mathrm{K}$: $2\mathrm{KMnO_4} \xrightarrow{513\,K} \mathrm{K_2MnO_4} + \mathrm{MnO_2} + \mathrm{O_2}$.
2. In $\mathrm{MnO_4^{2-}}$, Mn is $+6$ with configuration $3d^1$, so it has one unpaired electron and is paramagnetic.
3. $\mathrm{K_2MnO_4}$ (manganate) is green, so the green paramagnetic species is $\mathrm{K_2MnO_4}$, option $2$.

**Subtopic:** Potassium Permanganate (KMnO4) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q050_2cbf1b59_03112026.png?v=2cbf1b59b382)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Heating $\mathrm{KMnO_4}$ to 513 K decomposes it to potassium manganate, $\mathrm{K_2MnO_4}$, a green manganese(VI) species with one unpaired d electron, together with $\mathrm{MnO_2}$ and $\mathrm{O_2}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $\mathrm{KO_2}$ is the potassium-oxygen species taught as paramagnetic, so matching on the word 'paramagnetic' alone picks it, and the oxygen released in the decomposition seems to supply the formula
- **Why:** This question requires the product NCERT gives for the thermal decomposition of potassium permanganate, demonstrated by the stem fixing it as 'the green paramagnetic species formed by heating $\mathrm{KMnO_4}$ at 513 K'.
<!--/ecat-->

## Q51

Chemistry · organic · Hydrocarbons

Given below are two statements:
In the light of the above statements, choose the most appropriate answer from the options given below.

![printed figure: Newman projection of (2R,3R)-2,3-dibromobutane: front carbon Br (up), H (lower left), Me (lower right); rear carbon H (upper left), Me (upper right), Br (down)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q051_c54e9f4c_03112026.svg?v=c54e9f4c517c)

*Newman projection of (2R,3R)-2,3-dibromobutane: front carbon Br (up), H (lower left), Me (lower right); rear carbon H (upper left), Me (upper right), Br (down)*

![drawn: Newman projection of (2R,3R)-2,3-dibromobutane: front carbon Br (up), H (lower left), Me (lower right); rear carbon H (upper left), Me (upper right), Br (down)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q051_question_575fe822_03112026.svg?v=575fe8220a3e)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: (2R,3R)-2,3-dibromobutane `C[C@@H](Br)[C@@H](C)Br` ![(2R,3R)-2,3-dibromobutane](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q051_question_s1_1fce5fc4_03112026.svg?v=1fce5fc45d65)

- (Statement-I) \textit{trans}-But-2-ene upon treatment with $\mathrm{Br_2}$ in $\mathrm{CCl_4}$ gives the following product
- (Statement-II) \textit{cis}-But-2-ene upon treatment with alkaline $\mathrm{KMnO_4}$ gives the following product.

- **(1)** Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Anti addition of $\mathrm{Br_2}$ to \textit{trans}-but-2-ene gives meso-2,3-dibromobutane.
2. In the given Newman projection the front carbon has $\mathrm{Br}$ (up), $\mathrm{H}$ (lower left), $\mathrm{Me}$ (lower right); the back carbon has $\mathrm{Br}$ (down), $\mathrm{H}$ (upper left), $\mathrm{Me}$ (upper right).
3. With the two $\mathrm{Br}$ anti, the front $\mathrm{H}$ is anti to the back $\mathrm{Me}$, so the conformer has no centre of inversion; it is the chiral ($dl$) isomer, not meso.
4. Hence Statement I is incorrect.
5. Cold alkaline $\mathrm{KMnO_4}$ adds two $\mathrm{OH}$ groups syn; syn addition to \textit{cis}-but-2-ene gives meso-butane-2,3-diol, so Statement II (if it shows the meso diol) is correct.
6. Statement I incorrect, Statement II correct: option $1$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 9)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q051_67bced54_03112026.png?v=67bced54d91c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Bromine adds anti and alkaline permanganate adds syn, so the trans alkene gives the meso dibromide while the cis alkene gives the meso diol
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Both statements end 'gives the following product' and so are decided by two printed structures, but only one structure reached this step - a Newman projection of (2R,3R)-2,3-dibromobutane, which belongs to Statement I. Statement II's product was not supplied, so which verdict a student is drawn to cannot be settled from the record.
- **Why:** This question requires the stereochemical outcome of two named additions judged against drawn products, demonstrated by each statement ending in 'gives the following product' rather than naming one.
- **Note:** What a reviewer holding both figures should check: Statement I pairs trans-but-2-ene with a chiral (2R,3R) dibromide, whereas anti addition of bromine to the trans alkene gives the meso diastereomer, which is why the key marks Statement I incorrect; the route to the 'both correct' option would then be accepting the drawn dibromide without carrying anti addition through to meso. Statement II's product structure is absent from our record, so no trap is written. The record holds one figure for a stem that calls for two.
<!--/ecat-->

## Q52

Chemistry · organic · Haloalkanes and Haloarenes

One of the products formed in the following reaction is

![printed figure: cyclohexylmagnesium bromide + cyclohexanamine →](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q052_444220f2_03112026.svg?v=444220f24653)

*cyclohexylmagnesium bromide + cyclohexanamine →*

![drawn: cyclohexylmagnesium bromide + cyclohexanamine →](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_question_4d903bd8_04112026.svg?v=4d903bd879c3)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: cyclohexylmagnesium bromide `[Br][Mg][CH]1CCCCC1` ![cyclohexylmagnesium bromide](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_question_s1_d3eecdac_04112026.svg?v=d3eecdac0116); cyclohexanamine `NC1CCCCC1` ![cyclohexanamine](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_question_s2_98be994b_04112026.svg?v=98be994b2264)

- **(1)** cyclohexane `C1CCCCC1` ![cyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_option_1_s1_31f974b6_04112026.svg?v=31f974b63555)
- (2) N-cyclohexylcyclohexanamine `C1CCC(NC2CCCCC2)CC1` ![N-cyclohexylcyclohexanamine](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_option_2_s1_a8ab3d0b_04112026.svg?v=a8ab3d0bdbc9)
- (3) 2-cyclohexylcyclohexan-1-amine `NC1CCCCC1C1CCCCC1` ![2-cyclohexylcyclohexan-1-amine](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_option_3_s1_0b0abb1a_04112026.svg?v=0b0abb1a8d8f)
- (4) cyclohexylcyclohexane `C1CCC(C2CCCCC2)CC1` ![cyclohexylcyclohexane](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q052_option_4_s1_d7bf732b_04112026.svg?v=d7bf732b3773)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Grignard reagents are strong bases and react with compounds having acidic H, such as the $-NH_2$ hydrogen of an amine.
2. $C_6H_{11}MgBr + C_6H_{11}NH_2 \rightarrow C_6H_{12} + C_6H_{11}NHMgBr$.
3. The hydrocarbon product is cyclohexane, $C_6H_{12}$, which is option $1$.

**Subtopic:** Reactions of Haloalkanes with Metals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q052_23909b9f_03112026.png?v=23909b9f6029)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A Grignard reagent is a strong base and is destroyed by any acidic hydrogen, so with an amine's $\mathrm{N-H}$ it takes the proton and gives the alkane plus the magnesium amide
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings in this record and the scheme carries only the two reactants, so the product structures the question is answered from did not reach this step and no option's pull can be named
- **Why:** This question requires the product of a Grignard reagent meeting an acidic $\mathrm{N-H}$, demonstrated by the stem 'One of the products formed in the following reaction is' over a scheme of cyclohexylmagnesium bromide and cyclohexanamine.
- **Note:** The options for this question are empty in our record: the figure note says the arrow points to the options with no product drawn, and options_en holds four empty strings. For a reviewer holding the printed options, the mechanism to check is whether the drawn distractors include the coupled secondary amine, dicyclohexylamine, which is what a student gets by treating the Grignard carbon as a nucleophile toward nitrogen instead of as a base toward the $\mathrm{N-H}$ proton; the product the chemistry gives is cyclohexane with the magnesium amide.
<!--/ecat-->

## Q53

Chemistry · inorganic · The p–Block Elements

Given below are two statements:
In light of the above statements, choose the most appropriate answer from the options given below:

- (Statement-I) Heating $\mathrm{NaCl}$ with concentrated $\mathrm{H_2SO_4}$ and $\mathrm{MnO_2}$ results in oxidation of $\mathrm{Mn}$.
- (Statement-II) Heating $\mathrm{NaI}$ with concentrated $\mathrm{H_2SO_4}$ and $\mathrm{MnO_2}$ results in reduction of $\mathrm{Mn}$.

- **(1)** Statement-I is incorrect but Statement-II is correct.
- (2) Both Statement-I and Statement-II are correct.
- (3) Both Statement-I and Statement-II are incorrect.
- (4) Statement-I is correct but Statement-II is incorrect.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement-I: $4\mathrm{NaCl} + \mathrm{MnO_2} + 4\mathrm{H_2SO_4} \rightarrow \mathrm{MnCl_2} + 4\mathrm{NaHSO_4} + 2\mathrm{H_2O} + \mathrm{Cl_2}$.
2. Oxidation state of Mn changes from $+4$ in $\mathrm{MnO_2}$ to $+2$ in $\mathrm{MnCl_2}$, so Mn is reduced, not oxidised; Statement-I is incorrect.
3. Statement-II: $2\mathrm{NaI} + \mathrm{MnO_2} + 3\mathrm{H_2SO_4} \rightarrow 2\mathrm{NaHSO_4} + \mathrm{MnSO_4} + 2\mathrm{H_2O} + \mathrm{I_2}$.
4. Mn goes from $+4$ to $+2$ in $\mathrm{MnSO_4}$, so Mn is reduced; Statement-II is correct.
5. Statement-I incorrect, Statement-II correct, which is option $1$.

**Subtopic:** General Properties & Trends of Group 17 (Halogens) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q053_b26e0175_03112026.png?v=b26e01754a89)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** In both halide reactions manganese dioxide is the oxidising agent, so manganese itself falls from +4 to +2 and is reduced while the halide is oxidised
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  'Oxidation of Mn' is read as 'manganese does the oxidising', which makes Statement I read true and forces Statement II's 'reduction of Mn' to read false.
- **Why:** This question requires what two named halide reactions do to the manganese, demonstrated by the two statements differing only in the halide and in the words 'oxidation' and 'reduction'.
<!--/ecat-->

## Q54

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Among the following options, the correct trend in the electron gain enthalpy is

- (1) $\mathrm{I} > \mathrm{Br} > \mathrm{Cl} > \mathrm{F}$
- (2) $\mathrm{F} > \mathrm{Cl} > \mathrm{Br} > \mathrm{I}$
- (3) $\mathrm{Br} > \mathrm{Cl} > \mathrm{F} > \mathrm{I}$
- **(4)** $\mathrm{Cl} > \mathrm{F} > \mathrm{Br} > \mathrm{I}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Down group 17 the atomic size increases, so the added electron is held less strongly: $|\Delta_{eg}H|$ falls from Cl to Br to I.
2. F is an exception: its small, compact $2p$ subshell gives strong electron-electron repulsion, so $|\Delta_{eg}H|(\mathrm{F}) < |\Delta_{eg}H|(\mathrm{Cl})$ but still greater than Br.
3. Order of negative electron gain enthalpy: $\mathrm{Cl} > \mathrm{F} > \mathrm{Br} > \mathrm{I}$, which is option $4$.

**Subtopic:** Trends in Chemical Properties – Electron Gain Enthalpy · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 10)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q054_d197f68e_03112026.png?v=d197f68ef096)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Electron gain enthalpy is most negative for chlorine, not fluorine: the 2p shell of fluorine is so compact that the incoming electron is repelled by the ones already there, so the halogen order runs Cl > F > Br > I
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  F > Cl > Br > I is the true halogen order for electronegativity and the general down-a-group direction, so the order that every other halogen property follows is offered for the one property where fluorine is not first
- **Why:** This question requires the halogen order for one named property, demonstrated by the stem asking for 'the correct trend in the electron gain enthalpy' and by option 2 printing the order that holds for electronegativity.
- **Note:** E1 called this statement_options, which does not match the printed shape: the four options are symbolic orderings, not statements to be judged, so the shape recorded is mcq with asks: order. The printed orders compare magnitudes, since the enthalpies themselves are negative; the key is tagged as printed.
<!--/ecat-->

## Q55

Chemistry · inorganic · Coordination Compounds – Practice

Given below are two statements:
(Given : $\mathrm{oxH_2 = HOOC-COOH}$)
In light of the above statements, choose the most appropriate answer from the options given below:

- (Statement-I) $\mathrm{[Fe(ox)_3]^{3-}}$ is chiral.
- (Statement-II) trans-$\mathrm{[Cr(H_2O)_2(ox)_2]^{-}}$ is chiral.

- (1) Statement-I is incorrect but Statement-II is correct.
- (2) Both Statement-I and Statement-II are correct.
- (3) Both Statement-I and Statement-II are incorrect.
- **(4)** Statement-I is correct but Statement-II is incorrect.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. $\mathrm{[Fe(ox)_3]^{3-}}$ is an octahedral $\mathrm{[M(AA)_3]}$ complex with three bidentate oxalate ligands; it has no plane or centre of symmetry, so it exists as $\Delta$ and $\Lambda$ enantiomers and is chiral: Statement-I is correct.
2. In trans-$\mathrm{[Cr(H_2O)_2(ox)_2]^{-}}$ the two oxalates lie in the equatorial plane and the two $\mathrm{H_2O}$ are axial; that equatorial plane is a mirror plane, so the complex is achiral: Statement-II is incorrect.
3. Statement-I correct and Statement-II incorrect is option $4$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q055_6b05a1a4_03112026.png?v=6b05a1a4011e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A complex is chiral only if no plane of symmetry can be found: three bidentate ligands make a propeller with none, while the trans arrangement of two keeps one
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The printed 'trans' is passed over and the statement is graded as the taught claim about the cis bis(oxalato) complex, which is chiral, so both statements read as correct.
- **Why:** This question requires the symmetry test for chirality applied to two named complexes, demonstrated by Statement II printing 'trans-' in front of the complex whose cis form is the taught chiral example.
<!--/ecat-->

## Q56

Chemistry · organic · Biomolecules

The correct statement about peptides and proteins is

- (1) In $\alpha$-helices, the polypeptide chain is twisted into a left-handed screw (helix) through intramolecular hydrogen bonds.
- (2) Tertiary structure of proteins has two or more polypeptide subunits.
- (3) Only the proteins having a quaternary structure are biologically active.
- **(4)** In $\beta$-pleated sheet structures, peptide chains are held together by intermolecular hydrogen bonds.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option $1$: an $\alpha$-helix is a right-handed screw held by intramolecular H-bonds, so 'left-handed' makes it false.
2. Option $2$: an arrangement of two or more polypeptide subunits is quaternary structure, not tertiary, so it is false.
3. Option $3$: proteins with only tertiary structure (e.g. monomeric enzymes, myoglobin) are biologically active, so 'only' makes it false.
4. Option $4$: in $\beta$-pleated sheets the chains are stretched out side by side and held together by intermolecular H-bonds, so it is true; the answer is option $4$.

**Subtopic:** Proteins Classification and Structure · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q056_81aa5c4d_03112026.png?v=81aa5c4d2580)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The alpha-helix is a right-handed coil held by intramolecular hydrogen bonds; the beta-pleated sheet is stretched chains laid side by side and held by intermolecular hydrogen bonds; two or more subunits is the quaternary level
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Every clause of this sentence is the textbook description of the alpha-helix except the screw sense, which is printed left-handed instead of right-handed, so a student who checks it for the bond type passes it
- **Why:** This question requires one whole claim about protein structure graded as correct, demonstrated by option 4 reading 'In beta-pleated sheet structures, peptide chains are held together by intermolecular hydrogen bonds'.
<!--/ecat-->

## Q57

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Given below are two statements:
Statement-I: Oxidation of $p$-nitrotoluene with acidic $\mathrm{KMnO_4}$ gives an acid that is stronger than benzoic acid.
Statement-II: Reduction of $p$-nitrotoluene with $\mathrm{Sn/HCl}$ followed by neutralization gives an amine that is more basic than aniline.
In light of the above statements, choose the most appropriate answer from the options given below.

- (Statement-I) Oxidation of $p$-nitrotoluene with acidic $\mathrm{KMnO_4}$ gives an acid that is stronger than benzoic acid.
- (Statement-II) Reduction of $p$-nitrotoluene with $\mathrm{Sn/HCl}$ followed by neutralization gives an amine that is more basic than aniline.

- (1) Statement-I is incorrect but Statement-II is correct.
- **(2)** Both Statement-I and Statement-II are correct.
- (3) Both Statement-I and Statement-II are incorrect.
- (4) Statement-I is correct but Statement-II is incorrect.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Acidic $\mathrm{KMnO_4}$ oxidises the $-\mathrm{CH_3}$ of $p$-nitrotoluene to $-\mathrm{COOH}$, giving $p$-nitrobenzoic acid.
2. The $-\mathrm{NO_2}$ group withdraws electrons ($-I$, $-R$) and stabilises the carboxylate ion, so $p$-nitrobenzoic acid is stronger than benzoic acid; Statement-I is correct.
3. $\mathrm{Sn/HCl}$ followed by neutralisation reduces $-\mathrm{NO_2}$ to $-\mathrm{NH_2}$, giving $p$-toluidine ($p$-methylaniline).
4. The $-\mathrm{CH_3}$ group donates electrons ($+I$, hyperconjugation), raising electron density on N, so $p$-toluidine is more basic than aniline; Statement-II is correct.
5. Both statements are correct, which is option $2$.

**Subtopic:** Acidity of Carboxylic Acids · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q057_900efd10_03112026.png?v=900efd106a57)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Substituent effects push in opposite directions on the two properties: the nitro group withdraws electrons and strengthens the acid, the methyl group releases them and strengthens the base
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The acid half is settled on the securely held rule that an electron-withdrawing group strengthens an acid, and then the amine half is decided by the rule that a ring drains the nitrogen's lone pair, so a methyl substituent is read as lowering basicity too.
- **Why:** This question requires each product ranked against a reference compound, demonstrated by the statements asking for 'an acid that is stronger than benzoic acid' and 'an amine that is more basic than aniline'.
<!--/ecat-->

## Q58

Chemistry · organic · Amines

Identify the reactions which give aniline as the major product. Choose the correct answer form the options given below.

![printed figure: A. benzonitrile →($\ce{LiAlH4}$); B. benzamide →($\ce{KOH, Br2}$); C. nitrobenzene →($\ce{NaBH4}$); D. N-phenylacetamide →($\ce{HCl, H2O}$, Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q058_6a77f732_03112026.svg?v=6a77f732244d)

*A. benzonitrile →[$\ce{LiAlH4}$]; B. benzamide →[$\ce{KOH, Br2}$]; C. nitrobenzene →[$\ce{NaBH4}$]; D. N-phenylacetamide →[$\ce{HCl, H2O}$, Δ]*

![drawn: A. benzonitrile →($\ce{LiAlH4}$); B. benzamide →($\ce{KOH, Br2}$); C. nitrobenzene →($\ce{NaBH4}$); D. N-phenylacetamide →($\ce{HCl, H2O}$, Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q058_question_e443fcc6_03112026.svg?v=e443fcc60c2f)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: benzonitrile `N#Cc1ccccc1` ![benzonitrile](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q058_question_s1_1777697e_03112026.svg?v=1777697e1e3f); benzamide `NC(=O)c1ccccc1` ![benzamide](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q058_question_s2_6abc9e41_03112026.svg?v=6abc9e4164b1); nitrobenzene `O=[N+]([O-])c1ccccc1` ![nitrobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q058_question_s3_78028cdf_03112026.svg?v=78028cdf28d0); N-phenylacetamide `CC(=O)[N]c1ccccc1` ![N-phenylacetamide](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q058_question_s4_d139fd94_03112026.svg?v=d139fd949c4b)

- (A) [structure: benzene ring with $\mathrm{CN}$] $\xrightarrow{\mathrm{LiAlH_4}}$
- (B) [structure: benzene ring with $\mathrm{C(=O)NH_2}$] $\xrightarrow{\mathrm{KOH,\ Br_2}}$
- (C) [structure: benzene ring with $\mathrm{NO_2}$] $\xrightarrow{\mathrm{NaBH_4}}$
- (D) [structure: benzene ring with $\mathrm{NH{-}C(=O){-}CH_3}$] $\xrightarrow[\Delta]{\mathrm{HCl,\ H_2O}}$

- (1) C and D only
- (2) A and B only
- **(3)** B and D only
- (4) A and C only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A: $\mathrm{C_6H_5CN} \xrightarrow{\mathrm{LiAlH_4}} \mathrm{C_6H_5CH_2NH_2}$ (benzylamine), not aniline.
2. B: Hofmann bromamide degradation, $\mathrm{C_6H_5CONH_2} \xrightarrow{\mathrm{Br_2,\ KOH}} \mathrm{C_6H_5NH_2}$ (aniline, one carbon fewer).
3. C: $\mathrm{NaBH_4}$ does not reduce an aromatic $\mathrm{-NO_2}$ group to $\mathrm{-NH_2}$, so aniline is not the major product.
4. D: Acid hydrolysis of the amide, $\mathrm{C_6H_5NHCOCH_3} \xrightarrow[\Delta]{\mathrm{HCl,\ H_2O}} \mathrm{C_6H_5NH_2} + \mathrm{CH_3COOH}$ (aniline).
5. So B and D only give aniline, which is option $3$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 10)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q058_1ede9781_03112026.png?v=1ede97816b55)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Aniline comes from benzamide by Hofmann bromamide degradation and from acetanilide by hydrolysis; reducing benzonitrile lengthens the chain and sodium borohydride cannot touch a nitro group
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Nitrobenzene is the standard starting material for aniline, so reaction C is accepted on the substrate alone and the printed reagent, $\mathrm{NaBH_4}$, is never tested against the job.
- **Why:** This question requires the product of each printed step identified before the subset can be chosen, demonstrated by the four lettered items giving only a substrate and a reagent, such as 'nitrobenzene with NaBH4'.
- **Note:** The four lettered reactions were supplied as a transcription naming benzonitrile, benzamide, nitrobenzene and N-phenylacetamide with their reagents; no products are drawn in the record.
<!--/ecat-->

## Q59

Chemistry · physical · Thermodynamics

Two moles of an ideal gas undergo free expansion from $10\,\mathrm{L}$ to $100\,\mathrm{L}$ at $300\,\mathrm{K}$. The values of $\Delta S_{\mathrm{system}}$ and $\Delta S_{\mathrm{surroundings}}$ are (R is universal gas constant)

- **(1)** $\Delta S_{\mathrm{system}} = 4.606R$ ; $\Delta S_{\mathrm{surroundings}} = 0$
- (2) $\Delta S_{\mathrm{system}} = 0$; $\Delta S_{\mathrm{surroundings}} = 0$
- (3) $\Delta S_{\mathrm{system}} = 4.606\,R$; $\Delta S_{\mathrm{surroundings}} = -4.606\,R$
- (4) $\Delta S_{\mathrm{system}} = 0$; $\Delta S_{\mathrm{surroundings}} = 4.606R$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Entropy is a state function, so $\Delta S_{\mathrm{system}}$ is found along a reversible isothermal path between the same states: $\Delta S_{\mathrm{system}} = nR\ln\frac{V_2}{V_1}$.
2. $\Delta S_{\mathrm{system}} = 2R \times 2.303\log_{10}\frac{100}{10} = 2R \times 2.303 = 4.606\,R$.
3. In free expansion no heat is exchanged with the surroundings ($q = 0$), so $\Delta S_{\mathrm{surroundings}} = 0$.
4. $\Delta S_{\mathrm{system}} = 4.606\,R$, $\Delta S_{\mathrm{surroundings}} = 0$, which is option $1$.

**Subtopic:** Entropy, Second Law & Third Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q059_da182435_03112026.png?v=da18243548dd)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a free expansion nothing crosses the boundary, so the surroundings are unchanged, while the gas's entropy rises by $nR\ln(V_2/V_1) = 2R\ln 10 = 4.606R$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Working the gas's entropy change correctly and then imposing $\Delta S_{\mathrm{total}} = 0$ forces the surroundings to $-4.606R$, which is the answer for a reversible isothermal expansion rather than for the free expansion the stem states
- **Why:** This question requires the entropy change of each side of the boundary computed from the stem's numbers, demonstrated by the stem specifying 'free expansion from $10\,\mathrm{L}$ to $100\,\mathrm{L}$ at $300\,\mathrm{K}$'.
- **Note:** E1 called this statement_options, which does not match the printed shape: each option carries two values, $\Delta S_{\mathrm{system}}$ and $\Delta S_{\mathrm{surroundings}}$, that must both be right, so the shape recorded is two_part.
<!--/ecat-->

## Q60

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The compound that CANNOT be obtained from the aldol condensation reaction shown below, is

![printed figure: 2,2-dimethylcyclopentan-1-one + $\ce{PhCHO}$ →(NaOH, Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q060_711a1818_03112026.svg?v=711a1818e66c)

*2,2-dimethylcyclopentan-1-one + $\ce{PhCHO}$ →[NaOH, Δ]*

![drawn: 2,2-dimethylcyclopentan-1-one + $\ce{PhCHO}$ →(NaOH, Δ)](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_question_389c39e8_04112026.svg?v=389c39e83ff7)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2,2-dimethylcyclopentan-1-one `CC1(C)CCCC1=O` ![2,2-dimethylcyclopentan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_question_s1_4669c97f_04112026.svg?v=4669c97fa305); benzaldehyde `O=Cc1ccccc1` ![benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_question_s2_34066c30_04112026.svg?v=34066c303fa0)

- (1) (5Z)-5-benzylidene-2,2-dimethylcyclopentan-1-one `CC1(C)CC/C(=C/c2ccccc2)C1=O` ![(5Z)-5-benzylidene-2,2-dimethylcyclopentan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_option_1_s1_4565b725_04112026.svg?v=4565b7255b35)
- **(2)** 5-(5,5-dimethylcyclopent-1-en-1-yl)-2,2-dimethylcyclopentan-1-one `CC1(C)CCC(C2=CCCC2(C)C)C1=O` ![5-(5,5-dimethylcyclopent-1-en-1-yl)-2,2-dimethylcyclopentan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_option_2_s1_f038a5cd_04112026.svg?v=f038a5cd8751)
- (3) (5E)-5-benzylidene-2,2-dimethylcyclopentan-1-one `CC1(C)CC/C(=C\c2ccccc2)C1=O` ![(5E)-5-benzylidene-2,2-dimethylcyclopentan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_option_3_s1_aad35edd_04112026.svg?v=aad35eddc2cb)
- (4) (5E)-5-(2,2-dimethylcyclopentylidene)-2,2-dimethylcyclopentan-1-one `CC1(C)CC/C(=C2/CCCC2(C)C)C1=O` ![(5E)-5-(2,2-dimethylcyclopentylidene)-2,2-dimethylcyclopentan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/04112026/neet_papers/2026/2026_70/figures_drawn/q060_option_4_s1_0b717035_04112026.svg?v=0b71703518e3)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In 2,2-dimethylcyclopentanone the $\alpha$-carbon $C_2$ is quaternary, so only $C_5$ (CH$_2$) forms the enolate.
2. Cross aldol: the $C_5$ enolate adds to PhCHO, and dehydration gives $C_5{=}CHPh$, conjugated with $C{=}O$, as either the $E$ or the $Z$ isomer (options $1$ and $3$).
3. Self aldol: the $C_5$ enolate adds to the $C{=}O$ of a second ketone, giving a $\beta$-hydroxy ketone with $OH$ on the second ring's $C_1$.
4. E1cB dehydration removes the acidic $\alpha$-H on $C_5$ of the first ring, giving the exocyclic $C{=}C$ between the two rings, conjugated with $C{=}O$ (option $4$).
5. Option $2$ keeps an sp$^3$ $\alpha$-CH and places the $C{=}C$ inside the second ring, not conjugated with $C{=}O$, so aldol condensation cannot give it: option $2$.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q060_ce59f5d6_03112026.png?v=ce59f5d6ff9b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** In a crossed aldol condensation only a carbonyl compound with alpha-hydrogens can supply the enolate, and here the gem-dimethyl carbon of the ketone has none, so condensation with benzaldehyde can happen only at the other alpha-carbon
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings in this record and the scheme carries only the two reactants, so the candidate products the negated stem has to be judged against did not reach this step and no option's pull can be named
- **Why:** This question requires which product the available alpha-hydrogens permit, demonstrated by the stem 'The compound that CANNOT be obtained from the aldol condensation reaction shown below' over a scheme of 2,2-dimethylcyclopentan-1-one with $\mathrm{PhCHO}$ and $\mathrm{NaOH}$.
- **Note:** The options for this question are empty in our record: the figure note says the arrow has no product drawn and that the products are the options, and options_en holds four empty strings. For a reviewer holding the printed structures, the mechanisms to check are whether a drawn distractor requires enolisation at the quaternary C2, which carries two methyls and no alpha-hydrogen, or self-condensation of benzaldehyde, which has no alpha-hydrogen either, and whether the key turns on the stem's 'CANNOT'.
<!--/ecat-->

## Q61

Chemistry · inorganic · Coordination Compounds – Practice

The complex which has \textit{facial} and \textit{meridional} isomers is (Given : py = pyridine and en = $\mathrm{H_2N{-}CH_2{-}CH_2{-}NH_2}$)

- (1) $\mathrm{\left[Ni(en)_2(H_2O)_2\right]^{2+}}$
- **(2)** $\mathrm{\left[Cr(py)_3(Cl)_3\right]}$
- (3) $\mathrm{\left[Cr(H_2O)_6\right]^{3+}}$
- (4) $\mathrm{\left[Co(NH_3)_4(H_2O)_2\right]^{3+}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Facial and meridional isomers occur for octahedral complexes of type $\mathrm{[MA_3B_3]}$.
2. $\mathrm{[Ni(en)_2(H_2O)_2]^{2+}}$ is $\mathrm{[M(AA)_2B_2]}$: shows cis/trans (and optical), not fac/mer.
3. $\mathrm{[Cr(H_2O)_6]^{3+}}$ is $\mathrm{[MA_6]}$: no geometrical isomers.
4. $\mathrm{[Co(NH_3)_4(H_2O)_2]^{3+}}$ is $\mathrm{[MA_4B_2]}$: shows only cis/trans.
5. $\mathrm{[Cr(py)_3Cl_3]}$ is $\mathrm{[MA_3B_3]}$: shows fac and mer isomers, which is option $2$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 11)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q061_03ff14ea_03112026.png?v=03ff14eac185)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Facial and meridional isomers exist only for an octahedral $\mathrm{Ma_3b_3}$ complex, where the three like ligands either cap one face or run along a meridian
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $\mathrm{[Co(NH_3)_4(H_2O)_2]^{3+}}$ really does show geometrical isomerism, as the $\mathrm{Ma_4b_2}$ pattern the chapter uses for cis and trans, so matching on 'isomers' rather than on which isomers picks the familiar example
- **Why:** This question requires the ligand pattern that permits one named kind of isomerism, demonstrated by the stem asking for 'The complex which has facial and meridional isomers' and by option 2 being the only $\mathrm{Ma_3b_3}$ formula printed.
<!--/ecat-->

## Q62

Chemistry · physical · Basic Concepts of Chemistry

The numbers $17.0145$ and $21.0235$ were rounded to three figures after the decimal point. The resulting numbers, respectively, are

- (1) $17.015$ and $21.024$
- (2) $17.014$ and $21.023$
- (3) $17.015$ and $21.023$
- **(4)** $17.014$ and $21.024$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT rounding rule: if the digit to be dropped is $5$ (followed by nothing), the preceding digit is left unchanged if it is even and increased by $1$ if it is odd.
2. $17.0145$: the digit dropped is $5$ and the preceding digit $4$ is even, so $17.0145 \to 17.014$.
3. $21.0235$: the digit dropped is $5$ and the preceding digit $3$ is odd, so $21.0235 \to 21.024$.
4. The pair $17.014$ and $21.024$ is option $4$.

**Subtopic:** Significant Figures · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 11)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q062_1073f652_03112026.png?v=1073f652bbd3)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** When the digit dropped is exactly 5, the convention in the chapter leaves the preceding digit unchanged if it is even and raises it by one if it is odd, so $17.0145$ gives $17.014$ and $21.0235$ gives $21.024$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Applying the everyday rule that a 5 rounds the preceding digit up gives $17.015$ and $21.024$, which is this option exactly — the second number happens to agree with the convention and the first does not
- **Why:** This question requires the rounding convention applied to two printed numbers, demonstrated by the stem 'The numbers 17.0145 and 21.0235 were rounded to three figures after the decimal point'.
- **Note:** E1 called this plain_mcq by its default rule, which does not match the printed shape: the stem asks for the two results 'respectively' and each option carries both, so the shape recorded is two_part.
<!--/ecat-->

## Q63

Chemistry · physical · Basic Concepts of Chemistry

The amount of carbon dioxide evolved upon complete combustion of $116\,\mathrm{g}$ of $n$-butane is (Given: atomic mass in amu $\mathrm{H}=1$, $\mathrm{C}=12$ and $\mathrm{O}=16$)

- (1) $362\,\mathrm{g}$
- **(2)** $352\,\mathrm{g}$
- (3) $322\,\mathrm{g}$
- (4) $176\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $M(\mathrm{C_4H_{10}}) = 4(12) + 10(1) = 58\,\mathrm{g\,mol^{-1}}$.
2. $n(\mathrm{C_4H_{10}}) = \frac{116}{58} = 2\,\mathrm{mol}$.
3. $2\mathrm{C_4H_{10}} + 13\mathrm{O_2} \rightarrow 8\mathrm{CO_2} + 10\mathrm{H_2O}$, so 1 mol butane gives 4 mol $\mathrm{CO_2}$.
4. $n(\mathrm{CO_2}) = 2 \times 4 = 8\,\mathrm{mol}$.
5. $m(\mathrm{CO_2}) = 8 \times 44 = 352\,\mathrm{g}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 11)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q063_e62bf8da_03112026.png?v=e62bf8da01c2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Mass to moles first, then the balanced combustion equation fixes the mole ratio: each mole of butane yields four moles of carbon dioxide
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The balanced equation prints 4 CO2, so the coefficient itself gets read as the number of moles and $4\times 44 = 176$ g is written down, with the factor of 2 mol of butane never applied.
- **Why:** This question requires a mass-to-mole conversion carried through the combustion stoichiometry, demonstrated by the stem giving '116 g of n-butane' together with the atomic masses rather than a number of moles.
<!--/ecat-->

## Q64

Chemistry · physical · Structure of Atom

Consider the following schematic plots of orbital wavefunction ($\Psi_r$) against distance (r) from the nucleus. The figure representing two radial nodes in the orbital is

![printed figure: four schematic plots of radial wavefunction $\Psi_r$ (y-axis) against distance r (x-axis, origin 0), labelled A, B, C, D: A decays smoothly from a high value to zero without crossing the axis; B falls from a high value, crosses the dashed zero line once into a dip, then levels off just below zero; C falls from a high value, crosses below zero, rises above zero into a small hump, then levels off just above zero; D starts near zero, rises into a broad positive hump, crosses below zero into a dip, then levels off near zero](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q064_d722b4e0_03112026.svg?v=d722b4e0b42c)

*four schematic plots of radial wavefunction $\Psi_r$ (y-axis) against distance r (x-axis, origin 0), labelled A, B, C, D: A decays smoothly from a high value to zero without crossing the axis; B falls from a high value, crosses the dashed zero line once into a dip, then levels off just below zero; C falls from a high value, crosses below zero, rises above zero into a small hump, then levels off just above zero; D starts near zero, rises into a broad positive hump, crosses below zero into a dip, then levels off near zero*

- (1) D
- (2) A
- (3) B
- **(4)** C

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. A radial node is a point $r > 0$ where $\Psi_r$ changes sign, i.e. the curve crosses the dashed $\Psi_r = 0$ line.
2. Plot A decays from a maximum without crossing zero: $0$ radial nodes.
3. Plot B crosses zero once (positive to negative): $1$ radial node.
4. Plot C crosses zero twice (positive to negative, then negative to positive): $2$ radial nodes.
5. Plot D starts at $\Psi_r = 0$ at $r = 0$ (not a radial node) and crosses zero once: $1$ radial node.
6. Two radial nodes corresponds to plot C, which is option $4$.

**Subtopic:** Atomic Orbitals: Shapes, Energies and Nodes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q064_016810e6_03112026.png?v=016810e6eca9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A radial node is a distance at which the wavefunction changes sign; the zero at the nucleus and the tail at infinity are not counted
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Plot D is zero at the nucleus and crosses the axis once more, so a student who counts every place the curve touches zero adds the origin to the one real crossing and reports two radial nodes.
- **Why:** This question requires reading sign changes off four printed curves, demonstrated by the stem asking which 'figure' represents two radial nodes while the options are only the panel letters A to D.
- **Note:** The image itself was not opened at this step; the panel-by-panel transcription supplied with the packet (A no crossing, B one, C two, D zero at the origin plus one crossing) was used, and it agrees with the printed key of C. A reviewer holding the figure should confirm that D does start at zero, since that is what the trap rests on.
<!--/ecat-->

## Q65

Chemistry · organic · General Organic Chemistry

The following carbocation is stabilized by the interaction of the empty $p$ orbital with

![printed figure: 1-phenylethan-1-ylium (1-phenylethyl carbocation, $\ce{C6H5-CH^+-CH3}$)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q065_eb0d52c6_03112026.svg?v=eb0d52c605d0)

*1-phenylethan-1-ylium (1-phenylethyl carbocation, $\ce{C6H5-CH^+-CH3}$)*

![drawn: 1-phenylethan-1-ylium (1-phenylethyl carbocation, $\ce{C6H5-CH^+-CH3}$)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q065_question_e3a3939c_03112026.svg?v=e3a3939c71cb)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: 1-phenylethan-1-ylium `C[CH+]c1ccccc1` ![1-phenylethan-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q065_question_s1_9b5793d3_03112026.svg?v=9b5793d33636)

- (1) empty $\sigma^*$ and empty $\pi^*$ orbitals
- **(2)** filled $\sigma$ and filled $\pi$ orbitals
- (3) empty $\sigma$ and empty $\pi^*$ orbitals
- (4) empty $\sigma^*$ and filled $\pi$ orbitals

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The figure shows the 1-phenylethyl cation, $\mathrm{C_6H_5\overset{+}{C}H{-}CH_3}$, with an empty $p$ orbital on the cationic carbon.
2. An empty orbital is stabilized only by donation from filled orbitals, so options with empty $\sigma^*$, $\pi^*$ or $\sigma$ donors are ruled out.
3. The $\mathrm{CH_3}$ group gives hyperconjugation: filled $\sigma_{\mathrm{C-H}}$ orbitals overlap with the empty $p$ orbital.
4. The phenyl ring gives resonance: filled $\pi$ orbitals of the ring overlap with the empty $p$ orbital.
5. Hence stabilization is by filled $\sigma$ and filled $\pi$ orbitals, which is option $2$.

**Subtopic:** Hyperconjugation, Resonance Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q065_82b7efeb_03112026.png?v=82b7efebbc5a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An empty p orbital is stabilised only by donation from filled neighbours: the ring's filled pi system by resonance and the adjacent C-H sigma bonds by hyperconjugation
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Hyperconjugation is often carried as a sigma-star interaction, so the pi half is set down correctly as filled while the sigma half is written as the antibonding sigma-star.
- **Why:** This question requires the rule that a vacant orbital is stabilised by overlap with filled neighbours applied to the printed cation, demonstrated by the stem's phrase 'stabilized by the interaction of the empty p orbital with' and by the structure carrying both a methyl group and a ring.
- **Note:** The pattern classifier recorded statement_options, which would map to qtype statements. The printed options are not statements to be judged but orbital pairs completing the stem sentence, so mcq is recorded instead.
<!--/ecat-->

## Q66

Chemistry · inorganic · Coordination Compounds – Practice

A $1:3$ electrolyte in an aqueous solution is

- (1) $\mathrm{[Co(NH_3)_3(NO_2)_3]}$
- (2) $\mathrm{[CoCl_2(NH_3)_4]Cl}$
- (3) $\mathrm{[CoCl(NH_3)_5]Cl_2}$
- **(4)** $\mathrm{[Co(NH_3)_6]Cl_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Only chloride outside the coordination sphere ionises in water; a $1:3$ electrolyte gives one complex ion and three counter-ions.
2. $\mathrm{[Co(NH_3)_3(NO_2)_3]}$ is neutral with no counter-ions, so it is a non-electrolyte.
3. $\mathrm{[CoCl_2(NH_3)_4]Cl \rightarrow [CoCl_2(NH_3)_4]^+ + Cl^-}$, a $1:1$ electrolyte.
4. $\mathrm{[CoCl(NH_3)_5]Cl_2 \rightarrow [CoCl(NH_3)_5]^{2+} + 2Cl^-}$, a $1:2$ electrolyte.
5. $\mathrm{[Co(NH_3)_6]Cl_3 \rightarrow [Co(NH_3)_6]^{3+} + 3Cl^-}$, a $1:3$ electrolyte, which is option $4$.

**Subtopic:** Werner’s Theory and Applications of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q066_c57bf27a_03112026.png?v=c57bf27a1cda)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Only the groups written outside the square bracket ionise, so the electrolyte type is read from them and not from the atoms inside the coordination sphere
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  '1 : 3' gets read as 'three ions in solution', and $\mathrm{[CoCl(NH_3)_5]Cl_2}$ is exactly the complex that furnishes three ions - one cation and two chlorides.
- **Why:** This question requires applying the ionisation rule for the coordination sphere to four printed formulae, demonstrated by the stem asking for 'a 1:3 electrolyte' while every option is a cobalt complex of the same CoCl3 composition.
<!--/ecat-->

## Q67

Chemistry · physical · Electrochemistry

The standard electrode potential ($E^\circ$) for the half-cell reaction $\mathrm{Fe^{3+} + e^- \rightarrow Fe^{2+}}$ at $298\,\mathrm{K}$ is (Given: $E^\circ\left(\mathrm{Fe^{3+}/Fe}\right) = -0.04\,\mathrm{V}$ and $E^\circ\left(\mathrm{Fe^{2+}/Fe}\right) = -0.44\,\mathrm{V}$ at $298\,\mathrm{K}$)

- (1) $+0.92\,\mathrm{V}$
- (2) $+0.40\,\mathrm{V}$
- **(3)** $+0.76\,\mathrm{V}$
- (4) $-0.48\,\mathrm{V}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Target: $\mathrm{Fe^{3+} + e^- \rightarrow Fe^{2+}}$ = ($\mathrm{Fe^{3+} + 3e^- \rightarrow Fe}$) + ($\mathrm{Fe \rightarrow Fe^{2+} + 2e^-}$).
2. $\Delta G_1^\circ = -3F(-0.04) = +0.12F$.
3. $\Delta G_2^\circ = -[-2F(-0.44)] = -0.88F$.
4. $\Delta G^\circ = 0.12F - 0.88F = -0.76F = -1\cdot F E^\circ$.
5. $E^\circ = +0.76\,\mathrm{V}$, which is option $3$.

**Subtopic:** Electrode Potential and Standard Electrode Potential · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 11)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q067_20d9ba01_03112026.png?v=20d9ba01b024)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Electrode potentials are not additive; the free energies are, so couples combine as $nE^\circ$ weighted by the electrons each half-reaction transfers
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The two given potentials are simply subtracted, $-0.04-(-0.44) = +0.40$ V, as though $E^\circ$ added like a state function.
- **Why:** This question requires combining two half-cell potentials through their free energies, demonstrated by the stem supplying $E^\circ(\mathrm{Fe^{3+}/Fe})$ and $E^\circ(\mathrm{Fe^{2+}/Fe})$ for couples of three and two electrons while asking for a one-electron step.
<!--/ecat-->

## Q68

Chemistry · inorganic · The p–Block Elements

In potash alum, the ratio of $\mathrm{K^{+}}$ and $\mathrm{SO_4^{2-}}$ ions is

- (1) $3:2$
- **(2)** $1:2$
- (3) $2:1$
- (4) $2:3$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Potash alum is $\mathrm{K_2SO_4\cdot Al_2(SO_4)_3\cdot 24H_2O}$, i.e. $\mathrm{KAl(SO_4)_2\cdot 12H_2O}$.
2. It contains $2\,\mathrm{K^+}$ and $4\,\mathrm{SO_4^{2-}}$ per double-salt formula, so $\mathrm{K^+}:\mathrm{SO_4^{2-}} = 2:4 = 1:2$, which is option $2$.

**Subtopic:** Applications & Special Features of Group 13 · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q068_57078634_03112026.png?v=57078634b956)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Potash alum is $\mathrm{K_2SO_4 \cdot Al_2(SO_4)_3 \cdot 24H_2O}$, so the whole double salt must be counted: two potassium ions to four sulfates
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The count is taken from the potassium sulfate half of the double salt alone, where two potassium ions sit on one sulfate, so the ratio comes out the other way up as 2:1.
- **Why:** This question requires the stored composition of potash alum, demonstrated by the stem naming only 'potash alum' and supplying no formula from which the ions could be counted.
<!--/ecat-->

## Q69

Chemistry · physical · Solutions

Consider the following statements about the solutions formed by mixing two liquids.

- (A) An ideal solution thus formed obeys Raoult's law throughout the composition range.
- (B) Mixture of chloroform and acetone shows negative deviation from Raoult's law.
- (C) Mixture of aniline and phenol shows positive deviation from Raoult's law.

- (1) A and C only
- **(2)** A and B only
- (3) B and C only
- (4) A only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement A: an ideal solution obeys Raoult's law, $p_i = x_i p_i^\circ$, over the entire composition range, so A is true.
2. Statement B: chloroform and acetone form a hydrogen bond $\text{Cl}_3\text{C-H}\cdots\text{O=C(CH}_3)_2$, making A-B attractions stronger than A-A and B-B, so the mixture shows negative deviation; B is true.
3. Statement C: phenol and aniline form a hydrogen bond between phenolic $\text{O-H}$ and the $\text{N}$ of aniline, stronger than the like interactions, so the mixture shows negative deviation, not positive; C is false.
4. True statements are A and B only, which is option $2$.

**Subtopic:** Ideal and Nonideal Solutions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q069_0cfa427d_03112026.png?v=0cfa427d6cfe)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** When unlike molecules attract each other more strongly than their own kind, as in chloroform-acetone and phenol-aniline, the vapour pressure falls below Raoult's law: a negative deviation
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The sign rule is held the wrong way round - strong attraction between the two kinds of molecule taken to raise the vapour pressure - and that single inversion both rejects B and accepts C.
- **Why:** This question requires the deviation NCERT files each named mixture under, demonstrated by statements B and C naming the chloroform-acetone and aniline-phenol pairs rather than describing their interactions.
<!--/ecat-->

## Q70

Chemistry · physical · Electrochemistry

For a salt $\mathbf{XY}$, which is a strong electrolyte, the plot of $\Lambda_{\mathrm{m}}$ versus $\sqrt{c}$ has a slope of $-90.0\,\mathrm{S\,cm^{2}\,mol^{-3/2}\,L^{1/2}}$ at $298\,\mathrm{K}$. At $0.01\,\mathrm{M}$ concentration of $\mathbf{XY}$, the value of $\Lambda_{\mathrm{m}}$ is $145.0\,\mathrm{S\,cm^{2}\,mol^{-1}}$. The limiting molar conductivity of $\mathbf{Y}^{-}$ ion ($\lambda^{\mathrm{o}}_{\mathrm{Y}^{-}}$, in $\mathrm{S\,cm^{2}\,mol^{-1}}$) at $298\,\mathrm{K}$ will be (Given : $\lambda^{\mathrm{o}}_{\mathrm{X}^{+}} = 74.0\,\mathrm{S\,cm^{2}\,mol^{-1}}$)

- (1) $76.0$
- **(2)** $80.0$
- (3) $100.0$
- (4) $90.0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. For a strong electrolyte, $\Lambda_m = \Lambda_m^{o} - A\sqrt{c}$, with slope $-A = -90.0$.
2. $\sqrt{c} = \sqrt{0.01} = 0.1$.
3. $\Lambda_m^{o} = 145.0 + 90.0 \times 0.1 = 154.0\,\mathrm{S\,cm^2\,mol^{-1}}$.
4. $\lambda^{o}_{Y^-} = \Lambda_m^{o} - \lambda^{o}_{X^+} = 154.0 - 74.0 = 80.0$, which is option $2$.

**Subtopic:** Variation of Conductivity and Molar Conductivity with Concentration, Kohlrausch Law of Independent Migration of Ions · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 11)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q070_80f78fc8_03112026.png?v=80f78fc8b776)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The intercept of the $\Lambda_m$ against $\sqrt{c}$ plot is the limiting molar conductivity, which Kohlrausch's law then splits into the two ionic contributions
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each standard slip on this route was computed and none of them is printed: dropping the square root ($90 \times 0.01$) gives $\lambda^o = 71.9$, taking the slope with the wrong sign gives 62, skipping the $A\sqrt{c}$ correction altogether gives 71, and using the bare slope gives 161. The answer 80.0 comes from $\Lambda^o_m = 145 + 90(0.1) = 154$ and $154 - 74 = 80$, and the three remaining options are not the output of any of those routes.
- **Why:** This question requires the intercept of the conductivity plot to be recovered from the slope and one measured point and then split by Kohlrausch's law, demonstrated by the stem supplying the slope, $\Lambda_m$ at 0.01 M and $\lambda^o_{X^+}$ together.
- **Note:** no_trap is a positive finding here: the paper prints no option on any of the four slips this calculation invites (71.9, 62, 71, 161), so its wrong options spread the answer rather than catch a named error.
<!--/ecat-->

## Q71

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Arrange the following compounds in the increasing order of polarity. Choose the **correct** options given below. swer from the

- (A) $\mathrm{CH_3CH_2OCH_2CH_3}$
- (B) $\mathrm{CH_3CH_2OH}$
- (C) $\mathrm{CH_3COCH_3}$
- (D) $\mathrm{CH_3COOH}$

- **(1)** $\mathrm{A} < \mathrm{C} < \mathrm{B} < \mathrm{D}$
- (2) $\mathrm{A} < \mathrm{B} < \mathrm{C} < \mathrm{D}$
- (3) $\mathrm{C} < \mathrm{A} < \mathrm{D} < \mathrm{B}$
- (4) $\mathrm{C} < \mathrm{A} < \mathrm{B} < \mathrm{D}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2OCH_2CH_3}$ (A) has only a weak $\mathrm{C{-}O{-}C}$ dipole and no $\mathrm{O{-}H}$, so it is the least polar.
2. $\mathrm{CH_3COCH_3}$ (C) has a polar $\mathrm{C{=}O}$ group but no $\mathrm{O{-}H}$ hydrogen-bond donor, so $\mathrm{A} < \mathrm{C}$.
3. $\mathrm{CH_3CH_2OH}$ (B) has an $\mathrm{O{-}H}$ group that hydrogen bonds, so $\mathrm{C} < \mathrm{B}$.
4. $\mathrm{CH_3COOH}$ (D) has both $\mathrm{C{=}O}$ and $\mathrm{O{-}H}$ and hydrogen bonds most strongly, so $\mathrm{B} < \mathrm{D}$.
5. Order $\mathrm{A} < \mathrm{C} < \mathrm{B} < \mathrm{D}$ is option $1$.

**Subtopic:** Physical Properties of Aldehydes, Ketones, and Carboxylic Acids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q071_32838fea_03112026.png?v=32838fea5dcd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Across this series polarity is read from the functional group's hydrogen bonding: an ether neither donates nor strongly accepts, a ketone accepts, an alcohol donates, and a carboxylic acid does both most strongly
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The middle pair is ranked by dipole moment, where acetone at 2.9 D stands above ethanol at 1.7 D, so the ketone is placed above the alcohol and the four compounds come out in the order they are printed.
- **Why:** This question requires four lettered compounds arranged on a property that is not computed from any printed number, demonstrated by the stem asking for 'the increasing order of polarity' of a list identified only by structural formulae.
- **Note:** The pattern classifier recorded arrange_in_order, which would map to qtype mcq; statements is recorded because a lettered block A to D is printed above the options, which is the line used for this group. On the chemistry: ranking by dipole moment alone would put acetone (2.9 D) above both ethanol (1.7 D) and acetic acid (1.7 D), an order that no option prints, so the question's 'polarity' is the hydrogen-bonding reading the key follows. Tagged as printed.
<!--/ecat-->

## Q72

Chemistry · inorganic · Coordination Compounds – Practice

According to crystal field theory, the correct order of ligands with respect to their decreasing order of field strength is

- (1) $\mathrm{Cl^{-}} > \mathrm{NH_3} > \mathrm{H_2O} > \mathrm{CO}$
- **(2)** $\mathrm{CO} > \mathrm{NH_3} > \mathrm{H_2O} > \mathrm{Cl^{-}}$
- (3) $\mathrm{CO} > \mathrm{H_2O} > \mathrm{NH_3} > \mathrm{Cl^{-}}$
- (4) $\mathrm{Cl^{-}} > \mathrm{H_2O} > \mathrm{NH_3} > \mathrm{CO}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The spectrochemical series in increasing field strength is $\mathrm{Cl^{-}} < \mathrm{H_2O} < \mathrm{NH_3} < \mathrm{CO}$, so in decreasing order it is $\mathrm{CO} > \mathrm{NH_3} > \mathrm{H_2O} > \mathrm{Cl^{-}}$, which is option $2$.

**Subtopic:** Crystal Field Theory and Its Limitations · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q072_e13ba35b_03112026.png?v=e13ba35b5ce8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The spectrochemical series: carbonyl and cyanide are the strongest field ligands, ammonia beats water, and the halides are weakest
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The series is memorised in the increasing direction, $\mathrm{Cl^- < H_2O < NH_3 < CO}$, and gets copied out left to right, so the four ligands appear in exactly the remembered sequence while the stem asked for decreasing strength.
- **Why:** This question requires a remembered series to be laid out in the direction the stem names, demonstrated by the stem asking for 'decreasing order of field strength' and all four options being permutations of the same four ligands.
- **Note:** The pattern label arrange_in_order maps to qtype mcq here because no lettered block is printed: the ligands live inside the four options.
<!--/ecat-->

## Q73

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

The amino acid that gives a red-blood colour on treating its sodium fusion extract with sodium nitroprusside is

- (1) serine
- (2) leucine
- (3) threonine
- **(4)** methionine

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Sodium nitroprusside, $\mathrm{Na_2[Fe(CN)_5NO]}$, tests the sodium fusion extract for sulphur (present as $\mathrm{Na_2S}$).
2. $\mathrm{S^{2-} + [Fe(CN)_5NO]^{2-} \rightarrow [Fe(CN)_5NOS]^{4-}}$, a coloured complex, so the amino acid must contain sulphur.
3. Serine, leucine and threonine contain only C, H, N, O; methionine, $\mathrm{CH_3SCH_2CH_2CH(NH_2)COOH}$, contains S, which is option $4$.

**Subtopic:** Detection of Elements · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 12)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q073_df297d3f_03112026.png?v=df297d3f90e8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Sodium nitroprusside added to the sodium fusion extract is the test for sulphur, so the answer is whichever amino acid carries a sulphur atom
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Cysteine is the sulphur amino acid carried over from the amino-acid table, and serine is that same side chain with oxygen in place of sulphur, so a search for the thiol-bearing structure stops at the printed twin.
- **Why:** This question requires the meaning of a bench observation in Lassaigne's test, demonstrated by the stem specifying 'sodium fusion extract with sodium nitroprusside' rather than asking directly which amino acid contains sulphur.
- **Note:** The stem's colour word is 'red-blood', whereas the nitroprusside test for sulphur is described in NCERT as giving a violet colour; the key is unaffected, since methionine is the only sulphur-bearing option. Tagged as printed.
<!--/ecat-->

## Q74

Chemistry · physical · Redox Reactions

In an acidic medium, $10\,\mathrm{mL}$ of $0.25\,\mathrm{M}$ oxalic acid is titrated with $\mathrm{KMnO_4}$ solution. If the volume of $\mathrm{KMnO_4}$ solution required to reach end point is $10\,\mathrm{mL}$, the strength of the $\mathrm{KMnO_4}$ solution is

- (1) $0.15\,\mathrm{M}$
- **(2)** $0.10\,\mathrm{M}$
- (3) $0.20\,\mathrm{M}$
- (4) $0.25\,\mathrm{M}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In acidic medium $\mathrm{MnO_4^-} \to \mathrm{Mn^{2+}}$ gains $5e^-$, so n-factor of $\mathrm{KMnO_4}$ is $5$.
2. Oxalate $\mathrm{C_2O_4^{2-}} \to 2\mathrm{CO_2}$ loses $2e^-$, so n-factor of oxalic acid is $2$.
3. Milliequivalents of oxalic acid $= 0.25 \times 2 \times 10 = 5$.
4. Equating, $M \times 5 \times 10 = 5$.
5. $M = \frac{5}{50} = 0.10\,\mathrm{M}$, which is option $2$.

**Subtopic:** redox reactions as the basis for titrations using potassium permanganate – practice · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q074_b021d88e_03112026.png?v=b021d88e792b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A redox titration balances electrons, not molecules: oxalate releases two and permanganate takes five in acid, so the n-factors must enter the equivalence
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  $M_1V_1 = M_2V_2$ is applied as though this were an acid-base titration, and with the two volumes equal the permanganate concentration comes straight back as 0.25 M.
- **Why:** This question requires an equivalence calculated from electrons transferred, demonstrated by the stem fixing the medium as acidic and giving equal volumes, which makes the un-weighted answer identical to the printed oxalic acid concentration.
<!--/ecat-->

## Q75

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The correct statement is

- (1) Aluminium has five valence orbitals.
- **(2)** Boron has a maximum covalency of four.
- (3) Beryllium has three valence orbitals.
- (4) Magnesium has a maxium covalency of four.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Boron is in period 2, so its valence orbitals are $2s$ and three $2p$: $1 + 3 = 4$ orbitals, giving maximum covalency $4$ (e.g. $[BF_4]^-$). Option $2$ is correct.
2. Aluminium (period 3) has $3s$, $3p$ and $3d$ valence orbitals: $1 + 3 + 5 = 9$, not $5$, so option $1$ is false.
3. Beryllium (period 2) has $2s$ and $2p$: $1 + 3 = 4$ valence orbitals, not $3$, so option $3$ is false.
4. Magnesium (period 3) can use $d$ orbitals, so its maximum covalency exceeds $4$ (up to $6$), so option $4$ is false; the answer is option $2$.

**Subtopic:** Anomalous Properties of Second Period Elements · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 12)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q075_654b6d97_03112026.png?v=654b6d975b47)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A second-period element has only four valence orbitals, one 2s and three 2p, which caps boron's covalency at four; from the third period onwards d orbitals let the covalency grow
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  'Maximum covalency of four' is held as the headline and attached to magnesium, the element one period down from the one it belongs to, so the sentence is the right claim about the wrong element.
- **Why:** This question requires the stated NCERT line about second-period elements, demonstrated by the option 'Boron has a maximum covalency of four.' being graded as a whole claim against three rival claims of the same form.
- **Note:** Option 4 is printed as 'maxium covalency', a spelling slip in the record; it does not change what the option claims, so the tag follows the question as printed.
<!--/ecat-->

## Q76

Chemistry · organic · Hydrocarbons

Among the following, the compound having conjugated double bonds is

- (1) hepta-1,6-diene
- **(2)** hepta-1,3-diene
- (3) hepta-1,4-diene
- (4) hepta-1,5-diene

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Conjugated double bonds alternate with a single bond: $\mathrm{C{=}C{-}C{=}C}$, i.e. diene locants $n$ and $n+2$.
2. Hepta-1,3-diene: $\mathrm{CH_2{=}CH{-}CH{=}CH{-}C_3H_7}$, double bonds at 1 and 3, so conjugated.
3. Hepta-1,4-, 1,5- and 1,6-dienes have one or more $sp^3$ carbons between the double bonds, so they are isolated, not conjugated.
4. Therefore the answer is option $2$.

**Subtopic:** Classification and Nomenclature of Alkanes, Alkenes and Alkynes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q076_fd567cd4_03112026.png?v=fd567cd4f35f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Conjugation needs the two double bonds to share one single bond, which puts their locants two apart as in a 1,3-diene
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  'Separated by one single bond' is carried as 'separated by one carbon', and hepta-1,4-diene is exactly the name with one $\mathrm{sp^3}$ carbon sitting between the two double bonds.
- **Why:** This question requires the conjugation criterion applied to four IUPAC names, demonstrated by the options differing only in the second locant while the stem asks which 'compound having conjugated double bonds'.
<!--/ecat-->

## Q77

Chemistry · physical · Chemical Kinetics

$\mathrm{2A \xrightarrow{k} B}$ is a zero-order reaction, where $k = 1.0\,\mathrm{mol\,L^{-1}\,min^{-1}}$. If the initial concentration of A is $2\,\mathrm{M}$, then the time taken to complete $75\%$ of the reaction will be

- (1) $2.0\,\mathrm{min}$
- (2) $1.5\,\mathrm{min}$
- **(3)** $0.75\,\mathrm{min}$
- (4) $1.0\,\mathrm{min}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. For $2A \rightarrow B$, the rate of reaction is $r = -\frac{1}{2}\frac{d[A]}{dt}$; for zero order $r = k$.
2. So $-\frac{d[A]}{dt} = 2k = 2.0\,\mathrm{mol\,L^{-1}\,min^{-1}}$.
3. Amount of A consumed for $75\%$ completion: $0.75 \times 2\,\mathrm{M} = 1.5\,\mathrm{M}$.
4. $t = \frac{1.5\,\mathrm{M}}{2.0\,\mathrm{M\,min^{-1}}} = 0.75\,\mathrm{min}$, which is option $3$.

**Subtopic:** Zero Order Reactions · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 12)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q077_056f8aa4_03112026.png?v=056f8aa4c8f8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a zero-order reaction the amount consumed grows linearly with time, and the coefficient 2 in $\mathrm{2A \to B}$ means A disappears at twice the rate constant
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The textbook form $[A]_0 - [A] = kt$ is used as it stands, so the 1.5 M of A consumed is divided by k alone and the answer comes out at 1.5 min.
- **Why:** This question requires the zero-order rate law applied with the reaction's own stoichiometry, demonstrated by the stem printing '2A' with k in $\mathrm{mol\,L^{-1}\,min^{-1}}$ and asking for 75% completion.
<!--/ecat-->

## Q78

Chemistry · physical · Ionic Equilibrium

The correct order of solubility of the given salts in water at $298\,\mathrm{K}$ is

![printed figure: Table of Ksp at 298 K: $\ce{AgBr}$ 5.0×10⁻¹³; $\ce{Zn(OH)2}$ 1.0×10⁻¹⁵; $\ce{Hg2Cl2}$ 1.3×10⁻¹⁸](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q078_b6beb00f_03112026.svg?v=b6beb00f61e3)

*Table of Ksp at 298 K: $\ce{AgBr}$ 5.0×10⁻¹³; $\ce{Zn(OH)2}$ 1.0×10⁻¹⁵; $\ce{Hg2Cl2}$ 1.3×10⁻¹⁸*

- **(1)** $\mathrm{Zn(OH)_2} > \mathrm{AgBr} > \mathrm{Hg_2C1_2}$
- (2) $\mathrm{Hg_2Cl_2} > \mathrm{Zn(OH)_2} > \mathrm{AgBr}$
- (3) $\mathrm{AgBr} > \mathrm{Zn(OH)_2} > \mathrm{Hg_2C1_2}$
- (4) $\mathrm{Hg_2Cl_2} > \mathrm{AgBr} > \mathrm{Zn(OH)_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Read Ksp values from the table: $\mathrm{AgBr}: 5.0\times10^{-13}$, $\mathrm{Zn(OH)_2}: 1.0\times10^{-15}$, $\mathrm{Hg_2Cl_2}: 1.3\times10^{-18}$.
2. $\mathrm{AgBr}$ (1:1): $K_{sp} = s^2 \Rightarrow s = \sqrt{5.0\times10^{-13}} \approx 7.07\times10^{-7}\,\mathrm{M}$.
3. $\mathrm{Zn(OH)_2}$ (1:2): $K_{sp} = 4s^3 \Rightarrow s = (2.5\times10^{-16})^{1/3} \approx 6.3\times10^{-6}\,\mathrm{M}$.
4. $\mathrm{Hg_2Cl_2} \rightleftharpoons \mathrm{Hg_2^{2+}} + 2\mathrm{Cl^-}$: $K_{sp} = 4s^3 \Rightarrow s = (3.25\times10^{-19})^{1/3} \approx 6.9\times10^{-7}\,\mathrm{M}$.
5. Order: $\mathrm{Zn(OH)_2} > \mathrm{AgBr} > \mathrm{Hg_2Cl_2}$, which is option $1$.

**Subtopic:** Solubility Product Constant · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 12)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q078_5fd61bb0_03112026.png?v=5fd61bb00d8d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Solubility has to be extracted from $K_{sp}$ through the salt's own dissolution stoichiometry, so a 1:2 salt with the smaller $K_{sp}$ can still dissolve more than a 1:1 salt with the larger one
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The three $K_{sp}$ values are ranked as they stand, $5.0\times10^{-13}$ then $1.0\times10^{-15}$ then $1.3\times10^{-18}$, so the printed table order is handed over as the solubility order.
- **Why:** This question requires each solubility product converted into a molar solubility before the salts can be compared, demonstrated by the stem supplying a table of $K_{sp}$ values for a 1:1 salt and two 1:2 salts and by AgBr and $\mathrm{Hg_2Cl_2}$ separating only after that conversion ($7.1\times10^{-7}$ against $6.9\times10^{-7}$).
- **Note:** Options 1 and 3 print the mercury salt as 'Hg_2C1_2', with the digit one in place of the letter l; options 2 and 4 print Hg_2Cl_2. This is a transcription slip in our record and does not change what the option names. The $K_{sp}$ table itself reached this step only as a transcription (AgBr 5.0e-13, Zn(OH)2 1.0e-15, Hg2Cl2 1.3e-18), and the tags rest on those three values.
<!--/ecat-->

## Q79

Chemistry · physical · Redox Reactions

The correct decreasing order of oxidation state of the underlined atom in each molecule is

- (1) $\mathrm{\underline{P}_4O_6} > \mathrm{\underline{Cl}_2O_7} > \mathrm{\underline{Al}H_3}$
- (2) $\mathrm{\underline{P}_4O_{10}} > \mathrm{\underline{S}O_3} > \mathrm{H_2\underline{O}}$
- **(3)** $\mathrm{\underline{N}_2O_5} > \mathrm{\underline{Al}_2O_3} > \mathrm{H_2\underline{S}}$
- (4) $\mathrm{\underline{Pb}O_2} > \mathrm{\underline{N}_2O_3} > \mathrm{\underline{S}O_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{P_4O_6}$: $4x - 12 = 0 \Rightarrow x = +3$; $\mathrm{Cl_2O_7}$: $2x - 14 = 0 \Rightarrow x = +7$; $\mathrm{AlH_3}$: Al $= +3$. Order $+3, +7, +3$ is not decreasing.
2. Option 2: $\mathrm{P_4O_{10}}$: $4x - 20 = 0 \Rightarrow x = +5$; $\mathrm{SO_3}$: $x = +6$; $\mathrm{H_2O}$: O $= -2$. Since $+5 < +6$, not decreasing.
3. Option 3: $\mathrm{N_2O_5}$: $2x - 10 = 0 \Rightarrow x = +5$; $\mathrm{Al_2O_3}$: $2x - 6 = 0 \Rightarrow x = +3$; $\mathrm{H_2S}$: $2 + x = 0 \Rightarrow x = -2$.
4. $+5 > +3 > -2$ is strictly decreasing, so option 3 is correct.
5. Option 4: $\mathrm{PbO_2}$: $+4$; $\mathrm{N_2O_3}$: $+3$; $\mathrm{SO_3}$: $+6$. Since $+3 < +6$, not decreasing.

**Subtopic:** Oxidation Number · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 12)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q079_a2018a93_03112026.png?v=a2018a934dd1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Oxidation number is assigned from the electronegativity convention - oxygen is $-2$, hydrogen is $-1$ in a metal hydride - and not from how many oxygens the formula carries
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The oxygen count in the formula is used as a stand-in for the oxidation state, and the three oxygen subscripts in this option, 10 then 3 then 1, descend neatly even though the oxidation numbers are $+5$, $+6$ and $-2$.
- **Why:** This question requires oxidation numbers worked out and then arranged, demonstrated by the stem asking for 'the correct decreasing order of oxidation state of the underlined atom' across three different elements per option.
- **Note:** The pattern label arrange_in_order maps to qtype mcq: the species sit inside the options and no lettered block is printed.
<!--/ecat-->

## Q80

Chemistry · physical · Thermodynamics

Consider the reversible processes for $1.0\,\mathrm{mol}$ of an ideal gas as shown in the figure. $w_1$, $w_2$, $w_3$ and $w_4$ represent work done (in calories) in the processes 1, 2, 3 and 4, respectively; $\Delta U_2$ and $\Delta U_4$ are changes in the internal energy for the processes 2 and 4, respectively. [use $R = 2\,\mathrm{cal\,K^{-1}\,mol^{-1}}$] The correct option is

![printed figure: Pressure versus Volume graph of a reversible cycle (Carnot-type) for 1.0 mol ideal gas: state p1, V1, T1 →(process 1, isothermal at T1) p2, V2, T1 →(process 2, adiabatic) p3, V3, T2 →(process 3, isothermal at T2) p4, V4, T2 →(process 4, adiabatic) p1, V1, T1; Processes 2 and 4 are adiabatic](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q080_7b9eed94_03112026.svg?v=7b9eed94af73)

*Pressure versus Volume graph of a reversible cycle (Carnot-type) for 1.0 mol ideal gas: state p1, V1, T1 →[process 1, isothermal at T1] p2, V2, T1 →[process 2, adiabatic] p3, V3, T2 →[process 3, isothermal at T2] p4, V4, T2 →[process 4, adiabatic] p1, V1, T1; Processes 2 and 4 are adiabatic*

- (1) $w_1 + w_2 + w_3 + w_4 = 0$
- **(2)** $w_1 + w_3 = -2T_1 \ln\frac{V_2}{V_1} - 2T_2 \ln\frac{V_4}{V_3}$
- (3) $w_2 + w_4 = \Delta U_2 - \Delta U_4$
- (4) $w_1 + w_2 = 2T_1 \ln\frac{V_2}{V_1}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The figure is a Carnot cycle: processes $1$ and $3$ are reversible isothermals at $T_1$ and $T_2$; processes $2$ and $4$ are adiabatic.
2. With $w$ as work done on the gas, a reversible isothermal gives $w = -nRT\ln\frac{V_f}{V_i}$.
3. $w_1 = -(1)(2)T_1\ln\frac{V_2}{V_1} = -2T_1\ln\frac{V_2}{V_1}$.
4. $w_3 = -(1)(2)T_2\ln\frac{V_4}{V_3} = -2T_2\ln\frac{V_4}{V_3}$.
5. $w_1 + w_3 = -2T_1\ln\frac{V_2}{V_1} - 2T_2\ln\frac{V_4}{V_3}$, which is option $2$.
6. Check option $3$: for adiabatic steps $q=0$, so $w_2 = \Delta U_2 = C_V(T_2 - T_1)$ and $w_4 = \Delta U_4 = C_V(T_1 - T_2) = -\Delta U_2$; hence $w_2 + w_4 = 0 \neq \Delta U_2 - \Delta U_4 = 2\Delta U_2$.
7. Check option $1$: over the cycle $\Delta U = 0$, so $\sum w = -(q_1 + q_3) \neq 0$ since the cycle encloses non-zero area.
8. Check option $4$: $w_1 + w_2 = -2T_1\ln\frac{V_2}{V_1} + \Delta U_2 \neq 2T_1\ln\frac{V_2}{V_1}$; so option $2$ is correct.

**Subtopic:** Pressure–Volume Work for Isothermal Reversible Process · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 12)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q080_6ca3ba8f_03112026.png?v=6ca3ba8fce17)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Work is a path function: round a cycle the internal energy returns to its starting value but the work does not, and each isothermal leg contributes $-nRT\ln(V_f/V_i)$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The cyclic property $\Delta U = 0$ is carried across to the work, so the four work terms are set to sum to zero.
- **Why:** This question requires work expressions derived for each leg of the printed cycle, demonstrated by the options being symbolic equations in $T_1$, $T_2$ and the four volumes with R replaced by the stated value 2.
- **Note:** Which legs are isothermal and which adiabatic is fixed by the figure, which was supplied to this step only as a transcription (a clockwise p-V loop with processes 1 and 3 joining states of equal temperature and the caption 'Processes 2 and 4 are adiabatic'). The tags rest on that transcription.
<!--/ecat-->

## Q81

Chemistry · physical · Solutions

In the light of the above statements, choose the most appropriate answer from the options given below.

- (Assertion A) For an ideal solution formed by mixing liquids P and Q, $\Delta_{\mathrm{mix}}H = 0$ and $\Delta_{\mathrm{mix}}V = 0$
- (Reason R) No interactions occur between P and Q

- (1) A is not correct but R is correct
- (2) Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are correct but R is NOT the correct explanation of A
- **(4)** A is correct but R is not correct

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. For an ideal solution, $\Delta_{\mathrm{mix}}H = 0$ and $\Delta_{\mathrm{mix}}V = 0$, so Assertion A is correct.
2. In an ideal solution the $P\text{-}Q$ interactions are of the same magnitude as the $P\text{-}P$ and $Q\text{-}Q$ interactions; they are not absent, so Reason R is incorrect.
3. A correct and R not correct corresponds to option $4$.

**Subtopic:** Ideal and Nonideal Solutions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q081_8bad0fe7_03112026.png?v=8bad0fe7889d)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** An ideal solution shows $\Delta_{\mathrm{mix}}H = 0$ and $\Delta_{\mathrm{mix}}V = 0$ because the P-Q interaction is as strong as the P-P and Q-Q interactions, not because interactions are absent
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  'No interactions' is the true defining condition of the ideal gas, carried across to the ideal solution, and once R is read as correct it looks like exactly the thing that would make both $\Delta_{\mathrm{mix}}H$ and $\Delta_{\mathrm{mix}}V$ vanish
- **Why:** This question requires the reason NCERT gives for an ideal solution's zero enthalpy and volume of mixing, demonstrated by Reason R reading 'No interactions occur between P and Q' in place of interactions of equal magnitude.
<!--/ecat-->

## Q82

Chemistry · inorganic · Coordination Compounds – Practice

Among the species given below, the spin-only magnetic moment is highest for (Given : Atomic number of $\mathrm{Ti} = 22$, $\mathrm{Mn} = 25$, $\mathrm{Fe} = 26$ and $\mathrm{Co} = 27$)

- (1) $\mathrm{[Ti(H_2O)_6]^{3+}}$
- **(2)** $\mathrm{[Mn(CN)_6]^{3-}}$
- (3) $\mathrm{[Fe(CN)_6]^{3-}}$
- (4) $\mathrm{[Co(NH_3)_6]^{3+}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $\mathrm{[Ti(H_2O)_6]^{3+}}$: $\mathrm{Ti^{3+}}$ is $3d^1$, so $n = 1$ and $\mu = \sqrt{1(1+2)} = 1.73$ BM.
2. $\mathrm{[Mn(CN)_6]^{3-}}$: $\mathrm{Mn^{3+}}$ is $3d^4$; $\mathrm{CN^-}$ is strong field, giving $t_{2g}^4 e_g^0$ with $n = 2$.
3. $\mu = \sqrt{2(2+2)} = \sqrt{8} = 2.83$ BM for the Mn complex.
4. $\mathrm{[Fe(CN)_6]^{3-}}$: $\mathrm{Fe^{3+}}$ is $3d^5$, low spin $t_{2g}^5$, so $n = 1$ and $\mu = 1.73$ BM.
5. $\mathrm{[Co(NH_3)_6]^{3+}}$: $\mathrm{Co^{3+}}$ is $3d^6$, low spin $t_{2g}^6$, so $n = 0$ and $\mu = 0$.
6. Highest is $2.83$ BM for $\mathrm{[Mn(CN)_6]^{3-}}$, which is option $2$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 13)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q082_47e72210_03112026.png?v=47e722108297)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The spin-only moment is set by the number of unpaired electrons, and strong field ligands such as cyanide and ammonia pair electrons up before the count is made
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Iron(III) is read as a free $d^5$ ion with five unpaired electrons, the largest count available, because the cyanide printed in the formula is not allowed to pair them.
- **Why:** This question requires the field strength of each printed ligand applied before the unpaired electrons are counted, demonstrated by three of the four complexes carrying cyanide or ammonia rather than water.
<!--/ecat-->

## Q83

Chemistry · physical · Thermodynamics

A protein undergoes reversible thermal denaturation from its state N to denatured state D according to $\mathrm{N \rightleftharpoons D}$. At $60^\circ\mathrm{C}$, the concentrations of both N and D are equal at equilibrium, and the standard enthalpy change of denaturation of $666\,\mathrm{kJ\,mol^{-1}}$. The standard entropy change ($\Delta S^\circ$ in $\mathrm{kJ\,K^{-1}mol^{-1}}$) of the protein upon denaturation at $60^\circ\,\mathrm{C}$ is closest to:

- (1) $11.1$
- **(2)** $2.0$
- (3) $2000.0$
- (4) $333.0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Equal concentrations of N and D at equilibrium give $K = \frac{[\mathrm{D}]}{[\mathrm{N}]} = 1$.
2. $\Delta G^\circ = -RT\ln K = -RT\ln 1 = 0$.
3. $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ = 0 \Rightarrow \Delta S^\circ = \frac{\Delta H^\circ}{T}$.
4. $T = 60 + 273 = 333\,\mathrm{K}$.
5. $\Delta S^\circ = \frac{666\,\mathrm{kJ\,mol^{-1}}}{333\,\mathrm{K}} = 2.0\,\mathrm{kJ\,K^{-1}mol^{-1}}$, which is option $2$.

**Subtopic:** Gibbs Energy and Spontaneity · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 13)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q083_5a317ee8_03112026.png?v=5a317ee81d31)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Equal concentrations of the two states mean K = 1 and $\Delta G^\circ = 0$, so $\Delta S^\circ = \Delta H^\circ / T$ with T in kelvin
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The temperature is taken straight from the stem in degrees Celsius, and $666/60$ gives exactly the printed 11.1.
- **Why:** This question requires $\Delta S^\circ$ computed from $\Delta G^\circ = 0$, demonstrated by the stem stating that 'the concentrations of both N and D are equal at equilibrium' at a temperature printed in degrees Celsius.
<!--/ecat-->

## Q84

Chemistry · inorganic · The D- and F-Block Elements – Practice

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R. In light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) Generally, 3d transition metals have high melting points.
- (Reason R) Involvement of 3d-electrons in addition to 4s-electrons in the interatomic metallic bonding.

- (1) A is not correct but R is correct.
- **(2)** Both A and R are correct and R is the correct explanation of A.
- (3) Both A and R are correct and R is NOT the correct explanation of A.
- (4) A is correct but R is not correct.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Assertion A is true: 3d transition metals generally have high melting points.
2. Reason R is true: unpaired $(n-1)d$ electrons join the $ns$ electrons in interatomic metallic bonding, giving strong metallic bonds.
3. Strong metallic bonding is the cause of the high melting points, so R correctly explains A, which is option $2$.

**Subtopic:** Transition Elements (d-Block) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q084_57b1547d_03112026.png?v=57b1547d1aa0)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Transition metals melt high because electrons from the 3d shell join the 4s electrons in the metallic bond, and the word 'generally' covers Zn, Cd and Hg, whose filled d shell stays out of the bonding
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The assertion is hedged with 'Generally', and a student who holds the Zn, Cd and Hg exception reads past the hedge, grades the assertion false on those three metals and keeps the reason, which they recognise
- **Why:** This question requires the reason NCERT gives for the high melting points of the transition metals, demonstrated by Reason R reading 'Involvement of 3d-electrons in addition to 4s-electrons in the interatomic metallic bonding'.
<!--/ecat-->

## Q85

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Given below are two statements : One is labelled as Assertion A and the other is labelled as Reason R. In light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) The first ionization enthalpy of $\mathrm{O}$ is lower than that of $\mathrm{N}$ and $\mathrm{F}$.
- (Reason R) The loss of an electron from $\mathrm{O}$ leads to stable half-filled $p$ orbital.

- (1) A is not correct but R is correct.
- **(2)** Both A and R are correct and R is the correct explanation of A.
- (3) Both A and R are correct and R is NOT the correct explanation of A.
- (4) A is correct but R is not correct.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Configurations: $\mathrm{N}: 2s^2 2p^3$, $\mathrm{O}: 2s^2 2p^4$, $\mathrm{F}: 2s^2 2p^5$.
2. $\mathrm{N}$ has a stable half-filled $2p^3$ shell, so $IE_1(\mathrm{N}) > IE_1(\mathrm{O})$.
3. $\mathrm{F}$ has higher effective nuclear charge, so $IE_1(\mathrm{F}) > IE_1(\mathrm{O})$; Assertion A is correct.
4. $\mathrm{O} \rightarrow \mathrm{O^+} + e^-$ gives $\mathrm{O^+}: 2s^2 2p^3$, a stable half-filled $p$ subshell; Reason R is correct.
5. The ease of reaching the half-filled $2p^3$ state (equivalently, relief of paired-electron repulsion in $2p^4$) is why $\mathrm{O}$ ionises more easily, so R explains A: option $2$.

**Subtopic:** Trends in Chemical Properties – Ionization Enthalpy · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 13)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q085_eab24adc_03112026.png?v=eab24adc7d34)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Oxygen's 2p$^4$ loses one electron to give a half-filled 2p$^3$ cation, which is why its first ionisation enthalpy dips below nitrogen's and stays below fluorine's
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Half-filled stability is remembered as nitrogen's property, 2p$^3$ in the atom, so a reason that puts the half-filled p shell on the oxygen side reads as the fact attached to the wrong element and is graded incorrect
- **Why:** This question requires the reason NCERT gives for the dip in oxygen's first ionisation enthalpy, demonstrated by Reason R reading 'The loss of an electron from O leads to stable half-filled p orbital' while the assertion compares O with both N and F.
<!--/ecat-->

## Q86

Chemistry · organic · Hydrocarbons

Consider the following reaction sequences and choose the correct option.

![printed figure: 1-phenylpropyne →(H₂, Pd/C (Lindlar's Catalyst)) K; K →(HBr) M; 1-phenylpropyne →(Na/liq. NH₃) L; L →(HBr, benzoyl peroxide) N](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q086_75491622_03112026.svg?v=754916223117)

*1-phenylpropyne →[H₂, Pd/C (Lindlar's Catalyst)] K; K →[HBr] M; 1-phenylpropyne →[Na/liq. NH₃] L; L →[HBr, benzoyl peroxide] N*

![drawn: 1-phenylpropyne →(H₂, Pd/C (Lindlar's Catalyst)) K; K →(HBr) M; 1-phenylpropyne →(Na/liq. NH₃) L; L →(HBr, benzoyl peroxide) N](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q086_question_75f2df85_03112026.svg?v=75f2df85ed1c)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 1-phenylpropyne `CC#Cc1ccccc1` ![1-phenylpropyne](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q086_question_s1_f6e523d9_03112026.svg?v=f6e523d95aa6)

- (1) M and N are stereoisomers
- **(2)** K and L are geometrical isomers
- (3) K and L are enantiomers
- (4) M and N are geometrical isomers

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Lindlar's catalyst gives syn addition: $K = cis\text{-}Ph\text{-}CH{=}CH\text{-}CH_3$.
2. $Na/liq.\,NH_3$ gives anti addition: $L = trans\text{-}Ph\text{-}CH{=}CH\text{-}CH_3$.
3. $K$ and $L$ differ only in arrangement about the $C{=}C$, so they are geometrical isomers.
4. $K + HBr$ (ionic) goes via the benzylic carbocation: $M = Ph\text{-}CHBr\text{-}CH_2\text{-}CH_3$.
5. $L + HBr$/benzoyl peroxide goes via the benzylic radical, Br on the other carbon: $N = Ph\text{-}CH_2\text{-}CHBr\text{-}CH_3$.
6. $M$ and $N$ are position isomers, not stereoisomers or geometrical isomers; $K$ and $L$ are not enantiomers. Answer is option $2$.

**Subtopic:** Preparation of Alkenes, Isomerism · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 13)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q086_6bf5a7a5_03112026.png?v=6bf5a7a505fe)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Lindlar hydrogenation gives the cis alkene and sodium in liquid ammonia the trans alkene, so the two products of the alkyne are geometrical isomers
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  The peroxide is read as changing the face the HBr adds to rather than the carbon it adds at, so M and N come out as the same bromide with different stereochemistry and are called stereoisomers.
- **Why:** This question requires the products of four printed reactions worked out before any relationship can be named, demonstrated by the scheme giving only reagents - 'H2, Pd/C (Lindlar's Catalyst)', 'Na/liq. NH3', 'HBr' and 'HBr, benzoyl peroxide' - and labelling the products K, L, M and N.
- **Note:** The scheme was supplied as a transcription naming 1-phenylpropyne and the four reagent sets; the structures of K, L, M and N are not drawn in the record and were worked out from those reagents.
<!--/ecat-->

## Q87

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The highest occupied molecular orbital of $\mathrm{Ne_2}$ is:

- **(1)** $\sigma^{*}_{2p}$
- (2) $\pi_{2p}$
- (3) $\sigma_{2p}$
- (4) $\pi^{*}_{2p}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\mathrm{Ne_2}$ has $2 \times 10 = 20$ electrons.
2. For $Z > 7$ the order is $\sigma_{1s} < \sigma^{*}_{1s} < \sigma_{2s} < \sigma^{*}_{2s} < \sigma_{2p_z} < \pi_{2p_x}=\pi_{2p_y} < \pi^{*}_{2p_x}=\pi^{*}_{2p_y} < \sigma^{*}_{2p_z}$.
3. Filling 20 electrons: $\sigma_{1s}^2\,\sigma_{1s}^{*2}\,\sigma_{2s}^2\,\sigma_{2s}^{*2}\,\sigma_{2p_z}^2\,\pi_{2p_x}^2\,\pi_{2p_y}^2\,\pi_{2p_x}^{*2}\,\pi_{2p_y}^{*2}\,\sigma_{2p_z}^{*2}$.
4. The last orbital filled is $\sigma^{*}_{2p}$, so it is the HOMO, which is option $1$.

**Subtopic:** Energy Level Diagram for Molecular Orbitals · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q087_8fa68e65_03112026.png?v=8fa68e65683f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Neon contributes eight valence electrons each, so all sixteen fill the diagram to the top and the last pair sits in the antibonding $\sigma^*_{2p}$
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  $\pi^*_{2p}$ is the highest filled level in oxygen and fluorine, the two molecules the molecular orbital diagram is worked through for, so the answer for the neighbouring molecule is handed over unchanged.
- **Why:** This question requires the filling rule applied to a molecule whose diagram is not drawn out in the text, demonstrated by the stem naming $\mathrm{Ne_2}$ while the four options are the four candidate top levels of the same diagram.
- **Note:** Each wrong option is the highest occupied level of a different second-row diatomic - $\pi^*_{2p}$ for $\mathrm{O_2}$ and $\mathrm{F_2}$, $\sigma_{2p}$ for $\mathrm{N_2}$, $\pi_{2p}$ for $\mathrm{C_2}$ - which is why the trap was read as positional rather than as a resemblance between the symbols: replacing the labels with unlike words leaves the pull intact, because the student is answering for the neighbouring molecule.
<!--/ecat-->

## Q88

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match the species in List I with their geometry in List II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | $\mathrm{PCl_5}$ | I | Tetrahedral |
| B | $\mathrm{BrF_5}$ | II | Square Planar |
| C | $\mathrm{BF_4^-}$ | III | Trigonal bipyramidal |
| D | $\mathrm{[Ni(CN)_4]^{2-}}$ | IV | Square pyramidal |

- (1) A-III, B-II, C-I, D-IV
- (2) A-IV, B-III, C-I, D-II
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-III, B-I, C-II, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\mathrm{PCl_5}$: P has 5 bond pairs and 0 lone pairs, $sp^3d$, so trigonal bipyramidal: A-III.
2. $\mathrm{BrF_5}$: Br has 5 bond pairs and 1 lone pair, $sp^3d^2$, so square pyramidal: B-IV.
3. $\mathrm{BF_4^-}$: B has 4 bond pairs and 0 lone pairs, $sp^3$, so tetrahedral: C-I.
4. $\mathrm{[Ni(CN)_4]^{2-}}$: $\mathrm{Ni^{2+}}$ is $d^8$; strong-field $\mathrm{CN^-}$ pairs the electrons, giving $dsp^2$, so square planar: D-II.
5. A-III, B-IV, C-I, D-II matches option $3$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory, Hybridisation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q088_55acf92b_03112026.png?v=55acf92b6702)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Geometry follows from counting bond pairs and lone pairs: five bonds give trigonal bipyramidal, five bonds plus a lone pair give square pyramidal, four bonds give tetrahedral, and a $dsp^2$ four-coordinate nickel(II) cyanide complex is square planar
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Square planar and square pyramidal are filed together as 'the square ones', so once $\mathrm{PCl_5}$ and $\mathrm{BF_4^-}$ are placed the two remaining rows get the two square names the wrong way round
- **Why:** This question requires the electron-pair count applied to each formula to fix its shape, demonstrated by List I pairing $\mathrm{BrF_5}$ against List II's 'Square pyramidal' and 'Trigonal bipyramidal'.
- **Note:** asks is apply_rule rather than compare: each row hands over a formula and asks what geometry the pair count gives, which is a rule used on the case rather than two look-alike quantities being told apart.
<!--/ecat-->

## Q89

Chemistry · organic · Biomolecules

Match the vitamins in List-I with their sources in List-II
Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A | vitamin A | I | meat |
| B | vitamin $\mathrm{B_{12}}$ | II | sunflower oil |
| C | vitamin E | III | green leafy vegetables |
| D | vitamin K | IV | carrots |

- (1) A-III, B-I, C-IV, D-II
- (2) A-II, B-III, C-IV, D-I
- **(3)** A-IV, B-I, C-II, D-III
- (4) A-IV, B-II, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Vitamin A (via $\beta$-carotene) comes from carrots: $A \to IV$.
2. Vitamin $\mathrm{B_{12}}$ comes from animal foods such as meat: $B \to I$.
3. Vitamin E is abundant in vegetable oils such as sunflower oil: $C \to II$.
4. Vitamin K comes from green leafy vegetables: $D \to III$.
5. $A$-$IV$, $B$-$I$, $C$-$II$, $D$-$III$ is option $3$.

**Subtopic:** Vitamins Classification and Uses · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 13)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q089_79c3a4ae_03112026.png?v=79c3a4ae134f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The source the chapter prints for each vitamin: carrots for A, meat for $\mathrm{B_{12}}$, vegetable oils such as sunflower oil for E, and green leafy vegetables for K
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Green leafy vegetables really are a source of vitamin A, so a student who pairs A with III is pairing two things that genuinely go together — but the printed list keeps III for vitamin K and carrots for A, and the rest of the row assignments then have to be forced
- **Why:** This question requires the source NCERT prints for each named vitamin, demonstrated by List II offering 'carrots' and 'green leafy vegetables' as separate entries that both bear on vitamin A.
- **Note:** asks is fact_line rather than compare: each row asks for a source the chapter states, and compare on this printing would only restate the pairing that qtype match_columns already records.
<!--/ecat-->

## Q90

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

For the following reaction sequence, choose the correct option.

![printed figure: benzene →(i. $\ce{CH3COCl}$, $\ce{AlCl3}$; ii. $\ce{NaOCl}$) P + Q](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_agent/q090_a42e7ccc_03112026.svg?v=a42e7ccc1525)

*benzene →[i. $\ce{CH3COCl}$, $\ce{AlCl3}$; ii. $\ce{NaOCl}$] P + Q*

![drawn: benzene →(i. $\ce{CH3COCl}$, $\ce{AlCl3}$; ii. $\ce{NaOCl}$) P + Q](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q090_question_09051637_03112026.svg?v=0905163716e2)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/figures_drawn/q090_question_s1_85a743fb_03112026.svg?v=85a743fbf5b1)

- (1) Both P and Q are carbonyl compounds.
- (2) If P is the sodium salt of a carboxylic acid, Q is a primary alcohol.
- (3) P and Q are aromatic compounds.
- **(4)** If P gives a carboxylic acid on acidification, Q gives a poisonous gas on exposure to air and light.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Friedel-Crafts acylation: $\mathrm{C_6H_6 + CH_3COCl \xrightarrow{AlCl_3} C_6H_5COCH_3}$ (acetophenone).
2. Haloform reaction of the methyl ketone with $\mathrm{NaOCl}$: $\mathrm{C_6H_5COCH_3 \xrightarrow{NaOCl} C_6H_5COONa + CHCl_3}$, so $P = \mathrm{C_6H_5COONa}$ and $Q = \mathrm{CHCl_3}$.
3. Acidifying $P$ gives benzoic acid $\mathrm{C_6H_5COOH}$, a carboxylic acid.
4. $Q$ in air and light: $\mathrm{2CHCl_3 + O_2 \xrightarrow{h\nu} 2COCl_2 + 2HCl}$, giving poisonous phosgene.
5. Options 1, 2 and 3 fail ($P$ is a carboxylate salt, $Q$ is not an alcohol and is not aromatic), so option $4$.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 13)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q090_25ca44cf_03112026.png?v=25ca44cf5320)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Friedel-Crafts acylation gives acetophenone, and sodium hypochlorite then runs the haloform reaction on it: the products are sodium benzoate and chloroform
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The hypochlorite step is read as a disproportionation of the Cannizzaro kind, which does give a carboxylate salt and an alcohol, so the first half of the option is set down correctly and the second half follows the wrong reaction.
- **Why:** This question requires the products of a two-step sequence worked out before any option can be graded, demonstrated by the scheme printing only the reagents 'i. CH3COCl, AlCl3' and 'ii. NaOCl' with the products left as P and Q.
- **Note:** The pattern label arrange_in_order came from the words 'reaction sequence' in the stem and contradicts the printed shape: nothing is to be sequenced and each option is a standalone claim to be graded, so qtype statements is recorded. The scheme was supplied as a transcription (benzene with those two reagent sets giving P + Q).
<!--/ecat-->

## Q91

Biology · zoology · Animal Kingdom

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) The class name Reptilia refers to creeping or crawling mode of locomotion.
- (Statement II) All organisms belonging to Reptilia have three chambered heart.

- (1) Statement I is incorrect but Statement II is correct.
- (2) Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- **(4)** Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: the name Reptilia refers to the creeping or crawling mode of locomotion, so it is correct.
2. Statement II: reptiles usually have a three-chambered heart, but crocodiles have a four-chambered heart, so 'all' makes it incorrect.
3. Statement I correct and Statement II incorrect, which is option $4$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q091_f94ef1f6_03112026.png?v=f94ef1f6c9be)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The class name Reptilia comes from the Latin for creeping, and the reptilian heart is usually three-chambered but four-chambered in crocodiles
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The heart of a reptile is printed as usually three-chambered, and Statement II says all of them are; a student who holds the general rule and reads past the word 'All' marks the statement correct and takes both correct
- **Why:** This question requires two printed lines about a named class to be checked, demonstrated by 'All organisms belonging to Reptilia have three chambered heart'.
- **Note:** condition_missed is used in its operational sense: drop the quantifier 'All' and the statement becomes true, and the counter-example that falsifies it as printed is the crocodile's four-chambered heart.
<!--/ecat-->

## Q92

Biology · botany · Photosynthesis in Higher Plants

How many turns of Calvin cycle are required for the formation of three molecules of glucose ?

- **(1)** $18$
- (2) $6$
- (3) $3$
- (4) $1$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Each turn of the Calvin cycle fixes one $CO_2$, so one glucose ($C_6H_{12}O_6$) needs $6$ turns.
2. For three glucose molecules: $3 \times 6 = 18$ turns, which is option $1$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q092_e30eab7f_03112026.png?v=e30eab7f5dba)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Six turns of the Calvin cycle fix six CO2 into one glucose, so the number of turns scales with the number of glucose molecules asked for
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Six is the turn count carried for one glucose, and a student who recalls that figure reports it without multiplying by the stem's three, so the factor of 3 is dropped and 6 is printed as an option
- **Why:** This question requires multiplying the stored per-glucose turn count by the number the stem supplies, demonstrated by 'required for the formation of three molecules of glucose'.
<!--/ecat-->

## Q93

Biology · botany · Photosynthesis in Higher Plants

Photorespiration reaction catalyzed by RuBisCo is shown below: $\mathrm{RuBP} + \mathrm{O_2} \rightarrow \text{3-Phosphoglycerate} + \mathrm{X}$ Identify “X” from the given options:

- (1) Malate
- (2) Phosphoenolpyruvate
- **(3)** 2-phosphoglycolate
- (4) Oxaloacetate

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In photorespiration RuBisCO acts as an oxygenase: $\mathrm{RuBP}\,(5C) + \mathrm{O_2} \rightarrow \text{3-PGA}\,(3C) + \text{2-phosphoglycolate}\,(2C)$, so $X$ is 2-phosphoglycolate, option $3$.

**Subtopic:** Photorespiration · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q093_2ba481d0_03112026.png?v=2ba481d0367a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** When RuBisCO binds O2 instead of CO2, RuBP is split into one 3-phosphoglycerate and one 2-phosphoglycolate, with no sugar and no energy gained
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Oxaloacetate is the first product of the other carbon-fixing reaction the same chapter prints, PEP plus CO2 in C4 plants, so a student who holds 'the first product is OAA' from that reaction attaches it to this one
- **Why:** This question requires naming the missing product of a printed reaction, demonstrated by 'RuBP + O2 gives 3-Phosphoglycerate + X. Identify X from the given options'.
- **Note:** The pattern returned reaction_scheme, but one single-arrow reaction is printed, not a multi-arrow scheme; the current qtype is mcq either way. The swap test was applied to the trap: replacing 'oxaloacetate' with any other unlike C4 acid keeps the pull, because what carries the student is that the C4 acids are printed beside photorespiration, so it is position and not likeness.
<!--/ecat-->

## Q94

Biology · botany · Plant Kingdom

Given below are two statements:
Statement I: In gymnosperms, the male and female gametophytes remain within the sporangia.
Statement II: In gymnosperms, seeds are not covered.
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) In gymnosperms, the male and female gametophytes remain within the sporangia.
- (Statement II) In gymnosperms, seeds are not covered.

- (1) Statement I is incorrect but Statement II is correct.
- **(2)** Both Statement I and Statement II are correct.
- (3) Both Statement I and Statement II are incorrect.
- (4) Statement I is correct but Statement II is incorrect.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Statement I: in gymnosperms the male and female gametophytes have no independent free-living existence and remain within the sporangia retained on the sporophyte, so Statement I is correct.
2. Statement II: gymnosperm ovules are not enclosed in an ovary wall, so the seeds formed after fertilisation are naked (not covered), so Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Gymnosperms · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q094_bc3f9b48_03112026.png?v=bc3f9b48dfd2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperm gametophytes have no free-living existence and stay inside sporangia on the parent sporophyte, and the seeds that follow fertilisation are naked, not enclosed in a fruit
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Pollen is shed and carried to the ovule, and a student who holds that dispersal step sets it against Statement I and reads 'remain within the sporangia' as false, taking Statement I incorrect and Statement II correct
- **Why:** This question requires two printed lines about one group to be checked, demonstrated by 'the male and female gametophytes remain within the sporangia'.
<!--/ecat-->

## Q95

Biology · botany · Respiration in Plants

How many molecules of pyruvic acid are produced at the end of glycolysis from 206 molecules of glucose?

- **(1)** 412
- (2) 206
- (3) 309
- (4) 103

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Glycolysis converts one molecule of glucose ($C_6$) into two molecules of pyruvic acid ($C_3$).
2. $N_{pyruvate} = 2 \times 206 = 412$, which is option $1$.

**Subtopic:** Glycolysis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q095_e62d9d2a_03112026.png?v=e62d9d2a738b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Glycolysis splits each six-carbon glucose into two three-carbon pyruvates, so the pyruvate count is twice the glucose count
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  206 is the number the stem hands over, and a student who reads 'molecules of pyruvic acid produced from 206 molecules of glucose' as a one-for-one conversion drops the factor of 2 that the split introduces
- **Why:** This question requires scaling the stored two-pyruvate-per-glucose yield to the number given, demonstrated by 'produced at the end of glycolysis from 206 molecules of glucose'.
<!--/ecat-->

## Q96

Biology · botany · Biological Classification

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Fusion of protoplasms between gametes | I | Meiosis |
| B | Fusion of two nuclei | II | Plasmogamy |
| C | Generation of haploid spores | III | Karyogamy |

- (1) A-I, B-III, C-II
- **(2)** A-II, B-III, C-I
- (3) A-II, B-I, C-III
- (4) A-III, B-II, C-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Fusion of protoplasms between two gametes is plasmogamy, so $A \to II$.
2. Fusion of the two nuclei is karyogamy, so $B \to III$.
3. Meiosis in the zygote produces haploid spores, so $C \to I$.
4. $A$-$II$, $B$-$III$, $C$-$I$ matches option $2$.

**Subtopic:** Kingdom Fungi · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 14)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q096_94452f27_03112026.png?v=94452f27e834)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The fungal sexual cycle runs plasmogamy (protoplasms fuse), then karyogamy (nuclei fuse), then meiosis in the zygote to give haploid spores
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Both names end in -gamy and both name a fusion, so only the prefix separates them, and exchanging the prefixes leaves the one secure row (spores from meiosis) untouched. Plasma is the protoplasm and karyon the nucleus, which fixes A-II and B-III.
- **Why:** This question requires each named stage of the fungal cycle recognised from what fuses, demonstrated by List-I printing "Fusion of protoplasms between gametes" against "Fusion of two nuclei" with Plasmogamy and Karyogamy both standing in List-II. Rule 5 test applied: replace those two with unlike words and the trap dies, so the likeness of the names is doing the work, not their position.
<!--/ecat-->

## Q97

Biology · both · Cell: The Unit of Life

Mitochondrial inner membrane encloses ________.

- (1) aqueous humor
- **(2)** matrix
- (3) cytosol
- (4) mucus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The mitochondrial inner membrane forms the inner compartment, the matrix, so the answer is option $2$.

**Subtopic:** Mitochondria · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q097_00696b49_03112026.png?v=00696b49f51c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The mitochondrial inner membrane bounds the matrix; the outer membrane, the intermembrane space and the cytosol all lie outside it
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The mitochondrion sits in the cytosol, and a student who holds that relation reads 'encloses' as naming the fluid the membrane lies in, which inverts the direction of containment
- **Why:** This question requires the stated fact about which compartment the inner membrane bounds, demonstrated by the blank completing 'Mitochondrial inner membrane encloses'.
<!--/ecat-->

## Q98

Biology · botany · Morphology of Flowering Plants

Phyllotaxy is the pattern of arrangement of____.

- (1) sepals
- **(2)** leaves
- (3) flowers
- (4) fruits

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Phyllotaxy is defined as the pattern of arrangement of $\text{leaves}$ on the stem or branch (alternate, opposite, whorled), which is option $2$.

**Subtopic:** The Leaf · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q098_1efb11b1_03112026.png?v=1efb11b17331)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Phyllotaxy is the pattern in which leaves are arranged on the stem or branch, alternate, opposite or whorled
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Inflorescence is defined in the same chapter as the arrangement of flowers on the floral axis, so a student who holds that definition and not the leaf one answers the stem's 'pattern of arrangement' with flowers
- **Why:** This question requires the stated definition of a named term, demonstrated by 'Phyllotaxy is the pattern of arrangement of ____'.
- **Note:** Swap test applied: replacing 'flowers' with an unlike word keeps the pull, because what carries the student is that the chapter prints inflorescence and aestivation beside phyllotaxy, so position and not likeness decides it.
<!--/ecat-->

## Q99

Biology · botany · Biological Classification

Mad cow disease is caused by ________.

- (1) Mycoplasma sp.
- **(2)** prions
- (3) viroids
- (4) Aspergillus sp.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Mad cow disease is bovine spongiform encephalopathy (BSE), which NCERT lists as caused by prions (abnormally folded proteins), so the answer is option $2$.

**Subtopic:** Viroids, Prions & Lichens · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 14)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q099_032855b2_03112026.png?v=032855b20c3b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Prions are abnormally folded infectious proteins and cause mad cow disease, while viroids are free infectious RNA with no protein coat
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Viroids are printed in the same short passage as prions as the other acellular infectious agent, so a student who holds 'the two odd agents beside the viruses' but not which disease belongs to which takes the one named first
- **Why:** This question requires the stated causal agent of a named disorder, demonstrated by 'Mad cow disease is caused by ________'.
<!--/ecat-->

## Q100

Biology · both · Cell: The Unit of Life

Cell theory was formulated by______ .

- (1) Antonie Von Leeuwenhoek
- **(2)** Schleiden and Schwann
- (3) Robert Brown
- (4) Singer and Nicolson

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Cell theory was formulated by the botanist Schleiden and the zoologist Schwann, so the answer is option $2$.

**Subtopic:** Cell And Its Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q100_097e70c1_03112026.png?v=097e70c19a5b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cell theory was put together from Schleiden's work on plant cells and Schwann's on animal cells; Virchow later added that cells arise from pre-existing cells
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Leeuwenhoek opens the same historical paragraph as the man who first saw and described a live cell, so a student who holds 'he is the cell man' hands him the theory as well as the first sighting
- **Why:** This question requires the stated attribution of a named theory, demonstrated by 'Cell theory was formulated by______'.
- **Note:** Swap test applied: replacing 'Antonie Von Leeuwenhoek' with any unlike name keeps the pull, because what carries the student is that the chapter prints him in the same paragraph as the theory, so position and not likeness decides it.
<!--/ecat-->

## Q101

Biology · botany · Plant Growth and Development

Which of the following plant growth regulators promotes internode elongation prior to flowering in cabbage?

- (1) Ethephon
- (2) Abscisic acid
- **(3)** Gibberellin
- (4) Indole butyric acid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Internode elongation just before flowering in rosette plants like cabbage is called bolting, and it is promoted by gibberellins, so the answer is option $3$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q101_9f790a82_03112026.png?v=9f790a82cf38)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gibberellins cause bolting, the elongation of the internode just before flowering in rosette plants such as cabbage and beet
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Auxin is the regulator the chapter ties to cell elongation, so a student who holds 'elongation means auxin' reaches for the auxin on the list, indole butyric acid, instead of for the bolting line
- **Why:** This question requires the stated effect of one named regulator, demonstrated by 'promotes internode elongation prior to flowering in cabbage'.
<!--/ecat-->

## Q102

Biology · botany · Photosynthesis in Higher Plants

Which pigment has absorption peak at $700\,\mathrm{nm}$ in the photosynthetic reaction centre PS I (P700)?

- (1) Carotenoids
- (2) Chlorophyll b
- **(3)** Chlorophyll a
- (4) Xanthophylls

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The reaction centre of PS I, P700, is a special chlorophyll $a$ molecule absorbing maximally at $700\,\mathrm{nm}$, which is option $3$.

**Subtopic:** Pigments and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q102_d1493c65_03112026.png?v=d1493c656d52)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The reaction-centre pigment of both photosystems is chlorophyll a, P700 in PS I and P680 in PS II; the other pigments only harvest light and pass the energy on
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Chlorophyll a and chlorophyll b are separated by one letter and are printed as the first two entries of the same pigment list, so a student who holds 'the reaction centre is a chlorophyll' and not which one takes the other letter
- **Why:** This question requires the stated identity of a named reaction-centre pigment, demonstrated by 'absorption peak at 700 nm in the photosynthetic reaction centre PS I (P700)'.
- **Note:** Swap test applied: replacing 'Chlorophyll b' with an unlike pigment name kills the pull, because the two names differ by a single letter and that is what the student has to choose between, so likeness is carrying it.
<!--/ecat-->

## Q103

Biology · botany · Plant Kingdom

Sphenopsida class belongs to ______.

- **(1)** pteridophytes
- (2) bryophytes
- (3) angiosperms
- (4) gymnosperms

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT divides pteridophytes into four classes: Psilopsida, Lycopsida, Sphenopsida and Pteropsida, with Sphenopsida represented by $Equisetum$, so the answer is option $1$.

**Subtopic:** Pteridophytes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q103_4c95e9dd_03112026.png?v=4c95e9dda2fa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pteridophyta is divided into the classes Psilopsida, Lycopsida, Sphenopsida and Pteropsida, so a class name ending in -opsida belongs there
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Sphagnum is the moss the plant-kingdom chapter names for peat, and a student who reads the unfamiliar 'Sphenopsida' as that same Sph- word files it with the mosses, which are the bryophytes
- **Why:** This question requires filing a named class into the printed group it belongs to, demonstrated by 'Sphenopsida class belongs to ______'.
- **Note:** Swap test applied: replacing 'Sphenopsida' in the stem with 'Lycopsida' kills the bryophyte pull, so the resemblance to Sphagnum and not the position in the taught sequence is what carries the student.
<!--/ecat-->

## Q104

Biology · zoology · Locomotion and Movement

Which of the following represents the correct sequence of arrangement of bones in the lower limb of humans?

- (1) Femur-tarsal-patella-tibia
- (2) Femur-tibia-patella-tarsal
- (3) Patella-femur-tibia-tarsal
- **(4)** Femur-patella-tibia-tarsal

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Going from proximal to distal in the lower limb: $\text{femur} \rightarrow \text{patella (knee)} \rightarrow \text{tibia} \rightarrow \text{tarsals (ankle)}$, which is option $4$.

**Subtopic:** Appendicular Skeleton · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q104_c516a702_03112026.png?v=c516a7020478)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The bones of the lower limb run femur, then the patella at the knee, then tibia and fibula, then the tarsals of the ankle
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The printed list of leg bones runs femur, tibia and fibula, tarsals, and the patella is described in a separate sentence as covering the knee, so a student who builds the chain from the list and then drops the patella in afterwards puts it past the tibia
- **Why:** This question requires a printed sequence to be reproduced in order, demonstrated by 'the correct sequence of arrangement of bones in the lower limb'.
- **Note:** half_right is used because the option carries four parts and fails on one adjacency, the patella and tibia pair, while keeping the femur and tarsal ends right; no option in this set prints the exact reverse of the key.
<!--/ecat-->

## Q105

Biology · botany · Plant Growth and Development

Which of the following plant growth regulators is used as herbicide ?

- (1) Gibberellin
- **(2)** 2,4-D
- (3) Kinetin
- (4) Abscisic acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Among the options, $2,4\text{-D}$ (a synthetic auxin) is used as a herbicide to kill dicot weeds in monocot crops, which is option $2$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q105_e96a399d_03112026.png?v=e96a399dfc29)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** 2,4-D is the synthetic auxin used to kill dicot weeds, the one herbicidal use the growth-regulator section gives
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Abscisic acid is the growth inhibitor of the printed list, so a student who reads 'herbicide' as 'the regulator that stops growth' reaches for the inhibitor rather than for the weedkiller the chapter names
- **Why:** This question requires the stated use of one named regulator, demonstrated by 'Which of the following plant growth regulators is used as herbicide'.
<!--/ecat-->

## Q106

Biology · botany · The Living World

Genus represents ________.

- (1) a group of closely related families
- (2) an individual plant or animal
- (3) a population of plants and animals
- **(4)** a group of closely related species

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In NCERT's taxonomic hierarchy, a genus comprises a group of related species that share more characters with each other than with species of other genera, so the answer is option $4$.

**Subtopic:** Family, Genus and Species · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q106_049eef7c_03112026.png?v=049eef7c806f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each taxonomic rank is defined by the rank below it: a genus is a group of closely related species, and a family is a group of related genera
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The hierarchy is learnt as the same sentence repeated up the ranks, 'a group of closely related ___', so a student who holds the sentence form but slips one rank fills the blank with families, which is the definition of the rank two steps above
- **Why:** This question requires the stated definition of a taxonomic rank, demonstrated by 'Genus represents ________'.
- **Note:** Swap test applied: replacing 'families' with an unlike word keeps the pull, because what carries the student is the rank printed next to the right one in the hierarchy, so position and not likeness decides it.
<!--/ecat-->

## Q107

Biology · botany · Cell: The Unit of Life

The plastid that stores xanthophyll is known as

- (1) amyloplast
- (2) chloroplast
- **(3)** chromoplast
- (4) aleuroplast

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Per NCERT, chromoplasts store fat-soluble carotenoid pigments such as carotene and xanthophylls, so the answer is option $3$ (chromoplast).

**Subtopic:** Plastids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q107_6f751bfc_03112026.png?v=6f751bfca2f8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plastids are classified by what they hold: chromoplasts carry the fat-soluble carotenoid pigments including xanthophyll, while amyloplasts, elaioplasts and aleuroplasts are colourless food stores
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Chloroplasts do carry xanthophyll beside their chlorophyll, so the option is true of where the pigment is found in a green leaf; what the stem asks for is the plastid type that is named for holding the carotenoid pigments
- **Why:** This question requires the plastid type that is classified by its stored pigment, demonstrated by 'The plastid that stores xanthophyll is known as'.
- **Note:** Carotenoid pigments are also printed as present in chloroplasts, so on a literal reading of 'stores' option 2 is defensible; the rating follows the printed key and records the doubt here rather than re-judging it.
<!--/ecat-->

## Q108

Biology · zoology · Structural Organisation in Animals

In water, frogs respire using ____.

- (1) trachea
- **(2)** skin
- (3) buccal cavity
- (4) lungs

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT: in water the frog's skin acts as the respiratory organ (cutaneous respiration), so the answer is option $2$.

**Subtopic:** Anatomy of Frog · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q108_86181a43_03112026.png?v=86181a43b02c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The frog breathes through its skin when in water, and through the buccal cavity, skin and lungs when on land
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Lungs are the frog's respiratory organ on land, so dropping the stem's 'In water' makes the option true; a student who answers 'how does a frog breathe' rather than the question as printed names the lungs
- **Why:** This question requires the stated organ under the condition the stem sets, demonstrated by 'In water, frogs respire using ____'.
<!--/ecat-->

## Q109

Biology · zoology · Animal Kingdom

Which of the following is not a characteristic of chordates?

- (1) Presence of post anal part (tail)
- (2) Presence of notochord
- (3) Central nervous system is dorsal
- **(4)** Absence of gills

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. NCERT chordate characters: notochord present, dorsal hollow single central nervous system, paired pharyngeal gill slits present, post-anal part (tail) present; so 'Absence of gills' (option $4$) is not a characteristic.

**Subtopic:** Phylum – Chordata · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q109_baa67cbc_03112026.png?v=baa67cbc91c4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The chordate characters are a notochord, a dorsal hollow nerve cord and paired pharyngeal gill slits, so gills are present in chordates rather than absent
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Drop the stem's 'not' and the notochord option becomes the pick: it is the character whose name is inside the word 'chordates', so it is the option a student reaching for a chordate feature confirms first
- **Why:** This question requires the stated diagnostic features of a named group under a negated task, demonstrated by 'Which of the following is not a characteristic of chordates'.
- **Note:** Option 1 names a true chordate character that the printed three-feature sentence does not list, so the route to it is a real one that the trap axis has no value for; it is recorded in full under other_options rather than forced into a label.
<!--/ecat-->

## Q110

Biology · both · Cell: The Unit of Life

Smooth endoplasmic reticulum____.

- (1) is a site for the synthesis of carbohydrates
- (2) has ribosomes attached to its surface
- **(3)** is the major site for the synthesis of lipids
- (4) is actively involved in protein synthesis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Smooth ER has no ribosomes on its surface and is the major site of lipid synthesis (steroidal hormones in animal cells), so option $3$ is correct while options $2$ and $4$ describe rough ER.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q110_8eff14f3_03112026.png?v=8eff14f30cec)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The endoplasmic reticulum comes in two forms: rough ER carries ribosomes and handles protein synthesis, smooth ER has none and is the main site of lipid synthesis
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Protein synthesis is the function printed for the rough ER in the sentence immediately beside the one about lipids, so a student who holds both functions but not which form owns which takes the neighbour
- **Why:** This question requires the stated function of one named form of an organelle, demonstrated by the option 'is the major site for the synthesis of lipids' completing 'Smooth endoplasmic reticulum____'.
- **Note:** The options are predicates completing a printed blank rather than statements the stem asks to be judged, so the qtype stays mcq.
<!--/ecat-->

## Q111

Biology · both · Cell: The Unit of Life

Which of the following are characteristics of prokaryotic cells ? Choose the correct answer from the options given below :

- (a) Ribosomes are made of $50\mathrm{S}$ and $30\mathrm{S}$ subunits
- (b) They can have plasmids
- (c) They contain mesosome
- (d) They have peroxisomes

- **(1)** (a), (b) and (c) only
- (2) (b) and (c) only
- (3) (a) and (c) only
- (4) (a), (c) and (d) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. (a) Prokaryotic ribosomes are $70\mathrm{S}$, made of $50\mathrm{S}$ and $30\mathrm{S}$ subunits, so (a) is true.
2. (b) Many bacteria carry plasmids (extrachromosomal circular DNA), so (b) is true.
3. (c) Mesosomes, infoldings of the plasma membrane, are characteristic of prokaryotic cells, so (c) is true.
4. (d) Peroxisomes are membrane-bound organelles absent in prokaryotes, so (d) is false.
5. The true statements are (a), (b) and (c), which is option $1$.

**Subtopic:** Prokaryotic Cells And Its Modification · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q111_0004605b_03112026.png?v=0004605beac3)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A prokaryotic cell has a 70S ribosome built from 50S and 30S subunits, mesosomes formed by infolding of the plasma membrane, and often plasmids, but no membrane-bound microbodies such as peroxisomes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Statement (b) is hedged as 'They can have plasmids', so a student reading the stem's word 'characteristics' as something every prokaryote must show drops it and keeps only the two features that sound universal
- **Why:** This question requires the features NCERT lists for the prokaryotic cell, demonstrated by statement (c) 'They contain mesosome' against statement (d) 'They have peroxisomes'.
<!--/ecat-->

## Q112

Biology · both · Cell: The Unit of Life

Match List-I with List-II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Cristae | I | Flat membrane sacs in stroma of chloroplast |
| B | Cisternae | II | Infoldings in mitochondria |
| C | Thylakoids | III | Cell membrane |
| D | Phospholipid | IV | Disc shaped sacs in the Golgi apparatus |

- (1) A-IV, B-III, C-I, D-II
- (2) A-III, B-IV, C-I, D-II
- **(3)** A-II, B-IV, C-I, D-III
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Cristae are the infoldings of the inner mitochondrial membrane, so $A \rightarrow II$.
2. Cisternae are the flat disc-shaped sacs of the Golgi apparatus, so $B \rightarrow IV$.
3. Thylakoids are flat membranous sacs in the stroma of the chloroplast, so $C \rightarrow I$.
4. Phospholipids form the lipid bilayer of the cell membrane, so $D \rightarrow III$.
5. The match $A-II, B-IV, C-I, D-III$ is option $3$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 15)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q112_7340c18b_03112026.png?v=7340c18b5daa)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each membrane structure belongs to one organelle -- cristae to the mitochondrion, cisternae to the Golgi, thylakoids to the chloroplast -- while phospholipid is what the cell membrane itself is built from
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Phospholipid is what every membrane in the list is made of, so it is attached to the membrane entry that names a structure, the mitochondrial infoldings, and cristae is then left with "Cell membrane". The entry phospholipid labels here is the cell membrane, whose chief constituent it is.
- **Why:** This question requires each named structure placed in the organelle it belongs to, demonstrated by List-II giving locations -- "Infoldings in mitochondria", "Disc shaped sacs in the Golgi apparatus" -- rather than functions to compare. Rule 5 test applied: "Phospholipid" and "Cell membrane" resemble nothing in the list, so what carries the student is the adjacent entry in the same printed set of membranes, which is nearby_fact.
<!--/ecat-->

## Q113

Biology · zoology · Chemical Coordination and Integration

Which of the following statements related to pituitary gland are correct? Choose the correct answer from the options given below:

- (a) It is divided anatomically into adenohypophysis and neurohypophysis
- (b) It secretes follicle stimulating hormone
- (c) It secretes melanocyte stimulating hormone
- (d) It does not secrete prolactin

- (1) (b) and (c) only
- (2) (a) and (b) only
- **(3)** (a), (b) and (c) only
- (4) (c) and (d) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. (a) is true: anatomically the pituitary is divided into adenohypophysis and neurohypophysis; (b) is true: pars distalis secretes FSH; (c) is true: pars intermedia secretes MSH; (d) is false: pars distalis secretes prolactin, so the answer is (a), (b) and (c) only, option $3$.

**Subtopic:** The Pituitary Gland · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q113_f294d380_03112026.png?v=f294d380a834)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The pituitary is anatomically an adenohypophysis plus a neurohypophysis; pars distalis secretes FSH, prolactin, GH, TSH and ACTH, and pars intermedia secretes MSH
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  MSH is carried with the note that pars intermedia is almost merged with pars distalis in humans, so a student reads that as MSH not being a pituitary secretion and keeps only the two statements they are sure of
- **Why:** This question requires the hormones and the anatomical division NCERT assigns to the pituitary, demonstrated by statement (d) 'It does not secrete prolactin' standing against the pars distalis list that includes prolactin.
<!--/ecat-->

## Q114

Biology · botany · Photosynthesis in Higher Plants

> ⚠ The independent solve chose (1); the booklet prints (3).

Which of the following statements regarding photorespiration are correct ? Choose the correct answer from the options given below :

- (a) Do not occur in C3 plants
- (b) $\mathrm{CO_2}$ is consumed and $\mathrm{O_2}$ is generated
- (c) Phosphoglycolate is formed
- (d) No synthesis of ATP and NADPH

- (1) (c) and (d) only
- (2) (b) and (d) only
- **(3)** (a) and (b) only
- (4) (a) and (d) only

**Answer** — booklet: (3) · independent solve: (1) · differs

**Solved independently** (answer withheld)

1. Photorespiration happens in $\mathrm{C_3}$ plants because RuBisCO binds $\mathrm{O_2}$, so (a) is false.
2. In photorespiration $\mathrm{O_2}$ is consumed and $\mathrm{CO_2}$ is released, the reverse of (b), so (b) is false.
3. RuBisCO oxygenase action gives one $3$-PGA and one phosphoglycolate, so (c) is true.
4. NCERT states there is no synthesis of sugars, ATP or NADPH in photorespiration, so (d) is true.
5. Only (c) and (d) are correct, which is option $1$.

**Subtopic:** Photorespiration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q114_117248c4_03112026.png?v=117248c4734f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In photorespiration RuBisCO binds O2 instead of CO2, so phosphoglycolate is formed, O2 is used and CO2 released, and no ATP or NADPH is made; the pathway runs in C3 plants and is absent in C4
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No option's pull can be stated until the key is settled: statement (c) 'Phosphoglycolate is formed' and statement (d) 'No synthesis of ATP and NADPH' are both what the photorespiration section states, while (a) puts C3 where C4 belongs and (b) exchanges the two gases, so the set that follows from the printed statements is option 1 and the printed key is option 3
- **Why:** This question requires the facts NCERT states about the photorespiratory pathway, demonstrated by statement (c) 'Phosphoglycolate is formed' and statement (b) '$\mathrm{CO_2}$ is consumed and $\mathrm{O_2}$ is generated'.
- **Note:** Tagged as printed and not repaired. The key line reads 'Answer Key: 3', which selects '(a) and (b) only', but (a) reads 'Do not occur in C3 plants' and (b) reads 'CO2 is consumed and O2 is generated', each the reverse of what the photorespiration section says, while (c) and (d) match it. The three axes are recorded; the trap is left as no_trap under rulebook section 7, since a trap written over an unsettled key would name the pull of whichever set is wrong.
<!--/ecat-->

## Q115

Biology · zoology · Body Fluids and Circulation

Which of the following statements is incorrect ?

- **(1)** Fibrinogen is produced from fibrin
- (2) Blood coagulates in response to an injury
- (3) Blood clot consists of fibrins
- (4) Fibrin is produced from fibrinogen

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. During coagulation, thrombin converts inactive fibrinogen into fibrin, so option $4$ is correct; fibrin threads form the clot (option $3$ correct) in response to injury (option $2$ correct), hence the incorrect statement is option $1$.

**Subtopic:** Coagulation of Blood · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 15)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q115_bd7d6ad2_03112026.png?v=bd7d6ad2756b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Coagulation runs one way: the soluble plasma protein fibrinogen is converted into insoluble fibrin threads, which mesh into the clot
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The set prints the same conversion in both directions, so a student who holds it backwards reads 'Fibrin is produced from fibrinogen' as the false one and ticks it as the incorrect statement
- **Why:** This question requires the stated direction of a named conversion, demonstrated by the keyed option 'Fibrinogen is produced from fibrin' standing against 'Fibrin is produced from fibrinogen'.
<!--/ecat-->

## Q116

Biology · botany · The Living World

Arrange the following taxonomic categories in ascending order. Choose the correct answer from the options given below :

- (a) Genus
- (b) Class
- (c) Order
- (d) Phylum
- (e) Family
- (f) Kingdom
- (g) Species

- (1) (f), (c), (b), (g), (d), (e), (a)
- **(2)** (g), (a), (e), (c), (b), (d), (f)
- (3) (a), (c), (d), (g), (f), (b), (e)
- (4) (g), (c), (d), (b), (e), (a), (f)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The ascending taxonomic hierarchy runs Species $\rightarrow$ Genus $\rightarrow$ Family $\rightarrow$ Order $\rightarrow$ Class $\rightarrow$ Phylum $\rightarrow$ Kingdom, which maps to $(g), (a), (e), (c), (b), (d), (f)$, option $2$.

**Subtopic:** Taxonomic Categories · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 16)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q116_5faa966b_03112026.png?v=5faa966bde10)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The taxonomic hierarchy from the lowest category upward is species, genus, family, order, class, phylum, kingdom, so ascending means starting at species
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The hierarchy is drawn as a pyramid with kingdom at the top, so 'ascending' is read as moving down the page from kingdom, and option 1 is the only sequence that starts there
- **Why:** This question requires the taxonomic categories placed in rank order, demonstrated by the stem's instruction to 'Arrange the following taxonomic categories in ascending order'.
- **Note:** E1 called this arrange_in_order, which category_retired.qtype maps to mcq; the ordering demand is carried by asks: order.
<!--/ecat-->

## Q117

Biology · botany · Photosynthesis in Higher Plants

Select the correct sequence of experiments that led to a gradual understanding of photosynthesis in green plants.

- (1) Production of glucose $\rightarrow$ role of air $\rightarrow$ release of oxygen $\rightarrow$ absorption spectra of chlorophyll a and b
- (2) Absorption spectra of chlorophyll a and b $\rightarrow$ production of glucose $\rightarrow$ release of oxygen $\rightarrow$ role of air
- **(3)** Role of air $\rightarrow$ release of oxygen $\rightarrow$ production of glucose $\rightarrow$ absorption spectra of chlorophyll a and b
- (4) Release of oxygen $\rightarrow$ production of glucose $\rightarrow$ absorption spectra of chlorophyll a and b $\rightarrow$ role of air

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Priestley (1770) showed that air is restored by plants: role of air comes first.
2. Ingenhousz then showed that green parts release oxygen in sunlight: release of oxygen is second.
3. Sachs (1854) showed that glucose is produced (stored as starch) in green parts: production of glucose is third.
4. Engelmann (1880s) obtained the action spectrum matching the absorption spectra of chlorophyll $a$ and $b$: this is last.
5. Order: role of air $\rightarrow$ release of oxygen $\rightarrow$ production of glucose $\rightarrow$ absorption spectra, which is option $3$.

**Subtopic:** Photosynthesis Experiments · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q117_956dba1d_03112026.png?v=956dba1d5012)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The classical photosynthesis experiments in the order they happened: Priestley on the role of air, Ingenhousz on oxygen release, Sachs on glucose, Engelmann on the absorption spectra of chlorophyll a and b
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Option 2 holds the same four landmarks in the exact inverse of the right chain; a student who fixes on the absorption spectra as the work that finally explained photosynthesis enters the chain at that end and runs it back to the role of air
- **Why:** This question requires the chronological order of four named photosynthesis experiments, demonstrated by the stem's 'Select the correct sequence of experiments that led to a gradual understanding' with four options carrying the same four items in different orders.
- **Note:** E1 read this as arrange_in_order; the v2 qtype axis has no ordering shape, so the printed shape is mcq and the ordering demand sits on asks: order.
<!--/ecat-->

## Q118

Biology · both · Biomolecules

Match List-I with List-II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Starch | I | Fights infection |
| B | Antibody | II | Energy storage |
| C | Concanavalin A | III | Glucose transport |
| D | Glut-4 | IV | Lectin |

- (1) A-I, B-II, C-III, D-IV
- (2) A-I, B-II, C-IV, D-III
- **(3)** A-II, B-I, C-IV, D-III
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Starch is a storage polysaccharide in plants, so $A \rightarrow II$ (energy storage).
2. Antibodies fight infectious agents, so $B \rightarrow I$ (fights infection).
3. Concanavalin A is a lectin, so $C \rightarrow IV$.
4. GLUT-4 is a membrane protein that transports glucose into cells, so $D \rightarrow III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ matches option $3$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q118_71751b7c_03112026.png?v=71751b7c599b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each biomolecule is known by one job or class: starch stores energy, an antibody fights infection, concanavalin A is a lectin and Glut-4 carries glucose into the cell
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Lectins are the sugar-binding proteins and Glut-4 is the sugar protein a student can name, so "Lectin" goes to Glut-4 and concanavalin A is left with glucose transport. Concanavalin A is the lectin on record, and Glut-4 is the transporter that moves glucose across the membrane.
- **Why:** This question requires each molecule's own job or class recalled, demonstrated by List-II printing "Energy storage", "Fights infection", "Glucose transport" and "Lectin" -- one stated property per molecule, with nothing to compare between them. Rule 5 test applied: "Lectin" and "Glut-4" are nothing alike as words, so the pull is the neighbouring sugar-protein entry, which is nearby_fact.
<!--/ecat-->

## Q119

Biology · zoology · Locomotion and Movement

The number of vertebrae in a human is____.

- (1) $206$
- (2) $7$
- (3) $12$
- **(4)** $26$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The human vertebral column is formed by $26$ serially arranged units called vertebrae, so the answer is option $4$.

**Subtopic:** Axial Skeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q119_685cdc0e_03112026.png?v=685cdc0e1f20)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The human vertebral column is built of 26 serially arranged vertebrae, which is not the 206 bones of the whole skeleton
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $206$ is the count the chapter attaches to the human skeleton as a whole, so reading 'number of vertebrae' as 'number of bones' answers the skeleton question instead of the column question
- **Why:** This question requires the stored count the book prints for the vertebral column, demonstrated by the stem 'The number of vertebrae in a human is____' with four bare numbers as options.
- **Note:** E1 read this as fill_in_blank, which codebook §1 treats as an overlay rather than a shape; the printed shape is mcq.
<!--/ecat-->

## Q120

Biology · both · Cell: The Unit of Life

Endomembrane system includes ______ .

- (1) Golgi complex, chloroplast, peroxisomes and vacuole
- **(2)** endoplasmic reticulum, Golgi complex, lysosomes and vacuole
- (3) endoplasmic reticulum, chloroplast, peroxisomes and vacuole
- (4) mitochondria, chloroplast, peroxisomes and vacuole

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT defines the endomembrane system as ER, Golgi complex, lysosomes and vacuoles; mitochondria, chloroplasts and peroxisomes are not part of it, so the answer is option $2$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q120_b16e412e_03112026.png?v=b16e412ec835)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The endomembrane system is the set of organelles whose functions are coordinated — endoplasmic reticulum, Golgi complex, lysosomes and vacuoles — and mitochondria, chloroplast and peroxisomes are named as being outside it
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Two of the four names in this option are genuine members, and the pull is a rule of thumb: taking 'endomembrane' to mean every membrane-bound organelle keeps the endoplasmic reticulum and the vacuole and lets chloroplast and peroxisome in beside them
- **Why:** This question requires the stated membership of the endomembrane system, demonstrated by option 2's 'endoplasmic reticulum, Golgi complex, lysosomes and vacuole' having to be accepted or rejected as a whole set.
- **Note:** E1 read this as fill_in_blank, an overlay in codebook §1. Each option is a four-organelle set judged whole, which the retired E1 list called pair_options; the v2 qtype axis has no such value, so the shape is recorded as mcq.
<!--/ecat-->

## Q121

Biology · botany · Plant Growth and Development

Length of the stem at time $0$ is $20\,\mathrm{cm}$. The arithmetic growth rate is $30\,\mathrm{cm}$ per day. What is the length of the stem at the end of the $7^{\mathrm{th}}$ day?

- (1) $460\,\mathrm{cm}$
- (2) $50\,\mathrm{cm}$
- (3) $170\,\mathrm{cm}$
- **(4)** $230\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Arithmetic growth is linear: $L_t = L_0 + r t$.
2. $L_t = 20\,\mathrm{cm} + 30\,\mathrm{cm\,day^{-1}} \times 7\,\mathrm{day}$.
3. $L_t = 20 + 210 = 230\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Growth Rate and Absolute and Relative Growth Rate · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q121_e922a0b4_03112026.png?v=e922a0b4d64a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Arithmetic growth adds a constant increment in every unit of time, so $L_t = L_0 + rt$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The two printed numbers go into the wrong slots of $L_t = L_0 + rt$: with $30\,\mathrm{cm}$ read as the starting length and $20\,\mathrm{cm}$ per day as the rate, $30 + 20 \times 7 = 170$
- **Why:** This question requires a number computed from the stem's own figures, demonstrated by 'Length of the stem at time $0$ is $20\,\mathrm{cm}$' and 'The arithmetic growth rate is $30\,\mathrm{cm}$ per day'.
<!--/ecat-->

## Q122

Biology · botany · Biological Classification

Match List-I with List-II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Spherical | I | Vibrio |
| B | Rod | II | Cocci |
| C | Comma | III | Spirilla |
| D | Spirillum | IV | Bacilli |

- **(1)** A-II, B-IV, C-I, D-III
- (2) A-I, B-III, C-II, D-IV
- (3) A-III, B-II, C-I, D-IV
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Spherical bacteria are called cocci: $A \rightarrow II$; rod-shaped are bacilli: $B \rightarrow IV$; comma-shaped are vibrio: $C \rightarrow I$; spiral are spirilla: $D \rightarrow III$. This is option $1$.

**Subtopic:** Kingdom Monera · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 16)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q122_29115d3d_03112026.png?v=29115d3d3604)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bacteria are named by outline: cocci are spherical, bacilli are rods, vibrio is the comma and spirilla are the spirals
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Vibrio is carried in memory as a curved rod, so the "Rod" row takes it and "Comma" is left with bacilli. Bacillus is the straight rod and vibrio the comma, which is how the four outlines are printed.
- **Why:** This question requires the name attached to each bacterial outline, demonstrated by List-I printing bare shapes -- "Spherical", "Rod", "Comma" -- against the four form names in List-II. Rule 5 test applied: "Vibrio" and "Bacilli" bear no resemblance to each other, so position within the printed set of four shapes is what carries the student, which is nearby_fact.
<!--/ecat-->

## Q123

Biology · zoology · Body Fluids and Circulation

The number of action potentials generated by sino-arterial node (SAN) in a healthy human is ______ per minute.

- (1) 120 - 140
- (2) 28 - 30
- **(3)** 70 – 75
- (4) 100 - 110

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT says the SAN, the pacemaker, generates about $70$–$75$ action potentials per minute, which matches option $3$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q123_07a26642_03112026.png?v=07a26642f757)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The sino-atrial node fires 70-75 action potentials a minute, and that rate is what sets the resting heart beat
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong range against the figures this chapter prints: the only rate given is 70-75 per minute, beside a cardiac output of about 5 L and a pressure of 120/80 mm Hg. None of 28-30, 100-110 or 120-140 reproduces a printed value, none is a regional or partial count of the right one, and no stated relation converts 70-75 into any of them.
- **Why:** This question requires one stored rate the book prints, demonstrated by the stem 'The number of action potentials generated by sino-arterial node (SAN) in a healthy human is ______ per minute' with four numeric ranges as options.
- **Note:** The stem prints 'sino-arterial node' where the textbook prints 'sino-atrial node (SAN)'; tagged as printed, not repaired. A reviewer may want to test whether the textbook line's word 'maximum' ('SAN can generate the maximum number of action potentials') pulls upward, but that pull does not single out 100-110 over 120-140, so no one option could be named and no trap was recorded.
<!--/ecat-->

## Q124

Biology · botany · The Living World

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Family | I | Sapindales |
| B | Genus | II | Dicotyledonae |
| C | Class | III | Anacardiaceae |
| D | Phylum | IV | Angiospermae |
| E | Order | V | Mangifera |

- **(1)** A-III, B-V, C-II, D-IV, E-I
- (2) A-I, B-V, C-II, D-IV, E-III
- (3) A-II, B-I, C-III, D-IV, E-V
- (4) A-II, B-III, C-V, D-I, E-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In NCERT's classification of mango, Family = Anacardiaceae, so $A \to III$.
2. Genus = Mangifera, so $B \to V$.
3. Class = Dicotyledonae, so $C \to II$.
4. Phylum (Division) = Angiospermae, so $D \to IV$.
5. Order = Sapindales, so $E \to I$.
6. The match $A\text{-}III, B\text{-}V, C\text{-}II, D\text{-}IV, E\text{-}I$ is option $1$.

**Subtopic:** Taxonomic Categories · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q124_4f1399d3_03112026.png?v=4f1399d3f023)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Rank is readable from the ending of a taxon name: -aceae marks a family, -ales an order, while the generic name of the species is the genus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Three names place themselves -- Mangifera as the genus, Dicotyledonae as the class, Angiospermae as the division -- and the two Latin names left over are then entered in the other order. The endings settle it: -aceae belongs to the family, -ales to the order.
- **Why:** This question requires the rank-naming convention applied to five printed names, demonstrated by List-II supplying Anacardiaceae, Sapindales, Dicotyledonae and Angiospermae -- names whose endings, not their meanings, say which category each belongs to. Rule 5 test applied: "Sapindales" and "Anacardiaceae" do not resemble each other, and what carries the student is their adjacency as the two mid-ranks of the same printed hierarchy, so nearby_fact.
<!--/ecat-->

## Q125

Biology · zoology · Neural Control and Coordination

Which of the following is not a part of human central neural system ?

- **(1)** Pericardium
- (2) Arachnoid
- (3) Dura mater
- (4) Pia mater

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The brain is covered by three cranial meninges: outer dura mater, middle arachnoid and inner pia mater, so options $2$, $3$ and $4$ belong to the CNS; pericardium surrounds the heart, so the answer is option $1$.

**Subtopic:** Human Neural System and Its Divisions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q125_09cce912_03112026.png?v=09cce9125911)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Dura mater, arachnoid and pia mater are the three meninges that cover the central neural system; the pericardium is the sac around the heart
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student holding the covering as 'dura mater and pia mater' — the two names that travel together — treats the third name in the same printed list as the one that does not belong, and strikes out arachnoid instead of the heart's covering
- **Why:** This question requires the stated membership of the coverings of the central neural system, demonstrated by the stem's 'not a part of human central neural system' set against three printed meninges and 'Pericardium'.
- **Note:** Applied the codebook §5.1 swap test on the trap: arachnoid bears no resemblance at all to pericardium, so likeness is not what carries the student, and the option is reachable only because the book prints arachnoid inside the same three-name meninges list — nearby_fact, not look_alike_term.
<!--/ecat-->

## Q126

Biology · both · Cell Cycle and Cell Division

Given below are two statements : In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) Chromosomes are fully condensed at the end of prophase I.
- (Statement II) Meiosis I resembles mitosis.

- (1) Statement I is incorrect, but Statement II is true
- (2) Both Statement I and Statement II are true
- (3) Both Statement I and Statement II are false
- **(4)** Statement I is correct, but Statement II is false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Prophase I ends with diakinesis, by the end of which chromosomes are fully condensed and the spindle is assembled, so Statement I is true.
2. Meiosis I is reductional (homologues separate); meiosis II separates sister chromatids and resembles mitosis, so Statement II is false.
3. Statement I true and Statement II false matches option $4$.

**Subtopic:** Prophase I and Its Types, Meiosis II · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q126_93ec7320_03112026.png?v=93ec73208148)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chromosomes reach full condensation by the end of prophase I, and it is meiosis II, not meiosis I, that resembles an ordinary mitosis
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Meiosis I and meiosis II are separated by nothing but the numeral, so a student who holds 'one of the two meiotic divisions resembles mitosis' and not which one marks Statement II true and takes both correct
- **Why:** This question requires two printed lines about a division to be checked, demonstrated by 'Meiosis I resembles mitosis'.
- **Note:** Swap test applied: replacing 'Meiosis I' with an unlike term kills the pull, since the two divisions are told apart by the numeral alone, so the likeness carries it.
<!--/ecat-->

## Q127

Biology · botany · Morphology of Flowering Plants

Match List-I with List-II. Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A | Marginal placentation | I | \textit{Argemone} |
| B | Axile placentation | II | Tomato |
| C | Parietal placentation | III | \textit{Primrose} |
| D | Free central placentation | IV | Pea |

- **(1)** A-IV, B-II, C-I, D-III
- (2) A-II, B-IV, C-I, D-III
- (3) A-IV, B-II, C-III, D-I
- (4) A-IV, B-III, C-I, D-II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Marginal placentation (A) is seen in pea, so $A \rightarrow IV$.
2. Axile placentation (B) is seen in tomato, so $B \rightarrow II$.
3. Parietal placentation (C) is seen in \textit{Argemone}, so $C \rightarrow I$.
4. Free central placentation (D) is seen in \textit{Primrose}, so $D \rightarrow III$.
5. The match A-IV, B-II, C-I, D-III is option $1$.

**Subtopic:** Gynoecium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q127_c594dcd9_03112026.png?v=c594dcd91c5b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each placentation type has its own stock example: pea for marginal, tomato for axile, Argemone for parietal and Primrose for free central
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Pea and tomato anchor the first two rows, and the two remaining genera, Argemone and Primrose, are then entered in the other order. Argemone is the parietal example and Primrose the free central one.
- **Why:** This question requires the stock example recalled for each placentation type, demonstrated by List-I naming the four types and List-II naming four plants, one per type. Rule 5 test applied: "Argemone" and "Primrose" are nothing alike as words, so what carries the student is that they are the two unfamiliar genera printed together with these types, which is nearby_fact.
- **Note:** List-II item I is printed as \textit{Argemone} and item III as \textit{Primrose} in the record; the italic markup carries no information for the tagging.
<!--/ecat-->

## Q128

Biology · botany · Biological Classification

Symbiotic association between fungi and algae are called ________.

- (1) chrysophytes
- **(2)** lichens
- (3) sponges
- (4) mycorrhiza

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A mutually useful association of an alga (phycobiont) and a fungus (mycobiont) is a lichen, so the answer is option $2$; mycorrhiza is fungus with higher-plant roots, chrysophytes are protists, sponges are animals.

**Subtopic:** Viroids, Prions & Lichens · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 17)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q128_715eb480_03112026.png?v=715eb48038fe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A lichen is the symbiotic association of an alga with a fungus; the fungus-plus-root association is mycorrhiza
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Lichen and mycorrhiza are printed in the same breath as the two symbioses a fungus enters, so a student who holds 'fungus in partnership' as one fact and not the two partners it names reaches for the other half of that sentence
- **Why:** This question requires the term the book states for one named association, demonstrated by the stem 'Symbiotic association between fungi and algae are called ________' with four terms as options.
- **Note:** E1 read this as fill_in_blank, which codebook §1 treats as an overlay rather than a shape; the printed shape is mcq.
<!--/ecat-->

## Q129

Biology · botany · Biological Classification

Which of the following is not a prokaryote?

- **(1)** Fungi
- (2) Bacteria
- (3) Blue green algae
- (4) Mycoplasma

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Bacteria, blue green algae (cyanobacteria) and mycoplasma are prokaryotes (Kingdom Monera), while fungi have a membrane-bound nucleus and are eukaryotes, so the answer is option $1$.

**Subtopic:** Kingdom Monera · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q129_9d968702_03112026.png?v=9d9687023c12)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bacteria, cyanobacteria and mycoplasma are prokaryotes of Monera; fungi are eukaryotes with a true nucleus
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The name 'blue green algae' carries the word algae, and algae are taught as eukaryotes, so a student who answers from the name rather than from the kingdom strikes out the cyanobacteria as the non-prokaryote
- **Why:** This question requires the stated kingdom placement of four named organisms, demonstrated by the stem 'Which of the following is not a prokaryote?' with 'Blue green algae' printed against 'Fungi'.
- **Note:** Applied the codebook §5.1 swap test on the trap: print 'cyanobacteria' in place of 'Blue green algae' and the pull disappears, so it is the likeness of the name to the eukaryotic algae that carries the student, not where the book prints it — look_alike_term, not nearby_fact.
<!--/ecat-->

## Q130

Biology · both · Biomolecules

Arrange the following elements in descending order of their contribution to percentage weight of the human body.
Choose the correct answer from the options given below:

- (a) Oxygen
- (b) Carbon
- (c) Hydrogen
- (d) Nitrogen

- (1) (b), (a), (c), (d)
- **(2)** (a), (b), (c), (d)
- (3) (c), (a), (b), (d)
- (4) (b), (c), (d), (a)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. By percentage weight of the human body: $\text{O} \approx 65.0\%$, $\text{C} \approx 18.5\%$, $\text{H} \approx 9.5\%$, $\text{N} \approx 3.3\%$, so the descending order is $(a) > (b) > (c) > (d)$, which is option $2$.

**Subtopic:** How To Analyse Chemical Composition? · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 17)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q130_9ab1dddb_03112026.png?v=9ab1dddb1af4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** By percentage of body weight the human body is oxygen about 65, carbon about 18, hydrogen about 10 and nitrogen about 3, so oxygen leads by mass even though hydrogen leads by number of atoms
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Water is most of the body and $\mathrm{H_2O}$ carries two hydrogens for every oxygen, so hydrogen is ranked first — which is the true order by number of atoms, not by the percentage weight the stem asks for
- **Why:** This question requires the four elements ranked by their share of body mass, demonstrated by the stem asking for 'descending order of their contribution to percentage weight of the human body'.
- **Note:** E1 called this arrange_in_order, which category_retired.qtype maps to mcq; the ordering demand is carried by asks: order.
<!--/ecat-->

## Q131

Biology · zoology · Chemical Coordination and Integration

Which one of the following statements is incorrect?

- (1) $\beta$-cells of pancreas secrete insulin
- (2) $\alpha$-cells of pancreas secrete glucagon
- **(3)** $\alpha$-cells of pancreas secrete insulin
- (4) Glucagon stimulates glycogenolysis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\beta$-cells of the islets of Langerhans secrete insulin and $\alpha$-cells secrete glucagon, which promotes glycogenolysis, so the incorrect statement is that $\alpha$-cells secrete insulin (option $3$).

**Subtopic:** Pancreas · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q131_377d8192_03112026.png?v=377d8192348a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The islets of Langerhans divide the work: beta-cells secrete insulin, alpha-cells secrete glucagon, and glucagon drives glycogenolysis
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  'Beta-cells of pancreas secrete insulin' is the line about the pancreas that is printed and drilled hardest, so a student hunting for the statement that MATCHES what they know ticks it and answers the question the stem did not ask
- **Why:** This question requires judging four printed claims about pancreatic hormones against the stated facts, demonstrated by the stem 'Which one of the following statements is incorrect?' with options 1 and 3 differing only in '$\beta$-cells of pancreas' against '$\alpha$-cells of pancreas'.
- **Note:** E1's pattern fell through to plain_mcq by default, but the stem prints 'Which one of the following statements is incorrect?' and each option is a full claim to be judged, which is the codebook's statement_options shape, so qtype is recorded as statements.
<!--/ecat-->

## Q132

Biology · botany · Morphology of Flowering Plants

Which of the following are characteristic features of Solanaceae family? Choose the correct answer from the options given below:

- (a) Flowers are bisexual and actinomorphic
- (b) Calyx have five sepals and are united
- (c) Androecium have five stamens and are epipetalous
- (d) Ovary is inferior

- (1) (b), (c) and (d) only
- **(2)** (a), (b) and (c) only
- (3) (d) only
- (4) (a) and (b) only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In Solanaceae flowers are bisexual and actinomorphic, so (a) is true.
2. The calyx has five united (gamosepalous) sepals, so (b) is true.
3. The androecium has five epipetalous stamens, so (c) is true.
4. The ovary is superior (bicarpellary, syncarpous), so (d) is false.
5. Hence $(a), (b)$ and $(c)$ only, which is option $2$.

**Subtopic:** Solanaceae, Malvaceae and Cruciferae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q132_4253d0b4_03112026.png?v=4253d0b4d9e3)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Solanaceae flowers are bisexual and actinomorphic, with five united sepals, five epipetalous stamens and a superior ovary
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Statement (c) bundles two claims, five stamens and epipetalous, so a student sure of the number but unsure what epipetalous attaches to drops the whole statement and keeps the true but short set (a) and (b)
- **Why:** This question requires the floral features NCERT lists for Solanaceae, demonstrated by statement (d) 'Ovary is inferior' standing against the family's superior ovary.
<!--/ecat-->

## Q133

Biology · zoology · Animal Kingdom

Given below are two statements :
Statement I : When any plane passing through the central axis of the body divides the organism into two identical halves, it is called radial symmetry.
Statement II : In phylum Echinodermata, both adults and larvae are radially symmetrical.
In the light of the above statements, choose the most appropriate answer from the options given below :

- (Statement I) When any plane passing through the central axis of the body divides the organism into two identical halves, it is called radial symmetry.
- (Statement II) In phylum Echinodermata, both adults and larvae are radially symmetrical.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: radial symmetry is when any plane through the central axis divides the body into two identical halves, so Statement I is correct.
2. Statement II: in Echinodermata the adults are radially symmetrical but the larvae are bilaterally symmetrical, so Statement II is incorrect.
3. Statement I correct and Statement II incorrect gives option $4$.

**Subtopic:** Phylum – Echinodermata and Hemichordata, Basis of Classification · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q133_c794f967_03112026.png?v=c794f96788e1)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Radial symmetry means any plane through the central axis gives two identical halves, and adult echinoderms are radially symmetrical while their larvae are bilaterally symmetrical
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Statement II is true of the adults and false of the larvae, so a student who holds 'echinoderms are radially symmetrical' reads the half that matches, accepts the whole sentence and takes both correct
- **Why:** This question requires two printed lines to be checked, one of which is true of only part of what it claims, demonstrated by 'both adults and larvae are radially symmetrical'.
<!--/ecat-->

## Q134

Biology · both · Cell Cycle and Cell Division

The correct sequence of adult cell cycle phases is ______ .

- (1) S-M-G2-G1
- (2) G1-G2-S-M
- (3) G1-M-G2-S
- **(4)** G1-S-G2-M

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Interphase comes in the order $G_1 \rightarrow S \rightarrow G_2$, and M phase follows it, so the sequence is $G_1\text{-}S\text{-}G_2\text{-}M$, which is option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q134_d63c9815_03112026.png?v=d63c9815c116)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Interphase runs G1, then S where DNA is replicated, then G2, and only then does M phase divide the cell
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The two gaps are numbered G1 and G2, and the numbering reads as consecutive, so a student who orders by the subscripts puts the gaps together and pushes S after them, keeping G1 first and M last but transposing the middle pair
- **Why:** This question requires the order of the four named cell cycle phases, demonstrated by the stem 'The correct sequence of adult cell cycle phases is ______' with four options carrying the same four labels rearranged.
- **Note:** E1 read this as arrange_in_order; the v2 qtype axis has no ordering shape, so the printed shape is mcq and the ordering demand sits on asks: order.
<!--/ecat-->

## Q135

Biology · zoology · Structural Organisation in Animals

In frogs, the number of pairs of cranial nerves arising from the brain are _______.

- (1) $12$
- (2) $6$
- (3) $9$
- **(4)** $10$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Frog nervous system (NCERT Class 11): ten pairs of cranial nerves arise from the brain, which is option $4$ ($10$).

**Subtopic:** Anatomy of Frog · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 17)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q135_c1566965_03112026.png?v=c156696588cb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The frog's brain gives off ten pairs of cranial nerves, where the human brain gives off twelve
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $12$ pairs is the cranial-nerve figure carried from human neural anatomy, and it is true there, so a student who holds one cranial-nerve number answers for the human instead of for the frog
- **Why:** This question requires one stored count stated for the frog, demonstrated by the stem 'In frogs, the number of pairs of cranial nerves arising from the brain are _______' with four bare numbers as options.
- **Note:** E1 read this as fill_in_blank, an overlay under codebook §1; the printed shape is mcq.
<!--/ecat-->

## Q136

Biology · both · Biotechnology: Principles and Processes

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) In recombinant DNA technology, lysozyme is used for disrupting bacterial cells while cellulase is for plant cells.
- (Reason R) Isolation of genetic material needs disruption of cells.

- (1) A is not correct but R is correct
- **(2)** Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are correct but R is not the correct explanation of A
- (4) A is correct but R is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Assertion A: NCERT states bacterial cells are treated with lysozyme and plant cells with cellulase (fungus with chitinase) to break them open, so A is correct.
2. Reason R: DNA is enclosed within membranes, so isolating genetic material requires disrupting the cell first, so R is correct.
3. The enzymes in A are used precisely because cell disruption is needed (R), so R correctly explains A, which is option $2$.

**Subtopic:** Isolation of Genetic Material (DNA) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q136_00a667ed_03112026.png?v=00a667ed7390)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A cell is opened with the enzyme that attacks its own wall material -- lysozyme for bacterial walls, cellulase for plant walls -- because the DNA cannot be reached until the cell is broken
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  R is accepted as true and then set aside as too general to account for A, because it names no enzyme and no cell type while A is entirely about which enzyme goes with which cell. Breaking the cell open is precisely the job those enzymes are there to do, so R is the reason they are used at all.
- **Why:** This question requires judging whether the stated need to break cells open accounts for the choice of enzyme, demonstrated by R reading "Isolation of genetic material needs disruption of cells" against an Assertion that is entirely about which enzyme suits which cell.
<!--/ecat-->

## Q137

Biology · zoology · Reproductive Health

The method of directly injecting a sperm into ovum in assisted reproductive technology is called:

- (1) Embryo transfer (ET)
- (2) Gamete intra fallopian transfer (GIFT)
- (3) Zygote intra fallopian transfer (ZIFT)
- **(4)** Intra cytoplasmic sperm injection (ICSI)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Injecting a sperm directly into the cytoplasm of the ovum is called intra cytoplasmic sperm injection (ICSI), which is option $4$.

**Subtopic:** Assisted Reproductive Technologies (ART) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q137_74c0ffcf_03112026.png?v=74c0ffcfbeee)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** ICSI is the laboratory step of injecting a sperm straight into the ovum; GIFT, ZIFT and ET all name transfers of material into the female tract
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The four acronyms are printed as one block of assisted reproductive procedures, and a sperm is a gamete, so a student working from the expansion of the names picks the one procedure whose title says gamete
- **Why:** This question requires the stated definition of one named procedure, demonstrated by the stem 'The method of directly injecting a sperm into ovum in assisted reproductive technology is called' with four printed ART acronyms as options.
<!--/ecat-->

## Q138

Biology · zoology · Evolution

Adaptive radiation in placental mammals and Australian Marsupials leading to similarity between distant species is an example of

- (1) genetic drift
- (2) divergent evolution
- **(3)** convergent evolution
- (4) founder effect

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Placental mammals and Australian marsupials are distantly related lineages that independently evolved similar forms (e.g. placental wolf vs Tasmanian wolf), which NCERT describes as convergent evolution, option $3$.

**Subtopic:** What is Adaptive Radiation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 18)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q138_e294d9e6_03112026.png?v=e294d9e626b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** When two adaptive radiations in separate places end in look-alike forms, the book calls it convergent evolution; divergence is what a single radiation does
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Adaptive radiation is taught as one stock spreading into many forms, which is divergent evolution, and the stem prints the phrase 'adaptive radiation' in its first three words, so a student answers from that printed phrase and never reaches the stem's 'similarity between distant species'
- **Why:** This question requires the term the book attaches to one stated case, demonstrated by the stem 'Adaptive radiation in placental mammals and Australian Marsupials leading to similarity between distant species is an example of'.
- **Note:** Applied the codebook §5.1 swap test on the trap. 'Convergent' and 'divergent' do resemble each other, but rename them to two unlike words and the pull survives, because what carries the student is the printed fact that adaptive radiation is divergence — position, not likeness, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q139

Biology · botany · Principles of Inheritance and Variation

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the most appropriate answer from the options given below :

- (Assertion A) In an experiment, Mendel observed that the F1 progeny plants are all tall and none are dwarf.
- (Reason R) Stem height is a contrasting trait, with tall being dominant and dwarf being recessive.

- (1) A is not correct but R is correct
- **(2)** Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are correct but R is not the correct explanation of A
- (4) A is correct but R is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In Mendel's monohybrid cross $TT \times tt$, all F1 plants are $Tt$ and show the tall phenotype, so A is correct.
2. Tall and dwarf are a contrasting pair for stem height, with tall ($T$) dominant over dwarf ($t$), so R is correct.
3. Dominance of tall over dwarf is why $Tt$ F1 plants are all tall, so R correctly explains A, which is option $2$.

**Subtopic:** Monohybrid Cross · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q139_7845356b_03112026.png?v=7845356bedec)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In a monohybrid cross the F1 heterozygotes show only the dominant form, so all F1 plants are tall and the recessive dwarf reappears only in F2
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Mendel's dwarf plants are remembered -- correctly -- as reappearing in his results, so "none are dwarf" reads as false and the Assertion gets struck out. The dwarfs come back in the F2, at a quarter of the progeny; the F1 that A speaks of is uniformly tall.
- **Why:** This question requires the dominance of one allele recognised as the reason a whole generation shows one form, demonstrated by A naming "the F1 progeny" specifically while R supplies "tall being dominant and dwarf being recessive".
<!--/ecat-->

## Q140

Biology · botany · Biodiversity and Conservation

Arrange the following in descending order of number of species in the Amazonian rain forest. Choose the correct answer from the options given below:

- (a) Plants
- (b) Birds
- (c) Fishes
- (d) Invertebrates
- (e) Mammals

- (1) (b) $>$ (a) $>$ (d) $>$ (c) $>$ (e)
- (2) (c) $>$ (b) $>$ (d) $>$ (e) $>$ (a)
- **(3)** (d) $>$ (a) $>$ (c) $>$ (b) $>$ (e)
- (4) (e) $>$ (b) $>$ (a) $>$ (c) $>$ (d)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT species counts for the Amazonian rain forest: invertebrates $\approx 1{,}25{,}000$, plants $\approx 40{,}000$, fishes $\approx 3{,}000$, birds $\approx 1{,}300$, mammals $\approx 427$; so $(d) > (a) > (c) > (b) > (e)$, which is option $3$.

**Subtopic:** Latitudinal Gradients · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 18)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q140_c48cec3d_03112026.png?v=c48cec3df34a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** In the Amazonian rain forest species richness runs invertebrates above plants above fishes above birds above mammals, so the smaller the body the larger the number of species
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Ranking the groups by how large and conspicuous their members are puts mammals at the top and invertebrates at the bottom, which inverts both ends of the species count
- **Why:** This question requires the species counts NCERT gives for the Amazonian rain forest put in rank order, demonstrated by the stem asking for 'descending order of number of species in the Amazonian rain forest'.
- **Note:** E1 called this arrange_in_order, which category_retired.qtype maps to mcq; the ordering demand is carried by asks: order.
<!--/ecat-->

## Q141

Biology · zoology · Breathing and Exchange of Gases

Sponges exchange $\mathrm{O_2}$ with $\mathrm{CO_2}$ by ________.

- (1) gills
- **(2)** simple diffusion over their entire body surfaces
- (3) moist cuticle
- (4) tracheal tubes

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Sponges (lower invertebrates) have no specialised respiratory organs, so $\mathrm{O_2}$ and $\mathrm{CO_2}$ are exchanged by simple diffusion over the entire body surface, which is option $2$.

**Subtopic:** Respiratory Organs in Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q141_579476ec_03112026.png?v=579476ec9c05)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sponges and other lower invertebrates exchange gases by simple diffusion over the whole body surface; gills, moist cuticle and tracheal tubes belong to other animals in the same list
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Gills are printed a line away as the respiratory structure of aquatic animals, so a student who reasons from the sponge's habitat rather than from its body picks the water-breathing organ out of the same paragraph
- **Why:** This question requires one stated animal-to-mechanism pairing, demonstrated by the stem 'Sponges exchange $\mathrm{O_2}$ with $\mathrm{CO_2}$ by ________' with option 2 printing 'simple diffusion over their entire body surfaces'.
- **Note:** E1 read this as fill_in_blank, an overlay under codebook §1; the printed shape is mcq.
<!--/ecat-->

## Q142

Biology · zoology · Principles of Inheritance and Variation

For a person with blood group 'O', which of the following is **not** a possible combination of parents' blood group genotypes?

- **(1)** Father : $I^{A}\,I^{B}$ and Mother : $I^{A}\,i$
- (2) Father : $I^{A}\,i$ and Mother : $I^{B}\,i$
- (3) Father : $I^{A}\,i$ and Mother : $I^{A}\,i$
- (4) Father : $I^{B}\,i$ and Mother : $I^{B}\,i$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Blood group O has genotype $ii$, so the child must receive $i$ from each parent.
2. In option 1 the father is $I^{A}I^{B}$ and has no $i$ allele, so he cannot pass on $i$; an $ii$ child is impossible.
3. In options 2, 3 and 4 both parents carry $i$, so $i \times i \rightarrow ii$ is possible (probability $\frac{1}{4}$).
4. Hence the combination that is not possible is option $1$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q142_13592822_03112026.png?v=135928220072)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A group O child is $ii$, so each parent must be able to pass an i; a parent who is $I^A I^B$ has no i to pass
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  A student who reduces the printed genotypes to phenotypes gets an A father and a B mother and applies the rule that A with B gives AB, so group O looks impossible in this cross — but both parents are heterozygous, and $I^A i \times I^B i$ gives $ii$ in a quarter of the offspring
- **Why:** This question requires the inheritance rule for multiple alleles applied to four printed parental pairs, demonstrated by option 1's 'Father : $I^{A}\,I^{B}$', which carries no i to pass to an $ii$ child.
- **Note:** Options 3 and 4 are mirror images of each other, A against B, and the same phenotype-level route reaches both, so both are recorded as traps rather than one being called filler; the trap proper sits on option 2 because the A-with-B cross has a route of its own that singles it out.
<!--/ecat-->

## Q143

Biology · zoology · Evolution

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Modern Homo sapiens arose in Australia and moved across continents.
- (Statement II) Homo sapiens arose around 75000 to 10000 years ago.

- **(1)** Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement I: as NCERT teaches, Homo sapiens arose in Africa and moved across continents, not Australia, so Statement I is incorrect.
2. Statement II: NCERT states that during the ice age between $75{,}000$ and $10{,}000$ years ago modern Homo sapiens arose, so Statement II is correct.
3. Statement I incorrect and Statement II correct is option $1$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q143_4f18531d_03112026.png?v=4f18531d0f1c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Modern Homo sapiens arose in Africa and spread across the continents, during the ice age between 75,000 and 10,000 years ago
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Statement I is the printed sentence with the continent of origin exchanged for a continent the same migration story names as somewhere humans spread to, so a student reading a familiar line marks it correct and takes both correct
- **Why:** This question requires two printed lines about human origins to be checked, demonstrated by 'Modern Homo sapiens arose in Australia and moved across continents'.
- **Note:** Swap test applied: the pull survives replacing 'Australia' with another continent, because what carries the student is the otherwise verbatim sentence and a continent the migration account names, so position rather than likeness decides it.
<!--/ecat-->

## Q144

Biology · zoology · Human Health and Disease

Which of the following is used as an effective sedative and painkiller for treating post-surgery patients?

- (1) Anti-retroviral drugs
- (2) Interferon
- (3) Antibiotics
- **(4)** Morphine

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Opioids such as morphine act on opioid receptors in the CNS and gut; NCERT describes morphine as a very effective sedative and painkiller, very useful in patients who have undergone surgery, which is option $4$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q144_7d63955c_03112026.png?v=7d63955c641d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Morphine is the opioid the book names as an effective sedative and painkiller, useful in patients who have undergone surgery
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Antibiotics are genuinely what a post-surgical patient is put on, so a student who answers the stem's 'post-surgery patients' half and lets the 'sedative and painkiller' half go by picks a true fact about surgical care that is not the property asked for
- **Why:** This question requires one stated property of a named drug, demonstrated by the stem 'used as an effective sedative and painkiller for treating post-surgery patients'.
<!--/ecat-->

## Q145

Biology · botany · Sexual Reproduction in Flowering Plants

Which of the following plant produces non-albuminous seeds?

- **(1)** Pea
- (2) Wheat
- (3) Maize
- (4) Barley

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In pea the endosperm is fully used up during embryo development, so its seeds are non-albuminous, while wheat, maize and barley retain endosperm (albuminous), giving option $1$.

**Subtopic:** Embryo and Seed · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q145_dc2478f2_03112026.png?v=dc2478f20446)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Non-albuminous seeds keep no residual endosperm, as in pea; wheat, maize and barley are the albuminous examples
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked what separates the three wrong options from one another. Wheat, maize and barley are the first three names in the book's own albuminous list, printed together in one sentence, and the only error available here — holding the two lists the wrong way round — strikes all three at once, so no one of them can be named over the others. Also checked for a route that would select just one: none of the three is a sub-case, a look-alike or a differently-stated form of the key, and the stem prints no feature (a grain, a cotyledon count, a family) that would pick out wheat rather than maize or barley.
- **Why:** This question requires the membership of one stated list, demonstrated by the stem 'Which of the following plant produces non-albuminous seeds?' with three cereals printed against 'Pea'.
- **Note:** The option set also offers an elimination route that does not need the term at all — one legume against three cereals — which is worth recording for the strategy axis but is not a trap.
<!--/ecat-->

## Q146

Biology · botany · Organisms and Populations

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) Abingdon tortoise in Galapagos islands became extinct within a decade after goats were introduced.
- (Reason R) Goats were more efficient at browsing than Abingdon tortoise.

- (1) A is not correct but R is correct
- **(2)** Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are correct but R is not the correct explanation of A
- (4) A is correct but R is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Assertion A: the Abingdon tortoise of the Galapagos became extinct within a decade after goats were introduced, a standard example of interspecific competition; A is correct.
2. Reason R: goats were the more efficient browsers, so they out-competed the tortoise for food; R is correct.
3. The tortoise went extinct because it lost this competition for food, so R is the correct explanation of A, which is option $2$.

**Subtopic:** Competition · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 19)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q146_987ec3fe_03112026.png?v=987ec3fe019e)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Competition can remove a species outright: the goats took the same vegetation more efficiently, so the Abingdon tortoise lost its food supply
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Both statements are accepted, and the extinction is then put down to the goats wrecking the island's vegetation or trampling the habitat, so browsing efficiency becomes a true aside rather than the cause. The competitive edge in browsing IS the cause on record -- the two animals were feeding on the same plants.
- **Why:** This question requires a competitive advantage recognised as the cause of an extinction, demonstrated by R supplying "Goats were more efficient at browsing than Abingdon tortoise" for the event A reports.
<!--/ecat-->

## Q147

Biology · zoology · Human Reproduction

The covering of ovum at ovulation is

- (1) chorion
- (2) endometrium
- (3) zona radiata
- **(4)** zona pellucida

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the ovum released at ovulation is covered by the zona pellucida (inner, non-cellular) and the corona radiata (outer cells); among the options only zona pellucida matches, which is option $4$.

**Subtopic:** Female Gametogenesis (Oogenesis) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 19)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q147_f8d97562_03112026.png?v=f8d975620987)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The ovum shed at ovulation is wrapped in the zona pellucida, with the corona radiata outside it
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Zona radiata' is built from the two real names the figure carries, zona pellucida and corona radiata, so a student who remembers that the coverings are a zona and a radiata but not which word pairs with which accepts the hybrid
- **Why:** This question requires the stated name of one layer at one stated moment, demonstrated by the stem 'The covering of ovum at ovulation is' with 'zona radiata' printed beside 'zona pellucida'.
- **Note:** Applied the codebook §5.1 swap test: replace 'zona radiata' with an unlike word and the pull dies entirely, since the option has no existence apart from resembling the two real labels — likeness is doing the work, so look_alike_term.
<!--/ecat-->

## Q148

Biology · botany · Microbes in Human Welfare

Which of the following is used as a clot buster?

- (1) Statins
- **(2)** Streptokinase
- (3) Penicillin
- (4) Cyclosporin A

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Streptokinase, produced by $Streptococcus$ and modified by genetic engineering, dissolves blood clots, so it is the clot buster: option $2$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q148_8c66bf75_03112026.png?v=8c66bf7582fa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Streptokinase, from Streptococcus and modified by genetic engineering, is the clot buster; statins lower cholesterol and cyclosporin A suppresses immunity
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Statins are printed in the same list of microbial bioactive molecules and are the only other one that acts on the blood, so a student who retrieves that list by body system rather than by product reaches for the cholesterol drug when the stem names a clot
- **Why:** This question requires one stated microbe-to-product fact, demonstrated by the stem 'Which of the following is used as a clot buster?' with four printed bioactive molecules as options.
<!--/ecat-->

## Q149

Biology · zoology · Human Reproduction

Which of the following structure is not a part of the male reproductive system?

- **(1)** Infundibulum
- (2) Rete testis
- (3) Epididymis
- (4) Vasa efferentia

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Rete testis, vasa efferentia and epididymis are male accessory ducts, while the infundibulum is the funnel-shaped end of the female fallopian tube, so the answer is option $1$.

**Subtopic:** The Male Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q149_e68b0f13_03112026.png?v=e68b0f13a752)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The male duct path runs seminiferous tubules, rete testis, vasa efferentia, epididymis; the infundibulum is the funnel of the female fallopian tube
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  'Vasa efferentia' reads like the other 'vasa' of the syllabus, the vasa recta of the nephron, so a student who files the name under kidney vessels takes it for the structure that does not belong to the male tract
- **Why:** This question requires the stated membership of the male duct system, demonstrated by the stem 'Which of the following structure is not a part of the male reproductive system?' with 'Infundibulum' printed among three testicular ducts.
- **Note:** Applied the codebook §5.1 swap test on the trap: rename vasa efferentia to an unlike word and the pull dies, because what carries the student is its likeness to vasa recta and not where the book prints it — look_alike_term, not nearby_fact.
<!--/ecat-->

## Q150

Biology · zoology · Human Reproduction

Given below are two statements: In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Ovulation is caused by LH surge leading to rupture of Graafian follicles.
- (Statement II) Graafian follicle remaining after ovulation transform into corpus luteum and secretes large amount of estrogen.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- **(4)** Statement I is correct but Statement II is incorrect

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Statement I: the mid-cycle LH surge induces rupture of the Graafian follicle and release of the ovum, so Statement I is correct.
2. Statement II: the remnant Graafian follicle becomes the corpus luteum, which secretes large amounts of progesterone (not estrogen), so Statement II is incorrect.
3. Statement I correct and Statement II incorrect is option $4$.

**Subtopic:** Menstrual Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q150_981d9a7b_03112026.png?v=981d9a7b139f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The LH surge ruptures the Graafian follicle to release the ovum, and the remains of that follicle become the corpus luteum, which secretes large amounts of progesterone
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Estrogen is the other ovarian hormone printed in the same cycle account, so a student who holds that the corpus luteum forms and secretes a hormone but not which one accepts Statement II and takes both correct
- **Why:** This question requires two printed lines about the cycle to be checked, demonstrated by 'transform into corpus luteum and secretes large amount of estrogen'.
- **Note:** Swap test applied: the pull survives replacing 'estrogen' with an unlike hormone name, because what carries the student is that both hormones are printed in the same cycle account, so position decides it.
<!--/ecat-->

## Q151

Biology · zoology · Body Fluids and Circulation

The opening between the right atrium and the right ventricle is guarded by ____________.

- (1) sino-atrial node
- (2) bicuspid valve
- **(3)** tricuspid valve
- (4) semilunar valve

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The opening between the right atrium and right ventricle is guarded by a valve with three muscular flaps, the tricuspid valve, which is option $3$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q151_b2018a71_03112026.png?v=b2018a7146df)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Three cusps on the right, two on the left: the tricuspid valve guards the right atrio-ventricular opening and the bicuspid the left
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Tricuspid and bicuspid differ only in the prefix, and the two are printed in one sentence as the two atrio-ventricular valves, so a student who holds 'cuspid valve guards the atrio-ventricular opening' but not which number goes with which side takes the wrong prefix
- **Why:** This question requires one stated structure at one stated site, demonstrated by the stem 'The opening between the right atrium and the right ventricle is guarded by ____________' with 'bicuspid valve' printed beside 'tricuspid valve'.
- **Note:** Applied the codebook §5.1 swap test: print 'mitral valve' instead of 'bicuspid valve' and the pull drops away, since a student then has to know the left-side fact rather than merely pick a prefix — the likeness of tri- and bi-cuspid is what carries them, so look_alike_term. E1 read the printed blank as fill_in_blank, an overlay under §1, which leaves the shape mcq.
<!--/ecat-->

## Q152

Biology · zoology · Evolution

Which of the following is not evidence for evolution?

- (1) Divergent evolution of anatomical structures such as forelimbs
- (2) Convergent evolution of traits like wings of birds and butterflies
- (3) Paleontological evidence from fossil records
- **(4)** Embryological support for evolution as proposed by Ernst Heckel

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Divergent evolution (homologous forelimbs), convergent evolution (analogous wings) and fossil records are all taught in NCERT as evidences of evolution; the embryological support proposed by Ernst Haeckel was disproved by Karl Ernst von Baer, so option $4$ is not evidence for evolution.

**Subtopic:** Embryological Support for Evolution · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 19)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q152_f23efb38_03112026.png?v=f23efb380c7b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Haeckel's embryological support for evolution is the one the book records as disapproved, by von Baer; homology, analogy and the fossil record all stand as evidence
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The rule that analogous structures do not demonstrate common ancestry gets stretched into 'analogy is not evidence for evolution at all', so a student strikes the convergent-evolution line — but bird and butterfly wings are printed as evidence of convergent evolution, which is evolution being evidenced
- **Why:** This question requires knowing which printed line of evidence the chapter itself records as disapproved, demonstrated by option 4's 'Embryological support for evolution as proposed by Ernst Heckel' against three evidences stated without qualification.
- **Note:** E1 called the shape statement_options because the content lives in the four options, but the stem neither prints a lettered block nor says 'statements', so on the v2 axis this is mcq. On the trap label: the device is a conceptual rule over-applied rather than a quantitative relation, and formula_misused was chosen as its family on the strength of 'the right one misremembered'. If this device recurs, a named value such as rule_overextended would carry it better.
<!--/ecat-->

## Q153

Biology · both · Biotechnology and Its Applications

The inactive form of Bt toxin is converted to the active form in the insect gut___________.

- (1) by nucleases
- **(2)** due to alkaline pH
- (3) due to acidic pH
- (4) by proteases

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NCERT states that the inactive Bt protoxin is converted to the active toxin due to the alkaline $pH$ of the insect gut, which solubilises the crystals, so the answer is option $2$.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 19)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q153_391ed33c_03112026.png?v=391ed33cd098)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The Bt protoxin crystal is solubilised and activated by the alkaline pH of the insect gut
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The printed condition is inverted on the pH scale: a student who carries 'digestive juices are acidic' from human digestion gives the gut the opposite pH to the one the Bt line states
- **Why:** This question requires the cause the text gives for one stated change, demonstrated by the stem 'The inactive form of Bt toxin is converted to the active form in the insect gut___________' and option 2's 'due to alkaline pH'.
- **Note:** E1 read this as fill_in_blank, an overlay under codebook §1; the printed shape is mcq.
<!--/ecat-->

## Q154

Biology · zoology · Human Health and Disease

Colostrum, secreted by mother during initial days of lactation, is abundant in

- (1) IgD
- (2) IgG
- (3) IgM
- **(4)** IgA

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Colostrum, secreted in the first days of lactation, contains several antibodies, mainly $\text{IgA}$, which give the infant passive immunity, so the answer is option $4$.

**Subtopic:** Active and Passive Immunity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 19)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q154_b107c690_03112026.png?v=b107c690f118)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Colostrum, the first milk, is abundant in IgA, which gives the newborn passive immunity
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  IgG is the antibody carried as 'the most abundant one', and the stem's own word is abundant, so a student matches the remembered superlative to the printed adjective and answers for the serum instead of for the colostrum
- **Why:** This question requires one stated composition fact, demonstrated by the stem 'Colostrum, secreted by mother during initial days of lactation, is abundant in' with four antibody classes as options.
<!--/ecat-->

## Q155

Biology · botany · Sexual Reproduction in Flowering Plants

Which of the following in female gametophyte of an angiosperm helps in guiding the pollen tube for fertilizing the eggs?

- (1) Polar nucleus
- (2) Antipodals
- **(3)** Synergids
- (4) Central cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The filiform apparatus at the micropylar tip of the synergids guides the pollen tube into the embryo sac, so the answer is Synergids, option $3$.

**Subtopic:** Megasporangium (Ovule) and Embryo Sac · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q155_1ec59f14_03112026.png?v=1ec59f149056)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The two synergids of the egg apparatus carry the filiform apparatus, which guides the pollen tube into the embryo sac at the micropylar end
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The antipodals are the other small group of cells printed in the same embryo-sac account, so a student who remembers that a group of cells beside the egg does the guiding but not which end of the sac they sit at takes the other trio
- **Why:** This question requires the stated function of one named part of the embryo sac, demonstrated by 'helps in guiding the pollen tube for fertilizing the eggs'.
- **Note:** Swap test applied: replacing 'Antipodals' with an unlike word keeps the pull, because what carries the student is that the two trios are printed together in the same embryo-sac account, so position decides it.
<!--/ecat-->

## Q156

Biology · zoology · Reproductive Health

Which of the following disease is not sexually transmitted?

- (1) Genital warts
- (2) Syphilis
- **(3)** Tuberculosis
- (4) Gonorrhoea

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Genital warts, syphilis and gonorrhoea are sexually transmitted infections, while tuberculosis (caused by $Mycobacterium\ tuberculosis$) spreads through the air, so the answer is option $3$.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q156_d41b8e6f_03112026.png?v=d41b8e6fdff1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gonorrhoea, syphilis and genital warts are on the printed list of sexually transmitted infections; tuberculosis is airborne and is not
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the printed list of sexually transmitted infections: genital warts, syphilis and gonorrhoea are all named on it, and the keyed answer, tuberculosis, is the only option absent from it. No wrong option is reachable by a route other than reading past the stem's 'not', and that misreading singles out none of the three, so no option can be named as the one it lands on.
- **Why:** This question requires membership of a printed list under a negated task, demonstrated by 'Which of the following disease is not sexually transmitted'.
<!--/ecat-->

## Q157

Biology · both · Molecular Basis of Inheritance

Which of the following statements about lac-operon is correct?

- (1) Galactose can act as an inducer of lac operon
- **(2)** Gene i is constitutively expressed
- (3) Lactose activates repressor to bind to the operator
- (4) Genes i, z, y and a share single common promoter

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Option 1: the inducer of the lac operon is lactose (allolactose), not galactose, so it is false.
2. Option 2: the $i$ gene codes for the repressor and is transcribed constitutively from its own promoter, so it is true.
3. Option 3: lactose binds the repressor and inactivates it, preventing binding to the operator, so it is false.
4. Option 4: only $z$, $y$ and $a$ share the common lac promoter; $i$ has its own promoter, so it is false.
5. Hence the correct option is $2$.

**Subtopic:** The Lac Operon · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 19)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q157_91a1f326_03112026.png?v=91a1f326947c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The i gene is transcribed all the time to supply the repressor, while z, y and a sit under the single lac promoter and are switched on only when lactose inactivates that repressor
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Galactose is one syllable away from lactose and is the sugar the chapter keeps printing inside beta-galactosidase and as a product of lactose, so a student holding 'the sugar that induces the operon' takes the wrong member of the pair
- **Why:** This question requires each printed claim about a named operon to be checked against the stated account, demonstrated by 'Which of the following statements about lac-operon is correct'.
- **Note:** Swap test applied: replacing 'Galactose' with a sugar unlike lactose kills the pull, so the resemblance between the two names is what carries the student and the likeness wins over the shared position.
<!--/ecat-->

## Q158

Biology · both · Biotechnology: Principles and Processes

Match List-I with List-II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Transformation | I | Restriction enzyme |
| B | Cloning site | II | Transfer DNA to host bacteria |
| C | Selection | III | Replication |
| D | Ori | IV | Antibiotic |

- (1) A-IV, B-I, C-III, D-II
- **(2)** A-II, B-I, C-IV, D-III
- (3) A-I, B-II, C-IV, D-III
- (4) A-III, B-IV, C-II, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Transformation is the transfer of DNA into a host bacterium, so $A \rightarrow II$.
2. A cloning site is a recognition site for a restriction enzyme, so $B \rightarrow I$.
3. Selection of transformants uses antibiotic resistance markers, so $C \rightarrow IV$.
4. Ori is the origin of replication, so $D \rightarrow III$.
5. $A$-$II$, $B$-$I$, $C$-$IV$, $D$-$III$ is option $2$.

**Subtopic:** Cloning Vectors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q158_61178910_03112026.png?v=61178910782c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A cloning vector's parts each do one job -- ori for replication, the cloning site for the restriction enzyme's cut, the marker read with an antibiotic -- while transformation is the step that puts the DNA into the host
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  "Cloning site" is read as the place where the cloning happens, i.e. inside the host, so it takes "Transfer DNA to host bacteria" and transformation is left with the restriction enzyme. The transfer is the transformation step; the cloning site is the stretch of vector the restriction enzyme cuts.
- **Why:** This question requires each part of the cloning workflow matched to the job it does, demonstrated by List-II printing jobs and tools -- "Transfer DNA to host bacteria", "Restriction enzyme", "Replication", "Antibiotic" -- one per item in List-I. Rule 5 test applied before choosing the trap label: "Cloning site" and "Transformation" neither resemble each other nor stand or fall by their printed order; what the option does is move a correctly understood event, the transfer of DNA into the host, onto the wrong part of the system, which is wrong_site_attacked.
<!--/ecat-->

## Q159

Biology · zoology · Evolution

A population of diploid organisms is at Hardy-Weinberg equilibrium. If the frequency of allele A is $0.1$, the frequency of AA is

- (1) $0.99$
- **(2)** $0.01$
- (3) $0.02$
- (4) $0.10$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. At Hardy-Weinberg equilibrium the genotype frequencies are $p^2 : 2pq : q^2$, with $f(AA) = p^2$.
2. $f(AA) = p^2 = (0.1)^2 = 0.01$, which is option $2$.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q159_7f900a58_03112026.png?v=7f900a583162)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Under Hardy-Weinberg the frequency of a homozygote is the square of its allele frequency, so an allele frequency of 0.1 gives an AA frequency of 0.01
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  0.10 is the number the stem hands over as the frequency of allele A, so a student who has not separated allele frequency from genotype frequency reads 'the frequency of AA' as asking for the same quantity again
- **Why:** This question requires a number computed from the figure supplied, demonstrated by 'If the frequency of allele A is 0.1, the frequency of AA is'.
<!--/ecat-->

## Q160

Biology · zoology · Locomotion and Movement

Sperm motility is due to _________.

- (1) muscular movement
- **(2)** flagellar movement
- (3) ciliary movement
- (4) amoeboid movement

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The sperm tail is a flagellum, and its beating moves the sperm, so sperm motility is flagellar movement, which is option $2$.

**Subtopic:** Introduction and Types of Movement · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q160_3cd1c3b7_03112026.png?v=3cd1c3b7ff78)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The three types of cell movement are amoeboid, ciliary and flagellar, and the sperm's tail is a flagellum, so sperm swim by flagellar movement
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Ciliary movement is printed in the same sentence pair as flagellar movement, and both are whip-like appendages with the same internal build, so a student who holds 'the sperm is moved by a beating appendage' and not which appendage takes the neighbour
- **Why:** This question requires the stated type of movement for a named cell, demonstrated by 'Sperm motility is due to _________'.
- **Note:** Swap test applied: replacing 'ciliary movement' with an unlike term kills nothing about the resemblance of the words, since they resemble nothing; what carries the student is that the two types are printed side by side, so the label is nearby_fact.
<!--/ecat-->

## Q161

Biology · botany · Organisms and Populations

Consider a population of 10 million cells. Given the per-capita birth rate of 0.002 (per unit time) and the per-capita death rate of 0.002 (per unit time), the expected number of cells after 10 generations is

- (1) 100 million
- (2) 1 million
- (3) 5 million
- **(4)** 10 million

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Intrinsic rate of increase $r = b - d = 0.002 - 0.002 = 0$.
2. $N_t = N_0 e^{rt} = N_0 e^{0} = N_0$.
3. $N_t = 10$ million, which is option $4$.

**Subtopic:** Exponential Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q161_8c4e2aee_03112026.png?v=8c4e2aee4528)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In the exponential growth equation the intrinsic rate is the birth rate minus the death rate, so equal birth and death rates leave the population unchanged however long it runs
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student who reads 'after 10 generations' as a growth multiplier applies the 10 to the starting 10 million and gets 100 million, instead of first working out that $r = b - d = 0$
- **Why:** This question requires a number computed from the rates supplied, demonstrated by 'per-capita birth rate of 0.002 ... per-capita death rate of 0.002 ... after 10 generations'.
<!--/ecat-->

## Q162

Biology · zoology · Evolution

Given below are two statements : one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) Forelimbs of human and bats are homologous.
- (Reason R) Forelimbs of humans and bats have similar anatomical structure.

- (1) A is false but R is true
- **(2)** Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are true, but R is not the correct explanation of A
- (4) A is true but R is false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Homologous organs are those with the same basic anatomical structure and origin but different functions (divergent evolution).
2. Human and bat forelimbs share the same bone pattern: humerus, radius and ulna, carpals, metacarpals, phalanges, so A is true.
3. R states that they have similar anatomical structure, which is true.
4. Similar anatomical structure is the basis on which the forelimbs are called homologous, so R correctly explains A, which is option $2$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q162_da8634dd_03112026.png?v=da8634ddac2c)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Homologous organs share one underlying anatomical plan inherited from a common ancestor, however differently they are used
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Homology is held to its strict ground, common ancestry, and the shared anatomy is then judged a consequence rather than the reason -- all the more so because analogous organs can also look alike. Shared anatomical structure under different functions is the very criterion by which human and bat forelimbs are called homologous.
- **Why:** This question requires shared internal structure recognised as the ground on which organs are called homologous, demonstrated by R reading "Forelimbs of humans and bats have similar anatomical structure" against the Assertion that they "are homologous".
- **Note:** Options 1, 3 and 4 in this question are worded with true/false while option 2 is worded with correct; the four verdicts are the standard set and the wording difference does not change what is being asked, so it had no effect on the tagging.
<!--/ecat-->

## Q163

Biology · zoology · Locomotion and Movement

Muscle contraction is initiated by a signal sent by the central nervous system by the release of _______.

- (1) cyclic adenine monophosphate
- **(2)** acetyl choline
- (3) acetyl coenzyme A
- (4) cyclic guanine monophosphate

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Muscle contraction starts when a signal from the CNS reaches the neuromuscular junction through a motor neuron and releases the neurotransmitter acetylcholine, which is option $2$.

**Subtopic:** Mechanism of Muscle Contraction and Red and White Muscle Fibre · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q163_378dc572_03112026.png?v=378dc57296b0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The motor neuron releases acetylcholine at the neuromuscular junction, and that neurotransmitter generates the action potential that starts contraction
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Acetyl choline and acetyl coenzyme A share their first word, so a student who holds 'the acetyl compound of the signal' and not which one it is takes the respiratory carrier instead of the neurotransmitter
- **Why:** This question requires the stated substance released to begin a named process, demonstrated by 'initiated by a signal sent by the central nervous system by the release of _______'.
- **Note:** Swap test applied: replacing 'acetyl coenzyme A' with an unlike name kills the pull, so the shared word and not the position is carrying the student.
<!--/ecat-->

## Q164

Biology · zoology · Human Reproduction

Which of the following hormone is not secreted by human placenta?

- **(1)** LH
- (2) hCG
- (3) Estrogen
- (4) Progesterone

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the placenta secretes hCG, hPL, estrogens and progestogens; LH comes from the anterior pituitary, so the answer is option $1$.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q164_d595a2e3_03112026.png?v=d595a2e3cf38)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The placenta is itself an endocrine organ, secreting hCG, hPL, estrogens and progestogens, while LH comes from the anterior pituitary
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The corpus luteum is the source printed for progesterone in the menstrual-cycle account, so a student who files the hormone with that one gland reads it as not placental and ticks it under the stem's 'not'
- **Why:** This question requires the stated set of hormones from one named organ under a negated task, demonstrated by 'Which of the following hormone is not secreted by human placenta'.
- **Note:** Swap test applied: replacing 'Progesterone' with an unlike hormone name keeps the pull, because what carries the student is that the corpus luteum is printed as its source beside the placental list, so position decides it.
<!--/ecat-->

## Q165

Biology · zoology · Human Health and Disease

Which of the following statements is correct about Plasmodium?

- **(1)** Fertilization takes place in mosquito gut
- (2) Reproduces sexually in liver cells
- (3) Reproduces sexually in RBCs
- (4) Gametocytes develop in mosquito gut

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In humans Plasmodium multiplies asexually in liver cells and RBCs, which rules out options $2$ and $3$; gametocytes develop in human RBCs, not the mosquito gut, which rules out option $4$; fertilisation and development take place in the mosquito's stomach (gut), so the answer is option $1$.

**Subtopic:** Protozoal Diseases (Malaria) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q165_51424f78_03112026.png?v=51424f78e64b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plasmodium multiplies asexually in human liver cells and red blood cells, where the gametocytes form, and its sexual phase with fertilisation happens in the mosquito's gut
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  The gametocytes are the right structure moved one stage too early: they develop in human red blood cells and are only taken up by the mosquito, where the next event, fertilisation, is what happens in the gut
- **Why:** This question requires each printed claim about where a stage occurs to be checked, demonstrated by 'Which of the following statements is correct about Plasmodium'.
<!--/ecat-->

## Q166

Biology · botany · Ecosystem

Which of the following are primary consumers in a food chain?

- (1) Carnivores
- (2) Parasites
- (3) Predators
- **(4)** Herbivores

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Primary consumers eat producers (green plants) directly, so they are herbivores, which is option $4$.

**Subtopic:** Food Chains and Food Web · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q166_e2bf1b56_03112026.png?v=e2bf1b56e35b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a grazing food chain the plants are the producers and the herbivores that eat them are the primary consumers, with carnivores one level above
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Carnivores are the level printed immediately above the herbivores, so a student who reads 'primary' as the principal or top consumer, or who starts counting consumers at the herbivore, slips one level up
- **Why:** This question requires the stated name of one trophic level, demonstrated by 'Which of the following are primary consumers in a food chain'.
<!--/ecat-->

## Q167

Biology · zoology · Excretory Products and Their Elimination

Which of the following statements about the reabsorption process in Henle's loop are correct? Choose the correct answer from the options given below:

- (a) The descending limb of Henle's loop is permeable to water but almost impermeable to electrolytes.
- (b) Urine gets concentrated in Henle's loop.
- (c) Reabsorption of $\mathrm{Na^{+}}$ and water takes place in Henle's loop.
- (d) Active or passive transport of electrolytes occurs in the ascending limb of Henle's loop.

- **(1)** (a), (b) and (d) only
- (2) (a) and (b) only
- (3) (b), (c) and (d) only
- (4) (a), (b) and (c) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Statement (a): NCERT states the descending limb of Henle's loop is permeable to water but almost impermeable to electrolytes, so (a) is true.
2. Statement (d): NCERT states the ascending limb is impermeable to water but allows transport of electrolytes actively or passively, so (d) is true.
3. Statement (b): the filtrate is concentrated as it moves down the descending limb, so (b) is taken as true.
4. Only option $1$, (a), (b) and (d), contains both (a) and (d), so the answer is option $1$.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 20)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q167_15873c63_03112026.png?v=15873c63e732)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In Henle's loop the descending limb lets water out but holds electrolytes in, and the ascending limb lets electrolytes out but holds water in; conditional reabsorption of Na+ together with water belongs to the distal convoluted tubule
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Statement (c) is the tubule chapter's distal-convoluted-tubule sentence, reabsorption of Na+ and water, moved onto Henle's loop, so a student who recognises the sentence as true of the nephron admits it here
- **Why:** This question requires the reabsorption facts NCERT assigns to each limb of Henle's loop, demonstrated by statement (c) 'Reabsorption of Na+ and water takes place in Henle's loop', which is the line the chapter prints for the distal convoluted tubule.
- **Note:** Label chosen on the section 5.1 reading of wrong_site_attacked as the right change made at the wrong stage or site; the process in statement (c) is real and only its segment is wrong, which is why nearby_fact was not used.
<!--/ecat-->

## Q168

Biology · botany · Organisms and Populations

Given below are two statements: one is labelled as Assertion A and the other is labelled as Reason R. In the light of the above statements, choose the most appropriate answer from the options given below:

- (Assertion A) The logistic growth model of populations is considered more realistic than the exponential growth model.
- (Reason R) Resources are finite.

- (1) A is not correct but R is correct
- **(2)** Both A and R are correct and R is the correct explanation of A
- (3) Both A and R are correct but R is not the correct explanation of A
- (4) A is correct but R is not correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Assertion A is true: the logistic (Verhulst-Pearl) model, $\frac{dN}{dt} = rN\left(\frac{K-N}{K}\right)$, is considered more realistic than exponential growth.
2. Reason R is true: no population has unlimited resources, so resources are finite.
3. Finite resources impose a carrying capacity $K$, which is exactly why logistic growth is more realistic, so R correctly explains A: option $2$.

**Subtopic:** Logistic Growth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q168_28d89e97_03112026.png?v=28d89e971b27)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** No population has unlimited resources, so growth slows towards a carrying capacity -- which is why the logistic sigmoid model describes nature better than exponential growth
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  R is granted as obviously true and then rejected as an explanation because it is a bare general fact that names neither growth model. Finite resources are the whole reason a carrying capacity exists, and a carrying capacity is what makes the logistic curve the realistic one.
- **Why:** This question requires the finiteness of resources recognised as the reason one growth model is the realistic one, demonstrated by R reading "Resources are finite" against an Assertion comparing "the logistic growth model" with "the exponential growth model".
<!--/ecat-->

## Q169

Biology · zoology · Locomotion and Movement

Which of the following is the correct order of arrangement of vertebrate column from the head to toe?

- **(1)** Cervical vertebra, thoracic vertebra, lumbar vertebra, sacrum
- (2) Cervical vertebra, thoracic vertebra, sacrum, lumbar vertebra
- (3) Sacrum, lumbar vertebra, thoracic vertebra, cervical vertebra
- (4) Cervical vertebra, lumbar vertebra, thoracic vertebra, sacrum

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. From head to toe the vertebral column is arranged as cervical $\rightarrow$ thoracic $\rightarrow$ lumbar $\rightarrow$ sacrum, which is option $1$.

**Subtopic:** Axial Skeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q169_754169c8_03112026.png?v=754169c8d65f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The vertebral column runs cervical, thoracic, lumbar, sacral and coccygeal from the skull downwards
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  This option prints the whole series backwards, every adjacency intact and only the direction wrong, so a student who has the regions in order and reads the stem's two endpoints as naming the finishing point first takes it
- **Why:** This question requires a printed sequence to be reproduced in the direction the stem sets, demonstrated by 'the correct order of arrangement of vertebrate column from the head to toe'.
- **Note:** The stem reads 'vertebrate column' where 'vertebral column' is meant; the rating follows the question as printed. reversed is used because this option set prints the exact reverse of the key, which is the one wrong order a student with the series correctly memorised can still reach.
<!--/ecat-->

## Q170

Biology · botany · Organisms and Populations

Match List-I with List-II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Both species are harmed | I | Predation |
| B | One species is harmed and the other is benefited | II | Mutualism |
| C | Both species are benefited | III | Competition |
| D | One is benefited while the other has no effect | IV | Commensalism |

- **(1)** A-III, B-I, C-II, D-IV
- (2) A-III, B-IV, C-II, D-I
- (3) A-I, B-II, C-III, D-IV
- (4) A-II, B-I, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Both species harmed $(-/-)$ is competition, so $A \to III$.
2. One harmed and the other benefited $(+/-)$ is predation, so $B \to I$.
3. Both benefited $(+/+)$ is mutualism, so $C \to II$.
4. One benefited and the other unaffected $(+/0)$ is commensalism, so $D \to IV$.
5. $A\text{-}III, B\text{-}I, C\text{-}II, D\text{-}IV$ is option $1$.

**Subtopic:** Population Interactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q170_d6b32961_03112026.png?v=d6b32961f281)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each population interaction is named by who gains and who loses: both lose in competition, one gains at the other's cost in predation, both gain in mutualism, one gains and the other is unaffected in commensalism
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Commensalism is carried as "one lives at the other's expense", which is the pattern of the neighbouring interaction in the same table, so the harmed-and-benefited row takes commensalism and predation is pushed onto the row where one species is unaffected. Commensalism is the interaction in which the second species is neither helped nor harmed.
- **Why:** This question requires the name NCERT gives to each outcome pattern, demonstrated by List-I printing the patterns in words -- "Both species are harmed", "One is benefited while the other has no effect" -- against the four interaction names in List-II. Rule 5 test applied: Predation and Commensalism do not resemble each other as words, so what carries the student is the sign pattern of another member of the same printed family, which is nearby_fact.
<!--/ecat-->

## Q171

Biology · botany · Sexual Reproduction in Flowering Plants

If the diploid chromosome number of typical angiosperm is 36, what would be the chromosome number in its endosperm?

- (1) 72
- (2) 18
- (3) 36
- **(4)** 54

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Endosperm forms from triple fusion (one male gamete $n$ + two polar nuclei $2n$), so it is triploid, $3n$.
2. $2n = 36 \Rightarrow n = 18$.
3. $3n = 3 \times 18 = 54$, which is option $4$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q171_9ce51524_03112026.png?v=9ce515248759)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The endosperm is triploid, formed from two polar nuclei and one male gamete, so its chromosome number is three times the haploid number
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  18 is the correct first step, half of the printed 36, and a student who recalls that the endosperm forms inside the haploid embryo sac stops there instead of tripling it
- **Why:** This question requires a number computed from the figure supplied, demonstrated by 'If the diploid chromosome number of typical angiosperm is 36, what would be the chromosome number in its endosperm'.
<!--/ecat-->

## Q172

Biology · both · Molecular Basis of Inheritance

Which of the following enzymes synthesizes precursor mRNA?

- (1) DNA polymerase
- (2) RNA polymerase I
- **(3)** RNA polymerase II
- (4) RNA polymerase III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In eukaryotes, RNA polymerase I makes rRNAs, RNA polymerase III makes tRNA, 5S rRNA and snRNAs, and RNA polymerase II transcribes precursor mRNA (hnRNA), which is option $3$.

**Subtopic:** Transcription · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 21)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q172_02b27508_03112026.png?v=02b27508a97b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Eukaryotes use three RNA polymerases: pol I makes rRNA, pol II makes the precursor of mRNA, and pol III makes tRNA, 5S rRNA and the snRNAs
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  The three polymerases differ only by a roman numeral, so a student who has memorised that there are three and that each has its own product can hold the set and still hand the headline product, mRNA, to the first numeral
- **Why:** This question requires the stated assignment of one enzyme to one transcript, demonstrated by 'Which of the following enzymes synthesizes precursor mRNA'.
- **Note:** Swap test applied: replacing 'RNA polymerase I' with an unlike enzyme name kills the pull, because the three option names are distinguished by nothing but the numeral, so the resemblance and not the position is carrying the student; by the rulebook's tie-break the likeness wins.
<!--/ecat-->

## Q173

Biology · both · Biotechnology: Principles and Processes

Given below are two statements:
Statement I: Plasmids are autonomously replicating DNA.
Statement II: Plasmids are extrachromosomal DNA.
In the light of the above statements, choose the most appropriate answer from the options given below:

- (Statement I) Plasmids are autonomously replicating DNA.
- (Statement II) Plasmids are extrachromosomal DNA.

- (1) Statement I is incorrect but Statement II is correct
- **(2)** Both Statement I and Statement II are correct
- (3) Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Plasmids have their own origin of replication and replicate independently of chromosomal DNA, so Statement I is correct.
2. Plasmids lie outside the bacterial chromosome, i.e. they are extrachromosomal DNA, so Statement II is correct.
3. Both statements are correct, which is option $2$.

**Subtopic:** Principles of Biotechnology · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 21)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q173_fba65748_03112026.png?v=fba65748e8a1)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A plasmid is a small circular DNA lying outside the bacterial chromosome that carries its own origin of replication, so it copies itself independently of the host chromosome
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Statement I and Statement II are two descriptors of the same molecule lifted from one NCERT definition line, 'autonomously replicating' and 'extrachromosomal', so no option offers a rival fact; option 3 would need both of NCERT's own words to be wrong, and options 1 and 4 each need one of the two words to fail while the other stands, but the single sentence that supplies one supplies the other
- **Why:** This question requires confirming the two NCERT descriptors of a plasmid, demonstrated by Statement I reading 'Plasmids are autonomously replicating DNA' and Statement II 'Plasmids are extrachromosomal DNA', the two halves of one printed definition.
<!--/ecat-->

## Q174

Biology · botany · Sexual Reproduction in Flowering Plants

How many theca are present in each lobe of a typical bilobed angiosperm anther?

- (1) 12
- **(2)** 2
- (3) 6
- (4) 8

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. A typical angiosperm anther is bilobed and each lobe is dithecous, i.e. has $2$ theca, which is option $2$.

**Subtopic:** Flower – Male Reproductive System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q174_3d0491bc_03112026.png?v=3d0491bc26e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A typical angiosperm anther is bilobed and dithecous, with two theca in each lobe and four microsporangia in all
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The anther counts NCERT prints are 2 lobes, 2 theca per lobe and 4 microsporangia. The one figure that could be substituted for the keyed 2 is 4, the total microsporangia, and 4 is not among the options; 12, 6 and 8 answer no printed anther count and are produced by no operation on the printed numbers, so no wrong option has a route.
- **Why:** This question requires a stored count stated in the source rather than one computed, demonstrated by 'How many theca are present in each lobe of a typical bilobed angiosperm anther'.
- **Note:** The count is read off the source line about a dithecous anther, which is why asks is fact_line and not calculate even though the answer is a number: nothing in the stem is multiplied or divided.
<!--/ecat-->

## Q175

Biology · zoology · Evolution

Natural selection can lead to
Choose the correct answer from the options given below:

- (a) stabilisation
- (b) genetic drift
- (c) directional change
- (d) disruption

- (1) (a) and (c) only
- (2) (a) only
- **(3)** (a), (c) and (d) only
- (4) (a), (b), (c) and (d)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT describes three outcomes of natural selection: stabilising (a), directional (c) and disruptive (d); genetic drift (b) is a chance effect, not natural selection, so the answer is (a), (c) and (d) only, option $3$.

**Subtopic:** Types of Natural Selection · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q175_fdabe011_03112026.png?v=fdabe011bf96)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Natural selection acts in three ways — stabilising toward the mean, directional away from it, and disruptive toward both extremes — while genetic drift is random change unconnected to selection
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Genetic drift is printed in the same evolution section as the mechanism that changes gene frequencies alongside selection, so a student reading the stem as 'what changes a population' sweeps it in with the three types of selection
- **Why:** This question requires the three outcomes NCERT attributes to natural selection, demonstrated by item (b) 'genetic drift' sitting among them in the printed list.
<!--/ecat-->

## Q176

Biology · botany · Ecosystem

Which of the following statements are correct? Choose the correct answer from the options given below:

- (a) Energy flow from producers to consumers is unidirectional
- (b) Energy pyramid can never be inverted
- (c) Transfer of energy follows the $1\%$ law

- (1) (b) and (c) only
- (2) (a), (b) and (c)
- **(3)** (a) and (b) only
- (4) (a) and (c) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Energy flows one way, from producers to consumers ($\text{sun} \rightarrow$ producers $\rightarrow$ consumers), so statement (a) is correct.
2. Each trophic level holds less energy than the level below it, so the energy pyramid is always upright and can never be inverted; statement (b) is correct.
3. Energy transfer between trophic levels follows Lindeman's $10\%$ law, not a $1\%$ law, so statement (c) is incorrect.
4. Only (a) and (b) are correct, which is option $3$.

**Subtopic:** Energy Flow, Ecological Pyramids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q176_40694de3_03112026.png?v=40694de310e8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Energy moves one way from producers to consumers and the pyramid of energy is always upright; the transfer between trophic levels follows the 10 per cent law
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The energy-flow section carries two percentages — about 10 per cent passed on between trophic levels and the small percentage of incident light the producers capture — and statement (c) prints the second-sized number as the transfer law, so a student who remembers that a one-figure percentage belongs here accepts it
- **Why:** This question requires the stated rules of energy flow and of the ecological pyramids, demonstrated by statement (c) 'Transfer of energy follows the 1% law' against the 10 per cent law the chapter prints.
<!--/ecat-->

## Q177

Biology · zoology · Chemical Coordination and Integration

Match List-I with List-II. Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A | Excess growth hormone | I | Reabsorption of water and electrolytes in kidney |
| B | Luteinizing hormone | II | Contraction of uterus during child birth |
| C | Vasopressin | III | Acromegaly |
| D | Oxytocin | IV | Ovulation |

- (1) A-IV, B-III, C-I, D-II
- (2) A-III, B-IV, C-II, D-I
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-II, B-IV, C-I, D-III

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Excess growth hormone in adults causes acromegaly, so $A \rightarrow III$.
2. The LH surge induces ovulation, so $B \rightarrow IV$.
3. Vasopressin (ADH) stimulates reabsorption of water and electrolytes in the kidney tubules, so $C \rightarrow I$.
4. Oxytocin causes contraction of the uterus during child birth, so $D \rightarrow II$.
5. $A$-III, $B$-IV, $C$-I, $D$-II matches option $3$.

**Subtopic:** The Pituitary Gland · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 22)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q177_0fc0caf4_03112026.png?v=0fc0caf40d22)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each pituitary hormone has one named action or disorder: excess growth hormone gives acromegaly, LH triggers ovulation, vasopressin conserves water in the kidney and oxytocin contracts the uterus at birth
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The two posterior-pituitary hormones are released together and are learnt as one pair, so their actions are entered the other way round -- vasopressin on uterine contraction, oxytocin on water reabsorption -- while the two anterior rows stay right. Vasopressin acts on the kidney tubule and oxytocin on the uterine muscle.
- **Why:** This question requires each hormone matched to its own stated action or disorder, demonstrated by List-II printing "Reabsorption of water and electrolytes in kidney", "Contraction of uterus during child birth", "Acromegaly" and "Ovulation" -- one effect per hormone. Rule 5 test applied: "Vasopressin" and "Oxytocin" bear no resemblance to each other, so what carries the student is that they are the pair printed together as the posterior pituitary's output, which is nearby_fact.
<!--/ecat-->

## Q178

Biology · zoology · Human Health and Disease

Which of the following are secondary lymphoid organs? Choose the correct answer from the options given below:

- (a) Bone marrow
- (b) Tonsils
- (c) Spleen
- (d) Thymus

- (1) (a) and (d) only
- (2) (a) and (b) only
- **(3)** (b) and (c) only
- (4) (b) and (d) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the primary lymphoid organs are bone marrow and thymus, so (a) and (d) are excluded; the secondary lymphoid organs include spleen, lymph nodes, tonsils, Peyer's patches and MALT, so (b) tonsils and (c) spleen are secondary, giving option $3$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 22)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q178_3ab44413_03112026.png?v=3ab44413ac34)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bone marrow and thymus are the primary lymphoid organs where lymphocytes are made and mature; spleen, tonsils, lymph nodes, Peyer's patches and the appendix are secondary, where mature lymphocytes meet antigen
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Bone marrow and thymus are the pair the chapter names, correctly, as the primary lymphoid organs, so an eye that reaches the familiar pair before registering the stem's word 'secondary' answers the other half of the same classification
- **Why:** This question requires the split NCERT draws between primary and secondary lymphoid organs, demonstrated by the stem asking 'Which of the following are secondary lymphoid organs' while items (a) and (d) are the primary pair.
<!--/ecat-->

## Q179

Biology · both · Biotechnology: Principles and Processes

During PCR, primers bind to the DNA strands in the ________ step.

- (1) ligation
- (2) denaturation
- (3) extension
- **(4)** annealing

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. PCR cycle: denaturation separates strands, annealing lets primers bind to the template, extension lengthens them; so primers bind in annealing, option $4$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q179_078efc18_03112026.png?v=078efc182557)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A PCR cycle runs denaturation, then annealing where the two primers pair with the separated strands, then extension by a thermostable polymerase
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Denaturation is the step immediately before the one asked and is the step whose printed description is about the DNA strands separating, so a student who reads the stem's 'bind to the DNA strands' as pointing at the strand step takes the one before annealing
- **Why:** This question requires the stated step of a named procedure, demonstrated by 'primers bind to the DNA strands in the ________ step'.
<!--/ecat-->

## Q180

Biology · zoology · Principles of Inheritance and Variation

Given below are two statements:
Statement I: Down's syndrome is caused by the absence of one of the X-chromosomes.
Statement II: Turner's syndrome is caused by the presence of an additional copy of the chromosomes.
In the light of the above statements, choose the correct answer from the options given below:

- (Statement I) Down's syndrome is caused by the absence of one of the X-chromosomes.
- (Statement II) Turner's syndrome is caused by the presence of an additional copy of the chromosomes.

- (1) Statement I is incorrect but Statement II is correct
- (2) Both Statement I and Statement II are correct
- **(3)** Both Statement I and Statement II are incorrect
- (4) Statement I is correct but Statement II is incorrect

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Down's syndrome is caused by an additional copy of chromosome 21 (trisomy 21), not by absence of an X chromosome, so Statement I is incorrect.
2. Turner's syndrome is caused by the absence of one X chromosome ($44 + XO$, i.e. $45, X0$), not by an additional chromosome, so Statement II is incorrect.
3. Both statements are incorrect, which is option $3$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 22)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2026/2026_70/crops/q180_741c0c83_03112026.png?v=741c0c83f671)

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Down's syndrome is an extra copy of chromosome 21, Turner's syndrome is the loss of one X giving 45, X0 — the extra chromosome and the missing X belong to opposite disorders
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Each statement is NCERT's own cause clause printed under the other disorder's name, so the wording of both reads familiar and both get ticked true without the name being matched to the clause
- **Why:** This question requires the cause NCERT states for each named chromosomal disorder, demonstrated by Statement I reading 'Down's syndrome is caused by the absence of one of the X-chromosomes', which is the line the book prints for Turner's.
<!--/ecat-->

