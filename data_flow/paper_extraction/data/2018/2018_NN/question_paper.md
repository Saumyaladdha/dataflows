# NEET (UG) 2018 · Code NN

180 questions · source `NEET_Papers/2018/NEET_2018_Code_NN_official.pdf` · every image a CDN link (0 without one) · 7 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Electromagnetic Induction

The magnetic potential energy stored in a certain induction is $25\,\mathrm{Mj}$, when the current in the inductors is $60\,\mathrm{Ma}$. This inductors is of inductance

- (1) $13.89\,\mathrm{H}$
- (2) $0.138\,\mathrm{H}$
- (3) $1.389\,\mathrm{H}$
- (4) $138.88\,\mathrm{H}$

**Answer** — booklet: (none) · independent solve: (1) · unchecked

**Publisher's solution**

1. $U = \frac{1}{2}LI^{2}$
2. $25\times 10^{-3} = \frac{1}{2}L\left(60\times 10^{-3}\right)^{2}$
3. $\Rightarrow L = \frac{50\times 10^{-3}}{3600\times 10^{-6}}$
4. $= \frac{25\times 10}{103}$
5. $= 13.89\,\mathrm{H}$

**Solved independently** (answer withheld)

1. Energy stored in an inductor: $U = \frac{1}{2} L I^2$.
2. Rearrange for inductance: $L = \frac{2U}{I^2}$.
3. Substitute $U = 25\,\mathrm{mJ} = 25 \times 10^{-3}\,\mathrm{J}$ and $I = 60\,\mathrm{mA} = 60 \times 10^{-3}\,\mathrm{A}$: $L = \frac{2 \times 25 \times 10^{-3}}{(60 \times 10^{-3})^2}$.
4. $L = \frac{0.05}{3.6 \times 10^{-3}} = 13.89\,\mathrm{H}$, which is option $1$.

**Subtopic:** Energy Stored in an Inductor · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 1)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q001_1240ede2_03112026.png?v=1240ede2f9a3)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q001_f22e29c9_03112026.png?v=f22e29c95935)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The energy stored in an inductor is $U=\tfrac12 LI^2$, so the inductance follows as $L=2U/I^2$ once the energy and the current are put in SI units
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No key is stored for this question (`correct_answer` is null, `accepted_answers` is empty, `answer_line_as_printed` is null) and the stem's unit prefixes are stored as '25 Mj' and '60 Ma', so which option the paper awarded cannot be read off the record and no option can be called wrong.
- **Why:** This question requires the stored-energy relation to be inverted for $L$, demonstrated by the stem giving the magnetic potential energy and the current and asking 'This inductors is of inductance'.
- **Note:** Two separate gaps in our record, not in the paper: the answer key is absent, and the prefixes read 'Mj' and 'Ma' where the quantities and the option ladder both point to mJ and mA. A reviewer holding the printed paper should check $L = 2U/I^2 = 2(25\times10^{-3})/(60\times10^{-3})^2 = 13.89\,\mathrm{H}$ against option 1, and then test the three remaining options as a power-of-ten ladder (0.138, 1.389, 138.88) produced by mishandling the milli prefixes rather than by any wrong relation.
<!--/ecat-->

## Q2

Physics · Ray Optics

An object is placed at a distance of $40\,\mathrm{cm}$ from a concave mirror of focal length $15\,\mathrm{cm}$ If the object is displaced through a distance of $20\,\mathrm{cm}$ towards the mirrors, the displacement of the image will be

- (1) $36\,\mathrm{cm}$ towards the mirror
- (2) $30\,\mathrm{cm}$ away from the mirror
- (3) $30\,\mathrm{cm}$ towards the mirror
- **(4)** $36\,\mathrm{cm}$ away from the mirror

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\frac{1}{f} = \frac{1}{v} + \frac{1}{q}$
2. $\Rightarrow -\frac{1}{15} = \frac{1}{v} - \frac{1}{40}$
3. $\Rightarrow \frac{1}{v} = -\frac{1}{15} + \frac{1}{40}$
4. $\Rightarrow v = \frac{-600}{25}$
5. $v = -24\,\mathrm{cm}$
6. Finally $\frac{1}{15} = \frac{1}{v^{1}} - \frac{1}{20}$
7. $\Rightarrow -\frac{1}{15} + \frac{1}{20} = \frac{1}{v^{1}}$
8. $\Rightarrow v^{1} = \frac{300}{5}$
9. So image is displaced by $36\,\mathrm{cm}$ away from mirror (d)

**Solved independently** (answer withheld)

1. Use the mirror formula $\frac{1}{v} + \frac{1}{u} = \frac{1}{f}$ with $f = -15\,\mathrm{cm}$ (concave).
2. Initial position $u_1 = -40\,\mathrm{cm}$: $\frac{1}{v_1} = -\frac{1}{15} + \frac{1}{40} = \frac{-8+3}{120} = -\frac{1}{24}$, so $v_1 = -24\,\mathrm{cm}$.
3. Object moved $20\,\mathrm{cm}$ towards the mirror: $u_2 = -20\,\mathrm{cm}$.
4. $\frac{1}{v_2} = -\frac{1}{15} + \frac{1}{20} = \frac{-4+3}{60} = -\frac{1}{60}$, so $v_2 = -60\,\mathrm{cm}$.
5. The image shifts from $24\,\mathrm{cm}$ to $60\,\mathrm{cm}$ in front of the mirror: $|\Delta v| = 60 - 24 = 36\,\mathrm{cm}$ away from the mirror, which is option $4$.

**Subtopic:** Mirror Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 1)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q002_e5189756_03112026.png?v=e5189756e8dc)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q002_e4923140_03112026.png?v=e4923140f87b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The mirror equation has to be solved twice -- once for each object position -- and the image displacement is the difference of the two image distances, with its direction read from which one is larger
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The two image distances come out right, 24 cm and 60 cm, and then the 36 cm is read as a movement towards the mirror because the object was moved towards the mirror
- **Why:** This question requires the mirror equation solved at two object distances and the two image positions compared, demonstrated by the options pairing a magnitude with a direction, '36 cm towards the mirror' against '36 cm away from the mirror'.
- **Note:** E1's pattern returned statement_options because each option is a phrase rather than a bare number; the printed shape is a plain MCQ whose options are a magnitude plus a direction, so qtype is recorded as mcq.
<!--/ecat-->

## Q3

Physics · Electromagnetic Waves

An em wave is propagating in a medium with a velocity $\vec{V} = V\hat{i}$. The instantaneous oscillating electric field of this em wave is along $+y$ axis. Then the direction of oscillating magnetic field of the em wave will be along

- (1) $-x$ direction
- (2) $-z$ direction
- (3) $-y$ direction
- **(4)** $+z$ direction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Direction of propagation of Em wave is same as $\vec{E} \times \vec{B}$
2. So, $\hat{i} = \hat{j} \times (B)$
3. So direction of $B$ is along $k$

**Solved independently** (answer withheld)

1. An em wave travels along $\vec{E} \times \vec{B}$, so $\hat{E} \times \hat{B} = \hat{V} = \hat{i}$.
2. With $\hat{E} = \hat{j}$, we need $\hat{j} \times \hat{B} = \hat{i}$.
3. Since $\hat{j} \times \hat{k} = \hat{i}$, $\hat{B} = +\hat{k}$, i.e. the $+z$ direction, which is option $4$.

**Subtopic:** Transverse Nature of Electromagnetic Waves · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 1)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q003_13be67a1_03112026.png?v=13be67a178aa)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q003_97508df8_03112026.png?v=97508df8ffdc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In an electromagnetic wave $\vec E$, $\vec B$ and the direction of travel form a right-handed set in that order, so $\hat B = \hat v \times \hat E$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The right triad is used but in the other order -- $\hat E \times \hat v = \hat j \times \hat i = -\hat k$ -- which turns the answer round to $-z$
- **Why:** This question requires the right-handed $\vec E$-$\vec B$-propagation rule applied to a stated case, demonstrated by the stem fixing $\vec V = V\hat i$ and $\vec E$ 'along $+y$ axis' and asking only for the direction of $\vec B$.
<!--/ecat-->

## Q4

Physics · Ray Optics

The refractive index of the material of a prism is $\sqrt{2}$ and the angle of the prism is $30^{0}$. One of the two refracting surface of the prism is made a mirror inwards, by silver coating. A beam of monochromatic light entering the prism from the other face will retrace its path (after reflection from the silvered surface) if its angle of incidence on the prism is

- (1) Zero
- (2) $60^{0}$
- (3) $30^{0}$
- **(4)** $45^{0}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. According to question
2. Ray will retrace its path if $r_{2} = 0$
3. Also,
4. $A = r_{1} + r_{2}$
5. $\Rightarrow 30^{0} = r_{1}$
6. By small law,
7. $u = \frac{\sin i}{\sin 30^{0}}$
8. $\Rightarrow \sqrt{2} = \frac{\sin i}{\frac{1}{2}}$
9. $\Rightarrow i = 45^{0}$

**Solved independently** (answer withheld)

1. The ray retraces its path only if it strikes the silvered face along the normal, so the angle of incidence on that face is $r_2 = 0^\circ$.
2. For a prism $r_1 + r_2 = A$, so $r_1 = A - 0^\circ = 30^\circ$.
3. Snell's law at the first face: $\sin i = \mu \sin r_1 = \sqrt{2} \times \sin 30^\circ = \frac{\sqrt{2}}{2} = \frac{1}{\sqrt{2}}$.
4. $i = \sin^{-1}\left(\frac{1}{\sqrt{2}}\right) = 45^\circ$, which is option $4$.

**Subtopic:** Prism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 1)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q004_97b7328e_03112026.png?v=97b7328e689e)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q004_9faa4b53_03112026.png?v=9faa4b53afa4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ray retraces its path only if it strikes the silvered face along the normal, which fixes the angle of refraction inside the prism at the prism angle, and Snell's law at the entry face then gives the angle of incidence
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The internal geometry is done correctly and gives $r = A = 30^{\circ}$, and that intermediate angle is handed in as the angle of incidence without passing it through $\sin i = n \sin r$
- **Why:** This question requires the retrace condition turned into an internal angle and then Snell's law applied at the entry face, demonstrated by the stem supplying both a refractive index '$\sqrt2$' and a prism angle '$30^{0}$' and asking for the angle of incidence.
<!--/ecat-->

## Q5

Physics · Semiconductor Electronics

In the circuit shown in the figure, the input voltage $V_i$ is $20\,\mathrm{V}$, $V_{BE}=0$ and $V_{CE}=0$. The values of $I_B$, $I_c$ and $\beta$ are given by

![printed figure: Common-emitter n-p-n transistor: Vi through RB = 500 kOhm to base, collector through RC = 4 kOhm to 20 V, emitter to ground](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q005_a4bcdf16_03112026.png?v=a4bcdf1620ff)

*Common-emitter n-p-n transistor: Vi through RB = 500 kOhm to base, collector through RC = 4 kOhm to 20 V, emitter to ground*

- **(1)** $I_B = 40\,\mu\mathrm{A},\ I_C = 5\,\mathrm{mA},\ \beta = 125$
- (2) $I_B = 40\,\mu\mathrm{A},\ I_C = 10\,\mathrm{mA},\ \beta = 250$
- (3) $I_B = 20\,\mu\mathrm{A},\ I_C = 5\,\mathrm{mA},\ \beta = 250$
- (4) $I_B = 25\,\mu\mathrm{A},\ I_C = 5\,\mathrm{mA},\ \beta = 200$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $V_{BE} = 0$
2. $V_{CE} = 0$
3. $V_b = 0$
4. $I_C = \frac{(20 - 0)}{4 \times 10^{3}}$
5. $I_C = 5 \times 10^{-3} = 5\,\mathrm{mA}$
6. $V_i = V_{BE} + I_R R_B$
7. $20 = I_B \times 500 \times 10^{3}$
8. $I_B \frac{20}{500 \times 10^{3}} = 40\,\mu\mathrm{A}$
9. $\beta = \frac{I_C}{I_b} = \frac{25 \times 10^{-3}}{40 \times 10^{-6}} = 125$

**Solved independently** (answer withheld)

1. With $V_{BE}=0$, the whole input voltage drops across $R_B$: $I_B = \frac{V_i - V_{BE}}{R_B} = \frac{20\,\mathrm{V}}{500\times10^{3}\,\Omega}$.
2. $I_B = 40\times10^{-6}\,\mathrm{A} = 40\,\mu\mathrm{A}$.
3. With $V_{CE}=0$, the full $20\,\mathrm{V}$ supply drops across $R_C$: $I_C = \frac{20\,\mathrm{V}}{4\times10^{3}\,\Omega}$.
4. $I_C = 5\times10^{-3}\,\mathrm{A} = 5\,\mathrm{mA}$.
5. $\beta = \frac{I_C}{I_B} = \frac{5\times10^{-3}}{40\times10^{-6}} = 125$, which is option $1$.

**Subtopic:** Transistor as an Amplifier (Common Emitter Configuration): Voltage, Current and Power Gain · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 1)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q005_3afb47a9_03112026.png?v=3afb47a916a5)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q005_bcedbf26_03112026.png?v=bcedbf26aa76)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a common-emitter stage with $V_{BE}=0$ and $V_{CE}=0$ the whole input appears across $R_B$ and the whole supply across $R_C$, so $I_B=V_i/R_B$, $I_C=V_{CC}/R_C$ and $\beta=I_C/I_B$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  $I_B$ is found correctly as $40\,\mu\mathrm{A}$, but the collector resistor is given the input voltage as well as the supply, $40\,\mathrm{V}/4\,\mathrm{k\Omega} = 10\,\mathrm{mA}$, and $\beta$ then follows at 250
- **Why:** This question requires three quantities computed and reported together, demonstrated by the stem asking for 'The values of $I_B$, $I_c$ and $\beta$' and every option supplying all three.
- **Note:** E1's pattern returned statement_options on option length; the printed shape is a three-quantity answer judged whole, so qtype is recorded as two_part. The figure was supplied as a drawn spec carrying $R_B = 500\,\mathrm{k\Omega}$, $R_C = 4\,\mathrm{k\Omega}$ and the 20 V rail, so the circuit values needed for the trap are in the record.
<!--/ecat-->

## Q6

Physics · Semiconductor Electronics

In a p-n junction diode, change in temperature due to heating

- **(1)** affects the overall V – I Characteristics of p-n junction
- (2) affects only reverse resistance
- (3) does not affect resistance of p-n junction
- (4) affects only forward resistance

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Due to heating, number of electron-hole pairs will increase,  so overall resistance of diode will change.
2. Due to which forward biasing and reversed biasing both are charged.

**Solved independently** (answer withheld)

1. Heating increases thermal generation of electron-hole pairs, so the minority-carrier concentration $n_i^2 \propto T^3 e^{-E_g/kT}$ rises.
2. In reverse bias, the reverse saturation current $I_0$ rises with $T$, so the reverse resistance falls.
3. In forward bias, the barrier potential $V_0$ (knee voltage) falls with rising $T$, so the forward current at a given $V$ rises and the forward resistance falls.
4. Since both forward and reverse parts change, temperature affects the overall $V$-$I$ characteristics, which is option $1$.

**Subtopic:** VI Characteristics of PN Junction Diode · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q006_53441525_03112026.png?v=53441525c5f1)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q006_ca851792_03112026.png?v=ca851792819a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Heating a junction raises the number of thermally generated carriers and lowers the barrier potential, so both the forward and the reverse branch of the $V$-$I$ curve shift -- the whole characteristic moves, not one side of it
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Temperature is remembered through the one statement the chapter stresses -- that the reverse saturation current is strongly temperature dependent -- so the reverse branch is taken to be the only one affected
- **Why:** This question requires the effect of a stated change to be traced to both branches of the characteristic, demonstrated by the stem reading 'change in temperature due to heating' and the options rivalling each other over how much of the curve moves -- 'the overall V - I Characteristics' against 'only reverse resistance'.
- **Note:** E1's pattern returned statement_options; the stem is an unfinished sentence completed by each option rather than a block of claims to judge, so qtype is recorded as mcq.
<!--/ecat-->

## Q7

Physics · Semiconductor Electronics

In the combination of the following gates the output $Y$ can be written in terms of inputs $A$ and $B$ as

![printed figure: Inputs A and B through two NOT gates and two AND gates into an OR gate giving output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q007_67982957_03112026.png?v=679829579607)

*Inputs A and B through two NOT gates and two AND gates into an OR gate giving output Y*

- (1) $\overline{A+B}$
- (2) $\overline{A.B}$
- (3) $\overline{A.B}+A.B$
- **(4)** $A.\overline{B}+\overline{A}.B$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Two NOT gates, two AND gates and an OR gate giving Y = A·B̄ + Ā·B](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q007_sol_1_59a93243_03112026.png?v=59a93243d1ff)

*Two NOT gates, two AND gates and an OR gate giving Y = A·B̄ + Ā·B*

1. $Y = \left(A.\overline{B} + \overline{A}.B\right)$

**Solved independently** (answer withheld)

1. Tracing the figure: input $A$ goes directly to the upper AND gate and also, through a branch that hops over the $B$ line, into the lower NOT gate, giving $\overline{A}$ at the lower AND gate.
2. Input $B$ goes through the upper NOT gate, giving $\overline{B}$ at the upper AND gate, and also branches directly to the lower AND gate.
3. Upper AND output: $A\cdot\overline{B}$.
4. Lower AND output: $\overline{A}\cdot B$.
5. The OR gate combines them: $Y = A\cdot\overline{B} + \overline{A}\cdot B$, which is option $4$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q007_275e47a4_03112026.png?v=275e47a4d877)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q007_e7ccf1b2_03112026.png?v=e7ccf1b22771)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Reading a gate network into Boolean form: each AND gate here takes one plain input and one inverted input, so the OR of the two products is $A\bar B + \bar A B$, the exclusive-OR
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The inversion is taken on the output of an AND gate rather than on its input, so one branch is written as $\overline{A.B}$ instead of $\bar A.B$ while the other stays $A.B$
- **Why:** This question requires the drawn gate network to be translated into a Boolean expression, demonstrated by the stem reading 'In the combination of the following gates the output $Y$ can be written in terms of inputs $A$ and $B$ as' with the combination supplied only in the figure.
- **Note:** The figure was supplied as a drawn spec: $A$ goes straight to the lower AND and through an inverter to the upper AND, $B$ goes straight to the upper AND and through an inverter to the lower AND, and the two AND outputs feed an OR, which is the XOR of option 4. Option 3 as stored reads $\overline{A.B}+A.B$, which simplifies to 1; the trap route above is written against the stored text, and a reviewer with the booklet should check whether the printed option is $\bar A \bar B + A B$ (the XNOR) with an overline that lost its split, since the same wrong-stage inversion reaches either form.
<!--/ecat-->

## Q8

Physics · Thermal Properties of Matter

The power radiated by a black body is $P$ and it radiates maximum energy at wavelength, $\lambda_0$ If the temperature of the black body is now changes so that it radiates maximum energy at wavelength $\frac{3}{4}\lambda_0$, the power radiated by it becomes $nP$. The value of $n$ is

- (1) $\frac{81}{256}$
- (2) $\frac{3}{4}$
- **(3)** $\frac{256}{81}$
- (4) $\frac{4}{3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. We know, $\lambda_{\max}\,T = \text{constant}$ (wien's law)
2. So, $\lambda_{\max 1}T_1 = \lambda_{\max 2}T_2$
3. $\Rightarrow \lambda_0 T = \frac{3\lambda_0}{4}T'$
4. $\Rightarrow T' = \frac{4}{3}T$
5. So, $\frac{P_2}{P_1} = \left(\frac{T'}{T}\right)^{4} = \left(\frac{4}{3}\right)^{4} = \frac{256}{81}$

**Solved independently** (answer withheld)

1. By Wien's displacement law, $\lambda_m T = \text{constant}$, so $\lambda_0 T = \frac{3}{4}\lambda_0 T'$.
2. Hence $T' = \frac{4}{3}T$.
3. By Stefan's law, $P \propto T^4$, so $\frac{nP}{P} = \left(\frac{T'}{T}\right)^4$.
4. $n = \left(\frac{4}{3}\right)^4 = \frac{256}{81}$, which is option $3$.

**Subtopic:** Radiation Laws · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q008_4e01c7f6_03112026.png?v=4e01c7f63ec6)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q008_79adf288_03112026.png?v=79adf2884800)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Wien's law makes the peak wavelength inversely proportional to temperature, and Stefan's law makes the radiated power go as the fourth power of that temperature, so a wavelength cut to $3/4$ raises the power by $(4/3)^4$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Wien's law is used as a direct proportion, so the temperature ratio is taken as $3/4$ rather than $4/3$, and the fourth power of that is the reciprocal of the right answer, $81/256$
- **Why:** This question requires two proportionalities chained to give a factor, demonstrated by the stem defining the new power as '$nP$' and asking only for 'The value of $n$'.
<!--/ecat-->

## Q9

Physics · Mechanical Properties of Solids

Two wires are made of the same material and have the same volume. The first wire has cross sectional area $A$ and the second wire has cross sectional area $3A$. If the length of the first wire is increased by $\Delta l$ on applying a force $F$, how much force is needed to stretch the second wire by the same amount?

- (1) $F$
- **(2)** $9F$
- (3) $4F$
- (4) $6F$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Accd to ques
2. $Y = \frac{F \times L}{A\Delta L}$
3. Since vol. of both wired is same So,
4. $A \times L = 3A \times L'$
5. $= L^{1} = \frac{\Delta}{3}$,
6. $Y = \frac{F \times L}{A\Delta L} = \frac{F^{1} \times \frac{L}{3}}{3A \times \Delta L}$
7. $F^{I} = 9F$

**Solved independently** (answer withheld)

1. Same volume: $A\,l_1 = 3A\,l_2$, so $l_2 = \frac{l_1}{3}$.
2. Extension of a wire: $\Delta l = \frac{F\,l}{A\,Y}$, with the same $Y$ for both wires.
3. First wire: $\Delta l = \frac{F\,l_1}{A\,Y}$.
4. Second wire: $\Delta l = \frac{F_2\,(l_1/3)}{3A\,Y} = \frac{F_2\,l_1}{9A\,Y}$.
5. Equating the extensions: $\frac{F_2\,l_1}{9A\,Y} = \frac{F\,l_1}{A\,Y} \Rightarrow F_2 = 9F$, which is option $2$.

**Subtopic:** Hooke's Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q009_fd4669f1_03112026.png?v=fd4669f11db5)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q009_92dfcb00_03112026.png?v=92dfcb005b41)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For the same extension, the force goes as $F = YA\,\Delta l/L$, so tripling the area at fixed volume also shortens the wire to a third of its length and the force rises by $3\times3 = 9$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The two wires are read as interchangeable because they are the same material and the same volume, so Young's modulus is treated as settling the force by itself and the $A/L$ factor is dropped
- **Why:** This question requires the force for a fixed extension to be scaled by both the area and the length, demonstrated by the stem fixing 'the same volume' and then tripling the cross-section to '$3A$'.
- **Note:** The one-slip option that the area-only reasoning produces, $3F$, is not among the four printed options; the printed distractors other than $F$ sit off the 1/3/9 ladder.
<!--/ecat-->

## Q10

Physics · Thermodynamics

A sample of $0.1\,\mathrm{g}$ of water at $100^{0}\,\mathrm{C}$ and normal pressure $\left(1.013\times10^{5}\,\mathrm{Nm^{-2}}\right)$requires $54\,\mathrm{cal}$ of heat energy to convert to steam at $100^{0}\,\mathrm{C}$. if the volume of the steam produced is $167.1\,\mathrm{cc}$, the change in internal energy of the sample, is

- (1) $84.5\,\mathrm{J}$
- (2) $104.3\,\mathrm{J}$
- (3) $42.2\,\mathrm{J}$
- **(4)** $208.7\,\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\Delta u = \Delta q - \Delta w$
2. $\Delta q = 54 \times 4.2$
3. $= 226.8\,\mathrm{J}$
4. $\Delta w = p\Delta v$
5. $v_{i} = \frac{0.1}{1} = 0.1\,\mathrm{cc}$
6. $\Rightarrow \Delta v = 167\,\mathrm{cc}$
7. $= 167 \times$ [unreadable notation] $\mathrm{m^{3}}$
8. $\Delta w = 16.91\,\mathrm{J}$
9. C $\because \Delta w = P\Delta w$
10. $\Rightarrow \Delta u = 226.8 - 16.91$
11. $= 208.7\,\mathrm{j}$

**Solved independently** (answer withheld)

1. Heat supplied: $Q = 54\,\mathrm{cal} \times 4.18\,\mathrm{J\,cal^{-1}} \approx 225.7\,\mathrm{J}$.
2. Volume of $0.1\,\mathrm{g}$ liquid water $\approx 0.1\,\mathrm{cc}$, so $\Delta V = 167.1 - 0.1 = 167.0\,\mathrm{cc} = 1.670\times10^{-4}\,\mathrm{m^3}$.
3. Work done by the sample at constant pressure: $W = P\Delta V = 1.013\times10^{5} \times 1.670\times10^{-4} \approx 16.9\,\mathrm{J}$.
4. First law: $\Delta U = Q - W = 225.7 - 16.9 \approx 208.8\,\mathrm{J}$.
5. This matches $208.7\,\mathrm{J}$, which is option $4$.

**Subtopic:** Heat, Internal Energy, and Work · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q010_065be71b_03112026.png?v=065be71bd85c)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q010_404ed1df_03112026.png?v=404ed1df311b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** First law book-keeping at a phase change: the heat supplied goes partly into the work $P\Delta V$ done as the water expands into steam and the rest into internal energy, so $\Delta U = Q - P\Delta V$ with the calories converted to joules
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The printed numbers give $Q = 54\,\mathrm{cal} = 225.7\,\mathrm{J}$, $W = 1.013\times10^{5}\times167\times10^{-6} = 16.9\,\mathrm{J}$ and $\Delta U = 208.8\,\mathrm{J}$. I then ran the named slips available on this question and recorded what each yields: adding the work instead of subtracting it gives 242.6 J; leaving the calories unconverted gives 37.1 J; dropping the work term altogether gives 225.7 J; working wholly in calories gives 49.9 cal. None of those is printed, and the three wrong options stand at 0.50, 0.405 and 0.20 of the key with no operation on the stem's numbers reaching them.
- **Why:** This question requires the first law applied with a unit conversion, demonstrated by the stem giving the heat in calories, '54 cal', and the expansion as '167.1 cc' against a pressure in $\mathrm{Nm^{-2}}$ while the options are in joules.
- **Note:** no_trap here is a finding about the option set, not a gap: the three wrong values sit at one half, two fifths and one fifth of the key, and the slips available on this question -- sign of the work term, missing calorie conversion, work term omitted -- all land on values the paper does not print.
<!--/ecat-->

## Q11

Physics · Mechanical Properties of Fluids

A small sphere of radius ‘$r$’ falls from rest in a viscous liquid. AS a result is produced due to viscous force, The rate of production of heat when the sphere attains its terminal velocity, is proportional to

- (1) $r^{4}$
- (2) $r^{3}$
- **(3)** $r^{5}$
- (4) $r^{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Rate of prod of heat $= F \times u$
2. $= 6\pi n r v \times v$
3. $= 6\pi n r\left[\frac{2}{9}\frac{r^{2}g}{n}\left(p_{b} - p_{l}\right)\right]$
4. So, Rate of prod of heat $\times r^{5}$

**Solved independently** (answer withheld)

1. At terminal velocity the net force is zero, giving $v_t = \frac{2 r^{2} (\rho - \sigma) g}{9 \eta}$, so $v_t \propto r^{2}$.
2. The viscous force is $F = 6 \pi \eta r v_t$, so $F \propto r \cdot r^{2} = r^{3}$.
3. The rate of heat production equals the power against viscosity, $P = F v_t$.
4. $P \propto r^{3} \cdot r^{2} = r^{5}$, which is option $3$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q011_adad0460_03112026.png?v=adad046076d0)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q011_05e495c0_03112026.png?v=05e495c0bd9f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At terminal velocity the heat produced per second is the viscous force times the speed, and since Stokes' drag goes as $r$ while the terminal speed goes as $r^2$, the rate of heating goes as $r\cdot(r^2)^2 = r^5$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The viscous force $6\pi\eta r v$ is scaled correctly to $r\cdot r^2 = r^3$ and handed in, with the second factor of the speed -- the one that turns a force into a rate of working -- never multiplied in
- **Why:** This question requires two power laws combined into one proportionality, demonstrated by the stem asking what the rate of heat production 'is proportional to' with the four options being bare powers of $r$.
- **Note:** The stem as stored reads 'AS a result is produced due to viscous force', which has lost a word (heat); the quantity asked for is still named in the next clause, so the proportionality can be settled from the record.
<!--/ecat-->

## Q12

Physics · Modern Physics

when the light of frequency $2v_0$ (where $v_0$ is threshold frequency), if incident on a metal plate, the maximum velocity of electrons emitted is $v_1$. When the frequency of the incident radiation of increased to $5v_0$, the maximum velocity of electrons emitted from the same plate is $v_2$: The ratio of $v_1$ to $v_2$ is

- (1) $2 : 1$
- **(2)** $1 : 2$
- (3) $4 : 1$
- (4) $1 : 4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Accd to Ensein’s Eq,
2. $h \times 2v_0 = w_0 + \frac{1}{2}nv_1^{2}$ .....(1)
3. & $h \times 5v_0 = w_0 + \frac{1}{2}nv_1^{2}$ .....(2)
4. Since $w_0 = hv_0$
5. From (1), $hv_0 = \frac{1}{2}mv_1^{2}$
6. & From (2) $h \times 4v_0 = \frac{1}{2}mv_2^{2}$
7. $\Rightarrow 4 = \frac{v_2^{2}}{v_1^{2}}$
8. $\Rightarrow \frac{v_2}{v_1} = 2$

**Solved independently** (answer withheld)

1. Einstein's photoelectric equation: $\frac{1}{2}mv_{max}^2 = h\nu - h\nu_0$.
2. For $\nu = 2\nu_0$: $\frac{1}{2}mv_1^2 = h(2\nu_0 - \nu_0) = h\nu_0$.
3. For $\nu = 5\nu_0$: $\frac{1}{2}mv_2^2 = h(5\nu_0 - \nu_0) = 4h\nu_0$.
4. Dividing: $\frac{v_1^2}{v_2^2} = \frac{h\nu_0}{4h\nu_0} = \frac{1}{4}$.
5. $\frac{v_1}{v_2} = \sqrt{\frac{1}{4}} = \frac{1}{2}$, so $v_1 : v_2 = 1 : 2$, which is option $2$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q012_ccb2701b_03112026.png?v=ccb2701beebf)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q012_a37b1542_03112026.png?v=a37b15423ec2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Einstein's photoelectric equation gives the maximum kinetic energy as $h(\nu-\nu_0)$, so the energies here stand as $1:4$ and the speeds, going as the square root of the energy, stand as $1:2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The two kinetic energies are found correctly as $h\nu_0$ and $4h\nu_0$ and that $1:4$ is handed in as the ratio of the speeds, with the square root in $v = \sqrt{2K/m}$ never taken
- **Why:** This question requires the speed ratio drawn from the energy ratio, demonstrated by the stem asking for 'The ratio of $v_1$ to $v_2$' after fixing the frequencies at '$2v_0$' and '$5v_0$' against the threshold.
<!--/ecat-->

## Q13

Physics · Modern Physics

For a radioactive material, halflife is $10\,\mathrm{minutes}$, IF initially there are $600$ number of nuclei, the time taken (in minutes) for the disintergration of $450$ nuclei is

- (1) $15$
- **(2)** $20$
- (3) $30$
- (4) $10$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. After $450$ nucles disintegrates
2. No of nucles remaining $= 600 - 450$
3. $= 150$
4. & $150 = \frac{600}{4}$
5. So, $N = No \times \left(\frac{1}{2}\right)^{1}$
6. $\Rightarrow 150 = 600 \times \left(\frac{1}{2}\right)^{1}$
7. $\Rightarrow$ No of half lives $= 2$
8. So five taken $= 2 \times 10$
9. $= 20\,\mathrm{min}$

**Solved independently** (answer withheld)

1. Nuclei remaining after $450$ disintegrate: $N = 600 - 450 = 150$.
2. $\frac{N}{N_0} = \frac{150}{600} = \frac{1}{4} = \left(\frac{1}{2}\right)^{2}$, so $n = 2$ half-lives have passed.
3. $t = n\,T_{1/2} = 2 \times 10\,\mathrm{min} = 20\,\mathrm{min}$, which is option $2$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q013_651d3ebb_03112026.png?v=651d3ebbb47c)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q013_bb8b77cc_03112026.png?v=bb8b77cca8d4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Radioactive decay halves what is LEFT in each half-life, so 600 going to 150 survivors is two halvings and the elapsed time is two half-lives, not three quarters of one scaled up
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The 450 of 600 is read as three quarters of the sample, and three quarters is taken to need one and a half times the half-life: $1.5\times10 = 15$ minutes
- **Why:** This question requires the number of half-lives to be counted from the SURVIVORS, demonstrated by the stem giving 600 initial nuclei and asking for the time 'for the disintergration of 450 nuclei' rather than for the time to a stated remainder.
<!--/ecat-->

## Q14

Physics · Modern Physics

An electron of mass $m$ with an initial velocity $\vec{V} = V_0\hat{i}\ (V_0 > 0)$ enters an electric field $\vec{E} = -E_0\hat{i}\ (E_0 = \mathrm{constant} > 0)$ at $t = 0$. If $\lambda_0$ is its de-Broglie wavelength initially then its de-Broglie wavelength at time $t$ is

- (1) $\lambda_0$
- **(2)** $\frac{\lambda_0}{\left(1 + \frac{eE_0}{mV_0}t\right)}$
- (3) $\lambda_0 t$
- (4) $\lambda_0\left(1 + \frac{eE_0}{mV_0}t\right)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Arrow labelled v0 î and, below it, a longer arrow labelled E = −E0 î, both pointing right](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q014_sol_1_2f9f7fc3_03112026.svg?v=2f9f7fc321da)

*Arrow labelled v0 î and, below it, a longer arrow labelled E = −E0 î, both pointing right*

1. So, electron being a negative charge So, force exp, by it along the direction of its velocity so electron after ‘t’ sec is,
2. $V^{1} = V_{o} + \left(\frac{Ee}{m}\right)t$
3. So, $\lambda_{o} = \frac{h}{mv_{0}}$
4. $\lambda_{o} = \frac{h}{m\left(v_{1} + \frac{eE}{m}t\right)} = \frac{h}{mv_{o} + (eft)}$
5. $\Rightarrow \lambda^{1} = \frac{h / mvo}{1 + \frac{eET}{mv_{0}}} = \frac{v_{0}}{1 + \frac{eEt}{mv_{0}}}$

**Solved independently** (answer withheld)

1. Force on the electron: $\vec{F} = (-e)\vec{E} = (-e)(-E_0\hat{i}) = eE_0\hat{i}$, along the initial velocity.
2. Acceleration: $\vec{a} = \frac{eE_0}{m}\hat{i}$.
3. Velocity at time $t$: $v(t) = V_0 + \frac{eE_0}{m}t = V_0\left(1 + \frac{eE_0}{mV_0}t\right)$.
4. Initial wavelength: $\lambda_0 = \frac{h}{mV_0}$.
5. At time $t$: $\lambda = \frac{h}{m v(t)} = \frac{h}{mV_0\left(1 + \frac{eE_0}{mV_0}t\right)} = \frac{\lambda_0}{1 + \frac{eE_0}{mV_0}t}$, which is option $2$.

**Subtopic:** de Broglie Wavelength of an Accelerated Charged Particle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q014_7c3011f3_03112026.png?v=7c3011f35990)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q014_ceec47ad_03112026.png?v=ceec47ad7fa4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The field drives the electron forward, so its momentum grows as $mv_0 + eE_0t$ and the de Broglie wavelength, being inversely proportional to momentum, shrinks by that same factor
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The momentum is built correctly as $mv_0(1 + eE_0t/mv_0)$ and that factor is then multiplied into $\lambda_0$ instead of dividing it, which is $\lambda \propto p$ in place of $\lambda = h/p$
- **Why:** This question requires the momentum at time $t$ built from the field and then inverted through $\lambda = h/p$, demonstrated by the options being $\lambda_0$ multiplied and divided by the same bracket $\left(1+\frac{eE_0}{mV_0}t\right)$.
<!--/ecat-->

## Q15

Physics · Modern Physics

The ratio of kinetic energy to the total energy of an electron in a Bohr orbit of the hydrogen atom is:

- (1) $1 : -2$
- (2) $1 : 1$
- (3) $2 : -1$
- **(4)** $1 : -1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Since, Total energy $= -$ (Kinetic energy)
2. So, $\frac{\text{k.e}}{\text{t.e}}\ 1 : -1$

**Solved independently** (answer withheld)

1. In a Bohr orbit the centripetal force is the Coulomb force: $\frac{mv^2}{r} = \frac{kZe^2}{r^2}$.
2. So the kinetic energy is $K = \frac{1}{2}mv^2 = \frac{kZe^2}{2r}$.
3. The potential energy is $U = -\frac{kZe^2}{r} = -2K$.
4. The total energy is $E = K + U = K - 2K = -K$.
5. Hence $K : E = K : (-K) = 1 : -1$, which is option $4$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q015_e38e7f06_03112026.png?v=e38e7f06c853)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q015_8832a848_03112026.png?v=8832a8480dbb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** In a Bohr orbit the potential energy is twice the kinetic energy and negative, so the total energy is exactly minus the kinetic energy and the ratio asked for is $1:-1$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $1:-2$ is the kinetic-to-POTENTIAL ratio, the relation the chapter states for a Bohr orbit, offered where the stem asked for kinetic against TOTAL
- **Why:** This question requires one of the Bohr energy relations to be selected and used as a ratio, demonstrated by the stem naming 'kinetic energy to the total energy' while the options print both the $1:-2$ and the $1:-1$ pairings.
<!--/ecat-->

## Q16

Physics · Waves

A tuning fork is used to produced resonance in glass tube. The length of the air column in the tube can be adjusted by a variable piston. A room temperature of $27^{0}\,\mathrm{C}$ two successive resonances are produced at $20\,\mathrm{cm}$ and $73\,\mathrm{cm}$ column length. If the frequency of the tuning for is $320\,\mathrm{Hz}$, The velocity of sound in air at $27^{0}\,\mathrm{C}$ is

- (1) $300\,\mathrm{m/s}$
- (2) $330\,\mathrm{m/s}$
- (3) $350\,\mathrm{m/s}$
- (4) $339\,\mathrm{m/s}$

**Answer** — booklet: (none) · independent solve: (4) · unchecked

**Publisher's solution**

1. This is a closed pipe
2. Atv, $320 = \frac{v}{4\{20 + e} = \frac{3v}{4[73 + e]}$
3. $E$ = end correction
4. $\Rightarrow 73 + e = 60 + 3e$
5. $\Rightarrow e = \frac{13}{2}\,\mathrm{cm} = 6.5\,\mathrm{cm}$
6. So, $320 = = \frac{v}{4 \times \left(\frac{26.5}{100}\right)}$
7. $\Rightarrow v = 320 \times 4 \times \frac{26.5}{100} = 339\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. For a resonance tube, two successive resonance lengths differ by half a wavelength: $l_2 - l_1 = \frac{\lambda}{2}$.
2. $\frac{\lambda}{2} = 73\,\mathrm{cm} - 20\,\mathrm{cm} = 53\,\mathrm{cm}$.
3. $\lambda = 2 \times 53\,\mathrm{cm} = 106\,\mathrm{cm} = 1.06\,\mathrm{m}$.
4. $v = f\lambda = 320\,\mathrm{Hz} \times 1.06\,\mathrm{m} = 339.2\,\mathrm{m/s}$.
5. $339.2\,\mathrm{m/s} \approx 339\,\mathrm{m/s}$, which is option $4$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q016_f6fb5f11_03112026.png?v=f6fb5f11dfa3)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q016_d9f72887_03112026.png?v=d9f7288784b8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Successive resonances in a tube differ by half a wavelength, so the gap between the two column lengths gives $\lambda/2$ and the speed follows from $v = f\lambda$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No key is stored for this question: `correct_answer` is null, `accepted_answers` is empty and `answer_line_as_printed` is null, so there is no printed verdict to tag against and no option can be called wrong.
- **Why:** This question requires the wavelength read from the separation of two resonances and then multiplied by the frequency, demonstrated by the stem giving 'two successive resonances' at '20 cm and 73 cm' and a fork frequency of '320 Hz'.
- **Note:** Key absent from our record; the paper is not at fault. A reviewer holding the printed key should check $\lambda = 2(73-20)\,\mathrm{cm} = 1.06\,\mathrm{m}$ and $v = 320 \times 1.06 = 339\,\mathrm{m/s}$ against option 4, and then test option 2 (330 m/s) as the remembered textbook speed of sound offered in place of the computed one, which is the mechanism this option set looks built around.
<!--/ecat-->

## Q17

Physics · Capacitance

The electrostatic force between the metal plate of an isolated parallel capacitor $C$ having charge $Q$ and area $A$ is

- (1) inversely proportional to the distance between the plates
- **(2)** independent of the distance between the plates
- (3) proportional to the square root of the distance between the plates
- (4) linearly proportional to the distance between the plates.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $F = \frac{\sigma^{2}}{2e_{0}}A$
2. So it is independent of distance bet bertes

**Solved independently** (answer withheld)

1. The capacitor is isolated, so its charge $Q$ stays constant whatever the plate separation $d$.
2. The field due to one plate alone is $E' = \frac{\sigma}{2\varepsilon_0} = \frac{Q}{2\varepsilon_0 A}$.
3. The force on the other plate is $F = QE' = \frac{Q^2}{2\varepsilon_0 A}$.
4. $F$ contains no $d$, so the force is independent of the distance between the plates, which is option $2$.

**Subtopic:** The Parallel Plate Capacitor · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q017_891de57c_03112026.png?v=891de57cc2f6)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q017_653f0465_03112026.png?v=653f046578e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** On an ISOLATED capacitor the charge is fixed, so the field between the plates, $\sigma/\varepsilon_0 = Q/\varepsilon_0 A$, does not depend on the separation and neither does the force $Q^2/2\varepsilon_0 A$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The plate force is written as $QV/d$ with the voltage treated as fixed, which is the behaviour of a capacitor still across a battery, and that falls off as $1/d$
- **Why:** This question requires the fixed-charge condition applied to the plate force, demonstrated by the stem specifying 'an isolated parallel capacitor $C$ having charge $Q$ and area $A$' and every option describing a different dependence on the plate separation.
- **Note:** E1's pattern returned statement_options because each option is a phrase; the stem is a sentence completed by the options, with no lettered block, so qtype is recorded as mcq.
<!--/ecat-->

## Q18

Physics · Oscillations

A pendulum is hung from the roof of a sufficiently high building and is moving freely to an fro like a simple harmonic oscillator, The acceleration of the bob of the pendulum is $20\,\mathrm{m/s^2}$ at a distance of $5\,\mathrm{m}$ from the mean position. The time period of oscillation if

- (1) $1\,\mathrm{s}$
- (2) $2\pi\,\mathrm{s}$
- (3) $2\,\mathrm{s}$
- **(4)** $\pi\,\mathrm{s}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For SHM,
2. $Q = +W^{2}Y$
3. $\Rightarrow 20 = W^{2} \times 5$
4. $\Rightarrow w = 2 = \frac{2T_{1}}{T}$
5. $\Rightarrow T = T_{1}$

**Solved independently** (answer withheld)

1. In SHM the magnitude of acceleration is $|a| = \omega^2 x$.
2. $\omega^2 = \frac{a}{x} = \frac{20\,\mathrm{m/s^2}}{5\,\mathrm{m}} = 4\,\mathrm{s^{-2}}$.
3. $\omega = 2\,\mathrm{rad/s}$.
4. $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi\,\mathrm{s}$, which is option $4$.

**Subtopic:** Acceleration in SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q018_1c02f238_03112026.png?v=1c02f238ddc0)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q018_51d8477b_03112026.png?v=51d8477be31f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In simple harmonic motion the acceleration is $\omega^2$ times the displacement, so $\omega$ comes from $a/x$ and the period is $2\pi/\omega$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $\omega^2 = 20/5 = 4$ gives $\omega = 2$, and that 2 is handed in as the period in seconds without being carried through $T = 2\pi/\omega$
- **Why:** This question requires the angular frequency extracted from an acceleration-displacement pair and converted to a period, demonstrated by the stem giving '$20\,\mathrm{m/s^2}$ at a distance of $5\,\mathrm{m}$ from the mean position' and asking for the time period.
<!--/ecat-->

## Q19

Physics · Electrostatics

An electron falls from rest through a vertical distance $h$ in a uniform and vertically upward directed electric field $E$. The direction of electric field is not reversed, keeping its magnitude the same. A proton is allowed to fall from rest in its through the same vertical distance $h$. the time of fall of the electron, in comparison to the time of fall of the proton of

- (1) equal
- **(2)** smaller
- (3) 10 times greater
- (4) 5 times greater

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Time of fall $= t = \sqrt{\frac{2h}{a}}$
2. Where $a = \frac{eE}{m}$
3. $\Rightarrow t = \sqrt{\frac{2h}{eE} \times n}$
4. $\Rightarrow \frac{te}{tp} = \sqrt{\frac{Me}{Mp}} \simeq \frac{1}{42}$
5. $\Rightarrow te < tp$

**Solved independently** (answer withheld)

1. The electron has charge $-e$, so an upward field $E$ pushes it downward with force $F = eE$; gravity is negligible beside this force.
2. Electron acceleration: $a_e = \frac{eE}{m_e}$.
3. With the field reversed (downward), the proton of charge $+e$ is also pushed downward: $a_p = \frac{eE}{m_p}$.
4. Falling from rest, $h = \frac{1}{2} a t^2$, so $t = \sqrt{\frac{2h}{a}} = \sqrt{\frac{2hm}{eE}}$, i.e. $t \propto \sqrt{m}$.
5. $\frac{t_e}{t_p} = \sqrt{\frac{m_e}{m_p}} \ll 1$, so the electron's time of fall is smaller, which is option $2$.

**Subtopic:** Motion of Charged Particle in Uniform Electric Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q019_65dc6e98_03112026.png?v=65dc6e98421c)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q019_baa62efc_03112026.png?v=baa62efc911f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** With a vertical field present the two particles do not fall under gravity alone: the electric force per unit mass is enormous for the electron and tiny for the proton, so the electron's fall time is the shorter one
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The field is dropped out of the problem and the two particles are treated as freely falling bodies, for which the time over a height $h$ is the same whatever the mass
- **Why:** This question requires two fall times to be compared when a field acts as well as gravity, demonstrated by the stem holding the field's direction and magnitude fixed while asking for 'the time of fall of the electron, in comparison to the time of fall of the proton'.
- **Note:** `negative_words_seen` records the NOT in 'The direction of electric field is not reversed', which belongs to the setup rather than to the task, so the task polarity here is direct.
<!--/ecat-->

## Q20

Physics · Gravitation

The kinetic energies of a planet in an elliptical orbit about the sun, at positions A, B and C are $K_A$, $K_B$ and $K_C$, respectively. AC is the major axis and SB is perpendicular to AC at the position of the sun S as shown in the figure, then

![printed figure: Elliptical orbit with major axis AC, sun S on AC and SB perpendicular to AC](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q020_6312a7f2_03112026.png?v=6312a7f2e21f)

*Elliptical orbit with major axis AC, sun S on AC and SB perpendicular to AC*

- (1) $K_B > K_A > K_O$
- (2) $K_A < K_B < K_C$
- (3) $K_B < K_A < K_C$
- **(4)** $K_A > K_B > K_C$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. When planet revolves around star,
2. $Mvr =$ constent
3. So, $v \times \frac{1}{r}$
4. Since $r_{c}$ is max of $V_{c}$ is Min
5. So, $V_{A}$ is Max
6. So, $K_{A} > K_{B} > K_{C}$

**Solved independently** (answer withheld)

1. From the figure, the sun $S$ lies on the major axis close to $A$, so $A$ is the perihelion and $C$ the aphelion: $r_A < r_B < r_C$ where $r_B = SB$ is the semi-latus rectum.
2. Energy conservation (vis-viva): $v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$, so speed decreases as distance $r$ from the sun increases.
3. Hence $v_A > v_B > v_C$, and with $K = \frac{1}{2}mv^2$, $K_A > K_B > K_C$, which is option $4$.

**Subtopic:** Kepler's Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q020_741235f9_03112026.png?v=741235f9fda5)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q020_248b4595_03112026.png?v=248b4595e02f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Angular momentum is conserved along the orbit, so the planet is fastest where it is nearest the Sun: with S lying between the centre and A, the distances run SA < SB < SC and the kinetic energies run the other way
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Kinetic energy is taken to grow with distance from the Sun, which produces the exact reverse of the right order, $K_A < K_B < K_C$
- **Why:** This question requires three kinetic energies arranged by distance from the focus, demonstrated by the stem fixing that 'AC is the major axis and SB is perpendicular to AC at the position of the sun S' and every option printing a full ordering.
- **Note:** The figure was supplied as a drawn spec and places S between the ellipse centre and A, which is what settles SA < SB. Option 1 as stored reads '$K_B > K_A > K_O$'; the subscript O has no point in the figure behind it and is almost certainly a C, so the route above is written for the reading $K_B > K_A > K_C$.
<!--/ecat-->

## Q21

Physics · Rotational Motion

A solid sphere is in rolling motion. In rolling motion a body possesses translational kinetic energy ($K_t$) as well as rotational kinetic energy ($K_r$)simultaneously. The ratio $K_t : (K_t + K_r)$ for the sphere is

- (1) $2 : 5$
- (2) $7 : 10$
- (3) $10 : 7$
- **(4)** $5 : 7$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For body rolling,
2. $K_{\text{total}} = \frac{1}{2}mv^{2} + \frac{1}{2}Iw^{2}$
3. $= \frac{1}{2}mv^{2} + \frac{1}{2} \times \frac{2}{5}MR^{2} \times \frac{V^{2}}{R^{2}}$
4. $k_{\text{total}} = \frac{7}{10}mv^{2}$
5. So, $\frac{k_{t}}{k_{\text{total}}} = \frac{\frac{1}{2}mv^{2}}{\frac{7}{10}mv^{2}} = \frac{5}{7}$

**Solved independently** (answer withheld)

1. For a solid sphere, $I = \frac{2}{5}MR^2$ and rolling without slipping gives $\omega = \frac{v}{R}$.
2. $K_t = \frac{1}{2}Mv^2$.
3. $K_r = \frac{1}{2}I\omega^2 = \frac{1}{2}\cdot\frac{2}{5}MR^2\cdot\frac{v^2}{R^2} = \frac{1}{5}Mv^2$.
4. $K_t + K_r = \frac{1}{2}Mv^2 + \frac{1}{5}Mv^2 = \frac{7}{10}Mv^2$.
5. $\frac{K_t}{K_t + K_r} = \frac{1/2}{7/10} = \frac{5}{7}$, so the ratio is $5 : 7$, which is option $4$.

**Subtopic:** Rolling Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q021_91f8b569_03112026.png?v=91f8b56943c8)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q021_7eba7b96_03112026.png?v=7eba7b96aa0b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** A rolling solid sphere carries $K_r = \tfrac25 K_t$, so of the total energy the translational share is $\tfrac12 \div \tfrac{7}{10} = \tfrac57$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $2:5$ is the rotational-to-translational ratio quoted for a solid sphere, a true figure about the same motion, offered where the stem asked for translational against the TOTAL
- **Why:** This question requires one energy share expressed against the total, demonstrated by the stem writing the ratio out as '$K_t : (K_t + K_r)$' while the options also print the bare $2:5$ split.
<!--/ecat-->

## Q22

Physics · Gravitation

> ⚠ The independent solve chose (1); the booklet prints (3).

If the mass of the sun were ten times smaller and the universal gravitational constant were ten times larger in magnitude, which of the following is not correct?

- (1) ‘$g$’ on the Earth will not change
- (2) raindrops will fall faster
- **(3)** Time periods of a simple pendulum on the Earth would decrease
- (4) Walking on the ground would become more difficult.

**Answer** — booklet: (3) · independent solve: (1) · differs

**Publisher's solution**

1. $g = \frac{GM}{R^{2}}$, $M$= Mass of earth
2. Of $G$ becomes $10$ times, $g$ becomes $10$ times
3. Time period of pendulum $T = 2\pi\sqrt{\frac{L}{g}}$
4. So $T$ decreases.

**Solved independently** (answer withheld)

1. Acceleration due to gravity on the Earth is $g = \frac{G M_e}{R_e^2}$, which involves $G$ and the Earth's mass, not the sun's mass.
2. With $G' = 10G$: $g' = \frac{(10G) M_e}{R_e^2} = 10g$, so $g$ on the Earth increases.
3. Hence the statement '$g$ on the Earth will not change' is not correct (option $1$).
4. Larger $g$ makes raindrops fall faster, so option $2$ is correct.
5. $T = 2\pi\sqrt{\frac{l}{g}}$ decreases as $g$ increases, so option $3$ is correct.
6. Weight $mg$ increases, so walking becomes more difficult; option $4$ is correct.
7. The only incorrect statement is option $1$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q022_91af6c31_03112026.png?v=91af6c310cb9)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q022_8412db52_03112026.png?v=8412db527688)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Surface gravity is $g = GM_E/R_E^2$, so it is set by the Earth's mass and by $G$ -- the Sun's mass does not enter it, and a tenfold larger $G$ makes $g$ ten times larger, which shortens a pendulum's period
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The key as stored marks option 3, but $g = GM_E/R_E^2$ with $G$ ten times larger makes $g$ ten times larger, so a pendulum's period DOES decrease and option 3 is a correct statement, while option 1 ('g on the Earth will not change') is the false one the NOT-polarity asks for. With the record's key and the physics pointing at different options, naming a trap would risk writing one against the paper's actual answer.
- **Why:** This question requires $g = GM_E/R_E^2$ and $T = 2\pi\sqrt{l/g}$ applied to a hypothetical change in two constants, demonstrated by the stem altering 'the mass of the sun' and 'the universal gravitational constant' and asking 'which of the following is not correct?'.
- **Note:** Key contested, and the tag follows the record rather than repairing it. Options 2 and 4 (raindrops faster, walking harder) are both consequences of a larger $g$ and so are correct statements; option 3 is also a consequence of a larger $g$; option 1 is the only statement the stated change falsifies, since the Sun's mass never entered $g$ but $G$ did. A reviewer should check the printed key and option order for this booklet. The mechanism to check on option 1 is the dropped condition: leave the tenfold $G$ out of the stem and 'g will not change' becomes true, because the Sun's mass alone has no bearing on terrestrial $g$.
<!--/ecat-->

## Q23

Physics · Rotational Motion

A solid sphere is rotating freely about its symmetry axis in free space, The radius of the sphere is increased keeping its mass same Which of the following physical quantities would remain constant for the sphere?

- (1) Angular momentum
- (2) Angular velocity
- (3) Rotational kinetic energy
- (4) Moment of inertia

**Answer** — booklet: (none) · independent solve: (1) · unchecked

**Publisher's solution**

1. Since radius is increasing while sphere is rotating freely so, Torque $= v$
2. Hence angular $= \frac{Monumentum}{Constent}$

**Solved independently** (answer withheld)

1. The sphere rotates freely in free space, so the external torque is zero: $\tau_{ext} = 0$.
2. Zero external torque means angular momentum is conserved: $L = I\omega = \text{constant}$.
3. $I = \frac{2}{5}MR^2$ increases when $R$ increases at fixed $M$, so moment of inertia is not constant.
4. $\omega = \frac{L}{I}$ decreases as $I$ increases, so angular velocity is not constant.
5. $K = \frac{L^2}{2I}$ decreases as $I$ increases, so rotational kinetic energy is not constant.
6. Only angular momentum stays constant, which is option $1$.

**Subtopic:** Conservation of Angular Momentum · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 6)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q023_e377a4b3_03112026.png?v=e377a4b3fd02)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q023_e37ff87f_03112026.png?v=e37ff87fa754)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A body spinning in free space has no external torque on it, so its angular momentum is what stays fixed when the radius changes, while the moment of inertia, the angular velocity and the rotational kinetic energy all shift
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No key is stored for this question: `correct_answer` is null, `accepted_answers` is empty and `answer_line_as_printed` is null, so there is no printed verdict to tag against and no option can be called wrong.
- **Why:** This question requires the no-external-torque condition applied to a changed geometry, demonstrated by the stem specifying a sphere 'rotating freely about its symmetry axis in free space' whose 'radius is increased keeping its mass same' and asking which quantity stays constant.
- **Note:** Key absent from our record; the paper is not at fault. A reviewer holding the key should check angular momentum (option 1) as the conserved quantity, and then test option 2 as the mechanism this set looks built around -- 'rotating freely' read as 'spinning at a fixed rate', so that angular velocity is taken to be what is preserved while $I = \tfrac25 MR^2$ grows.
<!--/ecat-->

## Q24

Physics · Magnetic Effect of Electric Current

A metallic rod of mass per unit length $0.5\,\mathrm{kg\,m^{-1}}$ is lying horizontally on a smooth inclined plane which makes an angle of $30^{0}$ with the horizontal. The rod is not allowed to slide down by flowing a current through it when a magnetic field of induction $0.25\,\mathrm{T}$ is acting on it in the vertical direction. The current flowing in the rod to keep it stationary is

- **(1)** $11.32\,\mathrm{A}$
- (2) $7.14\,\mathrm{A}$
- (3) $14. 76\,\mathrm{A}$
- (4) $5.98\,\mathrm{A}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For rod to remain at rest,
2. $Ing\sin 30^{0} = F\cos 30^{0}$
3. $\Rightarrow ng \times \frac{1}{2} = BIl \times \frac{\sqrt{3}}{2}$
4. $\Rightarrow I = \left(\frac{m}{l}\right) g \times \frac{1}{\sqrt{3}} \times \frac{1}{B}$
5. $= 0.5 \times 10 \times \frac{1}{\sqrt{3}} \times 4$
6. $I = 11.32\,\mathrm{A}$

**Solved independently** (answer withheld)

1. The rod is horizontal and $\vec{B}$ is vertical, so the magnetic force $F = BIl$ is horizontal (perpendicular to both).
2. On a smooth incline, equilibrium along the incline requires $BIl\cos 30^{\circ} = mg\sin 30^{\circ}$.
3. $I = \frac{(m/l)\,g\tan 30^{\circ}}{B}$.
4. $I = \frac{0.5 \times 9.8 \times 0.5774}{0.25} = \frac{2.829}{0.25} = 11.32\,\mathrm{A}$, which is option $1$.

**Subtopic:** Magnetic Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q024_dd94100a_03112026.png?v=dd94100a8313)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q024_b5fc9f60_03112026.png?v=b5fc9f600b73)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A horizontal rod on a frictionless incline in a vertical field feels a horizontal force $BIL$, so balancing along the slope needs $mg\sin\theta = BIL\cos\theta$ and the current works out as $(m/L)g\tan\theta/B$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The printed data give $I = \lambda g \tan\theta / B = 0.5 \times 9.8 \times 0.577/0.25 = 11.32\,\mathrm{A}$, which is the key. I then ran the slips this question offers and recorded each: $\sin\theta$ for $\tan\theta$ gives 9.80 A, $\cos\theta$ gives 16.97 A, $\cot\theta$ gives 33.95 A, dropping the trigonometric factor altogether gives 19.60 A, and using $g=10$ gives 11.55 A. None of those is 7.14, 14.76 or 5.98, so no named route reaches a printed wrong option.
- **Why:** This question requires the slope equilibrium of a current-carrying rod in a vertical field reduced to a current, demonstrated by the stem giving the mass per unit length '$0.5\,\mathrm{kg\,m^{-1}}$', the field '$0.25\,\mathrm{T}$ ... in the vertical direction' and the incline '$30^{0}$'.
- **Note:** `negative_words_seen` records the NOT in 'The rod is not allowed to slide down', which states the equilibrium condition rather than negating the task, so the task polarity is direct. no_trap here is a finding about the option set: the two standard slips on this problem, using $\sin\theta$ or $\cos\theta$ in place of $\tan\theta$, give 9.80 A and 16.97 A and neither is printed.
<!--/ecat-->

## Q25

Physics · Alternating Current

> ⚠ The independent solve chose (2); the booklet prints (1).

A inductor $20\,\mathrm{mH}$, a capacitor $100\,\mu\mathrm{F}$ and a resistor $50\,\Omega$ are connected in series across a source of emf$_{1}$ $V = 10 \sin 314\,t$. The power loss in the circuit is

- **(1)** $1.13\,\mathrm{W}$
- (2) $0.79\,\mathrm{W}$
- (3) $2.74\,\mathrm{W}$
- (4) $0.43\,\mathrm{W}$

**Answer** — booklet: (1) · independent solve: (2) · differs

**Publisher's solution**

1. Impedence of circuit
2. $Z = \sqrt{R^{2} + \left(wl - \frac{1}{cw}\right)^{2}}$
3. $w = 314$
4. So, $wL = 314 \times \frac{20}{1000} = 6.28\,\mathrm{OHM}$
5. $\frac{1}{cw} = \frac{1}{314 \times 100} \times 10^{6} = 31.84\,\mathrm{ohm}$
6. $\Rightarrow Z = \sqrt{(50)^{2} + (31.84 - 6.28)^{2}}$
7. $X = 56\,\mathrm{ohm}$
8. Power Loss=
9. $= V_{\mathrm{rms}} \times I_{\mathrm{rms}} \times \frac{R}{Z}$
10. $= \frac{10}{\sqrt{2}} \times \frac{10}{\sqrt{2} \times 56} \times \frac{50}{56}$
11. $= 1.13\,\mathrm{w}$

**Solved independently** (answer withheld)

1. From $V = 10\sin 314t$: $V_0 = 10\,\mathrm{V}$ and $\omega = 314\,\mathrm{rad\,s^{-1}}$.
2. $X_L = \omega L = 314 \times 20\times10^{-3} = 6.28\,\Omega$.
3. $X_C = \frac{1}{\omega C} = \frac{1}{314 \times 100\times10^{-6}} = 31.85\,\Omega$.
4. $X_C - X_L = 31.85 - 6.28 = 25.57\,\Omega$.
5. $Z^2 = R^2 + (X_C - X_L)^2 = 2500 + 653.8 = 3153.8\,\Omega^2$, so $Z \approx 56.16\,\Omega$.
6. $V_{rms} = \frac{10}{\sqrt{2}} = 7.07\,\mathrm{V}$, so $I_{rms} = \frac{7.07}{56.16} = 0.126\,\mathrm{A}$.
7. Power loss $P = I_{rms}^2 R = (0.126)^2 \times 50 \approx 0.79\,\mathrm{W}$, which is option $2$.

**Subtopic:** Power in an AC Circuit · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q025_f105dee6_03112026.png?v=f105dee61210)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q025_5ee7b099_03112026.png?v=5ee7b099bf8d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Power in a series LCR circuit is dissipated in the resistor alone, $P = V_{rms}^2 R/Z^2$, with $Z$ built from $R$ and the difference of the two reactances at the source's own angular frequency
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Working from the printed values, $X_L = 314 \times 0.02 = 6.28\,\Omega$, $X_C = 1/(314 \times 10^{-4}) = 31.85\,\Omega$, $Z = \sqrt{50^2 + 25.57^2} = 56.2\,\Omega$ and $P = (10/\sqrt2)^2 \times 50/56.2^2 = 0.79\,\mathrm{W}$, which is option 2 -- while the record's key is option 1, 1.13 W. With the arithmetic and the stored key pointing at different options, naming a trap could put one on the paper's actual answer.
- **Why:** This question requires the impedance assembled from both reactances and then the resistive power taken from the rms emf, demonstrated by the stem giving '$V = 10 \sin 314\,t$' so that both $\omega$ and the peak voltage have to be read out of one expression.
- **Note:** Key contested, and the tag follows the record rather than repairing it. I could not reach 1.13 W by any route: using the peak voltage instead of the rms gives 1.59 W, ignoring the reactances gives 1.00 W, and $V_{rms}^2/Z$ gives 0.89 W. A reviewer should check this booklet's printed option order against the key, since 0.79 W is present in the set as option 2. The stem also stores the source as 'emf$_{1}$', which looks like a stray subscript.
<!--/ecat-->

## Q26

Physics · Electromagnetic Induction

> ⚠ The independent solve chose (2); the booklet prints (1).

A then diamagnetic rod is placed vertically between the poles of an electromagnet when the current in the electromagnet is switched on, then the diamagnetic rod is pushed up, out of the horizontal magnetic field, Hence the rod gains gravitational potential energy. The work required to do this comes from.

- **(1)** the induced electric field due to the changing magnectic field
- (2) the current source
- (3) the lattice structure of the material of the rod
- (4) the magnetic field

**Answer** — booklet: (1) · independent solve: (2) · differs

**Publisher's solution**

1. Because when electromagnet is switched in the magnetic field associated with rod increases and leads to generation of induced electric field.

**Solved independently** (answer withheld)

1. When the current is switched on, the electromagnet's field is set up by the external current source, which does work against the back-emf.
2. The diamagnetic rod is repelled from the strong-field region and rises, gaining gravitational potential energy $\Delta U = mgh$.
3. As the rod moves, the flux linkage of the coil changes, inducing an emf that the current source must work against; the extra work it does supplies $mgh$.
4. The magnetic field only stores and transfers energy, and the lattice and induced electric field are not energy sources, so the work comes from the current source, which is option $2$.

**Subtopic:** Induced Electric Field · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 6)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q026_41bbc112_03112026.png?v=41bbc1129096)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q026_0229a9bd_03112026.png?v=0229a9bd944f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A static magnetic field does no work; while the current is being switched on the changing field sets up an induced electric field, and that is what does the work lifting the diamagnetic rod
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The question is answered by tracing the energy back to whatever pays for everything in the circuit, so the current source is named -- which says where the field's energy came from, not what did work on the rod
- **Why:** This question requires the agent that does the work to be identified rather than the agent that supplies the force, demonstrated by the stem reading 'The work required to do this comes from.' after granting that the rod 'gains gravitational potential energy'.
<!--/ecat-->

## Q27

Physics · Magnetic Effect of Electric Current

Current sensitivity of a moving coil galvanometer is $5\,\mathrm{div/Ma}$ and its voltage sensitivity (angular deflection per unit voltage applied) is $20\,\mathrm{div/V}$. The resistance of the galvanometer is

- (1) $500\,\Omega$
- (2) $40\,\Omega$
- **(3)** $250\,\Omega$
- (4) $25\,\Omega$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $R = \frac{\text{Voltage Sensitivity}}{\text{Current Sensitivity}}\frac{(\mathrm{V/div})}{(\mathrm{A/div})}$
2. $= \frac{\frac{1}{20}}{\frac{1}{5000}} = 250\,\mathrm{ohm}$

**Solved independently** (answer withheld)

1. Current sensitivity $I_s = \frac{\theta}{I} = 5\,\mathrm{div/mA} = 5000\,\mathrm{div/A}$.
2. Voltage sensitivity $V_s = \frac{\theta}{V} = \frac{\theta}{I G} = \frac{I_s}{G}$.
3. $G = \frac{I_s}{V_s} = \frac{5000\,\mathrm{div/A}}{20\,\mathrm{div/V}} = 250\,\Omega$, which is option $3$.

**Subtopic:** Moving Coil Galvanometer · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q027_acf26565_03112026.png?v=acf265655c38)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q027_042e015c_03112026.png?v=042e015cec96)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Current sensitivity divided by voltage sensitivity is the galvanometer's resistance, provided the per-milliampere figure is first converted to a per-ampere figure
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The ratio $5/20 = 0.25$ is formed correctly and the milliampere is then cleared with a factor of $10^2$ instead of $10^3$, giving $25\,\Omega$ in place of $250\,\Omega$
- **Why:** This question requires one sensitivity divided by the other with a prefix conversion in between, demonstrated by the stem printing the two sensitivities in different units, '$5\,\mathrm{div/Ma}$' and '$20\,\mathrm{div/V}$'.
- **Note:** The current sensitivity is stored as '5 div/Ma'; the division required for the printed key makes this div/mA, and the trap above turns on exactly that prefix.
<!--/ecat-->

## Q28

Physics · Thermodynamics

The volume ($V$) of a monatomic gas varies with its temperature ($T$), as shown in the graph. The ratio of work done by the gas, to the heat absorbed by it, when it undergoes a change from state A to state B, is

![printed figure: V-T graph: straight line through origin O, process A to B along it](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q028_9b3a5606_03112026.png?v=9b3a5606fe93)

*V-T graph: straight line through origin O, process A to B along it*

- (1) $\frac{2}{7}$
- **(2)** $\frac{2}{5}$
- (3) $\frac{1}{3}$
- (4) $\frac{2}{3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Since graph shous,
2. $\mathrm{Vol} \times \mathrm{temp}$
3. So pressure = constent
4. $\Delta Q = n\,c_p\,\Delta T = n \times \frac{5}{2}R\,\Delta T.$
5. \{ For mobu atomic gas, $C_P = \frac{5}{2}R$ \}
6. $C_V = \frac{3}{2}R$
7. $W = nR\,\Delta T$
8. So, $\frac{w}{\Delta Q} = \frac{2}{5}$

**Solved independently** (answer withheld)

1. The $V$-$T$ graph is a straight line through the origin, so $V \propto T$ and the process A to B is isobaric ($P$ constant).
2. Work done at constant pressure: $W = P\Delta V = nR\Delta T$.
3. Heat absorbed at constant pressure: $Q = nC_p\Delta T$, with $C_p = \frac{5}{2}R$ for a monatomic gas, so $Q = \frac{5}{2}nR\Delta T$.
4. $\frac{W}{Q} = \frac{nR\Delta T}{\frac{5}{2}nR\Delta T} = \frac{2}{5}$, which is option $2$.

**Subtopic:** Isobaric Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q028_51e92007_03112026.png?v=51e9200780d6)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q028_6af99244_03112026.png?v=6af99244b155)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A straight $V$-$T$ line through the origin means constant pressure, so the work is $nR\Delta T$ and the heat is $nC_p\Delta T$ -- and for a MONATOMIC gas $C_p = \tfrac52 R$, giving $W/Q = 2/5$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The isobaric reading of the graph is right and $C_p$ is taken as $\tfrac72 R$, the diatomic value, so the ratio comes out as $2/7$
- **Why:** This question requires the process type read off the graph and then the monatomic heat capacity applied, demonstrated by the stem specifying 'a monatomic gas' and a $V$-$T$ plot whose line runs through the origin so that the pressure is constant.
- **Note:** The figure was supplied as a drawn spec: a straight line from the origin on $V$ against $T$ with the process marked A to B along it, which is what fixes the process as isobaric.
<!--/ecat-->

## Q29

Physics · Waves

The fundamental frequency in an open organ pipe is equal to the third harmonic of a closed organ pipe, If the length of the closed organ pipe is $20\,\mathrm{cm}$, the length of the open organ pipe is

- (1) $16\,\mathrm{cm}$
- **(2)** $13.2\,\mathrm{cm}$
- (3) $12.5\,\mathrm{cm}$
- (4) $8\,\mathrm{cm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to questions,
2. $\frac{\cancel{V}}{2L_0} = 3\frac{\cancel{V}}{4l_c}$
3. $\Rightarrow L_0 = \frac{4L_C}{3\times 2} = \frac{40}{3} = 13.3\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Fundamental of an open organ pipe of length $L_o$: $f_o = \frac{v}{2L_o}$.
2. Third harmonic of a closed organ pipe of length $L_c$: $f_3 = \frac{3v}{4L_c}$.
3. Set them equal: $\frac{v}{2L_o} = \frac{3v}{4L_c}$.
4. Solve for $L_o$: $L_o = \frac{4L_c}{6} = \frac{2L_c}{3}$.
5. Substitute $L_c = 20\,\mathrm{cm}$: $L_o = \frac{2 \times 20}{3} = \frac{40}{3} \approx 13.33\,\mathrm{cm}$.
6. The closest option is $13.2\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q029_9aa82221_03112026.png?v=9aa82221d94a)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q029_4282a792_03112026.png?v=4282a792ebfd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A closed pipe sounds only odd harmonics, so its third harmonic is $3v/4L_c$, and setting an open pipe's fundamental $v/2L_o$ equal to it gives $L_o = 2L_c/3$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The 'third harmonic' of the closed pipe is taken as its third available resonance, $5v/4L_c$, so the right formula is used with $n=5$ and $L_o$ comes out as $40/5 = 8\,\mathrm{cm}$
- **Why:** This question requires one pipe's harmonic equated with the other pipe's fundamental, demonstrated by the stem reading 'The fundamental frequency in an open organ pipe is equal to the third harmonic of a closed organ pipe' with the closed length fixed at 20 cm.
- **Note:** The key is printed as 13.2 cm where $2L_c/3$ is 13.3 cm; the tag follows the printed option.
<!--/ecat-->

## Q30

Physics · Thermodynamics

The efficiency of an ideal heat engine working between the freezing point and boiling point of water, is

- (1) $12.5\%$
- (2) $26.8\%$
- (3) $6.25\%$
- (4) $20\%$

**Answer** — booklet: (none) · independent solve: (2) · unchecked

**Publisher's solution**

1. $m = 1 - \frac{T_2}{T_1}$
2. $= 1 - \frac{273}{373} = \frac{100}{373} = 26.8\%$

**Solved independently** (answer withheld)

1. An ideal heat engine is a Carnot engine, so $\eta = 1 - \frac{T_2}{T_1}$.
2. Freezing point $T_2 = 273\,\text{K}$ and boiling point $T_1 = 373\,\text{K}$.
3. $\eta = 1 - \frac{273}{373} = \frac{100}{373} \approx 0.268$.
4. $\eta \approx 26.8\%$, which is option $2$.

**Subtopic:** Carnot Engine · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q030_ab00e65c_03112026.png?v=ab00e65cb5c9)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q030_ccb7d5c8_03112026.png?v=ccb7d5c89a3b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Carnot efficiency is $1 - T_C/T_H$ with both temperatures in kelvin, so the freezing and boiling points of water give $1 - 273/373$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No key is stored for this question: `correct_answer` is null, `accepted_answers` is empty and `answer_line_as_printed` is null, so there is no printed verdict to tag against and no option can be called wrong.
- **Why:** This question requires the Carnot efficiency evaluated between two named fixed points, demonstrated by the stem naming only 'the freezing point and boiling point of water' and leaving the temperatures to be supplied in kelvin.
- **Note:** Key absent from our record; the paper is not at fault. A reviewer holding the key should check $1 - 273/373 = 26.8\%$ against option 2. The mechanism this set looks built around is the Celsius-for-kelvin slip, which gives $1 - 0/100 = 100\%$ and is NOT printed, so the remaining options (12.5%, 20%, 6.25%) should be checked for any route at all before any trap is recorded.
<!--/ecat-->

## Q31

Physics · Kinetic Theory of Gases

At what temperature will the rms speed of oxygen molecules becomes just sufficient for escaping from the Earth’s atmosphere? (Given: Mass of oxygen molecule $(m) = 2.76\times10^{-26}\,\mathrm{kg}$ Boltzmann’s constant $k_{B} = 1.38\times10^{-23}\,\mathrm{J\,K^{-1}}$

- (1) $1.254\times10^{4}\,\mathrm{K}$
- (2) $2.508\times10^{4}\,\mathrm{k}$
- (3) $5.016\times10^{4}\,\mathrm{K}$
- (4) $8.360\times10^{4}\,\mathrm{K}$

**Answer** — booklet: (none) · independent solve: (4) · unchecked

**Publisher's solution**

1. For escaping out from earth, $\mathrm{Vrms} = \mathrm{vescepe}$
2. $\Rightarrow \sqrt{\frac{3KT}{M}} = 11.2\times10^{3}$
3. $\Rightarrow \sqrt{\frac{3\times1.38\times10^{-23}\times T}{22.76\times10^{-26}}} = 11200$
4. $\Rightarrow \frac{3T\times1000}{2} = 11200\times11200$
5. $\Rightarrow T \approx 8.36\times10^{4}\,\mathrm{K}$

**Solved independently** (answer withheld)

1. The molecules escape when $v_{rms} = v_e$, with $v_{rms} = \sqrt{\frac{3k_B T}{m}}$ and Earth's escape speed $v_e = 11.2\,\mathrm{km\,s^{-1}} = 1.12\times10^{4}\,\mathrm{m\,s^{-1}}$.
2. Squaring and solving for $T$: $T = \frac{m v_e^{2}}{3k_B}$.
3. $v_e^{2} = (1.12\times10^{4})^{2} = 1.2544\times10^{8}\,\mathrm{m^2\,s^{-2}}$.
4. $m v_e^{2} = 2.76\times10^{-26}\times1.2544\times10^{8} = 3.462\times10^{-18}\,\mathrm{J}$.
5. $3k_B = 3\times1.38\times10^{-23} = 4.14\times10^{-23}\,\mathrm{J\,K^{-1}}$.
6. $T = \frac{3.462\times10^{-18}}{4.14\times10^{-23}} \approx 8.36\times10^{4}\,\mathrm{K}$, which is option $4$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q031_6c828e65_03112026.png?v=6c828e6504bd)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q031_3c92e3f0_03112026.png?v=3c92e3f03922)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The temperature at which a gas molecule's rms speed equals the escape speed, from $\frac{3}{2}k_BT=\frac{1}{2}mv^2$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the record before looking for a route: the Given list breaks off mid-bracket after Boltzmann's constant with no closing parenthesis, no answer line was captured, and accepted_answers is empty, so no option can be excluded from carrying a trap
- **Why:** This question requires the temperature that makes $v_{rms}$ equal the escape speed, demonstrated by "the rms speed of oxygen molecules becomes just sufficient for escaping from the Earth's atmosphere" with $m$ and $k_B$ supplied; traps are withheld because the stored record is incomplete.
- **Note:** Record gaps, not a judgement on the paper: the stem's "(Given: ..." list is unclosed and stops after $k_B$, and unlike q032-q036 there is no answer_line_as_printed and accepted_answers is empty. Option 2 prints lowercase 'k' for kelvin. For a reviewer holding the booklet: with $v_{esc}=11.2\,\mathrm{km\,s^{-1}}$, $T=mv^2/3k_B=8.36\times10^{4}\,\mathrm{K}$, which is option 4, and the three lower options sit at $\times\frac12$, $\times\frac14$ and $\times\frac{3}{20}$ of it, with $1.254$ echoing the digits of $v^2=1.2544\times10^{8}$; the exponent-and-factor mechanism should be checked once the key is restored.
<!--/ecat-->

## Q32

Physics · Wave Optics

Unpolarised light is incident from air on a plane surface of a material of refractive index ‘$\mu$’ At a particular angle of incidence ‘I’, it is found that the reflected and refracted rays are perpendicular to each other, Which of the following options is correct for this situation?

- (1) $i = \tan^{-1}\left(\frac{1}{\mu}\right)$
- (2) Reflected light is polarized with its electric vector parallel to the plane of incidence
- (3) $i = \sin^{-1}\left(\frac{1}{\mu}\right)$
- **(4)** Reflected light is polarized with its electric vector perpendicular to the plane of incidence

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Since reflected & refracted rays are mutually perp
2. So, $\mu = \tan (i)$
3. So, Ans (4)

**Solved independently** (answer withheld)

1. Reflected and refracted rays perpendicular means $i + r = 90^\circ$, so $r = 90^\circ - i$.
2. Snell's law: $\sin i = \mu \sin r = \mu \sin(90^\circ - i) = \mu \cos i$.
3. Hence $\tan i = \mu$, i.e. $i = \tan^{-1}\mu$ (Brewster angle), so options $1$ ($\tan^{-1}(1/\mu)$) and $3$ ($\sin^{-1}(1/\mu)$) are wrong.
4. At the Brewster angle the component with $\vec{E}$ parallel to the plane of incidence is not reflected, so option $2$ is wrong.
5. The reflected light is plane polarized with $\vec{E}$ perpendicular to the plane of incidence, which is option $4$.

**Subtopic:** Polarization by Reflection and Refraction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q032_a9a24d14_03112026.png?v=a9a24d147707)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q032_2918bebc_03112026.png?v=2918bebca9fb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** At Brewster's angle the reflected beam is completely polarised perpendicular to the plane of incidence, and $\tan i_p=\mu$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who knows that reflection at this angle polarises the light, but stores the surviving vibration as lying in the plane of incidence, picks the parallel wording; it is the parallel component that passes into the refracted ray, so the reflection keeps only the perpendicular one
- **Why:** This question requires Brewster's condition applied to decide the state of the reflected beam, demonstrated by "the reflected and refracted rays are perpendicular to each other" with no numbers to compute.
<!--/ecat-->

## Q33

Physics · Wave Optics

In Young’s double slit experiment the separation $d$ between the slits is $2\,\mathrm{mm}$, the wavelength $\lambda$ of the light used is $5896\,\mathrm{A}$ and distance $D$ between the screen and slits is $100\,\mathrm{cm}$. It is found that the angular width of the fringes is $0.20^{0}$. To increase the fringe angular width to $0.21^{0}$ (with same $\lambda$ and $D$) the separation between he slits needs to be changed to

- (1) $1.7\,\mathrm{mm}$
- (2) $1.8\,\mathrm{mm}$
- (3) $2.1\,\mathrm{mm}$
- **(4)** $1.9\,\mathrm{mm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ang Fringe width $= \frac{\beta}{D} = \frac{\lambda}{d}$
2. $\Rightarrow 0.2 = \frac{\lambda}{2}$
3. & $0.21 = \frac{\lambda}{d^{1}}$
4. $\Rightarrow \frac{0.2}{0.21} = \frac{d^{1}}{2} \Rightarrow d^{1} = 1.9\,\mathrm{mm}$

**Solved independently** (answer withheld)

1. Angular fringe width in YDSE is $\theta = \frac{\lambda}{d}$, independent of $D$.
2. With $\lambda$ fixed, $\theta_1 d_1 = \theta_2 d_2$.
3. $d_2 = \frac{\theta_1}{\theta_2} d_1 = \frac{0.20^{\circ}}{0.21^{\circ}} \times 2\,\mathrm{mm}$.
4. $d_2 = 0.952 \times 2\,\mathrm{mm} \approx 1.905\,\mathrm{mm} \approx 1.9\,\mathrm{mm}$, which is option $4$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q033_ed939186_03112026.png?v=ed93918682e6)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q033_669953e9_03112026.png?v=669953e910d0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Angular fringe width in a double slit is $\theta=\lambda/d$, so widening the fringes means narrowing the slit separation
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A student who has $\theta=\lambda/d$ but moves $d$ the same way as $\theta$ raises the separation by the same 5% the width rose, landing on 2.1 mm; $d$ is in the denominator, so it has to fall
- **Why:** This question requires a new slit separation computed from the inverse relation between angular width and separation, demonstrated by "to increase the fringe angular width to $0.21^{0}$ (with same $\lambda$ and $D$) the separation between he slits needs to be changed to".
- **Note:** The printed $d$, $\lambda$ and $D$ are redundant once the two angular widths are given; only the ratio $0.20/0.21$ and $d=2\,\mathrm{mm}$ enter the answer.
<!--/ecat-->

## Q34

Physics · Ray Optics

An astronomical refracting telescope will have large angular magnification and high angular resolution, when it has an objective lens of \

- (1) small focal length and small diameter
- (2) small focal length and large diameter
- **(3)** large focal length and large diameter
- (4) large focal length and small diameter

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For telescope
2. $M = \frac{f_o}{f_e}$
3. & Resolving power $= \frac{D}{1.22\,\lambda}$
4. So, Ans (3)

**Solved independently** (answer withheld)

1. For a refracting telescope in normal adjustment, $m = \frac{f_o}{f_e}$, so a large objective focal length $f_o$ gives large angular magnification.
2. The minimum resolvable angle is $\Delta\theta = \frac{1.22\,\lambda}{D}$, so resolving power $\frac{1}{\Delta\theta} = \frac{D}{1.22\,\lambda}$ increases with objective diameter $D$.
3. Both conditions together need large focal length and large diameter, which is option $3$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q034_56bd80bc_03112026.png?v=56bd80bc66f7)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q034_65cd3d89_03112026.png?v=65cd3d897e16)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A telescope objective needs a long focal length for angular magnification and a wide aperture for resolution
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student applies $m=f_o/f_e$ correctly and so wants the long objective focal length, then treats the objective like a lens stopped down for a sharper picture and chooses the small diameter; the diffraction limit $1.22\lambda/D$ runs the other way
- **Why:** This question requires two stated relations applied to the objective's properties with no quantity produced, demonstrated by "will have large angular magnification and high angular resolution, when it has an objective lens of".
- **Note:** E1 called this statement_options; the four options are not statements to be judged but two objective-lens properties bundled in each option and graded whole, so the shape recorded here is two_part. The stem also ends in a stray backslash where the printed blank should be.
<!--/ecat-->

## Q35

Physics · Work, Energy and Power

A body initially at rest and sliding along a frictionless track from a height h (As shown in the figure) just completes a vertical circle of diameter $AB = D$. The height h is equal to

![printed figure: A body at rest at height h slides down a frictionless incline to A and enters a vertical circle of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q035_cbbce295_03112026.png?v=cbbce2959404)

*A body at rest at height h slides down a frictionless incline to A and enters a vertical circle of diameter AB*

- **(1)** $\frac{5}{4}D$
- (2) $\frac{3}{2}D$
- (3) $\frac{7}{5}D$
- (4) $D$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For body to complete vertical circle
2. $V_A = \sqrt{5Rg} = \sqrt{\frac{5}{2}gD}$
3. So, $\sqrt{2gH} = \sqrt{\frac{5}{2}gD}$
4. $\Rightarrow 2gH = \frac{5}{2}\cancel{g}D$
5. $\Rightarrow H = \frac{5}{4}D$

**Solved independently** (answer withheld)

1. The circle has diameter $AB = D$, so its radius is $R = \frac{D}{2}$.
2. To just complete the vertical circle, the speed at the top $B$ must satisfy $v_B^2 = gR$ (normal force zero there).
3. Energy conservation from $A$ to $B$: $v_A^2 = v_B^2 + 2g(2R) = gR + 4gR = 5gR$.
4. Energy conservation on the frictionless track from rest at height $h$ to $A$: $mgh = \frac{1}{2}m v_A^2 = \frac{5}{2}mgR$, so $h = \frac{5}{2}R$.
5. $h = \frac{5}{2}\cdot\frac{D}{2} = \frac{5}{4}D$, which is option $1$.

**Subtopic:** Motion in a Vertical Circular Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q035_d2284249_03112026.png?v=d2284249f59f)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q035_0df637f6_03112026.png?v=0df637f6c2c3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** To just complete a vertical circle the speed at the top must satisfy $v^2=gR$, so the release height is the loop height plus a quarter of the diameter
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  A student writes energy conservation from the release point to the top of the loop and reads "just completes" as barely arriving there, so sets $v_{top}=0$ and gets $h=D$; the loop also demands $v_{top}^2=gR$, which adds $D/4$
- **Why:** This question requires the release height derived from energy conservation plus the top-of-loop speed condition, demonstrated by "just completes a vertical circle of diameter $AB = D$".
- **Note:** The figure was supplied as a printed PNG plus a spec; in it $h$ is measured from the release point down to the level of A, the lower end of the loop, which is the reading the $\frac54 D$ key requires.
<!--/ecat-->

## Q36

Physics · Rotational Motion

Three objects, A : (a solid sphere), B: (A thin circular disk) and C : (a circular ring), each have the same mass $M$ and radius $R$. They all spin with the same angular speed about their own symmetry axes, The amounts of work ($W$) required to being them to rest, would satisfy the relation

- (1) $W_A > W_C > W_B$
- **(2)** $W_C > W_B > W_A$
- (3) $W_B > W_A > W_C$
- (4) $W_A > W_B > W_C$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Accd to work energy theorem, $W = k_f - k_i$
2. Since $k_f = 0$
3. $w \times k_i$
4. $K_A = \frac{1}{2} \times Iw^{2} = \frac{1}{2} \times \frac{2}{5} MR^{2}W^{2}$
5. $K_B = \frac{1}{2} \times \frac{1}{2} MR^{2}w^{2}$
6. $K_C = \frac{1}{2} MR^{2}w^{2}$
7. So, $W_C > W_B > W_A$

**Solved independently** (answer withheld)

1. By the work-energy theorem, the work needed to stop each body equals its rotational kinetic energy, $W = \frac{1}{2} I \omega^2$.
2. Since $M$, $R$ and $\omega$ are the same for all three, $W \propto I$.
3. Solid sphere about a diameter: $I_A = \frac{2}{5} M R^2 = 0.4\, M R^2$.
4. Thin disk about its symmetry axis: $I_B = \frac{1}{2} M R^2 = 0.5\, M R^2$.
5. Ring about its symmetry axis: $I_C = M R^2$.
6. $I_C > I_B > I_A \Rightarrow W_C > W_B > W_A$, which is option $2$.

**Subtopic:** Kinetic Energy of a Rigid Body Rotating About a Given Axis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q036_c62c1166_03112026.png?v=c62c1166e988)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q036_0d8d27c6_03112026.png?v=0d8d27c61e01)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Work to stop a spinning body is $\frac12 I\omega^2$, so for equal $M$, $R$ and $\omega$ the ranking is the ranking of moment of inertia: ring, then disc, then solid sphere
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student ranks the three bodies by how much material they contain rather than by how far that material sits from the axis, putting the solid sphere first and the hollow ring last, which is the exact reverse of $\frac25MR^2<\frac12MR^2<MR^2$
- **Why:** This question requires the three bodies ranked by rotational kinetic energy, demonstrated by "the amounts of work ($W$) required to being them to rest, would satisfy the relation" with each option an ordering.
<!--/ecat-->

## Q37

Physics · Laws of Motion

Which one of the following statements is incorrect?

- **(1)** coefficient of sliding friction has dimensions of length
- (2) Rolling friction is smaller than sliding
- (3) Friction force opposes the relative motion
- (4) Limiting value of static friction is directly proportional to normal reaction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mu$ is dimensionless

**Solved independently** (answer withheld)

1. The coefficient of sliding friction is defined as $\mu_k = \frac{f_k}{N}$.
2. Both $f_k$ and $N$ are forces with dimensions $[MLT^{-2}]$, so $[\mu_k] = \frac{[MLT^{-2}]}{[MLT^{-2}]} = [M^0L^0T^0]$, i.e. dimensionless, not length; statement $1$ is incorrect.
3. Rolling friction is smaller than sliding friction, friction opposes relative motion, and $f_s^{max} = \mu_s N$ is directly proportional to $N$, so statements $2$, $3$ and $4$ are correct.
4. The incorrect statement is option $1$.

**Subtopic:** Kinetic Friction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q037_228c249f_03112026.png?v=228c249fa3a2)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q037_86e40546_03112026.png?v=86e405468318)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The coefficient of friction is a dimensionless ratio of two forces, while the limiting static friction itself equals $\mu_s N$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  A student who has learnt that static friction is self-adjusting and only satisfies $f_s \le \mu_s N$ reads "directly proportional to normal reaction" as the false claim; the option says "Limiting value", and at that limit the relation is an equality
- **Why:** This question requires four printed claims about friction to be graded against stated facts, demonstrated by "Which one of the following statements is incorrect?" with "coefficient of sliding friction has dimensions of length" as the false one.
- **Note:** Negated task ("incorrect"), which is why the three wrong options are all true statements. The trap recorded is the one the printed wording supports — option 4's qualifier "Limiting value" — rather than a bare polarity reflex, because a polarity slip would not pick out any one of the three true options.
<!--/ecat-->

## Q38

Physics · Work, Energy and Power

A moving block having mass $m$, collides with another stationary block having mass $4m$ the lighter block comes to rest after collision, When the initial velocity of the lighter block is $v$, then the value of coefficient of restitution$(e)$ will be

- (1) $0.4$
- (2) $0.5$
- (3) $0.8$
- **(4)** $0.25$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. By conservation of linear momentum,
2. $mv + 4m \times 0 = m \times 0 + 4m \times v'$
3. $\Rightarrow v^{1} = \frac{v}{4}$
4. So, $e = \left|\frac{\frac{v}{4} - 0}{vr - 0}\right| = \frac{1}{4} = 0.25$

**Solved independently** (answer withheld)

1. Linear momentum is conserved: $m v + 4m(0) = m(0) + 4m\,v_2$.
2. So $v_2 = \frac{v}{4}$.
3. $e = \frac{v_2 - v_1}{u_1 - u_2} = \frac{\frac{v}{4} - 0}{v - 0}$.
4. $e = \frac{1}{4} = 0.25$, which is option $4$.

**Subtopic:** Problem on Coefficient of Restitution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q038_845c31cb_03112026.png?v=845c31cbf85d)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q038_87bc81a8_03112026.png?v=87bc81a87bae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Coefficient of restitution is the ratio of separation speed to approach speed, so a lighter block stopping dead fixes $e = m_1/m_2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  A student carries over the bouncing-ball form $e=\sqrt{h'/h}$, i.e. $e$ as the square root of the kinetic-energy ratio, and gets $\sqrt{\tfrac14}=0.5$; here $e$ is a ratio of relative velocities, which gives $0.25$
- **Why:** This question requires $e$ computed from momentum conservation plus the restitution definition, demonstrated by "the lighter block comes to rest after collision" with $m$ and $4m$ given.
<!--/ecat-->

## Q39

Physics · Current Electricity

A carbon resistor of $(47 \pm 4.7)\,\mathrm{k\Omega}$ is to be marked with rings of different colours for its identification. The colour code sequence will be

- (1) Green – orange – violet – gold
- (2) Violet – Yellow – Orange – Silver
- (3) yellow – green – Violet – gold
- (4) Yellow – Violet – Orange – Silver

**Answer** — booklet: (none) · independent solve: (4) · unchecked

**Publisher's solution**

1. $R = 47000\,\Omega \pm 4700\,\Omega$
2. So colour code is yellow violet orange silver
3. ($\because$ Tolerance $= 10\%$)

**Solved independently** (answer withheld)

1. $47\,\mathrm{k\Omega} = 47 \times 10^{3}\,\Omega$.
2. First digit $4 \rightarrow$ Yellow; second digit $7 \rightarrow$ Violet.
3. Multiplier $10^{3} \rightarrow$ Orange.
4. Tolerance $= \frac{4.7}{47} \times 100\% = 10\% \rightarrow$ Silver.
5. Sequence Yellow – Violet – Orange – Silver, which is option $4$.

**Subtopic:** Colour Code of Carbon Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q039_f1007268_03112026.png?v=f1007268eb41)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q039_d8d304a6_03112026.png?v=d8d304a6fe34)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The resistor colour code: two digit bands, a power-of-ten multiplier band, and a tolerance band read from the quoted uncertainty
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the record before looking for a route: no answer line was captured and accepted_answers is empty, so no option can be excluded from being the keyed one, and the rulebook's own worked example (§7) is a colour-code question tagged confidently against an unconfirmed record
- **Why:** This question requires the agreed colour-code convention applied band by band to a stated resistance and tolerance, demonstrated by "A carbon resistor of $(47 \pm 4.7)\,\mathrm{k\Omega}$ ... The colour code sequence will be".
- **Note:** Record gap, not a judgement on the paper: unlike q037, q038, q040-q042 this question carries no answer_line_as_printed and accepted_answers is empty. For a reviewer restoring the key: $47\,\mathrm{k\Omega} = 47\times10^{3}\,\Omega$ gives yellow (4), violet (7), orange ($\times10^{3}$), and $4.7/47 = 10\%$ gives silver — option 4. The mechanism to check once the key is in: option 2 prints the same four colours with the two digit bands interchanged (violet-yellow reads 74), which would be a `reversed` trap, while options 1 and 3 end in gold, i.e. $\pm5\%$, which the printed $\pm4.7\,\mathrm{k\Omega}$ rules out. E1 called the shape arrange_in_order; the live qtype list has no ordering shape, and each option is a four-band sequence graded whole, so two_part is recorded.
<!--/ecat-->

## Q40

Physics · Current Electricity

A set of ‘$n$’ equal resistors, of value ‘$R$’ each are connected in series to a battery of emf ‘$E$’ and internal resistance ‘$R$’. The current drawn is $I$. Now, the ‘$n$’ resistors are connected in parallel to the same battery, Then the current drawn from battery becomes $10\,I$, The value of ‘$n$’ is

- (1) 9
- **(2)** 10
- (3) 20
- (4) 11

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to question
2. $I = \frac{E}{nR + R} = \frac{E}{R\left(n + 1\right)}$
3. $\&\ 10I = \frac{E}{\frac{R}{n} + R} = \frac{E}{R\left[1 + \frac{1}{n}\right]}$
4. $\Rightarrow 10 = \frac{\frac{1}{\left(1 + \frac{1}{n}\right)}}{1\left(n + 1\right)} = \frac{n + 1}{1 + \frac{1}{n}} = n$
5. $n = 10$

**Solved independently** (answer withheld)

1. In series the $n$ resistors give $R_s = nR$, so $I = \frac{E}{nR + R} = \frac{E}{(n+1)R}$.
2. In parallel the $n$ resistors give $R_p = \frac{R}{n}$.
3. Then $I' = \frac{E}{\frac{R}{n} + R} = \frac{nE}{(n+1)R} = nI$.
4. Setting $I' = 10I$ gives $nI = 10I$, so $n = 10$, which is option $2$.

**Subtopic:** Combination of Resistors, Relationship Between EMF, Potential Difference and Current With Internal Resistance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q040_04260a05_03112026.png?v=04260a050054)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q040_9780b04f_03112026.png?v=9780b04f45ef)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With the battery's internal resistance equal to $R$, regrouping $n$ equal resistors from series to parallel multiplies the current by exactly $n$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  A student sets $nR+R = 10(R/n+R)$ and then drops the small $10R/n$ term as negligible beside $10R$, which leaves $n+1=10$ and so $n=9$; keeping the term gives $n^2-9n-10=0$ and $n=10$
- **Why:** This question requires $n$ computed from the two total resistances, demonstrated by "the current drawn from battery becomes $10\,I$, The value of '$n$' is".
<!--/ecat-->

## Q41

Physics · Current Electricity

A battery consists of a variable number ‘$n$’ of identical cells (Having resistance ‘$r$’ each) which are connected in series. The terminal of the battery are short-circuited and the current $I$ is measured. Which of the graphs shows the correct relationship between $I$ and $n$?

- (1) ![printed figure: Graph of I against n: a curve from the origin rising ever more steeply (concave up)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q041_option_1_17424e06_03112026.png?v=17424e06b63e) *Graph of I against n: a curve from the origin rising ever more steeply (concave up)*
- **(2)** ![printed figure: Graph of I against n: a horizontal line starting on the I axis](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q041_option_2_c07f114a_03112026.png?v=c07f114af043) *Graph of I against n: a horizontal line starting on the I axis*
- (3) ![printed figure: Graph of I against n: a curve rising from the origin and levelling off (concave down)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q041_option_3_bee91e33_03112026.png?v=bee91e331fba) *Graph of I against n: a curve rising from the origin and levelling off (concave down)*
- (4) ![printed figure: Graph of I against n: a straight line rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q041_option_4_62df237c_03112026.png?v=62df237c64e1) *Graph of I against n: a straight line rising from the origin O*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. When battery is short circuited
2. $I = \frac{ne}{nr} = \frac{e}{r}$
3. It is in dependent of ‘$n$’

**Solved independently** (answer withheld)

1. For $n$ identical cells in series, total emf is $nE$ and total internal resistance is $nr$.
2. Short-circuiting the terminals makes the external resistance $R = 0$.
3. $I = \frac{nE}{R + nr} = \frac{nE}{0 + nr} = \frac{E}{r}$.
4. $I = \frac{E}{r}$ does not depend on $n$, so the $I$ vs $n$ graph is a horizontal line, which is option $2$.

**Subtopic:** Combination of Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q041_0cab6ec7_03112026.png?v=0cab6ec756a3)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q041_06f528e4_03112026.png?v=06f528e46b29)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Shorting $n$ identical cells in series gives $I = nE/nr = E/r$, so the current does not depend on how many cells there are
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The four options are graphs and all four options_en are empty strings, so the curves were not supplied to this step; with no option content, no route can be named or audited
- **Why:** This question requires the dependence of the short-circuit current on the number of cells, demonstrated by "Which of the graphs shows the correct relationship between $I$ and $n$?".
- **Note:** Our reach, not damage to the paper: options 1-4 are graph images and the packet carries them as empty strings (has_figure is also recorded false). For a reviewer holding the four plots: adding cells in series raises the emf to $nE$ and the internal resistance to $nr$ together, so $I=E/r$ and the correct curve is a horizontal line. The distractor mechanism to check is a rising straight line, reached by adding the emfs while leaving the internal resistance at $r$ (that would be formula_misused), and a falling $1/n$ curve, reached by adding the resistances while leaving the emf at $E$.
<!--/ecat-->

## Q42

Physics · Kinematics

> ⚠ The independent solve chose (3); the booklet prints (4).

A toy car with charge $q$ moves on a frictionless horizontal plane surface under the influence of a uniform electric field $\vec{E}$. Due to the force $q$ ,$\vec{E}$ its velocity increases from 0 to $6\,\mathrm{m/s}$ in one second duration. At that instant the direction of the filed is reversed. The care continues to move for two more seconds under the influence of this field, The average velocity and the average speed of the toy car between 0 to 3 seconds are respectively

- (1) $1.5\,\mathrm{m/s}$, $3\,\mathrm{m/s}$
- (2) $2\,\mathrm{m/s}$, $4\,\mathrm{m/s}$
- (3) $1\,\mathrm{m/s}$, $3\,\mathrm{m/s}$
- **(4)** $1\,\mathrm{m/s}$, $3\,\mathrm{m/s}$

**Answer** — booklet: (4) · independent solve: (3) · differs

**Publisher's solution**

1. Acceleration, $a = \frac{qE}{m}$
2. $v = u + at$
3. $\Rightarrow 6 = 0 + \frac{qE}{m} \times 1$
4. $\Rightarrow \frac{qE}{m} = 6 = q$ ..........$(1)$
5. From $t = 1$ to $t = 3$, the body retards,
6. $V_f = 6 = \frac{qE}{m} \times 2 = -6\,\mathrm{m/s}$

![printed figure: Toy car stages: u = 0 to v = 6 m/s to v = 0 over t = 0, 1, 2, with displacements s1, s2 and the return s3 by t = 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q042_sol_1_da1460bc_03112026.svg?v=da1460bcd945)

*Toy car stages: u = 0 to v = 6 m/s to v = 0 over t = 0, 1, 2, with displacements s1, s2 and the return s3 by t = 3*

7. $CV = 6\,\mathrm{m/s}$
8. $S_1 = \frac{1}{2} \times a \times 1^2 = \frac{1}{2}a \quad \left[s = ut + \frac{1}{2}at^2\right]$
9. $S_2 = \frac{O^2 - 6^2}{2(-a)} = \frac{18}{a} \quad \left[S = \frac{v^2 - u^2}{29}\right]$
10. $S_3 = \frac{1}{2} \times 9 \times 1^2 = \frac{1}{2}a \quad \left[S = Ut + \frac{1}{2}at^2\right]$
11. Avg Speed $= \frac{\frac{1}{2}a + \frac{18}{a} + \frac{1}{2}a}{3}$
12. Putting $a = 6$
13. $\Rightarrow$ Avg speed $= 3\,\mathrm{m/s}$
14. Avg velocity $= \frac{\frac{1}{2}a + \frac{18}{a} + \frac{1}{2}a}{3}$
15. $= 1\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. From $0$ to $1\,\mathrm{s}$: $a = \frac{\Delta v}{\Delta t} = \frac{6 - 0}{1} = 6\,\mathrm{m/s^2}$.
2. $s_1 = \frac{1}{2} a t^2 = \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$ forward.
3. The field reverses, so the force reverses with the same magnitude: $a' = -6\,\mathrm{m/s^2}$ starting from $v = 6\,\mathrm{m/s}$.
4. From $1$ to $2\,\mathrm{s}$: $v = 6 - 6(1) = 0$, and $s_2 = 6(1) - \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$ forward.
5. From $2$ to $3\,\mathrm{s}$: the car starts from rest and moves back, $s_3 = \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$ backward.
6. Net displacement $= 3 + 3 - 3 = 3\,\mathrm{m}$; total distance $= 3 + 3 + 3 = 9\,\mathrm{m}$.
7. Average velocity $= \frac{3}{3} = 1\,\mathrm{m/s}$; average speed $= \frac{9}{3} = 3\,\mathrm{m/s}$.
8. The pair $1\,\mathrm{m/s}$, $3\,\mathrm{m/s}$ is printed as both option $3$ and option $4$; option $3$ is chosen.

**Subtopic:** Average Velocity, Average Speed · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 10)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q042_3965e383_03112026.png?v=3965e383d0bc)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q042_e9d5add2_03112026.png?v=e9d5add28ee7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Average velocity uses net displacement and average speed uses total path length, so reversing the field makes the two differ
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Options 3 and 4 are character-identical ($1\,\mathrm{m/s}$, $3\,\mathrm{m/s}$), so one of them is a damaged capture of a distinct printed option; tagging option 3 would mean tagging the text of the keyed answer
- **Why:** This question requires an average velocity and an average speed computed over the same three seconds, demonstrated by "The average velocity and the average speed of the toy car between 0 to 3 seconds are respectively".
- **Note:** Duplicated options, which §5a names as source damage rather than a property of the question: option 3 and option 4 carry the same text and the key points at 4. The physics is unaffected — $a=6\,\mathrm{m\,s^{-2}}$ for the first second then $-6\,\mathrm{m\,s^{-2}}$ for two more gives displacement $3+0=3\,\mathrm{m}$ and path length $3+3+3=9\,\mathrm{m}$, so $1\,\mathrm{m/s}$ and $3\,\mathrm{m/s}$, matching both duplicated options. A reviewer should restore option 3 from the printed booklet; option 2 ($2\,\mathrm{m/s}$, $4\,\mathrm{m/s}$) and option 1 ($1.5\,\mathrm{m/s}$, $3\,\mathrm{m/s}$) should then be checked for the displacement-for-distance swap and for the two-second-interval slip.
<!--/ecat-->

## Q43

Physics · Laws of Motion

A block of mass m is placed on a smooth inclined wedge ABC af inclination $\theta$ as shown in the figure. The wedge is given an acceleration ‘a’ towards the right. The relation between a and $\theta$ for the block to remain stationary on the wedge is

![printed figure: Block m on a smooth hatched wedge ABC of inclination θ, wedge accelerated by a to the right](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q043_3c16c24c_03112026.png?v=3c16c24cfbe2)

*Block m on a smooth hatched wedge ABC of inclination θ, wedge accelerated by a to the right*

- (1) $a = g\tan\theta$
- (2) $a = \frac{g}{\mathrm{cosec}\,\theta}$
- (3) $a = g\cos\theta$
- (4) $a = \frac{g}{\sin\theta}$

**Answer** — booklet: (none) · independent solve: (1) · unchecked

**Publisher's solution**

1. When wedge accelerate s, block, experiences psendo force in opp direction,
2. $\Rightarrow$ For block, to remain at rest,
3. $\cancel{m}g\sin\theta = \cancel{m}a\cos\theta$
4. $\Rightarrow \boxed{a = g\,\mathrm{ten}\,\theta}$

**Solved independently** (answer withheld)

1. From the figure, face $AB$ rises to the left at angle $\theta$, so its outward normal points up and to the right, and the wedge accelerates to the right with $a$.
2. In the wedge frame the block feels gravity $mg$ downward, a pseudo force $ma$ to the left, and the normal force $N$ (smooth surface, no friction).
3. Resolve along the incline: gravity's down-slope component is $mg\sin\theta$ and the pseudo force's up-slope component is $ma\cos\theta$.
4. For the block to stay at rest: $ma\cos\theta = mg\sin\theta$.
5. $a = g\frac{\sin\theta}{\cos\theta} = g\tan\theta$.
6. Check in the ground frame: $N\sin\theta = ma$ and $N\cos\theta = mg$ give $\tan\theta = \frac{a}{g}$, the same result, which is option $1$.

**Subtopic:** Pseudo Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q043_8714caf4_03112026.png?v=8714caf44bc4)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q043_4668767a_03112026.png?v=4668767af936)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In the accelerating wedge's frame the block feels a backward pseudo-force $ma$, and staying put on a smooth incline needs $ma\cos\theta = mg\sin\theta$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the record before looking for a route: no answer line was captured and accepted_answers is empty, so no option can be ruled out as the keyed one and any trap would risk sitting on the official answer
- **Why:** This question requires the acceleration expression derived from a force balance in the wedge's frame, demonstrated by "The relation between a and $\theta$ for the block to remain stationary on the wedge is".
- **Note:** Record gap, not a judgement on the paper: unlike q044 and q045 this question carries no answer_line_as_printed and accepted_answers is empty. The figure was supplied (PNG plus spec, inclination claimed at 30 deg and checked within 1.5 deg), so the shortfall is the key alone. For a reviewer restoring it: with the wedge accelerating right, balancing along the smooth surface gives $ma\cos\theta = mg\sin\theta$, so $a = g\tan\theta$ — option 1. The mechanism to check once the key is in: option 2 prints $g/\mathrm{cosec}\,\theta$, which is $g\sin\theta$ in disguise and is what resolving gravity along the surface alone yields, and option 3 is $g\cos\theta$, the perpendicular component; I would expect formula_misused on option 2, but it cannot be confirmed without the key.
<!--/ecat-->

## Q44

Physics · Units and Measurements

A student measured the diameter of a small steel ball using a screw gauge of least count $0.001\,\mathrm{cm}$. The main scale reading is $5\,\mathrm{mm}$ and zero of circular scale division coincides with $25$ divisions above the referene level. If screw gauge has a zero error of $-0.004\,\mathrm{cm}$, the correct diameter of the ball is.

- **(1)** $0.529\,\mathrm{cm}$
- (2) $0.521\,\mathrm{cm}$
- (3) $0.053\,\mathrm{cm}$
- (4) $0.525\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. L. count $= 0.001\,\mathrm{cm}$ zero error $= -0.004\,\mathrm{cm}$
2. MSR $= 5\,\mathrm{mm}$
3. Circuler scale Reeding $= 25 \times 0.001\,\mathrm{cm}$
4. $= 0.025\,\mathrm{cm}$
5. Diameter $= 0.5 + (0.5 + 25 \times 0.001) \times 0.001$
6. So, $d = 0.529\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Main scale reading: $\mathrm{MSR} = 5\,\mathrm{mm} = 0.5\,\mathrm{cm}$.
2. Circular scale reading: $\mathrm{CSR} = 25 \times 0.001\,\mathrm{cm} = 0.025\,\mathrm{cm}$.
3. Observed reading: $0.5 + 0.025 = 0.525\,\mathrm{cm}$.
4. Correct reading $=$ observed $-$ zero error $= 0.525 - (-0.004) = 0.529\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q044_9c5dc37f_03112026.png?v=9c5dc37f8368)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q044_61bf4c8a_03112026.png?v=61bf4c8a4e77)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A screw-gauge reading is main scale plus circular divisions times least count, and a zero error is subtracted with its own sign, so a negative zero error increases the diameter
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student reads "zero error" as something always taken away and subtracts $0.004$ from the observed $0.525\,\mathrm{cm}$ to get $0.521$; the rule is corrected $=$ observed $-$ (zero error), and with the error $-0.004$ that subtraction adds
- **Why:** This question requires a diameter computed from the two scale readings and then corrected, demonstrated by "If screw gauge has a zero error of $-0.004\,\mathrm{cm}$, the correct diameter of the ball is".
- **Note:** The stem says the circular-scale zero "coincides with 25 divisions above the referene level", which the $0.529\,\mathrm{cm}$ key treats as a reading of 25 divisions; the typo in "referene" is in our record.
<!--/ecat-->

## Q45

Physics · Rotational Motion

The moment of the force, $\vec{F}=4\hat{i}+5\hat{j}-6\hat{k}$ at $(2, 0, -3)$, about the point $(2, -2, -2)$, is given by

- **(1)** $-7\hat{i}-4\hat{j}-8k$
- (2) $-8\hat{i}-4\hat{j}-7\hat{k}$
- (3) $-7\hat{i}-8\hat{j}-4\hat{k}$
- (4) $-4\hat{i}-\hat{j}-8\hat{k}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\overset{\frown}{F} = 4\hat{i} + 5\hat{j} - 6k$
2. $\overset{\frown}{r} = 2\hat{j} - k$
3. Torque $= \overset{\frown}{r} \times \overset{\frown}{F}$
4. $= \begin{vmatrix} \hat{i} & \hat{j} & k \\ 0 & 2 & -1 \\ 4 & 5 & -6 \end{vmatrix}$
5. $\hat{i}(-7) - \hat{j}(4) + k(-8)$

**Solved independently** (answer withheld)

1. Position vector of the point of application relative to the reference point: $\vec{r} = (2-2)\hat{i} + (0-(-2))\hat{j} + (-3-(-2))\hat{k} = 2\hat{j} - \hat{k}$.
2. Torque is $\vec{\tau} = \vec{r} \times \vec{F}$ with $\vec{r} = (0, 2, -1)$ and $\vec{F} = (4, 5, -6)$.
3. $\tau_x = r_y F_z - r_z F_y = (2)(-6) - (-1)(5) = -12 + 5 = -7$.
4. $\tau_y = r_z F_x - r_x F_z = (-1)(4) - (0)(-6) = -4$.
5. $\tau_z = r_x F_y - r_y F_x = (0)(5) - (2)(4) = -8$.
6. $\vec{\tau} = -7\hat{i} - 4\hat{j} - 8\hat{k}$, which is option $1$.

**Subtopic:** Problems on Torque of a Force About the Axis of Rotation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q045_053e8a08_03112026.png?v=053e8a08fd71)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q045_5500fdb9_03112026.png?v=5500fdb9c5e6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Torque about a point is $\vec r \times \vec F$ with $\vec r$ drawn from that point to the point of application
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student works out the three minors $-7$, $-4$, $-8$ and then attaches them to $\hat i$, $\hat j$, $\hat k$ in the reverse order, giving $-8\hat i-4\hat j-7\hat k$; the middle component is unchanged by the reversal, which is why only the first and last swap
- **Why:** This question requires the cross product of a position vector and a force computed component by component, demonstrated by "The moment of the force, $\vec{F}=4\hat{i}+5\hat{j}-6\hat{k}$ at $(2, 0, -3)$, about the point $(2, -2, -2)$".
- **Note:** Option 1 as stored prints the last term as "8k" without the hat; the three components still read $-7$, $-4$, $-8$, so the key is unaffected.
<!--/ecat-->

## Q46

Biology · zoology · Locomotion and Movement

Which of the following hormones can play a significant role in osteoporosis?

- (1) Parathyroid hormone and prolactin
- (2) Aldosterone and Prolactin
- **(3)** Estrogen and parathyroid hormone
- (4) Progesterone and Aldosterone

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Parathyroid hormone and estrogen plays an important role in osteoporosis.
2. Parathyroid hormone maintains the calcium level by stimulating both resorption and formation of bone.
3. Estrogen inhibit bone resorption.

**Solved independently** (answer withheld)

1. Osteoporosis is an age-related disorder of reduced bone mass; decreased levels of $\text{estrogen}$ are a common cause, and $\text{PTH}$ promotes bone resorption (demineralisation), so the pair Estrogen and parathyroid hormone is option $3$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q046_c39fd0ea_03112026.png?v=c39fd0ea1a3b)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q046_35c81302_03112026.png?v=35c81302365f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Osteoporosis is tied to two hormones: falling estrogen after menopause, and parathyroid hormone, which dissolves calcium out of bone
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Parathyroid hormone is the calcium hormone of the chapter, so a student who spots it in an option stops checking and accepts prolactin alongside it; prolactin's stated job is mammary growth and milk production, which the chapter never links to bone loss
- **Why:** This question requires two stated hormone-to-disorder facts at once, demonstrated by each option being a pair of hormones -- "Estrogen and parathyroid hormone" -- of which both halves must hold.
- **Note:** The pattern classifier recorded plain_mcq, but each option is a PAIR of hormones accepted or rejected whole, which is the printed shape pair_options; the retired-value map in config/allowed_values.yaml sends pair_options to qtype statements, which is what is recorded here.
<!--/ecat-->

## Q47

Biology · zoology · Chemical Coordination and Integration

Which of the following is an amino acid derived hormone?

- (1) Estriol
- **(2)** Epinephrine
- (3) Estradiol
- (4) Ecdysone

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Epinephrine is an amino acid derivative hormone.
2. Estradiol, ecdysone and estriol are steroidal in nature.

**Solved independently** (answer withheld)

1. Estriol and estradiol are oestrogens, i.e. steroid hormones derived from cholesterol, so options $1$ and $3$ are ruled out.
2. Ecdysone is the insect moulting hormone, also a steroid, so option $4$ is ruled out.
3. Epinephrine (adrenaline) is a catecholamine made from the amino acid tyrosine, so it is amino acid derived, which is option $2$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q047_d8bb94b8_03112026.png?v=d8bb94b8e79c)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q047_aba27c0e_03112026.png?v=aba27c0eaacd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hormones are classified by chemical nature, and epinephrine is the chapter's own example of an amino-acid-derived hormone, while the estrogens and ecdysone are steroids
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Estriol and Estradiol are both estrogens and both steroids, so neither can be the single intended answer and each rules the other out on sight; ecdysone is a steroid as well, so all three distractors fall into one chemical class together and no single one is reachable by a route the other two do not share. The chapter's classification of hormones names epinephrine as the amino-acid derivative outright, so the question stands or falls on one printed line with no option set up to catch a student who has it.
- **Why:** This question requires one stated classification fact, demonstrated by the stem asking which hormone is "amino acid derived" with four hormone names as the options and no criterion printed to apply.
<!--/ecat-->

## Q48

Biology · zoology · Neural Control and Coordination

Which of the following structures or regions is incorrectly paired with its function?

- (1) Corpus callosum : band of fibers connecting left and right cerebral hemispheres
- (2) Medulla oblongata: Controls respiration and cardiovascular reflexes
- (3) Hypothalamus: Production of releasing hormones and regulation of temperature, hunger and thirst.
- (4) Limbic system: Consists of fibre tracts that interconnect different regions of brain; controls movement.

**Answer** — booklet: (none) · independent solve: (4) · unchecked

**Publisher's solution**

1. Limbic system is emotional brain.
2. It controls all emotions in our body but not movements.

**Solved independently** (answer withheld)

1. Corpus callosum is the band of nerve fibres connecting the left and right cerebral hemispheres, and the medulla oblongata controls respiration and cardiovascular reflexes, so options $1$ and $2$ are correct.
2. The hypothalamus produces releasing hormones and regulates body temperature, hunger and thirst, so option $3$ is correct.
3. The limbic system (amygdala, hippocampus, etc.) regulates sexual behaviour, emotional reactions and motivation, not movement via interconnecting fibre tracts, so option $4$ is the incorrect pairing.

**Subtopic:** Forebrain · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q048_7a828500_03112026.png?v=7a8285007a99)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q048_e2435c43_03112026.png?v=e2435c43b3e4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named brain region has one stated function: the corpus callosum connects the two hemispheres, the medulla runs respiration and cardiovascular reflexes, the hypothalamus makes releasing hormones and regulates temperature, hunger and thirst, and the limbic system governs emotion and sexual behaviour
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The record carries no answer for this question: correct_answer is null, accepted_answers is empty and answer_line_as_printed is null. Writing a trap means naming a wrong option, and with no key stored there is no way to be sure the option I would name is not the one the paper awarded, which is the one thing this step must never do
- **Why:** This question requires the stated function of each named region, demonstrated by every option being a region joined to a function -- "Medulla oblongata: Controls respiration and cardiovascular reflexes".
- **Note:** No key is stored for this question, so no option can be judged. For the reviewer who holds the printed answer: the printed content points at option 4, which gives the limbic system "fibre tracts that interconnect different regions of brain; controls movement" -- a description of fibre tracts rather than of the limbic ring, whose stated role is emotion and sexual behaviour. If that is the key, the device to check is that the sentence is a true description of something else in the same chapter, which would make the pull the neighbouring structure rather than the function. Nothing is recorded here until the answer line is supplied.
<!--/ecat-->

## Q49

Biology · zoology · Neural Control and Coordination

The transparent lens in the human eye is held in its place by.

- (1) smooth muscles attached to the ciliary body
- (2) Ligaments attached to the ciliary body
- (3) Smooth muscles attached to the iris
- (4) Ligaments attached to the iris

**Answer** — booklet: (none) · independent solve: (2) · unchecked

**Publisher's solution**

1. Lens in the human eye is held in its place by suspensory ligaments attached to the ciliary body.
2. Eye lens is held in place by suspending ligaments to ciliary muscles.

**Solved independently** (answer withheld)

1. The transparent crystalline lens is held in place by suspensory ligaments (zonule fibres) attached to the ciliary body, which is option $2$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q049_1e3e5511_03112026.png?v=1e3e5511b004)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q049_f0e39fa8_03112026.png?v=f0e39fa8df07)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The lens of the eye is slung in place by ligaments running to the ciliary body, while the ciliary muscle only changes its curvature
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The record carries no answer for this question: correct_answer is null, accepted_answers is empty and answer_line_as_printed is null. The four options cross two attachments, muscles against ligaments, with two anchors, ciliary body against iris, so naming a trap means naming three of the four cells of that grid as wrong, and with no key stored one of them could be the awarded option
- **Why:** This question requires one stated anatomical fact, demonstrated by the options crossing "smooth muscles" against "Ligaments" with "the ciliary body" against "the iris".
- **Note:** No key is stored for this question, so no option can be judged. For the reviewer who holds the printed answer: the anatomy points at option 2, since the lens hangs from the ciliary body by suspensory ligaments while the ciliary smooth muscle alters the lens's curvature rather than holding it. If that is the key, the device to check is the two-by-two layout -- one wrong attachment, one wrong anchor -- so that a student who has only half the fact right still finds a printed option. Nothing is recorded here until the answer line is supplied.
<!--/ecat-->

## Q50

Biology · zoology · Human Reproduction

The amnion of mammalian embryo is derived from

- (1) ectoderm and endoderm
- **(2)** ectoderm and mesoderm
- (3) mesoderm and trophoblast
- (4) endoderm and mesoderm

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The amnion arises from extra-embryonic somatic mesoderm on the outer side and the extra-embryonic ectoderm on the inner side.

**Solved independently** (answer withheld)

1. The amnion is an extraembryonic membrane formed from the somatopleure, which is extraembryonic ectoderm plus the somatic layer of extraembryonic mesoderm, so it is derived from ectoderm and mesoderm: option $2$.

**Subtopic:** Implantation and Embryonic Development · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q050_3f7e1116_03112026.png?v=3f7e11161f4d)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q050_b4552ae9_03112026.png?v=b4552ae95723)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The amnion is built from two layers, an inner lining of ectoderm and an outer sheet of extra-embryonic mesoderm, with the endoderm going to the gut and the yolk sac instead
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  A student rebuilding the answer instead of recalling it reads endo- as the inner layer, and the amniotic cavity is the inner cavity, so endoderm is written where the chapter has ectoderm; replace endoderm with a name that does not look like ectoderm and the pull disappears, which is the test that makes this a likeness trap rather than a position one
- **Why:** This question requires two stated facts at once about one structure's origin, demonstrated by each option being a pair of germ layers -- "ectoderm and mesoderm" -- of which both halves must hold.
- **Note:** The pattern classifier recorded plain_mcq, but each option is a PAIR of germ layers accepted or rejected whole, which is the printed shape pair_options; the retired-value map in config/allowed_values.yaml sends pair_options to qtype statements, which is what is recorded here.
<!--/ecat-->

## Q51

Biology · zoology · Human Reproduction

Hormones secreted by the placenta to maintain pregnancy are

- (1) hCG, progestogens, estrogens, glucocorticoids
- (2) hCG, Hpl, progestogens, estrogens
- **(3)** hCG, hPL, progestogens, estrogens
- (4) hCG, Hpl, estrogens, relaxin, oxytocin

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Human chorionic gonadotropin (HCG), estrogen, progesterone and human placental lactogen (hPL) are the 4 major hormones secreted by placenta.

**Solved independently** (answer withheld)

1. The placenta acts as an endocrine tissue and secretes $\text{hCG}$, $\text{hPL}$, estrogens and progestogens.
2. Option $1$ includes glucocorticoids, which come from the adrenal cortex, so it is wrong.
3. Option $4$ includes oxytocin, which comes from the posterior pituitary, so it is wrong.
4. Option $3$ lists $\text{hCG}$, $\text{hPL}$, progestogens and estrogens, which matches; option $2$ is the same set with 'Hpl', so option $3$ is chosen.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q051_6b060b28_03112026.png?v=6b060b2819ae)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q051_17d36b7c_03112026.png?v=17d36b7c412b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The placenta is an endocrine organ, and the hormones the chapter lists for it are hCG, hPL, progestogens and estrogens
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Options 2 and 3 as stored hold the same four hormones in the same order and differ only in how hPL is capitalised -- "hCG, Hpl, progestogens, estrogens" against "hCG, hPL, progestogens, estrogens" -- with option 3 keyed. A printed paper does not offer the same answer twice, so one of the two has been mis-transcribed, and any trap I named would rest on an option set that misleads for a reason the paper never intended
- **Why:** This question requires one stated list recalled whole, demonstrated by each option being a set of hormones -- "hCG, hPL, progestogens, estrogens" -- accepted or rejected together.
- **Note:** Duplicated option: 2 and 3 carry the identical hormone list and differ only in the capitalisation of hPL, which is the case §5a names as source_damage_artifact. A repair task should re-read options 2 and 3 against the printed paper. The two genuine distractors are visible and worth checking once it is repaired: option 1 adds glucocorticoids to the list, and option 4 drops progestogens and adds relaxin and oxytocin, both of which are hormones of pregnancy from elsewhere rather than from the placenta. The qtype note for this group applies here too -- the options are sets judged whole.
<!--/ecat-->

## Q52

Biology · zoology · Reproductive Health

The contraceptive ‘SAHELI’

- (1) is a post – coital contraceptive
- **(2)** blocks estrogen receptors in the uterus, preventing eggs from getting implanted
- (3) is an IUD.
- (4) increases the concentration of estrogen and prevents ovulation in females.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. SAHELI is a non-hormonal contraceptive birth control pill.
2. It prevents the implantation by blocking the estrogen receptors in the uterus.

**Solved independently** (answer withheld)

1. Saheli is the oral contraceptive for females containing a non-steroidal preparation (centchroman), taken once a week.
2. Being an oral pill, it is not an IUD (option $3$), and being a regular weekly pill it is not a post-coital (emergency) contraceptive (option $1$).
3. Being non-steroidal, it does not raise estrogen concentration (option $4$); it acts as an anti-estrogen by blocking estrogen receptors in the uterus, preventing implantation, which is option $2$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q052_2b08de71_03112026.png?v=2b08de71f014)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q052_034ed1e0_03112026.png?v=034ed1e074a6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Saheli is a non-steroidal once-a-week pill that blocks estrogen receptors in the uterus so a fertilised egg cannot implant, rather than suppressing ovulation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Saheli is an oral pill, and the mode of action the chapter states for oral contraceptive pills is inhibition of ovulation, so a student who carries the pill paragraph's general mechanism applies it to the one named pill.
- **Why:** This question requires the stated mode of action of one named contraceptive, demonstrated by the option "blocks estrogen receptors in the uterus, preventing eggs from getting implanted" standing against three rival descriptions of the same named pill.
<!--/ecat-->

## Q53

Biology · zoology · Human Reproduction

The difference between spermiogenesis and spermiation is

- **(1)** In spermiogenesis spermatozoa are formed, while in spermiation spermiation spermatozoa are released from sertoli cells into the cavity of seminiferous tubules.
- (2) In spermogenesis spermatids are formed, while in spermiation spermatozoa are formed.
- (3) in spermiogenesis spermatozoa from sertoli cells are released into the cavity of seminiferous tubules, while in spermiation spermatozoa are formed.
- (4) In spermiogenesis spermatozoa are formed, while in spermiation spermatids are formed.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In spermiogenesis, spermatids form motile spermatozoa.
2. Spermiation is a process in which mature spermatids are released from Sertoli cells into the seminiferous tubules.

**Solved independently** (answer withheld)

1. Spermiogenesis is the transformation of spermatids into spermatozoa, and spermiation is the release of spermatozoa from Sertoli cells into the cavity of the seminiferous tubules, which matches option $1$.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q053_0f387ca1_03112026.png?v=0f387ca1c3c2)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q053_bfd12bf3_03112026.png?v=bfd12bf38e72)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Spermiogenesis is the reshaping of spermatids into spermatozoa; spermiation is the later release of those spermatozoa from the Sertoli cells into the lumen of the seminiferous tubule
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The option opens with the key's first half word for word, so a student who checks only that spermiogenesis makes spermatozoa accepts it and then reads 'spermatids' in the second half as the other cell name in the same series.
- **Why:** This question requires holding two neighbouring stages of sperm production apart, demonstrated by the stem "The difference between spermiogenesis and spermiation is" and by option 4 repeating the key's first half word for word so that only the second half decides.
- **Note:** E1 called this statement_options from option length. The current qtype vocabulary reserves statements for lettered statements whose answer is a combination, which this is not, so the shape recorded is mcq. Option 1 as stored repeats the word "spermiation" and option 2 prints "spermogenesis"; both are recorded as printed and neither affects which option the key names.
<!--/ecat-->

## Q54

Biology · zoology · Principles of Inheritance and Variation

A woman has an X-linked condition on one of her X chromosomes. This chromosomes can be inherited by

- **(1)** Both sons and daughters
- (2) Only daughters
- (3) Only grandchildren
- (4) Only sons

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. As mother has X linked condition on 1 chromosome, both sons and daughter will inherit.
2. Son will be diseased and daughters will be carrier if the father is normal.

**Solved independently** (answer withheld)

1. Every child, son or daughter, receives one of the mother's two X chromosomes, so the X carrying the condition ($X'$) is passed on with probability $\frac{1}{2}$ to each child, whether son or daughter: option $1$.

**Subtopic:** Sex Determination in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q054_30ce1bb0_03112026.png?v=30ce1bb0402d)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q054_57bda9f8_03112026.png?v=57bda9f8b57d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A mother passes one of her two X chromosomes to every child, so an X-linked allele she carries can reach a son or a daughter; which of them shows the condition is a separate question
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The pedigrees for haemophilia and colour blindness show a carrier mother's sons as the affected ones, so a student holding that answers who manifests the condition rather than who receives the chromosome.
- **Why:** This question requires the rule of maternal X transmission applied to a stated case, demonstrated by the stem's "a woman has an X-linked condition on one of her X chromosomes" and options that partition the children by sex.
<!--/ecat-->

## Q55

Biology · zoology · Evolution

According to Hugo de Vries, the mechanism of evaluation is

- (1) Minor mutations
- (2) Multiple step mutations
- (3) Phenotypic variations
- **(4)** Saltation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. According to Hugo de vries, the mechanism of evolution is saltation or single step large mutation.

**Solved independently** (answer withheld)

1. Hugo de Vries, working on $\textit{Oenothera lamarckiana}$, proposed that large single-step mutations, not small directional variations, cause speciation; he called this saltation, which is option $4$.

**Subtopic:** Mechanism of Evolution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q055_403cc9b7_03112026.png?v=403cc9b7f4f5)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q055_9e17f1bf_03112026.png?v=9e17f1bff172)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hugo de Vries called his mechanism saltation: a single-step large mutation that makes a new species at once, as against Darwin's small gradual variations
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The gloss stored with the term is 'single step large mutation', and a student who has kept the word 'step' but not the word 'single' takes the option that prints 'step' with the count changed.
- **Why:** This question requires the term NCERT attaches to de Vries's mechanism, demonstrated by the stem "According to Hugo de Vries, the mechanism of evaluation is" with one technical term, saltation, among three descriptive phrases.
- **Note:** The stem prints "mechanism of evaluation" where evolution is meant; tagged as printed. The device on option 2 is a remembered phrase with one word changed, which the retired E5 vocabulary called single_word_substitution and which config/allowed_values.yaml maps forward onto nearby_fact; that is the label used.
<!--/ecat-->

## Q56

Biology · both · Molecular Basis of Inheritance

All of the following are part of an operon except

- (1) a promoter
- (2) an operator
- **(3)** an enhancer
- (4) structural genes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Enhancer are not a part of operon.
2. It is a short region of DNA hat can be bound by proteins (activators) to increase the likelihood that transcription of a particular gene will occur.

**Solved independently** (answer withheld)

1. An operon (as in the $lac$ operon) consists of a promoter, an operator and structural genes, with a regulator gene coding for the repressor.
2. An enhancer is a eukaryotic regulatory DNA sequence and is not a component of an operon, so the exception is option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q056_fdef71af_03112026.png?v=fdef71af669b)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q056_148b87a2_03112026.png?v=148b87a2c78f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An operon is a promoter, an operator and the structural genes they control; the enhancer is a eukaryotic regulatory element and has no place in it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Reading the stem as asking which component belongs turns the question round, and the operator is the component the operon is named after, so it is the one that confirms fastest.
- **Why:** This question requires the stated components of an operon, demonstrated by the stem "All of the following are part of an operon except" set against three genuine components and one eukaryotic element.
<!--/ecat-->

## Q57

Biology · both · Molecular Basis of Inheritance

AGGTATCGCAT is a sequence from the coding strand of a gene. What will be the corresponding sequence of the transcribed mRNA?

- (1) UCCAUAGCGUA
- **(2)** AGGUAUCGCAU
- (3) ACCUAUGCGAU
- (4) UGGTUTCGCAT

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Coding strand and mRNA has same nucleotide sequence except, ‘T’ – Thymine is replaced by ‘U’–Uracil in mRNA.

**Solved independently** (answer withheld)

1. The template strand is transcribed, so the mRNA is complementary to the template and has the same sequence as the coding strand.
2. Replace every $\mathrm{T}$ with $\mathrm{U}$: $\mathrm{AGGTATCGCAT} \rightarrow \mathrm{AGGUAUCGCAU}$, which is option $2$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q057_6bb5d8a3_03112026.png?v=6bb5d8a32470)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q057_32a1780b_03112026.png?v=32a1780b689e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An mRNA copies the coding strand letter for letter with uracil in place of thymine, because it is built against the template strand that is complementary to both
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Holding 'mRNA is complementary to the DNA' and complementing the printed letters gives UCCAUAGCGUA exactly; the stem's word 'coding' is what makes complementing the wrong move here.
- **Why:** This question requires the transcription convention applied to a given sequence, demonstrated by the stem's "from the coding strand of a gene" and by option 1 printing the exact complement of that strand.
- **Note:** E1 called this arrange_in_order, the pattern firing on the word "sequence"; nothing is put in order here and the shape recorded is mcq.
<!--/ecat-->

## Q58

Biology · zoology · Human Reproduction

Match the items given in the Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Proliferative Phase | i | Breakdown of endometrical lining |
| b | Secretory Phase | ii | Follicular phase |
| c | Menstruation | iii | Luteal Phase |

- (1) iii i ii
- (2) iii ii i
- **(3)** ii iii i
- (4) i iii ii

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Proliferative phase is also known as follicular phase.
2. Breakdown of endometrial lining is menstruation, and secretory phase is luteal phase.

**Solved independently** (answer withheld)

1. The proliferative phase of the uterine cycle, when the endometrium regenerates under oestrogen from growing follicles, coincides with the ovarian follicular phase: $a \rightarrow ii$.
2. The secretory phase, when the endometrium is maintained by progesterone from the corpus luteum, coincides with the luteal phase: $b \rightarrow iii$.
3. Menstruation is the breakdown and shedding of the endometrial lining: $c \rightarrow i$.
4. The sequence $a$-$ii$, $b$-$iii$, $c$-$i$ reads 'ii iii i', which is option $3$.

**Subtopic:** Menstrual Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q058_fedccdff_03112026.png?v=fedccdff06f2)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q058_909578b9_03112026.png?v=909578b98960)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The uterine phases of the menstrual cycle run alongside the ovarian ones: the proliferative phase is the follicular phase, the secretory phase is the luteal phase, and menstruation is the breakdown of the endometrial lining
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Progesterone from the corpus luteum is the hormone taught as building up and holding the endometrium, so a student attaches the word proliferative to the luteal phase; menstruation stays correctly on the breakdown of the lining, which is what makes the rest of the option look settled
- **Why:** This question requires the stated equivalence between the uterine and the ovarian names for each phase, demonstrated by Column II holding "Follicular phase" and "Luteal Phase" against Column I's "Proliferative Phase" and "Secretory Phase".
<!--/ecat-->

## Q59

Biology · zoology · Human Health and Disease

In which disease does mosquito transmitted pathogen cause chronic inflammation of lymphatic vessels?

- (1) Amoebiasis
- **(2)** Elephantiasis
- (3) Ringworm disease
- (4) Ascariasis

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Elephantiasis or filariasis is the mosquito transmitted disease that causes chronic inflammation to lymphatic vessels.

**Solved independently** (answer withheld)

1. Elephantiasis (filariasis) is caused by the filarial worms $Wuchereria$ ($W.\ bancrofti$, $W.\ malayi$), which the female $Culex$ mosquito carries; they cause chronic inflammation of the lymphatic vessels of the lower limbs, so the answer is option $2$. The other options are not mosquito-borne: amoebiasis, ringworm and ascariasis spread by contaminated food and water, houseflies or contact.

**Subtopic:** Filarial Diseases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q059_0c495d23_03112026.png?v=0c495d237ca8)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q059_2a7861c4_03112026.png?v=2a7861c4bdae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Wuchereria, the filarial worm carried by mosquitoes, lodges in the lymphatic vessels and inflames them for years, which is elephantiasis
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Ascaris is the worm the chapter describes at length in the paragraph just before the filarial worms, so a student who has stored the two helminth diseases as one block reaches for the one described first.
- **Why:** This question requires the stated link between a vector, a pathogen and the organ it damages, demonstrated by the stem's "chronic inflammation of lymphatic vessels" and four named diseases.
<!--/ecat-->

## Q60

Biology · zoology · Evolution

Among the following sets of examples for divergent evolution, select the incorrect option:

- **(1)** Eye of octopus, bat and man
- (2) Forelimbs of man, bat and cheetah
- (3) Brain of bat, man and cheetah
- (4) Heart of bat, man and cheetah

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Eye of octopus, mammal are formed due to convergent evolution.

**Solved independently** (answer withheld)

1. Divergent evolution produces $\text{homologous}$ organs: the same basic structure from a common ancestor, adapted to different needs.
2. Forelimbs, brain and heart of bat, man and cheetah (all mammals) share a common vertebrate origin, so options $2$, $3$ and $4$ are homologous, i.e. valid divergent-evolution examples.
3. The octopus eye (mollusc) and the mammalian eye (bat, man) have different origins but similar function, so they are $\text{analogous}$ organs from convergent evolution.
4. Hence the incorrect set for divergent evolution is option $1$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q060_e8bd1dd3_03112026.png?v=e8bd1dd3a23e)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q060_bffb73c8_03112026.png?v=bffb73c85eda)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Divergent evolution shows up as homologous organs inherited from a common ancestor; the octopus eye and the mammalian eye arrive at the same design without that shared ancestry, so they are analogous
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Read without the word 'incorrect' the stem asks for an example of divergent evolution, and the forelimbs of man, bat and cheetah are the textbook's own illustration of it.
- **Why:** This question requires the taught assignment of example sets to homology or analogy, demonstrated by the stem's "sets of examples for divergent evolution, select the incorrect option" and by option 1 being the one set that reaches outside the mammals, to the octopus.
- **Note:** The printed shape is four sets of items accepted or rejected whole, which the codebook's retired E1 list calls pair_options; the live qtype vocabulary reserves statements for lettered statements answered by a combination, so mcq is recorded. E1's own statement_options came from option length. Options 3 and 4 are reachable on a strict 'same structure, different function' reading of homology, which is the route recorded against them; the key is not affected, since homology turns on common ancestry.
<!--/ecat-->

## Q61

Biology · zoology · Evolution

The similarity of bone structure in the forelimbs of many vertebrates is an example of

- (1) Adaptive radiation
- **(2)** Homology
- (3) Convergent evolution
- (4) Analogy

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Homologous structures have same ancestors but the structures will have different functions.

**Solved independently** (answer withheld)

1. Forelimbs of whales, bats, cheetahs and humans share the same bone pattern (humerus, radius-ulna, carpals, metacarpals, phalanges) inherited from a common ancestor while doing different jobs; structures with the same origin and plan but different functions are homologous, so the answer is Homology, option $2$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q061_c8603446_03112026.png?v=c8603446bfbf)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q061_f4a7c856_03112026.png?v=f4a7c8565ee7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homology is one inherited bone plan under forelimbs doing different jobs, and it marks common ancestry rather than a shared way of life
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The stem's word is 'similarity', and analogy is the member of the homology-analogy pair that a student files under similarity, so the paired term is taken instead of the right one.
- **Why:** This question requires the term the book attaches to this case, demonstrated by the stem's "similarity of bone structure in the forelimbs of many vertebrates" with four named evolutionary terms as the options.
- **Note:** Test applied for the trap label on option 4: analogy does not resemble homology as a word, and replacing it with an unlike phrase carrying the same meaning leaves the pull intact, so it is the paired-concept position doing the work, not the likeness — hence nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q62

Biology · zoology · Human Health and Disease

Which of the following is not an autoimmune disease?

- (1) Vitiligo
- (2) Psoriasis
- **(3)** Alzheimer’s disease
- (4) Rheumatoid arthritis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Alzheimer’s disease is not an autoimmune disease.

**Solved independently** (answer withheld)

1. Vitiligo, psoriasis and rheumatoid arthritis are all autoimmune diseases, while Alzheimer's disease is a neurodegenerative disorder, so the answer is option $3$.

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q062_580830d9_03112026.png?v=580830d94d35)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q062_bba5c0d9_03112026.png?v=bba5c0d99cd9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Autoimmunity is the immune system attacking the body's own tissue, which covers vitiligo, psoriasis and rheumatoid arthritis, while Alzheimer's disease is neurodegenerative
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Drop the 'not' and the stem asks which is an autoimmune disease, and rheumatoid arthritis is the one example the chapter names for autoimmunity.
- **Why:** This question requires the stated classification of named disorders, demonstrated by the stem "Which of the following is not an autoimmune disease?" with three self-attack disorders and one neurodegenerative disease among the options.
<!--/ecat-->

## Q63

Biology · zoology · Principles of Inheritance and Variation

> ⚠ The independent solve chose (4); the booklet prints (2).

Which of the following characteristics represent ‘Inheritance of blood groups’ in humans?

- **(a)** Dominance
- **(b)** Co-dominance
- **(c)** Multiple allele
- **(d)** Incomplete dominance
- **(e)** Polygenic inheritance

- (1) a, c and e
- **(2)** b, c and e
- (3) b, d and e
- (4) a, b and c

**Answer** — booklet: (2) · independent solve: (4) · differs

**Publisher's solution**

1. Inheritance of blood group is an example of co-dominance, polygenic inheritance and multiple alleles.

**Solved independently** (answer withheld)

1. The ABO blood group is controlled by one gene $I$ with three alleles $I^A$, $I^B$ and $i$, so it shows multiple alleles (c).
2. In $I^A I^B$ both antigens are expressed (blood group AB), so $I^A$ and $I^B$ are co-dominant (b).
3. In $I^A i$ and $I^B i$ only A or B is expressed, so $I^A$ and $I^B$ are dominant over $i$ (a).
4. A single gene is involved and no intermediate phenotype arises, so (d) incomplete dominance and (e) polygenic inheritance do not apply.
5. The characteristics are a, b and c, which is option $4$.

**Subtopic:** Incomplete Dominance & Co-dominance, Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q063_d136acf3_03112026.png?v=d136acf32fe4)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q063_9daa2c68_03112026.png?v=9daa2c686356)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** ABO blood groups are inherited at one locus with three alleles, where the two antigen alleles are co-dominant to each other and both are dominant over the third.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stored key names option 2, b, c and e, and item e is polygenic inheritance, which the chapter attaches to skin colour and height rather than to blood groups; the set the subject supports, a, b and c, is printed as option 4, so any route written here would land on the option the chapter backs. Checked all four combinations against the chapter before leaving the trap open.
- **Why:** This question requires the inheritance pattern of one locus to be told apart from its neighbours, demonstrated by 'Co-dominance', 'Incomplete dominance' and 'Polygenic inheritance' all standing in the same lettered list.
- **Note:** Tagged as printed, following the rulebook's rule that the key is not re-judged at this step; the mismatch is recorded in the flag instead, and a reviewer should check the key index and the option order against the printed paper. Once the key is settled, the device to check is option 3, where incomplete dominance stands in for multiple alleles: both are described as neither allele being fully dominant, whereas the AB group shows both antigens together, which is co-dominance.
<!--/ecat-->

## Q64

Biology · botany · Microbes in Human Welfare

Conversion of milk to curd improves its nutritional value by increasing the amount of

- (1) Vitamin E
- (2) Vitamin D
- **(3)** Vitamin B12
- (4) Vitamin A

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Vitamin B12 content is increased when milk is converted into curd.

**Solved independently** (answer withheld)

1. Lactic acid bacteria (LAB) such as $Lactobacillus$ convert milk to curd, and in doing so they increase its vitamin $B_{12}$ content, so the answer is option $3$ (Vitamin B12).

**Subtopic:** Microbes in Household Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q064_847aeb57_03112026.png?v=847aeb57e94c)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q064_c5d83114_03112026.png?v=c5d831147c2b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lactic acid bacteria do more than curdle milk: they synthesise vitamin B12, so curd carries more of it than the milk it was made from
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Vitamin D is the vitamin attached to milk in every nutrition table, so the option answers what milk supplies rather than what fermenting it adds.
- **Why:** This question requires one stated fact about what fermentation adds, demonstrated by the stem's "improves its nutritional value by increasing the amount of" with four vitamins as the options.
<!--/ecat-->

## Q65

Biology · botany · Environmental Issues

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Eutrophication | i | UV-B radiation |
| b | Sanitary landfill | ii | Deforestation |
| c | Snow blindness | iii | Nutrient enrichment |
| d | Jhum cultivation | iv | Waste disposal |

- (1) a-i, b-ii, c-iv, d-iii
- (2) a-ii, b-i, c-iii, d-iv
- **(3)** a-iii, b-iv, c-i, d-ii
- (4) a-i, b-iii, c-iv, d-ii

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Eutrophication is nutrient enrichment.
2. Sanitary landfill is associated with waste disposal.
3. UV-B radiation causes snow blindness.
4. Jhum cultivation is associated with deforestation.

**Solved independently** (answer withheld)

1. Eutrophication is the nutrient enrichment of a water body, so $a \rightarrow iii$.
2. A sanitary landfill is a method of solid waste disposal, so $b \rightarrow iv$.
3. Snow blindness is inflammation of the cornea caused by high doses of UV-B radiation, so $c \rightarrow i$.
4. Jhum (slash-and-burn) cultivation clears forest land, causing deforestation, so $d \rightarrow ii$.
5. The matching $a$-$iii$, $b$-$iv$, $c$-$i$, $d$-$ii$ is option $3$.

**Subtopic:** Water Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q065_c4fc2895_03112026.png?v=c4fc2895dc1e)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q065_7a2e9582_03112026.png?v=7a2e95826e11)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named environmental problem has one stated cause: eutrophication is nutrient enrichment of water, a sanitary landfill is a waste-disposal method, snow blindness is caused by UV-B, and jhum cultivation drives deforestation
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each Column I item is defined in the chapter by its Column II partner -- eutrophication as the nutrient enrichment of a water body, a sanitary landfill as a method of waste disposal, snow blindness as an effect of UV-B, jhum as slash-and-burn deforestation -- and all three distractors move eutrophication off nutrient enrichment, so one definition a prepared student holds strikes out all three at once. I also tested the two readings that could carry someone part of the way, jhum as nutrient enrichment through the ash it leaves and landfill as nutrient enrichment through leachate, and neither reaches a single printed option on its own.
- **Why:** This question requires four stated cause-to-effect facts, demonstrated by Column II holding the defining phrase for each item in Column I -- "Nutrient enrichment" for "Eutrophication", "Waste disposal" for "Sanitary landfill".
<!--/ecat-->

## Q66

Biology · botany · Organisms and Populations

Which one of the following population interactions is widely used in medical science for the production of antibiotics?

- **(1)** Amensalism
- (2) Commensalism
- (3) Parasitism
- (4) Mutualism

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Amensalism/Antibiosis $(0, -)$
2. * Antibiotics are chemicals secreted by one microbial group (eg : Penicillium) which harm other microbes (eg : Staphylococcus)
3. * It has no effect on Penicillium or the organism which produces it.

**Solved independently** (answer withheld)

1. An antibiotic-producing microbe such as $Penicillium$ secretes a chemical that inhibits or kills other microbes (bacteria) while the producer itself gains nothing and is not harmed: an interaction of type $(-,\,0)$, which is amensalism, option $1$.

**Subtopic:** Commensalism and Ammensalism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q066_83d793a8_03112026.png?v=83d793a81eb2)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q066_79929ebb_03112026.png?v=79929ebb6baa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Amensalism is the interaction where one species is harmed and the other is unaffected, which is what a mould's antibiotic does to bacteria
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Amensalism and commensalism differ by two letters and sit in the same table, so a student who has fixed the idea but not the spelling takes the more familiar of the two words.
- **Why:** This question requires the taught definition of one population interaction matched to a named use, demonstrated by the stem's "widely used in medical science for the production of antibiotics" with four interaction names as the options.
- **Note:** Test applied for the trap label: replacing 'commensalism' with an unlike word of the same meaning takes most of the pull away, because what carries the student is the near-identical spelling of the two words, so look_alike_term wins over nearby_fact even though both terms also sit in the same table.
<!--/ecat-->

## Q67

Biology · botany · Biodiversity and Conservation

All of the following are included in ‘Ex-situconservation’ except

- (1) Seed banks
- (2) Wildlife safari parks
- (3) Botanical gardens
- **(4)** Sacred groves

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sacred grooves are an example of in-situ conservation.

**Solved independently** (answer withheld)

1. Ex-situ conservation protects organisms outside their natural habitat, e.g. seed banks, wildlife safari parks and botanical gardens, while sacred groves are forest patches protected in their natural setting (in-situ), so the exception is option $4$.

**Subtopic:** Ex Situ Conservation, In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q067_eba4e971_03112026.png?v=eba4e9711e27)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q067_74272df0_03112026.png?v=74272df0745c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex situ conservation keeps organisms away from their habitat - seed banks, botanical gardens, zoological and safari parks - while a sacred grove protects them where they already stand
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  The in-situ names a student carries are 'national parks' and 'wildlife sanctuaries', and 'Wildlife safari parks' reads as one of those two, so an off-site collection gets filed as on-site protection and becomes the exception.
- **Why:** This question requires the stated membership of NCERT's ex-situ list, demonstrated by the stem 'All of the following are included in ‘Ex-situconservation’ except' standing over four named conservation facilities with no criterion printed to apply.
- **Note:** Likeness-against-position test applied to option 2: replace 'Wildlife safari parks' with an unlike phrase such as 'gene bank' and the pull dies, because it is the shared words 'wildlife' and 'park' that carry the student, so look_alike_term rather than nearby_fact. Stem as stored has a lost space in 'Ex-situconservation'; it does not change the task.
<!--/ecat-->

## Q68

Biology · botany · Organisms and Populations

> ⚠ The independent solve chose (2); the booklet prints (1).

In a growing population of a country,

- **(1)** Pre-reproductive individuals are less than reproductive individuals
- (2) Pre-productive individuals are more than the reproductive individuals
- (3) reproductive individuals and pre- reproductive individuals are equal in number
- (4) reproductive individuals are less than the post- reproductive individuals.

**Answer** — booklet: (1) · independent solve: (2) · differs

**Publisher's solution**

1. For a growing population, pre-reproductive individuals are always less than the reproductive individuals.

**Solved independently** (answer withheld)

1. In a growing population the age pyramid is triangular with a broad base, so pre-reproductive individuals are more than reproductive individuals, which is option $2$.

**Subtopic:** Life History Variation and Population Attributes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q068_8f548dfc_03112026.png?v=8f548dfc4820)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q068_58ed7365_03112026.png?v=58ed7365bec0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A growing population has a broad-based age pyramid - more pre-reproductive individuals than reproductive ones
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stored key against the printed options: the key index selects option 1, 'Pre-reproductive individuals are less than reproductive individuals', while the growing-population age pyramid is the broad-based one, which is what option 2 states. The key index and this option order cannot both be as printed, so no wrong option can be named until the printed paper is consulted.
- **Why:** This question requires the age-pyramid shape NCERT gives for a growing population, demonstrated by the stem 'In a growing population of a country,' completed by four rival comparisons of the pre-reproductive and reproductive classes.
- **Note:** Key/option mismatch in our record, not a judgement on the paper: the stem's fact is the broad-based pyramid of a growing population, which option 2 carries, while the stored key points at option 1. The key is not re-judged here - a reviewer should check the printed option order for Q68 before any trap is written. Option 2 also prints 'Pre-productive' for 'Pre-reproductive'.
<!--/ecat-->

## Q69

Biology · zoology · Human Health and Disease

> ⚠ The independent solve chose (4); the booklet prints (2).

Which part of poppy plant is used to obtain the drug “Smack”?

- (1) Leaves
- **(2)** Flowers
- (3) Roots
- (4) Latex

**Answer** — booklet: (2) · independent solve: (4) · differs

**Publisher's solution**

1. Poppy flowers produce a milky fluid which works as a source of raw opium.
2. This will produce smack.

**Solved independently** (answer withheld)

1. Smack is heroin, i.e. diacetylmorphine, made by acetylation of morphine; morphine is extracted from the latex of the poppy plant $Papaver\ somniferum$, so the answer is option $4$ (Latex).

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q069_7341aaaf_03112026.png?v=7341aaafda8d)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q069_90767eba_03112026.png?v=90767eba70ae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Smack is heroin, acetylated morphine drawn from the latex of the opium poppy
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stored key against the printed options: the key index selects option 2, 'Flowers', while the part of the poppy that yields morphine and hence smack is the latex, printed here as option 4. With the key index and the option order in conflict, no wrong option can be named without the printed paper.
- **Why:** This question requires the plant part NCERT names as the source of the opioid, demonstrated by the stem 'Which part of poppy plant is used to obtain the drug “Smack”?' standing over four plant parts.
- **Note:** Key/option mismatch in our record: the subject answer, latex, is printed as option 4 while the stored key points at option 2. Tagged as printed and the key not re-judged; a reviewer should check the printed option order for Q69 before a trap is written. Had the key resolved to latex, the route to check would be the leaves-and-flowers pull from cannabis preparations, which are taught in the same NCERT paragraph.
<!--/ecat-->

## Q70

Biology · zoology · Digestion and Absorption

Which of the following gastric cells indirectly help in erythropoiesis?

- **(1)** Parietal cells
- (2) Chief cells
- (3) Goblet cells
- (4) Mucous cells

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Parietal cells produce intrinsic factor which is necessary for the absorption of Vitamin B12.
2. Inability to absorb vitamin B12 is associated with ineffective erythropoiesis.

**Solved independently** (answer withheld)

1. Parietal (oxyntic) cells of the gastric glands secrete $\mathrm{HCl}$ and Castle's intrinsic factor.
2. Intrinsic factor is needed to absorb vitamin $B_{12}$, and vitamin $B_{12}$ is needed for erythropoiesis, so parietal cells help indirectly. This is option $1$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q070_74bcffda_03112026.png?v=74bcffdabc7e)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q070_65b55647_03112026.png?v=65b55647843b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parietal cells secrete intrinsic factor along with HCl, and intrinsic factor is what allows vitamin B12 to be absorbed for red-cell formation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Chief cells are the other gastric gland cell printed in the same sentence as parietal cells, so a student who holds 'the stomach matters for vitamin B12' without holding which cell makes intrinsic factor takes the cell they can name a secretion for.
- **Why:** This question requires the stated secretion of one named gastric cell type, demonstrated by the stem 'Which of the following gastric cells indirectly help in erythropoiesis?' standing over four cell names.
- **Note:** Likeness-against-position test applied to option 2: 'chief' does not resemble 'parietal', so the pull is the two cells' place in one printed sentence - nearby_fact.
<!--/ecat-->

## Q71

Biology · zoology · Body Fluids and Circulation

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Fibrinogen | i | Osmotic balance |
| b | Globulin | ii | Blood clotting |
| c | Albumin | iii | Defence mechanism |

- **(1)** a-ii, b-iii, c-i
- (2) a-iii, b-ii, c-i
- (3) a-I, b-iii, c-ii
- (4) a-I, b-ii, c-iii

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Fibrinogen is associated with blood clotting, albumins helps in osmotic balance and globulin are part of defence mechanism.

**Solved independently** (answer withheld)

1. Fibrinogen is needed for blood clotting, so $a \rightarrow ii$; globulins are mainly involved in the body's defence mechanisms, so $b \rightarrow iii$; albumin helps keep the osmotic balance, so $c \rightarrow i$. That gives $a$-$ii$, $b$-$iii$, $c$-$i$, which is option $1$.

**Subtopic:** Blood and Plasma · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q071_9862dfe6_03112026.png?v=9862dfe6675e)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q071_e9e730f3_03112026.png?v=e9e730f35333)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The three major plasma proteins each have one stated job: fibrinogen for clotting, globulins for defence, albumins for osmotic balance
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student secure only on albumin and osmotic balance is left holding clotting and defence for the two proteins the chapter prints side by side, and takes the role printed beside the other one -- clotting for globulin, defence for fibrinogen
- **Why:** This question requires the stated job of each named plasma protein, demonstrated by Column II being three functions -- "Osmotic balance", "Blood clotting", "Defence mechanism" -- one of which the chapter states for each protein.
- **Note:** Options 3 and 4 print Column II's first numeral as a capital "I" rather than the lower-case "i" used elsewhere; the intended pairing is unambiguous and the key is unaffected.
<!--/ecat-->

## Q72

Biology · zoology · Breathing and Exchange of Gases

Which of the following is an occupational respiratory disorder?

- (1) Emphysema
- (2) Anthracis
- (3) Botulism
- **(4)** Silicosis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Silicosis is an occupational lung disorder.
2. Inhalation of silica dust causes silicosis.

**Solved independently** (answer withheld)

1. NCERT calls a respiratory disorder occupational when it comes from long exposure to dust at work, as in grinding or stone-breaking industries, leading to inflammation and fibrosis of the lungs.
2. Silicosis is caused by inhaling silica dust at work, so it fits; emphysema is mainly due to smoking and botulism is bacterial food poisoning, so neither fits. The answer is option $4$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q072_baa4dc04_03112026.png?v=baa4dc043016)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q072_82c8ff3b_03112026.png?v=82c8ff3bbae8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Occupational respiratory disorders are the dust diseases of the workplace - silicosis and asbestosis from grinding and stone-breaking - not the smoking disorders
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Emphysema stands in the respiratory-disorders paragraph immediately before NCERT's occupational-disorders paragraph and is also a disease of something inhaled, so a student reading 'occupational' as 'caused by what you breathe' takes the neighbour.
- **Why:** This question requires the stated membership of NCERT's occupational respiratory disorders, demonstrated by the stem 'Which of the following is an occupational respiratory disorder?' standing over four disorder names.
- **Note:** Two pulls sit on different options here. Option 1's pull survives the likeness test - swap 'emphysema' for an unlike word and its place in the same disorders section still carries the student - so it is nearby_fact and is taken as the question's one trap, because it is grounded in the printed NCERT section. Option 2's pull is the reverse case, a name resembling anthracosis, and is recorded as a second route in other_options.
<!--/ecat-->

## Q73

Biology · zoology · Locomotion and Movement

Calcium is important in skeletal muscle contraction because it

- (1) Prevents the formation of bonds between the myosin cross bridge and the actin filament.
- **(2)** Binds to troponin to remove the masking of active sites on actin myosin
- (3) Detaches the myosin head from the actin filament.
- (4) Activates the myosin ATPase by Binding to it.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Calcium released from sarcoplasmic reticulum causes a displacement of troponin from the active sites on actin where the myosin will bind to form cross bridges for muscle contraction.

**Solved independently** (answer withheld)

1. In a resting fibre, tropomyosin held by troponin masks the myosin-binding active sites on the actin filament.
2. A neural signal releases $\mathrm{Ca^{2+}}$ from the sarcoplasmic reticulum, and $\mathrm{Ca^{2+}}$ binds to a subunit of troponin on the actin filament.
3. This removes the masking of the active sites on actin for myosin, so cross bridges can form. That is option $2$. Option $1$ is the opposite effect, while options $3$ and $4$ describe what ATP does, not $\mathrm{Ca^{2+}}$.

**Subtopic:** Mechanism of Muscle Contraction and Red and White Muscle Fibre · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q073_4453ac79_03112026.png?v=4453ac790180)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q073_e6b0389c_03112026.png?v=e6b0389c36a8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Calcium binds a troponin subunit on the actin filament, unmasking actin's myosin-binding sites so cross bridges can form
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  A student holding 'calcium switches contraction on by binding' and 'the myosin head carries ATPase activity' joins the two and has calcium binding the myosin ATPase; the binding is real, but it happens on troponin out on the actin filament.
- **Why:** This question requires the reason NCERT gives for calcium's role in contraction, demonstrated by the stem 'Calcium is important in skeletal muscle contraction because it' followed by four rival mechanisms.
- **Note:** Option 2 as stored reads 'active sites on actin myosin'; the printed line is the masking of actin's active sites for myosin. That is wording damage in our record and it does not change which option the key names, so the question is tagged normally.
<!--/ecat-->

## Q74

Biology · zoology · Neural Control and Coordination

Nissal bodies are mainly composed of

- **(1)** Free ribosomes and RER
- (2) Proteins and lipids
- (3) Nucleic acids and SER
- (4) DNA and RNA

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Nissl bodies are composed of rough ER and free ribosomes.

**Solved independently** (answer withheld)

1. Nissl's granules, found in the cyton and dendrites of a neuron, are made of free ribosomes and rough endoplasmic reticulum (RER), which is option $1$.

**Subtopic:** Neuron as Structural and Functional Unit of Neural System and Types of Axon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q074_54a0cc65_03112026.png?v=54a0cc65066f)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q074_a213bf29_03112026.png?v=a213bf293661)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nissl granules of the neuron cell body are stacks of rough endoplasmic reticulum with free ribosomes - the cell's protein-making machinery, not a store of nucleic acid
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who holds 'Nissl granules are ribosomes on endoplasmic reticulum' and knows ribosomes are nucleic acid plus protein keeps the nucleic-acid half and supplies the wrong endoplasmic reticulum, smooth for rough.
- **Why:** This question requires the stated composition of a named neuronal structure, demonstrated by the stem 'Nissal bodies are mainly composed of' standing over four component pairs.
- **Note:** half_right is used under rule 2 because the option carries two parts and one of them, 'Nucleic acids', is defensible while 'SER' fails; the pull inside it is the SER/RER likeness, which is named in the route. Stem as stored spells 'Nissal' for Nissl.
<!--/ecat-->

## Q75

Biology · botany · Respiration in Plants

Which of these statements is incorrect?

- **(1)** Oxidative phosphorylation takes place in outer mitochondrial membrane.
- (2) Enzymes of TCA cycle are present in mitochondrial matrix.
- (3) Glycolysis operates as long as it is supplied with NAD that can pick up hydrogen atoms.
- (4) Glycolysis occurs in cytosoal

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Oxidative phosphorylation occurs in inner mitochondrial membrane and not in outer mitochondrial membrane.

**Solved independently** (answer withheld)

1. Oxidative phosphorylation happens at the electron transport system and $F_0F_1$ ATP synthase, which sit in the inner mitochondrial membrane, so statement $1$ is incorrect, while TCA enzymes in the matrix, glycolysis needing $NAD^+$ to accept hydrogen, and glycolysis in the cytosol are all correct; the answer is option $1$.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q075_4e102d11_03112026.png?v=4e102d11c511)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q075_fe4f60b1_03112026.png?v=fe4f60b15382)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Oxidative phosphorylation runs on the inner mitochondrial membrane, where the electron transport chain and ATP synthase sit; the outer membrane carries none of it
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stem is negated, so the three unselected options are the true statements, and I checked each against its printed source: TCA enzymes in the matrix, glycolysis in the cytosol and glycolysis running as long as NAD is available are NCERT's own lines with no word altered, so none of them offers a route to being read as the incorrect statement.
- **Why:** This question requires the stated site of oxidative phosphorylation, demonstrated by the option the key names, 'Oxidative phosphorylation takes place in outer mitochondrial membrane.', against three unaltered true statements.
- **Note:** no_trap is a finding here, not a gap: the catch in this item is the inner-for-outer substitution inside the keyed option, and a substitution inside the correct answer is not a wrong option a route can land on. Three fillers is the structure of a 'which statement is incorrect' item with three verbatim statements.
<!--/ecat-->

## Q76

Biology · both · Cell: The Unit of Life

Select the incorrect match:

- **(1)** Polytene chromosomes -Oocytes amphibians
- (2) Lampbrush chromosomes -Diplotene bivalents
- (3) Submetacentric chromosomes -L-shaped chromosomes
- (4) Allosomes -Sex chromosomes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Lampbrush chromosomes are found in amphibian oocytes.
2. Polytene chromosomes are found in larvae of some dipterans.

**Solved independently** (answer withheld)

1. Polytene chromosomes are found in the salivary glands of dipteran larvae such as $Drosophila$, not in amphibian oocytes; amphibian oocytes carry lampbrush chromosomes, so option $1$ is a wrong match.
2. Lampbrush chromosomes are the diplotene bivalents of oocytes, so option $2$ is correct.
3. A submetacentric chromosome has unequal arms and appears L-shaped at anaphase, so option $3$ is correct.
4. Allosomes are the sex chromosomes, so option $4$ is correct; the incorrect match is option $1$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q076_558c0401_03112026.png?v=558c04016590)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q076_48406189_03112026.png?v=48406189d3eb)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Polytene chromosomes are the giant chromosomes of Drosophila salivary glands, while lampbrush chromosomes are the ones seen in amphibian oocytes at diplotene
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The shape series is taught as one block - metacentric V-shaped, submetacentric L-shaped, acrocentric J-shaped, telocentric rod - and a student whose memory of the block has slipped by one neighbour reads 'Submetacentric - L-shaped' as the mismatch.
- **Why:** This question requires the stated partner of each named chromosome type, demonstrated by the stem 'Select the incorrect match:' over four term-and-feature pairs each accepted or rejected whole.
- **Note:** E1's pattern returned match_the_lists ('4 two lists'), but no two labelled columns and no pairing code are printed: each option is one pair judged whole, which the rulebook calls pair_options, so the shape recorded is two_part. Likeness-against-position test on option 3: 'submetacentric' and 'acrocentric' are told apart by their printed place in the shape series rather than by sounding alike, so nearby_fact.
<!--/ecat-->

## Q77

Biology · zoology · Digestion and Absorption

Which of the following terms describes human dentition?

- (1) Pleurodont, Diphyodont, Heterodont
- (2) Thecodont, Diphyodont, homodont
- (3) Pleurodont, monophyodont, homodont
- **(4)** Thecodont, Diphyodont, Heterodont

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Humans teeth are diphyodont, heterodont and thecodont.

**Solved independently** (answer withheld)

1. Each human tooth is set in a socket of the jaw bone, so the dentition is $\text{thecodont}$, not pleurodont. This rules out options $1$ and $3$.
2. Humans grow two sets of teeth in a lifetime, milk (deciduous) and permanent, so the dentition is $\text{diphyodont}$.
3. Humans have four types of teeth: incisors, canines, premolars and molars. So the dentition is $\text{heterodont}$, not homodont, which rules out option $2$.
4. $\text{Thecodont} + \text{Diphyodont} + \text{Heterodont}$ is option $4$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q077_b2c7c0eb_03112026.png?v=b2c7c0eb9f85)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q077_8d9269f8_03112026.png?v=8d9269f889f5)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Human teeth are thecodont (set in sockets), diphyodont (two sets in a lifetime) and heterodont (four kinds of teeth)
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Two of the three terms are the human ones, and the student supplies 'homodont' for 'heterodont' - the pair that differs only in its first syllable - so a correct thecodont-diphyodont memory still lands on a wrong option.
- **Why:** This question requires the three stated descriptors of human dentition, demonstrated by the stem 'Which of the following terms describes human dentition?' over options that each bundle three terms accepted or rejected together.
- **Note:** E1's pattern returned plain_mcq, but each option is a set of three same-kind terms taken whole - half an option right scores nothing - so the shape recorded is two_part. half_right is used under rule 2 because the option carries three parts and two of them hold; the pull inside it, homodont for heterodont, is named in the route.
<!--/ecat-->

## Q78

Biology · both · Cell: The Unit of Life

Which of the following events does not occur in rough endoplasmic reticulum?

- **(1)** Phospholipid synthesis
- (2) Protein folding
- (3) Cleavage of signal peptide
- (4) Protein glycosylation

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Phospholipid synthesis occur in smooth ER.

**Solved independently** (answer withheld)

1. Ribosomes on the RER make proteins that enter the RER lumen, where the signal peptide is cleaved, the protein is folded and glycosylation begins, so options $2$, $3$ and $4$ occur in RER.
2. NCERT names the smooth ER as the major site of lipid synthesis, so phospholipid synthesis does not occur in RER, which is option $1$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q078_b3a292b5_03112026.png?v=b3a292b5cbdb)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q078_07394a7b_03112026.png?v=07394a7ba51c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Rough ER handles protein traffic - synthesis, folding, signal-peptide cleavage and the first glycosylation - while lipid and phospholipid synthesis belongs to smooth ER
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Glycosylation is printed against the Golgi in the paragraph next to the ER's, so a student who stores 'glycoproteins are made in the Golgi' reads glycosylation as the event that does not belong to rough ER.
- **Why:** This question requires the stated division of labour between rough and smooth ER, demonstrated by the stem 'Which of the following events does not occur in rough endoplasmic reticulum?' with phospholipid synthesis among the options.
- **Note:** Likeness-against-position test on option 4: 'glycosylation' resembles no other option's wording, and what carries the student is the Golgi line printed beside the ER line, so nearby_fact.
<!--/ecat-->

## Q79

Biology · both · Cell: The Unit of Life

Many ribosomes many associate with a single mRNA to form multiple copies of a polypeptide simultaneously. Such strings of ribosomes are temed as

- (1) Nucleosome
- **(2)** Polysome
- (3) Plastidome
- (4) Polyhedral bodies

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Polysomes or polyribosomes are many ribosomes associated with single mRNA to form multiple copies of polypeptide simultaneously.

**Solved independently** (answer withheld)

1. Several ribosomes translating the same mRNA at once form a string called a polyribosome or $\text{polysome}$, which is option $2$.

**Subtopic:** Ribosomes And Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q079_03e6eadf_03112026.png?v=03e6eadf3bf6)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q079_a7837fa5_03112026.png?v=a7837fa51a5a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A string of ribosomes translating one mRNA at once is a polysome, or polyribosome
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Nucleosome is the other '-some' in the chapter and the one taught as a beads-on-string structure, so the stem's own phrase 'strings of ribosomes' lands a student on the string term they already hold.
- **Why:** This question requires the term NCERT gives for many ribosomes on one mRNA, demonstrated by the stem 'Such strings of ribosomes are temed as' over four structure names.
- **Note:** Likeness-against-position test on option 1: replace 'Nucleosome' with an unlike word such as 'centriole' and the pull dies, because the -some ending and the beads-on-string description are what carry the student, so look_alike_term. Option 4's pull is the weaker 'poly-' echo and is recorded as a second route. Stem as stored reads 'temed' for 'termed'.
<!--/ecat-->

## Q80

Biology · botany · Biological Classification

Ciliates differ from all other protozoans in

- **(1)** Having two types of nuclei
- (2) Using flagella for locomotion
- (3) Using pseudopodia for capturing prey
- (4) Having a contractile vacuole for removing excess water

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ciliates differs from other protozoans in having two types of nuclei.
2. eg. Paramoecium have two types of nuclei i.e. macronucleus & micronucleus.

**Solved independently** (answer withheld)

1. Ciliates such as $Paramoecium$ possess two kinds of nuclei (macronucleus and micronucleus), a feature not found in other protozoan groups, so the answer is option $1$; flagella belong to flagellates, pseudopodia to amoeboid protozoans, and contractile vacuoles also occur in $Amoeba$.

**Subtopic:** Protozoans · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q080_3e124e80_03112026.png?v=3e124e80f2ec)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q080_129df7d0_03112026.png?v=129df7d06958)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Ciliates are set apart from the other protozoan groups by carrying two kinds of nucleus; cilia, pseudopodia, flagella and contractile vacuoles are each shared with some other group
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The contractile vacuole is a true ciliate feature and is the one a student can name for Paramecium, but the stem asks for what ciliates do not share, and Amoeba keeps a contractile vacuole too.
- **Why:** This question requires telling the four protozoan groups apart on their features, demonstrated by the stem 'Ciliates differ from all other protozoans in' and by three options that each name a feature a different protozoan group owns.
- **Note:** asks is compare rather than fact_line because the printed task is not to produce one stored feature but to decide which of four features is unshared, which means holding the amoeboid, flagellated, ciliated and sporozoan groups apart; the value is recorded here on an mcq, not on a match item.
<!--/ecat-->

## Q81

Biology · zoology · Animal Kingdom

Identify the vertebrate group of animals characterized by crop and gizzard in its digestive system.

- (1) Osteichthyes
- (2) Amphibja
- **(3)** Aves
- (4) Reptilia

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Crop and gizzard are found in birds. They are the part of the alimentary canal.

**Solved independently** (answer withheld)

1. Birds (class Aves) have a crop that stores food and a gizzard that grinds it, so the answer is option $3$ (Aves).

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q081_b1e0b0a1_03112026.png?v=b1e0b0a111d7)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q081_70e05953_03112026.png?v=70e05953214f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The bird gut carries a crop for storing grain and a muscular gizzard for grinding it
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  I read each of the other three classes' printed descriptions for a crop or a gizzard: the bony-fish, amphibian and reptile accounts name neither, and the only other crop-and-gizzard guts on the syllabus belong to the earthworm and the cockroach, which are invertebrates and are not among the options, so no printed fact reaches any wrong option.
- **Why:** This question requires the stated organs of the bird digestive system, demonstrated by the stem 'Identify the vertebrate group of animals characterized by crop and gizzard in its digestive system.' over four vertebrate class names.
- **Note:** no_trap is a finding, not a gap: unlike q084 and q085 in this group, where the other options carry competing printed lines, here the three non-avian classes have no crop-or-gizzard statement at all, so nothing in the printed material carries a prepared student to them. Option 2 as stored reads 'Amphibja'.
<!--/ecat-->

## Q82

Biology · zoology · Animal Kingdom

Which one of these animals is not a homeotherm?

- (1) Psittacula
- (2) Macropus
- (3) Camelus
- **(4)** Chelone

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Chelone is basically a plant.
2. Rest of them are animals and are homeotherm.

**Solved independently** (answer withheld)

1. Only birds (Aves) and mammals (Mammalia) are homeotherms; reptiles are poikilotherms (cold-blooded).
2. $\textit{Psittacula}$ (parrot) is a bird, $\textit{Macropus}$ (kangaroo) and $\textit{Camelus}$ (camel) are mammals, so all three are homeotherms.
3. $\textit{Chelone}$ (turtle) is a reptile, hence not a homeotherm, which is option $4$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q082_1d13f044_03112026.png?v=1d13f044e754)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q082_15e8818b_03112026.png?v=15e8818bdba9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homeotherms hold a constant core body temperature - birds and mammals do; a reptile such as the turtle Chelone does not
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The camel is the animal the chapter beside this one uses for tolerating desert heat, so a student who stores 'the camel lets its body temperature swing' reads it as the animal that does not hold a constant temperature.
- **Why:** This question requires the stated division of vertebrates into those that hold a constant body temperature and those that do not, demonstrated by the stem 'Which one of these animals is not a homeotherm?' over four genus names.
- **Note:** Likeness-against-position test on option 3: 'Camelus' resembles no other option as a word, and what carries the student is a neighbouring taught fact about the camel's temperature tolerance, so nearby_fact in the sense the rulebook gives it - a fact about an adjacent case carried onto the wrong name.
<!--/ecat-->

## Q83

Biology · zoology · Structural Organisation in Animals

> ⚠ The independent solve chose (unsure); the booklet prints (4).

Which of the following features is used to identify a male cockroach from a female cockroach?

- (1) Presence of anal cerci
- (2) Presence of a boat shaped sternum on the
- (3) $9^{\mathrm{th}}$ abdominal segment
- **(4)** Forewings with darker tegmina

**Answer** — booklet: (4) · independent solve: (unsure) · ai_unsure

**Publisher's solution**

1. Males have caudal or anal styles whereas female cockroach have anal cerci.

**Solved independently** (answer withheld)

1. Anal cerci are found on the $10^{\mathrm{th}}$ segment in both sexes, so option $1$ cannot tell male from female.
2. Forewings formed as tegmina are found in both sexes, so option $4$ cannot tell them apart either.
3. A boat-shaped sternum is a female feature, and it is the $7^{\mathrm{th}}$ sternum, not the $9^{\mathrm{th}}$. So option $2$ (read together with option $3$) is wrong as written.
4. Only males have anal (caudal) styles on the $9^{\mathrm{th}}$ segment. No printed option names them, so no option can be confirmed.

**Subtopic:** Morphology of Cockroach · **Difficulty:** unsure (1 step)

**Printed in the booklet** (page 18)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q083_c8dc2f9e_03112026.png?v=c8dc2f9e2a8a)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q083_93ad0f62_03112026.png?v=93ad0f6204b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Male and female cockroaches are told apart by external features - the anal styles of the male and the boat-shaped sternum of the ninth abdominal segment in the female
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The option set as stored is broken, not merely odd: option 2 ends mid-phrase at 'Presence of a boat shaped sternum on the' and option 3 carries its continuation, '9th abdominal segment', so only three distinct options survive in four slots and one printed option is missing altogether. With an option lost, no wrong option can be named and no route audited.
- **Why:** This question requires the stated external difference between male and female cockroaches, demonstrated by the stem 'Which of the following features is used to identify a male cockroach from a female cockroach?' over features of the abdomen and wings.
- **Note:** Record damage, not a property of the paper: one printed option has been split across slots 2 and 3 of our record and a fourth option has been lost, which is why the earlier step left difficulty_level as 'unsure'. The stored key points at slot 4. A reviewer holding the printed paper should restore the four options and then check the route through the anal cerci, which both sexes carry, against the styles the male alone carries.
<!--/ecat-->

## Q84

Biology · zoology · Animal Kingdom

Which of the following animals does not undergo metamorphosis?

- (1) Starfish
- **(2)** Earthworm
- (3) Moth
- (4) Tunicate

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Earthworm do not undergo metamorphosis.

**Solved independently** (answer withheld)

1. Starfish (echinoderm) has a free-swimming bilaterally symmetrical larva that metamorphoses into the radial adult, moth is holometabolous (larva $\rightarrow$ pupa $\rightarrow$ adult), tunicate has a tadpole larva with retrogressive metamorphosis, while earthworm shows direct development (juveniles hatch from the cocoon with no larval stage), so the answer is option $2$.

**Subtopic:** Phylum – Annelida · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q084_56e1923d_03112026.png?v=56e1923d4c37)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q084_16e9597d_03112026.png?v=16e9597dc33d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Development is direct in the earthworm - no larva - while starfish, moth and tunicate all pass through a larva that metamorphoses
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The tunicate's taught headline is that its larval tail and notochord are lost in the adult, and a student who stores that loss as 'the larva just degenerates' reads the tunicate as the animal with no metamorphosis.
- **Why:** This question requires the stated development type of each named animal, demonstrated by the stem 'Which of the following animals does not undergo metamorphosis?' over four animals from four different phyla.
- **Note:** Likeness-against-position test on option 4: 'Tunicate' resembles none of the other names, and the pull is the taught tunicate line about losing the larval tail, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q85

Biology · botany · Biological Classification

Which of the following organisms are known as chief producers in the oceans?

- (1) Euglenoids
- (2) Dinoflagellates
- (3) Cyanobacteria
- **(4)** Diatoms

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Diatoms are the chief producers in the oceans.
2. They are a type of phytoplankton.

**Solved independently** (answer withheld)

1. Among protists, diatoms (chrysophytes) are photosynthetic plankton that make up most of the ocean's primary production, so they are the chief producers in the oceans: option $4$.

**Subtopic:** Chrysophytes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q085_a79aa186_03112026.png?v=a79aa186e9cd)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q085_3a5ae705_03112026.png?v=3a5ae70548c7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Diatoms are named the chief producers of the oceans; their silica walls and their numbers carry the marine food chain
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Dinoflagellates are printed in the paragraph next to the diatoms' and are marine and photosynthetic too, so a student who holds 'the ocean's producers are in this part of the chapter' without which paragraph takes the neighbour.
- **Why:** This question requires the group NCERT names as the ocean's chief producers, demonstrated by the stem 'Which of the following organisms are known as chief producers in the oceans?' over four photosynthetic groups.
- **Note:** Likeness-against-position test on option 2: 'Dinoflagellates' and 'Diatoms' do not resemble each other beyond a shared initial, and what carries the student is the two groups' adjacency in the printed chapter, so nearby_fact.
<!--/ecat-->

## Q86

Biology · zoology · Breathing and Exchange of Gases

Which of the following options correctly represents the lung ·conditions in asthma and emphysema, respectively?

- (1) Decreased respiratory surface; Inflammation of bronchioles
- **(2)** Inflammation of bronchioles; Decreased respiratory surface
- (3) Increased respiratory surface; Inflammation of bronchioles
- (4) Increased number of bronchioles; Increased respiratory surface

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Asthma is a difficulty in breathing causing wheezing due to inflammation of bronchi and bronchioles.
2. Emphysema is a chronic disorder in which alveolar walls are damaged due to which respiratory surface is decreased.

**Solved independently** (answer withheld)

1. Asthma is difficulty in breathing caused by $\text{inflammation of the bronchi and bronchioles}$.
2. Emphysema is a chronic disorder in which the alveolar walls are damaged, so the $\text{respiratory surface decreases}$.
3. Matching the order (asthma; emphysema) gives "Inflammation of bronchioles; Decreased respiratory surface", which is option $2$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q086_bab2bd06_03112026.png?v=bab2bd068636)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q086_0fb681e3_03112026.png?v=0fb681e39f8d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Asthma is inflammation of the bronchioles with difficulty in breathing; emphysema is the breakdown of alveolar walls, which cuts the surface available for exchange
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Both halves are the right facts and only their order fails: a student who attaches the first clause to the disorder they recall first, emphysema with its broken alveolar walls, reads the stem's order backwards.
- **Why:** This question requires the stated lung condition in each of two named disorders, demonstrated by the stem 'the lung conditions in asthma and emphysema, respectively' with options that pair two conditions in order.
- **Note:** E1's pattern returned statement_options, but each option carries two clauses answered together under the stem's 'respectively', and half an option right scores nothing, so the shape recorded is two_part. The option set is laid out as increase against decrease, which is why both fillers fail on a direction no printed line supplies.
<!--/ecat-->

## Q87

Biology · zoology · Body Fluids and Circulation

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Tricuspid valve | i | Between left atrium and left ventricle |
| b | Bicuspid valve | ii | Between right ventricle and pulmonary artery |
| c | Semilunar valve | iii | Between right atrium and right ventricle |

- (1) a-ii, b-i, c-iii
- **(2)** a-iii, b-i, c-ii
- (3) a-i, b-ii, c-iii
- (4) a-i, b-iii, c-ii

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Tricuspid valve is present between the right atrium and right ventricle.
2. Bicuspid valve is present between the left ventricle and left atrium.
3. Semilunar valves are present between right ventricle and pulmonary artery.

**Solved independently** (answer withheld)

1. The tricuspid valve guards the opening between the right atrium and the right ventricle, so $a \rightarrow iii$.
2. The bicuspid (mitral) valve guards the opening between the left atrium and the left ventricle, so $b \rightarrow i$.
3. The semilunar valve guards the opening from the right ventricle into the pulmonary artery, so $c \rightarrow ii$.
4. $a\text{-}iii,\ b\text{-}i,\ c\text{-}ii$ is option $2$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q087_2a55c227_03112026.png?v=2a55c227615d)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q087_fbf8ffbb_03112026.png?v=fbf8ffbb8df3)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The tricuspid valve guards the right atrio-ventricular opening, the bicuspid the left, and the semilunar valves guard the two arterial outlets
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The heart is drawn with its left side on the viewer's right, so a student recalling the labelled figure rather than the words reads the picture's right-hand chambers as the right side and puts the tricuspid valve between the left atrium and left ventricle
- **Why:** This question requires the stated position of each named valve, demonstrated by Column II giving locations -- "Between right atrium and right ventricle", "Between right ventricle and pulmonary artery".
<!--/ecat-->

## Q88

Biology · zoology · Breathing and Exchange of Gases

Match the items given in Column I with those in Column IT and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Tidal volume | i | $2500$ – $3000\,\mathrm{Ml}$ |
| b | Inspiratory Reserve volume | ii | $1100$ – $1200\,\mathrm{mL}$ |
| c | Expiratory Reserve volume | iii | $500$ – $550\,\mathrm{mL}$ |
| d | Residual volume | iv | $1000$ – $1100\,\mathrm{mL}$ |

- (1) a-iv, b-iii, c-ii, d-i
- (2) a-iii, b-ii, c-i, d-iv
- (3) a-i, b-iv, c-ii, d-iii
- **(4)** a-iii, b-i, c-iv, d-ii

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Tidal volume- $550$ to $550\,\mathrm{ml}$
2. Inspiratory reserve volume- $2100$-$3200\,\mathrm{ml}$
3. Expiratory reserve volume- $1000$ to $1200\,\mathrm{ml}$
4. Residual volume- around $1200\,\mathrm{ml}$

**Solved independently** (answer withheld)

1. Tidal volume is about $500\,\mathrm{mL}$, so (a) matches (iii) $500$ – $550\,\mathrm{mL}$.
2. Inspiratory reserve volume is about $2500$ – $3000\,\mathrm{mL}$, so (b) matches (i).
3. Expiratory reserve volume is about $1000$ – $1100\,\mathrm{mL}$, so (c) matches (iv).
4. Residual volume is about $1100$ – $1200\,\mathrm{mL}$, so (d) matches (ii).
5. The set a-iii, b-i, c-iv, d-ii is option $4$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q088_385b51fb_03112026.png?v=385b51fb2ec9)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q088_2fa26f94_03112026.png?v=2fa26f9429a0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The four printed respiratory volumes: tidal 500-550 mL, inspiratory reserve 2500-3000 mL, expiratory reserve 1000-1100 mL and residual 1100-1200 mL
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  A student who remembers one large figure of 2500-3000 mL for "the reserve volume" but not which reserve it belongs to hands it to the expiratory reserve volume, and the remaining numbers then fall in around it
- **Why:** This question requires four stored values, demonstrated by Column II being nothing but printed ranges -- "$500$ - $550\,\mathrm{mL}$", "$2500$ - $3000\,\mathrm{Ml}$" -- with no quantity to compute from the stem.
- **Note:** Column II item i is printed with a capital-M unit, "Ml", and the stem reads "Column IT" for "Column II"; both are transcription debris and neither changes what is asked or which option is keyed.
<!--/ecat-->

## Q89

Biology · zoology · Excretory Products and Their Elimination

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Glycosuria | i | Accumulation of uric acid in joints |
| b | Gout | ii | Mass of crystallised salts within the kidney |
| c | Renal calculi | iii | Inflammation in glomeruli |
| d | Glomerular nephritis | iv | Presence of glucose in urine |

- **(1)** iv i ii iii
- (2) iii ii iv i
- (3) ii iii i iv
- (4) i ii iii iv

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Glycosuria- presence of glucose in urine
2. Gout- accumulation of uric acid in joints
3. Renal calculi- mass of crystallized salts within the kidney
4. Glomerular nephritis- inflammation of glomeruli

**Solved independently** (answer withheld)

1. Glycosuria is the presence of glucose in urine, so $a \rightarrow iv$; gout is the accumulation of uric acid crystals in joints, so $b \rightarrow i$; renal calculi are stones of crystallised salts in the kidney, so $c \rightarrow ii$; glomerulonephritis is inflammation of the glomeruli, so $d \rightarrow iii$.
2. The sequence $a$-$iv$, $b$-$i$, $c$-$ii$, $d$-$iii$ reads iv i ii iii, which is option $1$.

**Subtopic:** Disorders Of The Excretory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q089_fe891cf7_03112026.png?v=fe891cf70b86)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q089_4bbd3334_03112026.png?v=4bbd33346914)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Four excretory disorders named by their own definitions: glycosuria is glucose in the urine, gout is uric acid in the joints, renal calculi are stones in the kidney and glomerular nephritis is inflammation of the glomeruli
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each Column I name carries its Column II partner inside it -- glyco-suria is sugar in urine, glomerular nephritis is inflammation of the glomeruli, renal calculi are stones in the kidney -- so any one of those readings strikes out all three distractors at once. I checked the one pairing a student could doubt, gout against uric acid, since the word gout does not say uric acid by itself, and no distractor pairs gout with the joints alongside anything the other three names allow.
- **Why:** This question requires four stated disorder-to-symptom facts, demonstrated by Column II spelling out the definition of each named disorder -- "Presence of glucose in urine", "Inflammation in glomeruli".
<!--/ecat-->

## Q90

Biology · zoology · Excretory Products and Their Elimination

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Ultrafiltration | i | Henle’s loop |
| b | Concentration of urine | ii | Ureter |
| c | Transport of urine | iii | Urinary bladder |
| d | Storage of urine | iv | Malpighian corpuscle |
|  |  | v | Proximal convoluted tubule |

- (1) v vi i iii
- (2) iv v ii iii
- (3) v iv i ii
- **(4)** iv i ii iii

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ultrafiltration occurs in glomerulus/Malpighian corpuscle.
2. Transport of urine occurs in ureter.
3. Storage of the urine occurs in urinary bladder.
4. Concentration of urine occurs in Henle’s loop.

**Solved independently** (answer withheld)

1. Ultrafiltration takes place in the Malpighian corpuscle (glomerulus + Bowman's capsule), so $a \rightarrow iv$.
2. Henle's loop (counter-current mechanism) concentrates the urine, so $b \rightarrow i$.
3. The ureter carries urine from the kidney to the bladder, so $c \rightarrow ii$.
4. The urinary bladder stores urine, so $d \rightarrow iii$.
5. The sequence $iv, i, ii, iii$ is option $4$.

**Subtopic:** Human Excretory System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q090_1e2470ff_03112026.png?v=1e2470fffd54)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q090_6502d580_03112026.png?v=6502d580858b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each step of urine formation and passage belongs to one named part: ultrafiltration to the Malpighian corpuscle, concentration of urine to Henle's loop, transport to the ureter and storage to the urinary bladder
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The proximal convoluted tubule is the segment taught as reabsorbing the bulk of the water and salts, so a student who reads "concentration of urine" as "where most water is taken back" hands that row to the PCT; the counter-current machinery that actually concentrates the urine is the next segment along, Henle's loop
- **Why:** This question requires the stated site of each named step, demonstrated by Column I being functions -- "Ultrafiltration", "Storage of urine" -- and Column II being parts of the excretory system.
- **Note:** Option 1 as stored cites "vi", a numeral absent from the printed Column II, which runs i to v. The key (option 4) and the two other distractors are intact and internally consistent, so the question and its answer stand; option 1 alone cannot be judged and should be re-read against the printed paper. Unlike the four-by-four lists in this paper, the missing entry cannot be recovered by elimination here, because Column II carries one more item than there are rows.
<!--/ecat-->

## Q91

Biology · botany · Anatomy of Flowering Plants

> ⚠ The independent solve chose (4); the booklet prints (1).

Secondary xylem and phloem in dicot stem are produced by

- **(1)** Axillary meristems
- (2) Apical meristems
- (3) Phellogen
- (4) Vascular cambium

**Answer** — booklet: (1) · independent solve: (4) · differs

**Publisher's solution**

1. Vascular cambium is partially secondary
2. Form secondary xylem towards its inside and secondary phloem towards outsides.
3. $4$ – $10$ times more secondary xylem is produced than secondary phloem.

**Solved independently** (answer withheld)

1. In a dicot stem, secondary growth comes from the $\text{vascular cambium}$, which cuts off secondary xylem towards the pith and secondary phloem towards the periphery, so the answer is option $4$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q091_9e91fb6f_03112026.png?v=9e91fb6f4f40)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q091_71a0375b_03112026.png?v=71a0375bc06f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Secondary xylem and secondary phloem are cut off by the vascular cambium of the dicot stem's cambial ring
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stored key against the printed options: the key index selects option 1, 'Axillary meristems', which produce branches, while the tissue-producing meristem the stem asks for is the vascular cambium, printed here as option 4. The key index and this option order cannot both be as printed, so no wrong option can be named.
- **Why:** This question requires the meristem NCERT names as the source of secondary vascular tissue, demonstrated by the stem 'Secondary xylem and phloem in dicot stem are produced by' over four meristem names.
- **Note:** Key/option mismatch in our record, not a judgement on the paper: the subject answer, vascular cambium, is printed as option 4 while the stored key points at option 1. The key is not re-judged here; a reviewer should check the printed option order for Q91. Had the key resolved to option 4, the routes to check would be phellogen, the other secondary meristem printed in the same section, and apical meristems, which give primary growth.
<!--/ecat-->

## Q92

Biology · botany · Morphology of Flowering Plants

Pneumatophores occur in

- (1) Submerged hydrophytes
- **(2)** Halophytes
- (3) Carnivorous plants
- (4) Free-floating hydrophytes

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Halophytes contain pneumatophores.
2. They are also known as breathing roots.
3. It helps in gaseous exchange.

**Solved independently** (answer withheld)

1. Pneumatophores are roots that grow vertically upwards out of waterlogged saline swamp soil to take in oxygen for respiration, as in mangroves such as $Rhizophora$; mangroves are halophytes, so the answer is option $2$.

**Subtopic:** The Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q092_a51c140f_03112026.png?v=a51c140f54b4)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q092_4522cd2c_03112026.png?v=4522cd2c7d3d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pneumatophores are the negatively geotropic breathing roots of mangroves, which grow up out of salty waterlogged soil to get oxygen
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Halophyte' and 'hydrophyte' differ by one syllable, so a student who stored the fact as 'breathing roots occur in -phytes of wet ground' retrieves the water word, and a submerged plant is the one that most obviously needs air.
- **Why:** This question requires the habitat group NCERT gives for breathing roots, demonstrated by the stem 'Pneumatophores occur in' over options that set halophytes against two kinds of hydrophyte.
- **Note:** Likeness-against-position test on option 1: replace 'hydrophytes' with an unlike word such as 'xerophytes' and the pull dies, because it is the near-identical -phyte names that carry the student, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q93

Biology · botany · Anatomy of Flowering Plants

Plants having little or no secondary growth are

- (1) Cycads
- **(2)** Grasses
- (3) Conifers
- (4) Deciduous angiosperms

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Grasses are monocots, do not have secondary growth

**Solved independently** (answer withheld)

1. Secondary growth comes from the vascular cambium and cork cambium, which are present in gymnosperms and dicots but generally absent in monocots.
2. Cycads and conifers are gymnosperms, and deciduous angiosperms are woody dicots, so all three show secondary growth.
3. Grasses are monocots with closed vascular bundles and no cambium, so they show little or no secondary growth: option $2$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q093_f4157fb4_03112026.png?v=f4157fb466b4)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q093_4f5eb6f4_03112026.png?v=4f5eb6f49122)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Monocots such as the grasses have no vascular cambium, so they show little or no secondary growth, while dicots and gymnosperms thicken from a cambial ring
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  I checked the other three against the printed criterion: cycads and conifers are gymnosperms, which the chapter treats as wood producers with a cambial ring, and 'deciduous angiosperms' names leaf fall, which no line connects to cambium at all - so none of the three carries a printed statement denying it secondary growth, and nothing reaches them.
- **Why:** This question requires the stated absence of secondary growth in monocots, demonstrated by the stem 'Plants having little or no secondary growth are' with grasses standing against two gymnosperm groups and the angiosperm trees.
- **Note:** no_trap is a finding: the three other options are all woody groups, so reaching them needs a printed line that contradicts their own account, and none exists. Two NCERT facts stack here - grasses are monocots, and monocots have no cambium - but both are stated facts rather than a criterion to apply, so asks stays fact_line, in line with the rest of this group.
<!--/ecat-->

## Q94

Biology · botany · Biological Classification

Select the wrong statement:

- (1) Mitochondria are the powerhouse of the cell in all kingdoms except Monera
- (2) Cell wall is present in members of Fungi and Plantae.
- (3) Pseudopodia are locomotory and feeding structures in Sporozoans.
- (4) Mushrooms belong to Basidiomycetes.

**Answer** — booklet: (none) · independent solve: (3) · unchecked

**Publisher's solution**

1. Pseudopodia are locomotory structures in sarcodines (Amoeboid)

**Solved independently** (answer withheld)

1. Statement $1$: Monera are prokaryotes with no membrane-bound organelles, so mitochondria are the powerhouse in all other kingdoms but not in Monera; this is true.
2. Statement $2$: Fungi have a chitin cell wall and Plantae have a cellulose cell wall; this is true.
3. Statement $3$: Pseudopodia (false feet) are the locomotory and food-capturing structures of amoeboid protozoans (Sarcodines, e.g. Amoeba); Sporozoans (e.g. Plasmodium) lack locomotory structures; this is false.
4. Statement $4$: Mushrooms (e.g. Agaricus) belong to the class Basidiomycetes; this is true.
5. The only wrong statement is $3$, so the answer is option $3$.

**Subtopic:** Protozoans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q094_94b59e9d_03112026.png?v=94b59e9dad48)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q094_6b85098e_03112026.png?v=6b85098e14d6)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The kingdom-level generalisations of biological classification: who lacks mitochondria, who has a cell wall, which protozoan group moves by pseudopodia, and where mushrooms sit
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The record carries no answer at all - correct_answer is null, accepted_answers is empty and answer_line_as_printed is null - so there is no way to tell which of the four statements is the wrong one the stem asks for, and no wrong option can be identified, let alone a route to it.
- **Why:** This question requires judging four stated kingdom-level claims against their printed sources, demonstrated by the stem 'Select the wrong statement:' over four standalone claims about mitochondria, cell walls, pseudopodia and mushrooms.
- **Note:** No key in our record for this question, so under rule 0.5 no trap is written. A reviewer should supply the printed answer for Q94 and then check the route on 'Pseudopodia are locomotory and feeding structures in Sporozoans.', since pseudopodia belong to the amoeboid protozoans and the sporozoans are the group printed last in the same list.
<!--/ecat-->

## Q95

Biology · botany · Anatomy of Flowering Plants

Casparian strips occur in

- **(1)** Endodermis
- (2) Epidermis
- (3) Cortex
- (4) Pericycle

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Casparian strips occurs in endodermis.
2. It is an inner layer of cells in the cortex of a root and of some stems, surrounding a vascular bundle.

**Solved independently** (answer withheld)

1. Casparian strips are suberin deposits on the tangential and radial walls of the endodermal cells of the root, so they occur in the $\text{endodermis}$, which is option $1$.

**Subtopic:** Dicotyledonous and Monocotyledonous Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q095_d71c78eb_03112026.png?v=d71c78ebdd81)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q095_73287939_03112026.png?v=73287939cd1f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Casparian strip is the suberised band in the walls of the root's endodermal cells, which forces water to pass through the cell itself
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The pericycle is the layer printed immediately inside the endodermis in the root's tissue sequence, so a student who remembers the strip as belonging to 'the layer around the vascular bundle' takes the next name in that sequence.
- **Why:** This question requires the stated location of a named root feature, demonstrated by the stem 'Casparian strips occur in' over four root layers.
- **Note:** Likeness-against-position test on option 4: 'pericycle' and 'endodermis' do not resemble each other as words, and the pull is their adjacency in the printed layer sequence, so nearby_fact.
<!--/ecat-->

## Q96

Biology · botany · Morphology of Flowering Plants

> ⚠ The independent solve chose (4); the booklet prints (3).

Sweet potato is a modified

- (1) Rhizome
- (2) Stem
- **(3)** Tap root
- (4) Adventitious root

**Answer** — booklet: (3) · independent solve: (4) · differs

**Publisher's solution**

1. Sweet potato is an example of tuberous root.
2. It is a modified tap root.

**Solved independently** (answer withheld)

1. NCERT lists sweet potato as an example of adventitious roots that become swollen to store food, so it is a modified adventitious root, which is option $4$.

**Subtopic:** The Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q096_51d0b918_03112026.png?v=51d0b918e762)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q096_467e8e3c_03112026.png?v=467e8e3c0229)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sweet potato stores its food in swollen adventitious roots, unlike the carrot's and turnip's swollen tap root
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the stored key against the printed options: the key index selects option 3, 'Tap root', while the storage organ printed for sweet potato is the adventitious root, which stands here as option 4 - the tap-root storage examples in the same printed line are carrot and turnip. The key index and this option order cannot both be as printed, so no wrong option can be named.
- **Why:** This question requires the stated root type that swells in a named storage plant, demonstrated by the stem 'Sweet potato is a modified' over two root types, a stem and a rhizome.
- **Note:** Key/option mismatch in our record, not a judgement on the paper: the subject answer, adventitious root, is printed as option 4 while the stored key points at option 3. The key is not re-judged here; a reviewer should check the printed option order for Q96. Had the key resolved to option 4, the routes to check would be the tap-root storage list (carrot, turnip, beet) printed in the same paragraph, and the potato-for-sweet-potato stem-tuber slip behind option 2.
<!--/ecat-->

## Q97

Biology · botany · Plant Kingdom

Which of the following statements is correct?

- (1) Stems are usually unbranched in both Cycas and Cedrus.
- (2) Ovules are not enclosed by ovary wall in gymnosperms.
- (3) Horsetails are gymnosperms.
- (4) Selaginella is heterosporous, while Salvinia, is homosporous.

**Answer** — booklet: (none) · independent solve: (2) · unchecked

**Publisher's solution**

1. Gymnosperms have naked ovule.
2. Called phanerograms without womb/ovary

**Solved independently** (answer withheld)

1. In gymnosperms the ovules are not enclosed by any ovary wall (naked seeds), so option $2$ is correct.
2. Cycas has an unbranched stem but Cedrus has a branched stem, so option $1$ is false.
3. Horsetails ($Equisetum$) are pteridophytes, not gymnosperms, so option $3$ is false.
4. Both $Selaginella$ and $Salvinia$ are heterosporous, so option $4$ is false; the answer is option $2$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q097_b28dacc8_03112026.png?v=b28dacc8bd92)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q097_0d640bed_03112026.png?v=0d640bed89ed)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What separates the plant groups in the printed account: naked ovules in gymnosperms, the branching habit of Cycas against Cedrus, where horsetails sit, and which pteridophytes are heterosporous
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The record carries no answer - correct_answer is null, accepted_answers is empty and answer_line_as_printed is null - so which of the four statements the paper counts as correct cannot be told, and with the key unknown no option can be classed as wrong or a route written to it.
- **Why:** This question requires judging four stated claims about plant groups against their printed sources, demonstrated by the stem 'Which of the following statements is correct?' over four standalone claims about gymnosperms, horsetails and spore types.
- **Note:** No key in our record for this question, so under rule 0.5 no trap is written. A reviewer should supply the printed answer for Q97 and then check two routes: 'Selaginella is heterosporous, while Salvinia, is homosporous.', a two-part claim whose first half holds and whose second fails, and 'Horsetails are gymnosperms.', where the printed group for horsetails is the pteridophytes.
<!--/ecat-->

## Q98

Biology · botany · Ecosystem

What type of ecological pyramid would be obtained with the following data?
Secondary consumer: $120\,\mathrm{g}$
Primary consumer: $60\,\mathrm{g}$
Primary producer: $10\,\mathrm{g}$

- (1) Upright pyramid of biomass
- **(2)** Inverted pyramid of biomass
- (3) Upright pyramid of numbers
- (4) Pyramid of energy

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The pyramid is inverted pyramid of biomass.

**Solved independently** (answer withheld)

1. The quantities are given in $\mathrm{g}$, so they are standing biomass, giving a pyramid of biomass (not numbers or energy).
2. Biomass increases upward: $10\,\mathrm{g}$ (producer) $< 60\,\mathrm{g}$ (primary consumer) $< 120\,\mathrm{g}$ (secondary consumer), so the base is smallest and the top is largest.
3. A pyramid with the smallest base is inverted, so it is an inverted pyramid of biomass, which is option $2$.

**Subtopic:** Ecological Pyramids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q098_8355722d_03112026.png?v=8355722d5be8)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q098_e18d1c09_03112026.png?v=e18d1c09e6c2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A pyramid built from masses is a pyramid of biomass, and it stands inverted when standing biomass rises up the trophic levels, as it does in the sea
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The general rule a student carries is that ecological pyramids stand upright, and applying it without reading the three printed figures - 10 g of producer under 60 g and then 120 g of consumers - gives the upright biomass pyramid.
- **Why:** This question requires the pyramid convention applied to the figures supplied, demonstrated by the stem 'What type of ecological pyramid would be obtained with the following data?' followed by 'Secondary consumer: 120 g, Primary consumer: 60 g, Primary producer: 10 g'.
- **Note:** asks is apply_rule rather than fact_line because the stem supplies its own data and the student has to run the pyramid convention over them; no quantity is produced, so it is not calculate. This is the one member of the group that is not answered off a printed sentence.
<!--/ecat-->

## Q99

Biology · botany · Environmental Issues

World Ozone Day is celebrated on

- (1) $22^{\mathrm{nd}}$ April
- (2) $5^{\mathrm{th}}$ June
- **(3)** $16^{\mathrm{th}}$ September
- (4) $21^{\mathrm{st}}$ April.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. 16 September is celebrated as world ozone day.

**Solved independently** (answer withheld)

1. World Ozone Day is observed on $16^{\mathrm{th}}$ September (anniversary of the Montreal Protocol, 1987), which is option $3$; $22^{\mathrm{nd}}$ April is Earth Day and $5^{\mathrm{th}}$ June is World Environment Day.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q099_538eea76_03112026.png?v=538eea76adfe)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q099_035b58f4_03112026.png?v=035b58f4c6af)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** World Ozone Day is 16 September, the day the Montreal Protocol on ozone-depleting substances was signed
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  5 June is a true and firmly held environmental date, but it is World Environment Day, so a student holding one environmental day and not the other answers the right kind of question with the wrong day's date.
- **Why:** This question requires the stated date of a named observance, demonstrated by the stem 'World Ozone Day is celebrated on' over four calendar dates.
- **Note:** answers_other_question rather than nearby_fact on option 2: the option is not a wrong name reached by position but a true answer to a different question, 'when is World Environment Day', which is the distinction the rulebook draws for this label. The same label is used on q100 in this group for the same kind of pull, as rule 3 requires.
<!--/ecat-->

## Q100

Biology · botany · Environmental Issues

In stratosphere, which of the following elements acts as a catalyst in degradation of ozone and release of molecular oxygen?

- (1) Oxygen
- (2) Carbon
- (3) $\mathrm{Fe}$
- **(4)** $\mathrm{Cl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{Cl}$ acts as catalyst for degradation of ozone.
2. It is release due to chlorofluorocarbons.

**Solved independently** (answer withheld)

1. UV radiation in the stratosphere breaks chlorofluorocarbons and releases $\mathrm{Cl}$ atoms; these $\mathrm{Cl}$ atoms degrade ozone ($\mathrm{Cl} + \mathrm{O_3} \rightarrow \mathrm{ClO} + \mathrm{O_2}$, then $\mathrm{ClO} + \mathrm{O} \rightarrow \mathrm{Cl} + \mathrm{O_2}$) and are regenerated, so $\mathrm{Cl}$ acts as the catalyst, which is option $4$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q100_7ac9da7a_03112026.png?v=7ac9da7aec43)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q100_a8086f29_03112026.png?v=a8086f29ad96)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ultraviolet light splits CFCs to free chlorine atoms, and each chlorine atom breaks ozone to molecular oxygen and is handed back unchanged, so it acts as a catalyst
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Oxygen is true in this reaction - the stem itself says molecular oxygen is released - so a student reading the sentence for the species it names answers 'what comes out' instead of 'what is handed back each cycle'.
- **Why:** This question requires the element NCERT names as the catalyst of ozone breakdown, demonstrated by the stem 'which of the following elements acts as a catalyst in degradation of ozone and release of molecular oxygen?' over four elements.
- **Note:** answers_other_question rather than nearby_fact on option 1: oxygen is not a wrong name reached by position, it is the true answer to the stem's own subordinate clause, 'release of molecular oxygen'. Paired deliberately with q099, which carries the same label for the same kind of pull.
<!--/ecat-->

## Q101

Biology · botany · Organisms and Populations

Natality refers to.

- (1) Number of individuals entering a habitat
- (2) Death rate
- (3) Number of individuals leaving the habitat
- **(4)** Birth rate

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Natality is birth rate whereas mortality is death rate.

**Solved independently** (answer withheld)

1. Natality is the number of births in a population during a given period, which is the birth rate, so the answer is option $4$; immigration is option $1$, mortality is option $2$ and emigration is option $3$.

**Subtopic:** Introduction of Organisms, Populations and Their Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q101_7853730c_03112026.png?v=7853730c004f)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q101_7eb450de_03112026.png?v=7eb450deda33)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Natality is the birth rate - the individuals added to a population by reproduction
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Natality and mortality are printed as one pair in the population-density equation, so a student who holds the pair but not which member is which takes the death rate.
- **Why:** This question requires the stated meaning of a named population attribute, demonstrated by the stem 'Natality refers to.' over birth rate, death rate and the two movement terms.
- **Note:** Likeness-against-position test on option 2: the option is printed as 'Death rate', which does not resemble the word 'natality' at all, so what carries the student is the natality-mortality pairing in the printed equation - nearby_fact, not look_alike_term. Had the option been printed as 'Mortality', the test would have gone the other way.
<!--/ecat-->

## Q102

Biology · botany · Organisms and Populations

Niche is

- **(1)** the functional role played by the organism where it lives
- (2) all the biological factors in the organism’s environment
- (3) the range of temperature that the organism’s ·needs to live
- (4) the physical space where an organism lives

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The functional role that is played by an organism where it lives is known as niche.

**Solved independently** (answer withheld)

1. NCERT describes an organism's niche as the range of conditions it can tolerate, the resources it uses and its distinct functional role in the ecological system, so the best fit is $\text{niche} = \text{functional role where it lives}$, which is option $1$.

**Subtopic:** Biome, Environmental Factors & Four Levels of Biological Organisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q102_a073c688_03112026.png?v=a073c688acd0)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q102_9a5a3684_03112026.png?v=9a5a368403ae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A niche is the functional role an organism plays where it lives; the place itself is its habitat.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The niche is glossed with the words 'where an organism lives', and the option naming the physical space is the habitat sentence printed beside the niche sentence.
- **Why:** This question requires the stated definition of a niche, demonstrated by the stem 'Niche is' followed by rival definitions, one of which is the definition of habitat.
- **Note:** E1 called this statement_options on option length; the four options are rival completions of 'Niche is' with no statement block printed, so the shape recorded is mcq. Option 3 carries a stray middle dot in 'the organism's ·needs to live'. nearby_fact and not look_alike_term: habitat and niche are not alike as words, and the route survives if the pair is replaced by two unlike terms, so position in the text is doing the work.
<!--/ecat-->

## Q103

Biology · botany · Environmental Issues

Which of the following is a secondary pollutant?

- **(1)** $\mathrm{O_3}$
- (2) $\mathrm{CO}$
- (3) $\mathrm{SO_2}$
- (4) $\mathrm{CO_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ozone is a secondary pollutant.

**Solved independently** (answer withheld)

1. A secondary pollutant forms in the atmosphere from reactions of primary pollutants; $\mathrm{CO}$, $\mathrm{SO_2}$ and $\mathrm{CO_2}$ are emitted directly, whereas $\mathrm{O_3}$ forms photochemically from $\mathrm{NO_x}$ and hydrocarbons, so the answer is option $1$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q103_aa75eb36_03112026.png?v=aa75eb36e5e4)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q103_318ac8cb_03112026.png?v=318ac8cb54e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A primary pollutant is emitted as it is; a secondary pollutant such as ozone is made in the air out of primary ones.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  $\mathrm{SO_2}$ is the pollutant whose atmospheric chemistry is taught - it goes on to sulphuric acid in acid rain - and taking part in that reaction is read as being the secondary pollutant, when the secondary pollutant is the product.
- **Why:** This question requires the distinction between an emitted pollutant and one formed in the atmosphere, demonstrated by 'Which of the following is a secondary pollutant?' standing over three directly emitted gases and $\mathrm{O_3}$.
<!--/ecat-->

## Q104

Biology · botany · Plant Kingdom

Winged pollen grains are present in

- **(1)** Pinus
- (2) Mustard
- (3) Mango
- (4) Cycas

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Winged pollen grains are present in Pinus.

**Solved independently** (answer withheld)

1. Pinus is a wind-pollinated gymnosperm whose pollen grains have two air-filled wings (sacci), whereas Cycas, mustard and mango pollen lack wings, so the answer is option $1$ (Pinus).

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q104_290a4baa_03112026.png?v=290a4baad985)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q104_cab3479e_03112026.png?v=cab3479e4f47)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pinus pollen carries two air-filled wings that let the wind lift it; this is a feature of the conifer, not of every gymnosperm.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Winged pollen is filed as a gymnosperm wind-pollination feature, and Cycas is the other gymnosperm printed in the same section, so the rule as remembered reaches it too.
- **Why:** This question requires the stated feature of Pinus pollen, demonstrated by 'Winged pollen grains are present in' followed by two angiosperms and a second gymnosperm.
<!--/ecat-->

## Q105

Biology · botany · Biological Classification

After karyogamy followed by meiosis, spores are produced exogenously in

- (1) Saccharomyces
- (2) Neurospora
- **(3)** Agaricus
- (4) Alternaria

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Agaricus spores are produced exogenously.

**Solved independently** (answer withheld)

1. In Basidiomycetes (e.g. $Agaricus$), karyogamy and meiosis occur in the basidium, and the four basidiospores are produced exogenously on it, whereas $Saccharomyces$ and $Neurospora$ (Ascomycetes) form ascospores endogenously in asci and $Alternaria$ (Deuteromycetes) has no known sexual stage, so the answer is option $3$.

**Subtopic:** Basidiomycetes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q105_93b820b4_03112026.png?v=93b820b4c8d1)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q105_19ed3616_03112026.png?v=19ed3616d550)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Basidiomycetes such as Agaricus form their spores on the outside of the basidium after karyogamy and meiosis, while ascomycetes form theirs inside an ascus.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Alternaria's conidia are cut off on the outside of the conidiophore, so the word 'exogenously' fits it, and the stem's first requirement - karyogamy then meiosis - is left out, which is exactly what conidia skip.
- **Why:** This question requires both printed requirements to hold at once, demonstrated by 'After karyogamy followed by meiosis, spores are produced exogenously', which the conidial fungus meets only in the second clause and the two ascomycetes only in the first.
<!--/ecat-->

## Q106

Biology · botany · Plant Kingdom

Which one is wrongly matched?

- (1) Unicellular organism – Chlorella
- (2) Unitlagellate gametes – Polysiplwnia
- (3) Gemma cups – Marchantia
- (4) Bitlagellate zoospores – Brown algae

**Answer** — booklet: (none) · independent solve: (2) · unchecked

**Publisher's solution**

1. Polysiphonia is a genus of red algae, where asexual spores and gametes are non-motile or non-flagellated.
2. Other options (1.3 & 4 ) are correctly matched.

**Solved independently** (answer withheld)

1. $\textit{Chlorella}$ is a unicellular green alga, so option $1$ is correctly matched.
2. $\textit{Polysiphonia}$ is a red alga (Rhodophyceae); red algae have no flagellated stages and their gametes are non-motile, so 'uniflagellate gametes' is wrongly matched.
3. $\textit{Marchantia}$ reproduces asexually by gemmae formed in gemma cups on the thallus, so option $3$ is correctly matched.
4. Brown algae (Phaeophyceae) produce pear-shaped zoospores bearing two unequal laterally attached flagella (biflagellate), so option $4$ is correctly matched.
5. The only wrong pair is option $2$.

**Subtopic:** Rhodophyceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 22)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q106_8fdccb9d_03112026.png?v=8fdccb9d7d59)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q106_27154610_03112026.png?v=27154610612f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each printed pair ties one feature to the group that shows it - unicellular Chlorella, uniflagellate gametes in red algae, gemma cups in Marchantia, biflagellate zoospores in brown algae.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The record carries no answer at all - correct_answer is null and accepted_answers is empty - and three of the four pairs are OCR-damaged, so no option can be tested against a key.
- **Why:** This question requires each printed feature to be checked against the organism named beside it, demonstrated by options of the form 'Gemma cups - Marchantia' judged whole under 'Which one is wrongly matched?'.
- **Note:** Stored as 'Unitlagellate gametes - Polysiplwnia' and 'Bitlagellate zoospores - Brown algae', that is uniflagellate / Polysiphonia and biflagellate; no key is stored. A reviewer holding the printed paper should settle which pair the key names before any route is written, and the pair to check first is the red alga, whose gametes are non-flagellate. The printed shape is four pairs accepted or rejected whole (pair_options), recorded here as statements; E1 called it statement_options on option length.
<!--/ecat-->

## Q107

Biology · botany · The Living World

Match the items given in Column I with those in Column 11 and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Herbarium | i | It is a place having a collection of preserved plants and animals. |
| b | Key | ii | A list that enumerates methodically all the species found in an area with brief description aiding identification: |
| c | Museum | iii | Is a place where dried and pressed plant specimens mounted on sheets are kept |
| d | Catalogue | iv | A booklet containing a list of characters and their alternates which are helpful in identification of various taxa. |

- **(1)** iii iv i ii
- (2) i iv iii ii
- (3) ii iv iii 1
- (4) iii ii i iv

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Herbarium – Dried and pressed plant specimen
2. Key – Identification of various taxa
3. Museum – Plant and animal specimen are preserved
4. Catalogue – Alphabetical listing of species

**Solved independently** (answer withheld)

1. A herbarium is a store of dried, pressed plant specimens mounted on sheets, so $a \rightarrow iii$.
2. A key is a booklet of characters and their alternates (couplets) used to identify taxa, so $b \rightarrow iv$.
3. A museum holds collections of preserved plants and animals, so $c \rightarrow i$.
4. A catalogue methodically enumerates all species of an area with brief descriptions, so $d \rightarrow ii$.
5. The order $iii, iv, i, ii$ matches option $1$.

**Subtopic:** Taxonomy and Systematics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q107_d5629836_03112026.png?v=d56298363c31)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q107_21be70b8_03112026.png?v=21be70b8e0ec)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The taxonomic aids are each defined by what they physically are: a herbarium is pressed plants on sheets, a museum is preserved plants and animals, a key is paired contrasting characters, and a catalogue is an enumerated list of the species of an area
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Column II's entry for the catalogue ends on the words "aiding identification", and identification is what a key is for, so a student reading for that phrase hands the catalogue's definition to the key and is left giving the key's own definition to the catalogue
- **Why:** This question requires the stated definition of each taxonomic aid, demonstrated by Column II being the definitions themselves -- "Is a place where dried and pressed plant specimens mounted on sheets are kept".
- **Note:** Option 3 is stored as "ii iv iii 1", with the digit 1 standing where the numeral i belongs. The four rows and four Column II entries make the pairing a one-to-one mapping, so with a-ii, b-iv and c-iii given, d can only be i; the option is therefore judged as a-ii, b-iv, c-iii, d-i without any repair to the record. The stem also reads "Column 11" for "Column II".
<!--/ecat-->

## Q108

Biology · botany · Sexual Reproduction in Flowering Plants

Which.one of the following plants shows a very close relationship with a species of moth, where non of the two can complete its life cycle without the other?

- (1) Viola
- (2) Hydrilla
- (3) Banana
- **(4)** Y Yucca

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Yucca has a very close relationship with moth.
2. They cannot complete their life cycle without each other.

**Solved independently** (answer withheld)

1. The plant-moth pair in which each partner depends on the other to complete its life cycle is $\text{Yucca}$ with the yucca moth: the moth pollinates the flower and lays eggs in its ovary, and the larvae feed on some of the developing seeds, so the answer is option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q108_6d07e4af_03112026.png?v=6d07e4af04a6)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q108_39f5cdae_03112026.png?v=39f5cdae3ae3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Yucca and its moth are the obligate mutualism the chapter names: the moth is the only pollinator, and its larvae feed only on Yucca seeds.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Viola is the plant the pollination section singles out for a special arrangement, its cleistogamous flowers, so 'a very close relationship' is read onto the plant that already carries a named special case.
- **Why:** This question requires the named obligate plant-pollinator pair, demonstrated by 'non of the two can complete its life cycle without the other' set against three plants whose chapter entries are cleistogamy, water pollination and parthenocarpy.
- **Note:** The stem is stored with 'Which.one' and 'non of the two', and option 4 reads 'Y Yucca' with a stray leading letter. The name is legible and is the stored key, so the question is tagged as printed.
<!--/ecat-->

## Q109

Biology · botany · Sexual Reproduction in Flowering Plants

Pollen grains can be stored for several years in liquid nitrogen having a temperature of

- (1) $-160^\circ\,\mathrm{C}$
- (2) $-120^\circ\,\mathrm{C}$
- **(3)** $-196^\circ\,\mathrm{C}$
- (4) $-80^\circ\,\mathrm{C}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Liquid nitrogen is used to store pollen grains at $-196^\circ\mathrm{C}$

**Solved independently** (answer withheld)

1. Pollen grains are stored for years by cryopreservation in liquid nitrogen at $-196^\circ\,\mathrm{C}$, which is option $3$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q109_4136f770_03112026.png?v=4136f770e890)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q109_f82e7e9b_03112026.png?v=f82e7e9b8134)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pollen is kept for years in liquid nitrogen, whose temperature is $-196^\circ$C, and that is the figure the chapter prints
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The answer is the temperature of liquid nitrogen, $-196^\circ$C, and I checked each of the other three numbers for a route: none is a value the chapter prints for any storage, none is the answer to a neighbouring question in the chapter, and none is produced by an operation on anything in the stem, which carries no numbers at all. They widen the spread around the right figure without offering a student anything to reason from.
- **Why:** This question requires one stored value, demonstrated by the stem naming the substance -- "liquid nitrogen having a temperature of" -- and the four options being nothing but temperatures.
<!--/ecat-->

## Q110

Biology · botany · Mineral Nutrition

> ⚠ The independent solve chose (2); the booklet prints (4).

In which of the following forms is iron absorbed by plants?

- (1) Both ferric and ferrous
- (2) Ferric
- (3) Free element
- **(4)** Ferrous

**Answer** — booklet: (4) · independent solve: (2) · differs

**Publisher's solution**

1. Ferrous is the form which is absorbed by the plants.

**Solved independently** (answer withheld)

1. NCERT Class 11 Mineral Nutrition states that plants obtain iron as ferric ions, $\mathrm{Fe^{3+}}$, so the answer is option $2$ (Ferric).

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q110_45e73f60_03112026.png?v=45e73f60916f)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q110_611b906e_03112026.png?v=611b906ec659)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Iron is taken up by plants as an ion, in one oxidation state, and not as the free metal nor in both states at once
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Iron is the micronutrient taught for its redox work, shuttling between $\mathrm{Fe^{2+}}$ and $\mathrm{Fe^{3+}}$ inside the plant, so a student who knows it exists in two states hedges and accepts both as the absorbed form; the question asks for the form in which it is ABSORBED, which is one of them
- **Why:** This question requires one stated uptake fact, demonstrated by the stem asking "In which of the following forms is iron absorbed by plants?" with oxidation states as the options.
- **Note:** KEY DOUBT, recorded and not acted on. Our record keys option 4, "Ferrous", while the NCERT line this question is built on reads that plants obtain iron in the form of ferric ions. The question is tagged as printed, as §7 requires. Because option 2, "Ferric", may in fact be the awarded option, no trap and no filler has been written for it -- putting either on a possibly awarded option is the one thing this step must not do -- so option 2 is deliberately left unassigned rather than being called a distractor. The trap recorded on option 1 and the filler on option 3 hold under either reading of the key, since both are wrong whichever single ionic form is correct. A repair task should re-read the printed answer line.
<!--/ecat-->

## Q111

Biology · botany · Mineral Nutrition

Which of the following elements is responsible for maintaining turgor in cells?

- (1) Calcium
- (2) Magnesium
- **(3)** Potassium
- (4) Sodium

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Potassium maintains the turgidity of the plant cells.
2. They also regulate opening and closing of stomata.

**Solved independently** (answer withheld)

1. In plant mineral nutrition, potassium ($\mathrm{K^{+}}$) maintains the anion-cation balance and the turgidity of cells, and drives stomatal opening and closing, so the answer is option $3$ (Potassium).

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q111_7111c2a2_03112026.png?v=7111c2a2bd27)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q111_a5678de2_03112026.png?v=a5678de2104b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Potassium is the element the chapter ties to cell turgidity, the anion-cation balance and the opening and closing of stomata
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Turgor reads as the firmness of a cell, and calcium is the element a student has learnt about for firmness -- it is laid down as calcium pectate in the middle lamella of the cell wall -- so the wall fact is offered where an osmotic one was asked for
- **Why:** This question requires one stated element-to-role fact, demonstrated by the stem asking which element is "responsible for maintaining turgor in cells" with four element names as the options.
<!--/ecat-->

## Q112

Biology · botany · Sexual Reproduction in Flowering Plants

Double fertilization is

- **(1)** Syngamy and triple fusion
- (2) Fusion of two male gametes of a pollen tube with two different eggs
- (3) Fusion of two male gametes with one egg
- (4) Fusion of one male gamete with two polar nuclei

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Syngamy and triple fusion occurs during double fertilization.
2. Triple fusion forms endosperm

**Solved independently** (answer withheld)

1. In angiosperms one male gamete fuses with the egg (syngamy, giving the diploid zygote) and the other fuses with the two polar nuclei (triple fusion, giving the triploid PEN); these two fusions together are called double fertilization, which is option $1$.

**Subtopic:** Double Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q112_aab63a29_03112026.png?v=aab63a29470c)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q112_5413358f_03112026.png?v=5413358feeb4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Double fertilisation is the pair of fusions inside one embryo sac: syngamy, one male gamete with the egg, and triple fusion, the other with the two polar nuclei
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  This option states triple fusion correctly, and a student who recognises it as a real event they have learnt takes it for the answer; it is one of the two fusions double fertilisation is made of, and the question asks for both
- **Why:** This question requires one stated definition, demonstrated by the keyed option naming both events -- "Syngamy and triple fusion" -- while the stem reads only "Double fertilization is".
<!--/ecat-->

## Q113

Biology · botany · Respiration in Plants

What is the role of $\mathrm{NAD^{+}}$ in cellular respiration?

- (1) It is the final electron acceptor for anaerobic respiration.
- (2) It functions as an enzyme.
- (3) Sr It is a nucleotide source for ATP synthesis.
- **(4)** It functions as an electron carrier.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In cellular respiration, $\mathrm{NAD^{+}}$ act as an electron

**Solved independently** (answer withheld)

1. In glycolysis and the Krebs cycle, dehydrogenases transfer electrons and hydrogen to $\mathrm{NAD^{+}}$, reducing it: $\mathrm{NAD^{+}} + 2e^{-} + 2\mathrm{H^{+}} \rightarrow \mathrm{NADH} + \mathrm{H^{+}}$.
2. $\mathrm{NADH}$ is reoxidised to $\mathrm{NAD^{+}}$ by passing the electrons to the electron transport system, so $\mathrm{NAD^{+}}$ is an electron carrier, which is option $4$.
3. $\mathrm{NAD^{+}}$ is a coenzyme, not an enzyme (rules out option $2$), it is not the final electron acceptor (rules out option $1$), and it does not supply nucleotides for ATP synthesis (rules out option $3$).

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q113_df38d1f8_03112026.png?v=df38d1f8a1ce)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q113_d4498ff4_03112026.png?v=d4498ff40028)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NAD+ is a coenzyme that picks electrons up at one step of respiration and hands them on at another, which is what being an electron carrier means
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Oxygen is the final electron acceptor of aerobic respiration, and a student looking for the anaerobic counterpart of that sentence puts NAD+ in the slot; NAD+ does take electrons up, but it passes them on, which is the opposite of being final
- **Why:** This question requires one stated role, demonstrated by the stem asking "What is the role of $\mathrm{NAD^{+}}$ in cellular respiration?" with each option a rival whole claim about that role.
- **Note:** Option 3 is stored with the stray characters "Sr " in front of its text; the claim itself is complete and judgeable, and the key is unaffected.
<!--/ecat-->

## Q114

Biology · botany · Photosynthesis in Higher Plants

Oxygen is not produced during photosynthesis by

- (1) .Chara
- **(2)** Green sulphur bacteria
- (3) Cyca,
- (4) Nostoc

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Green sulphur bacteria do not produce oxygen  during photosynthesis.

**Solved independently** (answer withheld)

1. Green sulphur bacteria use $\mathrm{H_2S}$ (not $\mathrm{H_2O}$) as the hydrogen donor, so their photosynthesis is anoxygenic and releases sulphur, not $\mathrm{O_2}$; Chara (alga), Cycas (gymnosperm) and Nostoc (cyanobacterium) all photolyse water and evolve $\mathrm{O_2}$, so the answer is option $2$.

**Subtopic:** Photosynthesis Experiments · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q114_447d3b36_03112026.png?v=447d3b36c83c)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q114_13d60ca0_03112026.png?v=13d60ca0470a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only the anoxygenic photosynthetic bacteria evolve no oxygen; cyanobacteria, algae and green plants all split water and release it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Nostoc is a prokaryote, and the general rule a student carries is that bacterial photosynthesis releases no oxygen, so the rule is applied to the one group of bacteria it does not cover -- the cyanobacteria, which split water exactly as plants do
- **Why:** This question requires one stated fact about which photosynthesisers release no oxygen, demonstrated by the stem "Oxygen is not produced during photosynthesis by" with four named organisms as the options.
- **Note:** Options 1 and 3 are stored with transcription debris, ".Chara" and "Cyca," for Cycas; both names are legible and the key is unaffected.
<!--/ecat-->

## Q115

Biology · both · Cell: The Unit of Life

The Golgi complex participates in

- (1) Activation of amino acid
- (2) Fatty acid breakdown
- (3) Respiration in bacteria
- **(4)** W Formation of secretory vesicles

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Secretory vesicles bud from Golgi and carry transport proteins to target cell organelles.

**Solved independently** (answer withheld)

1. The Golgi complex packages materials and buds them off as $\text{secretory vesicles}$. Amino acid activation happens in the cytoplasm, fatty acid breakdown happens in mitochondria and peroxisomes, and bacteria have no Golgi. So the answer is option $4$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q115_118489ad_03112026.png?v=118489ad96c2)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q115_778d378b_03112026.png?v=778d378bff57)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Golgi complex packages material for delivery, forming the secretory vesicles, and it also carries out glycosylation -- but it breaks nothing down
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The Golgi does have a lipid job in the chapter, the formation of glycolipids, so a student who remembers "Golgi and lipids" accepts a lipid process without checking its direction; breaking fatty acids down belongs to the glyoxysomes a few lines further on
- **Why:** This question requires one stated organelle function, demonstrated by the stem "The Golgi complex participates in" with four unrelated cellular processes as the options.
- **Note:** The keyed option is stored as "W Formation of secretory vesicles"; the stray leading character is transcription debris and the claim is complete.
<!--/ecat-->

## Q116

Biology · botany · Transport in Plants

Stomata] movement is M t affected by

- (1) $\mathrm{CO_2}$ concentration
- (2) Temperature
- **(3)** $\mathrm{O_2}$ concentration
- (4) Light

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Oxygen concentration does not determine the opening or closing of stomata.
2. It is the temperature, light and carbon-dioxide concentration that determines the opening of stomata.

**Solved independently** (answer withheld)

1. Guard-cell turgor, and therefore stomatal movement, is regulated by light, temperature, $\mathrm{CO_2}$ concentration and water status (ABA); $\mathrm{O_2}$ concentration is not a regulating factor, so the answer is option $3$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q116_0a5f0fcb_03112026.png?v=0a5f0fcb25d7)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q116_f94e2958_03112026.png?v=f94e2958484b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stomatal movement answers to light, temperature and the carbon dioxide concentration, but not to the oxygen concentration
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stem is stored as "Stomata] movement is M t affected by", and the mangled words sit exactly where the task's polarity belongs. The key, option 3, makes sense only if the printed stem negates -- light, temperature and carbon dioxide are all factors the chapter names, so an un-negated stem would have three correct answers. The whole trap on a question like this is the negation, and writing one from a stem whose negation we have lost would be building the finding on the damaged part
- **Why:** This question requires one stated fact about what stomatal movement responds to, demonstrated by the options being four environmental variables of which three are named in the chapter's account of stomatal opening.
- **Note:** Stem damage: "Stomata] movement is M t affected by" for what must read "Stomatal movement is not affected by". The field negative_words_seen is empty as a result, so the polarity was not captured either. For the reviewer who holds the printed stem: under the negated reading the device to check is that all three wrong options are true factors, so a student who reads past the negation meets three correct statements, and the trap would sit on whichever of light or carbon dioxide the chapter emphasises in the stomatal-opening account. Nothing is recorded until the stem is repaired.
<!--/ecat-->

## Q117

Biology · botany · Anatomy of Flowering Plants

Stomata in grass leaf are

- (1) Barrel shaped
- **(2)** Dumb-bell shaped
- (3) Rectangular
- (4) Kidney shaped

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Grasses are monocots, so the shape of the stomata should be dumb-bell shaped.

**Solved independently** (answer withheld)

1. In grasses the stomatal guard cells are dumb-bell shaped (dicot guard cells are bean/kidney shaped), so the answer is option $2$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q117_e0e26bfc_03112026.png?v=e0e26bfcc498)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q117_21519388_03112026.png?v=2151938874b9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Guard cells are bean- or kidney-shaped in most leaves, but in the grasses they are dumb-bell shaped
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Kidney-shaped guard cells are what the standard stomatal diagram shows and what the sentence immediately before the grass case states, so a student who has the general picture and not the grass line answers from the drawing they have seen
- **Why:** This question requires one stated fact about a named group, demonstrated by the stem "Stomata in grass leaf are" with four cell shapes as the options.
<!--/ecat-->

## Q118

Biology · both · Cell: The Unit of Life

Which of the following is true for nucleolus?

- **(1)** It is a site for active ribosomal RNA synthesis.
- (2) Larger nucleoli are present in dividing cells.
- (3) It takes part in spindle formation.
- (4) It is a membrane-bound structure.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Site for ribosomal RNA synthesis.

**Solved independently** (answer withheld)

1. The nucleolus is the site of active ribosomal RNA ($\text{rRNA}$) synthesis, it is not membrane-bound, larger nucleoli occur in cells active in protein synthesis (not dividing cells), and it does not form the spindle, so only option $1$ is true.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q118_47243de6_03112026.png?v=47243de60151)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q118_0582152d_03112026.png?v=0582152daa88)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The nucleolus is a naked, non-membrane-bound mass inside the nucleus where ribosomal RNA is actively made, and it is largest in cells busy making protein
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The chapter's own sentence reads that larger and more numerous nucleoli are present in cells actively carrying out protein synthesis, and this option keeps the whole sentence and swaps the activity to cell division -- so a student recalling the shape of the line accepts it without testing which activity it named
- **Why:** This question requires one stated fact about a named structure, demonstrated by the stem "Which of the following is true for nucleolus?" with each option a rival whole claim.
<!--/ecat-->

## Q119

Biology · botany · Photosynthesis in Higher Plants

Which of the following is not a product of light reaction of photosynthesis?

- (1) Oxygen
- (2) ATP
- (3) NADPH
- **(4)** NADH

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. NADH is not the end product of light reactions.
2. ATP, NADPH, oxygen are formed at the end of light reactions.

**Solved independently** (answer withheld)

1. The light reaction makes $\mathrm{ATP}$ and $\mathrm{NADPH}$, and photolysis of water releases $\mathrm{O_2}$. $\mathrm{NADH}$ is not one of its products, so the answer is option $4$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q119_c534a103_03112026.png?v=c534a1032b53)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q119_3ffbeb61_03112026.png?v=3ffbeb613138)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The light reaction yields ATP, NADPH and oxygen; NADH belongs to respiration, and the single letter P is the whole difference between the two reduced coenzymes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  NADPH and NADH differ by one letter and sit next to each other in the option list, so a student who knows the light reaction makes a reduced coenzyme and is hunting for the one that is not a product reads the P into the wrong option; replace NADH with any unlike name and the question falls apart, which is the test that makes this a likeness trap
- **Why:** This question requires one stated fact about which products belong to the light reaction, demonstrated by "NADPH" and "NADH" being printed as separate options of a stem asking which is "not a product of light reaction".
<!--/ecat-->

## Q120

Biology · both · Cell Cycle and Cell Division

> ⚠ The independent solve chose (4); the booklet prints (2).

The stage during which separation of the paired homologous chromosomes begins is

- (1) Zygotene
- **(2)** Pachytene
- (3) Diakinesis
- (4) Diplotene

**Answer** — booklet: (2) · independent solve: (4) · differs

**Publisher's solution**

1. Separation of homologous chromosomes begins in pachytene.

**Solved independently** (answer withheld)

1. In prophase I, $\text{zygotene}$ is pairing (synapsis), $\text{pachytene}$ is crossing over, $\text{diplotene}$ is when the synaptonemal complex dissolves and the homologues begin to separate except at the chiasmata, and $\text{diakinesis}$ is terminalisation of chiasmata, so the answer is Diplotene, option $4$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q120_c5fdd267_03112026.png?v=c5fdd267cbef)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q120_d0b11aa8_03112026.png?v=d0b11aa8895c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The substages of prophase I run zygotene for pairing, pachytene for crossing over, diplotene for the dissolution of the synaptonemal complex, and diakinesis for terminalisation
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Zygotene is the stage at which paired homologous chromosomes come into being, and the stem's own words are "the paired homologous chromosomes", so a student matching the phrase to the stage it defines answers the question about pairing instead of the one about separation
- **Why:** This question requires one stated fact about which substage an event starts in, demonstrated by the stem asking for the stage "during which separation of the paired homologous chromosomes begins" with four substages of prophase I as the options.
- **Note:** KEY DOUBT, recorded and not acted on. Our record keys option 2, Pachytene, while the NCERT line this question is built on puts the beginning of the separation of the recombined homologues at diplotene, with the dissolution of the synaptonemal complex. The question is tagged as printed, as §7 requires. Because option 4, Diplotene, may in fact be the awarded option, no trap and no filler has been written for it; option 4 is deliberately left unassigned rather than being called a distractor. The trap on option 1 and the route on option 3 hold under either reading of the key, since pairing belongs to zygotene and terminalisation to diakinesis whichever of pachytene or diplotene is awarded. A repair task should re-read the printed answer line.
<!--/ecat-->

## Q121

Biology · both · Biomolecules

The two functional groups characteristic of sugars are

- **(1)** carbonyl and hydroxyl
- (2) hydroxyl and methyl
- (3) carbonyl and phosphate
- (4) carbonyl and methyl

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Carbonyl and hydroxyl are two functional groups found in carbohydrates.

**Solved independently** (answer withheld)

1. Sugars (carbohydrates) are polyhydroxy aldehydes or polyhydroxy ketones, i.e. they carry one carbonyl group ($\mathrm{C{=}O}$) and several hydroxyl groups ($-\mathrm{OH}$), so the answer is option $1$.

**Subtopic:** Chemical Constituents Of Living Cells · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q121_1708bfd8_03112026.png?v=1708bfd81c98)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q121_7d94003b_03112026.png?v=7d94003b2867)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A sugar is a polyhydroxy aldehyde or ketone, so hydroxyl groups plus one carbonyl are its two characteristic groups
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Carbonyl is the right half, and phosphate is carried in by the sugar-phosphate backbone and by glucose-6-phosphate, so the pair reads as the familiar one; phosphate is present only in sugar derivatives, not in the definition of a sugar.
- **Why:** This question requires the pair of functional groups the source states for sugars, demonstrated by every option pairing one genuine sugar group with a group belonging to another class -- 'carbonyl and phosphate', 'hydroxyl and methyl'.
- **Note:** half_right is used rather than nearby_fact because each option is a two-part pair and exactly one part fails, which is the case rule 2 reserves for this label.
<!--/ecat-->

## Q122

Biology · botany · Biological Classification

Which among the following is not a prokaryote?

- (1) Oscillatoria
- **(2)** Saccliaromyces
- (3) Nostoc
- (4) Mycobacterium

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Saccharomyces, is a unicellular prokaryote.

**Solved independently** (answer withheld)

1. Oscillatoria and Nostoc are cyanobacteria (Monera) and Mycobacterium is a bacterium, so all three are prokaryotes; Saccharomyces (yeast) is a fungus with a true nucleus, a eukaryote, so the answer is option $2$.

**Subtopic:** Kingdom Monera · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q122_5b323a65_03112026.png?v=5b323a65d83d)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q122_299ceb1b_03112026.png?v=299ceb1b5a67)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cyanobacteria such as Oscillatoria and Nostoc are prokaryotes despite the name blue-green algae; yeast is a eukaryotic fungus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The phrase blue-green algae is printed beside cyanobacteria in Kingdom Monera, and algae file under plants, so Oscillatoria reads as the one eukaryote in the list; the name is a legacy label on an organism with no nucleus.
- **Why:** This question requires the kingdom the source assigns to each named organism, demonstrated by the stem 'Which among the following is not a prokaryote?' against four named genera.
- **Note:** Swap test for nearby_fact against look_alike_term: replace 'Oscillatoria' with an unlike name and the trap survives, because the pull is the printed phrase blue-green algae rather than any resemblance to 'Saccharomyces'. Option 2 is printed as 'Saccliaromyces', an OCR corruption of Saccharomyces; it does not change the labels, but the spelling should be repaired.
<!--/ecat-->

## Q123

Biology · botany · Reproduction in Organisms

Offsets are produced by

- (1) Parthenogenesis
- (2) Meiotic divisions
- (3) Parthenocarpy
- **(4)** Mitotic divisions

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Mitotic divisions/vegetative propagation produce the offsets.

**Solved independently** (answer withheld)

1. An offset is a vegetative propagule, so it is a form of asexual reproduction (vegetative propagation) in which the new plant comes from somatic tissue of the parent, by mitotic cell division; parthenogenesis and parthenocarpy concern unfertilised eggs and fruits, and meiosis gives gametes, so the answer is option $4$.

**Subtopic:** Asexual Reproduction and Vegetative Propagation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q123_0b72d657_03112026.png?v=0b72d657ff1f)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q123_90959a4e_03112026.png?v=90959a4e047a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Vegetative propagules such as offsets are pieces of the parent body that grow by mitosis, so the offspring is a clone
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Meiosis is the division the reproduction chapters attach to producing new individuals, so 'produced by' pulls to the reduction division; an offset is a detached piece of the parent that grows on, which takes mitosis and yields a genetically identical plant.
- **Why:** This question requires the rule that vegetative propagation runs on mitosis applied to a named propagule, demonstrated by options that are division types and reproductive modes -- 'Meiotic divisions', 'Mitotic divisions' -- with no sentence about offsets to read off.
- **Note:** 'Mitotic' and 'meiotic' do resemble each other, but the swap test decides the other way: replace 'Meiotic divisions' with 'reduction division' and the trap survives, because what carries the student is meiosis being the division the chapter ties to reproduction. Hence nearby_fact, not look_alike_term. apply_rule rather than fact_line because the source names the offset as a propagule without stating which division makes it; the student must file it as vegetative and then apply the rule.
<!--/ecat-->

## Q124

Biology · both · Principles of Inheritance and Variation

Select the correct statement:

- (1) Transduction was discovered by S. Altman.
- (2) Franklin Stahl coined the term “linkage”
- (3) Spliceosomes take part in translation.
- **(4)** Punnett square was developed by a British scientist.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Punnett square was developed by British scientist name as Reginald Punnett and William Bateson

**Solved independently** (answer withheld)

1. Option $1$: transduction was discovered by Zinder and Lederberg; S. Altman is known for the catalytic RNA (ribozyme). False.
2. Option $2$: the term "linkage" was coined by T. H. Morgan; Franklin Stahl is known for the Meselson–Stahl experiment. False.
3. Option $3$: spliceosomes remove introns from hnRNA during post-transcriptional processing, not during translation. False.
4. Option $4$: the Punnett square was developed by Reginald C. Punnett, a British geneticist. True, so the answer is option $4$.

**Subtopic:** Monohybrid Cross · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q124_865f7596_03112026.png?v=865f7596bbe3)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q124_e0680a68_03112026.png?v=e0680a68cf7b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Who is credited with what in genetics, and where each machine acts: spliceosomes remove introns from pre-mRNA in the nucleus, not at translation
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The spliceosome works on mRNA, and a student who files everything done to mRNA under making protein puts it in translation; splicing happens on the pre-mRNA inside the nucleus, before the transcript reaches a ribosome.
- **Why:** This question requires each printed claim judged against the attribution or stage the source states, demonstrated by options that are standalone sentences -- 'Spliceosomes take part in translation.', 'Punnett square was developed by a British scientist.'
- **Note:** qtype is statements because no lettered block is printed and each option is a full claim to be graded; the retired pattern label statement_options maps here. wrong_site_attacked is preferred over nearby_fact for option 3 because the machine named is the right one and only its stage has moved.
<!--/ecat-->

## Q125

Biology · botany · Sexual Reproduction in Flowering Plants

Which of the following has proved helpful in preserving pollen as fossils?

- **(1)** Sporopollenin
- (2) Pollenkitt
- (3) Oil content
- (4) Cellulosic intine

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Sporopollenin is found in the outer layer of pollen and is preserved in soil and sediments.

**Solved independently** (answer withheld)

1. The outer wall (exine) of a pollen grain is made of $\text{sporopollenin}$, one of the most resistant organic materials known: it withstands high temperatures, strong acids and alkalis, and no known enzyme degrades it. This is why pollen is well preserved as fossils, so the answer is option $1$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q125_2b19d5ea_03112026.png?v=2b19d5ea111e)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q125_27205144_03112026.png?v=272051446668)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sporopollenin in the exine is the most resistant organic material known, which is why pollen grains survive as fossils
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Exine and intine are printed in the same sentence of the pollen-wall account, so a student holding 'the wall has a tough layer and a cellulose layer' reaches for the inner one; the resistant material is sporopollenin in the exine, and cellulose is readily digested.
- **Why:** This question requires the named material the source credits with pollen's resistance, demonstrated by the stem 'has proved helpful in preserving pollen as fossils' set against four pollen-wall materials.
- **Note:** fact_line rather than reason_line: the answer asked for is the named substance and its function, which the brief places under fact_line, even though the source states the resistance in the same sentence.
<!--/ecat-->

## Q126

Biology · both · Principles of Inheritance and Variation

Which of the following pairs is wrongly matched?

- (1) T .H. Morgan : Linkage
- **(2)** Starch synthesis in pea : Multiple alleles
- (3) XO type sex determination : Grasshopper
- (4) ABO blood grouping : Co-dominance

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Starch synthesis in pea is not an example of multiple alleles.

**Solved independently** (answer withheld)

1. T. H. Morgan worked out linkage in $Drosophila$, so option $1$ is correctly matched.
2. Starch synthesis in pea is controlled by one gene with two alleles $B$ and $b$; $BB$ gives large grains, $bb$ small, and $Bb$ intermediate, so NCERT uses it for incomplete dominance (dominance being trait-dependent), not multiple alleles. Option $2$ is wrongly matched.
3. Grasshopper males are $XO$ and females $XX$, so option $3$ is correctly matched.
4. In ABO grouping $I^A$ and $I^B$ are both expressed in $I^AI^B$ (blood group AB), which is co-dominance, so option $4$ is correctly matched.
5. The only wrongly matched pair is option $2$.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q126_475556b9_03112026.png?v=475556b9299d)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q126_10475c67_03112026.png?v=10475c6752b3)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** ABO blood grouping illustrates both multiple alleles and co-dominance, while starch-grain size in pea is the incomplete-dominance case, not a multiple-allele one
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  ABO is the chapter's headline example of multiple alleles, so that property comes first and the printed partner co-dominance looks like the substitution; ABO carries both, because I-A and I-B are both expressed in an AB individual.
- **Why:** This question requires each printed pair checked against the concept the source attaches to it, demonstrated by the stem 'Which of the following pairs is wrongly matched?' with options such as 'ABO blood grouping : Co-dominance'.
- **Note:** E1's pattern read this as statement_options; the printed options are name-to-concept pairs judged whole, which the rulebook calls pair_options, and both retired labels map to the current qtype statements, so the shape disagreement does not change the tag. The trap sits on a correctly matched pair, which is what a 'wrongly matched' stem makes available.
<!--/ecat-->

## Q127

Biology · both · Molecular Basis of Inheritance

Select the correct match :

- **(1)** Francois Jacob and Jacques Monod – Lac operon
- (2) Alec Jeffreys – Streptococcus pneumoniae
- (3) Matthew Meselson and F. Stahl – Pisum sativum
- (4) Alfred Hershey and Martha Chase – TMV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The Discovery of the lac Operon.
2. In 1961, Francois Jacob and Jacques Monod proposed the operon model of gene regulation in bacteria.
3. The model was based on their study of the genes in E. coli that code for enzymes that affect the breakdown of lactose.
4. Francois Jacob and Jacques Monod.

**Solved independently** (answer withheld)

1. Francois Jacob and Jacques Monod first described the $lac$ operon in \textit{E. coli}, so option $1$ is a correct match.
2. Alec Jeffreys developed DNA fingerprinting; \textit{Streptococcus pneumoniae} was used by Griffith, so option $2$ is wrong.
3. Meselson and Stahl showed semi-conservative replication in \textit{E. coli}, not \textit{Pisum sativum}, so option $3$ is wrong.
4. Hershey and Chase used bacteriophage (T2) infecting \textit{E. coli}, not TMV, so option $4$ is wrong; the answer is option $1$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q127_a3012d90_03112026.png?v=a3012d9031f7)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q127_6c909dc6_03112026.png?v=6c909dc6a406)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each landmark experiment of this chapter goes with the organism or system it was done on: Jacob and Monod with the lac operon, Hershey and Chase with bacteriophage, Meselson and Stahl with E. coli, Griffith with Streptococcus pneumoniae
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Hershey and Chase are remembered as the pair who worked with a virus, and TMV is the other virus of the course, so a student holding the category rather than the name accepts it; their experiment was on bacteriophage T2, and TMV belongs to the tobacco mosaic work
- **Why:** This question requires one stated attribution, demonstrated by each option being a scientist joined to an organism or system -- "Alfred Hershey and Martha Chase - TMV" -- accepted or rejected whole.
- **Note:** The pattern classifier recorded match_the_lists, but no two columns are printed and there is no pairing code: list_i and list_ii are both empty and each option is itself a PAIR judged whole, which is the printed shape pair_options. The retired-value map in config/allowed_values.yaml sends pair_options to qtype statements, which is what is recorded here.
<!--/ecat-->

## Q128

Biology · botany · Reproduction in Organisms

Which of the following flowers only once in its life-time?

- (1) Papaya
- **(2)** Bamboo species ·
- (3) Mango
- (4) Jackfruit

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Most bamboo plants flower once in a life cycle of about $40$ to $50$ years.

**Solved independently** (answer withheld)

1. Bamboo species flower only once in their life-time (usually after $50$-$100$ years), produce large numbers of fruits and die, while papaya, mango and jackfruit flower year after year, so the answer is option $2$.

**Subtopic:** Phases of Life Cycle: Juvenile and Reproductive Phase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q128_78bf5a41_03112026.png?v=78bf5a41b3fc)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q128_d2f5db79_03112026.png?v=d2f5db79b793)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bamboo flowers only once in its life, generally after fifty to a hundred years, and then fruits and dies
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The three distractors are mango, papaya and jackfruit, all of which a student has seen flower and fruit season after season, so no remembered fact attaches a once-in-a-lifetime flowering to any of them. I also tested the one misreading available, "only once" taken as "once a year", which would point at the mango: the stem's own words are "only once in its life-time", and even under that misreading the papaya, which flowers more or less continuously, and the jackfruit would still have to be ruled out by the same everyday knowledge that rules out the mango -- so the misreading does not single out a printed option.
- **Why:** This question requires one stated fact about a named group, demonstrated by the stem asking which "flowers only once in its life-time" with four plants as the options and no criterion printed to apply.
<!--/ecat-->

## Q129

Biology · both · Molecular Basis of Inheritance

The experimental proof for. semiconservative replication of DNA was first shown in a

- (1) Virus
- (2) Fungus.
- (3) Plant
- **(4)** Bacterium

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The proof for semi-conservative replication was conducted on E.coli, which is a bacterium.

**Solved independently** (answer withheld)

1. Meselson and Stahl (1958) first showed semiconservative replication experimentally by growing $E.\ coli$ in $^{15}NH_4Cl$, then transferring it to $^{14}NH_4Cl$ and separating the DNA by $CsCl$ density-gradient centrifugation; $E.\ coli$ is a bacterium, so the answer is option $4$.

**Subtopic:** Experimental Proof that DNA is Semiconservative · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q129_c70ed124_03112026.png?v=c70ed124d852)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q129_e926265c_03112026.png?v=e926265c09d7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Semiconservative replication was first demonstrated by Meselson and Stahl in Escherichia coli, and only afterwards repeated in a plant
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The chapter states that the experiment was repeated on Vicia faba by Taylor and colleagues, so a student who remembers the plant demonstration and reads past the word "first" answers with the plant; drop "first" from the stem and this option becomes true
- **Why:** This question requires one stated fact under the stem's own qualifier, demonstrated by the words "was first shown in a" with four kinds of organism as the options.
<!--/ecat-->

## Q130

Biology · both · Biotechnology and Its Applications

Which of the following is commonly used as a vector for introducing a DNA fragment in human lymphocytes?

- (1) pBR 322
- **(2)** Retrovirus
- (3) A phage
- (4) Ti plasmid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Retroviruses are used for introducing DNA fragments in human lymphocytes.

**Solved independently** (answer withheld)

1. Retroviruses infect animal cells and integrate their genome into the host, so disarmed retroviruses serve as vectors for human cells such as lymphocytes (option $2$); pBR322 and phage $\lambda$ are used for E. coli, and the Ti plasmid of Agrobacterium is used for plants.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q130_ab9f65fa_03112026.png?v=ab9f65fa4b4d)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q130_4b45abaf_03112026.png?v=4b45abafb3c2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A vector has to be able to enter the host it is meant for: a retroviral vector delivers the gene into human lymphocytes, while pBR322 clones in E. coli and the Ti plasmid transforms plant cells
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  pBR322 is the vector the chapter teaches in detail, with its two antibiotic-resistance genes, its ori and its labelled map, so a student asked to name a vector names the one they have drawn; it is a plasmid for cloning in E. coli and cannot carry a gene into a human cell
- **Why:** This question requires one stated fact pairing a vector with its host, demonstrated by the stem naming "human lymphocytes" with four vectors as the options.
- **Note:** Option 3 is stored as "A phage", which is the lambda phage of the vector section rendered with its Greek letter lost. The option is identifiable and the key is unaffected.
<!--/ecat-->

## Q131

Biology · both · Molecular Basis of Inheritance

Select the correct match :

- (1) G. Mendel – Transformation
- **(2)** Ribozymo – Nucleic acid
- (3) T.H. Morgan – Transduction
- (4) $\mathrm{F_2}$ x Recessive parent – Dihybrid cross

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Ribozyme are nucleic acid molecules that are capable of catalysing different reactions.

**Solved independently** (answer withheld)

1. Option $1$: transformation was discovered by Griffith, not $\text{Mendel}$, so the match is wrong.
2. Option $2$: a ribozyme is an RNA molecule with catalytic activity, so it is a nucleic acid and the match is correct.
3. Option $3$: $\text{T.H. Morgan}$ is known for linkage and recombination; transduction was found by Zinder and Lederberg, so the match is wrong.
4. Option $4$: crossing an offspring with the recessive parent is a test cross, not a dihybrid cross, so the match is wrong.
5. Only option $2$ is a correct match.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q131_10e4ff41_03112026.png?v=10e4ff418cb1)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q131_af5fa9af_03112026.png?v=af5fa9af4f1a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A ribozyme is a nucleic acid that acts as a catalyst, which is why RNA could be both genetic material and enzyme in the RNA world
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Crossing with the recessive parent is the move a student recognises, because it is the test cross, and the recognisable fragment vouches for the rest of the pairing, so neither the generation nor the name printed beside it gets checked
- **Why:** This question requires one stated pairing recognised whole, demonstrated by each option being a term joined to a partner -- "Ribozymo - Nucleic acid" -- accepted or rejected together.
- **Note:** The pattern classifier recorded match_the_lists, but list_i and list_ii are both empty, no two columns are printed and the answer is not a pairing code: each option is itself a PAIR judged whole, which is the printed shape pair_options, mapped to qtype statements by config/allowed_values.yaml. The keyed option is stored as "Ribozymo" for ribozyme, which is transcription debris that does not change what is being matched.
<!--/ecat-->

## Q132

Biology · both · Biotechnology and Its Applications

Use of bioresources by multinational companies and organisations without authorisation from the concerned country and its people is called

- (1) Bioexploitaion
- (2) Bio-infringement
- (3) Biodegradation
- **(4)** Biopiracy

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Biopiracy is defined as the practice of commercially exploiting naturally occurring biochemical or genetic material, especially by obtaining patents that restrict its future use, while failing to pay fair compensation to the community from which it originates.

**Solved independently** (answer withheld)

1. Biopiracy is the use of bioresources by multinational companies and organisations without proper authorisation from, or compensatory payment to, the countries and people concerned, so the answer is option $4$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q132_406aaa8d_03112026.png?v=406aaa8d3d0b)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q132_77a29576_03112026.png?v=77a295761276)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biopiracy is the name for the use of bioresources by companies or organisations without authorisation from the country and people they came from
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Two of the three distractors, "Bioexploitaion" and "Bio-infringement", are not terms this material prints anywhere; reaching either needs the absence of the word biopiracy rather than any remembered fact, which is why the retired-value map sends a fabricated term to no trap. The third, Biodegradation, is a real term with a stated meaning of its own, the breaking down of waste by micro-organisms, and nothing in the stem's definition of unauthorised use of bioresources touches it. I checked the stem for any word a distractor could be built on and it supplies only "without authorisation", which is what the keyed term names.
- **Why:** This question requires one stated definition, demonstrated by the stem spelling the definition out -- "Use of bioresources ... without authorisation from the concerned country and its people is called" -- with four terms as the options.
<!--/ecat-->

## Q133

Biology · both · Biotechnology and Its Applications

A 'new' variety of rice was patented by a foreign company, though such varieties have been present in India for a long time. This is related to

- **(1)** Basmati
- (2) Co-067
- (3) Lerma Rojo
- (4) Sbarbati Sonora

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Basmati patent case is won by India but the trademark issue remains.

**Solved independently** (answer withheld)

1. The NCERT biopiracy example is the 1997 US patent given to an American company for Basmati rice, which has been grown in India for a very long time, so the answer is option $1$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q133_ad4669b4_03112026.png?v=ad4669b46706)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q133_bc556be9_03112026.png?v=bc556be9fb99)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biopiracy: a foreign company took a patent on Basmati, a rice landrace Indian farmers had already grown for generations
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Sharbati Sonora is the other variety the book presents as a new variety built out of an older one, so a student who stored that breeding story and not the patent story lands on it.
- **Why:** This question requires the single NCERT line naming the Indian variety a foreign company patented, demonstrated by the stem's "such varieties have been present in India for a long time" set against four bare variety names with no criterion printed to apply to them.
- **Note:** Option 4 is printed "Sbarbati Sonora", which reads as a mis-rendering of "Sharbati Sonora"; tagged as printed. I could not confirm from the record which crop "Co-067" names. If it is a rice variety it would be the stronger trap, since it would then be the only other rice on a stem that says rice, so a reviewer with the variety list should re-check that option before this trap is relied on.
<!--/ecat-->

## Q134

Biology · both · Biotechnology and Its Applications

In India, the organisation responsible for assessing the safety of introducing genetically modified organisms for public use is

- **(1)** Genetic Engineering Appraisal Committee (GEAC)
- (2) Indian Council of Medical Research (ICMR)
- (3) Research Committee on Genetic Manipulation (RCGM)
- (4) Council for Scientific and Industrial Research (CSIR)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. GEAC is involved in assessing the safety of introducing genetically modified organisms for public use.

**Solved independently** (answer withheld)

1. As NCERT Class 12 teaches, the Indian Government set up the Genetic Engineering Appraisal Committee (GEAC), which makes decisions about the validity of GM research and the safety of introducing GM organisms for public services, so the answer is option $1$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q134_fa187a39_03112026.png?v=fa187a39d208)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q134_0caa9e0a_03112026.png?v=0caa9e0aa99a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** GEAC is the Indian body that decides whether a genetically modified organism is safe to release for public use
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Both the key and this option are committees named after genetic engineering or genetic manipulation, so a student holding only 'the committee with genetics in its name clears GMOs' picks the one whose name repeats the stem's own subject.
- **Why:** This question requires the stated name of the regulatory body, demonstrated by the stem's "the organisation responsible for assessing the safety of introducing genetically modified organisms for public use" with four organisation names as the options. Test applied for the trap label: substituting an unlike name for option 3 while keeping a GM-oversight remit kills the pull, because the pull is the printed words 'Genetic Manipulation' echoing the stem, so the resemblance and not the position is doing the work.
- **Note:** E1 called this statement_options, decided on option length; the printed options are bare organisation names rather than statements to be judged, so the shape recorded here is mcq. Option 1 prints "Appraisal" where NCERT prints "Approval" and option 3 prints "Research Committee" where the body is generally "Review Committee"; both recorded as printed, key untouched.
<!--/ecat-->

## Q135

Biology · both · Biotechnology: Principles and Processes

The correct order of steps in Polymerase Chain Reaction (PCR) is

- **(1)** Denaturation, Annealing, Extension
- (2) Extension, Denaturation, Annealing
- (3) Denaturation, Extension, Annealing
- (4) Annealing, Extension, Denaturation

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Denaturation is the first step of PCR, the annealing and finally extension.

**Solved independently** (answer withheld)

1. A PCR cycle runs $\text{Denaturation} \rightarrow \text{Annealing} \rightarrow \text{Extension}$: heat separates the DNA strands, primers anneal to the single strands, and Taq polymerase extends them. This is option $1$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q135_fd119c1d_03112026.png?v=fd119c1d3085)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q135_822b9c6a_03112026.png?v=822b9c6a829a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A PCR cycle runs denaturation, then annealing, then extension, because primers cannot bind until the strands separate and the polymerase cannot extend until a primer is bound
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Denaturation first is secure, and then extension is remembered as the polymerase's main job and promoted to second place, which puts the two dependent steps in inverted order.
- **Why:** This question requires the taught sequence of the three PCR steps, demonstrated by the stem's "The correct order of steps" and four options that print the same three names in different orders.
- **Note:** E1 called this arrange_in_order, which maps onto qtype mcq through category_retired.qtype; the printed shape is a plain four-option question. half_right was ruled out for option 3: the option is not a compound claim with one part false but an ordering, and what fails in it is the annealing-to-extension direction, which is what reversed names.
<!--/ecat-->

## Q136

Chemistry · organic · Alcohols, Phenols and Ethers

Identify the major products P, Q and are in the following sequence of reactions:

![printed figure: benzene + 1-chloropropane ($\ce{CH3CH2CH2Cl}$) →(Anhydrous $\ce{AlCl3}$); P →((i) $\ce{O2}$, (ii) $\ce{H3O+}$/Δ) Q + R](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q136_202ccd88_03112026.png?v=202ccd88d1aa)

*benzene + 1-chloropropane ($\ce{CH3CH2CH2Cl}$) →[Anhydrous $\ce{AlCl3}$]; P →[(i) $\ce{O2}$, (ii) $\ce{H3O+}$/Δ] Q + R*

Structures: benzene `c1ccccc1`; 1-chloropropane `CCCCl`

- **(1)** isopropylbenzene `CC(C)c1ccccc1`; phenol `Oc1ccccc1`; propan-2-one `CC(C)=O`
- (2) propylbenzene `CCCc1ccccc1`; benzaldehyde `O=Cc1ccccc1`; ethanol `CCO`
- (3) isopropylbenzene `CC(C)c1ccccc1`; phenol `Oc1ccccc1`; propan-2-ol `CC(C)O`
- (4) propylbenzene `CCCc1ccccc1`; benzaldehyde `O=Cc1ccccc1`; benzoic acid `O=C(O)c1ccccc1`

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: benzene + 1-chloropropane →($\ce{AlCl3}$) isopropylbenzene P; P →(i)$\ce{O2}$, i) $\ce{H3O+}$) phenol Q + propan-2-one R](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q136_sol_1_a67dfbf2_03112026.svg?v=a67dfbf223ad)

*benzene + 1-chloropropane →[$\ce{AlCl3}$] isopropylbenzene P; P →[i)$\ce{O2}$, i) $\ce{H3O+}$] phenol Q + propan-2-one R*

![drawn: benzene + 1-chloropropane →($\ce{AlCl3}$) isopropylbenzene P; P →(i)$\ce{O2}$, i) $\ce{H3O+}$) phenol Q + propan-2-one R](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q136_solution_1_5750e473_03112026.svg?v=5750e473f557)  
*drawn on the booklet's geometry, checked against its SMILES*

1. The above reaction is a cumene reaction . Hence the correct option is 1

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2Cl} + \mathrm{AlCl_3} \rightarrow \mathrm{CH_3CH_2CH_2^{+}} + \mathrm{AlCl_4^{-}}$.
2. The primary carbocation undergoes a 1,2-hydride shift to the more stable secondary carbocation: $\mathrm{CH_3CH_2CH_2^{+}} \rightarrow \mathrm{(CH_3)_2CH^{+}}$.
3. Electrophilic substitution on benzene gives $P = \mathrm{C_6H_5CH(CH_3)_2}$ (cumene).
4. Air oxidation: $\mathrm{C_6H_5CH(CH_3)_2} + \mathrm{O_2} \rightarrow \mathrm{C_6H_5C(CH_3)_2OOH}$ (cumene hydroperoxide).
5. Acid hydrolysis with rearrangement: $\mathrm{C_6H_5C(CH_3)_2OOH} \xrightarrow{\mathrm{H_3O^+}/\Delta} \mathrm{C_6H_5OH} + \mathrm{CH_3COCH_3}$, so $Q$ = phenol and $R$ = acetone.
6. Cumene, phenol and $\mathrm{CH_3-CO-CH_3}$ is option $1$.

**Subtopic:** Preparation of Phenols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q136_7e9e69bd_03112026.png?v=7e9e69bd45d1)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q136_45779694_03112026.png?v=457796942449)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Friedel-Crafts alkylation with 1-chloropropane rearranges to the isopropyl cation and so gives cumene, whose air oxidation and acid hydrolysis split into phenol and acetone.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings, so there is no option text in which a pull could be named or tested.
- **Why:** This question requires the products of a printed two-step scheme, demonstrated by the arrows reading 'Anhydrous $\mathrm{AlCl_3}$' and '(i) $\mathrm{O_2}$, (ii) $\mathrm{H_3O^+}$/heat' over P and Q + R.
- **Note:** options_en holds four empty strings: the paper prints the options as structures and none was captured, so no option can be named. The scheme itself is stored in figure_image.text (benzene plus $\mathrm{CH_3CH_2CH_2Cl}$ over anhydrous $\mathrm{AlCl_3}$ to P, then O2 and acid to Q + R) and the stored stem reads 'P, Q and are', with R lost. The stem asks for three products in one answer, so the shape recorded is two_part; E1's pattern read 'sequence of reactions' as arrange_in_order, which is not an ordering task. A reviewer holding the options should check whether n-propylbenzene is offered as P, since the rearrangement of the primary chain to isopropyl is what the first step turns on.
<!--/ecat-->

## Q137

Chemistry · organic · Biomolecules

Which of the following compounds can form a zwitterion?

- **(1)** Glycine
- (2) Aniline
- (3) Benzoic acid
- (4) Acetanilide

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: glycine: 2-azaniumylacetate ($\ce{H3N+-CH2-COO-}$, zwitterion)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q137_sol_1_c165e39b_03112026.svg?v=c165e39b77a9)

*glycine: 2-azaniumylacetate ($\ce{H3N+-CH2-COO-}$, zwitterion)*

![drawn: glycine: 2-azaniumylacetate ($\ce{H3N+-CH2-COO-}$, zwitterion)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q137_solution_1_fc448be4_03112026.svg?v=fc448be4eec0)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Amino acids can form zwitter ion , i.e. dipolar ion
2. Hence the correct option is 1

**Solved independently** (answer withheld)

1. A zwitterion needs an acidic group and a basic group in the same molecule, so that a proton moves from one to the other.
2. Glycine, $\mathrm{H_2N{-}CH_2{-}COOH}$, has both: $\mathrm{H_2N{-}CH_2{-}COOH \rightarrow H_3\overset{+}{N}{-}CH_2{-}COO^-}$.
3. Aniline ($\mathrm{C_6H_5NH_2}$) has only a basic group, benzoic acid ($\mathrm{C_6H_5COOH}$) only an acidic group, and acetanilide ($\mathrm{C_6H_5NHCOCH_3}$) has a non-basic amide N and no acidic group.
4. So only glycine forms a zwitterion, which is option $1$.

**Subtopic:** Proteins Classification and Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q137_91c555c1_03112026.png?v=91c555c15256)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q137_8b0b73bd_03112026.png?v=8b0b73bd20c9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A zwitterion needs an acidic and a basic group in the same molecule, which is why an amino acid such as glycine carries $-\mathrm{COO^-}$ and $-\mathrm{NH_3^+}$ at once.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The zwitterion is remembered through its nitrogen half, the protonated amine, and aniline is the one compound in the list with a free $-\mathrm{NH_2}$ to protonate - but the proton has to come from an acid group in the same molecule.
- **Why:** This question requires the stated fact that amino acids exist as zwitterions, demonstrated by glycine being the one option carrying both $-\mathrm{COOH}$ and $-\mathrm{NH_2}$.
- **Note:** nearby_fact rather than look_alike_term: glycine and aniline are not alike as names, and replacing the pair with two unlike words leaves the route alive, because what carries it is aniline holding one of the two groups the rule needs.
<!--/ecat-->

## Q138

Chemistry · inorganic · Coordination Compounds – Practice

The geometry and magnetic behaviour of the complex $[\mathrm{Ni(Co)_4}]$ are

- (1) tetrahedral geometry and paramagnetic
- (2) square planar geometry and diamagnetic
- (3) ‘square planar geometry and paramagnetic
- **(4)** tetrahedral geometry and diamagnetic

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $[\mathrm{Ni(CO)4}]$ is diamagnetic and assumes tetrahedral structure.
2. Carbonyl is a strong ligand and involves force pairing.
3. Hence correct option is $4$

**Solved independently** (answer withheld)

1. In $[\mathrm{Ni(CO)_4}]$ each CO is neutral, so the oxidation state of Ni is $0$.
2. Ground state $\mathrm{Ni}(0)$: $[\mathrm{Ar}]\,3d^{8}\,4s^{2}$.
3. CO is a strong-field ligand, so the $4s$ electrons are pushed into $3d$, giving $3d^{10}\,4s^{0}$.
4. The four CO ligands donate into the empty $4s$ and three $4p$ orbitals: $sp^{3}$ hybridisation, so the geometry is tetrahedral.
5. With $3d^{10}$ all electrons are paired, so the number of unpaired electrons is $0$ and the complex is diamagnetic.
6. Tetrahedral and diamagnetic is option $4$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q138_0ba431d2_03112026.png?v=0ba431d29157)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q138_9e18faa5_03112026.png?v=9e18faa54cc5)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In $\mathrm{Ni(CO)_4}$ nickel is zero-valent and pairs up to 3d$^{10}$4s$^0$, so sp$^3$ hybridisation gives a tetrahedral molecule with no unpaired electron.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The geometry half is worked out correctly as tetrahedral, and then nickel is assumed to keep the unpaired d electrons it has in $\mathrm{Ni^{2+}}$ complexes, so the magnetic half fails and the whole option goes with it.
- **Why:** This question requires geometry and magnetic behaviour to be settled together from the metal's oxidation state, demonstrated by each option pairing one geometry with one magnetic behaviour.
- **Note:** The stem is stored as '[Ni(Co)_4]', with the carbonyl ligand CO carrying a lower-case o, and option 3 carries a stray opening quote. E1 called this statement_options; each option is two halves that must both hold, so the shape recorded is two_part.
<!--/ecat-->

## Q139

Chemistry · inorganic · Coordination Compounds – Practice

> ⚠ The independent solve chose (4); the booklet prints (1).

Iron carbonyl, $\mathrm{Fe(CO)_5}$ is

- **(1)** dinuclear
- (2) tetranuclear
- (3) trinuclear
- (4) monomuclear

**Answer** — booklet: (1) · independent solve: (4) · differs

**Publisher's solution**

1. $\mathrm{Fe(CO)_5}$ is ferrocene and is dinuclear complex

![printed figure: ferrocene (sandwich structure: Fe between two cyclopentadienyl rings)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q139_sol_1_3286f8aa_03112026.png?v=3286f8aace87)

*ferrocene (sandwich structure: Fe between two cyclopentadienyl rings)*

2. Hence the correct option is 1

**Solved independently** (answer withheld)

1. $\mathrm{Fe(CO)_5}$ contains only one Fe atom, bonded to five terminal CO ligands in a trigonal bipyramidal arrangement, with no metal-metal bond, so it is mononuclear, which is option $4$.

**Subtopic:** Bonding in Coordination Compounds and Metal Carbonyls · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q139_3d1a3237_03112026.png?v=3d1a3237ff92)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q139_154c05ce_03112026.png?v=154c05ce0778)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Iron pentacarbonyl has one iron atom at the centre of a trigonal bipyramid of five CO ligands, so it is mononuclear.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stored key names option 1, 'dinuclear', while the printed formula $\mathrm{Fe(CO)_5}$ carries a single iron and the stored option 4 reads 'monomuclear'; with the key index and the stored option order disagreeing, no option can be tested for a pull.
- **Why:** This question requires the nuclearity to be read off the printed formula, demonstrated by '$\mathrm{Fe(CO)_5}$' carrying one metal symbol against options naming one, two, three and four metal centres.
- **Note:** Tagged as printed, following the rule that the key is not re-judged at this step. The option the formula supports is the one stored as 'monomuclear', itself OCR-damaged; the dinuclear carbonyl of iron is $\mathrm{Fe_2(CO)_9}$. The nuclearity set is otherwise intact, so the fault sits in the pairing of key index to option text rather than in the question.
<!--/ecat-->

## Q140

Chemistry · inorganic · The D- and F-Block Elements – Practice

Match the metal ions given in column I with the spin magnetic moments of the ions given in Column II and assign the correct code:

| List-I | | List-II | |
|---|---|---|---|
| a | $\mathrm{Co^{3+}}$ | i | $\sqrt{8}\,\mathrm{B.\,M}$ |
| b | $\mathrm{Cr^{3+}}$ | ii | $\sqrt{35}\,\mathrm{B.\,M}$ |
| c | $\mathrm{Fe^{3+}}$ | iii | $\sqrt{3}\,\mathrm{B.\,M}$ |
| d | $\mathrm{Ni2^{+}}$ | Iv | $\sqrt{24}\,\mathrm{B.\,M}$ |
|  |  | V | $15\,\mathrm{B.\,M}$ |

- (1) a-iii, b-v, c-i, d-ii
- **(2)** a-iv, b-v, c-ii, d-i
- (3) a-iv, b-I, c-ii, d-iii
- (4) a-i, b-ii, c-iii, d-iv

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Co^{3+}}$ contains $4$ unpaired electrons, $\mu = \sqrt{24}\,\mathrm{B.M.}$
2. $\mathrm{Cr^{3+}}$ contains $3$ unpaired electrons, $\mu = \sqrt{15}\,\mathrm{B.M.}$
3. $\mathrm{Fe^{3+}}$ contains $5$ unpaired electrons, $\mu = \sqrt{35}\,\mathrm{B.M.}$
4. $\mathrm{Ni^{2+}}$ contains $2$ unpaired electrons, $\mu = \sqrt{8}\,\mathrm{B.M.}$
5. Therefore the correct option is 2

**Solved independently** (answer withheld)

1. Spin-only magnetic moment: $\mu = \sqrt{n(n+2)}\,\mathrm{B.M}$, where $n$ is the number of unpaired electrons (free ions).
2. $\mathrm{Co^{3+}}$: $[\mathrm{Ar}]3d^6$, $n = 4$, $\mu = \sqrt{4 \times 6} = \sqrt{24}\,\mathrm{B.M}$, so a-iv.
3. $\mathrm{Cr^{3+}}$: $[\mathrm{Ar}]3d^3$, $n = 3$, $\mu = \sqrt{3 \times 5} = \sqrt{15}\,\mathrm{B.M}$, so b-v.
4. $\mathrm{Fe^{3+}}$: $[\mathrm{Ar}]3d^5$, $n = 5$, $\mu = \sqrt{5 \times 7} = \sqrt{35}\,\mathrm{B.M}$, so c-ii.
5. $\mathrm{Ni^{2+}}$: $[\mathrm{Ar}]3d^8$, $n = 2$, $\mu = \sqrt{2 \times 4} = \sqrt{8}\,\mathrm{B.M}$, so d-i.
6. The match a-iv, b-v, c-ii, d-i is option $2$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q140_89a140c6_03112026.png?v=89a140c67b96)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q140_97bf804e_03112026.png?v=97bf804e795e)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spin-only moment is $\mu=\sqrt{n(n+2)}$ B.M., where $n$ is the number of unpaired 3d electrons left once the ion's charge has been taken off.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  $\mathrm{Co^{3+}}$ and $\mathrm{Fe^{3+}}$ are computed correctly as $\sqrt{24}$ and $\sqrt{35}$, and the other two ions are then given d-counts recalled from the ion next door - d$^9$, which is $\mathrm{Cu^{2+}}$'s count, for $\mathrm{Ni^{2+}}$, giving $\sqrt{3}$.
- **Why:** This question requires the spin-only moment to be computed for each ion, demonstrated by column II listing $\sqrt{8}$, $\sqrt{35}$, $\sqrt{3}$ and $\sqrt{24}$ B.M., which are $\sqrt{n(n+2)}$ for n = 2, 5, 1 and 4.
- **Note:** Column II item v is stored as '15 B.M' with the radical lost; the key's b-v pairing only works as $\sqrt{15}$ B.M. for $\mathrm{Cr^{3+}}$ (3d$^3$, n = 3). Option 3 is stored as 'b-I' and is read here as b-i ($\sqrt{8}$), since a-iv already carries iv in the same code. Column I item d is stored as 'Ni2+'. The key, option 2, is confirmed by the formula for all four ions, so the question is tagged as printed.
<!--/ecat-->

## Q141

Chemistry · inorganic · Coordination Compounds – Practice

The type of isomerism shown by the complex $\mathrm{[CoCl_2(en)_2]}$ is.

- (1) Linkage isomerism
- **(2)** Geometrical isomerism
- (3) Ionization isomerism
- (4) Coordination isomerism

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $[\mathrm{CoCl_2(en)_2}]$ shows geometrical isomerism
2. Hence the correct option is 2

**Solved independently** (answer withheld)

1. $\mathrm{[CoCl_2(en)_2]}$ is an octahedral complex of type $\mathrm{M(AA)_2B_2}$, with $\mathrm{en}$ bidentate and two monodentate $\mathrm{Cl^-}$.
2. The two $\mathrm{Cl^-}$ ligands can sit adjacent (cis) or opposite (trans), so the complex shows geometrical isomerism.
3. $\mathrm{Cl^-}$ and $\mathrm{en}$ are not ambidentate, so linkage isomerism is ruled out.
4. There is no counter-ion to exchange with a ligand and no second complex ion, so ionization and coordination isomerism are ruled out; the answer is option $2$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q141_c1c4212d_03112026.png?v=c1c4212d4686)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q141_922e7845_03112026.png?v=922e78459342)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $\mathrm{[CoCl_2(en)_2]}$ is an octahedral $\mathrm{MA_2B_2}$ complex, so its two chlorides can sit next to each other or opposite - cis-trans, that is geometrical, isomerism.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The two chlorides look like the ligand that trades places with the counter-ion in the taught example, but ionisation isomerism needs an ion written outside the square brackets and this formula has nothing outside them.
- **Why:** This question requires each isomerism type's requirement to be tested against the printed formula, demonstrated by '$\mathrm{[CoCl_2(en)_2]}$' having nothing outside the brackets, one metal centre and no ambidentate ligand.
<!--/ecat-->

## Q142

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which one of the following ions exhibits d-d transition and paramagnetism as well?

- **(1)** $\mathrm{MnO_4^{2-}}$
- (2) $\mathrm{CrO_4^{2-}}$
- (3) $\mathrm{MnO_4^{-}}$
- (4) $\mathrm{Cr_2O_7^{2-}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{MnO_4^{2-}}$ , the oxidation state of $\mathrm{Mn}$ is $+6$.
2. It will have one unpaired electron.
3. Hence it will exhibit paramagnetic behavior and also involves $d$-$d$ transition.
4. Hence the correct option is 1

**Solved independently** (answer withheld)

1. A d-d transition and paramagnetism both need at least one unpaired $d$ electron, so the metal ion must not be $d^0$.
2. $\mathrm{MnO_4^{2-}}$: $x - 8 = -2 \Rightarrow x = +6$; $\mathrm{Mn^{6+}}$ is $[\mathrm{Ar}]\,3d^1$, one unpaired electron.
3. $\mathrm{CrO_4^{2-}}$: $x - 8 = -2 \Rightarrow x = +6$; $\mathrm{Cr^{6+}}$ is $3d^0$, diamagnetic.
4. $\mathrm{MnO_4^{-}}$: $x - 8 = -1 \Rightarrow x = +7$; $\mathrm{Mn^{7+}}$ is $3d^0$, diamagnetic.
5. $\mathrm{Cr_2O_7^{2-}}$: $2x - 14 = -2 \Rightarrow x = +6$; $\mathrm{Cr^{6+}}$ is $3d^0$, diamagnetic.
6. Only $\mathrm{MnO_4^{2-}}$ ($3d^1$) is both paramagnetic and capable of a d-d transition, which is option $1$.

**Subtopic:** Magnetic Properties, Ionisation Enthalpies, Formation of Coloured Ions & Formation of Complex Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q142_a7911539_03112026.png?v=a7911539afd5)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q142_31601fed_03112026.png?v=31601fedb078)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A d-d transition and paramagnetism both need electrons in the d orbitals, and only $\mathrm{MnO_4^{2-}}$, where Mn is +6 and so 3d$^1$, has any; the other oxoanions are d$^0$ and get their colour from charge transfer.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Permanganate's deep purple is read as a d-d transition, so the most strongly coloured ion in the list is picked; Mn is +7 there, 3d$^0$, and the colour is charge transfer.
- **Why:** This question requires the oxidation state to be settled before colour is used as evidence, demonstrated by the stem asking for 'd-d transition and paramagnetism as well' over three d$^0$ oxoanions.
- **Note:** nearby_fact rather than look_alike_term: replacing $\mathrm{MnO_4^-}$ with an unlike formula keeps the route alive, because what carries it is the remembered colour of permanganate and not the one-charge resemblance to $\mathrm{MnO_4^{2-}}$. All three wrong options are reached by the same colour route, so the trap is placed on the deepest-coloured of them.
<!--/ecat-->

## Q143

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following molecules represents the order of hybridisation $\mathrm{sp^{2}}$, $\mathrm{sp^{2,}}$ $\mathrm{sp}$, $\mathrm{sp}$ from left to right atoms?

- (1) $\mathrm{CH_3 - CH = CH - CH_3}$
- (2) $\mathrm{HC = C - C = CH}$
- (3) $\mathrm{CH_2 = CH - CH = CH_2}$
- **(4)** $\mathrm{CH_2 = CH - C = CH}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: but-1-en-3-yne skeletal structure with each carbon labelled from left to right: sp2, sp2, sp, sp](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q143_sol_1_2350d99b_03112026.svg?v=2350d99b74a9)

*but-1-en-3-yne skeletal structure with each carbon labelled from left to right: sp2, sp2, sp, sp*

![drawn: but-1-en-3-yne skeletal structure with each carbon labelled from left to right: sp2, sp2, sp, sp](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q143_solution_1_798f54ea_03112026.svg?v=798f54ea34d0)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Hence the correct option is $4$

**Solved independently** (answer withheld)

1. A carbon in a double bond is $\mathrm{sp^2}$, a carbon in a triple bond is $\mathrm{sp}$, and a carbon with only single bonds is $\mathrm{sp^3}$.
2. Option 1, $\mathrm{CH_3-CH=CH-CH_3}$: $\mathrm{sp^3, sp^2, sp^2, sp^3}$, so it does not match.
3. Option 2, read as $\mathrm{HC\equiv C-C\equiv CH}$: $\mathrm{sp, sp, sp, sp}$, so it does not match.
4. Option 3, $\mathrm{CH_2=CH-CH=CH_2}$: $\mathrm{sp^2, sp^2, sp^2, sp^2}$, so it does not match.
5. Option 4, read as $\mathrm{CH_2=CH-C\equiv CH}$: $\mathrm{sp^2, sp^2, sp, sp}$, which matches the required order, so the answer is option $4$.

**Subtopic:** Hybridisation · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 28)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q143_59b667cf_03112026.png?v=59b667cf6deb)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q143_64cc34d5_03112026.png?v=64cc34d5df30)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A carbon's hybridisation follows the bonds at it: a doubly bonded carbon is sp$^2$ and a triply bonded one is sp, so only a triple bond can supply the sp, sp pair at one end of the chain.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first two labels asked, sp$^2$ and sp$^2$, are matched by buta-1,3-diene's left-hand carbons and the check stops there; its right-hand carbons are sp$^2$ as well, where the pattern asks for sp, sp.
- **Why:** This question requires each carbon's hybridisation to be assigned from its bonds, demonstrated by the stem asking for the order 'sp$^2$, sp$^2$, sp, sp from left to right atoms'.
- **Note:** Triple bonds are stored as single '=' signs: option 2 reads 'HC = C - C = CH' and option 4 'CH2 = CH - C = CH'. Valence recovers them as $\mathrm{HC\equiv C-C\equiv CH}$ and $\mathrm{CH_2=CH-C\equiv CH}$, and only the second gives the asked sp$^2$, sp$^2$, sp, sp, which is the stored key. The stem also prints the second label as 'sp^{2,}'.
<!--/ecat-->

## Q144

Chemistry · organic · General Organic Chemistry

> ⚠ The independent solve chose (3); the booklet prints (2).

Which of the following carbocations is expected to be most stable?

- (1) 6-Y-1-nitrocyclohexa-2,4-dien-1-ylium `*C1C=CC=C[C+]1[N+](=O)[O-]`
- **(2)** 6-Y-3-nitrocyclohexa-2,4-dien-1-ylium `*C1C=CC([N+](=O)[O-])=C[CH+]1`
- (3) 6-Y-4-nitrocyclohexa-2,4-dien-1-ylium `*C1C=C([N+](=O)[O-])C=C[CH+]1`
- (4) 4-Y-1-nitrocyclohexa-2,5-dien-1-ylium `*C1C=C[C+]([N+](=O)[O-])C=C1`

**Answer** — booklet: (2) · independent solve: (3) · differs

**Publisher's solution**

![printed figure: 6-Y-4-nitrocyclohexa-2,4-dien-1-ylium (ring carbon bearing H and Y; NO2 meta to it, not on a positive carbon)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q144_sol_1_431d5a2f_03112026.svg?v=431d5a2f3703)

*6-Y-4-nitrocyclohexa-2,4-dien-1-ylium (ring carbon bearing H and Y; NO2 meta to it, not on a positive carbon)*

![drawn: 6-Y-4-nitrocyclohexa-2,4-dien-1-ylium (ring carbon bearing H and Y; NO2 meta to it, not on a positive carbon)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q144_solution_1_3b540ce7_03112026.svg?v=3b540ce70336)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Hence the correct option is 2.

**Solved independently** (answer withheld)

1. Each structure is an arenium ($\sigma$-complex) ion formed when $Y^+$ attacks nitrobenzene; label the carbon bearing $-NO_2$ as $C_1$.
2. In a cyclohexadienyl cation the $+$ charge is spread over the 1st, 3rd and 5th carbons of the pentadienyl chain, i.e. the carbons ortho and para to the $sp^3$ carbon.
3. Options $1$ and $4$ place $+$ directly on $C_1$, next to the strongly $-I/-R$ $NO_2$ group: highly destabilised.
4. Option $2$ has the $sp^3$ carbon para to $C_1$, so its resonance hybrid also has a contributor with $+$ on $C_1$: destabilised.
5. Option $3$ has the $sp^3$ carbon meta to $C_1$, so $+$ is delocalised only over $C_2, C_4, C_6$ and never sits on $C_1$; the drawn $+$ at $C_4$ is also farthest from $NO_2$ (weakest $-I$).
6. Hence option $3$ (the meta-attack $\sigma$-complex) is the most stable carbocation.

**Subtopic:** Resonance Effect · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 29)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q144_7d16ef2f_03112026.png?v=7d16ef2f25eb)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q144_0b51fd04_03112026.png?v=0b51fd046be9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Carbocation stability rises with the delocalisation open to the empty p orbital, so resonance with a ring or a lone pair outranks hyperconjugation from neighbouring C-H bonds.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings, so there is no cation to compare and no option in which a pull could be named.
- **Why:** This question requires carbocation stabilities to be ranked by the delocalisation each one offers, demonstrated by the stem 'Which of the following carbocations is expected to be most stable?'.
- **Note:** options_en holds four empty strings while has_figure is false: the paper prints the four cations as structures and none was captured, so the comparison the stem asks for cannot be reconstructed. The stored key is option 2. A reviewer holding the options should check whether a cation stabilised only by hyperconjugation is offered against one stabilised by resonance, which is what the stored chapter tag, Resonance Effect, points at.
<!--/ecat-->

## Q145

Chemistry · organic · General Organic Chemistry

> ⚠ The independent solve chose (4); the booklet prints (2).

Which of the following is correct with respect to $-I$ effect of the substituents? ($\mathrm{R}$ = alkyl)

- (1) $-\mathrm{NR_2} > -\mathrm{OR} > -\mathrm{F}$
- **(2)** $-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$
- (3) $-\mathrm{NH_2} > -\mathrm{OR} > -\mathrm{F}$
- (4) $-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$

**Answer** — booklet: (2) · independent solve: (4) · differs

**Publisher's solution**

1. The correct order of $-\mathrm{I}$ effect is $\mathrm{NH_2} < \mathrm{OR} < \mathrm{F}$
2. Hence the correct option is 2

**Solved independently** (answer withheld)

1. The $-I$ effect of a substituent grows with the electronegativity of the atom bonded to the chain: $\mathrm{F} > \mathrm{O} > \mathrm{N}$.
2. So $-\mathrm{F} > -\mathrm{OR} > -\mathrm{NR_2}$ and $-\mathrm{F} > -\mathrm{OR} > -\mathrm{NH_2}$ in $-I$ strength; alkyl groups on N only lower the $-I$ of $-\mathrm{NR_2}$ further.
3. Options $1$ and $3$ give the reverse order, so both are false.
4. Option $2$ ($-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$) and option $4$ ($-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$) both hold; option $4$ is chosen as it compares alkyl-substituted N and O groups, matching the given $\mathrm{R}$ = alkyl.

**Subtopic:** Inductive Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q145_32583376_03112026.png?v=32583376c3e3)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q145_f56c2163_03112026.png?v=f56c21637ed8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The $-I$ effect grows with the electronegativity of the atom attached to the chain, so nitrogen is weakest, then oxygen, then fluorine.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  $-\mathrm{NH_2} > -\mathrm{OR} > -\mathrm{F}$ is the order of electron donation by resonance, and it gets written down for the inductive series, which runs the other way with electronegativity.
- **Why:** This question requires the $-I$ series to be arranged by the electronegativity of the attached atom, demonstrated by the options printing '$-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$' against its exact reverse.
- **Note:** Tagged as printed; the key is not re-judged here, and the doubt is carried by the flag. Options 2 and 4 express the same direction of the $-I$ series, which is why the flag is set, while the device the question turns on is the reversal in options 1 and 3 and is unaffected by it.
<!--/ecat-->

## Q146

Chemistry · physical · Ionic Equilibrium

The solubility of $\mathrm{BaSO_4}$in water is $2.42\times10^{-3}\,\mathrm{g\,L^{-1}}$ at $298\,\mathrm{K}$, The value of its solubility product ($K_{sp}$) will be (Given molar mass of $\mathrm{BaSO_4}$ = $233\,\mathrm{g\,mol^{-1}}$)

- (1) $1.08\times10^{-8}\,\mathrm{mol^2\,L^{-2}}$
- **(2)** $1.08\times10^{-10}\,\mathrm{mol^2\,L^{-2}}$
- (3) $1.08\times10^{-14}\,\mathrm{mol^2\,L^{-2}}$
- (4) $1.08\times10^{-12}\,\mathrm{mol^2\,L^{-2}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{BaSO4} \rightleftharpoons \mathrm{Ba^{2+}} + \mathrm{SO_{4}^{2-}}$
2. $\mathrm{Ksp} = [\mathrm{Ba^{2+}}]\,[\,\mathrm{So_{4}^{2-}}]$
3. $\mathrm{Ksp} = \mathrm{S^{2}}$
4. Hence the correct option is 2

**Solved independently** (answer withheld)

1. Convert the mass solubility to molar solubility: $s = \frac{2.42\times10^{-3}\,\mathrm{g\,L^{-1}}}{233\,\mathrm{g\,mol^{-1}}} = 1.0386\times10^{-5}\,\mathrm{mol\,L^{-1}}$.
2. $\mathrm{BaSO_4(s) \rightleftharpoons Ba^{2+}(aq) + SO_4^{2-}(aq)}$, so $[\mathrm{Ba^{2+}}] = [\mathrm{SO_4^{2-}}] = s$.
3. $K_{sp} = [\mathrm{Ba^{2+}}][\mathrm{SO_4^{2-}}] = s^2$.
4. $K_{sp} = (1.0386\times10^{-5})^2 = 1.0787\times10^{-10} \approx 1.08\times10^{-10}\,\mathrm{mol^2\,L^{-2}}$, which is option $2$.

**Subtopic:** Solubility Product Constant · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q146_832e12bc_03112026.png?v=832e12bcffb1)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q146_af28d6bb_03112026.png?v=af28d6bbea9d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a 1:1 salt the molar solubility is the mass solubility over the molar mass, and $K_{sp}=s^2$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The conversion $2.42\times10^{-3}/233$ is written as $1.04\times10^{-4}$ instead of $1.04\times10^{-5}$ - one power of ten lost - and squaring that gives $1.08\times10^{-8}$.
- **Why:** This question requires a mass solubility to be converted to a molarity and squared, demonstrated by the stem giving $2.42\times10^{-3}\,\mathrm{g\,L^{-1}}$ with the molar mass 233 g mol$^{-1}$ and options that differ only in the power of ten.
<!--/ecat-->

## Q147

Chemistry · physical · States of Matter

Given van der Waals constant for $\mathrm{NH_3}$, $\mathrm{H_2}$, $\mathrm{O_2}$ and $\mathrm{CO_2}$ are respectively 4.17, 0.244, 1.36 and 3.59, which one of the following gases is most easily liquefield?

- (1) $\mathrm{CO_2}$
- **(2)** $\mathrm{NH_3}$
- (3) $\mathrm{O_2}$
- (4) $\mathrm{H_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The rate of liquification is directly proportion to the Vanderwaals constant value.
2. $\mathrm{NH_3}$ having the highest value should easily undergo liquification.
3. The correct option is 2.

**Solved independently** (answer withheld)

1. The van der Waals constant $a$ measures the strength of intermolecular attraction, so a larger $a$ means a gas is more easily liquefied.
2. Order of the given values: $a(\mathrm{NH_3}) = 4.17 > a(\mathrm{CO_2}) = 3.59 > a(\mathrm{O_2}) = 1.36 > a(\mathrm{H_2}) = 0.244$.
3. $\mathrm{NH_3}$ has the largest $a$, so it is the most easily liquefied, which is option $2$.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q147_9ca6005c_03112026.png?v=9ca6005c7785)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q147_06c32a70_03112026.png?v=06c32a705c17)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The van der Waals constant $a$ measures the attraction between the molecules, so of a set of gases the one with the largest $a$ liquefies most easily.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $\mathrm{CO_2}$ is the gas the chapter liquefies - its isotherms are the ones drawn - so it is picked as the easily liquefied gas without reading the printed constants, where $\mathrm{NH_3}$'s 4.17 beats its 3.59.
- **Why:** This question requires the printed van der Waals constants to be read under the rule that a larger $a$ means easier liquefaction, demonstrated by the stem supplying 4.17, 0.244, 1.36 and 3.59 and asking which gas 'is most easily liquefield'.
<!--/ecat-->

## Q148

Chemistry · physical · Ionic Equilibrium

Following solution were prepared by mixing different volumes of $\mathrm{NaOH}$ and $\mathrm{HCl}$ of different concentration:

pH of which one of them will be equal to 1?

- **(a)** $60\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{HCl} + 40\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{NaOH}$
- **(b)** $55\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{HCl} + 45\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{NaOH}$
- **(c)** $75\,\mathrm{mL}\ \frac{\mathrm{M}}{5}\ \mathrm{HCl} + 25\,\mathrm{mL}\ \frac{\mathrm{M}}{5}\ \mathrm{NaOH}$
- **(d)** $100\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{HCl} + 100\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{NaOH}$

- **(1)** c
- (2) b
- (3) d
- (4) a

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Meq of $\mathrm{HCl} = 75 \times \frac{1}{5} \times 1 = 15$
2. Meq of $\mathrm{NaOH} = 25 \times \frac{1}{5} \times 1 = 5$
3. Meq of $\mathrm{HCl}$ in resulting solution $= 10$
4. Molarity of $\left[H^{+}\right]$ in resulting mixture $= \frac{10}{100} = \frac{1}{10}$
5. $\mathrm{pH} = -\log\left[H^{+}\right] = -\log\left[\frac{1}{10}\right] = 1.0$

**Solved independently** (answer withheld)

1. (a) $n_{H^+} = 60 \times 0.1 = 6\,\mathrm{mmol}$, $n_{OH^-} = 40 \times 0.1 = 4\,\mathrm{mmol}$.
2. (a) Excess $H^+ = 2\,\mathrm{mmol}$ in $100\,\mathrm{mL}$, so $[H^+] = 0.02\,\mathrm{M}$ and $\mathrm{pH} = 2 - \log 2 \approx 1.7$.
3. (b) Excess $H^+ = 5.5 - 4.5 = 1\,\mathrm{mmol}$ in $100\,\mathrm{mL}$, so $[H^+] = 0.01\,\mathrm{M}$ and $\mathrm{pH} = 2$.
4. (c) $n_{H^+} = 75 \times 0.2 = 15\,\mathrm{mmol}$, $n_{OH^-} = 25 \times 0.2 = 5\,\mathrm{mmol}$.
5. (c) Excess $H^+ = 10\,\mathrm{mmol}$ in $100\,\mathrm{mL}$, so $[H^+] = 0.1\,\mathrm{M}$ and $\mathrm{pH} = 1$.
6. (d) $n_{H^+} = n_{OH^-} = 10\,\mathrm{mmol}$, complete neutralisation, $\mathrm{pH} = 7$.
7. Only (c) gives $\mathrm{pH} = 1$, which is option $1$.

**Subtopic:** pH Scale · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q148_b3624586_03112026.png?v=b362458613bc)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q148_577e5ffa_03112026.png?v=577e5ffaec15)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** After mixing a strong acid with a strong base, the pH comes from the leftover moles of $\mathrm{H^+}$ divided by the TOTAL volume of the mixture, not from the molarity written on either stock bottle
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  In (a) the leftover acid is $60-40=20\,\mathrm{mL}$ of $\mathrm{M}/10$ $\mathrm{HCl}$, and dividing the $2\,\mathrm{mmol}$ of excess $\mathrm{H^+}$ by that $20\,\mathrm{mL}$ instead of the $100\,\mathrm{mL}$ mixture gives $0.1\,\mathrm{M}$ and pH 1, where the true figure is $0.02\,\mathrm{M}$ and pH 1.7
- **Why:** This question requires the excess $\mathrm{H^+}$ concentration of each mixture to be computed over the combined volume, demonstrated by the stem asking 'pH of which one of them will be equal to 1?' against recipes such as '$75\,\mathrm{mL}\ \mathrm{M}/5\ \mathrm{HCl} + 25\,\mathrm{mL}\ \mathrm{M}/5\ \mathrm{NaOH}$', where only the $\mathrm{M}/5$ pair leaves $10\,\mathrm{mmol}$ in $100\,\mathrm{mL}$.
- **Note:** E1's pattern returned plain_mcq on the 16-default, but the printed shape has a lettered block (a) to (d) above the options and each option is a bare letter, so the shape recorded here is statements. The lettered items are solution recipes rather than claims to judge; the answer still selects one letter from a printed lettered list. Key checks out: (c) gives $10\,\mathrm{mmol}$ excess $\mathrm{H^+}$ in $100\,\mathrm{mL}$, i.e. $0.1\,\mathrm{M}$, pH 1.
<!--/ecat-->

## Q149

Chemistry · physical · Surface Chemistry

On which of the following properties does the coagulating power of an ion depend?

- (1) The sign of charge on the ion alone
- (2) The magnitude of the charge on the ion alone.
- **(3)** Both magnitude and sign of the charge on the ion
- (4) Size of the ion alone.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The coagulation power depends on both magnitude and sign of the charge of the ion.

**Solved independently** (answer withheld)

1. Coagulation happens when an added ion neutralises the charge on the colloidal particles, so the active ion must carry a charge of opposite sign to the sol (e.g. cations for a negative $\mathrm{As_2S_3}$ sol).
2. Hardy-Schulze rule: the greater the valence of the flocculating ion, the greater its coagulating power, e.g. $\mathrm{Al^{3+}} > \mathrm{Ba^{2+}} > \mathrm{Na^{+}}$ for a negative sol.
3. Coagulating power therefore depends on both the sign and the magnitude of the charge on the ion, which is option $3$.

**Subtopic:** Coagulation of Colloids and Hardy-Schulze Rule · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q149_acac5bc0_03112026.png?v=acac5bc05ef7)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q149_302b2586_03112026.png?v=302b258690b4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** By the Hardy-Schulze rule an ion coagulates a sol only if its charge is opposite to the sol's, and its coagulating power then rises with the magnitude of that charge.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The rule is carried as 'the higher the valency, the greater the coagulating power', which is true as far as it goes, and the word 'alone' quietly drops the requirement that the charge be of the opposite sign.
- **Why:** This question requires the whole of the Hardy-Schulze rule rather than one half of it, demonstrated by three options offering a single property 'alone' against the one that keeps both magnitude and sign.
<!--/ecat-->

## Q150

Chemistry · inorganic · The p–Block Elements

Which of the following statements is not true for halogens?

- (1) Chlorine has the highest electron – gain enthalpy.
- (2) All form monobasic oxyacids.
- **(3)** All but fluorine show positive oxidation states.
- (4) All are oxidizing agents.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Fluorine can never have positive oxidation state.
2. Hence the correct option is 3

**Solved independently** (answer withheld)

1. Statement 1: $\Delta_{eg}H(\mathrm{Cl}) \approx -349\,\mathrm{kJ\,mol^{-1}}$ is more negative than $\Delta_{eg}H(\mathrm{F}) \approx -333\,\mathrm{kJ\,mol^{-1}}$, so chlorine has the largest electron gain enthalpy (in magnitude). True.
2. Statement 2: every halogen oxoacid ($\mathrm{HOF}$, $\mathrm{HOCl}$, $\mathrm{HClO_2}$, $\mathrm{HClO_3}$, $\mathrm{HClO_4}$, $\mathrm{HOBr}$, $\mathrm{HBrO_3}$, $\mathrm{HOI}$, $\mathrm{HIO_3}$, $\mathrm{HIO_4}$) has one ionisable $\mathrm{O{-}H}$, so all are monobasic. True.
3. Statement 4: all $\mathrm{X_2}$ readily accept electrons ($\mathrm{X_2} + 2e^- \rightarrow 2\mathrm{X^-}$), so all are oxidising agents. True.
4. Statement 3: fluorine, the most electronegative element, shows only $-1$; $\mathrm{Cl}$, $\mathrm{Br}$, $\mathrm{I}$ also show $+1, +3, +5, +7$. By oxidation-number rules this is true (in $\mathrm{HOF}$, $\mathrm{F} = -1$, $\mathrm{O} = 0$).
5. NCERT, however, names $\mathrm{HOF}$ 'fluoric(I) acid', which implies $\mathrm{F}$ is $+1$. That makes statement $3$ the only one that can be called not true, so the best pick is option $3$, with low confidence.

**Subtopic:** General Properties & Trends of Group 17 (Halogens) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q150_5632f75d_03112026.png?v=5632f75d3a18)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q150_f8dcd53f_03112026.png?v=f8dcd53f2185)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Group 17 general properties, including the anomaly that chlorine, not fluorine, has the most negative electron gain enthalpy
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The down-group rule says electron gain enthalpy becomes less negative from top to bottom, so the top member fluorine should be the highest, which makes 'Chlorine has the highest electron – gain enthalpy' read as the false statement
- **Why:** This question requires each printed claim about group 17 to be graded against the chapter's stated properties, demonstrated by 'Which of the following statements is not true for halogens?' over four independent property claims.
- **Note:** The stored key is option 3, 'All but fluorine show positive oxidation states'. On the chapter's own reading that statement is true (fluorine is restricted to -1 while the others reach +1 to +7), and the statement whose truth is actually arguable is option 2, since fluorine's only oxoacid, HOF, is unstable. Tagged as printed per the no-re-judging rule; flagged for a key check against the printed paper. The trap recorded sits on option 1, which is wrong under either reading of the key.
<!--/ecat-->

## Q151

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Considering Ellingham diagram, which of the following metals can be used to reduce alumina?

- (1) $\mathrm{Cu}$
- (2) $\mathrm{Fe}$
- **(3)** $\mathrm{Mg}$
- (4) $\mathrm{Zn}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{Mg}$ can be used to reduce alumina according to Ellingham diagram
2. Hence the correct option is 3

**Solved independently** (answer withheld)

1. A metal $\mathrm{M}$ can reduce $\mathrm{Al_2O_3}$ only if $\Delta_r G^\ominus$ for $\mathrm{Al_2O_3} + \mathrm{M} \rightarrow \mathrm{Al} + \mathrm{MO}$ is negative, i.e. the $\mathrm{M/MO}$ line lies below the $\mathrm{Al/Al_2O_3}$ line on the Ellingham diagram.
2. The $\mathrm{Cu/Cu_2O}$, $\mathrm{Fe/FeO}$ and $\mathrm{Zn/ZnO}$ lines all lie above the $\mathrm{Al/Al_2O_3}$ line, so $\Delta_r G^\ominus > 0$ for these metals.
3. The $\mathrm{Mg/MgO}$ line crosses below the $\mathrm{Al/Al_2O_3}$ line above about $1623\,\mathrm{K}$, so $\mathrm{Mg}$ can reduce alumina, which is option $3$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q151_463c7365_03112026.png?v=463c7365f466)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q151_22fe35dc_03112026.png?v=22fe35dcc8ac)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** On an Ellingham diagram a metal reduces another metal's oxide only if its own oxide line lies lower, and magnesium's lies below that of alumina at ordinary temperatures
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The thermite reaction printed in the chapter runs aluminium plus iron oxide, and reading that pair in the other direction turns iron into the reducing agent for alumina
- **Why:** This question requires the Ellingham criterion to be applied to four named metals, demonstrated by the stem's instruction 'Considering Ellingham diagram, which of the following metals can be used to reduce alumina?'
- **Note:** No diagram is supplied and none is needed: the stem names the diagram as the principle to use, and the four metals are judged by their known line positions.
<!--/ecat-->

## Q152

Chemistry · inorganic · The p–Block Elements

The correct order of atomic radii in group 13 elements is

- **(1)** $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{Tl}$
- (2) $\mathrm{B} < \mathrm{Al} < \mathrm{In} < \mathrm{Ga} < \mathrm{Tl}$
- (3) $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{Tl} < \mathrm{In}$
- (4) $\mathrm{B} < \mathrm{Al} < \mathrm{Ga} < \mathrm{In} < \mathrm{Tl}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{Al}$ is expection in the atomic radii of $13$ group
2. $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{TL}$.
3. Hence the correct option is $1$

**Solved independently** (answer withheld)

1. Atomic radius generally increases down group 13: $\mathrm{B}$ ($85$ pm) is the smallest.
2. In $\mathrm{Ga}$ the ten $3d$ electrons shield the nucleus poorly, so the larger effective nuclear charge makes $r_{\mathrm{Ga}}$ ($135$ pm) $< r_{\mathrm{Al}}$ ($143$ pm).
3. Going further down, $r_{\mathrm{In}} = 167$ pm $< r_{\mathrm{Tl}} = 170$ pm.
4. So the order is $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{Tl}$, which is option $1$.

**Subtopic:** General properties & Trends of Group 13 (Boron Family) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q152_63186756_03112026.png?v=6318675685bc)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q152_93941ecc_03112026.png?v=93941ecc90e5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Atomic radius increases down group 13 except at gallium, where the newly filled 3d shell shields poorly and leaves Ga slightly smaller than Al
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Applying 'atomic radius increases down a group' straight through group 13 gives the smooth order B < Al < Ga < In < Tl, which is the printed option that drops the gallium break
- **Why:** This question requires five named elements to be put in sequence on one property, demonstrated by 'The correct order of atomic radii in group 13 elements is' with four complete orderings as options.
<!--/ecat-->

## Q153

Chemistry · inorganic · Chemical Bonding and Molecular Structure

In the structure of $\mathrm{CIF_3}$, the number of lone pairs of electrons on central atom ‘$\mathrm{CI}$’ is

- (1) Three
- (2) One
- (3) Four
- **(4)** Two

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F atoms (F left, F right, F below), with two lone pairs of dots drawn above Cl](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q153_sol_1_16da9495_03112026.svg?v=16da9495f2cf)

*chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F atoms (F left, F right, F below), with two lone pairs of dots drawn above Cl*

![drawn: chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F atoms (F left, F right, F below), with two lone pairs of dots drawn above Cl](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q153_solution_1_8218498b_03112026.svg?v=8218498b584a)  
*drawn on the booklet's geometry, checked against its SMILES*

1. The central $\mathrm{Cl}$ atom has $2$ lone pair of electrons in $\mathrm{ClF_3}$ molecule.
2. Hence the correct option is 4

**Solved independently** (answer withheld)

1. Chlorine (group 17) has $7$ valence electrons.
2. Three of these form bonds with the three F atoms, giving $3$ bond pairs.
3. Remaining non-bonding electrons $= 7 - 3 = 4$, i.e. $\frac{4}{2} = 2$ lone pairs.
4. Total electron pairs $= 3 + 2 = 5$ ($sp^3d$, T-shaped), so the central Cl carries $2$ lone pairs, which is option $4$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q153_cb380973_03112026.png?v=cb3809737b2e)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q153_69046c3a_03112026.png?v=69046c3ab01d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Lone pairs on a central atom are the valence electrons left after bonding, divided into pairs: chlorine's seven electrons minus three bonds leave four electrons, so two lone pairs
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Seven valence electrons minus three used in Cl-F bonds leaves four, and reporting that four as the answer stops one step short of pairing them
- **Why:** This question requires the valence-electron bookkeeping rule to be applied to one named species, demonstrated by 'In the structure of CIF3, the number of lone pairs of electrons on central atom' with four counts as options.
- **Note:** The stem and option text print chlorine as 'CI' (capital I for l) throughout, an extraction artefact in the character, not a different element; ClF3 is unambiguous. No option is affected, so the record is still ratable.
<!--/ecat-->

## Q154

Chemistry · physical · Redox Reactions

The correct order of N – Compounds in its decreasing order of oxidation states is

- (1) $\mathrm{NH_4CI}$, $\mathrm{N_2}$, $\mathrm{NO}$, $\mathrm{HNO_3}$
- **(2)** $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{N_2}$, $\mathrm{NH_4CI}$
- (3) $\mathrm{HNO_3}$, $\mathrm{NH_4CI}$, $\mathrm{NO}$, $\mathrm{N_2}$
- (4) $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{NH_4CI}$, $\mathrm{N_4}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The oxidation state of $\mathrm{N}$ is $+5$, $+2$,$0$, $-3$ in $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{N_2}$, $\mathrm{NH_4Cl}$
2. Therefore the correct option is 2

**Solved independently** (answer withheld)

1. In $\mathrm{HNO_3}$: $(+1) + x + 3(-2) = 0 \Rightarrow x = +5$.
2. In $\mathrm{NO}$: $x + (-2) = 0 \Rightarrow x = +2$.
3. In $\mathrm{N_2}$ (element): $x = 0$.
4. In $\mathrm{NH_4Cl}$, the $\mathrm{NH_4^+}$ ion: $x + 4(+1) = +1 \Rightarrow x = -3$.
5. Decreasing order $+5 > +2 > 0 > -3$ gives $\mathrm{HNO_3}, \mathrm{NO}, \mathrm{N_2}, \mathrm{NH_4Cl}$, which is option $2$.

**Subtopic:** Oxidation Number · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q154_2101885e_03112026.png?v=2101885ed970)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q154_bee2918d_03112026.png?v=bee2918d7c84)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Oxidation number of nitrogen in each species, ranked: +5 in HNO3, +2 in NO, 0 in N2 and -3 in ammonium
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The four oxidation numbers are worked out correctly and then written from the lowest up, so the sequence printed is the exact reverse of the decreasing order the stem asks for
- **Why:** This question requires four species to be ranked on one computed property, demonstrated by 'The correct order of N – Compounds in its decreasing order of oxidation states is' with four complete sequences as options.
- **Note:** Option 4 ends in 'N_4', which is almost certainly a mis-set N2 in our record; a repair check against the printed paper is warranted. The key, option 2, and the two routed distractors do not depend on that token, so the question remains ratable as stored.
<!--/ecat-->

## Q155

Chemistry · inorganic · The p–Block Elements

Which one of the following elements of unable to form $\mathrm{MF_6^{3-}}$ ion ?

- (1) $\mathrm{In}$
- (2) $\mathrm{Ga}$
- **(3)** $\mathrm{B}$
- (4) $\mathrm{Al}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The maximum coordination number of $\mathrm{B}$ is $4$. It cannot form$\mathrm{MF_6^{3-}}$
2. Hence the correct option is $3$

**Solved independently** (answer withheld)

1. $\mathrm{MF_6^{3-}}$ needs the central atom M to take a covalency of $6$.
2. Boron is in period 2, so its valence shell has only $2s$ and $2p$ orbitals and no $d$ orbitals, which limits its maximum covalency to $4$ (e.g. $\mathrm{BF_4^-}$).
3. $\mathrm{Al}$, $\mathrm{Ga}$ and $\mathrm{In}$ have vacant $d$ orbitals, so they can expand their covalency to $6$ and form $\mathrm{MF_6^{3-}}$ (e.g. $\mathrm{AlF_6^{3-}}$).
4. So $\mathrm{B}$ is the element that cannot form $\mathrm{MF_6^{3-}}$, which is option $3$.

**Subtopic:** Anomalous behaviour of Boron & Diagonal Relationship (B–Si) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q155_a66c14a4_03112026.png?v=a66c14a40949)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q155_571df9d3_03112026.png?v=571df9d3de72)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Boron's maximum covalence is four because it has no d orbitals, so it stops at BF4- while the heavier group 13 members form MF6 3- ions
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The inert pair effect is printed in the same section as the fact asked for, and a student who reaches for it concludes that indium, the heavy member whose +1 state is stabilised, is the one that cannot form a +3 complex ion
- **Why:** This question requires the stated fact about which group 13 member cannot form the hexafluoro ion, demonstrated by 'Which one of the following elements of unable to form MF6 3- ion ?' with four coordinate group members as options.
- **Note:** The stem reads 'elements of unable to form', a typographical slip in our record that does not change what is asked.
<!--/ecat-->

## Q156

Chemistry · organic · Alcohols, Phenols and Ethers

The compound A on treatment with Na gives B, and with $\mathrm{PCI_5}$ gives C. B and C react together to give diethyl ether. A, B and C are in the order.

- **(1)** $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_{4=5}CI}$
- (2) $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_6}$, $\mathrm{C_2H_5CI}$
- (3) $\mathrm{C_2H_5CI}$, $\mathrm{C_2H_6}$, $\mathrm{C_2H_5OH}$
- (4) $\mathrm{C_4H_5OH}$, $\mathrm{C_2H_5CI}$,$\mathrm{C_2H_5ONa}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. A is ethyl alchol which on reaction with $\mathrm{Na}$ forms sodium ethoxide(B).
2. Ethylalcohol also react with $\mathrm{PCl_5}$ to form chloroethane(C)
3. B& C react together to form diethylether. This is Williamson synthesis.
4. Hence the correct option is 1

**Solved independently** (answer withheld)

1. Since B and C combine to give diethyl ether $\mathrm{C_2H_5OC_2H_5}$, this is a Williamson synthesis needing $\mathrm{C_2H_5ONa}$ and $\mathrm{C_2H_5Cl}$, so A must be ethanol $\mathrm{C_2H_5OH}$.
2. $\mathrm{C_2H_5OH + Na \rightarrow C_2H_5ONa + \tfrac{1}{2}H_2}$, so B is $\mathrm{C_2H_5ONa}$.
3. $\mathrm{C_2H_5OH + PCl_5 \rightarrow C_2H_5Cl + POCl_3 + HCl}$, so C is $\mathrm{C_2H_5Cl}$.
4. $\mathrm{C_2H_5ONa + C_2H_5Cl \rightarrow C_2H_5OC_2H_5 + NaCl}$, confirming the order $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_5Cl}$, which is option $1$.

**Subtopic:** Reactions of Alcohols, Preparation of Ethers by Williamson Ether Synthesis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q156_540974a9_03112026.png?v=540974a9ff29)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q156_0d869f17_03112026.png?v=0d869f17b86f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Sodium takes the O-H hydrogen of ethanol to give sodium ethoxide, PCl5 swaps the OH for Cl, and alkoxide plus halide is the Williamson route to diethyl ether
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A as ethanol and C as ethyl chloride are secure from the PCl5 step, and then sodium is remembered as the metal that strips halogen to give a hydrocarbon, so B comes out as ethane.
- **Why:** This question requires each reagent matched to the product it gives, demonstrated by the stem's "on treatment with Na gives B, and with PCl5 gives C. B and C react together to give diethyl ether".
- **Note:** Our record stores chlorine as "CI" throughout, and two options carry debris: option 1 prints its third species as C_2H_{4=5}CI where C2H5Cl is meant, and option 4 prints C_4H_5OH where ethanol is meant. The key is still identifiable, because option 1 is the only one placing sodium ethoxide at B, and the trap recorded above sits on option 2, which is stored cleanly. The route given for option 4 reads its first species as ethanol; a reviewer should repair the option text before that route is quoted.
<!--/ecat-->

## Q157

Chemistry · organic · Hydrocarbons

Hydrocarbon (A) reacts with bromine by substitution to form an alkyl bromide which by Wurtz reaction is converted to gaseous hydrocarbon containing less than four carbon atoms. (A) is

- **(1)** $\mathrm{CH_4}$
- (2) $\mathrm{CH\equiv CH}$
- (3) $\mathrm{CH_3-CH_3}$
- (4) $\mathrm{CH_2=CH_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Methane undergoes substitution reaction to form ethyl bromide which futher undergoes wurtz reaction to form ethane.
2. Hence the correct option is 1

**Solved independently** (answer withheld)

1. Only alkanes react with bromine by substitution; $\mathrm{CH\equiv CH}$ and $\mathrm{CH_2=CH_2}$ undergo addition of $\mathrm{Br_2}$, so options $2$ and $4$ are out.
2. $\mathrm{CH_4 + Br_2 \xrightarrow{h\nu} CH_3Br + HBr}$.
3. Wurtz reaction: $\mathrm{2CH_3Br + 2Na \xrightarrow{dry\ ether} CH_3-CH_3 + 2NaBr}$, giving ethane, a gas with $2 < 4$ carbon atoms.
4. For ethane: $\mathrm{C_2H_5Br}$ by Wurtz gives $\mathrm{C_4H_{10}}$, which has $4$ carbons, not fewer than four, so option $3$ is out.
5. Hence (A) is $\mathrm{CH_4}$, option $1$.

**Subtopic:** Preparation of Alkane, Chemical Properties of Alkane · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q157_f4f4fb0a_03112026.png?v=f4f4fb0ae610)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q157_fac5b0f5_03112026.png?v=fac5b0f5c4b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Wurtz coupling doubles the carbon skeleton and only an alkane gives an alkyl bromide by substitution, so a product with fewer than four carbons forces a one-carbon start
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Ethane satisfies every clause except the carbon count: it substitutes bromine and Wurtz gives a gas, but that gas is butane with four carbons, not fewer than four.
- **Why:** This question requires a starting hydrocarbon worked back from its reactions, demonstrated by the stem's "by substitution" and "gaseous hydrocarbon containing less than four carbon atoms".
<!--/ecat-->

## Q158

Chemistry · organic · Hydrocarbons

The compound $\mathrm{C_7H_8}$ undergoes the following reaction: $\mathrm{C_7H_8 \xrightarrow{3CI_2/\Delta} A \xrightarrow{Br_2/Fe} B \xrightarrow{Zn/HCI} C}$ The product ‘C’ is

- (1) p – bromotoluene
- **(2)** m- bromotoluene
- (3) 3 – bromo -2, 4, 6 – trichlorotoluene
- (4) o – bromotoluene

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: toluene →($\ce{3Cl2}$) (trichloromethyl)benzene (A) →($\ce{Br2}$/Fe) 1-bromo-3-(trichloromethyl)benzene (B) →(Zn/HCl) 1-bromo-3-methylbenzene (C)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q158_sol_1_d341d5ed_03112026.svg?v=d341d5edf77d)

*toluene →[$\ce{3Cl2}$] (trichloromethyl)benzene (A) →[$\ce{Br2}$/Fe] 1-bromo-3-(trichloromethyl)benzene (B) →[Zn/HCl] 1-bromo-3-methylbenzene (C)*

![drawn: toluene →($\ce{3Cl2}$) (trichloromethyl)benzene (A) →($\ce{Br2}$/Fe) 1-bromo-3-(trichloromethyl)benzene (B) →(Zn/HCl) 1-bromo-3-methylbenzene (C)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q158_solution_1_f33ea134_03112026.svg?v=f33ea1340c3e)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Hence the correct option is 2.

**Solved independently** (answer withheld)

1. $\mathrm{C_7H_8}$ is toluene, $\mathrm{C_6H_5CH_3}$.
2. With $\mathrm{Cl_2}$ and heat (free-radical conditions, no Lewis acid), all three side-chain H atoms are replaced: $\mathrm{C_6H_5CH_3 \xrightarrow{3Cl_2/\Delta} C_6H_5CCl_3}$ (A, benzotrichloride).
3. The $\mathrm{-CCl_3}$ group is strongly electron-withdrawing, so it deactivates the ring and directs electrophilic substitution to the meta position: $\mathrm{C_6H_5CCl_3 \xrightarrow{Br_2/Fe} \textit{m}\text{-}BrC_6H_4CCl_3}$ (B).
4. $\mathrm{Zn/HCl}$ reduces the $\mathrm{-CCl_3}$ group back to $\mathrm{-CH_3}$: $\mathrm{\textit{m}\text{-}BrC_6H_4CCl_3 \xrightarrow{Zn/HCl} \textit{m}\text{-}BrC_6H_4CH_3}$ (C).
5. C is $m$-bromotoluene, which is option $2$.

**Subtopic:** Chemical and Physical Properties of Benzene · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 32)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q158_fe2a34e3_03112026.png?v=fe2a34e3b2b0)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q158_50a3e265_03112026.png?v=50a3e2657e51)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Chlorinating the side chain turns the o/p-directing methyl into a meta-directing CCl3 group, bromine then enters meta, and Zn/HCl puts the methyl back
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Bromination is placed where a methyl group would send it, para, because the group carrying the ring at that moment is read as still being the methyl.
- **Why:** This question requires the directing effect of the group actually present at each stage, demonstrated by the stem's three printed steps, 3Cl2 with heat, then Br2/Fe, then Zn/HCl.
- **Note:** E1 called this reaction_scheme, which maps onto qtype mcq; the scheme is in the stem and the options are names.
<!--/ecat-->

## Q159

Chemistry · inorganic · Environmental Chemistry

Which oxide of nitrogen is not a common pollutant introduced into the atmosphere both due to natural and human activity?

- (1) $\mathrm{NO}$
- **(2)** $\mathrm{N_2O_5}$
- (3) $\mathrm{N_2O}$
- (4) $\mathrm{NO_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{N_2O_5}$ is not a pollutant which can be introduced into atmosphere due to human activity.

**Solved independently** (answer withheld)

1. $\mathrm{NO}$, $\mathrm{NO_2}$ and $\mathrm{N_2O}$ enter the atmosphere from both natural sources (lightning, microbial action) and human activity (combustion, fertilisers), so they are common pollutants; $\mathrm{N_2O_5}$ is not, which is option $2$.

**Subtopic:** Air Pollution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q159_c048bbdb_03112026.png?v=c048bbdb72a4)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q159_987e5238_03112026.png?v=987e52389f76)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NO, NO2 and N2O all enter the air from natural as well as human sources, while N2O5 is not an atmospheric pollutant at all
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  N2O is stored as laughing gas, the anaesthetic, and that identity answers 'which of these is not a pollutant' before the question of its sources is reached.
- **Why:** This question requires the stated list of nitrogen oxides counted as air pollutants, demonstrated by the stem's "not a common pollutant introduced into the atmosphere both due to natural and human activity".
<!--/ecat-->

## Q160

Chemistry · physical · Chemical Kinetics

The correct difference between first and second – order reactions is that

- (1) the rate of a first order reaction does depend on reactant concentrations; the rate of a second order reaction does not depend on reactant concentrations.
- (2) the rate of a first order reaction does not depend on reactant concentrations; the rate of a second order reaction does depend on reactant concentrations.
- (3) a first order reaction can be catalyzed; a second order reaction cannot be catalyzed.
- (4) the half life of a first order reaction does not depend on $[\mathrm{A}]_0$; the half life of a second order reaction does depend on $[\mathrm{A}]_0$

**Answer** — booklet: (none) · independent solve: (4) · unchecked

**Publisher's solution**

1. For first order reaction, $t_{\frac{1}{2}} = \frac{0.693}{k}$, which is independent of initial concentration of reactant.
2. For second order reaction, $t_{\frac{1}{2}} = \frac{1}{k\left(A_0\right)}$, which depends on initial concentration of reactant.

**Solved independently** (answer withheld)

1. For a first order reaction, $\text{rate} = k[\mathrm{A}]$, so the rate depends on reactant concentration; for a second order reaction, $\text{rate} = k[\mathrm{A}]^2$, which also depends on concentration. Options $1$ and $2$ are therefore false.
2. Catalysis is not restricted by reaction order; reactions of any order can be catalysed, so option $3$ is false.
3. First order: $t_{1/2} = \frac{0.693}{k}$, independent of $[\mathrm{A}]_0$.
4. Second order: $t_{1/2} = \frac{1}{k[\mathrm{A}]_0}$, which depends on $[\mathrm{A}]_0$.
5. Hence the correct difference is option $4$.

**Subtopic:** Half-Life of a Reaction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q160_8f24dfea_03112026.png?v=8f24dfea20a9)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q160_739a3aef_03112026.png?v=739a3aefd047)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Order fixes two separate things: the rate depends on concentration for both first and second order, but only the second-order half-life depends on the starting concentration
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Our record carries no key for this question: correct_answer is null and accepted_answers is empty, so no option can be named as the answer and no option can be named as wrong. The stem and all four options are present and intact, so nothing is wrong with the printed question; what is missing is our stored answer line.
- **Why:** This question requires two neighbouring kinetic orders held apart, demonstrated by the stem "The correct difference between first and second - order reactions is that" and by two options differing only in which order is said to depend on concentration.
- **Note:** No trap is written because the answer line is absent from our record, not because the question is faulty. The mechanism a reviewer holding the key should check: options 1 and 2 are the same claim about rate written in opposite directions, so whichever way a student half-remembers 'the rate depends on concentration' there is an option waiting, while the statement that actually separates the two orders is the half-life one, since a first-order half life is independent of the initial concentration and a second-order half life goes as $1/[A]_0$. Also, negative_words_seen records NOT, but every NOT here sits inside the options rather than in the task, so the task itself is direct.
<!--/ecat-->

## Q161

Chemistry · inorganic · The s-Block Elements

Among $\mathrm{CaH_2}$, $\mathrm{BeH_2}$, $\mathrm{BaH_2}$, the order of ionic character is

- (1) $\mathrm{BaH_2} < \mathrm{BeH_2} < \mathrm{CaH_2}$
- **(2)** $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$
- (3) $\mathrm{BeH_2} < \mathrm{BaH_2} < \mathrm{CaH_2}$
- (4) $\mathrm{CaH_2} < \mathrm{BeH_2} < \mathrm{BaH_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Metal hydrides are usually ionic in nature.
2. Smaller size of cation makes it less ionic. So the correct order is
3. $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$
4. Hence the correct option is 2

**Solved independently** (answer withheld)

1. Down group 2 ($\mathrm{Be} \rightarrow \mathrm{Ca} \rightarrow \mathrm{Ba}$) the metal's size increases and its electronegativity decreases.
2. A larger, more electropositive metal transfers its electron to H more completely, so ionic character rises down the group.
3. $\mathrm{BeH_2}$ is covalent and polymeric, while $\mathrm{BaH_2}$ is the most ionic, giving $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$, which is option $2$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q161_d239fb92_03112026.png?v=d239fb92f9c5)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q161_3d0a0d73_03112026.png?v=3d0a0d73f94c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Ionic character of the group-2 hydrides rises down the group as the cation gets larger and less polarising, so BeH2 is covalent and BaH2 is ionic
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Beryllium is placed at the bottom correctly, and then the calcium and barium pair is written the other way round, inverting the trend over the part of the group where it still has to be applied.
- **Why:** This question requires a group trend arranged over three named hydrides, demonstrated by the stem's "the order of ionic character" with four orderings of the same three formulas as the options.
- **Note:** E1 called this statement_options, the pattern firing on the LaTeX in the options; the options are orderings of three formulas, so the shape recorded is mcq and the ask is order.
<!--/ecat-->

## Q162

Chemistry · physical · Electrochemistry

Consider the change in oxidation state of bromine corresponding to different emf values as shown in the diagram below: Then the species undergoing disproportionation is

![printed figure: $\ce{BrO4^-}$ →(1·82 V) $\ce{BrO3^-}$ →(1·5 V) $\ce{HBrO}$ →(1·595 V) $\ce{Br2}$ →(1·0652 V) $\ce{Br^-}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q162_27dd069a_03112026.png?v=27dd069a9e26)

*$\ce{BrO4^-}$ →[1·82 V] $\ce{BrO3^-}$ →[1·5 V] $\ce{HBrO}$ →[1·595 V] $\ce{Br2}$ →[1·0652 V] $\ce{Br^-}$*

Structures: perbromate `[O-][Br+3]([O-])([O-])[O-]`; bromate `[O-][Br+2]([O-])[O-]`; hypobromous acid `OBr`; bromine `BrBr`; bromide `[Br-]`

- **(1)** $\mathrm{HBrO}$
- (2) $\mathrm{BrO_3^-}$
- (3) $\mathrm{Br_2}$
- (4) $\mathrm{BrO_4^-}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\overset{+1}{\mathrm{HBrO}} \longrightarrow \overset{0}{\mathrm{Br_2}}$, $E^{\circ}_{\mathrm{HBrO/Br_2}} = 1.595\,\mathrm{V}$
2. $\overset{+1}{\mathrm{HBrO}} \longrightarrow \overset{+5}{\mathrm{BrO_3^-}}$, $E^{\circ}_{\mathrm{BrO_3^-/HBrO}} = 1.5\,\mathrm{V}$
3. $E^{0}_{\mathrm{cell}} = E^{0}_{\mathrm{HBrO/Br_2}} - E^{0}_{\mathrm{BrO_3^-/HBrO}}$
4. $= 1.595 - 1.5$
5. $= 0.095\,\mathrm{V} = +\mathrm{ve}$
6. correct option is 1

**Solved independently** (answer withheld)

1. A species disproportionates spontaneously if $E^\circ_{\text{cell}} = E^\circ_{\text{(its reduction)}} - E^\circ_{\text{(couple for its oxidation)}} > 0$.
2. For $\mathrm{HBrO}$: reduction $\mathrm{HBrO} \rightarrow \mathrm{Br_2}$ has $E^\circ = 1.595\,\mathrm{V}$; oxidation $\mathrm{HBrO} \rightarrow \mathrm{BrO_3^-}$ uses the couple $E^\circ_{\mathrm{BrO_3^-}/\mathrm{HBrO}} = 1.5\,\mathrm{V}$.
3. $E^\circ_{\text{cell}} = 1.595 - 1.5 = +0.095\,\mathrm{V} > 0$, so $\mathrm{HBrO}$ disproportionates.
4. For $\mathrm{Br_2}$: $E^\circ_{\text{cell}} = 1.0652 - 1.595 = -0.5298\,\mathrm{V} < 0$, not spontaneous.
5. For $\mathrm{BrO_3^-}$: $E^\circ_{\text{cell}} = 1.5 - 1.82 = -0.32\,\mathrm{V} < 0$, not spontaneous.
6. $\mathrm{BrO_4^-}$ has Br in its highest state $(+7)$ and cannot be oxidised, so it cannot disproportionate.
7. Hence the species is $\mathrm{HBrO}$, option $1$.

**Subtopic:** Cell Potential · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q162_cdb8081b_03112026.png?v=cdb8081b661c)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q162_eaa31eab_03112026.png?v=eaa31eabaf99)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A species on a potential chain disproportionates when the potential on its right is larger than the one on its left, which for HBrO is $1.595$ V against $1.5$ V
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Bromine disproportionating in alkali is the remembered example of the word, so the answer gets taken from that reaction instead of from the potentials printed in the diagram.
- **Why:** This question requires the disproportionation criterion applied to printed potentials, demonstrated by the stem's "change in oxidation state of bromine corresponding to different emf values as shown in the diagram below".
- **Note:** The figure is supplied in our record both as a PNG and as the chain BrO4- to BrO3- to HBrO to Br2 to Br-, with the four potentials attached, so the question is auditable at this step. asks is recorded as apply_rule rather than read_diagram because the diagram supplies four numbers and the whole decision is the criterion applied to two of them.
<!--/ecat-->

## Q163

Chemistry · physical · Basic Concepts of Chemistry

In which case is the number of molecules of water maximum?

- (1) $10^{-3}\,\mathrm{mol}$ of water
- **(2)** $18\,\mathrm{mL}$ of water
- (3) $0.00224\,\mathrm{L}$ of water vapours at $1\,\mathrm{atm}$ and $273\,\mathrm{K}$
- (4) $0.18\,\mathrm{g}$ of water

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The maximum number of water molecules are present in $18\,\mathrm{ml}$ of water.
2. Number of water molecules $= n \times N_A$
3. Hence the correct option is $2$.

**Solved independently** (answer withheld)

1. Number of molecules $N = n N_A$, so the option with the most moles has the most molecules.
2. Option 1: $n = 10^{-3}\,\mathrm{mol}$.
3. Option 2: mass $= 18\,\mathrm{mL} \times 1\,\mathrm{g\,mL^{-1}} = 18\,\mathrm{g}$.
4. Option 2: $n = \frac{18\,\mathrm{g}}{18\,\mathrm{g\,mol^{-1}}} = 1\,\mathrm{mol}$.
5. Option 3: at $1\,\mathrm{atm}$ and $273\,\mathrm{K}$, $n = \frac{0.00224\,\mathrm{L}}{22.4\,\mathrm{L\,mol^{-1}}} = 10^{-4}\,\mathrm{mol}$.
6. Option 4: $n = \frac{0.18\,\mathrm{g}}{18\,\mathrm{g\,mol^{-1}}} = 10^{-2}\,\mathrm{mol}$.
7. The largest is $1\,\mathrm{mol}$, giving $N = 6.022 \times 10^{23}$ molecules, which is option $2$.

**Subtopic:** Mole Concept · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q163_0677e36b_03112026.png?v=0677e36b664e)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q163_b7804c6d_03112026.png?v=b7804c6df1bf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Counting molecules means getting every amount into moles first: through the molar mass for a mass, through the density for a liquid volume, and through 22.4 L per mole only for a gas at STP
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Carrying 22.4 L per mole across to the 18 mL of liquid water gives it only $8\times10^{-4}$ mol, which drops it below the 0.01 mol of the 0.18 g option.
- **Why:** This question requires four amounts converted to a common footing before they can be ranked, demonstrated by the stem's "the number of molecules of water maximum" with a mole, a volume of liquid, a volume of vapour and a mass as the options.
<!--/ecat-->

## Q164

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Carboxylic acids have higher boiling points than aldehydes, ketones and even alcohols of comparable molecular mass, it is due to their

- **(1)** formation of intermolecular H-bonding
- (2) formation of intramolecular H-bonding
- (3) more extensive association of carboxylic acid via van der Waal force of attraction
- (4) formation of carboxylate ion

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Carboxylic acids have higher boiling points than aldehydes and ketones as carboxylic acids can involve intermolecular Hydrogen bonding.
2. Hence the correct option is 1

**Solved independently** (answer withheld)

1. Carboxylic acid molecules associate through extensive intermolecular hydrogen bonding between $\mathrm{-COOH}$ groups, forming dimers that persist even in the vapour phase. So their boiling points are higher than those of aldehydes, ketones and alcohols of comparable molecular mass, which is option $1$.

**Subtopic:** Physical Properties of Aldehydes, Ketones, and Carboxylic Acids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q164_dd81f1dd_03112026.png?v=dd81f1dd0d0f)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q164_31421522_03112026.png?v=31421522ce68)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A carboxylic acid pairs with a second molecule through two hydrogen bonds into a dimer, and it is that intermolecular association which has to be pulled apart to boil it
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Intra and inter differ by two letters in front of the same word, so a student who has stored 'hydrogen bonding' as the reason takes whichever of the two prefixes comes to hand.
- **Why:** This question requires the reason given for a physical property, demonstrated by the stem's "it is due to their" with four rival causes as the options.
- **Note:** Test applied for the trap label: replacing 'intramolecular' with an unlike phrase of the same meaning, such as hydrogen bonding within one molecule, takes the pull away, so what carries the student is the near-identical word rather than the position of a neighbouring fact; hence look_alike_term. E1 called this statement_options from option length; the options are noun phrases completing the stem, so the shape recorded is mcq.
<!--/ecat-->

## Q165

Chemistry · organic · Alcohols, Phenols and Ethers

Compound A, $\mathrm{C_8H_{10}O}$ is found to react with $\mathrm{NaOI}$ (Produced by reacting Y with $\mathrm{NaOH}$) and yields a yellow precipitate with characteristic smell.
A and Y are respectively.

- (1) 2,4-dimethylphenol `Cc1ccc(O)c(C)c1` — $\mathrm{CH_3-C_6H_3(CH_3)-OH}$ and $\mathrm{I_2}$
- (2) (4-methylphenyl)methanol `Cc1ccc(CO)cc1` — $\mathrm{H_3C-C_6H_4-CH_2-OH}$ and $\mathrm{I_2}$
- **(3)** 1-phenylethanol `CC(O)c1ccccc1` — $\mathrm{C_6H_5-CH(OH)-CH_3}$ and $\mathrm{I_2}$
- (4) 2-phenylethanol `OCCc1ccccc1` — $\mathrm{C_6H_5-CH_2-CH_2-OH}$ and $\mathrm{I_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: 1-phenylethanol (A) →(NaOH; I2) benzoate + $\ce{CHI3}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q165_sol_1_5ebc873f_03112026.svg?v=5ebc873f9792)

*1-phenylethanol (A) →[NaOH; I2] benzoate + $\ce{CHI3}$*

![drawn: 1-phenylethanol (A) →(NaOH; I2) benzoate + $\ce{CHI3}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_drawn/q165_solution_1_7f5df099_03112026.svg?v=7f5df0997a0d)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Hence the correct option is 3

**Solved independently** (answer withheld)

1. A yellow precipitate with a characteristic smell formed with $\mathrm{NaOI}$ is iodoform, $\mathrm{CHI_3}$, and $\mathrm{NaOI}$ is made from $\mathrm{I_2 + 2NaOH \rightarrow NaOI + NaI + H_2O}$, so $Y = \mathrm{I_2}$.
2. The iodoform test is positive only for compounds with a $\mathrm{CH_3-CH(OH)-}$ (or $\mathrm{CH_3CO-}$) group.
3. Option $1$ is a phenol (2,4-dimethylphenol) and options $2$ and $4$ are primary alcohols with $\mathrm{-CH_2OH}$ not attached to a $\mathrm{CH_3-CH}$ unit, so none of them gives iodoform.
4. Option $3$, $\mathrm{C_6H_5-CH(OH)-CH_3}$ ($\mathrm{C_8H_{10}O}$), has the $\mathrm{CH_3-CH(OH)-}$ group: $\mathrm{C_6H_5CH(OH)CH_3 + 4I_2 + 6NaOH \rightarrow C_6H_5COONa + CHI_3\downarrow + 5NaI + 5H_2O}$, so the answer is option $3$.

**Subtopic:** Test of Alcohol · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q165_1295c8f6_03112026.png?v=1295c8f6b5c8)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q165_7498ef42_03112026.png?v=7498ef42e007)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** The iodoform test needs a methyl sitting on the carbon that carries the hydroxyl, so NaOI can oxidise it to a methyl ketone and then cleave off CHI3
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  The molecule does carry a methyl group, but on the ring rather than on the carbinol carbon, so a student who checks that a methyl is present without checking where it sits takes it.
- **Why:** This question requires the substrate identified from what a named reagent does to it, demonstrated by the stem's "yields a yellow precipitate with characteristic smell" and by all four options sharing the same molecular formula.
- **Note:** All four options print Y as I2, so the second half of the 'respectively' answer carries no information and the question is decided entirely by A. The shape is still two_part, because the stem asks for both.
<!--/ecat-->

## Q166

Chemistry · organic · Alcohols, Phenols and Ethers

In the reaction The electrophile involved is

![printed figure: phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q166_ecf3b962_03112026.png?v=ecf3b962a1b7)

*phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate*

Structures: phenol `Oc1ccccc1`; chloroform `ClC(Cl)Cl`; sodium hydroxide `[Na+].[OH-]`; sodium 2-formylphenolate `O=Cc1ccccc1[O-].[Na+]`

- **(1)** dichlorocarbene $(:\,\mathrm{CCI_2})$
- (2) dichloromethyl cation $\left(\overset{\otimes}{\mathrm{C}}\mathrm{HCI_2}\right)$
- (3) dichloromethyl anion $\left(\overset{\otimes}{\mathrm{C}}\mathrm{HCI_2}\right)$
- (4) formyl cation $\left(\overset{\otimes}{\mathrm{C}}\mathrm{HO}\right)$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In Riemer Tiemann Reaction the electrophile is dichlorocarbene.
2. Hence the correct option is 1

**Solved independently** (answer withheld)

1. The figure shows phenol $+\ \mathrm{CHCl_3} + \mathrm{NaOH} \rightarrow$ sodium salicylaldehyde (o-$\mathrm{CHO}$ phenoxide), which is the Reimer-Tiemann reaction.
2. $\mathrm{CHCl_3} + \mathrm{OH^-} \rightarrow \mathrm{^{-}CCl_3} + \mathrm{H_2O}$.
3. $\mathrm{^{-}CCl_3} \rightarrow :\mathrm{CCl_2} + \mathrm{Cl^-}$ ($\alpha$-elimination gives dichlorocarbene).
4. The electron-rich phenoxide ring attacks the electron-deficient $:\mathrm{CCl_2}$ at the ortho position, giving an o-$\mathrm{CHCl_2}$ intermediate that hydrolyses to o-$\mathrm{CHO}$.
5. So the electrophile is dichlorocarbene $(:\mathrm{CCl_2})$, which is option $1$.

**Subtopic:** Reactions of Phenols · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q166_da382f34_03112026.png?v=da382f34c8f1)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q166_520a5bc4_03112026.png?v=520a5bc49538)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Chloroform and alkali give dichlorocarbene, a neutral carbon with only six electrons, and that is the electrophile the phenoxide ring attacks
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The ring ends up carrying a CHO group, so the electrophile is read backwards off the product as the formyl cation, which is the electrophile of a different formylation.
- **Why:** This question requires the attacking species named for a printed reaction, demonstrated by the stem's "the electrophile involved is" over a scheme of phenol with CHCl3 and NaOH.
- **Note:** The figure is supplied in our record as a scheme and as a PNG, so the reagents and product are auditable here. Options 2 and 3 are stored with the same formula and the same overset symbol, so the charge that separates them survives only in their names; chlorine is stored as "CI" throughout.
<!--/ecat-->

## Q167

Chemistry · physical · Thermodynamics

The bod dissociation energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are in the ratio of $1 : 0.5 : 1$. $\Delta H$ for the formation of $\mathrm{XY}$ is $-200\,\mathrm{Kj\,mol^{-1}}$. The bond dissociation energy of $\mathrm{X_2}$ WILL BE

- (1) $400\,\mathrm{kJ\,mol^{-1}}$
- (2) $200\,\mathrm{kJ\,mol^{-1}}$.
- **(3)** $800\,\mathrm{kJ\,mol^{-1}}$
- (4) $100\,\mathrm{kJ\,mol^{-1}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The reaction for $\Delta_{f}H^{0}(\mathrm{XY})$
2. $\frac{1}{2}\mathrm{X_2}(g) + \frac{1}{2}\mathrm{Y_2}(g) \rightarrow \mathrm{XY}(g)$
3. Bond energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are $X$, $\frac{X}{2}$, $X$ respectively
4. $\Delta H = \left(\frac{X}{2} + \frac{X}{4}\right) - X = -200$
5. On solving, we get
6. $\Rightarrow -\frac{X}{2} + \frac{X}{4} = -200$
7. $\Rightarrow X = 800\,kj/mole$
8. Hence the correct option is 3.

**Solved independently** (answer withheld)

1. Let the bond dissociation energies be $\mathrm{X_2} = a$, $\mathrm{Y_2} = 0.5a$, $\mathrm{XY} = a$.
2. Formation of $\mathrm{XY}$: $\tfrac{1}{2}\mathrm{X_2} + \tfrac{1}{2}\mathrm{Y_2} \rightarrow \mathrm{XY}$.
3. $\Delta H = \sum \text{BE(broken)} - \sum \text{BE(formed)} = \tfrac{1}{2}a + \tfrac{1}{2}(0.5a) - a = -0.25a$.
4. $-0.25a = -200\,\mathrm{kJ\,mol^{-1}} \Rightarrow a = 800\,\mathrm{kJ\,mol^{-1}}$, which is option $3$.

**Subtopic:** Bond Enthalpy (ΔBondH°) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q167_438dba26_03112026.png?v=438dba267458)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q167_86ca7ce2_03112026.png?v=86ca7ce2d4cf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Forming one mole of XY breaks half an X-X bond and half a Y-Y bond and makes one X-Y bond, so the given enthalpy fixes a quarter of the X2 bond energy
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Writing the reaction as $X_2 + Y_2 \rightarrow 2XY$ and setting the given $-200$ against that equation drops a factor of two, giving $-0.5a = -200$ and $a = 400$.
- **Why:** This question requires a bond-energy balance solved for one unknown, demonstrated by the stem's ratio "1 : 0.5 : 1" together with "$\Delta H$ for the formation of XY is $-200$".
- **Note:** The stem prints "bod dissociation energies" for bond and "Kj mol^-1" for kJ mol^-1, and "WILL BE" in capitals; all recorded as printed and none of it affects the arithmetic.
<!--/ecat-->

## Q168

Chemistry · physical · Chemical Kinetics

When initial concentration of the reactant if doubled the half life periodof a zero order reaction

- (1) remains unchanged
- (2) is halved
- (3) is tripled
- **(4)** is doubled

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The half life period for a zero order reaction is directly proportional to the concn of the reactant.
2. Thus if the concentration of the reactant is doubled the half life period also will be doubled.
3. Hence the correct option is 4

**Solved independently** (answer withheld)

1. For a zero order reaction the integrated rate law is $[A] = [A]_0 - kt$.
2. At $t = t_{1/2}$, $[A] = \frac{[A]_0}{2}$, so $\frac{[A]_0}{2} = [A]_0 - k\,t_{1/2}$.
3. Hence $t_{1/2} = \frac{[A]_0}{2k}$, i.e. $t_{1/2} \propto [A]_0$.
4. Doubling the initial concentration: $t_{1/2}' = \frac{2[A]_0}{2k} = 2\,t_{1/2}$, so the half life is doubled, which is option $4$.

**Subtopic:** Half-Life of a Reaction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q168_04299e30_03112026.png?v=04299e30f232)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q168_f6dda43a_03112026.png?v=f6dda43ab875)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a zero-order reaction the half-life is $[A]_0/2k$, so it scales directly with the starting concentration instead of being independent of it
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The half-life relation that gets drilled is the first-order one, $t_{1/2} = 0.693/k$, which carries no concentration in it, and applying that relation here answers 'remains unchanged'.
- **Why:** This question requires how the half-life scales with the starting concentration for a stated order, demonstrated by the stem's "initial concentration of the reactant if doubled" together with "of a zero order reaction".
- **Note:** The stem prints "if doubled" for is doubled and runs "half life periodof" together; recorded as printed, and neither affects what is asked.
<!--/ecat-->

## Q169

Chemistry · physical · States of Matter

The correction factor ‘$a$’ to the ideal gas equation corresponds to

- **(1)** forces of attraction between the gas molecules
- (2) density of the gas molecules
- (3) electric field present between the gas molecules
- (4) volume of the gas molecules

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The correction factor $a$ to the ideal gas equation corresponds to force of attraction between the gas molecules.
2. Hence the correct option is 1

**Solved independently** (answer withheld)

1. Van der Waals equation: $\left(p + \frac{a n^2}{V^2}\right)(V - nb) = nRT$.
2. The term $\frac{a n^2}{V^2}$ corrects the pressure for the forces of attraction between gas molecules, while $b$ corrects for the volume of the molecules, so option $1$.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q169_47efc09c_03112026.png?v=47efc09c8afa)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q169_3e917f46_03112026.png?v=3e917f462161)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the van der Waals equation the 'a' term corrects the pressure for attraction between molecules, while 'b' corrects the volume for the space the molecules themselves occupy
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The equation carries two correction constants and the other one, 'b', is the molecular volume, so a student who knows there are two corrections but not which letter is which takes the volume.
- **Why:** This question requires the meaning attached to one constant of a named equation, demonstrated by the stem's "The correction factor 'a' to the ideal gas equation corresponds to".
- **Note:** E1 called this statement_options from option length; the options are noun phrases completing the stem, so the shape recorded is mcq.
<!--/ecat-->

## Q170

Chemistry · physical · Chemical Equilibrium

Which one of the following conditions will favour maximum formation of the product in the reaction. $\mathrm{A_2(g) + B_2(g) \rightleftharpoons X_2(g)}\ \Delta_r H = -X\,\mathrm{kJ}$?

- (1) High temperature and low pressure
- **(2)** Low temperature and high pressure
- (3) High temperature and high pressure
- (4) Low temperature and low pressure

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Exothermic reactions are best carried out at low temperature  and high pressure so that the eqb is shifted towards forward direction.
2. Hence the correct option is 2

**Solved independently** (answer withheld)

1. The reaction $\mathrm{A_2(g) + B_2(g) \rightleftharpoons X_2(g)}$ has $\Delta_r H = -X\,\mathrm{kJ} < 0$, so the forward reaction is exothermic.
2. By Le Chatelier's principle, lowering the temperature shifts an exothermic equilibrium forward, so low temperature favours $\mathrm{X_2}$.
3. $\Delta n_g = 1 - (1 + 1) = -1$, so the forward reaction reduces the number of gas moles.
4. Raising the pressure shifts equilibrium toward fewer gas moles, so high pressure favours $\mathrm{X_2}$.
5. Low temperature and high pressure is option $2$.

**Subtopic:** Le Chatelier's Principle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q170_8c5a75e8_03112026.png?v=8c5a75e8ec36)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q170_c7087e47_03112026.png?v=c7087e4701f6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Le Chatelier applied twice: an exothermic reaction is pushed forward by cooling, and a reaction that contracts from two gas moles to one is pushed forward by pressure
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The pressure half is settled correctly from the mole count, and then the temperature is raised because raising it is what makes a reaction go.
- **Why:** This question requires Le Chatelier's principle applied to a printed equilibrium, demonstrated by the stem's "$\Delta_r H = -X$ kJ" together with two gas molecules on the left against one on the right.
- **Note:** E1 called this statement_options from option length; the options are two-word conditions, so the shape recorded is mcq. The stem uses X both as the product's name and as the magnitude of the enthalpy, which is awkward but leaves the sign unambiguous.
<!--/ecat-->

## Q171

Chemistry · physical · Redox Reactions

For the redox reaction
$\mathrm{MnO_4^{-} + C_2O_4^{2-} + H^{+} \rightarrow Mn^{2+} + CO_2 + H_2O}$
The correct coefficient of the reactants for the balanced equation are
$\mathrm{MnO_4^{-}} \quad \mathrm{C_2O_4^{2-}} \quad \mathrm{H^{+}}$

- (1) $5 \quad 16 \quad 2$
- (2) $16 \quad 5 \quad 2$
- (3) $2 \quad 16 \quad 5$
- **(4)** $2 \quad 5 \quad 16$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{KMnO_4}$ acts as oxidizing agent in acidic medium and its n factor is $5$.
2. Oxalate ion n factor is $2$.
3. Hence the correct option is $4$

**Solved independently** (answer withheld)

1. Oxidation states: $\mathrm{Mn}$ goes from $+7$ in $\mathrm{MnO_4^{-}}$ to $+2$ in $\mathrm{Mn^{2+}}$, a gain of $5e^{-}$ per $\mathrm{MnO_4^{-}}$.
2. $\mathrm{C}$ goes from $+3$ in $\mathrm{C_2O_4^{2-}}$ to $+4$ in $\mathrm{CO_2}$, a loss of $2e^{-}$ per $\mathrm{C_2O_4^{2-}}$.
3. Equalise electrons: $2 \times 5 = 5 \times 2 = 10\,e^{-}$, so $2\,\mathrm{MnO_4^{-}} + 5\,\mathrm{C_2O_4^{2-}} \rightarrow 2\,\mathrm{Mn^{2+}} + 10\,\mathrm{CO_2}$.
4. Charge balance: $2(-1) + 5(-2) + x(+1) = 2(+2) \Rightarrow -12 + x = 4 \Rightarrow x = 16\,\mathrm{H^{+}}$.
5. Hydrogen balance gives $8\,\mathrm{H_2O}$; oxygen check: $8 + 20 = 28 = 20 + 8$.
6. Reactant coefficients $\mathrm{MnO_4^{-}} : \mathrm{C_2O_4^{2-}} : \mathrm{H^{+}} = 2 : 5 : 16$, which is option $4$.

**Subtopic:** Balancing of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 34)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q171_83571d18_03112026.png?v=83571d189beb)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q171_86776d2a_03112026.png?v=86776d2affc3)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Balancing a redox equation by electron book-keeping: permanganate gains 5 electrons and each oxalate loses 2, so the two half-reactions are cross-multiplied by 2 and 5 before hydrogen and oxygen are balanced
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Each species is given its own electron count instead of the other's -- 5 in front of $\mathrm{MnO_4^{-}}$ because $\mathrm{Mn(VII)}$ takes 5 electrons and 2 in front of $\mathrm{C_2O_4^{2-}}$ because oxalate gives 2 -- which is the correct pair of numbers with the cross-over left out
- **Why:** This question requires the coefficients to be produced by balancing electrons, charge and atoms for all three reactants together, demonstrated by the stem printing the header row '$\mathrm{MnO_4^{-}}\ \mathrm{C_2O_4^{2-}}\ \mathrm{H^+}$' and every option supplying three numbers that stand or fall as one.
- **Note:** E1's pattern returned plain_mcq on the 16-default; the printed shape is a three-column coefficient row answered as one unit, which is why qtype is recorded as two_part rather than mcq. Key checks out: $2\mathrm{MnO_4^{-}} + 5\mathrm{C_2O_4^{2-}} + 16\mathrm{H^+} \rightarrow 2\mathrm{Mn^{2+}} + 10\mathrm{CO_2} + 8\mathrm{H_2O}$ balances for O (28 each side), H (16 each side) and charge (+4 each side).
<!--/ecat-->

## Q172

Chemistry · organic · Polymers

Regarding cross linked or network polymers, which of the following statements is incorrect?

- **(1)** They contain strong covalent bonds in their polymer chains
- (2) They contain covalent bonds between various linear polymer chains
- (3) Examples are bakelite and melamine
- (4) They are formed from bi- and tri functional monomers

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cross linked or network polymers are formed from bi-functional and tri-functional monomers and contain strong covalent bonds between various linear polymer chains, e.g. bakelite, melamine etc.
2. Option (1) is not related to cross-linking.
3. Hence the correct option is 1

**Solved independently** (answer withheld)

1. Textbook definition: cross-linked (network) polymers are formed from bi-functional and tri-functional monomers and contain strong covalent bonds between various linear polymer chains, e.g. bakelite and melamine.
2. Statement $2$ (covalent bonds between linear chains) matches the definition, so it is correct.
3. Statement $3$ (bakelite and melamine as examples) matches, so it is correct.
4. Statement $4$ (formed from bi- and tri-functional monomers) matches, so it is correct.
5. Statement $1$ places the strong covalent bonds within the chains instead of between them, so it is the intended incorrect statement: option $1$.

**Subtopic:** Classification of Polymers Based on Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q172_e4ee291c_03112026.png?v=e4ee291ccf17)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q172_0438b2b7_03112026.png?v=0438b2b7d762)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What makes a polymer a network is covalent cross-links running BETWEEN separate chains; covalent bonds inside a chain are what every polymer has
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Holding the general fact that polymer chains are built of covalent bonds makes the claim about bonds BETWEEN chains look like the odd one, so the statement that states the defining feature is marked as the incorrect one.
- **Why:** This question requires the defining feature of network polymers held apart from a property every polymer has, demonstrated by option 1's "in their polymer chains" against option 2's "between various linear polymer chains".
- **Note:** Tagged as printed, with the key left at option 1, but the key rests on a wording substitution rather than on the chemistry: option 1 is the textbook sentence with "between various linear polymer chains" changed to "in their polymer chains", and read on its own every polymer does contain strong covalent bonds in its chains, so the statement is true in isolation and is incorrect only as a description of what distinguishes a network polymer. That is why the verdict is arguable_key and the card is flagged.
<!--/ecat-->

## Q173

Chemistry · organic · Amines

Nitration of aniline in strong acidix medium also gives m-nitroaniline because

- **(1)** In acidic (strong) medium aniline is present as anilinium ion.
- (2) In spite of substituents nitro group always goes to only m – position
- (3) In absence of substituents nitro group always goes to m-position
- (4) In electrophilic substitution reactions amino group is meta directive.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In strong acidic medium aniline converts to anilinium ion and it is a meta director.
2. Therefore the correct option is 1

**Solved independently** (answer withheld)

1. In strongly acidic nitrating mixture, aniline is protonated: $\mathrm{C_6H_5NH_2 + H^+ \rightarrow C_6H_5NH_3^+}$ (anilinium ion).
2. The $-\mathrm{NH_3^+}$ group has no lone pair to donate and withdraws electrons by $-I$ effect, so it is deactivating and meta-directing.
3. Hence nitration of the anilinium ion gives a substantial amount of $m$-nitroaniline, which is option $1$; options $2$, $3$ and $4$ are false general claims (free $-\mathrm{NH_2}$ is ortho/para-directing).

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q173_392c3ede_03112026.png?v=392c3ede8111)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q173_761e930b_03112026.png?v=761e930b0e91)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In strongly acidic medium aniline is protonated to the anilinium ion, whose positive nitrogen withdraws electrons and sends nitration to the meta position
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The meta-directing power belongs to the protonated nitrogen, and it gets read onto the amino group itself because that is the group printed in the stem.
- **Why:** This question requires the reason behind an observed product, demonstrated by the stem's trailing "because" together with its stated condition "in strong acidix medium".
- **Note:** The stem prints "acidix" for acidic; recorded as printed. Test applied for the trap label: 'amino group' and 'anilinium ion' do not resemble each other as words, and replacing either with an unlike term leaves the pull intact, so what carries the student is the two species sitting one option apart in the same explanation, not a likeness; hence nearby_fact. qtype is mcq rather than statements: the stem is a trailing 'because' asking for a cause, not an instruction to judge printed statements.
<!--/ecat-->

## Q174

Chemistry · inorganic · The s-Block Elements

Which of the following oxide is most acidic in nature?

- (1) $\mathrm{CaO}$
- (2) $\mathrm{MgO}$
- (3) $\mathrm{BaO}$
- **(4)** $\mathrm{BeO}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{BeO}$ is amphoteric rest all other oxides are basic in nature.
2. Hence the correct option is 4

**Solved independently** (answer withheld)

1. Down Group 2, metallic character rises, so oxides go from amphoteric to strongly basic: $\mathrm{BeO} < \mathrm{MgO} < \mathrm{CaO} < \mathrm{BaO}$ in basic strength.
2. $\mathrm{BeO}$ is amphoteric (reacts with both acids and bases), while $\mathrm{MgO}$, $\mathrm{CaO}$ and $\mathrm{BaO}$ are basic.
3. So the most acidic oxide is $\mathrm{BeO}$, which is option $4$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q174_218fda7e_03112026.png?v=218fda7ea240)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q174_2364faad_03112026.png?v=2364faad06b9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Acidic character of the group-2 oxides falls as the metal grows more electropositive, which leaves BeO, the amphoteric one, at the acidic end
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The group-2 trend that is drilled is basic character rising down the group, and carrying only the direction and not the property puts the most acidic oxide at the bottom, on barium.
- **Why:** This question requires the extreme of a group trend in oxide character, demonstrated by the stem's "most acidic in nature" with four group-2 oxides as the options.
<!--/ecat-->

## Q175

Chemistry · organic · Biomolecules

> ⚠ The independent solve chose (2); the booklet prints (3).

The difference between amylose and amylopectin is

- (1) Amylose is made up of glucose and galactose
- (2) Amylopectin have $1\rightarrow4$ $\alpha$-linkage and $1\rightarrow6$ $\alpha$-linkage
- **(3)** Amylopectin have $1\rightarrow4$ $\alpha$-linkage and $1\rightarrow6$ $\beta$-linkage
- (4) Amylose have $1\rightarrow4$ $\alpha$-linkage and $1\rightarrow6$ $\beta$-linkage

**Answer** — booklet: (3) · independent solve: (2) · differs

**Publisher's solution**

1. Amylose is less branched chain of $\alpha$ 1-4 glycosidic linkage whereas amylopectin is heavily branched and contains $\alpha$ 1-4 glycosidic linkage and $\beta$ 1-6 glycosidic linkage.
2. Hence the correct option is 3

**Solved independently** (answer withheld)

1. Both amylose and amylopectin are polymers of $\alpha$-D-glucose only (no galactose), so option $1$ is false.
2. Amylose is a linear chain joined only by $C_1 \rightarrow C_4$ $\alpha$-glycosidic links, so it has no $1\rightarrow6$ link at all; option $4$ is false.
3. Amylopectin is branched: its chain uses $C_1 \rightarrow C_4$ $\alpha$-links and its branch points use $C_1 \rightarrow C_6$ $\alpha$-links (not $\beta$), so option $3$ is false and option $2$ is correct.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q175_76e6248c_03112026.png?v=76e6248c171f)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q175_4861d40f_03112026.png?v=4861d40f3d47)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Starch is two polymers of glucose: amylose is an unbranched chain of $1\rightarrow4$ linked units, while amylopectin is branched and carries a second linkage at its $1\rightarrow6$ branch points
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Amylose and amylopectin are the same word to within a syllable, and this option prints the branched polymer's description against the unbranched one's name.
- **Why:** This question requires two components of starch held apart, demonstrated by the stem "The difference between amylose and amylopectin is" and by two options printing the same linkage pair against the two different names.
- **Note:** Tagged as printed, with the key left at option 3, but our record's key and the chemistry disagree and that must be resolved before this card is used. The accepted description of amylopectin is $1\rightarrow4$ alpha linkages along the chain and $1\rightarrow6$ ALPHA linkages at the branch points, which is what option 2 states; option 3 prints beta for the branch linkage. So either our stored option order has drifted from the printed paper, in which case the key index is stale, or option 3's text has lost its alpha. Option 2 is therefore left out of other_options deliberately: under the accepted chemistry it is the correct statement, so calling it a trap or a filler would record a false finding either way, and no role can honestly be assigned until the conflict is resolved. Option 4 is wrong under both readings, which is why the trap is written there. E1 returned null for the shape; the options are full statements completing the stem with no lettered block and no combination answer, so mcq is recorded.
<!--/ecat-->

## Q176

Chemistry · physical · Basic Concepts of Chemistry

A mixture of $2.3\,\mathrm{g}$ formic acid and $4.5\,\mathrm{g}$ oxalic acid is treated with conc. $\mathrm{H_2SO_4}$. The evolved gaseous mixture is passed through KOH pellets weight (in g) of the remaining product at STP will be

- (1) $4.4$
- (2) $1.4$
- **(3)** $2.8$
- (4) $3.0$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: formic acid ($\ce{HCOOH}$), 2.3g or (1/20 mol) →(Conc.$\ce{H2SO4}$) carbon monoxide ($\ce{CO(g)}$), 1/20 mol + water ($\ce{H2O(l)}$)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q176_sol_1_2d66e4ef_03112026.png?v=2d66e4ef7586)

*formic acid ($\ce{HCOOH}$), 2.3g or (1/20 mol) →[Conc.$\ce{H2SO4}$] carbon monoxide ($\ce{CO(g)}$), 1/20 mol + water ($\ce{H2O(l)}$)*

![printed figure: oxalic acid ($\ce{COOH-COOH}$), 4.5g or (1/20 mol) →(Conc.$\ce{H2SO4}$) carbon monoxide ($\ce{CO(g)}$), 1/20 mol + carbon dioxide ($\ce{CO2(g)}$), 1/20 mol + water ($\ce{H2O(l)}$)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q176_sol_2_c793cda1_03112026.png?v=c793cda14028)

*oxalic acid ($\ce{COOH-COOH}$), 4.5g or (1/20 mol) →[Conc.$\ce{H2SO4}$] carbon monoxide ($\ce{CO(g)}$), 1/20 mol + carbon dioxide ($\ce{CO2(g)}$), 1/20 mol + water ($\ce{H2O(l)}$)*

1. Gaseous mixture formed is $\mathrm{CO}$ and $\mathrm{CO_2}$ when it is passed through $\mathrm{KOH}$, only $\mathrm{CO_2}$ is absorbed.
2. So the remaining gas is $\mathrm{CO}$.
3. So, weight of remaining gaseous product $\mathrm{CO}$ is $\frac{2}{20} \times 28 = 2.8\,\mathrm{g}$

**Solved independently** (answer withheld)

1. $n(\mathrm{HCOOH}) = \frac{2.3}{46} = 0.05\,\mathrm{mol}$.
2. $\mathrm{HCOOH} \xrightarrow{\text{conc. } \mathrm{H_2SO_4}} \mathrm{CO} + \mathrm{H_2O}$, giving $0.05\,\mathrm{mol}$ CO.
3. $n(\mathrm{H_2C_2O_4}) = \frac{4.5}{90} = 0.05\,\mathrm{mol}$.
4. $\mathrm{H_2C_2O_4} \xrightarrow{\text{conc. } \mathrm{H_2SO_4}} \mathrm{CO} + \mathrm{CO_2} + \mathrm{H_2O}$, giving $0.05\,\mathrm{mol}$ CO and $0.05\,\mathrm{mol}$ $\mathrm{CO_2}$.
5. KOH pellets absorb $\mathrm{CO_2}$ (and water), so only CO remains: $0.05 + 0.05 = 0.10\,\mathrm{mol}$.
6. $m(\mathrm{CO}) = 0.10 \times 28 = 2.8\,\mathrm{g}$, which is option $3$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 35)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q176_754e2307_03112026.png?v=754e2307f09a)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q176_31d56699_03112026.png?v=31d566999a3f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Concentrated sulphuric acid dehydrates formic acid to CO and oxalic acid to CO and CO2 together, and KOH pellets take out only the CO2, so what is left to weigh is all of the CO
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Counting only the formic acid's CO leaves $0.05$ mol instead of $0.1$ mol, and $0.05 \times 28$ gives exactly the printed $1.4$.
- **Why:** This question requires two dehydrations and one selective absorption carried through to a mass, demonstrated by the stem's "treated with conc. H2SO4" and "passed through KOH pellets".
- **Note:** The stem's "at STP" is left over from a version asking for a volume; the options are masses in grams, so the condition does no work here.
<!--/ecat-->

## Q177

Chemistry · physical · Structure of Atom

Which one is wrong statement?

- (1) The value of $m$ for $d_{z}2$ is zero
- (2) Total orbital angular momentum of electron in ‘s’ orbital is equal to zero
- **(3)** ![printed figure: orbital-box diagram of the N atom: 1s² (↑↓), 2s² (↑↓), 2pₓ¹ (↑) 2p_y¹ (↑) 2p_z¹ (↓)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/figures_agent/q177_option_3_c5fe24e2_03112026.png?v=c5fe24e2eb33) *orbital-box diagram of the N atom: 1s² [↑↓], 2s² [↑↓], 2pₓ¹ [↑] 2p_y¹ [↑] 2p_z¹ [↓]* — The electronic configuration of $\mathrm{N}$ atom is
- (4) An orbital is designated by three quantum numbers while an electron in an atom is designated by four quantum numbers.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The electronic configuration written for Nitrogen goes against Hunds rule.
2. Hence the correct option is 3.

**Solved independently** (answer withheld)

1. For $d_{z^2}$, $l = 2$ and the orbital corresponds to $m_l = 0$, so statement 1 is correct.
2. Orbital angular momentum $= \sqrt{l(l+1)}\,\frac{h}{2\pi}$; for an s orbital $l = 0$, so it is $0$ and statement 2 is correct.
3. N ($Z = 7$) is $1s^2\,2s^2\,2p_x^1\,2p_y^1\,2p_z^1$; by Hund's rule the three unpaired $2p$ electrons must have parallel spins ($\uparrow\uparrow\uparrow$).
4. The drawn diagram shows $2p$ as $\uparrow\uparrow\downarrow$, which violates Hund's rule, so statement 3 is wrong.
5. An orbital is fixed by $n, l, m_l$ and an electron by $n, l, m_l, m_s$, so statement 4 is correct.
6. The wrong statement is option $3$.

**Subtopic:** Filling of Orbitals in Atom · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q177_a3fbf941_03112026.png?v=a3fbf941fb6d)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q177_959016ae_03112026.png?v=959016ae0217)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Quantum-number bookkeeping: m is zero for the dz2 orbital, an s electron has zero orbital angular momentum, and three quantum numbers fix an orbital while four fix an electron
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The keyed option is incomplete in our record: option 3 reads "The electronic configuration of N atom is" and stops, so the claim it makes is absent. Checked the other three options, which are all intact and all true, and they leave no wrong option to write a route to; naming a trap here would mean inventing the content of the option the question turns on.
- **Why:** This question requires three printed statements about quantum numbers judged against the stated rules, demonstrated by the stem "Which one is wrong statement?" with the dz2 value of m and the three-against-four quantum numbers among the options.
- **Note:** Option 3's content is missing from our record: the option ends at "is", with no configuration, orbital-box diagram or arrow notation after it. The printed paper almost certainly prints a configuration or an orbital diagram for nitrogen that breaks a rule, most likely Hund's rule or the Pauli principle, and that is what a reviewer holding the paper should check. Until then no option can be shown to be wrong, so no trap is recorded and nothing is written about the other three. The remaining three options were checked and are each correct as printed.
<!--/ecat-->

## Q178

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Consider the following species: $\mathrm{CN^{+}}$, $\mathrm{CN^{-}}$, $\mathrm{NO}$ and $\mathrm{CN}$ Which one of these will have the highest bond order?

- (1) $\mathrm{CN}$
- (2) $\mathrm{NO}$
- (3) $\mathrm{CN^{+}}$
- **(4)** $\mathrm{CN^{-}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{CN^{-}}$ has highest bond order $3$.
2. Hence the correct option is 4.

**Solved independently** (answer withheld)

1. Count electrons: $\mathrm{C} = 6$, $\mathrm{N} = 7$, $\mathrm{O} = 8$, so $\mathrm{CN^{+}} = 12$, $\mathrm{CN} = 13$, $\mathrm{CN^{-}} = 14$, $\mathrm{NO} = 15$ electrons.
2. $\mathrm{CN^{+}}$: $\text{BO} = \frac{8 - 4}{2} = 2$.
3. $\mathrm{CN}$: $\text{BO} = \frac{9 - 4}{2} = 2.5$.
4. $\mathrm{CN^{-}}$ (isoelectronic with $\mathrm{N_2}$): $\text{BO} = \frac{10 - 4}{2} = 3$.
5. $\mathrm{NO}$: $\text{BO} = \frac{10 - 5}{2} = 2.5$.
6. The highest bond order is $3$ for $\mathrm{CN^{-}}$, which is option $4$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q178_aa1f6156_03112026.png?v=aa1f61567a97)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q178_a6dbe9bc_03112026.png?v=a6dbe9bcf730)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Bond order is half the difference between bonding and antibonding electrons, and CN- with 14 valence electrons is isoelectronic with N2, which puts it at a triple bond
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The rule that taking an electron away raises the bond order is carried over from O2 to O2+, where the electron leaves an antibonding orbital; in CN the electron leaving is a bonding one.
- **Why:** This question requires molecular orbital filling applied to four species, demonstrated by the stem's "Which one of these will have the highest bond order?" over a cation, an anion, a neutral radical and NO.
- **Note:** asks is recorded as apply_rule rather than calculate: bond orders are worked out on the way, but the answer the stem asks for is a species, and the decisive move is the filling scheme applied to each.
<!--/ecat-->

## Q179

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Magnesium reacts with an element (X) to form an ionic compound. If the ground state electronic configuration of (X) is $1s^{2}\,2s^{2}\,2p^{3}$, the simplest formula for this compound is:

- **(1)** $\mathrm{Mg_{3}X_{2}}$
- (2) $\mathrm{Mg_{2}X_{3}}$
- (3) $\mathrm{Mg_{2}X}$
- (4) $\mathrm{MgX_{2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. X has $5$ valence electrons hence it can form $\mathrm{X^{3-}}$
2. The correct option is $\mathrm{Mg_{3}X_{2}}$.
3. Hence the correct option is $1$

**Solved independently** (answer withheld)

1. The configuration $1s^{2}\,2s^{2}\,2p^{3}$ has $5$ valence electrons, so $X$ gains $3$ electrons to complete its octet, forming $X^{3-}$.
2. Magnesium loses its $2$ valence electrons to form $\mathrm{Mg^{2+}}$.
3. Charge balance: $3(+2) + 2(-3) = 0$, so the formula is $\mathrm{Mg_{3}X_{2}}$, which is option $1$.

**Subtopic:** Covalent and Ionic Bond · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q179_3d7e288b_03112026.png?v=3d7e288b0211)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q179_2964d831_03112026.png?v=2964d831a1f7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A 2p3 configuration means five valence electrons and an X3- ion, which balances against Mg2+ only in the ratio three magnesium to two X
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The two charges come out right, 2+ and 3-, and are then crossed the wrong way, so the 2 lands on magnesium and the 3 on X.
- **Why:** This question requires a valency read off a configuration and turned into a formula, demonstrated by the stem's "ground state electronic configuration of (X) is 1s2 2s2 2p3" and "the simplest formula".
<!--/ecat-->

## Q180

Chemistry · physical · The Solid State

Iron exhibits bcc structure at room temperature Above $900^{\circ}\mathrm{C}$, it transforms to fcc structure. The ratio of density of iron at room temperature to that at $900^{\circ}\mathrm{C}$ (assuming molar mass and atomic radii of iron remains constant with temperature) is

- (1) $\frac{1}{2}$
- (2) $\frac{\sqrt{3}}{\sqrt{2}}$
- **(3)** $\frac{3\sqrt{3}}{4\sqrt{2}}$
- (4) $\frac{4\sqrt{3}}{3\sqrt{2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\frac{d1}{d2} = \frac{z1}{z2}\left(\frac{a2}{a1}\right)^{3}$
2. The correct option is 3.

**Solved independently** (answer withheld)

1. Density $\rho = \frac{Z M}{N_A a^3}$; with $M$ constant, $\rho \propto \frac{Z}{a^3}$.
2. For bcc, atoms touch along the body diagonal: $\sqrt{3}\,a_1 = 4r \Rightarrow a_1 = \frac{4r}{\sqrt{3}}$, and $Z_1 = 2$.
3. For fcc, atoms touch along the face diagonal: $\sqrt{2}\,a_2 = 4r \Rightarrow a_2 = 2\sqrt{2}\,r$, and $Z_2 = 4$.
4. $a_1^3 = \frac{64 r^3}{3\sqrt{3}}$ and $a_2^3 = 16\sqrt{2}\,r^3$.
5. $\frac{\rho_{bcc}}{\rho_{fcc}} = \frac{Z_1}{Z_2}\cdot\frac{a_2^3}{a_1^3} = \frac{2}{4}\cdot\frac{16\sqrt{2}\,r^3 \cdot 3\sqrt{3}}{64 r^3} = \frac{3\sqrt{3}\sqrt{2}}{8}$.
6. $\frac{3\sqrt{6}}{8} = \frac{3\sqrt{3}}{4\sqrt{2}} \approx 0.92$, which is option $3$.

**Subtopic:** Density and Edge Length Calculations for Cubic Unit Cells · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 36)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/crops/q180_1910771e_03112026.png?v=1910771e4e3a)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_NN/solutions/q180_d067ff4d_03112026.png?v=d067ff4da015)

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Density is $ZM/(a^3N_A)$, so with the radius held fixed the bcc and fcc cells differ both in atoms per cell and in how the edge relates to the radius
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Keeping only the atoms per cell, two against four, gives one half and drops the $a^3$ term, where the two structures also differ.
- **Why:** This question requires the density expression applied to two cubic cells at constant radius, demonstrated by the stem's "assuming molar mass and atomic radii of iron remains constant with temperature" and four surd ratios as the options.
- **Note:** asks is recorded as relation because the answer asked for is how many times the density changes between the two structures, and the options are that ratio rather than a value.
<!--/ecat-->

