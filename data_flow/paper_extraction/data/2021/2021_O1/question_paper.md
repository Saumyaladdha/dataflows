# NEET (UG) 2021 · Code O1

200 questions · source `NEET_Papers/2021/NEET_2021_Code_O1_official.pdf` · every image a CDN link (0 without one) · 73 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Modern Physics

A radioactive nucleus ${}^{A}_{Z}X$ undergoes spontaneous decay in the sequence ${}^{A}_{Z}X \rightarrow {}_{Z-1}B \rightarrow {}_{Z-3}C \rightarrow {}_{Z-2}D$, Atomic number of element X. The possible decay particles in the sequence are:

- **(1)** $\beta^{+}, \alpha, \beta^{-}$
- (2) $\beta^{-}, \alpha, \beta^{+}$
- (3) $\alpha, \beta^{-}, \beta^{+}$
- (4) $\alpha, \beta^{+}, \beta^{-}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. ${}^{A}_{Z}X \rightarrow {}^{A}_{Z-1}B - \beta^{+}$ Decay [atomic no. decreases by $1$]
2. ${}_{Z-1}B \rightarrow {}_{Z-3}C - \alpha$ Decay [atomic no. decreases by $2$]
3. ${}_{Z-3}C \rightarrow {}_{Z-2}D - \beta^{-}$ Decay [atomic no. increases by $1$]

**Solved independently** (answer withheld)

1. In $\beta^{+}$ decay $Z \to Z-1$; in $\alpha$ decay $Z \to Z-2$; in $\beta^{-}$ decay $Z \to Z+1$.
2. $X \to B$: $\Delta Z = (Z-1) - Z = -1$, so the particle is $\beta^{+}$.
3. $B \to C$: $\Delta Z = (Z-3) - (Z-1) = -2$, so the particle is $\alpha$.
4. $C \to D$: $\Delta Z = (Z-2) - (Z-3) = +1$, so the particle is $\beta^{-}$.
5. The sequence $\beta^{+}, \alpha, \beta^{-}$ is option $1$.

**Subtopic:** Alpha, Beta, and Gamma Decay · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 1)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q001_eab78d06_30102026.png?v=eab78d06c677)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q001_52731f97_30102026.png?v=52731f97c3b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Each decay is identified by what it does to the atomic number: $\beta^{+}$ lowers Z by one, $\alpha$ lowers it by two, and $\beta^{-}$ raises it by one
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Reading the first step's drop of one unit as ordinary beta decay inverts both beta signs: $\beta^{-}$ RAISES Z by one, so it cannot produce $Z-1$, and the step that does raise Z, the last one, is then left with $\beta^{+}$.
- **Why:** This question requires the decay rules applied to a printed chain of atomic numbers, demonstrated by the stem's sequence "${}^{A}_{Z}X \rightarrow {}_{Z-1}B \rightarrow {}_{Z-3}C \rightarrow {}_{Z-2}D$" and the request for "The possible decay particles in the sequence".
- **Note:** The stem's trailing fragment "Atomic number of element X." reads as debris from the printed question, and the mass number is dropped from B, C and D; neither affects what the Z subscripts decide, so the question is tagged as printed.
<!--/ecat-->

## Q2

Physics · Capacitance

Polar molecules are the molecules:

- (1) Acquire a dipole moment only when magnetic field is absent.
- **(2)** Having a permanent electric dipole moment .
- (3) Having zero dipole moment.
- (4) presence of electric field due to displacement of charges.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Definition Based

**Solved independently** (answer withheld)

1. In a polar molecule the centres of positive and negative charge are separated even without an external field, so the molecule has a permanent electric dipole moment $\vec{p} \neq 0$, which is option $2$.

**Subtopic:** Dielectrics and Polarisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 1)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q002_b7eb6225_30102026.png?v=b7eb62251da8)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q002_76ff18cf_30102026.png?v=76ff18cf90ae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A polar molecule carries a dipole moment of its own, built into its shape, whether or not any field is applied
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Displacement of charges in an applied field is the description printed beside this one, for what happens to a NON-polar molecule in a dielectric; a student who has the polarisation discussion in mind takes the neighbouring sentence, which describes an induced dipole rather than a permanent one.
- **Why:** This question requires the stated definition of a term, demonstrated by the stem "Polar molecules are the molecules:" with each option a rival completion of the definition.
- **Note:** E1 called this `statement_options`; under the current rule a stem that merely leaves a definition to be completed is not a judge-the-statements question, so `qtype` is `mcq`.
<!--/ecat-->

## Q3

Physics · Current Electricity

The effective resistance of a parallel connection that consists of four wires of equal length, equal area of cross-section and same material is $0.25\,\Omega$. What will be the effective resistance if they are connected in series?

- (1) $1\,\Omega$
- **(2)** $4\,\Omega$
- (3) $0.25\,\Omega$
- (4) $0.5\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Let each wire’s resistance be $R$
2. When all $4$ are in parallel:
3. $R_{eq} = R/4 = 0.25$
4. $R = 1\,\Omega$
5. When all are connected in in series:
6. $R_{eq} = 4R$
7. $= 4\,\Omega$

**Solved independently** (answer withheld)

1. Four identical wires each of resistance $R$ in parallel: $R_p = \frac{R}{4}$.
2. $\frac{R}{4} = 0.25\,\Omega \Rightarrow R = 1\,\Omega$.
3. In series: $R_s = 4R = 4 \times 1\,\Omega = 4\,\Omega$, which is option $2$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 1)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q003_93dddfa3_30102026.png?v=93dddfa3bfb0)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q003_1f7f7da9_30102026.png?v=1f7f7da9609d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For $n$ identical resistors the parallel value is $R/n$ and the series value is $nR$, so the series value is $n^2$ times the parallel one
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $1\,\Omega$ is the resistance of ONE wire, found on the way from $R/4 = 0.25$; the stem asked for the four of them in series, which is four times that.
- **Why:** This question requires a resistance computed from a printed effective value and a count, demonstrated by "The effective resistance of a parallel connection that consists of four wires ... is $0.25\,\Omega$. What will be the effective resistance if they are connected in series?"
<!--/ecat-->

## Q4

Physics · Current Electricity

Column-I gives certain physical terms associated with flow of current through a metallic conductor. Column-II gives some mathematical relations involving electrical quantities. Match Column-I and Column-II with appropriate relations.

| List-I | | List-II | |
|---|---|---|---|
| A | Drift Velocity | P | $\frac{m}{ne^{2}\rho}$ |
| B | Electrical Resistivity | Q | $nev_{d}$ |
| c | Relaxation Period | R | $\frac{eE}{n}\tau$ |
| D | Current Density | S | $\frac{E}{J}$ |

- (1) A-R, B-P, C-S, D-Q
- (2) A-R, B-Q, C-S, D-P
- **(3)** A-R, B-S, C-P, D-Q
- (4) A-R, B-S, C-Q, D-P

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A-R, B-S, C-P, D-Q
2. Direct Formula

**Solved independently** (answer withheld)

1. Drift velocity: $v_d = \frac{eE}{m}\tau$, which matches R, so A-R.
2. From $J = \sigma E$, resistivity $\rho = \frac{1}{\sigma} = \frac{E}{J}$, which is S, so B-S.
3. $\sigma = \frac{ne^{2}\tau}{m} = \frac{1}{\rho}$ gives $\tau = \frac{m}{ne^{2}\rho}$, which is P, so C-P.
4. Current density $J = nev_{d}$, which is Q, so D-Q.
5. A-R, B-S, C-P, D-Q is option $3$.

**Subtopic:** Resistivity, Drift Velocity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q004_22bf59a2_30102026.png?v=22bf59a2d7db)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q004_a3cf5892_30102026.png?v=a3cf58924c9b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The four standard relations of metallic conduction: $v_d=eE\tau/m$, $\rho=E/J$, $\tau=m/ne^2\rho$ and $J=nev_d$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $\frac{m}{ne^{2}\rho}$ is built from exactly the symbols of the resistivity formula $\rho=m/ne^{2}\tau$, so a student matching on symbols gives it to Electrical Resistivity; the $\rho$ sitting in its own denominator is the sign that the relation has already been solved for $\tau$.
- **Why:** This question requires the stated relation for each named conduction quantity, demonstrated by the stem asking the candidate to 'Match Column-I and Column-II with appropriate relations' where each Column-I row names one quantity and each Column-II entry is one printed relation.
- **Note:** List-II entry R reads $\frac{eE}{n}\tau$, where the drift-velocity relation requires $\frac{eE}{m}\tau$; the $m$ has been transcribed as $n$. It cannot change the answer or the trap, because all four options pair A with R, so row A is given away by the option set and no pairing decision rests on that glyph. Flagged for repair. Row C is the one row that needs the stated relation read in rearranged form, which is what the trap turns on; the other three rows are the relations as the chapter prints them.
<!--/ecat-->

## Q5

Physics · Capacitance

The equivalent capacitance of the combination shown in the figure is:

![printed figure: Three capacitors C: two in parallel between the input nodes, one across the right-hand loop](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q005_1fd12901_30102026.png?v=1fd12901ad23)

*Three capacitors C: two in parallel between the input nodes, one across the right-hand loop*

![drawn: Three capacitors C: two in parallel between the input nodes, one across the right-hand loop](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q005_question_db3112dd_02112026.svg?v=db3112ddda33)  
*drawn by code/lib/physics_figure.py*

- (1) $C/2$
- (2) $3C/2$
- (3) $3C$
- **(4)** $2C$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Shorted middle capacitor C removed: circuit reduces to two capacitors C in parallel](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q005_sol_1_d0f03a52_30102026.png?v=d0f03a526585)

*Shorted middle capacitor C removed: circuit reduces to two capacitors C in parallel*

![drawn: Shorted middle capacitor C removed: circuit reduces to two capacitors C in parallel](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q005_solution_1_c8b8c645_02112026.svg?v=c8b8c645f055)  
*drawn by code/lib/physics_figure.py*

1. $C_{eq} = 2C$

**Solved independently** (answer withheld)

1. Call the left terminal $A$ and the right terminal $B$. The top capacitor joins $A$ to node $P$, and the bottom capacitor joins $A$ to node $Q$.
2. Nodes $P$ and $Q$ both connect by plain wire to the right vertical wire, which is terminal $B$, so $V_P = V_Q = V_B$.
3. The middle capacitor sits between $P$ and $Q$, so it has no potential difference across it. It is shorted and adds nothing.
4. The top and bottom capacitors both lie between $A$ and $B$, so they are in parallel: $C_{eq} = C + C = 2C$, which is option $4$.

**Subtopic:** Combination of Capacitors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q005_4217c622_30102026.png?v=4217c6221579)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q005_4c73ae5a_30102026.png?v=4c73ae5a9236)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A capacitor whose two plates are joined to the same node carries no voltage and so adds nothing; only the elements that bridge the two terminals count
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Adding all three capacitors as a parallel bank gives $C + C + C = 3C$; the parallel rule may only be used on elements that sit across the SAME pair of nodes, and the third capacitor in this figure has both of its ends on one node, so it holds no charge.
- **Why:** This question requires the circuit's topology to be read before any formula is used, demonstrated by the stem "The equivalent capacitance of the combination shown in the figure is" and by the figure's netlist, in which one capacitor has both ends on node B.
- **Note:** The figure reached this step as a drawn specification with a netlist, so the shorted capacitor is visible in the record and the trap could be audited.
<!--/ecat-->

## Q6

Physics · Current Electricity

In a potentiometer circuit a cell of EMF $1.5\,\mathrm{V}$ gives balance point at $36\,\mathrm{cm}$ length of wire. If another cell of EMF $2.5\,\mathrm{V}$ replaces the first cell, then at what length of the wire, the balance point occurs?

- (1) $64\,\mathrm{cm}$
- (2) $62\,\mathrm{cm}$
- **(3)** $60\,\mathrm{cm}$
- (4) $21.6\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Potentiometer $\rightarrow$ Comparison of EMFs of cells
2. Direct formula: $\frac{E_1}{E_2} = \frac{\ell_1}{\ell_2}$
3. $\frac{1.5\,V}{2.5\,V} = \frac{36\,cm}{\ell_2}$
4. $\ell_2 = 60\,cm$

**Solved independently** (answer withheld)

1. In a potentiometer, $E \propto l$, so $\frac{E_1}{E_2} = \frac{l_1}{l_2}$.
2. $l_2 = l_1 \frac{E_2}{E_1} = 36\,\mathrm{cm} \times \frac{2.5}{1.5}$.
3. $l_2 = 60\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Potentiometer · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q006_995bcf3c_30102026.png?v=995bcf3c94e3)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q006_3c49cc2a_30102026.png?v=3c49cc2ac963)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On a potentiometer the balancing length is proportional to the EMF being balanced, so the lengths and the EMFs are in the same ratio
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  $21.6\,\mathrm{cm}$ is $36 \times \frac{1.5}{2.5}$, the ratio used upside down; balancing length rises with EMF, so the larger cell must balance further along the wire, not nearer the start.
- **Why:** This question requires a length computed from a printed length and two EMFs, demonstrated by "a cell of EMF $1.5\,\mathrm{V}$ gives balance point at $36\,\mathrm{cm}$ ... at what length of the wire, the balance point occurs?"
<!--/ecat-->

## Q7

Physics · Gravitation

The escape velocity from the Earth’s surface is $v$. The escape velocity from the surface of another planet having a radius, four times that of Earth and same mass density is:

- (1) $3v$
- **(2)** $4v$
- (3) $v$
- (4) $2v$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $v_{escape} = \sqrt{\frac{2GM}{R}}$
2. $= \sqrt{\frac{2G}{R} \times \frac{4}{3}\pi R^{3}\rho} \times \sqrt{\frac{8\pi G}{3}\rho R^{2}}$
3. $V_{escape} \propto R$ [density being same]
4. $V_{escape_{(other\ planet)}} = V_{escape_{(earth)}}$

**Solved independently** (answer withheld)

1. $v_e = \sqrt{\frac{2GM}{R}}$.
2. With the same density, $M = \frac{4}{3}\pi R^3 \rho$.
3. $v_e = \sqrt{\frac{8\pi G \rho R^2}{3}} = R\sqrt{\frac{8\pi G \rho}{3}} \propto R$.
4. $R' = 4R \Rightarrow v' = 4v$, which is option $2$.

**Subtopic:** Escape Velocity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q007_29c22c47_30102026.png?v=29c22c470b03)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q007_fb295d9e_30102026.png?v=fb295d9edd4b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At fixed density a planet's mass grows as the cube of its radius, so the escape velocity $\sqrt{2GM/R}$ grows in direct proportion to the radius
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Using $v_e = \sqrt{2gR}$ with $g$ left at its Earth value gives $\sqrt{4}\,v = 2v$; the stem's "same mass density" is exactly what makes $g$ itself four times larger, and the option is what you get by dropping that condition.
- **Why:** This question requires how many times one quantity changes when another does, demonstrated by "The escape velocity from the Earth's surface is $v$ ... another planet having a radius, four times that of Earth and same mass density" with every option a multiple of $v$.
<!--/ecat-->

## Q8

Physics · Thermal Properties of Matter

A cup of coffee cools from $90^{0}\mathrm{C}$ to $80^{0}\mathrm{C}$ in $t$ minutes, when the room temperature is $20^{0}\mathrm{C}$. The time taken by a similar cup of coffee to cool from $80^{0}\mathrm{C}$ to $60^{0}\mathrm{C}$ at a room temperature same at $20^{0}\mathrm{C}$ is

- (1) $\frac{10}{13}t$
- (2) $\frac{5}{13}t$
- (3) $\frac{13}{10}t$
- **(4)** $\frac{13}{5}t$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Newton’s law of cooling:
2. $-\frac{\Delta T}{\Delta t} = k\left[T_{avg} - T_{0}\right]$
3. 1st case: $\frac{10^{\circ}C}{t} = k\left[85 - 20\right]$
4. 2nd case: $\frac{20^{\circ}C}{t'} k\left[\frac{80 + 60}{2} - 20\right]$
5. $\frac{10}{t} . \frac{t'}{20} = \frac{65}{50}$
6. $t' = \frac{13t}{5}$

**Solved independently** (answer withheld)

1. Average-form Newton's law of cooling: $\frac{\Delta T}{\Delta t} = k\left(\bar{T} - T_s\right)$.
2. First cup: $\frac{90-80}{t} = k\left(\frac{90+80}{2} - 20\right) = 65k$.
3. So $k = \frac{10}{65t}$.
4. Second cup: $\frac{80-60}{t'} = k\left(\frac{80+60}{2} - 20\right) = 50k$.
5. $t' = \frac{20}{50k} = \frac{20 \times 65t}{50 \times 10} = \frac{13}{5}t$, which is option $4$.

**Subtopic:** Newton's Law of Cooling and Bimetallic Strips · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q008_5ac7a73a_30102026.png?v=5ac7a73a6d2c)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q008_11a0231b_30102026.png?v=11a0231b9fca)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Newton's law of cooling makes the rate of fall proportional to the excess of the average temperature of the interval over the room temperature, so each stage must use its own temperature drop and its own average
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Carrying the first stage's $10^{\circ}$ fall into the second stage, which actually falls $20^{\circ}$, halves the answer: $\frac{10}{T} = k(70-20)$ gives $T = \frac{13}{10}t$ instead of $\frac{13}{5}t$.
- **Why:** This question requires a time computed from two cooling stages, demonstrated by "A cup of coffee cools from $90^{0}\mathrm{C}$ to $80^{0}\mathrm{C}$ in $t$ minutes ... The time taken ... to cool from $80^{0}\mathrm{C}$ to $60^{0}\mathrm{C}$".
<!--/ecat-->

## Q9

Physics · Electromagnetic Waves

A capacitor of capacitance ‘C’, is connected across an ac source of voltage V, given by $V = V_0 \sin \omega t$ The displacement current between the plates of the capacitor, would then be given by:

- (1) $I_d = \frac{V_0}{\omega C} \sin \omega t$
- (2) $I_d = V_0 \omega C \sin \omega t$
- **(3)** $I_d = V_0 \omega C \cos \omega t$
- (4) $I_d = \frac{V_0}{\omega C} \cos \omega t$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Conduction current in case of capacitor with Ac source:
2. $I_c = V_0 \omega C \cos \omega t$
3. $\therefore$ Displacement current will be : $V_0 \omega C \cos \omega t$

**Solved independently** (answer withheld)

1. Displacement current between the plates equals the conduction current: $I_d = \epsilon_0 \frac{d\Phi_E}{dt} = \frac{dq}{dt}$.
2. Charge on the capacitor: $q = CV = CV_0 \sin \omega t$.
3. $I_d = \frac{d}{dt}(CV_0 \sin \omega t) = V_0 \omega C \cos \omega t$, which is option $3$.

**Subtopic:** Maxwell's Displacement Current · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q009_0653de51_30102026.png?v=0653de518d52)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q009_7d6e97f6_30102026.png?v=7d6e97f634bb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Displacement current in a capacitor is $C\,\mathrm{d}V/\mathrm{d}t$, so differentiating a sinusoidal voltage turns the sine into a cosine and brings out a factor $\omega C$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Using the amplitude relation $I = V/X_C$ on the instantaneous voltage, $\frac{V_0 \sin \omega t}{1/\omega C}$, gives the right size $V_0\omega C$ but keeps the sine, which says the current peaks when the voltage does; the current is the rate of change of charge, so it leads by a quarter cycle.
- **Why:** This question requires an expression derived from a printed voltage, demonstrated by "$V = V_0 \sin \omega t$ The displacement current between the plates of the capacitor, would then be given by" with four symbolic options.
<!--/ecat-->

## Q10

Physics · Kinematics

A small block slides down on a smooth inclined plane, starting from rest at time $t = 0$. Let $S_n$ be the distance travelled by the block in the interval $t = n - 1$ to $t = n$, Then, the ratio $\frac{S_n}{S_n + 1}$ is:

- (1) $\frac{2n+1}{2n-1}$
- (2) $\frac{2n}{2n-1}$
- (3) $\frac{2n-1}{2n}$
- **(4)** $\frac{2n-1}{2n+1}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $S_{n^{th}} = u + \frac{a}{2}[2n - 1]$
2. $u = 0$
3. $a = g\sin\theta$
4. $S_{n^{th}} = \frac{g\sin\theta}{2}[2n - 1]$
5. $S_{(n+1)^{th}} = \frac{g\sin\theta}{2}[2n + 1]$
6. $\frac{S_n}{S_{(n+1)}} = \frac{2n - 1}{2n + 1}$

**Solved independently** (answer withheld)

1. On a smooth incline the acceleration $a = g\sin\theta$ is constant and the block starts from rest.
2. $S_n = \frac{1}{2}a n^2 - \frac{1}{2}a(n-1)^2 = \frac{a}{2}(2n-1)$.
3. $S_{n+1} = \frac{a}{2}(2(n+1)-1) = \frac{a}{2}(2n+1)$.
4. $\frac{S_n}{S_{n+1}} = \frac{2n-1}{2n+1}$, which is option $4$.

**Subtopic:** Galileo's Law of Odd Number · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q010_76f107a0_30102026.png?v=76f107a07567)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q010_6b672573_30102026.png?v=6b6725735b8b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Starting from rest under constant acceleration the distances covered in successive seconds go as the odd numbers, so the nth interval carries $(2n-1)$ and the next carries $(2n+1)$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  $\frac{2n+1}{2n-1}$ is the key turned over, which is the ratio of the LATER interval to the earlier one; the block speeds up, so the interval that comes second is the longer distance and the asked ratio must be less than one.
- **Why:** This question requires an expression derived for successive intervals of uniformly accelerated motion, demonstrated by "Let $S_n$ be the distance travelled by the block in the interval $t = n - 1$ to $t = n$, Then, the ratio $\frac{S_n}{S_n + 1}$ is".
- **Note:** The stem prints the ratio as $\frac{S_n}{S_n + 1}$, which as typed reads as $S_n$ divided by $S_n+1$; the options are all built from $2n\pm1$, so the intended quantity is $S_{n+1}$ and the question is tagged on that reading.
<!--/ecat-->

## Q11

Physics · Units and Measurements

If force $[F]$, acceleration $[A]$ and time $[T]$ are chosen as the fundamental physical quantities. Find the dimensions of energy.

- (1) $[F]\,[A]\,[T^{-1}]$
- (2) $[F]\,[A^{-1}]\,[T]$
- (3) $[F]\,[A]\,[T]$
- **(4)** $[F]\,[A]\,[T^{2}]$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $E = F^{a}A^{b}T^{c}$
2. $\left[M^{1}L^{2}T^{-2}\right] = \left[MLT^{-2}\right]^{a}\left[LT^{-2}\right]^{b}\left[T^{c}\right]$
3. $M^{1}L^{2}T^{-2} = M^{a}L^{a+b}T^{-2-2b+c}$
4. $a = 1\ b = 1\ c \Rightarrow -2-2+c = -2$
5. $C = +2$
6. $E = \left[F^{1}A^{1}T^{2}\right]$

**Solved independently** (answer withheld)

1. Energy is work done: $E = F \cdot L$.
2. Acceleration has dimensions $[A] = [L T^{-2}]$, so $[L] = [A][T^{2}]$.
3. Substituting: $[E] = [F][L] = [F][A][T^{2}]$, which is option $4$.

**Subtopic:** Dimensional Formulae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q011_21ce5644_30102026.png?v=21ce564476a1)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q011_12a3851c_30102026.png?v=12a3851c9823)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a basis of force, acceleration and time, energy is force times distance, and distance in that basis is acceleration times time squared
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Taking the distance as $[A][T]$ rather than $[A][T^2]$ loses one power of time and gives $[F][A][T]$, which is the dimensional formula of POWER in this basis, since $[A][T]$ is a velocity and force times velocity is power.
- **Why:** This question requires a dimensional formula derived in a new basis, demonstrated by "If force $[F]$, acceleration $[A]$ and time $[T]$ are chosen as the fundamental physical quantities. Find the dimensions of energy."
<!--/ecat-->

## Q12

Physics · Electromagnetic Waves

For a plane electromagnetic wave propagating in $x$ - direction, which one of the following combination gives the correct possible directions for electric field $(E)$ and magnetic field $(B)$ respectively>

- (1) $\hat{j}+\hat{k}, -\hat{j}-\hat{k}$
- (2) $-\hat{j}+\hat{k}, -\hat{j}+\hat{k}$
- (3) $\hat{j}+\hat{k}, \hat{j}+\hat{k}$
- **(4)** $-\hat{j}+\hat{k}, -\hat{j}-\hat{k}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For direction
2. $\vec{E} \times \vec{B} = \vec{C}$
3. 1. $\left(\hat{j}+\hat{k}\right)\times\left(-\hat{j}-\hat{k}\right)=0$ $(wrong)$
4. 2. $\left(\hat{j}\times\hat{k}\right)\times\left(-\hat{j}\times\hat{k}\right)=0$ $(wrong)$
5. 3. $\left(\hat{j}+\hat{k}\right)\times\left(\hat{j}+\hat{k}\right)=0$ $(wrong)$
6. 4. $\left(-\hat{j}+\hat{k}\right)\times\left(-\hat{j}-\hat{k}\right)=\hat{i}+\hat{i}=2\hat{i}$ $(wrong)$

**Solved independently** (answer withheld)

1. For a plane EM wave, $\vec{E} \perp \vec{B}$ and $\vec{E} \times \vec{B}$ points along the propagation direction $+\hat{i}$.
2. Options $1$, $2$, $3$ have $\vec{B} = \pm\vec{E}$, so $\vec{E} \times \vec{B} = 0$; rejected.
3. Option $4$: $\vec{E}\cdot\vec{B} = (-\hat{j}+\hat{k})\cdot(-\hat{j}-\hat{k}) = 1 - 1 = 0$.
4. $(\vec{E}\times\vec{B})_x = E_yB_z - E_zB_y = (-1)(-1) - (1)(-1) = 2 > 0$, so $\vec{E}\times\vec{B} = 2\hat{i}$, along $+x$; option $4$.

**Subtopic:** Transverse Nature of Electromagnetic Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q012_3925d869_30102026.png?v=3925d86987f3)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q012_04b401a2_30102026.png?v=04b401a221b8)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In a plane electromagnetic wave the electric and magnetic fields are perpendicular to each other and to the direction of travel, with $\mathbf{E} \times \mathbf{B}$ pointing the way the wave goes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Its first half, $-\hat{j}+\hat{k}$, is the key's own electric-field direction, and the second half repeats it because 'E and B are in phase' is read as 'E and B point the same way'; in phase means they peak together in time, not that they share a direction.
- **Why:** This question requires a stated rule applied to printed direction pairs, demonstrated by "which one of the following combination gives the correct possible directions for electric field $(E)$ and magnetic field $(B)$ respectively".
- **Note:** E1 called this `multi_part_respectively`; I have mapped that onto `two_part` because the stem asks for two directions "respectively" and half an option scores nothing. If `two_part` is reserved in the allowed values for the Statement I / Statement II shape, this one should be read as `mcq` instead, and nothing else in the rating changes.
<!--/ecat-->

## Q13

Physics · Oscillations

A spring is stretched by $5\,\mathrm{cm}$ by a force $10\,\mathrm{N}$. The time period of the oscillations when a mass of $2\,\mathrm{kg}$ is suspended by it is:

- (1) $3.14\,\mathrm{s}$
- **(2)** $0.628\,\mathrm{s}$
- (3) $0.0628\,\mathrm{s}$
- (4) $6.28\,\mathrm{s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $F = kx \Rightarrow 10 = k\left[5\times10^{-2}\right]$
2. $k = 200$
3. $T = 2\pi\sqrt{\frac{m}{k}} = 2\pi\sqrt{\frac{2}{200}} = 2\pi\sqrt{\frac{1}{100}}$
4. $= 2\pi\left[\frac{1}{10}\right] = \frac{6.28}{10}$
5. $= 0.628$

**Solved independently** (answer withheld)

1. Spring constant from Hooke's law: $k = \frac{F}{x} = \frac{10\,\mathrm{N}}{0.05\,\mathrm{m}} = 200\,\mathrm{N\,m^{-1}}$.
2. Period of a spring-mass system: $T = 2\pi\sqrt{\frac{m}{k}}$.
3. $T = 2\pi\sqrt{\frac{2}{200}} = 2\pi \times 0.1 = 0.628\,\mathrm{s}$, which is option $2$.

**Subtopic:** Calculate Time Period of SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q013_31af007d_30102026.png?v=31af007d0523)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q013_8ce4afec_30102026.png?v=8ce4afec2873)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spring constant comes from the given force and extension in SI units, and the period of the hanging mass is then $2\pi\sqrt{m/k}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Leaving the extension in centimetres gives $k = 10/5 = 2\,\mathrm{N\,m^{-1}}$ instead of $10/0.05 = 200\,\mathrm{N\,m^{-1}}$, and $2\pi\sqrt{2/2} = 6.28\,\mathrm{s}$ is exactly ten times the right answer.
- **Why:** This question requires a number computed from a force, an extension and a mass, demonstrated by "A spring is stretched by $5\,\mathrm{cm}$ by a force $10\,\mathrm{N}$. The time period of the oscillations when a mass of $2\,\mathrm{kg}$ is suspended by it is".
<!--/ecat-->

## Q14

Physics · Work, Energy and Power

A particle is released from height $S$ from the surface of the Earth. At a certain height its kinetic energy is three times its potential energy. The height from the surface of earth and the speed of the particle at that instant are respectively

- (1) $\frac{S}{2}, \frac{\sqrt{3gS}}{2}$
- **(2)** $\frac{S}{4}, \sqrt{\frac{3gS}{2}}$
- (3) $\frac{S}{4}, \frac{3gS}{2}$
- (4) $\frac{S}{4}, \frac{\sqrt{3gS}}{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. So $\frac{1}{2}mu^{2} = 3mgh$
2. $\frac{1}{2}mu^{2} + mgh = mgS$
3. $3mgh + mgh = mgS$
4. $\boxed{h = \frac{S}{4}}$
5. and $u = 6g$

**Solved independently** (answer withheld)

1. Taking PE zero at the surface, total energy is conserved: $K + U = mgS$.
2. With $K = 3U$ at height $h$: $3mgh + mgh = mgS$.
3. So $4mgh = mgS \Rightarrow h = \frac{S}{4}$.
4. Kinetic energy there: $\frac{1}{2}mv^2 = 3mg\frac{S}{4} = \frac{3mgS}{4}$.
5. $v^2 = \frac{3gS}{2} \Rightarrow v = \sqrt{\frac{3gS}{2}}$, which is option $2$.

**Subtopic:** Conservation of Mechanical Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q014_5e3e7076_30102026.png?v=5e3e707692ec)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q014_c5020133_30102026.png?v=c5020133f562)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Mechanical energy is conserved in free fall, so fixing the ratio of kinetic to potential energy fixes the height, and the kinetic share then fixes the speed
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The height is right at $S/4$, and the speed follows from $\frac{1}{2}mv^2=\frac{3}{4}mgS$; clearing the mass but not the $\frac{1}{2}$ leaves $v^2=\frac{3}{4}gS$, whose root is the printed $\frac{\sqrt{3gS}}{2}$
- **Why:** This question requires a conserved-energy split applied to a stated ratio and then converted to a speed, demonstrated by "its kinetic energy is three times its potential energy" and by options that pair a height with a speed to be answered "respectively".
<!--/ecat-->

## Q15

Physics · Ray Optics

A lens of large focal length and large aperture is best suited as an objective of an astronomical telescope since:

- (1) A large aperture contributes to the quality and visibility of the images
- (2) A large area of the objective ensures better light gathering power
- (3) A large aperture provides a better resolution
- **(4)** All of the above

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Fact based

**Solved independently** (answer withheld)

1. Light-gathering power $\propto$ area $\propto D^2$, so a large aperture gives brighter, more visible images; resolving power $\propto \frac{D}{1.22\lambda}$ improves with $D$, and a large $f_o$ gives magnification $m = \frac{f_o}{f_e}$; so options $1$, $2$ and $3$ are all true, which is option $4$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q015_e7b61eca_30102026.png?v=e7b61eca6dd1)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q015_1281bb6e_30102026.png?v=1281bb6e03f7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A telescope objective is made large in aperture because aperture sets both the light gathered and the resolving power, and long in focal length because magnification is $f_o/f_e$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Light-gathering power is the reason NCERT states first for a large objective, so a student who finds that line among the options takes it as the reason and stops, missing that resolution is printed as a second true reason
- **Why:** This question requires the reason the textbook gives for a large-aperture objective, demonstrated by the stem ending in "since:" and by each option being a rival reason rather than a value.
<!--/ecat-->

## Q16

Physics · Electrostatics

Two charged spherical conductors of radius $R_1$ and $R_2$ are connected by a wire. Then the ratio of surface charge densities of the sphere $\left(\sigma_1/\sigma_2\right)$ is:

- (1) $\sqrt{\left(\frac{R_1}{R_2}\right)}$
- (2) $\frac{R_1^2}{R_2^2}$
- (3) $\frac{R_1}{R_2}$
- **(4)** $\frac{R_2}{R_1}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Two spheres R1 and R2 joined by a dashed line, charges (Q1-x) and (Q2+x)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q016_sol_1_e70fad62_30102026.png?v=e70fad627b6e)

*Two spheres R1 and R2 joined by a dashed line, charges (Q1-x) and (Q2+x)*

![drawn: Two spheres R1 and R2 joined by a dashed line, charges (Q1-x) and (Q2+x)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q016_solution_1_08b3933a_02112026.svg?v=08b3933aff57)  
*drawn by code/lib/physics_figure.py*

1. $\frac{K\left(Q_1 - x\right)}{R_1} = \frac{K\left(Q_2 + x\right)}{R_2} = \left(\frac{Q_1 - x}{Q_2 + x}\right) = \frac{R_1}{R_2}$
2. $\frac{\sigma_1}{\sigma_2} = \frac{\left(Q_1 - x\right)4\pi R_2^2}{\left(Q_2 + x\right)4\pi R_1^2} = \left(\frac{Q_1 - x}{Q_2 + x}\right) = \frac{R_2^2}{R_1^2}$
3. $= \frac{R_1}{R_2} \times \frac{R_2^2}{R_1} = \frac{R_2}{R_1}$

**Solved independently** (answer withheld)

1. Joined by a wire, both conductors reach the same potential: $\frac{kQ_1}{R_1} = \frac{kQ_2}{R_2}$.
2. Hence $\frac{Q_1}{Q_2} = \frac{R_1}{R_2}$.
3. Surface charge density is $\sigma = \frac{Q}{4\pi R^2}$, so $\frac{\sigma_1}{\sigma_2} = \frac{Q_1}{Q_2}\cdot\frac{R_2^2}{R_1^2}$.
4. $\frac{\sigma_1}{\sigma_2} = \frac{R_1}{R_2}\cdot\frac{R_2^2}{R_1^2} = \frac{R_2}{R_1}$, which is option $4$.

**Subtopic:** Common Potential and Redistribution of Charge Between Connected Conductors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q016_7fc86553_30102026.png?v=7fc86553ac20)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q016_b7892963_30102026.png?v=b78929637d1a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Joining two conductors equalises potential, so charge divides as the radii and surface charge density goes as the inverse radius
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $R_1/R_2$ is the correct charge ratio produced on the way to the answer, so the derivation's own intermediate result is sitting in the options while the question asked for the density ratio
- **Why:** This question requires the common-potential condition carried through to surface density, demonstrated by "connected by a wire" and by options that are powers of the radius ratio.
<!--/ecat-->

## Q17

Physics · Ray Optics

A convex lens ‘A’ of focal length $20\,\mathrm{cm}$ and a concave lens ‘B’ of focal length $5\,\mathrm{cm}$ are kept along the same axis with a distance ‘d’ between them. If a parallel beam of light falling on ‘A’ leaves ‘B’ as a parallel beam, then the distance ‘d’ in cm will be:

- (1) $50$
- (2) $30$
- (3) $25$
- **(4)** $15$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Convex lens (20cm) and concave lens (5cm) on one axis: parallel beam in, parallel beam out](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q017_sol_1_210cc6bc_30102026.png?v=210cc6bc6eb4)

*Convex lens (20cm) and concave lens (5cm) on one axis: parallel beam in, parallel beam out*

![drawn: Convex lens (20cm) and concave lens (5cm) on one axis: parallel beam in, parallel beam out](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q017_solution_1_fd288dbe_02112026.svg?v=fd288dbe02e5)  
*drawn by code/lib/physics_figure.py*

1. Separation between the lens: $15\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Parallel light leaving $B$ means the combination has zero power: $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2} = 0$.
2. Substitute $f_1 = +20\,\mathrm{cm}$, $f_2 = -5\,\mathrm{cm}$: $\frac{1}{20} - \frac{1}{5} + \frac{d}{100} = 0$.
3. $\frac{d}{100} = \frac{3}{20} \Rightarrow d = 15\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Position of Equivalent Lens When Two Lenses are Separated by a Distance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q017_d00d9693_30102026.png?v=d00d9693c0ee)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q017_f29086a2_30102026.png?v=f29086a2994d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Parallel light in and parallel light out means the second lens's focal point coincides with the first's, so the separation is the signed sum of the focal lengths
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The beam-expander rule "separation equals the sum of the focal lengths" is held without its signs, so the concave lens is entered as $+5$ and $20+5$ gives 25
- **Why:** This question requires the separated-lens condition for an afocal pair worked with lens signs, demonstrated by "a parallel beam of light falling on 'A' leaves 'B' as a parallel beam" and by the options being lengths in cm.
<!--/ecat-->

## Q18

Physics · Magnetic Effect of Electric Current

An infinitely long straight conductor carries a current of $5\,\mathrm{A}$ as shown. An electron is moving with a speed of $10^{5}\,\mathrm{m/s}$ parallel to the conductor. The perpendicular distance between the electron and the conductor is $20\,\mathrm{cm}$ at an instant. Calculate the magnitude of the force experienced by the electron at the instant.

![printed figure: Straight conductor PQ carrying 5 A, electron moving parallel to it at 20 cm with speed 10^5 m/s](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q018_1c1e90f7_30102026.png?v=1c1e90f7a77c)

*Straight conductor PQ carrying 5 A, electron moving parallel to it at 20 cm with speed 10^5 m/s*

![drawn: Straight conductor PQ carrying 5 A, electron moving parallel to it at 20 cm with speed 10^5 m/s](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q018_question_52e49620_02112026.svg?v=52e49620d945)  
*drawn by code/lib/physics_figure.py*

- (1) $4\pi \times 10^{-20}\,\mathrm{N}$
- **(2)** $8 \times 10^{-20}\,\mathrm{N}$
- (3) $4 \times 10^{-20}\,\mathrm{N}$
- (4) $8\pi \times 10^{-20}\,\mathrm{N}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\beta = \frac{\mu_0}{4\pi}\left(\frac{2I}{r}\right)$
2. $F = qBV$
3. $F = 1.6 \times 10^{-19} \times 10^{-7} \times \frac{2 \times 5}{0.2} \times 10^{5}$
4. $= \frac{16}{0.2} \times 10^{-26} \times 10^{5} = 8 \times 10^{-20}\,N$

**Solved independently** (answer withheld)

1. Field of a long straight wire at distance $r$: $B = \frac{\mu_0 I}{2\pi r}$.
2. $B = \frac{4\pi \times 10^{-7} \times 5}{2\pi \times 0.2} = 5 \times 10^{-6}\,\mathrm{T}$.
3. The electron moves parallel to the wire, so $\vec v \perp \vec B$ and $\sin 90^\circ = 1$.
4. $F = evB = 1.6 \times 10^{-19} \times 10^{5} \times 5 \times 10^{-6} = 8 \times 10^{-20}\,\mathrm{N}$, which is option $2$.

**Subtopic:** Magnetic Field, Lorentz Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q018_f7a3c914_30102026.png?v=f7a3c9141baf)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q018_efa8e521_30102026.png?v=efa8e521c7a6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The field of a long straight wire is $\mu_0I/2\pi r$, and a charge moving perpendicular to that field feels $qvB$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The two field formulas taught together differ only by a $\pi$, and taking the loop-centre form $\mu_0I/2r$ for the straight wire multiplies the field by $\pi$, turning $8\times10^{-20}$ N into the printed $8\pi\times10^{-20}$ N
- **Why:** This question requires the straight-wire field substituted into the magnetic force on a moving charge, demonstrated by "Calculate the magnitude of the force experienced by the electron" with $5\,\mathrm{A}$, $10^{5}\,\mathrm{m/s}$ and $20\,\mathrm{cm}$ all supplied.
- **Note:** The figure only repeats the geometry already stated in words (wire, electron parallel to it, 20 cm), so the numbers needed are all in the stem.
<!--/ecat-->

## Q19

Physics · Units and Measurements

If $E$ and $G$ respectively denote energy and gravitational constant, then $E/G$ has dimensions of:

- (1) $[\mathrm{M}][\mathrm{L}^{0}][\mathrm{T}^{0}]$
- (2) $[\mathrm{M}^{2}][\mathrm{L}^{-2}][\mathrm{T}^{-1}]$
- **(3)** $[\mathrm{M}^{2}][\mathrm{L}^{-1}][\mathrm{T}^{0}]$
- (4) $[\mathrm{M}][\mathrm{L}^{-1}][\mathrm{T}^{-1}]$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $[G] = \frac{F.r^{2}}{m^{2}} = [M^{-1}L^{3}T^{-2}]$
2. $[E] = [M^{-1}L^{2}T^{-2}]$
3. $\frac{[E]}{[G]} = \frac{[M^{-1}L^{2}T^{-2}]}{[M^{-1}L^{3}T^{-2}]} = [M^{2}L^{-1}T^{0}]$

**Solved independently** (answer withheld)

1. Energy: $[E] = [\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-2}]$.
2. From $F = \frac{G m_1 m_2}{r^2}$, $[G] = \frac{[F][L^2]}{[M^2]} = [\mathrm{M}^{-1}\mathrm{L}^{3}\mathrm{T}^{-2}]$.
3. $\frac{[E]}{[G]} = \frac{[\mathrm{M}\mathrm{L}^{2}\mathrm{T}^{-2}]}{[\mathrm{M}^{-1}\mathrm{L}^{3}\mathrm{T}^{-2}]} = [\mathrm{M}^{2}\mathrm{L}^{-1}\mathrm{T}^{0}]$, which is option $3$.

**Subtopic:** Dimensional Formulae · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q019_e1a41ec6_30102026.png?v=e1a41ec6ab1c)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q019_fe272786_30102026.png?v=fe272786bd18)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A dimensional formula for a quotient is obtained by subtracting the exponents of $G=[M^{-1}L^{3}T^{-2}]$ from those of $E=[ML^{2}T^{-2}]$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The one relation that makes energy divided by a constant into a mass is $m=E/c^2$, and carrying that shape over to $E/G$ gives a bare $[M][L^0][T^0]$ without ever writing $G$'s dimensions down
- **Why:** This question requires two dimensional formulae recalled and their exponents subtracted, demonstrated by "then $E/G$ has dimensions of" and by options written entirely as $M$, $L$, $T$ powers.
<!--/ecat-->

## Q20

Physics · Mechanical Properties of Fluids

The velocity of a small ball of mass $M$ and density $d$, when dropped in a container filled with glycerine becomes constant after some time. If the density of glycerine is $\frac{d}{2}$, then the viscous force acting on the ball will be :

- (1) $\frac{3}{2}Mg$
- (2) $2\,Mg$
- **(3)** $\frac{Mg}{2}$
- (4) $Mg$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Viscous force = weight - buoyant force
2. $= Vd_{1}g - Vd_{2}g$
3. $= Vd_{1}g - V\frac{d}{2}g$
4. $= \frac{Vdg}{2} = \frac{mg}{2}$

**Solved independently** (answer withheld)

1. At constant (terminal) velocity the net force is zero: $F_v + F_B = Mg$.
2. Volume of ball: $V = \frac{M}{d}$.
3. Buoyant force: $F_B = V \cdot \frac{d}{2} \cdot g = \frac{M}{d}\cdot\frac{d}{2}g = \frac{Mg}{2}$.
4. $F_v = Mg - \frac{Mg}{2} = \frac{Mg}{2}$, which is option $3$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q020_24d418c4_30102026.png?v=24d418c43b06)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q020_11041cc6_30102026.png?v=11041cc6ec9f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At terminal velocity the viscous force carries only the part of the weight that the upthrust does not, so $F=Mg\left(1-\frac{\rho_{\text{fluid}}}{\rho_{\text{ball}}}\right)$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  "Velocity becomes constant" gives zero net force, and reading that balance as viscous force against weight alone yields $Mg$ — which is the answer only for a fluid of negligible density, while the stem prints the glycerine's density as $d/2$
- **Why:** This question requires the terminal-velocity force balance written with the upthrust, demonstrated by "the density of glycerine is $\frac{d}{2}$" being supplied alongside the ball's density.
<!--/ecat-->

## Q21

Physics · Semiconductor Electronics

The electron concentration in an n-type semiconductor is the same as hole concentration in a p-type semiconductor. An external field (electric) is applied across each of them. Compare the currents in them.

- **(1)** Current in n-type $>$ current in p-type
- (2) No current will flow in p-type, current will only flow in n-type
- (3) Current in n-type $=$ current in p-type
- (4) Current in p-type $>$ current in n-type

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. All the other factors are same, so due to mobility
2. option (a)

**Solved independently** (answer withheld)

1. Current through a semiconductor is $I = n e A v_d = n e A \mu E$.
2. Given $n_e$ (n-type) $= n_h$ (p-type), and the same $E$ (and $A$) for both, so $I \propto \mu$.
3. Electrons have higher mobility than holes: $\mu_e > \mu_h$.
4. Hence $I_n > I_p$, i.e. current in n-type $>$ current in p-type, which is option $1$.

**Subtopic:** Mobility of Electrons and Holes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q021_a021184d_30102026.png?v=a021184d53d1)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q021_b933238e_30102026.png?v=b933238e35b8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Current density is $nq\mu E$, and electron mobility is higher than hole mobility, so equal carrier concentrations do not give equal currents
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Carrying current as "proportional to the number of carriers" makes equal concentrations in equal fields give equal currents, because the mobility factor has been dropped from $J=nq\mu E$
- **Why:** This question requires two samples held apart on mobility after concentration has been equalised, demonstrated by "The electron concentration in an n-type semiconductor is the same as hole concentration in a p-type semiconductor" and by "Compare the currents in them".
<!--/ecat-->

## Q22

Physics · Magnetic Effect of Electric Current

A thick current cable of radius $R$ carries current ‘$I$’ uniformly distributed across its cross - section. The variation of magnetic field $B(r)$ due to the cable with the distance ‘$r$’ from the axis of the cable is represented by :

- **(1)** ![printed figure: B against r: rises linearly from the origin to a peak at the cable surface, then falls off as a decaying curve](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q022_option_1_192151e6_30102026.png?v=192151e636d2) *B against r: rises linearly from the origin to a peak at the cable surface, then falls off as a decaying curve* ![drawn: B against r: rises linearly from the origin to a peak at the cable surface, then falls off as a decaying curve](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q022_option_1_17c1658b_02112026.svg?v=17c1658b6869)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: B versus r: rises steeply from zero at the origin, then flattens towards a roughly constant value](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q022_option_2_43c1a335_30102026.png?v=43c1a3356646) *B versus r: rises steeply from zero at the origin, then flattens towards a roughly constant value* ![drawn: B versus r: rises steeply from zero at the origin, then flattens towards a roughly constant value](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q022_option_2_aef9271c_02112026.svg?v=aef9271c8309)  
*drawn by code/lib/physics_figure.py*
- (3) ![printed figure: B against r: curve rising from the origin, concave upward, steepening](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q022_option_3_6509e38c_30102026.png?v=6509e38c2ae3) *B against r: curve rising from the origin, concave upward, steepening* ![drawn: B against r: curve rising from the origin, concave upward, steepening](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q022_option_3_c93b611c_02112026.svg?v=c93b611ce195)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: B against r: a straight line rising from the origin](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q022_option_4_d7c5628a_30102026.png?v=d7c5628a5850) *B against r: a straight line rising from the origin* ![drawn: B against r: a straight line rising from the origin](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q022_option_4_96fff0df_02112026.svg?v=96fff0df4bdf)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Concentric circles: cable cross-section with an inner Amperian loop of radius x](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q022_sol_1_12292866_30102026.png?v=1229286616a0)

*Concentric circles: cable cross-section with an inner Amperian loop of radius x*

![drawn: Concentric circles: cable cross-section with an inner Amperian loop of radius x](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q022_solution_1_bd154b66_02112026.svg?v=bd154b661751)  
*drawn by code/lib/physics_figure.py*

1. $J = \frac{I}{\pi R^{2}}$
2. $I_{e_n} = \frac{1}{\pi R^{2}} \times \pi x^{2} = \frac{Ix^{2}}{R^{2}}$
3. $\mu_0 I_{e_n} = \int \vec{B}.d\vec{l}$
4. $\mu_0 \frac{Ix^{2}}{R^{2}} = B \times 2\pi x$
5. $\Rightarrow B \propto x$
6. Initially it will increase linearly
7. After ‘R’ $\Rightarrow \mu_0 I = B \times 2\pi x$
8. $B \propto \frac{1}{x}$

![printed figure: Cross-section of the cable with a radial distance x drawn from its axis to a point outside](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q022_sol_2_e34f132d_30102026.png?v=e34f132d1dfe)

*Cross-section of the cable with a radial distance x drawn from its axis to a point outside*

![drawn: Cross-section of the cable with a radial distance x drawn from its axis to a point outside](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q022_solution_2_09009a44_02112026.svg?v=09009a44d964)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. Inside ($r<R$) the enclosed current is $I_{enc} = I\frac{r^2}{R^2}$.
2. Ampere's law gives $B(2\pi r) = \mu_0 I\frac{r^2}{R^2}$, so $B = \frac{\mu_0 I r}{2\pi R^2} \propto r$ (straight line through the origin).
3. Outside ($r\ge R$) $I_{enc}=I$, so $B = \frac{\mu_0 I}{2\pi r} \propto \frac{1}{r}$ (falling hyperbola).
4. $B$ is maximum at $r=R$, i.e. linear rise then $1/r$ decay, which is the graph in option $1$.

**Subtopic:** Ampere's Circuital Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q022_9151f197_30102026.png?v=9151f197e6a0)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q022_2684341c_30102026.png?v=2684341c3a5a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Ampere's law inside a uniformly filled cable gives $B\propto r$ and outside gives $B\propto 1/r$, with the maximum at the surface $r=R$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs of $B(r)$ and none of them was supplied to this step: all four option strings are empty and no figure accompanies the question, so no option can be inspected
- **Why:** This question requires the field of a thick cable read as a plot against distance, demonstrated by "The variation of magnetic field $B(r)$ due to the cable with the distance '$r$' from the axis of the cable is represented by :" with graphs in place of text options.
- **Note:** All four options_en values are empty strings and has_figure is false, so the graphs the question turns on are not in this packet; the paper itself is intact, so this is a reach limit on our side and not source damage. A reviewer holding the option graphs should check two things: whether a plot showing $B$ falling as $1/r$ from the axis outward (no rise inside the conductor) is offered, and whether a plot with the kink at $r=R$ replaced by a continuous rise is offered, since those are the two ways the inside branch $B\propto r$ is usually lost.
<!--/ecat-->

## Q23

Physics · Units and Measurements

A screw gauge gives the following readings when used to measure the diameter of a wire
Main scale reading : $0\,\mathrm{mm}$
Circular scale reading : $52$ divisions
Given that $1\,\mathrm{mm}$ on main scale corresponds to $100$ divisions on the circular scale. The diameter of the wire from the above data is:

- (1) $0.26\,\mathrm{cm}$
- **(2)** $0.052\,\mathrm{cm}$
- (3) $0.52\,\mathrm{cm}$
- (4) $0.026\,\mathrm{cm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{M.S.R} + \mathrm{L.C} \times \mathrm{C.S.R}$
2. $= \frac{1}{100} \times 52 = 0.52\,\mathrm{mm} = 0.052\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Least count: $LC = \frac{1\,\mathrm{mm}}{100} = 0.01\,\mathrm{mm}$.
2. Diameter: $d = MSR + CSR \times LC = 0 + 52 \times 0.01\,\mathrm{mm} = 0.52\,\mathrm{mm}$.
3. Convert: $0.52\,\mathrm{mm} = 0.052\,\mathrm{cm}$, which is option $2$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q023_1fcc1a67_30102026.png?v=1fcc1a67f113)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q023_13e2b2af_30102026.png?v=13e2b2af4146)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A screw gauge reading is the main scale plus the circular-scale count times the least count, where the least count is the pitch divided by the number of circular divisions
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $52\times0.01=0.52$ mm is the right number, and the options are in cm, so the answer is picked by its digits before the millimetre-to-centimetre step is taken
- **Why:** This question requires a least count built from the stem's own pitch and then applied to the circular reading, demonstrated by "Given that $1\,\mathrm{mm}$ on main scale corresponds to $100$ divisions on the circular scale" with options printed in cm.
<!--/ecat-->

## Q24

Physics · Modern Physics

The number of photons per second on an average emitted by the source of monochromatic light of wavelength $600\,\mathrm{nm}$, when it delivers the power of $3.3 \times 10^{-3}\,\mathrm{watt}$ will be : ($h = 6.6 \times 10^{-34}\,\mathrm{Js}$)

- **(1)** $10^{16}$
- (2) $10^{15}$
- (3) $10^{18}$
- (4) $10^{17}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $P = 3.3 \times 10^{-3}$
2. $3.3 \times 10^{-3} = h \times \frac{hc}{\lambda}$
3. $h = 100 \times 10^{14} = 10^{16}$

**Solved independently** (answer withheld)

1. Energy of one photon: $E = \frac{hc}{\lambda}$.
2. $E = \frac{6.6 \times 10^{-34} \times 3 \times 10^{8}}{600 \times 10^{-9}} = 3.3 \times 10^{-19}\,\mathrm{J}$.
3. Photons per second: $N = \frac{P}{E}$.
4. $N = \frac{3.3 \times 10^{-3}}{3.3 \times 10^{-19}} = 10^{16}\,\mathrm{s^{-1}}$, which is option $1$.

**Subtopic:** Photon Energy and Number of Photons · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q024_9428a5dc_30102026.png?v=9428a5dccd14)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q024_c92dee8b_30102026.png?v=c92dee8bf7c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The photon rate is the power divided by the energy of one photon, $n=P\lambda/hc$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Converting $600\,\mathrm{nm}$ with $10^{-10}$ instead of $10^{-9}$ makes $\lambda=6\times10^{-8}$ m, and $n=P\lambda/hc$ then returns $10^{15}$ in place of $10^{16}$
- **Why:** This question requires the power divided by a single photon's energy, demonstrated by "delivers the power of $3.3 \times 10^{-3}\,\mathrm{watt}$" with $h$ supplied and options that differ only in their exponent.
<!--/ecat-->

## Q25

Physics · Work, Energy and Power

Water falls from a height of $60\,\mathrm{m}$ at the rate of $15\,\mathrm{kg/s}$ to operate a turbine. The losses due to frictional force are $10\%$ of the input energy. How much power is generated by the turbine? ($g = 10\,\mathrm{m/s^2}$)

- (1) $12 .3\,\mathrm{kW}$
- (2) $7.0\,\mathrm{kW}$
- (3) $10.2\,\mathrm{kW}$
- **(4)** $8.1\,\mathrm{kW}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $P_i = (15)(10)(60) = 9000\,\mathrm{W}$
2. $P_{\mathrm{loss}} = (10/100) \times 9000 = 900\,\mathrm{W}$

**Solved independently** (answer withheld)

1. Input power is the rate of loss of potential energy: $P_{in} = \frac{dm}{dt} g h$.
2. $P_{in} = 15 \times 10 \times 60 = 9000\,\mathrm{W}$.
3. Losses are $10\%$, so $P_{out} = 0.9 \times P_{in}$.
4. $P_{out} = 0.9 \times 9000 = 8100\,\mathrm{W} = 8.1\,\mathrm{kW}$, which is option $4$.

**Subtopic:** Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 12)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q025_4a304db6_30102026.png?v=4a304db6c9bf)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q025_c79acd8c_30102026.png?v=c79acd8cfe7f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The power available from falling water is $\dot m g h$, and a stated percentage loss scales that input down
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the one slip this stem invites is skipping the loss, which gives $15\times10\times60=9.0$ kW, and $9.0$ kW is not printed; I also ran $g=9.8$ ($7.9$ kW), adding the $10\%$ instead of subtracting it ($9.9$ kW), and taking the loss off the output rather than the input ($8.1$ kW again), and none of $12.3$, $10.2$ or $7.0$ is reached
- **Why:** This question requires an input power from a mass flow rate and height, reduced by a stated percentage, demonstrated by "at the rate of $15\,\mathrm{kg/s}$" and "losses due to frictional force are $10\%$ of the input energy".
- **Note:** The usual distractor for this stem, the un-reduced 9.0 kW, is absent from the options, which is why the trap is no_trap: the three wrong values sit off every route through the stem's own numbers.
<!--/ecat-->

## Q26

Physics · Modern Physics

An electromagnetic wave of wavelength ‘$\lambda$’ is incident on a photosensitive surface of negligible work function. If ‘m’ mass is of photoelectron emitted from the surface has de-Broglie wavelength $\lambda_d$, then :

- **(1)** $\lambda = \left(\frac{2mc}{h}\right)\lambda_d^2$
- (2) $\lambda = \left(\frac{2h}{mc}\right)\lambda_d^2$
- (3) $\lambda = \left(\frac{2m}{hc}\right)\lambda_d^2$
- (4) $\lambda_d = \left(\frac{2mc}{h}\right)\lambda^2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $K.E = \frac{hc}{\lambda}$ $\lambda_d = \frac{h}{p} = \frac{h}{\sqrt{2mK.E.}}$
2. $\lambda_d = \frac{h}{\sqrt{2m\frac{hc}{\lambda}}} = \sqrt{\frac{h\lambda}{2mc}}$
3. $\Rightarrow \lambda_d^2 = \left(\frac{h}{2mC}\right)\lambda$

**Solved independently** (answer withheld)

1. Negligible work function, so all photon energy becomes kinetic energy: $K = \frac{hc}{\lambda}$.
2. de Broglie wavelength of the electron: $\lambda_d = \frac{h}{\sqrt{2mK}}$, so $\lambda_d^2 = \frac{h^2}{2mK}$.
3. Substitute $K$: $\lambda_d^2 = \frac{h^2 \lambda}{2mhc} = \frac{h\lambda}{2mc}$.
4. Rearrange: $\lambda = \left(\frac{2mc}{h}\right)\lambda_d^2$, which is option $1$.

**Subtopic:** Photoelectric Effect, de Broglie Wavelength of Matter Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q026_e91cc9e2_30102026.png?v=e91cc9e2e819)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q026_8122f9e6_30102026.png?v=8122f9e643be)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With a negligible work function the whole photon energy $hc/\lambda$ becomes the electron's kinetic energy, and that kinetic energy fixes its momentum and so its de Broglie wavelength $\lambda_d=h/p$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The prefactor $\frac{2mc}{h}$ is the one the derivation produces, and the option keeps it while exchanging the two wavelengths, so the squared wavelength becomes the light's instead of the electron's
- **Why:** This question requires a photon energy equated to an electron's kinetic energy and rewritten through $p=h/\lambda_d$, demonstrated by "a photosensitive surface of negligible work function" and by options that are rival algebraic relations between $\lambda$ and $\lambda_d$.
<!--/ecat-->

## Q27

Physics · Kinetic Theory of Gases

Match Column-I and Column-II and choose the correct match from the given choices.

| List-I | | List-II | |
|---|---|---|---|
| A | Root mean square speed of gas molecules | P | $\frac{1}{3}nmv^{-2}$ |
| B | Pressure exerted by ideal gas | Q | $\sqrt{\frac{3MT}{M}}$ |
| c | Average kinetic energy of a molecule | R | $\frac{5}{2}RT$ |
| D | Total internal energy of 1 mole of a diatomic gas | S | $\frac{3}{2}k_BT$ |

- **(1)** A-Q, B-P, C-S, D-R
- (2) A-R, B-Q, C-P, D-S
- (3) A-R, B-P, C-S, D-Q
- (4) A-Q, B-R, C-S, D-P

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Formula Based

**Solved independently** (answer withheld)

1. Root mean square speed: $v_{rms} = \sqrt{\frac{3RT}{M}}$, which matches Q, so A-Q.
2. Kinetic theory pressure: $P = \frac{1}{3} n m \overline{v^2}$, which matches P, so B-P.
3. Average kinetic energy of a molecule: $\bar{E} = \frac{3}{2} k_B T$, which matches S, so C-S.
4. A diatomic gas has $f = 5$, so for 1 mole $U = \frac{f}{2}RT = \frac{5}{2}RT$, which matches R, so D-R.
5. A-Q, B-P, C-S, D-R is option $1$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q027_43d9a7ea_30102026.png?v=43d9a7eabf05)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q027_f627e565_30102026.png?v=f627e565187b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The four standard kinetic-theory results: $v_{rms}=\sqrt{3RT/M}$, $P=\frac{1}{3}nm\overline{v^{2}}$, $\overline{KE}=\frac{3}{2}k_BT$ and $U=\frac{5}{2}RT$ per mole of a diatomic gas
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  In $\frac{1}{3}nm\overline{v^{2}}$ the $n$ is a number density, but read as a count of molecules the whole expression becomes an energy, so Total internal energy is paired with it and Pressure is left with $\frac{5}{2}RT$.
- **Why:** This question requires the stated relation for each named kinetic-theory quantity, demonstrated by the stem asking only to 'Match Column-I and Column-II' where Column-I holds four named quantities and Column-II four printed relations.
- **Note:** Two List-II entries are damaged in our record and should be repaired: P reads $\frac{1}{3}nmv^{-2}$ where the relation needs $\frac{1}{3}nm\overline{v^{2}}$ (an overbar rendered as an exponent), and Q reads $\sqrt{\frac{3MT}{M}}$ where it needs $\sqrt{\frac{3RT}{M}}$ (an $R$ transcribed as $M$). Read literally, Q reduces to $\sqrt{3T}$ and P is not a pressure, so the key pairing A-Q can only be confirmed on the repaired reading. I have tagged the question as printed on that repaired reading, which is uniquely recoverable because each entry is still the only one of its structural kind, and I have not re-judged the key: option 1 is correct for the intended expressions. A reviewer holding the printed paper should confirm both glyphs before this trap is published.
<!--/ecat-->

## Q28

Physics · Modern Physics

A nucleus with mass number 240 breaks into two fragments each of mass number 120, the binding energy per nucleon of unfragmented nuclei is $7.6\,\mathrm{MeV}$ while that of fragments is $8.5\,\mathrm{MeV}$. The total gain in the Binding Energy in the process is :

- (1) $804\,\mathrm{MeV}$
- **(2)** $216\,\mathrm{MeV}$
- (3) $0.9\,\mathrm{MeV}$
- (4) $9.4\,\mathrm{MeV}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $(240)(7.6\,Mev) + \Delta Q = (120)(8.5\,Mev) + (120)(8.5\,Mev)$
2. $T \cdot BE_{i} + gain$
3. $\Rightarrow \Delta Q = 240(8.5 - 7.6)\,Mev$
4. $= 216\,Mev$

**Solved independently** (answer withheld)

1. Initial binding energy: $BE_i = 240 \times 7.6\,\mathrm{MeV} = 1824\,\mathrm{MeV}$.
2. Final binding energy of the two fragments: $BE_f = 2 \times 120 \times 8.5\,\mathrm{MeV} = 2040\,\mathrm{MeV}$.
3. Gain: $\Delta BE = BE_f - BE_i = 2040 - 1824 = 216\,\mathrm{MeV}$, which is option $2$.

**Subtopic:** Mass Defect and Nuclear Binding Energy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q028_84d4e244_30102026.png?v=84d4e244dacc)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q028_a6ebd014_30102026.png?v=a6ebd01473be)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Total binding energy is the binding energy per nucleon times the nucleon count, so the gain in fission is the fragments' total minus the parent's total
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $8.5-7.6=0.9$ MeV is the gain per nucleon, a true quantity the stem's two numbers give in one subtraction, while the stem asks for the total over all 240 nucleons
- **Why:** This question requires per-nucleon binding energies converted to totals before being differenced, demonstrated by "The total gain in the Binding Energy in the process is" with mass numbers 240 and 120 supplied.
<!--/ecat-->

## Q29

Physics · Capacitance

A parallel plate capacitor has a uniform electric field '$\vec{E}$' in the space between the plates. If the distance between the plates is ‘d’ and the area of each plate is ‘A’ the energy stored in the capacitor is: ($\varepsilon_0$ = permittivity of free space)

- **(1)** $\frac{1}{2}\varepsilon_0 E^2 Ad$
- (2) $\frac{E^2 Ad}{\varepsilon_0}$
- (3) $\frac{1}{2}\varepsilon_0 E^2$
- (4) $\varepsilon_0 EAd$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $E = \frac{1}{2}CV^{2} = \frac{1}{2}\frac{(\varepsilon_0 A)}{d}\left(E^{2}d^{2}\right)$
2. $= \frac{1}{2}\varepsilon_0\left(Ad\right)E^{2}$

**Solved independently** (answer withheld)

1. The energy density in an electric field is $u = \frac{1}{2}\varepsilon_0 E^2$.
2. The uniform field fills the volume between the plates, $V = Ad$.
3. $U = uV = \frac{1}{2}\varepsilon_0 E^2 Ad$, which is option $1$.

**Subtopic:** Energy Stored in a Capacitor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q029_e6c31fcb_30102026.png?v=e6c31fcbfcf3)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q029_cb874f80_30102026.png?v=cb874f80234b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Field energy is the energy density $\frac{1}{2}\varepsilon_0E^2$ multiplied by the volume between the plates, $Ad$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\frac{1}{2}\varepsilon_0E^2$ is the energy density, the quantity the chapter prints in exactly this form, and the stem asks for the energy stored, which needs it multiplied by the volume $Ad$
- **Why:** This question requires the field energy density multiplied by the volume it occupies, demonstrated by "the distance between the plates is 'd' and the area of each plate is 'A'" being supplied with the field itself.
<!--/ecat-->

## Q30

Physics · Ray Optics

Find the value of angle of emergence from the prism. Refractive index of the glass is $\sqrt{3}$.

![printed figure: Right-angled prism with 60 degree base angle and a ray incident normally on the slant face](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q030_cfbef795_30102026.png?v=cfbef795e75c)

*Right-angled prism with 60 degree base angle and a ray incident normally on the slant face*

![drawn: Right-angled prism with 60 degree base angle and a ray incident normally on the slant face](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q030_question_e79784b7_02112026.svg?v=e79784b7dfe9)  
*drawn by code/lib/physics_figure.py*

- (1) $45^{\circ}$
- (2) $90^{\circ}$
- **(3)** $60^{\circ}$
- (4) $30^{\circ}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Ray normal to the hypotenuse of a 30-60-90 prism, refracted out of the vertical face](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q030_sol_1_4f776c47_30102026.png?v=4f776c47d289)

*Ray normal to the hypotenuse of a 30-60-90 prism, refracted out of the vertical face*

![drawn: Ray normal to the hypotenuse of a 30-60-90 prism, refracted out of the vertical face](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q030_solution_1_f846dc7c_02112026.svg?v=f846dc7c451d)  
*drawn by code/lib/physics_figure.py*

1. $(\sin\theta) = \sqrt{3}\sin 30^{\circ}$
2. $\sin\theta = \frac{\sqrt{3}}{2}$
3. $\theta = 60^{\circ}$

**Solved independently** (answer withheld)

1. The ray falls normally on the hypotenuse face, so $i_1 = 0$ and $r_1 = 0$: it enters undeviated.
2. The triangle has angles $90^{\circ}$ and $60^{\circ}$, so the angle between the hypotenuse and the vertical face is $A = 180^{\circ} - 90^{\circ} - 60^{\circ} = 30^{\circ}$.
3. The ray travels to the vertical face, where $r_2 = A - r_1 = 30^{\circ}$.
4. Critical angle: $\sin C = \frac{1}{\sqrt{3}} \approx 0.577$, so $C \approx 35.3^{\circ} > 30^{\circ}$ and the ray is not totally reflected.
5. Snell's law at the exit face: $\sin e = \mu \sin r_2 = \sqrt{3} \times \sin 30^{\circ} = \frac{\sqrt{3}}{2}$.
6. $e = 60^{\circ}$, which is option $3$.

**Subtopic:** Prism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q030_5d460fdc_30102026.png?v=5d460fdc808b)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q030_1a5a8c2c_30102026.png?v=1a5a8c2ceedf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ray entering a face at normal incidence is not bent there, so the prism geometry fixes its angle of incidence on the second face and Snell's law gives the emergence angle
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $30^{\circ}$ is the angle the ray really makes with the normal of the second face, carried straight out as the emergence angle because the ray entered the first face without bending
- **Why:** This question requires Snell's law applied at the second face after the geometry fixes the internal angle, demonstrated by "Refractive index of the glass is $\sqrt{3}$" with the figure's $60^{\circ}$ vertex and the ray drawn perpendicular to the slant face.
- **Note:** The figure arrived as a drawn spec, so the geometry could be read: a right angle at the top-left vertex, $60^{\circ}$ at the top-right, hence $30^{\circ}$ at the bottom, and a ray marked perpendicular to the slant face. That reading gives an internal angle of $30^{\circ}$ at the vertical face and $e=60^{\circ}$, which matches the printed key.
<!--/ecat-->

## Q31

Physics · Electrostatics

A dipole is placed in an electric filed as shown. In which direction will it move?

![printed figure: A dipole +q -q on the central line of three diverging electric field lines E](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q031_a09c0dc1_30102026.png?v=a09c0dc1ede2)

*A dipole +q -q on the central line of three diverging electric field lines E*

![drawn: A dipole +q -q on the central line of three diverging electric field lines E](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q031_question_e664cd2b_02112026.svg?v=e664cd2b6336)  
*drawn by code/lib/physics_figure.py*

- (1) Towards the left as its potential energy will decrease
- (2) Towards the right as its potential energy will increase
- (3) Towards the left as its potential energy will increase
- **(4)** Towards the right as its potential energy will decrease

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Towards the right as its potential energy decreases.

**Solved independently** (answer withheld)

1. The field lines spread out to the right, so $|\vec E|$ decreases with $x$: $E_{left} > E_{right}$.
2. $+q$ is on the left and $-q$ on the right, so $\vec p$ (from $-q$ to $+q$) points left, antiparallel to $\vec E$.
3. Force on $+q$: $qE_{left}$ to the right; force on $-q$: $qE_{right}$ to the left.
4. $F_{net} = q(E_{left} - E_{right}) > 0$, i.e. towards the right.
5. $U = -\vec p\cdot\vec E = -pE\cos 180^\circ = +pE$.
6. Moving right, $E$ decreases, so $U = pE$ decreases, consistent with motion under the net force; option $4$.

**Subtopic:** Force on a Dipole in a Non-Uniform Electric Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 14)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q031_1c76a253_30102026.png?v=1c76a2530190)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q031_271dfb7c_30102026.png?v=271dfb7c284b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A dipole in a non-uniform field feels a net force toward lower potential energy, and with $\vec p$ antiparallel to $\vec E$ that is away from the stronger field
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The rule that a dipole is drawn toward the stronger field holds only when $\vec p$ points along $\vec E$, and the figure prints $+q$ on the side nearer the source, which makes $\vec p$ antiparallel and reverses the force
- **Why:** This question requires the dipole-in-a-non-uniform-field rule applied to the printed orientation, demonstrated by "In which direction will it move?" with the figure showing $+q$ nearer the diverging source and each option pairing a direction with an energy change.
- **Note:** The figure arrived as a drawn spec and was read as follows: three dashed field lines diverging from a point at the left, so $E$ points right and weakens rightward, with the dipole on the middle line carrying $+q$ at the left end. Both routes agree on the answer — the net force $q[E(+q)-E(-q)]$ is rightward, and $U=+pE$ falls rightward.
<!--/ecat-->

## Q32

Physics · Semiconductor Electronics

> ⚠ The booklet prints answer (3), but its own printed solution works out to (1). The printed answer is kept as printed; treat the key as unconfirmed for this question.

> ⚠ The independent solve chose (1); the booklet prints (3).

Consider the following Statements (A) and (B) and identify the correct answer.

- (A) A zener diode is connected in reverse bias, when used as a voltage regulator.
- (B) The potential barrier of p - n junction lies between $0.1\,\mathrm{V}$ to $0.3\,\mathrm{V}$.

- (1) (A) is correct (B) is incorrect.
- (2) (A) is incorrect but (B) is correct.
- **(3)** (A) and (B) both are correct.
- (4) (A) and (B) both are incorrect.

**Answer** — booklet: (3) · independent solve: (1) · publisher_contradicts_itself

**Publisher's solution**

1. Zener diode is connected in reverse bias, when used as a voltage regulator.
2. The potential barrier of p - n junction can be more than the given range.

**Solved independently** (answer withheld)

1. As a voltage regulator a zener diode works in reverse breakdown, where $V_Z$ stays nearly constant, so it is reverse biased and (A) is correct.
2. The barrier potential of a p-n junction is about $0.7\,\mathrm{V}$ for Si and about $0.2$ to $0.3\,\mathrm{V}$ for Ge, so a general range of $0.1\,\mathrm{V}$ to $0.3\,\mathrm{V}$ is not correct and (B) is incorrect.
3. (A) correct and (B) incorrect matches option $1$.

**Subtopic:** Zener Diode, PN Junction Diode or Semiconductor Diode · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q032_82d4aab6_30102026.png?v=82d4aab640eb)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q032_8c5130dc_30102026.png?v=8c5130dca455)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A zener regulator is run in reverse bias at its breakdown voltage, and the barrier potential of a p-n junction is a few tenths of a volt
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Statement A is securely known, so the verdict turns on the number in B, and the barrier potential is printed as a pair of values — the $0.7\,\mathrm{V}$ for silicon sits beside the $0.3\,\mathrm{V}$ for germanium, so recalling the silicon figure puts B outside the stated range and marks it incorrect
- **Why:** This question requires two printed statements graded separately against stated facts, demonstrated by "Consider the following Statements (A) and (B) and identify the correct answer" with options that are the four truth combinations.
- **Note:** E1_question_type arrived as plain_mcq from the pattern default, but the record carries a labelled statement block (A) and (B) and the options are truth verdicts, so the shape recorded here is statements. Separately, statement B's band "$0.1\,\mathrm{V}$ to $0.3\,\mathrm{V}$" is graded correct by the printed key while the silicon value usually quoted is $0.7\,\mathrm{V}$; the tag follows the key, and a reviewer may want to check which edition's wording the examiner used.
<!--/ecat-->

## Q33

Physics · Modern Physics

A half-life of a radioactive nuclide is $100$ hours. The fraction of original activity that will remain after $150$ hours would be:

- (1) $\frac{2}{3}$
- (2) $\frac{2}{3\sqrt{2}}$
- (3) $\frac{1}{2}$
- **(4)** $\frac{1}{2\sqrt{2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $N = N_0\left(\frac{1}{2}\right)^{n}$
2. $= N_0\left(\frac{1}{2}\right)^{\frac{150}{100}}$
3. $= N_0\left(\frac{1}{2}\right)^{3/2}$
4. $\frac{N}{N_0} = \frac{1}{2\sqrt{2}}$

**Solved independently** (answer withheld)

1. Number of half-lives: $n = \frac{t}{T_{1/2}} = \frac{150}{100} = 1.5$.
2. Activity decays as $\frac{A}{A_0} = \left(\frac{1}{2}\right)^{n}$.
3. $\left(\frac{1}{2}\right)^{3/2} = \frac{1}{2} \cdot \frac{1}{\sqrt{2}} = \frac{1}{2\sqrt{2}}$, which is option $4$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q033_c93d25b5_30102026.png?v=c93d25b5af53)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q033_04ddfc64_30102026.png?v=04ddfc64e993)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Activity falls by a factor $\left(\frac{1}{2}\right)^{t/T_{1/2}}$, and the exponent need not be a whole number
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\frac{1}{2}$ is the fraction left after one half-life, and 150 hours contains one completed half-life, so the halving is counted once and the remaining 50 hours is left out of the exponent
- **Why:** This question requires the decay law used with a fractional number of half-lives, demonstrated by a half-life of $100$ hours set against $150$ hours and by options carrying a $\sqrt2$.
<!--/ecat-->

## Q34

Physics · Alternating Current

An inductor of inductance $L$, a capacitor of capacitance $C$ and a resistor of resistance ‘$R$’ are connected in series to an ac source of potential difference ‘$V$’ volts as shown in figures. Potential difference across $L$, $C$ and $R$ is $40\,\mathrm{V}$, $10\,\mathrm{V}$ and $40\,\mathrm{V}$, respectively. The amplitude of current flowing through LCR series circuit is $10\sqrt{2}$. The impedance of the circuit is :

![printed figure: Series LCR circuit across an ac source V, with the voltages 40 V, 10 V, 40 V marked across L, C and R](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q034_07062596_30102026.png?v=0706259659eb)

*Series LCR circuit across an ac source V, with the voltages 40 V, 10 V, 40 V marked across L, C and R*

![drawn: Series LCR circuit across an ac source V, with the voltages 40 V, 10 V, 40 V marked across L, C and R](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q034_question_c63c1ef4_02112026.svg?v=c63c1ef43b9e)  
*drawn by code/lib/physics_figure.py*

- (1) $4\,\Omega$
- **(2)** $5\,\Omega$
- (3) $4\sqrt{2}\,\Omega$
- (4) $\frac{5}{\sqrt{2}}\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $V_{rms} = \sqrt{30^{2} + 40^{2}} = 50$
2. $I_{rms} = \frac{10\sqrt{2}}{\sqrt{2}} = 10$
3. $Z = \frac{50}{10} = 5\,\Omega$

**Solved independently** (answer withheld)

1. Source voltage: $V = \sqrt{V_R^2 + (V_L - V_C)^2}$.
2. $V = \sqrt{40^2 + (40-10)^2} = \sqrt{1600 + 900} = 50\,\mathrm{V}$ (rms, as meter-type readings).
3. $I_{rms} = \frac{I_0}{\sqrt{2}} = \frac{10\sqrt{2}}{\sqrt{2}} = 10\,\mathrm{A}$.
4. $Z = \frac{V_{rms}}{I_{rms}} = \frac{50}{10} = 5\,\Omega$, which is option $2$.

**Subtopic:** Impedance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q034_9690a95e_30102026.png?v=9690a95eca3d)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q034_8ef8b1e3_30102026.png?v=8ef8b1e34ccc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a series LCR circuit the element voltages add as phasors, and impedance is that resultant voltage divided by the rms current
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The phasor sum $\sqrt{(40-10)^2+40^2}=50$ V is an rms voltage, and dividing it by the printed amplitude $10\sqrt{2}$ A gives $\frac{5}{\sqrt{2}}\,\Omega$ because the $\sqrt{2}$ that turns amplitude into rms is never used.
- **Why:** This question requires computing impedance from the phasor sum of the printed element voltages and the rms current, demonstrated by 'Potential difference across L, C and R is 40 V, 10 V and 40 V, respectively' together with 'The amplitude of current flowing through LCR series circuit is $10\sqrt{2}$'.
- **Note:** E1_question_type reads multi_part_respectively, but 'respectively' here only labels the three supplied voltages; the answer is one impedance, so the printed shape is a plain four-option mcq. The figure repeats the stem's three voltages and decides nothing on its own.
<!--/ecat-->

## Q35

Physics · Oscillations

A body is executing simple harmonic motion with frequency ‘$n$’, the frequency of its potential energy is:

- (1) $3n$
- (2) $4n$
- (3) $n$
- **(4)** $2n$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $2n$

**Solved independently** (answer withheld)

1. Displacement in SHM: $x = A\sin(\omega t)$ with $\omega = 2\pi n$.
2. Potential energy: $U = \frac{1}{2}kx^2 = \frac{1}{2}kA^2\sin^2(\omega t)$.
3. Using $\sin^2\theta = \frac{1 - \cos 2\theta}{2}$: $U = \frac{1}{4}kA^2\left(1 - \cos 2\omega t\right)$.
4. $U$ varies with angular frequency $2\omega$, so its frequency is $2n$, which is option $4$.

**Subtopic:** Energy Conservation in SHM · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q035_6677ed64_30102026.png?v=6677ed645ded)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q035_27b28f27_30102026.png?v=27b28f27bbd2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Potential energy of a harmonic oscillator goes as the square of the displacement, and squaring a sine doubles its frequency
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Treating the energy as following the displacement itself carries the frequency straight across as $n$, but $PE=\frac{1}{2}kA^{2}\sin^{2}\omega t$ depends on $x^{2}$, which repeats twice per period.
- **Why:** This question requires the factor linking the potential energy's frequency to the frequency of the motion, demonstrated by 'executing simple harmonic motion with frequency n' set against 'the frequency of its potential energy'.
<!--/ecat-->

## Q36

Physics · Rotational Motion

From a circular ring of mass ‘$M$’ and radius ‘$R$’ an arc corresponding to a $90^{\circ}$ sector is removed. The moment of inertia of the remaining part of the ring about an axis passing through the centre of the ring and perpendicular to the plane of the ring is ‘$K$’ times ‘$MR^{2}$’. Then the value of ‘$K$’ is :

- (1) $\frac{1}{4}$
- (2) $\frac{1}{8}$
- **(3)** $\frac{3}{4}$
- (4) $\frac{7}{8}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Ring in perspective with a vertical axis through its centre; a 90 degree sector (quarter) hatched as the removed part](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q036_sol_1_06a6a29f_30102026.png?v=06a6a29ffa65)

*Ring in perspective with a vertical axis through its centre; a 90 degree sector (quarter) hatched as the removed part*

![drawn: Ring in perspective with a vertical axis through its centre; a 90 degree sector (quarter) hatched as the removed part](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_drawn/q036_solution_1_ee0a6cd8_30102026.svg?v=ee0a6cd85cfc)  
*drawn by code/lib/physics_figure.py*

1. $I = \frac{3M}{4}R^{2}$
2. $= KMR^{2}$
3. $K = \frac{3}{[unreadable notation]}$

**Solved independently** (answer withheld)

1. A $90^{\circ}$ arc is $\frac{1}{4}$ of the ring, so its mass is $\frac{M}{4}$.
2. Remaining mass $= M - \frac{M}{4} = \frac{3M}{4}$.
3. Every element of the remaining arc is at distance $R$ from the axis, so $I = \frac{3M}{4}R^{2}$.
4. $K = \frac{3}{4}$, which is option $3$.

**Subtopic:** Moment of Inertia of a Circular Shape · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q036_595666de_30102026.png?v=595666de9f9d)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q036_ee0a1aff_30102026.png?v=ee0a1aff7e72)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Every element of a ring lies at distance R from the central axis, so the moment of inertia about that axis is simply the mass that remains times $R^{2}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $\frac{1}{4}MR^{2}$ is the moment of inertia of the arc that was cut away, so a student who prices the removed $90^{\circ}$ sector and stops has a true value for the wrong piece of the ring.
- **Why:** This question requires producing the numerical factor $K$ from the mass left after the cut, demonstrated by 'The moment of inertia of the remaining part of the ring ... is K times MR^2'.
<!--/ecat-->

## Q37

Physics · Alternating Current

A series LCR circuit containing $5.0\,\mathrm{H}$ inductor, $80\,\mu\mathrm{F}$ capacitor and $40\,\Omega$ resistor is connected to $230\,\mathrm{V}$ variable frequency ac source. The angular frequencies of the source at which power transferred to the circuit is half the power at the resonant angular frequency are likely to be:

- **(1)** $46\,\mathrm{rad/s}$ and $54\,\mathrm{rad/s}$
- (2) $42\,\mathrm{rad/s}$ and $58\,\mathrm{rad/s}$
- (3) $25\,\mathrm{rad/s}$ and $75\,\mathrm{rad/s}$
- (4) $50\,\mathrm{rad/s}$ and $25\,\mathrm{rad/s}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Band width at half power frequency
2. $\Delta\omega = \frac{R}{L}$
3. $= \frac{40}{5} = 8\,rad/s$

**Solved independently** (answer withheld)

1. Resonant angular frequency: $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{5.0 \times 80\times10^{-6}}}$.
2. $\sqrt{4\times10^{-4}} = 2\times10^{-2}$, so $\omega_0 = 50\,\mathrm{rad/s}$.
3. Half-power points satisfy $|X_L - X_C| = R$, giving bandwidth $\Delta\omega = \omega_2 - \omega_1 = \frac{R}{L}$.
4. $\Delta\omega = \frac{40}{5.0} = 8\,\mathrm{rad/s}$.
5. $\omega_{1,2} \approx \omega_0 \mp \frac{\Delta\omega}{2} = 50 \mp 4 = 46\,\mathrm{rad/s}$ and $54\,\mathrm{rad/s}$, which is option $1$.

**Subtopic:** Sharpness of Resonance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q037_7e19667b_30102026.png?v=7e19667b2d16)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q037_5d746133_30102026.png?v=5d7461339909)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The half-power frequencies sit one half-bandwidth either side of resonance: $\omega_0=1/\sqrt{LC}$ and the offset is $R/2L$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  $R/L=40/5=8$ rad/s is the full width between the half-power points, and carrying it as the offset on each side of resonance puts them at $50\pm 8$, i.e. 42 and 58 rad/s.
- **Why:** This question requires computing the resonant frequency and then the half-power offset from the printed constants, demonstrated by 'the angular frequencies of the source at which power transferred to the circuit is half the power at the resonant angular frequency'.
- **Note:** Checked for old_ncert_answer: the stem's 5.0 H, 80 microfarad, 40 ohm and 230 V are the standard worked resonance set and no value in them has been altered here, so no NCERT answer is sitting in the options as a changed-number distractor; the label needs both numbers named and there is only one.
<!--/ecat-->

## Q38

Physics · Magnetic Effect of Electric Current

A uniform conducting wire of length $12a$ and resistance ‘$R$’ is wound up as a current carrying coil in the shape of. (i) an equilateral triangle of side ‘$a$’. (ii) a square of side ‘$a$’. The magnetic dipole moments of the coil in each case respectively are:

- (i) an equilateral triangle of side ‘$a$’.
- (ii) a square of side ‘$a$’.

- (1) $3\,Ia^{2}$ and $4\,Ia^{2}$
- (2) $4\,Ia^{2}$ and $3\,Ia^{2}$
- **(3)** $\sqrt{3}\,Ia^{2}$ and $3\,Ia^{2}$
- (4) $3\,Ia^{2}$ and $I\,a^{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For triangle
2. $M = NiA$
3. $= 4 \times I\frac{\sqrt{3}}{4}a^{2}$
4. $= \sqrt{3}Ia^{2}$
5. For square $M = 3Ia^{2}$

**Solved independently** (answer withheld)

1. Triangle perimeter is $3a$, so the number of turns is $N_1 = \frac{12a}{3a} = 4$.
2. Area of one triangular turn: $A_1 = \frac{\sqrt{3}}{4}a^2$.
3. $m_1 = N_1 I A_1 = 4 \times I \times \frac{\sqrt{3}}{4}a^2 = \sqrt{3}\,Ia^2$.
4. Square perimeter is $4a$, so $N_2 = \frac{12a}{4a} = 3$.
5. Area of one square turn: $A_2 = a^2$.
6. $m_2 = N_2 I A_2 = 3\,Ia^2$, so the pair is $\sqrt{3}\,Ia^2$ and $3\,Ia^2$, which is option $3$.

**Subtopic:** Current Carrying Loop as a Magnetic Dipole · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q038_d3f1bf85_30102026.png?v=d3f1bf85cc41)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q038_b18e231f_30102026.png?v=b18e231fb0cf)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A fixed length of wire gives $n=\frac{\text{total length}}{\text{perimeter}}$ turns, and the dipole moment $nIA$ then depends on the shape through its area
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The turn counts are worked out correctly, 4 for the triangle and 3 for the square, and the area of both shapes is then taken as $a^2$, which leaves the square's $3Ia^2$ exactly right and the triangle's as $4Ia^2$
- **Why:** This question requires a turn count from a fixed wire length and then the shape's own area, demonstrated by "A uniform conducting wire of length $12a$" wound as a triangle and a square "respectively".
- **Note:** This question sits in the statements group because the export's format field recorded its (i) and (ii) cases in the statements array, but they are the two shapes to be computed, not statements to be judged; the shape recorded here is two_part, matching the pattern's own multi_part_respectively. The resistance $R$ in the stem is never used by the answer.
<!--/ecat-->

## Q39

Physics · Alternating Current

A step down transformer connected to an ac mains supply of $220\,\mathrm{V}$ is made to operate at $11\,\mathrm{V}$, $44\,\mathrm{W}$ lamp. Ignoring power losses in the transformer, what is the current in the primary circuit?

- (1) $2\,\mathrm{A}$
- (2) $4\,\mathrm{A}$
- **(3)** $0.2\,\mathrm{A}$
- (4) $0.4\,\mathrm{A}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\left(V_i\right)_{\text{Primary}} = \left(V_i\right)_{\text{Secondary}}$
2. $220i = 44$
3. $i = \frac{44}{220} = \frac{2}{10} = 0.2\,A$

**Solved independently** (answer withheld)

1. Ignoring losses, power drawn by the primary equals the lamp power: $P_p = P_s = 44\,\mathrm{W}$.
2. $I_p = \frac{P_p}{V_p} = \frac{44\,\mathrm{W}}{220\,\mathrm{V}}$.
3. $I_p = 0.2\,\mathrm{A}$, which is option $3$.

**Subtopic:** Transformer · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q039_24e7e802_30102026.png?v=24e7e802a93f)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q039_40f806b1_30102026.png?v=40f806b1bd79)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An ideal transformer passes the same power on both sides, so the primary current is the lamp's power divided by the mains voltage
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $44/11=4$ A is the lamp's own current, a true value the two secondary numbers hand over directly, but the stem asks for the current in the primary where the same 44 W is drawn at 220 V.
- **Why:** This question requires computing the primary current from power conservation across the transformer, demonstrated by 'Ignoring power losses in the transformer, what is the current in the primary circuit?' with the lamp given as '11 V, 44 W'.
<!--/ecat-->

## Q40

Physics · Electrostatics

Twenty seven drops of same size are charged at $220\,\mathrm{V}$ each. They combine to form a bigger drop. Calculate the potential of the bigger drop.

- (1) $1520\,\mathrm{V}$
- **(2)** $1980\,\mathrm{V}$
- (3) $660\,\mathrm{V}$
- (4) $1320\,\mathrm{V}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For bigger
2. $V = \frac{K27q}{R}$
3. $= \frac{K27q}{3r}$
4. $= 9\frac{Kq}{r}$
5. $= 9 \times 220$
6. $= 1980$

**Solved independently** (answer withheld)

1. Volume is conserved: $27 \cdot \frac{4}{3}\pi r^3 = \frac{4}{3}\pi R^3$, so $R = 3r$.
2. Charge is conserved: $Q = 27q$.
3. $V' = \frac{kQ}{R} = \frac{27kq}{3r} = 9\frac{kq}{r} = 9V$.
4. $V' = 9 \times 220\,\mathrm{V} = 1980\,\mathrm{V}$, which is option $2$.

**Subtopic:** Combination of Charged Drops · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q040_ef0ec060_30102026.png?v=ef0ec0606205)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q040_31dd78aa_30102026.png?v=31dd78aa4b63)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Merging n identical drops multiplies the charge by n and the radius by $n^{1/3}$, so the potential rises by $n^{2/3}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The merged drop's radius is $3r$, and scaling 220 V by that factor alone gives 660 V — it applies $V\propto R$ and never multiplies the charge by 27.
- **Why:** This question requires computing the merged drop's potential from how charge and radius each scale, demonstrated by 'Twenty seven drops of same size are charged at 220 V each. They combine to form a bigger drop.'
<!--/ecat-->

## Q41

Physics · Electromagnetic Induction

Two conducting circular loops of radii $R_1$ and $R_2$ are placed in the same plane with their centres coinciding. If $R_1 >> R_2$, the mutual inductance $M$ between them will be directly proportional to:

- (1) $\frac{R_1^2}{R_2}$
- **(2)** $\frac{R_2^2}{R_1}$
- (3) $\frac{R_1}{R_2}$
- (4) $\frac{R_2}{R_1}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Two concentric coplanar loops of radii R1 and R2, current I1 in the outer loop](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q041_sol_1_0af31dae_30102026.png?v=0af31daea23a)

*Two concentric coplanar loops of radii R1 and R2, current I1 in the outer loop*

![drawn: Two concentric coplanar loops of radii R1 and R2, current I1 in the outer loop](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q041_solution_1_2ab5b5cd_02112026.svg?v=2ab5b5cdfacd)  
*drawn by code/lib/physics_figure.py*

1. $B_1 = \frac{\mu_0 I_1}{2R_1}$
2. $\phi_2 = B_1\left(\pi R_2^2\right) = \frac{\mu_0 \pi R_2^2}{2R_1} I_1$
3. $\phi_2 = MI_1 \Rightarrow M = \frac{\mu_0 \pi R_2^2}{2R_1}$
4. $M \propto \frac{R_2^2}{R_1}$

**Solved independently** (answer withheld)

1. Pass current $I$ in the larger loop; its field at the centre is $B_1 = \frac{\mu_0 I}{2R_1}$.
2. Since $R_1 \gg R_2$, $B_1$ is nearly uniform over the small loop.
3. Flux through the small loop: $\phi_2 = B_1 \pi R_2^2 = \frac{\mu_0 \pi R_2^2 I}{2R_1}$.
4. $M = \frac{\phi_2}{I} = \frac{\mu_0 \pi R_2^2}{2R_1}$.
5. Hence $M \propto \frac{R_2^2}{R_1}$, which is option $2$.

**Subtopic:** Mutual Induction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q041_1a81e307_30102026.png?v=1a81e3072262)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q041_46bbe4ad_30102026.png?v=46bbe4ad1908)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Mutual inductance of a large coplanar loop and a tiny concentric one: the large loop's field at the centre times the small loop's area
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Putting the current in the SMALL loop and catching its field over the big loop's area gives $\frac{\mu_0 I}{2R_2}\pi R_1^{2}$, which is the correct expression with the two radii interchanged.
- **Why:** This question requires deriving the proportionality from the large loop's field and the small loop's area, demonstrated by 'If $R_1 >> R_2$, the mutual inductance M between them will be directly proportional to'.
<!--/ecat-->

## Q42

Physics · Gravitation

A particle of mass ‘m’ is projected with a velocity $u = kV_e$ $(k < 1)$ from the surface of the earth. ($V_e$ = escape velocity) The maximum height above the surface reached by the particle is:

- (1) $\dfrac{R^2 k}{1+k}$
- **(2)** $\dfrac{Rk^2}{1-k^2}$
- (3) $R\left(\dfrac{k}{1-k}\right)^2$
- (4) $R\left(\dfrac{k}{1+k}\right)^2$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Particle projected upward with speed KVe from the earth's surface of radius R](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q042_sol_1_134b7a63_30102026.png?v=134b7a63d31b)

*Particle projected upward with speed KVe from the earth's surface of radius R*

![drawn: Particle projected upward with speed KVe from the earth's surface of radius R](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q042_solution_1_c0619aa3_02112026.svg?v=c0619aa38281)  
*drawn by code/lib/physics_figure.py*

1. $V_e = \sqrt{\frac{2GM}{R}}$
2. $\frac{1}{2}m\left(kV_e\right)^2 + \left(-\frac{GMm}{R}\right) = 0 - \left(\frac{GMm}{R+H}\right)$
3. $\frac{1}{2}mk^2\frac{2GM}{R} - \frac{GMm}{R} = -\frac{GMm}{R+H}$
4. $K^2 - 1 = -\frac{R}{R+H} \Rightarrow R + H = -\frac{R}{K^2 - 1}$
5. $H = \frac{R}{1-K^2} - R = R\left(\frac{K^2}{1-K^2}\right)$

**Solved independently** (answer withheld)

1. Escape velocity: $V_e^2 = \frac{2GM}{R}$, so $u^2 = k^2 \frac{2GM}{R}$.
2. Energy conservation between surface and maximum height: $\frac{1}{2}m u^2 - \frac{GMm}{R} = -\frac{GMm}{R+h}$.
3. Substitute $u^2$: $\frac{k^2 GM}{R} - \frac{GM}{R} = -\frac{GM}{R+h}$, so $\frac{1-k^2}{R} = \frac{1}{R+h}$.
4. $R + h = \frac{R}{1-k^2}$.
5. $h = \frac{R}{1-k^2} - R = \frac{Rk^2}{1-k^2}$, which is option $2$.

**Subtopic:** Escape Velocity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q042_73da8470_30102026.png?v=73da84707e38)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q042_2153d413_30102026.png?v=2153d413279f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Energy conservation with the full $-GMm/r$ potential fixes the rise height when the launch speed is given as a fraction of escape speed
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The energy balance gives $h=\frac{Rk^{2}}{1-k^{2}}$, and factorising $1-k^{2}$ as $(1-k)^{2}$ turns that into $R\left(\frac{k}{1-k}\right)^{2}$.
- **Why:** This question requires deriving the height expression from the energy equation written with the full gravitational potential, demonstrated by 'projected with a velocity $u = kV_e$ $(k < 1)$ from the surface of the earth' and 'The maximum height above the surface reached by the particle is'.
<!--/ecat-->

## Q43

Physics · Rotational Motion

A uniform rod of length $200\,\mathrm{cm}$ and mass $500\,\mathrm{g}$ is balanced on a wedge placed at $40\,\mathrm{cm}$ mark. A mass of $2\,\mathrm{kg}$ is suspended from the rod at $20\,\mathrm{cm}$ and another unknown mass ‘$m$’ is suspended from the rod at $160\,\mathrm{cm}$ mark as shown in the figure. Find the value of ‘$m$’ such that the rod is in equilibrium. ($g = 10\,\mathrm{m/s^2}$)

![printed figure: A uniform rod on a wedge at the 40 cm mark, with 2 kg hung at 20 cm and m hung at 160 cm](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q043_a6067604_30102026.png?v=a60676046943)

*A uniform rod on a wedge at the 40 cm mark, with 2 kg hung at 20 cm and m hung at 160 cm*

![drawn: A uniform rod on a wedge at the 40 cm mark, with 2 kg hung at 20 cm and m hung at 160 cm](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q043_question_1f4bb123_02112026.svg?v=1f4bb1236e56)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{1}{6}\,\mathrm{kg}$
- **(2)** $\frac{1}{12}\,\mathrm{kg}$
- (3) $\frac{1}{2}\,\mathrm{kg}$
- (4) $\frac{1}{3}\,\mathrm{kg}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Rod with weights 2g, 0.5g at C and mg; separations 20, 60, 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q043_sol_1_dc9b415d_30102026.png?v=dc9b415d46da)

*Rod with weights 2g, 0.5g at C and mg; separations 20, 60, 60*

![drawn: Rod with weights 2g, 0.5g at C and mg; separations 20, 60, 60](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q043_solution_1_fd094285_02112026.svg?v=fd094285e1fb)  
*drawn by code/lib/physics_figure.py*

1. $2g(20) = (0.5)60 + mg(120)$
2. $4 = 3 + m12 \Rightarrow m = \frac{1}{12}\,kg$

**Solved independently** (answer withheld)

1. Take torques about the wedge at the $40\,\mathrm{cm}$ mark.
2. The $2\,\mathrm{kg}$ mass is $20\,\mathrm{cm}$ left of the pivot: $\tau_1 = 2g \times 20 = 40g$.
3. The rod's weight acts at its centre, $100\,\mathrm{cm}$, i.e. $60\,\mathrm{cm}$ right of the pivot: $\tau_2 = 0.5g \times 60 = 30g$.
4. The mass $m$ is $120\,\mathrm{cm}$ right of the pivot: $\tau_3 = mg \times 120$.
5. Equilibrium: $40g = 30g + 120mg$.
6. $m = \frac{10}{120} = \frac{1}{12}\,\mathrm{kg}$, which is option $2$.

**Subtopic:** Equilibrium of a Rigid Body · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q043_4f413ecf_30102026.png?v=4f413ecfe66b)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q043_aab24b3f_30102026.png?v=aab24b3f68c3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A rod balanced off its centre: torques about the wedge must include the rod's own weight acting at the 100 cm mark
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Balancing only the two hanging masses about the wedge gives $2\times 20=m\times 120$ and so $m=\frac{1}{3}$ kg; the rod's own 0.5 kg at the 100 cm mark contributes $0.5\times 60=30$ kg cm and never enters.
- **Why:** This question requires a torque balance about the wedge that includes the rod's weight, demonstrated by 'A uniform rod of length 200 cm and mass 500 g is balanced on a wedge placed at 40 cm mark'.
<!--/ecat-->

## Q44

Physics · Laws of Motion

A ball of mass $0.15\,\mathrm{kg}$ is dropped from a height $10\,\mathrm{m}$, strikes the ground and rebounds to the same height. The magnitude of impulse imparted to the ball is ($g = 10\,\mathrm{m/s^2}$) nearly:

- (1) $21\,\mathrm{kg\,m/s}$
- (2) $1.4\,\mathrm{kg\,m/s}$
- (3) $0\,\mathrm{kg\,m/s}$
- **(4)** $4.2\,\mathrm{kg\,m/s}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Ball dropped from 10 m falls with speed u = sqrt(2gh) and rebounds upward with speed u](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q044_sol_1_663658b5_30102026.png?v=663658b599ce)

*Ball dropped from 10 m falls with speed u = sqrt(2gh) and rebounds upward with speed u*

![drawn: Ball dropped from 10 m falls with speed u = sqrt(2gh) and rebounds upward with speed u](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q044_solution_1_016bb5ce_02112026.svg?v=016bb5ce81fa)  
*drawn by code/lib/physics_figure.py*

1. Impulse
2. $= 2mu = 2 \times 0.15 \times \sqrt{2gh}$
3. $= 0.3 \times 10 \times 1.41 = 4.23$

**Solved independently** (answer withheld)

1. Speed just before impact: $v = \sqrt{2gh} = \sqrt{2 \times 10 \times 10} = \sqrt{200} \approx 14.14\,\mathrm{m/s}$ (downward).
2. Rebounding to the same height means the speed just after impact is also $14.14\,\mathrm{m/s}$, now upward.
3. Impulse $= \Delta p = m v - (-m v) = 2 m v$.
4. $J = 2 \times 0.15 \times 14.14 \approx 4.24\,\mathrm{kg\,m/s}$, which is option $4$.

**Subtopic:** Impulse–Momentum Theorem · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q044_700d997f_30102026.png?v=700d997fb52a)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q044_60ef7ff8_30102026.png?v=60ef7ff8cb78)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Impulse is the change in momentum, and a bounce back to the same height reverses the velocity, so the two momenta add to $2mv$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  With the ball leaving as fast as it arrived, taking both momenta with the same sign makes the change $0.15\times 14.1-0.15\times 14.1=0$; the rebound velocity points the other way, so the two terms add instead, to $2mv=4.2$.
- **Why:** This question requires the change in momentum across a bounce that restores the height, demonstrated by 'strikes the ground and rebounds to the same height. The magnitude of impulse imparted to the ball is'.
<!--/ecat-->

## Q45

Physics · Kinematics

A particle moving in a circle of radius $R$ with a uniform speed takes a time $T$ to complete one revolution. I this particle were projected with the same speed at an angle '$\theta$' to the horizontal, the maximum height attained by it equals $4R$. The angle of projection, $\theta$, is then given by:

- (1) $\theta = \sin^{-1}\left(\dfrac{\pi^{2}R}{gT^{2}}\right)^{1/2}$
- **(2)** $\theta = \sin^{-1}\left(\dfrac{2gT^{2}}{\pi^{2}R}\right)^{1/2}$
- (3) $\theta = \cos^{-1}\left(\dfrac{gT^{2}}{\pi^{2}R}\right)^{1/2}$
- (4) $\theta = \cos^{-1}\left(\dfrac{\pi^{2}R}{gT^{2}}\right)^{1/2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Velocity v projected at angle theta above the horizontal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q045_sol_1_5abc17e9_30102026.png?v=5abc17e98404)

*Velocity v projected at angle theta above the horizontal*

![drawn: Velocity v projected at angle theta above the horizontal](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q045_solution_1_8583451c_02112026.svg?v=8583451c4cca)  
*drawn by code/lib/physics_figure.py*

1. $T = \frac{2\pi R}{v} \Rightarrow v = \frac{2\pi R}{T}$
2. $H = \frac{v^{2}\sin^{2}\theta}{2g}$
3. $H = R$
4. $4R = \left(\frac{2\pi R}{T}\right)^{2}\frac{\sin^{2}\theta}{2g}$
5. $\sqrt{\frac{2g}{R}\left(\frac{T}{\pi}\right)^{2}} = \sin\theta = \sqrt{\frac{2gT^{2}}{\pi^{2}R}}$

**Solved independently** (answer withheld)

1. Uniform circular motion: $v = \frac{2\pi R}{T}$, so $v^2 = \frac{4\pi^2 R^2}{T^2}$.
2. Maximum height of a projectile: $H = \frac{v^2 \sin^2\theta}{2g}$.
3. Set $H = 4R$: $\frac{v^2 \sin^2\theta}{2g} = 4R \Rightarrow \sin^2\theta = \frac{8gR}{v^2}$.
4. Substitute $v^2$: $\sin^2\theta = \frac{8gR\,T^2}{4\pi^2 R^2} = \frac{2gT^2}{\pi^2 R}$.
5. $\theta = \sin^{-1}\left(\frac{2gT^2}{\pi^2 R}\right)^{1/2}$, which is option $2$.

**Subtopic:** Maximum Height Reached · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q045_c2873f13_30102026.png?v=c2873f13b671)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q045_5499a2ef_30102026.png?v=5499a2ef5cc0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The circular motion fixes the speed as $v=2\pi R/T$, and the projectile's maximum height $v^{2}\sin^{2}\theta/2g$ then fixes the launch angle
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Isolating the sine upside down as $\sin^{2}\theta=\frac{v^{2}}{gH}$ and substituting $v=2\pi R/T$ with $H=4R$ gives exactly $\frac{\pi^{2}R}{gT^{2}}$.
- **Why:** This question requires chaining the circular speed into the projectile height formula and solving for the angle, demonstrated by 'takes a time T to complete one revolution' together with 'the maximum height attained by it equals 4R'.
- **Note:** The stem prints 'I this particle were projected', evidently 'If this particle were projected'. The missing letter does not change what is asked, so the question is tagged as printed.
<!--/ecat-->

## Q46

Physics · Semiconductor Electronics

For the given circuit, the input digital signals are applied at the terminals A, B and C. What would be the output at the terminal y?

![printed figure: Input waveforms A, B, C (0/5 V, instants t1 to t6) and the logic circuit: AND(A,B) and NAND(B,C) feed an OR gate with output y](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_46c25c2d_30102026.png?v=46c25c2dcf12)

*Input waveforms A, B, C (0/5 V, instants t1 to t6) and the logic circuit: AND(A,B) and NAND(B,C) feed an OR gate with output y*

![drawn: Input waveforms A, B, C (0/5 V, instants t1 to t6) and the logic circuit: AND(A,B) and NAND(B,C) feed an OR gate with output y](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q046_question_92adc2d5_02112026.svg?v=92adc2d56d63)  
*drawn by code/lib/physics_figure.py*

- (1) ![printed figure: Output y stays at 0 V with time marks t1 to t6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_option_1_a3579333_30102026.png?v=a3579333e4dd) *Output y stays at 0 V with time marks t1 to t6* ![drawn: Output y stays at 0 V with time marks t1 to t6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q046_option_1_836b85e5_02112026.svg?v=836b85e5796b)  
*drawn by code/lib/physics_figure.py*
- (2) ![printed figure: Output waveform: low, high pulse, low, then high (option 2)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_option_2_dbb6a5f9_30102026.png?v=dbb6a5f98805) *Output waveform: low, high pulse, low, then high (option 2)* ![drawn: Output waveform: low, high pulse, low, then high (option 2)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q046_option_2_54243d35_02112026.svg?v=54243d35bfc9)  
*drawn by code/lib/physics_figure.py*
- **(3)** ![printed figure: Output waveform: a constant level at 5 V](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_option_3_05834197_30102026.png?v=058341975110) *Output waveform: a constant level at 5 V* ![drawn: Output waveform: a constant level at 5 V](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q046_option_3_305735f0_02112026.svg?v=305735f09d4d)  
*drawn by code/lib/physics_figure.py*
- (4) ![printed figure: Output waveform of option (4): high, low, high, low between 5 V and 0 V](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_option_4_919a3a65_30102026.png?v=919a3a65c479) *Output waveform of option (4): high, low, high, low between 5 V and 0 V* ![drawn: Output waveform of option (4): high, low, high, low between 5 V and 0 V](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q046_option_4_8c4c5619_02112026.svg?v=8c4c56197f4f)  
*drawn by code/lib/physics_figure.py*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $Y_1 = A.B,\ Y_2\overline{B.C}$
2. $Y = Y_1 + Y_2 = A.B + \overline{B.C}$

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_sol_1_96467a2b_30102026.png?v=96467a2b35db)


![printed figure: Inputs A, B to an AND gate and B, C to a NAND gate; outputs Y1 and Y2 feed an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q046_sol_2_342405e8_30102026.png?v=342405e87e89)

*Inputs A, B to an AND gate and B, C to a NAND gate; outputs Y1 and Y2 feed an OR gate giving Y*

![drawn: Inputs A, B to an AND gate and B, C to a NAND gate; outputs Y1 and Y2 feed an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q046_solution_2_c5970f10_02112026.svg?v=c5970f10b99e)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. The upper gate is AND of $A$ and $B$; the lower gate is NAND of $B$ and $C$; both feed an OR gate, so $y = AB + \overline{BC}$.
2. For $t < t_2$ and $t > t_4$, $B = 0$, so $\overline{BC} = \overline{0} = 1$ and $y = 1$.
3. For $t_2 < t < t_4$, $B = 1$ and $C = 0$, so $\overline{BC} = \overline{0} = 1$ and $y = 1$.
4. Hence $y = 1$ (5 V) at all times, a constant 5 V line, which is option $3$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q046_84eada59_30102026.png?v=84eada59cfa7)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q046_9e980cd2_30102026.png?v=9e980cd23776)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Reading a two-gate combinational circuit off its wiring and tracing three input waveforms through it interval by interval
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are stored as empty strings in this packet, so there is no option waveform to examine and no route to any of them can be checked.
- **Why:** This question requires tracing supplied waveforms through a circuit that exists only in the figure, demonstrated by 'For the given circuit, the input digital signals are applied at the terminals A, B and C'.
- **Note:** Options 1 to 4 are empty strings in our record, so an option set is missing and no trap can be audited; recorded as source_damage_artifact and a repair task rather than as a property of the question. The figure IS supplied: its spec wires A and B into an AND gate, B and C into an AND gate carrying an inversion bubble, and both outputs into an OR gate, so $y=AB+\overline{BC}$. A reviewer holding the printed options should check for the waveform of $AB+BC$, which is what ignoring the bubble produces, and for $AB\cdot\overline{BC}$, which is what reading the final gate as an AND produces.
<!--/ecat-->

## Q47

Physics · Magnetic Effect of Electric Current

In the product $\vec{F} = q\left(\vec{v} \times \vec{B}\right) = q\vec{v} \times \left(B\hat{i} + B\hat{j} + B_0\hat{k}\right)$ For $q = 1$ and $\vec{v} = 2\hat{i} + 4\hat{j} + 6\hat{k}$ and $\vec{F} = 4\hat{i} - 20\hat{j} + 12\hat{k}$ What will be the complete expression for $\vec{B}$ ?

- (1) $8\hat{i} + 8\hat{j} - 6\hat{k}$
- (2) $6\hat{i} + 6\hat{j} - 8\hat{k}$
- (3) $-8\hat{i} - 8\hat{j} - 6\hat{k}$
- **(4)** $-6\hat{i} - 6\hat{j} - 8\hat{k}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\vec{v} = 2\hat{i} + 4\hat{j} + 6\hat{k}$
2. $\vec{F} = 4\hat{i} - 20\hat{j} + 12\hat{k}$
3. $\vec{B} = B\hat{i} + B\hat{j} + B_0\hat{k}$
4. $\vec{F} = q\begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 4 & 6 \\ B & B & B_0 \end{vmatrix}$
5. $= \hat{i}\left[4B_0 - 6B\right] - \hat{j}\left[2B_0 - 6B\right] + \hat{k}\left[2B - 4B\right]$
6. $\vec{F} = 4\hat{i} - 20\hat{j} + 12\hat{k}$
7. $4B_0 - 6B = 4$
8. $-\left(2B_0 - 6B\right) = 20 \Rightarrow 2B_0 = 20 + 6\left(-6\right)$
9. $-2B = 12 \Rightarrow B = -6$

**Solved independently** (answer withheld)

1. With $q = 1$, $\vec{F} = \vec{v} \times \vec{B}$ where $\vec{v} = (2, 4, 6)$ and $\vec{B} = (B, B, B_0)$.
2. $\vec{v} \times \vec{B} = (4B_0 - 6B)\hat{i} + (6B - 2B_0)\hat{j} + (2B - 4B)\hat{k}$.
3. $\hat{k}$: $-2B = 12 \Rightarrow B = -6$.
4. $\hat{i}$: $4B_0 - 6(-6) = 4 \Rightarrow B_0 = -8$.
5. $\hat{j}$ check: $6(-6) - 2(-8) = -36 + 16 = -20$, consistent.
6. $\vec{B} = -6\hat{i} - 6\hat{j} - 8\hat{k}$, which is option $4$.

**Subtopic:** Magnetic Field, Lorentz Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q047_204484f6_30102026.png?v=204484f618d1)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q047_d3e0cfda_30102026.png?v=d3e0cfdafaaf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A cross-product equation is solved component by component: each component of $\vec F$ gives one equation in the unknown components of $\vec B$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The $\hat k$ component of $\vec v\times\vec B$ is $v_xB_y-v_yB_x=2B-4B=-2B$, and taking the two products in the other order turns $-2B=12$ into $2B=12$, so the magnitudes 6, 6 and 8 all survive and only the signs on $\hat i$ and $\hat j$ flip
- **Why:** This question requires a cross product equated component by component and solved for the field, demonstrated by "What will be the complete expression for $\vec{B}$ ?" with $\vec v$ and $\vec F$ both given in components.
<!--/ecat-->

## Q48

Physics · Kinematics

A car starts from rest and accelerates at $5\,\mathrm{m/s^2}$. At $t = 4\,\mathrm{s}$, a ball is dropped out of a window by a person sitting in the car. What is the velocity and acceleration of the ball at $t = 6\,\mathrm{s}$? (Take $g = 10\,\mathrm{m/s^2}$)

- (1) $20\sqrt{2}\,\mathrm{m/s}, 0$
- **(2)** $20\sqrt{2}\,\mathrm{m/s}, 10\,\mathrm{m/s^2}$
- (3) $20\,\mathrm{m/s}, 5\,\mathrm{m/s^2}$
- (4) $20\,\mathrm{m/s}, 0$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Ball dropped from moving car at t = 4 follows a curved path; velocity components at t = 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q048_sol_1_7d661a14_30102026.png?v=7d661a14c9ba)

*Ball dropped from moving car at t = 4 follows a curved path; velocity components at t = 6*

![drawn: Ball dropped from moving car at t = 4 follows a curved path; velocity components at t = 6](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q048_solution_1_f9b3bf97_02112026.svg?v=f9b3bf97b202)  
*drawn by code/lib/physics_figure.py*

1. At $t = 4,\ v = 0 + 5 \times 4 = 20\,\mathrm{m/s}$
2. $v_y = 0 + 10 \times 2 = 20$
3. $v = \sqrt{20^2 + 20^2} = 20\sqrt{2},\ a = 10\,\mathrm{m/s^2}$

**Solved independently** (answer withheld)

1. At $t = 4\,\mathrm{s}$ the car's speed is $v = at = 5 \times 4 = 20\,\mathrm{m/s}$, so the ball leaves with horizontal velocity $u_x = 20\,\mathrm{m/s}$.
2. Once released, the only force on the ball is gravity, so $a_x = 0$ and $u_x$ stays $20\,\mathrm{m/s}$.
3. From $t = 4$ to $t = 6\,\mathrm{s}$ the ball falls for $2\,\mathrm{s}$: $v_y = g t = 10 \times 2 = 20\,\mathrm{m/s}$.
4. $v = \sqrt{u_x^2 + v_y^2} = \sqrt{20^2 + 20^2} = 20\sqrt{2}\,\mathrm{m/s}$.
5. The acceleration is $g = 10\,\mathrm{m/s^2}$ downward, which is option $2$.

**Subtopic:** Projectile Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q048_92194bb8_30102026.png?v=92194bb864d7)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q048_f15b939b_30102026.png?v=f15b939bb9b8)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ball released from an accelerating car keeps the horizontal velocity it had at release and is thereafter accelerated only by gravity
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The velocity half is worked out in full, $20\,\mathrm{m/s}$ horizontal and $20\,\mathrm{m/s}$ vertical giving $20\sqrt2\,\mathrm{m/s}$, and the acceleration half is answered by noticing that the ball no longer shares the car's $5\,\mathrm{m/s^2}$, which leaves zero
- **Why:** This question requires a release velocity carried forward while gravity acts for the remaining time, demonstrated by "What is the velocity and acceleration of the ball at $t = 6\,\mathrm{s}$?" with the drop at $t=4\,\mathrm{s}$.
<!--/ecat-->

## Q49

Physics · Current Electricity

Three resistors having resistance $r_1$, $r_2$, and $r_3$ are connected as shown in the given circuit. The ratio $i_3/i_1$ of currents in terms of resistances used in the circuit is:

![printed figure: r1 in series with parallel r2 and r3 between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q049_d6f0c76f_30102026.png?v=d6f0c76fc1f4)

*r1 in series with parallel r2 and r3 between terminals A and B*

![drawn: r1 in series with parallel r2 and r3 between terminals A and B](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q049_question_8bbf18f3_02112026.svg?v=8bbf18f3ab98)  
*drawn by code/lib/physics_figure.py*

- (1) $\frac{r_1}{r_1+r_2}$
- (2) $\frac{r_2}{r_1+r_3}$
- (3) $\frac{r_1}{r_2+r_3}$
- **(4)** $\frac{r_2}{r_2+r_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: r1 in series with parallel r2 and r3 between A and B, currents i1, i2, i3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q049_sol_1_d21f28ae_30102026.png?v=d21f28aefbc3)

*r1 in series with parallel r2 and r3 between A and B, currents i1, i2, i3*

![drawn: r1 in series with parallel r2 and r3 between A and B, currents i1, i2, i3](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q049_solution_1_c47a60f6_02112026.svg?v=c47a60f6a343)  
*drawn by code/lib/physics_figure.py*

1. $i_3 = \left(\frac{r_2}{r_2 + r_3}\right) i_1 \Rightarrow \frac{i_3}{i_1} = \left(\frac{r_2}{r_2 + r_3}\right)$

**Solved independently** (answer withheld)

1. $r_2$ and $r_3$ are in parallel, so they share the same voltage: $i_2 r_2 = i_3 r_3$.
2. Junction rule: $i_1 = i_2 + i_3$.
3. Substitute $i_2 = \frac{i_3 r_3}{r_2}$: $i_1 = i_3\left(\frac{r_3}{r_2} + 1\right) = i_3\frac{r_2 + r_3}{r_2}$.
4. $\frac{i_3}{i_1} = \frac{r_2}{r_2 + r_3}$, which is option $4$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q049_75053200_30102026.png?v=75053200220c)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q049_0d4da72a_30102026.png?v=0d4da72a9c23)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a current divider the fraction taken by one branch is the OTHER branch's resistance over the sum of the two, and a series resistor carries the whole current so it cannot enter the ratio
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The divider's numerator is got right, the sibling branch $r_2$, and the denominator is built from the resistance along $i_3$'s own route through the circuit, $r_1+r_3$, instead of from the two branches that share the junction
- **Why:** This question requires the current-divider rule applied to the junction the figure shows, demonstrated by "The ratio $i_3/i_1$ of currents in terms of resistances used in the circuit" with $r_1$ drawn in series ahead of the parallel pair.
- **Note:** The figure arrived as a drawn spec carrying a netlist — r1 between A and N, r2 and r3 both between N and B — so the topology the answer depends on could be read directly.
<!--/ecat-->

## Q50

Physics · Ray Optics

A point object is placed at a distance of $60\,\mathrm{cm}$ from a convex lens of focal length $30\,\mathrm{cm}$. If a plane mirror were put perpendicular to the principal axis of the lens and at a distance of $40\,\mathrm{cm}$ from it, the final image would be formed at a distance of:

![printed figure: Convex lens with object 60 cm to the left and a plane mirror 40 cm to the right on the principal axis](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q050_32c637ba_30102026.png?v=32c637babf19)

*Convex lens with object 60 cm to the left and a plane mirror 40 cm to the right on the principal axis*

![drawn: Convex lens with object 60 cm to the left and a plane mirror 40 cm to the right on the principal axis](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q050_question_75a7d09e_02112026.svg?v=75a7d09e87bd)  
*drawn by code/lib/physics_figure.py*

- (1) $30\mathrm{cm}$ from the plane mirror, it would be a virtual image.
- **(2)** $20\,\mathrm{cm}$ from the plane mirror, it would be a virtual image.
- (3) $20\,\mathrm{cm}$ from the lens, it would be a real image.
- (4) $30\,\mathrm{cm}$ from the lens, it would be a real image.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Convex lens (f = 30) with object at 60 and plane mirror at 40; ray traced to image 20 behind mirror and back through the lens](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q050_sol_1_9ae59d13_30102026.png?v=9ae59d13cf1a)

*Convex lens (f = 30) with object at 60 and plane mirror at 40; ray traced to image 20 behind mirror and back through the lens*

![drawn: Convex lens (f = 30) with object at 60 and plane mirror at 40; ray traced to image 20 behind mirror and back through the lens](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q050_solution_1_6bdf5cd4_02112026.svg?v=6bdf5cd46cdd)  
*drawn by code/lib/physics_figure.py*

1. $\frac{1}{v} - \frac{1}{u} = \frac{1}{f}$
2. $\frac{1}{v_1} - \frac{1}{(-60)} = \frac{1}{30}$
3. $\frac{1}{v_1} = \frac{1}{30} - \frac{1}{60} = \frac{1}{60}$
4. $v_1 = +60$
5. $\frac{1}{v_2} - \frac{1}{u} = \frac{1}{f}$
6. $\frac{1}{v_2} - \frac{1}{(-20)} = \frac{1}{30}$
7. $\frac{1}{v_2} = \frac{1}{30} - \frac{1}{20} = \frac{10}{30 \times 20}$
8. $v_2 = -60$

**Solved independently** (answer withheld)

1. Sign convention (Cartesian, applied per surface): distances measured from the optical centre/pole, positive along the direction of the incident light at that element. Lens at $x=0$, object at $x=-60\,\text{cm}$, mirror at $x=+40\,\text{cm}$.
2. First refraction at the lens (light travelling $+x$): $u=-60$, $f=+30$, so $\frac{1}{v}=\frac{1}{f}+\frac{1}{u}=\frac{1}{30}-\frac{1}{60}=\frac{1}{60}$, $v=+60\,\text{cm}$.
3. The converging rays heading for $x=+60$ meet the mirror at $x=+40$ first, so the lens image is a virtual object $60-40=20\,\text{cm}$ behind the plane mirror.
4. Reflection at the plane mirror: image is as far in front as the object is behind, so a real image forms $20\,\text{cm}$ in front of the mirror, at $x=+20\,\text{cm}$ (rays converge there, then diverge travelling $-x$).
5. Second refraction at the lens (light now travelling $-x$; take $-x$ as positive): the point at $x=+20$ is a real object on the incoming side, $u=-20$, $f=+30$.
6. $\frac{1}{v}=\frac{1}{30}-\frac{1}{20}=-\frac{1}{60}$, so $v=-60\,\text{cm}$: the image is on the incoming side, $60\,\text{cm}$ from the lens at $x=+60$.
7. Light then leaves the system travelling $-x$ and does not meet the mirror again; the final image is virtual (rays diverge from $x=+60$).
8. Final image: virtual, $60\,\text{cm}$ from the lens, i.e. $60-40=20\,\text{cm}$ from (behind) the plane mirror, which matches option $2$.

**Subtopic:** Lens Formula, Reflection at a Smooth Surface · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q050_ba9e85c4_30102026.png?v=ba9e85c44d68)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q050_39655b98_30102026.png?v=39655b983956)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The lens would image the object 60 cm away, which is behind the mirror, so that point acts as a virtual object and the plane mirror places the final image the same 20 cm on its own near side
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Applying the lens equation as $\frac{1}{v}=\frac{1}{f}+\frac{1}{u}$ with $u$ taken as $+60$ gives $\frac{1}{v}=\frac{1}{30}+\frac{1}{60}=\frac{1}{20}$, so the answer comes out as a real image $20\,\mathrm{cm}$ from the lens and the mirror is never used
- **Why:** This question requires a lens image located first and then re-imaged by a mirror standing inside that distance, demonstrated by "at a distance of $40\,\mathrm{cm}$ from it" when the lens alone would image at $60\,\mathrm{cm}$.
- **Note:** The key is tagged as printed, and the doubt is recorded here. Tracing the rays strictly: the lens image would fall $20\,\mathrm{cm}$ behind the mirror, the mirror reflects the converging beam, and the rays meet $20\,\mathrm{cm}$ in front of the mirror — which is also $20\,\mathrm{cm}$ from the lens, and where rays actually meet the image is real. That reading matches option 3's words, while the printed key is option 2, which measures the same $20\,\mathrm{cm}$ from the mirror and calls the image virtual. So options 2 and 3 can be read as describing one point with two different natures, and the key rests on which side of the mirror the $20\,\mathrm{cm}$ is counted to. The trap above is written on the independent arithmetic route to option 3 so that the teaching does not depend on that dispute.
<!--/ecat-->

## Q51

Chemistry · inorganic · Chemical Bonding and Molecular Structure

$\mathrm{BF_3}$ is planar and electron deficient compound. Hybridization and number of electrons around the central atom, respectively are

- **(1)** $\mathrm{Sp^2}$ and 6
- (2) $\mathrm{Sp^2}$ and 8
- (3) $\mathrm{Sp^3}$ and 4
- (4) $\mathrm{Sp^3}$ and 6

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: boron trifluoride (trigonal planar: B bonded to three F)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q051_sol_1_0ea2faab_30102026.png?v=0ea2faab334f)

*boron trifluoride (trigonal planar: B bonded to three F)*

![drawn: boron trifluoride (trigonal planar: B bonded to three F)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q051_solution_1_c5f78ff9_02112026.svg?v=c5f78ff9b7f9)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Hybridisation - $sp^{2}$
2. Number of electrons around the central atom $= 6$

**Solved independently** (answer withheld)

1. Boron has $3$ valence electrons ($2s^2 2p^1$) and forms $3$ $\sigma$ bonds with $\mathrm{F}$, with no lone pair.
2. $3$ electron domains $\Rightarrow$ $sp^2$ hybridization, trigonal planar geometry.
3. Electrons around B $= 3 \times 2 = 6$ (electron deficient, incomplete octet), which is option $1$.

**Subtopic:** Hybridisation, Octet Rule · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q051_5b7a40e1_30102026.png?v=5b7a40e1ff23)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q051_273bb9fc_30102026.png?v=273bb9fc3b27)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Three bond pairs make boron sp2 and the molecule planar, and with only three bonds boron carries six electrons, two short of an octet
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The hybridisation half is settled from 'planar' and is right here; the electron count is then completed with the octet, which is the number carried for every filled central atom. The stem's other word, 'electron deficient', is the one that makes it 6.
- **Why:** This question requires the hybridisation and electron count read off the printed description, demonstrated by the stem supplying both criteria itself, 'planar and electron deficient', so that option 2's '8' contradicts the second one.
<!--/ecat-->

## Q52

Chemistry · physical · Redox Reactions

Which of the following reactions is the metal displacement reaction? Choose the right option.

- (1) $\mathrm{Fe + 2HCl \longrightarrow FeCl_2 + H_2\uparrow}$
- (2) $\mathrm{2Pb(NO_3)_2 \longrightarrow 2PbO + 4NO_2 + O_2\uparrow}$
- (3) $\mathrm{2KClO_3 \xrightarrow{\Delta} 2KCl + 3O_2}$
- **(4)** $\mathrm{Cr_2O_3 + 2Al \xrightarrow{\Delta} Al_2O_3 + 2Cr}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Metal displacement reactions are the ones in which more reactive metal displaces a less reactive metal from its compound.
2. Thus, out of the given reactions, the metal displacement reaction is:
3. $\mathrm{Cr_2O_3 + 2Al \xrightarrow{\Delta} Al_2O_3 + 2Cr}$

**Solved independently** (answer withheld)

1. A metal displacement reaction is one where a metal in a compound is replaced by another metal: $\mathrm{A + BX \rightarrow AX + B}$, with $\mathrm{A}$ and $\mathrm{B}$ both metals.
2. Option 1, $\mathrm{Fe + 2HCl \rightarrow FeCl_2 + H_2}$, displaces hydrogen, not a metal.
3. Options 2 and 3 have a single reactant breaking into products, so they are decomposition reactions.
4. Option 4, $\mathrm{Cr_2O_3 + 2Al \rightarrow Al_2O_3 + 2Cr}$: $\mathrm{Al}$ displaces the metal $\mathrm{Cr}$, so it is a metal displacement reaction, which is option $4$.

**Subtopic:** Types of Redox Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q052_eb9a37ae_30102026.png?v=eb9a37ae888b)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q052_4845d50e_30102026.png?v=4845d50edc1b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In a metal displacement reaction the species displaced from its compound is a metal; when hydrogen is the species set free the reaction is a non-metal displacement
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Iron is a metal and it displaces something, so the equation reads as metal displacement to a student who takes the word 'metal' in the category name to describe the reactant doing the displacing. What is displaced here is hydrogen, which makes this the non-metal displacement example.
- **Why:** This question requires the definition of metal displacement applied to each printed equation, demonstrated by option 4, 'Cr2O3 + 2Al → Al2O3 + 2Cr', being the only one in which a metal leaves its compound.
<!--/ecat-->

## Q53

Chemistry · organic · Isomerism in Organic Compounds

The compound which shows metamerism is

- (1) $\mathrm{C_3H_6O}$
- **(2)** $\mathrm{C_4H_{10}O}$
- (3) $\mathrm{C_5H_{12}}$
- (4) $\mathrm{C_3H_8O}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Metamers are the isomers having the same molecular formula but different alkyl groups on two sides of functional groups.
2. $\mathrm{CH_3{-}CH_2{-}CH_2{-}O{-}CH_3}$, $\mathrm{CH_3{-}CH_2{-}O{-}CH_2{-}CH_3}$

**Solved independently** (answer withheld)

1. Metamerism needs a polyvalent functional group (e.g. $-\mathrm{O}-$ or $-\mathrm{CO}-$) with different alkyl groups attached on either side.
2. $\mathrm{C_4H_{10}O}$: $\mathrm{C_2H_5{-}O{-}C_2H_5}$ and $\mathrm{CH_3{-}O{-}C_3H_7}$ are metamers.
3. $\mathrm{C_3H_8O}$ has only one ether, $\mathrm{CH_3OC_2H_5}$; $\mathrm{C_3H_6O}$ has only one ketone, $\mathrm{CH_3COCH_3}$; $\mathrm{C_5H_{12}}$ is an alkane with no functional group, so none show metamerism.
4. Hence the answer is option $2$.

**Subtopic:** Tautomer and Metamer Isomerism · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q053_ab524541_30102026.png?v=ab524541f8e4)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q053_03ac9da3_30102026.png?v=03ac9da381d7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Metamerism needs a divalent group with two different alkyl groups on either side of it, which an ether first manages at four carbons
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Metamerism and tautomerism are two '-merism' names taught in the same breath, and $\mathrm{C_3H_6O}$ is acetone, the standard keto-enol tautomerism case. A student who has the two names as one answers the tautomerism question instead.
- **Why:** This question requires the definition of metamerism applied to four molecular formulas, demonstrated by the stem offering nothing but formulas, so the answer turns on which one can be split two different ways across a divalent atom.
<!--/ecat-->

## Q54

Chemistry · physical · Ionic Equilibrium

The $\mathrm{p}K_b$ of dimethylamine and $\mathrm{p}K_a$ of acetic acid are $3.27$ and $4.77$ respectively at $T\,(\mathrm{K})$. The correct option for the $\mathrm{pH}$ of dimethyl ammonium acetate solution is:

- **(1)** $7.75$
- (2) $6.25$
- (3) $8.50$
- (4) $5.50$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The given salt is a salt of weak acid + weak base.
2. $\mathrm{pH} = 0.5\,[\mathrm{p}K_w + \mathrm{p}K_a - \mathrm{p}K_b]$
3. $\mathrm{pH} = 0.5\,[14 + 4.77 - 3.27]$
4. $\mathrm{pH} = 0.5\,[15.5]$
5. $\mathrm{pH} = 7.75$

**Solved independently** (answer withheld)

1. Dimethyl ammonium acetate is a salt of a weak acid and a weak base, so $\mathrm{pH} = 7 + \frac{1}{2}(\mathrm{p}K_a - \mathrm{p}K_b)$.
2. $\mathrm{p}K_a - \mathrm{p}K_b = 4.77 - 3.27 = 1.50$.
3. $\mathrm{pH} = 7 + \frac{1.50}{2} = 7.75$, which is option $1$.

**Subtopic:** Hydrolysis of Salts · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q054_a187c869_30102026.png?v=a187c869f71b)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q054_918f2ce2_30102026.png?v=918f2ce216c7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For the salt of a weak acid with a weak base, $\mathrm{pH} = 7 + \frac{1}{2}(\mathrm{p}K_a - \mathrm{p}K_b)$, so the stronger of the two partners decides which side of 7 the solution sits
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Taking the half-difference the other way round, $7 + \frac{1}{2}(3.27-4.77)$, gives exactly $6.25$. The same number is also the pOH of the right answer, so two different slips land on this one option.
- **Why:** This question requires the pH relation for the salt of a weak acid and a weak base applied to the printed pK values, demonstrated by the options being $7 \pm 0.75$ and $7 \pm 1.50$, the four results of keeping or dropping the factor of one half and of either order of subtraction.
<!--/ecat-->

## Q55

Chemistry · inorganic · The s-Block Elements

The structure of beryllium chloride in solid state and vapour phase, are:

- (1) Dimer and Linear, respectively
- (2) Chain in both
- **(3)** Chain and dimer, respectively
- (4) Linear in both

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In solid state:

![printed figure: polymeric chain structure of solid beryllium chloride: four Be atoms in a row, each neighbouring pair joined by two bridging Cl atoms (the last bridge printed as one Cl and one O), with open wedge bonds at both chain ends](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q055_sol_1_96cebabc_30102026.png?v=96cebabc8268)

*polymeric chain structure of solid beryllium chloride: four Be atoms in a row, each neighbouring pair joined by two bridging Cl atoms (the last bridge printed as one Cl and one O), with open wedge bonds at both chain ends*

![drawn: polymeric chain structure of solid beryllium chloride: four Be atoms in a row, each neighbouring pair joined by two bridging Cl atoms (the last bridge printed as one Cl and one O), with open wedge bonds at both chain ends](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q055_solution_1_bbc8fd0e_02112026.svg?v=bbc8fd0e464d)  
*drawn by RDKit (code/lib/chem_cards.py)*

2. In vapour phase:

![printed figure: dimeric beryllium chloride ($\ce{Be2Cl4}$): Cl–Be(μ-Cl)2Be–Cl, two Be atoms bridged by two Cl atoms, each Be carrying one terminal Cl](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q055_sol_2_ea973dfd_30102026.png?v=ea973dfd7520)

*dimeric beryllium chloride ($\ce{Be2Cl4}$): Cl–Be(μ-Cl)2Be–Cl, two Be atoms bridged by two Cl atoms, each Be carrying one terminal Cl*

![drawn: dimeric beryllium chloride ($\ce{Be2Cl4}$): Cl–Be(μ-Cl)2Be–Cl, two Be atoms bridged by two Cl atoms, each Be carrying one terminal Cl](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q055_solution_2_e52ff6a8_02112026.svg?v=e52ff6a8125b)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. As NCERT teaches, solid $\mathrm{BeCl_2}$ has a chloro-bridged polymeric chain structure, and in the vapour phase it forms a chloro-bridged dimer $\mathrm{Be_2Cl_4}$, which breaks into the linear monomer only at high temperatures (about $1200\,\mathrm{K}$). This matches option $3$, chain and dimer.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q055_e779509a_30102026.png?v=e779509afd07)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q055_b0a1aafe_30102026.png?v=b0a1aafee22f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Solid beryllium chloride is a polymeric chain, and in the vapour it is a chlorine-bridged dimer that breaks into the linear monomer only near 1200 K
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The dimer and the linear monomer are both printed in the clause about the vapour, and 'linear' is the word that stays with a student, so the vapour is given the monomer and the dimer slides back onto the solid. The solid is the chain and the vapour is the dimer.
- **Why:** This question requires the stated structures of beryllium chloride in two states, demonstrated by the stem asking for 'solid state and vapour phase' together, so an option must get both halves right.
<!--/ecat-->

## Q56

Chemistry · inorganic · The D- and F-Block Elements – Practice

$\mathrm{Zr}$ ($Z = 40$) and $\mathrm{Hf}$ ($Z = 72$) have similar atomic and ionic radii because of:

- **(1)** lanthanoid contraction
- (2) having similar chemical properties
- (3) Belonging to same group
- (4) diagonal relationship

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Due to presence of $4f$ electrons in $\mathrm{Hf}$ it’s $Z_{\mathrm{eff}}$ increases, size remains the same.
2. This is also known as lanthanoid contraction.

**Solved independently** (answer withheld)

1. The $4f$ electrons filled before $\mathrm{Hf}$ ($Z=72$) shield poorly, so the lanthanoid contraction cancels the size increase expected from $\mathrm{Zr}$ ($4d$) to $\mathrm{Hf}$ ($5d$). Their radii are therefore nearly equal, which is option $1$.

**Subtopic:** Variation of Atomic and Ionic Radii · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q056_551aec90_30102026.png?v=551aec90cb88)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q056_66a8e4ac_30102026.png?v=66a8e4aceb76)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The lanthanoid contraction cancels the increase in size expected on going down group 4, which leaves hafnium with almost the radius of zirconium
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Zr and Hf are indeed one above the other in group 4, so the option is a true statement and the easiest one to confirm. Being in the same group is the reason radii normally GROW downwards; it is the lanthanoid contraction between the two that cancels that growth.
- **Why:** This question requires the stated cause of the radius similarity, demonstrated by the stem's 'have similar atomic and ionic radii because of' with two of the options restating the similarity instead of accounting for it.
<!--/ecat-->

## Q57

Chemistry · physical · Structure of Atom

A particular station of All India Radio, New Delhi, broadcasts on a frequency of $1,368\,\mathrm{KHz}$ (kilohertz). The wavelength of the electromagnetic radiation emitted by the transmitter is: [Speed of light, $c = 3 \times 10^{8}\,\mathrm{ms^{-1}}$]

- (1) $2192\,\mathrm{m}$
- (2) $21.92\,\mathrm{cm}$
- **(3)** $219.3\,\mathrm{m}$
- (4) $219.2\,\mathrm{m}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Wavelength = speed of light / Frequency
2. Wavelength $= 3 \times 10^{8} / 1368 \times 10^{3}$
3. Wavelength $= 219.298\,\mathrm{m} \approx 219.3\,\mathrm{m}$

**Solved independently** (answer withheld)

1. Convert the frequency: $\nu = 1368\,\mathrm{kHz} = 1.368 \times 10^{6}\,\mathrm{Hz}$.
2. Use $\lambda = \frac{c}{\nu}$.
3. $\lambda = \frac{3 \times 10^{8}}{1.368 \times 10^{6}} = 219.298\,\mathrm{m}$.
4. Rounded to one decimal place, $\lambda \approx 219.3\,\mathrm{m}$, which is option $3$.

**Subtopic:** Wave Nature of Electromagnetic Radiation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q057_02b254fa_30102026.png?v=02b254fa6e0e)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q057_e1fba349_30102026.png?v=e1fba3496ee8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Wavelength is the speed of light divided by the frequency, with the kilohertz turned into hertz first
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  $\frac{3\times10^{8}}{1.368\times10^{6}} = 219.298$ m, and a student who stops the division at three figures after the point reads 219.2 instead of rounding to 219.3. The method, the conversion and the magnitude are all right; only the last digit is cut rather than rounded.
- **Why:** This question requires $\lambda = c/\nu$ worked out from the printed frequency, demonstrated by the options holding the same digit string at three magnitudes, '2192 m', '219.2 m' and '21.92 cm', against the rounded 219.3 m.
<!--/ecat-->

## Q58

Chemistry · physical · Basic Concepts of Chemistry

An organic compound contains $78\%$ (by wt.) carbon and remaining percentage of hydrogen. The right option for the empirical formula of this compound is: [Atomic wt. Of C is 12, H is 1]

- **(1)** $\mathrm{CH_3}$
- (2) $\mathrm{CH_4}$
- (3) $\mathrm{CH}$
- (4) $\mathrm{CH_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Element | Percentage | Moles | Relative
2. $\mathrm{C}$ | $78$ | $6.5$ | $1$
3. $\mathrm{H}$ | $22$ | $22$ | $3.38$
4. Thus, empirical formula is $\mathrm{CH_3}$.

**Solved independently** (answer withheld)

1. Hydrogen percentage $= 100 - 78 = 22\%$.
2. Moles of C in 100 g: $\frac{78}{12} = 6.5$.
3. Moles of H in 100 g: $\frac{22}{1} = 22$.
4. Divide by the smaller: $\mathrm{C}:\mathrm{H} = 1 : \frac{22}{6.5} = 1 : 3.38$.
5. Nearest simple ratio among the options is $1:3$, so the empirical formula is $\mathrm{CH_3}$, option $1$.

**Subtopic:** Empirical and Molecular Formula · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q058_2c6eb054_30102026.png?v=2c6eb0549376)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q058_5df00a57_30102026.png?v=5df00a57d32d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An empirical formula is the mole ratio: divide each mass percentage by the atomic weight and reduce to the nearest whole numbers
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  $78/12 = 6.5$ and $22/1 = 22$, so the ratio is $1 : 3.38$, and rounding that hydrogen count upward gives $\mathrm{CH_4}$ — which is also the only option that is the formula of a familiar molecule. 3.38 rounds down, and the data give $\mathrm{CH_3}$.
- **Why:** This question requires the mole ratio computed from the printed percentages, demonstrated by the stem supplying '78% (by wt.) carbon' and the atomic weights, so the answer turns on where $1 : 3.38$ is rounded.
<!--/ecat-->

## Q59

Chemistry · inorganic · Coordination Compounds – Practice

Ethylenediaminetetraacetate (EDTA) ion is

- (1) Bidentate ligand with two “N” donor atoms
- (2) Tridentate ligand with three “N” donor atoms.
- **(3)** Hexadentate ligand with four “O” and two “N” donor atoms
- (4) Unidentate ligand

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ethylenediaminetetraacetate ion ($\mathrm{EDTA^{4-}}$) is an important hexadentate ligand.
2. It can bind through two nitrogen and four oxygen atoms to a central metal ion.

![printed figure: ethylenediaminetetraacetate ion ($\ce{EDTA^4-}$), drawn with lone pairs on both N atoms and all O atoms](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q059_sol_1_f335747c_30102026.png?v=f335747c0883)

*ethylenediaminetetraacetate ion ($\ce{EDTA^4-}$), drawn with lone pairs on both N atoms and all O atoms*

![drawn: ethylenediaminetetraacetate ion ($\ce{EDTA^4-}$), drawn with lone pairs on both N atoms and all O atoms](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q059_solution_1_eaf5d689_02112026.svg?v=eaf5d689fc23)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. EDTA$^{4-}$ has two amine nitrogen donors and four carboxylate oxygen donors, $2\,\text{N} + 4\,\text{O} = 6$ donor atoms, so it is hexadentate: option $3$.

**Subtopic:** Ligands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q059_0f3e9766_30102026.png?v=0f3e9766ad69)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q059_31a1a042_30102026.png?v=31a1a042229d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** EDTA binds through six sites — two amine nitrogens and four carboxylate oxygens — which makes it hexadentate
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The ligand's name opens with 'ethylenediamine', which is the name of the standard bidentate two-nitrogen ligand, so a student reading the first half of the name answers for 'en'. The name continues 'tetraacetate', and those four acetate oxygens are what take the count from two to six.
- **Why:** This question requires the stated denticity of EDTA and which atoms donate, demonstrated by option 3 reading 'Hexadentate ligand with four "O" and two "N" donor atoms', the count the printed name adds up to.
- **Note:** Each option bundles a denticity with its donor atoms, but the stem asks one thing, 'EDTA ion is', so the shape is recorded as mcq rather than two_part.
<!--/ecat-->

## Q60

Chemistry · inorganic · The s-Block Elements

Among the following alkaline earth metal halides, one which is covalent and soluble in organic solvents is:

- (1) Magnesium chloride
- **(2)** Beryllium chloride
- (3) Calcium chloride
- (4) Strontium chloride

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Beryllium halides are essentially covalent and soluble in organic solvents.
2. NCERT line - s block elements (Page no. 309)

**Solved independently** (answer withheld)

1. Be$^{2+}$ has the smallest size and highest charge density among the alkaline earth ions, so by Fajans' rules it strongly polarises Cl$^-$, making BeCl$_2$ covalent and soluble in organic solvents, while MgCl$_2$, CaCl$_2$ and SrCl$_2$ are ionic; this is option $2$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q060_b9451f14_30102026.png?v=b9451f14ca25)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q060_729cf87d_30102026.png?v=729cf87d0a32)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Beryllium's halides stand apart from the rest of group 2: the small, strongly polarising Be2+ makes BeCl2 covalent and soluble in organic solvents
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Magnesium is the element printed next to beryllium in the same passage on covalent character, so a student who has only 'the top of the group is the covalent end' takes the neighbour. Magnesium chloride is ionic; it is beryllium chloride that the chapter calls covalent and soluble in organic solvents.
- **Why:** This question requires the stated anomaly of beryllium among the alkaline earth halides, demonstrated by the stem's criterion 'covalent and soluble in organic solvents' against four chlorides from the same group.
- **Note:** Likeness test applied: beryllium and magnesium resemble each other in no part of their names, so what carries a student to magnesium is its position beside beryllium in the group and in the printed passage, which makes the label nearby_fact.
<!--/ecat-->

## Q61

Chemistry · physical · Surface Chemistry

The right option for the statement “Tyndall effect is exhibited by” is:

- **(1)** Starch solution
- (2) Urea Solution
- (3) $\mathrm{NaCl}$ solution
- (4) Glucose Solution

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Starch is a colloid.

**Solved independently** (answer withheld)

1. The Tyndall effect is the scattering of light by colloidal particles; true solutions do not show it.
2. Urea, $\mathrm{NaCl}$ and glucose dissolve to give true solutions, while starch forms a macromolecular colloid, so starch solution (option $1$) shows the Tyndall effect.

**Subtopic:** Properties of Colloids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q061_28fbb792_30102026.png?v=28fbb792549f)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q061_dd1251dd_30102026.png?v=dd1251dd5ccd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Only particles of colloidal size scatter a light beam, so the Tyndall effect separates a sol such as starch from true solutions of small molecules
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the scattering condition: urea (60 g/mol), sodium chloride and glucose (180 g/mol) all dissolve to particles far below the colloidal range, so all three fail for the identical reason and none carries a feature the others lack. The stem supplies no concentration, appearance or particle size that would favour one of them, and nothing in the three names resembles starch or is printed as a colloid, so no single route reaches one option rather than another.
- **Why:** This question requires the particle-size condition for scattering applied to four named solutions, demonstrated by the stem quoting only 'Tyndall effect is exhibited by' while the options are one macromolecular sol and three solutions of small molecules.
- **Note:** This is a no_trap finding reached after checking all three wrong options, not a gap: the question discriminates on one fact, whether starch is the colloid, and the three true solutions are interchangeable as distractors.
<!--/ecat-->

## Q62

Chemistry · physical · Electrochemistry

The molar conductance of $\mathrm{NaCl}$. $\mathrm{HCl}$ and $\mathrm{CH_3COONa}$ at infinite dilution are 126.45, 426.16 and $91.0\,\mathrm{S\,cm^{2}\,mol^{-1}}$ respectively. The molar conductance of $\mathrm{CH_3COOH}$ at infinite dilution is. Choose the right option for your answer.

- (1) $698.28\,\mathrm{S\,cm^{2}\,mol^{-1}}$
- (2) $540.48\,\mathrm{S\,cm^{2}\,mol^{-1}}$
- (3) $201.28\,\mathrm{S\,cm^{2}\,mol^{-1}}$
- **(4)** $390.71\,\mathrm{S\,cm^{2}\,mol^{-1}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\lambda^{\infty}(\mathrm{CH_3COOH}) = \lambda^{\infty}(\mathrm{CH_3COONa}) + \lambda^{\infty}(\mathrm{HCl}) - \lambda^{\infty}(\mathrm{NaCl})$
2. $= (91 + 426.16 - 126.45)\,\mathrm{S\,cm^{2}\,mol^{-1}}$
3. $= 390.71\,\mathrm{S\,cm^{2}\,mol^{-}}$

**Solved independently** (answer withheld)

1. By Kohlrausch's law, $\Lambda^\circ_m(\mathrm{CH_3COOH}) = \Lambda^\circ_m(\mathrm{HCl}) + \Lambda^\circ_m(\mathrm{CH_3COONa}) - \Lambda^\circ_m(\mathrm{NaCl})$.
2. $426.16 + 91.0 = 517.16\,\mathrm{S\,cm^{2}\,mol^{-1}}$.
3. $517.16 - 126.45 = 390.71\,\mathrm{S\,cm^{2}\,mol^{-1}}$, which is option $4$.

**Subtopic:** Applications of Kohlrausch Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q062_edb29139_30102026.png?v=edb291392648)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q062_37ed0031_30102026.png?v=37ed00310071)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Kohlrausch's law lets limiting molar conductances be added and subtracted like ions: $\Lambda^{\circ}(\mathrm{CH_3COOH}) = \Lambda^{\circ}(\mathrm{CH_3COONa}) + \Lambda^{\circ}(\mathrm{HCl}) - \Lambda^{\circ}(\mathrm{NaCl})$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Worked out every sign arrangement of the three printed values: all three added gives 643.61, NaCl added with the acetate subtracted gives 461.61, and both subtracted from HCl gives 208.71. None of those appears among the options, and none of the printed wrong values (698.28, 540.48, 201.28) is produced by adding or subtracting the three given conductances in any combination or by doubling any one of them, so no wrong option sits at the end of a nameable route.
- **Why:** This question requires Kohlrausch's law applied to the three printed conductances, demonstrated by $91.0 + 426.16 - 126.45 = 390.71$ being the printed key while no other signed combination of the same three numbers appears among the options.
- **Note:** The pattern classifier returned multi_part_respectively, but 'respectively' in this stem belongs to the three data values given, not to the answer, which is a single conductance; the shape is recorded as mcq.
<!--/ecat-->

## Q63

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

The correct structure of 2,6-Dimethyl-dec-4-ene

- (1) (E)-2,6-dimethyldec-3-ene `CCCCC(C)C/C=C/C(C)C` ![(E)-2,6-dimethyldec-3-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q063_option_1_s1_6ab00a5a_02112026.svg?v=6ab00a5ab00d)
- (2) (Z)-2,6-dimethyldec-5-ene `CCCC/C(C)=C\CCC(C)C` ![(Z)-2,6-dimethyldec-5-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q063_option_2_s1_ac18bbc0_02112026.svg?v=ac18bbc0d1c6)
- **(3)** (Z)-2,6-dimethyldec-4-ene `CCCCC(C)/C=C\CC(C)C` ![(Z)-2,6-dimethyldec-4-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q063_option_3_s1_c4da95e4_02112026.svg?v=c4da95e412ac)
- (4) (E)-6,9-dimethyldec-3-ene `CC/C=C/CC(C)CCC(C)C` ![(E)-6,9-dimethyldec-3-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q063_option_4_s1_d6f47d52_02112026.svg?v=d6f47d52bde8)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. 2,6-Dimethyl-dec-4-ene

![printed figure: (Z)-2,6-dimethyldec-4-ene with carbons numbered 1 to 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q063_sol_1_e4a5697d_30102026.png?v=e4a5697d3cd9)

*(Z)-2,6-dimethyldec-4-ene with carbons numbered 1 to 10*

![drawn: (Z)-2,6-dimethyldec-4-ene with carbons numbered 1 to 10](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q063_solution_1_1ac29edc_02112026.svg?v=1ac29edc6ea2)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Target: $\mathrm{CH_3-CH(CH_3)-CH_2-CH=CH-CH(CH_3)-CH_2CH_2CH_2CH_3}$, i.e. 10-carbon chain, $C_4=C_5$, methyls at $C_2$ and $C_6$.
2. Option 1: $\mathrm{(CH_3)_2CH-CH=CH-CH_2-CH(CH_3)-C_4H_9}$ has the double bond at $C_3$: 2,6-dimethyldec-3-ene.
3. Option 2: $\mathrm{(CH_3)_2CH-CH_2CH_2-CH=C(CH_3)-C_4H_9}$ has the double bond at $C_5$: 2,6-dimethyldec-5-ene.
4. Option 3: $\mathrm{(CH_3)_2CH-CH_2-CH=CH-CH(CH_3)-C_4H_9}$ has $C_4=C_5$ and methyls at $C_2$, $C_6$: 2,6-dimethyldec-4-ene.
5. Option 4: $\mathrm{(CH_3)_2CH-CH_2CH_2-CH(CH_3)-CH_2-CH=CH-CH_2CH_3}$ numbers from the other end as 6,9-dimethyldec-3-ene.
6. Only option $3$ matches 2,6-dimethyldec-4-ene.

**Subtopic:** Acyclic or Open Chain Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q063_4684dee6_30102026.png?v=4684dee6e0d9)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q063_d2b36a0f_30102026.png?v=d2b36a0f2ebd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An IUPAC name is read back into a skeleton: dec-4-ene is a ten-carbon chain with the double bond between C4 and C5, and 2,6-dimethyl puts a methyl on the second and sixth carbons of that chain
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are empty strings in this record and no figure is attached to the question, so there is nothing to examine; no trap can be named without the four structures the paper printed.
- **Why:** This question requires an IUPAC name turned back into a structure, demonstrated by the stem reading 'The correct structure of 2,6-Dimethyl-dec-4-ene' with the answer being a drawn skeleton.
- **Note:** The options are stored as four empty strings and has_figure is false with no figure record, so the option set as we hold it carries none of the printed content. The shape is recorded as mcq because the stem has no lettered items or lists, but the printed options were drawn structures, which this axis has no value for; the retired E1 vocabulary called that structure_options. A repair task is needed before any trap or key check can be written, and the key is left exactly as printed.
<!--/ecat-->

## Q64

Chemistry · physical · The Solid State

The correct option for the number of body centred unit cells in all 14 types of Bravais lattice unit cells is:

- (1) 2
- **(2)** 3
- (3) 7
- (4) 5

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Body centred unit cells are possible in Cubic, Tetragonal and Orthorhombic crystal system.

**Solved independently** (answer withheld)

1. Among the 7 crystal systems, a body-centred ($I$) lattice exists only for cubic, tetragonal and orthorhombic: $1 + 1 + 1 = 3$, which is option $2$.

**Subtopic:** Crystal Lattices, Unit Cells and Bravais Lattices · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q064_83070d97_30102026.png?v=83070d97404c)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q064_01b85400_30102026.png?v=01b85400cca1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Of the 14 Bravais lattices, three are body-centred: the cubic, the tetragonal and the orthorhombic systems each have an I-type variant
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Seven is the number carried in the same breath as 14 — the seven crystal systems — and it is also the number of non-primitive lattices among the 14, so two different wrong readings land on it. The stem asks only for the body-centred ones, and there are three.
- **Why:** This question requires the count of body-centred types read off the Bravais lattice table, demonstrated by the stem asking for them 'in all 14 types of Bravais lattice unit cells', with 7 - the number of crystal systems - printed as an option.
<!--/ecat-->

## Q65

Chemistry · organic · Polymers

Which one of the following polymers is Prepared by addition polymerisation?

- (1) Novolac
- (2) Dacron
- **(3)** Teflon
- (4) Nylon-66

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Tetra fluoroethylene (tetrafluoroethylene) →(free radical / Vinyl polymerization) poly(tetrafluoroethylene), repeat unit (-CF2-CF2-)n](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q065_sol_1_93835cce_30102026.png?v=93835cce12f7)

*Tetra fluoroethylene (tetrafluoroethylene) →[free radical / Vinyl polymerization] poly(tetrafluoroethylene), repeat unit [-CF2-CF2-]n*

![drawn: Tetra fluoroethylene (tetrafluoroethylene) →(free radical / Vinyl polymerization) poly(tetrafluoroethylene), repeat unit (-CF2-CF2-)n](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q065_solution_1_ce451a5e_02112026.svg?v=ce451a5eeabd)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Teflon is formed by addition polymerisation: $n\,\mathrm{CF_2{=}CF_2} \rightarrow \mathrm{-(CF_2-CF_2)_n-}$, while Novolac, Dacron and Nylon-66 are condensation polymers, so the answer is option $3$.

**Subtopic:** Classification of Polymers Based on Mode of Polymerisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q065_44c64224_30102026.png?v=44c642249eaa)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q065_c4669a3a_30102026.png?v=c4669a3af565)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Addition polymers grow by monomers adding across a double bond with nothing eliminated, which is how Teflon is made from tetrafluoroethene; Novolac, Dacron and Nylon-66 are all condensation polymers
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Dacron's chemical name is poly(ethylene terephthalate), and 'polyethylene' is the textbook addition polymer, so a student who places Dacron by that word rather than by its two monomers files it as an addition polymer. The ethylene in the name is ethylene glycol, which is condensed with terephthalic acid and gives off water.
- **Why:** This question requires each named polymer placed in its mode of polymerisation, demonstrated by the stem asking which is 'Prepared by addition polymerisation' while only Teflon's monomer, tetrafluoroethene, carries a double bond.
- **Note:** The one other reading the stem invites, taking 'addition' to mean two monomers added together, would fit Dacron, Nylon-66 and Novolac equally and so lands on no single option; the trap is recorded on the option that one named route reaches.
<!--/ecat-->

## Q66

Chemistry · organic · Alcohols, Phenols and Ethers

What is the IUPAC name of the organic compound formed in the following chemical reaction? $\text{Acetone}\xrightarrow[\text{(ii)}\,\mathrm{H_2O,H^+}]{\text{(i)}\,\mathrm{C_2H_5MgBr},\text{dry Ether}}\text{Product}$

- (1) pentan-3-ol
- **(2)** 2-methyl butan-2-ol
- (3) 2-methylpropan-2-ol
- (4) pentan-2-ol

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: acetone →((i) $\ce{C2H5MgBr}$, dryether) (2-methylbutan-2-yloxy)magnesium bromide →($\ce{H2O}$, $\ce{H+}$) 2-methylbutan-2-ol (carbons numbered 1, 2, 3, 4)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q066_sol_1_41ec8bc4_30102026.png?v=41ec8bc4ea83)

*acetone →[(i) $\ce{C2H5MgBr}$, dryether] (2-methylbutan-2-yloxy)magnesium bromide →[$\ce{H2O}$, $\ce{H+}$] 2-methylbutan-2-ol (carbons numbered 1, 2, 3, 4)*

![drawn: acetone →((i) $\ce{C2H5MgBr}$, dryether) (2-methylbutan-2-yloxy)magnesium bromide →($\ce{H2O}$, $\ce{H+}$) 2-methylbutan-2-ol (carbons numbered 1, 2, 3, 4)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q066_solution_1_9da48a28_02112026.svg?v=9da48a288dcb)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. $2$ - methyl - butan - $2$ - ol

**Solved independently** (answer withheld)

1. Acetone is $\mathrm{CH_3COCH_3}$; the nucleophilic ethyl group of $\mathrm{C_2H_5MgBr}$ attacks the carbonyl carbon.
2. This gives the alkoxide adduct $\mathrm{(CH_3)_2C(OMgBr)C_2H_5}$.
3. Acidic hydrolysis ($\mathrm{H_2O, H^+}$) gives the tertiary alcohol $\mathrm{(CH_3)_2C(OH)CH_2CH_3}$.
4. The longest chain has 4 carbons, with $-\mathrm{OH}$ and $-\mathrm{CH_3}$ on C-2: 2-methylbutan-2-ol, which is option $2$.

**Subtopic:** Preparation of Alcohols · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q066_615bbeb7_30102026.png?v=615bbeb727cf)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q066_41e61196_30102026.png?v=41e611961b68)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A Grignard reagent adds its alkyl group to the carbonyl carbon, so acetone plus ethyl magnesium bromide gives the tertiary alcohol 2-methylbutan-2-ol after hydrolysis
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Counting carbons as three plus two and stringing them into one straight chain puts the new OH in the middle of a pentane, which is pentan-3-ol — the product of adding ethyl to propanal, acetone's straight-chain isomer. In acetone the carbonyl is the middle carbon, so the ethyl arrives on a carbon that already carries two methyls.
- **Why:** This question requires the product of the printed Grignard addition and its IUPAC name, demonstrated by the scheme printing '(i) C2H5MgBr, dry Ether' on acetone, which fixes both the group added and the carbon it lands on.
- **Note:** The classifier called this reaction_scheme, which describes the stem; the answer is a name, so the shape on this axis is mcq with the scheme read in the stem.
<!--/ecat-->

## Q67

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List-I with List-II

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{PCl_5}$ | (i) | Square pyramidal |
| (b) | $\mathrm{SF_6}$ | (ii) | Trigonal planar |
| (c) | $\mathrm{BrF_5}$ | (iii) | Octahedral |
| (d) | $\mathrm{BF_3}$ | (iv) | Trigonal bipyramidal |

- (1) (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii)
- (2) (a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)
- **(3)** (a)-(iv), (b)-(iii), (c)-(i), (d)-(ii)
- (4) (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: phosphorus pentachloride ($\ce{PCl5}$), trigonal bipyramidal (wedge/dash drawing)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q067_sol_1_f956dbd3_30102026.png?v=f956dbd3565e)

*phosphorus pentachloride ($\ce{PCl5}$), trigonal bipyramidal (wedge/dash drawing)*

![printed figure: sulfur hexafluoride ($\ce{SF6}$), octahedral (wedge/dash drawing)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q067_sol_2_1f0ace0b_30102026.png?v=1f0ace0b01b9)

*sulfur hexafluoride ($\ce{SF6}$), octahedral (wedge/dash drawing)*

![printed figure: bromine pentafluoride ($\ce{BrF5}$), square pyramidal with one lone pair on Br (wedge/dash drawing)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q067_sol_3_1a30987a_30102026.png?v=1a30987a1d16)

*bromine pentafluoride ($\ce{BrF5}$), square pyramidal with one lone pair on Br (wedge/dash drawing)*

![printed figure: boron trifluoride ($\ce{BF3}$), trigonal planar](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q067_sol_4_b7950f3c_30102026.png?v=b7950f3c449a)

*boron trifluoride ($\ce{BF3}$), trigonal planar*

![drawn: boron trifluoride ($\ce{BF3}$), trigonal planar](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q067_solution_4_5d21e030_02112026.svg?v=5d21e030323c)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. $\mathrm{PCl_5}$: 5 bond pairs, 0 lone pairs on P, $sp^3d$ $\Rightarrow$ trigonal bipyramidal, so (a)-(iv).
2. $\mathrm{SF_6}$: 6 bond pairs, 0 lone pairs on S, $sp^3d^2$ $\Rightarrow$ octahedral, so (b)-(iii).
3. $\mathrm{BrF_5}$: 5 bond pairs, 1 lone pair on Br, $sp^3d^2$ $\Rightarrow$ square pyramidal, so (c)-(i).
4. $\mathrm{BF_3}$: 3 bond pairs, 0 lone pairs on B, $sp^2$ $\Rightarrow$ trigonal planar, so (d)-(ii).
5. The match (a)-(iv), (b)-(iii), (c)-(i), (d)-(ii) is option $3$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q067_242ea8ce_30102026.png?v=242ea8cea2d4)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q067_0e9b9042_30102026.png?v=0e9b9042d60c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** VSEPR shapes follow the total count of electron pairs, bonding and lone, so BrF5 with five bonds and one lone pair is square pyramidal while PCl5 with five bonds is trigonal bipyramidal
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Counting only the atoms bonded to the central atom turns BrF5's five fluorines into a trigonal bipyramid, which is the shape for five pairs with no lone pair. Of the two codes carrying that pair, this is the one that still gives BF3 the trigonal planar shape the student is sure of, so the two impossible pairs it also contains are never tested.
- **Why:** This question requires the VSEPR rule applied to each printed formula, demonstrated by List-II holding only shape names, so the row 'BrF5' is settled by whether the lone pair on bromine is counted.
<!--/ecat-->

## Q68

Chemistry · inorganic · The D- and F-Block Elements – Practice

The incorrect statement among the following is:

- (1) Lanthanoids are good conductors of heat and electricity
- (2) Actinoids are highly reactive metals, especially when finely divided.
- (3) Actinoid contraction is greater for element to element than Lanthanoid contraction
- **(4)** Most of the trivalent Lanthanoid ions are colorless in the solid state.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Many trivalent lanthanoid ions are coloured both in the solid state and in aqueous solutions.
2. Colour of these ions may be attributed to the presence of $f$-electrons.
3. NCERT line - $d$ and $f$ block elements

**Solved independently** (answer withheld)

1. Statement 1: lanthanoids are typical metals and good conductors of heat and electricity, so it is correct.
2. Statement 2: actinoids are highly reactive metals, especially when finely divided, so it is correct.
3. Statement 3: poor shielding by $5f$ electrons makes the actinoid contraction greater from element to element than the lanthanoid contraction, so it is correct.
4. Statement 4: many $Ln^{3+}$ ions are coloured in the solid state and in solution because of $f$-$f$ transitions (only $f^0$ and $f^{14}$ ions such as $La^{3+}$ and $Lu^{3+}$ are colourless), so this statement is incorrect. The answer is option $4$.

**Subtopic:** General Characteristics of Lanthanoids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q068_33e94104_30102026.png?v=33e9410480c1)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q068_9f083170_30102026.png?v=9f0831709c7e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Most trivalent lanthanoid ions are coloured in the solid state and in solution; the lanthanoids are good conductors, the actinoids are highly reactive when finely divided, and the actinoid contraction is the sharper of the two
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A student who knows the lanthanoid contraction by name and has not read the actinoid comparison reads this sentence as the one with its two terms exchanged, and stops there. It is printed as it stands: 5f electrons shield more poorly than 4f, so the actinoid contraction is greater from element to element - which makes this the answer to 'which statement is correct'.
- **Why:** This question requires the stated general characteristics of the f-block elements, demonstrated by option 4 claiming 'Most of the trivalent Lanthanoid ions are colorless in the solid state' where the printed line makes most of them coloured.
- **Note:** The retired per-option vocabulary carried this device as true_statement_trap; on the live twelve-value axis its family is answers_other_question, because the option is true and answers the stem with its 'incorrect' removed.
<!--/ecat-->

## Q69

Chemistry · organic · Hydrocarbons

Dihedral angle of least stable conformer of ethane is

- (1) $60^{\circ}$
- **(2)** $0^{\circ}$
- (3) $120^{\circ}$
- (4) $180^{\circ}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In this position, the dihedral angle ( also called the angle of rotation or the angle of torsion or torsional angle) is zero degree.

**Solved independently** (answer withheld)

1. In ethane the eclipsed conformer has the greatest torsional strain, so it is the least stable conformer.
2. In the eclipsed conformer the C$-$H bonds on the two carbons are aligned, so the dihedral angle is $0^{\circ}$, which is option $2$.

**Subtopic:** Isomerism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q069_66efb52e_30102026.png?v=66efb52e9f7f)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q069_263ec26f_30102026.png?v=263ec26f8995)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ethane is least stable when its hydrogens eclipse, which the convention records as a dihedral angle of 0 degrees; the staggered, most stable form sits 60 degrees away
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $60^{\circ}$ is the number carried for ethane's conformers - the staggered form, and the rotation that separates the two - so a student who retrieves it answers for the MOST stable conformer. The least stable one is the eclipsed form, recorded at $0^{\circ}$.
- **Why:** This question requires the dihedral angle the eclipsed conformer is quoted at, demonstrated by the stem asking for the 'least stable conformer of ethane' with the staggered form's 60 degrees printed beside it.
- **Note:** Flagged arguable_key and tagged as printed: ethane's hydrogens also eclipse at 120 degrees, so option 3 is defensible on the geometry, and the key rests on the convention that the eclipsed conformer is measured at 0 degrees. The tag follows the printed key; the doubt is recorded here, not acted on.
<!--/ecat-->

## Q70

Chemistry · physical · States of Matter

Choose the correct option for graphical representation of Boyle’s law, which shows a graph of pressure vs. Volume of a gas at different temperature.

- (1) ![printed figure: graph of Pressure (P) (bar) vs Volume (V) (dm³): three straight lines rising from the origin, labelled 200 K (steepest), 400 K, 600 K (least steep)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q070_option_1_583cbcee_30102026.png?v=583cbcee12c4) *graph of Pressure (P) (bar) vs Volume (V) (dm³): three straight lines rising from the origin, labelled 200 K (steepest), 400 K, 600 K (least steep)* — [graph]
- **(2)** ![printed figure: graph of Pressure (P) (bar) vs Volume (V) (dm³): three hyperbolic curves, labelled 600 K (outermost), 400 K, 200 K (innermost)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q070_option_2_5e265b6a_30102026.png?v=5e265b6aba10) *graph of Pressure (P) (bar) vs Volume (V) (dm³): three hyperbolic curves, labelled 600 K (outermost), 400 K, 200 K (innermost)* — [graph]
- (3) ![printed figure: graph of Pressure (P) (bar) vs Volume (V) (dm³): three hyperbolic curves, labelled 200 K (outermost), 400 K, 600 K (innermost)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q070_option_3_fa940a2a_30102026.png?v=fa940a2ac7b8) *graph of Pressure (P) (bar) vs Volume (V) (dm³): three hyperbolic curves, labelled 200 K (outermost), 400 K, 600 K (innermost)* — [graph]
- (4) ![printed figure: graph of Pressure (P) (bar) vs Volume (V) (dm³): a single horizontal line labelled (200 K, 400 K, 600 K)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q070_option_4_416cb31c_30102026.png?v=416cb31c874c) *graph of Pressure (P) (bar) vs Volume (V) (dm³): a single horizontal line labelled (200 K, 400 K, 600 K)* — [graph]

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The pressure varies with volume at constant temperature as $P = K/V$.
2. Thus, the graph should be hyperbolic.
3. Also, on increasing the temperature at constant volume, the pressure should increase.
4. Thus, the correct graph is (B).

![printed figure: graph of Pressure (P) (bar) vs Volume (V) (dm³): three hyperbolic curves, labelled 600 K (outermost), 400 K, 200 K (innermost)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q070_sol_1_7a1bc4a9_30102026.png?v=7a1bc4a981cc)

*graph of Pressure (P) (bar) vs Volume (V) (dm³): three hyperbolic curves, labelled 600 K (outermost), 400 K, 200 K (innermost)*


**Solved independently** (answer withheld)

1. At constant $T$, Boyle's law gives $PV = nRT = \text{constant}$, so each isotherm is a rectangular hyperbola $P = \frac{nRT}{V}$; this rules out the straight lines of option $1$ and the horizontal line of option $4$.
2. At a fixed $V$, $P \propto T$, so $P_{600\,K} > P_{400\,K} > P_{200\,K}$ and the $600\,K$ curve lies farthest from the origin.
3. Option $2$ shows hyperbolas with $600\,K$ outermost and $200\,K$ innermost; option $3$ has the order reversed, so the answer is option $2$.

**Subtopic:** Gas Laws · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q070_9dc97458_30102026.png?v=9dc97458f4dc)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q070_16faaadb_30102026.png?v=16faaadb2222)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Boyle's law plotted as pressure against volume gives a hyperbola, one for each temperature, with the higher-temperature isotherm lying farther from the origin
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are graphs and this step was handed only the placeholder text [graph] for each, so what any option actually draws cannot be seen
- **Why:** This question requires choosing the plot that represents a stated gas law, demonstrated by the stem's "Choose the correct option for graphical representation of Boyle's law, which shows a graph of pressure vs. Volume of a gas at different temperature".
- **Note:** All four options arrive as the literal string "[graph]" and no option image was supplied to this step, so no mechanism can be audited. A reviewer holding the printed options should check two candidates: a straight line offered in place of the P-V hyperbola, and isotherms stacked in reverse temperature order with the higher-T curve nearer the origin, which would be `reversed`.
<!--/ecat-->

## Q71

Chemistry · organic · Haloalkanes and Haloarenes

The correct sequence of bond enthalpy of ‘C-X’ bond is

- (1) $\mathrm{CH_3{-}F} < \mathrm{CH_3{-}Cl} > \mathrm{CH_3{-}Br} > \mathrm{CH_3{-}I}$
- (2) $\mathrm{CH_3{-}Cl} > \mathrm{CH_3{-}F} > \mathrm{CH_3{-}Br} > \mathrm{CH_3{-}I}$
- (3) $\mathrm{CH_3{-}F} < \mathrm{CH_3{-}Cl} < \mathrm{CH_3{-}Br} < \mathrm{CH_3{-}I}$
- **(4)** $\mathrm{CH_3{-}F} > \mathrm{CH_3{-}Cl} > \mathrm{CH_3{-}Br} > \mathrm{CH_3{-}I}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Due to high bond length $\mathrm{C{-}I}$ has less bond strength and has less bond dissociation enthalpy.
2. Because of short bond length $\mathrm{C{-}F}$ has high bond dissociation enthalpy so that increasing order of bond dissociation enthalpies

**Solved independently** (answer withheld)

1. Down the group F, Cl, Br, I the halogen gets larger, so the $\mathrm{C{-}X}$ bond gets longer and orbital overlap gets poorer, which lowers the bond enthalpy: $\mathrm{CH_3{-}F} > \mathrm{CH_3{-}Cl} > \mathrm{CH_3{-}Br} > \mathrm{CH_3{-}I}$, which is option $4$.

**Subtopic:** Nature of the C–X Bond · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q071_8564b4a5_30102026.png?v=8564b4a567aa)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q071_c9f4c540_30102026.png?v=c9f4c540d332)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** C-X bond enthalpy falls from C-F to C-I because the halogen's orbital grows larger and overlaps the carbon 2p orbital less well
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A student who holds the C-X bond LENGTH trend, which rises F < Cl < Br < I, reads that rising chain as the answer; bond enthalpy runs the opposite way to bond length, so the printed increasing order is the exact inverse of the key.
- **Why:** This question requires an ordering of a property across a halogen series, demonstrated by the stem "The correct sequence of bond enthalpy of 'C-X' bond is" and by all four options being chains of inequalities.
<!--/ecat-->

## Q72

Chemistry · inorganic · Hydrogen

Tritium, a radioactive isotope of hydrogen, emits which of the following particles?

- (1) Gamma ($\gamma$)
- (2) Neutron (n)
- **(3)** Beta ($\beta^{-}$)
- (4) Alpha ($\alpha$)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Tritium, a radioactive isotope of hydrogen, emits beta$(\beta^{-})$ particles.
2. ${}_{1}\mathrm{H}^{3} \rightarrow {}_{2}\mathrm{He}^{3} + {}_{-1}\mathrm{e}^{0} + \text{antineutrino}$

**Solved independently** (answer withheld)

1. Tritium $^{3}_{1}\mathrm{H}$ is neutron-rich and undergoes $\beta^{-}$ decay: $^{3}_{1}\mathrm{H} \rightarrow\, ^{3}_{2}\mathrm{He} + \beta^{-} + \bar{\nu}$, so the emitted particle is option $3$.

**Subtopic:** Isotopes of Hydrogen and Properties of Dihydrogen · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q072_61a0686c_30102026.png?v=61a0686c7a02)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q072_120fef25_30102026.png?v=120fef25c67c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tritium is neutron-rich and decays by beta emission, a neutron turning into a proton with an electron thrown out
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Alpha is the first decay mode printed in the list of radiations and is the one the word 'radioactive' in the stem calls up, so a student who stored 'radioactive nuclei emit alpha particles' without tying a mode to tritium takes it.
- **Why:** This question requires one stated fact about a named isotope, demonstrated by the stem "Tritium, a radioactive isotope of hydrogen, emits which of the following particles?" with four coordinate radiations as options and no criterion printed to apply.
<!--/ecat-->

## Q73

Chemistry · inorganic · The p–Block Elements



- (Statement I) Acid strength increases in the order given as $\mathrm{HF} << \mathrm{HCl} << \mathrm{HBr} << \mathrm{HI}$.
- (Statement II) As the size of the elements $\mathrm{F}$, $\mathrm{Cl}$, $\mathrm{Br}$, $\mathrm{I}$ increases down the group, the bond strength of $\mathrm{HF}$, $\mathrm{HCl}$, $\mathrm{HBr}$ and $\mathrm{HI}$ decreases and so the acid strength increases.

- (1) Statement I is correct but Statement II is false.
- (2) Statement I is incorrect but Statement II is true.
- **(3)** Both Statement I and Statement II are true
- (4) Both Statement I and Statement II are false.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The acidic strength of these acids varies in the order: $\mathrm{HF} < \mathrm{HCl} < \mathrm{HBr} < \mathrm{HI}$.
2. The stability of these halides decreases down the group due to decrease in bond ($\mathrm{H{-}X}$) dissociation enthalpy in the order: $\mathrm{H{-}F} > \mathrm{H{-}Cl} > \mathrm{H{-}Br} > \mathrm{H{-}I}$.

**Solved independently** (answer withheld)

1. Atomic size increases down the group: $\mathrm{F} < \mathrm{Cl} < \mathrm{Br} < \mathrm{I}$.
2. So the H-X bond dissociation enthalpy decreases: $\mathrm{H{-}F} > \mathrm{H{-}Cl} > \mathrm{H{-}Br} > \mathrm{H{-}I}$.
3. A weaker H-X bond releases $\mathrm{H^+}$ more easily, so acid strength is $\mathrm{HF} < \mathrm{HCl} < \mathrm{HBr} < \mathrm{HI}$; Statement I is true.
4. Statement II states exactly this size and bond-strength reasoning, so it is also true; this is option $3$.

**Subtopic:** Hydrogen Halides, Oxoacids of Halogens · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q073_18bd9fdc_30102026.png?v=18bd9fdc1839)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q073_31bd217d_30102026.png?v=31bd217d8726)

---

## Q74

Chemistry · organic · Chemistry in Everyday Life

Given below are two statements: In the light of the above statements, choose the correct answer from the options given below.

- (Statement I) Aspirin and Paracetamol belong to the class of narcotic analgesics.
- (Statement II) Morphine and Heroin are non-narcotic analgesics.

- (1) Statement I is correct but Statement II is false
- (2) Statement I is incorrect but Statement II is true
- (3) Both Statement I and Statement II are true
- **(4)** Both Statement I and Statement II are false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Aspirin and Paracetamol belong to the class of non narcotic analgesics.
2. Morphine and Heroin are narcotic analgesics.

**Solved independently** (answer withheld)

1. Aspirin and paracetamol are non-narcotic (non-addictive) analgesics, so Statement I is false; morphine and heroin are opiate narcotic analgesics, so Statement II is false; both false is option $4$.

**Subtopic:** Analgesics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q074_70b9dc4b_30102026.png?v=70b9dc4b1f52)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q074_215857e3_30102026.png?v=215857e33b93)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Aspirin and paracetamol are non-narcotic analgesics; morphine and heroin are the narcotic (opioid) ones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Morphine and heroin are the chapter's own examples of narcotics, so Statement II is struck out at once, and Statement I then passes unchecked because 'narcotic analgesics' is the heading printed immediately beside the one aspirin and paracetamol sit under.
- **Why:** This question requires the stated class membership of four named analgesics, demonstrated by Statement I reading 'Aspirin and Paracetamol belong to the class of narcotic analgesics' and Statement II reading 'Morphine and Heroin are non-narcotic analgesics' - the two printed classes exchanged.
- **Note:** E1's pattern label statement_i_ii is mapped to qtype `statements` because the stem prints a labelled statement block and instructs the candidate to judge it ('Given below are two statements ... choose the correct answer'); `two_part` is reserved here for the respectively-type stems that ask for several answers at once. On the trap axis I applied the nearby_fact / look_alike_term test from section 5.1: replacing 'narcotic' and 'non-narcotic' with two unlike class names leaves the trap standing, because what carries the student is which drug the book files under which heading, printed one after the other, so position does the work. I also considered `half_right`, since option 1 is a two-part verdict whose Statement II half is right, but that label would attach to every statement-pair question and would hide the actual pull, which is the swapped class list.
<!--/ecat-->

## Q75

Chemistry · physical · Thermodynamics

Which one among the following is the correct option for right relationship between $C_P$ and $C_V$ for one mole of ideal gas?

- (1) $C_P = RC_V$
- (2) $C_V = RC_P$
- (3) $C_P + C_V = R$
- **(4)** $C_P - C_V = R$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $C_p = C_v + R$

**Solved independently** (answer withheld)

1. For one mole of an ideal gas, Mayer's relation gives $C_P - C_V = R$, which is option $4$.

**Subtopic:** Heat Capacity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q075_4f6dbf0d_30102026.png?v=4f6dbf0db136)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q075_d24c50d3_30102026.png?v=d24c50d3143f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** For one mole of an ideal gas the molar heat capacities differ by the gas constant, $C_P - C_V = R$, because heating at constant pressure also does expansion work
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who remembers the shape of the relation, two heat capacities on one side and $R$ alone on the other, but not which operator joins them, writes the sum instead of the difference.
- **Why:** This question requires the stated relation between the two molar heat capacities, demonstrated by the stem asking for "right relationship between $C_P$ and $C_V$ for one mole of ideal gas" and by the four options being rival algebraic forms with no numbers to work.
- **Note:** This one is a recalled relation rather than a computation, so `asks` is `fact_line` and not `calculate`: nothing in the stem is a quantity to put into the relation.
<!--/ecat-->

## Q76

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

The maximum temperature that can be achieved in blast furnace is:

- (1) Upto $1900\,\mathrm{K}$
- (2) Upto $5000\,\mathrm{K}$
- (3) Upto $1200\,\mathrm{K}$
- **(4)** Upto $2200\,\mathrm{K}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In the Blast furnace, reduction of iron oxides takes place in different temperature ranges.
2. Hot air is blown from the bottom of the furnace and coke is burnt to give temperature upto about $2200\,\mathrm{K}$ in the lower portion itself

**Solved independently** (answer withheld)

1. In the NCERT blast furnace, the temperature rises from about $500\,\mathrm{K}$ at the top to about $2170\,\mathrm{K} \approx 2200\,\mathrm{K}$ in the combustion zone near the tuyeres ($\mathrm{C} + \mathrm{O_2} \rightarrow \mathrm{CO_2}$), so the maximum is up to $2200\,\mathrm{K}$, which is option $4$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q076_36953299_30102026.png?v=3695329950f4)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q076_f8272159_30102026.png?v=f82721593a34)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The blast furnace runs hottest at its base, up to about 2200 K, which is why the zone reactions are described band by band up the shaft
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The blast-furnace passage prints its zone temperatures as bands running from a few hundred to about 1500 K, and 1200 K sits inside one of them, so a student recalling a temperature from that passage recalls a zone figure rather than the maximum at the base.
- **Why:** This question requires a stored number about a named industrial process, demonstrated by the stem "The maximum temperature that can be achieved in blast furnace is:" and by four bare temperatures as options with nothing in the stem to compute from.
<!--/ecat-->

## Q77

Chemistry · physical · Chemical Kinetics

For a reaction $\mathrm{A \rightarrow B}$, enthalpy of reaction is $-4.2\,\mathrm{kJ\,mol^{-1}}$ and enthalpy of activation is $9.6\,\mathrm{kJ\,mol^{-1}}$. The correct potential energy profile for the reaction is shown in option.

- (1) ![printed figure: (a) potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a single high peak and falls to B at about the same level as A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q077_option_1_13494fac_30102026.png?v=13494fac01f9) *(a) potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a single high peak and falls to B at about the same level as A*
- (2) ![printed figure: (b) potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies well above A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q077_option_2_e21c7c0b_30102026.png?v=e21c7c0bfb62) *(b) potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies well above A*
- (3) ![printed figure: (c) potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies slightly above A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q077_option_3_b887d9bb_30102026.png?v=b887d9bb1978) *(c) potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies slightly above A*
- **(4)** ![printed figure: potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies below A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q077_option_4_61dfd0f3_30102026.png?v=61dfd0f30c21) *potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies below A*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Since the enthalpy of reaction is negative, it means product has lesser potential energy than the reactant.
2. Thus, the correct graph would be (D)

![printed figure: potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies below A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q077_sol_1_7d9a9067_30102026.png?v=7d9a90679623)

*potential energy profile: PE (↑) vs Reaction Progress; curve rises from A over a peak and falls to B, which lies below A*


**Solved independently** (answer withheld)

1. $\Delta H = E_B - E_A = -4.2\,\mathrm{kJ\,mol^{-1}} < 0$, so the reaction is exothermic and $B$ must lie below $A$.
2. $E_a = E_{TS} - E_A = 9.6\,\mathrm{kJ\,mol^{-1}}$, so the peak lies $9.6$ above $A$.
3. $\frac{E_a}{|\Delta H|} = \frac{9.6}{4.2} \approx 2.3$, so the barrier height is about twice the drop from $A$ to $B$.
4. Profiles $2$ and $3$ show $B$ above $A$ (endothermic), so they are rejected.
5. Profile $1$ shows $B$ nearly level with $A$ under a very tall peak, so $E_a/|\Delta H| \gg 2.3$; rejected.
6. Profile $4$ shows $B$ clearly below $A$ with the peak about twice that drop above $A$, which is option $4$.

**Subtopic:** Activation Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q077_c34c0ac9_30102026.png?v=c34c0ac98fab)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q077_7017f7dc_30102026.png?v=7017f7dca55e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A potential-energy profile must show the barrier measured from the reactant level, here 9.6 kJ/mol up, and the product level below the reactant level because the reaction gives out 4.2 kJ/mol
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are energy-profile diagrams and every option arrives as an empty string, so no drawn curve was supplied to this step and no route to a wrong curve can be named
- **Why:** This question requires matching two given energies to a drawn energy profile, demonstrated by the stem "enthalpy of reaction is $-4.2\,\mathrm{kJ\,mol^{-1}}$ and enthalpy of activation is $9.6\,\mathrm{kJ\,mol^{-1}}$. The correct potential energy profile for the reaction is shown in option."
- **Note:** Options 1-4 are empty strings and `figure_image` is null, so the option diagrams never reached this step; the paper itself is not in doubt, so this is recorded as no_trap rather than source damage. A reviewer holding the printed options should check the two devices this stem invites: a profile drawn uphill overall, which reads the minus sign off $\Delta H$, and a barrier of 9.6 drawn from the product side instead of the reactant side.
<!--/ecat-->

## Q78

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Which one of the following methods can be used to obtain highly pure metal which is liquid at room temperature?

- **(1)** Distillation
- (2) Zone refining
- (3) Electrolysis
- (4) Chromatography

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Distillation:
2. This is very useful for low boiling metals like zinc and mercury. The impure metal is evaporated to obtain the pure metal as distillate.
3. NCERT line: Metallurgy

**Solved independently** (answer withheld)

1. The metal that is liquid at room temperature is mercury, $\mathrm{Hg}$, and it has a low boiling point.
2. NCERT refines low-boiling metals such as $\mathrm{Zn}$ and $\mathrm{Hg}$ by distillation: the metal vaporises and leaves the impurities behind, so the answer is option $1$.

**Subtopic:** Refining of Metals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q078_5a261200_30102026.png?v=5a26120016c9)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q078_12ee3bcc_30102026.png?v=12ee3bcc2636)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Distillation is the refining method for low-boiling metals such as mercury and zinc, which are volatile enough to be vaporised away from their non-volatile impurities
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Zone refining is the method the chapter ties to the words 'very pure', so a student who answers from the stem's phrase "highly pure metal" and drops the other printed condition, "liquid at room temperature", picks it.
- **Why:** This question requires the stated refining method for a named kind of metal, demonstrated by the stem "Which one of the following methods can be used to obtain highly pure metal which is liquid at room temperature?" with four named methods as options.
<!--/ecat-->

## Q79

Chemistry · organic · Biomolecules

The RBC deficiency is deficiency disease of

- (1) Vitamin $\mathrm{B_{1}}$
- (2) Vitamin $\mathrm{B_{2}}$
- **(3)** Vitamin $\mathrm{B_{12}}$
- (4) Vitamin $\mathrm{B_{6}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Vitamin $\mathrm{B_{12}}$ : Deficiency disease - Pernicious anaemia (RBC deficient in haemoglobin)
2. NCERT Table 14.3 - Biomolecules

**Solved independently** (answer withheld)

1. RBC deficiency (pernicious/megaloblastic anaemia) results from lack of Vitamin $\mathrm{B_{12}}$, which is option $3$.

**Subtopic:** Vitamins Classification and Uses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q079_e1505401_30102026.png?v=e15054012cd6)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q079_c00519ce_30102026.png?v=c00519ce05c6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Vitamin B12, cobalamin, is the vitamin whose deficiency stops red blood cells maturing and so causes pernicious anaemia
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The label $\mathrm{B_{12}}$ is the label $\mathrm{B_1}$ with one digit added, so a student who stored the answer as 'vitamin B-one-something' reads the shorter label as the one they remember.
- **Why:** This question requires one row of the vitamin-and-deficiency table, demonstrated by the stem "The RBC deficiency is deficiency disease of" and by the four options being four labels from the same B series.
- **Note:** Applied the swap test on the trap axis: replace the four labels with thiamine, riboflavin, pyridoxine and cobalamin and the pull on option 1 dies, because nothing about 'thiamine' resembles 'cobalamin'. The resemblance of the bare labels is doing the work, so `look_alike_term` rather than `nearby_fact`. Separately, the stem's wording ("The RBC deficiency is deficiency disease of") is awkward as printed; tagged as printed.
<!--/ecat-->

## Q80

Chemistry · organic · Hydrocarbons

The major product of the following chemical reaction is: $\mathrm{(CH_3)_2CH{-}CH{=}CH_2 + HBr \xrightarrow{(C_6H_5CO)_2O_2} ?}$

![printed figure: 3-methylbut-1-ene + $\ce{HBr}$ →($\ce{(C6H5CO)2O2}$) ?](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q080_4fd7d8d1_30102026.png?v=4fd7d8d13dce)

*3-methylbut-1-ene + $\ce{HBr}$ →[$\ce{(C6H5CO)2O2}$] ?*

![drawn: 3-methylbut-1-ene + $\ce{HBr}$ →($\ce{(C6H5CO)2O2}$) ?](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_question_6321fce8_02112026.svg?v=6321fce8c83e)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 3-methylbut-1-ene `C=CC(C)C` ![3-methylbut-1-ene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_question_s1_d4ad795a_02112026.svg?v=d4ad795aeeb9); hydrogen bromide `Br` ![hydrogen bromide](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_question_s2_e3c4ea0a_02112026.svg?v=e3c4ea0a0a12)

- (1) 2-bromo-3-methylbutane `CC(C)C(C)Br` ![2-bromo-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_option_1_s1_18faa9fe_02112026.svg?v=18faa9fe6ac0) — $\mathrm{(CH_3)_2CH{-}CH(Br){-}CH_3}$
- (2) 2-bromo-2-methylbutane `CCC(C)(C)Br` ![2-bromo-2-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_option_2_s1_c5380da6_02112026.svg?v=c5380da663c8) — $\mathrm{(CH_3)_2CBr{-}CH_2{-}CH_3}$
- **(3)** 1-bromo-3-methylbutane `CC(C)CCBr` ![1-bromo-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_option_3_s1_341b975d_02112026.svg?v=341b975d31b1) — $\mathrm{(CH_3)_2CH{-}CH_2{-}CH_2{-}Br}$
- (4) 3-methylbutyl benzoate `CC(C)CCOC(=O)c1ccccc1` ![3-methylbutyl benzoate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_option_4_s1_fee2c4d9_02112026.svg?v=fee2c4d9f121) — $\mathrm{(CH_3)_2CH{-}CH_2{-}CH_2{-}O{-}COC_6H_5}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In the presence of peroxide anti markovnikov addition of $\mathrm{HBr}$ take place.

![printed figure: 3-methylbut-1-ene + $\ce{HBr}$ →($\ce{(C6H5CO)2O2}$) 1-bromo-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q080_sol_1_cc34a01c_30102026.png?v=cc34a01c2038)

*3-methylbut-1-ene + $\ce{HBr}$ →[$\ce{(C6H5CO)2O2}$] 1-bromo-3-methylbutane*

![drawn: 3-methylbut-1-ene + $\ce{HBr}$ →($\ce{(C6H5CO)2O2}$) 1-bromo-3-methylbutane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q080_solution_1_0909f875_02112026.svg?v=0909f8752746)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Benzoyl peroxide $\mathrm{(C_6H_5CO)_2O_2}$ starts a free-radical chain: $\mathrm{C_6H_5\dot{}} + \mathrm{HBr} \rightarrow \mathrm{C_6H_6} + \mathrm{Br^{\bullet}}$ (peroxide/Kharasch effect).
2. $\mathrm{Br^{\bullet}}$ adds to the terminal $\mathrm{CH_2}$ to give the more stable secondary radical $\mathrm{(CH_3)_2CH{-}\dot{C}H{-}CH_2Br}$.
3. This radical takes H from HBr: $\mathrm{(CH_3)_2CH{-}CH_2{-}CH_2Br}$ (anti-Markovnikov product), which is option $3$.

**Subtopic:** Chemical Properties of Alkenes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q080_b574f3a3_30102026.png?v=b574f3a3af8a)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q080_d6ef8fd7_30102026.png?v=d6ef8fd7c243)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** HBr adds to an alkene through a bromine radical when a peroxide is present, so the bromine ends up on the less substituted carbon, the reverse of Markovnikov addition
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Markovnikov's rule puts the bromine on the more substituted carbon of the double bond, which is exactly option 1; the peroxide written over the arrow is the condition that reverses the rule, and the option is what you get by not using it.
- **Why:** This question requires the product of a named reagent on a named substrate under the printed condition, demonstrated by the arrow in the stem carrying $\mathrm{(C_6H_5CO)_2O_2}$ over it and the question "The major product of the following chemical reaction is".
<!--/ecat-->

## Q81

Chemistry · physical · The Solid State

Right option for the number of tetrahedral and octahedral voids in hexagonal primitive unit cell are

- (1) 2, 1
- **(2)** 12, 6
- (3) 8, 4
- (4) 6, 12

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. HCP has effectively $6$ atoms per unit cell. Now,
2. Number of tetrahedral voids $= 2n = 12$
3. Number of octahedral voids $= n = 6$

**Solved independently** (answer withheld)

1. Atoms in the hexagonal unit cell: $N = 12 \times \frac{1}{6} + 2 \times \frac{1}{2} + 3 = 6$.
2. Tetrahedral voids $= 2N = 2 \times 6 = 12$.
3. Octahedral voids $= N = 6$.
4. So the pair is $12, 6$, which is option $2$.

**Subtopic:** Close Packing, Tetrahedral and Octahedral Voids and Formula of Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 37)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q081_ec013c64_30102026.png?v=ec013c64719a)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q081_ff5a59ee_30102026.png?v=ff5a59ee875e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a close-packed structure the octahedral voids equal the number of atoms in the cell and the tetrahedral voids are twice that, so the six-atom hexagonal cell holds 12 and 6
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  8 and 4 are the true void counts for the cubic close-packed cell, which has 4 atoms; a student who applies the right rule to the cell they practised rather than to the hexagonal one printed in the stem lands exactly there.
- **Why:** This question requires two counts produced from a stored rule and the atom content of a named cell, demonstrated by the stem "the number of tetrahedral and octahedral voids in hexagonal primitive unit cell" and by every option being a pair of integers.
<!--/ecat-->

## Q82

Chemistry · inorganic · The p–Block Elements

Noble gases are named because of their inertness towards reactivity. Identify an incorrect statement about them.

- (1) Noble gases have weak dispersion forces
- (2) Noble gases have large positive values of electron gain enthalpy
- (3) Noble gases are sparingly soluble in water
- **(4)** Noble gases have very high melting and boiling points

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. They have very low melting and boiling points because the only type of interatomic interaction in these elements is weak dispersion forces.

**Solved independently** (answer withheld)

1. Noble gases are monoatomic with only weak London dispersion forces between atoms, so statement 1 is correct.
2. Their stable $ns^2np^6$ configuration makes electron gain enthalpy large and positive, so statement 2 is correct.
3. They are only sparingly soluble in water, so statement 3 is correct.
4. Weak interatomic forces give very low, not very high, melting and boiling points, so statement 4 is incorrect: option $4$.

**Subtopic:** General Properties & Trends of Group 18 (Noble Gases) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q082_2fdd5070_30102026.png?v=2fdd50707ae0)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q082_1c75309c_30102026.png?v=1c75309cee44)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Noble gases are monoatomic and held together only by weak dispersion forces, which is why their melting and boiling points are the lowest in their periods
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The stem's opening sentence hands the student the inertness premise, and weak dispersion forces are the printed statement of that premise, so answering the question the stem resembles, which statement is right, lands on the line the student can vouch for.
- **Why:** This question requires four stated properties of one group to be graded true or false, demonstrated by the stem "Identify an incorrect statement about them" with each option a full claim about noble gases.
- **Note:** `qtype` is `statements` because the stem itself instructs the student to judge statements, even though no lettered block is printed; E1 called this `statement_options`, which maps onto the same reading.
<!--/ecat-->

## Q83

Chemistry · organic · Haloalkanes and Haloarenes

The major product formed in dehydrohalogenation reaction of 2-Bromopentane is pent-2-ene. This product formation is based on?

- (1) Hofmann Rule
- (2) Huckel's Rule
- **(3)** Saytzeff’s Rule
- (4) Hund’s Rule

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: 2-bromopentane →(Alc. KOH, Δ) pent-1-ene + pent-2-ene (Major)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q083_sol_1_1fd9a4e8_30102026.png?v=1fd9a4e8a581)

*2-bromopentane →[Alc. KOH, Δ] pent-1-ene + pent-2-ene (Major)*

![drawn: 2-bromopentane →(Alc. KOH, Δ) pent-1-ene + pent-2-ene (Major)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q083_solution_1_a0fc2a9b_02112026.svg?v=a0fc2a9b0ba0)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. Saytzeff’s rule

**Solved independently** (answer withheld)

1. Dehydrohalogenation of 2-bromopentane can give pent-1-ene or pent-2-ene; the more substituted alkene, pent-2-ene, is the major product, as Saytzeff's rule predicts (option $3$).

**Subtopic:** Reactions of Haloalkanes – Elimination Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 38)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q083_44a8aea4_30102026.png?v=44a8aea4855b)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q083_767a97b5_30102026.png?v=767a97b57a54)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Saytzeff's rule is the one that names the more substituted alkene as the major elimination product, which is why 2-bromopentane gives pent-2-ene and not pent-1-ene
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Hofmann's rule is printed as the counterpart of Saytzeff's in the same elimination discussion, naming the less substituted alkene, so a student who knows the pair exists but not which way round each runs takes the other name.
- **Why:** This question requires the name of the rule that accounts for a stated outcome, demonstrated by the stem "The major product formed in dehydrohalogenation reaction of 2-Bromopentane is pent-2-ene. This product formation is based on?" with four named rules as options.
<!--/ecat-->

## Q84

Chemistry · organic · Amines

Identify the compound that will react with HInsberg’s reagent to give a solid which dissolves in alkali.

- **(1)** ethanamine `CCN` ![ethanamine](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q084_option_1_s1_a2fc910e_02112026.svg?v=a2fc910e0991) — $\mathrm{CH_3CH_2\ddot{N}H_2}$
- (2) N-ethyl-N-methylethanamine `CCN(C)CC` ![N-ethyl-N-methylethanamine](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q084_option_2_s1_d3214b17_02112026.svg?v=d3214b17f89a) — $\mathrm{CH_3CH_2\ddot{N}(CH_3)CH_2CH_3}$
- (3) nitroethane `CC[N+](=O)[O-]` ![nitroethane](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q084_option_3_s1_a5496a03_02112026.svg?v=a5496a0362f5) — $\mathrm{CH_3CH_2\ddot{N}O_2}$
- (4) N-methylethanamine `CCNC` ![N-methylethanamine](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q084_option_4_s1_02b944d7_02112026.svg?v=02b944d75990) — $\mathrm{CH_3CH_2\ddot{N}HCH_3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Primary amine on reaction with Hinsberg's reagent give a solid which dissolves in alkali.

![printed figure: ethanamine (Primary amine) + benzenesulfonyl chloride (Benzenesulfonyl chloride) →(− HCl) N-ethylbenzenesulfonamide (N-Alkylbenzenesulfonamide (Soluble in aqueous NaOH)) →(NaOH, − H₂O) sodium N-ethylbenzenesulfonamide (Sulfonamide salt of sodium)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q084_sol_1_e7070c3a_30102026.png?v=e7070c3a5ae6)

*ethanamine (Primary amine) + benzenesulfonyl chloride (Benzenesulfonyl chloride) →[− HCl] N-ethylbenzenesulfonamide (N-Alkylbenzenesulfonamide (Soluble in aqueous NaOH)) →[NaOH, − H₂O] sodium N-ethylbenzenesulfonamide (Sulfonamide salt of sodium)*

![drawn: ethanamine (Primary amine) + benzenesulfonyl chloride (Benzenesulfonyl chloride) →(− HCl) N-ethylbenzenesulfonamide (N-Alkylbenzenesulfonamide (Soluble in aqueous NaOH)) →(NaOH, − H₂O) sodium N-ethylbenzenesulfonamide (Sulfonamide salt of sodium)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q084_solution_1_77aeb802_02112026.svg?v=77aeb8020eb4)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Hinsberg's reagent is benzenesulfonyl chloride, $\mathrm{C_6H_5SO_2Cl}$.
2. A primary amine reacts: $\mathrm{C_2H_5NH_2 + C_6H_5SO_2Cl \rightarrow C_6H_5SO_2NHC_2H_5}$. The H on N is acidic because of the strongly electron-withdrawing sulfonyl group, so this solid dissolves in alkali.
3. The secondary amine $\mathrm{C_2H_5NHCH_3}$ forms $\mathrm{C_6H_5SO_2N(CH_3)C_2H_5}$, which has no H on N, so it does not dissolve in alkali.
4. The tertiary amine does not react, and the nitro compound is not an amine, so the answer is option $1$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q084_f238c103_30102026.png?v=f238c103923a)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q084_30040c4c_30102026.png?v=30040c4cc695)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hinsberg's reagent turns a primary amine into an N-monosubstituted sulphonamide whose remaining N-H is acidic, so that solid dissolves in alkali while the secondary amine's disubstituted product does not
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The Hinsberg test is set out as three cases in a row, and the secondary amine is the case printed beside the primary one; a student who has stored 'primary and secondary both give a solid' takes the neighbouring case and never gets to the alkali half of the stem.
- **Why:** This question requires which substrate a named reagent converts into a product with a stated property, demonstrated by the stem "Identify the compound that will react with HInsberg's reagent to give a solid which dissolves in alkali".
<!--/ecat-->

## Q85

Chemistry · physical · Solutions

The following solutions were prepared by dissolving $10\,\mathrm{g}$ glucose ($\mathrm{C_6H_{12}O_6}$) in $250\,\mathrm{ml}$ of water ($P_1$) $10\,\mathrm{g}$ of urea ($\mathrm{CH_4N_2O}$) in $250\,\mathrm{ml}$ of water ($P_2$) and $10\,\mathrm{g}$ of sucrose ($\mathrm{C_{12}H_{12}O_{11}}$) in $250\,\mathrm{ml}$ of water ($P_3$). The right option for the decreasing order of osmotic pressure of these solutions is.

- (1) $P_2 > P_3 > P_1$
- (2) $P_3 > P_1 > P_2$
- **(3)** $P_2 > P_1 > P_3$
- (4) $P_1 > P_2 > P_3$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\Pi = \frac{wRT}{MV}$
2. Here, all the given solutions have the same volume and mass of solute. Thus, the osmotic pressure will decrease with increase in molar mass of solute.
3. Thus, the order should be: $P_2 > P_1 > P_3$

**Solved independently** (answer withheld)

1. All three are non-electrolytes, so $\pi = \frac{n}{V}RT$ with the same $V$ and $T$; hence $\pi \propto n = \frac{10}{M}$.
2. $n_{\text{urea}} = \frac{10}{60} \approx 0.167\,\mathrm{mol}$.
3. $n_{\text{glucose}} = \frac{10}{180} \approx 0.0556\,\mathrm{mol}$.
4. $n_{\text{sucrose}} = \frac{10}{342} \approx 0.0292\,\mathrm{mol}$.
5. $n_{\text{urea}} > n_{\text{glucose}} > n_{\text{sucrose}} \Rightarrow P_2 > P_1 > P_3$, which is option $3$.

**Subtopic:** Osmosis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q085_e3b91345_30102026.png?v=e3b91345c524)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q085_6317ff9f_30102026.png?v=6317ff9f418c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Osmotic pressure follows the number of dissolved particles, so for equal masses in equal volumes it runs inversely with molar mass: urea beats glucose beats sucrose
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Ranking the three solutions by the size of the solute, sucrose then glucose then urea, produces $P_3 > P_1 > P_2$, which is the key read backwards; for equal masses the molar mass enters as $1/M$, so the heaviest solute gives the fewest particles and the least pressure.
- **Why:** This question requires three solutions ranked on a colligative property, demonstrated by the stem "The right option for the decreasing order of osmotic pressure of these solutions is" and by every option being a chain of inequalities in $P_1$, $P_2$, $P_3$.
- **Note:** The stem prints sucrose as $\mathrm{C_{12}H_{12}O_{11}}$, which is one hydrogen count short of sucrose ($\mathrm{C_{12}H_{22}O_{11}}$); as printed it still has by far the largest molar mass of the three, so the key is unaffected. Tagged as printed.
<!--/ecat-->

## Q86

Chemistry · inorganic · Environmental Chemistry

Match List - I with List – II
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{2SO_2(g) + O_2(g) \longrightarrow 2SO_3(g)}$ | (i) | Acid rain |
| (b) | $\mathrm{HOCl(g) \xrightarrow{hv} \dot{O}H + \dot{C}l}$ | (ii) | Smog |
| (c) | $\mathrm{CaCO_3 + H_2SO_4 \longrightarrow CaSO_4 + H_2O + CO_2}$ | (iii) | Ozone depletion |
| (d) | $\mathrm{NO_2(g) \xrightarrow{hv} NO(g) + O(g)}$ | (iv) | Tropospheric pollution |

- **(1)** (a)-(iv), (b)-(iii), (c)-(i), (d)-(ii)
- (2) (a)-(iii), (b)-(ii), (c)-(iv), (d)-(i)
- (3) (a)-(i), (b)-(ii), (c)-(iii), (d)-(iv)
- (4) (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (c) represents effect of acid rain on marble.

**Solved independently** (answer withheld)

1. $\mathrm{2SO_2 + O_2 \rightarrow 2SO_3}$ is oxidation of a gaseous pollutant in the lower atmosphere, so (a) matches (iv) tropospheric pollution.
2. $\mathrm{HOCl \xrightarrow{h\nu} \dot{O}H + \dot{C}l}$ releases chlorine radicals in the stratosphere, so (b) matches (iii) ozone depletion.
3. $\mathrm{CaCO_3 + H_2SO_4 \rightarrow CaSO_4 + H_2O + CO_2}$ is acid corroding marble, so (c) matches (i) acid rain.
4. $\mathrm{NO_2 \xrightarrow{h\nu} NO + O}$ is the first step of photochemical smog, so (d) matches (ii) smog.
5. The set a-(iv), b-(iii), c-(i), d-(ii) is option $1$.

**Subtopic:** Air Pollution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q086_10ad8456_30102026.png?v=10ad845618cc)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q086_d995326e_30102026.png?v=d995326e8606)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each printed equation belongs to one named air-pollution phenomenon: chlorine radicals from photolysis deplete ozone, NO2 photolysis starts photochemical smog, sulphuric acid eating marble is acid rain, and SO2 oxidising in air is tropospheric pollution
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  SO2 oxidising to SO3 is the first step on the way to sulphuric acid, so a student reading row (a) pairs it with acid rain, and only one code does that. The acid-rain entry in this list is the reaction acid rain performs on marble, which then has nowhere left to go.
- **Why:** This question requires knowing which phenomenon each equation is printed under, demonstrated by List-II holding 'Acid rain' once while two of the four equations belong to acid-rain chemistry, so the one that is acid rain's effect takes the slot.
<!--/ecat-->

## Q87

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The intermediate compound “X” in the following chemical reaction is

![printed figure: toluene + $\ce{CrO2Cl2}$ →($\ce{CS2}$) X →($\ce{H3O+}$) benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q087_a1994de1_30102026.png?v=a1994de117da)

*toluene + $\ce{CrO2Cl2}$ →[$\ce{CS2}$] X →[$\ce{H3O+}$] benzaldehyde*

![drawn: toluene + $\ce{CrO2Cl2}$ →($\ce{CS2}$) X →($\ce{H3O+}$) benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_question_a90f2c61_02112026.svg?v=a90f2c618c55)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: toluene `Cc1ccccc1` ![toluene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_question_s1_b4bc3ebf_02112026.svg?v=b4bc3ebff656); chromyl chloride `[O]=[Cr](=[O])([Cl])[Cl]` ![chromyl chloride](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_question_s2_853137d1_02112026.svg?v=853137d16297); benzaldehyde `O=Cc1ccccc1` ![benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_question_s3_013e4894_02112026.svg?v=013e489470a6)

- (1) (dichloromethyl)benzene `ClC(Cl)c1ccccc1` ![(dichloromethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_option_1_s1_0e8700f9_02112026.svg?v=0e8700f9926c)
- (2) (chloromethyl)benzene `ClCc1ccccc1` ![(chloromethyl)benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_option_2_s1_d67637a1_02112026.svg?v=d67637a1836b)
- **(3)** phenylmethylene bis(hydroxydichlorochromium) ether (chromium complex) `[OH][Cr]([Cl])([Cl])[O]C([O][Cr]([OH])([Cl])[Cl])c1ccccc1` ![phenylmethylene bis(hydroxydichlorochromium) ether (chromium complex)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_option_3_s1_f1e1217a_02112026.svg?v=f1e1217a5456)
- (4) [(acetyloxy)(phenyl)methyl] acetate `CC(=O)OC(OC(C)=O)c1ccccc1` ![((acetyloxy)(phenyl)methyl) acetate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_option_4_s1_63a8dc9d_02112026.svg?v=63a8dc9dde4f)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Toluene + $\ce{CrO2Cl2}$ →($\ce{CS2}$) Chromium complex ($\ce{C6H5CH(OCrOHCl2)2}$) →($\ce{H3O+}$) Benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q087_sol_1_078ae38c_30102026.png?v=078ae38c3326)

*Toluene + $\ce{CrO2Cl2}$ →[$\ce{CS2}$] Chromium complex ($\ce{C6H5CH(OCrOHCl2)2}$) →[$\ce{H3O+}$] Benzaldehyde*

![drawn: Toluene + $\ce{CrO2Cl2}$ →($\ce{CS2}$) Chromium complex ($\ce{C6H5CH(OCrOHCl2)2}$) →($\ce{H3O+}$) Benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q087_solution_1_4a43e937_02112026.svg?v=4a43e93765b6)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. The reaction of toluene with $\mathrm{CrO_2Cl_2}$ in $\mathrm{CS_2}$ followed by $\mathrm{H_3O^+}$ is the Etard reaction, and it gives benzaldehyde.
2. The intermediate X is the chromium complex $\mathrm{C_6H_5CH(OCrOHCl_2)_2}$, which is hydrolysed to $\mathrm{C_6H_5CHO}$. This is option $3$.

**Subtopic:** Preparation of Benzaldehyde · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 39)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q087_b192d034_30102026.png?v=b192d034950b)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q087_93244ef9_30102026.png?v=93244ef9b134)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Chromyl chloride attacks the methyl group of toluene to give a chromium complex of the side chain, and only hydrolysis of that complex releases benzaldehyde
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four options are drawn structures and each arrives as an empty string, so no option content was supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires the intermediate of a two-step scheme with a named reagent, demonstrated by the stem "The intermediate compound 'X' in the following chemical reaction is" with $\mathrm{CrO_2Cl_2/CS_2}$ over the first arrow and $\mathrm{H_3O^{+}}$ over the second.
- **Note:** Options 1-4 are empty strings; the stem's scheme was captured but the option structures were not supplied to this step, so no trap can be audited, and the paper itself is not in doubt. A reviewer holding the printed options should check for benzaldehyde itself offered as the intermediate, which is the hydrolysis product and so answers the step after the one asked, and for attack moved onto the ring (benzyl chloride or a chlorotoluene) instead of the methyl side chain, which would be `wrong_site_attacked`.
<!--/ecat-->

## Q88

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Match List - I with List - II
Choose the correct answer form the options given below.

![printed figure: (a) benzene →(CO, HCl / Anhy. $\ce{AlCl2}$/CuCl)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q088_a5ef04ee_30102026.png?v=a5ef04ee6d5a)

*(a) benzene →[CO, HCl / Anhy. $\ce{AlCl2}$/CuCl]*

![drawn: (a) benzene →(CO, HCl / Anhy. $\ce{AlCl2}$/CuCl)](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q088_question_f74a45b7_02112026.svg?v=f74a45b7664f)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: benzene `c1ccccc1` ![benzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q088_question_s1_dbf27a87_02112026.svg?v=dbf27a872e50)

| List-I | | List-II | |
|---|---|---|---|
| (a) | [benzene ring structure, see figure] $\xrightarrow[\mathrm{Anhy.AlCl_2/CuCl}]{\mathrm{CO,HCl}}$ CO, HCl Anhy. $\mathrm{AlCl_3/CuCl}$ | (i) | Hell-Volhard-Zelinsky reaction |
| (b) | $\mathrm{R-\overset{O}{\overset{\\|}{C}}-CH_3 + NaOX \longrightarrow}$ | (ii) | Gattermann-Koch |
| (c) | $\mathrm{R-CH_2-OH + R'COOH \xrightarrow{Conc.H_2SO_4}}$ | (iii) | Haloform reaction |
| (d) | $\mathrm{R-CH_2COOH \xrightarrow[(ii)H_2O]{(i)X_2/Red\ P}}$ | (iv) | Esterification |

- (1) (a)-(i), (b)-(iv), (c)-(iii), (d)-(ii)
- **(2)** (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i)
- (3) (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)
- (4) (a)-(iii), (b)-(ii), (c)-(i), (d)-(iv)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: benzene →(CO, HCl / Anhyd. $\ce{AlCl3}$/CuCl) benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q088_sol_1_79711828_30102026.png?v=797118281a27)

*benzene →[CO, HCl / Anhyd. $\ce{AlCl3}$/CuCl] benzaldehyde*

![drawn: benzene →(CO, HCl / Anhyd. $\ce{AlCl3}$/CuCl) benzaldehyde](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q088_solution_1_0d6fa77c_02112026.svg?v=0d6fa77c5d60)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. (ii) Gattermann-Koch reaction
2. (b) $\mathrm{R-\overset{O}{\overset{\|}{C}}-CH_3 + \xrightarrow{NaOX} R-\overset{O}{\overset{\|}{C}}-\overset{\ominus}{O} + CHX_3}$ (iii) Haloform reaction
3. (C) $\mathrm{R-CH_2-OH + R'COOH \xrightarrow{Conc.\ H_2SO_4} R-CH_2-O-\underset{\underset{O}{\|}}{C}-R' + H_2O}$ (iv) Esterification
4. (d) $\mathrm{R-CH_2COOH \xrightarrow[(ii)\ H_2O]{(i)\ X_2/Red\ P} R-\underset{\underset{X}{|}}{CH}-COOH}$ (i) Hell-Volhard-Zelinsky reaction

**Solved independently** (answer withheld)

1. (a) Benzene $\xrightarrow{\mathrm{CO,\ HCl,\ anhyd.\ AlCl_3/CuCl}}$ benzaldehyde is the Gattermann-Koch reaction, so (a)-(ii).
2. (b) A methyl ketone $\mathrm{R-CO-CH_3}$ with $\mathrm{NaOX}$ gives $\mathrm{CHX_3}$: the haloform reaction, so (b)-(iii).
3. (c) $\mathrm{RCH_2OH + R'COOH \xrightarrow{conc.\ H_2SO_4} R'COOCH_2R}$ is esterification, so (c)-(iv).
4. (d) $\mathrm{RCH_2COOH \xrightarrow{(i)\ X_2/red\ P,\ (ii)\ H_2O} RCHXCOOH}$ is the Hell-Volhard-Zelinsky reaction, so (d)-(i).
5. The match (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i) is option $2$.

**Subtopic:** Named Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 40)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q088_28be15c1_30102026.png?v=28be15c15012)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q088_7e8d45e2_30102026.png?v=7e8d45e21976)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Each reagent set names its own reaction: CO with HCl over AlCl3/CuCl formylates benzene (Gattermann-Koch), a methyl ketone with NaOX gives the haloform, an alcohol with an acid and conc. H2SO4 esterifies, and X2 with red phosphorus halogenates the alpha carbon of an acid (Hell-Volhard-Zelinsky)
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked all three wrong codes: they are the three cyclic rotations of the key and share no pair with it, so each needs all four reagent sets misread at once. Any single row a student can place strikes all three out, since the esterification pair appears only in the key. The one confusion the reagents do invite, the two halogen reactions (b) with NaOX and (d) with X2/red P, is offered in no code by itself: the only option carrying that swap also puts esterification on the benzene row and Gattermann-Koch on the alcohol row, which no reading of those reagents supports.
- **Why:** This question requires matching each reagent set to its named reaction, demonstrated by List-II holding only reaction names such as 'Hell-Volhard-Zelinsky reaction' while each row of List-I prints the reagents that define one of them.
- **Note:** This is a no_trap finding, not an unexamined question: the four options are the four cyclic rotations of one mapping, so no wrong code holds a single correct pair and none is reached by a nameable misreading. The figure for row (a) was not opened at this step; the transcribed text and the extraction note together give benzene with CO, HCl and anhydrous AlCl3/CuCl, which is enough to place the row. The extraction note records that the booklet itself prints 'AlCl2' under the arrow, apparently a misprint for AlCl3; the question is tagged as printed and the misprint is not treated as part of any trap.
<!--/ecat-->

## Q89

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

The product formed in the following chemical reaction is

![printed figure: methyl 2-(2-methyl-6-oxocyclohexyl)acetate →(NaBH₄ / C₂H₅OH) ?](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q089_7cffc6e4_30102026.png?v=7cffc6e4c6aa)

*methyl 2-(2-methyl-6-oxocyclohexyl)acetate →[NaBH₄ / C₂H₅OH] ?*

![drawn: methyl 2-(2-methyl-6-oxocyclohexyl)acetate →(NaBH₄ / C₂H₅OH) ?](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_question_60f0138b_02112026.svg?v=60f0138b2900)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: methyl 2-(2-methyl-6-oxocyclohexyl)acetate `COC(=O)CC1C(=O)CCCC1C` ![methyl 2-(2-methyl-6-oxocyclohexyl)acetate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_question_s1_8fdb97d4_02112026.svg?v=8fdb97d4fc08)

- (1) 2-(2-hydroxypropyl)-3-methylcyclohexan-1-ol `CC(O)CC1C(C)CCCC1O` ![2-(2-hydroxypropyl)-3-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_option_1_s1_bf879dcc_02112026.svg?v=bf879dcccfd5)
- **(2)** methyl 2-(2-hydroxy-6-methylcyclohexyl)acetate `COC(=O)CC1C(C)CCCC1O` ![methyl 2-(2-hydroxy-6-methylcyclohexyl)acetate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_option_2_s1_eb1e36c9_02112026.svg?v=eb1e36c9d105)
- (3) 2-(2-hydroxy-2-methoxyethyl)-3-methylcyclohexan-1-ol `COC(O)CC1C(C)CCCC1O` ![2-(2-hydroxy-2-methoxyethyl)-3-methylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_option_3_s1_5563f315_02112026.svg?v=5563f315e21f)
- (4) 2-(2-hydroxyethyl)-3-methylcyclohexan-1-one `CC1CCCC(=O)C1CCO` ![2-(2-hydroxyethyl)-3-methylcyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_option_4_s1_3d2fda33_02112026.svg?v=3d2fda3349e3)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: methyl 2-(2-methyl-6-oxocyclohexyl)acetate →(NaBH₄ / C₂H₅OH) methyl 2-(2-hydroxy-6-methylcyclohexyl)acetate](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q089_sol_1_10f5ada1_30102026.png?v=10f5ada1cf6a)

*methyl 2-(2-methyl-6-oxocyclohexyl)acetate →[NaBH₄ / C₂H₅OH] methyl 2-(2-hydroxy-6-methylcyclohexyl)acetate*

![drawn: methyl 2-(2-methyl-6-oxocyclohexyl)acetate →(NaBH₄ / C₂H₅OH) methyl 2-(2-hydroxy-6-methylcyclohexyl)acetate](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q089_solution_1_50c1ec63_02112026.svg?v=50c1ec6332b9)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. The substrate has a ring ketone and a side-chain methyl ester $-CH_2COOCH_3$.
2. $NaBH_4$ in $C_2H_5OH$ is a mild hydride donor that reduces aldehydes and ketones but not esters.
3. The ring $C=O$ becomes $CH-OH$ while $-CH_2COOCH_3$ stays unchanged, which matches option $2$.

**Subtopic:** Reduction of Aldehydes and Ketones · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 41)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q089_7a49de58_30102026.png?v=7a49de58740c)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q089_3a62bafe_30102026.png?v=3a62bafe7299)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Sodium borohydride reduces an aldehyde or ketone to an alcohol but leaves an ester untouched, so only the ring carbonyl changes
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four options are drawn structures and each arrives as an empty string, so no option content was supplied to this step and no route to a wrong structure can be named
- **Why:** This question requires the product of a named reducing agent on a substrate carrying two different carbonyls, demonstrated by the stem "The product formed in the following chemical reaction is" with $\mathrm{NaBH_4}$ over the arrow and $\mathrm{C_2H_5OH}$ under it.
- **Note:** Options 1-4 are empty strings; the substrate and reagents were captured but the option structures were not supplied to this step, so no trap can be audited, and the paper itself is not in doubt. A reviewer holding the printed options should check two devices this substrate invites: both carbonyls shown reduced, which ignores that $\mathrm{NaBH_4}$ spares the ester, and the ester alone shown reduced with the ketone left, which would be `wrong_site_attacked`.
<!--/ecat-->

## Q90

Chemistry · physical · States of Matter

Choose the correct option for the total pressure (in atm.) in a mixture of $4\,\mathrm{g}$ $\mathrm{O_2}$ and $2\,\mathrm{g}$ $\mathrm{H_2}$ confined in a total volume of one litre at $0^{\circ}\,\mathrm{C}$ is:

- **(1)** $25.18$
- (2) $26.02$
- (3) $2.518$
- (4) $2.602$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Moles of $\mathrm{O_2} = \frac{4}{32} = 0.125$
2. Moles of $\mathrm{H_2} = \frac{2}{2} = 1$
3. Total moles $= 1.125$
4. Now, $PV = nRT$
5. $P = 1.125 \times 0.082 \times 273 = 25.18\,\mathrm{atm}$

**Solved independently** (answer withheld)

1. $n_{\mathrm{O_2}} = \frac{4}{32} = 0.125\,\mathrm{mol}$.
2. $n_{\mathrm{H_2}} = \frac{2}{2} = 1\,\mathrm{mol}$.
3. $n_{\text{total}} = 0.125 + 1 = 1.125\,\mathrm{mol}$.
4. $T = 0^{\circ}\mathrm{C} = 273\,\mathrm{K}$, $V = 1\,\mathrm{L}$.
5. $P = \frac{nRT}{V} = \frac{1.125 \times 0.082 \times 273}{1} = 25.18\,\mathrm{atm}$, which is option $1$.

**Subtopic:** Dalton's Law of Partial Pressures · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 42)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q090_cdbbb306_30102026.png?v=cdbbb30621bd)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q090_ea55b2fb_30102026.png?v=ea55b2fbf4af)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a gas mixture the total pressure is set by the total number of moles, so each mass must be divided by its own molar mass before $PV = nRT$ is used
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $2.518$ is the key with the decimal point one place to the left, which is what writing $R$ as $0.00821$ instead of $0.0821\,\mathrm{L\,atm\,K^{-1}\,mol^{-1}}$ produces: $1.125 \times 0.00821 \times 273 = 2.52$.
- **Why:** This question requires a number computed from the stem's masses, volume and temperature, demonstrated by "the total pressure (in atm.) in a mixture of $4\,\mathrm{g}$ $\mathrm{O_2}$ and $2\,\mathrm{g}$ $\mathrm{H_2}$ confined in a total volume of one litre at $0^{\circ}\,\mathrm{C}$".
<!--/ecat-->

## Q91

Chemistry · physical · Solutions

The correct option for the value of vapour pressure of a solution at $45^\circ\mathrm{C}$ with benzene to octane in molar ratio $3 : 2$ is: [At $45^\circ\mathrm{C}$ vapour pressure of benzene is $280\,\mathrm{mm\,Hg}$ and that of octane is $420\,\mathrm{mm\,Hg}$. Assume Ideal gas]

- **(1)** $336\,\mathrm{mm}$ of $\mathrm{Hg}$
- (2) $350\,\mathrm{mm}$ of $\mathrm{Hg}$
- (3) $160\,\mathrm{mm}$ of $\mathrm{Hg}$
- (4) $168\,\mathrm{mm}$ of $\mathrm{Hg}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Let benzene is B and octane is O
2. $X_{B} = 3/5 = 0.6$
3. $X_{O} = 2/5 = 0.4$
4. Now, $PT = P_{B}^{0}X_{B} + P_{O}^{0}X_{O} = 0.6(280)+0.4(420) = 336\,\mathrm{mm\,Hg}$

**Solved independently** (answer withheld)

1. Mole fractions from the ratio $3:2$: $x_{B} = \frac{3}{5} = 0.6$, $x_{O} = \frac{2}{5} = 0.4$.
2. Raoult's law for an ideal solution: $P = x_{B}P^\circ_{B} + x_{O}P^\circ_{O}$.
3. $P = 0.6 \times 280 + 0.4 \times 420 = 168 + 168$.
4. $P = 336\,\mathrm{mm\,Hg}$, which is option $1$.

**Subtopic:** Vapour Pressure of Liquid Solutions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q091_94a6945a_30102026.png?v=94a6945ad4ea)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q091_63c819d2_30102026.png?v=63c819d2173f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Raoult's law gives the total vapour pressure of an ideal mixture as the sum of both components' partial pressures, each the pure vapour pressure times that component's mole fraction
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $168$ is a true partial pressure here, and because $0.6 \times 280$ and $0.4 \times 420$ both come to $168$, any student who works out one Raoult term and stops reads it as the answer; the stem asked for the vapour pressure of the solution, which is the sum of the two.
- **Why:** This question requires a number computed from two pure vapour pressures and a printed mole ratio, demonstrated by the stem "the value of vapour pressure of a solution at $45^\circ\mathrm{C}$ with benzene to octane in molar ratio $3 : 2$".
<!--/ecat-->

## Q92

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following molecules is non-polar in nature?

- **(1)** $\mathrm{SbCl_5}$
- (2) $\mathrm{NO_2}$
- (3) $\mathrm{POCl_3}$
- (4) $\mathrm{CH_2O}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: antimony pentachloride ($\ce{SbCl5}$), trigonal bipyramidal: two axial Cl and three equatorial Cl (one wedge, one dash) around Sb](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q092_sol_1_efc503ea_30102026.png?v=efc503ea4699)

*antimony pentachloride ($\ce{SbCl5}$), trigonal bipyramidal: two axial Cl and three equatorial Cl (one wedge, one dash) around Sb*


**Solved independently** (answer withheld)

1. $\mathrm{SbCl_5}$: Sb has 5 bond pairs and 0 lone pairs, $sp^3d$, symmetric trigonal bipyramidal, so $\mu = 0$ (non-polar).
2. $\mathrm{NO_2}$: angular (bent) with an odd electron, net dipole $\mu \neq 0$.
3. $\mathrm{POCl_3}$: tetrahedral with one P=O and three P-Cl bonds, dipoles do not cancel, $\mu \neq 0$.
4. $\mathrm{CH_2O}$: trigonal planar with C=O and two C-H bonds, $\mu \neq 0$.
5. Only $\mathrm{SbCl_5}$ is non-polar, which is option $1$.

**Subtopic:** Dipole Moment · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 43)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q092_fb1d93eb_30102026.png?v=fb1d93eb32a2)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q092_99440c99_30102026.png?v=99440c9956c1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A molecule is non-polar only when its bond dipoles cancel, which needs every position around the central atom filled by the same group in a symmetric shape, as in trigonal bipyramidal $\mathrm{SbCl_5}$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  $\mathrm{NO_2}$ reads as a symmetric $\mathrm{AB_2}$ molecule like $\mathrm{CO_2}$, where the two bond dipoles point opposite ways and cancel; the cancellation rule needs the two bonds to be exactly opposed, and the unpaired electron on nitrogen bends $\mathrm{NO_2}$ to about $134^\circ$ so they do not.
- **Why:** This question requires a stated criterion applied to four named molecules, demonstrated by the stem "Which of the following molecules is non-polar in nature?" with four formulas and nothing to compute.
<!--/ecat-->

## Q93

Chemistry · organic · Amines

The reagent ‘R’ in the given sequence of chemical reaction is:

![printed figure: 2,4,6-tribromoaniline →(NaNO₂.HCl, 0 - 5°C) 2,4,6-tribromobenzenediazonium chloride →(R) 1,3,5-tribromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q093_7e2a94c7_30102026.png?v=7e2a94c717de)

*2,4,6-tribromoaniline →[NaNO₂.HCl, 0 - 5°C] 2,4,6-tribromobenzenediazonium chloride →[R] 1,3,5-tribromobenzene*

![drawn: 2,4,6-tribromoaniline →(NaNO₂.HCl, 0 - 5°C) 2,4,6-tribromobenzenediazonium chloride →(R) 1,3,5-tribromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q093_question_a6009382_02112026.svg?v=a600938238d8)  
*drawn by RDKit (code/lib/chem_cards.py)*

Structures: 2,4,6-tribromoaniline `Nc1c(Br)cc(Br)cc1Br` ![2,4,6-tribromoaniline](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q093_question_s1_efd7036e_02112026.svg?v=efd7036ece87); 2,4,6-tribromobenzenediazonium chloride `N#[N+]c1c(Br)cc(Br)cc1Br.[Cl-]` ![2,4,6-tribromobenzenediazonium chloride](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q093_question_s2_4c9c97e1_02112026.svg?v=4c9c97e138fd); 1,3,5-tribromobenzene `Brc1cc(Br)cc(Br)c1` ![1,3,5-tribromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q093_question_s3_d56596a1_02112026.svg?v=d56596a1d27c)

- (1) $\mathrm{HI}$
- (2) $\mathrm{CuCN/KCN}$
- (3) $\mathrm{H_2O}$
- **(4)** $\mathrm{CH_3CH_2OH}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: 2,4,6-tribromoaniline →(NaNO₂.HCl, 0 - 5°C) 2,4,6-tribromobenzenediazonium chloride →(CH₃CH₂OH) 1,3,5-tribromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q093_sol_1_5ded2c1d_30102026.png?v=5ded2c1dbccd)

*2,4,6-tribromoaniline →[NaNO₂.HCl, 0 - 5°C] 2,4,6-tribromobenzenediazonium chloride →[CH₃CH₂OH] 1,3,5-tribromobenzene*

![drawn: 2,4,6-tribromoaniline →(NaNO₂.HCl, 0 - 5°C) 2,4,6-tribromobenzenediazonium chloride →(CH₃CH₂OH) 1,3,5-tribromobenzene](https://d30lmobgrc5gb8.cloudfront.net/general/02112026/neet_papers/2021/2021_O1/figures_drawn/q093_solution_1_92d4b2ed_02112026.svg?v=92d4b2eda9d1)  
*drawn by RDKit (code/lib/chem_cards.py)*


**Solved independently** (answer withheld)

1. Diazotisation with $\mathrm{NaNO_2/HCl}$ at $0$-$5^\circ\mathrm{C}$ converts 2,4,6-tribromoaniline to 2,4,6-tribromobenzenediazonium chloride.
2. The product 1,3,5-tribromobenzene has $\mathrm{H}$ where $\mathrm{-N_2^+Cl^-}$ was, so $R$ must reduce the diazonium group to $\mathrm{H}$.
3. Mild reducing agents $\mathrm{H_3PO_2}$ or $\mathrm{CH_3CH_2OH}$ do this: $\mathrm{ArN_2^+Cl^- + CH_3CH_2OH \rightarrow ArH + N_2 + CH_3CHO + HCl}$.
4. $\mathrm{CuCN/KCN}$ would give $\mathrm{ArCN}$ and $\mathrm{H_2O}$ would give $\mathrm{ArOH}$; $\mathrm{HI}$ is not the standard reagent here, so the answer is option $4$.

**Subtopic:** Chemical Reactions of Diazonium Salts and Coupling Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 43)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q093_7f9de6cb_30102026.png?v=7f9de6cb7b10)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q093_e798eac7_30102026.png?v=e798eac79f10)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Ethanol replaces the diazonium group of an arenediazonium salt by hydrogen, which is how a ring substituent can be introduced and then removed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Water on a warmed diazonium salt is the first replacement reaction printed in the diazonium table, so a student reading from reagent to product takes that row and does not check that the printed product, 1,3,5-tribromobenzene, carries no OH group.
- **Why:** This question requires which reagent effects a printed conversion, demonstrated by the stem "The reagent 'R' in the given sequence of chemical reaction is" with the diazonium salt on one side of the arrow and 1,3,5-tribromobenzene on the other.
- **Note:** E1 classified this as `arrange_in_order` from the word 'sequence' in the stem, but nothing is ordered: the options are four single reagents and the answer is one of them, so the printed shape is `mcq` with `asks: reaction`. Swap test on the trap axis: the four reagent names are wholly unlike one another, and the pull survives, because what carries the student is that each is a row of the same diazonium-reactions table; hence `nearby_fact` and not `look_alike_term`.
<!--/ecat-->

## Q94

Chemistry · inorganic · Coordination Compounds – Practice

Match List - I with List - II. Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{[Fe(CN)_6]^{3-}}$ | (i) | $5.92\,\mathrm{BM}$ |
| (b) | $\mathrm{[Fe(H_2O)_6]^{3+}}$ | (ii) | $0\,\mathrm{BM}$ |
| (c) | $\mathrm{[Fe(CN)_6]^{4-}}$ | (iii) | $4.90\,\mathrm{BM}$ |
| (d) | $\mathrm{[Fe(H_2O)_6]^{2+}}$ | (iv) | $1.73\,\mathrm{BM}$ |

- (1) (a)-(i), (b)-(iii), (c)-(iv), (d)-(ii)
- **(2)** (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)
- (3) (a)-(iv), (b)-(ii), (c)-(i), (d)-(iii)
- (4) (a)-(ii), (b)-(iv), (c)-(iii), (d)-(i)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{[Fe(CN)_6]^{4-}}$: $\mathrm{Fe^{2+}} = [\mathrm{Ar}]\,3d^{6}$
2. In the presence of strong field $\mathrm{CN^{-}}$ ligand, electrons will be paired and magnetic moment $= 0\,\mathrm{B.M.}$

**Solved independently** (answer withheld)

1. Use $\mu = \sqrt{n(n+2)}\,\mathrm{BM}$; $\mathrm{CN^-}$ is a strong-field ligand (low spin), $\mathrm{H_2O}$ is weak-field (high spin).
2. (a) $\mathrm{[Fe(CN)_6]^{3-}}$: $\mathrm{Fe^{3+}}$, $d^5$ low spin $t_{2g}^5$, $n=1$, $\mu=\sqrt{3}=1.73\,\mathrm{BM}$ → (iv).
3. (b) $\mathrm{[Fe(H_2O)_6]^{3+}}$: $\mathrm{Fe^{3+}}$, $d^5$ high spin $t_{2g}^3e_g^2$, $n=5$, $\mu=\sqrt{35}=5.92\,\mathrm{BM}$ → (i).
4. (c) $\mathrm{[Fe(CN)_6]^{4-}}$: $\mathrm{Fe^{2+}}$, $d^6$ low spin $t_{2g}^6$, $n=0$, $\mu=0\,\mathrm{BM}$ → (ii).
5. (d) $\mathrm{[Fe(H_2O)_6]^{2+}}$: $\mathrm{Fe^{2+}}$, $d^6$ high spin $t_{2g}^4e_g^2$, $n=4$, $\mu=\sqrt{24}=4.90\,\mathrm{BM}$ → (iii).
6. Matching (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii) is option $2$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 43)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q094_38c390e1_30102026.png?v=38c390e1ab0b)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q094_8e192a9c_30102026.png?v=8e192a9c4b48)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spin-only moment follows from the number of unpaired electrons, and that number depends on the ligand: CN- pairs the d electrons (low spin) while H2O leaves them unpaired (high spin)
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Fe3+ is d5, and five unpaired electrons give $\sqrt{5\times7}=5.92$ BM — the value for the free ion, reached by not letting the printed CN- do anything. Only this code pairs $\mathrm{[Fe(CN)_6]^{3-}}$ with 5.92 BM, so the one dropped condition selects the whole code.
- **Why:** This question requires the spin-only moment worked out for each complex, demonstrated by List-II holding the four values 5.92, 0, 4.90 and 1.73 BM, which are fixed once the unpaired count is settled from the oxidation state and the ligand.
<!--/ecat-->

## Q95

Chemistry · physical · Structure of Atom

From the following pairs of ions which one is not an iso-electronic pair?

- (1) $\mathrm{Mn^{2+}}$, $\mathrm{Fe^{3+}}$
- **(2)** $\mathrm{Fe^{2+}}$, $\mathrm{Mn^{2+}}$
- (3) $\mathrm{O^{2-}}$, $\mathrm{F^{-}}$
- (4) $\mathrm{Na^{+}}$, $\mathrm{Mg^{2+}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Isoelectronic pairs have the same number of electrons. The number of electrons in
2. $\mathrm{Fe^{2+}} = 24$
3. $\mathrm{Mn^{2+}} = 23$
4. Thus, these ions are not isoelectronic.

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{Mn^{2+}}$ has $25-2=23$ electrons and $\mathrm{Fe^{3+}}$ has $26-3=23$ electrons, so they are isoelectronic.
2. Option 2: $\mathrm{Fe^{2+}}$ has $26-2=24$ electrons and $\mathrm{Mn^{2+}}$ has $25-2=23$ electrons, so they are not isoelectronic.
3. Option 3: $\mathrm{O^{2-}}$ has $8+2=10$ electrons and $\mathrm{F^{-}}$ has $9+1=10$ electrons, so they are isoelectronic.
4. Option 4: $\mathrm{Na^{+}}$ has $11-1=10$ electrons and $\mathrm{Mg^{2+}}$ has $12-2=10$ electrons, so they are isoelectronic.
5. The only non-isoelectronic pair is $\mathrm{Fe^{2+}}, \mathrm{Mn^{2+}}$, which is option $2$.

**Subtopic:** Isoelectronic Species · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q095_eb24fe50_30102026.png?v=eb24fe502a8c)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q095_e6532f2c_30102026.png?v=e6532f2c3a11)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Iso-electronic species are those with the same number of electrons, which is found by subtracting the charge from the atomic number, not by comparing the charges themselves
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Comparing the ions instead of counting their electrons, $\mathrm{Mn^{2+}}$ and $\mathrm{Fe^{3+}}$ differ in both element and charge, so the pair reads as the mismatched one; counting gives $25-2=23$ and $26-3=23$, the same number, which is what iso-electronic means.
- **Why:** This question requires a stated criterion applied to four printed pairs, demonstrated by the stem "From the following pairs of ions which one is not an iso-electronic pair?"
- **Note:** The two main-group pairs (options 3 and 4) are recorded as fillers on the same ground, that the question's own subtraction settles both from the periodic table and both sit in one printed iso-electronic list. The discrimination in this question is between the two transition-metal pairs.
<!--/ecat-->

## Q96

Chemistry · physical · Thermodynamics

For irreversible expansion of an ideal gas under isothermal condition, the correct option is:

- **(1)** $\Delta U = 0,\ \Delta S_{\mathrm{total}} \neq 0$
- (2) $\Delta U \neq 0,\ \Delta S_{\mathrm{total}} = 0$
- (3) $\Delta U = 0,\ \Delta S_{\mathrm{total}} = 0$
- (4) $\Delta U \neq 0,\ \Delta S_{\mathrm{total}} \neq 0$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For irreversible processes, the entropy of the universe increases, i.e., $\Delta S_{\mathrm{total}} > 0$
2. Also, since the process is isothermal$(\Delta T = 0)$ and gas is ideal, $\Delta U = nC_{V}\Delta T = 0$

**Solved independently** (answer withheld)

1. For an ideal gas $U$ depends only on $T$; isothermal means $\Delta T = 0$, so $\Delta U = nC_v\Delta T = 0$.
2. For an irreversible (spontaneous) process, the second law gives $\Delta S_{\mathrm{total}} = \Delta S_{\mathrm{sys}} + \Delta S_{\mathrm{surr}} > 0$, so $\Delta S_{\mathrm{total}} \neq 0$.
3. $\Delta U = 0,\ \Delta S_{\mathrm{total}} \neq 0$ is option $1$.

**Subtopic:** Entropy, Second Law & Third Law, Internal Energy and First Law of Thermodynamics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q096_06536532_30102026.png?v=06536532e340)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q096_ae67cf4f_30102026.png?v=ae67cf4f2f26)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An ideal gas expanding at constant temperature keeps its internal energy, but an irreversible expansion still makes the entropy of the universe rise
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first half, $\Delta U = 0$, is right for any isothermal change in an ideal gas, and the surrounding correctness vouches for the second half; $\Delta S_{\mathrm{total}} = 0$ is the result for a REVERSIBLE change, so this option is what you get by using 'isothermal' and dropping 'irreversible'.
- **Why:** This question requires two stated conditions applied to one process, demonstrated by the stem "For irreversible expansion of an ideal gas under isothermal condition" and by each option pairing a $\Delta U$ verdict with a $\Delta S_{\mathrm{total}}$ verdict.
- **Note:** `half_right` is used here under the rule that permits it only on an option of two or more parts: each option carries two independent verdicts, and option 3 fails on exactly one of them.
<!--/ecat-->

## Q97

Chemistry · physical · Electrochemistry

The molar conductivity of $0.007\,\mathrm{M}$ acetic acid is $20\,\mathrm{S\,cm^{2}\,mol^{-1}}$. What is the dissociation constant of acetic acid? Choose the correct option.
$\lambda^{o}_{\mathrm{H}} = 350\,\mathrm{S\,cm^{2}\,mol^{-1}}$
$\lambda^{o} = 50\,\mathrm{S\,cm^{2}\,mol^{-1}}$

- **(1)** $1.75 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$
- (2) $2.50 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$
- (3) $1.75 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$
- (4) $2.50 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. By Kohlrausch's law, $\Lambda^{o}_{m} = \lambda^{o}_{\mathrm{H^+}} + \lambda^{o}_{\mathrm{CH_3COO^-}} = 350 + 50 = 400\,\mathrm{S\,cm^{2}\,mol^{-1}}$.
2. $\alpha = \frac{\Lambda_m}{\Lambda^{o}_{m}} = \frac{20}{400} = 0.05$.
3. $K_a \approx c\alpha^{2} = 0.007 \times (0.05)^{2} = 1.75 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$, which is option $1$.

**Subtopic:** Applications of Kohlrausch Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 44)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q097_a7fd4c68_30102026.png?v=a7fd4c684881)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The degree of dissociation of a weak acid is its molar conductivity divided by the limiting value from Kohlrausch's law, and the dissociation constant is then $K_a = C\alpha^2$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $1.75 \times 10^{-4}$ is the key with one power of ten added, which is exactly what reading the concentration as $0.07\,\mathrm{M}$ instead of the printed $0.007\,\mathrm{M}$ produces: $0.07 \times (0.05)^2 = 1.75 \times 10^{-4}$.
- **Why:** This question requires a number computed from the stem's conductivity data, demonstrated by "The molar conductivity of $0.007\,\mathrm{M}$ acetic acid is $20\,\mathrm{S\,cm^{2}\,mol^{-1}}$. What is the dissociation constant of acetic acid?"
- **Note:** The stem prints the second limiting conductivity as a bare $\lambda^{o} = 50$ with no ion named; the key follows from reading it as the acetate ion's value, which is how it is tagged. The key also uses $K_a = C\alpha^2$ without the $(1-\alpha)$ denominator, which would give $1.84 \times 10^{-5}$; the nearest printed option is still option 1, so the key stands as printed.
<!--/ecat-->

## Q98

Chemistry · physical · Chemical Kinetics

The slope of Arrhenius Plot ($\ln k$ v/s $1/T$) of first order reaction is $-5 \times 10^{3}\,\mathrm{K}$. The value of $E_a$ of the reaction is. Choose the correct option for your answer. [Given $R = 8.314\,\mathrm{J\,K^{-1}\,mol^{-1}}$]

- (1) $166\,\mathrm{kJ\,mol^{-1}}$
- (2) $-83\,\mathrm{kJ\,mol^{-1}}$
- **(3)** $41.5\,\mathrm{kJ\,mol^{-1}}$
- (4) $83.0\,\mathrm{kJ\,mol^{-1}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The logarithmic form of Arrhenius equation is
2. $\ln k = -\frac{E_a}{RT} + \ln A$
3. Slope $= -E_a/R \Rightarrow E_a = -(\text{slope})R$
4. $E_a = 5 \times 10^{3} \times 8.314 = 41.57 \times 10^{3}$

**Solved independently** (answer withheld)

1. Arrhenius equation in log form: $\ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$, so the slope of $\ln k$ vs $1/T$ is $-\frac{E_a}{R}$.
2. $-\frac{E_a}{R} = -5 \times 10^{3}\,\mathrm{K} \Rightarrow E_a = 5 \times 10^{3}\,\mathrm{K} \times R$.
3. $E_a = 5 \times 10^{3} \times 8.314\,\mathrm{J\,mol^{-1}} = 41570\,\mathrm{J\,mol^{-1}}$.
4. $41570\,\mathrm{J\,mol^{-1}} = 41.57\,\mathrm{kJ\,mol^{-1}} \approx 41.5\,\mathrm{kJ\,mol^{-1}}$, which is option $3$.

**Subtopic:** Arrhenius Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q098_2dec1e23_30102026.png?v=2dec1e2324e8)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q098_719c799f_30102026.png?v=719c799f35d2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** On a plot of $\ln k$ against $1/T$ the slope is $-E_a/R$, so the activation energy is the slope's magnitude times the gas constant with no conversion factor
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The base-ten form of the Arrhenius plot carries an extra $2.303$ in the denominator, and a student who remembers that there is a factor of about 2 there and applies $E_a = 2R \times 5 \times 10^{3}$ gets $83.1\,\mathrm{kJ\,mol^{-1}}$, exactly twice the right answer.
- **Why:** This question requires a number computed from a printed slope and a given constant, demonstrated by "The slope of Arrhenius Plot ($\ln k$ v/s $1/T$) of first order reaction is $-5 \times 10^{3}\,\mathrm{K}$" with $R$ supplied.
<!--/ecat-->

## Q99

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

$\mathrm{CH_3CH_2COO^{-}Na^{+}} \xrightarrow[\text{Heat}]{\mathrm{NaOH},\,+?} \mathrm{CH_3CH_3} + \mathrm{Na_2CO_3}$.
Consider the above reaction and identify the missing reagent/chemical

- **(1)** $\mathrm{CaO}$
- (2) DIBAL-H
- (3) $\mathrm{B_2H_6}$
- (4) Red Phosphorus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{CH_3CH_2COO^{-}Na^{+}} \xrightarrow[\text{Heat}]{\mathrm{NaOH+CaO}} \mathrm{CH_3CH_3} + \mathrm{Na_2CO_3}$
2. It is soda lime decarboxylation reaction.

**Solved independently** (answer withheld)

1. Sodium propanoate loses $\mathrm{CO_2}$ (as $\mathrm{Na_2CO_3}$) to give ethane, a decarboxylation with one fewer carbon.
2. Decarboxylation of sodium carboxylates is done by heating with soda lime, $\mathrm{NaOH} + \mathrm{CaO}$, so the missing reagent is $\mathrm{CaO}$, option $1$.

**Subtopic:** Reactions with Ammonia and Decarboxylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 45)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q099_8f23b05b_30102026.png?v=8f23b05bde8b)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q099_a2b8872c_30102026.png?v=a2b8872c688f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Soda lime, sodium hydroxide fused with calcium oxide, decarboxylates a sodium carboxylate on heating, so the carboxyl carbon leaves as carbonate and the alkane is left behind
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Diborane is the reagent printed for reducing a carboxylic acid, so a student who reads $\mathrm{{-}COO^{-}Na^{+}} \rightarrow \mathrm{CH_3}$ as the carboxyl group being stripped by a reducing agent picks it; that reagent answers which reagent reduces an acid, while this scheme is a decarboxylation and the stem already prints its reducing-free partner, NaOH.
- **Why:** This question requires the reagent that completes a printed conversion, demonstrated by the stem "Consider the above reaction and identify the missing reagent/chemical" with $\mathrm{NaOH}$ and a question mark over the arrow and $\mathrm{CH_3CH_3} + \mathrm{Na_2CO_3}$ as the products.
- **Note:** E1 called this `reaction_scheme`, which describes the stem rather than the answer's form; the printed shape is a stem with one scheme and four single reagents as options, so `qtype` is `mcq`.
<!--/ecat-->

## Q100

Chemistry · inorganic · The p–Block Elements

In which one of the following arrangements the given sequence is not strictly according to the properties indicated against it?

- (1) $\mathrm{NH_3} < \mathrm{PH_3} < \mathrm{AsH_3} < \mathrm{SbH_3}$ : Increasing acidic character
- (2) $\mathrm{CO_2} < \mathrm{SiO_2} < \mathrm{SnO_2} < \mathrm{PbO_2}$ : Increasing oxidizing power
- (3) $\mathrm{HF} < \mathrm{HCl} < \mathrm{HBr} < \mathrm{HI}$ : Increasing acidic strength
- **(4)** $\mathrm{H_2O} < \mathrm{H_2S} < \mathrm{H_2Se} < \mathrm{H_2Te}$ : Increasing $\mathrm{p}K_a$ values

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{H_2O}$, $\mathrm{H_2S}$, $\mathrm{H_2Se}$, $\mathrm{H_2Te}$ $\downarrow$
2. $\because$ B.E $\downarrow$
3. $K_a \uparrow$ $\mathrm{p}K_a \downarrow$

**Solved independently** (answer withheld)

1. Down group 16, the $\mathrm{H{-}E}$ bond weakens, so acid strength increases: $\mathrm{H_2O} < \mathrm{H_2S} < \mathrm{H_2Se} < \mathrm{H_2Te}$.
2. Higher acid strength means lower $\mathrm{p}K_a$, so $\mathrm{p}K_a$: $\mathrm{H_2O} > \mathrm{H_2S} > \mathrm{H_2Se} > \mathrm{H_2Te}$; option $4$ states the reverse.
3. Option $1$: basicity falls and acidic character rises from $\mathrm{NH_3}$ to $\mathrm{SbH_3}$, correct.
4. Option $2$: inert pair effect makes $+4$ least stable for Pb, so $\mathrm{PbO_2}$ is the strongest oxidant, correct.
5. Option $3$: $\mathrm{H{-}X}$ bond strength falls from HF to HI, so acidity rises, correct; answer is option $4$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 45)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q100_51c3f240_30102026.png?v=51c3f240c648)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/solutions/q100_418a72d2_30102026.png?v=418a72d276f6)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Acidity of the hydrides rises down a group because the bond to hydrogen weakens, and $\mathrm{p}K_a$ is the inverse scale, so it must fall where acidity rises
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Deciding hydrogen-halide acidity by electronegativity puts HF at the top and makes the printed rising order look like the arrangement that fails; what governs here is the H-X bond dissociation enthalpy, which falls from HF to HI, so the printed order stands and the arrangement that actually fails is the $\mathrm{p}K_a$ one.
- **Why:** This question requires four printed orderings to be checked against the property each claims to follow, demonstrated by the stem "In which one of the following arrangements the given sequence is not strictly according to the properties indicated against it?" with each option carrying a chain of species and the property named after a colon.
- **Note:** `qtype` is `statements` because each option is a complete claim graded true or false, which is the same demand the paper's other negated question (q082) carries; E1 called it `arrange_in_order` from the chains inside the options, but the answer is a verdict on an arrangement, not an arrangement. The key turns on $\mathrm{p}K_a$ being the inverse of acidity, so option 4's chain is the only one stated against its own property.
<!--/ecat-->

## Q101

Biology · both · Biotechnology: Principles and Processes

During the purification process for recombinant DNA technology, addition of chilled ethanol precipitates out:

- (1) Histones
- (2) Polysaccharides
- (3) RNA
- **(4)** DNA

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In recombinant DNA technology the cell is lysed, RNA is removed by ribonuclease, proteins by protease and polysaccharides by cellulase/chitinase; addition of chilled ethanol then precipitates out the purified DNA as fine threads, which is option $4$.

**Subtopic:** Isolation of Genetic Material (DNA) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q101_fafce927_30102026.png?v=fafce92714c1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In DNA isolation each contaminant has its own enzyme - RNase, protease, cellulase - and the last step, chilled ethanol, brings down the purified DNA as fine threads
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  'Precipitates out' reads like the step that gets rid of a contaminant, and RNA is the contaminant named two sentences earlier in the same paragraph; alcohol does precipitate nucleic acid, but by this stage ribonuclease has already removed the RNA, so what comes out is the DNA.
- **Why:** This question requires the stated step in the isolation protocol, demonstrated by the stem 'addition of chilled ethanol precipitates out:' with four molecules from the same paragraph as options.
<!--/ecat-->

## Q102

Biology · botany · Sexual Reproduction in Flowering Plants

A typical angiosperm embryo sac at maturity is

- (1) 7-nucleate and 7-celled
- (2) 8-nucleate and 8-celled
- **(3)** 8-nucleate and 7-celled
- (4) 7-nucleate and 8-celled

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The typical (Polygonum-type) mature embryo sac has $3$ antipodals $+ 3$ egg apparatus cells $+ 2$ polar nuclei $= 8$ nuclei in $3 + 3 + 1 = 7$ cells, as the two polar nuclei lie in one central cell, so it is 8-nucleate and 7-celled, option $3$.

**Subtopic:** Megasporangium (Ovule) and Embryo Sac · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q102_8f371b2c_30102026.png?v=8f371b2c8451)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A mature embryo sac has eight nuclei but seven cells, because the two polar nuclei share the single large central cell
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Eight is the number that gets remembered, and one nucleus per cell then forces eight cells; the two polar nuclei stay together in one central cell, so the cell count stops at seven.
- **Why:** This question requires the stated nucleus and cell counts of the mature embryo sac, demonstrated by four options that cross '7' and '8' against each other.
<!--/ecat-->

## Q103

Biology · both · Cell: The Unit of Life

Which of the following is an incorrect statement ?

- (1) The perinuclear space forms a barrier between the materials present inside the nucleus and that of the cytoplasm
- (2) Nuclear pores act as passages for proteins and RNA molecules in both directions between nucleus and cytoplasm
- **(3)** Mature sieve tube elements possess a conspicuous nucleus and usual cytoplasmic organelles
- (4) Microbodies are present both in plant and animal cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Mature sieve tube elements lose their nucleus at maturity and are kept alive by companion cells, so statement $3$ is incorrect; statements $1$, $2$ and $4$ are correct as NCERT gives them, so the answer is option $3$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q103_09abcf41_30102026.png?v=09abcf414a8d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A mature sieve tube element keeps a thin peripheral cytoplasm but loses its nucleus; the other three options are the chapter's own lines on the perinuclear space, nuclear pores and microbodies
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Option 1 reads as though it contradicts option 2 - a barrier, against passages open in both directions - so a reader hunting the false statement settles on the barrier. Both are the chapter's own sentences: the perinuclear space is the barrier and the pores are the interruptions in it.
- **Why:** This question requires judging four printed claims for the one that is false, demonstrated by the stem 'Which of the following is an incorrect statement ?' against option 3's 'Mature sieve tube elements possess a conspicuous nucleus and usual cytoplasmic organelles'.
- **Note:** qtype is statements because the stem asks for a statement to be judged, which is the rulebook's test; the task is negated ('incorrect'), and the trap is the live form of the retired true_statement_trap, whose family on the live axis is answers_other_question.
<!--/ecat-->

## Q104

Biology · botany · Plant Growth and Development

The plant hormone used to destroy weeds in a field is

- **(1)** 2, 4-D
- (2) IBA
- (3) IAA
- (4) NAA

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Auxins such as $2,4\text{-D}$ are widely used as herbicides to kill dicotyledonous weeds without affecting monocot crops, while IBA, IAA and NAA are used for rooting and other growth effects, so the answer is option $1$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 46)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q104_b21145fb_30102026.png?v=b21145fb4a51)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** 2,4-D is the synthetic auxin used as a herbicide against dicot weeds; IAA and IBA are the natural auxins and NAA the other synthetic one
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The synthetic auxins are named in one breath, 'NAA and 2,4-D', so a student who has stored them as a pair and is asked for the weedkiller can take the other member of the pair; the herbicidal use is attached to 2,4-D alone.
- **Why:** This question requires the stated use of one named auxin, demonstrated by the stem 'The plant hormone used to destroy weeds in a field is' with four auxins as options.
- **Note:** Swap test applied: replacing '2,4-D' and 'NAA' with two unlike words leaves the pull intact, because what carries the reader is the pair being printed together and not any likeness between the two names, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q105

Biology · botany · Anatomy of Flowering Plants

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Cells with active cell division capacity | (i) | Vascular Tissues |
| (b) | Tissue having all cells similar in structure and function | (ii) | Meristematic tissues |
| (c) | Tissue having different type of cells | (iii) | Sclereids |
| (d) | Dead cells with highly thickened walls and narrow lumen | (iv) | Simple Tissue |

- (1) (a)- (i); (b) - (ii); (c) - (iii);(d) - (iv)
- (2) (a)- (iii); (b) - (ii); (c) - (iv);(d) - (i)
- **(3)** (a)- (ii); (b) - (iv); (c) - (i);(d) - (iii)
- (4) (a)- (iv); (b) - (iii); (c) - (ii);(d) - (i)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. (a) Cells that can actively divide make up meristematic tissue, so $(a)\to(ii)$.
2. (b) A tissue whose cells are all alike in structure and function is a simple tissue, so $(b)\to(iv)$.
3. (c) A tissue made of different kinds of cells is a complex tissue, which here means vascular tissue, so $(c)\to(i)$.
4. (d) Dead cells with heavily thickened walls and a narrow lumen are sclereids, so $(d)\to(iii)$.
5. The matching $(a)-(ii),(b)-(iv),(c)-(i),(d)-(iii)$ is option $3$.

**Subtopic:** The Tissue, Permanent Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q105_a01da193_30102026.png?v=a01da193f2ec)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Meristematic tissue divides, a simple tissue is built of one cell type and a complex vascular tissue of several, and sclereids are the dead thick-walled sclerenchyma cells
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Sclerenchyma is what 'dead cells with highly thickened walls and narrow lumen' describes, and the chapter files sclerenchyma among the SIMPLE tissues, so (d)-(iv) reads correct; option 1 is the only code offering it, and the same code hands Meristematic tissues to (b), which is true of meristem cells but is the wording used to define a simple tissue.
- **Why:** This question requires the chapter's stated definitions of four tissue terms, demonstrated by list I's '(b) Tissue having all cells similar in structure and function' against list II's '(iv) Simple Tissue'.
<!--/ecat-->

## Q106

Biology · both · Biotechnology: Principles and Processes

Which of the following is not an application of PCR (Polymerase Chain Reaction)

- **(1)** Purification of isolated protein
- (2) Detection of gene mutation
- (3) Molecular diagnosis
- (4) Gene amplification

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. PCR amplifies DNA sequences, so it is used for gene amplification, detecting gene mutations and molecular diagnosis; it acts on nucleic acids, not proteins, so purification of isolated protein is not an application (option $1$).

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q106_4d72f14c_30102026.png?v=4d72f14cd1f4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** PCR amplifies DNA and is used for molecular diagnosis and mutation detection; purifying an isolated protein belongs to downstream processing
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Gene amplification is what PCR IS, and the stem spells the name out as 'Polymerase Chain Reaction', so the option that states it is where a reader going straight for the PCR fact lands; the stem asks for the application that is NOT PCR's.
- **Why:** This question requires separating PCR's uses from a downstream step, demonstrated by the stem 'Which of the following is not an application of PCR' against option 1's 'Purification of isolated protein'.
- **Note:** The question's only device is the negation, so all three wrong options are reached by the same route and differ only in which true application the reader stops at; they are recorded as three routes rather than compressed, because none of them is a filler.
<!--/ecat-->

## Q107

Biology · both · Biotechnology: Principles and Processes

Which of the following is a correct sequence of steps in a PCR (Polymerase Chain Reaction) ?

- (1) Extension, Denaturation, Annealing
- (2) Annealing, Denaturation, Extension
- **(3)** Denaturation, Annealing, Extension
- (4) Denaturation, Extension, Annealing

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Each PCR cycle runs in this order: denaturation of the dsDNA at high temperature, then annealing of the primers, then extension by Taq polymerase. That is option $3$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q107_2bb75136_30102026.png?v=2bb751369791)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** One PCR cycle runs denaturation, then annealing of the primers, then extension by Taq polymerase
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Denaturation first is the step whose place is certain, and the cycle is then finished off with 'the enzyme builds the new strand'; Taq has nothing to build from until a primer has annealed, so extension cannot come before annealing.
- **Why:** This question requires the order of the three steps within one cycle, demonstrated by the stem 'a correct sequence of steps in a PCR' with each option printed as a full ordering.
- **Note:** E1 called this arrange_in_order; the current qtype axis carries no ordering shape, so the printed shape is mcq and the ordering is carried by asks: order.
<!--/ecat-->

## Q108

Biology · both · Biotechnology and Its Applications

When gene targetting involving gene amplification is attempted in an individual's tissue to treat disease, it is known as:

- (1) Molecular diagnosis
- (2) Safety testing
- (3) Biopiracy
- **(4)** Gene therapy

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Introducing or correcting genes in an individual's cells or tissues to treat a disease is called gene therapy, so the answer is option $4$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q108_3829d67a_30102026.png?v=3829d67a50a6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gene therapy is the correction of a gene defect by delivering a working gene into a patient's own tissue; molecular diagnosis only detects the defect
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The stem prints the words 'gene amplification', and amplification by PCR is the technique the molecular diagnosis paragraph is built on, so the phrase in the stem is matched to the technique that uses it instead of to the purpose the stem states
- **Why:** This question requires the name NCERT gives one procedure, demonstrated by the stem 'attempted in an individual's tissue to treat disease, it is known as:'.
- **Note:** The stem's phrase 'gene targetting involving gene amplification' is not NCERT's wording for gene therapy; tagged as printed, and the key is the only option that is a treatment.
<!--/ecat-->

## Q109

Biology · both · Principles of Inheritance and Variation

Mutations in plant cells can be induced by:

- **(1)** Gamma rays
- (2) Zeatin
- (3) Kinetin
- (4) Infrared rays

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Gamma rays are ionising radiation and act as a mutagen that can induce mutations in plant cells (mutation breeding), whereas zeatin and kinetin are cytokinins and infrared rays are non-ionising, so the answer is option $1$.

**Subtopic:** Mutation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q109_34f2f711_30102026.png?v=34f2f711e12f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mutations are induced by ionising radiation such as gamma rays and by chemical mutagens; plant growth regulators do not change the DNA sequence
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who knows that radiation induces mutations but not that the radiation has to be ionising has two radiations on the list and takes the other one
- **Why:** This question requires the agent NCERT states can induce mutations, demonstrated by the stem 'Mutations in plant cells can be induced by:' with two radiations and two cytokinins as options.
<!--/ecat-->

## Q110

Biology · botany · Plant Kingdom

Which of the following algae produce Carrageen?

- **(1)** Red Algae
- (2) Blue-Green Algae
- (3) Green Algae
- (4) Brown Algae

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Carrageen is a commercial hydrocolloid extracted from red algae (Rhodophyceae), while brown algae give algin, so the answer is option $1$.

**Subtopic:** Rhodophyceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q110_52124572_30102026.png?v=52124572db09)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Carrageen is the hydrocolloid obtained from red algae; algin is the one obtained from brown algae
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The two hydrocolloids are printed in a single breath - algin from brown algae and carrageen from red algae - so a student who remembers that one of the pair belongs to brown algae attaches the wrong half of the sentence
- **Why:** This question requires the algal group NCERT names as the source of one product, demonstrated by the stem 'Which of the following algae produce Carrageen?' with four algal classes as options.
<!--/ecat-->

## Q111

Biology · botany · Morphology of Flowering Plants

Diadelphous stamens are found in:

- **(1)** Pea
- (2) China rose and citrus
- (3) China rose
- (4) Citrus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Diadelphous stamens are united in two bundles, as in pea ($(9)+1$); China rose is monadelphous and citrus is polyadelphous, so the answer is option $1$.

**Subtopic:** Androecium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q111_41341039_30102026.png?v=413410391d5c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stamens united into two bundles are diadelphous, the example being pea; one bundle is monoadelphous (China rose) and more than two is polyadelphous (citrus)
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Diadelphous and polyadelphous differ only in the prefix, so a student who has stored '-adelphous means stamens in bundles' without fixing the number takes the example attached to the other many-bundle term
- **Why:** This question requires the example NCERT prints for one androecium term, demonstrated by the stem 'Diadelphous stamens are found in:' against the three examples printed with the adelphous terms. Swap test applied: replace polyadelphous with an unlike word and the pull dies, because it is the shared -adelphous ending and the number prefix that carry the student, so look_alike_term rather than nearby_fact.
- **Note:** Option 2 bundles two examples while the other three are single, so the option set is not pairs throughout and the shape stays mcq.
<!--/ecat-->

## Q112

Biology · botany · Ecosystem

Which of the following statements is not correct?

- (1) Pyramid of energy is always upright
- (2) Pyramid of numbers in a grassland ecosystem is upright
- (3) Pyramid of biomass in sea is generally inverted.
- **(4)** Pyramid of biomass in sea is generally upright

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Pyramid of energy is always upright, because energy is lost at each trophic level, so option $1$ is correct; in a grassland, producers outnumber herbivores, which outnumber carnivores, so option $2$ (upright pyramid of numbers) is correct; in the sea the phytoplankton biomass is smaller than the consumer biomass, so the pyramid of biomass is generally inverted, which makes option $3$ correct and option $4$ the statement that is not correct.

**Subtopic:** Ecological Pyramids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 48)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q112_70e53361_30102026.png?v=70e53361ba53)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Energy pyramids are always upright and grassland number pyramids are upright, but the biomass pyramid in the sea is inverted because the tiny producers are outweighed by the consumers they support
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The general rule learnt is that ecological pyramids stand upright, and applying it to the sea makes the printed exception look like the planted error, so the true statement is marked as the incorrect one
- **Why:** This question requires one printed statement about ecological pyramids to be found false, demonstrated by options 3 and 4 printing 'Pyramid of biomass in sea is generally inverted' and 'generally upright' against each other.
<!--/ecat-->

## Q113

Biology · both · Biomolecules

Which of the following are not secondary metabolites in plants?

- (1) Vinblastin, curcumin
- (2) Rubber, gums
- (3) Morphine, codeine
- **(4)** Amino acids, glucose

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Amino acids and glucose take part in basic metabolism (primary metabolites), while vinblastin, curcumin, rubber, gums, morphine and codeine are secondary metabolites, so the answer is option $4$.

**Subtopic:** Primary And Secondary Metabolites · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q113_c01fc33b_30102026.png?v=c01fc33b307c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Amino acids and glucose are primary metabolites found in every cell; alkaloids, drugs, pigments, rubber and gums are the secondary metabolites of plants
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Rubber and gums are polymers, and the polymers a student knows best - starch and cellulose - sit in the primary metabolite family, so the pair is read into the wrong column and flagged as the one that is not secondary
- **Why:** This question requires membership of the primary rather than the secondary metabolite list, demonstrated by the option 'Amino acids, glucose' against three pairs drawn from the secondary metabolite table.
- **Note:** E1's pattern returned plain_mcq, but every option is a PAIR of compounds accepted or rejected whole, which is the retired pair_options; category_retired.qtype maps that to statements, so that is the shape recorded.
<!--/ecat-->

## Q114

Biology · botany · Plant Kingdom

Gemmae are present in:

- (1) Some Gymnosperms
- **(2)** Some Liverworts
- (3) Mosses
- (4) Pteridophytes

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Gemmae are green, multicellular asexual buds formed in gemma cups on the thalli of some liverworts (e.g. Marchantia), so the answer is option $2$.

**Subtopic:** Liverworts · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q114_66a3bdd4_30102026.png?v=66a3bdd4e768)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gemmae are the green multicellular asexual buds by which some liverworts reproduce vegetatively
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Gemmae are stored as a bryophyte item, and mosses are the other bryophyte, described in the paragraph that follows the liverwort one, so the neighbouring group is offered for the one the structure belongs to
- **Why:** This question requires the group NCERT names as bearing one structure, demonstrated by the stem 'Gemmae are present in:' against four plant groups.
- **Note:** Swap test applied: liverworts and mosses do not resemble each other as words, and the pull survives renaming because it comes from the moss paragraph standing beside the liverwort one, so nearby_fact.
<!--/ecat-->

## Q115

Biology · both · Cell: The Unit of Life

When the centromere is situated in the middle of two equal arms of chromosomes, the chromosome is referred as:

- (1) Sub-metacentric
- (2) Acrocentric
- **(3)** Metacentric
- (4) Telocentric

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. A centromere placed centrally gives two equal arms, and NCERT calls this chromosome metacentric, which is option $3$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q115_3e2aefe1_30102026.png?v=3e2aefe143b8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A chromosome with the centromere exactly in the middle, giving two equal arms, is metacentric; shifting the centromere slightly off centre makes it sub-metacentric
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Sub-metacentric is metacentric with one syllable added, so a student who has the family of names but not the position each one fixes picks the longer form of the word that is on the tip of the tongue
- **Why:** This question requires the name NCERT gives one centromere position, demonstrated by the stem 'When the centromere is situated in the middle of two equal arms of chromosomes, the chromosome is referred as:'. Swap test applied: replace sub-metacentric with an unlike word and the pull dies, so the likeness between the two names is doing the work.
<!--/ecat-->

## Q116

Biology · both · Evolution

The factor that leads to Founder effect in a population is:

- (1) Mutation
- **(2)** Genetic drift
- (3) Natural selection
- (4) Genetic recombination

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The founder effect arises when a few individuals found a new population, so allele frequencies shift by chance sampling, which is genetic drift, option $2$.

**Subtopic:** Hardy-Weinberg Principle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 49)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q116_0f6e7aa3_30102026.png?v=0f6e7aa3b9a9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The founder effect is a case of genetic drift: a few individuals start a new population whose allele frequencies differ from the population they came from
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Natural selection is the chapter's headline agent of changed allele frequencies, so a student who knows the founder effect involves a new population with different frequencies reaches for the mechanism the chapter spends most of its space on
- **Why:** This question requires the cause NCERT assigns to a named effect, demonstrated by the stem 'The factor that leads to Founder effect in a population is:'.
- **Note:** All four options are drawn from the chapter's own list of factors that disturb Hardy-Weinberg equilibrium, so position in the text does not single any one out; the pull was assigned on which factor the chapter presents as the usual cause of a frequency change.
<!--/ecat-->

## Q117

Biology · botany · Plant Kingdom

Genera like Selaginella and Salvinia produce two kinds of spores. Such plants are known as:

- (1) Homosporous
- **(2)** Heterosporous
- (3) Homosorus
- (4) Heterosorus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Selaginella and Salvinia produce two kinds of spores, small microspores and large megaspores; plants producing two kinds of spores are termed heterosporous, which is option $2$.

**Subtopic:** Pteridophytes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q117_9029761d_30102026.png?v=9029761da232)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plants producing two kinds of spores, macrospores and microspores, are heterosporous; producing a single kind of spore is homosporous
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Homosporous and heterosporous differ only in the prefix and are printed in the same two sentences, so a student who remembers the word-pair but not which prefix means 'two kinds' takes the other half of it
- **Why:** This question requires the term NCERT attaches to two named genera, demonstrated by the stem 'Genera like Selaginella and Salvinia produce two kinds of spores. Such plants are known as:'. Swap test applied: replace homosporous with an unlike word and the pull dies, so the shared ending and the swapped prefix are what carry the student.
<!--/ecat-->

## Q118

Biology · botany · Ecosystem

In the equation $\mathrm{GPP - R = NPP}$ R represents

- (1) Environment factor
- **(2)** Respiration losses
- (3) Radiant energy
- (4) Retardation factor

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. NPP is what is left of GPP after the producers' own respiration, so $\mathrm{GPP} - R = \mathrm{NPP}$ means $R$ = respiration losses, which is option $2$.

**Subtopic:** Productivity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q118_234961e6_30102026.png?v=234961e620c5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In GPP - R = NPP the term subtracted is respiration loss, the energy the producers themselves spend, and what remains is the net primary productivity available to consumers
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  R is expanded from its initial letter, and radiant energy is a real quantity in the same productivity section, so a student who recognises the equation but not the term reads the symbol as the other R word the topic supplies
- **Why:** This question requires the term NCERT's own equation uses for the subtracted quantity, demonstrated by the stem 'In the equation GPP - R = NPP R represents'. Swap test applied: two options are R words and replacing them with unlike words kills the pull, so the resemblance of the initial carries the student and this is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q119

Biology · botany · Plant Kingdom

Which of the following plants is monoecious?

- (1) Marchantia polymorpha
- (2) Cycas circinalis
- (3) Carica papaya
- **(4)** Chara

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Monoecious means male and female sex organs are borne on the same plant.
2. $Marchantia\ polymorpha$ has separate male and female thalli (antheridiophore and archegoniophore on different plants), so it is dioecious.
3. $Cycas$ has male cones and megasporophylls on separate plants, so it is dioecious.
4. $Carica\ papaya$ has separate male and female plants, so it is dioecious.
5. $Chara$ bears the oogonium (nucule) and antheridium (globule) on the same thallus, so it is monoecious, which is option $4$.

**Subtopic:** Chlorophyceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q119_55238cf2_30102026.png?v=55238cf26238)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A monoecious plant bears both male and female reproductive structures on the same individual, which is how NCERT prints Chara against the dioecious Marchantia
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Chara and Marchantia are printed as the two panels of one figure, one labelled monoecious and the other dioecious, so a student who remembers the figure but not which panel carries which label picks the plant beside the answer
- **Why:** This question requires the plant NCERT prints as monoecious, demonstrated by the stem 'Which of the following plants is monoecious?' with Chara against three plants the book prints as dioecious.
- **Note:** All three wrong options are plants the text describes as dioecious, so a student holding the two terms the right way round can exclude every one of them; what separates the pull is which of the three is printed next to the key.
<!--/ecat-->

## Q120

Biology · botany · Ecosystem

The amount of nutrients such as carbon, nitrogen, phosphorus and calcium

- **(1)** Standing state
- (2) Standing crop
- (3) Climax
- (4) Climax community

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT defines the amount of nutrients such as carbon, nitrogen, phosphorus and calcium present in the soil at any given time as the standing state, which is option $1$ (standing crop is the living biomass at a time).

**Subtopic:** Nutrient Cycling · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 50)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q120_599223c4_30102026.png?v=599223c4f529)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The quantity of nutrients held in the soil at a given moment is the standing state; standing crop is the biomass of living material present at a trophic level
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the stored stem stops mid-sentence after 'carbon, nitrogen, phosphorus and calcium', with no predicate and no blank, so what the question asks of those nutrients is not in the record and any route to a wrong option would be inferred from words we do not have
- **Why:** This question requires the term NCERT gives for a quantity of soil nutrients, demonstrated by the surviving stem words 'The amount of nutrients such as carbon, nitrogen, phosphorus and calcium' set against four ecosystem terms.
- **Note:** Stem truncated in our record: the clause that completes the definition and poses the question is missing, so no trap is written (rulebook 0.5 and section 7). A reviewer holding the printed paper should check the standing state / standing crop pull on option 2 - the two terms differ by one word and the chapter prints both within the nutrient cycling section, one for the nutrient amount in the soil and one for the biomass - and whether options 3 and 4, climax and climax community, are a second near-identical pair.
<!--/ecat-->

## Q121

Biology · botany · Sexual Reproduction in Flowering Plants

The term used for transfer of pollen grains from anthers of one plant to stigma of a different plant which, during pollination, brings genetically different types of pollen grains to stigma, is:

- (1) Chasmogamy
- (2) Cleistogamy
- **(3)** Xenogamy
- (4) Geitonogamy

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Pollen moving from the anther of one plant to the stigma of a genetically different plant is xenogamy (cross-pollination), which is option $3$.

**Subtopic:** Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q121_12226b47_30102026.png?v=12226b47e55c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Xenogamy is pollen transfer to the stigma of a different plant, the only kind of pollination that brings genetically different pollen; geitonogamy moves pollen between flowers of the same plant
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Geitonogamy is the entry printed immediately before xenogamy and is also defined as pollen reaching ANOTHER flower, so a student who remembers 'another' but not whether the other flower is on the same plant takes the preceding term
- **Why:** This question requires the term NCERT defines for one kind of pollen transfer, demonstrated by the stem's words 'from anthers of one plant to stigma of a different plant'.
- **Note:** Swap test applied: all four options end in -gamy, so the shared ending discriminates nothing, and what carries the student to geitonogamy is its position as the neighbouring definition about another flower - nearby_fact, not look_alike_term.
<!--/ecat-->

## Q122

Biology · botany · Anatomy of Flowering Plants

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Lenticels | (i) | Phellogen |
| (b) | Cork cambium | (ii) | Suberin deposition |
| (c) | Secondary cortex | (iii) | Exchange of gases |
| (d) | Cork | (iv) | Phelloderm |

- (1) (a)- (ii); (b) - (iii); (c) - (iv);(d) - (i)
- (2) (a)- (iv); (b) - (ii); (c) - (i);(d) - (iii)
- (3) (a)- (iv); (b) - (i); (c) - (iii);(d) - (ii)
- **(4)** (a)- (iii); (b) - (i); (c) - (iv);(d) - (ii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Lenticels are openings in the bark for exchange of gases: (a)-(iii).
2. Cork cambium is also called phellogen: (b)-(i).
3. Secondary cortex is also called phelloderm: (c)-(iv).
4. Cork (phellem) cells have suberin deposited in their walls: (d)-(ii).
5. The match $a$-$iii$, $b$-$i$, $c$-$iv$, $d$-$ii$ is option $4$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q122_09d73891_30102026.png?v=09d73891ae43)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In secondary growth the cork cambium is the phellogen, the cork it cuts outwards is suberised, the secondary cortex it cuts inwards is the phelloderm, and lenticels are the openings that let gases through
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Phellogen, phellem and phelloderm are one family of near-identical words, so a student who can place only phellogen gives the remaining phello- word to the remaining unfamiliar item, the lenticels, and sends the plain-English 'exchange of gases' to the secondary cortex.
- **Why:** This question requires the stated membership of the periderm, demonstrated by list II's '(i) Phellogen' and '(iv) Phelloderm' against list I's '(b) Cork cambium' and '(c) Secondary cortex'.
- **Note:** Swap test applied: replacing 'Phelloderm' with 'secondary cortex layer' makes the pairing immediate, so the likeness between the phello- words is the pull and the label is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q123

Biology · both · Biotechnology: Principles and Processes

DNA strands on a gel stained with ethidium bromide when viewed under UV radiation, appear as:

- (1) Dark red bands
- (2) Bright blue bands
- (3) Yellow bands
- **(4)** Bright orange bands

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Ethidium bromide binds DNA and fluoresces under UV radiation, so the DNA fragments on the gel show up as bright orange bands, which is option $4$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q123_a4329310_30102026.png?v=a43293104430)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** DNA fragments on an agarose gel are made visible by staining with ethidium bromide and exposing the gel to UV light, which makes them fluoresce as bright orange bands
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  What is remembered is the phrase 'bright bands under UV', and the colour is then supplied by the other thing named in the same sentence - the UV lamp, whose own glow is violet-blue - instead of by the dye's fluorescence
- **Why:** This question requires the observation a named bench procedure yields, demonstrated by the stem 'DNA strands on a gel stained with ethidium bromide when viewed under UV radiation, appear as:'.
<!--/ecat-->

## Q124

Biology · both · Cell Cycle and Cell Division

Which of the following stages of meiosis involves division of centromere?

- **(1)** Anaphase II
- (2) Telophase II
- (3) Metaphase I
- (4) Metaphase II

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In meiosis I (including metaphase I) centromeres stay intact; homologous chromosomes separate. Centromeres split at anaphase II so sister chromatids move to opposite poles, which is option $1$.

**Subtopic:** Anaphase II and Telophase II · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q124_fc69d659_30102026.png?v=fc69d6592973)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The centromere splits only once in meiosis, at anaphase II, when the sister chromatids finally separate; through the whole of meiosis I it stays intact
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Metaphase II is where the centromere is named in the text, as the point the spindle fibres attach to, so a student who searches memory for the stage the word centromere appears in picks the stage before the one where it divides
- **Why:** This question requires the meiotic stage NCERT ties the splitting of the centromere to, demonstrated by the stem 'Which of the following stages of meiosis involves division of centromere?'.
<!--/ecat-->

## Q125

Biology · both · Principles of Inheritance and Variation

The production of gametes by the parents, formation of zygotes, the $\mathrm{F_1}$ and $\mathrm{F_2}$ plants can be understood from a diagram called

- **(1)** Punnett square
- (2) Net square
- (3) Bullet square
- (4) Punch square

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The diagram showing parental gametes, zygote formation and $\mathrm{F_1}$ and $\mathrm{F_2}$ plants is the Punnett square (devised by R.C. Punnett), which is option $1$.

**Subtopic:** Monohybrid Cross · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q125_6fc5360f_30102026.png?v=6fc5360f2722)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The grid used to work out gamete combinations, zygotes and the F1 and F2 generations of a cross is the Punnett square, named after its deviser
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Punch and Punnett open with the same syllable, so a student who has the name by sound from class rather than from the printed page picks the near-spelling
- **Why:** This question requires the name NCERT gives one diagram, demonstrated by the stem 'can be understood from a diagram called' with three invented squares beside it. Swap test applied: only 'Punch' resembles 'Punnett', and replacing it with an unlike word kills the pull, so the resemblance is the device.
<!--/ecat-->

## Q126

Biology · botany · Plant Growth and Development

Plants follow different pathways in response to environment or phases of life to form different kinds of structures. This ability is called

- **(1)** Plasticity
- (2) Maturity
- (3) Elasticity
- (4) Flexibility

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Forming different structures by following different pathways in response to environment or phase of life is defined as plasticity (e.g. heterophylly in cotton, coriander, larkspur, buttercup), which is option $1$.

**Subtopic:** Development and Plasticity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q126_4972cd77_30102026.png?v=4972cd778690)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plasticity is a plant's ability to form different kinds of structures in response to the environment or to its phase of life, as in heterophylly in cotton and coriander
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Plasticity and elasticity are the pair of -icity words learnt together, so a student who recognises the stem as the sentence defining one of them reaches for the other
- **Why:** This question requires the term NCERT attaches to a described ability, demonstrated by the stem reproducing the textbook sentence 'Plants follow different pathways in response to environment or phases of life to form different kinds of structures'. Swap test applied: elasticity resembles plasticity directly, and renaming it to an unlike word removes the pull, so look_alike_term.
<!--/ecat-->

## Q127

Biology · botany · Organisms and Populations

Amensalism can be represented as :

- (1) Species A ( - ) ; Species B ( - )
- (2) Species A ( +) ; Species B (0)
- **(3)** Species A ( - ) ; Species B (0)
- (4) Species A ( + );Species B ( + )

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In amensalism one species is harmed ($-$) and the other is unaffected ($0$), so the interaction is $(-,\,0)$, which is option $3$.

**Subtopic:** Commensalism and Ammensalism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q127_02da687e_30102026.png?v=02da687e229b)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Amensalism: one species is harmed while the other is neither helped nor harmed, so its sign pair is (-) and (0)
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Commensalism' and 'amensalism' differ by a syllable and both carry a (0) for the unaffected partner, so a student who has stored 'one species unaffected' and reaches for the better-remembered commensalism supplies its (+) for Species A. NCERT's interaction table gives (+)(0) to commensalism and (-)(0) to amensalism.
- **Why:** This question requires the sign pair NCERT assigns to amensalism in its table of interspecific interactions, demonstrated by the options being nothing but four sign combinations, 'Species A ( - ) ; Species B (0)' and its rivals.
- **Note:** The pattern classifier called this statement_options, but each option is a two-part sign set accepted or rejected whole; the nearest qtype in this axis is two_part, which is what is recorded.
<!--/ecat-->

## Q128

Biology · both · Strategies for Enhancement in Food Production

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Protoplast fusion | (i) | Totipotency |
| (b) | Plant tissue culture | (ii) | Pomato |
| (c) | Meristem culture | (iii) | Somaclones |
| (d) | Micropropagation | (iv) | Virus free plants |

- (1) (a)- (iii); (b) - (iv); (c) - (i);(d) - (ii)
- (2) (a)- (iv); (b) - (iii); (c) - (ii);(d) - (i)
- (3) (a)- (iii); (b) - (iv); (c) - (ii);(d) - (i)
- **(4)** (a)- (ii); (b) - (i); (c) - (iv);(d) - (iii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Protoplast fusion of potato and tomato protoplasts gives the somatic hybrid pomato: $(a) \rightarrow (ii)$.
2. Plant tissue culture depends on totipotency, the ability of a cell to grow into a whole plant: $(b) \rightarrow (i)$.
3. Meristem (apical/axillary) culture is used to get virus-free plants: $(c) \rightarrow (iv)$.
4. Micropropagation produces genetically identical plants, called somaclones: $(d) \rightarrow (iii)$.
5. The match $(a)-(ii), (b)-(i), (c)-(iv), (d)-(iii)$ is option $4$.

**Subtopic:** Tissue Culture · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q128_d4c2767d_30102026.png?v=d4c2767d5b85)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tissue culture rests on totipotency, meristem culture gives virus-free plants, micropropagation gives somaclones, and protoplast fusion gave the pomato
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Protoplast fusion is taught as somatic hybridisation and 'Somaclones' carries the same soma-, so the two words pull together; somaclones are the genetically identical plants micropropagation turns out, while the named product of protoplast fusion is the pomato.
- **Why:** This question requires the stated product of each culture technique, demonstrated by list II's '(ii) Pomato' and '(iv) Virus free plants'.
- **Note:** Swap test applied: rename somaclones 'identical clones from culture' and the pull to protoplast fusion dies, so likeness rather than position is doing the work. All three wrong codes carry a route here, so none is recorded as filler.
<!--/ecat-->

## Q129

Biology · botany · Organisms and Populations

Inspite of interspecific competition in nature, which mechanism the competing species might have evolved for their survival?

- (1) Mutualism
- (2) Predation
- **(3)** Resource partitioning
- (4) Competitive release

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. As NCERT teaches, species that compete for the same resource can coexist by using it differently, for example different foraging times or patterns, as MacArthur's warblers do. This is resource partitioning, option $3$.

**Subtopic:** Competition · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q129_c711db68_30102026.png?v=c711db6821eb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Resource partitioning: two competing species coexist by differing in when or where they use the shared resource rather than by one eliminating the other
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  'Competitive release' is the other competition term NCERT prints in the same passage, and its name repeats the stem's own word, so a student hunting that passage for a named mechanism lands on it. It names what a species does after its competitor has been removed, not how two competitors survive together.
- **Why:** This question requires the mechanism NCERT names for coexistence under competition, demonstrated by the stem's 'which mechanism the competing species might have evolved for their survival' with three other named interaction phenomena offered beside it.
<!--/ecat-->

## Q130

Biology · botany · Plant Kingdom

Which of the following algae contains mannitol as reserve food material?

- (1) Volvox
- (2) Ulothrix
- **(3)** Ectocarpus
- (4) Gracilaria

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Phaeophyceae (brown algae) store food as complex carbohydrates in the form of laminarin or mannitol; Ectocarpus is a brown alga, so the answer is option $3$.

**Subtopic:** Phaeophyceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q130_b23b12c3_30102026.png?v=b23b12c342e1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Brown algae (Phaeophyceae) store food as mannitol and laminarin, green algae as starch and red algae as floridean starch
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Gracilaria is printed in the Rhodophyceae row of NCERT's algae table, directly under the Phaeophyceae row that carries mannitol, so a student who has the table's shape but not which marine genus sits in which row picks up the example from the neighbouring row. Gracilaria's stored food is floridean starch.
- **Why:** This question requires the stored-food line NCERT prints for Phaeophyceae, demonstrated by the stem's 'which of the following algae contains mannitol as reserve food material' with one genus offered from each of three algal classes.
- **Note:** Likeness test applied: Ectocarpus and Gracilaria resemble each other in no part, so what carries a student to Gracilaria is its position in the table beside the brown algae, which makes the label nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q131

Biology · botany · Plant Growth and Development

The site of perception of light in plants during photoperiodism is:

- (1) Axillary bud
- **(2)** Leaf
- (3) Shoot apex
- (4) Stem

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Photoperiodic stimulus is perceived by the $\text{leaf}$ and transmitted to the shoot apex to induce flowering, so the answer is option $2$.

**Subtopic:** Photoperiodism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q131_3e68f3d4_30102026.png?v=3e68f3d41dda)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In photoperiodism the leaf perceives the light and dark periods, and the floral stimulus then travels to the shoot apex where flowering is expressed
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  NCERT prints the shoot apex as where the hormonal floral stimulus arrives and flowers are produced, so a student holding 'flowering happens at the shoot apex' moves the perception there as well. The apex is the site of the response; perception is in the leaf.
- **Why:** This question requires the organ NCERT names as perceiving light in photoperiodism, demonstrated by the stem's 'site of perception of light in plants during photoperiodism' set against three organs that belong to the response end of the same passage.
<!--/ecat-->

## Q132

Biology · botany · Photosynthesis in Higher Plants

The first stable product of $\mathrm{CO_2}$ fixation in sorghum is:

- (1) Succinic acid
- (2) Phosphoglyceric acid
- (3) Pyruvic acid
- **(4)** Oxaloacetic acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Sorghum is a $\mathrm{C_4}$ plant, so primary $\mathrm{CO_2}$ fixation in mesophyll cells is by PEP carboxylase: $\mathrm{PEP + CO_2 \rightarrow}$ oxaloacetic acid (OAA), the first stable product, which is option $4$.

**Subtopic:** The C₄ Pathway · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 53)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q132_d5a0039a_30102026.png?v=d5a0039af565)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sorghum is a C4 plant, and the C4 pathway fixes CO2 first into the four-carbon oxaloacetic acid in the mesophyll cells
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  3-phosphoglyceric acid is the first stable product of the Calvin cycle and so the answer for any C3 plant, and a student who answers 'first stable product of CO2 fixation' without registering which plant is named gives it. The one word 'sorghum' is what makes oxaloacetic acid the answer, because NCERT lists sorghum among its C4 plants.
- **Why:** This question requires the first fixation product of the C4 pathway together with the fact that the named plant uses it, demonstrated by the stem's 'in sorghum' being the only word that rules out the Calvin-cycle answer 'Phosphoglyceric acid'.
<!--/ecat-->

## Q133

Biology · both · Cell: The Unit of Life

Match List -I with LIst – II

| List-I | | List-II | |
|---|---|---|---|
| (a) | Cristae | (i) | Primary con striction in chromosome |
| (b) | Thylakoide | (ii) | Disc-shaped sacs in Golgi apparatus |
| (c) | Centromere | (iii) | Infoldings in mitochondria |
| (d) | Cisternae | (iv) | Flattened membranous sacs in stroma of plastids |

- **(1)** (a)-(iii), (b)-(iv), (c)- (i), (d)-(ii)
- (2) (a)-(ii), (b)-(iii), (c)- (iv), (d)-(i)
- (3) (a)-(iv), (b)-(iii), (c)- (ii), (d)-(i)
- (4) (a)-(i), (b)-(iv), (c)- (iii), (d)-(ii)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Cristae $\to$ infoldings in mitochondria (iii); thylakoids $\to$ flattened membranous sacs in stroma of plastids (iv); centromere $\to$ primary constriction in chromosome (i); cisternae $\to$ disc-shaped sacs in Golgi apparatus (ii); so (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii) is option $1$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q133_79f67b76_30102026.png?v=79f67b7649ee)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cristae are the mitochondrion's inner-membrane infoldings, thylakoids the chloroplast's stromal sacs, cisternae the Golgi's discs, and the centromere the chromosome's primary constriction
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Cristae and thylakoids are the two internal membrane systems taught side by side, one for each energy-converting organelle, and option 3 exchanges them — (a) to the sacs in the stroma, (b) to the infoldings in the mitochondria.
- **Why:** This question requires matching each named part to the organelle its description names, demonstrated by list II's '(iii) Infoldings in mitochondria' against list I's '(a) Cristae'.
- **Note:** Swap test applied: rename cristae and thylakoid and the exchange still works, because what is short is which organelle's membranes carry which name, so position in the chapter rather than likeness of the words is the pull.
<!--/ecat-->

## Q134

Biology · both · Molecular Basis of Inheritance

Complete the flow chart on central dogma.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q134_1f5c2186_30102026.png?v=1f5c21868bbc)

- **(1)** (a)-Replication; (b)-Transcription; (c) -Translation; (d)-Protein
- (2) (a)-Transduction; (b)-Translation; (c) -Replication; (d)-Protein
- (3) (a)-Replication; (b)-Transcription; (c) -Transduction; (d)-Protein
- (4) (a)-Translation; (b)-Replication; (c) -Transcription; (d)-Transduction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In the flow chart, (a) is the self-loop on DNA, which is replication; DNA $\rightarrow$ mRNA (b) is transcription; mRNA $\rightarrow$ (d) via (c) is translation, giving protein, so the answer is option $1$.

**Subtopic:** Central Dogma · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q134_e2747c28_30102026.png?v=e2747c289981)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Central dogma: DNA is copied by replication, read out into RNA by transcription, and that RNA is translated into protein
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first two arrows are filled exactly right here, replication then transcription, and only the third slot reads 'Transduction' instead of translation, so a student who fills the chart left to right and stops checking once the opening matches accepts the whole set. Transduction is the transfer of genes by a virus and is no step of the central dogma.
- **Why:** This question requires naming each arrow of the printed central-dogma flow chart, demonstrated by every option supplying a complete set '(a)-...; (b)-...; (c)-...; (d)-Protein' so that one wrong slot fails the whole option.
- **Note:** The figure was not opened at this step; the slot order was taken from the option text and the stem's named topic, both of which fix replication, transcription, translation, protein. The pattern classifier called this statement_options, but each option is a four-slot set accepted or rejected whole, so two_part is recorded as the nearest shape on this axis.
<!--/ecat-->

## Q135

Biology · botany · Transport in Plants

Match List -I with List – II
Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Cohesion | (i) | More attraction in liquid phase |
| (b) | Adhesion | (ii) | Mutual attraction among water molecules |
| (c) | Surface tension | (iii) | Water loss in liquid phase |
| (d) | Guttation | (iv) | Attraction towards polar surfaces |

- (1) (a)-(iii), (b)-(i), (c)- (iv), (d)-(ii)
- (2) (a)-(ii), (b)-(i), (c)- (iv), (d)-(iii)
- **(3)** (a)-(ii), (b)-(iv), (c)- (i), (d)-(iii)
- (4) (a)-(iv), (b)-(iii), (c)- (ii), (d)-(i)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Cohesion is the mutual attraction among water molecules, so $(a)\to(ii)$; adhesion is attraction of water to polar surfaces, so $(b)\to(iv)$; surface tension arises because water molecules are more attracted to each other in the liquid phase than to the gas phase, so $(c)\to(i)$; guttation is loss of water in liquid form, so $(d)\to(iii)$, which is option $3$.

**Subtopic:** Water Movement up a Plant: Root Pressure and Guttation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q135_5938fc2e_30102026.png?v=5938fc2e00c1)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cohesion is water-to-water attraction, adhesion is water-to-polar-surface attraction, surface tension is the greater attraction in the liquid than in the gas phase, and guttation is water lost as liquid
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Attraction towards polar surfaces' carries the word surface, which pulls it towards Surface tension, and (i) 'More attraction in liquid phase' then reads as another molecule-to-molecule statement and goes to Adhesion.
- **Why:** This question requires the chapter's stated definitions, demonstrated by list II's '(i) More attraction in liquid phase' against list I's '(c) Surface tension'.
- **Note:** Swap test applied: rewrite (iv) as 'attraction towards wettable walls' and the pull to Surface tension dies, so the shared word is doing the work and the label is look_alike_term.
<!--/ecat-->

## Q136

Biology · botany · Photosynthesis in Higher Plants

Which of the following statements is incorrect?

- (1) Grana lamellae have both PS I and PS II
- **(2)** Cyclic photophosphorylation involves both PS I and PS II.
- (3) Both ATP and $\mathrm{NADPH + H^{+}}$ are synthesized during non-cyclic photophosphorylation.
- (4) Stroma lamellae have PS I only and lack NADP reductase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Cyclic photophosphorylation uses only PS I: electrons from $P_{700}$ cycle back via the electron transport chain, so PS II is not involved. Statement $2$ is therefore incorrect, while grana lamellae carry both PS I and PS II, non-cyclic photophosphorylation makes both ATP and $\mathrm{NADPH + H^{+}}$, and stroma lamellae have PS I only and lack NADP reductase. The answer is option $2$.

**Subtopic:** Cyclic and Non-Cyclic Photophosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 55)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q136_38167471_30102026.png?v=38167471b26f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Grana thylakoids carry both PS I and PS II, stroma lamellae carry only PS I and no NADP reductase, and cyclic photophosphorylation runs on PS I alone
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Hunting for a false claim, a student stops at the one statement written in absolute terms — 'PS I only and lack NADP reductase' — because an absolute claim is the easiest kind to suspect, and so never reaches the cyclic claim in option 2. The sentence is NCERT's own, so it answers 'which statement is correct', not the 'incorrect' the stem asked for.
- **Why:** This question requires the stated distribution of the two photosystems and what each kind of photophosphorylation uses, demonstrated by the stem's 'which of the following statements is incorrect' with 'Cyclic photophosphorylation involves both PS I and PS II' as the only claim NCERT contradicts.
- **Note:** The retired per-option vocabulary carried this device as true_statement_trap; on the live twelve-value axis its family is answers_other_question, since the option is true and answers the un-negated form of the stem.
<!--/ecat-->

## Q137

Biology · botany · Anatomy of Flowering Plants

Select the correct pair.

- **(1)** Cells of medullary rays that form part of cambial ring - Interfascicular cambium
- (2) Loose parenchyma cells rupturing the epidermis and forming a lens-shaped opening in bark - Spongy parenchyma
- (3) Large colorless empty cells in the epidermis of grass leaves – Subsidiary cells
- (4) In dicot leaves, vascular bundles are surrounded by large thick-walled cells– Conjunctive tissue

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Medullary ray cells next to the intrafascicular cambium become meristematic and form the $\text{interfascicular cambium}$, so pair $1$ is correct.
2. Loose parenchyma cells that rupture the epidermis to form a lens-shaped opening (lenticel) are complementary cells, not spongy parenchyma, so pair $2$ is wrong.
3. Large, colourless, empty epidermal cells in grass leaves are bulliform cells, not subsidiary cells, so pair $3$ is wrong.
4. In dicot leaves, the large thick-walled cells around vascular bundles are bundle sheath cells, not conjunctive tissue, so pair $4$ is wrong. The answer is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q137_3ab4d518_30102026.png?v=3ab4d518ac3a)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each anatomical term names one described structure: medullary-ray cells turning meristematic make the interfascicular cambium, loose complementary cells make a lenticel, bulliform cells sit in the grass epidermis and bundle-sheath cells ring the vascular bundle
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Bulliform cells and subsidiary cells are both printed as epidermal cells of a grass leaf in the same anatomy passage, so a student who stored the two names as a pair without their descriptions takes whichever comes first. The large, colourless, empty cells are bulliform; subsidiary cells are the ones flanking the guard cells.
- **Why:** This question requires the term NCERT attaches to each described structure, demonstrated by the stem's 'Select the correct pair' with every option carrying a description and a name that must both hold at once.
- **Note:** The pattern classifier called this statement_options, but each option is a description-and-term pair accepted or rejected whole with no two printed columns, so two_part is recorded rather than match_columns. Likeness test on the trap: bulliform and subsidiary resemble each other in no part, so position in the same passage is what carries the student, which makes it nearby_fact.
<!--/ecat-->

## Q138

Biology · both · Molecular Basis of Inheritance

Identify the correct statement.

- (1) The coding strand in a transcription unit is copied to an mRNA
- (2) Split gene arrangement is characteristic of prokaryotes
- (3) In capping, methyl guanosine triphosphate is added to the 3’ end of hnRNA.
- **(4)** RNA polymerase binds with Rho factor to terminate the process of transcription in bacteria.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option $1$ is false: the template strand ($3' \rightarrow 5'$) is copied into mRNA, not the coding strand.
2. Option $2$ is false: split genes (exons and introns) are characteristic of eukaryotes.
3. Option $3$ is false: in capping, methyl guanosine triphosphate is added to the $5'$ end of hnRNA; the $3'$ end gets the poly-A tail.
4. Option $4$ is true: RNA polymerase associates transiently with the $\rho$ (rho) factor to terminate transcription in bacteria, so the answer is option $4$.

**Subtopic:** Transcription · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 55)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q138_438f8b77_30102026.png?v=438f8b7741f2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In transcription the template strand is copied, capping adds methyl guanosine triphosphate to the 5' end, split genes belong to eukaryotes, and in bacteria Rho factor acting with RNA polymerase terminates the process
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  The strand called 'coding' sounds like the strand whose code is read out, so a student goes to it for the copying step. Copying is the right event at the wrong strand: the template strand is transcribed, and the other is called coding only by convention.
- **Why:** This question requires the stated facts of transcription and RNA processing, demonstrated by three options each moving one printed element — the strand copied, the end capped, the group with split genes — away from where NCERT puts it.
<!--/ecat-->

## Q139

Biology · both · Cell Cycle and Cell Division

Match List -I with LIst – II

| List-I | | List-II | |
|---|---|---|---|
| (a) | S phase | (i) | Proteins are synthesized |
| (b) | $\mathrm{G_2}$ phase | (ii) | Inactive phase |
| (c) | Quiescent stage | (iii) | Interval between mitosis and initiation of DNA replication |
| (d) | $\mathrm{G_1}$ phase | (iv) | DNA replication |

- **(1)** (a)-(iv), (b)-(i), (c)- (ii), (d)-(iii)
- (2) (a)-(ii), (b)-(iv), (c)- (iii), (d)-(i)
- (3) (a)-(iii), (b)-(ii), (c)- (i), (d)-(iv)
- (4) (a)-(iv), (b)-(ii), (c)- (iii), (d)-(i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. S phase is when DNA replication takes place, so (a)-(iv).
2. In $\mathrm{G_2}$ phase proteins are synthesized in preparation for mitosis, so (b)-(i).
3. The quiescent stage ($\mathrm{G_0}$) is the inactive phase, so (c)-(ii).
4. $\mathrm{G_1}$ phase is the interval between mitosis and initiation of DNA replication, so (d)-(iii).
5. The match (a)-(iv), (b)-(i), (c)-(ii), (d)-(iii) is option $1$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q139_9ab043cd_30102026.png?v=9ab043cdc048)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** S replicates the DNA, G1 is the gap between mitosis and replication, G2 is where proteins are made before mitosis, and the quiescent stage is the inactive G0
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Growth and synthesis are what both gap phases are about, and the chapter prints 'proteins are synthesised' under G2 and 'the interval between mitosis and the initiation of DNA replication' under G1; option 4 exchanges the two, which then forces G1's own description onto the quiescent stage.
- **Why:** This question requires each phase's stated event, demonstrated by list II's '(iii) Interval between mitosis and initiation of DNA replication' against list I's '(d) $\mathrm{G_1}$ phase'.
- **Note:** Swap test applied: rename the two gap phases and the exchange survives, because what is forgotten is which gap the protein synthesis is printed under, so the label is nearby_fact rather than look_alike_term despite the labels $\mathrm{G_1}$ and $\mathrm{G_2}$ differing by one character.
<!--/ecat-->

## Q140

Biology · botany · Mineral Nutrition

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Nitrococcus | (i) | Denitrification |
| (b) | Rhizobium | (ii) | Conversion of ammonia to nitrite |
| (c) | Thiobacillus | (iii) | Conversion of nitrite to nitrate |
| (d) | Nitrobacter | (iv) | Conversion of atmospheric nitrogen to ammonia |

- (1) (a)- (iii); (b) - (i); (c) - (iv);(d) - (ii)
- (2) (a)- (iv); (b) - (iii); (c) - (ii);(d) - (i)
- **(3)** (a)- (ii); (b) - (iv); (c) - (i);(d) - (iii)
- (4) (a)- (i); (b) - (ii); (c) - (iii);(d) - (iv)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\text{Nitrococcus}$ oxidises $NH_3 \to NO_2^-$, so (a)-(ii).
2. $\text{Rhizobium}$ fixes atmospheric $N_2 \to NH_3$, so (b)-(iv).
3. $\text{Thiobacillus}$ carries out denitrification ($NO_3^- \to N_2$), so (c)-(i).
4. $\text{Nitrobacter}$ oxidises $NO_2^- \to NO_3^-$, so (d)-(iii); this matches option $3$.

**Subtopic:** Nitrogen Fixation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q140_3d797e85_30102026.png?v=3d797e85cf55)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nitrification runs in two steps with different bacteria - Nitrococcus oxidises ammonia to nitrite and Nitrobacter nitrite to nitrate - while Rhizobium fixes nitrogen and Thiobacillus denitrifies
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The two nitrifying steps are printed one after the other, and option 1 is the only code that exchanges their organisms, giving Nitrococcus the nitrite-to-nitrate step and Nitrobacter the ammonia-to-nitrite step.
- **Why:** This question requires each organism's stated step in the nitrogen cycle, demonstrated by list II's '(ii) Conversion of ammonia to nitrite' and '(iii) Conversion of nitrite to nitrate'.
- **Note:** Swap test applied: replace the two organism names with unlike words and the exchange still works, because what is short is which of the two consecutive steps each bacterium runs, so position carries it and not the shared 'Nitro-'.
<!--/ecat-->

## Q141

Biology · botany · Morphology of Flowering Plants

Match list I with list II.

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/figures_agent/q141_86c8cae2_30102026.png?v=86c8cae25d8c)

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\%\,\text{⚥}\,\mathrm{K_{(5)}\,C_{1+2+(2)}\,A_{(9)+1}\,\underline{G}_{1}}$ | (i) | Brassicaceae |
| (b) | $\oplus\,\text{⚥}\,\mathrm{K_{(5)}}\,\overset{\frown}{\mathrm{C_{(5)}\,A_{5}}}\,\mathrm{\underline{G}_{2}}$ | (ii) | Liliaceae |
| (c) | $\oplus\,\text{⚥}\,\overset{\frown}{\mathrm{P_{(3+3)}\,A_{3+3}}}\,\mathrm{\underline{G}_{(3)}}$ | (iii) | Fabaceae |
| (d) | $\oplus\,\text{⚥}\,\mathrm{K_{2+2}\,C_{4}\,A_{2-4}\,\underline{G}_{(2)}}$ | (iv) | Solanaceae |

- (1) (a)- (ii); (b) - (iii); (c) - (iv);(d) - (i)
- (2) (a)- (iv); (b) - (ii); (c) - (i);(d) - (iii)
- **(3)** (a)- (iii); (b) - (iv); (c) - (ii);(d) - (i)
- (4) (a)- (i); (b) - (ii); (c) - (iii);(d) - (iv)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. (a) $\%\,K_{(5)}\,C_{1+2+(2)}\,A_{(9)+1}\,\underline{G}_1$: zygomorphic, vexillary corolla, diadelphous stamens, monocarpellary ovary, so Fabaceae (iii).
2. (b) $\oplus\,K_{(5)}\,\overset{\frown}{C_{(5)}A_5}\,\underline{G}_2$: actinomorphic, epipetalous stamens, bicarpellary superior ovary, so Solanaceae (iv).
3. (c) $\oplus\,\overset{\frown}{P_{(3+3)}A_{3+3}}\,\underline{G}_{(3)}$: trimerous perianth, epiphyllous stamens, tricarpellary syncarpous ovary, so Liliaceae (ii).
4. (d) $\oplus\,K_{2+2}\,C_4\,A_{2+4}\,\underline{G}_{(2)}$: cruciform corolla, tetradynamous stamens, bicarpellary ovary, so Brassicaceae (i).
5. The match (a)-(iii), (b)-(iv), (c)-(ii), (d)-(i) is option $3$.

**Subtopic:** Solanaceae, Malvaceae and Cruciferae, Leguminosae, Compositae, Gramineae and Fabaceae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 56)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q141_083941a8_30102026.png?v=083941a8ca0a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A floral formula is decoded from its symbols: P for a perianth, % for zygomorphy, and stamen notations like $\mathrm{A_{(9)+1}}$ or $\mathrm{A_{2-4}}$ name the family
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all three wrong codes pair Liliaceae with a formula printed with K and C, while (c) is the only row printed with a perianth, $\mathrm{P_{(3+3)}}$; I also checked the one exchange the two $\mathrm{K_{(5)}}$ formulae invite, and the single code offering it has to give the zygomorphic $\mathrm{A_{(9)+1}}$ formula to Liliaceae as well
- **Why:** This question requires decoding four printed floral formulae, demonstrated by list I's '(c) $\oplus$ ⚥ $\mathrm{P_{(3+3)}\,A_{3+3}}\,\underline{\mathrm{G}}_{(3)}$' against list II's '(ii) Liliaceae'.
- **Note:** has_figure is true and the printed image carries the formulae, but list I reproduces all four in full, so the question was readable at this step. no_trap here is a finding: with the perianth notation appearing in only one row, no wrong code survives a single symbol check.
<!--/ecat-->

## Q142

Biology · both · Biomolecules

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Protein | (i) | $\mathrm{C=C}$ double bonds |
| (b) | Unsaturated fatty acid | (ii) | Phosphodiester bonds |
| (c) | Nucleic acid | (iii) | Glycosidic bonds |
| (d) | Polysaccharide | (iv) | Peptide bonds |

- (1) (a)- (ii); (b) - (i); (c) - (iv);(d) - (iii)
- (2) (a)- (iv); (b) - (iii); (c) - (i);(d) - (ii)
- **(3)** (a)- (iv); (b) - (i); (c) - (ii);(d) - (iii)
- (4) (a)- (i); (b) - (iv); (c) - (iii);(d) - (ii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Amino acids in a protein are joined by peptide bonds, so $(a) \rightarrow (iv)$; unsaturated fatty acids contain $\mathrm{C=C}$ double bonds, so $(b) \rightarrow (i)$; nucleotides in a nucleic acid are joined by phosphodiester bonds, so $(c) \rightarrow (ii)$; monosaccharides in a polysaccharide are joined by glycosidic bonds, so $(d) \rightarrow (iii)$. This matches option $3$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q142_36e3d5b5_30102026.png?v=36e3d5b587db)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each macromolecule class is defined by its own linkage - peptide for protein, phosphodiester for nucleic acid, glycosidic for polysaccharide, C=C for an unsaturated fatty acid
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  each list II bond names its own class inside its own word, and every wrong code breaks at least two of those four links; I checked the one textual hook that could cross them, the N-glycosidic linkage the chapter prints for a nucleoside, and the only code offering nucleic acid to glycosidic also gives the peptide bond to a fatty acid
- **Why:** This question requires each class's characteristic linkage, demonstrated by list II's '(ii) Phosphodiester bonds' against list I's '(c) Nucleic acid'.
- **Note:** no_trap is recorded as a finding, not a gap: three of the four list II entries carry their class in their own name, so a single word in each row decides it and no wrong code keeps more than one defensible pair.
<!--/ecat-->

## Q143

Biology · botany · Respiration in Plants

Which of the following statements is incorrect?

- (1) ATP is synthesized through complex V
- (2) Oxidation-reduction reactions produce proton gradient in respiration.
- (3) During aerobic respiration, role of oxygen is limited to the terminal stage
- **(4)** In ETC (Electron Transport Chain), one molecule of $\mathrm{NADH + H^+}$ gives rise to 2 ATP molecules, and one $\mathrm{FADH_2}$ gives rise to 3 ATP molecules

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Complex V is ATP synthase, so ATP is made through complex V: option $1$ is correct.
2. Redox reactions in the ETC pump protons and set up the proton gradient: option $2$ is correct.
3. Oxygen acts only as the final electron acceptor at the end of the ETC, the terminal stage: option $3$ is correct.
4. Per NCERT, one $\mathrm{NADH + H^+}$ gives $3$ ATP and one $\mathrm{FADH_2}$ gives $2$ ATP. Option $4$ swaps these values, so it is the incorrect statement.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q143_448678b7_30102026.png?v=448678b78d8b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the electron transport chain one NADH yields 3 ATP and one FADH2 yields 2 ATP, and oxygen's only role is to accept the electrons at the end
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A student who holds that aerobic respiration needs oxygen throughout reads 'limited to the terminal stage' as too narrow and ends the hunt for the false statement there, never checking the two ATP numbers in option 4. The sentence is NCERT's own, so it answers 'which statement is correct' rather than the 'incorrect' the stem asked for.
- **Why:** This question requires the stated ATP yields of the respiratory chain, demonstrated by option 4 printing 'one molecule of NADH + H+ gives rise to 2 ATP molecules, and one FADH2 gives rise to 3 ATP molecules' with the two figures exchanged.
<!--/ecat-->

## Q144

Biology · both · Molecular Basis of Inheritance

DNA fingerprinting involves identifying differences in some specific regions in DNA sequence, called as:

- (1) Single nucleotides
- (2) Polymorphic DNA
- (3) Satellite DNA
- **(4)** Repetitive DNA

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. As NCERT teaches it, DNA fingerprinting identifies differences in specific regions of the DNA sequence called repetitive DNA, which is option $4$.

**Subtopic:** DNA Fingerprinting · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q144_d54c66bc_30102026.png?v=d54c66bc8f86)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA fingerprinting compares repetitive DNA, the regions where a short stretch of sequence is repeated many times over
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Satellite DNA is the term in the sentences that follow this one, where the repetitive DNA separating out as small peaks is given that name, and mini- and micro-satellites are what the chapter then says fingerprinting uses. A student reading forward one sentence hands back the follow-on term instead of the one the stem's own words define.
- **Why:** This question requires the name NCERT gives these regions, demonstrated by the stem reproducing its sentence 'differences in some specific regions in DNA sequence, called as' with three other real sequence terms offered.
- **Note:** The pattern classifier returned arrange_in_order, but nothing in the stem or options is a sequence to be put in order: it is one blank with four named terms, so mcq is recorded.
<!--/ecat-->

## Q145

Biology · botany · Biological Classification

Which of the following statements is correct?

- (1) Organisms that depend on living plants are called saprophytes
- (2) Some of the organisms can fix atmospheric nitrogen in specialized cells called sheath cells
- (3) Fusion of two cells is called Karyogamy.
- **(4)** Fusion of protoplasms between two motile or non-motile gametes is called plasmogamy

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Option $1$ is false: organisms that depend on living plants are parasites; saprophytes feed on dead organic matter.
2. Option $2$ is false: cyanobacteria such as Nostoc and Anabaena fix atmospheric nitrogen in specialised cells called heterocysts, not sheath cells.
3. Option $3$ is false: karyogamy is the fusion of two nuclei, not of two cells.
4. Option $4$ is true: fusion of protoplasms between two motile or non-motile gametes is plasmogamy, so the answer is option $4$.

**Subtopic:** Kingdom Fungi · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 57)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q145_4b2d9d1a_30102026.png?v=4b2d9d1ac712)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In fungal sexual reproduction plasmogamy is the fusion of the two protoplasms and karyogamy the fusion of the two nuclei that follows it
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Plasmogamy and karyogamy are two '-gamy' words printed one after the other in the same sentence, and a student who has not decoded the prefixes attaches cell fusion to whichever of them comes to mind. Karyogamy is the fusion of nuclei; the fusion of cells is plasmogamy.
- **Why:** This question requires the stated definitions of the fungal fusion stages, demonstrated by the key reading 'Fusion of protoplasms between two motile or non-motile gametes is called plasmogamy' while option 3 attaches the same event to karyogamy.
<!--/ecat-->

## Q146

Biology · both · Biotechnology and Its Applications

Now a days it is possible to detect the mutated gene causing cancer by allowing radioactive probe to hybridise its complementary DNA in a clone of cells, followed by its detection using autoradiography because :

- **(1)** mutated gene does not appear on a Photographic film as the probe has no complementarity with it
- (2) mutated gene does not appear on Photographic film as the probe has complementarity with it
- (3) mutated gene partially appears on a photographic film
- (4) mutated gene completely and clearly appears on a photographic film.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The radioactive probe is complementary to the normal DNA sequence, so it hybridises only there and the mutated sequence lacks complementarity; hence the clone carrying the mutated gene does not appear on the photographic film, which is option $1$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q146_99fd8d3c_30102026.png?v=99fd8d3c0989)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A radioactive probe is built against the normal sequence, so the clone carrying the mutated gene is the one that leaves no spot on the film
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The stem's own words 'hybridise its complementary DNA' put complementarity in front of a student who remembers the result — the mutant clone does not show up — but not the clause that explains it, and this option pairs the remembered result with complementarity present. A probe that did pair with the mutated gene would leave its radioactivity there and the clone would appear.
- **Why:** This question requires the reason the source gives for the technique working, demonstrated by the stem ending in 'autoradiography because :' and the key supplying the clause 'as the probe has no complementarity with it'.
- **Note:** negative_words_seen carries NOT, but the negation sits inside the option wording ('does not appear'), not in the task; the task is direct. Options 1 and 2 are the same conclusion with the reason clause inverted, which is what makes this a reason_line question rather than a fact_line one.
<!--/ecat-->

## Q147

Biology · both · Biotechnology: Principles and Processes

Plasmid pBR322 has PsI restriction enzyme site within gene amp$^{R}$ that confers ampicillin resistance. If this enzyme is used for inserting a gene for $\beta$-galactoside production and the recombinant plasmid is inserted in a E.coli strain

- (1) it will lead to lysis of host cell.
- (2) it will be able to produce a novel protein with dual ability
- **(3)** it will not be able to confer ampicillin resistance to the host cell
- (4) the transformed cells will have the ability to resist ampicillin as well as produce $\beta$-galactoside

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. The PstI site lies within the $amp^{R}$ gene of pBR322, so the foreign gene is ligated into $amp^{R}$.
2. Insertion of foreign DNA disrupts the coding sequence of $amp^{R}$ (insertional inactivation), so no functional ampicillin-resistance product is made.
3. Hence the recombinant plasmid cannot confer ampicillin resistance on the transformed E. coli, which is option $3$; options $1$, $2$ and $4$ do not follow.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 58)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q147_6302e6a3_30102026.png?v=6302e6a35603)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Insertional inactivation: cloning into a restriction site that lies inside a selectable marker destroys that marker, so the recombinant loses the resistance the plasmid used to give
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  pBR322 is learnt as the plasmid that carries ampicillin resistance, so a student holding that as a fixed feature of the vector adds the new gene on top of it and keeps both properties. The stem has placed the PstI site inside ampR, which means the insert breaks that gene and the resistance goes with it.
- **Why:** This question requires a known rule applied to the case printed here, demonstrated by the stem specifying a 'PsI restriction enzyme site within gene amp$^{R}$ that confers ampicillin resistance' and asking what the transformed cell then does.
- **Note:** Stem prints 'PsI' for PstI and 'β-galactoside' for β-galactosidase; neither affects which option is right. Option 4 is also a two-part option with one part failing, but the question turns on the printed location of the site, so condition_missed is the primary and half_right is the secondary reading.
<!--/ecat-->

## Q148

Biology · botany · Sexual Reproduction in Flowering Plants

In some members of which of the following pairs of families, pollen grains retain their viability for months after release ?

- (1) Poaceae ; Solanaceae
- **(2)** Rosaceae ; Leguminosae
- (3) Poaceae ; Rosaceae
- (4) Poaceae ; Leguminosae

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Pollen grains of cereals of $\text{Poaceae}$ (rice, wheat) lose viability within about $30$ minutes of release, so options $1$, $3$ and $4$ are excluded; some members of $\text{Rosaceae}$, $\text{Leguminosae}$ and $\text{Solanaceae}$ keep viability for months, so the pair $\text{Rosaceae}$ ; $\text{Leguminosae}$ is option $2$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 58)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q148_fa624d60_30102026.png?v=fa624d60575b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pollen viability is family-specific: cereal pollen (Poaceae) dies within about 30 minutes of release, while Rosaceae, Leguminosae and Solanaceae pollen keeps for months
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Solanaceae is one of the three families named as keeping pollen viable for months and it is missing from the key, so a student who remembers that name finds it only here. Its partner is Poaceae, the rice-and-wheat family from the same sentence whose pollen loses viability in 30 minutes, and one failing half sinks the whole pair.
- **Why:** This question requires the stated family-by-family fact about pollen viability, demonstrated by the options being four pairs of family names — 'Poaceae ; Solanaceae', 'Rosaceae ; Leguminosae' — with no criterion printed to reason from.
- **Note:** Three families are named in the source as keeping viability for months (Rosaceae, Leguminoseae, Solanaceae), so option 1 holds one qualifying family and fails only on Poaceae; the printed key, option 2, is the only pair with both halves qualifying and stands. The options are pairs accepted or rejected whole, a shape the qtype axis has no value for, so this is recorded as mcq.
<!--/ecat-->

## Q149

Biology · both · Molecular Basis of Inheritance

What is the role of RNA polymerase III in the process of transcription in eukaryotes?

- (1) Transcribes precursor of mRNA
- (2) Transcribes only snRNAs
- (3) Transcribes rRNAs ($28\mathrm{S}$, $18\mathrm{S}$ and $5.8\mathrm{S}$)
- **(4)** Transcribes tRNA, $5\mathrm{s}$ rRNA and snRNA

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Eukaryotic RNA polymerase I transcribes $28\mathrm{S}$, $18\mathrm{S}$ and $5.8\mathrm{S}$ rRNA; RNA polymerase II transcribes hnRNA (precursor of mRNA); RNA polymerase III transcribes tRNA, $5\mathrm{S}$ rRNA and snRNAs, which is option $4$.

**Subtopic:** Transcription · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q149_2afcf7ea_30102026.png?v=2afcf7ea7986)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The three eukaryotic RNA polymerases have fixed transcript sets: I makes 28S, 18S and 5.8S rRNA, II makes the mRNA precursor, III makes tRNA, 5S rRNA and snRNA
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The three polymerases and their transcripts are printed in one sentence, and the only rRNA given to polymerase III is 5S. A student who recalls that polymerase III does make an rRNA, and sees rRNAs listed, takes the line printed next door, which is polymerase I's: 28S, 18S and 5.8S.
- **Why:** This question requires one stated fact about which transcripts a named polymerase makes, demonstrated by the key reproducing the printed list 'tRNA, 5s rRNA and snRNA'.
- **Note:** Applied the swap test on the trap axis: the options are whole transcript lists, not similar-sounding names, so replacing them with unlike wording leaves the pull intact and position in the one source sentence is doing the work. That makes it nearby_fact, not look_alike_term.
<!--/ecat-->

## Q150

Biology · botany · Organisms and Populations

In the exponential growth equation $N_t = N_0 e^{rt}$, e represents:

- **(1)** The base of natural logarithms
- (2) The base of geometric logarithms
- (3) The base of number logarithms
- (4) The base of exponential logarithms

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In $N_t = N_0 e^{rt}$, $e \approx 2.71828$ is the base of natural logarithms, which is option $1$.

**Subtopic:** Exponential Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q150_d0af9645_30102026.png?v=d0af96459469)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the exponential growth equation $N_t = N_0 e^{rt}$ the letter e is the base of natural logarithms, about 2.71828
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  The stem calls the relation the exponential growth equation, so 'the base of exponential logarithms' reads as a real term assembled from words already on the page. No system of logarithms carries that name; e is the base of the natural logarithms.
- **Why:** This question requires the stated meaning of a symbol in a printed equation, demonstrated by all four options reading 'The base of ___ logarithms' with only the adjective changing.
- **Note:** Applied the swap test on the trap axis: replace 'exponential' with an unlike word and nothing pulls, so the likeness of the invented term to the real one is carrying the student, which makes it look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q151

Biology · zoology · Animal Kingdom

Read the following statements.
Choose the correct answer from the options given below.

- (a) Metagenesis is observed in Helminths.
- (b) Echinoderms are triploblastic and coelomate animals.
- (c) Round worms have organ-system level of body organization.
- (d) Comb plates present in ctenophores help in digestion.
- (e) Water vascular system is characteristic of Echinoderms.

- (1) (a), (d) and (e) are correct
- **(2)** (b), (c) and (e) are correct
- (3) (c), (d) and (e) are correct
- (4) (a), (b) and (c) are correct

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. (a) is false: metagenesis (alternation of polyp and medusa) is seen in Cnidaria, not in helminths.
2. (b) is true: echinoderms are triploblastic and coelomate.
3. (c) is true: roundworms (Aschelminthes) show organ-system level of organisation.
4. (d) is false: comb plates in ctenophores help in locomotion, not digestion.
5. (e) is true: the water vascular system is characteristic of echinoderms.
6. True statements are $(b), (c), (e)$, which is option $2$.

**Subtopic:** Phylum – Echinodermata and Hemichordata, Phylum – Aschelminthes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 59)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q151_d9e40327_30102026.png?v=d9e403278a22)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Metagenesis belongs to the cnidarians, ctenophore comb plates are organs of locomotion, and echinoderms are triploblastic coelomates with a water vascular system
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  In the ctenophore paragraph the comb plates are given their job in one sentence and digestion is the subject of the very next, so a student who recalls that both words belong to the same short passage joins them and accepts statement (d). The comb plates are organs of locomotion.
- **Why:** This question requires five stated phylum facts to be checked one at a time, demonstrated by the options being subsets such as '(c), (d) and (e) are correct' in which 'Comb plates present in ctenophores help in digestion' is the only failing member.
<!--/ecat-->

## Q152

Biology · zoology · Animal Kingdom

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Metamerism | (i) | Coelenterata |
| (b) | Canal system | (ii) | Ctenophora |
| (c) | Comb plates | (iii) | Annelida |
| (d) | Cnidoblasts | (iv) | Porifera |

- **(1)** (a)- (iii); (b) - (iv); (c) - (ii); (d) - (i)
- (2) (a)- (iv); (b) - (i); (c) - (ii); (d) - (iii)
- (3) (a)- (iv); (b) - (iii); (c) - (i); (d) - (ii)
- (4) (a)- (iii); (b) - (iv); (c) - (i); (d) - (ii)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Metamerism (true segmentation) is characteristic of Annelida: $(a) \to (iii)$.
2. The water canal system is characteristic of Porifera: $(b) \to (iv)$.
3. Eight external rows of ciliated comb plates are characteristic of Ctenophora: $(c) \to (ii)$.
4. Cnidoblasts (stinging cells) are characteristic of Coelenterata (Cnidaria): $(d) \to (i)$.
5. The match $(a)-(iii), (b)-(iv), (c)-(ii), (d)-(i)$ is option $1$.

**Subtopic:** Classification of Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 59)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q152_2e1784fb_30102026.png?v=2e1784fbd367)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Metamerism is annelid segmentation, the canal system is the sponge's, comb plates are ctenophoran and cnidoblasts belong to Coelenterata
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Ctenophora is introduced immediately after Coelenterata and shares its diploblastic, radially symmetrical, tissue-level body; option 4 keeps the two secure pairs and exchanges just these two phyla, giving the comb plates to Coelenterata and the cnidoblasts to Ctenophora.
- **Why:** This question requires each phylum's diagnostic feature, demonstrated by list I's '(c) Comb plates' against list II's '(ii) Ctenophora'.
- **Note:** Swap test applied: rename the two phyla and the exchange survives, because what is short is which of the two adjacent diploblastic phyla the comb plates are printed under, so the label is nearby_fact.
<!--/ecat-->

## Q153

Biology · zoology · Structural Organisation in Animals

Which of the following statements wrongly represents the nature of smooth muscle?

- **(1)** Communication among the cells is performed by intercalated discs
- (2) These muscles are present in the wall of blood vessels
- (3) These muscle have no striations
- (4) They are involuntary muscles

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Smooth muscle is non-striated, involuntary and lines hollow organs such as blood vessel walls, so options $2$, $3$ and $4$ are correct; intercalated discs are found only in cardiac muscle, so option $1$ misrepresents smooth muscle.

**Subtopic:** Muscle Tissue and Neural Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q153_a8e16653_30102026.png?v=a8e16653e75c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Intercalated discs join cardiac muscle cells; smooth muscle is non-striated, involuntary and lies in the walls of blood vessels and hollow visceral organs
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the three options other than the key one by one: smooth muscle does lie in the wall of blood vessels, does lack striations and is involuntary, and each is a printed property of smooth muscle. With the stem asking which statement wrongly represents smooth muscle, a true statement cannot be selected, and no route reaches one of these three that does not reach all three equally.
- **Why:** This question requires one stated fact — which muscle type intercalated discs belong to — demonstrated by option 1 naming 'intercalated discs' while the other three state properties the text gives to smooth muscle.
- **Note:** The negated task leaves all three non-key options as true lines about smooth muscle, so there is no option-specific route and all three are fillers. That is what the printed option set supports, not a gap in the checking: the only device here is the polarity of 'wrongly represents', which the trap axis has no value for and which is already recorded by task_polarity.
<!--/ecat-->

## Q154

Biology · both · Cell Cycle and Cell Division

The centriole undergoes duplication during:

- (1) Metaphase
- (2) $\mathrm{G_2}$ phase
- **(3)** S-phase
- (4) Prophase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT: during the S phase DNA replicates in the nucleus and, in animal cells, the centriole duplicates in the cytoplasm, so the answer is option $3$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q154_6981ef83_30102026.png?v=6981ef8398e7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The centriole duplicates in the cytoplasm during S phase, at the same time as DNA is replicated in the nucleus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  G$_2$ is the phase printed immediately after S and described as the one spent preparing for mitosis, so a student who files centriole duplication under getting ready to divide moves the event one phase along. The duplication is printed inside the S-phase line, next to DNA replication.
- **Why:** This question requires the stated fact about which phase of the cell cycle a named event belongs to, demonstrated by the four options being four phases of the cycle with no criterion printed to derive the answer from.
<!--/ecat-->

## Q155

Biology · both · Biotechnology and Its Applications

With regard to insulin choose correct options. Choose the correct answer from the options given below.

- (a) C-peptide is not present in mature insulin.
- (b) The insulin produced by rDNA technology has  C-peptide.
- (c) The pro-insulin has C-peptide.
- (d) A-peptide and B-peptide of insulin are interconnected by disulphide bridges

- **(1)** (a), (c) and (d) only
- (2) (a) and (d) only
- (3) (b) and (d) only
- (4) (b) and (c) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Insulin is made as pro-insulin, which carries an extra stretch called the C-peptide, so (c) is true.
2. During maturation the C-peptide is removed, so mature insulin has no C-peptide and (a) is true.
3. Chains $A$ and $B$ of mature insulin are linked by disulphide bridges, so (d) is true.
4. In rDNA technology the $A$ and $B$ chains are produced separately and joined by disulphide bonds, so the product has no C-peptide and (b) is false.
5. True statements are (a), (c) and (d), which is option $1$.

**Subtopic:** Genetically Engineered Insulin · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 60)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q155_b54d24c2_30102026.png?v=b54d24c2df4c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The C peptide connects the A and B chains in pro-insulin and is cut out when insulin matures, which is why the engineered hormone is made as two chains joined by disulphide bridges
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Statements (a) and (d) are the two insulin facts learnt by name — no C peptide in the mature hormone, A and B chains held by disulphide bridges — while (c) needs the student to know where the C peptide sat before it was removed. Unable to place (c), the student takes the shorter set that contains nothing doubtful, and it is short by one true statement.
- **Why:** This question requires the stated facts about where the C peptide sits at each stage, demonstrated by option 2 naming '(a) and (d) only' while statement (c), 'The pro-insulin has C-peptide', is equally printed.
<!--/ecat-->

## Q156

Biology · zoology · Reproductive Health

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Vaults | (i) | Entry of sperm through Cervix is blocked |
| (b) | IUDs | (ii) | Removal of Vas deferens |
| (c) | Vasectomy | (iii) | Phagocytosis of sperms within the Uterus |
| (d) | Tubectomy | (iv) | Removal of fallopian tube |

- (1) (a)- (ii); (b) - (iv); (c) - (iii);(d) - (i)
- (2) (a)- (iii); (b) - (i); (c) - (iv);(d) - (ii)
- (3) (a)- (iv); (b) - (ii); (c) - (i);(d) - (iii)
- **(4)** (a)- (i); (b) - (iii); (c) - (ii);(d) - (iv)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Vaults are barrier methods that cover the cervix, so entry of sperm through the cervix is blocked: $(a) \to (i)$.
2. IUDs increase phagocytosis of sperms within the uterus: $(b) \to (iii)$.
3. Vasectomy removes a small part of the vas deferens: $(c) \to (ii)$.
4. Tubectomy removes a small part of the fallopian tube: $(d) \to (iv)$.
5. The match $(a)-(i), (b)-(iii), (c)-(ii), (d)-(iv)$ is option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q156_0c314041_30102026.png?v=0c3140419376)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Vaults block the cervix, IUDs make the uterus phagocytose sperm, vasectomy removes part of the vas deferens and tubectomy part of the fallopian tube
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Vasectomy and tubectomy are two -ectomy words for the two sterilisation operations, and option 2 is the only code that exchanges them, giving the fallopian tube to vasectomy and the vas deferens to tubectomy.
- **Why:** This question requires each method's stated mechanism, demonstrated by list II's '(ii) Removal of Vas deferens' against list I's '(c) Vasectomy'.
- **Note:** Swap test applied: replace the two names with 'cutting the sperm duct' and 'cutting the egg duct' and the pull dies, so the likeness of the two surgical names is the pull and the label is look_alike_term.
<!--/ecat-->

## Q157

Biology · both · Molecular Basis of Inheritance

Which of the following RNAs is not required for the synthesis of protein?

- (1) rRNA
- **(2)** siRNA
- (3) mRNA
- (4) tRNA

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Translation uses mRNA as template, tRNA to carry amino acids and rRNA in ribosomes, while siRNA only silences genes by RNA interference, so the answer is option $2$.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q157_f49bde50_30102026.png?v=f49bde504d26)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Translation needs all three of mRNA, tRNA and rRNA; siRNA belongs to RNA interference and takes no part in making a protein
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the line that all three RNAs are needed to synthesise a protein: mRNA is the template, tRNA brings the amino acid and reads the code, rRNA is the structural and catalytic part of the ribosome. All three are printed as required, so under a stem asking which is not required none of them is selectable, and no route reaches one of the three that does not reach the other two equally.
- **Why:** This question requires one stated fact, which RNAs translation needs, demonstrated by the three distractors being exactly the three types the text names as needed to synthesise a protein while siRNA belongs to the gene-silencing section.
- **Note:** The device here is the negated task with every distractor a printed truth — the retired axis's true_statement_trap. The live 12 values have no family for it, and no single option dominates, so this is recorded as no_trap rather than forced onto one option. A reviewer who wants the device captured should add a polarity value to the trap axis; naming an option here would be false precision.
<!--/ecat-->

## Q158

Biology · both · Biomolecules

Identify the incorrect pair.

- (1) Lectins - Concanavalin A
- **(2)** Drugs - Ricin
- (3) Alkaloids - Codeine
- (4) Toxin - Abrin

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In the NCERT table of secondary metabolites, Concanavalin A is a lectin, codeine is an alkaloid, abrin and ricin are toxins, and vinblastin and curcumin are drugs, so the pair $\text{Drugs} - \text{Ricin}$ (option $2$) is the incorrect one.

**Subtopic:** Primary And Secondary Metabolites · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q158_882fc247_30102026.png?v=882fc24719e6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the secondary-metabolite classification ricin is a toxin, not a drug; codeine is listed as an alkaloid and concanavalin A as a lectin
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Codeine is sold as a medicine, so a student sorting the list by what a substance is used for rather than by the class the source files it under reads 'Alkaloids - Codeine' as the misfiled pair and gives codeine to the drugs row printed beside it. The source puts codeine with morphine under alkaloids and names vinblastin and curcumin as its drugs; ricin is the name that has been lifted out of the toxins row.
- **Why:** This question requires the taught classification of named secondary metabolites, demonstrated by option 2 pairing 'Drugs - Ricin' where the source lists ricin among the toxins.
- **Note:** Applied the swap test on the trap axis: the pull on option 3 does not depend on any likeness between the words codeine and ricin, but on the drugs row standing beside the alkaloids row in the same printed list, so it is nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q159

Biology · both · Biotechnology: Principles and Processes

A specific recognition sequence identified by endonucleases to make cuts at specific positions within the DNA is:

- **(1)** Palindromic Nucleotide sequences
- (2) Poly(A) tail sequences
- (3) Degenerate primer sequence
- (4) Okazaki sequences

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Restriction endonucleases inspect DNA and bind a specific recognition sequence that is a palindrome (reads the same $5' \rightarrow 3'$ on both strands), cutting within it; so the answer is option $1$.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q159_a90a79bc_30102026.png?v=a90a79bc14d9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Restriction endonucleases cut at palindromic recognition sequences, which read the same on both strands in the 5'→3' direction
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option for any connection to a restriction site: a poly(A) tail is added to hnRNA after transcription, Okazaki names the short fragments made on the lagging strand during replication, and degeneracy describes the code or a primer set designed around it. None names a sequence an enzyme recognises, and none shares a word with the stem's 'specific recognition sequence', 'endonucleases' or 'cuts at specific positions'.
- **Why:** This question requires the stated name of the site restriction enzymes act on, demonstrated by the stem's 'specific recognition sequence identified by endonucleases to make cuts at specific positions within the DNA'.
- **Note:** E1_question_type reads arrange_in_order, which the printed shape contradicts: nothing is to be sequenced, the stem asks one question and each option is a noun phrase, so the shape recorded here is mcq. The pattern most likely fired on the word 'sequence' appearing in the stem and in three options.
<!--/ecat-->

## Q160

Biology · both · Strategies for Enhancement in Food Production

Which of the following is not an objective of Biofortification in crops ?

- (1) Improve vitamin content
- (2) Improve micronutrient and mineral content
- (3) Improve protein content
- **(4)** Improve resistance to diseases

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Biofortification is breeding crops for higher nutritional quality: improved protein content and quality, oil content and quality, vitamin content, and micronutrient and mineral content, so options $1$, $2$ and $3$ are its objectives while improving resistance to diseases (option $4$) belongs to breeding for disease resistance, not biofortification.

**Subtopic:** Biofortification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q160_fb45071e_30102026.png?v=fb45071ecb4e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biofortification breeds crops for nutritional quality — more vitamins, minerals, protein and healthier fats; breeding for disease resistance is a separate aim of plant breeding
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the printed definition of biofortification, breeding crops for higher levels of vitamins and minerals or higher protein and healthier fats: vitamin content, micronutrient and mineral content and protein content are the three items of that one sentence. Each is a printed objective, so none is selectable under a stem asking which is not an objective, and no route reaches one of the three without reaching the others.
- **Why:** This question requires the stated aims of a named programme, demonstrated by option 4 reading 'Improve resistance to diseases', which the source treats under breeding for disease resistance and not under biofortification.
- **Note:** Same device as q157: the task is negated and all three distractors are printed truths from one sentence, the retired axis's true_statement_trap, for which the live 12 values have no family. No single option dominates, so no_trap is recorded rather than an option being chosen to make the field look filled.
<!--/ecat-->

## Q161

Biology · zoology · Locomotion and Movement

Chronic auto immune disorder affecting neuromuscular junction leading to fatigue, weakening and paralysis of skeletal muscle is called as:

- **(1)** Myasthenia gravis
- (2) Gout
- (3) Arthritis
- (4) Muscular dystrophy

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The NCERT describes myasthenia gravis as an auto immune disorder affecting the neuromuscular junction that leads to fatigue, weakening and paralysis of skeletal muscle, so the answer is option $1$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 61)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q161_5560b67b_30102026.png?v=5560b67bf832)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Myasthenia gravis is the autoimmune disorder of the neuromuscular junction; muscular dystrophy is genetic degeneration of muscle and arthritis is joint inflammation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The stem's 'weakening and paralysis of skeletal muscle' is also how the next entry in the same list of muscular and skeletal disorders reads — progressive degeneration of skeletal muscle — so a student matching on the muscle-weakness half of the description lands there. That entry is printed as genetic and says nothing about the neuromuscular junction or about autoimmunity.
- **Why:** This question requires one stated fact, the name attached to a printed description, demonstrated by the stem reproducing the entry 'auto immune disorder affecting neuromuscular junction leading to fatigue, weakening and paralysis of skeletal muscle'.
- **Note:** Applied the swap test on the trap axis: replace myasthenia gravis and muscular dystrophy with two unlike words and the pull survives, because it rests on the neighbouring entry in the same disorders list sharing the muscle-weakness description, not on the names resembling each other. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q162

Biology · botany · The Living World

Which one of the following belongs to the family Muscidae?

- (1) Cockroach
- **(2)** House fly
- (3) Fire fly
- (4) Grasshopper

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The house fly, $Musca\ domestica$, gives its name to the family Muscidae, so the answer is option $2$.

**Subtopic:** Family, Genus and Species · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q162_8a291289_30102026.png?v=8a2912892a15)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Family Muscidae is the housefly's family, Musca domestica; a firefly is a beetle and belongs elsewhere despite the word fly in its name
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Two of the four options end in 'fly', and a student who holds Muscidae only as 'the fly family' has to choose between them on the strength of the word. Firefly is a beetle; the family is built on Musca, the housefly's genus name.
- **Why:** This question requires one stated fact, which named animal sits in a named family, demonstrated by the stem asking 'Which one of the following belongs to the family Muscidae?' with four common names as options.
- **Note:** Applied the swap test on the trap axis: replace 'Fire fly' with 'beetle' and the pull disappears, so the likeness between the two 'fly' names is doing the work and this is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q163

Biology · zoology · Breathing and Exchange of Gases

The partial pressures (in mm Hg) of oxygen ($\mathrm{O_2}$) and carbon dioxide. ($\mathrm{CO_2}$) at alveoli (the site of diffusion) are:

- (1) $p\mathrm{O_2} = 95$ and $p\mathrm{CO_2} = 40$
- (2) $p\mathrm{O_2} = 159$ and $p\mathrm{CO_2} = 0.3$
- **(3)** $p\mathrm{O_2} = 104$ and $p\mathrm{CO_2} = 40$
- (4) $p\mathrm{O_2} = 40$ and $p\mathrm{CO_2} = 45$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. NCERT's table of respiratory gas partial pressures gives alveolar air $p\mathrm{O_2} = 104$ mm Hg and $p\mathrm{CO_2} = 40$ mm Hg, which is option $3$ (option $2$ is atmospheric air, option $4$ is deoxygenated blood, option $1$ is oxygenated blood).

**Subtopic:** Exchange Of Gases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q163_8f2c3c93_30102026.png?v=8f2c3c936230)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Alveolar air stands at $p\mathrm{O_2}=104$ and $p\mathrm{CO_2}=40$ mm Hg; the other rows of the same table are atmospheric air, the two blood samples and the tissues
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The table of partial pressures prints alveoli and oxygenated blood as neighbouring rows, and the two rows share $p\mathrm{CO_2}=40$, so the only figure that separates them is 104 against 95. A student who recalls the 40 and a mid-nineties oxygen figure reads off the wrong row.
- **Why:** This question requires a stored pair of values from a printed table, demonstrated by all four options being complete rows of that table of partial pressures with nothing in the stem to compute from.
- **Note:** Option 1 can also be read as half_right, since its $p\mathrm{CO_2}$ matches the key, but the device of the question is that every wrong option is a whole other row of the one table — option 4 shares neither value — so position is what carries the student and nearby_fact is the primary.
<!--/ecat-->

## Q164

Biology · both · Biotechnology: Principles and Processes

During the process of gene amplification using PCR, if very high temperature is not maintained in the beginning, then which of the following steps of PCR will be affected first?

- **(1)** Denaturation
- (2) Ligation
- (3) Annealing
- (4) Extension

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. PCR cycle order per NCERT: denaturation (high temperature, about $94^{\circ}C$) $\rightarrow$ annealing $\rightarrow$ extension; the step that needs very high temperature at the start is denaturation, so it is affected first, which is option $1$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q164_68efe575_30102026.png?v=68efe57579be)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** PCR's first step, denaturation, is the one that needs about 94 °C to separate the two DNA strands; annealing and extension run at lower temperatures afterwards
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Annealing is the step whose temperature a student is taught to think about, because it is set by the primers, and it is the step that follows the one the stem is really about. It would indeed fail, but only because denaturation failed first and left no single strands for the primers to bind.
- **Why:** This question requires a known requirement applied to a case the stem invents, demonstrated by the conditional 'if very high temperature is not maintained in the beginning, then which of the following steps of PCR will be affected first'.
- **Note:** The adjacency test on the trap axis: option 3 is the step printed immediately after the one the stem is about, and the two names resemble each other in no way, so this is nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q165

Biology · zoology · Body Fluids and Circulation

Which enzyme is responsible for the conversion of inactive fibrinogens to fibrins?

- (1) Epinephrine
- (2) Thrombokinase
- **(3)** Thrombin
- (4) Renin

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Thrombokinase converts prothrombin to thrombin, and $\text{thrombin}$ then converts inactive fibrinogen to fibrin, so the answer is option $3$.

**Subtopic:** Coagulation of Blood · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q165_f9473f75_30102026.png?v=f9473f756e63)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Thrombin converts inactive fibrinogen into fibrin; the enzyme complex thrombokinase acts one step earlier, converting prothrombin into thrombin
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Thrombin and thrombokinase share a name and sit in consecutive sentences of the clotting account, and thrombokinase is the one printed as 'required for the above reaction'. A student holding the pair of names loosely takes the longer one, which belongs to the step before: prothrombin to thrombin.
- **Why:** This question requires one stated fact, which enzyme carries out a named conversion, demonstrated by the stem asking for 'the conversion of inactive fibrinogens to fibrins'.
- **Note:** Both trap-axis tests fire on option 2 — thrombokinase is printed beside thrombin and the two names resemble each other — and the rulebook's tie-break gives it to the likeness, so look_alike_term is recorded and the adjacency is stated in the route for the reader.
<!--/ecat-->

## Q166

Biology · both · Cell: The Unit of Life

The organelles that are included in the endomembrane system are

- (1) Golgi complex, Mitochondria; Ribosomes and Lysosomes
- (2) Golgi complex, Endoplasmic reticulum, Mitochondria and Lysosomes
- (3) Endoplasmic reticulum, Mitochondria, Ribosomes and Lysosomes
- **(4)** Endoplasmic reticulum, Golgi complex, Lysosomes and Vacuoles

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the endomembrane system comprises the endoplasmic reticulum, Golgi complex, lysosomes and vacuoles, whose functions are coordinated; mitochondria (and chloroplasts, peroxisomes) are not included, and ribosomes are non-membranous, so option $4$ is correct.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 62)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q166_912d680e_30102026.png?v=912d680eebc0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The endomembrane system is the four organelles whose functions are coordinated — endoplasmic reticulum, Golgi complex, lysosomes and vacuoles — and mitochondria, chloroplast and peroxisomes are expressly left out
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Three of this option's four members are genuinely in the system — Golgi, endoplasmic reticulum and lysosomes — and the fourth replaces the vacuole, the member most easily dropped, with the mitochondrion, which the source names as excluded. The set is accepted or rejected whole, so one wrong member sinks it.
- **Why:** This question requires membership of a taught list, demonstrated by the stem reading 'The organelles that are included in the endomembrane system are' with each option a set of four organelle names.
- **Note:** E1_question_type reads statement_options, which the printed shape contradicts: the options are sets of organelle names, not statements to be judged. They are accepted or rejected whole, a shape the qtype axis has no value for, so this is recorded as mcq, and that whole-set reading is what licenses half_right on the trap axis.
<!--/ecat-->

## Q167

Biology · zoology · Reproductive Health

Which one of the following is an example of Hormone releasing IUD?

- (1) Cu 7
- (2) Multiload 375
- (3) CuT
- **(4)** LNG 20

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Cu 7, CuT and Multiload 375 are copper-releasing IUDs, while LNG-20 releases the hormone levonorgestrel, so the hormone-releasing IUD is option $4$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q167_9da79faa_30102026.png?v=9da79faa09aa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** IUDs come in three printed kinds: non-medicated, copper releasing (CuT, Cu7, Multiload 375) and hormone releasing (Progestasert, LNG-20)
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The copper-releasing group is printed in the clause next to the hormone-releasing one, and two of its three names announce themselves with Cu. Multiload 375 is the one that does not, so striking out the names with copper in them leaves it standing as the apparently non-copper device — but it is listed with the copper ones.
- **Why:** This question requires membership of a printed list, demonstrated by the stem asking for 'an example of Hormone releasing IUD' and three of the options being the devices listed as copper releasing.
- **Note:** Applied the swap test on the trap axis: the pull on option 2 does not rest on any likeness between the names Multiload 375 and LNG 20, but on its position in the copper-releasing list combined with its name lacking the Cu marker, so nearby_fact.
<!--/ecat-->

## Q168

Biology · zoology · Digestion and Absorption

Succus entericus is referred to as:

- (1) Gastric juice
- (2) Chyme
- (3) Pancreatic juice
- **(4)** Intestinal juice

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Succus entericus is the name for the secretions of the brush border cells and intestinal glands of the small intestine, i.e. intestinal juice, which is option $4$.

**Subtopic:** Digestion of Food · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q168_d2ecf302_30102026.png?v=d2ecf3022bd5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Succus entericus is NCERT's name for the intestinal juice secreted by the mucosa of the small intestine itself
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Succus entericus is held in memory only as a juice that works in the duodenum, and pancreatic juice is the duodenal juice NCERT prints just before it in the same run of secretions, so the adjacent one is taken for it
- **Why:** This question requires the name NCERT gives one digestive secretion, demonstrated by the stem 'Succus entericus is referred to as:' with four named secretions as the options.
<!--/ecat-->

## Q169

Biology · zoology · Breathing and Exchange of Gases

Select the favourable conditions required for the formation of oxyhaemoglobin at the alveoli.

- (1) High $\mathrm{pO_2}$, high $\mathrm{pCO_2}$, less $\mathrm{H^+}$, higher temperature
- (2) Low $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, more $\mathrm{H^+}$, higher temperature
- **(3)** High $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, less $\mathrm{H^+}$, lower temperature
- (4) Low $\mathrm{pO_2}$, high $\mathrm{pCO_2}$, more $\mathrm{H^+}$, higher temperature

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the alveoli, high $\mathrm{pO_2}$, low $\mathrm{pCO_2}$, less $\mathrm{H^+}$ and lower temperature favour the formation of oxyhaemoglobin, which is option $3$.

**Subtopic:** Transport of Gases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q169_a8206cef_30102026.png?v=a8206ceff85c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Oxygen loads onto haemoglobin at the alveoli because pO2 is high there while pCO2, H+ and temperature are all low; the tissues present the opposite set
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Low pO2, high pCO2, more H+ and higher temperature is the set NCERT prints for oxygen being RELEASED in the tissues, so recalling the dissociation sentence without checking which site the stem names lands on a true line about the wrong site
- **Why:** This question requires the condition set NCERT states for oxygen loading, demonstrated by the stem 'favourable conditions required for the formation of oxyhaemoglobin at the alveoli'.
- **Note:** Printed shape is four condition bundles accepted or rejected whole (the retired vocabulary's pair_options, which category_retired.qtype maps to statements), not a lettered statement block; E1's statement_options maps to the same current value.
<!--/ecat-->

## Q170

Biology · zoology · Reproductive Health

Veneral diseases can spread through: Choose the correct answer from the options below:

- (a) Using sterile needles
- (b) Transfusion of blood from infected person
- (c) Infected mother to foetus
- (d) Kissing
- (e) Inheritance

- **(1)** (b) and (c) only
- (2) (a) and (c) only
- (3) (a), (b) and (c) only
- (4) (b), (c) and (d) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. (a) Sterile needles carry no pathogen, so they cannot spread venereal disease: false.
2. (b) Transfusion of blood from an infected person transmits STIs such as HIV and hepatitis B: true.
3. (c) An infected mother can pass the infection to the foetus: true.
4. (d) Kissing is casual contact and is not a route of venereal disease transmission: false.
5. (e) STIs are infections, not inherited traits: false.
6. Only (b) and (c) are true, which is option $1$.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 63)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q170_c2edb8ce_30102026.png?v=c2edb8ce71ce)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sexually transmitted infections pass by sexual contact, by transfusion of infected blood, by sharing a used needle and from an infected mother to the foetus; they are not inherited
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The printed transmission list includes sharing injection needles with an infected person, so a student who reads statement (a) for its noun and not for the word 'sterile' adds it to the two routes they are sure of. A sterile needle is the one that carries nothing.
- **Why:** This question requires the stated routes by which these infections spread, demonstrated by statement (a) reading 'Using sterile needles' where the printed route is a needle shared with an infected person.
- **Note:** The record is internally inconsistent and is tagged as it stands, not repaired: accepted_answers carries only '1', while answer_line_as_printed reads 'Answer: (a) or (d)', which names option 4 as a second accepted answer. Option 4, '(b), (c) and (d) only', is therefore left out of other_options rather than given a trap, since a trap must not sit on an accepted option; a reviewer holding the printed paper should settle whether kissing was keyed in. The stem's 'Veneral' is the paper's spelling.
<!--/ecat-->

## Q171

Biology · both · Cell Cycle and Cell Division

The fruit fly has 8 chromosomes $(2n)$ in each cell. During interphase of Mitosis if the number of chromosomes at $\mathrm{G_1}$ phase is 8, what would be the number of chromosomes after S phase?

- (1) 4
- (2) 32
- **(3)** 8
- (4) 16

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In $\mathrm{G_1}$ the cell has $2n = 8$ chromosomes.
2. In S phase each chromosome replicates into two sister chromatids held at one centromere, so DNA content goes from $2C$ to $4C$.
3. Chromosome number is counted by centromeres, so it stays $2n = 8$ after S phase, which is option $3$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q171_7ffa7bd6_30102026.png?v=7ffa7bd6ea32)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** S phase doubles the DNA and gives every chromosome two sister chromatids, but it leaves the chromosome number unchanged
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  'DNA is duplicated in S phase' is carried straight over to the chromosome count, so 8 is doubled to 16 - but the quantity that doubles is the DNA and the chromatid number, not the number of chromosomes
- **Why:** This question requires the rule for what S phase does applied to a stated count, demonstrated by the stem 'if the number of chromosomes at G1 phase is 8, what would be the number of chromosomes after S phase?'.
<!--/ecat-->

## Q172

Biology · both · Molecular Basis of Inheritance

If Adenine makes $30\%$ of the DNA molecule, what will be the percentage of Thymine, Guanine and Cytosine in it?

- **(1)** T : $30$; G : $20$; C : $20$
- (2) T : $20$; G : $25$; C : $25$
- (3) T : $20$; G : $30$; C : $20$
- (4) T : $20$; G : $20$; C : $30$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. By Chargaff's rule $A = T$, so $T = 30\%$.
2. $G + C = 100\% - (30\% + 30\%) = 40\%$.
3. Since $G = C$, $G = C = \frac{40\%}{2} = 20\%$, which is option $1$.

**Subtopic:** Salient Features of Structure of DNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q172_66410d9d_30102026.png?v=66410d9d3b2b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Chargaff's equivalence, A = T and G = C, fixes thymine from adenine and leaves the remainder to be shared equally by guanine and cytosine
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Chargaff's rule is stored as 'each pair makes up half the molecule', so $A + T$ is set to 50 giving $T = 20$, and the other 50 is split as $G = C = 25$
- **Why:** This question requires Chargaff's equivalence turned into percentages, demonstrated by the stem 'If Adenine makes 30% of the DNA molecule, what will be the percentage of Thymine, Guanine and Cytosine in it?'.
- **Note:** All three wrong options print T : 20, so every wrong route passes through the same mis-stored rule and then differs on which base is given adenine's share.
<!--/ecat-->

## Q173

Biology · zoology · Animal Kingdom

Which one of the following organisms bears hollow and pneumatic long bones?

- (1) Macropus
- (2) Ornithorhynchus
- **(3)** Neophron
- (4) Hemidactylus

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Birds (class Aves) have long bones that are hollow and filled with air cavities (pneumatic), so the organism must be a bird; $Neophron$ (vulture) is the only bird, which is option $3$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q173_a6f777cb_30102026.png?v=a6f777cb091f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hollow, air-filled pneumatic long bones are a diagnostic feature of birds, lightening the skeleton for flight
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who correctly knows pneumatic bones are a bird feature then has to find the bird, and 'Ornitho-' plus the duck bill makes Ornithorhynchus read as one, so the egg-laying mammal NCERT files one class away is picked
- **Why:** This question requires the group NCERT ties one skeletal feature to, demonstrated by the stem 'Which one of the following organisms bears hollow and pneumatic long bones?' set against four genus names. Swap test applied: Neophron and Ornithorhynchus do not resemble each other, and replacing Neophron with any other bird name leaves the pull intact, so position in the adjacent class is doing the work, not likeness.
<!--/ecat-->

## Q174

Biology · both · Molecular Basis of Inheritance

Which is the “Only enzyme” that has “Capability” to catalyse Initiation. Elongation and Termination in the process of transcription in prokaryotes?

- (1) DNA Ligase
- (2) DNase
- (3) DNA dependent DNA polymerase
- **(4)** DNA dependent RNA polymerase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Prokaryotic transcription uses a single DNA-dependent RNA polymerase, which (with $\sigma$ and $\rho$ factors) catalyses initiation, elongation and termination, so the answer is option $4$.

**Subtopic:** Transcription · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q174_2e573d5a_30102026.png?v=2e573d5ac9af)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In prokaryotes a single enzyme, DNA-dependent RNA polymerase, catalyses initiation, elongation and termination of transcription, helped by sigma and rho factors
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The option differs from the answer by one word inside a four-word name, so a student who has stored the tag 'DNA dependent ... polymerase' without fixing which nucleic acid is made takes the first name that matches the tag
- **Why:** This question requires the enzyme NCERT names for prokaryotic transcription, demonstrated by the stem asking for the 'Only enzyme' that can catalyse 'Initiation. Elongation and Termination'. Swap test applied: replace option 3's 'DNA polymerase' with an unrelated enzyme name and the pull dies, so the one-word likeness is carrying the student, which is why look_alike_term beats nearby_fact here.
<!--/ecat-->

## Q175

Biology · zoology · Animal Kingdom

Match the following:

| List-I | | List-II | |
|---|---|---|---|
| (a) | Physalia | (i) | Pearl oyster |
| (b) | Limulus | (ii) | Portuguese Man of War |
| (c) | Ancylostoma | (iii) | Living fossil |
| (d) | Pinctada | (iv) | Hookworm |

- **(1)** (a)- (ii); (b) - (iii); (c) - (iv);(d) - (i)
- (2) (a)- (i); (b) - (iv); (c) - (iii);(d) - (ii)
- (3) (a)- (ii); (b) - (iii); (c) - (i);(d) - (iv)
- (4) (a)- (iv) - (i); (c) - (iii);(d) - (ii)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. $\text{Physalia} \rightarrow$ Portuguese Man of War, so (a)-(ii).
2. $\text{Limulus}$ (king crab) $\rightarrow$ living fossil, so (b)-(iii).
3. $\text{Ancylostoma} \rightarrow$ hookworm, so (c)-(iv).
4. $\text{Pinctada} \rightarrow$ pearl oyster, so (d)-(i).
5. (a)-(ii), (b)-(iii), (c)-(iv), (d)-(i) matches option $1$.

**Subtopic:** Classification of Animals · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 64)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q175_b986ee6f_30102026.png?v=b986ee6f1aec)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Physalia is the Portuguese Man of War, Limulus the living fossil, Ancylostoma the hookworm and Pinctada the pearl oyster
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  option 4 is stored as '(a)- (iv) - (i); (c) - (iii);(d) - (ii)', which carries no (b) pairing and an extra '- (i)', so one of the four options is not all there and no mechanism can be read off the set
- **Why:** This question requires each genus's stated common name, demonstrated by list I's '(a) Physalia' against list II's '(ii) Portuguese Man of War'.
- **Note:** Option 4 as stored is malformed - '(a)- (iv) - (i); (c) - (iii);(d) - (ii)' has no (b) entry and a doubled dash - so the option set is incomplete and the trap axis stays empty under rule 0.5. The key (option 1) and the other two codes read cleanly. A reviewer holding the printed paper should check option 3, which keeps (a)-(ii) and (b)-(iii) and exchanges hookworm and pearl oyster between Ancylostoma and Pinctada, and should repair option 4 before any trap is written.
<!--/ecat-->

## Q176

Biology · both · Cell Cycle and Cell Division

Which stage of meiotic prophase shows terminalisation of chiasmata as its distinctive feature?

- **(1)** Diakinesis
- (2) Pachytene
- (3) Leptotene
- (4) Zygotene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. In diakinesis, the final stage of meiotic prophase I, the chiasmata move towards the ends of the bivalents (terminalisation), so the answer is option $1$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q176_107254b3_30102026.png?v=107254b32143)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chiasmata are formed during crossing over and are dragged to the ends of the paired chromosomes only at diakinesis, the last sub-stage of prophase I
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Chiasmata are stored in memory as a pachytene item, because pachytene is the sub-stage where crossing over and the recombination nodules are printed, so the stage that makes chiasmata is offered for the stage that terminalises them
- **Why:** This question requires the prophase I sub-stage NCERT ties one named event to, demonstrated by the stem 'Which stage of meiotic prophase shows terminalisation of chiasmata as its distinctive feature?'. Swap test applied: diakinesis and pachytene do not resemble each other as words, and the pull survives any renaming because it comes from the chiasma-forming event printed at pachytene, so this is nearby_fact and not look_alike_term.
- **Note:** wrong_site_attacked was considered, since the option does place the stem's event at another stage. It was ruled out because what carries the student is a different event the book prints at pachytene (crossing over), which is the nearby_fact family; allowed_values maps the retired wrong_site_or_stage to nearby_fact for this case.
<!--/ecat-->

## Q177

Biology · botany · Environmental Issues

Dobson units are used to measure thickness of:

- **(1)** Ozone
- (2) Troposphere
- (3) CFCs
- (4) Stratosphere

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. The thickness of the ozone layer, measured as the ozone in a column of air from the ground to the top of the atmosphere, is given in Dobson units (DU), so the answer is option $1$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q177_1b23b5b0_30102026.png?v=1b23b5b0a9fc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The thickness of ozone in a column of air is reported in Dobson units
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The remembered phrase is 'the ozone layer in the stratosphere', so a student who recalls that Dobson units measure a thickness high in the atmosphere attaches the unit to the layer named in the same sentence rather than to the gas
- **Why:** This question requires the quantity NCERT says Dobson units report, demonstrated by the stem 'Dobson units are used to measure thickness of:' with a gas and two atmospheric layers among the options.
<!--/ecat-->

## Q178

Biology · zoology · Digestion and Absorption

Sphincter of oddi is present at:

- (1) Gastro-oesophageal junction
- (2) Junction of jejunum and duodenum
- (3) Ileo-caecal junction
- **(4)** Junction of hepato-pancreatic duct and duodenum

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. The bile duct and pancreatic duct join to form the common hepato-pancreatic duct, which opens into the duodenum and is guarded by the sphincter of Oddi, so the answer is option $4$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q178_25aff594_30102026.png?v=25aff59475b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The sphincter of Oddi guards the opening of the common hepato-pancreatic duct into the duodenum
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  What survives in memory is that the sphincter of Oddi is somewhere in the duodenum, and this is the other option that prints the word duodenum, so the location is matched on the organ instead of on the junction
- **Why:** This question requires the location NCERT states for one named sphincter, demonstrated by the stem 'Sphincter of oddi is present at:' with four gut junctions as options.
<!--/ecat-->

## Q179

Biology · both · Principles of Inheritance and Variation

In a cross between a male and female, both heterozygous for sickle cell anaemia gene, what percentage of the progeny will be diseased?

- **(1)** $25\%$
- (2) $100\%$
- (3) $50\%$
- (4) $75\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Sickle cell anaemia is autosomal recessive, so each parent is $\mathrm{Hb^A Hb^S}$.
2. $\mathrm{Hb^A Hb^S} \times \mathrm{Hb^A Hb^S} \rightarrow \frac{1}{4}\,\mathrm{Hb^A Hb^A} : \frac{1}{2}\,\mathrm{Hb^A Hb^S} : \frac{1}{4}\,\mathrm{Hb^S Hb^S}$.
3. Only $\mathrm{Hb^S Hb^S}$ is diseased: $\frac{1}{4} = 25\%$, which is option $1$.

**Subtopic:** Sickle-cell Anaemia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 65)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q179_a29bdbc9_30102026.png?v=a29bdbc95ae9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Sickle-cell anaemia is autosomal recessive, so a carrier times carrier cross gives 1 normal : 2 carriers : 1 diseased and only the homozygote is diseased
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  50% is the correct figure for the CARRIER fraction of the same cross, so a student who builds the 1 : 2 : 1 square and then reads off the biggest class answers the carrier question instead of the diseased one
- **Why:** This question requires a percentage worked out from a monohybrid cross, demonstrated by the stem 'both heterozygous for sickle cell anaemia gene, what percentage of the progeny will be diseased?'.
<!--/ecat-->

## Q180

Biology · zoology · Body Fluids and Circulation

Persons with “AB” blood group are called as “Universal recipients”. This is due to:

- (1) Presence of antibodies, anti-A and anti-B, on RBCs
- **(2)** Absence of antibodies, anti-A and anti-B, in plasma
- (3) Absence of antigens A and B on the surface of RBCs
- (4) Absence of antigens A and B in plasma

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. AB blood has antigens A and B on the RBC surface and no anti-A or anti-B antibodies in the plasma, so it can receive blood of any ABO group without agglutination; this is option $2$.

**Subtopic:** Blood Group and Rh Group · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q180_7de5267f_30102026.png?v=7de5267fbd23)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** AB plasma carries neither anti-A nor anti-B antibody, so blood of any group can be given to an AB recipient without agglutination
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Absence of A and B antigens on the red cells is the stated reason group O is the universal DONOR, so a student who remembers one entry of the blood-group table supplies that explanation for the title printed in the row beside it
- **Why:** This question requires the reason NCERT gives for one blood group's title, demonstrated by the stem 'Persons with “AB” blood group are called as “Universal recipients”. This is due to:'.
<!--/ecat-->

## Q181

Biology · zoology · Structural Organisation in Animals

Which of the following characteristics is incorrect with respect to cockroach ?

- (1) In females, 7th-9th sterna together form a genital pouch
- (2) 10th abdominal segment in both sexes, bears a pair of anal cerci
- **(3)** A ring of gastric caeca is present at the junction of midgut and hind gut
- (4) Hypopharynx lies within the cavity enclosed by the mouth parts.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Gastric caeca in cockroach form a ring at the junction of the foregut (gizzard) and midgut; the midgut-hindgut junction bears the Malpighian tubules, so statement $3$ is incorrect while $1$, $2$ and $4$ are correct.

**Subtopic:** Anatomy of Cockroach · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 66)

![printed question 181](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q181_49a4a064_30102026.png?v=49a4a064133b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the cockroach the ring of gastric (hepatic) caeca sits at the foregut-midgut junction; the midgut-hindgut junction is where the Malpighian tubules arise
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Anal styles are the appendage NCERT prints as male-only, and a student who has the two terminal appendages the wrong way round reads 'in both sexes' as the planted error and flags this true line instead
- **Why:** This question requires one printed anatomical fact about the cockroach to be found false, demonstrated by the option 'A ring of gastric caeca is present at the junction of midgut and hind gut' against a stem asking which characteristic is incorrect.
- **Note:** The key option is built by substituting one word in the printed line - the caeca ring is at the foregut-midgut junction, not the midgut-hindgut junction - so a student who stores the caeca only as sitting 'at a gut junction' accepts it and must flag one of the three verbatim options instead.
<!--/ecat-->

## Q182

Biology · zoology · Chemical Coordination and Integration

Erythropoietin hormone which stimulates R.B.C. formation is produced by

- (1) The cells of bone marrow
- **(2)** Juxtaglomerular cells of the kidney
- (3) Alpha cells of pancreas
- (4) The cells of rostral adenohypophysis

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. The juxtaglomerular cells of the kidney secrete the peptide hormone erythropoietin, which stimulates erythropoiesis, so the answer is option $2$.

**Subtopic:** Hormones of Heart, Kidney and Gastrointestinal Tract · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 182](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q182_d2a3c456_30102026.png?v=d2a3c4566c2b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Erythropoietin is secreted by the juxtaglomerular cells of the kidney, and acts on the bone marrow where red cells are made
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The stem hands over the words 'stimulates R.B.C. formation', and the bone marrow is where red cells are formed, so the site the hormone ACTS on is given for the site that MAKES it
- **Why:** This question requires the source NCERT states for one hormone, demonstrated by the stem 'Erythropoietin hormone which stimulates R.B.C. formation is produced by'.
- **Note:** E1's pattern returned statement_options, but the printed options are noun phrases naming cell types, not statements to be judged, so the shape recorded here is mcq.
<!--/ecat-->

## Q183

Biology · botany · Microbes in Human Welfare

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Aspergillus niger | (i) | Acetic Acid |
| (b) | Acetobacter aceti | (ii) | Lactic Acid |
| (c) | Clostridium butylicum | (iii) | Citric Acid |
| (d) | Lactobacillus | (iv) | Butyric Acid |

- (1) (a)- (ii); (b) - (iii); (c) - (i);(d) - (iv)
- (2) (a)- (iv); (b) - (ii); (c) - (i);(d) - (iii)
- **(3)** (a)- (iii); (b) - (i); (c) - (iv);(d) - (ii)
- (4) (a)- (i); (b) - (ii); (c) - (iii);(d) - (iv)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. $\textit{Aspergillus niger}$ (fungus) produces citric acid: (a)-(iii); $\textit{Acetobacter aceti}$ produces acetic acid: (b)-(i); $\textit{Clostridium butylicum}$ produces butyric acid: (c)-(iv); $\textit{Lactobacillus}$ produces lactic acid: (d)-(ii). This matches option $3$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 183](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q183_5ccca594_30102026.png?v=5ccca594ffa7)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each industrial microbe is named for its product: Acetobacter aceti makes acetic acid, Clostridium butylicum butyric acid, Lactobacillus lactic acid, and Aspergillus niger citric acid
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  three of the four rows carry the product inside the organism's own name - aceti/acetic, butylicum/butyric, Lactobacillus/lactic - and every wrong code breaks at least two of those echoes, which also fixes Aspergillus niger to citric acid by elimination
- **Why:** This question requires each microbe's stated product, demonstrated by list I's '(b) Acetobacter aceti' against list II's '(i) Acetic Acid'.
- **Note:** no_trap is a finding here: the organism names carry their products, so no wrong code keeps a single defensible pair.
<!--/ecat-->

## Q184

Biology · zoology · Human Reproduction

Receptors for sperm binding in mammals are present on

- (1) Perivitelline space
- **(2)** Zona pellucida
- (3) Corona radiata
- (4) Vitelline membrane

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. In mammals the sperm first contacts the zona pellucida, whose glycoprotein receptors (e.g. ZP3) bind the sperm and trigger the acrosome reaction, so the answer is option $2$.

**Subtopic:** Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 66)

![printed question 184](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q184_42277f14_30102026.png?v=42277f14c767)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In mammals the sperm-binding receptors sit in the zona pellucida, the glycoprotein coat immediately around the ovum
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The corona radiata is the layer the sperm meets first, so a student who remembers the order of the coats the sperm must cross offers the outermost one for the one that actually carries the receptors
- **Why:** This question requires the layer NCERT states carries the sperm receptors, demonstrated by the stem 'Receptors for sperm binding in mammals are present on' with four egg coats and spaces as options.
<!--/ecat-->

## Q185

Biology · both · Biotechnology and Its Applications

For effective treatment of the disease, early diagnosis and understanding its pathophysiology is very important. Which of the following molecular diagnostic techniques is very useful for early detection?

- **(1)** ELISA Technique
- (2) Hybridization Technique
- (3) Western Blotting Technique
- (4) Southern Blotting Technique

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. NCERT Class 12 (Molecular diagnosis) lists recombinant DNA technology, PCR and ELISA as techniques for early diagnosis, and among the options only ELISA (option $1$) is named there.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 185](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q185_60358500_30102026.png?v=60358500c152)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** ELISA detects infection from the antigen or the antibody in a sample, and is one of the techniques NCERT names for diagnosis before the disease declares itself
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Probe hybridisation is the other molecular diagnosis method printed in the same short section, where a radioactively tagged single strand finds its complement, so a student recalling the section rather than the sentence picks the method beside the one asked for
- **Why:** This question requires the technique NCERT names for diagnosis before symptoms appear, demonstrated by the stem 'Which of the following molecular diagnostic techniques is very useful for early detection?'.
- **Note:** Option 2 is itself a molecular diagnosis method the same NCERT section describes, which is what makes it the pull; the key is tagged as printed because the 'early diagnosis' sentence names ELISA by name.
<!--/ecat-->

## Q186

Biology · both · Molecular Basis of Inheritance

Statement I: The codon ‘AUG’ codes for methionine and phenylalanine.
Statement II: ‘AAA’ and ‘AAG’ both codons code for the amino acid lysine.

- (Statement I) The codon ‘AUG’ codes for methionine and phenylalanine.
- (Statement II) ‘AAA’ and ‘AAG’ both codons code for the amino acid lysine.

- (1) Statement I is correct but statement II is false
- **(2)** Statement I is incorrect but statement II is true
- (3) Both Statement I and Statement II are true
- (4) Both Statement I and Statement II are false

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. $AUG$ codes only for methionine (and is the start codon); phenylalanine is coded by $UUU$/$UUC$, so Statement I is incorrect.
2. $AAA$ and $AAG$ are both codons for lysine (degeneracy of the code), so Statement II is true; this is option $2$.

**Subtopic:** Genetic Code and Its Features · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 186](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q186_96879dda_30102026.png?v=96879dda9385)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The genetic code is degenerate but unambiguous: AUG stands for methionine alone and doubles as the start codon, while lysine has two codons, AAA and AAG
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Statement I opens with a fact everyone has — AUG codes for methionine — and the error is the two words appended to it. A student who verifies the methionine half, passes the statement and then checks Statement II, which is true, comes out with both true.
- **Why:** This question requires two stated facts from the codon dictionary checked one at a time, demonstrated by Statement I appending 'and phenylalanine' to the methionine codon and Statement II pairing 'AAA' and 'AAG' with lysine.
- **Note:** qtype is two_part rather than statements: the printed shape is exactly two labelled statements with the four truth verdicts as options, which is the shape the axis keeps two_part for, while statements covers the three-or-more lettered lists whose options select a subset.
<!--/ecat-->

## Q187

Biology · zoology · Locomotion and Movement

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Scapula | (i) | Cartilaginous joints |
| (b) | Cranium | (ii) | Flat bones |
| (c) | Sternum | (iii) | Fibrous joints |
| (d) | Vertebral column | (iv) | Triangular flat bone |

- (1) (a)- (iv); (b) - (ii); (c) - (iii);(d) - (i)
- **(2)** (a)- (iv); (b) - (iii); (c) - (ii);(d) - (i)
- (3) (a)- (i); (b) - (iii); (c) - (ii);(d) - (iv)
- (4) (a)- (ii); (b) - (iii); (c) - (iv);(d) - (i)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Scapula is a large triangular flat bone, so $(a) \rightarrow (iv)$.
2. Cranial bones are joined by sutures, which are fibrous joints, so $(b) \rightarrow (iii)$.
3. Sternum is a flat bone on the ventral midline of the thorax, so $(c) \rightarrow (ii)$.
4. Adjacent vertebrae are joined by cartilaginous joints, so $(d) \rightarrow (i)$.
5. The set $(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)$ is option $2$.

**Subtopic:** Axial Skeleton, Joints · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 67)

![printed question 187](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q187_4cbc0907_30102026.png?v=4cbc09078736)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The scapula is the triangular flat bone and the sternum the flat bone, while the cranial bones are joined by fibrous sutures and the vertebrae by cartilaginous joints
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The chapter's own phrase is 'the flat skull bones', so pairing Cranium with 'Flat bones' states something true about the cranium - but that entry in list II is the sternum's description, and what the cranium is printed under is the fibrous suture joint.
- **Why:** This question requires separating a bone's shape from its joint type, demonstrated by list II holding both '(ii) Flat bones' and '(iv) Triangular flat bone' while list I prints '(b) Cranium' and '(c) Sternum'.
- **Note:** The label is answers_other_question rather than half_right because what pulls is the truth of the pair - the cranial bones ARE flat - and not the code being partly right; list II reserves that entry for the sternum, so the option answers a question the grid did not ask.
<!--/ecat-->

## Q188

Biology · both · Strategies for Enhancement in Food Production

Which of the following is not a step in Multiple Ovulation Embryo Transfer Technology (MOET) ?

- (1) Cow is fertilized by artificial insemination
- (2) Fertilized eggs are transferred to surrogate mothers at 8-32 cell stage
- **(3)** Cow is administered hormone having LH like activity for super ovulation
- (4) Cow yields about 6-8 eggs at a time

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In MOET (as NCERT teaches) super ovulation is induced with a hormone having FSH-like activity, so option $3$ (LH-like activity) is not a step; the cow yields $6$-$8$ eggs, is fertilized by mating or artificial insemination, and embryos at the $8$-$32$ cell stage go to surrogate mothers, so options $1$, $2$ and $4$ are steps.

**Subtopic:** Animal Breeding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 67)

![printed question 188](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q188_84b04eef_30102026.png?v=84b04eef7ffb)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In MOET the cow is given an FSH-like hormone to cause superovulation, yields 6-8 eggs, is inseminated, and the embryos are moved to surrogates at the 8-32 cell stage
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The procedure prints two number ranges close together - 6-8 eggs and the 8-32 cell stage - and a student holding them the wrong way round reads 'yields about 6-8 eggs' as the altered line and flags a true statement
- **Why:** This question requires one printed step of a named breeding procedure to be found altered, demonstrated by the option 'Cow is administered hormone having LH like activity for super ovulation' against a procedure whose hormone is FSH-like.
- **Note:** The key option is a one-word substitution, FSH-like to LH-like, inside an otherwise verbatim step, which is why the pull sits on the two numbered statements rather than on the hormone.
<!--/ecat-->

## Q189

Biology · zoology · Human Reproduction

Which of the following secretes the hormone, relaxin, during the later phase of pregnancy?

- (1) Foetus
- (2) Uterus
- (3) Graafian follicle
- **(4)** Corpus luteum

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. In the later phase of pregnancy the ovary secretes relaxin; the ovarian structure that is active during pregnancy is the corpus luteum (Graafian follicles do not mature during pregnancy), so the answer is option $4$.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 189](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q189_9244764d_30102026.png?v=9244764df278)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Relaxin is secreted by the ovary's corpus luteum in the later phase of pregnancy
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who has placed relaxin in the ovary still has to pick between the ovary's two named structures, and the Graafian follicle is the one printed first in the ovarian cycle, so the structure that precedes the corpus luteum is taken for it
- **Why:** This question requires the source NCERT states for one hormone of pregnancy, demonstrated by the stem 'Which of the following secretes the hormone, relaxin, during the later phase of pregnancy?'.
- **Note:** NCERT's own sentence says the ovary secretes relaxin in the later phase of pregnancy; the key names the corpus luteum, the ovarian body that persists through pregnancy, so the tag follows the printed key.
<!--/ecat-->

## Q190

Biology · both · Molecular Basis of Inheritance

Which one Of the following statements about Histones is wrong ?

- (1) Histones are rich in amino acids - Lysine and Arginine
- (2) Histones carry positive charge in the side chain.
- (3) Histones are organized to form a unit of 8 molecules.
- **(4)** The pH of histones is slightly acidic

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Histones are rich in the basic amino acids lysine and arginine, so statement $1$ is correct.
2. Lysine and arginine carry positively charged side chains, so statement $2$ is correct.
3. Eight histone molecules form the histone octamer, so statement $3$ is correct.
4. Because of their basic residues, histones are basic proteins, not slightly acidic, so statement $4$ is the wrong one and the answer is option $4$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 190](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q190_e5ae7f8e_30102026.png?v=e5ae7f8ea79b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Histones are basic proteins, rich in lysine and arginine, whose positively charged side chains let eight of them form the core the DNA winds around
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The word histone pulls the basic amino acid histidine with it, so a student who has stored histones as the histidine-rich protein reads the pair 'Lysine and Arginine' as the swapped line and marks it wrong
- **Why:** This question requires one printed property of histones to be found false, demonstrated by the option 'The pH of histones is slightly acidic' against a protein the chapter calls basic.
- **Note:** Swap test applied on the trap: replace histone with an unrelated protein name and the pull dies, because it is the histone / histidine resemblance that supplies the wrong residue, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q191

Biology · zoology · Structural Organisation in Animals

Identify the types of cell junctions that help to stop the leakage of the substances across a tissue and facilitation of communication with neighbouring cells via rapid transfer of ions and molecules

- (1) Adhering junctions and Tight junctions, respectively
- (2) Adhering junctions and Gap junctions, respectively
- (3) Gap junctions and Adhering junctions, respectively
- **(4)** Tight junctions and Gap junctions, respectively

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Tight junctions stop substances from leaking across a tissue, and gap junctions let ions and small molecules pass quickly between neighbouring cells, so the order is Tight then Gap, which is option $4$.

**Subtopic:** Animal Tissues: Epithelial Tissue · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 191](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q191_73352e9c_30102026.png?v=73352e9c3e05)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tight junctions seal neighbouring cells so substances cannot leak across a tissue, while gap junctions link their cytoplasms for rapid passage of ions and small molecules; adhering junctions only cement cells together
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The second half is correct - gap junctions are the communicating ones - and the first name is then read off the word 'adhering', which sounds like cells stuck together tightly enough that nothing can leak between them
- **Why:** This question requires two function-to-junction lines NCERT states, demonstrated by the stem's near-verbatim pair 'stop the leakage of the substances across a tissue' and 'rapid transfer of ions and molecules'.
- **Note:** E1's pattern returned statement_options; the printed shape is two answers joined by 'respectively' in every option, which is the retired multi_part_respectively, so qtype is recorded as two_part.
<!--/ecat-->

## Q192

Biology · both · Biomolecules

Following are the statements with reference to 'lipids'.
Choose the correct answer from the options given below

- (a) Lipids having only single bonds are called unsaturated fatty acids.
- (b) Lecithin is a phospholipid
- (c) Trihydroxy propane is glycerol.
- (d) Palmitic acid has 20 carbon atoms including carboxyl carbon
- (e) Arachidonic acid has 16 carbon atoms

- **(1)** (b) and (c) only
- (2) (b) and (e) only
- (3) (a) and (b) only
- (4) (c) and (d) only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. (a) is false: fatty acids with only single $C\!-\!C$ bonds are saturated, not unsaturated.
2. (b) is true: lecithin is a phospholipid.
3. (c) is true: glycerol is trihydroxy propane, $C_3H_5(OH)_3$.
4. (d) is false: palmitic acid has $16$ carbon atoms including the carboxyl carbon, not $20$.
5. (e) is false: arachidonic acid has $20$ carbon atoms, not $16$.
6. Only (b) and (c) are correct, which is option $1$.

**Subtopic:** Lipids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 68)

![printed question 192](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q192_a76090ee_30102026.png?v=a76090ee4dde)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Palmitic acid has 16 carbons and arachidonic acid 20, fatty acids with only single bonds are saturated, lecithin is a phospholipid and glycerol is trihydroxy propane
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The two carbon counts have been exchanged between statements (d) and (e): palmitic acid's 16 is printed against arachidonic acid and arachidonic acid's 20 against palmitic. A student who holds the pair of numbers without which acid owns which accepts (e) as printed, and with lecithin secure that gives (b) and (e).
- **Why:** This question requires the stated carbon counts and definitions for lipids, demonstrated by statements (d) and (e) printing 'Palmitic acid has 20 carbon atoms' and 'Arachidonic acid has 16 carbon atoms' with the two counts exchanged.
<!--/ecat-->

## Q193

Biology · zoology · Human Health and Disease

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Filariasis | (i) | Haemophilus influenzae |
| (b) | Amoebiasis | (ii) | Trichophyton |
| (c) | Pneumonia | (iii) | Wuchereria bancrofti |
| (d) | Ringworm | (iv) | Entamoeba histolytica |

- (1) (a)- (i); (b) - (ii); (c) - (iv);(d) - (iii)
- (2) (a)- (ii); (b) - (iii); (c) - (i);(d) - (iv)
- (3) (a)- (iv); (b) - (i); (c) - (iii);(d) - (ii)
- **(4)** (a)- (iii); (b) - (iv); (c) - (i);(d) - (ii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Solved independently** (answer withheld)

1. Filariasis is caused by $Wuchereria\ bancrofti$ (iii), amoebiasis by $Entamoeba\ histolytica$ (iv), pneumonia by $Haemophilus\ influenzae$ (i) and ringworm by $Trichophyton$ (ii). This gives (a)-(iii), (b)-(iv), (c)-(i), (d)-(ii), which is option $4$.

**Subtopic:** Common Diseases in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 193](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q193_82877444_30102026.png?v=82877444af17)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Wuchereria bancrofti causes filariasis, Entamoeba histolytica amoebiasis, Trichophyton ringworm and Haemophilus influenzae pneumonia
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  three of the four rows are fixed by the names themselves - amoebiasis/Entamoeba, filariasis/the filarial worm Wuchereria, ringworm/the fungus Trichophyton - and each wrong code breaks at least two of them, leaving pneumonia with Haemophilus influenzae by elimination
- **Why:** This question requires each disease's stated causal agent, demonstrated by list I's '(b) Amoebiasis' against list II's '(iv) Entamoeba histolytica'.
- **Note:** no_trap is a finding: the disease names carry their agents, so no wrong code holds more than one defensible pair.
<!--/ecat-->

## Q194

Biology · zoology · Locomotion and Movement

During the muscular contraction which of the following events occur? Choose the correct answer from the options given below.

- (a) 'H' zone disappears
- (b) 'A' band widens
- (c) 'I' band reduces in width
- (d) Myosine hydrolyzes ATP, releasing the ADP and Pi.
- (e) Z-lines attached to actins are pulled inwards.

- (1) (b),(c),(d),(e) only
- (2) (b),(d),(e),(a) only
- **(3)** (a),(c),(d),(e) only
- (4) (a),(b),(c),(d) only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. In the sliding filament model, thin filaments slide over thick filaments, so the length of the $A$ band (thick filament length) stays constant; statement (b) is false.
2. As actin slides towards the centre, the $H$ zone narrows and disappears, statement (a) is true.
3. The $I$ band reduces in width, statement (c) is true.
4. The myosin head hydrolyses $\mathrm{ATP}$ to $\mathrm{ADP} + \mathrm{P_i}$ to energise the cross-bridge cycle, statement (d) is true.
5. Actin filaments attached to the $Z$-lines are pulled inwards towards the centre of the sarcomere, statement (e) is true.
6. True set (a),(c),(d),(e) matches option $3$.

**Subtopic:** Mechanism of Muscle Contraction and Red and White Muscle Fibre · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 69)

![printed question 194](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q194_a564e227_30102026.png?v=a564e2271929)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In contraction the actin filaments slide over the myosin: the I bands shorten and the H zone disappears while the A band keeps its length
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The printed sentence pairs two verbs — the I bands get reduced, the A bands retain their length — and this option is exactly the set a student picks who has those verbs the other way round: (b) accepted because the A band is taken to change, (c) dropped because the I band is taken to stay. One exchange selects the whole option.
- **Why:** This question requires the stated changes in each band during contraction, demonstrated by statement (b) reading "'A' band widens" where the printed line has the A bands retaining their length.
<!--/ecat-->

## Q195

Biology · botany · Organisms and Populations

In the light of the above statements, choose the correct answer from the options given below

- Assertion (A) A person goes to high altitude and experiences 'altitude sickness' with symptoms like breathing difficulty and heart palpitations.
- Reason (R) Due to low atmospheric pressure at high altitude, the body does not get sufficient oxygen.

- (1) (A) is true but (R) is false
- (2) (A) is false but (R) is true
- **(3)** Both (A) and (R) are true and (R) is the correct explanation of (A)
- (4) Both (A) and (R) are true but (R) is not the  correct explanation of (A)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. At high altitude the atmospheric pressure is low, so $pO_2$ is low and the body does not get enough oxygen, so (R) is true.
2. This lack of oxygen causes altitude sickness, with symptoms like breathing difficulty and heart palpitations, so (A) is true.
3. The low oxygen supply in (R) is the cause of the symptoms in (A), so (R) correctly explains (A), which is option $3$.

**Subtopic:** Homeostasis, Adaptations and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 69)

![printed question 195](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q195_6d9eed61_30102026.png?v=6d9eed61071e)

---

<!--ecat-->
#### Categories

- **Type:** **Assertion and Reason** (`assertion_reason`) — a labelled Assertion and Reason, judged for truth and explanation
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** At high altitude the whole air column presses less, so oxygen's partial pressure falls and the blood loads less oxygen; faster breathing and a racing heart are the body compensating.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The true neighbouring fact that air stays about 21% oxygen all the way up is used to deny the Reason, since the Reason reads as though there were less oxygen in the air at altitude
- **Why:** This question requires deciding whether a stated cause accounts for a stated symptom list, demonstrated by the Reason reading 'Due to low atmospheric pressure at high altitude, the body does not get sufficient oxygen' set against an Assertion whose content is 'breathing difficulty and heart palpitations'.
- **Note:** negative_words_seen lists NOT and FALSE, but both come from the standard A/R option wording, not from the task; the task is direct.
<!--/ecat-->

## Q196

Biology · both · Evolution

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Adaptive radiation | (i) | Selection of resistant varieties due to excessive use of herbicides and pesticides |
| (b) | Convergent evolution | (ii) | Bones of forelimbs in Man and Whale |
| (c) | Divergent evolution | (iii) | Wings of butterfly and birds |
| (d) | Evolution by anthropogenic action | (iv) | Darwin Finches |

- (1) (a)- (ii); (b) - (i); (c) - (iv);(d) - (iii)
- (2) (a)- (i); (b) - (iv); (c) - (iii);(d) - (ii)
- **(3)** (a)- (iv); (b) - (iii); (c) - (ii);(d) - (i)
- (4) (a)- (iii); (b) - (ii); (c) - (i);(d) - (iv)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Darwin finches radiating from a common ancestor into varied forms is adaptive radiation: $(a) \rightarrow (iv)$.
2. Wings of butterfly and birds are analogous organs, a result of convergent evolution: $(b) \rightarrow (iii)$.
3. Forelimb bones of man and whale are homologous organs, a result of divergent evolution: $(c) \rightarrow (ii)$.
4. Selection of resistant varieties due to excessive herbicide and pesticide use is evolution by anthropogenic action: $(d) \rightarrow (i)$.
5. The match $(a)-(iv), (b)-(iii), (c)-(ii), (d)-(i)$ is option $3$.

**Subtopic:** Homology and Analogy, What is Adaptive Radiation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 196](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q196_56600bb6_30102026.png?v=56600bb659e6)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homologous forelimbs are divergent evolution, analogous wings are convergent, Darwin's finches are adaptive radiation and herbicide resistance is evolution by anthropogenic action
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Option 4 attaches 'Convergent evolution' to the forelimb bones of Man and Whale, which is the homology example - the analogy/homology pair applied the wrong way round, since the butterfly's and bird's wings are the convergent case.
- **Why:** This question requires the homology-analogy distinction applied to two printed examples, demonstrated by list II's '(ii) Bones of forelimbs in Man and Whale' and '(iii) Wings of butterfly and birds'.
- **Note:** reversed rather than half_right: option 4 shares no pair with the key, so there is nothing partly right about it; what it does is invert the convergent/divergent relation itself.
<!--/ecat-->

## Q197

Biology · zoology · Structural Organisation in Animals

Following are the statements about prostomium of earthworm. Choose the correct answer from the options given below

- (a) It serves as a covering for mouth
- (b) It helps to open cracks in the soil into which it can crawl
- (c) It is one of the sensory structures
- (d) It is the first body segment

- (1) (a), (b), (c) and (d) are correct
- (2) (b), (c) are correct
- **(3)** (a), (b) and (c) are correct
- (4) (a), (b) and (d) are correct

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Per NCERT, the prostomium is a fleshy lobe over the mouth that serves as a covering for the mouth, so $(a)$ is true.
2. It acts as a wedge to force open cracks in the soil into which the earthworm crawls, so $(b)$ is true.
3. The prostomium is sensory in function, so $(c)$ is true.
4. The first body segment is the peristomium (buccal segment) containing the mouth; the prostomium is not a segment, so $(d)$ is false.
5. Correct set $= (a), (b), (c)$, which is option $3$.

**Subtopic:** Earthworm · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 70)

![printed question 197](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q197_515296a8_30102026.png?v=515296a8a4b6)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The prostomium is a sensory lobe that covers the mouth and wedges open cracks in the soil; the first body segment is the peristomium
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Prostomium' and 'peristomium' differ in two letters, and the sentence that makes the peristomium the first body segment is the one right after the prostomium's description. A student carrying the two as one word accepts statement (d) and, with the other three printed word for word, takes the whole set as correct.
- **Why:** This question requires the stated facts about the prostomium, demonstrated by statement (d) reading 'It is the first body segment' when that sentence belongs to the peristomium.
- **Note:** Likeness test applied: prostomium and peristomium are also printed in consecutive sentences, so position holds as well, but the two names resemble each other closely and the rulebook gives the likeness precedence, so the label is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q198

Biology · both · Biotechnology and Its Applications

The Adenosine deaminase deficiency results into:

- (1) Digestive disorder
- (2) Addison’s disease
- **(3)** Dysfunction of Immune system
- (4) Parkinson’s disease

**Answer** — booklet: (3) · independent solve: (3) · agree

**Solved independently** (answer withheld)

1. Adenosine deaminase is needed for normal immune function; its deficiency causes SCID (the first gene-therapy case), a dysfunction of the immune system, which is option $3$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 198](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q198_55e8e907_30102026.png?v=55e8e907d369)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Adenosine deaminase deficiency destroys the immune function of the lymphocytes, which is the SCID treated by gene therapy
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Adenosine and Addison open with the same syllables, so a student who has met the phrase 'adenosine deaminase deficiency' as a sound rather than as a function reaches for the named disease whose spelling echoes it
- **Why:** This question requires the consequence NCERT states for one enzyme deficiency, demonstrated by the stem 'The Adenosine deaminase deficiency results into:' with one system failure among three named disorders.
- **Note:** Swap test applied: replace Addison's with an unlike disease name and the pull dies, because nothing but the Aden-/Addi- resemblance carries a student there, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q199

Biology · botany · Organisms and Populations

Match list I with list II.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Allen’s Rule | (i) | Kangaroo rat |
| (b) | Physiological adaptation | (ii) | Desert lizard |
| (c) | Behavioural adaptation | (iii) | Marine fish at depth |
| (d) | Biochemical adaptation | (iv) | Polar seal |

- **(1)** (a)- (iv); (b) - (i); (c) - (ii);(d) - (iii)
- (2) (a)- (iv); (b) - (iii); (c) - (ii;(d) - (i)
- (3) (a)- (iv); (b) - (ii); (c) - (iii);(d) - (i)
- (4) (a)- (iv); (b) - (i); (c) - (iii);(d) - (ii)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Solved independently** (answer withheld)

1. Allen's rule (shorter ears and limbs in cold climates to reduce heat loss) matches the polar seal: $(a) \to (iv)$.
2. The kangaroo rat meets its water needs by internal fat oxidation and concentrated urine, a physiological adaptation: $(b) \to (i)$.
3. The desert lizard regulates body temperature by basking in the sun or moving into shade, a behavioural adaptation: $(c) \to (ii)$.
4. Marine fish at great depth survive the high pressure through biochemical adaptations: $(d) \to (iii)$.
5. The set $(a)-(iv), (b)-(i), (c)-(ii), (d)-(iii)$ is option $1$.

**Subtopic:** Homeostasis, Adaptations and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 199](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q199_26eb8fd9_30102026.png?v=26eb8fd99a50)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Allen's rule is the polar seal's small extremities, the kangaroo rat's water economy is physiological, the desert lizard's basking and burrowing is behavioural, and the deep-sea fish's tolerance is biochemical
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Physiological and biochemical adaptations are introduced in the same passage, and the kangaroo rat's trick - making its water by oxidising fat - is itself a piece of chemistry, so option 2's exchange of the two keeps both pairs inside that passage.
- **Why:** This question requires each adaptation's stated category, demonstrated by list II's '(i) Kangaroo rat' against list I's '(b) Physiological adaptation'.
- **Note:** Option 2 as stored reads '(c) - (ii;(d) - (i)' - a missing closing bracket. The pairings it names are unambiguous, so this is a typo rather than a missing option and the question is tagged as printed; a reviewer should still close the bracket. Swap test applied to the trap: rename the two categories and the exchange survives, because what is short is which heading the kangaroo rat is printed under.
<!--/ecat-->

## Q200

Biology · zoology · Human Reproduction

Which of these is not an important component of initiation of parturition in humans?

- (1) Release of Oxytocin
- **(2)** Release of Prolactin
- (3) Increase in estrogen and progesterone ratio
- (4) Synthesis of prostaglandins

**Answer** — booklet: (2) · independent solve: (2) · agree

**Solved independently** (answer withheld)

1. Parturition starts through a neuroendocrine mechanism: signals from the full-term foetus and placenta cause mild uterine contractions (the foetal ejection reflex), which trigger the release of oxytocin. A rising estrogen:progesterone ratio and prostaglandin synthesis also strengthen the contractions. Prolactin controls lactation, not the start of labour, so the answer is option $2$.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 71)

![printed question 200](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2021/2021_O1/crops/q200_2772a876_30102026.png?v=2772a8761f28)

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parturition is driven by the foetal ejection reflex, oxytocin, prostaglandins and a rising estrogen-to-progesterone ratio; prolactin belongs to lactation, after the birth
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Progesterone has to fall for labour to start, so the phrase 'increase in estrogen and progesterone ratio' is read as both hormones rising and is flagged as the component that cannot belong
- **Why:** This question requires one component of a stated mechanism to be identified as belonging elsewhere, demonstrated by the option 'Release of Prolactin' against a stem asking what is not part of the initiation of parturition.
- **Note:** Of the four options only oxytocin is named in NCERT's parturition paragraph, so options 3 and 4 have to be judged from physiology beyond that paragraph; this is what makes the prostaglandin option reachable for a student revising from the text alone.
<!--/ecat-->

