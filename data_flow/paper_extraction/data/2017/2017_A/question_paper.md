# NEET (UG) 2017 · Code A

180 questions · source `NEET_Papers/2017/NEET_2017_Code_A_official.pdf` · every image a CDN link (0 without one) · 39 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Current Electricity

A potentiometer is an accurate and versatile device to make electrical measurements of E.M.F, because the method involves :

- (1) Cells
- (2) Potential gradients
- **(3)** A condition of no current flow through the galvanometer
- (4) A combination of cells, galvanometer and resistances

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Reading of potentiometer is accurate because during taking reading it does not draw any current from the circuit.

**Solved independently** (answer withheld)

1. At the balance point the galvanometer shows null deflection, so $I_g = 0$ and the cell under test supplies no current, giving $E = k\,l$ with no $Ir$ drop; this no-current condition is option $3$.

**Subtopic:** Potentiometer · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q001_d03cc730_27102026.png?v=d03cc7304b18)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q001_75f62108_27102026.png?v=75f621085651)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Potentiometer measures EMF by null balance: at the balance point no current is drawn from the cell, so its internal resistance drops no potential
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The uniform potential gradient along the wire is how the potentiometer is calibrated; the null balance is what makes the EMF reading accurate. A student who holds only the first principle offers it for the second.
- **Why:** This question requires naming the feature of the potentiometer's method that makes an EMF measurement accurate, demonstrated by the stem's "because the method involves" and option 3, "A condition of no current flow through the galvanometer".
<!--/ecat-->

## Q2

Physics · Thermodynamics

A gas mixture consists of 2 moles of $\mathrm{O_2}$ and 4 moles of Ar at temperature $T$. Neglecting all vibrational modes, the total internal energy of the system is

- (1) $4\,RT$
- (2) $15\,RT$
- (3) $9\,RT$
- **(4)** $11\,RT$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $U = n_1\frac{f_1}{2}RT + n_2\frac{f_2}{2}RT$
2. $= 2 \times \frac{5}{2}RT + 4 \times \frac{3}{2}RT$
3. $= 5\,RT + 6\,RT$
4. $U = 11\,RT$

**Solved independently** (answer withheld)

1. With vibrational modes neglected, $\mathrm{O_2}$ (diatomic) has $f_1 = 5$ degrees of freedom and Ar (monatomic) has $f_2 = 3$.
2. Internal energy of $\mathrm{O_2}$: $U_1 = n_1 \frac{f_1}{2} RT = 2 \times \frac{5}{2} RT = 5\,RT$.
3. Internal energy of Ar: $U_2 = n_2 \frac{f_2}{2} RT = 4 \times \frac{3}{2} RT = 6\,RT$.
4. $U = U_1 + U_2 = 5\,RT + 6\,RT = 11\,RT$, which is option $4$.

**Subtopic:** Specific Heat Capacity of Monoatomic, Diatomic, and Polyatomic Gases · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q002_0f566f34_27102026.png?v=0f566f34338e)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q002_974715fb_27102026.png?v=974715fb1ea9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Internal energy of a gas mixture: add $\tfrac{f}{2}nRT$ over the species, with $f=5$ for a diatomic and $f=3$ for a monatomic
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who remembers internal energy as $\tfrac{3}{2}nRT$ applies it to all 6 moles and gets $9RT$. Argon's $6RT$ is right, but oxygen's two rotational modes are left out, and oxygen contributes $5RT$, not $3RT$.
- **Also:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The mirror-image slip: $\tfrac{5}{2}nRT$ applied to BOTH gases, treating argon as diatomic too. That gives exactly the $15RT$ printed as option 2.
- **Why:** This question requires summing $\tfrac{f}{2}nRT$ over two gases with different degrees of freedom, demonstrated by the stem's "2 moles of $\mathrm{O_2}$ and 4 moles of Ar" together with "Neglecting all vibrational modes".
- **Note:** Option 3 is the one that leaves a term out of an otherwise correct sum; the mirror-image route is recorded above.
<!--/ecat-->

## Q3

Physics · Modern Physics

> ⚠ The printed solution says "No option is correct": the question has no correct option as printed, and the printed answer comes from a corrected reading.

Radioactive material 'A' has decay constant '$8\lambda$' and material 'B' has decay constant '$\lambda$'. Initially they have same number of nuclei. After what time, the ratio of number of nuclei of material 'B' to that 'A' will be $\frac{1}{e}$?

- (1) $\frac{1}{\lambda}$
- **(2)** $\frac{1}{7\lambda}$
- (3) $\frac{1}{8\lambda}$
- (4) $\frac{1}{9\lambda}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. No option is correct
2. If we take $\frac{N_A}{N_B} = \frac{1}{e}$
3. Then
4. $\frac{N_A}{N_B} = \frac{e^{-8\lambda t}}{e^{-\lambda t}}$
5. $\frac{1}{e} = e^{-7\lambda t}$
6. $-1 = -7\lambda t$
7. $t = \frac{1}{7\lambda}$

**Solved independently** (answer withheld)

1. $N_A = N_0 e^{-8\lambda t}$ and $N_B = N_0 e^{-\lambda t}$ since both start with $N_0$ nuclei.
2. $\frac{N_B}{N_A} = \frac{e^{-\lambda t}}{e^{-8\lambda t}} = e^{7\lambda t}$.
3. Setting $e^{7\lambda t} = \frac{1}{e}$ gives $7\lambda t = -1$, i.e. a negative time, because $N_B/N_A \ge 1$ for all $t \ge 0$.
4. The physically meaningful reading is $\frac{N_A}{N_B} = e^{-7\lambda t} = \frac{1}{e}$, so $7\lambda t = 1$.
5. $t = \frac{1}{7\lambda}$, which is option $2$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q003_03fd2706_27102026.png?v=03fd27068319)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q003_f95a1f02_27102026.png?v=f95a1f02d5a5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Radioactive decay law: the ratio of two samples with different decay constants falls with the difference of those constants, $e^{-(\lambda_A-\lambda_B)t}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  A student who combines the two exponents by adding the decay constants, $8\lambda+\lambda$, lands on $t=\frac{1}{9\lambda}$. A ratio divides the two exponentials, so the constants subtract: $8\lambda-\lambda=7\lambda$, giving $\frac{1}{7\lambda}$.
- **Why:** This question requires solving the decay law for the time at which a ratio of surviving nuclei reaches $\frac{1}{e}$, demonstrated by the stem's "decay constant $8\lambda$" and "decay constant $\lambda$" against options all of the form $\frac{1}{n\lambda}$.
<!--/ecat-->

## Q4

Physics · Mechanical Properties of Fluids

A U tube with both ends open to the atmosphere, is partially filled with water. Oil, which is immiscible with water, is poured into one side until it stands at a distance of $10\,\mathrm{mm}$ above the water level on the other side. Meanwhile the water rises by $65\,\mathrm{mm}$ from its original level (see diagram). The density of the oil is

![printed figure: U tube with oil column AB in the left arm and water in the bend and right arm; water rises 65 mm from initial level D to final level E, oil top A stands 10 mm above E](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q004_36521d5f_27102026.svg?v=36521d5fe968)

*U tube with oil column AB in the left arm and water in the bend and right arm; water rises 65 mm from initial level D to final level E, oil top A stands 10 mm above E*

![drawn: U tube with oil column AB in the left arm and water in the bend and right arm; water rises 65 mm from initial level D to final level E, oil top A stands 10 mm above E](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q004_question_ca7723eb_27102026.svg?v=ca7723eb6b4b)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $650\,\mathrm{kg\,m^{-3}}$
- (2) $425\,\mathrm{kg\,m^{-3}}$
- (3) $800\,\mathrm{kg\,m^{-3}}$
- **(4)** $928\,\mathrm{kg\,m^{-3}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $h_{\mathrm{oil}}\,\rho_{\mathrm{oil}}\,g = h_{\mathrm{water}}\,\rho_{\mathrm{water}}\,g$
2. $140 \times \rho_{\mathrm{oil}} = 130 \times \rho_{\mathrm{water}}$
3. $\rho_{\mathrm{oil}} = \frac{13}{14} \times 1000\,\mathrm{kg/m^{3}}$
4. $\rho_{\mathrm{oil}} = 928\,\mathrm{kg\,m^{-3}}$

**Solved independently** (answer withheld)

1. Water rises $65\,\mathrm{mm}$ on the right, so the oil-water interface on the left falls $65\,\mathrm{mm}$ to level $B$.
2. Water column above level $B$ on the right: $h_w = 65 + 65 = 130\,\mathrm{mm}$.
3. Oil column above $B$ on the left: $h_o = 130 + 10 = 140\,\mathrm{mm}$.
4. Equal pressure at level $B$: $\rho_o g h_o = \rho_w g h_w$.
5. $\rho_o = 1000 \times \frac{130}{140} \approx 928\,\mathrm{kg\,m^{-3}}$, which is option $4$.

**Subtopic:** Problems on Hydrostatics · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q004_8d20ea09_27102026.png?v=8d20ea096792)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q004_4e991992_27102026.png?v=4e991992e832)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Hydrostatic balance in a U-tube: pressures match at the level where the liquids meet, so $\rho_{\mathrm{oil}}h_{\mathrm{oil}}=\rho_{w}h_{w}$, and the two water levels differ by twice the rise
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  No option has a route a prepared student would take; the three wrong options are fillers.
- **Why:** This question requires balancing a 140 mm oil column against a 130 mm water column about the level where the two meet, demonstrated by the stem's "stands at a distance of $10\,\mathrm{mm}$ above the water level on the other side" and "the water rises by $65\,\mathrm{mm}$".
- **Note:** The figure is present and its drawn check passes, so the question is complete. I could demonstrate no arithmetic route to option 1 ($650$) or option 2 ($425$); the classic dropped factor of two, which gives $867$, is not printed.
<!--/ecat-->

## Q5

Physics · Magnetic Effect of Electric Current

A 250-Turn rectangular coil of length $2.1\,\mathrm{cm}$ and width $1.25\,\mathrm{cm}$ carries a current of $85\,\mu\mathrm{A}$ and subjected to a magnetic field of strength $0.85\,\mathrm{T}$. Work done for rotating the coil by $180^\circ$ against the torque is

- **(1)** $9.1\,\mu\mathrm{J}$
- (2) $4.55\,\mu\mathrm{J}$
- (3) $2.3\,\mu\mathrm{J}$
- (4) $1.15\,\mu\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $W = MB\,(\cos\theta_{1} - \cos\theta_{2})$
2. When it is rotated by angle $180^\circ$ then
3. $W = 2MB$
4. $W = 2\,(NIA)B$
5. $= 2 \times 250 \times 85 \times 10^{-6}[1.25 \times 2.1 \times 10^{-4}] \times 85 \times 10^{-2}$
6. $= 9.1\,\mu\mathrm{J}$

**Solved independently** (answer withheld)

1. Area of the coil: $A = 2.1\times10^{-2}\,\mathrm{m} \times 1.25\times10^{-2}\,\mathrm{m} = 2.625\times10^{-4}\,\mathrm{m^2}$.
2. Magnetic moment: $m = NIA = 250 \times 85\times10^{-6} \times 2.625\times10^{-4} = 5.578\times10^{-6}\,\mathrm{A\,m^2}$.
3. Work to rotate from $\theta = 0^\circ$ to $\theta = 180^\circ$: $W = mB(\cos 0^\circ - \cos 180^\circ) = 2mB$.
4. $W = 2 \times 5.578\times10^{-6} \times 0.85 = 9.48\times10^{-6}\,\mathrm{J} \approx 9.5\,\mu\mathrm{J}$.
5. The nearest option is $9.1\,\mu\mathrm{J}$, which is option $1$.

**Subtopic:** Work Done or Potential Energy of a Current-Carrying Loop in a Uniform Magnetic Field · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 2)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q005_4a146a18_27102026.png?v=4a146a1842f1)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q005_8cb53dd8_27102026.png?v=8cb53dd81e8c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Work to turn a current loop in a magnetic field is the change in $-MB\cos\theta$, so a $180^\circ$ flip costs $2MB$ with $M=NIA$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  A student who takes the work as $MB$, the size of the dipole's energy at one orientation, instead of the change from $-MB$ to $+MB$, halves the answer and lands on $4.55\,\mu\mathrm{J}$. The flip crosses both halves, so the cost is $2MB$.
- **Why:** This question requires the energy change of a magnetic dipole turned end to end, demonstrated by the stem's "Work done for rotating the coil by $180^\circ$ against the torque" with $M=NIA$ built from the 250 turns, $85\,\mu\mathrm{A}$ and the $2.1\,\mathrm{cm}\times1.25\,\mathrm{cm}$ area.
- **Note:** Substituting the printed numbers gives $2NIAB=9.5\,\mu\mathrm{J}$ while option 1 reads $9.1\,\mu\mathrm{J}$; tagged as printed, key not re-judged. Options 2, 3 and 4 are successive halvings of the printed option 1, and only the first halving has a named route.
<!--/ecat-->

## Q6

Physics · Modern Physics

The de-Broglie wavelength of a neutron in thermal equilibrium with heavy water at a temperature $T$ (Kelvin) and mass $m$, is

- (1) $\dfrac{h}{\sqrt{mkT}}$
- **(2)** $\dfrac{h}{\sqrt{3mkT}}$
- (3) $\dfrac{2h}{\sqrt{3mkT}}$
- (4) $\dfrac{2h}{\sqrt{mkT}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. de-Broglie wavelength
2. $\lambda = \frac{h}{mv}$
3. $= \frac{h}{\sqrt{2m(\mathrm{KE})}}$
4. $= \frac{h}{\sqrt{2m\left(\frac{3}{2}kT\right)}}$
5. $\lambda = \frac{h}{\sqrt{3mkT}}$

**Solved independently** (answer withheld)

1. A neutron in thermal equilibrium at temperature $T$ has mean kinetic energy $E = \frac{3}{2}kT$.
2. Momentum $p = \sqrt{2mE} = \sqrt{2m \cdot \frac{3}{2}kT} = \sqrt{3mkT}$.
3. de Broglie wavelength $\lambda = \frac{h}{p} = \frac{h}{\sqrt{3mkT}}$, which is option $2$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q006_6b712bb9_27102026.png?v=6b712bb934b1)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q006_b4c78635_27102026.png?v=b4c786355763)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** de Broglie wavelength of a thermal particle: $p=\sqrt{2mE}$ with $E=\tfrac{3}{2}kT$ gives $\lambda=\dfrac{h}{\sqrt{3mkT}}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student who remembers equipartition as $\tfrac{1}{2}kT$ for the particle rather than $\tfrac{1}{2}kT$ per degree of freedom sets $\frac{p^2}{2m}=\tfrac{1}{2}kT$ and gets $\frac{h}{\sqrt{mkT}}$. A free neutron has three translational degrees, so $E=\tfrac{3}{2}kT$ and the 3 stays under the root.
- **Why:** This question requires chaining equipartition to the de Broglie relation, demonstrated by the stem's "in thermal equilibrium with heavy water at a temperature $T$" and options that differ only in the 3 under the root and a factor 2.
- **Note:** The four options sit as a grid, $\{h,2h\}$ crossed with $\{\sqrt{mkT},\sqrt{3mkT}\}$; `grid_of_slips` was considered for the set, but only the dropped 3 has a route I can name, so the trap is pinned to option 1.
<!--/ecat-->

## Q7

Physics · Laws of Motion

One end of string of length $l$ is connected to a particle of mass '$m$' and the other end is connected to a small peg on a smooth horizontal table. If the particle moves in circle with speed '$v$', the net force on the particle (directed towards center) will be ($T$ represents the tension in the string)

- **(1)** $T$
- (2) $T+\dfrac{mv^{2}}{l}$
- (3) $T-\dfrac{mv^{2}}{l}$
- (4) Zero

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Centripetal force $\left(\frac{mv^{2}}{l}\right)$ is provided by tension so the net force will be equal to tension $i.e.$, $T$.

**Solved independently** (answer withheld)

1. Vertically, the normal reaction balances gravity: $N = mg$, so these give no net force.
2. The table is smooth, so there is no friction; the only horizontal force on the particle is the tension $T$ along the string towards the peg.
3. Hence the net force towards the centre is $F_{net} = T$ (which equals $\frac{mv^2}{l}$), which is option $1$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 3)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q007_0d33ee1e_27102026.png?v=0d33ee1e6566)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q007_33f5fc77_27102026.png?v=33f5fc771309)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In uniform circular motion the string's tension IS the net inward force; $\frac{mv^{2}}{l}$ is that same force written another way, not a second one.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  A student who writes down 'the centripetal force is $\frac{mv^{2}}{l}$' and then notices that the string also pulls with $T$ adds the two, giving option 2. The tension is what supplies that $\frac{mv^{2}}{l}$, so adding them enters one force twice and the net inward force is just $T$.
- **Why:** This question requires Newton's second law applied to a particle in a circle on a frictionless table, demonstrated by the stem's own note '($T$ represents the tension in the string)' and by options 2 and 3 combining $T$ with $\frac{mv^{2}}{l}$.
- **Note:** The table is smooth and horizontal, so tension is the only horizontal force; nothing is computed and the answer is a named force, which is why this is `apply_rule` and not `calculate`.
<!--/ecat-->

## Q8

Physics · Electromagnetic Induction

Figure shows a circuit contains three identical resistors with resistance $R = 9.0\,\Omega$ each, two identical inductors with inductance $L = 2.0\,\mathrm{mH}$ each, and an ideal battery with emf $\varepsilon = 18\,\mathrm{V}$. The current '$i$' through the battery just after the switch closed is

![printed figure: Battery and open switch feeding three parallel branches: L in series with R, a single R, and R in series with L that has C across it](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q008_b3392921_27102026.svg?v=b3392921aa93)

*Battery and open switch feeding three parallel branches: L in series with R, a single R, and R in series with L that has C across it*

![drawn: Battery and open switch feeding three parallel branches: L in series with R, a single R, and R in series with L that has C across it](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q008_question_7c07361c_27102026.svg?v=7c07361c3b7b)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $2\,\mathrm{mA}$
- (2) $0.2\,\mathrm{A}$
- **(3)** $2\,\mathrm{A}$
- (4) $0$ ampere

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Battery ε in parallel with branches L1-R1, R2, and R3 in series with L2 || C](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q008_sol_1_7de0eb6e_27102026.svg?v=7de0eb6efefb)

*Battery ε in parallel with branches L1-R1, R2, and R3 in series with L2 || C*

![drawn: Battery ε in parallel with branches L1-R1, R2, and R3 in series with L2 || C](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q008_solution_1_1f5fc548_27102026.svg?v=1f5fc54830fe)  
*drawn on the booklet's geometry, checked against its figure spec*

1. At $t = 0$, no current flows through $R_1$ and $R_3$

![printed figure: A cell of emf ε in one loop with the resistor R2, current i along the top wire](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q008_sol_2_83b7c3c4_29102026.svg?v=83b7c3c4232d)

*A cell of emf ε in one loop with the resistor R2, current i along the top wire*

![drawn: A cell of emf ε in one loop with the resistor R2, current i along the top wire](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q008_solution_2_c752d9ee_27102026.svg?v=c752d9eec517)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $i = \frac{\varepsilon}{R_2}$
3. $= \frac{18}{9}$
4. $= 2\,\mathrm{A}$
5. Note : Not correctly framed but the best option out of given is (3).

**Solved independently** (answer withheld)

1. At $t = 0^+$ an inductor opposes any sudden change in current, so each inductor branch carries $i_L = 0$ (acts as an open circuit).
2. Left branch ($L$ in series with $R$) carries no current.
3. Right branch ($R$ in series with $L$) carries no current if the capacitor is ignored, as the stem lists only resistors, inductors and the battery.
4. Only the middle resistor conducts: $i = \frac{\varepsilon}{R} = \frac{18\,\mathrm{V}}{9.0\,\Omega} = 2\,\mathrm{A}$, which is option $3$.

**Subtopic:** LR Circuits · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q008_1252b336_27102026.png?v=1252b336d20f)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q008_3ba3e5fd_27102026.png?v=3ba3e5fd8681)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Just after a switch closes, an inductor holds its own branch current at zero, so only the purely resistive branch draws current from the battery.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who remembers 'the current through an inductor cannot change instantly, so it is zero just after closing' applies that to the battery too and reads the whole circuit as dead, which is option 4. The rule bites only on the two branches that contain an $L$; the middle branch is a bare $R$, so the battery still delivers $18/9 = 2\,\mathrm{A}$.
- **Why:** This question requires the $t=0^{+}$ behaviour of an inductor followed by one division, demonstrated by the stem's 'just after the switch closed' together with $\varepsilon = 18\,\mathrm{V}$ and $R = 9.0\,\Omega$.
<!--/ecat-->

## Q9

Physics · Kinematics

The $x$ and $y$ coordinates of the particle at any time are $x = 5t - 2t^{2}$ and $y = 10t$ respectively, where $x$ and $y$ are in meters and $t$ in seconds. The acceleration of the particle at $t = 2\,\mathrm{s}$ is

- (1) $0$
- (2) $5\,\mathrm{m/s^{2}}$
- **(3)** $-4\,\mathrm{m/s^{2}}$
- (4) $-8\,\mathrm{m/s^{2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $x = 5t - 2t^{2}$ \quad $y = 10t$
2. $\frac{dx}{dt} = 5 - 4t$ \quad $\frac{dy}{dt} = 10$
3. $v_{x} = 5 - 4t$ \quad $v_{y} = 10$
4. $\frac{dv}{dt}x = -4$ \quad $\frac{dv}{dt}y = 10$
5. $a_{x} = -4$ \quad $a_{y} = 0$
6. Acceleration of particle at $t = 2\,\mathrm{s}$ is $= -4\,\mathrm{m/s^{2}}$

**Solved independently** (answer withheld)

1. $v_x = \frac{dx}{dt} = 5 - 4t$.
2. $a_x = \frac{dv_x}{dt} = -4\,\mathrm{m/s^2}$, independent of $t$.
3. $v_y = \frac{dy}{dt} = 10$, so $a_y = \frac{dv_y}{dt} = 0$.
4. At $t = 2\,\mathrm{s}$, $\vec{a} = -4\,\hat{i}\,\mathrm{m/s^2}$, i.e. $-4\,\mathrm{m/s^2}$, which is option $3$.

**Subtopic:** Instantaneous Acceleration · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q009_45ad0405_27102026.png?v=45ad04059025)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q009_004ce3a5_27102026.png?v=004ce3a5c5e5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Instantaneous acceleration is the second derivative of position, and a constant $t^{2}$ coefficient makes it the same at every instant.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The stem names an instant, $t = 2\,\mathrm{s}$, so a student who differentiates once to $v_x = 5 - 4t$ reads the $-4t$ term as the acceleration and substitutes, giving $-8\,\mathrm{m/s^{2}}$. Differentiating the second time gives $-4\,\mathrm{m/s^{2}}$, with no $t$ left in it to substitute into.
- **Why:** This question requires differentiating $x = 5t - 2t^{2}$ twice and $y = 10t$ twice, demonstrated by the $y$ motion contributing nothing and by options 3 and 4 differing only by whether $t = 2\,\mathrm{s}$ was put in.
<!--/ecat-->

## Q10

Physics · Electrostatics

Suppose the charge of a proton and an electron differ slightly. One of them is $-e$, the other is $(e + \Delta e)$. If the net of electrostatic force and gravitational force between two hydrogen atoms placed at a distance $d$ (much greater than atomic size) apart is zero, then $\Delta e$ is of the order of [Given mass of hydrogen $m_h = 1.67 \times 10^{-27}\,\mathrm{kg}$]

- (1) $10^{-20}\,\mathrm{C}$
- (2) $10^{-23}\,\mathrm{C}$
- **(3)** $10^{-37}\,\mathrm{C}$
- (4) $10^{-47}\,\mathrm{C}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $F_e = F_g$
2. $\frac{1}{4\pi\varepsilon_0}\frac{\Delta e^2}{d^2} = \frac{Gm^2}{d^2}$
3. $9 \times 10^{9}\,(\Delta e^2) = 6.67 \times 10^{-11} \times 1.67 \times 10^{-27} \times 1.67 \times 10^{-27}$
4. $\Delta e^2 = \frac{6.67 \times 1.67 \times 1.67}{9} \times 10^{-74}$
5. $\Delta e \approx 10^{-37}$

**Solved independently** (answer withheld)

1. Each hydrogen atom has net charge $(e + \Delta e) - e = \Delta e$.
2. Electrostatic repulsion between the atoms: $F_e = \frac{k (\Delta e)^2}{d^2}$.
3. Gravitational attraction: $F_g = \frac{G m_h^2}{d^2}$.
4. Net force zero: $\frac{k (\Delta e)^2}{d^2} = \frac{G m_h^2}{d^2} \Rightarrow \Delta e = m_h \sqrt{\frac{G}{k}}$.
5. $\sqrt{\frac{G}{k}} = \sqrt{\frac{6.67 \times 10^{-11}}{9 \times 10^{9}}} = \sqrt{7.41 \times 10^{-21}} \approx 8.61 \times 10^{-11}\,\mathrm{C/kg}$.
6. $\Delta e = 1.67 \times 10^{-27} \times 8.61 \times 10^{-11} \approx 1.44 \times 10^{-37}\,\mathrm{C}$, of order $10^{-37}\,\mathrm{C}$, which is option $3$.

**Subtopic:** Coulomb's Law · **Difficulty:** hard (4 steps, 2 of 4 options live)

**Printed in the booklet** (page 4)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q010_ef086770_27102026.png?v=ef0867705c8e)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q010_a3e0218a_27102026.png?v=a3e0218a25ed)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Setting the Coulomb repulsion of the two residual charges equal to the gravitational attraction makes $d$ cancel and leaves $\Delta e = m_h\sqrt{4\pi\varepsilon_0 G}$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  A student who reaches $(\Delta e)^{2} = 4\pi\varepsilon_0 G m_h^{2}$ and then takes the root of the mass only, reading $\sqrt{m_h^{2}} = m_h$ as the whole job, is left with $m_h \times 4\pi\varepsilon_0 G = 1.2\times10^{-47}\,\mathrm{C}$, which is option 4. The constant has to come out of the root as well, giving $m_h\sqrt{4\pi\varepsilon_0 G} = 1.4\times10^{-37}\,\mathrm{C}$.
- **Why:** This question requires equating two inverse-square forces so the separation cancels, demonstrated by the stem's 'the net of electrostatic force and gravitational force between two hydrogen atoms placed at a distance $d$ ... is zero' and by options that are bare orders of magnitude.
- **Note:** Options 1 and 2 ($10^{-20}$ and $10^{-23}\,\mathrm{C}$) sit a decade or four below the elementary charge and no single wrong operation in this balance lands on either, so they are left untagged rather than given a rationale each.
<!--/ecat-->

## Q11

Physics · Thermal Properties of Matter

Two rods $A$ and $B$ of different materials are welded together as shown in figure. Their thermal conductivities are $K_1$ and $K_2$. The thermal conductivity of the composite rod will be

![printed figure: Two rods A and B of length d welded side by side between temperatures T1 and T2](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q011_27fc8fd1_27102026.svg?v=27fc8fd11634)

*Two rods A and B of length d welded side by side between temperatures T1 and T2*

![drawn: Two rods A and B of length d welded side by side between temperatures T1 and T2](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q011_question_74fd02f2_27102026.svg?v=74fd02f2ccc2)  
*drawn on the booklet's geometry, checked against its figure spec*

- **(1)** $\dfrac{K_1 + K_2}{2}$
- (2) $\dfrac{3(K_1 + K_2)}{2}$
- (3) $K_1 + K_2$
- (4) $2(K_1 + K_2)$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Thermal current
2. $H = H_1 + H_2$
3. $= \frac{K_1 A(T_1 - T_2)}{d} + \frac{K_2 A(T_1 - T_2)}{d}$
4. $\frac{K_{EQ} 2A(T_1 - T_2)}{d} = \frac{A(T_1 - T_2)}{d}[K_1 + K_2]$
5. $K_{EQ} = \left[\frac{K_1 + K_2}{2}\right]$

**Solved independently** (answer withheld)

1. The figure shows both rods spanning the same length $d$ between $T_1$ and $T_2$, so they conduct heat in parallel.
2. For parallel conduction the heat currents add: $\frac{K_{eq}(A_1 + A_2)\Delta T}{d} = \frac{K_1 A_1 \Delta T}{d} + \frac{K_2 A_2 \Delta T}{d}$.
3. The two rods appear to have equal cross-section $A_1 = A_2 = A$, so $K_{eq} \cdot 2A = K_1 A + K_2 A$.
4. $K_{eq} = \frac{K_1 + K_2}{2}$, which is option $1$.

**Subtopic:** Connection of Rods · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 4)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q011_0a55d6be_27102026.png?v=0a55d6bebe51)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q011_5f47e2e4_27102026.png?v=5f47e2e422d3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Rods welded side by side conduct in parallel: their conductances add, but the cross-section doubles too, so $K_{eq} = \frac{K_1+K_2}{2}$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who remembers only 'in parallel they add' writes $K_1+K_2$ and stops, which is option 3. That sum is the conductance of the two rods together, and it is carried by twice the area of one rod, so the composite rod's conductivity is half of it.
- **Why:** This question requires the parallel heat-flow combination with the doubled area taken into account, demonstrated by the figure showing rods $A$ and $B$ welded side by side across the same length $d$ between $T_1$ and $T_2$.
- **Note:** Options 2 and 4 are the same sum scaled by $\tfrac{3}{2}$ and $2$; no stated rule produces either factor, so only option 3 is tagged.
<!--/ecat-->

## Q12

Physics · Electrostatics

The diagrams below show regions of equipotentials. A positive charge is moved from $A$ to $B$ in each diagram.

![printed figure: Four regions of equipotentials (a)-(d), a positive charge moved from A to B in each](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q012_3c333c20_27102026.svg?v=3c333c20484f)

*Four regions of equipotentials (a)-(d), a positive charge moved from A to B in each*

![drawn: Four regions of equipotentials (a)-(d), a positive charge moved from A to B in each](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q012_question_48fa9954_27102026.svg?v=48fa99548c5d)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) Maximum work is required to move $q$ in figure (c).
- **(2)** In all the four cases the work done is the same.
- (3) Minimum work is required to move $q$ in figure (a).
- (4) Maximum work is required to move $q$ in figure (b).

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Work done $w = q\Delta V$
2. $\Delta V$ is same in all the cases so work is done will be same in all the cases.

**Solved independently** (answer withheld)

1. Work done moving a charge in an electrostatic field depends only on end potentials: $W = q(V_B - V_A)$.
2. From the figure, in each of (a), (b), (c), (d) point $A$ is on the $10\,\text{V}$ surface and $B$ on the $40\,\text{V}$ surface.
3. $W = q(40 - 10) = 30q$ in all four cases, so the work is the same, which is option $2$.

**Subtopic:** Equipotential Surfaces · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 4)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q012_d30c2076_27102026.png?v=d30c2076a7b7)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q012_6f7d9f28_27102026.png?v=6f7d9f283a56)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Work done on a charge moved between two equipotentials depends only on the two potentials, not on the path length or on how the surfaces happen to be drawn.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The equipotentials in figure (c) are drawn furthest apart, so a student who reaches for $W = qEd$ and measures the picture makes (c) the costliest move. Every panel carries the charge from the $10\,\mathrm{V}$ surface to the $40\,\mathrm{V}$ one, so the work is $30q$ in all four and option 2 holds.
- **Why:** This question requires the path-independence of electrostatic work, demonstrated by all four panels labelling $A$ on the $10\,\mathrm{V}$ surface and $B$ on the $40\,\mathrm{V}$ surface while only the spacing and curvature change.
- **Note:** No statement block is printed; the stem is an instruction and each option is a full claim to be judged, so the printed shape is `statements`. The figure supplies only labels that are identical across the four panels, so nothing is measured off it and the deciding work is the rule, not the reading.
<!--/ecat-->

## Q13

Physics · Modern Physics

The ratio of wavelengths of the last line of Balmer series and the last line of Lyman series is

- (1) $2$
- (2) $1$
- **(3)** $4$
- (4) $0.5$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For last Balmer series
2. $\frac{1}{\lambda_b} = R\left[\frac{1}{2^2} - \frac{1}{\infty^2}\right]$
3. $\lambda_b = \frac{4}{R}$
4. For last Lyman series
5. $\frac{1}{\lambda_l} = R\left[\frac{1}{1^2} - \frac{1}{\infty^2}\right]$
6. $\lambda_l = \frac{1}{R}$
7. $\frac{\lambda_b}{\lambda_l} = \frac{\frac{4}{R}}{\frac{1}{R}}$
8. $\frac{\lambda_b}{\lambda_l} = 4$

**Solved independently** (answer withheld)

1. The last line of a series is the series limit, a transition from $n_i = \infty$.
2. Balmer: $\frac{1}{\lambda_B} = R\left(\frac{1}{2^2} - \frac{1}{\infty^2}\right) = \frac{R}{4}$, so $\lambda_B = \frac{4}{R}$.
3. Lyman: $\frac{1}{\lambda_L} = R\left(\frac{1}{1^2} - \frac{1}{\infty^2}\right) = R$, so $\lambda_L = \frac{1}{R}$.
4. $\frac{\lambda_B}{\lambda_L} = \frac{4/R}{1/R} = 4$, which is option $3$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 4)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q013_9f700083_27102026.png?v=9f700083460a)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q013_9c3ee60f_27102026.png?v=9c3ee60fce44)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The last line of a hydrogen series is its limit ($n\to\infty$), so the wavelength there is set by the lower level alone: $\lambda_{\text{limit}} = n^2/R$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  At the series limit $\lambda = n^2/R$, so the ratio is $2^2/1^2 = 4$. A student who carries the dependence as $\lambda \propto n$ instead of $n^2$ takes $2/1$ and stops at $2$.
- **Why:** This question requires the factor by which the series-limit wavelength changes when the lower level moves from $n=1$ to $n=2$, demonstrated by 'The ratio of wavelengths of the last line of Balmer series and the last line of Lyman series' with four bare numbers as the options.
<!--/ecat-->

## Q14

Physics · Wave Optics

Young’s double slit experiment is first performed in air and then in a medium other than air. It is found that $8^{\text{th}}$ bright fringe in the medium lies where $5^{\text{th}}$ dark fringe lies in air. The refractive index of the medium is nearly

- (1) $1.25$
- (2) $1.59$
- (3) $1.69$
- **(4)** $1.78$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $X_{1} = X_{5\text{th dark}} = (2 \times 5 - 1)\,\frac{\lambda D}{2d}$
2. $X_{2} = X_{8\text{th bright}} = 8\,\frac{\lambda D}{\mu d}$
3. $X_{1} = X_{2}$
4. $\frac{9}{2}\,\frac{\lambda D}{d} = 8\,\frac{\lambda D}{\mu d}$
5. $\mu = \frac{16}{9} = 1.78$

**Solved independently** (answer withheld)

1. In the medium the wavelength becomes $\lambda' = \frac{\lambda}{n}$.
2. Position of the $8^{\text{th}}$ bright fringe in the medium: $y = \frac{8\lambda' D}{d} = \frac{8\lambda D}{n d}$.
3. Position of the $5^{\text{th}}$ dark fringe in air: $y = \frac{(2\cdot 5 - 1)\lambda D}{2d} = \frac{4.5\lambda D}{d}$.
4. Equate: $\frac{8}{n} = 4.5$.
5. $n = \frac{8}{4.5} \approx 1.78$, which is option $4$.

**Subtopic:** Young's Double-Slit Experiment (YDSE) · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 5)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q014_074152ce_27102026.png?v=074152cedc55)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q014_7486380b_27102026.png?v=7486380b23c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Immersing the slits shrinks the fringe width to $\beta/\mu$, so a high-order fringe in the medium falls where a lower-order air fringe sat; dark fringes sit at half-integer orders
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The 5th dark fringe sits at $4.5\lambda D/d$, one half-order short of the 5th bright fringe. A student who uses the bright-fringe position for it solves $8/\mu = 5$ and gets $1.6$, which is the printed $1.59$, instead of $8/4.5 = 1.78$.
- **Why:** This question requires computing the refractive index from the coincidence of two fringe positions, demonstrated by '$8^{\text{th}}$ bright fringe in the medium lies where $5^{\text{th}}$ dark fringe lies in air' and four numerical options.
<!--/ecat-->

## Q15

Physics · Oscillations

A particle executes linear simple harmonic motion with an amplitude of $3\,\mathrm{cm}$. When the particle is at $2\,\mathrm{cm}$ from the mean position, the magnitude of its velocity is equal to that of its acceleration. Then its time period in seconds is

- (1) $\dfrac{\sqrt{5}}{\pi}$
- (2) $\dfrac{\sqrt{5}}{2\pi}$
- **(3)** $\dfrac{4\pi}{\sqrt{5}}$
- (4) $\dfrac{2\pi}{\sqrt{3}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $v = \omega\sqrt{A^{2} - x^{2}}$
2. $a = x\omega^{2}$
3. $v = a$
4. $\omega\sqrt{A^{2} - x^{2}} = x\omega^{2}$
5. $\sqrt{(3)^{2} - (2)^{2}} = 2\left(\frac{2\pi}{T}\right)$
6. $\sqrt{5} = \frac{4\pi}{T}$
7. $T = \frac{4\pi}{\sqrt{5}}$

**Solved independently** (answer withheld)

1. Speed in SHM: $|v| = \omega\sqrt{A^2 - x^2} = \omega\sqrt{3^2 - 2^2} = \sqrt{5}\,\omega$.
2. Acceleration magnitude: $|a| = \omega^2 x = 2\omega^2$.
3. Set equal: $\sqrt{5}\,\omega = 2\omega^2 \Rightarrow \omega = \frac{\sqrt{5}}{2}\,\mathrm{s^{-1}}$.
4. $T = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{5}/2} = \frac{4\pi}{\sqrt{5}}\,\mathrm{s}$, which is option $3$.

**Subtopic:** Calculate Time Period of SHM · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 5)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q015_d10723e2_27102026.png?v=d10723e26c84)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q015_48698f36_27102026.png?v=48698f365263)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In SHM the speed is $\omega\sqrt{A^2-x^2}$ and the acceleration is $\omega^2 x$; equating their magnitudes at a stated displacement fixes $\omega$, and hence the period
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Equating $\omega\sqrt{5} = 2\omega^2$ gives $\omega = \sqrt5/2$ and $T = 4\pi/\sqrt5$. The other three only rearrange $\sqrt5$, $\pi$ and a factor of 2 or 4, and no step of this problem produces any of them: $2\pi/\sqrt3$ would need an amplitude of 2 cm with a displacement of 1 cm, which the stem does not print.
- **Why:** This question requires solving $\omega\sqrt{A^2-x^2} = \omega^2 x$ for the time period, demonstrated by 'the magnitude of its velocity is equal to that of its acceleration' with an amplitude of $3\,\mathrm{cm}$ and a displacement of $2\,\mathrm{cm}$.
<!--/ecat-->

## Q16

Physics · Thermodynamics

Thermodynamic processes are indicated in the following diagram. Match the following

![printed figure: P-V diagram with isotherms 300 K, 500 K, 700 K and four processes I, II, III, IV from state i](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q016_b7bed811_27102026.svg?v=b7bed81193ee)

*P-V diagram with isotherms 300 K, 500 K, 700 K and four processes I, II, III, IV from state i*

![drawn: P-V diagram with isotherms 300 K, 500 K, 700 K and four processes I, II, III, IV from state i](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q016_question_298ab2aa_27102026.svg?v=298ab2aa34bb)  
*drawn on the booklet's geometry, checked against its figure spec*

| List-I | | List-II | |
|---|---|---|---|
| P | Process I | a | Adiabatic |
| Q | Process II | b | Isobaric |
| R | Process III | c | Isochoric |
| S | Process IV | d | Isothermal |

- (1) P $\rightarrow$ a, Q $\rightarrow$ c, R $\rightarrow$ d, S $\rightarrow$ b
- **(2)** P $\rightarrow$ c, Q $\rightarrow$ a, R $\rightarrow$ d, S $\rightarrow$ b
- (3) P $\rightarrow$ c, Q $\rightarrow$ d, R $\rightarrow$ b, S $\rightarrow$ a
- (4) P $\rightarrow$ d, Q $\rightarrow$ b, R $\rightarrow$ a, S $\rightarrow$ c

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Process I = Isochoric
2. II = Adiabatic
3. III = Isothermal
4. IV = Isobaric

**Solved independently** (answer withheld)

1. Process I is a vertical line on the $P$-$V$ diagram, so $V$ is constant: isochoric, $P \rightarrow c$.
2. Process II is steeper than the isotherm through $i$ and ends on the $300\,\text{K}$ curve, so $T$ falls with no heat exchange: adiabatic, $Q \rightarrow a$.
3. Process III runs along the $500\,\text{K}$ curve, so $T$ is constant: isothermal, $R \rightarrow d$.
4. Process IV is a horizontal line, so $P$ is constant: isobaric, $S \rightarrow b$.
5. $P \rightarrow c,\ Q \rightarrow a,\ R \rightarrow d,\ S \rightarrow b$ is option $2$.

**Subtopic:** Thermodynamic Processes · **Difficulty:** medium (4 steps, 2 of 4 options live)

**Printed in the booklet** (page 5)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q016_377c9379_27102026.png?v=377c9379232b)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q016_fc0db18b_27102026.png?v=fc0db18bdc99)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Naming a thermodynamic process from its path on a $P$-$V$ diagram: vertical is isochoric, horizontal is isobaric, along one isotherm is isothermal, and a curve that crosses to a lower isotherm is adiabatic.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who carries only "the adiabatic curve is steeper than the isotherm" looks for the steepest path, and process I is drawn as a straight vertical line, so I is read as adiabatic and II is left with isochoric, which is option 1. But a vertical path on a $P$-$V$ diagram holds $V$ fixed, so I is the isochoric one, and it is II that leaves the 500 K isotherm through $i$ and lands on the 300 K isotherm.
- **Why:** This question requires reading each printed path against the three isotherms before any name can be assigned, demonstrated by List I being only "Process I" to "Process IV" while the figure carries "300 K, 500 K, 700 K" and all four paths starting from the single state $i$.
<!--/ecat-->

## Q17

Physics · Capacitance

A capacitor is charged by a battery. The battery is removed and another identical uncharged capacitor is connected in parallel. The total electrostatic energy of resulting system

- (1) Increases by a factor of 4
- **(2)** Decreases by a factor of 2
- (3) Remains the same
- (4) Increases by a factor of 2

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: A capacitor C and a cell V in one rectangular loop](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q017_sol_1_b280802e_27102026.svg?v=b280802e9a22)

*A capacitor C and a cell V in one rectangular loop*

![drawn: A capacitor C and a cell V in one rectangular loop](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q017_solution_1_8a420a97_27102026.svg?v=8a420a97bce3)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Charge on capacitor
2. $q = CV$
3. when it is connected with another uncharged capacitor.

![printed figure: Two capacitors C connected in parallel in one loop, the charged one carrying q](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q017_sol_2_60ebe223_27102026.svg?v=60ebe223d588)

*Two capacitors C connected in parallel in one loop, the charged one carrying q*

![drawn: Two capacitors C connected in parallel in one loop, the charged one carrying q](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q017_solution_2_4f378fda_27102026.svg?v=4f378fda6a65)  
*drawn on the booklet's geometry, checked against its figure spec*

4. $V_c = \frac{q_1 + q_2}{C_1 + C_2} = \frac{q + 0}{C + C}$
5. $V_c = \frac{V}{2}$
6. Initial energy
7. $U_i = \frac{1}{2}CV^2$
8. Final energy
9. $U_f = \frac{1}{2}C\left(\frac{V}{2}\right)^2 + \frac{1}{2}C\left(\frac{V}{2}\right)^2$
10. $= \frac{CV^2}{4}$
11. Loss of energy $= U_{\mathrm{i}} - U_f$
12. $= \frac{CV^2}{4}$
13. $i.e.$ decreases by a factor $(2)$

**Solved independently** (answer withheld)

1. With the battery removed, the charge $Q$ on the first capacitor is conserved; initial energy $U = \frac{Q^2}{2C}$.
2. Connecting an identical uncharged capacitor in parallel gives $C' = C + C = 2C$ with the same total charge $Q$.
3. $U' = \frac{Q^2}{2C'} = \frac{Q^2}{4C} = \frac{U}{2}$.
4. The energy decreases by a factor of $2$, which is option $2$.

**Subtopic:** Redistribution of Charges, Energy Stored in a Capacitor · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 5)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q017_765d3c76_27102026.png?v=765d3c760eb7)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q017_a98dedf6_27102026.png?v=a98dedf6e6ae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Once the battery is disconnected the charge is what stays fixed, so doubling the capacitance halves $Q^2/2C$ — the missing half leaves as heat while the charge redistributes
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  A student who holds $V$ fixed, as it would be with the battery still attached, doubles $C$ in $U = \frac{1}{2}CV^2$ and reads off twice the energy. With the battery removed it is $Q$ that is fixed, so $U = Q^2/2C$ halves instead.
- **Also:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  'Remains the same' is the true verdict for the total charge, which is conserved in this connection, so a student who carries conservation straight over from charge to energy picks it. The energy is not conserved — half of it is dissipated as the charge shares out.
- **Why:** This question requires knowing which quantity is held fixed after the source is disconnected and by what factor the stored energy then moves, demonstrated by 'The battery is removed and another identical uncharged capacitor is connected in parallel' with options phrased as factors.
<!--/ecat-->

## Q18

Physics · Modern Physics

The photoelectric threshold wavelength of silver is $3250 \times 10^{-10}\,\mathrm{m}$. The velocity of the electron ejected from a silver surface by ultraviolet light of wavelength $2536 \times 10^{-10}\,\mathrm{m}$ is (Given $h = 4.14 \times 10^{-15}\,\mathrm{eVs}$ and $c = 3 \times 10^{8}\,\mathrm{ms^{-1}}$)

- **(1)** $\approx 6 \times 10^{5}\,\mathrm{ms^{-1}}$
- **(2)** $\approx 0.6 \times 10^{6}\,\mathrm{ms^{-1}}$
- (3) $\approx 61 \times 10^{3}\,\mathrm{ms^{-1}}$
- (4) $\approx 0.3 \times 10^{6}\,\mathrm{ms^{-1}}$

**Answer** — booklet: (1, 2) · independent solve: (1) · agree

**Publisher's solution**

1. $\lambda_0 = 3250 \times 10^{-10}\,\mathrm{m}$
2. $\lambda = 2536 \times 10^{-10}\,\mathrm{m}$
3. $\phi = \frac{1242\,\mathrm{eV\text{-}nm}}{325\,\mathrm{nm}} = 3.82\,\mathrm{eV}$
4. $h\nu = \frac{1242\,\mathrm{eV\text{-}nm}}{253.6\,\mathrm{nm}} = 4.89\,\mathrm{eV}$
5. $\mathrm{KE}_{\mathrm{max}} = (4.89 - 3.82)\,\mathrm{eV} = 1.077\,\mathrm{eV}$
6. $\frac{1}{2}mv^{2} = 1.077 \times 1.6 \times 10^{-19}$
7. $v = \sqrt{\frac{2 \times 1.077 \times 1.6 \times 10^{-19}}{9.1 \times 10^{-31}}}$
8. $v = 0.6 \times 10^{6}\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. $hc = 4.14 \times 10^{-15}\,\mathrm{eVs} \times 3 \times 10^{8}\,\mathrm{ms^{-1}} = 1.242 \times 10^{-6}\,\mathrm{eV\,m}$.
2. $E = \frac{hc}{\lambda} = \frac{1.242 \times 10^{-6}}{2.536 \times 10^{-7}} \approx 4.897\,\mathrm{eV}$.
3. $\phi_0 = \frac{hc}{\lambda_0} = \frac{1.242 \times 10^{-6}}{3.25 \times 10^{-7}} \approx 3.822\,\mathrm{eV}$.
4. $K_{max} = E - \phi_0 \approx 1.076\,\mathrm{eV} = 1.076 \times 1.6 \times 10^{-19}\,\mathrm{J} \approx 1.72 \times 10^{-19}\,\mathrm{J}$.
5. $v = \sqrt{\frac{2K_{max}}{m_e}} = \sqrt{\frac{2 \times 1.72 \times 10^{-19}}{9.11 \times 10^{-31}}} \approx \sqrt{3.78 \times 10^{11}} \approx 6.15 \times 10^{5}\,\mathrm{ms^{-1}}$.
6. $6.15 \times 10^{5}\,\mathrm{ms^{-1}} \approx 6 \times 10^{5}\,\mathrm{ms^{-1}}$, which is option $1$ (option $2$, $0.6 \times 10^{6}$, is the same value).

**Subtopic:** Photoelectric Effect · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 6)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q018_6a3593d9_27102026.png?v=6a3593d9bfdf)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q018_77de3ffa_27102026.png?v=77de3ffa0b7e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Einstein's photoelectric equation: the ejected electron's kinetic energy is the photon energy minus the work function that the threshold wavelength fixes
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Rearranging $K = \frac{1}{2}mv^2$ as $v = \sqrt{K/2m}$ instead of $\sqrt{2K/m}$ puts the 2 under the mass. With $K = 1.08\,\mathrm{eV}$ that yields $3.1\times10^{5}\,\mathrm{ms^{-1}}$, exactly half of the $6.1\times10^{5}$ the correct rearrangement gives.
- **Why:** This question requires computing the ejected electron's speed from the threshold and incident wavelengths, demonstrated by 'The velocity of the electron ejected from a silver surface by ultraviolet light of wavelength $2536 \times 10^{-10}\,\mathrm{m}$' with $h$ and $c$ supplied in the stem.
- **Note:** Options 1 and 2 are the same number written two ways, $6 \times 10^{5} = 0.6 \times 10^{6}\,\mathrm{ms^{-1}}$, and the answer line awards both. The four options are bare values, so the printed shape is a plain MCQ.
<!--/ecat-->

## Q19

Physics · Units and Measurements

A physical quantity of the dimensions of length that can be formed out of $c$, $G$ and $\dfrac{e^2}{4\pi\varepsilon_0}$ is [$c$ is velocity of light, $G$ is universal constant of gravitation and $e$ is charge]

- **(1)** $\dfrac{1}{c^2}\left[G\dfrac{e^2}{4\pi\varepsilon_0}\right]^{\frac{1}{2}}$
- (2) $c^2\left[G\dfrac{e^2}{4\pi\varepsilon_0}\right]^{\frac{1}{2}}$
- (3) $\dfrac{1}{c^2}\left[\dfrac{e^2}{G4\pi\varepsilon_0}\right]^{\frac{1}{2}}$
- (4) $\dfrac{1}{c}G\dfrac{e^2}{4\pi\varepsilon_0}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Let $\dfrac{e^2}{4\pi\varepsilon_0} = A = \mathrm{ML^{3}T^{-2}}$
2. $l = C^{x}G^{y}(A)^{z}$
3. $L = [\mathrm{LT^{-1}}]^{x}\,[\mathrm{M^{-1}L^{3}T^{-2}}]^{y}\,[\mathrm{ML^{3}T^{-2}}]^{z}$
4. $-y + z = 0 \Rightarrow y = z$ ...(i)
5. $x + 3y + 3z = 1$ ...(ii)
6. $-x - 4z = 0$ ...(iii)
7. From (i), (ii) & (iii)
8. $z = y = \dfrac{1}{2},\ x = -2$

**Solved independently** (answer withheld)

1. From Coulomb's law $F = \frac{e^2}{4\pi\varepsilon_0 r^2}$, so $\left[\frac{e^2}{4\pi\varepsilon_0}\right] = [F r^2] = M L^3 T^{-2}$.
2. From $F = \frac{G m^2}{r^2}$, $[G] = M^{-1} L^3 T^{-2}$.
3. $\left[G\frac{e^2}{4\pi\varepsilon_0}\right] = M^{-1}L^3T^{-2} \cdot M L^3 T^{-2} = L^6 T^{-4}$.
4. $\left[G\frac{e^2}{4\pi\varepsilon_0}\right]^{1/2} = L^3 T^{-2}$.
5. $[c^2] = L^2 T^{-2}$, so $\frac{1}{c^2}\left[G\frac{e^2}{4\pi\varepsilon_0}\right]^{1/2} = \frac{L^3T^{-2}}{L^2T^{-2}} = L$, which is option $1$.

**Subtopic:** Deducing Relation Among the Physical Quantities Using Dimensional Equation · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 6)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q019_6707a655_27102026.png?v=6707a6553f33)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q019_4776a781_27102026.png?v=4776a781ff42)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Dimensional homogeneity: choose the exponents of $c$, $G$ and $e^2/4\pi\varepsilon_0$ so that mass and time cancel and one power of length survives
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  $G$ carries $M^{-1}$ and $e^2/4\pi\varepsilon_0$ carries $M^{+1}$, so the mass cancels when the two are multiplied. A student who cancels by dividing puts $G$ underneath, which leaves $\sqrt{M^2}$ in the bracket and gives mass, not length.
- **Why:** This question requires deriving which combination of the three constants carries the dimension of length, demonstrated by 'A physical quantity of the dimensions of length that can be formed out of $c$, $G$ and $\dfrac{e^2}{4\pi\varepsilon_0}$' with four symbolic options.
<!--/ecat-->

## Q20

Physics · Waves

Two cars moving in opposite directions approach each other with speed of $22\,\mathrm{m/s}$ and $16.5\,\mathrm{m/s}$ respectively. The driver of the first car blows a horn having a frequency $400\,\mathrm{Hz}$. The frequency heard by the driver of the second car is [velocity of sound $340\,\mathrm{m/s}$]

- (1) $350\,\mathrm{Hz}$
- (2) $361\,\mathrm{Hz}$
- (3) $411\,\mathrm{Hz}$
- **(4)** $448\,\mathrm{Hz}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $f_{A} = f\left[\frac{v + v_{o}}{v - v_{s}}\right]$
2. $= 400\left[\frac{340 + 16.5}{340 - 22}\right]$
3. $f_{A} = 448\,\mathrm{Hz}$

**Solved independently** (answer withheld)

1. Source (first car) moves toward the observer with $v_s = 22\,\mathrm{m/s}$; observer (second car) moves toward the source with $v_o = 16.5\,\mathrm{m/s}$.
2. $f' = f\,\frac{v + v_o}{v - v_s}$.
3. $f' = 400 \times \frac{340 + 16.5}{340 - 22} = 400 \times \frac{356.5}{318}$.
4. $f' = \frac{142600}{318} \approx 448\,\mathrm{Hz}$, which is option $4$.

**Subtopic:** Doppler Effect · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 7)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q020_70836801_27102026.png?v=7083680105bd)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q020_7a4d9260_27102026.png?v=7a4d9260312e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Doppler effect with source and observer both approaching: $f' = f\dfrac{v+v_o}{v-v_s}$, each speed entering on its own side of the fraction
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The formula gives $400 \times \frac{340+16.5}{340-22} = 448$ Hz. Inverting both signs gives $357$ Hz, which is not printed, and the half-done routes that put the closing speed $38.5\,\mathrm{m/s}$ into the numerator alone ($445$ Hz) or the denominator alone ($451$ Hz) both round to the key. $350$, $361$ and $411$ are not produced by any named misstep on the printed numbers.
- **Why:** This question requires computing the received frequency with both speeds placed correctly in the Doppler formula, demonstrated by 'Two cars moving in opposite directions approach each other with speed of $22\,\mathrm{m/s}$ and $16.5\,\mathrm{m/s}$ respectively' and four frequencies as the options.
<!--/ecat-->

## Q21

Physics · Semiconductor Electronics

In a common emitter transistor amplifier the audio signal voltage across the collector is $3\,\mathrm{V}$. The resistance of collector is $3\,\mathrm{k\Omega}$. If current gain is $100$ and the base resistance is $2\,\mathrm{k\Omega}$, the voltage and power gain of the amplifier is

- (1) $200$ and $1000$
- (2) $15$ and $200$
- **(3)** $150$ and $15000$
- (4) $20$ and $2000$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Current gain $(\beta) = 100$
2. Voltage gain $(A_V) = \beta\frac{R_c}{R_b}$
3. $= 100\left(\frac{3}{2}\right)$
4. $= 150$
5. Power gain $= A_V\,\beta$
6. $= 150\,(100)$
7. $= 15000$

**Solved independently** (answer withheld)

1. Voltage gain of a CE amplifier: $A_V = \beta \frac{R_C}{R_B}$.
2. $A_V = 100 \times \frac{3\,\mathrm{k\Omega}}{2\,\mathrm{k\Omega}} = 150$.
3. Power gain: $A_P = \beta \times A_V$.
4. $A_P = 100 \times 150 = 15000$, which is option $3$.

**Subtopic:** Transistor as an Amplifier (Common Emitter Configuration): Voltage, Current and Power Gain · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 7)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q021_e6455572_27102026.png?v=e6455572f4c6)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q021_06ed6001_27102026.png?v=06ed600138a1)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Common-emitter amplifier: the voltage gain is $\beta R_C/R_B$ and the power gain is the voltage gain times the current gain
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The working passes through an input signal of $20\,\mathrm{mV}$: $3\,\mathrm{V}/3\,\mathrm{k\Omega} = 1\,\mathrm{mA}$ in the collector, $10\,\mathrm{\mu A}$ in the base, $10\,\mathrm{\mu A}\times 2\,\mathrm{k\Omega} = 20\,\mathrm{mV}$. A student who stops there and reads that 20 as the voltage gain, instead of dividing $3\,\mathrm{V}$ by it to get 150, then multiplies by $\beta$ and lands on the printed pair 20 and 2000.
- **Why:** This question requires computing both gains from the collector and base resistances and the current gain, demonstrated by 'the voltage and power gain of the amplifier is' with every option printing two numbers that must both hold.
- **Note:** Each option pairs a voltage gain with a power gain, so the answer has two halves and half of one scores nothing.
<!--/ecat-->

## Q22

Physics · Semiconductor Electronics

Which one of the following represents forward bias diode?

![printed figure: Four diode-resistor series branches with end potentials, numbered (1) to (4)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q022_10fd60ef_27102026.svg?v=10fd60efc5a3)

*Four diode-resistor series branches with end potentials, numbered (1) to (4)*

![drawn: Four diode-resistor series branches with end potentials, numbered (1) to (4)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q022_question_77166c19_27102026.svg?v=77166c199301)  
*drawn on the booklet's geometry, checked against its figure spec*

- **(1)** $0\,\mathrm{V}$ — $R$ — $-2\,\mathrm{V}$
- (2) $-4\,\mathrm{V}$ — $R$ — $-3\,\mathrm{V}$
- (3) $-2\,\mathrm{V}$ — $R$ — $+2\,\mathrm{V}$
- (4) $3\,\mathrm{V}$ — $R$ — $5\,\mathrm{V}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In forward bias, $p$-type semiconductor is at higher potential w.r.t. $n$-type semiconductor.

**Solved independently** (answer withheld)

1. From the figure, each diode's arrow points right, so the anode (p-side) is on the left terminal and the cathode (n-side) is towards $R$ on the right.
2. A diode is forward biased when $V_{p} > V_{n}$.
3. Option 1: $V_p = 0\,\mathrm{V} > V_n = -2\,\mathrm{V}$, forward biased.
4. Option 2: $-4\,\mathrm{V} < -3\,\mathrm{V}$; option 3: $-2\,\mathrm{V} < +2\,\mathrm{V}$; option 4: $3\,\mathrm{V} < 5\,\mathrm{V}$; all reverse biased.
5. Hence the answer is option $1$.

**Subtopic:** PN Junction Diode Under Forward Bias · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 7)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q022_89b721b6_27102026.png?v=89b721b6f40a)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q022_76fda0a2_27102026.png?v=76fda0a277f6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A diode is forward biased when its p-side sits at the higher potential; only the difference across the junction counts, not whether the end voltages are positive
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  A student who holds the condition as 'the p-side must be at a positive voltage' rather than 'at the higher potential' rejects the key's $0\,\mathrm{V}$ and $-2\,\mathrm{V}$ and takes the branch whose two ends are both positive. In that branch the p-side is at $3\,\mathrm{V}$ against $5\,\mathrm{V}$, so it is 2 V lower and the diode is reverse biased.
- **Why:** This question requires reading the end potentials off four drawn branches and applying the forward-bias condition to each, demonstrated by 'Which one of the following represents forward bias diode?' with the four diode-resistor branches and their potentials printed only in the figure.
- **Note:** The four options are drawn circuit branches, each a diode and a resistor in series with a potential marked at either end.
<!--/ecat-->

## Q23

Physics · Oscillations

A spring of force constant $k$ is cut into lengths of ratio $1 : 2 : 3$. They are connected in series and the new force constant is $k'$. Then they are connected in parallel and force constant is $k''$. Then $k' : k''$ is

- (1) $1 : 6$
- (2) $1 : 9$
- **(3)** $1 : 11$
- (4) $1 : 14$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Spring constant $\propto \frac{1}{\text{length}}$
2. $k \propto \frac{1}{l}$
3. i.e, $k_1 = 6k$
4. $k_2 = 3k$
5. $k_3 = 2k$
6. In series
7. $\frac{1}{k'} = \frac{1}{6k} + \frac{1}{3k} + \frac{1}{2k}$
8. $\frac{1}{k'} = \frac{6}{6k}$
9. $k' = k$
10. $k'' = 6k + 3k + 2k$
11. $k'' = 11k$
12. $\frac{k'}{k''} = \frac{1}{11}$ i.e $k' : k'' = 1 : 11$

**Solved independently** (answer withheld)

1. Spring constant varies inversely with length: $k l = \text{const}$.
2. Lengths in ratio $1:2:3$ are $\frac{L}{6}, \frac{L}{3}, \frac{L}{2}$, so constants are $k_1 = 6k$, $k_2 = 3k$, $k_3 = 2k$.
3. Series: $\frac{1}{k'} = \frac{1}{6k} + \frac{1}{3k} + \frac{1}{2k} = \frac{1+2+3}{6k} = \frac{1}{k}$, so $k' = k$.
4. Parallel: $k'' = 6k + 3k + 2k = 11k$.
5. $k' : k'' = k : 11k = 1 : 11$, which is option $3$.

**Subtopic:** Combination of Springs · **Difficulty:** hard (4 steps, 2 of 4 options live)

**Printed in the booklet** (page 7)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q023_dd2a5044_27102026.png?v=dd2a50443729)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q023_d501eba1_27102026.png?v=d501eba16fd9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** A cut spring piece is stiffer in inverse proportion to its length; series combination adds reciprocals of the constants and parallel adds the constants
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Drop the cutting and treat the three pieces as three springs each of constant $k$: series gives $k/3$, parallel gives $3k$, and the ratio is $1:9$. The pieces are $L/6$, $L/3$ and $L/2$ long, so their constants are $6k$, $3k$ and $2k$, which makes $k' = k$ and $k'' = 11k$.
- **Why:** This question requires the two combination rules applied to the pieces' own force constants, demonstrated by 'A spring of force constant $k$ is cut into lengths of ratio $1 : 2 : 3$' and the answer being asked as 'Then $k' : k''$ is'.
<!--/ecat-->

## Q24

Physics · Semiconductor Electronics

The given electrical network is equivalent to

![printed figure: NOR gate on A and B, then a NOR gate with both inputs joined, then a NOT gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q024_981ca707_29102026.svg?v=981ca7075a3b)

*NOR gate on A and B, then a NOR gate with both inputs joined, then a NOT gate giving Y*

![drawn: NOR gate on A and B, then a NOR gate with both inputs joined, then a NOT gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q024_question_0ced9b32_27102026.svg?v=0ced9b321d2a)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) AND gate
- (2) OR gate
- **(3)** NOR gate
- (4) NOT gate

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $Y = \overline{A + B}$

**Solved independently** (answer withheld)

1. The first gate is a NOR gate: $Y_1 = \overline{A + B}$.
2. The second gate is a NOR gate with both inputs tied together, so it acts as a NOT gate: $Y_2 = \overline{Y_1 + Y_1} = \overline{Y_1} = A + B$.
3. The last gate is a NOT gate: $Y = \overline{Y_2} = \overline{A + B}$.
4. $Y = \overline{A + B}$ is the NOR gate, which is option $3$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 7)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q024_accd3f30_27102026.png?v=accd3f300ce2)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q024_fd7cb54c_27102026.png?v=fd7cb54c1131)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A NOR gate with its two inputs tied together acts as a NOT, and two NOTs in a row cancel, so the chain collapses back to NOR
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The first two gates do give OR: $(A+B)'$ inverted by the second NOR with its inputs joined returns $A+B$. A student who stops at that point has the correct intermediate and misses the third gate, the NOT bubble at the output, which turns $A+B$ back into $(A+B)'$.
- **Why:** This question requires tracing the drawn chain of gates and reducing it to one, demonstrated by 'The given electrical network is equivalent to' with the network — a NOR, then a NOR with both inputs joined, then a NOT — supplied only as a figure.
<!--/ecat-->

## Q25

Physics · Gravitation

The acceleration due to gravity at a height $1\,\mathrm{km}$ above the earth is the same as at a depth $d$ below the surface of earth. Then

- (1) $d = \frac{1}{2}\,\mathrm{km}$
- (2) $d = 1\,\mathrm{km}$
- (3) $d = \frac{3}{2}\,\mathrm{km}$
- **(4)** $d = 2\,\mathrm{km}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Above earth surface
2. $g' = g\left(1 - \frac{2h}{R_e}\right)$
3. $\Delta g' = g\,\frac{2h}{R_e}$ …(1)
4. Below earth surface
5. $g' = g\left(1 - \frac{d}{R_e}\right)$
6. $\Delta g = g\,\frac{d}{R_e}$ …(2)
7. From (1) & (2)
8. $d = 2h$
9. $d = 2 \times 1\,\mathrm{km}$

**Solved independently** (answer withheld)

1. For a small height $h \ll R$, $g_h = g\left(1 - \frac{2h}{R}\right)$.
2. At depth $d$, $g_d = g\left(1 - \frac{d}{R}\right)$.
3. Setting $g_h = g_d$ gives $\frac{2h}{R} = \frac{d}{R}$, so $d = 2h$.
4. $d = 2 \times 1\,\mathrm{km} = 2\,\mathrm{km}$, which is option $4$.

**Subtopic:** Variation in g Due to Height and Rotation, Variation in g Due to Depth Inside the Earth · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 8)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q025_40b36bea_27102026.png?v=40b36bea5443)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q025_aa8a1a46_27102026.png?v=aa8a1a46cf50)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Near the surface $g$ falls as $1-2h/R$ going up but only as $1-d/R$ going down, so matching the two needs a depth twice the height
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  A student who carries both corrections as $1-x/R$, with no factor of 2 on the height one, matches them by setting $d$ equal to $h$ and reads off 1 km. The height correction is $1-2h/R$, so the match is at $d = 2h = 2$ km.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who remembers that one of the two corrections carries a 2 but hangs it on the depth solves $h/R = 2d/R$. That states the relation backwards: it gives $d = h/2 = \frac{1}{2}$ km where the right relation is $d = 2h$.
- **Why:** This question requires equating the height and depth expressions for $g$ and solving for the depth, demonstrated by 'The acceleration due to gravity at a height $1\,\mathrm{km}$ above the earth is the same as at a depth $d$ below the surface of earth'.
<!--/ecat-->

## Q26

Physics · Rotational Motion

Which of the following statements are correct?

- **(a)** Centre of mass of a body always coincides with the centre of gravity of the body.
- **(b)** Centre of mass of a body is the point at which the total gravitational torque on the body is zero
- **(c)** A couple on a body produce both translational and rotational motion in a body.
- **(d)** Mechanical advantage greater than one means that small effort can be used to lift a large load.

- **(1)** (b) and (d)
- (2) (a) and (b)
- (3) (b) and (c)
- (4) (c) and (d)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Centre of mass may or may not coincide with centre of gravity.

**Solved independently** (answer withheld)

1. (a) is false: the centre of mass coincides with the centre of gravity only when $\vec g$ is uniform over the body.
2. (b): in a uniform field $\sum \vec r_i \times m_i \vec g = \left(\sum m_i \vec r_i\right) \times \vec g = 0$ about the CM, so the gravitational torque about the CM is zero; taken as true.
3. (c) is false: a couple has $\vec F_{net} = \vec F + (-\vec F) = 0$, so it gives only rotation, no translation.
4. (d) is true: $MA = \frac{\text{Load}}{\text{Effort}} > 1 \Rightarrow \text{Effort} < \text{Load}$.
5. True set is (b) and (d), which is option $1$.

**Subtopic:** Equilibrium of a Rigid Body · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 8)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q026_588b88d9_27102026.png?v=588b88d9bb25)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q026_2a47fd97_27102026.png?v=2a47fd97b844)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Centre of mass against centre of gravity, a couple as two equal and opposite forces with zero resultant, and mechanical advantage as load divided by effort.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student who learned "centre of mass and centre of gravity are the same point" reads (a) as that very sentence and pairs it with (b), which gives option 2. The word that breaks (a) is "always": once the body is tall enough for $g$ to change over its height the centre of gravity shifts below the centre of mass, and (a) is true only for the uniform field it does not state.
- **Why:** This question requires holding centre of mass apart from centre of gravity and knowing that a couple has no resultant force, demonstrated by (a)'s "always coincides with the centre of gravity" and (c)'s "produce both translational and rotational motion".
<!--/ecat-->

## Q27

Physics · Thermodynamics

A Carnot engine having an efficiency of $\frac{1}{10}$ as heat engine, is used as a refrigerator. If the work done on the system is $10\,\mathrm{J}$, the amount of energy absorbed from the reservoir at lower temperature is

- (1) $1\,\mathrm{J}$
- **(2)** $90\,\mathrm{J}$
- (3) $99\,\mathrm{J}$
- (4) $100\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\beta = \frac{1-\eta}{\eta}$
2. $= \frac{1-\frac{1}{10}}{\frac{1}{10}} = \frac{\frac{9}{10}}{\frac{1}{10}}$
3. $\beta = 9$
4. $\beta = \frac{Q_2}{W}$
5. $Q_2 = 9 \times 10 = 90\,\mathrm{J}$

**Solved independently** (answer withheld)

1. For a reversible Carnot cycle run as a refrigerator, $\eta = \frac{W}{Q_H} = \frac{1}{10}$.
2. $Q_H = \frac{W}{\eta} = 10 \times 10\,\mathrm{J} = 100\,\mathrm{J}$.
3. $Q_L = Q_H - W = 100\,\mathrm{J} - 10\,\mathrm{J} = 90\,\mathrm{J}$, which is option $2$.

**Subtopic:** Refrigerator and Heat Pump, Carnot Engine · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 8)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q027_95379a49_27102026.png?v=95379a4902c9)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q027_8cce0795_27102026.png?v=8cce0795f292)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A Carnot refrigerator's coefficient of performance is set by the engine efficiency: $Q_2/W=(1-\eta)/\eta$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Efficiency $\frac{1}{10}$ with $W=10\,\mathrm{J}$ gives the hot-side heat $Q_1=W/\eta=100\,\mathrm{J}$ in one line, and that is the number a student has in hand first. The cold reservoir supplies only $Q_1-W=90\,\mathrm{J}$, the other $10\,\mathrm{J}$ being the work put in.
- **Why:** This question requires a number computed from the stem's data, demonstrated by 'the work done on the system is $10\,\mathrm{J}$' with four options in joules.
<!--/ecat-->

## Q28

Physics · Magnetic Effect of Electric Current

If $\theta_1$ and $\theta_2$ be the apparent angles of dip observed in two vertical planes at right angles to each other, then the true angle of dip $\theta$ is given by

- **(1)** $\cot^2\theta = \cot^2\theta_1 + \cot^2\theta_2$
- (2) $\tan^2\theta = \tan^2\theta_1 + \tan^2\theta_2$
- (3) $\cot^2\theta = \cot^2\theta_1 - \cot^2\theta_2$
- (4) $\tan^2\theta = \tan^2\theta_1 - \tan^2\theta_2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\cot^2\theta = \cot^2\theta_1 + \cot^2\theta_2$

**Solved independently** (answer withheld)

1. Let the first vertical plane make angle $\alpha$ with the magnetic meridian; the second is at $90^\circ - \alpha$.
2. In the first plane the horizontal component is $H\cos\alpha$, so $\tan\theta_1 = \frac{V}{H\cos\alpha}$, i.e. $\cot\theta_1 = \frac{H\cos\alpha}{V}$.
3. In the second plane the horizontal component is $H\sin\alpha$, so $\cot\theta_2 = \frac{H\sin\alpha}{V}$.
4. Squaring and adding: $\cot^2\theta_1 + \cot^2\theta_2 = \frac{H^2(\cos^2\alpha + \sin^2\alpha)}{V^2} = \frac{H^2}{V^2}$.
5. True dip satisfies $\cot\theta = \frac{H}{V}$, so $\cot^2\theta = \cot^2\theta_1 + \cot^2\theta_2$, which is option $1$.

**Subtopic:** Magnetism and Matter · **Difficulty:** hard (3 steps, 4 of 4 options live)

**Printed in the booklet** (page 8)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q028_de2bcbba_27102026.png?v=de2bcbba0b9a)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q028_f70de838_27102026.png?v=f70de8381114)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Apparent dip: only the horizontal field component is split between the two vertical planes, so the cotangents add in quadrature
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The dip relation a student carries is $\tan\theta=B_V/B_H$, so on being told two apparent dips add in quadrature they write the sum in tangents. The vertical component is the same in both planes and only the horizontal one is resolved, so every term inverts and it is $\cot^2\theta=\cot^2\theta_1+\cot^2\theta_2$.
- **Why:** This question requires deriving the relation between the true dip and two apparent dips, demonstrated by the four options being symbolic equations in $\cot^2$ and $\tan^2$ with no numbers in the stem.
<!--/ecat-->

## Q29

Physics · Magnetic Effect of Electric Current

An arrangement of three parallel straight wires placed perpendicular to plane of paper carrying same current '$I$' along the same direction is shown in Fig. Magnitude of force per unit length on the middle wire '$B$' is given by

![printed figure: Three parallel wires A, B, C perpendicular to the paper, current out of the page; AB = BC = d with a 90 degree angle at B](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q029_417d28c7_27102026.svg?v=417d28c70ca9)

*Three parallel wires A, B, C perpendicular to the paper, current out of the page; AB = BC = d with a 90 degree angle at B*

![drawn: Three parallel wires A, B, C perpendicular to the paper, current out of the page; AB = BC = d with a 90 degree angle at B](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q029_question_5bfd0fef_27102026.svg?v=5bfd0feffc31)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\dfrac{\mu_0 I^2}{2\pi d}$
- (2) $\dfrac{2\mu_0 I^2}{\pi d}$
- (3) $\dfrac{\sqrt{2}\mu_0 I^2}{\pi d}$
- **(4)** $\dfrac{\mu_0 I^2}{\sqrt{2}\pi d}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Force between $BC$ and $AB$ will be same in magnitude.

![printed figure: Forces F on wire B from wires C and A, each at distance d, at 90 degrees](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q029_sol_1_941d1304_27102026.svg?v=941d1304e148)

*Forces F on wire B from wires C and A, each at distance d, at 90 degrees*

![drawn: Forces F on wire B from wires C and A, each at distance d, at 90 degrees](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q029_solution_1_6a1b6937_27102026.svg?v=6a1b69372568)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $F_{BC} = F_{BA} = \frac{\mu_0 I^2}{2\pi d}$
3. $F = \sqrt{2}F_{BC}$
4. $= \sqrt{2}\frac{\mu_0}{2\pi}\frac{I^2}{d}$
5. $F = \frac{\mu_0 I^2}{\sqrt{2}\pi d}$

**Solved independently** (answer withheld)

1. Parallel wires with currents in the same direction attract, so the force on $B$ due to $A$ points from $B$ toward $A$, and the force due to $C$ points from $B$ toward $C$.
2. Each force per unit length has magnitude $F_{BA} = F_{BC} = \frac{\mu_0 I \cdot I}{2\pi d} = \frac{\mu_0 I^2}{2\pi d}$.
3. From the figure, $BA \perp BC$, so the two forces are at $90^\circ$.
4. $F = \sqrt{F_{BA}^2 + F_{BC}^2} = \sqrt{2}\,\frac{\mu_0 I^2}{2\pi d}$.
5. $\sqrt{2}\,\frac{\mu_0 I^2}{2\pi d} = \frac{\mu_0 I^2}{\sqrt{2}\pi d}$, which is option $4$.

**Subtopic:** Force Between Two Parallel Current-Carrying Conductors · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 8)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q029_f209b0d6_27102026.png?v=f209b0d6294a)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q029_b88fbbae_27102026.png?v=b88fbbae13b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Force per unit length between parallel currents, with the two neighbours' equal forces at right angles added as vectors
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $F/l=\mu_0I^2/2\pi d$ is the one formula this chapter supplies, so a student who applies it to a single neighbour writes it straight down. Wire $B$ has two neighbours, both at distance $d$ and $90^\circ$ apart, so the two equal forces compose to $\sqrt2\,\mu_0I^2/2\pi d=\mu_0I^2/\sqrt2\pi d$.
- **Why:** This question requires combining two force-per-length terms into one expression, demonstrated by 'Magnitude of force per unit length on the middle wire' and a figure fixing $AB=BC=d$ with $90^\circ$ at $B$.
- **Note:** The figure is needed, not decorative: the $90^\circ$ angle and the two equal spacings appear nowhere in the stem text.
<!--/ecat-->

## Q30

Physics · Gravitation

Two astronauts are floating in gravitational free space after having lost contact with their spaceship. The two will:

- (1) Keep floating at the same distance between them
- **(2)** Move towards each other
- (3) Move away from each other
- (4) Will become stationary

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Both the astronauts are in the condition of weightness.
2. Gravitational force between them pulls towards each other.

**Solved independently** (answer withheld)

1. In gravitation-free space there is no external field, but the mutual attraction $F = \frac{G m_1 m_2}{r^2}$ between the two astronauts still acts.
2. This attractive force accelerates each astronaut towards the other, while their centre of mass stays at rest because $F_{ext} = 0$.
3. So the separation $r$ decreases and they move towards each other, which is option $2$.

**Subtopic:** Gravitational Force Between Two or More Particles · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 9)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q030_36652072_27102026.png?v=36652072c683)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q030_abaa22a3_27102026.png?v=abaa22a3c152)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Every pair of masses attracts; field-free space removes the outside gravity, not the bodies' own
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 1  
  'Gravitational free space' is read as 'no gravitational force acts here', and on that reading nothing can change, so the separation is kept. The phrase rules out outside fields only; the astronauts are themselves masses, so they attract and close on each other.
- **Proposed:** `stem_phrase_over_read` — the option is exactly what follows from taking a printed stem phrase ('gravitational free space') in a stronger, absolute sense than it carries. condition_missed is for an option that becomes true when a condition the stem states is dropped, but here the phrase is kept and stretched, and the thing overlooked -- that the two bodies are themselves sources of gravity -- is never printed as a condition to drop. nearby_fact does not fit either: nothing about an adjacent body or concept is offered.
- **Why:** This question requires applying the law that any two masses attract to a case with no external field, demonstrated by options that give only a sense of motion -- 'Move towards each other' -- and no quantity.
<!--/ecat-->

## Q31

Physics · Electromagnetic Waves

In an electromagnetic wave in free space the root mean square value of the electric field is $E_{\mathrm{rms}} = 6\,\mathrm{V/m}$. The peak value of the magnetic field is

- (1) $1.41 \times 10^{-8}\,\mathrm{T}$
- **(2)** $2.83 \times 10^{-8}\,\mathrm{T}$
- (3) $0.70 \times 10^{-8}\,\mathrm{T}$
- (4) $4.23 \times 10^{-8}\,\mathrm{T}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\frac{E_{\mathrm{rms}}}{B_{\mathrm{rms}}} = c$
2. $B_{\mathrm{rms}} = \frac{E_{\mathrm{rms}}}{c}$
3. $= \frac{6}{3 \times 10^{8}}$
4. $B_{\mathrm{rms}} = 2 \times 10^{-8}$
5. $B_{\mathrm{rms}} = \frac{B_0}{\sqrt{2}}$
6. $B_0 = \sqrt{2} \times B_{\mathrm{rms}}$
7. $= \sqrt{2} \times 2 \times 10^{-8}$
8. $= 2.83 \times 10^{-8}\,\mathrm{T}$

**Solved independently** (answer withheld)

1. The peak electric field is $E_0 = \sqrt{2}\,E_{\mathrm{rms}}$.
2. $E_0 = 1.414 \times 6\,\mathrm{V/m} = 8.485\,\mathrm{V/m}$.
3. In free space $B_0 = \frac{E_0}{c}$.
4. $B_0 = \frac{8.485}{3 \times 10^{8}}\,\mathrm{T} = 2.83 \times 10^{-8}\,\mathrm{T}$, which is option $2$.

**Subtopic:** Relation Between E, B, and Speed of Light · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 9)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q031_da512b5a_27102026.png?v=da512b5af65f)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q031_584e25c3_27102026.png?v=584e25c3d389)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In an electromagnetic wave $E_0/B_0=c$, and the peak value is $\sqrt2$ times the rms value
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $B_{\mathrm{rms}}=E_{\mathrm{rms}}/c=6/(3\times10^8)=2\times10^{-8}\,\mathrm{T}$ comes first, and the $\sqrt2$ between rms and peak then gets applied as a division, giving $1.41\times10^{-8}\,\mathrm{T}$. Peak is the larger of the two, so the factor multiplies and the value is $2.83\times10^{-8}\,\mathrm{T}$.
- **Why:** This question requires a number computed from the stem's value, demonstrated by '$E_{\mathrm{rms}}=6\,\mathrm{V/m}$' with four options in tesla.
- **Note:** The intermediate $2\times10^{-8}\,\mathrm{T}$ is not printed, so stopping at $B_{\mathrm{rms}}$ lands on no option; every option is a $\sqrt2$ multiple of it.
<!--/ecat-->

## Q32

Physics · Mechanical Properties of Solids

The bulk modulus of a spherical object is ‘$B$’. If it is subjected to uniform pressure ‘$p$’, the fractional decrease in radius is

- (1) $\frac{p}{B}$
- (2) $\frac{B}{3p}$
- (3) $\frac{3p}{B}$
- **(4)** $\frac{p}{3B}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $B = \frac{p}{\left(\frac{\Delta V}{V}\right)}$
2. $\frac{\Delta V}{V} = \frac{p}{B}$
3. $3\frac{\Delta r}{r} = \frac{p}{B}$
4. $\frac{\Delta r}{r} = \frac{p}{3B}$

**Solved independently** (answer withheld)

1. By definition $B = \frac{p}{\Delta V / V}$, so $\frac{\Delta V}{V} = \frac{p}{B}$.
2. $V = \frac{4}{3}\pi r^3 \Rightarrow \frac{\Delta V}{V} = 3\frac{\Delta r}{r}$.
3. $3\frac{\Delta r}{r} = \frac{p}{B} \Rightarrow \frac{\Delta r}{r} = \frac{p}{3B}$, which is option $4$.

**Subtopic:** Relation Between Density, Pressure and Bulk Modulus · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 9)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q032_46fe2566_27102026.png?v=46fe25666e91)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q032_a9e2c8fa_27102026.png?v=a9e2c8fac186)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Bulk modulus ties pressure to volume strain, and for a sphere the volume strain is three times the fractional change in radius
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  $B=p/(\Delta V/V)$ rearranges to $\Delta V/V=p/B$, and since the stem also asks for a fraction a student takes that as the answer. Radius is a length, so $\Delta V/V=3\Delta r/r$ and the radius carries the extra 3, giving $p/3B$.
- **Why:** This question requires deriving the radial strain from the definition of bulk modulus, demonstrated by 'the fractional decrease in radius' with the four options being expressions in $p$ and $B$ alone.
<!--/ecat-->

## Q33

Physics · Ray Optics

The ratio of resolving powers of an optical microscope for two wavelengths $\lambda_1 = 4000\,\text{Å}$ and $\lambda_2 = 6000\,\text{Å}$ is

- (1) $8 : 27$
- (2) $9 : 4$
- **(3)** $3 : 2$
- (4) $16 : 81$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Resolving power $\propto \frac{1}{\lambda}$
2. $\frac{R_1}{R_2} = \frac{\lambda_2}{\lambda_1}$
3. $= \frac{6000\,\text{Å}}{4000\,\text{Å}}$
4. $= \frac{3}{2}$

**Solved independently** (answer withheld)

1. Resolving power of a microscope: $RP = \frac{2\mu \sin\theta}{1.22\,\lambda}$, so $RP \propto \frac{1}{\lambda}$.
2. $\frac{RP_1}{RP_2} = \frac{\lambda_2}{\lambda_1} = \frac{6000\,\text{Å}}{4000\,\text{Å}} = \frac{3}{2}$.
3. $RP_1 : RP_2 = 3 : 2$, which is option $3$.

**Subtopic:** Resolving and Magnifying Power of Microscope · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 9)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q033_49f189cc_27102026.png?v=49f189ccf8d6)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q033_db8cd0fb_27102026.png?v=db8cd0fb482b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Resolving power of a microscope varies inversely with the wavelength, to the first power
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Inverting the wavelengths gives $6000:4000=3:2$, and a student carrying the wavelength as a squared dependence squares that to $9:4$. Resolving power goes as $1/\lambda$ itself, so the ratio stays at the first power.
- **Why:** This question requires how the resolving power scales with wavelength, demonstrated by 'The ratio of resolving powers of an optical microscope for two wavelengths' and four options printed as ratios.
- **Note:** The straight un-inverted ratio $2:3$ is not among the options, so the only wrong routes printed are higher powers of the ratio: $9:4$ is $(3:2)^2$, $8:27$ is $(2:3)^3$, $16:81$ is $(2:3)^4$.
<!--/ecat-->

## Q34

Physics · Work, Energy and Power

Consider a drop of rain water having mass $1\,\mathrm{g}$ falling from a height of $1\,\mathrm{km}$. It hits the ground with a speed of $50\,\mathrm{m/s}$. Take $g$ constant with a value $10\,\mathrm{m/s^2}$. The work done by the (i) gravitational force and the (ii) resistive force of air is

- (1) (i) $-10\,\mathrm{J}$ (ii) $-8.25\,\mathrm{J}$
- (2) (i) $1.25\,\mathrm{J}$ (ii) $-8.25\,\mathrm{J}$
- (3) (i) $100\,\mathrm{J}$ (ii) $8.75\,\mathrm{J}$
- **(4)** (i) $10\,\mathrm{J}$ (ii) $-8.75\,\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $w_{g} + w_{a} = K_{f} - K_{i}$
2. $mgh + w_{a} = \frac{1}{2}mv^{2} - 0$
3. $10^{-3} \times 10 \times 10^{3} + w_{a} = \frac{1}{2} \times 10^{-3} \times (50)^{2}$
4. $w_{a} = -8.75\,\mathrm{J}$ i.e. work done due to air resistance and work done due to gravity $= 10\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Gravitational work: $W_g = mgh = (10^{-3}\,\mathrm{kg})(10\,\mathrm{m/s^2})(1000\,\mathrm{m}) = 10\,\mathrm{J}$.
2. Final kinetic energy: $K_f = \frac{1}{2}mv^2 = \frac{1}{2}(10^{-3})(50)^2 = 1.25\,\mathrm{J}$ (starting from rest, $K_i = 0$).
3. Work-energy theorem: $W_g + W_{air} = K_f - K_i = 1.25\,\mathrm{J}$.
4. $W_{air} = 1.25 - 10 = -8.75\,\mathrm{J}$, so (i) $10\,\mathrm{J}$, (ii) $-8.75\,\mathrm{J}$, which is option $4$.

**Subtopic:** Work–Energy Theorem, Work Done by Gravity or Spring Force · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 9)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q034_8aed7660_27102026.png?v=8aed76600c73)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q034_662cce09_27102026.png?v=662cce09ac52)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Work-energy theorem on a falling drop: gravity does positive work, air resistance negative, and the two together give the kinetic energy
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The drop loses $10\,\mathrm{J}$ of potential energy, so gravity's work gets written with that minus sign as $-10\,\mathrm{J}$. The work done BY gravity is $+mgh=+10\,\mathrm{J}$ because the force and the $1\,\mathrm{km}$ displacement point the same way; the minus belongs to $\Delta U$.
- **Why:** This question requires two numbers computed from the stem's data, demonstrated by 'The work done by the (i) gravitational force and the (ii) resistive force of air is' with each option printing an (i) and an (ii) value.
- **Note:** The options cross the two signs: option 1 carries gravity's $10\,\mathrm{J}$ with the sign flipped, option 3 carries the air's $8.75\,\mathrm{J}$ with the sign flipped. The $-8.25\,\mathrm{J}$ in options 1 and 2 has no arithmetic route from $1\,\mathrm{g}$, $1\,\mathrm{km}$ and $50\,\mathrm{m/s}$; it is a digit away from $-8.75\,\mathrm{J}$.
<!--/ecat-->

## Q35

Physics · Thermal Properties of Matter

A spherical black body with a radius of $12\,\mathrm{cm}$ radiates $450\,\mathrm{watt}$ power at $500\,\mathrm{K}$. If the radius were halved and the temperature doubled, the power radiated in watt would be

- (1) $225$
- (2) $450$
- (3) $1000$
- **(4)** $1800$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Rate of power loss
2. $r \propto R^{2}T^{4}$
3. $\frac{r_1}{r_2} = \frac{R_1^{2}T_1^{4}}{R_2^{2}T_2^{4}}$
4. $= 4 \times \frac{1}{16}$
5. $\frac{450}{r_2} = \frac{1}{4}$
6. $r_2 = 1800\,\mathrm{watt}$

**Solved independently** (answer withheld)

1. For a black body, $P = \sigma A T^4 = \sigma (4\pi r^2) T^4$, so $P \propto r^2 T^4$.
2. $\frac{P'}{P} = \left(\frac{r'}{r}\right)^2 \left(\frac{T'}{T}\right)^4 = \left(\frac{1}{2}\right)^2 (2)^4$.
3. $\left(\frac{1}{2}\right)^2 (2)^4 = \frac{1}{4} \times 16 = 4$.
4. $P' = 4 \times 450\,\mathrm{W} = 1800\,\mathrm{W}$, which is option $4$.

**Subtopic:** Radiation Laws · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 10)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q035_4e203507_27102026.png?v=4e203507bd0a)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q035_f7a6be27_27102026.png?v=f7a6be2768f7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Stefan's law: radiated power goes as area times $T^4$, so halving the radius and doubling the temperature multiplies the power by 4
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  With the temperature carried as a square, the area's $\frac{1}{4}$ and the temperature's $4$ look as though they cancel, so the power is reported unchanged at $450\,\mathrm{W}$. Stefan's law carries the fourth power, so the factor is $\frac{1}{4}\times16=4$ and the power is $1800\,\mathrm{W}$.
- **Why:** This question requires how many times the radiated power changes, demonstrated by 'If the radius were halved and the temperature doubled', which leaves the printed radius of $12\,\mathrm{cm}$ unused.
- **Note:** Option 1, $225\,\mathrm{W}$, is the same wrong route with the temperature kept linear: $\frac{1}{4}\times2=\frac{1}{2}$.
<!--/ecat-->

## Q36

Physics · Laws of Motion

Two blocks $A$ and $B$ of masses $3m$ and $m$ respectively are connected by a massless and inextensible string. The whole system is suspended by a massless spring as shown in figure. The magnitudes of acceleration of $A$ and $B$ immediately after the string is cut, are respectively

![printed figure: Blocks A (3m) and B (m) joined by a string, hung from a ceiling by a spring](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q036_f587aa54_29102026.svg?v=f587aa548aa2)

*Blocks A (3m) and B (m) joined by a string, hung from a ceiling by a spring*

![drawn: Blocks A (3m) and B (m) joined by a string, hung from a ceiling by a spring](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q036_question_482ee863_27102026.svg?v=482ee8634dcb)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $g, \frac{g}{3}$
- **(2)** $\frac{g}{3}, g$
- (3) $g, g$
- (4) $\frac{g}{3}, \frac{g}{3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Free-body diagram of block 3m: spring force kx up, string tension T and weight 3mg down](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q036_sol_1_e9d064b3_27102026.svg?v=e9d064b30505)

*Free-body diagram of block 3m: spring force kx up, string tension T and weight 3mg down*

![drawn: Free-body diagram of block 3m: spring force kx up, string tension T and weight 3mg down](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q036_solution_1_3e350288_27102026.svg?v=3e3502887208)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Before the string is cut
2. $kx = T + 3mg$ ...(1)
3. $T = mg$ ...(2)

![printed figure: Free-body diagram of block m: tension T upward, weight mg downward](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q036_sol_2_d9568090_27102026.svg?v=d95680905cde)

*Free-body diagram of block m: tension T upward, weight mg downward*

![drawn: Free-body diagram of block m: tension T upward, weight mg downward](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q036_solution_2_a1adc73a_27102026.svg?v=a1adc73afa85)  
*drawn on the booklet's geometry, checked against its figure spec*

4. $\Rightarrow kx = 4mg$
5. After the string is cut, $T = 0$
6. $a = \frac{kx - 3mg}{3m}$

![printed figure: Free-body diagrams of blocks 3m and m just after the string is cut](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q036_sol_3_b2405b55_27102026.svg?v=b2405b556732)

*Free-body diagrams of blocks 3m and m just after the string is cut*

![drawn: Free-body diagrams of blocks 3m and m just after the string is cut](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q036_solution_3_2abfe316_27102026.svg?v=2abfe316c8bc)  
*drawn on the booklet's geometry, checked against its figure spec*

7. $a = \frac{4mg - 3mg}{3m}$
8. $a = \frac{g}{3}\uparrow$

**Solved independently** (answer withheld)

1. Before the cut, equilibrium of the whole system gives spring force $kx = (3m + m)g = 4mg$.
2. The spring cannot change its extension instantly, so just after the cut it still pulls $A$ up with $4mg$.
3. For $A$: $3m\,a_A = 4mg - 3mg = mg \Rightarrow a_A = \frac{g}{3}$.
4. For $B$: string tension becomes zero, so only gravity acts and $a_B = g$.
5. $\left(\frac{g}{3}, g\right)$ is option $2$.

**Subtopic:** Block and Spring Problem · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 10)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q036_70790dc4_27102026.png?v=70790dc45302)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q036_16cd753f_27102026.png?v=16cd753f3f31)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A spring cannot change its stretch in the instant a string is cut, so the block it holds is not in free fall while the block below is
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Once the string is cut both blocks look like free bodies with only weight on them, so both are given $g$ -- and for $B$, which is now hanging from nothing, $g$ is right. The spring is still stretched to the $4mg$ it carried a moment earlier, so $A$ has $(4mg-3mg)/3m=g/3$ upward, not $g$.
- **Why:** This question requires computing both accelerations, demonstrated by 'The magnitudes of acceleration of A and B immediately after the string is cut, are respectively' with each option printing a pair.
- **Note:** Option 1 is the correct pair of magnitudes attached to the wrong blocks. The figure is needed: nothing in the stem text says which block the spring holds and which hangs below.
<!--/ecat-->

## Q37

Physics · Wave Optics

Two Polaroids $P_1$ and $P_2$ are placed with their axis perpendicular to each other. Unpolarised light $I_0$ is incident on $P_1$. A third polaroid $P_3$ is kept in between $P_1$ and $P_2$ such that its axis makes an angle $45^\circ$ with that of $P_1$. The intensity of transmitted light through $P_2$ is

- (1) $\frac{I_0}{2}$
- (2) $\frac{I_0}{4}$
- **(3)** $\frac{I_0}{8}$
- (4) $\frac{I_0}{16}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Unpolarised light I0 through polaroids P1, P3, P2; P3 axis at 45° and P2 axis at 90° to P1 axis](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q037_sol_1_638dd625_27102026.svg?v=638dd6252d26)

*Unpolarised light I0 through polaroids P1, P3, P2; P3 axis at 45° and P2 axis at 90° to P1 axis*

![drawn: Unpolarised light I0 through polaroids P1, P3, P2; P3 axis at 45° and P2 axis at 90° to P1 axis](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q037_solution_1_6b8e7705_27102026.svg?v=6b8e7705f408)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $I_2 = \frac{I_0}{2}\cos^2 45^\circ$
2. $= \frac{I_0}{2} \times \frac{1}{2}$
3. $= \frac{I_0}{4}$
4. $I_3 = \frac{I_0}{4}\cos^2 45^\circ$
5. $I_3 = \frac{I_0}{8}$

**Solved independently** (answer withheld)

1. Unpolarised light through $P_1$: $I_1 = \frac{I_0}{2}$.
2. Through $P_3$ at $45^\circ$ to $P_1$ (Malus's law): $I_3 = I_1 \cos^2 45^\circ = \frac{I_0}{2} \times \frac{1}{2} = \frac{I_0}{4}$.
3. $P_2$ is perpendicular to $P_1$, so the angle between $P_3$ and $P_2$ is $90^\circ - 45^\circ = 45^\circ$.
4. Through $P_2$: $I_2 = I_3 \cos^2 45^\circ = \frac{I_0}{4} \times \frac{1}{2} = \frac{I_0}{8}$, which is option $3$.

**Subtopic:** Polaroids · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 10)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q037_0f42fe06_27102026.png?v=0f42fe06edaf)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q037_ab452d04_27102026.png?v=ab452d048a1c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Malus's law applied stage by stage, with unpolarised light halved at the first polaroid
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  $P_1$ halves the unpolarised light to $I_0/2$ and $P_3$ at $45^\circ$ halves it again to $I_0/4$, which is where a student who has used Malus's law once stops. $P_2$ is still $45^\circ$ away from $P_3$, so a third factor of $\cos^2 45^\circ$ applies and the transmitted intensity is $I_0/8$.
- **Why:** This question requires applying Malus's law through three stages to a number, demonstrated by 'The intensity of transmitted light through $P_2$' with the options printed as fractions of $I_0$.
<!--/ecat-->

## Q38

Physics · Electromagnetic Induction

A long solenoid of diameter $0.1\,\mathrm{m}$ has $2 \times 10^{4}$ turns per meter. At the centre of the solenoid, a coil of $100$ turns and radius $0.01\,\mathrm{m}$ is placed with its axis coinciding with the solenoid axis. The current in the solenoid reduces at a constant rate to $0\,\mathrm{A}$ from $4\,\mathrm{A}$ in $0.05\,\mathrm{s}$. If the resistance of the coil is $10\pi^{2}\,\Omega$, the total charge flowing through the coil during this time is

- (1) $32\pi\,\mu\mathrm{C}$
- (2) $16\,\mu\mathrm{C}$
- **(3)** $32\,\mu\mathrm{C}$
- (4) $16\pi\,\mu\mathrm{C}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\varepsilon = -N\frac{d\phi}{dt}$
2. $\left|\frac{\varepsilon}{R}\right| = \frac{N}{R}\frac{d\phi}{dt}$
3. $dq = \frac{N}{R}d\phi$
4. $\Delta Q = \frac{N(\Delta\phi)}{R}$
5. $\Delta Q = \frac{\Delta\phi_{\mathrm{total}}}{R}$
6. $= \frac{(NBA)}{R}$
7. $= \frac{\mu_0 n i \pi r^{2}}{R}$
8. Putting values
9. $= \frac{4\pi \times 10^{-7} \times 100 \times 4 \times \pi \times (0.01)^{2}}{10\pi^{2}}$
10. $\Delta Q = 32\,\mu\mathrm{C}$

**Solved independently** (answer withheld)

1. The field inside the solenoid is uniform: $B = \mu_0 n I$, and the coil (radius $0.01\,\mathrm{m}$) lies wholly inside it, so its flux area is $A = \pi r^2 = \pi \times 10^{-4}\,\mathrm{m^2}$.
2. Total flux change through the coil: $\Delta\Phi = N \mu_0 n \,\Delta I\, A$.
3. $\Delta\Phi = 100 \times 4\pi\times10^{-7} \times 2\times10^{4} \times 4 \times \pi\times10^{-4} = 32\pi^2\times10^{-5}\,\mathrm{Wb}$.
4. Charge is independent of time: $Q = \frac{\Delta\Phi}{R} = \frac{32\pi^2\times10^{-5}}{10\pi^2} = 3.2\times10^{-5}\,\mathrm{C}$.
5. $Q = 32\,\mu\mathrm{C}$, which is option $3$.

**Subtopic:** Faraday's Law of Electromagnetic Induction · **Difficulty:** hard (5 steps, 3 of 4 options live)

**Printed in the booklet** (page 11)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q038_d257d7ea_27102026.png?v=d257d7ea6a51)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q038_e6486cea_27102026.png?v=e6486cea8fdd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Charge through a coil is set by the total flux change and the resistance, $q=N\Delta\Phi/R$, whatever the time taken
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Two $\pi$'s enter the numerator, one from $\mu_0=4\pi\times10^{-7}$ and one from the coil's area $\pi r^2$, and the printed resistance $10\pi^2\,\Omega$ is there to remove both. Cancel only one of them and the answer reads $32\pi\,\mu\mathrm{C}$ instead of $32\,\mu\mathrm{C}$.
- **Why:** This question requires a number computed from the stem's data, demonstrated by 'the total charge flowing through the coil during this time' with four options in $\mu\mathrm{C}$.
- **Note:** The options are $32$ and $16$ each printed with and without $\pi$, so the whole decision rests on whether the $\pi^2$ cancels. The solenoid's diameter of $0.1\,\mathrm{m}$ is not needed: the coil of radius $0.01\,\mathrm{m}$ sits inside the uniform field.
<!--/ecat-->

## Q39

Physics · Rotational Motion

Two discs of same moment of inertia rotating about their regular axis passing through centre and perpendicular to the plane of disc with angular velocities $\omega_1$ and $\omega_2$. They are brought into contact face to face coinciding the axis of rotation. The expression for loss of energy during this process is

- (1) $\frac{1}{2}I(\omega_1+\omega_2)^2$
- **(2)** $\frac{1}{4}I(\omega_1-\omega_2)^2$
- (3) $I(\omega_1-\omega_2)^2$
- (4) $\frac{I}{8}(\omega_1-\omega_2)^2$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\Delta KE = \frac{1}{2}\frac{I_1 I_2}{I_1 + I_2}(\omega_1 - \omega_2)^2$
2. $= \frac{1}{2}\frac{I^2}{(2I)}(\omega_1 - \omega_2)^2$
3. $= \frac{1}{4}I(\omega_1 - \omega_2)^2$

**Solved independently** (answer withheld)

1. No external torque acts, so angular momentum is conserved: $I\omega_1 + I\omega_2 = 2I\omega$.
2. $\omega = \frac{\omega_1+\omega_2}{2}$.
3. Initial kinetic energy: $K_i = \frac{1}{2}I\omega_1^2 + \frac{1}{2}I\omega_2^2$.
4. Final kinetic energy: $K_f = \frac{1}{2}(2I)\omega^2 = \frac{1}{4}I(\omega_1+\omega_2)^2$.
5. $\Delta K = K_i - K_f = \frac{1}{4}I\left[2\omega_1^2 + 2\omega_2^2 - (\omega_1+\omega_2)^2\right]$.
6. $\Delta K = \frac{1}{4}I(\omega_1-\omega_2)^2$, which is option $2$.

**Subtopic:** Conservation of Angular Momentum · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 11)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q039_3b019b07_27102026.png?v=3b019b072a5a)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q039_688d99fd_27102026.png?v=688d99fdd182)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Two rotating bodies brought into contact keep their total angular momentum, and the energy lost depends on the relative angular velocity
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Each disc's angular velocity shifts by $\frac{\omega_1-\omega_2}{2}$ in reaching the common value, and feeding that into $\frac{1}{2}I\omega^2$ for one disc gives $\frac{I}{8}(\omega_1-\omega_2)^2$. The dissipation belongs to the pair, $\frac{I_1I_2}{2(I_1+I_2)}(\omega_1-\omega_2)^2$, which with $I_1=I_2=I$ is $\frac{1}{4}I(\omega_1-\omega_2)^2$.
- **Why:** This question requires deriving the energy loss from angular-momentum conservation, demonstrated by 'The expression for loss of energy during this process is' with four symbolic options in $I$, $\omega_1$ and $\omega_2$.
- **Note:** Three options carry the correct $(\omega_1-\omega_2)^2$ structure and differ only in the prefactor $\frac{1}{4}$, $1$ or $\frac{1}{8}$, so the whole decision sits on that factor. Option 1 is the only one built on the sum, and $\frac{1}{2}I(\omega_1+\omega_2)^2$ is not the final kinetic energy either, which is $\frac{I}{4}(\omega_1+\omega_2)^2$.
<!--/ecat-->

## Q40

Physics · Kinematics

Preeti reached the metro station and found that the escalator was not working. She walked up the stationary escalator in time $t_1$. On other days, if she remains stationary on the moving escalator, then the escalator takes her up in time $t_2$. The time taken by her to walk up on the moving escalator will be

- (1) $\frac{t_1 + t_2}{2}$
- (2) $\frac{t_1 t_2}{t_2 - t_1}$
- **(3)** $\frac{t_1 t_2}{t_2 + t_1}$
- (4) $t_1 - t_2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Velocity of girl w.r.t. elevator $= \frac{d}{t_1} = v_{ge}$
2. Velocity of elevator w.r.t. ground $v_{eG} = \frac{d}{t_2}$ then
3. velocity of girl w.r.t. ground
4. $\vec{v}_{gG} = \vec{v}_{ge} + \vec{v}_{eG}$
5. i.e, $v_{gG} = v_{ge} + v_{eG}$
6. $\frac{d}{t} = \frac{d}{t_1} + \frac{d}{t_2}$
7. $\frac{1}{t} = \frac{1}{t_1} + \frac{1}{t_2}$
8. $t = \frac{t_1 t_2}{(t_1 + t_2)}$

**Solved independently** (answer withheld)

1. Let the escalator length be $L$; her walking speed is $v_1 = \frac{L}{t_1}$ and the escalator speed is $v_2 = \frac{L}{t_2}$.
2. Walking on the moving escalator, the speeds add: $v = v_1 + v_2 = \frac{L}{t_1} + \frac{L}{t_2}$.
3. $t = \frac{L}{v} = \frac{1}{\frac{1}{t_1} + \frac{1}{t_2}} = \frac{t_1 t_2}{t_1 + t_2}$, which is option $3$.

**Subtopic:** Relative Motion in 1D · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 11)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q040_440bd16e_27102026.png?v=440bd16e4ae6)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q040_5a96ee3d_27102026.png?v=5a96ee3d5be0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Walking and the escalator add their speeds, so the reciprocals of the two times add
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Her walking and the escalator's lift clearly combine, and the two numbers in hand are times, so the two times get averaged to $\frac{t_1+t_2}{2}$. Speeds are the quantity that adds over the same staircase, so $\frac{1}{t}=\frac{1}{t_1}+\frac{1}{t_2}$ and $t=\frac{t_1t_2}{t_1+t_2}$, which is shorter than either $t_1$ or $t_2$.
- **Also:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $\frac{t_1t_2}{t_2-t_1}$ is the published result for the other version of this problem, walking up while the escalator runs down, where the two speeds subtract. Here both carry her the same way, so the speeds add and the minus sign becomes a plus.
- **Why:** This question requires deriving the combined time from the two single-agent times, demonstrated by 'The time taken by her to walk up on the moving escalator will be' with four symbolic options in $t_1$ and $t_2$.
<!--/ecat-->

## Q41

Physics · Rotational Motion

A rope is wound around a hollow cylinder of mass $3\,\mathrm{kg}$ and radius $40\,\mathrm{cm}$. What is the angular acceleration of the cylinder if the rope is pulled with a force of $30\,\mathrm{N}$?

- (1) $25\,\mathrm{m/s^2}$
- (2) $0.25\,\mathrm{rad/s^2}$
- **(3)** $25\,\mathrm{rad/s^2}$
- (4) $5\,\mathrm{m/s^2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Rope wound on a hollow cylinder of radius 40 cm pulled down with F = 30 N](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q041_sol_1_16b1e27a_27102026.svg?v=16b1e27a59ca)

*Rope wound on a hollow cylinder of radius 40 cm pulled down with F = 30 N*

![drawn: Rope wound on a hollow cylinder of radius 40 cm pulled down with F = 30 N](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q041_solution_1_82295983_27102026.svg?v=822959831d21)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\tau = I\alpha$
2. $F \times R = MR^{2}\alpha$
3. $30 \times 0.4 = 3 \times (0.4)^{2}\,\alpha$
4. $12 = 3 \times 0.16\,\alpha$
5. $400 = 16\,\alpha$
6. $\alpha = 25\,\mathrm{rad/s^{2}}$

**Solved independently** (answer withheld)

1. For a hollow cylinder about its axis, $I = MR^2 = 3 \times (0.4)^2 = 0.48\,\mathrm{kg\,m^2}$.
2. Torque from the rope: $\tau = FR = 30 \times 0.4 = 12\,\mathrm{N\,m}$.
3. $\alpha = \frac{\tau}{I} = \frac{12}{0.48} = 25\,\mathrm{rad/s^2}$, which is option $3$.

**Subtopic:** Problems on Torque of a Force About the Axis of Rotation · **Difficulty:** medium (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 11)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q041_295c164f_27102026.png?v=295c164f985e)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q041_8c184ac6_27102026.png?v=8c184ac6a2bf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Angular acceleration from torque: $\alpha=FR/I$, with $I=mR^2$ for a hollow cylinder
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The radius is printed as $40\,\mathrm{cm}$, and left in centimetres $\alpha=FR/mR^2=F/mR=30/(3\times40)=0.25$, which is printed with the right unit. In metres $R=0.4$ and $\alpha=30/(3\times0.4)=25\,\mathrm{rad/s^2}$.
- **Why:** This question requires a number computed from the stem's data, demonstrated by 'What is the angular acceleration of the cylinder if the rope is pulled with a force of $30\,\mathrm{N}$?' with four numerical options.
- **Note:** Two options carry $\mathrm{m/s^2}$, which is not a unit of angular acceleration at all, and one of them prints the correct magnitude $25$.
<!--/ecat-->

## Q42

Physics · Ray Optics

A beam of light from a source $L$ is incident normally on a plane mirror fixed at a certain distance $x$ from the source. The beam is reflected back as a spot on a scale placed just above the source $L$. When the mirror is rotated through a small angle $\theta$, the spot of the light is found to move through a distance $y$ on the scale. The angle $\theta$ is given by

- **(1)** $\frac{y}{2x}$
- (2) $\frac{y}{x}$
- (3) $\frac{x}{2y}$
- (4) $\frac{x}{y}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. When mirror is rotated by $\theta$ angle reflected ray will be rotated by $2\theta$.

![printed figure: Incident and reflected rays at angle 2θ from the mirror, spot displacement y at distance x](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q042_sol_1_d358c1c3_29102026.svg?v=d358c1c3ac26)

*Incident and reflected rays at angle 2θ from the mirror, spot displacement y at distance x*

![drawn: Incident and reflected rays at angle 2θ from the mirror, spot displacement y at distance x](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q042_solution_1_67801778_27102026.svg?v=67801778ca69)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $\frac{y}{x} = 2\theta$
3. $\theta = \frac{y}{2x}$

**Solved independently** (answer withheld)

1. Rotating a plane mirror through $\theta$ with the incident ray fixed rotates the reflected ray through $2\theta$.
2. The spot on the scale at distance $x$ moves by $y = x\tan 2\theta$.
3. For small $\theta$, $\tan 2\theta \approx 2\theta$, so $y \approx 2x\theta$.
4. $\theta = \frac{y}{2x}$, which is option $1$.

**Subtopic:** Reflection at a Smooth Surface · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 12)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q042_3a562529_27102026.png?v=3a5625296a22)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q042_2eabfd70_27102026.png?v=2eabfd709611)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Rotating a mirror by $\theta$ turns the reflected ray by $2\theta$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Taking the spot to sweep through the same angle the mirror turned gives $\theta=y/x$ in one line from arc over radius. The reflected ray turns through twice the mirror's rotation, so it is $2\theta=y/x$ and $\theta=y/2x$.
- **Why:** This question requires deriving the small angle from the spot's displacement, demonstrated by 'the spot of the light is found to move through a distance $y$ on the scale. The angle $\theta$ is given by' with four options in $x$ and $y$.
- **Note:** Options 3 and 4 are the reciprocals of options 1 and 2, so a student who sets up arc over radius upside down still finds a printed option.
<!--/ecat-->

## Q43

Physics · Waves

The two nearest harmonics of a tube closed at one end and open at other end are $220\,\mathrm{Hz}$ and $260\,\mathrm{Hz}$. What is the fundamental frequency of the system?

- (1) $10\,\mathrm{Hz}$
- **(2)** $20\,\mathrm{Hz}$
- (3) $30\,\mathrm{Hz}$
- (4) $40\,\mathrm{Hz}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Two successive frequencies of closed pipe
2. $\frac{nv}{4l} = 220 \quad \ldots(\mathrm{i})$
3. $\frac{(n+2)v}{4l} = 260 \quad \ldots(\mathrm{ii})$
4. Dividing (ii) by (i), we get
5. $\frac{n+2}{n} = \frac{260}{220} = \frac{13}{11}$
6. $11n + 22 = 13n$
7. $n = 11$
8. So, $11\frac{v}{4l} = 220$
9. $\frac{v}{4l} = 20$
10. So fundamental frequency is $20\,\mathrm{Hz}$.

**Solved independently** (answer withheld)

1. A tube closed at one end supports only odd harmonics: $f_n = (2n-1)f_0$.
2. Two nearest harmonics differ by $2f_0$: $2f_0 = 260\,\mathrm{Hz} - 220\,\mathrm{Hz} = 40\,\mathrm{Hz}$.
3. $f_0 = \frac{40}{2} = 20\,\mathrm{Hz}$.
4. Check: $\frac{220}{20} = 11$ and $\frac{260}{20} = 13$, both odd, consistent; this is option $2$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 12)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q043_c95ffbf1_27102026.png?v=c95ffbf1f0a0)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q043_354aa817_27102026.png?v=354aa817ba14)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A tube closed at one end sounds only the odd harmonics, so neighbouring harmonics are $2f_0$ apart
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  In a string or a pipe open at both ends consecutive harmonics differ by the fundamental, so the gap $260-220=40\,\mathrm{Hz}$ is read straight off as the answer. The stem's tube is 'closed at one end', which leaves only odd harmonics, so neighbours sit $2f_0$ apart and $f_0=20\,\mathrm{Hz}$.
- **Why:** This question requires a number computed from the two given frequencies, demonstrated by 'The two nearest harmonics of a tube closed at one end and open at other end are $220\,\mathrm{Hz}$ and $260\,\mathrm{Hz}$'.
- **Note:** Checks out as printed: $220$ and $260\,\mathrm{Hz}$ are the 11th and 13th harmonics of $20\,\mathrm{Hz}$, both odd, so the pair is consistent with a closed tube.
<!--/ecat-->

## Q44

Physics · Ray Optics

A thin prism having refracting angle $10^\circ$ is made of glass of refractive index $1.42$. This prism is combined with another thin prism of glass of refractive index $1.7$. This combination produces dispersion without deviation. The refracting angle of second prism should be

- (1) $4^\circ$
- **(2)** $6^\circ$
- (3) $8^\circ$
- (4) $10^\circ$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $(\mu - 1)A + (\mu' - 1)A' = 0$
2. $|(\mu - 1)A| = |(\mu' - 1)A'|$
3. $(1.42 - 1) \times 10^\circ = (1.7 - 1)A'$
4. $4.2 = 0.7A'$
5. $A' = 6^\circ$

**Solved independently** (answer withheld)

1. For a thin prism the deviation is $\delta = (\mu - 1)A$.
2. Deviation by the first prism: $\delta_1 = (1.42 - 1)\times 10^\circ = 4.2^\circ$.
3. Deviation by the second prism: $\delta_2 = (1.7 - 1)A_2 = 0.7A_2$.
4. No net deviation requires $\delta_1 = \delta_2$, so $0.7A_2 = 4.2^\circ$.
5. $A_2 = \frac{4.2^\circ}{0.7} = 6^\circ$, which is option $2$.

**Subtopic:** Dispersion · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 12)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q044_808e478d_27102026.png?v=808e478d65cc)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q044_490be542_27102026.png?v=490be542d251)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A thin prism deviates light by $(\mu-1)A$, so dispersion without deviation needs $(\mu_1-1)A_1=(\mu_2-1)A_2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Balancing the two prisms on their refractive indices alone gives $A_2=(\mu_1/\mu_2)A_1=(1.42/1.7)\times10=8.35^\circ$, which lands on the printed $8^\circ$. Deviation goes as $\mu-1$, not $\mu$, so the balance is $0.42\times10=0.7\times A_2$ and $A_2=6^\circ$.
- **Why:** This question requires a number computed from the two refractive indices and the first angle, demonstrated by 'This combination produces dispersion without deviation. The refracting angle of second prism should be'.
- **Note:** Option 4 is the stem's own $10^\circ$ repeated; equal angles would cancel the deviation only if the two glasses had equal refractive indices, and the stem gives $1.42$ and $1.7$.
<!--/ecat-->

## Q45

Physics · Current Electricity

The resistance of a wire is '$R$' ohm. If it is melted and stretched to '$n$' times its original length, its new resistance will be

- (1) $nR$
- (2) $\dfrac{R}{n}$
- **(3)** $n^{2}R$
- (4) $\dfrac{R}{n^{2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\frac{R_2}{R_1} = \frac{l_2^{2}}{l_1^{2}}$
2. $= \frac{n^{2}l_1^{2}}{l_1^{2}}$
3. $\frac{R_2}{R_1} = n^{2}$
4. $R_2 = n^{2}R_1$

**Solved independently** (answer withheld)

1. Melting and stretching keeps the volume constant: $lA = l'A'$.
2. With $l' = nl$, the new area is $A' = \frac{A}{n}$.
3. $R' = \frac{\rho l'}{A'} = \frac{\rho (nl)}{A/n}$.
4. $R' = n^{2}\frac{\rho l}{A} = n^{2}R$, which is option $3$.

**Subtopic:** Resistance · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 12)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q045_07086c44_27102026.png?v=07086c444469)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q045_132b0326_27102026.png?v=132b03260669)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Resistance of a stretched wire: melting and redrawing keeps the volume fixed, so the area falls as the length rises and $R \propto L^{2}$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student who substitutes into $R = \rho L / A$ and changes only the length gets $nR$, treating the wire as if it were merely longer. Melting and stretching keeps the volume, so the area also drops to $A/n$ and the two factors multiply: $R' = \rho (nL)/(A/n) = n^{2}R$.
- **Why:** This question requires the power of $n$ in $R \propto L^{2}$ at fixed volume rather than any number, demonstrated by the stem giving the resistance only as "'$R$' ohm" and the four options being $nR$, $R/n$, $n^{2}R$ and $R/n^{2}$.
<!--/ecat-->

## Q46

Chemistry · organic · Hydrocarbons

With respect to the conformers of ethane, which of the following statements is true?

- (1) Bond angle remains same but bond length changes
- (2) Bond angle changes but bond length remains same
- (3) Both bond angle and bond length change
- **(4)** Both bond angles and bond length remains same

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. There is no change in bond angles and bond lengths in the conformations of ethane.
2. There is only change in dihedral angle.

**Solved independently** (answer withheld)

1. Conformers of ethane (e.g. staggered and eclipsed) interconvert by free rotation about the $\mathrm{C{-}C}$ $\sigma$ bond.
2. This rotation changes only the dihedral angle between $\mathrm{C{-}H}$ bonds on adjacent carbons, so both bond angles and bond lengths stay the same, which is option $4$.

**Subtopic:** Isomerism · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q046_bf3ace46_27102026.png?v=bf3ace467e99)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q046_f2a620f1_27102026.png?v=f2a620f157f7)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Conformers of ethane are one molecule at different twists about the C–C bond, so every bond length and every bond angle is untouched
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student who remembers that the eclipsed form is strained decides the strain has to go somewhere and lets the H–C–H angles splay, while correctly keeping the bond lengths fixed. Rotation about a sigma bond breaks nothing, so the torsional strain shows up as an energy difference, not as a change in angle.
- **Why:** This question requires the stated fact that nothing but rotation about the C–C single bond separates ethane's conformers, demonstrated by the stem "With respect to the conformers of ethane, which of the following statements is true?" and four options that only cross bond angle against bond length.
<!--/ecat-->

## Q47

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following pairs of compounds is isoelectronic and isostructural?

- (1) $\mathrm{BeCl_2}$, $\mathrm{XeF_2}$
- (2) $\mathrm{TeI_2}$, $\mathrm{XeF_2}$
- **(3)** $\mathrm{IBr_2^-}$, $\mathrm{XeF_2}$
- (4) $\mathrm{IF_3}$, $\mathrm{XeF_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{IBr_2^-}$, $\mathrm{XeF_2}$
2. Total number of valence electrons are equal in both the species and both the species are linear also.

**Solved independently** (answer withheld)

1. $\mathrm{XeF_2}$: valence electrons $= 8 + 2(7) = 22$; Xe has 2 bond pairs and 3 lone pairs, $sp^3d$, so the shape is linear.
2. $\mathrm{BeCl_2}$: $2 + 2(7) = 16$ valence electrons, so it is not isoelectronic with $\mathrm{XeF_2}$.
3. $\mathrm{TeI_2}$: $6 + 2(7) = 20$ valence electrons, 2 lone pairs on Te, bent shape, so neither isoelectronic nor isostructural.
4. $\mathrm{IF_3}$: $7 + 3(7) = 28$ valence electrons, 3 bond pairs and 2 lone pairs, T-shaped, so it does not match.
5. $\mathrm{IBr_2^-}$: $7 + 2(7) + 1 = 22$ valence electrons; I has 2 bond pairs and 3 lone pairs, $sp^3d$, linear.
6. $\mathrm{IBr_2^-}$ and $\mathrm{XeF_2}$ are both isoelectronic (22 valence electrons) and isostructural (linear), which is option $3$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** hard (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q047_f741c010_27102026.png?v=f741c0101d4e)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q047_627dd115_27102026.png?v=627dd115befa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Isoelectronic and isostructural together demand the same valence-electron count and the same VSEPR shape, lone pairs counted
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  $\mathrm{BeCl_2}$ and $\mathrm{XeF_2}$ are both linear, so a student who tests only the shape sees the pair match and stops. The electron count fails: $\mathrm{BeCl_2}$ carries 16 valence electrons against 22 in $\mathrm{XeF_2}$, which is why $\mathrm{IBr_2^-}$ is the pair that passes both tests.
- **Why:** This question requires the valence-electron count and the VSEPR shape worked out for each printed pair, demonstrated by the stem asking for the pair that is "isoelectronic and isostructural" — two separate tests every option must pass.
<!--/ecat-->

## Q48

Chemistry · inorganic · The p–Block Elements

$\mathrm{HgCl_2}$ and $\mathrm{I_2}$ both when dissolved in water containing $\mathrm{I^-}$ ions the pair of species formed is

- (1) $\mathrm{HgI_2}$, $\mathrm{I_3^-}$
- (2) $\mathrm{HgI_2}$, $\mathrm{I^-}$
- **(3)** $\mathrm{HgI_4^{2-}}$, $\mathrm{I_3^-}$
- (4) $\mathrm{Hg_2I_2}$, $\mathrm{I^-}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In a solution containing $\mathrm{HgCl_2}$, $\mathrm{I_2}$ and $\mathrm{I^-}$, both $\mathrm{HgCl_2}$ and $\mathrm{I_2}$ compete for $\mathrm{I^-}$.
2. Since formation constant of $[\mathrm{HgI_4}]^{2-}$ is $1.9 \times 10^{30}$ which is very large as compared with $\mathrm{I_3^-}$ $(K_f = 700)$
3. $\therefore$ $\mathrm{I^-}$ will preferentially combine with $\mathrm{HgCl_2}$.
4. $\mathrm{HgCl_2} + 2\mathrm{I^-} \rightarrow \mathrm{HgI_2}\downarrow + 2\mathrm{Cl^-}$ (Red ppt)
5. $\mathrm{HgI_2} + 2\mathrm{I^-} \rightarrow [\mathrm{HgI_4}]^{2-}$ (soluble)

**Solved independently** (answer withheld)

1. $\mathrm{HgCl_2 + 2I^- \rightarrow HgI_2\downarrow + 2Cl^-}$; in excess $\mathrm{I^-}$ the precipitate dissolves: $\mathrm{HgI_2 + 2I^- \rightarrow [HgI_4]^{2-}}$.
2. $\mathrm{I_2 + I^- \rightarrow I_3^-}$ (triiodide formation makes iodine soluble in water).
3. The pair formed is $\mathrm{HgI_4^{2-}}$ and $\mathrm{I_3^-}$, which is option $3$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** hard (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q048_7b075b78_27102026.png?v=7b075b78f742)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q048_1263d716_27102026.png?v=1263d71609c2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Iodide added past the first equivalent dissolves $\mathrm{HgI_2}$ to the tetraiodomercurate(II) ion, and takes $\mathrm{I_2}$ to triiodide
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student swaps chloride for iodide one for one, gets $\mathrm{HgI_2}$, and pairs it with the $\mathrm{I_3^-}$ that $\mathrm{I_2} + \mathrm{I^-}$ plainly gives. $\mathrm{HgI_2}$ is only the first stop — the same iodide that made it goes on to dissolve it as $\mathrm{HgI_4^{2-}}$, so one half of this pair is right and one half is one step short.
- **Why:** This question requires what iodide does to each of the two solutes, demonstrated by the stem "$\mathrm{HgCl_2}$ and $\mathrm{I_2}$ both when dissolved in water containing $\mathrm{I^-}$ ions the pair of species formed is".
- **Note:** The stem does not print the word "excess"; the keyed answer $\mathrm{HgI_4^{2-}}$ requires iodide beyond the first two equivalents.
<!--/ecat-->

## Q49

Chemistry · organic · Chemistry in Everyday Life

Mixture of chloroxylenol and terpineol acts as

- (1) Analgesic
- **(2)** Antiseptic
- (3) Antipyretic
- (4) Antibiotic

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Mixture of chloroxylenol and terpineol acts as antiseptic.

**Solved independently** (answer withheld)

1. A mixture of chloroxylenol and terpineol is the commercial antiseptic Dettol, so it acts as an antiseptic, which is option $2$.

**Subtopic:** Antiseptics and Disinfectants · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q049_e1f3927b_27102026.png?v=e1f3927b4f94)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q049_5bcb38e6_27102026.png?v=5bcb38e67292)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Antiseptics are applied to living tissue; Dettol is chloroxylenol dissolved in terpineol
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Analgesic, antipyretic and antibiotic are coordinate drug classes from the same NCERT section, and the stem prints nothing — no symptom, no site of use, no structure — that points at any of them. The item turns entirely on recalling what the named pair of chemicals is sold as, so no option is reached by a wrong route rather than by not knowing.
- **Why:** This question requires the stored fact that chloroxylenol with terpineol is the antiseptic Dettol, demonstrated by four options that are bare class names — "Analgesic", "Antiseptic", "Antipyretic", "Antibiotic" — with no criterion in the stem to apply to them.
<!--/ecat-->

## Q50

Chemistry · physical · The Solid State

Which is the incorrect statement?

- **(1)** $\mathrm{FeO_{0.98}}$ has non stoichiometric metal deficiency defect
- (2) Density decreases in case of crystals with Schottky's defect
- (3) $\mathrm{NaCl(s)}$ is insulator, silicon is semiconductor, silver is conductor, quartz is piezo electric crystal
- **(4)** Frenkel defect is favoured in those ionic compounds in which sizes of cation and anions are almost equal

**Answer** — booklet: (1, 4) · independent solve: (4) · agree

**Publisher's solution**

1. Frenkel defect occurs in those ionic compounds in which size of cation and anion is largely different.
2. Non-stoichiometric ferrous oxide is $\mathrm{Fe_{0.93-0.96}O_{1.00}}$ and it is due to metal deficiency defect.

**Solved independently** (answer withheld)

1. $\mathrm{FeO_{0.98}}$ has fewer $\mathrm{Fe}$ than $\mathrm{O}$ ions, a non-stoichiometric metal deficiency defect, so option $1$ is correct.
2. Schottky defect removes cation-anion pairs from the lattice, so mass per unit volume falls and density decreases; option $2$ is correct.
3. $\mathrm{NaCl(s)}$ is an insulator, $\mathrm{Si}$ a semiconductor, $\mathrm{Ag}$ a conductor and quartz piezoelectric; option $3$ is correct.
4. Frenkel defect needs a small cation that fits interstitial sites, i.e. a large difference in ion sizes; nearly equal sizes favour Schottky defect, so option $4$ is the incorrect statement.

**Subtopic:** Imperfections in Solids · **Difficulty:** medium (4 steps, 2 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q050_c31ce5e4_27102026.png?v=c31ce5e4ecc9)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q050_b565ae82_27102026.png?v=b565ae82cd08)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Point defects in ionic solids: a Schottky defect takes a cation and an anion out of the crystal and lowers the density, a Frenkel defect only moves a cation into an interstitial site, and the cation–anion size difference decides which defect a compound shows
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Schottky and Frenkel are learnt as a pair with one density result each, and a student carrying Frenkel's 'density unchanged' on Schottky reads option 2 as the planted error. In a Schottky defect the two ions leave the crystal altogether, so mass is lost while the volume stays the same and the density does fall.
- **Also:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Silicon's conductivity is taught through doping, so a student holding 'silicon conducts only once it is doped' takes 'silicon is semiconductor' for the loose clause in a four-part option and rejects the whole of option 3. Pure silicon is an intrinsic semiconductor on its own; doping raises its conductivity but is not what makes it one.
- **Why:** This question requires filing each named solid and defect under the category or the consequence that defines it, demonstrated by option 2 'Density decreases in case of crystals with Schottky's defect' and option 4 'Frenkel defect is favoured in those ionic compounds in which sizes of cation and anions are almost equal', which are graded against the defect criteria with nothing to compute and no new case to work out.
<!--/ecat-->

## Q51

Chemistry · physical · Ionic Equilibrium

Concentration of the $\mathrm{Ag^{+}}$ ions in a saturated solution of $\mathrm{Ag_2C_2O_4}$ is $2.2 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$. Solubility product of $\mathrm{Ag_2C_2O_4}$ is

- (1) $2.42 \times 10^{-8}$
- (2) $2.66 \times 10^{-12}$
- (3) $4.5 \times 10^{-11}$
- **(4)** $5.3 \times 10^{-12}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{Ag_2C_2O_4(s)} \rightleftharpoons \underset{2s}{2\,\mathrm{Ag^{+}(aq)}} + \underset{s}{\mathrm{C_2O_4^{2-}(aq)}}$
2. $K_{SP} = [\mathrm{Ag^{+}}]^{2}\,[\mathrm{C_2O_4^{2-}}]$
3. $[\mathrm{Ag^{+}}] = 2.2 \times 10^{-4}\,\mathrm{M}$
4. $\therefore\ [\mathrm{C_2O_4^{2-}}] = \frac{2.2\times10^{-4}}{2}\,\mathrm{M} = 1.1\times10^{-4}\,\mathrm{M}$
5. $\therefore\ K_{SP} = (2.2 \times 10^{-4})^{2}\,(1.1 \times 10^{-4})$
6. $= 5.324 \times 10^{-12}$

**Solved independently** (answer withheld)

1. $\mathrm{Ag_2C_2O_4 \rightleftharpoons 2Ag^{+} + C_2O_4^{2-}}$, so $[\mathrm{C_2O_4^{2-}}] = \frac{1}{2}[\mathrm{Ag^{+}}]$.
2. $[\mathrm{C_2O_4^{2-}}] = \frac{2.2 \times 10^{-4}}{2} = 1.1 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$.
3. $K_{sp} = [\mathrm{Ag^{+}}]^2[\mathrm{C_2O_4^{2-}}]$.
4. $[\mathrm{Ag^{+}}]^2 = (2.2 \times 10^{-4})^2 = 4.84 \times 10^{-8}$.
5. $K_{sp} = 4.84 \times 10^{-8} \times 1.1 \times 10^{-4} = 5.324 \times 10^{-12} \approx 5.3 \times 10^{-12}$, which is option $4$.

**Subtopic:** Solubility Product Constant · **Difficulty:** hard (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q051_a6b7f2c2_27102026.png?v=a6b7f2c2128a)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q051_56d2a2d1_27102026.png?v=56d2a2d1bb51)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Solubility product of a 2:1 salt: for $\mathrm{Ag_2C_2O_4}$, $K_{sp}=[\mathrm{Ag^+}]^2[\mathrm{C_2O_4^{2-}}]$ with $[\mathrm{Ag^+}]=2s$ and $[\mathrm{C_2O_4^{2-}}]=s$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  A student who writes the solubility product the way it is written for AgCl, one ion each, multiplies the given $2.2\times10^{-4}$ by the oxalate's $1.1\times10^{-4}$ and gets $2.42\times10^{-8}$. $\mathrm{Ag_2C_2O_4}$ releases two silver ions per formula unit, so the silver term is squared and the answer drops four orders to $5.3\times10^{-12}$.
- **Also:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Solubility product written as $2s^3$ instead of $4s^3$ -- the stoichiometric 2 carried in as a multiplier rather than squared. That gives exactly the $2.66\times10^{-12}$ printed as option 2.
- **Why:** This question requires computing $K_{sp}$ from one ion's concentration through the salt's stoichiometry, demonstrated by the stem supplying only 'Concentration of the $\mathrm{Ag^{+}}$ ions in a saturated solution of $\mathrm{Ag_2C_2O_4}$ is $2.2 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$' and asking for the solubility product.
- **Note:** Two exact wrong-route options sit on this question; the second is recorded above rather than left in this note.
<!--/ecat-->

## Q52

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Of the following, which is the product formed when cyclohexanone undergoes aldol condensation followed by heating?

- (1) 2-(2-hydroxycyclohexyl)cyclohexan-1-one `O=C1CCCCC1C1CCCCC1O` ![2-(2-hydroxycyclohexyl)cyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q052_question_s1_8f5ba25f_27102026.svg?v=8f5ba25fcac8)
- **(2)** 2-cyclohexylidenecyclohexan-1-one `O=C1CCCCC1=C1CCCCC1` ![2-cyclohexylidenecyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q052_question_s2_b6972e82_27102026.svg?v=b6972e820137)
- (3) 2-cyclohexylcyclohexan-1-ol `OC1CCCCC1C1CCCCC1` ![2-cyclohexylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q052_question_s3_455a22ae_27102026.svg?v=455a22ae263a)
- (4) 2-(2-oxocyclohexylidene)cyclohexan-1-one `O=C1CCCCC1=C1CCCCC1=O` ![2-(2-oxocyclohexylidene)cyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q052_question_s4_21cb351a_27102026.svg?v=21cb351a392b)

Options as printed:

![printed figure: (1) 2-(2-hydroxycyclohexyl)cyclohexan-1-one; (2) 2-cyclohexylidenecyclohexan-1-one; (3) 2-cyclohexylcyclohexan-1-ol; (4) 2-(2-oxocyclohexylidene)cyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q052_a88b32d3_27102026.svg?v=a88b32d3d390)

*(1) 2-(2-hydroxycyclohexyl)cyclohexan-1-one; (2) 2-cyclohexylidenecyclohexan-1-one; (3) 2-cyclohexylcyclohexan-1-ol; (4) 2-(2-oxocyclohexylidene)cyclohexan-1-one*

![drawn: (1) 2-(2-hydroxycyclohexyl)cyclohexan-1-one; (2) 2-cyclohexylidenecyclohexan-1-one; (3) 2-cyclohexylcyclohexan-1-ol; (4) 2-(2-oxocyclohexylidene)cyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q052_question_c0f81c4e_27102026.svg?v=c0f81c4ee4fd)  
*drawn on the booklet's geometry, checked against its SMILES*

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: I. cyclohexanone + cyclohexanone →((i) $\ce{OH-}$, (ii) Δ) 2-cyclohexylidenecyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q052_sol_1_e5a78c70_29102026.svg?v=e5a78c70a5d1)

*I. cyclohexanone + cyclohexanone →[(i) $\ce{OH-}$, (ii) Δ] 2-cyclohexylidenecyclohexan-1-one*

![drawn: I. cyclohexanone + cyclohexanone →((i) $\ce{OH-}$, (ii) Δ) 2-cyclohexylidenecyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q052_solution_1_3b14086b_27102026.svg?v=3b14086b4aa2)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. The enolate of one cyclohexanone (formed at the $\alpha$-carbon) attacks the $C=O$ carbon of a second cyclohexanone, giving the aldol: 2-(1-hydroxycyclohexyl)cyclohexan-1-one.
2. On heating, this $\beta$-hydroxy ketone dehydrates ($-H_2O$) to form a $C=C$ conjugated with the remaining $C=O$.
3. The product is 2-cyclohexylidenecyclohexan-1-one: one ring carries the $C=O$, the exocyclic double bond joins the two rings, and the other ring has no oxygen, which is option $2$.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 13)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q052_b4fd4a5b_27102026.png?v=b4fd4a5bd35f)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q052_d44fa49b_27102026.png?v=d44fa49ba24d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Aldol condensation: a ketone adds to itself at the alpha carbon, then loses water on heating to leave the alpha,beta-unsaturated ketone
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  A student who stops at the aldol step, where the alpha carbon of one cyclohexanone adds to the carbonyl of the other, writes down the beta-hydroxy ketone and is finished. The stem's 'followed by heating' is what drives off that water to make the C=C of option (2), so option (1) is exactly the right answer to the question with that phrase deleted.
- **Why:** This question requires the product of a ketone's self-aldol plus loss of water, demonstrated by the stem's 'aldol condensation followed by heating' and by option (1) printing the un-dehydrated beta-hydroxy ketone.
- **Note:** The four options are printed as drawn structures: (1) 2-(2-hydroxycyclohexyl)cyclohexan-1-one, (2) 2-cyclohexylidenecyclohexan-1-one, (3) 2-cyclohexylcyclohexan-1-ol, (4) 2-(2-oxocyclohexylidene)cyclohexan-1-one.
<!--/ecat-->

## Q53

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The species, having bond angles of $120^\circ$ is

- (1) $\mathrm{PH_3}$
- (2) $\mathrm{ClF_3}$
- (3) $\mathrm{NCl_3}$
- **(4)** $\mathrm{BCl_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: boron trichloride ($\ce{BCl3}$), trigonal planar, with the Cl-B-Cl bond angle marked 120°](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q053_sol_1_89421f7c_29102026.svg?v=89421f7c76d6)

*boron trichloride ($\ce{BCl3}$), trigonal planar, with the Cl-B-Cl bond angle marked 120°*

![drawn: boron trichloride ($\ce{BCl3}$), trigonal planar, with the Cl-B-Cl bond angle marked 120°](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q053_solution_1_dfcb6942_27102026.svg?v=dfcb6942111d)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. $\mathrm{PH_3}$: 3 bond pairs and 1 lone pair on P, pyramidal, bond angle $\approx 93.5^\circ$.
2. $\mathrm{ClF_3}$: 3 bond pairs and 2 lone pairs on Cl ($sp^3d$), T-shaped, bond angle $\approx 87.5^\circ$.
3. $\mathrm{NCl_3}$: 3 bond pairs and 1 lone pair on N, pyramidal, bond angle $\approx 107^\circ$.
4. $\mathrm{BCl_3}$: 3 bond pairs and no lone pair on B ($sp^2$), trigonal planar, bond angle $= 120^\circ$, which is option $4$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 14)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q053_8103ed28_27102026.png?v=8103ed28b2af)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q053_3ef26a71_27102026.png?v=3ef26a7194a8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** VSEPR: count bonding pairs and lone pairs on the central atom; three bonds with no lone pair is trigonal planar at $120^\circ$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who counts the three chlorines round nitrogen and treats $\mathrm{NCl_3}$ as the same shape as $\mathrm{BCl_3}$, since the formulas differ only in the central atom, reads off $120^\circ$. Nitrogen's lone pair is the term left out of the electron-pair count; it makes the molecule pyramidal at about $107^\circ$, while boron carries no lone pair and is flat at $120^\circ$.
- **Why:** This question requires VSEPR applied to four named species, demonstrated by the stem asking for 'The species, having bond angles of $120^\circ$' while every option is an $\mathrm{EX_3}$ formula.
<!--/ecat-->

## Q54

Chemistry · physical · Solutions

If molality of the dilute solution is doubled, the value of molal depression constant ($K_f$) will be

- (1) Doubled
- (2) Halved
- (3) Tripled
- **(4)** Unchanged

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $K_f$ (molal depression constant) is a characteristic of solvent and is independent of molality.

**Solved independently** (answer withheld)

1. $\Delta T_f = K_f\, m$, and $K_f = \frac{R\, M_{solvent}\, T_f^2}{1000\, \Delta_{fus}H}$ depends only on the solvent, so doubling $m$ doubles $\Delta T_f$ while $K_f$ stays unchanged, which is option $4$.

**Subtopic:** Depression of Freezing Point · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 14)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q054_63e08b91_27102026.png?v=63e08b91e3ad)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q054_0b0b94c0_27102026.png?v=0b0b94c00e71)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The molal depression constant is a property of the solvent alone; in $\Delta T_f = K_f m$ only $\Delta T_f$ responds when the molality changes
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Doubling the molality does double something — in $\Delta T_f = K_f m$ it doubles $\Delta T_f$ — so a student holding that relation carries the doubling onto the symbol the stem actually names. $K_f$ is fixed by the solvent and keeps the same value at every concentration, so 'Doubled' is the right answer to a question about the freezing point depression, not about $K_f$.
- **Why:** This question requires stating how $K_f$ responds when a second quantity is changed, demonstrated by the stem 'If molality of the dilute solution is doubled, the value of molal depression constant ($K_f$) will be' and by options that are only directions of change.
<!--/ecat-->

## Q55

Chemistry · organic · Alcohols, Phenols and Ethers

Which one is the most acidic compound?

- (1) 4-methylphenol `Cc1ccc(O)cc1` ![4-methylphenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q055_question_s1_36957d6d_27102026.svg?v=36957d6d42ec)
- (2) phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q055_question_s2_09ff75eb_27102026.svg?v=09ff75ebe831)
- (3) 4-nitrophenol `O=[N+]([O-])c1ccc(O)cc1` ![4-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q055_question_s3_befa77e9_27102026.svg?v=befa77e9b759)
- **(4)** 2,4,6-trinitrophenol `O=[N+]([O-])c1cc([N+](=O)[O-])c(O)c([N+](=O)[O-])c1` ![2,4,6-trinitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q055_question_s4_334a7b8b_27102026.svg?v=334a7b8ba7f7)

Options as printed:

![printed figure: (1) 4-methylphenol; (2) phenol; (3) 4-nitrophenol; (4) 2,4,6-trinitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q055_c8b55680_27102026.svg?v=c8b55680aa33)

*(1) 4-methylphenol; (2) phenol; (3) 4-nitrophenol; (4) 2,4,6-trinitrophenol*

![drawn: (1) 4-methylphenol; (2) phenol; (3) 4-nitrophenol; (4) 2,4,6-trinitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q055_question_f0d6c17b_27102026.svg?v=f0d6c17bd484)  
*drawn on the booklet's geometry, checked against its SMILES*

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $-\mathrm{NO_2}$ group has very strong $-I$ & $-R$ effects.

**Solved independently** (answer withheld)

1. Acidity of a phenol rises when electron-withdrawing groups stabilise the phenoxide ion by $-I$ and $-R$ effects, and falls with electron-donating groups.
2. Option 1 ($p$-cresol) has $-\mathrm{CH_3}$ ($+I$, hyperconjugation), which destabilises the phenoxide, so it is less acidic than phenol (option 2).
3. Option 3 ($p$-nitrophenol) has one $-\mathrm{NO_2}$ at the para position, which stabilises the phenoxide, so it is more acidic than phenol.
4. Option 4 (2,4,6-trinitrophenol) has three $-\mathrm{NO_2}$ groups at ortho and para positions, giving the greatest phenoxide stabilisation ($\mathrm{p}K_a \approx 0.4$).
5. Order: $4 > 3 > 2 > 1$, so the most acidic compound is option $4$.

**Subtopic:** Acidity of Phenols · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 14)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q055_d9d69e7b_27102026.png?v=d9d69e7b1262)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q055_d681298d_27102026.png?v=d681298d687c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Phenol acidity rises as electron-withdrawing groups spread the negative charge of the phenoxide; three nitro groups do far more than one
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A student who knows a nitro group pulls charge off the phenoxide and stabilises it picks the nitrophenol the moment one appears, without counting how many nitro groups each ring carries. 4-nitrophenol is the answer to 'which of these is more acidic than phenol'; the stem asked for the most acidic, and picric acid carries three nitro groups, two of them ortho to the OH.
- **Why:** This question requires four phenols ranked on acidity, demonstrated by the stem's 'Which one is the most acidic compound?' and by the options running from a methyl-substituted phenol through phenol and one nitro group to three nitro groups.
- **Note:** The four options are printed as drawn structures: (1) 4-methylphenol, (2) phenol, (3) 4-nitrophenol, (4) 2,4,6-trinitrophenol.
<!--/ecat-->

## Q56

Chemistry · inorganic · The p–Block Elements

It is because of inability of $\mathrm{ns^{2}}$ electrons of the valence shell to participate in bonding that

- **(1)** $\mathrm{Sn^{2+}}$ is reducing while $\mathrm{Pb^{4+}}$ is oxidising
- (2) $\mathrm{Sn^{2+}}$ is oxidising while $\mathrm{Pb^{4+}}$ is reducing
- (3) $\mathrm{Sn^{2+}}$ and $\mathrm{Pb^{2+}}$ are both oxidising and reducing
- (4) $\mathrm{Sn^{4+}}$ is reducing while $\mathrm{Pb^{4+}}$ is oxidising

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Inability of $ns^{2}$ electrons of the valence shell to participate in bonding on moving down the group in heavier p-block elements is called inert pair effect
2. As a result, $\mathrm{Pb(II)}$ is more stable than $\mathrm{Pb(IV)}$
3. $\mathrm{Sn(IV)}$ is more stable than $\mathrm{Sn(II)}$
4. $\therefore$ $\mathrm{Pb(IV)}$ is easily reduced to $\mathrm{Pb(II)}$
5. $\therefore$ $\mathrm{Pb(IV)}$ is oxidising agent
6. $\mathrm{Sn(II)}$ is easily oxidised to $\mathrm{Sn(IV)}$
7. $\therefore$ $\mathrm{Sn(II)}$ is reducing agent

**Solved independently** (answer withheld)

1. The reluctance of $ns^2$ electrons to bond (inert pair effect) grows down group 14, so the $+2$ state gets more stable relative to $+4$.
2. For tin the $+4$ state is still the more stable one, so $\mathrm{Sn^{2+}} \rightarrow \mathrm{Sn^{4+}} + 2e^-$ happens readily, making $\mathrm{Sn^{2+}}$ a reducing agent.
3. For lead the $+2$ state is the more stable one, so $\mathrm{Pb^{4+}} + 2e^- \rightarrow \mathrm{Pb^{2+}}$ happens readily, making $\mathrm{Pb^{4+}}$ an oxidising agent.
4. This matches option $1$.

**Subtopic:** General Properties & Trends of Group 14 (Carbon Family) · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 14)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q056_6caf6d94_27102026.png?v=6caf6d949a39)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q056_88426514_27102026.png?v=88426514e159)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Inert pair effect: going down group 14 the $\mathrm{ns^2}$ pair stops taking part in bonding, so lead settles at +2 and tin at +4
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who remembers that the inert pair stabilises the lower oxidation state, but not that it is the heavier element whose pair goes inert, applies it to tin and reads $\mathrm{Sn^{2+}}$ as the settled ion that takes electrons. It is lead's pair that is inert: $\mathrm{Pb^{2+}}$ is the stable state, so $\mathrm{Pb^{4+}}$ is the oxidising ion and $\mathrm{Sn^{2+}}$ the reducing one, and option (2) prints those two roles exchanged.
- **Why:** This question requires the consequence NCERT draws from the inert pair effect, demonstrated by the stem reading 'It is because of inability of $\mathrm{ns^{2}}$ electrons of the valence shell to participate in bonding that' with each option completing it as a redox role.
<!--/ecat-->

## Q57

Chemistry · organic · Hydrocarbons

Predict the correct intermediate and product in the following reaction $\mathrm{H_3C{-}C{\equiv}CH} \xrightarrow[\mathrm{HgSO_4}]{\mathrm{H_2O,\ H_2SO_4}} \underset{\text{(A)}}{\text{intermediate}} \longrightarrow \underset{\text{(B)}}{\text{product}}$

- (1) A : $\mathrm{H_3C{-}\underset{\underset{\displaystyle SO_4}{|}}{C}{=}CH_2}$ B : $\mathrm{H_3C{-}\underset{\underset{\displaystyle O}{\|}}{C}{-}CH_3}$
- (2) A : $\mathrm{H_3C{-}\underset{\underset{\displaystyle OH}{|}}{C}{=}CH_2}$ B : $\mathrm{H_3C{-}\underset{\underset{\displaystyle SO_4}{|}}{C}{=}CH_2}$
- (3) A : $\mathrm{H_3C{-}\underset{\underset{\displaystyle O}{\|}}{C}{-}CH_3}$ B : $\mathrm{H_3C{-}C{\equiv}CH}$
- **(4)** A : $\mathrm{H_3C{-}\underset{\underset{\displaystyle OH}{|}}{C}{=}CH_2}$ B : $\mathrm{H_3C{-}\underset{\underset{\displaystyle O}{\|}}{C}{-}CH_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{H_3C{-}C{\equiv}CH} \longrightarrow \underset{\text{(A)}}{\mathrm{H_3C{-}\overset{\overset{\displaystyle OH}{|}}{C}{=}CH}}$
2. $\underset{\text{(A)}}{\mathrm{H_3C{-}\overset{\overset{\displaystyle OH}{|}}{C}{=}CH}} \xrightarrow{\text{Tautomerism}} \underset{\text{(B)}}{\mathrm{H_3C{-}\overset{\overset{\displaystyle O}{\|}}{C}{-}CH_3}}$

**Solved independently** (answer withheld)

1. Acid-catalysed $\mathrm{Hg^{2+}}$ hydration adds $\mathrm{H_2O}$ across $\mathrm{C{\equiv}C}$ by Markovnikov's rule, so $\mathrm{OH}$ goes to the internal carbon: $\mathrm{H_3C{-}C{\equiv}CH} \rightarrow \mathrm{H_3C{-}C(OH){=}CH_2}$ (enol, A).
2. The enol undergoes keto-enol tautomerism: $\mathrm{H_3C{-}C(OH){=}CH_2} \rightarrow \mathrm{H_3C{-}CO{-}CH_3}$ (acetone, B).
3. A = enol, B = acetone matches option $4$.

**Subtopic:** Chemical Properties of Alkynes · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 14)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q057_e6160607_27102026.png?v=e61606079fbe)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q057_117a0c4a_27102026.png?v=117a0c4a3653)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Acid-catalysed hydration of an alkyne over $\mathrm{HgSO_4}$ adds water the Markovnikov way to give an enol, which tautomerises to the ketone
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student who knows the hydration of propyne ends at acetone picks an option whose B is acetone, then takes the $\mathrm{H_2SO_4}$ to add across the triple bond and writes a sulfate adduct as the intermediate. The first species formed is the enol $\mathrm{CH_3{-}C(OH){=}CH_2}$, so option (1) is right on B and wrong on A.
- **Why:** This question requires both species along the hydration of an alkyne, demonstrated by the stem's 'Predict the correct intermediate and product in the following reaction' and by each option printing an A and a B that are accepted together.
<!--/ecat-->

## Q58

Chemistry · physical · Chemical Equilibrium

Which one of the following statements is not correct?

- (1) Catalyst does not initiate any reaction
- **(2)** The value of equilibrium constant is changed in the presence of a catalyst in the reaction at equilibrium
- (3) Enzymes catalyse mainly bio-chemical reactions
- (4) Coenzymes increase the catalytic activity of enzyme

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A catalyst decreases activation energies of both the forward and backward reaction by same amount, therefore, it speeds up both forward and backward reaction by same rate.
2. Equilibrium constant is therefore not affected by catalyst at a given temperature.

**Solved independently** (answer withheld)

1. A catalyst lowers the activation energy of the forward and backward reactions by the same amount, so $k_f$ and $k_b$ rise by the same factor and $K = \frac{k_f}{k_b}$ stays the same. Statement 2 says $K$ changes, so it is the incorrect one: option $2$.

**Subtopic:** Effect of a Catalyst on Equilibrium · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 14)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q058_be9d3a93_27102026.png?v=be9d3a9370fb)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q058_0339d7a7_27102026.png?v=0339d7a77165)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A catalyst lowers the forward and reverse activation barriers by the same amount, so it speeds the approach to equilibrium but leaves $K$ and the equilibrium position unchanged
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Option 1 is itself a denial, 'Catalyst does not initiate any reaction', so a student already tracking the stem's 'not correct' meets a second negative and reads this option as the false one. It is true: a catalyst speeds up a reaction that already proceeds and cannot start one that would not otherwise go.
- **Why:** This question requires grading four printed claims about catalysts and enzymes as stated, demonstrated by option 2 'The value of equilibrium constant is changed in the presence of a catalyst in the reaction at equilibrium', which is settled by the stated effect of a catalyst on $K$ with nothing to compute and no new case to apply a rule to.
<!--/ecat-->

## Q59

Chemistry · physical · Structure of Atom

Which one is the wrong statement?

- (1) de-Broglie's wavelength is given by $\lambda = \dfrac{h}{mv}$, where m = mass of the particle, v = group velocity of the particle
- (2) The uncertainty principle is $\Delta E \times \Delta t \geq \dfrac{h}{4\pi}$
- (3) Half-filled and fully filled orbitals have greater stability due to greater exchange energy, greater symmetry and more balanced arrangement
- **(4)** The energy of $2s$ orbital is less than the energy of $2p$ orbital in case of Hydrogen like atoms

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Energy of $2s$-orbital and $2p$-orbital in case of hydrogen like atoms is equal.

**Solved independently** (answer withheld)

1. For a hydrogen-like atom, $E_n = -\frac{13.6\,Z^2}{n^2}\,\text{eV}$, which depends only on $n$, not on $l$.
2. So $E_{2s} = E_{2p}$; the claim $E_{2s} < E_{2p}$ is false, while options $1$, $2$ and $3$ are standard correct statements, so the answer is option $4$.

**Subtopic:** Atomic Orbitals: Shapes, Energies and Nodes · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 15)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q059_fdcb84dc_27102026.png?v=fdcb84dce759)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q059_e02a5dbd_27102026.png?v=e02a5dbd8b46)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In hydrogen-like one-electron species the orbital energy depends on $n$ alone, so $2s$ and $2p$ are degenerate; the $(n+l)$ ordering splits them only in multi-electron atoms
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who holds the uncertainty principle only as $\Delta x \cdot \Delta p \geq \frac{h}{4\pi}$ sees $\Delta E$ and $\Delta t$ sitting in that same inequality and reads the swapped pair of variables as the planted error. The energy–time form is an equally standard statement of the same principle, so option 2 is true and is not the wrong statement.
- **Why:** This question requires using the rule that a one-electron species' energy depends on $n$ alone on the $2s$ versus $2p$ case, demonstrated by option 4 'The energy of $2s$ orbital is less than the energy of $2p$ orbital in case of Hydrogen like atoms', whose truth turns entirely on the 'Hydrogen like' qualifier.
- **Note:** The keyed option 4 is false only because of its closing qualifier: drop 'in case of Hydrogen like atoms' and it states the true $(n+l)$ ordering for multi-electron atoms. That is the route by which the keyed statement can be read as true, and it is recorded here rather than as the trap, because a trap must name an option a student is pulled towards.
<!--/ecat-->

## Q60

Chemistry · physical · Thermodynamics

A gas is allowed to expand in a well insulated container against a constant external pressure of $2.5\,\mathrm{atm}$ from an initial volume of $2.50\,\mathrm{L}$ to a final volume of $4.50\,\mathrm{L}$. The change in internal energy $\Delta U$ of the gas in joules will be

- (1) $1136.25\,\mathrm{J}$
- (2) $-500\,\mathrm{J}$
- **(3)** $-505\,\mathrm{J}$
- (4) $+505\,\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\Delta U = q + w$
2. For adiabatic process, $q = 0$
3. $\therefore\ \Delta U = w$
4. $= -P\cdot\Delta V$
5. $= -2.5\,\mathrm{atm} \times (4.5 - 2.5)\,\mathrm{L}$
6. $= -2.5 \times 2\,\mathrm{L\text{-}atm}$
7. $= -5 \times 101.3\,\mathrm{J}$
8. $= -506.5\,\mathrm{J}$
9. $\approx -505\,\mathrm{J}$

**Solved independently** (answer withheld)

1. The container is well insulated, so the process is adiabatic: $q = 0$.
2. First law: $\Delta U = q + w = w$.
3. Work against constant external pressure: $w = -P_{ext}(V_2 - V_1) = -2.5\,\mathrm{atm} \times (4.50 - 2.50)\,\mathrm{L} = -5.0\,\mathrm{L\,atm}$.
4. Convert: $-5.0\,\mathrm{L\,atm} \times 101\,\mathrm{J\,L^{-1}\,atm^{-1}} \approx -505\,\mathrm{J}$.
5. $\Delta U = -505\,\mathrm{J}$, which is option $3$.

**Subtopic:** Internal Energy and First Law of Thermodynamics · **Difficulty:** hard (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 15)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q060_e64ea071_27102026.png?v=e64ea071c859)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q060_5d1e43a3_27102026.png?v=5d1e43a3e541)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Well insulated means $q = 0$, so $\Delta U$ is the work alone, and expansion against a constant external pressure gives $w = -P_{ext}\Delta V$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student who works out $P_{ext}\Delta V = 2.5 \times 2.00 = 5.0\,\mathrm{L\,atm} = 505\,\mathrm{J}$ and enters that as $\Delta U$ has the magnitude and the method right and the sign still to settle. The gas expands, so it spends those 505 J on the surroundings, and with no heat admitted through the insulation $\Delta U = -505\,\mathrm{J}$.
- **Also:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Putting the final volume into the work term in place of the change in volume gives $2.5 \times 4.50 \times 101 = 1136.25\,\mathrm{J}$, which is option (1) to the last digit. The work is set by $\Delta V = 2.00\,\mathrm{L}$, not by the 4.50 L the gas ends at.
- **Why:** This question requires the work computed from $-P_{ext}\Delta V$ with $q$ set to zero, demonstrated by the stem's 'well insulated container against a constant external pressure of $2.5\,\mathrm{atm}$' and options quoted in joules.
- **Note:** The options are built on $1\,\mathrm{L\,atm} = 101\,\mathrm{J}$: $5\,\mathrm{L\,atm}$ gives the keyed $505\,\mathrm{J}$, and option (2)'s $-500\,\mathrm{J}$ is the same work rounded at $100\,\mathrm{J}$ per $\mathrm{L\,atm}$.
<!--/ecat-->

## Q61

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Consider the reactions :
$\underset{(\mathrm{C_2H_6O})}{\mathrm{X}} \xrightarrow[573\,\mathrm{K}]{\mathrm{Cu}\,/} \mathrm{A} \xrightarrow[-\mathrm{OH},\,\Delta]{[\mathrm{Ag(NH_3)_2}]^{+}} \text{Silver mirror observed}$
$\mathrm{A} \xrightarrow{-\mathrm{OH},\,\Delta} \mathrm{Y}$
$\mathrm{A} \xrightarrow{\mathrm{NH_2-NH-\overset{\displaystyle O}{\overset{\|}{C}}-NH_2}} \mathrm{Z}$
Identify A, X, Y and Z

![printed figure: X ($\ce{C2H6O}$) →(Cu / 573 K) A; A →($\ce{(Ag(NH3)2)+}$, –OH, Δ) Silver mirror observed; A →(–OH, Δ) Y; A →(hydrazinecarboxamide ($\ce{NH2-NH-C(=O)-NH2}$)) Z](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q061_a8755655_29102026.svg?v=a8755655dceb)

*X ($\ce{C2H6O}$) →[Cu / 573 K] A; A →[$\ce{[Ag(NH3)2]+}$, –OH, Δ] Silver mirror observed; A →[–OH, Δ] Y; A →[hydrazinecarboxamide ($\ce{NH2-NH-C(=O)-NH2}$)] Z*

![drawn: X ($\ce{C2H6O}$) →(Cu / 573 K) A; A →($\ce{(Ag(NH3)2)+}$, –OH, Δ) Silver mirror observed; A →(–OH, Δ) Y; A →(hydrazinecarboxamide ($\ce{NH2-NH-C(=O)-NH2}$)) Z](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q061_question_1a203f32_27102026.svg?v=1a203f32f278)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: hydrazinecarboxamide `NNC(N)=O` ![hydrazinecarboxamide](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q061_question_s1_e70c30b7_27102026.svg?v=e70c30b73bfb)

- (1) A-Methoxymethane, X-Ethanoic acid, Y-Acetate ion, Z-hydrazine
- (2) A-Methoxymethane, X-Ethanol, Y-Ethanoic acid, Z-Semicarbazide
- **(3)** A-Ethanal, X-Ethanol, Y-But-2-enal, Z-Semicarbazone
- (4) A-Ethanol, X-Acetaldehyde, Y-Butanone, Z-Hydrazone

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Since 'A' gives positive silver mirror test therefore, it must be an aldehyde or $\alpha$-Hydroxyketone.
2. Reaction with semicarbazide indicates that A can be an aldehyde or ketone.
3. Reaction with $\mathrm{OH^{-}}$ i.e., aldol condensation (by assuming alkali to be dilute) indicates that A is aldehyde as aldol reaction of ketones is reversible and carried out in special apparatus.
4. These indicates option (3).
5. $\underset{\text{(X)}}{\mathrm{CH_3{-}CH_2OH}} \xrightarrow[573\,\mathrm{K}]{\mathrm{Cu}} \underset{\text{(A) ethanal}}{\mathrm{CH_3{-}CHO}} \xrightarrow[\Delta]{[\mathrm{Ag(NH_3)_2}]^{+},\,\mathrm{OH^{-}}} \mathrm{CH_3{-}COOH}$
6. $\mathrm{CH_3{-}CHO} \xrightarrow{\mathrm{H_2N-NH-\overset{\overset{O}{\|}}{C}-NH_2}} \underset{\text{(Z)}}{\mathrm{CH_3-CH=N-NH-\overset{\overset{O}{\|}}{C}-NH_2}}$
7. $\mathrm{CH_3{-}CHO} \xrightarrow{\mathrm{OH^{-}}} \underset{\text{3-Hydroxybutanal}}{\mathrm{CH_3-\overset{\overset{OH}{|}}{C}H-CH_2-CHO}} \xrightarrow{\Delta} \underset{\text{(Y) But-2-enal}}{\mathrm{CH_3-CH=CH-CHO}}$

**Solved independently** (answer withheld)

1. $X = \mathrm{C_2H_6O}$ is dehydrogenated by Cu at 573 K, so it is a primary alcohol: $X = \mathrm{CH_3CH_2OH}$ (ethanol).
2. $\mathrm{CH_3CH_2OH} \xrightarrow{\mathrm{Cu},\,573\,K} \mathrm{CH_3CHO} + \mathrm{H_2}$, so $A$ = ethanal, consistent with the silver mirror from $[\mathrm{Ag(NH_3)_2}]^+$.
3. $2\,\mathrm{CH_3CHO} \xrightarrow{\mathrm{OH^-},\,\Delta} \mathrm{CH_3CH{=}CHCHO}$ (aldol condensation), so $Y$ = but-2-enal.
4. $\mathrm{CH_3CHO} + \mathrm{H_2NNHCONH_2} \rightarrow \mathrm{CH_3CH{=}NNHCONH_2}$, so $Z$ = semicarbazone.
5. A = Ethanal, X = Ethanol, Y = But-2-enal, Z = Semicarbazone matches option $3$.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen, Nucleophilic Addition Reactions · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 15)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q061_ff9e07d9_27102026.png?v=ff9e07d92de6)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q061_07bdd540_27102026.png?v=07bdd540bf4b)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Copper at 573 K dehydrogenates a primary alcohol to an aldehyde, and the aldehyde then gives Tollens' silver mirror, self-condenses to an alpha,beta-unsaturated aldehyde and condenses with semicarbazide to a semicarbazone
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student who recognises the familiar ethanol-and-acetaldehyde pair but does not check which side of the $\mathrm{Cu}/573\,\mathrm{K}$ arrow each belongs on puts ethanol at A and acetaldehyde at X. The arrow runs away from the alcohol, so X is ethanol and A is ethanal, and only an aldehyde at A can give the silver mirror the scheme reports.
- **Why:** This question requires every arrow in the scheme mapped to its product, demonstrated by the stem's 'Identify A, X, Y and Z' and by each option naming all four together.
<!--/ecat-->

## Q62

Chemistry · organic · Hydrocarbons

Which one is the correct order of acidity?

- (1) $\mathrm{CH_2=CH_2} > \mathrm{CH_3-CH=CH_2} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH\equiv CH}$
- **(2)** $\mathrm{CH\equiv CH} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-CH_3}$
- (3) $\mathrm{CH\equiv CH} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH_3-CH_3}$
- (4) $\mathrm{CH_3-CH_3} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH\equiv CH}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Correct order is
2. $\underset{\text{(Two acidic hydrogens)}}{\mathrm{H-C\equiv C-H}} > \underset{\text{(One acidic hydrogen)}}{\mathrm{H_3C-C\equiv C-H}} > \mathrm{H_2C=CH_2} > \mathrm{CH_3-CH_3}$

**Solved independently** (answer withheld)

1. Acidity of a C-H bond rises with the $s$-character of the carbon: $sp\,(50\%) > sp^2\,(33\%) > sp^3\,(25\%)$, so terminal alkynes $>$ alkenes $>$ alkanes.
2. In $\mathrm{CH_3-C\equiv CH}$ the $+I$ effect of $\mathrm{CH_3}$ destabilises the acetylide anion, so $\mathrm{CH\equiv CH} > \mathrm{CH_3-C\equiv CH}$.
3. Order: $\mathrm{CH\equiv CH} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-CH_3}$, which is option $2$.

**Subtopic:** Chemical Properties of Alkynes · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 15)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q062_8c112151_27102026.png?v=8c1121513c75)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q062_34b096c4_27102026.png?v=34b096c4593d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Terminal C-H acidity follows the s-character of the carbon holding the hydrogen, $sp > sp^2 > sp^3$, and a methyl group on the alkyne pushes its acidity down a little
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student who knows acidity tracks s-character but attaches it the wrong way round, as more s-character meaning a weaker acid, writes the series out from ethane and ends with ethyne. Option (4) is the keyed chain printed back to front: the $sp$ carbon of ethyne holds its electron pair closest in and is the most acidic, with ethane least.
- **Why:** This question requires four hydrocarbons put in order of acidity, demonstrated by the stem's 'Which one is the correct order of acidity?' and by every option printing a full four-term chain.
<!--/ecat-->

## Q63

Chemistry · physical · Electrochemistry

In the electrochemical cell : $\mathrm{Zn|ZnSO_4(0.01\,M)||CuSO_4(1.0\,M)|Cu}$, the emf of this Daniel cell is $E_1$. When the concentration of $\mathrm{ZnSO_4}$ is changed to $1.0\,\mathrm{M}$ and that of $\mathrm{CuSO_4}$ changed to $0.01\,\mathrm{M}$, the emf changes to $E_2$. From the following, which one is the relationship between $E_1$ and $E_2$? (Given, $\frac{RT}{F} = 0.059$)

- (1) $E_1 = E_2$
- (2) $E_1 < E_2$
- **(3)** $E_1 > E_2$
- (4) $E_2 = 0 \neq E_1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{Zn|ZnSO_4(0.01\,M)||CuSO_4(1.0\,M)|Cu}$
2. $\therefore\ E_1 = E^{\circ}_{\mathrm{cell}} - \frac{2.303RT}{2 \times F} \times \log\frac{(0.01)}{1}$
3. When concentrations are changed
4. $\therefore\ E_2 = E^{\circ}_{\mathrm{cell}} - \frac{2.303RT}{2F} \times \log\frac{1}{0.01}$
5. i.e., $E_1 > E_2$

**Solved independently** (answer withheld)

1. Cell reaction: $\mathrm{Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu}$, with $n = 2$.
2. Nernst equation: $E = E^\circ - \frac{0.059}{2}\log\frac{[\mathrm{Zn^{2+}}]}{[\mathrm{Cu^{2+}}]}$.
3. $E_1 = E^\circ - 0.0295\log\frac{0.01}{1.0} = E^\circ + 0.059\,\mathrm{V}$.
4. $E_2 = E^\circ - 0.0295\log\frac{1.0}{0.01} = E^\circ - 0.059\,\mathrm{V}$.
5. $E_1 - E_2 = 0.118\,\mathrm{V} > 0$, so $E_1 > E_2$, which is option $3$.

**Subtopic:** Nernst Equation · **Difficulty:** medium (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 16)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q063_7ea8cca7_27102026.png?v=7ea8cca778b5)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q063_7e7b248c_27102026.png?v=7e7b248c57d8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Nernst equation: the cell emf falls as the product ion builds up relative to the reactant ion, so $E = E^\circ - \frac{0.059}{2}\log\frac{[\mathrm{Zn^{2+}}]}{[\mathrm{Cu^{2+}}]}$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who writes the Nernst quotient straight off the cell diagram as $[\mathrm{Cu^{2+}}]/[\mathrm{Zn^{2+}}]$ instead of $[\mathrm{Zn^{2+}}]/[\mathrm{Cu^{2+}}]$ gets $\log Q = +2$ for the first cell and $-2$ for the second. That hands back $E_1 < E_2$, the keyed inequality turned round; with the quotient the right way up $E_1 = E^\circ + 0.059$ and $E_2 = E^\circ - 0.059$.
- **Why:** This question requires both emfs worked out from the Nernst equation and then compared, demonstrated by the stem supplying '(Given, $\frac{RT}{F} = 0.059$)' together with two sets of concentrations.
<!--/ecat-->

## Q64

Chemistry · organic · Amines

The correct increasing order of basic strength for the following compounds is

![printed figure: (I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q064_eb608e4e_29102026.svg?v=eb608e4e7026)

*(I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline*

![drawn: (I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q064_question_a5a3fe8b_27102026.svg?v=a5a3fe8b0947)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: aniline `Nc1ccccc1` ![aniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q064_question_s1_d81f396d_27102026.svg?v=d81f396d8ee8); 4-nitroaniline `Nc1ccc([N+](=O)[O-])cc1` ![4-nitroaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q064_question_s2_7e623ecc_27102026.svg?v=7e623ecc1e2d); 4-methylaniline `Cc1ccc(N)cc1` ![4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q064_question_s3_eec3bc0c_27102026.svg?v=eec3bc0c957a)

- (1) II < III < I
- (2) III < I < II
- (3) III < II < I
- **(4)** II < I < III

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $-\mathrm{NO_2}$ has strong $-R$ effect and $-\mathrm{CH_3}$ shows $+R$ effect.
2. $\therefore$ Order of basic strength is

![printed figure: 4-nitroaniline < aniline < 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q064_sol_1_889b4354_29102026.svg?v=889b4354c62d)

*4-nitroaniline < aniline < 4-methylaniline*

![drawn: 4-nitroaniline < aniline < 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q064_solution_1_3bb4a087_27102026.svg?v=3bb4a0874636)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. Identify the compounds: I is aniline $\mathrm{C_6H_5NH_2}$, II is p-nitroaniline $p\text{-}\mathrm{O_2NC_6H_4NH_2}$, III is p-toluidine $p\text{-}\mathrm{CH_3C_6H_4NH_2}$.
2. The $-\mathrm{NO_2}$ group at the para position withdraws electrons by $-R$ and $-I$, delocalising the $\mathrm{N}$ lone pair further and making II the weakest base.
3. The $-\mathrm{CH_3}$ group at the para position donates electrons by $+I$ and hyperconjugation, increasing electron density on $\mathrm{N}$ and making III the strongest base.
4. Aniline (I) with no substituent lies between them, so the increasing order is $\mathrm{II} < \mathrm{I} < \mathrm{III}$, which is option $4$.

**Subtopic:** Chemical Reactions of Amines (Basicity, Alkylation and Acylation) · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 16)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q064_bf05df26_27102026.png?v=bf05df261b51)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q064_56dfd7ba_27102026.png?v=56dfd7ba8836)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Ring substituents shift aniline's basicity: $-\mathrm{NO_2}$ pulls electron density off the nitrogen, $-\mathrm{CH_3}$ pushes it towards the nitrogen
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who gets the chemistry right — 4-methylaniline the strongest base, 4-nitroaniline the weakest — and then writes the list strongest-first lands exactly on III < I < II. The stem asks for increasing strength, so the same correct ranking printed in the direction asked is II < I < III.
- **Why:** This question requires three printed anilines ranked on one property, demonstrated by the stem "The correct increasing order of basic strength for the following compounds is" with (I) aniline, (II) 4-nitroaniline and (III) 4-methylaniline supplied in the figure.
- **Note:** The stem does not name the three compounds; the figure carries them, and its stored labels read "(I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline".
<!--/ecat-->

## Q65

Chemistry · inorganic · The p–Block Elements

In which pair of ions both the species contain S – S bond?

- (1) $\mathrm{S_2O_7^{2-}}$, $\mathrm{S_2O_3^{2-}}$
- **(2)** $\mathrm{S_4O_6^{2-}}$, $\mathrm{S_2O_3^{2-}}$
- (3) $\mathrm{S_2O_7^{2-}}$, $\mathrm{S_2O_8^{2-}}$
- (4) $\mathrm{S_4O_6^{2-}}$, $\mathrm{S_2O_7^{2-}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: tetrathionate $\ce{(S4O6)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q065_sol_1_a2e0d8cd_29102026.svg?v=a2e0d8cdf2bf)

*tetrathionate $\ce{[S4O6]^{2-}}$*

![drawn: tetrathionate $\ce{(S4O6)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q065_solution_1_37385f29_27102026.svg?v=37385f291e1e)  
*drawn on the booklet's geometry, checked against its SMILES*

![printed figure: thiosulfate $\ce{(S2O3)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q065_sol_2_b52ef43a_29102026.svg?v=b52ef43a6334)

*thiosulfate $\ce{[S2O3]^{2-}}$*

![drawn: thiosulfate $\ce{(S2O3)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q065_solution_2_facf9da8_27102026.svg?v=facf9da8e11e)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. $\mathrm{S_2O_7^{2-}}$ (pyrosulfate) is $\mathrm{O_3S{-}O{-}SO_3}$: the two S atoms are bridged by O, so no S–S bond.
2. $\mathrm{S_2O_8^{2-}}$ (peroxodisulfate) is $\mathrm{O_3S{-}O{-}O{-}SO_3}$: a peroxide O–O link, no S–S bond.
3. $\mathrm{S_2O_3^{2-}}$ (thiosulfate) has one S bonded directly to the central S: contains an S–S bond.
4. $\mathrm{S_4O_6^{2-}}$ (tetrathionate) is $\mathrm{O_3S{-}S{-}S{-}SO_3}$: contains S–S bonds.
5. Only option $2$ ($\mathrm{S_4O_6^{2-}}$, $\mathrm{S_2O_3^{2-}}$) has S–S in both species.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 16)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q065_3414432d_27102026.png?v=3414432d9f63)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q065_bd2b244d_27102026.png?v=bd2b244d4c44)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Thiosulphate and tetrathionate hold sulphur bonded straight to sulphur; in pyrosulphate and peroxodisulphate the two sulphurs are joined through oxygen
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The S–S bond in thiosulphate is the securely taught one, so a student anchors on $\mathrm{S_2O_3^{2-}}$ and then has to choose its partner. $\mathrm{S_2O_7^{2-}}$ shows two sulphurs in its formula, but they are bridged as S–O–S, so half this pair qualifies and half does not.
- **Why:** This question requires knowing which sulphur oxoanions carry a direct sulphur–sulphur bond, demonstrated by the stem "In which pair of ions both the species contain S – S bond?" with $\mathrm{S_2O_7^{2-}}$ offered in three of the four pairs.
<!--/ecat-->

## Q66

Chemistry · inorganic · Coordination Compounds – Practice

The correct order of the stoichiometries of $\mathrm{AgCl}$ formed when $\mathrm{AgNO_3}$ in excess is treated with the complexes : $\mathrm{CoCl_3\cdot 6NH_3}$, $\mathrm{CoCl_3\cdot 5NH_3}$, $\mathrm{CoCl_3\cdot 4NH_3}$ respectively is

- (1) 1 $\mathrm{AgCl}$, 3 $\mathrm{AgCl}$, 2 $\mathrm{AgCl}$
- (2) 3 $\mathrm{AgCl}$, 1 $\mathrm{AgCl}$, 2 $\mathrm{AgCl}$
- **(3)** 3 $\mathrm{AgCl}$, 2 $\mathrm{AgCl}$, 1 $\mathrm{AgCl}$
- (4) 2 $\mathrm{AgCl}$, 3 $\mathrm{AgCl}$, 1 $\mathrm{AgCl}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Complexes are respectively $\mathrm{[Co(NH_3)_6]Cl_3}$, $\mathrm{[Co(NH_3)_5Cl]Cl_2}$ and $\mathrm{[Co(NH_3)_4Cl_2]Cl}$

**Solved independently** (answer withheld)

1. Co(III) has coordination number $6$, so $\mathrm{NH_3}$ and any remaining $\mathrm{Cl^-}$ fill six positions in the coordination sphere.
2. $\mathrm{CoCl_3\cdot 6NH_3} = [\mathrm{Co(NH_3)_6}]\mathrm{Cl_3}$: all $3$ $\mathrm{Cl^-}$ are ionisable, giving $3\,\mathrm{AgCl}$.
3. $\mathrm{CoCl_3\cdot 5NH_3} = [\mathrm{Co(NH_3)_5Cl}]\mathrm{Cl_2}$: $2$ ionisable $\mathrm{Cl^-}$, giving $2\,\mathrm{AgCl}$.
4. $\mathrm{CoCl_3\cdot 4NH_3} = [\mathrm{Co(NH_3)_4Cl_2}]\mathrm{Cl}$: $1$ ionisable $\mathrm{Cl^-}$, giving $1\,\mathrm{AgCl}$.
5. Order $3, 2, 1$ matches option $3$.

**Subtopic:** Werner’s Theory and Applications of Coordination Compounds · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 16)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q066_502aa3d2_27102026.png?v=502aa3d28eff)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q066_b3759b08_27102026.png?v=b3759b08c02c)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Werner's primary and secondary valence: only the chloride sitting outside the coordination sphere is free to come down as AgCl
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The three wrong options are permutations of the same counts 1, 2 and 3. The reversal that a student reading "order" as increasing would write, 1 AgCl then 2 AgCl then 3 AgCl, is not printed at all, and no rule applied to the three formulas yields 1-3-2, 3-1-2 or 2-3-1.
- **Why:** This question requires the ionisable chloride counted for each of three cobalt ammine complexes, demonstrated by the stem naming "$\mathrm{CoCl_3\cdot 6NH_3}$, $\mathrm{CoCl_3\cdot 5NH_3}$, $\mathrm{CoCl_3\cdot 4NH_3}$ respectively" against options that print one AgCl count per complex.
- **Note:** The printed shape is three answers wanted at once, not a ranking: each option gives one AgCl count per named complex, joined by the stem's "respectively". The pattern classifier read the stem word "order" and returned arrange_in_order, which the options do not bear out — none of them orders the three complexes.
<!--/ecat-->

## Q67

Chemistry · inorganic · The p–Block Elements

Match the interhalogen compounds of column I with the geometry in column II and assign the correct code

| List-I | | List-II | |
|---|---|---|---|
| a | $\mathrm{XX'}$ | i | T-shape |
| b | $\mathrm{XX'_3}$ | ii | Pentagonal bipyramidal |
| c | $\mathrm{XX'_5}$ | iii | Linear |
| d | $\mathrm{XX'_7}$ | iv | Square-pyramidal |
|  |  | v | Tetrahedral |

- (1) (a) (iii) (b) (iv) (c) (i) (d) (ii)
- **(2)** (a) (iii) (b) (i) (c) (iv) (d) (ii)
- (3) (a) (v) (b) (iv) (c) (iii) (d) (ii)
- (4) (a) (iv) (b) (iii) (c) (ii) (d) (i)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{XX'} \rightarrow$ Linear
2. $\mathrm{XX'_3} \rightarrow$ Example : $\mathrm{CIF_3} \rightarrow$ T-shape
3. $\mathrm{XX'_5} \rightarrow$ Example : $\mathrm{BrF_5} \rightarrow$ Square pyramidal
4. $\mathrm{XX'_7} \rightarrow$ Example : $\mathrm{IF_7} \rightarrow$ Pentagonal bipyramidal

**Solved independently** (answer withheld)

1. $\mathrm{XX'}$ is a diatomic molecule, so it is linear: (a)-(iii).
2. $\mathrm{XX'_3}$ (e.g. $\mathrm{ClF_3}$) has 3 bond pairs and 2 lone pairs ($sp^3d$), giving a T-shape: (b)-(i).
3. $\mathrm{XX'_5}$ (e.g. $\mathrm{BrF_5}$) has 5 bond pairs and 1 lone pair ($sp^3d^2$), giving a square-pyramidal shape: (c)-(iv).
4. $\mathrm{XX'_7}$ (e.g. $\mathrm{IF_7}$) has 7 bond pairs ($sp^3d^3$), giving a pentagonal bipyramidal shape: (d)-(ii).
5. The match (a)-(iii), (b)-(i), (c)-(iv), (d)-(ii) is option $2$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 16)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q067_52f6d7ee_27102026.png?v=52f6d7ee0139)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q067_8e7aec11_27102026.png?v=8e7aec11af1f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Interhalogen shapes from bond pairs plus lone pairs: $\mathrm{XX'}$ linear, $\mathrm{XX'_3}$ T-shaped, $\mathrm{XX'_5}$ square pyramidal, $\mathrm{XX'_7}$ pentagonal bipyramidal
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  This code keeps the two secure pairs, $\mathrm{XX'}$ linear and $\mathrm{XX'_7}$ pentagonal bipyramidal, and interchanges only the middle two, which is what a student writes who holds 'T-shaped' and 'square pyramidal' as the two interhalogen shapes without which formula owns which. Counting settles it: $\mathrm{XX'_5}$ has five bonds and one lone pair and is the square pyramid, $\mathrm{XX'_3}$ has three bonds and two lone pairs and is the T.
- **Why:** This question requires each interhalogen formula paired with its shape, demonstrated by the stem 'Match the interhalogen compounds of column I with the geometry in column II and assign the correct code' and options printed as pairing codes.
- **Note:** Column II prints five entries for four formulas, so 'Tetrahedral' is left unused by the key.
<!--/ecat-->

## Q68

Chemistry · inorganic · The D- and F-Block Elements – Practice

The reason for greater range of oxidation states in actinoids is attributed to

- (1) The radioactive nature of actinoids
- (2) Actinoid contraction
- **(3)** $5f$, $6d$ and $7s$ levels having comparable energies
- (4) $4f$ and $5d$ levels being close in energies

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. It is a fact.

**Solved independently** (answer withheld)

1. Actinoids show a wider range of oxidation states than lanthanoids because their $5f$, $6d$ and $7s$ levels have comparable energies, so electrons from all of them can be used in bonding, which is option $3$.

**Subtopic:** Lanthanoids & Actinoids · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 17)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q068_1ed997af_27102026.png?v=1ed997af2a00)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q068_2cd51efb_27102026.png?v=2cd51efb2aa1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Actinoids show a wide span of oxidation states because 5f, 6d and 7s lie close enough in energy for electrons from all three to enter bonding
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who holds the right shape of the explanation — two sets of levels close in energy — reaches for the f and d pair met first, the lanthanoids' 4f and 5d. That pair belongs to the series whose oxidation state is almost always +3, which is the opposite of the wide range the stem is asking about.
- **Also:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Actinoid contraction is a real term from the same section and sounds like an explanation, so a student picks it as the named cause. What it accounts for is the steady fall in actinoid radii across the series, not how many oxidation states each element can reach.
- **Why:** This question requires the explanation the text gives for a stated property, demonstrated by the stem "The reason for greater range of oxidation states in actinoids is attributed to".
<!--/ecat-->

## Q69

Chemistry · physical · Chemical Equilibrium

A $20$ litre container at $400\,\mathrm{K}$ contains $\mathrm{CO_2}(g)$ at pressure $0.4\,\mathrm{atm}$ and an excess of $\mathrm{SrO}$ (neglect the volume of solid $\mathrm{SrO}$). The volume of the containers is now decreased by moving the movable piston fitted in the container. The maximum volume of the container, when pressure of $\mathrm{CO_2}$ attains its maximum value, will be (Given that : $\mathrm{SrCO_3}(s) \rightleftharpoons \mathrm{SrO}(s) + \mathrm{CO_2}(g)$. $K_p = 1.6\,\mathrm{atm}$)

- **(1)** $5$ litre
- (2) $10$ litre
- (3) $4$ litre
- (4) $2$ litre

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Max. pressure of $\mathrm{CO_2}$ = Pressure of $\mathrm{CO_2}$ at equilibrium
2. For reaction,
3. $\mathrm{SrCO_3}(s) \rightleftharpoons \mathrm{SrO}(s) + \mathrm{CO_2}$
4. $K_p = P_{\mathrm{CO_2}} = 1.6\,\mathrm{atm}$ = maximum pressure of $\mathrm{CO_2}$
5. Volume of container at this stage,
6. $V = \frac{nRT}{P}$ ...(i)
7. Since container is sealed and reaction was not earlier at equilibrium
8. $\therefore\ n = \text{constant}$
9. $n = \frac{PV}{RT} = \frac{0.4 \times 20}{RT}$ ...(ii)
10. Put equation (ii) in equation (i)
11. $V = \left[\frac{0.4 \times 20}{RT}\right]\frac{RT}{1.6} = 5\,\mathrm{L}$

**Solved independently** (answer withheld)

1. For $\mathrm{SrCO_3}(s) \rightleftharpoons \mathrm{SrO}(s) + \mathrm{CO_2}(g)$, $K_p = p_{\mathrm{CO_2}}$, so the maximum pressure of $\mathrm{CO_2}$ is $1.6\,\mathrm{atm}$.
2. Until $p_{\mathrm{CO_2}}$ reaches $1.6\,\mathrm{atm}$ no $\mathrm{SrCO_3}$ forms, so the gas amount is fixed and Boyle's law applies at $400\,\mathrm{K}$: $P_1V_1 = P_2V_2$.
3. $0.4\,\mathrm{atm} \times 20\,\mathrm{L} = 1.6\,\mathrm{atm} \times V \Rightarrow V = \frac{8}{1.6} = 5\,\mathrm{L}$.
4. Below $5\,\mathrm{L}$ the pressure stays at $1.6\,\mathrm{atm}$, so the maximum volume at which it attains its maximum is $5\,\mathrm{L}$, option $1$.

**Subtopic:** Homogeneous and Heterogeneous Equilibria · **Difficulty:** hard (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 17)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q069_11c5f877_27102026.png?v=11c5f8779419)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q069_9d2a1493_27102026.png?v=9d2a14931d1f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a heterogeneous equilibrium the $\mathrm{CO_2}$ pressure cannot climb past $K_p$ — squeeze beyond that and the gas is taken up as $\mathrm{SrCO_3}$ instead of rising
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  A student works out how far the gas can be squeezed, $1.6/0.4 = 4$, and writes 4 down as the answer because the number is sitting there. That 4 is the compression factor, not a volume; the volume is $20/4 = 5$ litre.
- **Why:** This question requires a volume computed from the given pressure and the given equilibrium constant, demonstrated by the stem supplying "$20$ litre", "$0.4\,\mathrm{atm}$" and "$K_p = 1.6\,\mathrm{atm}$" against four volume options.
<!--/ecat-->

## Q70

Chemistry · organic · General Organic Chemistry

The correct statement regarding electrophile is

- (1) Electrophile is a negatively charged species and can form a bond by accepting a pair of electrons from a nucleophile
- (2) Electrophile is a negatively charged species and can form a bond by accepting a pair of electrons from another electrophile
- (3) Electrophiles are generally neutral species and can form a bond by accepting a pair of electrons from a nucleophile
- **(4)** Electrophile can be either neutral or positively charged species and can form a bond by accepting a pair of electrons from a nucleophile

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Fact.

**Solved independently** (answer withheld)

1. An electrophile is an electron-deficient species that forms a bond by accepting an electron pair from a nucleophile; it can be neutral (e.g. $\mathrm{BF_3}$, $\mathrm{AlCl_3}$) or positively charged (e.g. $\mathrm{NO_2^+}$, $\mathrm{H^+}$), so option $4$ is correct and options $1$, $2$, $3$ are wrong.

**Subtopic:** Electrophile and Nucleophile · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 17)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q070_b643b44c_27102026.png?v=b643b44cad0f)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q070_0f20374e_27102026.png?v=0f20374ebd78)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An electrophile is electron-deficient — neutral like $\mathrm{BF_3}$ or positive like $\mathrm{H^+}$ — and it takes an electron pair from a nucleophile
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The electrophiles drilled hardest in the chapter — $\mathrm{BF_3}$, $\mathrm{AlCl_3}$, $\mathrm{SO_3}$ — are all neutral, so "generally neutral species" reads like the taught generalisation and the rest of the sentence is word for word correct. $\mathrm{H^+}$ and $\mathrm{NO_2^+}$ are electrophiles too, which is why the charge clause has to allow both.
- **Why:** This question requires the definition of an electrophile as stated, demonstrated by the stem "The correct statement regarding electrophile is" over four options that differ only in which charges an electrophile may carry and which species it takes electrons from.
<!--/ecat-->

## Q71

Chemistry · inorganic · Environmental Chemistry

Which of the following is a sink for $\mathrm{CO}$?

- (1) Haemoglobin
- **(2)** Micro-organisms present in the soil
- (3) Oceans
- (4) Plants

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Micro-organisms present in the soil is a sink for $\mathrm{CO}$.

**Solved independently** (answer withheld)

1. Soil micro-organisms take up and oxidise atmospheric $\mathrm{CO}$, which makes soil the main natural sink for $\mathrm{CO}$, so the answer is option $2$.

**Subtopic:** Air Pollution · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 17)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q071_d8e3881c_27102026.png?v=d8e3881c4145)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q071_181a5974_27102026.png?v=181a59740514)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A sink is whatever takes a pollutant back out of the atmosphere; for carbon monoxide that is soil micro-organisms, which oxidise it
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Haemoglobin is the one thing the chapter ties to carbon monoxide — CO binds it some 200 times more tightly than oxygen does — so the word CO pulls a student straight to it. That fact answers what CO does to a person who breathes it, not what removes CO from the air, and haemoglobin inside a body is no part of the atmospheric budget.
- **Why:** This question requires the stated fact about what removes CO from the atmosphere, demonstrated by the stem "Which of the following is a sink for $\mathrm{CO}$?" over four named candidates with no criterion printed to apply.
<!--/ecat-->

## Q72

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The element $Z = 114$ has been discovered recently. It will belong to which of the following family group and electronic configuration?

- (1) Halogen family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{5}$
- **(2)** Carbon family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{2}$
- (3) Oxygen family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{4}$
- (4) Nitrogen family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{6}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $Z = 114$ belong to Group $14$, carbon family
2. Electronic configuration $= [\mathrm{Rn}]5f^{14}6d^{10}7s^{2}7p^{2}$

**Solved independently** (answer withheld)

1. The core is $[\mathrm{Rn}]$ with $Z = 86$, so $114 - 86 = 28$ electrons remain to place.
2. Fill in order: $5f^{14}$ (14), $6d^{10}$ (10), $7s^{2}$ (2), which uses $26$ electrons.
3. The remaining $28 - 26 = 2$ electrons go to $7p$, giving $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{2}$.
4. Valence configuration $ns^{2}np^{2}$ means group $14$, the carbon family, which is option $2$.

**Subtopic:** Electronic Configurations · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 17)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q072_c362062f_27102026.png?v=c362062fa030)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q072_ef4aadb8_27102026.png?v=ef4aadb8c796)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Place a superheavy element by filling the shells after [Rn] — 5f, then 6d, then 7s, then 7p — and the number of 7p electrons fixes the group
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  A student takes the 28 electrons past radon, spends 14 on 5f and 10 on 6d, sees 4 left and puts all four into 7p while still writing 7s2 — so the 7s pair is counted twice. The configuration printed in this option sums to 116 electrons, and the family name goes with it, which is why both halves look consistent.
- **Why:** This question requires the filling order applied to a new atomic number, demonstrated by the stem "The element $Z = 114$ has been discovered recently. It will belong to which of the following family group and electronic configuration?"
- **Note:** Option 4 is internally inconsistent as printed: it names the nitrogen family but gives $7p^{6}$, which is a noble gas configuration and sums to 118 electrons. Option 1 ($7p^{5}$) and option 3 ($7p^{4}$) are each self-consistent, for elements 117 and 116.
<!--/ecat-->

## Q73

Chemistry · inorganic · Coordination Compounds – Practice

Correct increasing order for the wavelengths of absorption in the visible region for the complexes of $\mathrm{Co^{3+}}$ is

- **(1)** $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(H_2O)_6]^{3+}}$
- (2) $\mathrm{[Co(H_2O)_6]^{3+}}$, $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$
- (3) $\mathrm{[Co(H_2O)_6]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(en)_3]^{3+}}$
- (4) $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(H_2O)_6]^{3+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The order of the ligand in the spectrochemical series
2. $\mathrm{H_2O} < \mathrm{NH_3} < \mathrm{en}$
3. Hence, the wavelength of the light observed will be in the order
4. $\mathrm{[Co(H_2O)_6]^{3+}} < \mathrm{[Co(NH_3)_6]^{3+}} < \mathrm{[Co(en)_3]^{3+}}$
5. Thus, wavelength absorbed will be in the opposite order
6. i.e., $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(H_2O)_6]^{3+}}$

**Solved independently** (answer withheld)

1. Spectrochemical series: $\mathrm{en} > \mathrm{NH_3} > \mathrm{H_2O}$, so $\Delta_o$: $\mathrm{[Co(en)_3]^{3+}} > \mathrm{[Co(NH_3)_6]^{3+}} > \mathrm{[Co(H_2O)_6]^{3+}}$.
2. Absorbed wavelength $\lambda = \frac{hc}{\Delta_o}$, so a larger $\Delta_o$ means a shorter $\lambda$.
3. Increasing $\lambda$: $\mathrm{[Co(en)_3]^{3+}} < \mathrm{[Co(NH_3)_6]^{3+}} < \mathrm{[Co(H_2O)_6]^{3+}}$, which is option $1$.

**Subtopic:** Crystal Field Theory and Its Limitations, Colour in Coordination Compounds · **Difficulty:** hard (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 17)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q073_4f0c382b_27102026.png?v=4f0c382bd97d)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q073_f663bd38_27102026.png?v=f663bd38be86)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A strong-field ligand widens $\Delta_o$, and a wider gap is absorbed at a shorter wavelength — wavelength runs opposite to the spectrochemical series
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A student recalls the spectrochemical series in the order it is taught, $\mathrm{H_2O} < \mathrm{NH_3} < \mathrm{en}$, and writes it straight down as the increasing order asked for. That is the increasing order of field strength; since $\lambda = hc/\Delta_o$, increasing wavelength is the same three complexes the other way round.
- **Why:** This question requires three complexes of one metal ion ranked on absorption wavelength, demonstrated by the stem "Correct increasing order for the wavelengths of absorption in the visible region for the complexes of $\mathrm{Co^{3+}}$ is".
<!--/ecat-->

## Q74

Chemistry · organic · Biomolecules

Which of the following statements is not correct?

- (1) Insulin maintains sugar level in the blood of a human body
- (2) Ovalbumin is a simple food reserve in egg-white
- (3) Blood proteins thrombin and fibrinogen are involved in blood clotting
- **(4)** Denaturation makes the proteins more active

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Due to denaturation of proteins, globules unfold and helix get uncoiled and protein loses its biological activity.

**Solved independently** (answer withheld)

1. Insulin lowers blood glucose, so option $1$ is correct; ovalbumin is the simple storage protein of egg-white, so option $2$ is correct; thrombin and fibrinogen take part in clotting, so option $3$ is correct. Denaturation destroys the native 3D structure and so the function of a protein, which makes option $4$ the incorrect statement.

**Subtopic:** Denaturation of Proteins and Enzymes · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q074_7b34695b_27102026.png?v=7b34695ba7d0)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q074_462adac2_27102026.png?v=462adac2f3be)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Denaturation unfolds the protein's secondary and tertiary structure, and the biological activity goes with it
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Options 1, 2 and 3 are textbook sentences about three unrelated proteins — insulin and blood sugar, ovalbumin as egg-white food reserve, thrombin and fibrinogen in clotting — and none of them has a word altered to make it falsely attractive under a "not correct" stem. "Ovalbumin is a simple food reserve in egg-white" is the source's own wording, so nothing but the keyed option is reachable by a wrong route.
- **Why:** This question requires each printed claim about proteins graded against the stated facts, demonstrated by the stem "Which of the following statements is not correct?" over four independent statements.
<!--/ecat-->

## Q75

Chemistry · inorganic · Coordination Compounds – Practice

An example of a sigma bonded organometallic compound is :

- (1) Ruthenocene
- **(2)** Grignard's reagent
- (3) Ferrocene
- (4) Cobaltocene

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Grignard's reagent i.e., $\mathrm{RMgX}$ is $\sigma$-bonded organometallic compound.

**Solved independently** (answer withheld)

1. Grignard's reagent $\mathrm{RMgX}$ contains a direct $\sigma$ bond between carbon and magnesium, while ruthenocene, ferrocene and cobaltocene are $\pi$-bonded $\eta^5$ sandwich compounds $\mathrm{M(C_5H_5)_2}$, so the answer is option $2$.

**Subtopic:** Bonding in Coordination Compounds and Metal Carbonyls · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q075_7527fc95_27102026.png?v=7527fc95f0f4)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q075_0421dab3_27102026.png?v=0421dab37f19)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Organometallics are split by how carbon holds the metal: Grignard's C–Mg is a plain sigma bond, the metallocenes bond through the ring's $\pi$ system
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Ferrocene is the organometallic compound the chapter names first and draws, so a student who stored "ferrocene is the example" and not the bonding split picks it. Its iron is held by the $\pi$ electrons of two cyclopentadienyl rings, which puts it in the other half of the same taught classification.
- **Why:** This question requires the stated fact about which named compound is sigma bonded, demonstrated by the stem "An example of a sigma bonded organometallic compound is :" with three of the four options being metallocenes.
<!--/ecat-->

## Q76

Chemistry · physical · Solutions

Which of the following is dependent on temperature?

- (1) Molality
- **(2)** Molarity
- (3) Mole fraction
- (4) Weight percentage

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Molarity includes volume of solution which can change with change in temperature.

**Solved independently** (answer withheld)

1. Molarity $M = \frac{n_{\text{solute}}}{V_{\text{solution}}\,(\text{L})}$ contains the solution volume.
2. Volume expands or contracts with temperature, so $V = V(T)$ and hence $M$ changes with $T$.
3. Molality $m = \frac{n_{\text{solute}}}{\text{kg solvent}}$, mole fraction $x = \frac{n_i}{n_{\text{total}}}$ and weight percentage $= \frac{w_{\text{solute}}}{w_{\text{solution}}} \times 100$ use only masses or moles, so they are temperature independent.
4. Only molarity depends on temperature, which is option $2$.

**Subtopic:** Molarity · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q076_d448f7de_27102026.png?v=d448f7de8346)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q076_f4ba32c8_27102026.png?v=f4ba32c8d5b1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Any concentration measured per volume drifts with temperature; the ones built on mass or mole counts do not
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Molarity and molality differ by one letter, so a student who stored only "one of this pair changes with temperature" can come down on either. Molality is moles per kilogram of solvent and mass is fixed; it is molarity that carries volume in its denominator, and volume expands when the solution is warmed.
- **Why:** This question requires the stated temperature behaviour of the concentration units, demonstrated by the stem "Which of the following is dependent on temperature?" over four named concentration measures.
<!--/ecat-->

## Q77

Chemistry · physical · Thermodynamics

For a given reaction, $\Delta H = 35.5\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S = 83.6\,\mathrm{JK^{-1}\,mol^{-1}}$. The reaction is spontaneous at : (Assume that $\Delta H$ and $\Delta S$ do not vary with temperature)

- (1) $T < 425\,\mathrm{K}$
- **(2)** $T > 425\,\mathrm{K}$
- (3) All temperatures
- (4) $T > 298\,\mathrm{K}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\because\ \Delta G = \Delta H - T\Delta S$
2. For a reaction to be spontaneous, $\Delta G = -\mathrm{ve}$
3. i.e., $\Delta H < T\Delta S$
4. $\therefore\ T > \frac{\Delta H}{\Delta S} = \frac{35.5 \times 10^{3}\,\mathrm{J}}{83.6\,\mathrm{JK^{-1}}}$
5. i.e., $T > 425\,\mathrm{K}$

**Solved independently** (answer withheld)

1. Spontaneity requires $\Delta G = \Delta H - T\Delta S < 0$.
2. Convert units: $\Delta H = 35.5\,\mathrm{kJ\,mol^{-1}} = 35500\,\mathrm{J\,mol^{-1}}$.
3. At equilibrium $T = \frac{\Delta H}{\Delta S} = \frac{35500}{83.6} \approx 424.6\,\mathrm{K} \approx 425\,\mathrm{K}$.
4. Since $\Delta H > 0$ and $\Delta S > 0$, $\Delta G < 0$ only when $T\Delta S > \Delta H$, i.e. $T > 425\,\mathrm{K}$, which is option $2$.

**Subtopic:** Gibbs Energy and Spontaneity · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q077_06db63f5_27102026.png?v=06db63f527f9)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q077_f21799c6_27102026.png?v=f21799c66758)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Gibbs energy fixes a crossover temperature: when $\Delta H$ and $\Delta S$ are both positive the reaction turns spontaneous only above $T = \Delta H/\Delta S$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The crossover $T = \frac{35500}{83.6} = 425$ K is printed in two options, so the only thing left in doubt is which side of it, and a student who rearranges $\Delta H - T\Delta S < 0$ into $T\Delta S < \Delta H$ writes $T < 425$ K. With $\Delta S$ positive the $T\Delta S$ term only overtakes $\Delta H$ as $T$ rises, so the spontaneous side is the hot one.
- **Why:** This question requires the temperature at which $\Delta G$ changes sign, demonstrated by the stem supplying both $\Delta H = 35.5\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S = 83.6\,\mathrm{JK^{-1}\,mol^{-1}}$ and by the options being inequalities in $T$.
<!--/ecat-->

## Q78

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

The most suitable method of separation of $1 : 1$ mixture of ortho and para-nitrophenols is

- (1) Sublimation
- (2) Chromatography
- (3) Crystallisation
- **(4)** Steam distillation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Steam distillation is the most suitable method of separation of $1 : 1$ mixture of ortho and para nitrophenols as there is intramolecular H-bonds in ortho nitrophenol.

**Solved independently** (answer withheld)

1. In $o$-nitrophenol the $-OH$ and $-NO_2$ groups form an intramolecular hydrogen bond, so the molecules do not associate and the compound is steam volatile.
2. In $p$-nitrophenol hydrogen bonding is intermolecular, so the molecules associate, raising the boiling point; it is not steam volatile.
3. The ortho isomer distils over with steam while the para isomer stays behind, so steam distillation (option $4$) is the most suitable method.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q078_eb508105_27102026.png?v=eb5081052dd1)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q078_89c7bd8d_27102026.png?v=89c7bd8d540b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Steam distillation separates a steam-volatile component from one that is not; ortho-nitrophenol is chelated by intramolecular hydrogen bonding and comes over with the steam, para-nitrophenol does not
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Both nitrophenols are solids, so a student reaches for the technique the same chapter gives for solids, fractional crystallisation. The two isomers are too close in solubility for that to split a $1:1$ mixture, while their steam volatilities differ sharply because only the ortho isomer is internally hydrogen bonded.
- **Why:** This question requires the purification technique the chapter ties to this pair, demonstrated by the stem naming a "$1 : 1$ mixture of ortho and para-nitrophenols" and by the four options being four named separation methods.
<!--/ecat-->

## Q79

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which one of the following pairs of species have the same bond order?

- (1) $\mathrm{CO}$, $\mathrm{NO}$
- (2) $\mathrm{O_2}$, $\mathrm{NO^+}$
- **(3)** $\mathrm{CN^-}$, $\mathrm{CO}$
- (4) $\mathrm{N_2}$, $\mathrm{O_2^-}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{CN^{(-)}}$ and $\mathrm{CO}$ have bond order $3$ each.

**Solved independently** (answer withheld)

1. Bond order $= \frac{N_b - N_a}{2}$ from MO theory.
2. $\mathrm{CO}$ (14 e$^-$): $\frac{10-4}{2} = 3$; $\mathrm{NO}$ (15 e$^-$): $\frac{10-5}{2} = 2.5$, so option 1 differs.
3. $\mathrm{O_2}$ (16 e$^-$): $\frac{10-6}{2} = 2$; $\mathrm{NO^+}$ (14 e$^-$): $3$, so option 2 differs.
4. $\mathrm{CN^-}$ (14 e$^-$): $\frac{10-4}{2} = 3$; $\mathrm{CO}$: $3$, so option 3 matches.
5. $\mathrm{N_2}$ (14 e$^-$): $3$; $\mathrm{O_2^-}$ (17 e$^-$): $\frac{10-7}{2} = 1.5$, so option 4 differs.
6. Only $\mathrm{CN^-}$, $\mathrm{CO}$ share bond order $3$, which is option $3$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q079_89b006bf_27102026.png?v=89b006bfd3e0)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q079_53e4f2fe_27102026.png?v=53e4f2fe90f6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Bond order read off the molecular-orbital electron count, where isoelectronic species share it: $\mathrm{CN^-}$ and $\mathrm{CO}$ both hold 14 electrons and are both triple bonded
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  $\mathrm{CO}$ is the triple-bonded species every student has memorised and $\mathrm{NO}$ sits one electron away from it, so a student who confirms $\mathrm{CO}$ at 3 and treats that extra electron as non-bonding reads the pair as equal. The 15th electron goes into an antibonding $\pi^*$, which pulls $\mathrm{NO}$ down to $2.5$.
- **Why:** This question requires two species to be matched on one computed property, demonstrated by the stem "Which one of the following pairs of species have the same bond order?" and by each option printing a pair that is accepted or rejected whole.
- **Note:** The answer is a pair, not a number, so the demand is comparison rather than calculation even though each bond order has to be counted out.
<!--/ecat-->

## Q80

Chemistry · organic · Haloalkanes and Haloarenes

Identify A and predict the type of reaction

![printed figure: 1-bromo-3-methoxybenzene →($\ce{NaNH2}$) A](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q080_4d1640a1_29102026.svg?v=4d1640a13be3)

*1-bromo-3-methoxybenzene →[$\ce{NaNH2}$] A*

![drawn: 1-bromo-3-methoxybenzene →($\ce{NaNH2}$) A](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_question_8ada3544_27102026.svg?v=8ada35441301)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: 1-bromo-3-methoxybenzene `COc1cccc(Br)c1` ![1-bromo-3-methoxybenzene](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_question_s1_4606fe4b_27102026.svg?v=4606fe4bf0c9)

- **(1)** 3-methoxyaniline `COc1cccc(N)c1` ![3-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_option_1_s1_eb8f97fa_27102026.svg?v=eb8f97fa5df6) — and substitution reaction
- (2) 2-methoxyaniline `COc1ccccc1N` ![2-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_option_2_s1_7f1e1454_27102026.svg?v=7f1e145464eb) — and elimination addition reaction
- (3) 1-bromo-2-methoxybenzene `COc1ccccc1Br` ![1-bromo-2-methoxybenzene](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_option_3_s1_5832fd0e_27102026.svg?v=5832fd0e2cda) — and cine substitution reaction
- (4) anisole `COc1ccccc1` ![anisole](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_option_4_s1_c9107e15_27102026.svg?v=c9107e15c534) — and cine substitution reaction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Sol. 1-bromo-3-methoxybenzene →($\ce{NH2-}$) 2-bromo-6-methoxybenzen-1-ide → 1,2-didehydro-3-methoxybenzene (Benzyne)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q080_sol_1_a9b6b4a5_27102026.svg?v=a9b6b4a5c1e8)

*Sol. 1-bromo-3-methoxybenzene →[$\ce{NH2-}$] 2-bromo-6-methoxybenzen-1-ide → 1,2-didehydro-3-methoxybenzene (Benzyne)*

![drawn: Sol. 1-bromo-3-methoxybenzene →($\ce{NH2-}$) 2-bromo-6-methoxybenzen-1-ide → 1,2-didehydro-3-methoxybenzene (Benzyne)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_solution_1_53c8d347_27102026.svg?v=53c8d347178f)  
*drawn on the booklet's geometry, checked against its SMILES*

![printed figure: 1,2-didehydro-3-methoxybenzene + $\ce{NH2-}$ (paths a and b) →(X) 2-amino-3-methoxybenzen-1-ide (Less stable); 1,2-didehydro-3-methoxybenzene + $\ce{NH2-}$ → 2-amino-6-methoxybenzen-1-ide →($\ce{H-NH2}$) 3-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q080_sol_2_c9521977_27102026.svg?v=c9521977ae14)

*1,2-didehydro-3-methoxybenzene + $\ce{NH2-}$ (paths a and b) →[X] 2-amino-3-methoxybenzen-1-ide (Less stable); 1,2-didehydro-3-methoxybenzene + $\ce{NH2-}$ → 2-amino-6-methoxybenzen-1-ide →[$\ce{H-NH2}$] 3-methoxyaniline*

![drawn: 1,2-didehydro-3-methoxybenzene + $\ce{NH2-}$ (paths a and b) →(X) 2-amino-3-methoxybenzen-1-ide (Less stable); 1,2-didehydro-3-methoxybenzene + $\ce{NH2-}$ → 2-amino-6-methoxybenzen-1-ide →($\ce{H-NH2}$) 3-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q080_solution_2_db4054ce_27102026.svg?v=db4054ce8e0c)  
*drawn on the booklet's geometry, checked against its SMILES*

1. More stable as $-$ve charge is close to electron withdrawing group
2. $\because$ Incoming nucleophile ends on same ‘C’ on which ‘Br’ (Leaving group) was present
3. $\therefore$ NOT cine substitution.

**Solved independently** (answer withheld)

1. $\mathrm{NH_2^-}$ removes the most acidic H ortho to Br, which is $\mathrm{C_2{-}H}$ lying between $\mathrm{OCH_3}$ (C1) and Br (C3).
2. Loss of $\mathrm{Br^-}$ from the resulting aryl anion gives the 2,3-benzyne (triple bond between C2 and C3).
3. $\mathrm{NH_2^-}$ adds to the aryne at C3 so the negative charge develops at C2, ortho to $\mathrm{OCH_3}$, where the $-I$ effect of oxygen stabilises it.
4. Protonation gives $m\text{-}\mathrm{H_2N C_6H_4 OCH_3}$ ($m$-anisidine): Br is replaced by $\mathrm{NH_2}$ at the same carbon.
5. Option 1 shows $m$-anisidine with a substitution reaction; option 2 has the wrong ($o$) product, options 3 and 4 do not introduce $\mathrm{NH_2}$, so the answer is option $1$.

**Subtopic:** Reactions of Haloarenes · **Difficulty:** unsure (0 steps, 4 of 4 options live)

**Printed in the booklet** (page 18)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q080_dc45e550_27102026.png?v=dc45e55071d1)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q080_cada23d9_27102026.png?v=cada23d95b6d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** $\mathrm{NaNH_2}$ on an aryl halide goes through a benzyne intermediate, so the amide can attach at the carbon next to the one that carried the halogen
- **Why:** This question requires the product of a named reagent on a named substrate together with the name of the pathway, demonstrated by the stem "Identify A and predict the type of reaction" over the scheme "1-bromo-3-methoxybenzene →[$\ce{NaNH2}$] A" and by each option carrying a structure plus a reaction-type phrase.
- **Note:** No trap can be written: the structure offered for A is absent from every option, whose text begins at "and ...", and with the structures gone options 3 and 4 both read "and cine substitution reaction", so the option set cannot be told apart. The shape is two_part rather than a plain MCQ because each option answers both halves of "Identify A and predict the type of reaction". The key is tagged as printed.
<!--/ecat-->

## Q81

Chemistry · physical · Chemical Kinetics

A first order reaction has a specific reaction rate of $10^{-2}\,\mathrm{s^{-1}}$. How much time will it take for $20\,\mathrm{g}$ of the reactant to reduce to $5\,\mathrm{g}$?

- (1) $238.6$ second
- **(2)** $138.6$ second
- (3) $346.5$ second
- (4) $693.0$ second

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $t_{1/2} = \frac{0.693}{10^{-2}}$ second
2. For the reduction of $20\,\mathrm{g}$ of reactant to $5\,\mathrm{g}$, two $t_{1/2}$ is required.
3. $\therefore\; t = 2 \times \frac{0.693}{10^{-2}}$ second
4. $= 138.6$ second

**Solved independently** (answer withheld)

1. For a first order reaction, $t = \frac{2.303}{k}\log\frac{[A]_0}{[A]}$.
2. $\frac{[A]_0}{[A]} = \frac{20\,\mathrm{g}}{5\,\mathrm{g}} = 4$.
3. $\frac{2.303}{k} = \frac{2.303}{10^{-2}\,\mathrm{s^{-1}}} = 230.3\,\mathrm{s}$.
4. $t = 230.3 \times \log 4 = 230.3 \times 0.6021 \approx 138.6\,\mathrm{s}$.
5. Check: $t_{1/2} = \frac{0.693}{10^{-2}} = 69.3\,\mathrm{s}$; $20 \to 10 \to 5\,\mathrm{g}$ is $2t_{1/2} = 138.6\,\mathrm{s}$, which is option $2$.

**Subtopic:** First Order Reactions · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 19)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q081_f5ad48e2_27102026.png?v=f5ad48e2d830)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q081_c5bc7f83_27102026.png?v=c5bc7f832d90)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** First order decay depends only on the ratio of amounts, so 20 g to 5 g is two half-lives: $t = \frac{2.303}{k}\log 4$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  A student reaches for the one number this chapter is memorised by, $t_{1/2} = \frac{0.693}{k}$, and divides $0.693$ by $10^{-2}$ as $693$ instead of $69.3$. Even carried out correctly that is a single half-life, and 20 g to 5 g is two, so $t = 2 \times 69.3 = 138.6$ s.
- **Why:** This question requires a time computed from a first order rate constant, demonstrated by the stem giving "a specific reaction rate of $10^{-2}\,\mathrm{s^{-1}}$" and asking the time for "$20\,\mathrm{g}$ of the reactant to reduce to $5\,\mathrm{g}$".
<!--/ecat-->

## Q82

Chemistry · inorganic · The p–Block Elements

Name the gas that can readily decolourises acidified $\mathrm{KMnO_4}$ solution:

- (1) $\mathrm{CO_2}$
- **(2)** $\mathrm{SO_2}$
- (3) $\mathrm{NO_2}$
- (4) $\mathrm{P_2O_5}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{SO_2}$ is readily decolourises acidified $\mathrm{KMnO_4}$.

**Solved independently** (answer withheld)

1. $\mathrm{SO_2}$ (S in +4 state) acts as a reducing agent and reduces purple $\mathrm{MnO_4^-}$ to nearly colourless $\mathrm{Mn^{2+}}$: $2\mathrm{MnO_4^-} + 5\mathrm{SO_2} + 2\mathrm{H_2O} \rightarrow 2\mathrm{Mn^{2+}} + 5\mathrm{SO_4^{2-}} + 4\mathrm{H^+}$; $\mathrm{CO_2}$, $\mathrm{NO_2}$ and $\mathrm{P_2O_5}$ do not readily do this, so the answer is option $2$.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 19)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q082_892a23dd_27102026.png?v=892a23ddeb2d)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q082_fe94c923_27102026.png?v=fe94c9237569)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** $\mathrm{SO_2}$ is a reducing gas — sulphur goes from $+4$ to $+6$ — and that is what discharges the purple colour of acidified permanganate
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  $\mathrm{NO_2}$ is the other pungent acidic oxide taught a few pages away, so a student holding only "a sharp, reactive gaseous oxide" picks it. The test needs a gas that can still be oxidised, and it is sulphur's $+4 \rightarrow +6$ step that the chapter attaches to decolourising $\mathrm{KMnO_4}$.
- **Why:** This question requires the name of the gas tied to a stated colour change, demonstrated by the stem "Name the gas that can readily decolourises acidified $\mathrm{KMnO_4}$ solution" and by the options being four named oxides.
- **Note:** Option 4, $\mathrm{P_2O_5}$, is not a gas, so it does not meet the stem's own description of what is wanted.
<!--/ecat-->

## Q83

Chemistry · organic · Alcohols, Phenols and Ethers

The heating of phenyl-methyl ethers with $\mathrm{HI}$ produces.

- (1) Ethyl chlorides
- (2) Iodobenzene
- **(3)** Phenol
- (4) Benzene

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: anisole →(HI) phenol + iodomethane ($\ce{CH3I}$)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q083_sol_1_25d3079a_27102026.svg?v=25d3079a1c2c)

*anisole →[HI] phenol + iodomethane ($\ce{CH3I}$)*

![drawn: anisole →(HI) phenol + iodomethane ($\ce{CH3I}$)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q083_solution_1_b31fe1d5_27102026.svg?v=b31fe1d505c6)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. HI protonates the ether oxygen: $\mathrm{C_6H_5\!-\!\overset{+}{O}H\!-\!CH_3}$.
2. $\mathrm{I^-}$ attacks the methyl carbon ($S_N2$), since the aryl $\mathrm{C\!-\!O}$ bond has partial double-bond character and cannot be cleaved.
3. $\mathrm{C_6H_5OCH_3 + HI \rightarrow C_6H_5OH + CH_3I}$, so the product is phenol, option $3$.

**Subtopic:** Reactions of Ethers · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 19)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q083_26ef2627_27102026.png?v=26ef2627b08a)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q083_0e67fc3c_27102026.png?v=0e67fc3ccc10)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Aryl alkyl ethers cleave with HI at the alkyl-oxygen bond, so anisole gives phenol plus methyl iodide
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Ether cleavage is carried as the single line 'HI gives an iodide', and a student who lets the iodide land on the ring side writes iodobenzene. Iodide cannot displace on the $sp^2$ ring carbon, whose C-O bond has partial double-bond character, so the methyl side takes the iodine and phenol is what is left.
- **Why:** This question requires the product a named reagent gives with a named substrate, demonstrated by the stem 'The heating of phenyl-methyl ethers with $\mathrm{HI}$ produces.' and four product names as options.
<!--/ecat-->

## Q84

Chemistry · inorganic · Coordination Compounds – Practice

Pick out the correct statement with respect $\mathrm{[Mn(CN)_6]^{3-}}$ :

- (1) It is $sp^3d^2$ hybridised and octahedral
- (2) It is $sp^3d^2$ hybridised and tetrahedral
- **(3)** It is $d^2sp^3$ hybridised and octahedral
- (4) It is $dsp^2$ hybridised and square planar

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{[Mn(CN)_6]^{3-}}$
2. $\mathrm{Mn(III)} = [\mathrm{Ar}]3d^{4}$
3. $\mathrm{CN^{-}}$ being strong field ligand forces pairing of electrons
4. This gives $t_{2g}^{4}e_{g}^{0}$
5. $\therefore$ $\mathrm{Mn(III)} = [\mathrm{Ar}]$

![printed figure: orbital-box diagram of Mn: 3d boxes with one paired and two unpaired electrons and two empty 3d boxes, empty 4s box and three empty 4p boxes; the two empty 3d, the 4s and the 4p boxes are enclosed in a dotted box labelled $d^2sp^3$; Coordination number of Mn = 6](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q084_sol_1_5e431c3b_29102026.svg?v=5e431c3bf524)

*orbital-box diagram of Mn: 3d boxes with one paired and two unpaired electrons and two empty 3d boxes, empty 4s box and three empty 4p boxes; the two empty 3d, the 4s and the 4p boxes are enclosed in a dotted box labelled $d^2sp^3$; Coordination number of Mn = 6*

6. $\because$ Coordination number of $\mathrm{Mn} = 6$
7. $\therefore$ Structure = octahedral
8. $\mathrm{[Mn(CN)_6]^{3-}} =$

![printed figure: orbital-box diagram: (Ar) then 3d boxes with one paired and two unpaired electrons, then two 3d boxes, one 4s box and three 4p boxes each filled with a crossed (ligand) electron pair, enclosed in a dotted box labelled $d^2sp^3$](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2017/2017_A/figures_agent/q084_sol_2_b484c37a_29102026.svg?v=b484c37afece)

*orbital-box diagram: [Ar] then 3d boxes with one paired and two unpaired electrons, then two 3d boxes, one 4s box and three 4p boxes each filled with a crossed (ligand) electron pair, enclosed in a dotted box labelled $d^2sp^3$*


**Solved independently** (answer withheld)

1. Oxidation state: $x + 6(-1) = -3 \Rightarrow x = +3$.
2. $\mathrm{Mn^{3+}}$ has configuration $[\mathrm{Ar}]\,3d^4$.
3. $\mathrm{CN^-}$ is a strong-field ligand, so the four $3d$ electrons pair into three orbitals ($t_{2g}^4$), leaving two $3d$ orbitals empty.
4. The two vacant $3d$, one $4s$ and three $4p$ orbitals mix: $d^2sp^3$ (inner-orbital) hybridisation.
5. Six ligands with $d^2sp^3$ give an octahedral geometry, which is option $3$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 19)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q084_9c60dd77_27102026.png?v=9c60dd7746bf)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q084_0a9a6148_27102026.png?v=0a9a6148a569)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Strong-field $\mathrm{CN^-}$ pairs the $d^4$ electrons of Mn(III) and frees two inner $3d$ orbitals, so the complex is inner-orbital $d^2sp^3$ and octahedral
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Six ligands do make an octahedron, so this option gets the shape right and a student who counts ligands and stops reaches for the outer-orbital $sp^3d^2$ set that fits $\mathrm{[MnF_6]^{3-}}$. $\mathrm{CN^-}$ is a strong-field ligand, so it pairs the $d$ electrons first and the two freed $3d$ orbitals make the set $d^2sp^3$.
- **Also:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  $\mathrm{[Ni(CN)_4]^{2-}}$ is the cyanide complex taught as $dsp^2$ and square planar, and that pairing carries over to any ion with $\mathrm{CN^-}$ in it. The ion here has six cyanides, not four, so a four-coordinate orbital set cannot be built.
- **Why:** This question requires the hybridisation rule for a strong-field ligand applied to this ion, demonstrated by the options holding the coordination number fixed and differing in the orbital set, 'It is $sp^3d^2$ hybridised and octahedral' against 'It is $d^2sp^3$ hybridised and octahedral'.
- **Note:** The stem reads 'Pick out the correct statement' and each option is a two-part claim about hybridisation and shape, so the printed shape is statements judged one by one rather than a plain MCQ.
<!--/ecat-->

## Q85

Chemistry · inorganic · The s-Block Elements

Ionic mobility of which of the following alkali metal ions is lowest when aqueous solution of their salts are put under an electric field?

- (1) $\mathrm{Na}$
- (2) $\mathrm{K}$
- (3) $\mathrm{Rb}$
- **(4)** $\mathrm{Li}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{Li^{+}}$ being smallest, has maximum charge density
2. $\therefore$ $\mathrm{Li^{+}}$ is most heavily hydrated among all alkali metal ions. Effective size of $\mathrm{Li^{+}}$ in aq solution is therefore, largest.
3. $\therefore$ Moves slowest under electric field.

**Solved independently** (answer withheld)

1. Smaller bare ion means higher charge density, so stronger hydration: $\mathrm{Li^+} > \mathrm{Na^+} > \mathrm{K^+} > \mathrm{Rb^+}$.
2. A bigger hydrated radius means lower mobility, so $\mathrm{Li^+} < \mathrm{Na^+} < \mathrm{K^+} < \mathrm{Rb^+}$, which makes $\mathrm{Li^+}$ the lowest: option $4$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 19)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q085_d17554e3_27102026.png?v=d17554e3b7e5)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q085_531c7f70_27102026.png?v=531c7f701edd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Ionic mobility in water goes by hydrated size, not bare size, so the smallest ion $\mathrm{Li^+}$ drags the biggest water sheath and moves slowest
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Rank the four on bare ionic radius and the largest ion, $\mathrm{Rb^+}$, is the one that must move slowest, which is the answer reached by reading past the stem's 'aqueous solution'. In water the small, densely charged $\mathrm{Li^+}$ holds the thickest hydration shell, so the mobility order is the reverse of the bare-size order and $\mathrm{Li}$ is lowest.
- **Why:** This question requires four ions of one group compared on a single property under a stated medium, demonstrated by the stem 'when aqueous solution of their salts are put under an electric field'.
<!--/ecat-->

## Q86

Chemistry · physical · Chemical Equilibrium

The equilibrium constants of the following are.
$\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$ $K_1$
$\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$ $K_2$
$\mathrm{H_2 + \frac{1}{2}O_2 \longrightarrow H_2O}$ $K_3$
The equilibrium constant (K) of the reaction:
$\mathrm{2NH_3 + \frac{5}{2}O_2 \overset{K}{\rightleftharpoons} 2NO + 3H_2O}$, will be

- (1) $K_1K_3^3/K_2$
- **(2)** $K_2K_3^3/K_1$
- (3) $K_2K_3/K_1$
- (4) $K_2^3K_3/K_1$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (I) $\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$; $K_1 = \frac{[\mathrm{NH_3}]^2}{[\mathrm{N_2}][\mathrm{H_2}]^3}$
2. (II) $\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$; $K_2 = \frac{[\mathrm{NO}]^2}{[\mathrm{N_2}][\mathrm{O_2}]}$
3. (III) $\mathrm{H_2 + \frac{1}{2}O_2 \longrightarrow H_2O}$; $K_3 = \frac{[\mathrm{H_2O}]}{[\mathrm{H_2}][\mathrm{O_2}]^{1/2}}$
4. (II + $3 \times$ III – II) will give
5. $\mathrm{2NH_3 + \frac{5}{2}O_2 \overset{K}{\rightleftharpoons} 2NO + 3H_2O}$;
6. $\therefore\ K = K_2 \times K_3^3 / K_1$

**Solved independently** (answer withheld)

1. Reverse reaction 1: $\mathrm{2NH_3 \rightleftharpoons N_2 + 3H_2}$, constant $\frac{1}{K_1}$.
2. Keep reaction 2: $\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$, constant $K_2$.
3. Multiply reaction 3 by 3: $\mathrm{3H_2 + \frac{3}{2}O_2 \rightleftharpoons 3H_2O}$, constant $K_3^3$.
4. Add the three: $\mathrm{N_2}$ and $\mathrm{3H_2}$ cancel, $\mathrm{O_2}$ totals $1 + \frac{3}{2} = \frac{5}{2}$, giving $\mathrm{2NH_3 + \frac{5}{2}O_2 \rightleftharpoons 2NO + 3H_2O}$.
5. Constants multiply on adding reactions: $K = \frac{K_2 K_3^3}{K_1}$, which is option $2$.

**Subtopic:** Law of Chemical Equilibrium · **Difficulty:** hard (4 steps, 4 of 4 options live)

**Printed in the booklet** (page 19)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q086_82c3c036_27102026.png?v=82c3c036518e)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q086_d2209629_27102026.png?v=d22096291c04)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Adding reactions multiplies their equilibrium constants, reversing one inverts its constant, and multiplying a reaction by $n$ raises its constant to the $n$th power
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who assembles the target correctly, reversing the ammonia synthesis and adding the other two, but writes $K_3$ once instead of $K_3^3$ lands exactly on $K_2K_3/K_1$. Three $\mathrm{H_2O}$ are needed in the target, so reaction 3 is taken three times and its constant is cubed.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  This is the expression you get by inverting the wrong reaction, putting $K_2$ in the denominator and $K_1$ on top. $\mathrm{NH_3}$ sits on the left of the target and on the right of reaction 1, so it is reaction 1 that has to be run backwards and $K_1$ that goes below.
- **Why:** This question requires three given constants combined to match a target equation, demonstrated by the options being quotients of $K_1$, $K_2$ and $K_3$ carrying powers, '$K_2K_3^3/K_1$' against '$K_2K_3/K_1$'.
<!--/ecat-->

## Q87

Chemistry · organic · Amines

Which of the following reactions is appropriate for converting acetamide to methanamine?

- (1) Carbylamine reaction
- **(2)** Hoffmann hypobromamide reaction
- (3) Stephens reaction
- (4) Gabriels phthalimide synthesis

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{CH_3-\overset{\displaystyle O}{\overset{\|}{C}}-NH_2 + Br_2 + 4NaOH \xrightarrow{\Delta} CH_3-NH_2 + 2NaBr + Na_2CO_3 + 3H_2O}$
2. This is Hoffmann Bromamide reaction.

**Solved independently** (answer withheld)

1. Acetamide is $\mathrm{CH_3CONH_2}$ (2 carbons) and methanamine is $\mathrm{CH_3NH_2}$ (1 carbon), so the reaction must remove one carbon.
2. Hoffmann bromamide degradation: $\mathrm{CH_3CONH_2 + Br_2 + 4NaOH \rightarrow CH_3NH_2 + Na_2CO_3 + 2NaBr + 2H_2O}$, which gives exactly this product.
3. Carbylamine gives isocyanides, Stephens reduces nitriles to aldehydes, and Gabriel synthesis starts from an alkyl halide, so option $2$ is correct.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 20)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q087_68b910d0_27102026.png?v=68b910d0bc09)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q087_28801b19_27102026.png?v=28801b19d514)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Hoffmann bromamide degradation takes an amide to a primary amine with one carbon fewer
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Gabriel's synthesis is the other named route in the same chapter that delivers a clean primary amine, so a student filing the question under 'how to make a primary amine' reaches for it. It starts from phthalimide and an alkyl halide and keeps the carbon count, whereas acetamide to methanamine starts from an amide and loses a carbon.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Carbylamine is the other reaction a student stores next to 'primary amine', but it runs the other way: it consumes a primary amine with $\mathrm{CHCl_3}$ and $\mathrm{KOH}$ to give an isocyanide. It tests for the product the stem wants made.
- **Why:** This question requires the named reaction that performs a stated conversion, demonstrated by the stem 'appropriate for converting acetamide to methanamine' with four named reactions as the options.
<!--/ecat-->

## Q88

Chemistry · physical · Chemical Kinetics

Mechanism of a hypothetical reaction $\mathrm{X_2 + Y_2 \rightarrow 2XY}$ is given below : The overall order of the reaction will be

- **((i))** $\mathrm{X_2 \rightarrow X + X}$ (fast)
- **((ii))** $\mathrm{X + Y_2 \rightleftharpoons XY + Y}$ (slow)
- **((iii))** $\mathrm{X + Y \rightarrow XY}$ (fast)

- (1) $1$
- (2) $2$
- (3) $0$
- **(4)** $1.5$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The solution of this question is given by assuming step (i) to be reversible which is not given in question
2. Overall rate = Rate of slowest step (ii)
3. $= k[\mathrm{X}]\,[\mathrm{Y_2}]$ ...(1)
4. $k$ = rate constant of step (ii)
5. Assuming step (i) to be reversible, its equilibrium constant,
6. $k_{eq} = \frac{[\mathrm{X}]^2}{[\mathrm{X_2}]} \Rightarrow [\mathrm{X}] = k_{eq}^{\frac{1}{2}}[\mathrm{X_2}]^{\frac{1}{2}}$ ...(2)
7. Put (2) in (1)
8. Rate $= kk_{eq}^{\frac{1}{2}}[\mathrm{X_2}]^{\frac{1}{2}}[\mathrm{Y_2}]$
9. Overall order $= \frac{1}{2} + 1 = \frac{3}{2}$

**Solved independently** (answer withheld)

1. The slow step (ii) is rate-determining, so $\text{rate} = k[\mathrm{X}][\mathrm{Y_2}]$.
2. $\mathrm{X}$ is an intermediate formed in the fast step (i), treated as a pre-equilibrium: $K = \frac{[\mathrm{X}]^2}{[\mathrm{X_2}]}$.
3. So $[\mathrm{X}] = K^{1/2}[\mathrm{X_2}]^{1/2}$.
4. Substituting: $\text{rate} = kK^{1/2}[\mathrm{X_2}]^{1/2}[\mathrm{Y_2}]$.
5. Overall order $= \frac{1}{2} + 1 = 1.5$, which is option $4$.

**Subtopic:** Order of a Reaction · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 20)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q088_81c7b568_27102026.png?v=81c7b5681f8f)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q088_f9d916d4_27102026.png?v=f9d916d4092c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The slow step fixes the rate law, but an intermediate in it must first be replaced using the fast equilibrium before the exponents are added
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Read the rate straight off the slow step as $k[X][Y_2]$ and the exponents add to $1+1=2$, which is where a student stops who treats the intermediate $X$ as an ordinary reactant whose concentration is known. $X$ comes from the fast equilibrium $\mathrm{X_2 \rightleftharpoons 2X}$, so $[X] \propto [X_2]^{1/2}$ and the order is $\tfrac{1}{2} + 1 = 1.5$.
- **Why:** This question requires a rate law built from the printed mechanism and its exponents summed, demonstrated by step (ii) '$\mathrm{X + Y_2 \rightleftharpoons XY + Y}$ (slow)' carrying the intermediate $X$ that step (i) '$\mathrm{X_2 \rightarrow X + X}$ (fast)' supplies.
- **Note:** The three lettered items are the steps of a mechanism, not claims to be judged, and the answer wanted is a single number rather than a combination of them.
<!--/ecat-->

## Q89

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

The IUPAC name of the compound [figure] is ________.

![printed figure: (E)-2-methyl-3-oxohex-4-enal](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q089_d5ab0371_27102026.svg?v=d5ab0371bedc)

*(E)-2-methyl-3-oxohex-4-enal*

![drawn: (E)-2-methyl-3-oxohex-4-enal](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q089_question_375a179f_27102026.svg?v=375a179fdd86)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: (E)-2-methyl-3-oxohex-4-enal `C/C=C/C(=O)C(C)C=O` ![(E)-2-methyl-3-oxohex-4-enal](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q089_question_s1_49ab0e2a_27102026.svg?v=49ab0e2a91dd)

- **(1)** 3-keto-2-methylhex-4-enal
- (2) 5-formylhex-2-en-3-one
- (3) 5-methyl-4-oxohex-2-en-5-al
- (4) 3-keto-2-methylhex-5-enal

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: (E)-2-methyl-3-oxohex-4-enal with locants printed beside the carbons: 1 (methyl branch), 2, 3 (C=O), 4, 5, 6](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q089_sol_1_17a5c9c2_27102026.svg?v=17a5c9c22c65)

*(E)-2-methyl-3-oxohex-4-enal with locants printed beside the carbons: 1 (methyl branch), 2, 3 (C=O), 4, 5, 6*

![drawn: (E)-2-methyl-3-oxohex-4-enal with locants printed beside the carbons: 1 (methyl branch), 2, 3 (C=O), 4, 5, 6](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_drawn/q089_solution_1_8c103844_27102026.svg?v=8c1038442ec5)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Aldehydes get higher priority over ketone and alkene in numbering of principal C-chain.
2. $\therefore$ 3-keto-2-methylhex-4-enal

**Solved independently** (answer withheld)

1. The figure shows $\mathrm{OHC{-}CH(CH_3){-}CO{-}CH{=}CH{-}CH_3}$.
2. The aldehyde $\mathrm{-CHO}$ is the principal group, so it is $C1$ and the suffix is $-al$.
3. The longest chain containing $C1$ and the $C{=}C$ has six carbons: hex.
4. Numbering from $C1$: methyl at $C2$, ketone ($\mathrm{oxo}$/keto) at $C3$, double bond $C4{=}C5$.
5. Name: $2$-methyl-$3$-oxohex-$4$-enal, written in the options as 3-keto-2-methylhex-4-enal, option $1$.

**Subtopic:** Nomenclature of Organic Compounds Having Functional Group(s) · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 20)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q089_0afad01b_27102026.png?v=0afad01b9645)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q089_800a6c85_27102026.png?v=800a6c858ff5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Naming a chain carrying both an aldehyde and a ketone: the aldehyde is senior, so it takes C1 and the suffix, the ketone becomes an oxo prefix, and a double bond is numbered from the lower of its two carbons
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Chain length, the methyl at C2, the ketone at C3 and the -al suffix are all right here, and only the alkene locant differs from the key. The double bond joins C4 and C5, and a student who quotes the far carbon of the pair writes hex-5-enal where the rule takes the lower one, hex-4-enal.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  This is the name you build if the ketone is made the principal group and the aldehyde demoted to a 'formyl' prefix, which is the seniority order the wrong way round. The aldehyde outranks the ketone, so the suffix must be -al and the ketone drops to a prefix.
- **Why:** This question requires the naming conventions applied to the drawn chain, demonstrated by three options naming the same skeleton and differing only in which group takes the suffix and where the locants fall, '3-keto-2-methylhex-4-enal' against '5-formylhex-2-en-3-one'.
- **Note:** The keyed name uses the older 'keto' prefix; written strictly the drawn compound is 2-methyl-3-oxohex-4-enal. Option 1 is still the only option with the right chain, suffix and locants.
<!--/ecat-->

## Q90

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Extraction of gold and silver involves leaching with $\mathrm{CN^{-}}$ ion. Silver is later recovered by

- (1) Liquation
- (2) Distillation
- (3) Zone refining
- **(4)** Displacement with $\mathrm{Zn}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{Zn}$ being more reactive than $\mathrm{Ag}$ and $\mathrm{Au}$, displaces them.
2. From Native ore,
3. $\mathrm{4Ag + 8NaCN + 2H_2O + O_2} \xrightarrow{\text{Leaching}} \underset{\substack{\text{Soluble}\\ \text{Sodium dicyanoargentate(I)}}}{\mathrm{4Na[Ag(CN)_2]}} + \mathrm{4NaOH}$
4. $\mathrm{2Na[Ag(CN)_2] + Zn} \xrightarrow{\text{Displacement}} \mathrm{Na_2[Zn(CN)_4] + 2Ag}\downarrow$

**Solved independently** (answer withheld)

1. Leaching: $4\mathrm{Ag} + 8\mathrm{CN^-} + 2\mathrm{H_2O} + \mathrm{O_2} \rightarrow 4[\mathrm{Ag(CN)_2}]^- + 4\mathrm{OH^-}$ puts silver into solution as a cyanide complex.
2. Zinc is more electropositive than silver, so it reduces the complex: $2[\mathrm{Ag(CN)_2}]^- + \mathrm{Zn} \rightarrow [\mathrm{Zn(CN)_4}]^{2-} + 2\mathrm{Ag}$.
3. So silver is recovered by displacement with $\mathrm{Zn}$, which is option $4$.

**Subtopic:** Refining of Metals · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 20)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q090_9a2f7f52_27102026.png?v=9a2f7f523a15)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q090_d73c2e6f_27102026.png?v=d73c2e6f75bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the cyanide process silver stays in solution as $\mathrm{[Ag(CN)_2]^-}$ and is dropped out by a more electropositive metal, zinc
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The other three are refining methods for a metal already in hand - distillation for volatile zinc and mercury, liquation for a low-melting metal run down a sloping hearth, zone refining for semiconductors such as silicon and germanium. The silver in this stem is still dissolved as a cyanide complex, so none of the three is a route to it and none competes with displacement by zinc.
- **Why:** This question requires the stated next step of a named extraction process, demonstrated by the stem 'Extraction of gold and silver involves leaching with $\mathrm{CN^{-}}$ ion. Silver is later recovered by'.
<!--/ecat-->

## Q91

Biology · botany · Sexual Reproduction in Flowering Plants

Double fertilization is exhibited by

- (1) Gymnosperms
- (2) Algae
- (3) Fungi
- **(4)** Angiosperms

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Double fertilization is a characteristic feature exhibited by angiosperms.
2. It involves syngamy and triple fusion.

**Solved independently** (answer withheld)

1. Double fertilization means two fusions in the embryo sac: syngamy (male gamete $+$ egg $\rightarrow$ $2n$ zygote) and triple fusion (male gamete $+$ two polar nuclei $\rightarrow$ $3n$ primary endosperm nucleus); this occurs only in angiosperms, which is option $4$.

**Subtopic:** Double Fertilisation · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q091_f1bc6cd9_27102026.png?v=f1bc6cd91c26)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q091_6ab9f0e5_27102026.png?v=6ab9f0e56dc5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Double fertilisation: syngamy plus triple fusion inside the embryo sac, an event unique to angiosperms.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Gymnosperms are the other seed-bearing group, and a student who remembers only that the egg is fertilised inside an ovule in both reaches for them. Gymnosperms have no central cell with two polar nuclei, so the second fusion that makes the endosperm never happens.
- **Why:** This question requires the NCERT line that double fertilisation occurs only in flowering plants, demonstrated by the stem 'Double fertilization is exhibited by' and four whole plant groups as options with nothing in the stem to work from.
- **NCERT:** “Since two types of fusions, syngamy and triple fusion take place in an embryo sac the phenomenon is termed double fertilisation, an event unique to flowering plants.”  
  *sexual reproduction in flowering plants, page 18*
<!--/ecat-->

## Q92

Biology · botany · Biological Classification

Which of the following are found in extreme saline conditions?

- **(1)** Archaebacteria
- (2) Eubacteria
- (3) Cyanobacteria
- (4) Mycobacteria

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Archaebacteria are able to survive in harsh conditions because of branched lipid chain in cell membrane which reduces fluidity of cell membrane.
2. Halophiles are exclusively found in saline habitats.

**Solved independently** (answer withheld)

1. Organisms found in extreme saline conditions are halophiles, and halophiles are a group of archaebacteria, so the answer is option $1$.

**Subtopic:** Archaebacteria & Mycoplasma · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q092_eec70bb3_27102026.png?v=eec70bb36d60)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q092_9a8e55c8_27102026.png?v=9a8e55c8dd27)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Archaebacteria live in the harshest habitats - salty areas, hot springs, marshes - and their different cell wall is what lets them.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Cyanobacteria are the bacteria a student meets in the odd habitats - marine water, bare rock, hot springs - so the word 'extreme' points at them. The halophiles NCERT names for salty areas are archaebacteria, and the cell wall structure that permits it is theirs, not the cyanobacterial one.
- **Why:** This question requires the NCERT placement of halophiles inside archaebacteria, demonstrated by the stem asking which organisms are 'found in extreme saline conditions' and by all four options being bare group names.
- **NCERT:** “These bacteria are special since they live in some of the most harsh habitats such as extreme salty areas (halophiles), hot springs (thermoacidophiles) and marshy areas (methanogens).”  
  *biological classification, page 13*
<!--/ecat-->

## Q93

Biology · botany · Mineral Nutrition

Select the mismatch :

- (1) Frankia – Alnus
- **(2)** Rhodospirillum – Mycorrhiza
- (3) Anabaena – Nitrogen fixer
- (4) Rhizobium – Alfalfa

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rhodospirillum is anaerobic, free living nitrogen fixer.
2. Mycorrhiza is a symbiotic relationship between fungi and roots of higher plants.

**Solved independently** (answer withheld)

1. Frankia forms N$_2$-fixing root nodules on non-leguminous Alnus, Anabaena is a cyanobacterial N$_2$ fixer and Rhizobium nodulates the legume alfalfa, so options $1$, $3$ and $4$ match; Rhodospirillum is a free-living anaerobic N$_2$-fixing bacterium, not a mycorrhizal fungus, so option $2$ is the mismatch.

**Subtopic:** Nitrogen Fixation · **Difficulty:** hard (4 steps, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q093_1fcbac7c_27102026.png?v=1fcbac7c0112)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q093_d2f07f96_27102026.png?v=d2f07f9694ba)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Nitrogen-fixing microbes and their partners: Rhizobium with legumes, Frankia with Alnus, Anabaena and Rhodospirillum free-living.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The stem asks for the pair that fails, and a student who reads 'mismatch' as 'match' then hunts for the pairing they can confirm lands on 'Rhizobium - Alfalfa', the standard legume nodulation example. It is a true pairing, which is exactly why it cannot be the answer.
- **Why:** This question requires judging organism-to-partner pairings and reporting the one that fails, demonstrated by the stem 'Select the mismatch :' and by each option being printed as a pair such as 'Rhodospirillum - Mycorrhiza'.
<!--/ecat-->

## Q94

Biology · both · Biotechnology: Principles and Processes

What is the criterion for DNA fragments movement on agarose gel during gel electrophoresis?

- (1) The larger the fragment size, the farther it moves
- **(2)** The smaller the fragment size, the farther it moves
- (3) Positively charged fragments move to farther end
- (4) Negatively charged fragments do not move

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. During gel electrophoresis, DNA fragments separate (resolve) according to their size through sieving effect provided by agarose gel.

**Solved independently** (answer withheld)

1. DNA is negatively charged, so all fragments move toward the anode; the agarose matrix sieves them by size, so the smaller the fragment, the farther it moves, which is option $2$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q094_5347f889_27102026.png?v=5347f889fb38)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q094_6ac4f1a5_27102026.png?v=6ac4f1a55627)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Gel electrophoresis separates DNA by size: the agarose mesh sieves, so smaller fragments travel farther from the well.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who holds only 'electrophoresis separates DNA by size' and pictures the bigger fragment as carrying more charge and so being pulled harder reads the relation backwards. The agarose mesh sieves, so the larger the fragment the sooner it is held up.
- **Why:** This question requires the separation principle of agarose gel electrophoresis, demonstrated by the stem asking for 'the criterion for DNA fragments movement' and by options 1 and 2 printing the same size rule in opposite directions.
- **NCERT:** “Hence, the smaller the fragment size, the farther it moves.”  
  *biotechnology principles and processes, page 168*
- **Note:** negative_words_seen lists NOT, but that NOT sits inside option 4 ('Negatively charged fragments do not move'); the task itself is direct.
<!--/ecat-->

## Q95

Biology · botany · Sexual Reproduction in Flowering Plants

Attractants and rewards are required for

- (1) Anemophily
- **(2)** Entomophily
- (3) Hydrophily
- (4) Cleistogamy

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Insect pollinated plants provide rewards as edible pollen grain and nectar as usual rewards.
2. While some plants also provide safe place for deposition of eggs.

**Solved independently** (answer withheld)

1. Attractants (colour, fragrance) and rewards (nectar, pollen) are needed only when a living pollinator must be drawn to the flower, i.e. in entomophily, which is option $2$; anemophily, hydrophily and cleistogamy need no pollinator visits.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q095_540aaac5_27102026.png?v=540aaac5d1f7)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q095_3d5eb539_27102026.png?v=3d5eb53924ed)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Entomophily: insect-pollinated flowers advertise with colour and scent and pay the visitor with nectar and pollen.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who turns 'rewards' into 'what the plant spends on pollination' reaches for anemophily, the mode remembered for releasing enormous quantities of pollen. Wind takes no payment - attractants and nectar exist only where an animal visitor has to be drawn in and kept returning.
- **Why:** This question requires the NCERT fact that floral rewards are offered to animal pollinators, demonstrated by the stem 'Attractants and rewards are required for' and by the four options being named pollination modes.
- **NCERT:** “Majority of insect-pollinated flowers are large, colourful, fragrant and rich in nectar.”  
  *sexual reproduction in flowering plants, page 14*
<!--/ecat-->

## Q96

Biology · botany · Anatomy of Flowering Plants

Which of the following is made up of dead cells?

- (1) Xylem parenchyma
- (2) Collenchyma
- **(3)** Phellem
- (4) Phloem

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Cork cambium undergoes periclinal division and cuts off thick walled suberised dead cork cells towards outside and it cuts off thin walled living cells i.e., phelloderm on inner side.

**Solved independently** (answer withheld)

1. Phellem (cork) cells are dead at maturity, with suberin-deposited walls, whereas xylem parenchyma, collenchyma and phloem are living, so the answer is option $3$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q096_4026d3d6_27102026.png?v=4026d3d65e75)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q096_fde2b52f_27102026.png?v=fde2b52f6e96)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tissues dead at maturity: phellem (cork), tracheids, vessels and fibres, as against living parenchyma, collenchyma and phloem.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Xylem is dead at maturity' is the line a student carries, and option 1 is the one that puts the word xylem in front of them. Xylem parenchyma is the single living element of xylem - the dead elements are the tracheids, vessels and fibres - while phellem is dead at maturity.
- **Why:** This question requires knowing which mature tissue consists of dead cells, demonstrated by the stem 'Which of the following is made up of dead cells?' and by the options naming four tissues whose living status is the only thing that separates them.
<!--/ecat-->

## Q97

Biology · zoology · Digestion and Absorption

Which cells of 'Crypts of Lieberkuhn' secrete antibacterial lysozyme?

- (1) Argentaffin cells
- **(2)** Paneth cells
- (3) Zymogen cells
- (4) Kupffer cells

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Kupffer-cells are phagocytic cells of liver.
2. Zymogen cells are enzyme producing cells.
3. Paneth cell secretes lysozyme which acts as anti-bacterial agent.
4. Argentaffin cells are hormone producing cells.

**Solved independently** (answer withheld)

1. Paneth cells, at the base of the intestinal Crypts of Lieberk$\ddot{u}$hn, secrete the antibacterial enzyme lysozyme, so the answer is option $2$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q097_e4228585_27102026.png?v=e4228585176c)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q097_6289ee2b_27102026.png?v=6289ee2bb698)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cell types of the crypts of Lieberkuhn and what each one secretes: Paneth cells make the antibacterial lysozyme.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Argentaffin cells sit in the crypts of Lieberkuhn too, so a student who has only the word 'crypts' linked to a cell name reaches for them. They are the hormone-secreting cells of the crypt; the lysozyme comes from the Paneth cells.
- **Why:** This question requires one stored cell-to-secretion association, demonstrated by the stem supplying the function -- 'secrete antibacterial lysozyme' -- and the four options being cell names.
<!--/ecat-->

## Q98

Biology · zoology · Body Fluids and Circulation

Adult human RBCs are enucleate. Which of the following statement(s) is/are most appropriate explanation for this feature?

- **(a)** They do not need to reproduce
- **(b)** They are somatic cells
- **(c)** They do not metabolize
- **(d)** All their internal space is available for oxygen transport

- **(1)** Only (d)
- (2) Only (a)
- (3) (a), (c) and (d)
- (4) (b) and (c)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In Human RBCs, nucleus degenerates during maturation which provide more space for oxygen carrying pigment (Haemoglobin).
2. It lacks most of the cell organelles including mitochondria so respires anaerobically.

**Solved independently** (answer withheld)

1. Mature mammalian RBCs lose their nucleus so the whole cell interior can be packed with haemoglobin, which raises oxygen-carrying capacity. Statement (c) is false because RBCs still metabolize anaerobically, and (a) and (b) do not explain the feature, so the answer is Only (d), option $1$.

**Subtopic:** Formed Elements And Their Types · **Difficulty:** hard (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q098_0e88e491_27102026.png?v=0e88e4911cd7)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q098_cd9139dc_27102026.png?v=cd9139dc913f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Why mammalian red blood cells shed the nucleus: the whole interior is freed for haemoglobin and oxygen carriage
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A cell with no nucleus cannot divide, so (a) 'They do not need to reproduce' reads like the reason for enucleation rather than its consequence, and RBCs having no mitochondria makes (c) 'They do not metabolize' sound safe. Bundling both with the true (d) gives option 3, but RBCs do metabolize glucose anaerobically.
- **Why:** This question requires judging which statement explains the feature rather than merely following from it, demonstrated by the stem asking for the 'most appropriate explanation for this feature' and by (d) 'All their internal space is available for oxygen transport' being the only statement that gives a purpose.
- **NCERT:** “RBCs are devoid of nucleus in most of the mammals and are biconcave in shape. They have a red coloured, iron containing complex protein called haemoglobin, hence the colour and name of these cells. A healthy individual has 12-16 gms of haemoglobin in every 100 ml of blood. These molecules play a significant role in transport of respiratory gases.”  
  *body fluids and circulation, page 194*
<!--/ecat-->

## Q99

Biology · zoology · Body Fluids and Circulation

The hepatic portal vein drains blood to liver from

- (1) Heart
- (2) Stomach
- (3) Kidneys
- **(4)** Intestine

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In hepatic portal system, hepatic portal vein carries maximum amount of nutrients from intestine to liver.

**Solved independently** (answer withheld)

1. The hepatic portal vein carries absorbed nutrient-rich blood from the intestine to the liver before it enters the systemic circulation, which is option $4$.

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 21)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q099_13dec28f_27102026.png?v=13dec28f87d4)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q099_92045740_27102026.png?v=92045740bf44)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hepatic portal system: the hepatic portal vein carries blood from the intestine to the liver before it goes on to the heart.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The stomach is the neighbouring part of the same gut and a student holding the loose form 'the portal vein collects blood from the gut' lands on it. The line the key follows ties the hepatic portal vein specifically to the intestine.
- **Why:** This question requires one stored anatomical fact about where a named vessel collects its blood, demonstrated by the stem 'The hepatic portal vein drains blood to liver from' followed by four organ names.
- **NCERT:** “The hepatic portal vein carries blood from intestine to the liver before it is delivered to the systemic circulation.”  
  *body fluids and circulation, page 201*
- **Note:** Option 2 is defensible on a straight anatomical reading, since the gastric veins also feed the hepatic portal vein; the key rests on the textbook sentence that the hepatic portal vein carries blood from the intestine to the liver. Tagged as printed, key not re-judged.
<!--/ecat-->

## Q100

Biology · both · Molecular Basis of Inheritance

The final proof for DNA as the genetic material came from the experiments of

- (1) Griffith
- **(2)** Hershey and Chase
- (3) Avery, Mcleod and McCarty
- (4) Hargobind Khorana

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Hershey and Chase gave unequivocal proof which ended the debate between protein and DNA as genetic material.

**Solved independently** (answer withheld)

1. Hershey and Chase (1952) labelled phage DNA with $^{32}\mathrm{P}$ and phage protein with $^{35}\mathrm{S}$; only $^{32}\mathrm{P}$ entered the bacteria, giving the unequivocal proof that DNA is the genetic material, which is option $2$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 22)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q100_8724cda3_27102026.png?v=8724cda36310)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q100_0d24d950_27102026.png?v=0d24d95039db)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hershey-Chase experiment: radioactively labelled bacteriophage showed that DNA, not protein, enters the bacterium, settling DNA as the genetic material.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Avery, MacLeod and McCarty did identify DNA as the transforming principle, so a student who remembers that experiment answers with their names. The stem asks for the FINAL proof, and their biochemical result still left room for protein contamination, which the labelled-phage work closed.
- **Why:** This question requires attaching one experiment to the workers who did it, demonstrated by the stem asking for 'the final proof for DNA as the genetic material' with four sets of names as options.
- **NCERT:** “The unequivocal proof that DNA is the genetic material came from the experiments of Alfred Hershey and Martha Chase (1952).”  
  *molecular basis of inheritance, page 85*
<!--/ecat-->

## Q101

Biology · botany · Biological Classification

Which among the following are the smallest living cells, known without a definite cell wall, pathogenic to plants as well as animals and can survive without oxygen?

- (1) Bacillus
- (2) Pseudomonas
- **(3)** Mycoplasma
- (4) Nostoc

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Mycoplasmas are smallest, wall-less prokaryotes, pleomorphic in nature.
2. These are pathogenic on both plants and animals.

**Solved independently** (answer withheld)

1. Mycoplasma are the smallest known living cells, have no cell wall, can survive without oxygen and cause diseases in plants and animals, so the answer is option $3$.

**Subtopic:** Archaebacteria & Mycoplasma · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 22)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q101_9fa05baf_27102026.png?v=9fa05baf525a)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q101_d8eb39b7_27102026.png?v=d8eb39b76b4f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mycoplasma: the smallest living cells, lacking a definite cell wall, pathogenic to plants and animals and able to survive without oxygen.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Pseudomonas really does infect both plants and animals, so a student who anchors on that one clause of the stem stops there. It has a definite cell wall and is nowhere near the smallest cell, and those are the two clauses that leave only Mycoplasma.
- **Why:** This question requires one organism recovered from a stack of diagnostic characters, demonstrated by the stem chaining 'smallest living cells', 'without a definite cell wall' and 'can survive without oxygen'.
- **NCERT:** “The Mycoplasma are organisms that completely lack a cell wall. They are the smallest living cells known and can survive without oxygen. Many mycoplasma are pathogenic in animals and plants.”  
  *biological classification, page 14*
<!--/ecat-->

## Q102

Biology · both · Cell Cycle and Cell Division

Which of the following options gives the correct sequence of events during mitosis?

- (1) Condensation $\rightarrow$ nuclear membrane disassembly $\rightarrow$ crossing over $\rightarrow$ segregation $\rightarrow$ telophase
- **(2)** Condensation $\rightarrow$ nuclear membrane disassembly $\rightarrow$ arrangement at equator $\rightarrow$ centromere division $\rightarrow$ segregation $\rightarrow$ telophase
- (3) Condensation $\rightarrow$ crossing over $\rightarrow$ nuclear membrane disassembly $\rightarrow$ segregation $\rightarrow$ telophase
- (4) Condensation $\rightarrow$ arrangement at equator $\rightarrow$ centromere division $\rightarrow$ segregation $\rightarrow$ telophase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The correct sequence of events during mitosis would be as follows
2. (i) Condensation of DNA so that chromosomes become visible occurs during early to mid-prophase.
3. (ii) Nuclear membrane disassembly begins at late prophase or transition to metaphase.
4. (iii) Arrangement of chromosomes at equator occurs during metaphase, called congression.
5. (iv) Centromere division or splitting occurs during anaphase forming daughter chromosomes.
6. (v) Segregation also occurs during anaphase as daughter chromosomes separate and move to opposite poles.
7. (vi) Telophase leads to formation of two daughter nuclei.

**Solved independently** (answer withheld)

1. Crossing over happens only in meiosis (pachytene), so options $1$ and $3$ are out; option $4$ leaves out nuclear membrane disassembly before the chromosomes align at the equator, so the full mitotic order condensation $\rightarrow$ nuclear membrane disassembly $\rightarrow$ arrangement at equator $\rightarrow$ centromere division $\rightarrow$ segregation $\rightarrow$ telophase is option $2$.

**Subtopic:** Prophase and Metaphase · **Difficulty:** hard (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 22)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q102_7164c67e_27102026.png?v=7164c67e3a3a)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q102_4409f2c4_27102026.png?v=4409f2c4e433)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Order of events in mitosis: chromosome condensation, nuclear membrane disassembly, arrangement at the equator, centromere division, segregation, telophase -- with no crossing over anywhere in it.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Every event in option 4 is a real mitotic event in the right order, so a student who screens the options only for the meiotic word 'crossing over' strikes out 1 and 3 and takes 4 as the clean sequence. It leaves out nuclear membrane disassembly, which has to happen before the chromosomes can line up at the equator.
- **Why:** This question requires the sequence of mitotic stages, demonstrated by the four options differing only in which events are listed and in what order they are printed.
- **NCERT:** “Mitosis is also divided into four stages namely prophase, metaphase, anaphase and telophase. Chromosome condensation occurs during prophase. Simultaneously, the centrioles move to the opposite poles. The nuclear envelope and the nucleolus disappear and the spindle fibres start appearing. Metaphase is marked by the alignment of chromosomes at the equatorial plate. During anaphase the centromeres divide and the chromatids start moving towards the two opposite poles. Once the chromatids reach the two poles, the chromosomal elongation starts, nucleolus and the nuclear membrane reappear. This stage is called the telophase.”  
  *cell cycle and cell division, page 129*
- **Note:** A second device sits on this set: options 1 and 3 insert 'crossing over', a meiotic event, into mitosis. It is spread across two options rather than landing on one, so the single recorded trap is the dominant one on option 4.
<!--/ecat-->

## Q103

Biology · both · Biomolecules

Which one of the following statements is correct, with reference to enzymes?

- (1) Apoenzyme $=$ Holoenzyme $+$ Coenzyme
- **(2)** Holoenzyme $=$ Apoenzyme $+$ Coenzyme
- (3) Coenzyme $=$ Apoenzyme $+$ Holoenzyme
- (4) Holoenzyme $=$ Coenzyme $+$ Cofactor

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Holoenzyme is conjugated enzyme in which protein part is apoenzyme while non-protein is cofactor.
2. Coenzyme are also organic compounds but their association with apoenzyme is only transient and serve as cofactors.

**Solved independently** (answer withheld)

1. The protein portion of a conjugated enzyme is the apoenzyme, and the organic non-protein part is the coenzyme; together they form the active holoenzyme, so $\text{Holoenzyme} = \text{Apoenzyme} + \text{Coenzyme}$, which is option $2$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 22)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q103_e660258a_27102026.png?v=e660258ad479)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q103_5c8021f8_27102026.png?v=5c8021f82e44)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Holoenzyme, apoenzyme and coenzyme: the catalytically active holoenzyme is the protein apoenzyme plus its non-protein coenzyme.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student who has the three names but not which of them is the complete enzyme reads the equation the other way round and makes the apoenzyme the sum. The apoenzyme is the protein part on its own; the whole active enzyme is the holoenzyme.
- **Why:** This question requires three neighbouring enzyme terms held apart, demonstrated by option 2 'Holoenzyme = Apoenzyme + Coenzyme' and option 1 printing the same three terms rearranged.
- **NCERT:** “However, there are a number of cases in which non-protein constituents called co-factors are bound to the the enzyme to make the enzyme catalytically active. In these instances, the protein portion of the enzymes is called the apoenzyme. Three kinds of cofactors may be identified: prosthetic groups, co-enzymes and metal ions.”  
  *biomolecules, page 117*
<!--/ecat-->

## Q104

Biology · both · Molecular Basis of Inheritance

During DNA replication, Okazaki fragments are used to elongate

- (1) The leading strand towards replication fork
- (2) The lagging strand towards replication fork
- (3) The leading strand away from replication fork
- **(4)** The lagging strand away from the replication fork

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Two DNA polymerase molecules work simultaneous at the DNA fork, one on the leading strand and the other on the lagging strand.
2. Each Okazaki fragment is synthesized by DNA polymerase at lagging strand in $5' \rightarrow 3'$ direction.
3. New Okazaki fragments appear as the replication fork opens further.
4. As the first Okazaki fragment appears away from the replication fork, the direction of elongation would be away from replication fork.

**Solved independently** (answer withheld)

1. Okazaki fragments are formed only on the lagging strand; the leading strand is synthesised continuously, which rules out options $1$ and $3$.
2. DNA polymerase adds nucleotides only in the $5' \rightarrow 3'$ direction, and on the lagging strand this direction points away from the replication fork.
3. So each Okazaki fragment elongates the lagging strand away from the replication fork, which is option $4$.

**Subtopic:** The Machinery and the Enzymes of Replication · **Difficulty:** hard (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 22)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q104_f36b2d57_27102026.png?v=f36b2d571ad0)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q104_9e083c7f_27102026.png?v=9e083c7f65f8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Okazaki fragments build the lagging strand, each short piece laid down 5'→3' and therefore pointing away from the advancing replication fork
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student who has stored only 'Okazaki fragments belong to the lagging strand' still has the direction to choose, and the fork's own forward movement supplies 'towards'. Synthesis runs 5'→3' only, so each fragment is laid down pointing back, away from the fork.
- **Why:** This question requires the stated fact of which strand Okazaki fragments elongate and in which direction, demonstrated by the four options crossing 'The leading strand' / 'The lagging strand' with 'towards replication fork' / 'away from the replication fork'.
- **NCERT:** “Consequently, on one strand (the template with polarity 3′→5′), the replication is continuous, while on the other (the template with polarity 5′→3′), it is discontinuous. The discontinuously synthesised fragments are later joined by the enzyme DNA ligase (Figure 5.8).”  
  *molecular basis of inheritance, page 90*
<!--/ecat-->

## Q105

Biology · both · Biomolecules

Which of the following are not polymeric?

- (1) Nucleic acids
- (2) Proteins
- (3) Polysaccharides
- **(4)** Lipids

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. – Nucleic acids are polymers of nucleotides
2. – Proteins are polymers of amino acids
3. – Polysaccharides are polymers of monosaccharides
4. – Lipids are the esters of fatty acids and alcohol

**Solved independently** (answer withheld)

1. Nucleic acids, proteins and polysaccharides are true biopolymers (of nucleotides, amino acids and monosaccharides); lipids have low molecular weight (below $800\,\text{Da}$), are not built from repeating monomers and appear in the acid-insoluble fraction only because they form membrane vesicles, so the answer is option $4$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 22)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q105_a0b6b27a_27102026.png?v=a0b6b27aab84)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q105_b65a6f60_27102026.png?v=b65a6f600fcd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nucleic acids, proteins and polysaccharides are polymers of repeating monomers; lipids are not polymeric, even though they turn up in the acid-insoluble fraction
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Nucleic acids, proteins and polysaccharides are the three polymers NCERT names in one line, and each is as plainly polymeric as the other two. Nothing marks one of them out as the option a particular mistake would land on.
- **Why:** This question requires the stated fact that lipids are not polymers, demonstrated by the stem 'Which of the following are not polymeric?' set against three classes whose polymer status NCERT gives in the same sentence.
- **NCERT:** “The molecules in the insoluble fraction with the exception of lipids are polymeric substances.”  
  *biomolecules, page 108*
<!--/ecat-->

## Q106

Biology · botany · Biodiversity and Conservation

The region of Biosphere Reserve which is legally protected and where no human activity is allowed is known as

- **(1)** Core zone
- (2) Buffer zone
- (3) Transition zone
- (4) Restoration zone

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Biosphere reserve is protected area with multipurpose activities.
2. It has three zones
3. (a) Core zone – without any human interference
4. (b) Buffer zone – with limited human activity
5. (c) Transition zone – human settlement, grazing cultivation etc., are allowed.

**Solved independently** (answer withheld)

1. A biosphere reserve has a legally protected $\text{core zone}$ with no human activity, surrounded by a $\text{buffer zone}$ (limited activity) and an outer $\text{transition zone}$ (human activity), so the answer is option $1$.

**Subtopic:** In Situ Conservation · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q106_91b20d67_27102026.png?v=91b20d67b31d)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q106_af612b37_27102026.png?v=af612b37599e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A biosphere reserve is zoned: an undisturbed core, a buffer where limited research and education are allowed, and a transition zone carrying human settlement
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The buffer zone's stated job is to shield the core, so a student who holds 'the buffer is the protective zone' reads the stem's 'legally protected' as describing it. The buffer still permits research, education and limited use; it is the core alone where no human activity is allowed.
- **Why:** This question requires the stated definition of the core zone, demonstrated by the stem 'legally protected and where no human activity is allowed' matched against four named zones.
<!--/ecat-->

## Q107

Biology · botany · Sexual Reproduction in Flowering Plants

A dioecious flowering plant prevents both:

- (1) Autogamy and xenogamy
- **(2)** Autogamy and geitonogamy
- (3) Geitonogamy and xenogamy
- (4) Cleistogamy and xenogamy

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. When unisexual male and female flowers are present on different plants the condition is called dioecious and it prevents both autogamy and geitonogamy.

**Solved independently** (answer withheld)

1. Dioecious means male and female flowers are on separate plants, so every flower is unisexual and no plant carries both sexes.
2. With no bisexual flowers and no female flowers on a male plant (or male flowers on a female plant), pollen cannot reach a stigma of the same flower (autogamy) or of another flower on the same plant (geitonogamy).
3. Only cross-pollination between different plants (xenogamy) is possible, so the plant prevents autogamy and geitonogamy, which is option $2$.

**Subtopic:** Outbreeding Devices · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q107_f1656ccf_27102026.png?v=f1656ccf9cde)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q107_16c17359_27102026.png?v=16c173594d45)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Dioecy puts male and female flowers on separate plants, which rules out selfing within a flower (autogamy) and selfing between two flowers of one plant (geitonogamy)
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Autogamy is the half anyone can fix, and the second term then has to separate geitonogamy from xenogamy. A student who has those two definitions the wrong way round, taking xenogamy as pollination between two flowers of the same plant, picks autogamy and xenogamy; true xenogamy, between separate plants, is exactly what dioecy forces.
- **Why:** This question requires the stated consequence of dioecy, demonstrated by the stem 'A dioecious flowering plant prevents both:' and options that each bundle two of autogamy, geitonogamy and xenogamy.
- **NCERT:** “In several species such as papaya, male and female flowers are present on different plants, that is each plant is either male or female (dioecy). This condition prevents both autogamy and geitonogamy.”  
  *sexual reproduction in flowering plants, page 15*
<!--/ecat-->

## Q108

Biology · zoology · Chemical Coordination and Integration

A temporary endocrine gland in the human body is

- (1) Pineal gland
- (2) Corpus cardiacum
- **(3)** Corpus luteum
- (4) Corpus allatum

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Corpus luteum is the temporary endocrine structure formed in the ovary after ovulation.
2. It is responsible for the release of the hormones like progesterone, oestrogen etc.

**Solved independently** (answer withheld)

1. The corpus luteum develops from the ruptured Graafian follicle after ovulation, secretes progesterone, and degenerates if no pregnancy follows, so it is a temporary human endocrine gland (option $3$).

**Subtopic:** Gonads · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q108_1f4fd1ea_27102026.png?v=1f4fd1eabb7d)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q108_359d8a4e_27102026.png?v=359d8a4ee56d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The corpus luteum forms from the ruptured follicle after ovulation and breaks down when pregnancy does not follow, so it is the one human endocrine gland with a fixed lifespan
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  A student who has stored 'the pineal regresses and calcifies with age' reads that as temporary and picks it. The pineal is present from birth and secretes melatonin lifelong, while the corpus luteum is built and dismantled inside a single cycle.
- **Also:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Corpus allatum is a real endocrine gland sharing the first word, so a student who has stored 'corpus something = endocrine gland' without storing the animal reaches for it. It is an insect gland, and the stem asks for one in the human body.
- **Why:** This question requires the stated fact that the corpus luteum is transient, demonstrated by the stem 'A temporary endocrine gland in the human body is' against three permanent glands, two of them insect.
- **NCERT:** “After ovulation, the ruptured follicle is converted to a structure called corpus luteum, which secretes mainly progesterone.”  
  *chemical coordination and integration, page 246*
<!--/ecat-->

## Q109

Biology · zoology · Reproductive Health

Match the following sexually transmitted diseases (Column - I) with their causative agent (Column - II) and select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| a | Gonorrhea | i | HIV |
| b | Syphilis | ii | Neisseria |
| c | Genital Warts | iii | Treponema |
| d | AIDS | iv | Human Papilloma virus |

- **(1)** (a) (ii), (b) (iii), (c) (iv), (d) (i)
- (2) (a) (iii), (b) (iv), (c) (i), (d) (ii)
- (3) (a) (iv), (b) (ii), (c) (iii), (d) (i)
- (4) (a) (iv), (b) (iii), (c) (ii), (d) (i)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Gonorrhoea – Neisseria (Bacteria)
2. Syphilis – Treponema (Bacteria)
3. Genital Warts – Human papilloma virus (Virus)
4. AIDS – HIV (Virus)

**Solved independently** (answer withheld)

1. Gonorrhea is caused by $Neisseria$ $gonorrhoeae$ (a-ii), syphilis by $Treponema$ $pallidum$ (b-iii), genital warts by Human Papilloma virus (c-iv) and AIDS by HIV (d-i), which is option $1$.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q109_8af8ddf8_27102026.png?v=8af8ddf806ac)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q109_7a8687f7_27102026.png?v=7a8687f7865a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Each sexually transmitted infection has one named causative agent: gonorrhoea to Neisseria, syphilis to Treponema, genital warts to human papilloma virus, AIDS to HIV
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student who has Treponema for syphilis and HIV for AIDS secure is left to place the other two agents, and option 4 is the key with exactly those two exchanged, gonorrhoea given 'Human Papilloma virus' and genital warts given 'Neisseria'. Column II prints the bare genus 'Neisseria' instead of Neisseria gonorrhoeae, so the one name that would have named its own disease no longer does.
- **Why:** This question requires the correct pairing of four diseases to four agents, demonstrated by the stem 'Match the following sexually transmitted diseases (Column - I) with their causative agent (Column - II)' and options that are four-pair codes.
<!--/ecat-->

## Q110

Biology · zoology · Human Health and Disease

Transplantation of tissues/organs fails often due to non-acceptance by the patient's body. Which type of immune-response is responsible for such rejections?

- (1) Autoimmune response
- **(2)** Cell-mediated immune response
- (3) Hormonal immune response
- (4) Physiological immune response

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Non-acceptance or rejection of graft or transplanted tissues/organs is due to cell mediated immune response.

**Solved independently** (answer withheld)

1. The body tells self from non-self, and T-lymphocytes attack the transplanted (non-self) tissue, so the rejection is a cell-mediated immune response, which is option $2$.

**Subtopic:** Acquired Immunity · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q110_63e6e87e_27102026.png?v=63e6e87e5962)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q110_b7fbe639_27102026.png?v=b7fbe6391472)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Graft rejection is carried out by T lymphocytes recognising donor tissue as non-self: cell-mediated immunity, not antibodies
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The stem's 'non-acceptance by the patient's body' reads like the body turning on tissue sitting inside it, so a student holding 'immune attack on tissue in my own body = autoimmunity' picks the autoimmune response. Autoimmunity is an attack on self antigens; a graft carries non-self antigens that T cells read as foreign.
- **Why:** This question requires the reason NCERT gives for graft rejection, demonstrated by the stem 'Which type of immune-response is responsible for such rejections?'.
- **NCERT:** “The body is able to differentiate ‘self ’ and ‘nonself’ and the cell-mediated immune response is responsible for the graft rejection.”  
  *human health and disease, page 135*
<!--/ecat-->

## Q111

Biology · both · Molecular Basis of Inheritance

Spliceosomes are not found in cells of

- (1) Plants
- (2) Fungi
- (3) Animals
- **(4)** Bacteria

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Spliceosomes are used in removal of introns during post-transcriptional processing of hnRNA in eukaryotes only as split genes are absent as prokaryotes.

**Solved independently** (answer withheld)

1. Spliceosomes splice introns out of eukaryotic pre-mRNA; plants, fungi and animals are eukaryotes, while bacteria are prokaryotes with no split genes, so spliceosomes are absent in bacteria (option $4$).

**Subtopic:** Transcription · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q111_bc97f317_27102026.png?v=bc97f3178ae8)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q111_381fd611_27102026.png?v=381fd6113b54)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Splicing of hnRNA happens in the eukaryotic nucleus, so the spliceosome exists only in eukaryotes; bacteria have no nucleus and no introns in their protein-coding genes
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Plants, fungi and animals are all eukaryotes and carry spliceosomes for exactly the same reason, so the three wrong options are interchangeable and none is the landing point of a particular confusion.
- **Why:** This question requires the stated fact that spliceosomes are eukaryotic, demonstrated by the stem 'Spliceosomes are not found in cells of' set against three eukaryotic kingdoms and one prokaryote.
- **NCERT:** “In bacteria, since the mRNA does not require any processing to become active, and also since transcription and translation take place in the same compartment (there is no separation of cytosol and nucleus in bacteria), many times the translation can begin much before the mRNA is fully transcribed.”  
  *molecular basis of inheritance, page 94*
<!--/ecat-->

## Q112

Biology · botany · Plant Kingdom

An example of colonial alga is

- (1) Chlorella
- **(2)** Volvox
- (3) Ulothrix
- (4) Spirogyra

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Volvox is motile colonial fresh water alga with definite number of vegetative cells.

**Solved independently** (answer withheld)

1. Volvox forms a colony of flagellated cells, whereas Chlorella is unicellular and Ulothrix and Spirogyra are filamentous, so the answer is option $2$.

**Subtopic:** Algae · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q112_9d5d6f99_27102026.png?v=9d5d6f996715)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q112_33922e80_27102026.png?v=33922e803f29)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Green algae differ in body form: Chlorella is unicellular, Ulothrix and Spirogyra are filamentous, Volvox is a motile colony of cells
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four are green algae from the same NCERT paragraph and no part of a name carries the body form, so the question is settled by one stored habit. Ulothrix and Spirogyra are both filamentous, so a student who confuses a filament with a colony has no single option to land on.
- **Why:** This question requires the stated example of a colonial alga, demonstrated by the stem 'An example of colonial alga is' followed by four named green algae of the same class.
- **NCERT:** “The form and size of algae is highly variable, ranging from colonial forms like Volvox and the filamentous forms like Ulothrix and Spirogyra (Figure 3.1).”  
  *plant kingdom, page 24*
<!--/ecat-->

## Q113

Biology · zoology · The Living World

Which of the following represents order of 'Horse'?

- (1) Equidae
- **(2)** Perissodactyla
- (3) Caballus
- (4) Ferus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Horse belongs to order perissodactyla of class mammalia.
2. Perissodactyla includes odd-toed mammals.

**Solved independently** (answer withheld)

1. The horse is classified as order Perissodactyla, family Equidae, genus $Equus$, species $caballus$ (subspecies of $ferus$), so the order is Perissodactyla, which is option $2$.

**Subtopic:** Order and Class · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q113_78f4c8fa_27102026.png?v=78f4c8fa5fb7)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q113_113280a8_27102026.png?v=113280a869a3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each taxonomic rank has its own name and its own ending: Equidae is the horse's family, Perissodactyla the order, and caballus the species epithet
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Equidae is the horse's real higher taxon, so a student who has stored one Latin group name for the horse without storing which rank it sits at offers it. The '-idae' ending marks a family, and the stem asked for the order.
- **Why:** This question requires the stated rank the horse occupies, demonstrated by the stem 'Which of the following represents order of Horse?' with a family name and two species-level names printed beside the order.
<!--/ecat-->

## Q114

Biology · both · Cell: The Unit of Life

Which of the following cell organelles is responsible for extracting energy from carbohydrates to form ATP?

- (1) Lysosome
- (2) Ribosome
- (3) Chloroplast
- **(4)** Mitochondrion

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Mitochondria are the site of aerobic oxidation of carbohydrates to generate ATP.

**Solved independently** (answer withheld)

1. Mitochondria carry out aerobic respiration (Krebs cycle and oxidative phosphorylation), oxidising carbohydrate-derived substrates to produce ATP, so the answer is option $4$ (Mitochondrion).

**Subtopic:** Mitochondria · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 23)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q114_d6cd5856_27102026.png?v=d6cd58564809)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q114_0391b880_27102026.png?v=0391b8804e71)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mitochondria run aerobic respiration: they oxidise carbohydrate and trap the energy released as ATP
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Chloroplasts do make ATP, so a student whose stored line is 'the chloroplast is the ATP-producing organelle' finds the stem's 'to form ATP' answered there. Chloroplast ATP comes from light and is spent building carbohydrate; extracting the energy back out of carbohydrate is the mitochondrion's work.
- **Why:** This question requires the stated function of the mitochondrion, demonstrated by the stem 'responsible for extracting energy from carbohydrates to form ATP' against four named organelles.
- **NCERT:** “Mitochondria are the sites of aerobic respiration. They produce cellular energy in the form of ATP, hence they are called ‘power houses’ of the cell.”  
  *cell the unit of life, page 96*
<!--/ecat-->

## Q115

Biology · both · Biotechnology: Principles and Processes

The process of separation and purification of expressed protein before marketing is called

- (1) Upstream processing
- **(2)** Downstream processing
- (3) Bioprocessing
- (4) Postproduction processing

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Biosynthetic stage for synthesis of product in recombinant DNA technology is called upstreaming process while after completion of biosynthetic stage, the product has to be subjected through a series of processes which include separation and purification are collectively referred to as downstreaming processing.

**Solved independently** (answer withheld)

1. After the protein is made in the bioreactor, its separation and purification (with formulation and quality testing) before marketing is called downstream processing, which is option $2$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q115_3efec3b5_27102026.png?v=3efec3b5ba64)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q115_c703860a_27102026.png?v=c703860a77db)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A bioprocess splits into upstream work before the product exists and downstream recovery afterwards: separation, purification and formulation of the expressed protein
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Upstream and downstream name the two halves of one production line, so a student who holds the pair but not which end is which takes the term that comes first in the taught sequence. Upstream processing is the medium, the inoculum and the fermentation; separating and purifying an expressed protein happens after all of that.
- **Why:** This question requires the stated definition of downstream processing, demonstrated by the stem 'separation and purification of expressed protein before marketing' against the named pair upstream / downstream.
- **NCERT:** “The processes include separation and purification, which are collectively referred to as downstream processing.”  
  *biotechnology principles and processes, page 174*
<!--/ecat-->

## Q116

Biology · botany · Organisms and Populations

Mycorrhizae are the example of

- (1) Fungistasis
- (2) Amensalism
- (3) Antibiosis
- **(4)** Mutualism

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Mycorrhizae is a symbiotic association of fungi with roots of higher plants.

**Solved independently** (answer withheld)

1. Mycorrhiza is a symbiotic association between a fungus and plant roots in which the fungus helps absorb phosphorus and water and the plant supplies carbohydrates, so both benefit ($+/+$), which is mutualism, option $4$.

**Subtopic:** Mutualism · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q116_a6d1c7f7_27102026.png?v=a6d1c7f74eeb)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q116_a210ec19_27102026.png?v=a210ec190875)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mycorrhiza is a fungus living on roots where the fungus absorbs minerals for the plant and the plant feeds it sugars, so both partners gain: mutualism
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Fungistasis and antibiosis name the suppression of one organism by another rather than a category of population interaction, and amensalism needs one partner harmed, which nothing in 'Mycorrhizae' supplies. No single one of the three is where a particular mistake arrives.
- **Why:** This question requires the stated interaction mycorrhizae exemplify, demonstrated by the stem 'Mycorrhizae are the example of' followed by four interaction terms.
- **NCERT:** “Similarly, the mycorrhizae are associations between fungi and the roots of higher plants. The fungi help the plant in the absorption of essential nutrients from the soil while the plant in turn provides the fungi with energy-yielding carbohydrates.”  
  *organisms and populations, page 201*
<!--/ecat-->

## Q117

Biology · botany · Biological Classification

Viroids differ from viruses in having :

- (1) DNA molecules with protein coat
- (2) DNA molecules without protein coat
- (3) RNA molecules with protein coat
- **(4)** RNA molecules without protein coat

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Viroids are sub-viral agents as infectious RNA particles, without protein coat.

**Solved independently** (answer withheld)

1. Viroids are infectious agents made of free RNA with no protein coat (capsid), unlike viruses, which have a protein coat, so the answer is option $4$.

**Subtopic:** Viroids, Prions & Lichens · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q117_372536dd_27102026.png?v=372536dd0f81)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q117_1e5acd9f_27102026.png?v=1e5acd9f14a8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A viroid is naked infectious RNA of low molecular weight; what separates it from a virus is the missing protein coat, not the kind of nucleic acid
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who stores the difference as a nucleic-acid difference -- 'viruses are DNA, viroids are RNA' -- keeps the coat and picks RNA with a protein coat. Viruses can be RNA too, so the coat is the half that actually does the separating.
- **Why:** This question requires the stated difference between viroids and viruses, demonstrated by the four options crossing 'DNA molecules' / 'RNA molecules' with 'with protein coat' / 'without protein coat'.
- **NCERT:** “It was found to be a free RNA; it lacked the protein coat that is found in viruses, hence the name viroid.”  
  *biological classification, page 21*
<!--/ecat-->

## Q118

Biology · botany · Morphology of Flowering Plants

Root hairs develop from the region of

- **(1)** Maturation
- (2) Elongation
- (3) Root cap
- (4) Meristematic activity

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In roots, the root hairs arise from zone of maturation.
2. This zone is differentiated zone thus bearing root hairs.

**Solved independently** (answer withheld)

1. Behind the root cap come the region of meristematic activity and then the region of elongation. Cells of the region of elongation gradually differentiate and mature, forming the region of maturation, and root hairs grow from epidermal cells of this region, so the answer is option $1$.

**Subtopic:** The Root · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q118_4c44d9e2_27102026.png?v=4c44d9e2ff79)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q118_0b3a87ab_27102026.png?v=0b3a87abec0c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A root is zoned from the tip upwards -- root cap, meristem, elongation, maturation -- and root hairs are the outgrowths of the maturation region
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The elongation region is the immediate neighbour below, so a student who stores 'root hairs appear just behind the growing tip' stops one zone short. Cells differentiate only after they have finished elongating, and the hairs belong to the maturation region above it.
- **Why:** This question requires the stated region that bears root hairs, demonstrated by the stem 'Root hairs develop from the region of' against the named root regions.
- **NCERT:** “Hence, this zone, proximal to region of elongation, is called the region of maturation. From this region some of the epidermal cells form very fine and delicate, thread-like structures called root hairs.”  
  *morphology of flowering plants, page 59*
<!--/ecat-->

## Q119

Biology · botany · Morphology of Flowering Plants

Coconut fruit is a

- **(1)** Drupe
- (2) Berry
- (3) Nut
- (4) Capsule

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Coconut fruit is a drupe.
2. A drupe develops from monocarpellary superior ovary and are one seeded.

**Solved independently** (answer withheld)

1. Coconut has a fibrous mesocarp and a hard stony endocarp around a single seed, so it is a drupe, which is option $1$.

**Subtopic:** The Fruit · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q119_c7a70f7b_27102026.png?v=c7a70f7bb706)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q119_b01fcda0_27102026.png?v=b01fcda0fd3c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Fruit type is fixed by the pericarp: a drupe has a fleshy or fibrous middle layer over a stony inner layer, which is what encloses the coconut seed
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 3  
  The everyday name prints this option inside the stem -- coco-nut -- and the hard shell seems to confirm it, so a student who does not go to the pericarp takes nut. The coconut has a fibrous mesocarp over a stony endocarp, which is the definition of a drupe.
- **Proposed:** `vernacular_name_echo` — the option is the organism's ordinary English name taken for its technical class, with the word printed inside the stem itself; nearby_fact needs a true fact about an adjacent thing and nothing true about nuts is being offered here, and answers_other_question needs the option to be the right answer to some other question, which 'Nut' is not for the coconut
- **Why:** This question requires the stated fruit type of the coconut, demonstrated by the stem 'Coconut fruit is a' against four pericarp-defined fruit types.
- **NCERT:** “In coconut which is also a drupe, the mesocarp is fibrous.”  
  *morphology of flowering plants, page 65*
<!--/ecat-->

## Q120

Biology · botany · Organisms and Populations

Plants which produce characterstic pneumatophores and show vivipary belong to

- (1) Mesophytes
- **(2)** Halophytes
- (3) Psammophytes
- (4) Hydrophytes

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Halophytes growing in saline soils show
2. (i) Vivipary which is in-situ seed germination
3. (ii) Pneumatophores for gaseous exchange

**Solved independently** (answer withheld)

1. Pneumatophores and vivipary are the defining features of mangrove vegetation (e.g. $\textit{Rhizophora}$), which grows in saline, waterlogged soil; such salt-tolerant plants are halophytes, option $2$.

**Subtopic:** Homeostasis, Adaptations and Its Types · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q120_a8f8cbaa_27102026.png?v=a8f8cbaa8938)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q120_420fdc8d_27102026.png?v=420fdc8dbbfb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mangroves of saline swamps meet waterlogged salt soil with pneumatophores for gas exchange and with vivipary, the seed germinating on the parent plant
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Pneumatophores are breathing roots that stick up out of waterlogged ground, so a student who stores 'pneumatophore = a plant standing in water' files the plant with the hydrophytes. Hydrophytes are plants of fresh water; pneumatophores with vivipary are the salt-marsh mangrove pair, and those are halophytes.
- **Why:** This question requires the stated group that shows these two adaptations, demonstrated by the stem 'produce characterstic pneumatophores and show vivipary belong to' against four named plant groups.
<!--/ecat-->

## Q121

Biology · botany · Biodiversity and Conservation

Which one of the following is related to Ex-situ conservation of threatened animals and plants?

- **(1)** Wildlife Safari parks
- (2) Biodiversity hot spots
- (3) Amazon rainforest
- (4) Himalayan region

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ex-situ conservation is offsite strategy for conservation of animals and plants in zoological park and botanical gardens respectively.

**Solved independently** (answer withheld)

1. Ex-situ conservation means protecting threatened species outside their natural habitat, e.g. zoos, botanical gardens and wildlife safari parks, so option $1$ fits while options $2$, $3$ and $4$ are natural habitats (in-situ).

**Subtopic:** Ex Situ Conservation · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q121_344565fb_27102026.png?v=344565fb57b2)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q121_e5c6551e_27102026.png?v=e5c6551e2bbd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex situ conservation keeps a threatened species outside its natural habitat -- zoos, safari parks, botanical gardens, seed and gene banks
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Biodiversity hot spots are the other named conservation device in the same section, so a student holding 'hot spot = a conservation measure' reaches for it. A hot spot is protected where the species already live, which makes it in situ -- the opposite of what the stem asks.
- **Why:** This question requires the stated examples of ex situ conservation, demonstrated by the stem 'related to Ex-situ conservation of threatened animals and plants?' with three in-habitat answers printed beside the safari park.
- **NCERT:** “Ex situ Conservation– In this approach, threatened animals and plants are taken out from their natural habitat and placed in special setting where they can be protected and given special care. Zoological parks, botanical gardens and wildlife safari parks serve this purpose.”  
  *biodiversity and conservation, page 225*
<!--/ecat-->

## Q122

Biology · botany · Plant Kingdom

Select the mismatch :

- **(1)** Pinus – Dioecious
- (2) Cycas – Dioecious
- (3) Salvinia – Heterosporous
- (4) Equisetum – Homosporous

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Pinus is monoecious plant having both male and female cones on same plant.

**Solved independently** (answer withheld)

1. $\textit{Pinus}$ bears male and female cones on the same plant, so it is monoecious, not dioecious: the pair in option $1$ is a mismatch.
2. $\textit{Cycas}$ has male and female cones on separate plants (dioecious), $\textit{Salvinia}$ is a heterosporous water fern, and $\textit{Equisetum}$ is homosporous, so options $2$, $3$ and $4$ are correct pairs; the answer is option $1$.

**Subtopic:** Gymnosperms · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q122_766b0410_27102026.png?v=766b04102b5c)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q122_ef6b7413_27102026.png?v=ef6b7413a427)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Pinus is monoecious, bearing both cones on one tree, while Cycas is dioecious; among pteridophytes Salvinia is heterosporous and Equisetum homosporous
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Options 1 and 2 print the same word 'Dioecious' against the two gymnosperms learnt as a pair, so the whole question reduces to which of Pinus and Cycas carries it. A student who has the two the wrong way round marks the Cycas row as the mismatch; Cycas really is dioecious, and it is Pinus that bears male and female cones on one tree.
- **Why:** This question requires adjudicating four printed organism-trait pairings, demonstrated by the stem 'Select the mismatch :' with 'Pinus – Dioecious' and 'Cycas – Dioecious' differing only in the genus.
- **NCERT:** “The male or female cones or strobili may be borne on the same tree (Pinus). However, in cycas male cones and megasporophylls are borne on different trees.”  
  *plant kingdom, page 33*
<!--/ecat-->

## Q123

Biology · botany · Transport in Plants

Which of the following facilitates opening of stomatal aperture?

- (1) Contraction of outer wall of guard cells
- (2) Decrease in turgidity of guard cells
- **(3)** Radial orientation of cellulose microfibrils in the cell wall of guard cells
- (4) Longitudinal orientation of cellulose microfibrils in the cell wall of guard cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Cellulose microfibrils are oriented radially rather than longitudinally which makes easy for the stoma to open.

**Solved independently** (answer withheld)

1. Stomata open when guard cells become turgid, and the radial orientation of cellulose microfibrils in the guard cell wall makes the outer walls bulge outward and pull the inner walls apart, so option $3$ is correct.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q123_6547f1c2_27102026.png?v=6547f1c26926)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q123_ce7f8121_27102026.png?v=ce7f8121eec5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stomatal opening turns on guard-cell wall architecture: cellulose microfibrils laid radially, with a thick inner wall, make the turgid cell bow outwards and pull the pore open
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Option 4 is the key with one word changed, "Longitudinal" for "Radial", so a student who retained that microfibril orientation is the answer but not which orientation has nothing left to separate the two. Radial fibrils act like inextensible hoops, so the swelling cell can only lengthen and curve away from the pore; fibrils running lengthwise would stop exactly that.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Turgor is the mechanism this topic is taught by, so a student who reaches for water movement rather than wall structure takes the turgidity option. The one printed is the closing condition: water entering and raising turgidity is what opens the aperture, and losing it is what shuts it.
- **Why:** This question requires the stated structural fact about the guard cell wall, demonstrated by the stem "Which of the following facilitates opening of stomatal aperture?" against the key option "Radial orientation of cellulose microfibrils in the cell wall of guard cells".
- **Note:** Each option is a noun phrase naming one condition and no lettered block is printed, so the printed shape is a plain "which of the following" question rather than statements put up for judgement.
<!--/ecat-->

## Q124

Biology · both · Molecular Basis of Inheritance

The association of histone H1 with a nucleosome indicates:

- (1) Transcription is occurring
- (2) DNA replication is occurring
- **(3)** The DNA is condensed into a Chromatin Fibre
- (4) The DNA double helix is exposed

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The association of H1 protein indicates the complete formation of nucleosome.
2. Therefore the DNA is in condensed form.

**Solved independently** (answer withheld)

1. Histone $H1$ is the linker histone: it binds the nucleosome where linker DNA enters and leaves, and its association packs nucleosomes into the condensed chromatin fibre, so DNA is condensed (not exposed, not being transcribed or replicated), which is option $3$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 24)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q124_2cf50a58_27102026.png?v=2cf50a5847e4)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q124_1f0f5481_27102026.png?v=1f0f54815383)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Histone H1 binds the linker DNA where the helix enters and leaves the nucleosome, and that binding is what stacks nucleosomes into the chromatin fibre
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  H1 is remembered as the histone that is not inside the bead — it sits on the linker DNA between nucleosomes — so a student reads its presence as a sign the helix is still lying open. That linker binding is what draws neighbouring nucleosomes together into the chromatin fibre, so it marks the condensed state, not the exposed one.
- **Why:** This question requires what the presence of a named protein signifies, demonstrated by the stem "The association of histone H1 with a nucleosome indicates:" and by the options being rival states of the DNA.
<!--/ecat-->

## Q125

Biology · both · Biotechnology: Principles and Processes

DNA fragments are

- (1) Positively charged
- **(2)** Negatively charged
- (3) Neutral
- (4) Either positively or negatively charged depending on their size

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. DNA fragments are negatively charged because of phosphate group.

**Solved independently** (answer withheld)

1. Each nucleotide in the DNA backbone has an ionised phosphate group ($\mathrm{PO_4^{-}}$), so DNA fragments carry a net negative charge whatever their size, which is option $2$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q125_a6ce26b4_27102026.png?v=a6ce26b48940)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q125_cceea0b8_27102026.png?v=cceea0b808df)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Every phosphate in the DNA backbone carries a negative charge, which is why an electric field drives fragments towards the anode in a gel
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The sentence this topic is memorised by is that fragments separate according to size, so a student asked instead about charge reaches for the size fact and hangs it on charge. Size decides only how far a fragment travels through the gel; every fragment, long or short, is negative because the charge sits on the phosphate backbone.
- **Why:** This question requires one stated property of DNA, demonstrated by the bare stem "DNA fragments are" with the four options being charge states.
- **NCERT:** “Since DNA fragments are negatively charged molecules they can be separated by forcing them to move towards the anode under an electric field through a medium/matrix.”  
  *biotechnology principles and processes, page 168*
<!--/ecat-->

## Q126

Biology · zoology · Human Reproduction

Capacitation occurs in

- (1) Rete testis
- (2) Epididymis
- (3) Vas deferens
- **(4)** Female Reproductive tract

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Capacitation is increase in fertilising capacity of sperms which occurs in female reproductive tract.

**Solved independently** (answer withheld)

1. Capacitation is the activation of sperm that takes place inside the female reproductive tract, so the answer is option $4$.

**Subtopic:** Fertilisation · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q126_f15fde72_27102026.png?v=f15fde7288c5)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q126_d1a0e030_27102026.png?v=d1a0e030e634)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Capacitation is the final change sperm undergo in the female reproductive tract, after the epididymis has already made them motile
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Sperm maturation in the epididymis is the fact printed alongside capacitation, so a student who has merged the two into one event of "becoming competent" picks the epididymis. The epididymis gives motility; capacitation is the later change brought about by the secretions of the female tract, without which the sperm cannot fertilise.
- **Why:** This question requires the site at which a named event happens, demonstrated by the stem "Capacitation occurs in" and by the options being four successive parts of the reproductive tract.
<!--/ecat-->

## Q127

Biology · botany · Ecosystem

Which ecosystem has the maximum biomass?

- **(1)** Forest ecosystem
- (2) Grassland ecosystem
- (3) Pond ecosystem
- (4) Lake ecosystem

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. High productive ecosystem are
2. – Tropical rain forest
3. – Coral reef
4. – Estuaries
5. – Sugarcane fields

**Solved independently** (answer withheld)

1. Forest producers are large, long-lived trees that store a great deal of woody biomass, so the forest standing crop ($\mathrm{kg\,m^{-2}}$) is far higher than that of grassland or aquatic ecosystems (pond and lake producers are short-lived phytoplankton), which is option $1$.

**Subtopic:** Productivity · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q127_ddfcb67c_27102026.png?v=ddfcb67c0314)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q127_48b05dda_27102026.png?v=48b05dda2d59)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Standing crop: a forest's accumulated woody biomass per unit area outweighs that of a grassland or a water body, whatever their productivity
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The pond is the one ecosystem biomass is taught through — it is the standard case of an inverted pyramid of biomass, where the fish outweigh the phytoplankton — so a student who sees "biomass" and "ecosystem" together returns that remembered answer. It answers where the pyramid inverts, not which ecosystem holds the most biomass, and the standing crop of a pond's producers is small precisely because it turns over fast.
- **Why:** This question requires four named ecosystems to be weighed against one another on a single quantity, demonstrated by the stem "Which ecosystem has the maximum biomass?" with no value printed for any of them.
<!--/ecat-->

## Q128

Biology · zoology · Principles of Inheritance and Variation

A disease caused by an autosomal primary non-disjunction is

- **(1)** Down's syndrome
- (2) Klinefelter's syndrome
- (3) Turner's syndrome
- (4) Sickle cell anemia

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Down’s syndrome is caused by non-disjunction of $21^{\mathrm{st}}$ chromosome.

**Solved independently** (answer withheld)

1. Down's syndrome is trisomy of chromosome $21$ (an autosome) caused by non-disjunction, while Klinefelter's ($47,XXY$) and Turner's ($45,XO$) are sex-chromosome aneuploidies and sickle cell anemia is a single-gene point mutation, so the answer is option $1$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q128_52f68c79_27102026.png?v=52f68c79b2ce)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q128_07ba67b7_27102026.png?v=07ba67b773dd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Primary non-disjunction leaves a gamete with an extra chromosome; when that chromosome is an autosome it gives trisomy 21, Down's syndrome, and when it is a sex chromosome it gives Klinefelter's or Turner's
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Klinefelter's syndrome is itself caused by primary non-disjunction, so a student who reads the stem as far as "non-disjunction" and stops has an option that fully fits. The extra chromosome there is an X, and the only word that rules it out is "autosomal".
- **Why:** This question requires a disorder to be matched to a stated cause, demonstrated by the stem "A disease caused by an autosomal primary non-disjunction is", whose word "autosomal" is what separates Down's syndrome from the two sex-chromosome options.
- **NCERT:** “Failure of segregation of chromatids during cell division cycle results in the gain or loss of a chromosome(s), called aneuploidy. For example, Down’s syndrome results in the gain of extra copy of chromosome 21. Similarly, Turner’s syndrome results due to loss of an X chromosome in human females.”  
  *principles of inheritance and variation, page 75*
<!--/ecat-->

## Q129

Biology · botany · Plant Kingdom

Life cycle of Ectocarpus and Fucus respectively are

- (1) Haplontic, Diplontic
- (2) Diplontic, Haplodiplontic
- **(3)** Haplodiplontic, Diplontic
- (4) Haplodiplontic, Haplontic

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ectocarpus has haplodiplontic life cycle and Fucus has diplontic life cycle.

**Solved independently** (answer withheld)

1. Ectocarpus has both a free-living haploid gametophyte and a diploid sporophyte, so its life cycle is haplodiplontic; Fucus has a diploid thallus and only the gametes are haploid, so its life cycle is diplontic, which is option $3$.

**Subtopic:** Phaeophyceae · **Difficulty:** hard (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q129_6d486ef4_27102026.png?v=6d486ef45869)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q129_95c1e68c_27102026.png?v=95c1e68c9e73)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Haplontic, diplontic and haplodiplontic life cycles: Ectocarpus alternates a haploid and a diploid plant, while Fucus is diploid throughout and only its gametes are haploid
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Option 2 is the key with the two attributions exchanged, so a student who has retained that one of these two brown algae is diplontic and the other haplodiplontic, but not which is which, has a coin to toss. Fucus is the diplontic one and Ectocarpus the alternating one.
- **Also:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Haplontic is the life cycle most algae are taught with — Spirogyra, Chlamydomonas, Volvox — so a student who places Ectocarpus correctly then falls back on the algal default for Fucus. Fucus keeps a diploid plant body and reduces only at gamete formation, so the second half fails.
- **Why:** This question requires each alga to be assigned its life cycle class, demonstrated by the stem "Life cycle of Ectocarpus and Fucus respectively are" and by every option pairing two class names.
- **Note:** The answer has two halves held together by "respectively", and neither half scores on its own.
<!--/ecat-->

## Q130

Biology · both · Molecular Basis of Inheritance

> ⚠ The booklet lost this question's number and first line. The opening "If there are 999 bases in an RNA that codes for a" is restored word for word from Code B q112, Code C q28, Code D q89 (same exam).

If there are 999 bases in an RNA that codes for a protein with 333 amino acids, and the base at position 901 is deleted such that the length of the RNA becomes 998 bases, how many codons will be altered?

- (1) 1
- (2) 11
- **(3)** 33
- (4) 333

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. If deletion occurs at $901^{\mathrm{st}}$ position the remaining $98$ bases specifying for $33$ codons of amino acids will be altered.

**Solved independently** (answer withheld)

1. A protein of $333$ amino acids is coded by $333 \times 3 = 999$ bases.
2. Base $901$ is the first base of codon $\frac{900}{3} + 1 = 301$.
3. Deleting it causes a frameshift from codon $301$ to the last codon $333$.
4. Codons altered $= 333 - 301 + 1 = 33$, which is option $3$.

**Subtopic:** Effect of Mutation on Genetic Code · **Difficulty:** hard (3 steps, 3 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q130_e9b6a702_27102026.png?v=e9b6a702e147)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q130_200a0d7e_27102026.png?v=200a0d7eb7c7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A single base deletion shifts the reading frame from its own codon onward, so how many codons change depends on where in the message the base is lost
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  A student holding the rule "a deletion shifts the frame, so everything after it is altered" reaches for the whole protein and picks 333, the figure the stem itself supplies as the number of amino acids. Base 901 sits in codon 301, so the altered stretch is codons 301 to 333, which is 33.
- **Why:** This question requires a count worked out from the stem's own numbers, demonstrated by "the base at position 901 is deleted" set against "999 bases in an RNA that codes for a protein with 333 amino acids".
- **NCERT:** “Insertion or deletion of one or two bases changes the reading frame from the point of insertion or deletion.”  
  *molecular basis of inheritance, page 97*
<!--/ecat-->

## Q131

Biology · zoology · Locomotion and Movement

The pivot joint between atlas and axis is a type of

- (1) Fibrous joint
- (2) Cartilaginous joint
- **(3)** Synovial joint
- (4) Saddle joint

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Synovial joints are freely movable joint which allow considerable movements.
2. Pivot joint is a type of synovial joint which provide rotational movement as in between atlas and axis vertebrae of vertebral column.

**Solved independently** (answer withheld)

1. The pivot joint between the atlas and the axis allows free rotation and has a synovial cavity, so it is a type of synovial joint, which is option $3$.

**Subtopic:** Joints · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q131_94f186a1_27102026.png?v=94f186a190e4)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q131_a18ace98_27102026.png?v=a18ace9882c5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Joints are classed by what lies between the bones, and a pivot joint has a fluid-filled cavity, which makes it synovial whatever bones it connects
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Atlas and axis are vertebrae, and the joints between adjacent vertebrae are the standard example of a cartilaginous joint, so a student who classifies by location rather than by what is between the bones picks it. The atlas-axis pivot is the exception in that column: it has a synovial cavity and allows the head to rotate, which a cartilaginous joint cannot.
- **Why:** This question requires a named joint to be placed in its class, demonstrated by the stem "The pivot joint between atlas and axis is a type of" with the options being classes of joint.
- **NCERT:** “Synovial joints are characterised by the presence of a fluid filled synovial cavity between the articulating surfaces of the two bones. Such an arragement allows considerable movement. These joints help in locomotion and many other movements. Ball and socket joint (between humerus and pectoral girdle), hinge joint (knee joint), pivot joint (between atlas and axis), gliding joint (between the carpals) and saddle joint (between carpal and metacarpal of thumb) are some examples.”  
  *locomotion and movement, page 227*
<!--/ecat-->

## Q132

Biology · both · Biotechnology: Principles and Processes

A gene whose expression helps to identify transformed cell is known as

- **(1)** Selectable marker
- (2) Vector
- (3) Plasmid
- (4) Structural gene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In recombinant DNA technology, selectable markers helps in identifying and eliminating non-transformants and selectively permitting the growth of the transformants.

**Solved independently** (answer withheld)

1. A selectable marker (e.g. an antibiotic-resistance gene such as $amp^R$) lets only transformed cells survive or show a phenotype, so it identifies transformants: option $1$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q132_532c95ec_27102026.png?v=532c95ec6661)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q132_e2b78f06_27102026.png?v=e2b78f06efd0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A selectable marker is the extra gene riding on the vector whose expression lets transformed cells be told apart from untransformed ones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Only two options are genes at all, and "structural gene" is the other one — the gene of interest, whose expression is the whole purpose of the transformation — so a student who reads "whose expression" as "the gene being expressed" lands there. What identifies a transformant is the second gene on the vector, typically antibiotic resistance, which lets the untransformed cells be killed off.
- **Why:** This question requires the term for a stated role, demonstrated by the stem "A gene whose expression helps to identify transformed cell is known as".
- **NCERT:** “(ii) Selectable marker : In addition to ‘ori’, the vector requires a selectable marker, which helps in identifying and eliminating non-transformants and selectively permitting the growth of the transformants.”  
  *biotechnology principles and processes, page 169*
- **Note:** Options 2 and 3 name a carrier rather than a gene, so the stem's own words "A gene" rule them out.
<!--/ecat-->

## Q133

Biology · botany · Ecosystem

Presence of plants arranged into well defined vertical layers depending on their height can be seen best in :

- (1) Tropical Savannah
- **(2)** Tropical Rain Forest
- (3) Grassland
- (4) Temperate Forest

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The tropical rain forest have five vertical strata on the basis of height of plants. i.e., ground vegetation, shrubs, short canopy trees, tall canopy trees and tall emergent trees.

**Solved independently** (answer withheld)

1. Vertical stratification, with plants of different heights forming distinct layers, is most clearly seen in the tropical rain forest, so the answer is option $2$.

**Subtopic:** Ecosystem – Structure, Function and Components · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q133_78606921_27102026.png?v=78606921b561)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q133_5d6866a4_27102026.png?v=5d6866a4d44f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Stratification: the vertical layering of vegetation by height, which is most sharply developed in a tropical rain forest
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Layering is taught as a property of forests — trees on top, then shrubs, then herbs — so a student who gets as far as "a forest" still has two forest options and the stem prints nothing to separate them. A temperate forest is broadly canopy over herb layer, while a tropical rain forest stacks emergent, canopy, understorey, shrub and ground layers, which is what "well defined vertical layers" turns on.
- **Why:** This question requires four named communities to be weighed against each other on how sharply they are layered, demonstrated by the stem "can be seen best in" with no criterion printed to apply.
- **NCERT:** “Vertical distribution of different species occupying different levels is called stratification. For example, trees occupy top vertical strata or layer of a forest, shrubs the second and herbs and grasses occupy the bottom layers.”  
  *ecosystem, page 206*
<!--/ecat-->

## Q134

Biology · zoology · Principles of Inheritance and Variation

The genotypes of a Husband and Wife are $\mathrm{I^AI^B}$ and $\mathrm{I^Ai}$. Among the blood types of their children, how many different genotypes and phenotypes are possible?

- (1) 3 genotypes ; 3 phenotypes
- (2) 3 genotypes ; 4 phenotypes
- **(3)** 4 genotypes ; 3 phenotypes
- (4) 4 genotypes ; 4 phenotypes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Husband $\times$ Wife: $\mathrm{I^AI^B}$ $\times$ $\mathrm{I^Ai}$

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/figures_agent/q134_sol_1_48a3d35f_27102026.svg?v=48a3d35fc22f)

2. Number of genotypes $= 4$
3. Number of phenotypes $= 3$
4. $\mathrm{I^AI^A}$ and $\mathrm{I^Ai} = \mathrm{A}$
5. $\mathrm{I^AI^B} = \mathrm{AB}$
6. $\mathrm{I^Bi} = \mathrm{B}$

**Solved independently** (answer withheld)

1. Husband $\mathrm{I^AI^B}$ makes gametes $\mathrm{I^A}$ and $\mathrm{I^B}$; wife $\mathrm{I^Ai}$ makes gametes $\mathrm{I^A}$ and $\mathrm{i}$.
2. Crossing gives $\mathrm{I^AI^A}$, $\mathrm{I^Ai}$, $\mathrm{I^AI^B}$, $\mathrm{I^Bi}$, so there are $4$ distinct genotypes.
3. $\mathrm{I^AI^A}$ and $\mathrm{I^Ai}$ are both blood group A, $\mathrm{I^AI^B}$ is AB, $\mathrm{I^Bi}$ is B, so there are $3$ phenotypes.
4. $4$ genotypes and $3$ phenotypes is option $3$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 25)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q134_bb747707_27102026.png?v=bb7477073f48)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q134_e288dde7_27102026.png?v=e288dde74ba7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Multiple alleles with one recessive: $\mathrm{I^A}$ and $\mathrm{I^B}$ are codominant while $i$ is recessive, so four genotypes collapse into three blood groups
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student who works the cross correctly to $\mathrm{I^AI^A}$, $\mathrm{I^Ai}$, $\mathrm{I^AI^B}$ and $\mathrm{I^Bi}$ then counts one blood group per genotype and reports four of each. $\mathrm{I^AI^A}$ and $\mathrm{I^Ai}$ are both group A because $i$ is recessive, so the genotype count is right and the phenotype count is one too many.
- **Why:** This question requires two counts produced from a cross, demonstrated by the stem "how many different genotypes and phenotypes are possible?" and by each option carrying one number for each.
- **NCERT:** “Because humans are diploid organisms, each person possesses any two of the three I gene alleles. Iᴬ and Iᴮ are completely dominant over i, in other words when Iᴬ and i are present only Iᴬ expresses (because i does not produce any sugar), and when Iᴮ and i are present Iᴮ expresses. But when Iᴬ and Iᴮ are present together they both express their own types of sugars: this is because of co-dominance.”  
  *principles of inheritance and variation, page 61*
- **Note:** Each option is a pair of counts joined by a semicolon, so the answer has two halves rather than being a statement put up for judgement.
<!--/ecat-->

## Q135

Biology · botany · Plant Kingdom

Zygotic meiosis is characteristic of

- (1) Marchantia
- (2) Fucus
- (3) Funaria
- **(4)** Chlamydomonas

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Chlamydomonas has haplontic life cycle hence showing zygotic meiosis or initial meiosis.

**Solved independently** (answer withheld)

1. Zygotic meiosis means the diploid zygote is the only $2n$ stage and divides meiotically, which defines the haplontic life cycle; Chlamydomonas is haplontic, Fucus is diplontic, and Marchantia and Funaria are haplo-diplontic, so the answer is option $4$.

**Subtopic:** Chlorophyceae · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q135_9795b10f_27102026.png?v=9795b10fbf5e)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q135_83efe123_27102026.png?v=83efe123333e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Zygotic meiosis is the haplontic cycle: the zygote is the only diploid cell and divides by meiosis at once, as in Chlamydomonas and Volvox
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Fucus is the other alga on the list and sits in the same taught figure of life-cycle patterns, so a student who remembers the three patterns but not which alga illustrates which reaches for it. Fucus is the diplontic example, where meiosis happens at gamete formation, not in the zygote.
- **Why:** This question requires the stated fact about which organism shows zygotic meiosis, demonstrated by the four options being named algae and mosses with no criterion printed to apply.
<!--/ecat-->

## Q136

Biology · botany · Microbes in Human Welfare

Which of the following is correctly matched for the product produced by them?

- (1) Acetobacter aceti : Antibiotics
- (2) Methanobacterium : Lactic acid
- (3) Penicillium notatum : Acetic acid
- **(4)** Saccharomyces cerevisiae : Ethanol

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Saccharomyces cerevisiae is commonly called Brewer’s yeast.
2. It causes fermentation of carbohydrates producing ethanol.

**Solved independently** (answer withheld)

1. $\textit{Acetobacter aceti}$ produces acetic acid, $\textit{Methanobacterium}$ produces methane, $\textit{Penicillium notatum}$ produces penicillin, and $\textit{Saccharomyces cerevisiae}$ produces ethanol, so only option $4$ is correctly matched.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (4 steps, 1 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q136_99464809_27102026.png?v=99464809af44)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q136_8567a4aa_27102026.png?v=8567a4aa6452)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Each industrial microbe is tied to one product: Acetobacter aceti to acetic acid, Methanobacterium to methane, Penicillium notatum to penicillin, Saccharomyces cerevisiae to ethanol
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who files Penicillium with the moulds used in industrial fermentation, beside Aspergillus niger and its citric acid, accepts an organic acid as its product. Penicillium notatum is the antibiotic producer of that chapter, and acetic acid belongs to Acetobacter aceti in the same table.
- **Why:** This question requires the correct microbe-to-product pairing rather than one recalled name, demonstrated by the stem asking which option is "correctly matched for the product produced by them" and every option printing an organism beside a product.
- **NCERT:** “Yeast (Saccharomyces cerevisiae) is used for commercial production of ethanol.”  
  *microbes in human welfare, page 153*
- **Note:** Each option is an organism-and-product pair accepted or rejected whole, but no lettered list and no pairing code is printed, so the shape on the page is a four-answer question whose answers happen to be pairs.
<!--/ecat-->

## Q137

Biology · zoology · Body Fluids and Circulation

Frog's heart when taken out of the body continues to beat for some time
Select the best option from the following statements

- **(a)** Frog is a poikilotherm
- **(b)** Frog does not have any coronary circulation
- **(c)** Heart is "myogenic" in nature
- **(d)** Heart is autoexcitable

- (1) Only (c)
- (2) Only (d)
- (3) (a) & (b)
- **(4)** (c) & (d)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Frog or the vertebrates have myogenic heart having self contractile system or are autoexcitable; because of this condition, it will keep on working outside the body for some time.

**Solved independently** (answer withheld)

1. Statements (a) and (b) may be true of frogs, but neither explains why an excised heart keeps beating, so option $3$ is out.
2. The heartbeat originates in specialised cardiac muscle (SA node) without nerve input, i.e. the heart is myogenic (c) and therefore autoexcitable (d); both statements describe the cause, so option $4$, (c) & (d).

**Subtopic:** Regulation of Cardiac Activity · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q137_d8fe592f_27102026.png?v=d8fe592f8e6f)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q137_e67c44cb_27102026.png?v=e67c44cb07cb)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A myogenic heart: the beat is started by the heart's own autoexcitable nodal tissue, not by a nerve, so an excised heart keeps beating
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student who remembers the one NCERT word 'myogenic' takes it as the whole explanation and stops at (c). 'Autoexcitable' in (d) is that same property stated as the nodal tissue firing on its own, so the key takes the two together.
- **Why:** This question requires recognising that 'myogenic' and 'autoexcitable' name one property of the heart's nodal tissue, demonstrated by option 1 offering 'Only (c)' and option 2 'Only (d)' while the key takes '(c) & (d)'.
- **NCERT:** “Normal activities of the heart are regulated intrinsically, i.e., auto regulated by specialised muscles (nodal tissue), hence the heart is called myogenic.”  
  *body fluids and circulation, page 202*
<!--/ecat-->

## Q138

Biology · botany · Respiration in Plants

Which statement is wrong for Krebs' cycle?

- (1) There are three points in the cycle where $\mathrm{NAD^{+}}$ is reduced to $\mathrm{NADH + H^{+}}$
- (2) There is one point in the cycle where $\mathrm{FAD^{+}}$ is reduced to $\mathrm{FADH_2}$
- (3) During conversion of succinyl CoA to succinic acid, a molecule of GTP is synthesised
- **(4)** The cycle starts with condensation of acetyl group (acetyl CoA) with pyruvic acid to yield citric acid

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Krebs cycle starts with condensation of acetyl CoA (2C) with oxaloacetic acid (4C) to form citric acid (6C).

**Solved independently** (answer withheld)

1. In the TCA cycle the acetyl group of acetyl CoA condenses with oxaloacetic acid (OAA) and water to give citric acid, so statement $4$ (condensation with pyruvic acid) is wrong; statements $1$ (3 NADH), $2$ (1 $\mathrm{FADH_2}$) and $3$ (GTP at succinyl CoA $\to$ succinic acid) are correct, so the answer is option $4$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** medium (4 steps, 2 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q138_18c1669a_27102026.png?v=18c1669ae97c)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q138_db0005ba_27102026.png?v=db0005badfec)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** One turn of the citric acid cycle starts by condensing acetyl CoA with oxaloacetic acid, not with pyruvic acid, and yields 3 NADH, 1 FADH2 and 1 GTP
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Substrate-level phosphorylation is first met in glycolysis, where the product is ATP, so a student carries ATP across to the succinyl CoA step and reads this line as the error. The text prints GTP at that step, so the line is true and the false one is the condensation partner.
- **Why:** This question requires the facts the text states about one turn of the cycle, demonstrated by option 4 reading "condensation of acetyl group (acetyl CoA) with pyruvic acid" where oxaloacetic acid is the named partner.
- **NCERT:** “The TCA cycle starts with the condensation of acetyl group with oxaloacetic acid (OAA) and water to yield citric acid (Figure 12.3).”  
  *respiration in plants, page 158*
<!--/ecat-->

## Q139

Biology · zoology · Animal Kingdom

In case of poriferans the spongocoel is lined with flagellated cells called :

- (1) Ostia
- (2) Oscula
- **(3)** Choanocytes
- (4) Mesenchymal cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Choanocytes (collar cells) form lining of spongocoel in poriferans (sponges).
2. Flagella in collar cells provide circulation to water in water canal system.

**Solved independently** (answer withheld)

1. In poriferans, the spongocoel is lined by flagellated collar cells called choanocytes, so the answer is option $3$.

**Subtopic:** Phylum – Porifera · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q139_cd71fa1a_27102026.png?v=cd71fa1a40dc)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q139_cdd89997_27102026.png?v=cdd89997ebd7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Choanocytes, the flagellated collar cells, line the spongocoel and canals of a sponge and drive its water current
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The sentence a student remembers about sponges is the water route, where water enters through the ostia into the spongocoel and leaves by the osculum, so the term printed next to "spongocoel" in memory is picked. Ostia are pores in the body wall, not cells; the flagellated lining is made of choanocytes.
- **Why:** This question requires the stated name of a lining cell, demonstrated by the stem asking what the "flagellated cells" lining the spongocoel are "called".
- **NCERT:** “Choanocytes or collar cells line the spongocoel and the canals.”  
  *animal kingdom, page 40*
<!--/ecat-->

## Q140

Biology · both · Molecular Basis of Inheritance

Which of the following RNAs should be most abundant in animal cell?

- **(1)** r-RNA
- (2) t-RNA
- (3) m-RNA
- (4) mi-RNA

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{rRNA}$ is most abundant in animal cell.
2. It constitutes $80\%$ of total $\mathrm{RNA}$ of the cell.

**Solved independently** (answer withheld)

1. Ribosomes are present in very large numbers in every cell, and rRNA is their main structural and catalytic part, so $\text{rRNA} \approx 80\%$ of total cellular RNA, more than $\text{tRNA}$, $\text{mRNA}$ or $\text{miRNA}$; this is option $1$.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q140_26b96b7b_27102026.png?v=26b96b7b5f7c)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q140_9b7e443e_27102026.png?v=9b7e443e03ac)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ribosomal RNA is about four fifths of a cell's RNA because ribosomes are its most numerous RNA-bearing particles, while mRNA is the most varied and the least abundant
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  A student reasoning from "every gene is transcribed into its own mRNA" concludes that mRNA must outnumber the rest, and option 3 is the right answer to which RNA has the most distinct species. Those many species together are only a few per cent of cellular RNA, so by amount rRNA leads at about 80%.
- **Why:** This question requires the stored fact about how much of a cell's RNA each type makes up, demonstrated by the options being the four RNA types with no quantity printed to work from.
<!--/ecat-->

## Q141

Biology · zoology · Animal Kingdom

Which among these is the correct combination of aquatic mammals?

- (1) Seals, Dolphins, Sharks
- (2) Dolphins, Seals, Trygon
- **(3)** Whales, Dolphins, Seals
- (4) Trygon, Whales, Seals

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Sharks and Trygon (sting ray) are the members of chondrichthyes (cartilaginous fish) while whale, Dolphin and Seals are aquatic mammals belong to class mammalia.

**Solved independently** (answer withheld)

1. Sharks and $Trygon$ are cartilaginous fishes (Chondrichthyes), not mammals, so options $1$, $2$ and $4$ are out; whales, dolphins and seals are all aquatic mammals, which is option $3$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 26)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q141_e04408c2_27102026.png?v=e04408c2f235)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q141_8c6e0ef9_27102026.png?v=8c6e0ef9bd16)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Whales, dolphins and seals are mammals; sharks and Trygon are cartilaginous fishes, however aquatic and however viviparous
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Two of the three named animals are mammals, and a student who sorts by "large sea animal that bears live young" lets the shark through, since many sharks are viviparous. Shark is a cartilaginous fish, so the set fails on one member and the whole option scores nothing.
- **Why:** This question requires the class each named aquatic animal belongs to, demonstrated by the stem asking for the "correct combination of aquatic mammals" and each option printing three animal names together.
- **NCERT:** “Lest we forget, some mammals live wholly in water. Whales, dolphins, seals and sea cows are some examples.”  
  *evolution, page 124*
- **Note:** Each option is a set of three names accepted or rejected whole, though nothing is lettered or listed on the page.
<!--/ecat-->

## Q142

Biology · botany · Photosynthesis in Higher Plants

With reference to factors affecting the rate of photosynthesis, which of the following statements is **not** correct?

- (1) Light saturation for $\mathrm{CO_2}$ fixation occurs at $10\%$ of full sunlight
- (2) Increasing atmospheric $\mathrm{CO_2}$ concentration upto $0.05\%$ can enhance $\mathrm{CO_2}$ fixation rate
- **(3)** $\mathrm{C_3}$ plants responds to higher temperatures with enhanced photosynthesis while $\mathrm{C_4}$ plants have much lower temperature optimum
- (4) Tomato is a greenhouse crop which can be grown in $\mathrm{CO_2}$ - enriched atmosphere for higher yield

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In $\mathrm{C_3}$ plants photosynthesis is decreased at higher temperature due to increased photorespiration.
2. $\mathrm{C_4}$ plants have higher temperature optimum because of the presence of pyruvate phosphate dikinase enzyme, which is sensitive to low temperature.

**Solved independently** (answer withheld)

1. Light saturation for $\mathrm{CO_2}$ fixation occurs at about $10\%$ of full sunlight, so option $1$ is correct.
2. Raising $\mathrm{CO_2}$ up to about $0.05\%$ increases the $\mathrm{CO_2}$ fixation rate, so option $2$ is correct.
3. $\mathrm{C_4}$ plants show enhanced photosynthesis at higher temperatures and $\mathrm{C_3}$ plants have a lower temperature optimum; option $3$ swaps them, so it is not correct.
4. Tomato is grown in $\mathrm{CO_2}$-enriched greenhouses for higher yield, so option $4$ is correct.
5. The incorrect statement is option $3$.

**Subtopic:** Factors Affecting Photosynthesis · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 27)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q142_52cc11cb_27102026.png?v=52cc11cb6300)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q142_fc52fb22_27102026.png?v=fc52fb2216fe)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Light saturates at about 10% of full sunlight and CO2 enrichment helps up to 0.05%, but it is the C4 plants that carry the higher temperature optimum, not the C3
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The other three options are the section's own sentences on light saturation at 10% of full sunlight, enrichment up to 0.05% and tomato as a greenhouse crop, so none of them offers a changed or adjacent fact to reach for. The device sits inside the keyed option, where the two temperature optima are printed the wrong way round.
- **Why:** This question requires the stated facts about factors affecting photosynthesis, demonstrated by option 3 reading "C3 plants responds to higher temperatures with enhanced photosynthesis while C4 plants have much lower temperature optimum".
- **NCERT:** “The C₄ plants respond to higher temperatures and show higher rate of photosynthesis while C₃ plants have a much lower temperature optimum.”  
  *photosynthesis in higher plants, page 150*
<!--/ecat-->

## Q143

Biology · botany · Organisms and Populations

Asymptote in a logistic growth curve is obtained when

- (1) The value of '$r$' approaches zero
- **(2)** $K = N$
- (3) $K > N$
- (4) $K < N$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A population growing in a habitat with limited resources shows logistic growth curve.
2. For logistic growth
3. $\frac{dN}{dt} = rN\left(\frac{K - N}{K}\right)$
4. If $K = N$ then $\frac{K - N}{K} = 0$
5. $\therefore$ the $\frac{dN}{dt} = 0$,
6. the population reaches asymptote.

**Solved independently** (answer withheld)

1. In the logistic (Verhulst-Pearl) model, $\frac{dN}{dt} = rN\left(\frac{K-N}{K}\right)$, and the curve flattens into its asymptote when growth stops, i.e. $\frac{dN}{dt} = 0$ with $N = K$, which is option $2$.

**Subtopic:** Logistic Growth · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 27)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q143_47868c8f_27102026.png?v=47868c8f4de4)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q143_01e40728_27102026.png?v=01e407288fe8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The logistic curve flattens when the population has filled its carrying capacity, so the asymptote is where $N = K$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Growth really does stop at the asymptote, so a student who reads "no further increase" as "the growth rate constant has run down" sets $r = 0$. In $\frac{dN}{dt} = rN\left(\frac{K-N}{K}\right)$, $r$ is a fixed parameter of the species; what vanishes is the factor $K - N$, and that happens when $N = K$.
- **Why:** This question requires the stated fact that the logistic curve plateaus at carrying capacity, demonstrated by the options being conditions on $K$ and $N$ rather than numbers to compute.
- **NCERT:** “A population growing in a habitat with limited resources show initially a lag phase, followed by phases of acceleration and deceleration and finally an asymptote, when the population density reaches the carrying capacity.”  
  *organisms and populations, page 195*
<!--/ecat-->

## Q144

Biology · zoology · Locomotion and Movement

Out of 'X' pairs of ribs in humans only 'Y' pairs are true ribs. Select the option that correctly represents values of X and Y and provides their explanation :

- **(1)** $X = 12$, $Y = 7$ True ribs are attached dorsally to vertebral column and ventrally to the sternum
- (2) $X = 12$, $Y = 5$ True ribs are attached dorsally to vertebral column and sternum on the two ends
- (3) $X = 24$, $Y = 7$ True ribs are dorsally attached to vertebral column but are free on ventral side
- (4) $X = 24$, $Y = 12$ True ribs are dorsally attached to vertebral column but are free on ventral side

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In human, $12$ pairs of ribs are present in which $7$ pairs of ribs ($1^{\mathrm{st}}$ to $7^{\mathrm{th}}$ pairs) are attached dorsally to vertebral column and ventrally to the sternum.

**Solved independently** (answer withheld)

1. Humans have $12$ pairs of ribs, so $X = 12$; the first $7$ pairs are true ribs, so $Y = 7$. True ribs join the vertebral column dorsally and the sternum ventrally (by hyaline cartilage), which is option $1$.

**Subtopic:** Axial Skeleton · **Difficulty:** medium (3 steps, 2 of 4 options live)

**Printed in the booklet** (page 27)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q144_8507c0c5_27102026.png?v=8507c0c57a67)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q144_62cdcbc1_27102026.png?v=62cdcbc186ea)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Humans have 12 pairs of ribs, and the first 7 pairs are the true ribs because each joins the vertebral column behind and the sternum in front
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  This option gets 12 pairs right and describes the true rib correctly as attached at both ends, so everything a student checks first holds. Its $Y = 5$ is the count of the pairs that are not true ribs, the 3 vertebrochondral plus the 2 floating, so one part of a three-part option fails and the whole option scores nothing.
- **Also:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The stem counts in "pairs", and a student who carries the remembered total of 24 ribs straight into X drops that word. Without "pairs" 24 is the right figure, which is why it is printed twice.
- **Why:** This question requires the stated rib counts together with the attachment that defines a true rib, demonstrated by the stem asking for "values of X and Y" and for the option that "provides their explanation".
- **NCERT:** “There are 12 pairs of ribs. Each rib is a thin flat bone connected dorsally to the vertebral column and ventrally to the sternum. It has two articulation surfaces on its dorsal end and is hence called bicephalic. First seven pairs of ribs are called true ribs. Dorsally, they are attached to the thoracic vertebrae and ventrally connected to the sternum with the help of hyaline cartilage.”  
  *locomotion and movement, page 225*
- **Note:** Every option bundles two numbers and a sentence of anatomy that must all hold together, which is why the shape is recorded as two_part rather than as four rival statements.
<!--/ecat-->

## Q145

Biology · both · Biotechnology: Principles and Processes

The DNA fragments separated on an agarose gel can be visualised after staining with

- (1) Bromophenol blue
- (2) Acetocarmine
- (3) Aniline blue
- **(4)** Ethidium bromide

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ethidium bromide is used to stain the DNA fragments and will appear as orange coloured bands under UV light.

**Solved independently** (answer withheld)

1. DNA fragments separated by agarose gel electrophoresis are stained with ethidium bromide, which intercalates into DNA and shows bright orange bands under UV light, so the answer is option $4$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 27)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q145_250bce3e_27102026.png?v=250bce3e3c40)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q145_b4dfbe66_27102026.png?v=b4dfbe667484)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA bands separated on an agarose gel are made visible by staining with ethidium bromide and exposing the gel to UV light
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Acetocarmine is the stain a student meets for DNA in the root-tip squash, so the question "which of these four stains DNA" lands there. It stains chromosomes in a fixed tissue; the bands in a gel are shown by ethidium bromide under UV.
- **Why:** This question requires the stated name of the stain used after electrophoresis, demonstrated by the stem asking what the separated fragments "can be visualised after staining with".
- **NCERT:** “The separated DNA fragments can be visualised only after staining the DNA with a compound known as ethidium bromide followed by exposure to UV radiation (you cannot see pure DNA fragments in the visible light and without staining).”  
  *biotechnology principles and processes, page 168*
<!--/ecat-->

## Q146

Biology · botany · Sexual Reproduction in Flowering Plants

Functional megaspore in an angiosperm develops into

- (1) Ovule
- (2) Endosperm
- **(3)** Embryo sac
- (4) Embryo

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Megaspore is the first cell of female gametophytic generation in angiosperm.
2. It undergoes three successive generations of free nuclear mitosis to form $8$-nucleated and $7$-celled embryo sac.

**Solved independently** (answer withheld)

1. In an angiosperm, the functional megaspore undergoes three successive free-nuclear mitoses ($2^3 = 8$ nuclei) and cell wall formation to give the 7-celled, 8-nucleate embryo sac, which is option $3$.

**Subtopic:** Megasporangium (Ovule) and Embryo Sac · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 27)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q146_960dc421_27102026.png?v=960dc4216562)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q146_9bb84504_27102026.png?v=9bb845044ca7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Of the four megaspores only one stays functional and grows into the embryo sac, the female gametophyte lying inside the ovule
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The chapter names the megasporangium and the ovule as the same thing in one breath, so a student holding "megaspore, megasporangium, ovule" as one chain concludes the megaspore grows into the ovule. The ovule is the structure that encloses the megaspore mother cell; what the functional megaspore becomes is the embryo sac inside it.
- **Why:** This question requires the stated fate of the functional megaspore, demonstrated by the four options being structures of the same ovule with no criterion printed to apply.
- **NCERT:** “Only the functional megaspore develops into the female gametophyte (embryo sac).”  
  *sexual reproduction in flowering plants, page 10*
<!--/ecat-->

## Q147

Biology · botany · Principles of Inheritance and Variation

Among the following characters, which one was not considered by Mendel in his experiments on pea?

- (1) Stem – Tall or Dwarf
- **(2)** Trichomes – Glandular or non-glandular
- (3) Seed – Green or Yellow
- (4) Pod – Inflated or Constricted

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. During his experiments Mendel studied seven characters.
2. Nature of trichomes i.e., glandular or non-glandular was not considered by Mendel.

**Solved independently** (answer withheld)

1. Mendel's seven contrasting characters were stem height, flower colour, flower position, pod shape, pod colour, seed shape and seed colour; stem (1), seed colour (3) and pod shape (4) are on the list, while trichomes (2) are not, so the answer is option $2$.

**Subtopic:** Contrasting Traits Studied by Mendel in Pea · **Difficulty:** easy (1 step, 1 of 4 options live)

**Printed in the booklet** (page 27)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q147_b68604b9_27102026.png?v=b68604b98edf)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q147_d55a4765_27102026.png?v=d55a47656ce7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mendel worked with seven pairs of contrasting pea characters, among them stem height, seed colour and pod shape; trichome type is not one of them
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The other three options name stem height, seed colour and pod shape, which are three of the seven characters printed in Mendel's own list, so none of them carries a changed or adjacent fact to reach for. The device sits in the keyed option, which fits the pea but is absent from that list.
- **Why:** This question requires Mendel's printed list of pea characters, demonstrated by option 2 reading "Trichomes – Glandular or non-glandular", which the list does not contain.
- **NCERT:** “S.No. | Characters | Contrasting Traits 1. | Stem height | Tall/dwarf 2. | Flower colour | Violet/white 3. | Flower position | Axial/terminal 4. | Pod shape | Inflated/constricted 5. | Pod colour | Green/yellow 6. | Seed shape | Round/wrinkled 7. | Seed colour | Yellow/green”  
  *principles of inheritance and variation, page 55*
<!--/ecat-->

## Q148

Biology · zoology · Breathing and Exchange of Gases

Lungs are made up of air-filled sacs the alveoli. They do not collapse even after forceful expiration, because of :

- **(1)** Residual Volume
- (2) Inspiratory Reserve Volume
- (3) Tidal Volume
- (4) Expiratory Reserve Volume

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Volume of air present in lungs after forceful expiration as residual volume which prevents the collapsing of alveoli even after forceful expiration.

**Solved independently** (answer withheld)

1. Even after a forceful expiration, a volume of air ($RV \approx 1100\text{--}1200\,\text{mL}$) stays in the lungs and cannot be expelled; this residual volume keeps the alveoli from collapsing, which is option $1$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q148_982d0db4_27102026.png?v=982d0db4d9fb)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q148_d54f9a79_27102026.png?v=d54f9a790727)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Residual volume is the air left in the lungs after the most forceful expiration, and it is what holds the alveoli open
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Expiratory reserve volume is defined as the extra air a person can push out by a forcible expiration, so the stem's words "forceful expiration" point straight at it. That volume is the air which leaves; what keeps the alveoli from collapsing is the air which stays behind.
- **Why:** This question requires the reason the alveoli stay inflated, demonstrated by the stem asking why "they do not collapse even after forceful expiration, because of".
- **NCERT:** “Residual Volume (RV): Volume of air remaining in the lungs even after a forcible expiration.”  
  *breathing and exchange of gases, page 187*
<!--/ecat-->

## Q149

Biology · zoology · Chemical Coordination and Integration

GnRH, a hypothalamic hormone, needed in reproduction, acts on

- (1) Anterior pituitary gland and stimulates secretion of LH and oxytocin
- **(2)** Anterior pituitary gland and stimulates secretion of LH and FSH
- (3) Posterior pituitary gland and stimulates secretion of oxytocin and FSH
- (4) Posterior pituitary gland and stimulates secretion of LH and relaxin

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Hypothalamus secretes GnRH which stimulates anterior pituitary gland for the secretion of gonadotropins (FSH and LH).

**Solved independently** (answer withheld)

1. GnRH (gonadotropin-releasing hormone) acts on the anterior pituitary and stimulates secretion of the gonadotropins LH and FSH, which is option $2$.

**Subtopic:** The Hypothalamus · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q149_88fd59bc_27102026.png?v=88fd59bca526)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q149_b902b665_27102026.png?v=b902b665f2c4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** GnRH from the hypothalamus acts on the anterior pituitary and drives the two gonadotropins, LH and FSH
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The lobe is right and so is LH, and oxytocin is the other pituitary hormone a student ties to reproduction, so most of the option checks out before the error is reached. Oxytocin comes from the posterior pituitary and is not under GnRH; the pair GnRH releases is LH and FSH.
- **Why:** This question requires the stated target of GnRH together with what it releases there, demonstrated by every option naming a pituitary lobe beside a pair of hormones.
- **NCERT:** “The increased levels of GnRH then acts at the anterior pituitary gland and stimulates secretion of two gonadotropins – luteinising hormone (LH) and follicle stimulating hormone (FSH).”  
  *human reproduction, page 31*
- **Note:** Each option bundles a lobe and two hormone names that must all hold together, which is what makes one part right and one part wrong possible here.
<!--/ecat-->

## Q150

Biology · botany · Morphology of Flowering Plants

In Bougainvillea thorns are the modifications of

- (1) Stipules
- (2) Adventitious root
- **(3)** Stem
- (4) Leaf

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Thorns are hard, pointed straight structures for protection.
2. These are modified stem

**Solved independently** (answer withheld)

1. Thorns of Bougainvillea develop from axillary buds, which are stem structures, so they are stem modifications (option $3$).

**Subtopic:** The Stem · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q150_d0cf0ca5_27102026.png?v=d0cf0ca5a610)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q150_c82c09d0_27102026.png?v=c82c09d03c0b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A thorn borne in the axil, as in Bougainvillea and Citrus, grows from an axillary bud and is therefore a stem modification
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The same chapter turns leaves into spines in Opuntia, so a student holding "thorns are modified leaves" carries that case across to Bougainvillea. The Bougainvillea thorn arises from an axillary bud, which places it with the stem modifications, beside the tendrils of grapevine.
- **Why:** This question requires the stated plant part a Bougainvillea thorn is derived from, demonstrated by the four options being coordinate plant parts with no criterion printed to apply.
<!--/ecat-->

## Q151

Biology · both · Principles of Inheritance and Variation

Which one from those given below is the period for Mendel's hybridization experiments?

- **(1)** 1856 - 1863
- (2) 1840 - 1850
- (3) 1857 - 1869
- (4) 1870 - 1877

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Mendel conducted hybridization experiments on Pea plant for 7 years between 1856 to 1863 and his data was published in 1865 (according to NCERT).

**Solved independently** (answer withheld)

1. Mendel conducted his hybridization experiments on garden pea for seven years, $1856$–$1863$, which is option $1$.

**Subtopic:** Principles of Laws of Inheritance · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q151_04c03a26_27102026.png?v=04c03a26ba9d)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q151_3efdf1a1_27102026.png?v=3efdf1a19188)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mendel ran his pea hybridisation experiments for seven years, from 1856 to 1863
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 4  
  The period is printed as seven years, 1856 to 1863, and "seven years" is the part a student carries away and checks against. 1870-1877 spans exactly seven years as well, so running that check confirms a wrong range instead of striking it out.
- **Proposed:** `passes_remembered_check` — the option is wrong on the fact but satisfies the one quantitative feature a student verifies, here the seven-year span that the source prints alongside the dates, so the check cannot separate it from the key. no_trap says nothing pulls, yet this option survives the student's own test; nearby_fact needs a true fact about an adjacent thing to be offered, and 1870-1877 is attached to nothing; arithmetic_slip needs an operation on the stem's numbers, and the stem supplies none.
- **Why:** This question requires the stored date of Mendel's experiments, demonstrated by the four options being bare year ranges with nothing in the stem to work from.
- **NCERT:** “Gregor Mendel, conducted hybridisation experiments on garden peas for seven years (1856-1863) and proposed the laws of inheritance in living organisms.”  
  *principles of inheritance and variation, page 54*
- **Note:** Two of the four ranges span exactly seven years, 1856-1863 and 1870-1877, so the duration the source states does not separate them.
<!--/ecat-->

## Q152

Biology · zoology · Neural Control and Coordination

Good vision depends on adequate intake of carotene rich food
Select the best option from the following statements

- **(a)** Vitamin A derivatives are formed from carotene
- **(b)** The photopigments are embedded in the membrane discs of the inner segment
- **(c)** Retinal is a derivative of vitamin A
- **(d)** Retinal is a light absorbing part of all the visual photopigments

- (1) (a) & (b)
- **(2)** (a), (c) & (d)
- (3) (a) & (c)
- (4) (b), (c) & (d)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Carotene is the source of retinal which is involved in formation of rhodopsin of rod cells.
2. Retinal, a derivative of vitamin A, is the light-absorbing part of all visual photopigments.

**Solved independently** (answer withheld)

1. Statement (a): carotene is cleaved to form vitamin A derivatives, so (a) is true.
2. Statement (b): the photopigments sit in the membrane discs of the outer segment of rods and cones, not the inner segment, so (b) is false.
3. Statement (c): retinal is the aldehyde derivative of vitamin A, so (c) is true.
4. Statement (d): retinal bound to opsin is the light-absorbing chromophore of all visual photopigments, so (d) is true.
5. True set $= \{a, c, d\}$, which is option $2$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** hard (4 steps, 3 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q152_bf98aefc_27102026.png?v=bf98aefc4a61)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q152_3a31a203_27102026.png?v=3a31a203a08f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Vision chemistry: carotene yields vitamin A, retinal is its derivative, and retinal is the light-absorbing group of every visual photopigment in the outer-segment discs
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The photopigments really do sit in stacked membrane discs, so a student who recalls the discs but not which end of the photoreceptor holds them accepts (b) and builds option 4. The discs are in the outer segment; the inner segment carries the mitochondria and the nucleus.
- **Why:** This question requires tracing carotene to vitamin A to retinal to the photopigments and rejecting the statement that misplaces them, demonstrated by (b) putting the photopigment-bearing membrane discs in 'the inner segment'.
<!--/ecat-->

## Q153

Biology · botany · Environmental Issues

Which one of the following statements is not valid for aerosols?

- (1) They are harmful to human health
- (2) They alter rainfall and monsoon patterns
- **(3)** They cause increased agricultural productivity
- (4) They have negative impact on agricultural land

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Aerosols can cause various problems to agriculture through its direct or indirect effects on plants.
2. However continually increasing air pollution may represent a persistent and largely irreversible threat to agriculture in the future.

**Solved independently** (answer withheld)

1. Aerosols (fine suspended particles) harm human health, alter rainfall and monsoon patterns and damage agricultural land, so options $1$, $2$ and $4$ are valid; increased agricultural productivity is not an effect of aerosols, so the invalid statement is option $3$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q153_92d3f8cf_27102026.png?v=92d3f8cf9e06)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q153_3566f92b_27102026.png?v=3566f92b2c3c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Aerosols harm human health, shift rainfall and monsoon patterns and damage farmland; nothing about them raises crop yield
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The other three options are the chapter's own claims about aerosols, so none of them offers a changed or adjacent fact to reach for. Options 3 and 4 are flatly contrary to each other about agriculture, which hands a student a route to the key rather than a pull onto a wrong option.
- **Why:** This question requires the stated effects of aerosols, demonstrated by option 3 reading "They cause increased agricultural productivity" while option 4 reads "They have negative impact on agricultural land".
<!--/ecat-->

## Q154

Biology · zoology · Excretory Products and Their Elimination

A decrease in blood pressure/volume will not cause the release of

- (1) Renin
- **(2)** Atrial Natriuretic Factor
- (3) Aldosterone
- (4) ADH

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A decrease in blood pressure / volume stimulates the release of renin, aldosterone, and ADH while increase in blood pressure / volume stimulates the release of Atrial Natriuretic Factor (ANF) which cause vasodilation and also inhibits RAAS (Renin Angiotensin Aldosterone System) mechanism that decreases the blood volume/pressure.

**Solved independently** (answer withheld)

1. A fall in blood pressure/volume activates the JG cells to release renin, which leads via angiotensin II to aldosterone release, and also stimulates ADH release; ANF is secreted by the atria only when blood pressure/volume rises, so the answer is option $2$.

**Subtopic:** Regulation Of Kidney Function · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q154_472a2160_27102026.png?v=472a21603432)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q154_4205f23f_27102026.png?v=4205f23f3472)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A fall in blood pressure or volume releases renin, aldosterone and ADH; ANF is the opposite signal, secreted when a rise stretches the atria
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  ADH is taught through the osmoreceptors, as the hormone released when the body loses water, so a student who files it under osmolarity rather than volume reads it as the one a pressure drop leaves alone. That fluid loss is itself the fall in blood volume, so ADH is released; the hormone of the opposite change is ANF from the stretched atria.
- **Why:** This question requires which hormones follow from a stated fall in blood pressure or volume, demonstrated by the stem printing that change and the options being four hormones of fluid balance.
- **NCERT:** “An increase in blood flow to the atria of the heart can cause the release of Atrial Natriuretic Factor (ANF).”  
  *excretory products and their elimination, page 212*
<!--/ecat-->

## Q155

Biology · zoology · Strategies for Enhancement in Food Production

Homozygous purelines in cattle can be obtained by

- **(1)** mating of related individuals of same breed
- (2) mating of unrelated individuals of same breed
- (3) mating of individuals of different breed
- (4) mating of individuals of different species

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Inbreeding results in increase in the homozygosity.
2. Therefore, mating of the related individuals of same breed will increase homozygosity.

**Solved independently** (answer withheld)

1. Inbreeding, i.e. mating of related individuals of the same breed over several generations, increases homozygosity and so produces homozygous purelines, which is option $1$.

**Subtopic:** Animal Breeding · **Difficulty:** medium (1 step, 2 of 4 options live)

**Printed in the booklet** (page 28)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q155_f68ed51f_27102026.png?v=f68ed51f0ae7)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q155_decd5dfa_27102026.png?v=decd5dfabf42)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inbreeding -- mating close relatives within one breed -- drives homozygosity and fixes a pureline, while outbreeding does the opposite
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A student who anchors on 'same breed' as the inbreeding cue, and remembers that a pureline is built inside one breed, reads option 2 as saying the same thing. Mating unrelated animals of one breed is out-crossing, the method used to break inbreeding depression, so it lowers homozygosity instead of raising it.
- **Why:** This question requires the stated fact that inbreeding yields homozygous purelines, demonstrated by the four options being the four named breeding methods given as definitions -- 'mating of related individuals of same breed' against unrelated, different breed and different species.
<!--/ecat-->

## Q156

Biology · botany · Anatomy of Flowering Plants

The vascular cambium normally gives rise to

- (1) Phelloderm
- (2) Primary phloem
- **(3)** Secondary xylem
- (4) Periderm

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. During secondary growth, vascular cambium gives rise to secondary xylem and secondary phloem.
2. Phelloderm is formed by cork cambium.

**Solved independently** (answer withheld)

1. The vascular cambium divides to cut off secondary xylem towards the inside and secondary phloem towards the outside, so it normally gives rise to secondary xylem, which is option $3$; phelloderm and periderm come from the cork cambium (phellogen), and primary phloem comes from the procambium.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q156_91233823_27102026.png?v=91233823b9bf)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q156_c0b25155_27102026.png?v=c0b251556207)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Vascular cambium adds secondary xylem inwards and secondary phloem outwards; the cork cambium is the meristem that makes phellem, phelloderm and so the periderm
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Phelloderm, and the periderm in option 4, both belong to secondary growth, so a student carrying one undifferentiated 'cambium' reaches for them. Those are the cork cambium's work -- cork outside, phelloderm inside -- while the vascular cambium's inward product is secondary xylem.
- **Also:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The vascular cambium does make phloem, so a student who stops at 'cambium makes xylem and phloem' accepts option 2. The primary phloem was laid down by the procambium before the cambium existed; what the cambium adds is secondary phloem.
- **Why:** This question requires the stated product of one named meristem, demonstrated by the stem 'The vascular cambium normally gives rise to' with four tissues of the same secondary-growth section as options.
- **NCERT:** “Such vascular bundles because of the presence of cambium possess the ability to form secondary xylem and phloem tissues, and hence are called open vascular bundles.”  
  *anatomy of flowering plants, page 73*
<!--/ecat-->

## Q157

Biology · zoology · Excretory Products and Their Elimination

Which of the following statements is correct?

- **(1)** The ascending limb of loop of Henle is impermeable to water
- (2) The descending limb of loop of Henle is impermeable to water
- (3) The ascending limb of loop of Henle is permeable to water
- (4) The descending limb of loop of Henle is permeable to electrolytes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Descending limb of loop of Henle is permeable to water but impermeable to electrolytes while ascending limb is impermeable to water but permeable to electrolytes.

**Solved independently** (answer withheld)

1. The ascending limb of the loop of Henle is impermeable to water and transports electrolytes out, so option $1$ is true and option $3$ is false.
2. The descending limb is permeable to water but almost impermeable to electrolytes, so options $2$ and $4$ are false.
3. Only option $1$ is correct.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** hard (2 steps, 4 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q157_9a1149d4_27102026.png?v=9a1149d4bb58)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q157_bcee59f0_27102026.png?v=bcee59f0ea5d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the loop of Henle the descending limb lets water out and the ascending limb does not; that split is what concentrates the urine
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The counter-current story leaves students holding 'the loop is impermeable to water' as a single slogan, and option 2 hangs it on the descending limb. The descending limb is the permeable one -- water leaves it -- and it is the ascending limb that water cannot cross.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Option 3 is the key's own sentence with the verdict flipped on the same limb, so a student who recalls that the limbs differ but not which way round can settle there. The ascending limb is impermeable to water and moves electrolytes out instead.
- **Why:** This question requires the NCERT sentence on loop-of-Henle permeability, demonstrated by the stem 'Which of the following statements is correct?' and four options that cross the two limbs with permeable and impermeable.
- **NCERT:** “The ascending limb is impermeable to water but allows transport of electrolytes actively or passively.”  
  *excretory products and their elimination, page 209*
<!--/ecat-->

## Q158

Biology · botany · Plant Growth and Development

Fruit and leaf drop at early stages can be prevented by the application of

- (1) Cytokinins
- (2) Ethylene
- **(3)** Auxins
- (4) Gibberellic acid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Auxins prevent premature leaf and fruit fall.
2. NAA prevents fruit drop in tomato; 2,4-D prevents fruit drop in Citrus.

**Solved independently** (answer withheld)

1. Auxins such as NAA, applied early, stop the abscission layer from forming and so prevent premature fruit and leaf drop. This is option $3$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q158_0f052872_27102026.png?v=0f0528724fdd)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q158_5de57c14_27102026.png?v=5de57c14aa3d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Auxin holds young fruits and leaves on the plant; ethylene is the hormone of abscission and ripening
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Ethylene is the regulator tied to fruit and leaf drop, so the phrase 'fruit and leaf drop' in the stem pulls a student straight to it. The stem asks what prevents the drop at early stages, and ethylene hastens abscission rather than preventing it.
- **Why:** This question requires the stated effect of one growth regulator, demonstrated by the stem 'Fruit and leaf drop at early stages can be prevented by the application of' with four named plant growth regulators as options.
- **NCERT:** “Auxins promote flowering e.g. in pineapples. They help to prevent fruit and leaf drop at early stages but promote the abscission of older mature leaves and fruits.”  
  *plant growth and development, page 175*
<!--/ecat-->

## Q159

Biology · zoology · Digestion and Absorption

A baby boy aged two years is admitted to play school and passes through a dental check-up. The dentist observed that the boy had twenty teeth. Which teeth were absent?

- (1) Incisors
- (2) Canines
- **(3)** Pre-molars
- (4) Molars

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Total number of teeth in human child $= 20$.
2. Premolars are absent in primary dentition.

**Solved independently** (answer withheld)

1. A two-year-old with $20$ teeth has the full deciduous (milk) set.
2. Deciduous dental formula per half jaw is $\frac{2102}{2102}$, i.e. $I\,2,\ C\,1,\ PM\,0,\ M\,2$, giving $5 \times 4 = 20$ teeth.
3. $PM = 0$, so the pre-molars are absent, which is option $3$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** medium (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q159_c73249a1_27102026.png?v=c73249a1e90f)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q159_d90cb0e9_27102026.png?v=d90cb0e94fa2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The milk dentition is twenty teeth and contains no premolars; premolars arrive only with the permanent set
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Premolars and molars both sit at the back of the jaw, so a student holding only 'the back teeth are not all in yet' takes molars. The milk set carries two molars in each half jaw; the class it has none of is the premolars.
- **Why:** This question requires the fact that the deciduous set of twenty teeth holds no premolars, demonstrated by the stem reporting that 'the boy had twenty teeth' and asking 'Which teeth were absent?' with four tooth classes as options.
<!--/ecat-->

## Q160

Biology · zoology · Animal Kingdom

An important characteristic that Hemichordates share with Chordates is

- (1) Absence of notochord
- (2) Ventral tubular nerve cord
- **(3)** Pharynx with gill slits
- (4) Pharynx without gill slits

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pharyngeal gill slits are present in hemichordates as well as in chordates.
2. Notochord is present in chordates only.
3. Ventral tubular nerve cord is characteristic feature of non-chordates.

**Solved independently** (answer withheld)

1. Hemichordates, like chordates, have a pharynx perforated by gill slits, while they lack a true notochord (the stomochord is not a notochord) and chordates have a dorsal, not ventral, tubular nerve cord, so the shared characteristic is option $3$.

**Subtopic:** Phylum – Echinodermata and Hemichordata · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q160_f54d687f_27102026.png?v=f54d687f422c)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q160_19d780d3_27102026.png?v=19d780d3b644)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pharyngeal gill slits are the chordate character hemichordates also show; the notochord is the one they lack
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The fact most students store about Hemichordata is the reason it was moved out of Chordata -- it has no notochord -- and option 1 prints exactly that. It is true of hemichordates but answers how they differ from chordates, whereas the stem asks for a character the two share.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who recalls 'a tubular nerve cord' as the chordate character but not its position takes option 2. In chordates that cord is dorsal; a ventral nerve cord is the invertebrate arrangement, as in earthworms and insects.
- **Why:** This question requires the stated chordate character that hemichordates also possess, demonstrated by the stem 'An important characteristic that Hemichordates share with Chordates is' and options that set presence against absence of notochord and of gill slits.
<!--/ecat-->

## Q161

Biology · zoology · Evolution

Artificial selection to obtain cows yielding higher milk output represents

- (1) Stabilizing selection as it stabilizes this character in the population
- **(2)** Directional as it pushes the mean of the character in one direction
- (3) Disruptive as it splits the population into two one yielding higher output and the other lower output
- (4) Stabilizing followed by disruptive as it stabilizes the population to produce higher yielding cows

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Artificial selection to obtain cow yielding higher milk output will shift the peak to one direction, hence, will be an example of Directional selection.
2. In stabilizing selection, the organisms with the mean value of the trait are selected.
3. In disruptive selection, both extremes get selected.

**Solved independently** (answer withheld)

1. Artificial selection for higher milk yield favours only the high-yield end of the trait distribution, so the population mean moves in one direction, which is directional selection (option $2$).

**Subtopic:** Types of Natural Selection · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q161_5a0d048a_27102026.png?v=5a0d048a554d)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q161_d4bd26f0_27102026.png?v=d4bd26f0dcf3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Directional selection shifts the population mean towards one extreme; stabilising selection holds the mean where it is and trims both extremes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Breeding a high-yield herd sounds like fixing a desirable character, and option 1's wording 'stabilizes this character in the population' matches that reading. Stabilising selection keeps the mean where it already is; breeding only from the highest yielders moves the mean upward, which is the directional case.
- **Why:** This question requires the criterion for one type of selection applied to a case the book does not list, demonstrated by option 2 carrying the test itself -- 'as it pushes the mean of the character in one direction'.
- **NCERT:** “Natural selection can lead to stabilisation (in which more individuals acquire mean character value), directional change (more individuals acquire value other than the mean character value) or disruption (more individuals acquire peripheral character value at both ends of the distribution curve) (Figure 6.8).”  
  *evolution, page 121*
<!--/ecat-->

## Q162

Biology · zoology · Structural Organisation in Animals

Select the correct route for the passage of sperms in male frogs :

- (1) Testes $\rightarrow$ Bidder's canal $\rightarrow$ Kidney $\rightarrow$ Vasa efferentia $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca
- (2) Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Seminal Vesicle $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca
- (3) Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Bidder's canal $\rightarrow$ Ureter $\rightarrow$ Cloaca
- **(4)** Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Bidder's canal $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In male frog the sperms will move from
2. Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Bidder’s canal $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca.

**Solved independently** (answer withheld)

1. In the male frog, sperms leave the testes through the vasa efferentia, which enter the kidney and open into Bidder's canal; Bidder's canal communicates with the urinogenital duct, which opens into the cloaca, so the route is Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Bidder's canal $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca, which is option $4$.

**Subtopic:** Anatomy of Frog · **Difficulty:** hard (2 steps, 3 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q162_ff7bcd4c_27102026.png?v=ff7bcd4cde52)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q162_8b53c916_27102026.png?v=8b53c916afbf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Frog sperm route: testes to vasa efferentia, through the kidney into Bidder's canal, then the urinogenital duct to the cloaca
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Option 2 is the key with one stop replaced, and the replacement is the seminal vesicle a student carries over from the mammalian tract of vas deferens, seminal vesicle and urethra. In the frog the sperm pass from the kidney into Bidder's canal, which is what leads them on to the urinogenital duct.
- **Also:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Option 1 keeps the right endpoints, testes and cloaca, and interchanges the first two stops, so a student who holds the organ names but not their order can accept it. Sperm enter the vasa efferentia first and reach Bidder's canal only after passing through the kidney.
- **Why:** This question requires the order of the ducts carrying sperm in the frog, demonstrated by the stem 'Select the correct route for the passage of sperms in male frogs' and four options built from the same organ names in different sequences.
- **NCERT:** “Vasa efferentia are 10-12 in number that arise from testes. They enter the kidneys on their side and open into Bidder’s canal. Finally it communicates with the urinogenital duct that comes out of the kidneys and opens into the cloaca.”  
  *structural organisation in animals, page 83*
<!--/ecat-->

## Q163

Biology · zoology · Digestion and Absorption

Which of the following options best represents the enzyme composition of pancreatic juice?

- (1) Amylase, peptidase, trypsinogen, rennin
- (2) Amylase, pepsin, trypsinogen, maltase
- (3) Peptidase, amylase, pepsin, rennin
- **(4)** Lipase, amylase, trypsinogen, procarboxy-peptidase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Rennin and Pepsin enzymes are present in the gastric juice.
2. Maltase is present in the intestinal juice.

**Solved independently** (answer withheld)

1. Pancreatic juice contains trypsinogen, chymotrypsinogen, procarboxypeptidases, amylase, lipases and nucleases; pepsin and rennin are gastric enzymes, so options $1$, $2$ and $3$ are out, leaving option $4$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 29)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q163_5cc29760_27102026.png?v=5cc2976015f0)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q163_4adb0fe5_27102026.png?v=4adb0fe5d699)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pancreatic juice carries trypsinogen, chymotrypsinogen, procarboxypeptidase, amylase, lipase and nucleases -- no pepsin and no rennin
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Option 1 opens with amylase and trypsinogen, both genuinely pancreatic, so a student who verifies the two names he is sure of and takes the rest on association accepts the set. Rennin is a gastric enzyme and the peptidases act at the intestinal brush border, so two of its four members are not in pancreatic juice at all.
- **Why:** This question requires the enzyme list given for pancreatic juice, demonstrated by the stem asking which option 'best represents the enzyme composition of pancreatic juice' with each option a set of four enzyme names.
<!--/ecat-->

## Q164

Biology · botany · Photosynthesis in Higher Plants

Phosphoenol pyruvate (PEP) is the primary $\mathrm{CO_2}$ acceptor in :

- (1) $\mathrm{C_3}$ plants
- **(2)** $\mathrm{C_4}$ plants
- (3) $\mathrm{C_2}$ plants
- (4) $\mathrm{C_3}$ and $\mathrm{C_4}$ plants

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. PEP is $3\mathrm{C}$ compound which serves as primary $\mathrm{CO_2}$ acceptor in the mesophyll cell cytoplasm of $\mathrm{C_4}$ plants like maize, sugarcane, *Sorghum* etc.

**Solved independently** (answer withheld)

1. In $\mathrm{C_4}$ plants, the primary $\mathrm{CO_2}$ acceptor in mesophyll cells is PEP, carboxylated by PEP carboxylase to oxaloacetate (OAA), while $\mathrm{C_3}$ plants use RuBP, so the answer is option $2$.

**Subtopic:** The C₄ Pathway · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q164_1975ecd4_27102026.png?v=1975ecd474aa)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q164_8326dca4_27102026.png?v=8326dca497b0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** PEP is the primary CO2 acceptor in the mesophyll of C4 plants; RuBP is the acceptor of the Calvin cycle
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The C3 pathway is the one taught first and PEP is itself a three-carbon acid, so a student matching the '3' in the molecule to the '3' in C3 lands on option 1. The C3 acceptor is the five-carbon RuBP; PEP takes up CO2 in C4 mesophyll cells and gives the four-carbon acid that names the pathway.
- **Why:** This question requires the stated identity of the primary CO2 acceptor of one pathway, demonstrated by the stem 'Phosphoenol pyruvate (PEP) is the primary CO2 acceptor in' with the plant classes C3, C4, C2 and both as options.
- **NCERT:** “The primary CO₂ acceptor is a 3-carbon molecule phosphoenol pyruvate (PEP) and is present in the mesophyll cells.”  
  *photosynthesis in higher plants, page 146*
<!--/ecat-->

## Q165

Biology · botany · Sexual Reproduction in Flowering Plants

The morphological nature of the edible part of coconut is

- (1) Perisperm
- (2) Cotyledon
- **(3)** Endosperm
- (4) Pericarp

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Coconut has double endosperm with liquid endosperm and cellular endosperm.

**Solved independently** (answer withheld)

1. In coconut, the edible white kernel is cellular endosperm and the coconut water is free-nuclear endosperm, so the edible part is the $\text{endosperm}$, which is option $3$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q165_0d0adefa_27102026.png?v=0d0adefac78e)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q165_f66251c1_27102026.png?v=f66251c181c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Both the water and the white kernel of a coconut are endosperm; perisperm is leftover nucellus, as in black pepper and beet
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Perisperm is printed a line away from endosperm in the account of seed structure and the two names differ by one syllable, so a student who recalls that the coconut's flesh is a '-sperm' tissue can take option 1. The perisperm is persistent nucellus and appears in black pepper and beet, not as the stored food of a coconut.
- **Why:** This question requires the stated morphological identity of one edible part, demonstrated by the stem 'The morphological nature of the edible part of coconut is' with four seed and fruit tissues as options.
- **NCERT:** “The coconut water from tender coconut that you are familiar with, is nothing but free-nuclear endosperm (made up of thousands of nuclei) and the surrounding white kernel is the cellular endosperm.”  
  *sexual reproduction in flowering plants, page 18*
<!--/ecat-->

## Q166

Biology · both · Cell Cycle and Cell Division

Anaphase promoting complex (APC) is a protein degradation machinery necessary for proper mitosis of animal cells. If APC is defective in a human cell, which of the following is expected to occur?

- (1) Chromosomes will not condense
- (2) Chromosomes will be fragmented
- **(3)** Chromosomes will not segregate
- (4) Recombination of chromosome arms will occur

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Anaphase Promoting Complex (APC) is a protein necessary for separation of daughter chromosomes during anaphase.
2. If APC is defective then the chromosomes will fail to segregate during anaphase.

**Solved independently** (answer withheld)

1. APC/C ubiquitinates securin (and mitotic cyclin) to trigger the metaphase-to-anaphase transition; if APC is defective, securin is not degraded, separase stays inactive, cohesin is not cleaved, and the sister chromatids cannot separate, so chromosomes will not segregate, which is option $3$.

**Subtopic:** Cytokinesis and Significance of Mitosis · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q166_d793a90e_27102026.png?v=d793a90eb8cb)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q166_763cedaf_27102026.png?v=763cedafb1cd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Anaphase is the stage at which sister chromatids separate, so a complex named for promoting anaphase is required for segregation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The stem describes APC only as 'necessary for proper mitosis' and names no stage, so a student who does not read 'anaphase' out of the acronym picks the first visible event of mitosis -- chromosomes condensing. Condensation belongs to prophase and happens whatever APC does; what fails at anaphase is the separation of the sister chromatids.
- **Why:** This question requires the function of one named stage applied to a defect the book does not discuss, demonstrated by the stem defining APC as 'a protein degradation machinery necessary for proper mitosis' and then asking what is expected to occur if it is defective.
- **NCERT:** “At the onset of anaphase, each chromosome arranged at the metaphase plate is split simultaneously and the two daughter chromatids, now referred to as daughter chromosomes of the future daughter nuclei, begin their migration towards the two opposite poles.”  
  *cell cycle and cell division, page 123*
- **Note:** The anaphase promoting complex is not named in the chapter; the stem supplies its definition, so the question is answerable from the acronym plus what anaphase does.
<!--/ecat-->

## Q167

Biology · zoology · Human Health and Disease

MALT constitutes about ___________ percent of the lymphoid tissue in human body.

- **(1)** $50\%$
- (2) $20\%$
- (3) $70\%$
- (4) $10\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. MALT is Mucosa Associated Lymphoid Tissue and it constitutes about $50$ percent of the lymphoid tissue in human body.

**Solved independently** (answer withheld)

1. MALT (mucosa-associated lymphoid tissue) lining the respiratory, digestive and urogenital tracts constitutes about $50\%$ of the lymphoid tissue in the human body, which is option $1$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** medium (1 step, 4 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q167_f4c61ecb_27102026.png?v=f4c61ecb5717)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q167_45bfb106_27102026.png?v=45bfb10628fa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** MALT -- the lymphoid tissue lining the gut, airways and urogenital tract -- is about half of all the lymphoid tissue in the body
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stem supplies no quantity to work from, and the three wrong options are bare percentages -- 20, 70 and 10 -- with no stated figure or computation leading to any one of them in preference to the others.
- **Why:** This question requires a stored percentage, demonstrated by the printed blank in 'MALT constitutes about ___________ percent of the lymphoid tissue in human body' with four bare percentages as options.
- **NCERT:** “There is lymphoid tissue also located within the lining of the major tracts (respiratory, digestive and urogenital tracts) called mucosa-associated lymphoid tissue (MALT). It constitutes about 50 per cent of the lymphoid tissue in human body.”  
  *human health and disease, page 138*
<!--/ecat-->

## Q168

Biology · zoology · Neural Control and Coordination

Receptor sites for neurotransmitters are present on

- (1) Membranes of synaptic vesicles
- (2) Pre-synaptic membrane
- (3) Tips of axons
- **(4)** Post-synaptic membrane

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Pre-synaptic membrane is involved in the release of neurotransmitter in the chemical synapse.
2. The receptors sites for neurotransmitters are present on post-synaptic membrane.

**Solved independently** (answer withheld)

1. Neurotransmitters released from synaptic vesicles into the synaptic cleft bind to specific receptors located on the post-synaptic membrane, which is option $4$.

**Subtopic:** Transmission of Impulses · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q168_cb458db3_27102026.png?v=cb458db3f58f)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q168_73e84353_27102026.png?v=73e843532b0b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Neurotransmitter is released from the pre-synaptic membrane and binds receptors on the post-synaptic membrane
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The pre-synaptic membrane is the part of the synapse that the account of transmission ties to neurotransmitters -- the vesicles fuse there and release them -- so a student storing 'neurotransmitter goes with the pre-synaptic membrane' takes option 2. Release happens there; the receptors that bind the transmitter sit on the membrane across the cleft.
- **Why:** This question requires the location of one named site, demonstrated by the stem 'Receptor sites for neurotransmitters are present on' with four parts of the same synapse as options.
- **NCERT:** “The released neurotransmitters bind to their specific receptors, present on the post-synaptic membrane.”  
  *neural control and coordination, page 234*
<!--/ecat-->

## Q169

Biology · zoology · Chemical Coordination and Integration

Hypersecretion of Growth Hormone in adults does not cause further increase in height, because

- (1) Growth Hormone becomes inactive in adults
- **(2)** Epiphyseal plates close after adolescence
- (3) Bones loose their sensitivity to Growth Hormone in adults
- (4) Muscle fibres do not grow in size after birth

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Epiphyseal plate is responsible for the growth of bone which close after adolescence so hypersecretion of growth hormone in adults does not cause further increase in height.

**Solved independently** (answer withheld)

1. Longitudinal bone growth, and therefore height, happens only at open epiphyseal plates; these close (ossify) after adolescence, so adult GH hypersecretion causes acromegaly instead of more height, which is option $2$.

**Subtopic:** The Pituitary Gland · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q169_875d9da1_27102026.png?v=875d9da1f1e0)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q169_85d72a95_27102026.png?v=85d72a95cb3f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Growth hormone can lengthen a bone only while its epiphyseal plate is open; after adolescence the plate closes and excess GH thickens bone instead
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student who has got as far as 'what changed is the bone, not the hormone' but cannot name the epiphyseal plate takes option 3's loss of sensitivity. Adult bone does still answer to growth hormone -- that answer is acromegaly, the thickening of jaw, hands and feet -- so what has gone is the growth plate where length was added, not the responsiveness.
- **Why:** This question requires the reason height stops responding to growth hormone, demonstrated by the stem's trailing 'because' and four rival explanations as options.
- **NCERT:** “Excess secretion of growth hormone in adults especially in middle age can result in severe disfigurement (especially of the face) called Acromegaly, which may lead to serious complications, and premature death if unchecked.”  
  *chemical coordination and integration, page 241*
<!--/ecat-->

## Q170

Biology · botany · Biodiversity and Conservation

Alexander Von Humbolt described for the first time

- (1) Ecological Biodiversity
- (2) Laws of limiting factor
- **(3)** Species area relationships
- (4) Population Growth equation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Alexander Von Humboldt observed that within a region species richness increases with the increases in area.

**Solved independently** (answer withheld)

1. Alexander von Humboldt was the first to describe the species-area relationship, where species richness $S$ rises with area $A$ as $\log S = \log C + Z \log A$, which is option $3$.

**Subtopic:** Species–Area Relationships · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q170_fe74b2df_27102026.png?v=fe74b2df8053)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q170_819b8511_27102026.png?v=819b8511e186)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Humboldt's species-area relationship: species richness rises with the area explored, up to a limit
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Two of the three wrong options are real ecological results that the chapters attribute to other named people -- the law of limiting factors and the logistic population growth equation -- and the third, 'Ecological Biodiversity', is not a term the chapter uses at all. Nothing in the stem narrows them, so no single option carries the misattribution.
- **Why:** This question requires an attribution, demonstrated by the stem 'Alexander Von Humbolt described for the first time' with four named ecological results as options.
- **NCERT:** “(ii) Species-Area relationships: During his pioneering and extensive explorations in the wilderness of South American jungles, the great German naturalist and geographer Alexander von Humboldt observed that within a region species richness increased with increasing explored area, but only up to a limit.”  
  *biodiversity and conservation, page 220*
<!--/ecat-->

## Q171

Biology · zoology · Neural Control and Coordination

Myelin sheath is produced by

- **(1)** Schwann Cells and Oligodendrocytes
- (2) Astrocytes and Schwann Cells
- (3) Oligodendrocytes and Osteoclasts
- (4) Osteoclasts and Astrocytes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Oligodendrocytes are neuroglial cells which produce myelin sheath in central nervous system while Schwann cell produces myelin sheath in peripheral nervous system.

**Solved independently** (answer withheld)

1. Myelin sheath is formed by Schwann cells in the peripheral nervous system and by oligodendrocytes in the central nervous system, while astrocytes are supporting glia and osteoclasts are bone-resorbing cells, so the answer is option $1$.

**Subtopic:** Neuron as Structural and Functional Unit of Neural System and Types of Axon · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q171_1e5acb2c_27102026.png?v=1e5acb2cf9dc)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q171_7eb3c5f7_27102026.png?v=7eb3c5f79ba4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Schwann cells myelinate peripheral axons and oligodendrocytes myelinate axons inside the central nervous system
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Schwann cells are the myelinating cell recalled first and astrocytes are the glial cell named next to them, so option 2 reads as 'the two glial cells' and half of it is correct. Astrocytes support and feed neurons but lay down no myelin; the central myelin comes from the oligodendrocytes that option 2 leaves out.
- **Why:** This question requires the two cell types that lay down myelin, demonstrated by the stem 'Myelin sheath is produced by' and each option naming a pair of cells to be accepted or rejected whole.
- **NCERT:** “The myelinated nerve fibres are enveloped with Schwann cells, which form a myelin sheath around the axon.”  
  *neural control and coordination, page 231*
<!--/ecat-->

## Q172

Biology · zoology · Reproductive Health

In case of a couple where the male is having a very low sperm count, which technique will be suitable for fertilisation?

- (1) Intrauterine transfer
- (2) Gamete intracytoplasmic fallopian transfer
- **(3)** Artificial Insemination
- (4) Intracytoplasmic sperm injection

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Infertility cases due to inability of the male partner to inseminate the female or due to very low sperm count in the ejaculates, could be corrected by artificial insemination (AI).

**Solved independently** (answer withheld)

1. NCERT Class 12 (Reproductive Health) states that infertility due to the male's inability to inseminate or due to very low sperm counts in the ejaculate can be corrected by artificial insemination (AI), so the answer is option $3$.

**Subtopic:** Assisted Reproductive Technologies (ART) · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 30)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q172_54889154_27102026.png?v=5488915469eb)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q172_1c7c3c4c_27102026.png?v=1c7c3c4cbb90)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Artificial insemination is the technique prescribed when the male's sperm count is very low -- semen is introduced into the vagina or the uterus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  ICSI is the neighbouring technique in the same list of assisted technologies, described as injecting a sperm directly into the ovum, so a student reasoning from a shortage of sperm to 'then place one sperm inside the egg' takes option 4. The sentence that names a very low sperm count is the artificial insemination one, where the semen is introduced into the vagina or the uterus.
- **Why:** This question requires the technique the book ties to one named condition, demonstrated by the stem 'In case of a couple where the male is having a very low sperm count, which technique will be suitable for fertilisation?' with four named assisted reproductive procedures as options.
- **NCERT:** “Infertility cases either due to inability of the male partner to inseminate the female or due to very low sperm counts in the ejaculates, could be corrected by artificial insemination (AI) technique.”  
  *reproductive health, page 48*
- **Note:** Option 4, intracytoplasmic sperm injection, is defensible on clinical grounds for a very low sperm count; the printed key rests on the textbook sentence that names this condition under artificial insemination, and the tags follow the printed key. Option 2 as printed, 'Gamete intracytoplasmic fallopian transfer', conflates the names of two different procedures.
<!--/ecat-->

## Q173

Biology · both · Cell: The Unit of Life

Which of the following components provides sticky character to the bacterial cell?

- (1) Cell wall
- (2) Nuclear membrane
- (3) Plasma membrane
- **(4)** Glycocalyx

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sticky character of the bacterial wall is due to glycocalyx or slime layer.
2. This layer is rich in glycoproteins.

**Solved independently** (answer withheld)

1. In bacteria the outermost part of the cell envelope is the glycocalyx (a loose slime layer or a thick capsule), and it gives the cell its sticky character, so the answer is option $4$.

**Subtopic:** Prokaryotic Cells And Its Modification · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q173_62d4d514_27102026.png?v=62d4d5147f76)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q173_8b56f2c3_27102026.png?v=8b56f2c3a667)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The glycocalyx is the outermost layer of the bacterial cell envelope, the slime or capsule that makes the cell sticky
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The bacterial envelope is taught as three bound layers in order, glycocalyx then cell wall then plasma membrane, so a student holding 'the cell wall is the tough outer coat of a bacterium' stops at the wall. The wall gives rigidity and shape; the sticky slime or capsule lying outside it is the glycocalyx.
- **Why:** This question requires the stated fact about which envelope layer is sticky, demonstrated by 'Cell wall', 'Plasma membrane' and 'Glycocalyx' being three named layers of the same bacterial envelope with no criterion printed to apply.
- **NCERT:** “Glycocalyx differs in composition and thickness among different bacteria. It could be a loose sheath called the slime layer in some, while in others it may be thick and tough, called the capsule.”  
  *cell the unit of life, page 90*
<!--/ecat-->

## Q174

Biology · both · Molecular Basis of Inheritance

DNA replication in bacteria occurs

- (1) During S-phase
- (2) Within nucleolus
- **(3)** Prior to fission
- (4) Just before transcription

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. DNA replication in bacteria occurs prior to fission.
2. Prokaryotes do not show well marked S-phase due to their primitive nature.

**Solved independently** (answer withheld)

1. Bacteria are prokaryotes with no nucleus or nucleolus, so option $2$ is wrong, and they have no eukaryotic cell cycle with an S-phase, so option $1$ is wrong.
2. Transcription in bacteria goes on continuously and does not wait on replication, so option $4$ is wrong.
3. The bacterial chromosome must be copied before the cell divides into two by binary fission, so DNA replication occurs prior to fission, which is option $3$.

**Subtopic:** Replication · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q174_98dc3a2b_27102026.png?v=98dc3a2bc2a3)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q174_15e36546_27102026.png?v=15e3654695dd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bacteria run no G1-S-G2-M cycle, so the chromosome replicates and segregates immediately before binary fission
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'DNA replicates during S phase' is the line carried over from the eukaryotic cell cycle, and the stem's bare wording 'DNA replication in bacteria occurs' invites it unchanged. Bacteria have no S phase to put it in, so the event is timed to the division itself.
- **Why:** This question requires the stated timing of bacterial DNA replication, demonstrated by the key option 'Prior to fission' naming the division event where the other options name cell-cycle phases and sites.
- **NCERT:** “In eukaryotes, the replication of DNA takes place at S-phase of the cell-cycle.”  
  *molecular basis of inheritance, page 91*
<!--/ecat-->

## Q175

Biology · zoology · Reproductive Health

The function of copper ions in copper releasing IUD's is :

- **(1)** They suppress sperm motility and fertilising capacity of sperms
- (2) They inhibit gametogenesis
- (3) They make uterus unsuitable for implantation
- (4) They inhibit ovulation

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{Cu^{2+}}$ interfere in the sperm movement, hence suppress the sperm motility and fertilising capacity of sperms.

**Solved independently** (answer withheld)

1. Copper-releasing IUDs (e.g. $\text{CuT}$, $\text{Cu7}$, Multiload 375) release $\text{Cu}^{2+}$ ions that suppress sperm motility and the fertilising capacity of sperms, which is option $1$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (1 step, 3 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q175_4febdf03_27102026.png?v=4febdf03e427)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q175_ff824124_27102026.png?v=ff824124a60e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Copper-releasing IUDs act by Cu ions suppressing sperm motility and fertilising capacity; it is the hormone-releasing IUDs that make the uterus unsuitable for implantation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  'Makes the uterus unsuitable for implantation' is the textbook function of the hormone-releasing IUD, the next device in the same list of intrauterine devices, so a student who stores one mechanism for all IUDs reaches for it. The stem asks about copper ions, which act on the sperms rather than on the endometrium.
- **Why:** This question requires the stated function of one named contraceptive device, demonstrated by the stem 'The function of copper ions in copper releasing IUD's is' naming copper ions rather than IUDs in general.
- **NCERT:** “IUDs increase phagocytosis of sperms within the uterus and the Cu ions released suppress sperm motility and the fertilising capacity of sperms.”  
  *reproductive health, page 44*
<!--/ecat-->

## Q176

Biology · botany · Microbes in Human Welfare

Which of the following in sewage treatment removes suspended solids?

- (1) Tertiary treatment
- (2) Secondary treatment
- **(3)** Primary treatment
- (4) Sludge treatment

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Primary treatment is a physical process which involves sequential filtration and sedimentation.

**Solved independently** (answer withheld)

1. Primary treatment is the physical stage of sewage treatment, in which floating debris and suspended solids are removed by sequential filtration and sedimentation, so the answer is option $3$.

**Subtopic:** Microbes in Sewage Treatment · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q176_5c39bc5a_27102026.png?v=5c39bc5a0dc1)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q176_6e0dd04d_27102026.png?v=6e0dd04d1b02)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Primary sewage treatment is physical, filtration and sedimentation taking out floating debris and suspended solids; secondary treatment is biological and lowers the BOD
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Secondary treatment is the stage the chapter spends its detail on, with flocs, aeration and BOD, so a student holding 'secondary treatment is the step that actually cleans the sewage' picks it. Taking out suspended solids is the sedimentation step, which sits in primary treatment.
- **Why:** This question requires the stated job of one named stage, demonstrated by the four options being the successive named stages of the same sewage plant, 'Tertiary', 'Secondary', 'Primary' and 'Sludge treatment'.
- **NCERT:** “Primary treatment : These treatment steps basically involve physical removal of particles – large and small – from the sewage through filtration and sedimentation.”  
  *microbes in human welfare, page 154*
<!--/ecat-->

## Q177

Biology · botany · Transport in Plants

The water potential of pure water is

- **(1)** Zero
- (2) Less than zero
- (3) More than zero but less than one
- (4) More than one

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. By convention, the water potential of pure water at standard temperature, which is not under any pressure, is taken to be zero.

**Solved independently** (answer withheld)

1. By convention, pure water at standard temperature and pressure has $\Psi_w = 0$ (solute potential $\Psi_s = 0$, pressure potential $\Psi_p = 0$), so the answer is option $1$ (Zero).

**Subtopic:** Water Potential · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q177_e1c5ed91_27102026.png?v=e1c5ed9142a3)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q177_604e3faa_27102026.png?v=604e3faabee5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Water potential is measured from pure water, which is fixed at zero; adding solute can only pull it below zero
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Every water potential a student handles comes out negative, because solute potential is negative, so 'water potential is less than zero' gets carried as the rule. That rule holds for any solution, which is exactly what the stem's word 'pure' rules out: pure water is the zero the scale is measured against.
- **Why:** This question requires the stated reference value of water potential, demonstrated by the stem specifying 'pure water' and the options spanning zero and the ranges either side of it.
<!--/ecat-->

## Q178

Biology · botany · Anatomy of Flowering Plants

Identify the wrong statement in context of heartwood.

- (1) Organic compounds are deposited in it
- (2) It is highly durable
- **(3)** It conducts water and minerals efficiently
- (4) It comprises dead elements with highly lignified walls

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Heartwood is physiologically inactive due to deposition of organic compounds and tyloses formation, so this will not conduct water and minerals.

**Solved independently** (answer withheld)

1. Heartwood consists of dead elements with highly lignified walls filled with organic compounds (tannins, resins, gums), which make it durable, but it does not conduct water and minerals; that is done by sapwood, so the wrong statement is option $3$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (2 steps, 2 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q178_78baf9a2_27102026.png?v=78baf9a2fffd)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q178_a22ebd89_27102026.png?v=a22ebd892246)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Heartwood is dead, highly lignified and filled with deposited organic compounds, so it is durable but conducts nothing; conduction is the sapwood's job
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who has heartwood and sapwood the wrong way round reads 'conducts water and minerals efficiently' as a true heartwood fact, and then the one statement that contradicts conduction, dead elements with highly lignified walls, reads as the wrong one. Those dead lignified elements are what heartwood is; efficient conduction belongs to the sapwood.
- **Why:** This question requires the stated facts about heartwood, demonstrated by the stem 'Identify the wrong statement in context of heartwood' standing over three options that restate the heartwood description and one that states the sapwood's role.
<!--/ecat-->

## Q179

Biology · zoology · Principles of Inheritance and Variation

Thalassemia and sickle cell anemia are caused due to a problem in globin molecule synthesis. Select the correct statement.

- (1) Both are due to a qualitative defect in globin chain synthesis
- (2) Both are due to a quantitative defect in globin chain synthesis
- **(3)** Thalassemia is due to less synthesis of globin molecules
- (4) Sickle cell anemia is due to a quantitative problem of globin molecules

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Thalassemia differs from sickle-cell anaemia in that the former is a quantitative problem of synthesising too few globin molecules while the latter is a qualitative problem of synthesising an incorrectly functioning globin.

**Solved independently** (answer withheld)

1. Thalassemia results from mutation or deletion that reduces or stops synthesis of $\alpha$ or $\beta$ globin chains, i.e. a quantitative problem: fewer globin molecules are made.
2. Sickle cell anemia results from a single substitution ($\text{Glu} \rightarrow \text{Val}$ at the 6th position of $\beta$-globin), i.e. a qualitative problem: a faulty globin is made.
3. So options $1$, $2$ and $4$ are false and option $3$ is correct.

**Subtopic:** Thalassemia, Sickle-cell Anaemia · **Difficulty:** hard (2 steps, 4 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q179_844534e9_27102026.png?v=844534e9f0dc)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q179_39a7c236_27102026.png?v=39a7c23635dd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Thalassemia is a quantitative defect, too few globin chains made; sickle cell anaemia is a qualitative defect, a normal amount of a wrongly built globin chain
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The words quantitative and qualitative are learnt as a pair tied to these two disorders, and a student who keeps the pair but loses which goes with which hangs 'quantitative' on sickle cell anaemia. Option 4 is that pair stated backwards: the quantitative defect is thalassemia's, and sickle cell anaemia makes enough globin, just the wrong globin.
- **Why:** This question requires the difference between two named disorders on one axis, demonstrated by the options setting 'a qualitative defect' against 'a quantitative defect' for the same two diseases named in the stem.
- **NCERT:** “Thalassemia differs from sickle-cell anaemia in that the former is a quantitative problem of synthesising too few globin molecules while the latter is a qualitative problem of synthesising an incorrectly functioning globin.”  
  *principles of inheritance and variation, page 75*
<!--/ecat-->

## Q180

Biology · botany · Sexual Reproduction in Flowering Plants

Flowers which have single ovule in the ovary and are packed into inflorescence are usually pollinated by

- (1) Water
- (2) Bee
- **(3)** Wind
- (4) Bat

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Wind pollination or anemophily is favoured by flowers having a single ovule in each ovary, and numerous flowers packed in an inflorescence.
2. Wind pollination is a non-directional pollination.

**Solved independently** (answer withheld)

1. Flowers with a single ovule per ovary and many flowers packed into an inflorescence (e.g. the corn cob, grasses) are characteristic of wind pollination, which is option $3$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step, 2 of 4 options live)

**Printed in the booklet** (page 31)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/crops/q180_e0356a83_27102026.png?v=e0356a83502a)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2017/2017_A/solutions/q180_08c55dda_27102026.png?v=08c55ddaf8a4)

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Wind-pollinated flowers carry a single ovule per ovary and crowd many flowers into an inflorescence, the maize cob being the standard example
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Insect pollination is the syndrome taught in most detail, and 'packed into inflorescence' reads like a showy composite head built to advertise to a bee. Bee-pollinated flowers are the large, coloured, scented, nectar-bearing kind; a single ovule per ovary with crowded flowers is the wind-pollination description.
- **Why:** This question requires the stated features of one pollination agent's flowers, demonstrated by the stem reproducing them as given, 'single ovule in the ovary and are packed into inflorescence', with the four options being the four named agents.
- **NCERT:** “Wind-pollinated flowers often have a single ovule in each ovary and numerous flowers packed into an inflorescence; a familiar example is the corn cob – the ears you see are nothing but the stigma and style which wave in the wind to trap pollen grains.”  
  *sexual reproduction in flowering plants, page 13*
<!--/ecat-->

