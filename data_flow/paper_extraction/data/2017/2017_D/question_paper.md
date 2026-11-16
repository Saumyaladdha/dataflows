# NEET (UG) 2017 · Code D

180 questions · source `NEET_Papers/2017/NEET_2017_Code_D_official.pdf` · every image a CDN link (0 without one) · 47 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Waves

The two nearest harmonics of a tube closed at one end and open at other end are $220\,\mathrm{Hz}$ and $260\,\mathrm{Hz}$. What is the fundamental frequency of the system?

- (1) $30\,\mathrm{Hz}$
- (2) $40\,\mathrm{Hz}$
- (3) $10\,\mathrm{Hz}$
- **(4)** $20\,\mathrm{Hz}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Two successive frequencies of closed pipe
2. $\frac{nv}{4l} = 220$ ...(i)
3. $\frac{(n + 2)v}{4l} = 260$ ...(ii)
4. Dividing (ii) by (i), we get
5. $\frac{n + 2}{n} = \frac{260}{220} = \frac{13}{11}$
6. $11n + 22 = 13n$
7. $n = 11$
8. So, $11\frac{v}{4l} = 220$
9. $\frac{v}{4l} = 20$
10. So fundamental frequency is $20\,\mathrm{Hz}$.

**Solved independently** (answer withheld)

1. A tube closed at one end supports only odd harmonics: $f = (2n-1) f_0$.
2. Two nearest harmonics differ by $2f_0$: $2f_0 = 260\,\mathrm{Hz} - 220\,\mathrm{Hz} = 40\,\mathrm{Hz}$.
3. $f_0 = \frac{40}{2} = 20\,\mathrm{Hz}$.
4. Check: $\frac{220}{20} = 11$ and $\frac{260}{20} = 13$ are consecutive odd integers, so $f_0 = 20\,\mathrm{Hz}$, which is option $4$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q001_fbeb5914_30102026.png?v=fbeb59143291)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q001_9e36a13f_30102026.png?v=9e36a13f4fb3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A pipe closed at one end sounds only the odd harmonics, so two successive harmonics are separated by twice the fundamental
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The gap between the two printed frequencies, $260-220=40$ Hz, is handed in as the fundamental, which is the rule for a pipe open at BOTH ends, so the stem's 'closed at one end' never enters the arithmetic.
- **Why:** This question requires the harmonic spacing of a pipe closed at one end to be applied to a printed pair of frequencies, demonstrated by 'The two nearest harmonics of a tube closed at one end and open at other end are $220\,\mathrm{Hz}$ and $260\,\mathrm{Hz}$'.
<!--/ecat-->

## Q2

Physics · Mechanical Properties of Fluids

A U tube with both ends open to the atmosphere, is partially filled with water. Oil, which is immiscible with water, is poured into one side until it stands at a distance of $10\,\mathrm{mm}$ above the water level on the other side. Meanwhile the water rises by $65\,\mathrm{mm}$ from its original level (see diagram). The density of the oil is

![printed figure: U-tube: oil column AB in the left limb, water rising from D to E in the right limb](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q002_c722a2f0_30102026.svg?v=c722a2f00263)

*U-tube: oil column AB in the left limb, water rising from D to E in the right limb*

![drawn: U-tube: oil column AB in the left limb, water rising from D to E in the right limb](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q002_question_d0c24347_30102026.svg?v=d0c2434722a0)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $800\,\mathrm{kg\,m^{-3}}$
- **(2)** $928\,\mathrm{kg\,m^{-3}}$
- (3) $650\,\mathrm{kg\,m^{-3}}$
- (4) $425\,\mathrm{kg\,m^{-3}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $h_{\mathrm{oil}}\,\rho_{\mathrm{oil}}\,g = h_{\mathrm{water}}\,\rho_{\mathrm{water}}\,g$
2. $140 \times \rho_{\mathrm{oil}} = 130 \times \rho_{\mathrm{water}}$
3. $\rho_{\mathrm{oil}} = \frac{13}{14} \times 1000\,\mathrm{kg/m^{3}}$
4. $\rho_{\mathrm{oil}} = 928\,\mathrm{kg\,m^{-3}}$

**Solved independently** (answer withheld)

1. Water rises $65\,\mathrm{mm}$ on the right, so it falls $65\,\mathrm{mm}$ on the oil side; the oil-water interface $B$ is $130\,\mathrm{mm}$ below the final water level $E$.
2. Oil top $A$ is $10\,\mathrm{mm}$ above $E$, so $h_{oil} = 65 + 65 + 10 = 140\,\mathrm{mm}$.
3. Water column above level $BC$ on the right: $h_w = 65 + 65 = 130\,\mathrm{mm}$.
4. Equal pressures at $B$ and $C$: $P_a + \rho_{oil} g h_{oil} = P_a + \rho_w g h_w$.
5. $\rho_{oil} = \rho_w \frac{h_w}{h_{oil}} = 1000 \times \frac{130}{140} \approx 928.6\,\mathrm{kg\,m^{-3}}$.
6. $\approx 928\,\mathrm{kg\,m^{-3}}$, which is option $2$.

**Subtopic:** Problems on Hydrostatics · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q002_f3fca778_30102026.png?v=f3fca7785566)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q002_552b31ef_30102026.png?v=552b31efa1f7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At the oil-water interface the two columns balance, so the 140 mm of oil weighs the same as the 130 mm of water standing above the same level
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $800\,\mathrm{kg\,m^{-3}}$ is the round figure oil is given in textbook problems, so the answer handed in is the density of oil in general rather than the density this U-tube's heights force, which is 928.
- **Why:** This question requires the hydrostatic balance written at the oil-water interface with the column heights read off the figure, demonstrated by 'it stands at a distance of $10\,\mathrm{mm}$ above the water level on the other side' together with 'the water rises by $65\,\mathrm{mm}$ from its original level'.
- **Note:** The figure is supplied as a drawn spec whose print check matched all 15 printed labels, including the 10 mm mark and both 65 mm arrows, so the oil and water column lengths are determinable from the record.
<!--/ecat-->

## Q3

Physics · Oscillations

A particle executes linear simple harmonic motion with an amplitude of $3\,\mathrm{cm}$. When the particle is at $2\,\mathrm{cm}$ from the mean position, the magnitude of its velocity is equal to that of its acceleration. Then its time period in seconds is

- **(1)** $\dfrac{4\pi}{\sqrt{5}}$
- (2) $\dfrac{2\pi}{\sqrt{3}}$
- (3) $\dfrac{\sqrt{5}}{\pi}$
- (4) $\dfrac{\sqrt{5}}{2\pi}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $v = \omega\sqrt{A^{2} - x^{2}}$
2. $a = x\omega^{2}$
3. $v = a$
4. $\omega\sqrt{A^{2} - x^{2}} = x\omega^{2}$
5. $\sqrt{(3)^{2} - (2)^{2}} = 2\left(\frac{2\pi}{T}\right)$
6. $\sqrt{5} = \frac{4\pi}{T}$
7. $T = \frac{4\pi}{\sqrt{5}}$

**Solved independently** (answer withheld)

1. In SHM the speed at displacement $x$ is $|v| = \omega\sqrt{A^2 - x^2}$.
2. With $A = 3\,\mathrm{cm}$ and $x = 2\,\mathrm{cm}$: $|v| = \omega\sqrt{9 - 4} = \sqrt{5}\,\omega$.
3. The acceleration magnitude is $|a| = \omega^2 x = 2\omega^2$.
4. Setting $|v| = |a|$: $\sqrt{5}\,\omega = 2\omega^2 \Rightarrow \omega = \frac{\sqrt{5}}{2}\,\mathrm{rad\,s^{-1}}$.
5. $T = \frac{2\pi}{\omega} = \frac{2\pi}{\sqrt{5}/2} = \frac{4\pi}{\sqrt{5}}\,\mathrm{s}$, which is option $1$.

**Subtopic:** Calculate Time Period of SHM · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q003_352710be_30102026.png?v=352710beac4b)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q003_a7ea5b7f_30102026.png?v=a7ea5b7f5928)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At displacement x in SHM the speed is $\omega\sqrt{A^2-x^2}$ and the acceleration is $\omega^2x$; equating the two fixes $\omega$, and the period is $2\pi/\omega$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The work up to $\omega=\frac{\sqrt5}{2}$ is right, and then $T=\frac{2\pi}{\omega}$ is written with $\omega$ and $\pi$ changing places as $\frac{2\omega}{\pi}$, which is exactly $\frac{\sqrt5}{\pi}$.
- **Why:** This question requires the SHM speed and acceleration at one displacement to be equated and the result turned into a period, demonstrated by 'the magnitude of its velocity is equal to that of its acceleration' and 'its time period in seconds is'.
<!--/ecat-->

## Q4

Physics · Gravitation

Two astronauts are floating in gravitational free space after having lost contact with their spaceship. The two will:

- (1) Move away from each other
- (2) Will become stationary
- (3) Keep floating at the same distance between them
- **(4)** Move towards each other

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Both the astronauts are in the condition of weightness.
2. Gravitational force between them pulls towards each other.

**Solved independently** (answer withheld)

1. In gravitational free space there is no external gravitational field, so $\vec{F}_{\text{ext}} = 0$.
2. The two astronauts still attract each other with $F = \frac{G m_1 m_2}{r^2}$, directed along the line joining them.
3. This attraction is unopposed, so each accelerates towards the other while the centre of mass stays fixed; they move towards each other, which is option $4$.

**Subtopic:** Universal Law of Gravitation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q004_68dc2b0f_30102026.png?v=68dc2b0faefc)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q004_a9ce8056_30102026.png?v=a9ce80564b60)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Gravitational free space removes outside fields, not the astronauts' own attraction for each other, which is the one force left and is always a pull
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  'Gravitational free space' is read as gravity being switched off, so nothing is left to act and the gap is taken to stay fixed - but the phrase removes external fields only, and the two bodies still pull on each other.
- **Why:** This question requires the universal law of gravitation applied to two masses with no other agency present, demonstrated by 'floating in gravitational free space after having lost contact with their spaceship'.
<!--/ecat-->

## Q5

Physics · Modern Physics

The de-Broglie wavelength of a neutron in thermal equilibrium with heavy water at a temperature $T$ (Kelvin) and mass $m$, is

- (1) $\dfrac{2h}{\sqrt{3mkT}}$
- (2) $\dfrac{2h}{\sqrt{mkT}}$
- (3) $\dfrac{h}{\sqrt{mkT}}$
- **(4)** $\dfrac{h}{\sqrt{3mkT}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. de-Broglie wavelength
2. $\lambda = \frac{h}{mv}$
3. $= \frac{h}{\sqrt{2m(\mathrm{KE})}}$
4. $= \frac{h}{\sqrt{2m(\frac{3}{2}kT)}}$
5. $\lambda = \frac{h}{\sqrt{3mkT}}$

**Solved independently** (answer withheld)

1. In thermal equilibrium at temperature $T$, the mean kinetic energy of the neutron is $E = \frac{3}{2}kT$.
2. Momentum from kinetic energy: $p = \sqrt{2mE}$.
3. $p = \sqrt{2m \cdot \frac{3}{2}kT} = \sqrt{3mkT}$.
4. $\lambda = \frac{h}{p} = \frac{h}{\sqrt{3mkT}}$, which is option $4$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q005_fa83fbd8_30102026.png?v=fa83fbd833fc)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q005_a5a83e79_30102026.png?v=a5a83e797616)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A neutron in thermal equilibrium carries $\frac32kT$ of kinetic energy, so its momentum is $\sqrt{3mkT}$ and its de Broglie wavelength $h/\sqrt{3mkT}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Equipartition is brought in as $\frac12kT$ instead of $\frac32kT$, and $p=\sqrt{2mE}$ then returns $\sqrt{mkT}$ in place of $\sqrt{3mkT}$.
- **Why:** This question requires a particle's thermal kinetic energy to be converted into a de Broglie wavelength, demonstrated by 'in thermal equilibrium with heavy water at a temperature $T$ (Kelvin) and mass $m$' with all four options built from h, m, k and T.
<!--/ecat-->

## Q6

Physics · Capacitance

A capacitor is charged by a battery. The battery is removed and another identical uncharged capacitor is connected in parallel. The total electrostatic energy of resulting system

- (1) Remains the same
- (2) Increases by a factor of 2
- (3) Increases by a factor of 4
- **(4)** Decreases by a factor of 2

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: A capacitor C connected across a cell V in one rectangular loop](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q006_sol_1_666c9b7d_30102026.svg?v=666c9b7d6ede)

*A capacitor C connected across a cell V in one rectangular loop*

![drawn: A capacitor C connected across a cell V in one rectangular loop](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q006_solution_1_d15abef9_30102026.svg?v=d15abef9b640)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Charge on capacitor $q = CV$
2. when it is connected with another uncharged capacitor.

![printed figure: A charged capacitor C (charge q) connected in parallel with an identical uncharged capacitor C](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q006_sol_2_5b1bf8a0_30102026.svg?v=5b1bf8a04c1f)

*A charged capacitor C (charge q) connected in parallel with an identical uncharged capacitor C*

![drawn: A charged capacitor C (charge q) connected in parallel with an identical uncharged capacitor C](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q006_solution_2_0e444995_30102026.svg?v=0e4449956195)  
*drawn on the booklet's geometry, checked against its figure spec*

3. $V_c = \frac{q_1 + q_2}{C_1 + C_2} = \frac{q + 0}{C + C}$
4. $V_c = \frac{V}{2}$
5. Initial energy $U_i = \frac{1}{2}CV^{2}$
6. Final energy $U_f = \frac{1}{2}C\left(\frac{V}{2}\right)^{2} + \frac{1}{2}C\left(\frac{V}{2}\right)^{2}$
7. $= \frac{CV^{2}}{4}$
8. Loss of energy $= U_i - U_f$
9. $= \frac{CV^{2}}{4}$
10. i.e. decreases by a factor $(2)$

**Solved independently** (answer withheld)

1. Initial energy of the isolated charged capacitor: $U = \frac{Q^2}{2C}$.
2. With the battery removed, the total charge $Q$ is conserved when the identical uncharged capacitor is connected.
3. Two identical capacitors in parallel give $C' = C + C = 2C$.
4. Final energy: $U' = \frac{Q^2}{2C'} = \frac{Q^2}{2(2C)} = \frac{Q^2}{4C}$.
5. $\frac{U'}{U} = \frac{Q^2/4C}{Q^2/2C} = \frac{1}{2}$, so the energy decreases by a factor of $2$, which is option $4$.

**Subtopic:** Redistribution of Charges · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q006_19ab8c56_30102026.png?v=19ab8c569ae4)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q006_89389e7c_30102026.png?v=89389e7cb9b2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Once the battery is gone the charge is fixed, so sharing it with an equal capacitor doubles C at constant Q and halves $U=\frac{Q^2}{2C}$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The voltage is held at its old value, as though the battery were still across the plates, and $U=\frac12CV^2$ with C doubled then reads as twice the energy; the stem's 'The battery is removed' is exactly what forbids holding V fixed.
- **Why:** This question requires the quantity that stays fixed after disconnection to be identified before an energy formula is used, demonstrated by 'The battery is removed and another identical uncharged capacitor is connected in parallel'.
<!--/ecat-->

## Q7

Physics · Semiconductor Electronics

Which one of the following represents forward bias diode?

- (1) ![printed figure: A diode and resistor R in series between -2 V (left) and +2 V (right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q007_option_1_cf942e45_30102026.svg?v=cf942e453c4a) *A diode and resistor R in series between -2 V (left) and +2 V (right)* ![drawn: A diode and resistor R in series between -2 V (left) and +2 V (right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q007_option_1_d2b2c768_30102026.svg?v=d2b2c76810bf)  
*drawn on the booklet's geometry, checked against its figure spec* — $-2\,\mathrm{V}$ — [diode] — $R$ — $+2\,\mathrm{V}$
- (2) ![printed figure: A diode and a resistor R in series between a 3 V end and a 5 V end](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q007_option_2_945be8ba_30102026.svg?v=945be8baf34c) *A diode and a resistor R in series between a 3 V end and a 5 V end* ![drawn: A diode and a resistor R in series between a 3 V end and a 5 V end](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q007_option_2_d5a2dc1b_30102026.svg?v=d5a2dc1b60d2)  
*drawn on the booklet's geometry, checked against its figure spec* — $3\,\mathrm{V}$ — [diode] — $R$ — $5\,\mathrm{V}$
- **(3)** ![printed figure: Diode and resistor R in series between 0 V (left) and -2 V (right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q007_option_3_6b467c00_30102026.svg?v=6b467c006397) *Diode and resistor R in series between 0 V (left) and -2 V (right)* ![drawn: Diode and resistor R in series between 0 V (left) and -2 V (right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q007_option_3_0463d36d_30102026.svg?v=0463d36df705)  
*drawn on the booklet's geometry, checked against its figure spec* — $0\,\mathrm{V}$ — [diode] — $R$ — $-2\,\mathrm{V}$
- (4) ![printed figure: Diode in series with resistor R between -4 V (left) and -3 V (right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q007_option_4_b517d8b1_30102026.svg?v=b517d8b1a23a) *Diode in series with resistor R between -4 V (left) and -3 V (right)* ![drawn: Diode in series with resistor R between -4 V (left) and -3 V (right)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q007_option_4_ae1566c0_30102026.svg?v=ae1566c05ded)  
*drawn on the booklet's geometry, checked against its figure spec* — $-4\,\mathrm{V}$ — [diode] — $R$ — $-3\,\mathrm{V}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In forward bias, $p$-type semiconductor is at higher potential w.r.t. $n$-type semiconductor.

**Solved independently** (answer withheld)

1. In all four drawings the diode arrow points from the left terminal toward $R$, so the anode ($p$-side) is on the left and the cathode ($n$-side) is on the right.
2. A diode is forward biased when $V_{p} > V_{n}$, so here the condition is $V_{\text{left}} > V_{\text{right}}$.
3. Option 1: $-2\,\mathrm{V} < +2\,\mathrm{V}$, so the diode is reverse biased.
4. Option 2: $3\,\mathrm{V} < 5\,\mathrm{V}$, so the diode is reverse biased.
5. Option 3: $0\,\mathrm{V} > -2\,\mathrm{V}$, so the diode is forward biased.
6. Option 4: $-4\,\mathrm{V} < -3\,\mathrm{V}$, so the diode is reverse biased.
7. Only option $3$ is forward biased.

**Subtopic:** PN Junction Diode Under Forward Bias · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q007_dcc371d8_30102026.png?v=dcc371d860da)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q007_610180ba_30102026.png?v=610180ba9faf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A junction diode is forward biased when the p-side is held at the higher potential, so only the sign of the potential drop across it matters, not how large the two potentials are
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A minus at one end and a plus at the other is taken as the picture of forward bias, so the $-2\,\mathrm{V}$ to $+2\,\mathrm{V}$ arrangement is picked - but the plus is on the far side of the diode, which is reverse bias with the biggest drop of the four.
- **Why:** This question requires the forward-bias condition applied to four printed potential pairs, demonstrated by 'Which one of the following represents forward bias diode?' with the options differing only in the two terminal potentials.
- **Note:** E1's pattern called this statement_options on '15 full-statement options', which contradicts the printed shape: the four options are circuit fragments, not statements, so qtype is recorded as mcq. Our stored option text flattens the diode symbol to '[diode]' and so does not carry its orientation; the tags read the printed p-side as the left-hand terminal in all four options, which is the reading under which the printed key, option 3, is the only forward-biased case (its right-hand end is the only one below its left-hand end).
<!--/ecat-->

## Q8

Physics · Modern Physics

The photoelectric threshold wavelength of silver is $3250 \times 10^{-10}\,\mathrm{m}$. The velocity of the electron ejected from a silver surface by ultraviolet light of wavelength $2536 \times 10^{-10}\,\mathrm{m}$ is (Given $h = 4.14 \times 10^{-15}\,\mathrm{eVs}$ and $c = 3 \times 10^{8}\,\mathrm{ms^{-1}}$)

- (1) $\approx 61 \times 10^{3}\,\mathrm{ms^{-1}}$
- (2) $\approx 0.3 \times 10^{6}\,\mathrm{ms^{-1}}$
- **(3)** $\approx 6 \times 10^{5}\,\mathrm{ms^{-1}}$
- **(4)** $\approx 0.6 \times 10^{6}\,\mathrm{ms^{-1}}$

**Answer** — booklet: (3, 4) · independent solve: (4) · agree

**Publisher's solution**

1. $\lambda_0 = 3250 \times 10^{-10}\,\mathrm{m}$
2. $\lambda = 2536 \times 10^{-10}\,\mathrm{m}$
3. $\phi = \frac{1242\,\mathrm{eV\text{-}nm}}{325\,\mathrm{nm}} = 3.82\,\mathrm{eV}$
4. $h\nu = \frac{1242\,\mathrm{eV\text{-}nm}}{253.6\,\mathrm{nm}} = 4.89\,\mathrm{eV}$
5. $\mathrm{KE_{max}} = (4.89 - 3.82)\,\mathrm{eV} = 1.077\,\mathrm{eV}$
6. $\frac{1}{2}mv^{2} = 1.077 \times 1.6 \times 10^{-19}$
7. $v = \sqrt{\frac{2 \times 1.077 \times 1.6 \times 10^{-19}}{9.1 \times 10^{-31}}}$
8. $v = 0.6 \times 10^{6}\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. $hc = 4.14 \times 10^{-15}\,\mathrm{eV\,s} \times 3 \times 10^{8}\,\mathrm{m\,s^{-1}} = 1.242 \times 10^{-6}\,\mathrm{eV\,m}$.
2. Photon energy: $E = \frac{hc}{\lambda} = \frac{1.242 \times 10^{-6}}{2536 \times 10^{-10}} \approx 4.898\,\mathrm{eV}$.
3. Work function: $\phi_0 = \frac{hc}{\lambda_0} = \frac{1.242 \times 10^{-6}}{3250 \times 10^{-10}} \approx 3.822\,\mathrm{eV}$.
4. Einstein's equation: $K_{max} = E - \phi_0 = 4.898 - 3.822 \approx 1.076\,\mathrm{eV}$.
5. Convert to joules: $K_{max} = 1.076 \times 1.6 \times 10^{-19} \approx 1.722 \times 10^{-19}\,\mathrm{J}$.
6. $v = \sqrt{\frac{2K_{max}}{m_e}} = \sqrt{\frac{2 \times 1.722 \times 10^{-19}}{9.1 \times 10^{-31}}} = \sqrt{3.784 \times 10^{11}} \approx 6.15 \times 10^{5}\,\mathrm{m\,s^{-1}}$.
7. $6.15 \times 10^{5} \approx 0.6 \times 10^{6}\,\mathrm{m\,s^{-1}} = 6 \times 10^{5}\,\mathrm{m\,s^{-1}}$, which matches both option $3$ and option $4$; option $4$ chosen.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q008_e852309d_30102026.png?v=e852309d0319)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q008_272cacbc_30102026.png?v=272cacbc6e34)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Einstein's photoelectric equation: the photon energy above the work function set by the threshold wavelength appears as the electron's kinetic energy
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $61\times10^3\,\mathrm{m\,s^{-1}}$ is the answer with one power of ten lost under the square root - exactly what $\sqrt{2K/m}$ returns if the electron mass is carried as $9.1\times10^{-29}$ kg instead of $9.1\times10^{-31}$ kg.
- **Why:** This question requires the photon energy above the threshold to be turned into an electron speed, demonstrated by 'The photoelectric threshold wavelength of silver is $3250\times10^{-10}\,\mathrm{m}$' with the ejecting light at $2536\times10^{-10}\,\mathrm{m}$.
- **Note:** Options 3 and 4 are the same speed written two ways, $6\times10^{5}$ and $0.6\times10^{6}\,\mathrm{m\,s^{-1}}$, and the printed answer line accepts both - 'Answer (3 & 4)* Both answers are correct.' The duplication is in the printed paper, not in our record, so it is not recorded as source damage; neither accepted option is given a role. E1's pattern called this statement_options on '15 full-statement options', which the four numeric options contradict, so qtype is mcq.
<!--/ecat-->

## Q9

Physics · Waves

Two cars moving in opposite directions approach each other with speed of $22\,\mathrm{m/s}$ and $16.5\,\mathrm{m/s}$ respectively. The driver of the first car blows a horn having a frequency $400\,\mathrm{Hz}$. The frequency heard by the driver of the second car is [velocity of sound $340\,\mathrm{m/s}$]

- (1) $411\,\mathrm{Hz}$
- **(2)** $448\,\mathrm{Hz}$
- (3) $350\,\mathrm{Hz}$
- (4) $361\,\mathrm{Hz}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $f_A = f\left[\frac{v + v_o}{v - v_s}\right]$
2. $= 400\left[\frac{340 + 16.5}{340 - 22}\right]$
3. $f_A = 448\,\mathrm{Hz}$

**Solved independently** (answer withheld)

1. Source (first car) moves toward the observer with $v_s = 22\,\mathrm{m/s}$; observer (second car) moves toward the source with $v_o = 16.5\,\mathrm{m/s}$.
2. For approach, $f' = f\,\frac{v + v_o}{v - v_s}$.
3. $f' = 400 \times \frac{340 + 16.5}{340 - 22} = 400 \times \frac{356.5}{318}$.
4. $f' = \frac{142600}{318} \approx 448.4\,\mathrm{Hz}$.
5. $f' \approx 448\,\mathrm{Hz}$, which is option $2$.

**Subtopic:** Doppler Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q009_af6a425f_30102026.png?v=af6a425f3239)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q009_88b628cd_30102026.png?v=88b628cd888f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Doppler effect with both source and listener moving: approach puts the listener's speed on top and the source's speed as a subtraction underneath, so the pitch rises
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The two speeds go into the formula with the signs of a recession, $400\times\frac{340-16.5}{340+22}=357$ Hz, so the pitch comes out below the horn's 400 Hz and 361 Hz is the printed option that value lands on.
- **Why:** This question requires the Doppler formula applied with both source and listener in motion, demonstrated by 'Two cars moving in opposite directions approach each other with speed of $22\,\mathrm{m/s}$ and $16.5\,\mathrm{m/s}$'.
- **Note:** None of the three wrong options is the exact output of a Doppler substitution; each route above is quoted with the value it actually computes (357 Hz for option 4, 407 Hz for option 1) so a reviewer can audit the few-hertz gap to the printed figure. Worth recording that swapping the two speeds between source and listener still gives 448 Hz ($400\times362/323.5=447.6$), so that confusion is not punished here. E1's pattern called the item multi_part_respectively because 'respectively' appears in the stem, but it is governing the two car speeds and the answer is a single frequency, so qtype is mcq.
<!--/ecat-->

## Q10

Physics · Electromagnetic Induction

Figure shows a circuit contains three identical resistors with resistance $R = 9.0\,\Omega$ each, two identical inductors with inductance $L = 2.0\,\mathrm{mH}$ each, and an ideal battery with emf $\varepsilon = 18\,\mathrm{V}$. The current '$i$' through the battery just after the switch closed is

![printed figure: Battery and switch feeding three parallel branches: L-R, R, and R followed by L parallel to C](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q010_8b81d6a4_30102026.svg?v=8b81d6a4301a)

*Battery and switch feeding three parallel branches: L-R, R, and R followed by L parallel to C*

![drawn: Battery and switch feeding three parallel branches: L-R, R, and R followed by L parallel to C](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q010_question_0d5ca263_30102026.svg?v=0d5ca263b2fb)  
*drawn on the booklet's geometry, checked against its figure spec*

- **(1)** $2\,\mathrm{A}$
- (2) $0$ ampere
- (3) $2\,\mathrm{mA}$
- (4) $0.2\,\mathrm{A}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Battery ε across three parallel branches: L1 in series with R1, R2 alone, and R3 in series with L2, where C is in parallel with L2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q010_sol_1_d3df41e9_30102026.svg?v=d3df41e91c7f)

*Battery ε across three parallel branches: L1 in series with R1, R2 alone, and R3 in series with L2, where C is in parallel with L2*

![drawn: Battery ε across three parallel branches: L1 in series with R1, R2 alone, and R3 in series with L2, where C is in parallel with L2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q010_solution_1_4bc054da_30102026.svg?v=4bc054da83f2)  
*drawn on the booklet's geometry, checked against its figure spec*

1. At $t = 0$, no current flows through $R_1$ and $R_3$

![printed figure: A battery of emf ε driving current i through a resistor R2 in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q010_sol_2_6254d646_30102026.svg?v=6254d646513d)

*A battery of emf ε driving current i through a resistor R2 in one loop*

![drawn: A battery of emf ε driving current i through a resistor R2 in one loop](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q010_solution_2_82549032_30102026.svg?v=8254903295b0)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $i = \frac{\varepsilon}{R_2}$
3. $= \frac{18}{9}$
4. $= 2\,\mathrm{A}$
5. Note : Not correctly framed but the best option out of given is (1).

**Solved independently** (answer withheld)

1. Just after the switch closes, an inductor opposes any sudden change in current, so each inductor carries $i_L(0^+) = 0$ and behaves as an open circuit.
2. Branch 1 ($L$ in series with $R$): $i_1 = 0$.
3. Branch 2 (plain $R$): $i_2 = \frac{\varepsilon}{R} = \frac{18\,\mathrm{V}}{9.0\,\Omega} = 2\,\mathrm{A}$.
4. Branch 3 ($R$ in series with $L$): with the inductor open and no capacitor considered (the stem lists only resistors, inductors and battery), $i_3 = 0$.
5. $i = i_1 + i_2 + i_3 = 0 + 2 + 0 = 2\,\mathrm{A}$, which is option $1$.
6. Caveat: the figure draws an uncharged capacitor $C$ across the second inductor; at $t=0^+$ it would act as a short, giving $i_3 = \frac{18}{9} = 2\,\mathrm{A}$ and $i = 4\,\mathrm{A}$, which matches no option.

**Subtopic:** LR Circuits · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q010_15d5c029_30102026.png?v=15d5c0298110)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q010_65fe2b6c_30102026.png?v=65fe2b6c27d5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An inductor keeps its current at zero through the instant the switch closes, so immediately after closing only the branch with no inductor in it carries current
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  'Current through an inductor cannot change instantly' is applied to the whole circuit rather than to the branches that actually contain an inductor, so the battery current is taken to start at zero - but the middle branch is a bare 9 ohm resistor with no inductor in it.
- **Why:** This question requires the instantaneous state of an inductor at switch-on to be settled before Ohm's law is used, demonstrated by 'The current $i$ through the battery just after the switch closed'.
- **Note:** The stem lists three resistors, two inductors and the battery, but the supplied figure's netlist also carries a capacitor C in parallel with the second inductor. With an uncharged capacitor that third branch would conduct at $t=0$ and the battery current would be 4 A, which is not a printed option; the printed key, 2 A, follows the stem's component list, and the asterisk on 'Answer (1*)' is consistent with the source itself flagging the item. Tagged as printed.
<!--/ecat-->

## Q11

Physics · Ray Optics

A beam of light from a source $L$ is incident normally on a plane mirror fixed at a certain distance $x$ from the source. The beam is reflected back as a spot on a scale placed just above the source $L$. When the mirror is rotated through a small angle $\theta$, the spot of the light is found to move through a distance $y$ on the scale. The angle $\theta$ is given by

- (1) $\frac{x}{2y}$
- (2) $\frac{x}{y}$
- **(3)** $\frac{y}{2x}$
- (4) $\frac{y}{x}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. When mirror is rotated by $\theta$ angle reflected ray will be rotated by $2\theta$.

![printed figure: Isosceles triangle: two rays of length x from the apex with apex angle 2θ, base y marked by a double arrow](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q011_sol_1_39ae4179_30102026.svg?v=39ae41792476)

*Isosceles triangle: two rays of length x from the apex with apex angle 2θ, base y marked by a double arrow*

![drawn: Isosceles triangle: two rays of length x from the apex with apex angle 2θ, base y marked by a double arrow](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q011_solution_1_a3ced60a_30102026.svg?v=a3ced60a22c4)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $\frac{y}{x} = 2\theta$
3. $\theta = \frac{y}{2x}$

**Solved independently** (answer withheld)

1. When a plane mirror rotates through $\theta$, the reflected ray rotates through $2\theta$ (incident ray fixed).
2. The spot on the scale at distance $x$ moves by $y$, so $\tan 2\theta = \frac{y}{x}$.
3. For a small angle, $\tan 2\theta \approx 2\theta$, so $2\theta = \frac{y}{x}$.
4. $\theta = \frac{y}{2x}$, which is option $3$.

**Subtopic:** Reflection at a Smooth Surface · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q011_8433605a_30102026.png?v=8433605ae1ff)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q011_039336f7_30102026.png?v=039336f76b04)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Turning a mirror through an angle turns the reflected beam through twice that angle, so the spot's shift is $y=x\tan2\theta\approx2x\theta$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The beam is taken to swing through the same angle as the mirror, so the geometry is written $\theta=y/x$ and the doubling that reflection produces never appears.
- **Why:** This question requires the mirror-rotation doubling to be combined with the small-angle geometry of the scale reading, demonstrated by 'When the mirror is rotated through a small angle $\theta$, the spot of the light is found to move through a distance $y$ on the scale'.
- **Note:** Applied the codebook's arithmetic_slip-against-formula_misused test: the missing 2 is not lost while computing, it is absent from the relation the student is using, so the label is formula_misused.
<!--/ecat-->

## Q12

Physics · Magnetic Effect of Electric Current

An arrangement of three parallel straight wires placed perpendicular to plane of paper carrying same current ‘$I$’ along the same direction is shown in Fig. Magnitude of force per unit length on the middle wire ‘$B$’ is given by

![printed figure: Three parallel wires A, B, C perpendicular to the page, with BA = BC = d and angle ABC = 90 degrees](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q012_c2805564_30102026.svg?v=c2805564c79d)

*Three parallel wires A, B, C perpendicular to the page, with BA = BC = d and angle ABC = 90 degrees*

![drawn: Three parallel wires A, B, C perpendicular to the page, with BA = BC = d and angle ABC = 90 degrees](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q012_question_5c547bbf_30102026.svg?v=5c547bbf8aa9)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\frac{\sqrt{2}\mu_0 I^2}{\pi d}$
- **(2)** $\frac{\mu_0 I^2}{\sqrt{2}\pi d}$
- (3) $\frac{\mu_0 I^2}{2\pi d}$
- (4) $\frac{2\mu_0 I^2}{\pi d}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Force between $BC$ and $AB$ will be same in magnitude.

![printed figure: Forces F on wire B due to wires C and A, at right angles](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q012_sol_1_dcb1a6fe_30102026.svg?v=dcb1a6fe5aa9)

*Forces F on wire B due to wires C and A, at right angles*

![drawn: Forces F on wire B due to wires C and A, at right angles](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q012_solution_1_78d8e119_30102026.svg?v=78d8e119dba1)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $F_{BC} = F_{BA} = \frac{\mu_0 I^2}{2\pi d}$
3. $F = \sqrt{2}F_{BC}$
4. $= \sqrt{2}\frac{\mu_0}{2\pi}\frac{I^2}{d}$
5. $F = \frac{\mu_0 I^2}{\sqrt{2}\pi d}$

**Solved independently** (answer withheld)

1. Force per unit length between two parallel wires carrying current $I$ at separation $d$ is $f = \frac{\mu_0 I^2}{2\pi d}$, attractive since the currents are in the same direction.
2. From the figure, wire $A$ is a distance $d$ below $B$, so $A$ pulls $B$ downward with $f_A = \frac{\mu_0 I^2}{2\pi d}$.
3. Wire $C$ is a distance $d$ to the right of $B$, so $C$ pulls $B$ to the right with $f_C = \frac{\mu_0 I^2}{2\pi d}$.
4. The two forces are at $90^\circ$, so $f_B = \sqrt{f_A^2 + f_C^2} = \sqrt{2}\,\frac{\mu_0 I^2}{2\pi d}$.
5. $\sqrt{2}\,\frac{\mu_0 I^2}{2\pi d} = \frac{\mu_0 I^2}{\sqrt{2}\,\pi d}$, which is option $2$.

**Subtopic:** Force Between Two Parallel Current-Carrying Conductors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q012_7cd0213c_30102026.png?v=7cd0213c186a)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q012_a7ddf65b_30102026.png?v=a7ddf65be7f6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Parallel currents in the same direction attract, so the middle wire feels two equal pulls at right angles and the resultant is $\sqrt2$ times one of them
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\frac{\mu_0I^2}{2\pi d}$ is the force per unit length between ONE pair of parallel wires - the expression the textbook prints - so recalling it answers 'what does A do to B' and the equal pull from C, at $90^\circ$ to it, never gets added.
- **Why:** This question requires two equal perpendicular magnetic forces to be added as vectors, demonstrated by 'Magnitude of force per unit length on the middle wire B' with the figure marking BA = BC = d and angle ABC as $90^\circ$.
<!--/ecat-->

## Q13

Physics · Wave Optics

Young’s double slit experiment is first performed in air and then in a medium other than air. It is found that $8^{\mathrm{th}}$ bright fringe in the medium lies where $5^{\mathrm{th}}$ dark fringe lies in air. The refractive index of the medium is nearly

- (1) $1.69$
- **(2)** $1.78$
- (3) $1.25$
- (4) $1.59$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $X_1 = X_{5\text{th dark}} = (2 \times 5 - 1)\frac{\lambda D}{2d}$
2. $X_2 = X_{8\text{th bright}} = 8\frac{\lambda D}{\mu d}$
3. $X_1 = X_2$
4. $\frac{9}{2}\frac{\cancel{\lambda D}}{\cancel{d}} = 8\frac{\cancel{\lambda D}}{\mu \cancel{d}}$
5. $\mu = \frac{16}{9} = 1.78$

**Solved independently** (answer withheld)

1. In the medium the wavelength becomes $\lambda' = \frac{\lambda}{\mu}$.
2. Position of the $8^{\mathrm{th}}$ bright fringe in the medium: $y_8 = \frac{8\lambda' D}{d} = \frac{8\lambda D}{\mu d}$.
3. Position of the $5^{\mathrm{th}}$ dark fringe in air: $y_5 = \frac{(2 \times 5 - 1)\lambda D}{2d} = \frac{4.5\,\lambda D}{d}$.
4. Equate the two positions: $\frac{8\lambda D}{\mu d} = \frac{4.5\,\lambda D}{d}$.
5. $\mu = \frac{8}{4.5} = \frac{16}{9} \approx 1.78$, which is option $2$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q013_6e3838b3_30102026.png?v=6e3838b384d1)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q013_b580e4d2_30102026.png?v=b580e4d27e5b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Fringe width shrinks by the refractive index in a medium, and the nth dark fringe sits at $(n-\tfrac12)$ fringe widths, not at n
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The 5th dark fringe is placed at 5 fringe widths instead of 4.5, so the coincidence reads $8/\mu=5$ and the index comes out as $8/5=1.6$, which the options print as 1.59.
- **Why:** This question requires the coincidence of a bright fringe in a medium with a dark fringe in air to be written in fringe widths, demonstrated by '$8^{\mathrm{th}}$ bright fringe in the medium lies where $5^{\mathrm{th}}$ dark fringe lies in air'.
- **Note:** The route to option 4 computes 1.60 while the option is printed as 1.59; the stem's own 'nearly' covers that gap, and the numbers are given here so the step can be audited.
<!--/ecat-->

## Q14

Physics · Oscillations

A spring of force constant $k$ is cut into lengths of ratio $1 : 2 : 3$. They are connected in series and the new force constant is $k'$. Then they are connected in parallel and force constant is $k''$. Then $k' : k''$ is

- **(1)** $1 : 11$
- (2) $1 : 14$
- (3) $1 : 6$
- (4) $1 : 9$

**Answer** — booklet: (1) · independent solve: (1) · agree

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
12. $\frac{k'}{\ } = \frac{1}{11}$ i.e $k' : k'' = 1 : 11$

**Solved independently** (answer withheld)

1. For a uniform spring $k \propto \frac{1}{l}$, i.e. $kl = \text{constant}$.
2. Lengths in ratio $1:2:3$ give $l_1 = \frac{l}{6},\ l_2 = \frac{l}{3},\ l_3 = \frac{l}{2}$.
3. So $k_1 = 6k,\ k_2 = 3k,\ k_3 = 2k$.
4. Series: $\frac{1}{k'} = \frac{1}{6k} + \frac{1}{3k} + \frac{1}{2k} = \frac{1+2+3}{6k} = \frac{1}{k}$, so $k' = k$.
5. Parallel: $k'' = 6k + 3k + 2k = 11k$.
6. $k' : k'' = k : 11k = 1 : 11$, which is option $1$.

**Subtopic:** Combination of Springs · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q014_75ec3fc9_30102026.png?v=75ec3fc9e378)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q014_419e6dcc_30102026.png?v=419e6dcceca9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A spring's stiffness varies inversely with its length, so cutting in 1 : 2 : 3 gives 6k, 3k and 2k - the series set restores k and the parallel set sums to 11k
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The remembered result for n IDENTICAL springs - series $k/n$, parallel $nk$, ratio $1:n^2$ - is applied with $n=3$, giving $1:9$, which drops the stem's printed 1 : 2 : 3 and the unequal stiffnesses it forces.
- **Why:** This question requires the inverse length dependence of stiffness applied to unequal pieces before the series and parallel rules are used, demonstrated by 'cut into lengths of ratio $1 : 2 : 3$'.
<!--/ecat-->

## Q15

Physics · Ray Optics

A thin prism having refracting angle $10^\circ$ is made of glass of refractive index $1.42$. This prism is combined with another thin prism of glass of refractive index $1.7$. This combination produces dispersion without deviation. The refracting angle of second prism should be

- (1) $8^\circ$
- (2) $10^\circ$
- (3) $4^\circ$
- **(4)** $6^\circ$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $(\mu - 1)A + (\mu' - 1)A' = 0$
2. $|(\mu - 1)A| = |(\mu' - 1)A'|$
3. $(1.42 - 1)\times 10^\circ = (1.7 - 1)A'$
4. $4.2 = 0.7A'$
5. $A' = 6^\circ$

**Solved independently** (answer withheld)

1. For a thin prism the deviation is $\delta = (\mu - 1)A$.
2. The prisms are placed in opposite orientation, so zero net deviation requires $\delta_1 = \delta_2$, i.e. $(\mu_1 - 1)A_1 = (\mu_2 - 1)A_2$.
3. $\delta_1 = (1.42 - 1)\times 10^\circ = 4.2^\circ$.
4. $(1.7 - 1)A_2 = 4.2^\circ \Rightarrow A_2 = \frac{4.2^\circ}{0.7} = 6^\circ$, which is option $4$.

**Subtopic:** Dispersion · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q015_40ce820e_30102026.png?v=40ce820e1288)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q015_a70b84f3_30102026.png?v=a70b84f3f9e5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A thin prism deviates a ray by $(\mu-1)A$, so dispersion without deviation needs $(\mu_1-1)A_1=(\mu_2-1)A_2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The deviation is taken as $\mu A$ rather than $(\mu-1)A$, so the angles are balanced as $A_2=10\times\frac{1.42}{1.7}=8.35^\circ$ and the $8^\circ$ option is read off.
- **Why:** This question requires the thin-prism deviation $(\mu-1)A$ to be balanced between two prisms, demonstrated by 'This combination produces dispersion without deviation'.
<!--/ecat-->

## Q16

Physics · Thermodynamics

A gas mixture consists of 2 moles of $\mathrm{O_2}$ and 4 moles of Ar at temperature $T$. Neglecting all vibrational modes, the total internal energy of the system is

- (1) $9\,RT$
- **(2)** $11\,RT$
- (3) $4\,RT$
- (4) $15\,RT$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $U = n_1\frac{f_1}{2}RT + n_2\frac{f_2}{2}RT$
2. $= 2 \times \frac{5}{2}RT + 4 \times \frac{3}{2}RT$
3. $= 5\,RT + 6\,RT$
4. $U = 11\,RT$

**Solved independently** (answer withheld)

1. Neglecting vibration, $\mathrm{O_2}$ (diatomic) has $f_1 = 5$ degrees of freedom and Ar (monatomic) has $f_2 = 3$.
2. Total internal energy $U = n_1\frac{f_1}{2}RT + n_2\frac{f_2}{2}RT$.
3. $U_{\mathrm{O_2}} = 2 \times \frac{5}{2}RT = 5RT$.
4. $U_{\mathrm{Ar}} = 4 \times \frac{3}{2}RT = 6RT$.
5. $U = 5RT + 6RT = 11RT$, which is option $2$.

**Subtopic:** Specific Heat Capacity of Monoatomic, Diatomic, and Polyatomic Gases · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q016_5260d0ed_30102026.png?v=5260d0ed464a)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q016_e44a3ee2_30102026.png?v=e44a3ee28d1c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Internal energy counts degrees of freedom mole by mole: $\tfrac52RT$ per mole of a diatomic gas with vibration frozen out, $\tfrac32RT$ per mole of a monatomic one
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The monatomic expression $U=\tfrac32nRT$ is used for the whole mixture, so all six moles are given three degrees of freedom and the total comes out $6\times\tfrac32RT=9RT$.
- **Why:** This question requires degrees of freedom to be counted separately for each gas and weighted by its moles, demonstrated by '2 moles of $\mathrm{O_2}$ and 4 moles of Ar' with 'Neglecting all vibrational modes'.
<!--/ecat-->

## Q17

Physics · Work, Energy and Power

Consider a drop of rain water having mass $1\,\mathrm{g}$ falling from a height of $1\,\mathrm{km}$. It hits the ground with a speed of $50\,\mathrm{m/s}$. Take $g$ constant with a value $10\,\mathrm{m/s^2}$. The work done by the (i) gravitational force and the (ii) resistive force of air is

- (1) (i) $100\,\mathrm{J}$ (ii) $8.75\,\mathrm{J}$
- **(2)** (i) $10\,\mathrm{J}$ (ii) $-8.75\,\mathrm{J}$
- (3) (i) $-10\,\mathrm{J}$ (ii) $-8.25\,\mathrm{J}$
- (4) (i) $1.25\,\mathrm{J}$ (ii) $-8.25\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $w_g + w_a = K_f - K_i$
2. $mgh + w_a = \frac{1}{2}mv^{2} - 0$
3. $10^{-3} \times 10 \times 10^{3} + w_a = \frac{1}{2} \times 10^{-3} \times (50)^{2}$
4. $w_a = -8.75\,\mathrm{J}$ i.e. work done due to air resistance and work done due to gravity $= 10\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Convert mass: $m = 1\,\mathrm{g} = 10^{-3}\,\mathrm{kg}$, $h = 1\,\mathrm{km} = 1000\,\mathrm{m}$.
2. Work by gravity: $W_g = mgh = 10^{-3} \times 10 \times 1000 = 10\,\mathrm{J}$.
3. Final kinetic energy: $K_f = \frac{1}{2} m v^2 = \frac{1}{2} \times 10^{-3} \times (50)^2 = 1.25\,\mathrm{J}$, with $K_i = 0$.
4. Work-energy theorem: $W_g + W_{air} = K_f - K_i = 1.25\,\mathrm{J}$.
5. $W_{air} = 1.25 - 10 = -8.75\,\mathrm{J}$.
6. (i) $10\,\mathrm{J}$, (ii) $-8.75\,\mathrm{J}$, which is option $2$.

**Subtopic:** Work–Energy Theorem · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q017_0b61c8c9_30102026.png?v=0b61c8c98736)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q017_224628d1_30102026.png?v=224628d10050)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Gravity does positive work $mgh$ on a falling drop, and the air's work is whatever makes the sum equal the kinetic energy gained, so it comes out negative
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The size of the gravitational work is got right and then signed the way a potential-energy change is signed - $\Delta U=-mgh=-10$ J - so part (i) reads as $-10$ J even though gravity pulls the drop the way it moves.
- **Why:** This question requires both works to be signed and the resistive one to be got from the work-energy theorem, demonstrated by 'The work done by the (i) gravitational force and the (ii) resistive force of air is'.
- **Note:** Each option bundles two labelled values that must both hold, so the printed shape is two_part rather than the plain_mcq the pattern classifier defaulted to. No wrong option here is reachable by a single error: every one pairs a reachable half (the $+8.75$ sign flip, the $-10$ sign flip, the 1.25 J net work) with a figure no route produces - 100 J needs the kilometre as $10^4$ m, and $-8.25$ J is not what $1.25-10$ gives.
<!--/ecat-->

## Q18

Physics · Kinematics

The $x$ and $y$ coordinates of the particle at any time are $x = 5t - 2t^{2}$ and $y = 10t$ respectively, where $x$ and $y$ are in meters and $t$ in seconds. The acceleration of the particle at $t = 2\,\mathrm{s}$ is

- **(1)** $-4\,\mathrm{m/s^{2}}$
- (2) $-8\,\mathrm{m/s^{2}}$
- (3) $0$
- (4) $5\,\mathrm{m/s^{2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $x = 5t - 2t^{2}$, $y = 10t$
2. $\frac{dx}{dt} = 5 - 4t$, $\frac{dy}{dt} = 10$
3. $v_{x} = 5 - 4t$, $v_{y} = 10$
4. $\frac{dv}{dt}x = -4$, $\frac{dv}{dt}y = 10$
5. $a_{x} = -4$, $a_{y} = 0$
6. Acceleration of particle at $t = 2\,\mathrm{s}$ is $= -4\,\mathrm{m/s^{2}}$

**Solved independently** (answer withheld)

1. $v_x = \frac{dx}{dt} = \frac{d}{dt}(5t - 2t^{2}) = 5 - 4t$.
2. $a_x = \frac{dv_x}{dt} = -4\,\mathrm{m/s^{2}}$, which does not depend on $t$.
3. $v_y = \frac{dy}{dt} = \frac{d}{dt}(10t) = 10\,\mathrm{m/s}$.
4. $a_y = \frac{dv_y}{dt} = 0$.
5. $\vec{a} = a_x\hat{i} + a_y\hat{j} = -4\hat{i}\,\mathrm{m/s^{2}}$, so at $t = 2\,\mathrm{s}$ the acceleration is $-4\,\mathrm{m/s^{2}}$, which is option $1$.

**Subtopic:** Instantaneous Acceleration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q018_52b0ab7d_30102026.png?v=52b0ab7dcc8f)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q018_639171ba_30102026.png?v=639171bae3ab)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Acceleration is the second derivative of position, and for $x=5t-2t^2$ that second derivative carries no t at all
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The two differentiations are done correctly to $a_x=-4\,\mathrm{m/s^2}$ and then the stated time is substituted into a result that has no t in it, $-4\times2=-8$.
- **Why:** This question requires the position components to be differentiated twice, demonstrated by '$x = 5t - 2t^{2}$ and $y = 10t$' with 'The acceleration of the particle at $t = 2\,\mathrm{s}$'.
- **Note:** E1's pattern called this multi_part_respectively because 'respectively' appears in the stem, but there it governs the two coordinate equations and the answer is a single acceleration, so the printed shape is a plain MCQ.
<!--/ecat-->

## Q19

Physics · Rotational Motion

Two discs of same moment of inertia rotating about their regular axis passing through centre and perpendicular to the plane of disc with angular velocities $\omega_1$ and $\omega_2$. They are brought into contact face to face coinciding the axis of rotation. The expression for loss of energy during this process is

- (1) $I(\omega_1 - \omega_2)^2$
- (2) $\frac{I}{8}(\omega_1 - \omega_2)^2$
- (3) $\frac{1}{2}I(\omega_1 + \omega_2)^2$
- **(4)** $\frac{1}{4}I(\omega_1 - \omega_2)^2$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\Delta \mathrm{KE} = \frac{1}{2}\frac{I_1 I_2}{I_1 + I_2}(\omega_1 - \omega_2)^2$
2. $= \frac{1}{2}\frac{I^2}{(2I)}(\omega_1 - \omega_2)^2$
3. $= \frac{1}{4}I(\omega_1 - \omega_2)^2$

**Solved independently** (answer withheld)

1. No external torque acts, so angular momentum is conserved: $I\omega_1 + I\omega_2 = 2I\omega$.
2. $\omega = \frac{\omega_1 + \omega_2}{2}$.
3. Initial kinetic energy: $K_i = \frac{1}{2}I\omega_1^2 + \frac{1}{2}I\omega_2^2 = \frac{1}{2}I(\omega_1^2 + \omega_2^2)$.
4. Final kinetic energy: $K_f = \frac{1}{2}(2I)\left(\frac{\omega_1 + \omega_2}{2}\right)^2 = \frac{1}{4}I(\omega_1 + \omega_2)^2$.
5. $\Delta K = K_i - K_f = \frac{1}{4}I\left[2\omega_1^2 + 2\omega_2^2 - (\omega_1 + \omega_2)^2\right]$.
6. $\Delta K = \frac{1}{4}I(\omega_1^2 - 2\omega_1\omega_2 + \omega_2^2) = \frac{1}{4}I(\omega_1 - \omega_2)^2$, which is option $4$.

**Subtopic:** Conservation of Angular Momentum, Kinetic Energy of a Rigid Body Rotating About a Given Axis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q019_db96b41b_30102026.png?v=db96b41b923f)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q019_bf948796_30102026.png?v=bf9487962a7a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** When two rotating discs couple, angular momentum is conserved and the kinetic energy lost is fixed by the difference of their angular velocities, never by their sum
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The loss in a rotational coupling is $\frac{1}{2}I_{eff}(\omega_1-\omega_2)^2$ with $I_{eff}$ the reduced moment $\frac{I\cdot I}{I+I}=\frac{I}{2}$; putting the combined moment $2I$ in that slot gives $I(\omega_1-\omega_2)^2$.
- **Why:** This question requires deriving the energy lost when two rotating bodies couple, demonstrated by the stem asking for 'the expression for loss of energy during this process' with only $I$, $\omega_1$ and $\omega_2$ supplied.
<!--/ecat-->

## Q20

Physics · Thermodynamics

Thermodynamic processes are indicated in the following diagram.
Match the following

![printed figure: P-V diagram with isotherms 700 K, 500 K, 300 K and processes I-IV from state i](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q020_94e03df0_30102026.svg?v=94e03df090a3)

*P-V diagram with isotherms 700 K, 500 K, 300 K and processes I-IV from state i*

![drawn: P-V diagram with isotherms 700 K, 500 K, 300 K and processes I-IV from state i](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q020_question_0d1ed2fe_30102026.svg?v=0d1ed2febb39)  
*drawn on the booklet's geometry, checked against its figure spec*

| List-I | | List-II | |
|---|---|---|---|
| P | Process I | a | Adiabatic |
| Q | Process II | b | Isobaric |
| R | Process III | c | Isochoric |
| S | Process IV | d | Isothermal |

- (1) P $\rightarrow$ c, Q $\rightarrow$ d, R $\rightarrow$ b, S $\rightarrow$ a
- (2) P $\rightarrow$ d, Q $\rightarrow$ b, R $\rightarrow$ a, S $\rightarrow$ c
- (3) P $\rightarrow$ a, Q $\rightarrow$ c, R $\rightarrow$ d, S $\rightarrow$ b
- **(4)** P $\rightarrow$ c, Q $\rightarrow$ a, R $\rightarrow$ d, S $\rightarrow$ b

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Process I = Isochoric
2. II = Adiabatic
3. III = Isothermal
4. IV = Isobaric

**Solved independently** (answer withheld)

1. Process I is a vertical line on the $P$-$V$ diagram, so $V$ is constant: isochoric, $P \rightarrow c$.
2. Process IV is a horizontal line, so $P$ is constant: isobaric, $S \rightarrow b$.
3. Process III starts at $i$ and ends at $f$ on the same $500\,\text{K}$ curve, so $T$ is constant: isothermal, $R \rightarrow d$.
4. Process II is steeper than the isotherm and ends on the $300\,\text{K}$ curve; an adiabat has slope $\frac{dP}{dV} = -\gamma \frac{P}{V}$, steeper than an isotherm's $-\frac{P}{V}$: adiabatic, $Q \rightarrow a$.
5. $P \rightarrow c,\ Q \rightarrow a,\ R \rightarrow d,\ S \rightarrow b$ is option $4$.

**Subtopic:** Problems on Different Graphs of P, V, and T, Thermodynamic Processes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q020_010672cb_30102026.png?v=010672cbc117)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q020_57ba5fe0_30102026.png?v=57ba5fe055eb)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** On a $P$-$V$ diagram a vertical path is isochoric and a horizontal one isobaric; a path that runs along an isotherm is isothermal, while one that cuts across to a lower isotherm is adiabatic
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  'An adiabat is steeper than an isotherm' taken to its limit makes the vertical segment I the adiabatic path, and the only label then left for the curve II is isochoric
- **Why:** This question requires each printed path to be read for what it holds constant, demonstrated by the figure's three isotherms labelled 700 K, 500 K and 300 K with processes I to IV all leaving the one state $i$.
- **Note:** The figure was supplied as a checked spec - all 14 printed labels present, every printed line covered - so the geometry could be read directly: I is vertical from $i$, IV is horizontal, III runs along the 500 K isotherm that passes through $i$, and II leaves that isotherm and ends on the 300 K one. That is the printed key, option 4. asks is read_diagram and not compare: every row is settled by looking at one path in the figure, and nothing in the question asks the four process names to be told apart in the abstract.
<!--/ecat-->

## Q21

Physics · Mechanical Properties of Solids

The bulk modulus of a spherical object is ‘$B$’. If it is subjected to uniform pressure ‘$p$’, the fractional decrease in radius is

- (1) $\dfrac{3p}{B}$
- **(2)** $\dfrac{p}{3B}$
- (3) $\dfrac{p}{B}$
- (4) $\dfrac{B}{3p}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $B = \frac{p}{\left(\frac{\Delta V}{V}\right)}$
2. $\frac{\Delta V}{V} = \frac{p}{B}$
3. $3\frac{\Delta r}{r} = \frac{p}{B}$
4. $\frac{\Delta r}{r} = \frac{p}{3B}$

**Solved independently** (answer withheld)

1. By definition of bulk modulus, $B = \frac{p}{\Delta V / V}$, so $\frac{\Delta V}{V} = \frac{p}{B}$.
2. For a sphere $V = \frac{4}{3}\pi r^3$, so $\frac{\Delta V}{V} = 3\frac{\Delta r}{r}$.
3. Equating, $3\frac{\Delta r}{r} = \frac{p}{B}$.
4. $\frac{\Delta r}{r} = \frac{p}{3B}$, which is option $2$.

**Subtopic:** Relation Between Density, Pressure and Bulk Modulus · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q021_d51a821c_30102026.png?v=d51a821c23d2)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q021_2991cfc6_30102026.png?v=2991cfc6b7d3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Bulk modulus ties pressure to volume strain, and for a sphere the volume strain is three times the linear strain
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\frac{p}{B}$ is the fractional decrease in VOLUME, which the first line of the solution hands over; the stem asks for the fractional decrease in radius, which is a third of it.
- **Why:** This question requires converting a volume strain into a linear strain through the bulk-modulus definition, demonstrated by the stem asking for 'the fractional decrease in radius' of a sphere 'subjected to uniform pressure p'.
<!--/ecat-->

## Q22

Physics · Gravitation

The acceleration due to gravity at a height $1\,\mathrm{km}$ above the earth is the same as at a depth $d$ below the surface of earth. Then

- (1) $d = \frac{3}{2}\,\mathrm{km}$
- **(2)** $d = 2\,\mathrm{km}$
- (3) $d = \frac{1}{2}\,\mathrm{km}$
- (4) $d = 1\,\mathrm{km}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Above earth surface
2. $g' = g\left(1 - \frac{2h}{R_e}\right)$
3. $\Delta g' = g\frac{2h}{R_e}$ $\ldots(1)$
4. Below earth surface
5. $g' = g\left(1 - \frac{d}{R_e}\right)$
6. $\Delta g = g\frac{d}{R_e}$ $\ldots(2)$
7. From $(1)$ & $(2)$
8. $d = 2h$
9. $d = 2 \times 1\,\mathrm{km}$

**Solved independently** (answer withheld)

1. For a small height $h \ll R$, $g_h = g\left(1 - \frac{2h}{R}\right)$.
2. At depth $d$, $g_d = g\left(1 - \frac{d}{R}\right)$.
3. Setting $g_h = g_d$: $\frac{2h}{R} = \frac{d}{R}$, so $d = 2h$.
4. $d = 2 \times 1\,\mathrm{km} = 2\,\mathrm{km}$, which is option $2$.

**Subtopic:** Variation in g Due to Height and Rotation, Variation in g Due to Depth Inside the Earth · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q022_10b3e9eb_30102026.png?v=10b3e9eb41d5)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q022_31abdcbb_30102026.png?v=31abdcbba220)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** g falls off twice as fast with height as with depth: $g_h = g(1-2h/R)$ against $g_d = g(1-d/R)$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  One and the same variation used above and below the surface, each entering as $1-x/R$, makes the two equal when $d=h$, which prints as $d=1$ km.
- **Why:** This question requires equating two different variations of g, demonstrated by the stem setting the value 'at a height 1 km above the earth' equal to the value 'at a depth d below the surface'.
<!--/ecat-->

## Q23

Physics · Electrostatics

The diagrams below show regions of equipotentials. A positive charge is moved from $A$ to $B$ in each diagram.

![printed figure: Four equipotential regions (a)-(d) with a charge moved from A to B](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q023_f2ba62b4_30102026.svg?v=f2ba62b4320d)

*Four equipotential regions (a)-(d) with a charge moved from A to B*

![drawn: Four equipotential regions (a)-(d) with a charge moved from A to B](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q023_question_d314ab05_30102026.svg?v=d314ab05f306)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) Minimum work is required to move $q$ in figure (a).
- (2) Maximum work is required to move $q$ in figure (b).
- (3) Maximum work is required to move $q$ in figure (c).
- **(4)** In all the four cases the work done is the same.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Work done $w = q\Delta V$
2. $\Delta V$ is same in all the cases so work is done will be same in all the cases.

**Solved independently** (answer withheld)

1. The work done by an external agent in moving charge $q$ slowly from $A$ to $B$ is $W = q(V_B - V_A)$, which is independent of the path and of the shape of the equipotentials.
2. From the figure, in each of (a), (b), (c) and (d), $A$ lies on the $10\,\text{V}$ surface and $B$ lies on the $40\,\text{V}$ surface, so $V_A = 10\,\text{V}$ and $V_B = 40\,\text{V}$.
3. $W = q(40 - 10)\,\text{V} = 30q$ for every figure, so the work done is the same in all four cases, which is option $4$.

**Subtopic:** Equipotential Surfaces · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q023_cbcbffbb_30102026.png?v=cbcbffbbba1f)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q023_bdb6833b_30102026.png?v=bdb6833b425a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Work done carrying a charge between two equipotentials depends only on the potential difference between them, not on the path length, the spacing of the surfaces or their shape
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Reading the work as force times the drawn separation picks figure (c), where the A-to-B gap is the widest of the four and the equipotentials are unevenly spaced.
- **Why:** This question requires reading the end-point potentials off four drawings instead of their geometry, demonstrated by every figure placing A on the 10 V surface and B on the 40 V surface while option 4 reads 'In all the four cases the work done is the same.'
- **Note:** The pattern classifier called this statement_options because each option is a full sentence; recorded as mcq because the stem prints no lettered statement block and no instruction to judge statements, only a description of the figures. The figure spec was supplied with all 28 labels printed, so A, B and the four potentials could be read directly.
<!--/ecat-->

## Q24

Physics · Kinematics

Preeti reached the metro station and found that the escalator was not working. She walked up the stationary escalator in time $t_1$. On other days, if she remains stationary on the moving escalator, then the escalator takes her up in time $t_2$. The time taken by her to walk up on the moving escalator will be

- **(1)** $\dfrac{t_1 t_2}{t_2 + t_1}$
- (2) $t_1 - t_2$
- (3) $\dfrac{t_1 + t_2}{2}$
- (4) $\dfrac{t_1 t_2}{t_2 - t_1}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Velocity of girl w.r.t. elevator $= \frac{d}{t_1} = v_{ge}$
2. Velocity of elevator w.r.t. ground $v_{eG} = \frac{d}{t_2}$
3. then velocity of girl w.r.t. ground $\vec{v}_{gG} = \vec{v}_{ge} + \vec{v}_{eG}$
4. i.e, $v_{gG} = v_{ge} + v_{eG}$
5. $\frac{d}{t} = \frac{d}{t_1} + \frac{d}{t_2}$
6. $\frac{1}{t} = \frac{1}{t_1} + \frac{1}{t_2}$
7. $t = \frac{t_1 t_2}{(t_1 + t_2)}$

**Solved independently** (answer withheld)

1. Let the escalator length be $L$. Her walking speed relative to the escalator is $v_1 = \frac{L}{t_1}$.
2. The escalator's speed is $v_2 = \frac{L}{t_2}$.
3. Walking up the moving escalator, the speeds add: $v = v_1 + v_2 = \frac{L}{t_1} + \frac{L}{t_2} = \frac{L(t_1 + t_2)}{t_1 t_2}$.
4. $t = \frac{L}{v} = \frac{t_1 t_2}{t_1 + t_2}$, which is option $1$.

**Subtopic:** Relative Motion in 1D · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q024_390b5621_30102026.png?v=390b5621a611)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q024_538e75b6_30102026.png?v=538e75b62534)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Her walking speed and the escalator's speed add, so the reciprocals of the two times add: $\frac{1}{t}=\frac{1}{t_1}+\frac{1}{t_2}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  $\frac{t_1t_2}{t_2-t_1}$ is the combined-time form for two speeds that oppose each other, and here the walk and the escalator are both upward.
- **Why:** This question requires adding two speeds and converting back to a time, demonstrated by the stem supplying the time up 'the stationary escalator' and the time 'stationary on the moving escalator' and asking for the time doing both at once.
<!--/ecat-->

## Q25

Physics · Laws of Motion

Two blocks $A$ and $B$ of masses $3m$ and $m$ respectively are connected by a massless and inextensible string. The whole system is suspended by a massless spring as shown in figure. The magnitudes of acceleration of $A$ and $B$ immediately after the string is cut, are respectively

![printed figure: Block A (3m) hung from a ceiling spring, block B (m) hung from A by a string](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q025_2b72e92b_30102026.svg?v=2b72e92b0eaa)

*Block A (3m) hung from a ceiling spring, block B (m) hung from A by a string*

![drawn: Block A (3m) hung from a ceiling spring, block B (m) hung from A by a string](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q025_question_828cffad_30102026.svg?v=828cffad7514)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $g$, $g$
- (2) $\frac{g}{3}$, $\frac{g}{3}$
- (3) $g$, $\frac{g}{3}$
- **(4)** $\frac{g}{3}$, $g$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Free-body diagram of block 3m: kx upward, T and 3mg downward](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q025_sol_1_20270bf4_30102026.svg?v=20270bf453f3)

*Free-body diagram of block 3m: kx upward, T and 3mg downward*

![drawn: Free-body diagram of block 3m: kx upward, T and 3mg downward](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q025_solution_1_bcce492d_30102026.svg?v=bcce492da27c)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Before the string is cut
2. $kx = T + 3mg$ ...(1)
3. $T = mg$ ...(2)

![printed figure: Free-body diagram of block m: tension T up, weight mg down](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q025_sol_2_97151a35_30102026.svg?v=97151a355ec9)

*Free-body diagram of block m: tension T up, weight mg down*

![drawn: Free-body diagram of block m: tension T up, weight mg down](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q025_solution_2_48716171_30102026.svg?v=487161710948)  
*drawn on the booklet's geometry, checked against its figure spec*

4. $\Rightarrow kx = 4mg$
5. After the string is cut, $T = 0$

![printed figure: Free-body diagrams of block 3m (kx up, 3mg down) and block m (mg down, a = g) just after the string is cut](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q025_sol_3_88b7c5c7_30102026.svg?v=88b7c5c7a6f4)

*Free-body diagrams of block 3m (kx up, 3mg down) and block m (mg down, a = g) just after the string is cut*

![drawn: Free-body diagrams of block 3m (kx up, 3mg down) and block m (mg down, a = g) just after the string is cut](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q025_solution_3_9e7fc41a_30102026.svg?v=9e7fc41a877d)  
*drawn on the booklet's geometry, checked against its figure spec*

6. $a = \frac{kx - 3mg}{3m}$
7. $a = \frac{4mg - 3mg}{3m}$
8. $a = \frac{g}{3}\uparrow$

**Solved independently** (answer withheld)

1. In equilibrium the spring supports both blocks: $kx = (3m + m)g = 4mg$.
2. The spring extension cannot change instantaneously, so just after the cut the spring force on $A$ is still $4mg$ upward.
3. For $A$: $kx - 3mg = 3m\,a_A \Rightarrow 4mg - 3mg = 3m\,a_A$.
4. $a_A = \frac{mg}{3m} = \frac{g}{3}$.
5. For $B$: the string tension becomes zero, so only gravity acts and $a_B = g$.
6. Magnitudes are $\frac{g}{3}$ and $g$ respectively, which is option $4$.

**Subtopic:** Block and Spring Problem · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q025_7a3d65fa_30102026.png?v=7a3d65fa758c)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q025_f9ae53f1_30102026.png?v=f9ae53f168dd)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A spring's length, and so its force, cannot change in the instant the string is cut, while the string's tension vanishes at once
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Both magnitudes are right and tied to the wrong blocks: g belongs to the freed block B and $\frac{g}{3}$ to A, which the stretched spring still holds.
- **Why:** This question requires two accelerations at the same instant, one set by the spring's unchanged force and one by free fall, demonstrated by the stem asking for 'the magnitudes of acceleration of A and B immediately after the string is cut, are respectively'.
- **Note:** The pattern classifier's multi_part_respectively is recorded here as two_part: each option prints a pair of accelerations judged whole.
<!--/ecat-->

## Q26

Physics · Thermal Properties of Matter

A spherical black body with a radius of $12\,\mathrm{cm}$ radiates $450\,\mathrm{watt}$ power at $500\,\mathrm{K}$. If the radius were halved and the temperature doubled, the power radiated in watt would be

- (1) $1000$
- **(2)** $1800$
- (3) $225$
- (4) $450$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rate of power loss
2. $r \propto R^{2}T^{4}$
3. $\frac{r_1}{r_2} = \frac{R_1^{2}T_1^{4}}{R_2^{2}T_2^{4}}$
4. $= 4 \times \frac{1}{16}$
5. $\frac{450}{r_2} = \frac{1}{4}$
6. $r_2 = 1800\,\mathrm{watt}$

**Solved independently** (answer withheld)

1. By the Stefan-Boltzmann law for a black sphere, $P = \sigma (4\pi r^2) T^4$, so $P \propto r^2 T^4$.
2. $\frac{P'}{P} = \left(\frac{r'}{r}\right)^2 \left(\frac{T'}{T}\right)^4 = \left(\frac{1}{2}\right)^2 (2)^4$.
3. $\left(\frac{1}{2}\right)^2 (2)^4 = \frac{1}{4} \times 16 = 4$.
4. $P' = 4 \times 450\,\mathrm{W} = 1800\,\mathrm{W}$, which is option $2$.

**Subtopic:** Radiation Laws · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q026_04c1dc91_30102026.png?v=04c1dc914bca)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q026_9ba561b5_30102026.png?v=9ba561b508db)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Stefan's law: a black body's radiated power goes as the square of its radius and the fourth power of its absolute temperature
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  With the temperature taken to the second power instead of the fourth, the quarter from halving the radius and the four from doubling T cancel exactly, and the power comes back as the 450 W the stem printed.
- **Why:** This question requires scaling one quantity by the changes in two others, demonstrated by the stem reading 'if the radius were halved and the temperature doubled, the power radiated in watt would be'.
<!--/ecat-->

## Q27

Physics · Thermal Properties of Matter

Two rods $A$ and $B$ of different materials are welded together as shown in figure. Their thermal conductivities are $K_1$ and $K_2$. The thermal conductivity of the composite rod will be

![printed figure: Two rods A (K1) and B (K2) welded side by side along length d, ends at T1 and T2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q027_8e0aa54b_30102026.svg?v=8e0aa54b88eb)

*Two rods A (K1) and B (K2) welded side by side along length d, ends at T1 and T2*

![drawn: Two rods A (K1) and B (K2) welded side by side along length d, ends at T1 and T2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q027_question_fe45c1b6_30102026.svg?v=fe45c1b611cb)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $K_1 + K_2$
- (2) $2(K_1 + K_2)$
- **(3)** $\dfrac{K_1 + K_2}{2}$
- (4) $\dfrac{3(K_1 + K_2)}{2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Thermal current
2. $H = H_1 + H_2$
3. $= \frac{K_1 A(T_1 - T_2)}{d} + \frac{K_2 A(T_1 - T_2)}{d}$
4. $\frac{K_{EQ} 2A(T_1 - T_2)}{d} = \frac{A(T_1 - T_2)}{d}[K_1 + K_2]$
5. $K_{EQ} = \left[\frac{K_1 + K_2}{2}\right]$

**Solved independently** (answer withheld)

1. The figure shows $A$ and $B$ stacked one above the other, both spanning from $T_1$ to $T_2$ over length $d$, so they conduct in parallel.
2. Heat current through $A$: $H_1 = \frac{K_1 A (T_1 - T_2)}{d}$; through $B$: $H_2 = \frac{K_2 A (T_1 - T_2)}{d}$, taking equal cross-sections $A$.
3. Composite rod of area $2A$: $H = H_1 + H_2 = \frac{K_{eq} (2A)(T_1 - T_2)}{d}$.
4. $K_{eq} \cdot 2A = K_1 A + K_2 A \Rightarrow K_{eq} = \frac{K_1 + K_2}{2}$, which is option $3$.

**Subtopic:** Connection of Rods · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q027_0cdf4cf6_30102026.png?v=0cdf4cf69cd8)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q027_2541cb38_30102026.png?v=2541cb382d30)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Rods welded side by side conduct in parallel: the conductances add, and the composite's conductivity is the area-weighted average of the two
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Adding the two conductivities, the way conductances in parallel are added, leaves out that the composite rod also has twice the cross-section of either rod.
- **Why:** This question requires combining two conductivities for a side-by-side weld, demonstrated by the figure placing both rods across the whole length d between $T_1$ and $T_2$ with equal cross-sections.
<!--/ecat-->

## Q28

Physics · Laws of Motion

One end of string of length $l$ is connected to a particle of mass ‘$m$’ and the other end is connected to a small peg on a smooth horizontal table. If the particle moves in circle with speed ‘$v$’, the net force on the particle (directed towards center) will be ($T$ represents the tension in the string)

- (1) $T-\frac{mv^{2}}{l}$
- (2) Zero
- **(3)** $T$
- (4) $T+\frac{mv^{2}}{l}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Centripetal force $\left(\frac{mv^{2}}{l}\right)$ is provided by tension so the net force will be equal to tension i.e., $T$.

**Solved independently** (answer withheld)

1. Vertically, the normal reaction balances gravity: $N - mg = 0$.
2. The table is smooth, so there is no friction; the only horizontal force is the tension $T$, directed toward the peg (centre).
3. Net force toward the centre: $F_{net} = T$, which provides the centripetal force, $T = \frac{mv^{2}}{l}$.
4. So the net force is $T$, which is option $3$.

**Subtopic:** Tension in String in Circular Motion · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q028_bef62cab_30102026.png?v=bef62cab2299)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q028_74f4b7fc_30102026.png?v=74f4b7fc3c14)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $\frac{mv^2}{l}$ is the centripetal force required, not an extra force acting; on a smooth table the string's tension is the whole of the net inward force
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Writing $T-\frac{mv^2}{l}$ treats the centripetal requirement as a second, outward force to be taken off the tension — the balance that belongs to the rotating frame, not to the table.
- **Why:** This question requires deciding which forces actually act on the particle before any formula is used, demonstrated by the stem specifying a 'smooth horizontal table' and asking for 'the net force on the particle (directed towards center)' with T defined as the tension.
<!--/ecat-->

## Q29

Physics · Semiconductor Electronics

In a common emitter transistor amplifier the audio signal voltage across the collector is $3\,\mathrm{V}$. The resistance of collector is $3\,\mathrm{k\Omega}$. If current gain is $100$ and the base resistance is $2\,\mathrm{k\Omega}$, the voltage and power gain of the amplifier is

- **(1)** 150 and 15000
- (2) 20 and 2000
- (3) 200 and 1000
- (4) 15 and 200

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Current gain $(\beta) = 100$
2. Voltage gain $(A_V) = \beta\frac{R_c}{R_b}$
3. $= 100\left(\frac{3}{2}\right)$
4. $= 150$
5. Power gain $= A_V\,\beta$
6. $= 150\,(100)$
7. $= 15000$

**Solved independently** (answer withheld)

1. For a common emitter amplifier, voltage gain $A_v = \beta \frac{R_C}{R_B}$.
2. $A_v = 100 \times \frac{3\,\mathrm{k\Omega}}{2\,\mathrm{k\Omega}} = 150$.
3. Power gain $A_p = \beta \times A_v$.
4. $A_p = 100 \times 150 = 15000$.
5. $150$ and $15000$ matches option $1$.

**Subtopic:** Transistor as an Amplifier (Common Emitter Configuration): Voltage, Current and Power Gain · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 9)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q029_f3bcd2ac_30102026.png?v=f3bcd2ac9b96)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q029_53635350_30102026.png?v=536353503c7a)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a common-emitter amplifier the voltage gain is $\beta R_C/R_B$ and the power gain is that voltage gain times the current gain
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  20 is the input signal in millivolts, which the standard working produces on the way — $I_C=1$ mA, $I_B=10\,\mu$A, $V_{in}=I_BR_B=20$ mV — and 2000 is that 20 carried through the power-gain step.
- **Why:** This question requires both gains of a common-emitter stage at once, demonstrated by the stem asking for 'the voltage and power gain of the amplifier' and every option printing two numbers.
- **Note:** The pattern classifier defaulted to plain_mcq; recorded as two_part because each option prints a voltage gain and a power gain judged together. Two fillers here is itself the finding about this option set: only options 1 and 2 are internally consistent with power gain = voltage gain x current gain.
<!--/ecat-->

## Q30

Physics · Center of Mass

Which of the following statements are correct?

- **((a))** Centre of mass of a body always coincides with the centre of gravity of the body.
- **((b))** Centre of mass of a body is the point at which the total gravitational torque on the body is zero
- **((c))** A couple on a body produce both translational and rotational motion in a body.
- **((d))** Mechanical advantage greater than one means that small effort can be used to lift a large load.

- (1) (b) and (c)
- (2) (c) and (d)
- **(3)** (b) and (d)
- (4) (a) and (b)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Centre of mass may or may not coincide with centre of gravity.

**Solved independently** (answer withheld)

1. (a): The centre of mass coincides with the centre of gravity only when $\vec g$ is uniform over the body, so 'always' makes (a) false.
2. (b): The total gravitational torque $\sum \vec r_i \times m_i \vec g$ vanishes about the centre of gravity; for uniform $\vec g$ this is $\left(\sum m_i \vec r_i\right) \times \vec g = 0$ about the centre of mass, so (b) is taken as true.
3. (c): A couple is two equal and opposite forces, so $\vec F_{net} = 0$ and there is no translational motion, only rotation; (c) is false.
4. (d): $\text{M.A.} = \frac{\text{Load}}{\text{Effort}} > 1 \Rightarrow \text{Effort} < \text{Load}$, so a small effort lifts a large load; (d) is true.
5. The correct statements are (b) and (d), which is option $3$.

**Subtopic:** Center of Gravity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q030_906bd38d_30102026.png?v=906bd38d6720)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q030_0bb39aac_30102026.png?v=0bb39aac8594)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Centre of gravity is the point where the total gravitational torque vanishes and coincides with the centre of mass only while the field over the body is uniform; a couple, having zero resultant force, turns a body without translating it
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The textbook line that the centre of gravity of a body coincides with its centre of mass makes (a) read as settled once the word 'always' is skimmed, and (b) is printed with the very same two terms, so the pair looks like one idea said twice; (a) fails because the two points separate as soon as the gravitational field across the body is non-uniform.
- **Why:** This question requires four printed statements to be graded one by one against the definitions the textbook states, demonstrated by the stem 'Which of the following statements are correct?' standing above the block (a) to (d) and by every option naming a pair of those letters.
- **Note:** Statement (b) as printed defines the centre of MASS as the point of zero total gravitational torque, which is the textbook's definition of the centre of GRAVITY; the key counts (b) as correct, which holds only under the uniform-field assumption that makes the two points the same. The question is tagged as printed and the key is not re-judged.
<!--/ecat-->

## Q31

Physics · Rotational Motion

A rope is wound around a hollow cylinder of mass $3\,\mathrm{kg}$ and radius $40\,\mathrm{cm}$. What is the angular acceleration of the cylinder if the rope is pulled with a force of $30\,\mathrm{N}$?

- **(1)** $25\,\mathrm{rad/s^2}$
- (2) $5\,\mathrm{m/s^2}$
- (3) $25\,\mathrm{m/s^2}$
- (4) $0.25\,\mathrm{rad/s^2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Rope wound on a cylinder of radius 40 cm pulled down tangentially with F = 30 N](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q031_sol_1_46158344_30102026.svg?v=461583444b60)

*Rope wound on a cylinder of radius 40 cm pulled down tangentially with F = 30 N*

![drawn: Rope wound on a cylinder of radius 40 cm pulled down tangentially with F = 30 N](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q031_solution_1_f25ca29b_30102026.svg?v=f25ca29b4179)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\tau = I\,\alpha$
2. $F \times R = MR^{2}\alpha$
3. $30 \times 0.4 = 3 \times (0.4)^{2}\,\alpha$
4. $12 = 3 \times 0.16\,\alpha$
5. $400 = 16\,\alpha$
6. $\alpha = 25\,\mathrm{rad/s^{2}}$

**Solved independently** (answer withheld)

1. The rope applies a tangential force at the rim, so the torque is $\tau = F R = 30\,\mathrm{N} \times 0.4\,\mathrm{m} = 12\,\mathrm{N\,m}$.
2. For a thin hollow cylinder about its axis, $I = M R^2 = 3\,\mathrm{kg} \times (0.4\,\mathrm{m})^2 = 0.48\,\mathrm{kg\,m^2}$.
3. $\alpha = \frac{\tau}{I} = \frac{12}{0.48} = 25\,\mathrm{rad/s^2}$.
4. Angular acceleration has units of $\mathrm{rad/s^2}$, so the answer is $25\,\mathrm{rad/s^2}$, which is option $1$.

**Subtopic:** Problems on Torque of a Force About the Axis of Rotation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q031_6f071fac_30102026.png?v=6f071facac17)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q031_19a4c9c1_30102026.png?v=19a4c9c11371)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Angular acceleration is torque over moment of inertia, and for a hollow cylinder $I=MR^2$, so $\alpha=\frac{F}{MR}$ with R in metres
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Keeping the radius as the printed 40 instead of 0.4 m gives $\alpha=\frac{30}{3\times40}=0.25\ \mathrm{rad/s^2}$, with every piece of the physics correct.
- **Why:** This question requires a torque divided by a moment of inertia, demonstrated by the stem giving a pull of '30 N' on a 'hollow cylinder' of radius '40 cm' and asking for the angular acceleration.
<!--/ecat-->

## Q32

Physics · Electromagnetic Induction

A long solenoid of diameter $0.1\,\mathrm{m}$ has $2 \times 10^{4}$ turns per meter. At the centre of the solenoid, a coil of 100 turns and radius $0.01\,\mathrm{m}$ is placed with its axis coinciding with the solenoid axis. The current in the solenoid reduces at a constant rate to $0\,\mathrm{A}$ from $4\,\mathrm{A}$ in $0.05\,\mathrm{s}$. If the resistance of the coil is $10\pi^{2}\,\Omega$, the total charge flowing through the coil during this time is

- **(1)** $32\,\mu\mathrm{C}$
- (2) $16\pi\,\mu\mathrm{C}$
- (3) $32\pi\,\mu\mathrm{C}$
- (4) $16\,\mu\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\varepsilon = -N\frac{d\phi}{dt}$
2. $\left|\frac{\varepsilon}{R}\right| = \frac{N}{R}\frac{d\phi}{dt}$
3. $dq = \frac{N}{R}d\phi$
4. $\Delta Q = \frac{N(\Delta\phi)}{R}$
5. $\Delta Q = \frac{\Delta\phi_{\mathrm{total}}}{R}$
6. $= \frac{(NBA)}{R}$
7. $= \frac{\mu_{0}ni\pi r^{2}}{R}$
8. Putting values
9. $= \frac{4\pi \times 10^{-7} \times 100 \times 4 \times \pi \times (0.01)^{2}}{10\pi^{2}}$
10. $\Delta Q = 32\,\mu\mathrm{C}$

**Solved independently** (answer withheld)

1. Field inside the long solenoid: $B = \mu_0 n I$, uniform over the coil since the coil radius $0.01\,\mathrm{m}$ is less than the solenoid radius $0.05\,\mathrm{m}$.
2. Flux linkage through the coil: $N\Phi = N \mu_0 n I \pi r^2$.
3. Change in flux linkage as $I$ goes from $4\,\mathrm{A}$ to $0$: $\Delta(N\Phi) = 100 \times 4\pi \times 10^{-7} \times 2 \times 10^{4} \times 4 \times \pi (0.01)^2$.
4. Evaluate: $\Delta(N\Phi) = 3.2\pi^2 \times 10^{-4}\,\mathrm{Wb}$.
5. Charge through the coil: $Q = \frac{\Delta(N\Phi)}{R} = \frac{3.2\pi^2 \times 10^{-4}}{10\pi^2}$.
6. $Q = 3.2 \times 10^{-5}\,\mathrm{C} = 32\,\mu\mathrm{C}$, which is option $1$.

**Subtopic:** Faraday's Law of Electromagnetic Induction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q032_1cd27a35_30102026.png?v=1cd27a357fae)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q032_9ce4146c_30102026.png?v=9ce4146c43da)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The charge that flows is the whole flux change divided by the resistance, $q=\frac{N\Delta(BA)}{R}$, so the time taken never enters
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  The $\pi$ in $\mu_0=4\pi\times10^{-7}$ and the $\pi$ in the coil's area $\pi r^2$ make a $\pi^2$ that the printed $10\pi^2\ \Omega$ cancels exactly; leaving one $\pi$ uncancelled turns $32\ \mu$C into $32\pi\ \mu$C.
- **Why:** This question requires the flux change through the coil divided by its resistance, demonstrated by the stem reading 'the resistance of the coil is $10\pi^2\ \Omega$' and asking for 'the total charge flowing through the coil during this time'.
<!--/ecat-->

## Q33

Physics · Modern Physics

The ratio of wavelengths of the last line of Balmer series and the last line of Lyman series is

- **(1)** 4
- (2) 0.5
- (3) 2
- (4) 1

**Answer** — booklet: (1) · independent solve: (1) · agree

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

1. The last line of a series is its series limit, the transition from $n_i = \infty$.
2. Balmer limit: $\frac{1}{\lambda_B} = R\left(\frac{1}{2^2} - \frac{1}{\infty^2}\right) = \frac{R}{4}$, so $\lambda_B = \frac{4}{R}$.
3. Lyman limit: $\frac{1}{\lambda_L} = R\left(\frac{1}{1^2} - \frac{1}{\infty^2}\right) = R$, so $\lambda_L = \frac{1}{R}$.
4. $\frac{\lambda_B}{\lambda_L} = \frac{4/R}{1/R} = 4$, which is option $1$.

**Subtopic:** Spectral Lines of Hydrogen Atom · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q033_9bbdb2f4_30102026.png?v=9bbdb2f48d61)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q033_2de4066f_30102026.png?v=2de4066f0931)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The last line of a hydrogen series is its limit, $n_{upper}\to\infty$, so the limit wavelength is $\frac{n_{lower}^2}{R}$ — $\frac{4}{R}$ for Balmer and $\frac{1}{R}$ for Lyman
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Taking the limit wavelength as proportional to the lower level n rather than to $n^2$ gives $\frac{2}{1}=2$ in place of $\frac{4}{1}=4$.
- **Why:** This question requires the series-limit wavelength of two hydrogen series and their ratio, demonstrated by the stem asking for 'the last line of Balmer series and the last line of Lyman series'.
<!--/ecat-->

## Q34

Physics · Electrostatics

Suppose the charge of a proton and an electron differ slightly. One of them is $-e$, the other is $(e + \Delta e)$. If the net of electrostatic force and gravitational force between two hydrogen atoms placed at a distance $d$ (much greater than atomic size) apart is zero, then $\Delta e$ is of the order of [Given mass of hydrogen $m_h = 1.67 \times 10^{-27}\,\mathrm{kg}$]

- **(1)** $10^{-37}\,\mathrm{C}$
- (2) $10^{-47}\,\mathrm{C}$
- (3) $10^{-20}\,\mathrm{C}$
- (4) $10^{-23}\,\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $F_e = F_g$
2. $\frac{1}{4\pi\varepsilon_0}\frac{\Delta e^2}{d^2} = \frac{Gm^2}{d^2}$
3. $9 \times 10^{9}\,(\Delta e^2) = 6.67 \times 10^{-11} \times 1.67 \times 10^{-27} \times 1.67 \times 10^{-27}$
4. $\Delta e^2 = \frac{6.67 \times 1.67 \times 1.67}{9} \times 10^{-74}$
5. $\Delta e \approx 10^{-37}$

**Solved independently** (answer withheld)

1. Each hydrogen atom has net charge $q = (e + \Delta e) - e = \Delta e$.
2. Electrostatic repulsion between the atoms: $F_e = \frac{1}{4\pi\varepsilon_0}\frac{(\Delta e)^2}{d^2}$.
3. Gravitational attraction between the atoms: $F_g = \frac{G m_h^2}{d^2}$.
4. Net force zero means $F_e = F_g$, so $\frac{(\Delta e)^2}{4\pi\varepsilon_0} = G m_h^2$.
5. $\Delta e = m_h\sqrt{4\pi\varepsilon_0 G} = m_h\sqrt{\frac{G}{k}}$ with $k = 9\times10^{9}\,\mathrm{N\,m^2\,C^{-2}}$.
6. $\sqrt{\frac{6.67\times10^{-11}}{9\times10^{9}}} = \sqrt{7.41\times10^{-21}} \approx 8.6\times10^{-11}$.
7. $\Delta e \approx 1.67\times10^{-27} \times 8.6\times10^{-11} \approx 1.44\times10^{-37}\,\mathrm{C}$, of the order $10^{-37}\,\mathrm{C}$, which is option $1$.

**Subtopic:** Coulomb's Law · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 10)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q034_46195762_30102026.png?v=461957621041)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q034_d9766af1_30102026.png?v=d9766af14ade)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Setting the Coulomb repulsion of two charges $\Delta e$ equal to the gravitational attraction of two hydrogen masses gives $\Delta e=m_h\sqrt{G/k}$, with the separation cancelling out
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Leaving the square root off $\frac{G}{k}$ gives $m_h\frac{G}{k}=1.67\times10^{-27}\times7.4\times10^{-21}\approx10^{-47}$ C instead of $m_h\sqrt{G/k}\approx10^{-37}$ C.
- **Why:** This question requires balancing Coulomb's law against gravitation for two hydrogen atoms, demonstrated by the stem asking what order $\Delta e$ is 'if the net of electrostatic force and gravitational force between two hydrogen atoms ... is zero'.
<!--/ecat-->

## Q35

Physics · Semiconductor Electronics

The given electrical network is equivalent to

![printed figure: Inputs A and B through a NOR gate, then a NOR gate with both inputs tied together, then a NOT gate to output Y](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q035_ef443b4d_30102026.svg?v=ef443b4dfd00)

*Inputs A and B through a NOR gate, then a NOR gate with both inputs tied together, then a NOT gate to output Y*

![drawn: Inputs A and B through a NOR gate, then a NOR gate with both inputs tied together, then a NOT gate to output Y](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q035_question_9201e2a6_30102026.svg?v=9201e2a66291)  
*drawn on the booklet's geometry, checked against its figure spec*

- **(1)** NOR gate
- (2) NOT gate
- (3) AND gate
- (4) OR gate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $Y = \overline{A + B}$

**Solved independently** (answer withheld)

1. First gate is a NOR: $Y_1 = \overline{A + B}$.
2. Second NOR has both inputs tied to $Y_1$, so it acts as NOT: $Y_2 = \overline{Y_1 + Y_1} = \overline{Y_1} = A + B$.
3. Third gate is a NOT: $Y = \overline{Y_2} = \overline{A + B}$.
4. $Y = \overline{A + B}$ is the NOR function, which is option $1$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q035_aa5090f0_30102026.png?v=aa5090f010b5)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q035_9941455d_30102026.png?v=9941455de524)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A NOR gate with its two inputs tied together acts as a NOT gate, so the two inversions following the first NOR cancel and the network is a NOR
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Missing the bubble on the middle gate turns it into a pass-through, which leaves the final NOT cancelling the first gate's bubble and the output reading as OR — the exact complement of the right gate.
- **Why:** This question requires tracing a three-stage gate network and reducing it, demonstrated by the stem reading 'The given electrical network is equivalent to' while naming no gate — the OR bodies, the output bubbles and the tied inputs of the middle gate exist only in the figure.
- **Note:** The figure spec was supplied and readable: two OR bodies each with an output bubble, the second with its two inputs tied together, then a NOT triangle to Y. So the network could be reduced without the printed image.
<!--/ecat-->

## Q36

Physics · Thermodynamics

A Carnot engine having an efficiency of $\frac{1}{10}$ as heat engine, is used as a refrigerator. If the work done on the system is $10\,\mathrm{J}$, the amount of energy absorbed from the reservoir at lower temperature is

- (1) $99\,\mathrm{J}$
- (2) $100\,\mathrm{J}$
- (3) $1\,\mathrm{J}$
- **(4)** $90\,\mathrm{J}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\beta = \frac{1-\eta}{\eta}$
2. $= \frac{1-\frac{1}{10}}{\frac{1}{10}} = \frac{\frac{9}{10}}{\frac{1}{10}}$
3. $\beta = 9$
4. $\beta = \frac{Q_2}{W}$
5. $Q_2 = 9 \times 10 = 90\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Engine efficiency: $\eta = 1 - \frac{T_2}{T_1} = \frac{1}{10}$, so $\frac{T_2}{T_1} = \frac{9}{10}$.
2. Coefficient of performance of the same Carnot cycle run as a refrigerator: $\beta = \frac{T_2}{T_1 - T_2} = \frac{1-\eta}{\eta}$.
3. $\beta = \frac{9/10}{1/10} = 9$.
4. Heat absorbed from the cold reservoir: $Q_2 = \beta W = 9 \times 10\,\mathrm{J} = 90\,\mathrm{J}$, which is option $4$.

**Subtopic:** Refrigerator and Heat Pump, Carnot Engine · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q036_e174432f_30102026.png?v=e174432fdc73)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q036_5b99bbf4_30102026.png?v=5b99bbf41fb2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Run backwards, a Carnot engine of efficiency $\eta$ has coefficient of performance $\frac{1-\eta}{\eta}$, so the heat drawn from the cold reservoir is $W\left(\frac{1}{\eta}-1\right)$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  100 J is the heat delivered to the HOT reservoir, $\frac{W}{\eta}$, which the same calculation produces; the stem asks for the heat taken in at the lower temperature, which is 100 J less the 10 J of work.
- **Why:** This question requires converting an engine efficiency into a refrigerator's coefficient of performance, demonstrated by the stem reading 'a Carnot engine having an efficiency of 1/10 as heat engine, is used as a refrigerator' and asking for 'the amount of energy absorbed from the reservoir at lower temperature'.
<!--/ecat-->

## Q37

Physics · Electromagnetic Waves

In an electromagnetic wave in free space the root mean square value of the electric field is $E_{rms} = 6\,\mathrm{V/m}$. The peak value of the magnetic field is

- (1) $0.70 \times 10^{-8}\,\mathrm{T}$
- (2) $4.23 \times 10^{-8}\,\mathrm{T}$
- (3) $1.41 \times 10^{-8}\,\mathrm{T}$
- **(4)** $2.83 \times 10^{-8}\,\mathrm{T}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\frac{E_{rms}}{B_{rms}} = c$
2. $B_{rms} = \frac{E_{rms}}{c}$
3. $= \frac{6}{3 \times 10^{8}}$
4. $B_{rms} = 2 \times 10^{-8}$
5. $B_{rms} = \frac{B_0}{\sqrt{2}}$
6. $B_0 = \sqrt{2} \times B_{rms}$
7. $= \sqrt{2} \times 2 \times 10^{-8}$
8. $= 2.83 \times 10^{-8}\,\mathrm{T}$

**Solved independently** (answer withheld)

1. The peak electric field is $E_0 = \sqrt{2}\,E_{rms} = \sqrt{2} \times 6 \approx 8.485\,\mathrm{V/m}$.
2. In free space $B_0 = \frac{E_0}{c}$.
3. $B_0 = \frac{8.485}{3 \times 10^{8}} \approx 2.83 \times 10^{-8}\,\mathrm{T}$, which is option $4$.

**Subtopic:** Relation Between E, B, and Speed of Light · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q037_1fb7bbd1_30102026.png?v=1fb7bbd1ea91)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q037_9a3b0a8b_30102026.png?v=9a3b0a8bf964)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In an electromagnetic wave $B=\frac{E}{c}$ at every instant, and the peak value of a sinusoid is $\sqrt{2}$ times its rms value
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Dividing by $\sqrt{2}$ where it should be multiplied gives $\frac{6}{\sqrt{2}\times3\times10^{8}}=1.41\times10^{-8}$ T, with the $B=\frac{E}{c}$ step itself done correctly.
- **Why:** This question requires an rms-to-peak conversion on top of the field relation, demonstrated by the stem giving '$E_{rms}=6$ V/m' and asking for 'the peak value of the magnetic field'.
<!--/ecat-->

## Q38

Physics · Wave Optics

Two Polaroids $P_1$ and $P_2$ are placed with their axis perpendicular to each other. Unpolarised light $I_0$ is incident on $P_1$. A third polaroid $P_3$ is kept in between $P_1$ and $P_2$ such that its axis makes an angle $45^\circ$ with that of $P_1$. The intensity of transmitted light through $P_2$ is

- **(1)** $\dfrac{I_0}{8}$
- (2) $\dfrac{I_0}{16}$
- (3) $\dfrac{I_0}{2}$
- (4) $\dfrac{I_0}{4}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: Unpolarised light I0 passing through polaroids P1, P3 and P2, with the axes of P3 and P2 at 45 deg and 90 deg to the axis of P1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q038_sol_1_5cde3725_30102026.svg?v=5cde3725b5a7)

*Unpolarised light I0 passing through polaroids P1, P3 and P2, with the axes of P3 and P2 at 45 deg and 90 deg to the axis of P1*

![drawn: Unpolarised light I0 passing through polaroids P1, P3 and P2, with the axes of P3 and P2 at 45 deg and 90 deg to the axis of P1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q038_solution_1_4d8f0287_30102026.svg?v=4d8f02873131)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $I_2 = \frac{I_0}{2}\cos^2 45^\circ$
2. $= \frac{I_0}{2} \times \frac{1}{2}$
3. $= \frac{I_0}{4}$
4. $I_3 = \frac{I_0}{4}\cos^2 45^\circ$
5. $I_3 = \frac{I_0}{8}$

**Solved independently** (answer withheld)

1. Unpolarised light through $P_1$: $I_1 = \frac{I_0}{2}$.
2. $P_3$ makes $45^\circ$ with $P_1$, so by Malus's law $I_3 = I_1 \cos^2 45^\circ = \frac{I_0}{2} \times \frac{1}{2} = \frac{I_0}{4}$.
3. $P_2$ is perpendicular to $P_1$, so it makes $90^\circ - 45^\circ = 45^\circ$ with $P_3$.
4. $I_2 = I_3 \cos^2 45^\circ = \frac{I_0}{4} \times \frac{1}{2} = \frac{I_0}{8}$, which is option $1$.

**Subtopic:** Polaroids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q038_511600c8_30102026.png?v=511600c8181a)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q038_5e29488c_30102026.png?v=5e29488cc8b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Each polaroid applies its own $\cos^2\theta$ to the light that reaches it, and unpolarised light loses half of its intensity at the first sheet
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $\frac{I_0}{4}$ is the intensity leaving $P_3$, which the working produces one stage before the end; the stem asks what gets through $P_2$.
- **Why:** This question requires applying Malus's law twice after the unpolarised halving, demonstrated by the stem placing $P_3$'s axis at 'an angle 45$^\circ$ with that of $P_1$' between two crossed polaroids and asking for the intensity 'through $P_2$'.
<!--/ecat-->

## Q39

Physics · Magnetic Effect of Electric Current

If $\theta_1$ and $\theta_2$ be the apparent angles of dip observed in two vertical planes at right angles to each other, then the true angle of dip $\theta$ is given by

- (1) $\cot^2\theta = \cot^2\theta_1 - \cot^2\theta_2$
- (2) $\tan^2\theta = \tan^2\theta_1 - \tan^2\theta_2$
- **(3)** $\cot^2\theta = \cot^2\theta_1 + \cot^2\theta_2$
- (4) $\tan^2\theta = \tan^2\theta_1 + \tan^2\theta_2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\cot^2\theta = \cot^2\theta_1 + \cot^2\theta_2$

**Solved independently** (answer withheld)

1. True dip satisfies $\tan\theta = \frac{B_V}{B_H}$, so $\cot\theta = \frac{B_H}{B_V}$.
2. In a vertical plane at angle $\alpha$ to the magnetic meridian, the horizontal component is $B_H\cos\alpha$ while $B_V$ is unchanged, so $\tan\theta_1 = \frac{B_V}{B_H\cos\alpha}$, i.e. $\cot\theta_1 = \cot\theta\cos\alpha$.
3. In the perpendicular vertical plane the horizontal component is $B_H\sin\alpha$, so $\tan\theta_2 = \frac{B_V}{B_H\sin\alpha}$, i.e. $\cot\theta_2 = \cot\theta\sin\alpha$.
4. Squaring and adding: $\cot^2\theta_1 + \cot^2\theta_2 = \cot^2\theta(\cos^2\alpha + \sin^2\alpha) = \cot^2\theta$.
5. Hence $\cot^2\theta = \cot^2\theta_1 + \cot^2\theta_2$, which is option $3$.

**Subtopic:** Earth's Magnetism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q039_67e7fa19_30102026.png?v=67e7fa190c44)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q039_9fdae7db_30102026.png?v=9fdae7db8b0c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Apparent dip always exceeds the true dip, and for two vertical planes at right angles the cotangent squares add: $\cot^2\theta=\cot^2\theta_1+\cot^2\theta_2$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Dip is defined by $\tan\theta=B_V/B_H$, so a student holding 'dip is a tangent' writes the additive rule in tangents and reads off $\tan^2\theta=\tan^2\theta_1+\tan^2\theta_2$; it is the horizontal component that splits between the two planes, so the cotangents are what add.
- **Why:** This question requires the composition rule for two perpendicular apparent dips to be reproduced in the right trigonometric function and with the right sign, demonstrated by the four options printing the same relation as either $\cot^2$ or $\tan^2$ with either a plus or a minus.
<!--/ecat-->

## Q40

Physics · Magnetic Effect of Electric Current

A 250-Turn rectangular coil of length $2.1\,\mathrm{cm}$ and width $1.25\,\mathrm{cm}$ carries a current of $85\,\mu\mathrm{A}$ and subjected to a magnetic field of strength $0.85\,\mathrm{T}$. Work done for rotating the coil by $180^\circ$ against the torque is

- (1) $2.3\,\mu\mathrm{J}$
- (2) $1.15\,\mu\mathrm{J}$
- **(3)** $9.1\,\mu\mathrm{J}$
- (4) $4.55\,\mu\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $W = MB(\cos\theta_1 - \cos\theta_2)$
2. When it is rotated by angle $180^\circ$ then
3. $W = 2MB$
4. $W = 2(NIA)B$
5. $= 2 \times 250 \times 85 \times 10^{-6}[1.25 \times 2.1 \times 10^{-4}] \times 85 \times 10^{-2}$
6. $= 9.1\,\mu\mathrm{J}$

**Solved independently** (answer withheld)

1. Area of the coil: $A = 2.1\times10^{-2}\,\mathrm{m} \times 1.25\times10^{-2}\,\mathrm{m} = 2.625\times10^{-4}\,\mathrm{m^2}$.
2. Magnetic moment: $m = NIA = 250 \times 85\times10^{-6} \times 2.625\times10^{-4} = 5.578\times10^{-6}\,\mathrm{A\,m^2}$.
3. Work against the torque from $\theta = 0^\circ$ to $\theta = 180^\circ$: $W = U(180^\circ) - U(0^\circ) = -mB\cos 180^\circ + mB\cos 0^\circ = 2mB$.
4. $W = 2 \times 5.578\times10^{-6} \times 0.85 = 9.48\times10^{-6}\,\mathrm{J} \approx 9.5\,\mu\mathrm{J}$.
5. The nearest option is $9.1\,\mu\mathrm{J}$, which is option $3$.

**Subtopic:** Work Done or Potential Energy of a Current-Carrying Loop in a Uniform Magnetic Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q040_1c5cc78e_30102026.png?v=1c5cc78ec2ad)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q040_995b37a2_30102026.png?v=995b37a27492)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Work done against the magnetic torque is the change in orientation energy $U=-MB\cos\theta$, so a $180^\circ$ turn costs $2MB$ with $M=NIA$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Evaluating $MB=250\times85\,\mu\mathrm{A}\times2.625\times10^{-4}\,\mathrm{m^2}\times0.85\,\mathrm{T}$ and stopping there delivers half the work, because the coil starts at $-MB$ and ends at $+MB$, a gap of $2MB$; the printed $4.55\,\mu\mathrm{J}$ is exactly the key halved.
- **Why:** This question requires the orientation-energy difference for a half turn to be computed as $W=2NIAB$ from the stem's own numbers, demonstrated by the stem asking for 'Work done for rotating the coil by $180^\circ$ against the torque'.
- **Note:** Substituting the printed numbers into $2NIAB$ gives $9.48\,\mu\mathrm{J}$ while the key prints $9.1\,\mu\mathrm{J}$; $9.1$ is the nearest option and the tag follows the printed key. The four options are that key successively halved ($9.1$, $4.55$, $2.3$, $1.15$), which is why every route here turns on the factor of 2.
<!--/ecat-->

## Q41

Physics · Current Electricity

The resistance of a wire is '$R$' ohm. If it is melted and stretched to '$n$' times its original length, its new resistance will be

- **(1)** $n^2R$
- (2) $\dfrac{R}{n^2}$
- (3) $nR$
- (4) $\dfrac{R}{n}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\frac{R_2}{R_1} = \frac{l_2^2}{l_1^2}$
2. $= \frac{n^2 l_1^2}{l_1^2}$
3. $\frac{R_2}{R_1} = n^2$
4. $R_2 = n^2 R_1$

**Solved independently** (answer withheld)

1. Melting and stretching keeps the volume constant: $lA = (nl)A'$, so $A' = \frac{A}{n}$.
2. $R' = \frac{\rho (nl)}{A/n} = n^2 \frac{\rho l}{A}$.
3. Since $R = \frac{\rho l}{A}$, $R' = n^2 R$, which is option $1$.

**Subtopic:** Resistance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q041_96a4c460_30102026.png?v=96a4c460c930)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q041_f5b6be2c_30102026.png?v=f5b6be2c619a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Melting and redrawing a wire keeps its volume, so stretching the length $n$ times thins the cross-section $n$ times and $R=\rho L/A$ rises by $n^2$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Reading only 'stretched to $n$ times its original length' and feeding it into $R=\rho L/A$ gives $nR$; the stem's word 'melted' fixes the volume, so the area drops to $A/n$ at the same time and the two factors multiply to $n^2$.
- **Why:** This question requires the factor by which resistance changes when a volume-conserving wire is lengthened $n$ times, demonstrated by the options all being $R$ carrying $n^{\pm1}$ or $n^{\pm2}$ and by the stem's word 'melted'.
<!--/ecat-->

## Q42

Physics · Units and Measurements

A physical quantity of the dimensions of length that can be formed out of $c$, $G$ and $\frac{e^2}{4\pi\varepsilon_0}$ is [$c$ is velocity of light, $G$ is universal constant of gravitation and $e$ is charge]

- (1) $\frac{1}{c^2}\left[\frac{e^2}{G4\pi\varepsilon_0}\right]^{\frac{1}{2}}$
- (2) $\frac{1}{c}G\frac{e^2}{4\pi\varepsilon_0}$
- **(3)** $\frac{1}{c^2}\left[G\frac{e^2}{4\pi\varepsilon_0}\right]^{\frac{1}{2}}$
- (4) $c^2\left[G\frac{e^2}{4\pi\varepsilon_0}\right]^{\frac{1}{2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Let $\frac{e^{2}}{4\pi\varepsilon_0} = A = \mathrm{ML^{3}T^{-2}}$
2. $l = C^{x}G^{y}(A)^{z}$
3. $L = [\mathrm{LT^{-1}}]^{x}\,[\mathrm{M^{-1}L^{3}T^{-2}}]^{y}\,[\mathrm{ML^{3}T^{-2}}]^{z}$
4. $-y + z = 0 \Rightarrow y = z$ ...(i)
5. $x + 3y + 3z = 1$ ...(ii)
6. $-x - 4z = 0$ ...(iii)
7. From (i), (ii) & (iii)
8. $z = y = \frac{1}{2}$, $x = -2$

**Solved independently** (answer withheld)

1. $[G] = M^{-1} L^{3} T^{-2}$ since $F = \frac{G m_1 m_2}{r^2}$.
2. $\left[\frac{e^2}{4\pi\varepsilon_0}\right] = [F r^2] = M L T^{-2} \cdot L^2 = M L^{3} T^{-2}$.
3. $\left[G \frac{e^2}{4\pi\varepsilon_0}\right] = M^{-1} L^{3} T^{-2} \cdot M L^{3} T^{-2} = L^{6} T^{-4}$.
4. $\left[G \frac{e^2}{4\pi\varepsilon_0}\right]^{1/2} = L^{3} T^{-2}$.
5. $[c^2] = L^{2} T^{-2}$.
6. $\frac{1}{c^2}\left[G \frac{e^2}{4\pi\varepsilon_0}\right]^{1/2} = \frac{L^{3} T^{-2}}{L^{2} T^{-2}} = L$, which is option $3$.

**Subtopic:** Deducing Relation Among the Physical Quantities Using Dimensional Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q042_a76d451c_30102026.png?v=a76d451c5b44)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q042_155448a4_30102026.png?v=155448a497b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Building a length by matching powers of M, L and T: $G\,e^2/4\pi\varepsilon_0$ has dimensions $L^6T^{-4}$, so its square root divided by $c^2$ is a length
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The bracket's square root works out to $L^3T^{-2}$, and reaching a length needs $c$ to the power $-2$; writing $c^2$ in front instead of $1/c^2$ flips one exponent and lands on option 4.
- **Why:** This question requires powers of M, L and T to be matched until a length is assembled from three given constants, demonstrated by the stem asking for 'A physical quantity of the dimensions of length that can be formed out of $c$, $G$ and $\frac{e^2}{4\pi\varepsilon_0}$'.
<!--/ecat-->

## Q43

Physics · Modern Physics

> ⚠ The printed solution says "No option is correct": the question has no correct option as printed, and the printed answer comes from a corrected reading.

Radioactive material 'A' has decay constant '$8\lambda$' and material 'B' has decay constant '$\lambda$'. Initially they have same number of nuclei. After what time, the ratio of number of nuclei of material 'B' to that 'A' will be $\frac{1}{e}$?

- (1) $\frac{1}{8\lambda}$
- (2) $\frac{1}{9\lambda}$
- (3) $\frac{1}{\lambda}$
- **(4)** $\frac{1}{7\lambda}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. No option is correct
2. If we take $\frac{N_A}{N_B} = \frac{1}{e}$
3. Then $\frac{N_A}{N_B} = \frac{e^{-8\lambda t}}{e^{-\lambda t}}$
4. $\frac{1}{e} = e^{-7\lambda t}$
5. $-1 = -7\lambda t$
6. $t = \frac{1}{7\lambda}$

**Solved independently** (answer withheld)

1. Decay law: $N_A = N_0 e^{-8\lambda t}$ and $N_B = N_0 e^{-\lambda t}$, with the same $N_0$ for both.
2. Ratio as worded: $\frac{N_B}{N_A} = e^{7\lambda t}$, which is $\ge 1$ for all $t \ge 0$. Setting it to $\frac{1}{e}$ needs $t = -\frac{1}{7\lambda}$, which is not physical.
3. So the intended ratio must be $\frac{N_A}{N_B} = e^{-7\lambda t}$.
4. Set $e^{-7\lambda t} = e^{-1}$, so $7\lambda t = 1$.
5. $t = \frac{1}{7\lambda}$, which is option $4$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q043_12a58e64_30102026.png?v=12a58e64793d)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q043_fcac5a8e_30102026.png?v=fcac5a8e4372)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Each material survives as $e^{-\lambda t}$, so the ratio of the two populations carries the difference of the decay constants, $8\lambda-\lambda=7\lambda$, and $e^{-7\lambda t}=1/e$ at $t=1/7\lambda$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Combining the two survival factors by multiplying, $e^{-8\lambda t}\cdot e^{-\lambda t}=e^{-9\lambda t}$, turns the ratio into a product and gives $t=1/9\lambda$; dividing subtracts the exponents and leaves $7\lambda$.
- **Why:** This question requires a ratio of two exponential decays to be reduced to one exponential and solved for the time, demonstrated by the stem giving decay constants '$8\lambda$' and '$\lambda$' with the target ratio '$\frac{1}{e}$'.
- **Note:** As printed the stem asks for the ratio of B to A, which is $e^{+7\lambda t}$ and never equals $1/e$ for positive $t$; the key's $1/7\lambda$ follows from the ratio of A to B. The question is tagged as printed and the routes are read against the key's direction.
<!--/ecat-->

## Q44

Physics · Current Electricity

A potentiometer is an accurate and versatile device to make electrical measurements of E.M.F, because the method involves :

- **(1)** A condition of no current flow through the galvanometer
- (2) A combination of cells, galvanometer and resistances
- (3) Cells
- (4) Potential gradients

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Reading of potentiometer is accurate because during taking reading it does not draw any current from the circuit.

**Solved independently** (answer withheld)

1. At the balance length $l$ the galvanometer shows zero deflection, so $I_g = 0$ and no current is drawn from the test cell; this null condition is what makes the method accurate, so the answer is option $1$.

**Subtopic:** Potentiometer · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q044_6d2128e8_30102026.png?v=6d2128e8d39e)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q044_ee0032ff_30102026.png?v=ee0032ff9e77)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The potentiometer measures EMF by a null method: at balance no current is drawn from the cell, so no potential is lost across its internal resistance and the EMF itself is read
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The potentiometer's working principle is the uniform potential gradient along its wire, so this option answers 'what does the instrument work on' rather than the stem's 'because' — the gradient explains how a length becomes a potential difference, not why the reading is the EMF rather than the terminal voltage.
- **Why:** This question requires the reason the textbook gives for the potentiometer's accuracy, demonstrated by the stem ending 'because the method involves :' and by the key reading 'A condition of no current flow through the galvanometer'.
<!--/ecat-->

## Q45

Physics · Ray Optics

The ratio of resolving powers of an optical microscope for two wavelengths $\lambda_1 = 4000\,\text{\AA}$ and $\lambda_2 = 6000\,\text{\AA}$ is

- **(1)** $3 : 2$
- (2) $16 : 81$
- (3) $8 : 27$
- (4) $9 : 4$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Resolving power $\propto \frac{1}{\lambda}$
2. $\frac{R_1}{R_2} = \frac{\lambda_2}{\lambda_1}$
3. $= \frac{6000\,\text{\AA}}{4000\,\text{\AA}}$
4. $= \frac{3}{2}$

**Solved independently** (answer withheld)

1. The resolving power of a microscope is $RP = \frac{2\mu \sin\theta}{1.22\lambda}$, so $RP \propto \frac{1}{\lambda}$.
2. $\frac{RP_1}{RP_2} = \frac{\lambda_2}{\lambda_1}$.
3. $\frac{RP_1}{RP_2} = \frac{6000\,\text{\AA}}{4000\,\text{\AA}} = \frac{3}{2}$, i.e. $3 : 2$, which is option $1$.

**Subtopic:** Resolving and Magnifying Power of Microscope · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 12)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q045_d6e39cf0_30102026.png?v=d6e39cf0486b)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q045_8ad30d47_30102026.png?v=8ad30d47fd64)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Resolving power of a microscope is $2\mu\sin\theta/1.22\lambda$, so it goes as $1/\lambda$ and the ratio of resolving powers is the inverse ratio of the wavelengths
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Getting the sense right -- the $4000\,\text{\AA}$ light resolves better -- and then squaring the inverse ratio gives $(3/2)^2=9:4$; resolving power carries $\lambda$ to the first power, so the ratio stays $3:2$.
- **Why:** This question requires the factor by which resolving power changes when the wavelength changes, demonstrated by the stem asking for 'The ratio of resolving powers of an optical microscope for two wavelengths' and by the options being bare ratios of that one quantity.
<!--/ecat-->

## Q46

Biology · zoology · Principles of Inheritance and Variation

A disease caused by an autosomal primary non-disjunction is

- (1) Turner's syndrome
- (2) Sickle cell anemia
- **(3)** Down's syndrome
- (4) Klinefelter's syndrome

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Down’s syndrome is caused by non-disjunction of $21^{\mathrm{st}}$ chromosome.

**Solved independently** (answer withheld)

1. Autosomal non-disjunction gives an extra or missing autosome: Down's syndrome is trisomy $21$ ($2n+1 = 47$, $+21$), while Turner's ($45, XO$) and Klinefelter's ($47, XXY$) are sex chromosome aneuploidies and sickle cell anemia is a point mutation ($GAG \rightarrow GUG$), so the answer is option $3$.

**Subtopic:** Chromosomal Disorders · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q046_3e8c2cb9_30102026.png?v=3e8c2cb9cb23)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q046_3b5ec7a1_30102026.png?v=3b5ec7a18088)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Down's syndrome is trisomy of chromosome 21, an autosome; Turner's and Klinefelter's come from non-disjunction of the sex chromosomes, and sickle-cell anaemia is a point mutation, not a chromosome count
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Klinefelter's is the other extra-chromosome syndrome the chapter builds out of primary non-disjunction, so a student who reads "non-disjunction" and stops takes it; the extra chromosome there is an X, and the stem said autosomal
- **Why:** This question requires the fact that the trisomy NCERT assigns to an autosome is of chromosome 21, demonstrated by the stem's two qualifiers "autosomal" and "primary non-disjunction" each being satisfied by a different wrong option.
<!--/ecat-->

## Q47

Biology · botany · Sexual Reproduction in Flowering Plants

A dioecious flowering plant prevents both:

- (1) Geitonogamy and xenogamy
- (2) Cleistogamy and xenogamy
- (3) Autogamy and xenogamy
- **(4)** Autogamy and geitonogamy

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. When unisexual male and female flowers are present on different plants the condition is called dioecious and it prevents both autogamy and geitonogamy.

**Solved independently** (answer withheld)

1. A dioecious plant bears male and female flowers on separate plants, so every flower is unisexual and each plant has only one sex; this prevents autogamy (same flower) and geitonogamy (different flower of the same plant), leaving only xenogamy, which is option $4$.

**Subtopic:** Outbreeding Devices · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q047_4360d106_30102026.png?v=4360d106c358)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q047_ffaeb40a_30102026.png?v=ffaeb40a2a67)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Autogamy is pollination within one flower, geitonogamy between two flowers of the same plant, xenogamy between two plants — so a plant carrying only one sex loses the first two and is left with the third
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Option 3 opens with autogamy, which is certainly blocked, and a student who holds NCERT's remark that geitonogamy is functionally cross-pollination concludes a dioecious plant can still do it and puts xenogamy in the second slot
- **Why:** This question requires the definitions of autogamy, geitonogamy and xenogamy to be tested against a stated condition, demonstrated by the stem supplying only "a dioecious flowering plant" and each option naming two modes that must both be excluded by it.
- **Note:** On a strict reading option 2's first term is also excluded by dioecy, since a cleistogamous flower must be bisexual; the option still fails on xenogamy, so the printed key stands.
<!--/ecat-->

## Q48

Biology · botany · Sexual Reproduction in Flowering Plants

Attractants and rewards are required for

- (1) Hydrophily
- (2) Cleistogamy
- (3) Anemophily
- **(4)** Entomophily

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Insect pollinated plants provide rewards as edible pollen grain and nectar as usual rewards.
2. While some plants also provide safe place for deposition of eggs.

**Solved independently** (answer withheld)

1. Attractants (bright colour, fragrance) and rewards (nectar, pollen) are needed only where an animal agent must be drawn to the flower, i.e. in biotic pollination; hydrophily and anemophily are abiotic, and cleistogamous flowers never open, so the answer is entomophily, option $4$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q048_f728df8b_30102026.png?v=f728df8bb052)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q048_e45a9ced_30102026.png?v=e45a9ced382c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nectar, scent and colour are advertisements paid to an animal pollinator, so they belong to insect pollination; wind- and water-pollinated flowers are small, dull and offer no reward
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  A student who knows rewards are paid to a living pollinator but holds the -phily names as one cluster of similar words picks the -phily term they have drilled most often against entomophily, and anemo- is wind, which pays nothing
- **Why:** This question requires the stated fact that nectar and scent belong to animal-pollinated flowers, demonstrated by the stem offering only "Attractants and rewards" and the options naming four pollination modes with no criterion printed to apply.
<!--/ecat-->

## Q49

Biology · botany · Biodiversity and Conservation

Alexander Von Humboldt described for the first time

- **(1)** Species area relationships
- (2) Population Growth equation
- (3) Ecological Biodiversity
- (4) Laws of limiting factor

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Alexander Von Humboldt observed that within a region species richness increases with the increases in area.

**Solved independently** (answer withheld)

1. Alexander von Humboldt, exploring South American jungles, observed that within a region species richness increases with explored area up to a limit, described as $\log S = \log C + Z \log A$, the species-area relationship, which is option $1$.

**Subtopic:** Species–Area Relationships · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q049_cda235a5_30102026.png?v=cda235a54987)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q049_1589eb1d_30102026.png?v=1589eb1d8c02)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Species richness rises with the area explored, up to a limit — the relationship Alexander von Humboldt was the first to describe
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The Biodiversity chapter carries two attributions a few paragraphs apart — Humboldt for the species-area relationship and Edward Wilson for popularising the term biodiversity — so a student who remembers that the chapter credits someone with biodiversity attaches it to the name in the stem
- **Why:** This question requires one stated attribution, demonstrated by the stem naming "Alexander Von Humboldt" and the four options naming four separate findings, none of which can be derived from the other three.
<!--/ecat-->

## Q50

Biology · both · Cell: The Unit of Life

Which of the following cell organelles is responsible for extracting energy from carbohydrates to form ATP?

- (1) Chloroplast
- **(2)** Mitochondrion
- (3) Lysosome
- (4) Ribosome

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Mitochondria are the site of aerobic oxidation of carbohydrates to generate ATP.

**Solved independently** (answer withheld)

1. The mitochondrion is the site of aerobic respiration, where carbohydrate-derived substrates are oxidised and the released energy forms ATP, so the answer is option $2$ (Mitochondrion).

**Subtopic:** Mitochondria · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q050_a8565c7a_30102026.png?v=a8565c7a2695)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q050_46a28f3a_30102026.png?v=46a28f3ad753)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The mitochondrion oxidises carbohydrate to release energy as ATP; the chloroplast runs the same link the other way, storing energy in carbohydrate
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The chloroplast does form ATP, so the second half of the stem is satisfied, and a student who holds "chloroplast is the energy organelle" takes it without noticing that the carbohydrate there is the product, not the fuel
- **Why:** This question requires the stated function of one named organelle, demonstrated by the stem printing the direction of the link — "extracting energy from carbohydrates to form ATP" — against four organelles each with one taught job.
<!--/ecat-->

## Q51

Biology · botany · Plant Kingdom

Zygotic meiosis is characterstic of

- (1) Funaria
- **(2)** Chlamydomonas
- (3) Marchantia
- (4) Fucus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Chlamydomonas has haplontic life cycle hence showing zygotic meiosis or initial meiosis.

**Solved independently** (answer withheld)

1. Zygotic meiosis means the diploid zygote divides by meiosis, which happens in a haplontic life cycle; among the options only Chlamydomonas is haplontic (Funaria and Marchantia are haplo-diplontic, Fucus is diplontic), so the answer is option $2$.

**Subtopic:** Plant Life Cycles and Alternation of Generations · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q051_807eeee8_30102026.png?v=807eeee89571)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q051_4359816a_30102026.png?v=4359816af1ce)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a haplontic life cycle the zygote is the only diploid cell and it divides by meiosis at once, which is the pattern NCERT prints for Chlamydomonas
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Chlamydomonas and Fucus are the two algae printed in the same life-cycle account, one row apart, so a student who remembers that an alga is the example here but not which column it sits in takes Fucus, whose meiosis is gametic and not zygotic
- **Why:** This question requires the life-cycle pattern NCERT states for a named genus, demonstrated by the stem supplying only "Zygotic meiosis" and the options naming four genera drawn from the same life-cycle account.
- **Note:** The pattern classifier returned plain_mcq, which matches the printed shape.
<!--/ecat-->

## Q52

Biology · zoology · Neural Control and Coordination

Good vision depends on adequate intake of carotene rich food
Select the best option from the following statements

- **(a)** Vitamin A derivatives are formed from carotene
- **(b)** The photopigments are embedded in the membrane discs of the inner segment
- **(c)** Retinal is a derivative of vitamin A
- **(d)** Retinal is a light absorbing part of all the visual photopigments

- (1) (a) and (c)
- (2) (b), (c) and (d)
- (3) (a) and (b)
- **(4)** (a), (c) and (d)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Carotene is the source of retinal which is involved in formation of rhodopsin of rod cells.
2. Retinal, a derivative of vitamin A, is the light-absorbing part of all visual photopigments.

**Solved independently** (answer withheld)

1. Statement (a): carotene is the precursor of vitamin A, so vitamin A derivatives are formed from carotene; (a) is true.
2. Statement (b): the photopigments of rods and cones lie in the membrane discs of the outer segment, not the inner segment; (b) is false.
3. Statement (c): retinal is an aldehyde derivative of vitamin A; (c) is true.
4. Statement (d): retinal is the light-absorbing part of all visual photopigments (rhodopsin and the cone opsins); (d) is true.
5. True set $= \{a, c, d\}$, which matches option $4$: (a), (c) and (d).

**Subtopic:** Sense Organs: The Eye · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q052_f4405b51_30102026.png?v=f4405b517dc3)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q052_ad7bf78e_30102026.png?v=ad7bf78e4eee)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Carotene gives vitamin A, vitamin A gives retinal, and retinal is the light-absorbing part of every visual photopigment, which sits in the membrane discs of the rod's outer segment
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Statements (a) and (c) are the two the stem's own sentence about carotene vouches for, so the set is checked and closed, and (d) is let go because 'all the visual photopigments' reads as an overstatement; retinal really is the light-absorbing part of every visual photopigment, so the chosen set is true but short.
- **Why:** This question requires each printed statement to be judged true or false, demonstrated by (b) 'The photopigments are embedded in the membrane discs of the inner segment' being excluded for naming the wrong segment rather than for being irrelevant.
<!--/ecat-->

## Q53

Biology · botany · Principles of Inheritance and Variation

Among the following characters, which one was not considered by Mendel in his experiments on pea?

- (1) Seed – Green or Yellow
- (2) Pod – Inflated or Constricted
- (3) Stem – Tall or Dwarf
- **(4)** Trichomes – Glandular or non-glandular

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. During his experiments Mendel studied seven characters.
2. Nature of trichomes i.e., glandular or non-glandular was not considered by Mendel.

**Solved independently** (answer withheld)

1. Mendel studied seven pairs of contrasting traits in pea: seed shape, seed colour, flower colour, pod shape, pod colour, flower position and stem height; seed colour (option $1$), pod shape (option $2$) and stem height (option $3$) are among them, but trichome type is not, so the answer is option $4$.

**Subtopic:** Contrasting Traits Studied by Mendel in Pea · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q053_be067534_30102026.png?v=be067534bd79)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q053_9c405428_30102026.png?v=9c405428bc47)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mendel's seven contrasting characters in pea are a fixed printed list - stem height, flower colour, flower position, pod shape, pod colour, seed shape, seed colour - and trichome type is not one of them
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Reading the stem as 'which one WAS considered' puts the answer on the pair the whole monohybrid cross is worked with, tall against dwarf. The printed 'not' makes a character you can confirm one to strike out, not one to mark.
- **Why:** This question requires the printed list of seven contrasting characters in pea, demonstrated by 'Trichomes - Glandular or non-glandular' being the one option whose character is absent from that list.
- **Note:** type_patterns called this statement_options; each printed option is a character with its two contrasting forms, not a statement to be judged, so the shape recorded is mcq. The three wrong options all carry the authentic form pairs, so the question turns on the character names alone.
<!--/ecat-->

## Q54

Biology · both · Molecular Basis of Inheritance

The association of histone H1 with a nucleosome indicates:

- **(1)** The DNA is condensed into a Chromatin Fibre
- (2) The DNA double helix is exposed
- (3) Transcription is occurring
- (4) DNA replication is occurring

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The association of H1 protein indicates the complete formation of nucleosome.
2. Therefore the DNA is in condensed form.

**Solved independently** (answer withheld)

1. Histone $H1$ is the linker histone: it binds the linker DNA at the entry and exit of each nucleosome and packs the beads-on-string into a condensed chromatin fibre (about $30\,\text{nm}$), so the DNA is condensed, which is option $1$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q054_eece1567_30102026.png?v=eece1567f193)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q054_a8f4cbaf_30102026.png?v=a8f4cbaf60e5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Histone H1 binds the DNA where it enters and leaves the nucleosome, and that binding is what packs the beads-on-a-string into the chromatin fibre
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  In the beads-on-a-string picture the DNA is wound round the outside of each bead and lies bare between beads, so one more histone reads as sitting on the outside and leaving the helix open. H1 does the opposite: it ties the entering and leaving turns together, which is the step that folds the string into a condensed fibre.
- **Why:** This question requires what histone H1's association with a nucleosome says about the packing state of the DNA, demonstrated by 'The DNA is condensed into a Chromatin Fibre' standing against 'The DNA double helix is exposed'.
<!--/ecat-->

## Q55

Biology · zoology · Locomotion and Movement

The pivot joint between atlas and axis is a type of

- **(1)** Synovial joint
- (2) Saddle joint
- (3) Fibrous joint
- (4) Cartilaginous joint

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Synovial joints are freely movable joint which allow considerable movements.
2. Pivot joint is a type of synovial joint which provide rotational movement as in between atlas and axis vertebrae of vertebral column.

**Solved independently** (answer withheld)

1. Synovial joints have a fluid-filled synovial cavity between the articulating bones and are classed as ball and socket, hinge, pivot, gliding and saddle joints; the pivot joint between atlas and axis is therefore a synovial joint, which is option $1$.

**Subtopic:** Joints · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q055_eba2974d_30102026.png?v=eba2974d7705)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q055_484a0ddb_30102026.png?v=484a0ddb3d94)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The pivot joint between atlas and axis is listed among the synovial joints, which have a fluid-filled cavity between the articulating surfaces; the cartilaginous class is the one given for joints between adjacent vertebrae
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The joint between adjacent vertebrae is printed as the cartilaginous pattern, and the atlas sits on the axis, so the rule is carried straight across. The stem's own words 'pivot joint' are what overrule it, because the pivot joint between atlas and axis is printed in the synovial list.
- **Why:** This question requires the joint class the named joint belongs to, demonstrated by the stem printing 'The pivot joint between atlas and axis', which is the example listed under synovial joints. Delete the words 'pivot joint' from the stem and option 4 becomes defensible on the adjacent-vertebrae line, which is what condition_missed records.
<!--/ecat-->

## Q56

Biology · zoology · Neural Control and Coordination

Receptor sites for neurotransmitters are present on

- (1) Tips of axons
- **(2)** Post-synaptic membrane
- (3) Membranes of synaptic vesicles
- (4) Pre-synaptic membrane

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Pre-synaptic membrane is involved in the release of neurotransmitter in the chemical synapse.
2. The receptors sites for neurotransmitters are present on post-synaptic membrane.

**Solved independently** (answer withheld)

1. Neurotransmitters released into the synaptic cleft bind to specific receptors present on the $\text{post-synaptic membrane}$, which is option $2$.

**Subtopic:** Transmission of Impulses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q056_ee5a8611_30102026.png?v=ee5a8611c825)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q056_4732eab1_30102026.png?v=4732eab14a3d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The neurotransmitter is released at the axon terminal of the pre-synaptic neuron and binds specific receptors on the post-synaptic membrane across the cleft
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Pre-synaptic and post-synaptic differ by a prefix, so a student carrying 'the receptors are on the synaptic membrane' takes the face the account dwells on, the one the transmitter leaves. The receptors are on the membrane the transmitter crosses the cleft to reach.
- **Why:** This question requires where the receptor sites for neurotransmitters lie, demonstrated by the options offering both faces of the cleft, 'Post-synaptic membrane' against 'Pre-synaptic membrane'. Swap test applied: replace 'Pre-synaptic membrane' with an unlike term and the pull dies, so the likeness of the two names is doing the work, not printed position - look_alike_term.
<!--/ecat-->

## Q57

Biology · zoology · Human Reproduction

GnRH, a hypothalamic hormone, needed in reproduction, acts on

- (1) Posterior pituitary gland and stimulates secretion of oxytocin and FSH
- (2) Posterior pituitary gland and stimulates secretion of LH and relaxin
- (3) Anterior pituitary gland and stimulates secretion of LH and oxytocin
- **(4)** Anterior pituitary gland and stimulates secretion of LH and FSH

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Hypothalamus secretes GnRH which stimulates anterior pituitary gland for the secretion of gonadotropins (FSH and LH).

**Solved independently** (answer withheld)

1. GnRH (gonadotropin releasing hormone) from the hypothalamus acts on the $\text{anterior pituitary}$, not the posterior pituitary, so options $1$ and $2$ are out.
2. It stimulates release of the gonadotropins $\text{LH}$ and $\text{FSH}$; oxytocin is released from the posterior pituitary, so option $3$ is out, leaving option $4$.

**Subtopic:** Hormonal Regulation of Reproduction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q057_751c9e6a_30102026.png?v=751c9e6a5a73)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q057_1e8a6390_30102026.png?v=1e8a63901647)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** GnRH from the hypothalamus acts on the anterior pituitary and brings out the two gonadotropins, LH and FSH
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  With the lobe right and LH right, a second hormone still has to be supplied, and oxytocin is the hormone filed under reproduction. Oxytocin is not a gonadotropin and is not under GnRH's control; the pair brought out is LH with FSH.
- **Why:** This question requires both the lobe GnRH acts on and the two hormones it brings out, demonstrated by 'Anterior pituitary gland and stimulates secretion of LH and FSH' being graded whole against options that alter one half.
- **Note:** type_patterns called this statement_options; each option bundles a lobe with a hormone pair that must both hold, so the shape recorded is two_part - and that is why this is the one question in the group whose trap is half_right.
<!--/ecat-->

## Q58

Biology · zoology · Chemical Coordination and Integration

Hypersecretion of Growth Hormone in adults does not cause further increase in height, because

- (1) Bones loose their sensitivity to Growth Hormone in adults
- (2) Muscle fibres do not grow in size after birth
- (3) Growth Hormone becomes inactive in adults
- **(4)** Epiphyseal plates close after adolescence

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Epiphyseal plate is responsible for the growth of bone which close after adolescence so hypersecretion of growth hormone in adults does not cause further increase in height.

**Solved independently** (answer withheld)

1. Height increase comes from bones growing longer at the epiphyseal (growth) plates; these plates close (ossify) after adolescence, so adult GH hypersecretion cannot raise height and leads to acromegaly instead, which is option $4$.

**Subtopic:** The Pituitary Gland · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q058_ef811398_30102026.png?v=ef811398c8eb)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q058_c057dca3_30102026.png?v=c057dca3f0a2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Length is added to a long bone at its epiphyseal plates, and once those cartilage plates close after adolescence excess growth hormone can only thicken bone, which is acromegaly
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  A hormone works through its receptor, so a student explaining an absent effect puts the block at the receptor and reads adult bone as having stopped listening. The block is at the growth plate, not at the receptor: adult bone still answers growth hormone, which is why the excess disfigures the face and hands.
- **Why:** This question requires the reason height stops answering growth hormone in the adult, demonstrated by the stem's trailing 'because' and by option 4 'Epiphyseal plates close after adolescence'.
- **Note:** type_patterns called this statement_options; the options are rival explanations completing the stem's 'because', not statements put up to be judged, and long sentences as options do not make the shape statements, so mcq is recorded.
<!--/ecat-->

## Q59

Biology · botany · Mineral Nutrition

Select the mismatch :

- (1) Anabaena – Nitrogen fixer
- (2) Rhizobium – Alfalfa
- (3) Frankia – Alnus
- **(4)** Rhodospirillum – Mycorrhiza

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Rhodospirillum is anaerobic, free living nitrogen fixer.
2. Mycorrhiza is a symbiotic relationship between fungi and roots of higher plants.

**Solved independently** (answer withheld)

1. $\textit{Anabaena}$ is a cyanobacterium that fixes nitrogen, so option $1$ is a correct pair.
2. $\textit{Rhizobium}$ forms symbiotic root nodules on legumes such as alfalfa, so option $2$ is a correct pair.
3. $\textit{Frankia}$ forms nitrogen-fixing root nodules on the non-legume $\textit{Alnus}$, so option $3$ is a correct pair.
4. $\textit{Rhodospirillum}$ is a free-living anaerobic nitrogen-fixing bacterium, while mycorrhiza is a fungus-root association, so option $4$ is the mismatch.

**Subtopic:** Nitrogen Fixation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q059_1e345b25_30102026.png?v=1e345b25c539)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q059_4944f4f5_30102026.png?v=4944f4f53e6a)

---

<!--ecat-->
#### Categories

- **Type:** **New type (proposed)** (`new_type`) — a printed shape none of the above describes
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Which microbe fixes nitrogen with which partner, and which nitrogen fixers are free-living instead of living in a root association
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Frankia and Rhizobium are the two symbiotic nitrogen fixers printed in the same list, and a student who filed them under one line — bacteria in the root nodules of legumes — reads Alnus, a tree that is no legume, as the pair the paper altered.
- **Why:** This question requires the microbe-to-partner pairings the text prints for nitrogen fixation, demonstrated by three options being its own pairs and the stem asking only for the 'mismatch'.
- **Note:** E1_question_type reads plain_mcq, but every option is printed as a pair judged whole; the live qtype vocabulary has no value for that shape, so new_type carries it with a proposal.
<!--/ecat-->

## Q60

Biology · botany · Environmental Issues

Which one of the following statements is not valid for aerosols?

- **(1)** They cause increased agricultural productivity
- (2) They have negative impact on agricultural land
- (3) They are harmful to human health
- (4) They alter rainfall and monsoon patterns

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Aerosols can cause various problems to agriculture through its direct or indirect effects on plants.
2. However continually increasing air pollution may represent a persistent and largely irreversible threat to agriculture in the future.

**Solved independently** (answer withheld)

1. Aerosols are suspended particulate pollutants that are harmful to human health (respiratory problems), so option $3$ is valid; they scatter and absorb sunlight and act as cloud condensation nuclei, altering rainfall and monsoon patterns, so option $4$ is valid; their deposition and reduced sunlight harm agricultural land and crops, so option $2$ is valid; hence the statement that they increase agricultural productivity is not valid, which is option $1$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q060_8aa48d5e_30102026.png?v=8aa48d5ef0f3)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q060_364c6ac1_30102026.png?v=364c6ac1f6f7)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Aerosols thrown into the atmosphere damage crops, human health and rainfall patterns; nothing in their account credits them with raising yields
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Option 2 is the aerosol effect the book states in its own sentence, so a student carrying the stem as 'which statement is valid' finds the remembered line and stops before the word 'not'.
- **Why:** This question requires the printed effects of aerosols, demonstrated by three options restating them and the stem asking which one is 'not valid'.
<!--/ecat-->

## Q61

Biology · botany · Biodiversity and Conservation

Which one of the following is related to Ex-situ conservation of threatened animals and plants?

- (1) Amazon rainforest
- (2) Himalayan region
- **(3)** Wildlife Safari parks
- (4) Biodiversity hot spots

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ex-situ conservation is offsite strategy for conservation of animals and plants in zoological park and botanical gardens respectively.

**Solved independently** (answer withheld)

1. Ex-situ conservation protects threatened plants and animals outside their natural habitat, in places such as zoological parks, botanical gardens and wildlife safari parks; Amazon rainforest, Himalayan region and biodiversity hot spots are natural habitats or in-situ concepts, so the answer is option $3$.

**Subtopic:** Ex Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q061_4254e62a_30102026.png?v=4254e62ae8c9)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q061_0797199f_30102026.png?v=0797199f6dbb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex situ conservation keeps threatened species away from their habitat — zoos, botanical gardens, safari parks — while hot spots and wild regions are in situ
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Biodiversity hot spots is the conservation term printed in the paragraph just before the ex situ one, so a student who filed both paragraphs under one heading picks the term they recognise as a strategy.
- **Why:** This question requires the printed example list of ex situ conservation, demonstrated by the option 'Wildlife Safari parks' standing against three named wild regions.
<!--/ecat-->

## Q62

Biology · botany · Transport in Plants

Which of the following facilitates opening of stomatal aperture?

- **(1)** Radial orientation of cellulose microfibrils in the cell wall of guard cells
- (2) Longitudinal orientation of cellulose microfibrils in the cell wall of guard cells
- (3) Contraction of outer wall of guard cells
- (4) Decrease in turgidity of guard cells

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cellulose microfibrils are oriented radially rather than longitudinally which makes easy for the stoma to open.

**Solved independently** (answer withheld)

1. Guard cells open the stoma when they become turgid, and the radial orientation of cellulose microfibrils in their walls makes the outer walls bow outward and pull the inner walls into a crescent, so the pore opens: option $1$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q062_7e59315e_30102026.png?v=7e59315ec3e1)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q062_49de1442_30102026.png?v=49de1442ba68)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Stomata open because the guard-cell wall is built to deform outwards: radial cellulose microfibrils and a thick inner wall turn incoming water into a wider pore
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who kept the sentence's contrast — microfibrils radial rather than longitudinal — without keeping which way it ran takes the other half of the pair.
- **Why:** This question requires the reason the text gives for stomatal opening, demonstrated by the stem asking what 'facilitates opening of stomatal aperture' and by options that offer rival mechanisms rather than a named part.
- **Note:** E1_question_type reads statement_options, but the stem is a completion question asking which factor opens the stoma, not an instruction to judge statements, so qtype is recorded as mcq.
<!--/ecat-->

## Q63

Biology · botany · Plant Kingdom

Select the mismatch :

- (1) Salvinia – Heterosporous
- (2) Equisetum – Homosporous
- **(3)** Pinus – Dioecious
- (4) Cycas – Dioecious

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Pinus is monoecious plant having both male and female cones on same plant.

**Solved independently** (answer withheld)

1. $\textit{Salvinia}$ produces microspores and megaspores, so it is heterosporous: option $1$ matches.
2. $\textit{Equisetum}$ produces one kind of spore, so it is homosporous: option $2$ matches.
3. $\textit{Pinus}$ bears male and female cones on the same tree, so it is monoecious, not dioecious: option $3$ is a mismatch.
4. $\textit{Cycas}$ bears male and female cones on separate plants, so it is dioecious: option $4$ matches.
5. The only mismatch is option $3$.

**Subtopic:** Gymnosperms · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q063_d6c392bb_30102026.png?v=d6c392bb133f)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q063_b2b3f7d5_30102026.png?v=b2b3f7d5d8f0)

---

<!--ecat-->
#### Categories

- **Type:** **New type (proposed)** (`new_type`) — a printed shape none of the above describes
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Spore type and sex distribution are group-by-group facts: the pteridophyte majority is homosporous with Salvinia an exception, and among gymnosperms Cycas is dioecious while Pinus carries both cones on one plant
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The general line that the pteridophyte majority is homosporous sits beside the sentence naming Salvinia as an exception, and a student who kept only the general line reads a fern called heterosporous as the planted error.
- **Why:** This question requires the printed spore-type and sex facts for named plant groups, demonstrated by 'Pinus – Dioecious' being the one pair the text contradicts. On the trap axis I applied the swap test: replace the plant names with unlike words and the pull on option 1 survives, so position — the general rule printed beside its exception — is doing the work, and the label is nearby_fact rather than look_alike_term.
- **Note:** E1_question_type reads plain_mcq, but every option is printed as a pair judged whole, the same shape as q059; the live qtype vocabulary has no value for it, so new_type carries it with a proposal.
<!--/ecat-->

## Q64

Biology · botany · Organisms and Populations

Asymptote in a logistic growth curve is obtained when

- (1) $K > N$
- (2) $K < N$
- (3) The value of '$r$' approaches zero
- **(4)** $K = N$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A population growing in a habitat with limited resources shows logistic growth curve.
2. For logistic growth
3. $\frac{dN}{dt} = rN\left(\frac{K - N}{K}\right)$
4. If $K = N$ then $\frac{K - N}{K} = 0$
5. $\therefore$ the $\frac{dN}{dt} = 0$,
6. the population reaches asymptote.

**Solved independently** (answer withheld)

1. The logistic (Verhulst-Pearl) growth equation is $\frac{dN}{dt} = rN\left(\frac{K-N}{K}\right)$.
2. When $N = K$, $\frac{K-N}{K} = 0$, so $\frac{dN}{dt} = 0$ and the sigmoid curve flattens into its asymptote. This is when $K = N$, option $4$.

**Subtopic:** Logistic Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q064_bbe32c03_30102026.png?v=bbe32c03ae8d)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q064_8ba6b064_30102026.png?v=8ba6b064a2a2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In logistic growth the curve levels off when the population equals the carrying capacity, so the realised growth falls to zero while the intrinsic rate r stays what it was
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  A student who reads r in $\frac{dN}{dt} = rN\left(1 - \frac{N}{K}\right)$ as 'the growth rate' makes the growth vanish by sending r to zero, which zeroes the wrong symbol.
- **Why:** This question requires the logistic relation applied to the plateau case, demonstrated by options that are relations between K and N rather than a sentence to be recalled.
<!--/ecat-->

## Q65

Biology · both · Biotechnology: Principles and Processes

The process of separation and purification of expressed protein before marketing is called

- (1) Bioprocessing
- (2) Postproduction processing
- (3) Upstream processing
- **(4)** Downstream processing

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Biosynthetic stage for synthesis of product in recombinant DNA technology is called upstreaming process while after completion of biosynthetic stage, the product has to be subjected through a series of processes which include separation and purification are collectively referred to as downstreaming processing.

**Solved independently** (answer withheld)

1. After the product is formed in the bioreactor, it must be separated and purified, and given suitable formulation and quality control before marketing; these steps together are called $\text{downstream processing}$, which is option $4$.

**Subtopic:** Obtaining the Foreign Gene Product & Downstream Processing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q065_d6b93f34_30102026.png?v=d6b93f34ed35)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q065_f4dd8ce7_30102026.png?v=f4dd8ce7e275)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Downstream processing is the name for everything done after the protein has been expressed — separation, purification and formulation — before the product can be sold
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Upstream' and 'downstream' are the same word-frame with the direction switched, and a student who stored only '...stream processing' as the name of these stages takes the one they met first.
- **Why:** This question requires the printed name of the stage that follows expression, demonstrated by the stem's 'separation and purification of expressed protein before marketing'. The likeness test decides the trap axis: replace 'upstream' with a word unlike 'downstream' and the pull dies, so the label is look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q66

Biology · botany · Transport in Plants

The water potential of pure water is

- (1) More than zero but less than one
- (2) More than one
- **(3)** Zero
- (4) Less than zero

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. By convention, the water potential of pure water at standard temperature, which is not under any pressure, is taken to be zero.

**Solved independently** (answer withheld)

1. By convention, the water potential of pure water at standard temperature and atmospheric pressure is $\Psi_w = 0$, which is option $3$.

**Subtopic:** Water Potential · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q066_355acf51_30102026.png?v=355acf51de65)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q066_8d673342_30102026.png?v=8d673342d7b1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pure water at standard conditions is the reference point of the water-potential scale, so its value is zero and every solution sits below it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  A student who stored 'water potential is always negative' — true once a solute is in the water — applies it to the one case the stem has excluded by printing 'pure'.
- **Why:** This question requires the reference value of the water-potential scale, demonstrated by the stem specifying 'pure water' rather than a solution.
<!--/ecat-->

## Q67

Biology · zoology · Reproductive Health

The function of copper ions in copper releasing IUD's is :

- (1) They make uterus unsuitable for implantation
- (2) They inhibit ovulation
- **(3)** They suppress sperm motility and fertilising capacity of sperms
- (4) They inhibit gametogenesis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{Cu^{2+}}$ interfere in the sperm movement, hence suppress the sperm motility and fertilising capacity of sperms.

**Solved independently** (answer withheld)

1. Copper-releasing IUDs release $\mathrm{Cu^{2+}}$ ions, which suppress sperm motility and the fertilising capacity of sperms, so the answer is option $3$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q067_a2213afb_30102026.png?v=a2213afbc113)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q067_c1bf5a1c_30102026.png?v=c1bf5a1c04d7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A copper-releasing IUD acts on the sperm — the ions cut motility and fertilising capacity — while making the uterus unfit for implantation is what the hormone-releasing device does
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The line about making the uterus unsuitable for implantation sits in the same IUD paragraph, attached to the hormone-releasing devices, so a student who stored that paragraph as one block about IUDs brings it to the copper question.
- **Why:** This question requires the printed action of the copper ions themselves, demonstrated by the stem asking for 'the function of copper ions in copper releasing IUD's'. The swap test puts the trap on nearby_fact: rename the two device types with unlike words and the pull survives, because it is the sentence printed alongside that carries it.
<!--/ecat-->

## Q68

Biology · botany · Sexual Reproduction in Flowering Plants

Double fertilization is exhibited by

- (1) Fungi
- **(2)** Angiosperms
- (3) Gymnosperms
- (4) Algae

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Double fertilization is a characteristic feature exhibited by angiosperms.
2. It involves syngamy and triple fusion.

**Solved independently** (answer withheld)

1. Double fertilisation is syngamy (male gamete $+$ egg $\to$ zygote, $2n$) together with triple fusion (male gamete $+$ two polar nuclei $\to$ primary endosperm nucleus, $3n$), a feature unique to angiosperms, which is option $2$.

**Subtopic:** Double Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q068_906da6d6_30102026.png?v=906da6d6d0f4)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q068_81567e03_30102026.png?v=81567e038fea)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Double fertilisation — syngamy plus the triple fusion that makes endosperm — happens inside an embryo sac, so it belongs to angiosperms alone
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Gymnosperms are the seed plants taught immediately beside angiosperms and they also send two male gametes down a pollen tube, so a student who kept 'seed plants, two male gametes' as one line reaches for the adjacent group.
- **Why:** This question requires the group in which double fertilisation occurs, demonstrated by four coordinate groups being offered with no criterion printed to apply.
<!--/ecat-->

## Q69

Biology · botany · Ecosystem

Presence of plants arranged into well defined vertical layers depending on their height can be seen best in :

- (1) Grassland
- (2) Temperate Forest
- (3) Tropical Savannah
- **(4)** Tropical Rain Forest

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The tropical rain forest have five vertical strata on the basis of height of plants.
2. i.e., ground vegetation, shrubs, short canopy trees, tall canopy trees and tall emergent trees.

**Solved independently** (answer withheld)

1. Vertical stratification means plants of different heights occupying distinct layers; it is best developed in tropical rain forests, which have emergent, canopy, understorey, shrub and herb layers, so the answer is option $4$.

**Subtopic:** Ecosystem – Structure, Function and Components · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q069_0e28349c_30102026.png?v=0e28349c83c1)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q069_136ab69b_30102026.png?v=136ab69b06f8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Stratification is sharpest where species of many different heights share one patch: a tropical rain forest stacks emergent, canopy, understorey, shrub and herb layers
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  A temperate forest does carry a canopy, a shrub layer and a herb layer, so a student who tests each option for 'does this have vertical layers' stops at the first forest and never weighs the stem's 'best'.
- **Why:** This question requires four ecosystems to be ranked on how sharply their vegetation is stratified, demonstrated by the stem's 'can be seen best in' with two forests among the options.
- **Note:** The trap option is true of the general property and fails only on the stem's superlative 'best'. answers_other_question is the nearest live label and carries it, but a named value for a true-but-not-superlative option would carry it more exactly; recording it here so the vocabulary can take it if it recurs.
<!--/ecat-->

## Q70

Biology · botany · Ecosystem

Which ecosystem has the maximum biomass?

- (1) Pond ecosystem
- (2) Lake ecosystem
- **(3)** Forest ecosystem
- (4) Grassland ecosystem

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. High productive ecosystem are
2. – Tropical rain forest
3. – Coral reef
4. – Estuaries
5. – Sugarcane fields

**Solved independently** (answer withheld)

1. Standing biomass per unit area is highest in forest ecosystems because large trees store organic matter in woody tissue, while pond and lake producers are mostly small phytoplankton and grasslands have only herbaceous plants, so the answer is option $3$.

**Subtopic:** Types of Ecosystems · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q070_1cc18e14_30102026.png?v=1cc18e14b127)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q070_f860af1b_30102026.png?v=f860af1bdf53)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Biomass is the living matter standing at one moment, and the trunks and branches a forest keeps standing hold far more of it than grass or water-column producers
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  A student who reads 'biomass' as how fast the plants grow picks the grass crop that is renewed every season, which answers the turnover question and not the standing-crop one the stem asks.
- **Why:** This question requires four ecosystems to be ranked by standing biomass, demonstrated by the stem's 'maximum' over options that set two aquatic ecosystems against two terrestrial ones.
<!--/ecat-->

## Q71

Biology · botany · Morphology of Flowering Plants

Root hairs develop from the region of

- (1) Root cap
- (2) Meristematic activity
- **(3)** Maturation
- (4) Elongation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In roots, the root hairs arise from zone of maturation.
2. This zone is differentiated zone thus bearing root hairs.

**Solved independently** (answer withheld)

1. In NCERT the region proximal to the zone of elongation is the region of maturation, and some epidermal cells there form very fine thread-like root hairs, so the answer is option $3$.

**Subtopic:** The Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q071_0fb95cc9_30102026.png?v=0fb95cc96e2f)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q071_d8364fe4_30102026.png?v=d8364fe4ff84)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Root hairs are outgrowths of epidermal cells in the region of maturation, the zone above elongation where cells have finished growing and differentiate
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Elongation is the zone printed immediately before maturation in the root-tip sequence, and a student who kept the order but not which zone bears the hairs takes the neighbouring one, where the cells are still visibly growing.
- **Why:** This question requires the printed zone of the root tip that bears root hairs, demonstrated by four options that are the named regions of that tip. The swap test puts the trap on nearby_fact: replace the zone names with unlike words and the pull on 'Elongation' survives, because what carries it is the zone printed next to the right one, not the resemblance between 'maturation' and 'meristematic'.
<!--/ecat-->

## Q72

Biology · both · Molecular Basis of Inheritance

DNA replication in bacteria occurs

- **(1)** Prior to fission
- (2) Just before transcription
- (3) During S-phase
- (4) Within nucleolus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. DNA replication in bacteria occurs prior to fission.
2. Prokaryotes do not show well marked S-phase due to their primitive nature.

**Solved independently** (answer withheld)

1. Bacteria are prokaryotes with no nucleus or nucleolus and no eukaryotic cell-cycle phases such as S-phase, so their circular DNA is copied before the cell divides by binary fission, which is option $1$.

**Subtopic:** Replication · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q072_95cb43ee_30102026.png?v=95cb43ee82e3)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q072_5013f352_30102026.png?v=5013f352684b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A bacterium has no S phase and no nucleus: it copies its single chromosome and then splits, so replication sits just ahead of binary fission
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  'DNA is replicated in S phase' is a rule about the eukaryotic cell cycle, and a student who applies it without stopping at the stem's 'in bacteria' lands on a phase a bacterium does not have.
- **Why:** This question requires when a bacterium copies its DNA, demonstrated by the stem's 'in bacteria' standing against options that name a eukaryotic phase and a eukaryotic structure.
<!--/ecat-->

## Q73

Biology · zoology · Strategies for Enhancement in Food Production

Homozygous purelines in cattle can be obtained by

- (1) mating of individuals of different breed
- (2) mating of individuals of different species
- **(3)** mating of related individuals of same breed
- (4) mating of unrelated individuals of same breed

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Inbreeding results in increase in the homozygosity.
2. Therefore, mating of the related individuals of same breed will increase homozygosity.

**Solved independently** (answer withheld)

1. Inbreeding, i.e. mating of more closely related individuals of the same breed for $4$-$6$ generations, increases homozygosity and so yields homozygous purelines; this is option $3$.

**Subtopic:** Animal Breeding · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q073_a038dc59_30102026.png?v=a038dc590118)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q073_96f87985_30102026.png?v=96f879852683)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inbreeding — mating closely related animals inside one breed — is what drives homozygosity up and yields a pureline; mating unrelated or different stock pulls it the other way
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The option keeps the right half of the printed definition, 'same breed', and inverts the word that decides it: a student who stored 'within the same breed' and lost 'closely related' takes unrelated, because avoiding relatives sounds like the safe breeding advice.
- **Why:** This question requires which mating scheme raises homozygosity, demonstrated by options that differ only in whether the animals are related and whether they share a breed.
- **Note:** E1_question_type reads statement_options, but the stem is a completion question and each option is a phrase naming a mating scheme rather than a statement to be judged, so qtype is recorded as mcq.
<!--/ecat-->

## Q74

Biology · botany · Morphology of Flowering Plants

In Bougainvillea thorns are the modifications of

- **(1)** Stem
- (2) Leaf
- (3) Stipules
- (4) Adventitious root

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Thorns are hard, pointed straight structures for protection.
2. These are modified stem

**Solved independently** (answer withheld)

1. In Bougainvillea (as in Citrus) the axillary buds of the stem become woody, straight, pointed thorns, so the thorns are modifications of the $\text{stem}$, which is option $1$.

**Subtopic:** The Stem · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q074_a694f9fa_30102026.png?v=a694f9fa9193)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q074_c0c6334c_30102026.png?v=c0c6334c5a3d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Thorns are shoot structures — in Bougainvillea the axillary bud becomes the thorn — while the spines of plants such as Opuntia are modified leaves
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The leaf-modification paragraph with its spiny example sits beside the stem-modification one, and a student who stored 'sharp outgrowths are modified leaves' brings that line to a thorn.
- **Why:** This question requires which organ the thorn of a named plant is a modification of, demonstrated by the options offering stem, leaf, stipule and root for Bougainvillea. The swap test puts the trap on nearby_fact: 'stem' and 'leaf' do not resemble each other and the pull survives any renaming, because it is the neighbouring modification example that carries it.
<!--/ecat-->

## Q75

Biology · zoology · Excretory Products and Their Elimination

A decrease in blood pressure/volume will not cause the release of

- (1) Aldosterone
- (2) ADH
- (3) Renin
- **(4)** Atrial Natriuretic Factor

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A decrease in blood pressure / volume stimulates the release of renin, aldosterone, and ADH while increase in blood pressure / volume stimulates the release of Atrial Natriuretic Factor (ANF) which cause vasodilation and also inhibits RAAS (Renin Angiotensin Aldosterone System) mechanism that decreases the blood volume/pressure.

**Solved independently** (answer withheld)

1. A fall in glomerular blood flow/pressure activates the JG cells to release $\text{renin}$, which converts angiotensinogen to angiotensin I and then to angiotensin II.
2. Angiotensin II stimulates the adrenal cortex to release $\text{aldosterone}$, increasing Na$^+$ and water reabsorption.
3. A fall in blood volume also stimulates release of $\text{ADH}$ from the neurohypophysis to conserve water.
4. $\text{ANF}$ is released by atrial walls only when blood pressure/volume increases, so a decrease will not cause its release: option $4$.

**Subtopic:** Regulation Of Kidney Function · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q075_d4b8564e_30102026.png?v=d4b8564e09c5)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q075_15099d28_30102026.png?v=15099d2893dc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A fall in blood pressure or volume switches on the renin-angiotensin machinery with aldosterone and ADH; ANF is the opposite signal, released when the atria are stretched by a rise
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Renin is the first thing the kidney releases when blood volume falls, which answers 'which IS released'; a student reading the stem for its trigger rather than for its 'not' stops at the hormone the account ties straight to a falling pressure.
- **Why:** This question requires which hormone is not released when blood pressure or volume falls, demonstrated by the stem's 'will not cause' against three hormones whose printed trigger is exactly that fall.
<!--/ecat-->

## Q76

Biology · botany · Respiration in Plants

Which statement is wrong for Krebs' cycle?

- (1) During conversion of succinyl CoA to succinic acid, a molecule of GTP is synthesised
- **(2)** The cycle starts with condensation of acetyl group (acetyl CoA) with pyruvic acid to yield citric acid
- (3) There are three points in the cycle where $\mathrm{NAD^{+}}$ is reduced to $\mathrm{NADH + H^{+}}$
- (4) There is one point in the cycle where $\mathrm{FAD^{+}}$ is reduced to $\mathrm{FADH_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Krebs cycle starts with condensation of acetyl CoA (2C) with oxaloacetic acid (4C) to form citric acid (6C).

**Solved independently** (answer withheld)

1. The first step of the cycle is $\text{acetyl CoA} + \text{oxaloacetic acid} + \mathrm{H_2O} \rightarrow \text{citric acid} + \text{CoA}$, so the acceptor is oxaloacetic acid, not pyruvic acid; statement $2$ is wrong.
2. Succinyl CoA $\rightarrow$ succinic acid is coupled to substrate-level phosphorylation forming $\mathrm{GTP}$, so statement $1$ is correct.
3. $\mathrm{NAD^{+}}$ is reduced to $\mathrm{NADH + H^{+}}$ at three points (isocitrate, $\alpha$-ketoglutarate, malate steps), so statement $3$ is correct.
4. $\mathrm{FAD}$ is reduced to $\mathrm{FADH_2}$ at one point (succinate $\rightarrow$ fumarate), so statement $4$ is correct; the wrong statement is option $2$.

**Subtopic:** Aerobic Respiration And Tricarboxylic Acid Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q076_02ae2d66_30102026.png?v=02ae2d66d89b)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q076_c851c96f_30102026.png?v=c851c96ff429)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Krebs' cycle starts when acetyl CoA condenses with oxaloacetic acid, and inside it three NAD+ and one FAD are reduced while one GTP is made at the succinyl CoA step
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  A student who stored substrate-level phosphorylation as making ATP meets 'GTP' at the succinyl CoA step, reads the one-letter difference as the word the paper swapped, and marks a true line as the wrong one.
- **Why:** This question requires the printed steps of Krebs' cycle, demonstrated by the key option naming 'pyruvic acid' as what acetyl CoA condenses with. The likeness test puts the trap on look_alike_term: it is the one-letter distance between the printed GTP and the remembered ATP that makes a true option read as the planted error, and the pull dies if the coin printed there is a word unlike ATP.
- **Note:** Option 4 prints 'FAD+' where the oxidised flavin is written FAD; that is a notation oddity in the option and does not change which statement the key marks as wrong. A strict reader could flag the '+' itself, which is worth a repair pass on the option text rather than a trap tag.
<!--/ecat-->

## Q77

Biology · both · Cell Cycle and Cell Division

Anaphase promoting complex (APC) is a protein degradation machinery necessary for proper mitosis of animal cells. If APC is defective in a human cell, which of the following is expected to occur?

- **(1)** Chromosomes will not segregate
- (2) Recombination of chromosome arms will occur
- (3) Chromosomes will not condense
- (4) Chromosomes will be fragmented

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Anaphase Promoting Complex (APC) is a protein necessary for separation of daughter chromosomes during anaphase.
2. If APC is defective then the chromosomes will fail to segregate during anaphase.

**Solved independently** (answer withheld)

1. APC is the degradation machinery that triggers the metaphase-to-anaphase transition, letting sister chromatids separate and move to opposite poles.
2. If APC is defective, the protein holding sister chromatids together is not removed, so anaphase separation fails and chromosomes will not segregate, which is option $1$.

**Subtopic:** Anaphase and Telophase · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q077_d8e88084_30102026.png?v=d8e88084685e)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q077_9882985f_30102026.png?v=9882985f4e93)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Sister chromatids separate at anaphase, and the anaphase promoting complex is the degradation machinery that releases them, so losing it blocks segregation and nothing earlier
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  A student who holds 'mitosis cannot run without timely protein destruction' but files that machinery at the opening of mitosis predicts the first visible step fails, so chromosomes never condense. Condensation happens in prophase and needs no APC; the step APC gates is the release of sister chromatids.
- **Why:** This question requires a known function to be applied to a supplied defect, demonstrated by the stem's 'If APC is defective in a human cell, which of the following is expected to occur?'
- **Note:** The pattern called this statement_options, but the options are short predicted outcomes rather than claims to be graded correct or incorrect, so qtype is mcq. The recorded NOT sits inside the options ('will not segregate', 'will not condense'), not in the task.
<!--/ecat-->

## Q78

Biology · zoology · Digestion and Absorption

Which of the following options best represents the enzyme composition of pancreatic juice?

- (1) Peptidase, amylase, pepsin, rennin
- **(2)** Lipase, amylase, trypsinogen, procarboxypeptidase
- (3) Amylase, peptidase, trypsinogen, rennin
- (4) Amylase, pepsin, trypsinogen, maltase

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rennin and Pepsin enzymes are present in the gastric juice.
2. Maltase is present in the intestinal juice.

**Solved independently** (answer withheld)

1. Pancreatic juice carries the inactive enzymes trypsinogen, chymotrypsinogen and procarboxypeptidases, together with amylases, lipases and nucleases; pepsin and rennin are gastric enzymes, while maltase and peptidases come from the intestinal juice, so option $2$ (lipase, amylase, trypsinogen, procarboxypeptidase) is the only fully pancreatic set.

**Subtopic:** Digestion of Food · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q078_67204059_30102026.png?v=67204059bb00)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q078_6a63b760_30102026.png?v=6a63b760a748)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pancreatic juice carries trypsinogen, chymotrypsinogen, procarboxypeptidase, amylase, lipase and nucleases; pepsin and rennin are gastric, and peptidases and maltase are intestinal
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Amylase and trypsinogen are both genuinely pancreatic, so a student who checks a set by the names they are sure of accepts the whole option and never tests rennin. Rennin is secreted by the gastric glands of an infant, and 'peptidase' belongs to the intestinal juice, so the set fails on two of its four names.
- **Why:** This question requires the stated membership of a taught secretion list, demonstrated by the stem's 'best represents the enzyme composition of pancreatic juice'.
- **Note:** The pattern called this statement_options; each option is a four-name enzyme set scored whole, half right scoring nothing, so qtype is two_part.
<!--/ecat-->

## Q79

Biology · botany · Plant Kingdom

Life cycle of Ectocarpus and Fucus respectively are

- **(1)** Haplodiplontic, Diplontic
- (2) Haplodiplontic, Haplontic
- (3) Haplontic, Diplontic
- (4) Diplontic, Haplodiplontic

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ectocarpus has haplodiplontic life cycle and Fucus has diplontic life cycle.

**Solved independently** (answer withheld)

1. As NCERT teaches, Ectocarpus, Polysiphonia and kelps have a $\text{haplodiplontic}$ life cycle, and Fucus, an alga, has a $\text{diplontic}$ life cycle, so the pair is (Haplodiplontic, Diplontic), which is option $1$.

**Subtopic:** Plant Life Cycles and Alternation of Generations · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q079_eaf1f88f_30102026.png?v=eaf1f88fc08b)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q079_42b1d311_30102026.png?v=42b1d3111251)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ectocarpus is haplo-diplontic, with free-living haploid and diploid phases, while Fucus is diplontic, the only haploid cells being its gametes
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student holding both life-cycle terms but not which alga owns which hands diplontic to Ectocarpus, and the option printed is the exact interchange of the key's two labels. The order matters because the stem pairs the two names with 'respectively'.
- **Why:** This question requires two stated list memberships returned in the printed order, demonstrated by the stem's 'Life cycle of Ectocarpus and Fucus respectively are'.
<!--/ecat-->

## Q80

Biology · botany · Anatomy of Flowering Plants

Which of the following is made up of dead cells?

- **(1)** Phellem
- (2) Phloem
- (3) Xylem parenchyma
- (4) Collenchyma

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Cork cambium undergoes periclinal division and cuts off thick walled suberised dead cork cells towards outside and it cuts off thin walled living cells i.e., phelloderm on inner side.

**Solved independently** (answer withheld)

1. Phellem (cork) cells are compactly arranged, have suberin deposited in their walls and are dead at maturity, whereas phloem (sieve tubes, companion cells, phloem parenchyma), xylem parenchyma and collenchyma are living, so the answer is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q080_795d2a43_30102026.png?v=795d2a43802f)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q080_8d659261_30102026.png?v=8d6592612031)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cork, the phellem, is dead at maturity, whereas xylem parenchyma is the living element of xylem, the sieve tubes and companion cells of phloem are living, and collenchyma is a living mechanical tissue
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The dead-cell fact belongs to the tracheids, vessels and fibres printed in the same xylem paragraph, and a student who carries 'xylem is dead' across to the fourth element of xylem ticks xylem parenchyma. Parenchyma is the word that decides it: it is the one living component of the tissue.
- **Why:** This question requires the stated living-or-dead status of a named tissue, demonstrated by the stem's 'made up of dead cells' set against the option 'Xylem parenchyma'.
- **Note:** On the nearby_fact against look_alike_term test: 'xylem parenchyma' and 'phellem' do not resemble each other, so likeness cannot be the pull, and swapping the wrong name for an unlike word leaves the trap standing because the dead-xylem fact printed beside parenchyma carries it. The resemblance route that does exist here, phellem against phloem, is recorded on option 2.
<!--/ecat-->

## Q81

Biology · botany · Microbes in Human Welfare

Which of the following is correctly matched for the product produced by them?

- (1) Penicillium notatum : Acetic acid
- **(2)** Saccharomyces cerevisiae : Ethanol
- (3) Acetobacter aceti : Antibiotics
- (4) Methanobacterium : Lactic acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Saccharomyces cerevisiae is commonly called Brewer’s yeast.
2. It causes fermentation of carbohydrates producing ethanol.

**Solved independently** (answer withheld)

1. Option $1$: $\textit{Penicillium notatum}$ produces the antibiotic penicillin, not acetic acid, so it is mismatched.
2. Option $2$: $\textit{Saccharomyces cerevisiae}$ (brewer's yeast) ferments sugars to ethanol, so it is correctly matched.
3. Option $3$: $\textit{Acetobacter aceti}$ produces acetic acid, not antibiotics, so it is mismatched.
4. Option $4$: $\textit{Methanobacterium}$ produces methane (biogas), not lactic acid, so it is mismatched; the answer is option $2$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q081_601fbd41_30102026.png?v=601fbd41cfb3)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q081_5037f198_30102026.png?v=5037f1986256)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each industrial microbe goes with one product: Saccharomyces cerevisiae with ethanol, Penicillium notatum with penicillin, Acetobacter aceti with acetic acid and Methanobacterium with methane
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Acetic acid is a product printed one row away from Penicillium in the same microbes-and-products table, so a student who remembers that both names belong to the table but not which row they share accepts the pairing. The acid is the row for Acetobacter aceti, and Penicillium notatum's product is penicillin.
- **Why:** This question requires one taught organism-to-product pairing to be confirmed, demonstrated by the stem's 'correctly matched for the product produced by them' and the option 'Saccharomyces cerevisiae : Ethanol'.
- **Note:** The pattern called this statement_options; each option is an organism-and-product pair scored whole, so qtype is two_part. It is not match_columns, because no two columns are printed and the answer is not a pairing code.
<!--/ecat-->

## Q82

Biology · botany · Plant Growth and Development

Fruit and leaf drop at early stages can be prevented by the application of

- **(1)** Auxins
- (2) Gibberellic acid
- (3) Cytokinins
- (4) Ethylene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Auxins prevent premature leaf and fruit fall.
2. NAA prevents fruit drop in tomato; 2,4-D prevents fruit drop in Citrus.

**Solved independently** (answer withheld)

1. Auxins prevent premature fruit and leaf drop at early stages, though they promote abscission of older mature leaves and fruits, so the answer is option $1$ (Auxins).

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q082_b9139e18_30102026.png?v=b9139e186047)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q082_0a928ee0_30102026.png?v=0a928ee061bf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Auxins prevent fruit and leaf fall at early stages while promoting the abscission of older, mature leaves and fruits; ethylene is the hormone that promotes abscission
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Ethylene is the hormone tied to senescence and abscission of leaves and fruits, so a student who matches the hormone to the event without reading the direction of the stem lands on it. The stem asks what prevents early drop, and ethylene does the opposite of that.
- **Why:** This question requires the stated physiological effect of one growth regulator, demonstrated by the stem's 'Fruit and leaf drop at early stages can be prevented by the application of'.
<!--/ecat-->

## Q83

Biology · botany · Biological Classification

Viroids differ from viruses in having :

- (1) RNA molecules with protein coat
- **(2)** RNA molecules without protein coat
- (3) DNA molecules with protein coat
- (4) DNA molecules without protein coat

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Viroids are sub-viral agents as infectious RNA particles, without protein coat.

**Solved independently** (answer withheld)

1. Viroids, discovered by T.O. Diener as the cause of potato spindle tuber disease, are free RNA molecules that lack the protein coat found in viruses, so the answer is option $2$.

**Subtopic:** Viroids, Prions & Lichens · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q083_b44ca39a_30102026.png?v=b44ca39a6bc7)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q083_a9d9454f_30102026.png?v=a9d9454fbef7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A viroid is free infectious RNA with no protein coat, where a virus keeps its nucleic acid packed inside a capsid
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A student who stores 'viroid equals RNA' has the first half right and carries the capsid across from the virus the stem is comparing it with. Both halves of the option are scored, and the coat is the very feature the stem says differs.
- **Why:** This question requires the stated defining feature of one agent set against another, demonstrated by the stem's 'Viroids differ from viruses in having' and the option 'RNA molecules without protein coat'.
- **Note:** The pattern called this statement_options; the options are noun phrases completing the stem, and each pairs a nucleic acid with a coat status so that both halves are scored, which is why qtype is two_part and the trap can be half_right.
<!--/ecat-->

## Q84

Biology · both · Biomolecules

Which of the following are not polymeric?

- (1) Polysaccharides
- **(2)** Lipids
- (3) Nucleic acids
- (4) Proteins

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Nucleic acids are polymers of nucleotides
2. Proteins are polymers of amino acids
3. Polysaccharides are polymers of monosaccharides
4. Lipids are the esters of fatty acids and alcohol

**Solved independently** (answer withheld)

1. Polysaccharides (monosaccharide chains), nucleic acids (nucleotide chains) and proteins (amino acid chains) are polymers, but lipids have low molecular weight and are not strictly macromolecules, so they are not polymeric: option $2$.

**Subtopic:** Biomacromolecules · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q084_19e57c06_30102026.png?v=19e57c064d96)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q084_4e546ace_30102026.png?v=4e546aced892)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Polysaccharides, nucleic acids and proteins are polymers built of repeating monomers, while lipids are small molecules that do not polymerise
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each of the other three is named as a polymer in the source's own words, polysaccharides as long chains of sugars, nucleic acids as polynucleotides and proteins as polypeptides, so no partly remembered fact lands on one of them rather than another. The error this question punishes, counting lipids among the macromolecules of the acid-insoluble fraction, falls on the key itself and singles out no distractor.
- **Why:** This question requires the stated monomer-and-polymer status of four biomolecule classes, demonstrated by the stem's 'Which of the following are not polymeric?' against the option 'Lipids'.
- **Note:** no_trap is the finding here, and the three fillers record what was checked rather than padding: every wrong option is a class the source itself names as a polymer, so the question discriminates on whether lipids were stored as non-polymeric and not on any route into a distractor. The recorded NOT is in the task, which is what makes lipids the answer.
<!--/ecat-->

## Q85

Biology · zoology · Chemical Coordination and Integration

A temporary endocrine gland in the human body is

- **(1)** Corpus luteum
- (2) Corpus allatum
- (3) Pineal gland
- (4) Corpus cardiacum

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Corpus luteum is the temporary endocrine structure formed in the ovary after ovulation.
2. It is responsible for the release of the hormones like progesterone, oestrogen etc.

**Solved independently** (answer withheld)

1. The corpus luteum forms from the ruptured Graafian follicle after ovulation, secretes progesterone, and degenerates (into the corpus albicans) if fertilisation does not occur. It is therefore a temporary endocrine gland in humans, which is option $1$; the pineal gland is a permanent human gland, and the corpus allatum and corpus cardiacum are insect endocrine glands.

**Subtopic:** Gonads · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q085_07d511eb_30102026.png?v=07d511eb4f43)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q085_4f4e005c_30102026.png?v=4f4e005ccaa7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The corpus luteum forms from the ruptured follicle and secretes progesterone only until it regresses, which is what makes it a temporary endocrine gland
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Three of the four options open with 'corpus', and corpus allatum is a gland a student has met by name, so the shared word carries them onto it. It is an insect gland, and the stem restricts the answer to the human body.
- **Why:** This question requires the stated life span of a named human gland, demonstrated by the stem's 'A temporary endocrine gland in the human body is'.
- **Note:** On the look_alike_term against nearby_fact test: swapping corpus allatum for an unlike name, such as the insect prothoracic gland, kills most of the pull, so the resemblance of the corpus names is doing the work rather than position in the text.
<!--/ecat-->

## Q86

Biology · botany · Photosynthesis in Higher Plants

Phosphonol pyruvate (PEP) is the primary $\mathrm{CO_2}$ acceptor in :

- (1) $\mathrm{C_2}$ plants
- (2) $\mathrm{C_3}$ and $\mathrm{C_4}$ plants
- (3) $\mathrm{C_3}$ plants
- **(4)** $\mathrm{C_4}$ plants

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. PEP is 3C compound which serves as primary $\mathrm{CO_2}$ acceptor in the mesophyll cell cytoplasm of $\mathrm{C_4}$ plants like maize, sugarcane, Sorghum etc.

**Solved independently** (answer withheld)

1. In $\mathrm{C_4}$ plants the primary $\mathrm{CO_2}$ acceptor in mesophyll cells is the 3-carbon PEP, fixed by PEP carboxylase to form the 4-carbon OAA, while $\mathrm{C_3}$ plants use RuBP, so the answer is option $4$.

**Subtopic:** The C₄ Pathway · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q086_def171bb_30102026.png?v=def171bb376e)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q086_8d7b7afe_30102026.png?v=8d7b7afe459f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a C4 plant PEP in the mesophyll takes up CO2 first and gives the four-carbon OAA; in a C3 plant the primary acceptor is RuBP
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  C4 leaves do run the Calvin cycle in their bundle-sheath cells, so a student who remembers that both pathways work in a C4 plant reads the inclusive option as the safe one. The stem asks for the primary acceptor, and in a C3 plant that is RuBP, so the C3 half of this option fails.
- **Why:** This question requires the stated first acceptor of one pathway, demonstrated by the stem's 'primary $\mathrm{CO_2}$ acceptor' set against the option '$\mathrm{C_4}$ plants'.
- **Note:** The stem prints 'Phosphonol pyruvate' for phosphoenolpyruvate; the abbreviation PEP beside it makes the species unambiguous, so the tag follows the question as printed and the spelling is flagged for repair rather than treated as a trap.
<!--/ecat-->

## Q87

Biology · botany · Organisms and Populations

Plants which produce characterstic pneumatophores and show vivipary belong to

- (1) Psammophytes
- (2) Hydrophytes
- (3) Mesophytes
- **(4)** Halophytes

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Halophytes growing in saline soils show
2. (i) Vivipary which is in-situ seed germination
3. (ii) Pneumatophores for gaseous exchange

**Solved independently** (answer withheld)

1. Pneumatophores (negatively geotropic breathing roots) and vivipary (seed germination on the parent plant) are typical of mangrove plants such as $Rhizophora$, which grow in saline swampy soil and are therefore halophytes, option $4$.

**Subtopic:** Homeostasis, Adaptations and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q087_00e7c6db_30102026.png?v=00e7c6dbe390)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q087_762edbf7_30102026.png?v=762edbf71908)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mangroves of saline tidal swamps are halophytes, and pneumatophores and vivipary are their adaptations to salt-laden, waterlogged soil
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Pneumatophores are breathing roots that come up out of waterlogged mud, so a student who reads the feature as an adaptation to standing water names the water category sitting beside halophytes in the same habitat list. The class is decided by salt, not by water: a pond hydrophyte has neither breathing roots nor viviparous seedlings.
- **Why:** This question requires two diagnostic features to be referred to the habitat class the source prints them under, demonstrated by the stem's 'pneumatophores and show vivipary belong to'.
- **Note:** On the nearby_fact against look_alike_term test: all four options end in -phyte, so the shared form cannot single this one out, and swapping hydrophytes for an unlike phrase such as 'submerged aquatics' leaves the pull intact, because the waterlogged-soil reasoning carries it. The stem prints 'characterstic' for characteristic.
<!--/ecat-->

## Q88

Biology · botany · Organisms and Populations

Mycorrhizae are the example of

- (1) Antibiosis
- **(2)** Mutualism
- (3) Fungistasis
- (4) Amensalism

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Mycorrhizae is a symbiotic association of fungi with roots of higher plants.

**Solved independently** (answer withheld)

1. Mycorrhiza is a fungus--root association in which the fungus absorbs mineral nutrients (e.g. phosphorus) from the soil for the plant and the plant provides energy-yielding carbohydrates to the fungus, so both partners gain ($+/+$), which is mutualism, option $2$.

**Subtopic:** Mutualism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q088_647172bf_30102026.png?v=647172bfead1)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q088_3f05547a_30102026.png?v=3f05547a9f86)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mycorrhiza is a mutualism: the fungus supplies the root with water and minerals and takes sugars in return, so both partners gain
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Amensalism is the entry printed beside mutualism in the table of interspecific interactions and the one with no worked example against it, so a student holding the table of names without its examples can park mycorrhiza there. Mycorrhiza has both partners gaining, which is the plus-plus row.
- **Why:** This question requires a named association to be placed in the interaction class the source files it under, demonstrated by the stem's 'Mycorrhizae are the example of' and the option 'Mutualism'.
<!--/ecat-->

## Q89

Biology · both · Molecular Basis of Inheritance

If there are 999 bases in an RNA that codes for a protein with 333 amino acids, and the base at position 901 is deleted such that the length of the RNA becomes 998 bases, how many codons will be altered?

- **(1)** 33
- (2) 333
- (3) 1
- (4) 11

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. If deletion occurs at $901^{\mathrm{st}}$ position the remaining $98$ bases specifying for $33$ codons of amino acids will be altered.

**Solved independently** (answer withheld)

1. Each codon has $3$ bases, so $999$ bases give $\frac{999}{3} = 333$ codons.
2. Codons $1$ to $300$ cover bases $1$ to $3 \times 300 = 900$, so they are unaffected by the deletion.
3. Base $901$ is the first base of codon $301$, so deleting it causes a frameshift from codon $301$ onward.
4. Altered codons $= 333 - 301 + 1 = 33$, which is option $1$.

**Subtopic:** Effect of Mutation on Genetic Code · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q089_f30c825b_30102026.png?v=f30c825b2e79)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q089_599ce4ee_30102026.png?v=599ce4eecd26)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A single base deletion shifts the reading frame from that point onward, so every codon downstream of the deletion is read differently and nothing upstream changes
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The frameshift rule gets carried as 'the whole message is read differently', and 333 is already printed in the stem as the number of amino acids, so the total codon count reads as the answer to how many codons are altered. Only the codons after base 901 are re-read: bases 901 to 999 are 99 bases, which is 33 codons.
- **Why:** This question requires a count computed from the stem's own numbers, demonstrated by the stem's 'the base at position 901 is deleted such that the length of the RNA becomes 998 bases, how many codons will be altered?'
<!--/ecat-->

## Q90

Biology · both · Biotechnology: Principles and Processes

A gene whose expression helps to identify transformed cell is known as

- (1) Plasmid
- (2) Structural gene
- **(3)** Selectable marker
- (4) Vector

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In recombinant DNA technology, selectable markers helps in identifying and eliminating non-transformants and selectively permitting the growth of the transformants.

**Solved independently** (answer withheld)

1. A selectable marker is a gene whose expression (e.g. antibiotic resistance such as $amp^R$ or $tet^R$) lets transformed cells be identified and selected while non-transformants are eliminated, so the answer is option $3$.

**Subtopic:** ORI and Selectable Marker · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q090_fbc24eb3_30102026.png?v=fbc24eb3c5d5)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q090_4ee9ac95_30102026.png?v=4ee9ac95f3d1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A selectable marker is the gene carried on a vector whose expression lets transformants be identified and non-transformants eliminated
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The sentence a student remembers, that this is what helps identify transformants, is printed inside the paragraph on the features a vector must have, so the paragraph's subject gets handed the role its component performs. The stem asks for a gene, and the vector is the molecule that carries the gene.
- **Why:** This question requires the term the source attaches to a stated function, demonstrated by the stem's 'A gene whose expression helps to identify transformed cell'.
<!--/ecat-->

## Q91

Biology · botany · Biological Classification

Which of the following are found in extreme saline conditions?

- (1) Cyanobacteria
- (2) Mycobacteria
- **(3)** Archaebacteria
- (4) Eubacteria

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Archaebacteria are able to survive in harsh conditions because of branched lipid chain in cell membrane which reduces fluidity of cell membrane.
2. Halophiles are exclusively found in saline habitats.

**Solved independently** (answer withheld)

1. Organisms living in extreme saline conditions are halophiles, which are $\text{Archaebacteria}$ (they survive harsh habitats due to their distinct cell wall), so the answer is option $3$.

**Subtopic:** Archaebacteria & Mycoplasma · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q091_0122d083_30102026.png?v=0122d083663b)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q091_177e9ab8_30102026.png?v=177e9ab83b68)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Archaebacteria are the monerans of harsh habitats, extreme salt, hot springs and marshes, while cyanobacteria and the rest of the bacteria sit under the eubacteria
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The extreme-salt line belongs to the archaebacterial paragraph, and the eubacterial paragraph follows it directly, so a student who holds 'salt-loving bacteria' without the split between the two groups takes the one called the true bacteria. The halophiles the stem points at are the archaebacteria.
- **Why:** This question requires the habitat the source prints against one group of Monera, demonstrated by the stem's 'found in extreme saline conditions' and the option 'Archaebacteria'.
- **Note:** On the nearby_fact against look_alike_term test: every option ends in -bacteria, so the shared form cannot single this one out, and replacing Eubacteria with the unlike phrase 'true bacteria' leaves the pull intact, so the adjacency of the two paragraphs, not the likeness of the names, is doing the work.
<!--/ecat-->

## Q92

Biology · zoology · Locomotion and Movement

Out of 'X' pairs of ribs in humans only 'Y' pairs are true ribs. Select the option that correctly represents values of X and Y and provides their explanation :

- (1) $X = 24, Y = 7$ True ribs are dorsally attached to vertebral column but are free on ventral side
- (2) $X = 24, Y = 12$ True ribs are dorsally attached to vertebral column but are free on ventral side
- **(3)** $X = 12, Y = 7$ True ribs are attached dorsally to vertebral column and ventrally to the sternum
- (4) $X = 12, Y = 5$ True ribs are attached dorsally to vertebral column and sternum on the two ends

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In human, 12 pairs of ribs are present in which 7 pairs of ribs ($1^{\mathrm{st}}$ to $7^{\mathrm{th}}$ pairs) are attached dorsally to vertebral column and ventrally to the sternum.

**Solved independently** (answer withheld)

1. Humans have $12$ pairs of ribs, so $X = 12$; this rules out options $1$ and $2$ ($X = 24$ counts individual ribs, not pairs).
2. The first $7$ pairs are true ribs, so $Y = 7$; this rules out option $4$ ($Y = 5$).
3. True ribs articulate dorsally with the thoracic vertebrae and ventrally with the sternum through hyaline cartilage, matching the explanation in option $3$.

**Subtopic:** Axial Skeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q092_cc6b4913_30102026.png?v=cc6b4913fce9)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q092_764ea302_30102026.png?v=764ea3028d7f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The human rib cage has 12 pairs of ribs, and the first seven pairs are the true ribs because they join the vertebral column behind and the sternum in front
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student can have X equal to 12 and the two-ended attachment right and still take the wrong side of the seven-and-five split, because five is the number of pairs that are not true ribs, three false plus two floating. Every part of the option is scored together, and Y is the part that fails.
- **Why:** This question requires two stated counts together with the stated criterion behind them, demonstrated by the stem's 'Select the option that correctly represents values of X and Y and provides their explanation'.
- **Note:** The pattern called this statement_options; each option bundles two values and a claim scored together, half right scoring nothing, so qtype is two_part.
<!--/ecat-->

## Q93

Biology · zoology · Human Health and Disease

MALT constitutes about ___________ percent of the lymphoid tissue in human body

- (1) $70\%$
- (2) $10\%$
- **(3)** $50\%$
- (4) $20\%$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. MALT is Mucosa Associated Lymphoid Tissue and it constitutes about $50$ percent of the lymphoid tissue in human body.

**Solved independently** (answer withheld)

1. Mucosa-associated lymphoid tissue (MALT) in the linings of the respiratory, digestive and urogenital tracts makes up about $50\%$ of the lymphoid tissue in the human body, so the answer is option $3$.

**Subtopic:** Immune System and Lymphoid Organs · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q093_33faa4f0_30102026.png?v=33faa4f040e1)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q093_7b6b85f5_30102026.png?v=7b6b85f53a79)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The mucosa-associated lymphoid tissue lining the major tracts holds about half of the lymphoid tissue in the human body
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each of 70%, 10% and 20% was checked for a printed source: none is a figure the chapter attaches to MALT or to any other lymphoid organ, and the stem supplies no quantity to compute from. The only route to a wrong option is misremembering the one stored number, so the question discriminates on whether '50 per cent' was stored and not on any reasoning a distractor absorbs.
- **Why:** This question requires one stored figure to be returned, demonstrated by the stem's 'MALT constitutes about ___________ percent of the lymphoid tissue in human body'.
- **Note:** no_trap is the finding, and the three fillers record what was checked rather than padding: the options are four round percentages and only the stored value separates them. The printed blank is a fill-in-the-blank overlay on a plain mcq, and the qtype vocabulary carries no fill_in_blank value, so mcq is recorded.
<!--/ecat-->

## Q94

Biology · both · Principles of Inheritance and Variation

Which one from those given below is the period for Mendel's hybridization experiments?

- (1) 1857 - 1869
- (2) 1870 - 1877
- **(3)** 1856 - 1863
- (4) 1840 - 1850

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Mendel conducted hybridization experiments on Pea plant for 7 years between 1856 to 1863 and his data was published in 1865 (according to NCERT).

**Solved independently** (answer withheld)

1. Mendel performed hybridisation experiments on the garden pea for seven years, from $1856$ to $1863$, which is option $3$.

**Subtopic:** Principles of Laws of Inheritance · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q094_d84fe25e_30102026.png?v=d84fe25e62f2)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q094_d388becc_30102026.png?v=d388becc3625)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mendel's hybridisation experiments on garden peas ran for seven years, from 1856 to 1863
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The Mendel date a student carries alongside the experiments is the mid-1860s publication of the paper, and option 1 is the only range that covers it. The stem asks instead for the years the experiments ran, which the source gives as 1856 to 1863, so the fact printed beside the right one is what lands here.
- **Why:** This question requires a date the source prints and nothing else, demonstrated by the stem's 'the period for Mendel's hybridization experiments'.
- **Note:** On nearby_fact against look_alike_term: the options are number ranges, not terms, so likeness of names cannot apply; the primary trap is nearby_fact in its literal sense, the publication date printed beside the experimental period in every account of Mendel.
<!--/ecat-->

## Q95

Biology · zoology · Body Fluids and Circulation

Adult human RBCs are enucleate. Which of the following statement(s) is/are most appropriate explanation for this feature?

- **(a)** They do not need to reproduce
- **(b)** They are somatic cells
- **(c)** They do not metabolize
- **(d)** All their internal space is available for oxygen transport

- (1) (a), (c) and (d)
- (2) (b) and (c)
- **(3)** Only (d)
- (4) Only (a)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In Human RBCs, nucleus degenerates during maturation which provide more space for oxygen carrying pigment (Haemoglobin).
2. It lacks most of the cell organelles including mitochondria so respires anaerobically.

**Solved independently** (answer withheld)

1. Statement (c) is false: mature RBCs still metabolise glucose by anaerobic glycolysis to make ATP.
2. Statement (b) does not explain the feature: almost all other somatic cells keep their nucleus.
3. Statement (a) is at most a consequence of losing the nucleus, not the adaptive reason for it.
4. Statement (d) is the adaptive explanation: without a nucleus the cell holds more haemoglobin, so more $\mathrm{O_2}$ can be carried.
5. Only (d) is the most appropriate explanation, which is option $3$.

**Subtopic:** Formed Elements And Their Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q095_c5136c19_30102026.png?v=c5136c197380)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q095_23e1f15c_30102026.png?v=23e1f15c81c4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The mature red blood cell loses its nucleus so that the whole of its interior is free for haemoglobin and oxygen carriage
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Having no nucleus means the cell cannot divide, and that consequence is then read back as the cause, so 'they do not need to reproduce' is picked as the explanation; the arrow runs the other way, and the explanation the question wants is the space the missing nucleus frees for oxygen transport.
- **Why:** This question requires the reason a stated feature exists rather than a check on four separate facts, demonstrated by the stem 'Which of the following statement(s) is/are most appropriate explanation for this feature?'.
- **Note:** negative_words_seen records 'NOT', but the only negatives are inside the lettered statements ('do not need to reproduce', 'do not metabolize'); the task itself is direct.
<!--/ecat-->

## Q96

Biology · zoology · Neural Control and Coordination

Myelin sheath is produced by

- (1) Oligodendrocytes and Osteoclasts
- (2) Osteoclasts and Astrocytes
- **(3)** Schwann Cells and Oligodendrocytes
- (4) Astrocytes and Schwann Cells

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Oligodendrocytes are neuroglial cells which produce myelin sheath in central nervous system while Schwann cell produces myelin sheath in peripheral nervous system.

**Solved independently** (answer withheld)

1. Myelin sheath is made by Schwann cells around peripheral axons and by oligodendrocytes around central axons, while osteoclasts (bone-resorbing cells) and astrocytes (supporting glia) make no myelin, so the pair is Schwann cells and oligodendrocytes, which is option $3$.

**Subtopic:** Neuron as Structural and Functional Unit of Neural System and Types of Axon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q096_068f8638_30102026.png?v=068f8638db67)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q096_5d76439c_30102026.png?v=5d76439cf68e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Myelin is laid down by two different glial cells: Schwann cells around peripheral axons and oligodendrocytes around central ones
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Schwann cells are the myelinating cell fixed first, and astrocytes are the glial cell of the CNS named most often, so the pair reads as one cell for the nerves and one for the brain; astrocytes support and nourish neurons and lay down no myelin.
- **Why:** This question requires the stated fact about which two glial cells produce myelin, demonstrated by the stem 'Myelin sheath is produced by' with each option printing a pair of named cells and no criterion to apply.
- **Note:** Each option is a pair of cell names accepted or rejected whole, which the rulebook's E1 axis calls pair_options. The qtype axis has no pair value, and the stem prints no lettered list and no instruction to judge statements, so the shape is recorded as mcq and the pair structure flagged here.
<!--/ecat-->

## Q97

Biology · zoology · Excretory Products and Their Elimination

Which of the following statements is correct?

- (1) The ascending limb of loop of Henle is permeable to water
- (2) The descending limb of loop of Henle is permeable to electrolytes
- **(3)** The ascending limb of loop of Henle is impermeable to water
- (4) The descending limb of loop of Henle is impermeable to water

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Descending limb of loop of Henle is permeable to water but impermeable to electrolytes while ascending limb is impermeable to water but permeable to electrolytes.

**Solved independently** (answer withheld)

1. NCERT: the descending limb of the loop of Henle is permeable to water but almost impermeable to electrolytes, which rules out options $2$ and $4$; the ascending limb is impermeable to water but allows active or passive transport of electrolytes, which rules out option $1$ and makes option $3$ correct.

**Subtopic:** Function of the Tubules and their types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q097_3ca4815d_30102026.png?v=3ca4815d0e9a)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q097_8e40e9b5_30102026.png?v=8e40e9b5dc1b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The two limbs of the loop of Henle have opposite permeabilities: water leaves the descending limb, while the ascending limb lets out electrolytes but not water
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  'Impermeable to water' is the half of the pair that stays in memory, and hanging it on the descending limb inverts the pair, because water is exactly what does leave the descending limb and exactly what cannot cross the ascending one.
- **Why:** This question requires the stated fact about each limb's permeability, demonstrated by the four options printing the same two limbs crossed with 'permeable' and 'impermeable'.
<!--/ecat-->

## Q98

Biology · both · Molecular Basis of Inheritance

During DNA replication, Okazaki fragments are used to enlongate

- (1) The leading strand away from replication fork
- **(2)** The lagging strand away from the replication fork
- (3) The leading strand towards replication fork
- (4) The lagging strand towards replication fork

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Two DNA polymerase molecules work simultaneous at the DNA fork, one on the leading strand and the other on the lagging strand.
2. Each Okazaki fragment is synthesized by DNA polymerase at lagging strand in $5' \rightarrow 3'$ direction.
3. New Okazaki fragments appear as the replication fork opens further.
4. As the first Okazaki fragment appears away from the replication fork, the direction of elongation would be away from replication fork.

**Solved independently** (answer withheld)

1. DNA polymerase can add nucleotides only in the $5' \rightarrow 3'$ direction.
2. On the template with polarity $3' \rightarrow 5'$ the new strand (leading) grows continuously towards the replication fork, so Okazaki fragments are not used there.
3. On the other template ($5' \rightarrow 3'$) the new strand (lagging) is made discontinuously as short Okazaki fragments, each synthesised $5' \rightarrow 3'$, i.e. away from the replication fork, and later joined by DNA ligase.
4. So Okazaki fragments elongate the lagging strand away from the replication fork, which is option $2$.

**Subtopic:** The Machinery and the Enzymes of Replication · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q098_2a33d53f_30102026.png?v=2a33d53feb1b)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q098_9535126f_30102026.png?v=9535126fa5ba)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Okazaki fragments are the short pieces of the discontinuously built lagging strand, and each one is laid down in the direction away from the advancing replication fork
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Okazaki fragments are correctly pinned to the lagging strand, and the direction is then filled in from the picture of synthesis chasing the fork; because the lagging strand's template runs the wrong way for continuous building, its fragments are in fact laid down away from the fork.
- **Why:** This question requires the stated fact about which strand Okazaki fragments build and in which direction, demonstrated by the options crossing 'leading' and 'lagging' with 'towards' and 'away from' the replication fork.
- **Note:** E1's pattern returned statement_options, but the stem 'During DNA replication, Okazaki fragments are used to enlongate' is a sentence to be completed, not an instruction to judge statements, so the shape recorded is mcq; long option sentences alone do not make a question statements. The stem as stored also prints 'enlongate' for 'elongate'.
<!--/ecat-->

## Q99

Biology · both · Biomolecules

Which one of the following statements is correct, with reference to enzymes?

- (1) Coenzyme = Apoenzyme + Holoenzyme
- (2) Holoenzyme = Coenzyme + Cofactor
- (3) Apoenzyme = Holoenzyme + Coenzyme
- **(4)** Holoenzyme = Apoenzyme + Coenzyme

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Holoenzyme is conjugated enzyme in which protein part is apoenzyme while non-protein is cofactor.
2. Coenzyme are also organic compounds but their association with apoenzyme is only transient and serve as cofactors.

**Solved independently** (answer withheld)

1. The protein part of a conjugated enzyme is the apoenzyme and the organic non-protein part is the coenzyme; together they form the active holoenzyme, $\text{Holoenzyme} = \text{Apoenzyme} + \text{Coenzyme}$, which is option $4$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q099_0d937476_30102026.png?v=0d93747643b3)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q099_30c86839_30102026.png?v=30c86839f20b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The holoenzyme is the complete working enzyme: the protein apoenzyme plus its non-protein coenzyme
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The three names are remembered as belonging to one equation, and the apoenzyme, being the protein bulk, is taken for the whole; that puts the holoenzyme on the right of the equals sign as a part of one of its own parts.
- **Why:** This question requires the stated definition of which enzyme term is the whole and which are its parts, demonstrated by 'Holoenzyme = Apoenzyme + Coenzyme' being one of four permutations of the same names.
- **Note:** The options are printed as equations rather than as sentences, but the stem reads 'Which one of the following statements is correct, with reference to enzymes?', which is what puts the shape at statements.
<!--/ecat-->

## Q100

Biology · both · Biotechnology: Principles and Processes

DNA fragments are

- (1) Neutral
- (2) Either positively or negatively charged depending on their size
- (3) Positively charged
- **(4)** Negatively charged

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. DNA fragments are negatively charged because of phosphate group.

**Solved independently** (answer withheld)

1. The phosphate groups in the sugar-phosphate backbone give DNA fragments a net negative charge, whatever their size, so they move toward the anode in gel electrophoresis; this is option $4$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q100_ecdaaa21_30102026.png?v=ecdaaa217d22)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q100_d8c105ac_30102026.png?v=d8c105ac5a33)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Every DNA fragment carries a negative charge from its phosphate backbone, which is why an electric field can pull it through a gel
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Size is the word carried out of this subtopic, because the sentence printed beside the charge one says the fragments resolve according to size; size settles how far a fragment travels, not the sign of its charge, which is negative on every fragment.
- **Why:** This question requires the stated fact that DNA fragments carry a negative charge, demonstrated by the bare stem 'DNA fragments are' with charge signs as the four options.
<!--/ecat-->

## Q101

Biology · both · Biotechnology: Principles and Processes

The DNA fragments separated on an agarose gel can be visualised after staining with

- (1) Aniline blue
- **(2)** Ethidium bromide
- (3) Bromophenol blue
- (4) Acetocarmine

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Ethidium bromide is used to stain the DNA fragments and will appear as orange coloured bands under UV light.

**Solved independently** (answer withheld)

1. Separated DNA fragments on an agarose gel are stained with ethidium bromide and, on exposure to UV radiation, show up as bright orange bands, which is option $2$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q101_31cbb96f_30102026.png?v=31cbb96fc758)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q101_5e9d8f45_30102026.png?v=5e9d8f450dcc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** DNA separated on an agarose gel is made visible by staining with ethidium bromide and viewing under ultraviolet light
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Bromophenol blue is the other dye belonging to a gel run, going into the loading buffer so the sample's front can be watched, so a dye remembered from the bench lands here; it marks the migrating front and neither binds DNA nor fluoresces under ultraviolet light.
- **Why:** This question requires the material used at the visualising step of a named bench procedure, demonstrated by the stem 'separated on an agarose gel can be visualised after staining with' and by all four options being real laboratory stains. The nearby_fact against look_alike_term test applied was the swap test: replace 'Bromophenol blue' with an unlike dye name and the pull survives, because what carries the student is that the dye belongs to the same gel step, so it is nearby_fact even though both names carry 'brom'.
<!--/ecat-->

## Q102

Biology · botany · Biological Classification

Which among the following are the smallest living cells, known without a definite cell wall, pathogenic to plants as well as animals and can survive without oxygen?

- **(1)** Mycoplasma
- (2) Nostoc
- (3) Bacillus
- (4) Pseudomonas

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Mycoplasmas are smallest, wall-less prokaryotes, pleomorphic in nature.
2. These are pathogenic on both plants and animals.

**Solved independently** (answer withheld)

1. Mycoplasma lack a cell wall, are the smallest known living cells, can survive without oxygen and cause disease in plants and animals; Nostoc (cyanobacterium), Bacillus and Pseudomonas all have cell walls, so the answer is option $1$.

**Subtopic:** Archaebacteria & Mycoplasma · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q102_dc295175_30102026.png?v=dc2951754f3a)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q102_5de2e613_30102026.png?v=5de2e6132144)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Mycoplasma are the smallest living cells known, they lack a cell wall altogether, they survive without oxygen and they cause disease in both plants and animals
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Pseudomonas is the bacterium printed as the denitrifier that keeps respiring on nitrate when oxygen runs out, so a student who scans the stem for the one clause they can place — "can survive without oxygen" — matches it there and stops
- **Why:** This question requires the set of statements NCERT prints about one named genus, demonstrated by the stem reproducing them as its own clauses — "smallest living cells", "without a definite cell wall", "can survive without oxygen".
<!--/ecat-->

## Q103

Biology · botany · Sexual Reproduction in Flowering Plants

The morphological nature of the edible part of coconut is

- **(1)** Endosperm
- (2) Pericarp
- (3) Perisperm
- (4) Cotyledon

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Coconut has double endosperm with liquid endosperm and cellular endosperm.

**Solved independently** (answer withheld)

1. In coconut the edible tender water is free-nuclear endosperm and the surrounding white kernel is cellular endosperm, so the edible part is $\text{endosperm}$, which is option $1$.

**Subtopic:** Post-Fertilisation: Structures, Events and Endosperm · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q103_1972d5c7_30102026.png?v=1972d5c7515a)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q103_b62839bc_30102026.png?v=b62839bc397d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The white kernel and the water of a coconut are both endosperm — cellular and free-nuclear respectively — so the edible part is endosperm, not fruit wall and not cotyledon
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Perisperm differs from endosperm by one syllable and is printed in the same post-fertilisation paragraph, so a student who has the two storage words in one bundle takes the one they half-recall as the persistent food tissue
- **Why:** This question requires the stated identity of one named structure, demonstrated by the stem asking for "the morphological nature of the edible part of coconut" and the four options naming four different tissues of fruit and seed.
<!--/ecat-->

## Q104

Biology · zoology · Structural Organisation in Animals

Select the correct route for the passage of sperms in male frogs :

- (1) Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Bidder's canal $\rightarrow$ Ureter $\rightarrow$ Cloaca
- **(2)** Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Bidder's canal $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca
- (3) Testes $\rightarrow$ Bidder's canal $\rightarrow$ Kidney $\rightarrow$ Vasa efferentia $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca
- (4) Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Seminal Vesicle $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In male frog the sperms will move from
2. Testes $\rightarrow$ Vasa efferentia $\rightarrow$ Kidney $\rightarrow$ Bidder’s canal $\rightarrow$ Urinogenital duct $\rightarrow$ Cloaca.

**Solved independently** (answer withheld)

1. Vasa efferentia arise from the testes and enter the kidney, where they open into Bidder's canal; Bidder's canal communicates with the urinogenital duct, which opens into the cloaca, so the route is $\text{Testes} \rightarrow \text{Vasa efferentia} \rightarrow \text{Kidney} \rightarrow \text{Bidder's canal} \rightarrow \text{Urinogenital duct} \rightarrow \text{Cloaca}$, which is option $2$.

**Subtopic:** Anatomy of Frog · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q104_957173c7_30102026.png?v=957173c705fa)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q104_6fb57927_30102026.png?v=6fb579279bff)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** In a male frog sperm leave the testes by the vasa efferentia into the kidney, collect in Bidder's canal, and leave through the urinogenital duct to the cloaca
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Option 4 reproduces the first three links and the last two exactly and swaps only Bidder's canal for a seminal vesicle, so a student who imports the human route — vas deferens, seminal vesicle, urethra — onto the frog finds a chain in which every other name is where they expect it
- **Why:** This question requires the printed sequence of ducts to be reproduced in order, demonstrated by the stem asking for "the correct route for the passage of sperms" and each option printing the same organs chained by arrows.
- **Note:** The pattern classifier returned null and described the options as reactions; what is printed is four arrow-chains of organ names, so the shape is a plain four-option question and the order information is carried by asks: order.
<!--/ecat-->

## Q105

Biology · botany · Anatomy of Flowering Plants

Identify the wrong statement in context of heartwood.

- **(1)** It conducts water and minerals efficiently
- (2) It comprises dead elements with highly lignified walls
- (3) Organic compounds are deposited in it
- (4) It is highly durable

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Heartwood is physiologically inactive due to deposition of organic compounds and tyloses formation, so this will not conduct water and minerals.

**Solved independently** (answer withheld)

1. Heartwood (duramen) is the dark central secondary xylem whose cells are dead with highly lignified walls, and organic compounds such as tannins, resins, oils and gums are deposited in it, which makes it durable and resistant to microbes and insects; it does not conduct water and minerals (sapwood does), so the wrong statement is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q105_a4379b78_30102026.png?v=a4379b7828ba)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q105_c22aa15b_30102026.png?v=c22aa15bb1b8)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Heartwood is dead, lignified, deposit-filled wood that gives mechanical support and durability; the conducting of water and minerals is the sapwood's job
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Option 2 is the book's own description of heartwood, so a student reading for the statement that best fits heartwood ticks it and answers "which statement is correct" instead of the question printed, which asks for the wrong one
- **Why:** This question requires three printed properties of heartwood to be graded against the book's line, demonstrated by the stem reading "Identify the wrong statement in context of heartwood" with each option a full claim about it.
<!--/ecat-->

## Q106

Biology · zoology · Human Health and Disease

Transplantation of tissues/organs fails often due to non-acceptance by the patient's body. Which type of immune-response is responsible for such rejections?

- (1) Hormonal immune response
- (2) Physiological immune response
- (3) Autoimmune response
- **(4)** Cell-mediated immune response

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Non-acceptance or rejection of graft or transplanted tissues/organs is due to cell mediated immune response.

**Solved independently** (answer withheld)

1. The body's ability to tell 'self' from 'non-self' tissue, which leads to graft rejection, is a function of the cell-mediated immune response (T-lymphocytes), which is option $4$.

**Subtopic:** Acquired Immunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q106_eafd6402_30102026.png?v=eafd640269cf)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q106_ac6cc912_30102026.png?v=ac6cc912f6c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A graft is rejected by the cell-mediated immune response, the T-cell arm that recognises non-self tissue; the antibody arm is called humoral, not hormonal
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The printed partner of cell-mediated immunity is the humoral response, and "hormonal" is one letter-cluster away from it, so a student who holds the two-arm split but reads the option as the word they learnt takes the antibody arm by mistake
- **Why:** This question requires the stated fact about which arm of acquired immunity rejects a graft, demonstrated by the stem asking "Which type of immune-response is responsible for such rejections?" with four response names as options.
<!--/ecat-->

## Q107

Biology · botany · Biodiversity and Conservation

The region of Biosphere Reserve which is legally protected and where no human activity is allowed is known as

- (1) Transition zone
- (2) Restoration zone
- **(3)** Core zone
- (4) Buffer zone

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Biosphere reserve is protected area with multipurpose activities.
2. It has three zones
3. (a) Core zone – without any human interference
4. (b) Buffer zone – with limited human activity
5. (c) Transition zone – human settlement, grazing cultivation etc., are allowed.

**Solved independently** (answer withheld)

1. A biosphere reserve has a legally protected $\text{core zone}$ where no human activity is allowed, surrounded by a $\text{buffer zone}$ (limited activity) and an outer $\text{transition zone}$ (human settlement), so the answer is option $3$.

**Subtopic:** In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q107_ee093eda_30102026.png?v=ee093eda76f6)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q107_da32ebd0_30102026.png?v=da32ebd0a0de)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A biosphere reserve is zoned from the inside out — the core zone is legally protected and closed to human activity, the buffer allows limited use, the transition zone carries settlement and cropping
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The buffer zone is the ring printed immediately around the core in the same zoning scheme, and a student who reads "buffer" as the part that shields the reserve concludes it is the protected one
- **Why:** This question requires the stated definition of one zone in the reserve's zoning scheme, demonstrated by the stem printing its two criteria — "legally protected" and "no human activity is allowed" — against four zone names.
<!--/ecat-->

## Q108

Biology · zoology · Principles of Inheritance and Variation

Thalassemia and sickle cell anemia are caused due to a problem in globin molecule synthesis. Select the correct statement.

- **(1)** Thalassemia is due to less synthesis of globin molecules
- (2) Sickle cell anemia is due to a quantitative problem of globin molecules
- (3) Both are due to a qualitative defect in globin chain synthesis
- (4) Both are due to a quantitative defect in globin chain synthesis

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Thalassemia differs from sickle-cell anaemia in that the former is a quantitative problem of synthesising too few globin molecules while the latter is a qualitative problem of synthesising an incorrectly functioning globin.

**Solved independently** (answer withheld)

1. Thalassemia is a quantitative problem: too few globin chains are synthesised, while sickle-cell anaemia is a qualitative problem: a single substitution $\text{Glu} \rightarrow \text{Val}$ at position 6 of the $\beta$-globin chain; so options 2, 3 and 4 are false and option $1$ (less synthesis of globin in thalassemia) is correct.

**Subtopic:** Thalassemia, Sickle-cell Anaemia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q108_2eae4377_30102026.png?v=2eae43775f2d)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q108_fea58747_30102026.png?v=fea587474d5f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Thalassemia is a quantitative defect, too few globin chains being made, while sickle cell anaemia is a qualitative one, a normal amount of a faulty chain
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The pair of words is held without which disorder owns which, so 'quantitative' is attached to sickle cell anaemia, where the single amino-acid substitution makes a faulty chain rather than fewer chains
- **Why:** This question requires a quantitative defect to be separated from a qualitative one in globin synthesis, demonstrated by option 1's 'Thalassemia is due to less synthesis of globin molecules' standing against option 2's 'Sickle cell anemia is due to a quantitative problem of globin molecules'.
<!--/ecat-->

## Q109

Biology · botany · Sexual Reproduction in Flowering Plants

Flowers which have single ovule in the ovary and are packed into inflorescence are usually pollinated by

- **(1)** Wind
- (2) Bat
- (3) Water
- (4) Bee

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Wind pollination or anemophily is favoured by flowers having a single ovule in each ovary, and numerous flowers packed in an inflorescence.
2. Wind pollination is a non-directional pollination.

**Solved independently** (answer withheld)

1. Wind pollination is non-directional, so plants that use it produce many flowers, each with a single ovule in the ovary, packed into an inflorescence (e.g. the corn cob); these traits describe anemophily, which is option $1$ (Wind).

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q109_51cb78d9_30102026.png?v=51cb78d9e9f3)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q109_8cb9c84f_30102026.png?v=8cb9c84f9f75)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Wind-pollinated flowers are small and non-showy, with a single ovule in each ovary and many flowers crowded into one inflorescence, the corn cob being the printed example
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Insect pollination is the case the chapter develops at length, so 'packed into inflorescence' is read as a cluster advertising itself to a bee and the single-ovule clue is passed over
- **Why:** This question requires the stated trait list of one pollinating agent, demonstrated by the stem's 'single ovule in the ovary and are packed into inflorescence'.
- **Note:** Swap test on the trap label: replacing 'Bee' with any other animal pollinator leaves the pull intact, because what carries it is the insect-pollination trait list printed beside the wind one, not any resemblance between the words. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q110

Biology · zoology · Animal Kingdom

An important characteristic that Hemichordates share with Chordates is

- **(1)** Pharynx with gill slits
- (2) Pharynx without gill slits
- (3) Absence of notochord
- (4) Ventral tubular nerve cord

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Pharyngeal gill slits are present in hemichordates as well as in chordates.
2. Notochord is present in chordates only.
3. Ventral tubular nerve cord is characteristic feature of non-chordates.

**Solved independently** (answer withheld)

1. The fundamental features of chordates are a notochord, a dorsal hollow (tubular) nerve cord and paired pharyngeal gill slits.
2. Hemichordates have a pharynx with gill slits, so they share this chordate feature (option $1$).
3. Option $2$ (pharynx without gill slits) is wrong, since hemichordates do have gill slits; option $3$ (absence of notochord) is a non-chordate trait, not a shared chordate feature; option $4$ (ventral tubular nerve cord) is a non-chordate feature, as chordates have a dorsal nerve cord.
4. So the shared characteristic is pharynx with gill slits, which is option $1$.

**Subtopic:** Phylum – Echinodermata and Hemichordata, Phylum – Chordata · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q110_65a665f0_30102026.png?v=65a665f0ddce)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q110_4d9d1236_30102026.png?v=4d9d12365aa1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hemichordates have a pharynx with gill slits, the one chordate feature they share; the notochord and the dorsal hollow nerve cord they do not
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  'Absence of notochord' is a true statement about hemichordates and is the very point on which they are kept out of Chordata, so it is picked for a stem that asked what the two groups share
- **Why:** This question requires the stated feature held in common by two phyla, demonstrated by the stem's 'An important characteristic that Hemichordates share with Chordates'.
<!--/ecat-->

## Q111

Biology · both · Cell Cycle and Cell Division

Which of the following options gives the correct sequence of events during mitosis?

- (1) Condensation $\rightarrow$ crossing over $\rightarrow$ nuclear membrane disassembly $\rightarrow$ segregation $\rightarrow$ telophase
- (2) Condensation $\rightarrow$ arrangement at equator $\rightarrow$ centromere division $\rightarrow$ segregation $\rightarrow$ telophase
- (3) Condensation $\rightarrow$ nuclear membrane disassembly $\rightarrow$ crossing over $\rightarrow$ segregation $\rightarrow$ telophase
- **(4)** Condensation $\rightarrow$ nuclear membrane disassembly $\rightarrow$ arrangement at equator $\rightarrow$ centromere division $\rightarrow$ segregation $\rightarrow$ telophase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct sequence of events during mitosis would be as follows
2. (i) Condensation of $\mathrm{DNA}$ so that chromosomes become visible occurs during early to mid-prophase.
3. (ii) Nuclear membrane disassembly begins at late prophase or transition to metaphase.
4. (iii) Arrangement of chromosomes at equator occurs during metaphase, called congression.
5. (iv) Centromere division or splitting occurs during anaphase forming daughter chromosomes.
6. (v) Segregation also occurs during anaphase as daughter chromosomes separate and move to opposite poles.
7. (vi) Telophase leads to formation of two daughter nuclei.

**Solved independently** (answer withheld)

1. Crossing over happens only in prophase I of meiosis, not in mitosis, so options $1$ and $3$ are wrong.
2. In prophase chromatin condenses into chromosomes; by the end of prophase the nuclear envelope disassembles.
3. In metaphase chromosomes align at the equator (metaphase plate).
4. In anaphase centromeres split and sister chromatids segregate to opposite poles, followed by telophase.
5. So the sequence is condensation $\rightarrow$ nuclear membrane disassembly $\rightarrow$ arrangement at equator $\rightarrow$ centromere division $\rightarrow$ segregation $\rightarrow$ telophase, which is option $4$ (option $2$ omits nuclear membrane disassembly).

**Subtopic:** Prophase and Metaphase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q111_baee1b17_30102026.png?v=baee1b17e0dd)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q111_335e535d_30102026.png?v=335e535d2a09)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Mitotic prophase ends with the nuclear envelope disassembling, metaphase lines the chromosomes at the equator, anaphase splits the centromeres and segregates them, and crossing over belongs to meiosis
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Every event in option 2 is a genuine mitotic event in the right relative order, so the sequence is accepted on its order alone and the missing nuclear-envelope step is not looked for
- **Why:** This question requires the ordered events of mitosis, demonstrated by option 4 carrying 'nuclear membrane disassembly, arrangement at equator, centromere division' where option 2 drops the envelope step.
- **Note:** E1 read this as arrange_in_order, which category_retired.qtype maps onto mcq; the sequencing is carried on the asks axis as order. The crossing-over device, a meiotic event moved into a mitotic list, sits in options 1 and 3, but it splits across two options so no single option dominates for it; the named trap is therefore option 2, the one option that looks like a complete mitotic sequence with a step missing.
<!--/ecat-->

## Q112

Biology · both · Molecular Basis of Inheritance

The final proof for DNA as the genetic material came from the experiments of

- (1) Avery, Mcleod and McCarty
- (2) Hargobind Khorana
- (3) Griffith
- **(4)** Hershey and Chase

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Hershey and Chase gave unequivocal proof which ended the debate between protein and $\mathrm{DNA}$ as genetic material.

**Solved independently** (answer withheld)

1. Griffith showed transformation, Avery, MacLeod and McCarty identified DNA as the transforming principle, but the final, unequivocal proof came from Hershey and Chase (1952), whose $^{32}\mathrm{P}$-labelled phage DNA (not $^{35}\mathrm{S}$-labelled protein) entered bacteria, which is option $4$.

**Subtopic:** DNA vs RNA & Genetic Material is DNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q112_1f331887_30102026.png?v=1f331887c012)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q112_b76fa8f7_30102026.png?v=b76fa8f7737d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hershey and Chase's labelling of phage DNA and protein gave the unequivocal proof that DNA is the genetic material, while Avery, MacLeod and McCarty had earlier shown the transforming principle to be DNA
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Avery, MacLeod and McCarty is held as 'the DNA proof' and is the experiment printed immediately before the phage work, so the stem's word 'final' is passed over
- **Why:** This question requires one attribution as the chapter states it, demonstrated by the stem's 'The final proof for DNA as the genetic material'.
- **Note:** Swap test on the trap label: replacing 'Avery, Mcleod and McCarty' with an unlike set of names leaves the pull, because what carries it is the experiment's position immediately before Hershey and Chase in the printed sequence, not any resemblance between the names. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q113

Biology · both · Biotechnology: Principles and Processes

What is the criterion for DNA fragments movement on agarose gel during gel electrophoresis?

- (1) Positively charged fragments move to farther end
- (2) Negatively charged fragments do not move
- (3) The larger the fragment size, the farther it moves
- **(4)** The smaller the fragment size, the farther it moves

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. During gel electrophoresis, DNA fragments separate (resolve) according to their size through sieving effect provided by agarose gel.

**Solved independently** (answer withheld)

1. DNA fragments are negatively charged and move towards the anode, so options $1$ and $2$ are wrong. The agarose gel acts as a sieve and separates fragments by size, so smaller fragments move farther, which is option $4$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q113_9e219704_30102026.png?v=9e2197048595)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q113_442d9346_30102026.png?v=442d93465e9e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The agarose meshwork sieves DNA, so the smaller a fragment is the farther it travels from the well
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The sieving relation is remembered as a relation between size and distance with the sense inverted, so the larger fragment is made to travel farther
- **Why:** This question requires the stated criterion for migration on agarose, demonstrated by option 4's 'The smaller the fragment size, the farther it moves' against option 3's inversion of it.
- **Note:** E1's pattern read full-sentence options as statement_options. The stem is a direct question, 'What is the criterion for DNA fragments movement...', with no statement block and no lettered list, so on the current axis the printed shape is mcq rather than statements.
<!--/ecat-->

## Q114

Biology · botany · Photosynthesis in Higher Plants

With reference to factors affecting the rate of photosynthesis, which of the following statements is not correct?

- **(1)** $\mathrm{C_3}$ plants responds to higher temperatures with enhanced photosynthesis while $\mathrm{C_4}$ plants have much lower temperature optimum
- (2) Tomato is a greenhouse crop which can be grown in $\mathrm{CO_2}$ - enriched atmosphere for higher yield
- (3) Light saturation for $\mathrm{CO_2}$ fixation occurs at $10\%$ of full sunlight
- (4) Increasing atmospheric $\mathrm{CO_2}$ concentration upto $0.05\%$ can enhance $\mathrm{CO_2}$ fixation rate

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In $\mathrm{C_3}$ plants photosynthesis is decreased at higher temperature due to increased photorespiration.
2. $\mathrm{C_4}$ plants have higher temperature optimum because of the presence of pyruvate phosphate dikinase enzyme, which is sensitive to low temperature.

**Solved independently** (answer withheld)

1. Option $1$ swaps the plant types: it is $\mathrm{C_4}$ plants that respond to higher temperatures with more photosynthesis, while $\mathrm{C_3}$ plants have a much lower temperature optimum, so option $1$ is not correct.
2. Option $2$ is correct: greenhouse crops such as tomato are grown in $\mathrm{CO_2}$-enriched air for higher yield.
3. Option $3$ is correct: light saturation for $\mathrm{CO_2}$ fixation occurs at about $10\%$ of full sunlight.
4. Option $4$ is correct: raising atmospheric $\mathrm{CO_2}$ up to about $0.05\%$ increases the $\mathrm{CO_2}$ fixation rate.
5. The statement that is not correct is option $1$.

**Subtopic:** Factors Affecting Photosynthesis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q114_d65a191a_30102026.png?v=d65a191aa317)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q114_7e08d212_30102026.png?v=7e08d212fbf2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** C4 plants, not C3, respond to higher temperatures with a higher rate of photosynthesis; the chapter's other limiting-factor figures are light saturation at 10 per cent of full sunlight and a useful CO2 rise up to 0.05 per cent
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  'High CO2 damages the plant' is remembered without the ceiling it is stated against, so an option saying a rise up to 0.05 per cent enhances fixation is marked as the incorrect one
- **Why:** This question requires four printed statements about limiting factors to be checked one by one, demonstrated by option 1 swapping the groups in 'C3 plants responds to higher temperatures with enhanced photosynthesis while C4 plants have much lower temperature optimum'.
- **Note:** The key here is the one statement that is false, so the trap necessarily sits on a statement that is true: options 2, 3 and 4 are all the chapter's own lines, and the one named is the option whose stated limit can be dropped.
<!--/ecat-->

## Q115

Biology · zoology · Evolution

Artificial selection to obtain cows yielding higher milk output represents

- (1) Disruptive as it splits the population into two one yielding higher output and the other lower output
- (2) Stabilizing followed by disruptive as it stabilizes the population to produce higher yielding cows
- (3) Stabilizing selection as it stabilizes this character in the population
- **(4)** Directional as it pushes the mean of the character in one direction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Artificial selection to obtain cow yielding higher milk output will shift the peak to one direction, hence, will be an example of Directional selection.
2. In stabilizing selection, the organisms with the mean value of the trait are selected.
3. In disruptive selection, both extremes get selected.

**Solved independently** (answer withheld)

1. Artificial selection for higher milk output keeps only the cows at the high-yield end of the distribution for breeding, so the population mean of the trait moves in one direction, which is directional selection ($\text{option } 4$).

**Subtopic:** Types of Natural Selection · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q115_807155b6_30102026.png?v=807155b61140)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q115_e29b8e4a_30102026.png?v=e29b8e4a07e9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Breeding for ever higher milk yield shifts the population mean one way, which is directional selection; stabilising selection holds the mean and disruptive selection favours both extremes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A breeding programme that fixes a character in a herd is heard as a population being stabilised, so the mode whose name carries that word is taken
- **Why:** This question requires the taught definitions of the selection modes carried onto a breeding case, demonstrated by option 4's 'Directional as it pushes the mean of the character in one direction'.
- **Note:** E1's pattern read the justified options as statement_options; the stem is a lead-in ('Artificial selection ... represents') with no statement block and no lettered list, so the printed shape on the current axis is mcq. Swap test on the trap label: renaming 'Stabilizing' to an unlike word leaves the pull, which comes from its place in the printed trio of selection modes, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q116

Biology · botany · Microbes in Human Welfare

> ⚠ The booklet lost this question's number and first line. The opening "Which of the following in sewage treatment removes" is restored word for word from Code A q176, Code B q118, Code C q72 (same exam).

Which of the following in sewage treatment removes suspended solids?

- **(1)** Primary treatment
- (2) Sludge treatment
- (3) Tertiary treatment
- (4) Secondary treatment

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Primary treatment is a physical process which involves sequential filtration and sedimentation.

**Solved independently** (answer withheld)

1. Primary treatment of sewage physically removes large and small particles by sequential filtration and sedimentation, so the suspended solids settle out as primary sludge; this is option $1$.

**Subtopic:** Microbes in Sewage Treatment · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 22)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q116_b74b65cb_30102026.png?v=b74b65cb7f65)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q116_b6c98e14_30102026.png?v=b6c98e1492c3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Primary treatment is the physical stage, filtration and then sedimentation taking out the grit and the suspended solids; secondary treatment is the biological stage that works on the dissolved organic matter
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Secondary treatment is the stage the chapter describes at length, and the flocs settling in its settling tank are read as the solids being taken out
- **Why:** This question requires the stated work of one named stage, demonstrated by the stem's 'in sewage treatment removes suspended solids'.
- **Note:** Swap test on the trap label: renaming 'Secondary treatment' leaves the pull, because what carries it is its position as the adjacent, more fully described stage of the same printed sequence, not any resemblance to 'Primary treatment'. So nearby_fact.
<!--/ecat-->

## Q117

Biology · both · Molecular Basis of Inheritance

Spliceosomes are not found in cells of

- (1) Animals
- **(2)** Bacteria
- (3) Plants
- (4) Fungi

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Spliceosomes are used in removal of introns during post-transcriptional processing of hnRNA in eukaryotes only as split genes are absent as prokaryotes.

**Solved independently** (answer withheld)

1. Spliceosomes remove introns from eukaryotic hnRNA; prokaryotes such as bacteria have no split genes (no introns) and hence no spliceosomes, while animals, plants and fungi are eukaryotes, so the answer is option $2$.

**Subtopic:** Transcription · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q117_04fd2ad6_30102026.png?v=04fd2ad60433)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q117_006598b5_30102026.png?v=006598b58020)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Split genes and the spliceosome are eukaryotic; a bacterial gene carries no introns, so there is nothing for a spliceosome to remove
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option: animals, plants and fungi are three eukaryotic kingdoms, all equally spliceosome-bearing, so no printed fact separates one from another, and the stem's 'not' is the only device in the question but lands on all three alike, which leaves no one option to name
- **Why:** This question requires the stated distribution of spliceosomes, demonstrated by three options naming eukaryotic kingdoms and only 'Bacteria' naming a prokaryote.
- **Note:** Recorded as no_trap rather than left blank: the device is the task's 'not', and it has three equally true landing places. Naming one of the three eukaryote options would mean inventing a reason to prefer one kingdom over the others, which the printed question does not supply. A reviewer should check whether the printed paper emphasised the 'not', since that is the only thing this question turns on.
<!--/ecat-->

## Q118

Biology · botany · Sexual Reproduction in Flowering Plants

Functional megaspore in an angiosperm develops into

- **(1)** Embryo sac
- (2) Embryo
- (3) Ovule
- (4) Endosperm

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Megaspore is the first cell of female gametophytic generation in angiosperm.
2. It undergoes three successive generations of free nuclear mitosis to form 8-nucleated and 7-celled embryo sac.

**Solved independently** (answer withheld)

1. The megaspore mother cell divides by meiosis to give four megaspores, and only one of them stays functional.
2. The nucleus of the functional megaspore goes through $3$ free-nuclear mitotic divisions, giving $2^3 = 8$ nuclei, which become organised into a $7$-celled, $8$-nucleate structure: the female gametophyte, or embryo sac, which is option $1$.

**Subtopic:** Megasporangium (Ovule) and Embryo Sac · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q118_fbd479b1_30102026.png?v=fbd479b19dd7)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q118_1216be72_30102026.png?v=1216be728d28)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The functional megaspore enlarges into the female gametophyte, the seven-celled and eight-nucleate embryo sac, inside the ovule
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  'Embryo' is taken as the short form of 'embryo sac', so the half-remembered word is matched to an option without the rest of the name being checked
- **Why:** This question requires the stated product of one named cell, demonstrated by the stem's 'Functional megaspore in an angiosperm develops into'.
- **Note:** Swap test on the trap label: if option 2 read 'Zygote' instead of 'Embryo' the pull would go, since nothing else about it fits the megaspore. The resemblance to the right answer's own words is doing the work, so look_alike_term rather than nearby_fact, even though the three wrong options are all stages of the same printed sequence.
<!--/ecat-->

## Q119

Biology · both · Cell: The Unit of Life

Which of the following components provides sticky character to the bacterial cell?

- (1) Plasma membrane
- **(2)** Glycocalyx
- (3) Cell wall
- (4) Nuclear membrane

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sticky character of the bacterial wall is due to glycocalyx or slime layer.
2. This layer is rich in glycoproteins.

**Solved independently** (answer withheld)

1. The bacterial cell envelope is made of the outermost $\text{glycocalyx}$, then the $\text{cell wall}$, then the $\text{plasma membrane}$; the glycocalyx (a loose slime layer or a thick capsule) is the part that makes the cell sticky. This is option $2$.

**Subtopic:** Prokaryotic Cells And Its Modification · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q119_81b00821_30102026.png?v=81b00821d03e)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q119_41fd00e9_30102026.png?v=41fd00e968fd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The glycocalyx, the bacterium's outermost coat as a loose slime layer or a thick capsule, is what makes the cell surface sticky
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The cell wall is held as the bacterium's outer covering, so a property of the surface is attached to it and the layer printed outside it is passed over
- **Why:** This question requires the stated function of one named surface layer, demonstrated by the stem's 'provides sticky character to the bacterial cell'.
- **Note:** Swap test on the trap label: renaming 'Cell wall' leaves the pull, which comes from its being the adjacent layer of the same printed envelope description rather than from any resemblance to 'Glycocalyx'. So nearby_fact.
<!--/ecat-->

## Q120

Biology · zoology · Animal Kingdom

Which among these is the correct combination of aquatic mammals?

- **(1)** Whales, Dolphins Seals
- (2) Trygon, Whales, Seals
- (3) Seals, Dolphins, Sharks
- (4) Dolphins, Seals, Trygon

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Sharks and Trygon (sting ray) are the members of chondrichthyes (cartilaginous fish) while whale, Dolphin and Seals are aquatic mammals belong to class mammalia.

**Solved independently** (answer withheld)

1. Whales, dolphins and seals are aquatic members of class Mammalia, while Trygon (sting ray) and sharks belong to Chondrichthyes, so only option $1$ has three mammals.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q120_f60b1080_30102026.png?v=f60b1080a0dc)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q120_aa2c0246_30102026.png?v=aa2c0246885b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Whales, dolphins and seals are mammals, while Trygon and the sharks are cartilaginous fishes, aquatic but not mammalian
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Seals and dolphins are placed correctly and the set is then accepted whole, so 'Sharks' is carried past on the strength of the two names in front of it
- **Why:** This question requires every name in a set to be placed in its class, demonstrated by each wrong option differing from 'Whales, Dolphins Seals' by exactly one fish name.
- **Note:** E1's pattern fell through to plain_mcq, but each option is a set of three organisms accepted or rejected whole, which is the codebook's pair_options and maps onto statements through category_retired.qtype; the shape on the page is recorded. Our stored option 1 reads 'Whales, Dolphins Seals' with a comma missing, which does not change what the option says or how it is judged.
<!--/ecat-->

## Q121

Biology · zoology · The Living World

Which of the following represents order of 'Horse'?

- (1) Caballus
- (2) Ferus
- (3) Equidae
- **(4)** Perissodactyla

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Horse belongs to order perissodactyla of class mammalia.
2. Perissodactyla includes odd-toed mammals.

**Solved independently** (answer withheld)

1. In the taxonomic hierarchy of the horse, Family is Equidae, the species epithets are caballus/ferus, and the Order is Perissodactyla, which is option $4$.

**Subtopic:** Order and Class · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q121_63fc141e_30102026.png?v=63fc141ed3b5)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q121_9e5f8c6e_30102026.png?v=9e5f8c6e29b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the horse's classification Perissodactyla is the order, Equidae the family and caballus the species name
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Equidae is the rank printed next to the order in the horse's own table row, so a student holding the names without their ranks takes the one that looks most taxonomic
- **Why:** This question requires one named rank read off the classification of a named animal, demonstrated by the stem's 'Which of the following represents order of Horse'.
- **Note:** Swap test on the trap label: replacing 'Equidae' with an unlike family name such as Felidae leaves the pull, because what carries it is the rank sitting beside the order in the printed table, not a resemblance to 'Perissodactyla'. So nearby_fact.
<!--/ecat-->

## Q122

Biology · zoology · Breathing and Exchange of Gases

Lungs are made up of air-filled sacs the alveoli. They do not collapse even after forceful expiration, because of :

- (1) Tidal Volume
- (2) Expiratory Reserve Volume
- **(3)** Residual Volume
- (4) Inspiratory Reserve Volume

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Volume of air present in lungs after forceful expiration as residual volume which prevents the collapsing of alveoli even after forceful expiration.

**Solved independently** (answer withheld)

1. Residual volume (about 1100-1200 mL) is the air that stays in the lungs even after a forcible expiration, so it keeps the alveoli from collapsing, which is option $3$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q122_de07485b_30102026.png?v=de07485be327)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q122_f0d7a8fc_30102026.png?v=f0d7a8fc7a8f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Residual volume is the air that stays in the lungs even after a forcible expiration, and it is what keeps the alveoli from collapsing
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The stem's phrase 'forceful expiration' matches the definition of expiratory reserve volume, so the volume defined by that effort is offered in place of the volume left behind after it
- **Why:** This question requires the reason the chapter gives for the alveoli staying inflated, demonstrated by the stem's 'They do not collapse even after forceful expiration, because of'.
- **Note:** Swap test on the trap label: renaming 'Expiratory Reserve Volume' to something unlike leaves the pull, because what carries it is the content of that definition matching the stem's phrase, not the mild likeness of 'Reserve' to 'Residual'. So nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q123

Biology · zoology · Human Reproduction

Capacitation occurs in

- (1) Vas deferens
- **(2)** Female Reproductive tract
- (3) Rete testis
- (4) Epididymis

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Capacitation is increase in fertilising capacity of sperms which occurs in female reproductive tract.

**Solved independently** (answer withheld)

1. Capacitation is the activation of sperm (membrane changes that enable the acrosome reaction), and it occurs only after sperm enter the female reproductive tract, so the answer is option $2$.

**Subtopic:** Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q123_6b7dae6a_30102026.png?v=6b7dae6adf61)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q123_be34524f_30102026.png?v=be34524f6827)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Capacitation is the change the sperm undergoes in the female reproductive tract; its maturation in the male tract happens earlier, in the epididymis
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Maturation of the sperm is printed at the epididymis, so a question about a further change in the sperm is answered with the one male-tract site that already owns a change
- **Why:** This question requires the stated site of one named event, demonstrated by the stem's 'Capacitation occurs in' with three male-tract sites set against the female tract.
- **Note:** Swap test on the trap label: renaming 'Epididymis' leaves the pull, because what carries it is that the chapter prints sperm maturation at that site, not any resemblance between the words. So nearby_fact.
<!--/ecat-->

## Q124

Biology · both · Molecular Basis of Inheritance

Which of the following RNAs should be most abundant in animal cell?

- (1) m-RNA
- (2) mi-RNA
- **(3)** r-RNA
- (4) t-RNA

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. rRNA is most abundant in animal cell.
2. It constitutes $80\%$ of total RNA of the cell.

**Solved independently** (answer withheld)

1. Ribosomes are present in very large numbers in every cell, and rRNA is their main structural and catalytic component, so rRNA makes up about $80\%$ of total cellular RNA, much more than tRNA ($\sim 15\%$), mRNA ($\sim 5\%$) or miRNA (trace). The answer is r-RNA, option $3$.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q124_963349c3_30102026.png?v=963349c3e109)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q124_eaee8fab_30102026.png?v=eaee8fabadf2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Ribosomal RNA is the bulk of a cell's RNA because every ribosome is built largely of it, while mRNA and tRNA are the smaller fractions
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  mRNA is the RNA the chapter foregrounds, the transcript that translation reads, so the question 'which matters most' is answered where 'which is most abundant' was asked
- **Why:** This question requires four members of one family to be ranked by amount, demonstrated by the stem's 'should be most abundant in animal cell'.
- **Note:** Recorded as compare rather than fact_line because the stem is a superlative over four members of a single family, not a single stated property of one of them. The option set also admits a count-against-mass argument for t-RNA; the tag follows the printed key, r-RNA, which is the standard figure of about four fifths of cellular RNA.
<!--/ecat-->

## Q125

Biology · zoology · Digestion and Absorption

Which cells of 'Crypts of Lieberkuhn' secrete antibacterial lysozyme?

- (1) Zymogen cells
- (2) Kupffer cells
- (3) Argentaffin cells
- **(4)** Paneth cells

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Kupffer-cells are phagocytic cells of liver.
2. Zymogen cells are enzyme producing cells.
3. Paneth cell secretes lysozyme which acts as anti-bacterial agent.
4. Argentaffin cells are hormone producing cells.

**Solved independently** (answer withheld)

1. Paneth cells at the base of the crypts of Lieberkuhn secrete the antibacterial enzyme lysozyme, so the answer is option $4$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q125_2f9444df_30102026.png?v=2f9444df369c)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q125_fb1f1ee3_30102026.png?v=fb1f1ee3f3fd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Paneth cells of the crypts of Lieberkuhn secrete the antibacterial lysozyme, while the argentaffin cells of the same crypts are the hormone-secreting ones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Argentaffin cells are the other cell type printed inside the crypts of Lieberkuhn, so a student with the address right and the secretion unattached takes the name that shares the address
- **Why:** This question requires the stated secretion of one named cell type, demonstrated by the stem's 'Which cells of Crypts of Lieberkuhn secrete antibacterial lysozyme'.
- **Note:** Swap test on the trap label: argentaffin and Paneth do not resemble each other, and replacing either name with an unlike word leaves the pull, which comes from both cells sitting in the same printed crypt. So nearby_fact. The -zym- resemblance route is real but is carried as option 1 rather than as the question's trap, because the crypt address is the clue the stem itself supplies.
<!--/ecat-->

## Q126

Biology · zoology · Reproductive Health

In case of a couple where the male is having a very low sperm count, which technique will be suitable for fertilisation?

- **(1)** Artificial Insemination
- (2) Intracytoplasmic sperm injection
- (3) Intrauterine transfer
- (4) Gamete intracytoplasmic fallopian transfer

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Infertility cases due to inability of the male partner to inseminate the female or due to very low sperm count in the ejaculates, could be corrected by artificial insemination (AI).

**Solved independently** (answer withheld)

1. NCERT Class 12 (Reproductive Health) states that infertility due to the male's inability to inseminate, or due to very low sperm counts in the ejaculate, can be corrected by the artificial insemination (AI) technique, so the answer is option $1$.

**Subtopic:** Assisted Reproductive Technologies (ART) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q126_04a79698_30102026.png?v=04a79698768e)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q126_1cb1c065_30102026.png?v=1cb1c0651028)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT attaches a very low sperm count to artificial insemination, in which semen from the husband or a donor is introduced into the vagina or the uterus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Injecting one sperm straight into the ovum reads as the repair for a man with almost no sperm, so the technique printed further down the same ART list is taken. NCERT's indication sentence attaches 'very low sperm counts in the ejaculates' to artificial insemination and keeps ICSI for an embryo formed in the laboratory.
- **Why:** This question requires the technique the source attaches to a low sperm count, demonstrated by the stem's 'the male is having a very low sperm count, which technique will be suitable for fertilisation'. Swap test applied to the trap: rename ICSI with an unlike word and the pull survives, because its place in the printed ART list and its sperm-handling role carry the student, not any likeness to 'artificial insemination' - so nearby_fact, not look_alike_term.
- **Note:** Options 2 and 3 are both near-misses of printed ART names, which is what makes this question turn on one sentence rather than on the technique list. ICSI is defensible on clinical grounds, but the stem reuses the source's own phrase for the artificial-insemination indication, so the question is tagged as printed and the key is not re-judged here.
<!--/ecat-->

## Q127

Biology · zoology · Body Fluids and Circulation

Frog's heart when taken out of the body continues to beat for some time
Select the best option from the following statements

- **((a))** Frog is a poikilotherm
- **((b))** Frog does not have any coronary circulation
- **((c))** Heart is "myogenic" in nature
- **((d))** Heart is autoexcitable

- (1) (a) & (b)
- **(2)** (c) & (d)
- (3) Only (c)
- (4) Only (d)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Frog or the vertebrates have myogenic heart having self contractile system or are autoexcitable; because of this condition, it will keep on working outside the body for some time.

**Solved independently** (answer withheld)

1. The isolated heart keeps beating without nerve input, so the impulse starts in its own specialised muscle: the heart is $\text{myogenic}$, i.e. $\text{autoexcitable}$. Statements $(c)$ and $(d)$ both give this cause, while $(a)$ and $(b)$ do not explain the beat, so the answer is option $2$.

**Subtopic:** Regulation of Cardiac Activity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q127_b6503367_30102026.png?v=b650336790ec)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q127_07ee6d0f_30102026.png?v=07ee6d0f2929)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The vertebrate heartbeat starts in the heart muscle itself, so an excised myogenic and autoexcitable heart goes on beating without any nerve supply
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Both statements in this set are true of a frog, so a student who checks the four statements for truth instead of for explanatory force ticks them; being a poikilotherm and lacking coronary vessels bear on how long an excised heart lasts, not on what makes it beat at all.
- **Why:** This question requires the reason a stated observation happens, demonstrated by the rejected statements '(a) Frog is a poikilotherm' and '(b) Frog does not have any coronary circulation' being true of the animal yet not accounting for the beating.
- **Note:** negative_words_seen records 'NOT', but the only negative is inside statement (b), 'Frog does not have any coronary circulation'; the task itself is direct. (a) and (b) are sometimes offered elsewhere as bearing on how long an excised frog heart survives; the tag follows the printed key, which takes (c) and (d) as the explanation of the beating.
<!--/ecat-->

## Q128

Biology · zoology · Reproductive Health

Match the following sexually transmitted diseases (Column - I) with their causative agent (Column - II) and select the correct option.

| List-I | | List-II | |
|---|---|---|---|
| (a) | Gonorrhea | (i) | HIV |
| (b) | Syphilis | (ii) | Neisseria |
| (c) | Genital Warts | (iii) | Treponema |
| (d) | AIDS | (iv) | Human Papilloma virus |

- (1) (iv) (ii) (iii) (i)
- (2) (iv) (iii) (ii) (i)
- **(3)** (ii) (iii) (iv) (i)
- (4) (iii) (iv) (i) (ii)

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Gonorrhoea – Neisseria (Bacteria)
2. Syphilis – Treponema (Bacteria)
3. Genital Warts – Human papilloma virus (Virus)
4. AIDS – HIV (Virus)

**Solved independently** (answer withheld)

1. Gonorrhea is caused by $Neisseria$ (ii), syphilis by $Treponema$ (iii), genital warts by Human Papilloma virus (iv) and AIDS by HIV (i), so the match is $a \to (ii),\ b \to (iii),\ c \to (iv),\ d \to (i)$, which is option $3$.

**Subtopic:** Sexually Transmitted Infections (STIs) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q128_a51ba524_30102026.png?v=a51ba524d886)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q128_a8675fdc_30102026.png?v=a8675fdc128c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each sexually transmitted infection is tied to one named agent: Neisseria for gonorrhoea, Treponema for syphilis, Human Papilloma virus for genital warts, HIV for AIDS
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Option 2 keeps the two pairings whose agent name is bound tightest to the disease — Syphilis-Treponema and AIDS-HIV — so a student who verifies those two and stops accepts a code in which the gonorrhoea and genital-warts agents have been exchanged
- **Why:** This question requires the causative agent NCERT names for each listed infection, demonstrated by Column II printing four agents — "HIV", "Neisseria", "Treponema", "Human Papilloma virus" — against four named diseases, with no criterion in the stem to apply to them.
- **Note:** Single-question packet, so there was no sibling to compare the labels against. The viral/bacterial split in Column II (HIV and Human Papilloma virus against Neisseria and Treponema) strikes options 1, 2 and 4 at once, which is why only one pairing row does any discriminating.
<!--/ecat-->

## Q129

Biology · zoology · Principles of Inheritance and Variation

The genotypes of a Husband and Wife are $I^{A}I^{B}$ and $I^{A}i$. Among the blood types of their children, how many different genotypes and phenotypes are possible?

- **(1)** 4 genotypes ; 3 phenotypes
- (2) 4 genotypes ; 4 phenotypes
- (3) 3 genotypes ; 3 phenotypes
- (4) 3 genotypes ; 4 phenotypes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Husband ($I^{A}I^{B}$) $\times$ Wife ($I^{A}i$)

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q129_sol_1_7d8024aa_30102026.svg?v=7d8024aa67e0)

2. Number of genotypes $= 4$
3. Number of phenotypes $= 3$
4. $I^{A}I^{A}$ and $I^{A}i = \mathrm{A}$
5. $I^{A}I^{B} = \mathrm{AB}$
6. $I^{B}i = \mathrm{B}$

**Solved independently** (answer withheld)

1. Husband $I^{A}I^{B}$ forms gametes $I^{A}$ and $I^{B}$; wife $I^{A}i$ forms gametes $I^{A}$ and $i$.
2. Crossing gives children $I^{A}I^{A}$, $I^{A}i$, $I^{A}I^{B}$ and $I^{B}i$, i.e. $4$ genotypes.
3. $I^{A}$ and $I^{B}$ are dominant over $i$ and codominant with each other, so $I^{A}I^{A}$ and $I^{A}i$ are group A, $I^{A}I^{B}$ is group AB and $I^{B}i$ is group B.
4. That is $4$ genotypes and $3$ phenotypes, which is option $1$.

**Subtopic:** Incomplete Dominance & Co-dominance, Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q129_a314c03a_30102026.png?v=a314c03a3647)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q129_d575b9e9_30102026.png?v=d575b9e9ec27)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** $I^A$ and $I^B$ are codominant and both dominate $i$, so two different genotypes can show the same blood group A
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The square gives four boxes, and reading one blood group off each box turns four genotypes into four phenotypes. $I^AI^A$ and $I^Ai$ are both group A, so the four genotypes carry only three groups: A, AB and B.
- **Why:** This question requires the offspring of $I^AI^B \times I^Ai$ to be worked out and the two counts taken off it, demonstrated by 'how many different genotypes and phenotypes are possible'.
- **Note:** type_patterns called this statement_options; the printed options are two counts bundled together, not statements to be judged, so the shape recorded is two_part - half an option right scores nothing here.
<!--/ecat-->

## Q130

Biology · zoology · Body Fluids and Circulation

The hepatic portal vein drains blood to liver from

- (1) Kidneys
- **(2)** Intestine
- (3) Heart
- (4) Stomach

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In hepatic portal system, hepatic portal vein carries maximum amount of nutrients from intestine to liver.

**Solved independently** (answer withheld)

1. The hepatic portal system, as described in NCERT, carries blood from the $\text{intestine}$ to the $\text{liver}$ through the hepatic portal vein before it reaches the systemic circulation, so the answer is option $2$ (Intestine).

**Subtopic:** Electrocardiogram (ECG) and Double Circulation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q130_ff57b0e1_30102026.png?v=ff57b0e1af1f)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q130_976b18cb_30102026.png?v=976b18cb421d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The hepatic portal vein is the one vessel that carries blood from the intestine to the liver before that blood reaches the systemic circulation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Holding the portal vein as the vessel that takes absorbed food from the gut to the liver, a student names the digestive organ that comes first in the alimentary canal. The printed line names the intestine, which is where absorption happens and so where the portal blood is loaded.
- **Why:** This question requires the stated source of the hepatic portal vein's blood, demonstrated by the stem's 'drains blood to liver from' with four organs offered and no criterion printed to work from. Swap test applied: replace 'Stomach' with an unlike organ and the pull dies, so it is the stomach's position beside the intestine in the gut sequence that carries the student - nearby_fact, not look_alike_term.
<!--/ecat-->

## Q131

Biology · botany · Morphology of Flowering Plants

Coconut fruit is a

- (1) Nut
- (2) Capsule
- **(3)** Drupe
- (4) Berry

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Coconut fruit is a drupe.
2. A drupe develops from monocarpellary superior ovary and are one seeded.

**Solved independently** (answer withheld)

1. Coconut develops from a monocarpellary superior ovary and is one-seeded, with a thin epicarp, a fibrous mesocarp and a hard stony endocarp, which is a drupe (NCERT Class 11 gives coconut as a drupe with a fibrous mesocarp), so option $3$.

**Subtopic:** The Fruit · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q131_3ab3f1c1_30102026.png?v=3ab3f1c157e4)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q131_7549ef6f_30102026.png?v=7549ef6f005d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The coconut is a drupe: a one-seeded fruit from a monocarpellary superior ovary whose pericarp is fibrous outside and stony within
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The fruit's own name ends in 'nut', and its husk is dry rather than juicy, so the dry one-seeded class is taken straight off the name. The printed line is 'In mango and coconut, the fruit is a drupe', and it is the three-layered pericarp, not the common name, that files it.
- **Why:** This question requires the fruit class the source assigns to the coconut, demonstrated by the stem 'Coconut fruit is a' with four fruit types offered and no pericarp description printed to classify from. Swap test applied: rename the fruit and the pull to 'Nut' dies, so the likeness between 'coconut' and 'nut' is doing the work - look_alike_term, not nearby_fact.
<!--/ecat-->

## Q132

Biology · botany · Anatomy of Flowering Plants

The vascular cambium normally gives rise to

- **(1)** Secondary xylem
- (2) Periderm
- (3) Phelloderm
- (4) Primary phloem

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. During secondary growth, vascular cambium gives rise to secondary xylem and secondary phloem.
2. Phelloderm is formed by cork cambium.

**Solved independently** (answer withheld)

1. The vascular cambium is a lateral meristem that cuts off $\text{secondary xylem}$ towards the pith and $\text{secondary phloem}$ towards the periphery, so option $1$ (Secondary xylem) is a product of it; options $2$ and $3$ (periderm, phelloderm) come from the cork cambium and option $4$ (primary phloem) comes from the procambium, so the answer is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q132_5c2d75e0_30102026.png?v=5c2d75e0beeb)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q132_95ccb175_30102026.png?v=95ccb17585b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The vascular cambium cuts off secondary xylem inward and secondary phloem outward; phellem, phelloderm and the periderm are the cork cambium's products
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A student holding one undivided 'cambium' that cuts off cells to the inside and the outside picks the inward product printed in the same secondary-growth account. Phelloderm is cut off inward by the cork cambium, not by the vascular cambium, whose inward product is secondary xylem.
- **Why:** This question requires which tissue the vascular cambium produces, demonstrated by 'Secondary xylem' being set against 'Periderm' and 'Phelloderm', which belong to the cork cambium. Swap test applied to the trap: replace 'Phelloderm' with an unlike word and the pull survives, because what carries the student is its printing inside the same secondary-growth account, not any likeness to secondary xylem - nearby_fact.
- **Note:** All three wrong options carry a route, which is why no filler is recorded here: two are cork-cambium products and the third is the remembered pair with its qualifier changed.
<!--/ecat-->

## Q133

Biology · zoology · Animal Kingdom

In case of poriferans the spongocoel is lined with flagellated cells called :

- **(1)** Choanocytes
- (2) Mesenchymal cells
- (3) Ostia
- (4) Oscula

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Choanocytes (collar cells) form lining of spongocoel in poriferans (sponges).
2. Flagella in collar cells provide circulation to water in water canal system.

**Solved independently** (answer withheld)

1. In poriferans the spongocoel and canals are lined by flagellated collar cells, the choanocytes; ostia are incurrent pores and the osculum is the excurrent opening, so the answer is option $1$.

**Subtopic:** Phylum – Porifera · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q133_bcccbbab_30102026.png?v=bcccbbab9dc7)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q133_bd5efa6f_30102026.png?v=bd5efa6fc81f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In sponges the spongocoel and the canals are lined by choanocytes, the flagellated collar cells; ostia and the osculum are the openings of the water path, not cells
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The word 'spongocoel' retrieves the one printed sentence it appears in, and the other term in that sentence is 'minute pores (ostia)', so a student answers from the sentence rather than from the question. Ostia are pores in the body wall where water enters; the lining named in the same account is the choanocyte.
- **Why:** This question requires the name of the cells lining the spongocoel, demonstrated by the stem's 'lined with flagellated cells called'. Swap test applied: replace 'Ostia' with an unlike word and the pull survives, since it is the term's printing in the same sentence as 'spongocoel' that carries the student - nearby_fact, not look_alike_term (ostia and oscula resemble each other, but that pair is two wrong options, not the wrong one and the right one).
<!--/ecat-->

## Q134

Biology · zoology · Digestion and Absorption

A baby boy aged two years is admitted to play school and passes through a dental check-up. The dentist observed that the boy had twenty teeth. Which teeth were absent?

- **(1)** Pre-molars
- (2) Molars
- (3) Incisors
- (4) Canines

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Total number of teeth in human child $= 20$.
2. Premolars are absent in primary dentition.

**Solved independently** (answer withheld)

1. A two-year-old child has only the deciduous (milk) teeth, $20$ in all.
2. Deciduous dental formula per half of each jaw: $\frac{2102}{2102}$ (incisors $2$, canines $1$, premolars $0$, molars $2$), giving $(2+1+0+2)\times 4 = 20$.
3. Premolars are $0$ in the milk set and appear only in the permanent set ($\frac{2123}{2123} = 32$), so the absent teeth are premolars, option $1$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q134_46f6f7f1_30102026.png?v=46f6f7f16a49)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q134_ecc56bc3_30102026.png?v=ecc56bc3bfbf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The milk set is 2102 in each half jaw - two incisors, one canine, no premolar, two molars - so the premolars arrive only with the permanent set of 32
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Premolar is molar with a prefix, so a student who remembers only that the milk set is short of back teeth picks the back-tooth name. The milk set keeps eight molars, two in each half jaw, and it is the eight premolars together with four molars that are still to come.
- **Why:** This question requires the deciduous dental formula applied to the case described, demonstrated by 'the boy had twenty teeth' with the absent class left to be named. Swap test applied to the trap: replace 'Molars' with an unlike word and both routes to it die, and the surviving pull is that premolar and molar are the same word with a prefix - look_alike_term, with the twelve-missing count recorded as the second way to the same option.
<!--/ecat-->

## Q135

Biology · botany · Plant Kingdom

An example of colonial alga is

- (1) Ulothrix
- (2) Spirogyra
- (3) Chlorella
- **(4)** Volvox

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Volvox is motile colonial fresh water alga with definite number of vegetative cells.

**Solved independently** (answer withheld)

1. NCERT (Plant Kingdom, algae) classes Chlorella as unicellular, $Ulothrix$ and $Spirogyra$ as filamentous, and $Volvox$ as colonial, so the answer is option $4$.

**Subtopic:** Algae · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q135_a408234a_30102026.png?v=a408234adc8e)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q135_dfaaa91c_30102026.png?v=dfaaa91c6112)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Among the green algae Volvox is the colonial form, a sphere of cells in a common matrix, while Ulothrix and Spirogyra are the filamentous forms
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Ulothrix is printed in the same green-algal example list as Volvox, so a student holding the names without the body form attached to each takes a neighbour from that list. In the same sentence Ulothrix is one of the filamentous examples - a thread of cells joined end to end, not a colony held in a common matrix.
- **Why:** This question requires the genus the source names as the colonial alga, demonstrated by the stem's 'An example of colonial alga' with four green algal genera offered. Swap test applied: replace 'Ulothrix' with an unlike word and the pull survives, because the two names are not alike and it is the shared printed list that carries the student - nearby_fact, not look_alike_term.
<!--/ecat-->

## Q136

Chemistry · inorganic · Coordination Compounds – Practice

An example of a sigma bonded organometallic compound is

- (1) Ferrocene
- (2) Cobaltocene
- (3) Ruthenocene
- **(4)** Grignard's reagent

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Grignard's reagent i.e., $\mathrm{RMgX}$ is $\sigma$-bonded organometallic compound.

**Solved independently** (answer withheld)

1. In Grignard's reagent $\mathrm{RMgX}$ the metal is joined to carbon by a single $\mathrm{Mg{-}C}$ $\sigma$ bond, so it is a $\sigma$-bonded organometallic compound, while ferrocene $\mathrm{Fe(C_5H_5)_2}$, cobaltocene $\mathrm{Co(C_5H_5)_2}$ and ruthenocene $\mathrm{Ru(C_5H_5)_2}$ are $\pi$-bonded ($\eta^5$) sandwich compounds; the answer is option $4$.

**Subtopic:** Bonding in Coordination Compounds and Metal Carbonyls · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q136_736dd20a_30102026.png?v=736dd20aef03)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q136_9ec1a546_30102026.png?v=9ec1a546bc91)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Organometallics split by bond type: a Grignard reagent carries a metal-carbon sigma bond, while the metallocenes hold the metal through the pi electrons of their rings
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Ferrocene is the compound the chapter uses as its showpiece organometallic, so a student holding only 'ferrocene is the organometallic compound' ticks it without sorting sigma from pi; the iron in ferrocene sits between two cyclopentadienyl rings and is held by their pi electrons, not by a sigma bond.
- **Why:** This question requires the stated distinction between sigma- and pi-bonded organometallics, demonstrated by the stem's 'a sigma bonded organometallic compound' set against three metallocenes. Swap test applied: replacing 'Ferrocene' with an unlike name keeps the pull, because what carries the student is the chapter's printed showpiece, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q137

Chemistry · organic · Hydrocarbons

Which one is the correct order of acidity?

- (1) $\mathrm{CH\equiv CH} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH_3-CH_3}$
- (2) $\mathrm{CH_3-CH_3} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH\equiv CH}$
- (3) $\mathrm{CH_2=CH_2} > \mathrm{CH_3-CH=CH_2} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH\equiv CH}$
- **(4)** $\mathrm{CH\equiv CH} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-CH_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Correct order is
2. $\mathrm{H-C\equiv C-H}$ (Two acidic hydrogens) $> \mathrm{H_3C-C\equiv C-H}$ (One acidic hydrogen) $> \mathrm{H_2C=CH_2} > \mathrm{CH_3-CH_3}$

**Solved independently** (answer withheld)

1. Acidity of a $\mathrm{C-H}$ bond rises with the $s$-character of the carbon: $sp\,(50\%) > sp^2\,(33\%) > sp^3\,(25\%)$, so terminal alkynes $>$ alkenes $>$ alkanes.
2. Between the alkynes, the $\mathrm{CH_3}$ group in $\mathrm{CH_3-C\equiv CH}$ exerts a $+I$ effect that destabilises the acetylide anion, so $\mathrm{CH\equiv CH} > \mathrm{CH_3-C\equiv CH}$.
3. Order: $\mathrm{CH\equiv CH} > \mathrm{CH_3-C\equiv CH} > \mathrm{CH_2=CH_2} > \mathrm{CH_3-CH_3}$, which is option $4$.

**Subtopic:** Chemical Properties of Alkynes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q137_af917ed5_30102026.png?v=af917ed533d0)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q137_0e23a1f1_30102026.png?v=0e23a1f1c8ad)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** C-H acidity follows the s character of the carbon orbital holding the hydrogen: sp beats sp2 beats sp3, because the carbanion left behind is more stable the closer its lone pair sits to the nucleus
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A methyl group really does push electrons into the anion it leaves behind, so a student who weighs that effect heavily demotes propyne below ethene while keeping ethyne first and ethane last; propyne's acidic hydrogen is still on an sp carbon, which outweighs the alkyl donation and keeps it in second place.
- **Why:** This question requires four hydrocarbons ranked by C-H acidity, demonstrated by the stem's 'correct order of acidity' with each option printing a full four-term order.
- **Note:** half_right is used because the option prints four terms and fails on one interior adjacency only; the codebook's `reversed` explicitly excludes one swapped pair inside a longer order, and option 2 is where the full inversion sits.
<!--/ecat-->

## Q138

Chemistry · organic · Hydrocarbons

Predict the correct intermediate and product in the following reaction $\mathrm{H_3C-C\equiv CH\xrightarrow[HgSO_4]{H_2O,\ H_2SO_4}}$ intermediate (A) $\longrightarrow$ product (B)

- (1) propan-2-one `CC(C)=O`; propyne `C#CC` — A : $\mathrm{H_3C-\underset{\underset{O}{\|}}{C}-CH_3}$ B : $\mathrm{H_3C-C\equiv CH}$
- **(2)** prop-1-en-2-ol `C=C(C)O`; propan-2-one `CC(C)=O` — A : $\mathrm{H_3C-\underset{\underset{OH}{|}}{C}=CH_2}$ B : $\mathrm{H_3C-\underset{\underset{O}{\|}}{C}-CH_3}$
- (3) prop-1-en-2-yl sulfate `C=C(C)OS(=O)(=O)[O-]`; propan-2-one `CC(C)=O` — A : $\mathrm{H_3C-\underset{\underset{SO_4}{|}}{C}=CH_2}$ B : $\mathrm{H_3C-\underset{\underset{O}{\|}}{C}-CH_3}$
- (4) prop-1-en-2-ol `C=C(C)O`; prop-1-en-2-yl sulfate `C=C(C)OS(=O)(=O)[O-]` — A : $\mathrm{H_3C-\underset{\underset{OH}{|}}{C}=CH_2}$ B : $\mathrm{H_3C-\underset{\underset{SO_4}{|}}{C}=CH_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: I. propyne → 2-hydroxyprop-1-en-1-yl ($\ce{H3C-C(OH)=CH}$) (A); (A) →(Tautomerism) propan-2-one (B)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q138_sol_1_4b51d7ae_30102026.svg?v=4b51d7ae561f)

*I. propyne → 2-hydroxyprop-1-en-1-yl ($\ce{H3C-C(OH)=CH}$) (A); (A) →[Tautomerism] propan-2-one (B)*


**Solved independently** (answer withheld)

1. Dilute $\mathrm{H_2SO_4}$ with $\mathrm{HgSO_4}$ hydrates the alkyne $\mathrm{H_3C-C\equiv CH}$ by adding $\mathrm{H_2O}$ across the triple bond.
2. By Markovnikov's rule, $\mathrm{H}$ goes to the terminal carbon and $\mathrm{OH}$ to the internal carbon, giving the enol $\mathrm{H_3C-C(OH)=CH_2}$ as intermediate (A).
3. The enol is unstable and tautomerises (keto-enol) to the ketone $\mathrm{H_3C-CO-CH_3}$ (acetone) as product (B).
4. A = $\mathrm{H_3C-C(OH)=CH_2}$, B = $\mathrm{H_3C-CO-CH_3}$, which is option $2$.

**Subtopic:** Chemical Properties of Alkynes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q138_daceb793_30102026.png?v=daceb793bbb8)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q138_ed3a0f83_30102026.png?v=ed3a0f834a3c)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Acid-catalysed hydration of an alkyne over HgSO4 adds water by Markovnikov's rule to give an enol, which tautomerises to the carbonyl compound, so propyne ends as acetone
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  H2SO4 is printed over the arrow, so a student who has acetone fixed as the product builds the intermediate out of the reagent in front of them and writes a sulphate group across the former triple bond; what adds is water, so the intermediate is the enol CH3-C(OH)=CH2.
- **Why:** This question requires the intermediate and the product of acid-catalysed alkyne hydration together, demonstrated by every option printing both 'A :' and 'B :' and standing or falling as a whole.
<!--/ecat-->

## Q139

Chemistry · inorganic · The p–Block Elements

It is because of inability of $ns^{2}$ electrons of the valence shell to participate in bonding that

- (1) $\mathrm{Sn^{2+}}$ and $\mathrm{Pb^{2+}}$ are both oxidising and reducing
- (2) $\mathrm{Sn^{4+}}$ is reducing while $\mathrm{Pb^{4+}}$ is oxidising
- **(3)** $\mathrm{Sn^{2+}}$ is reducing while $\mathrm{Pb^{4+}}$ is oxidising
- (4) $\mathrm{Sn^{2+}}$ is oxidising while $\mathrm{Pb^{4+}}$ is reducing

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Inability of $ns^{2}$ electrons of the valence shell to participate in bonding on moving down the group in heavier p-block elements is called inert pair effect
2. As a result, $\mathrm{Pb(II)}$ is more stable than $\mathrm{Pb(IV)}$
3. $\mathrm{Sn(IV)}$ is more stable than $\mathrm{Sn(II)}$
4. $\therefore$ $\mathrm{Pb(IV)}$ is easily reduced to $\mathrm{Pb(II)}$
5. $\therefore$ $\mathrm{Pb(IV)}$ is oxidising agent
6. $\mathrm{Sn(II)}$ is easily oxidised to $\mathrm{Sn(IV)}$
7. $\therefore$ $\mathrm{Sn(II)}$ is reducing agent

**Solved independently** (answer withheld)

1. The reluctance of the $ns^{2}$ electrons to take part in bonding is the inert pair effect, which grows down group 14, so the $+2$ state becomes more stable relative to $+4$ going down the group.
2. For tin the $+4$ state is still the more stable one, so $\mathrm{Sn^{2+}} \rightarrow \mathrm{Sn^{4+}} + 2e^{-}$ happens readily and $\mathrm{Sn^{2+}}$ acts as a reducing agent.
3. For lead the inert pair effect is strong, so $+2$ is the more stable state and $\mathrm{Pb^{4+}} + 2e^{-} \rightarrow \mathrm{Pb^{2+}}$ happens readily, making $\mathrm{Pb^{4+}}$ an oxidising agent.
4. So $\mathrm{Sn^{2+}}$ is reducing while $\mathrm{Pb^{4+}}$ is oxidising, which is option $3$.

**Subtopic:** General Properties & Trends of Group 14 (Carbon Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q139_4b0417ee_30102026.png?v=4b0417ee18f7)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q139_d9c69929_30102026.png?v=d9c69929a8ff)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inert pair effect in group 14: lead's 6s2 pair stays out of bonding, so Pb(IV) is an oxidising agent, while tin's stable state is +4 and Sn(II) is a reducing agent
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Tin does prefer +4 and lead does prefer +2, so a student who holds that much and then reads 'Sn2+ moving to Sn4+' as grabbing electrons writes Sn2+ oxidising and Pb4+ reducing; +2 to +4 is a loss of two electrons, which makes Sn2+ the reducing agent and Pb4+, which drops to +2, the oxidising one.
- **Why:** This question requires the printed consequence of the inert pair effect in group 14, demonstrated by the stem supplying the cause -- 'inability of ns2 electrons of the valence shell to participate in bonding' -- while the options supply rival redox behaviours.
- **Note:** The stem prints the reason and asks for the behaviour it explains, so the answer slot holds the fact the chapter states rather than a reason; hence fact_line and not reason_line.
<!--/ecat-->

## Q140

Chemistry · inorganic · The s-Block Elements

Ionic mobility of which of the following alkali metal ions is lowest when aqueous solution of their salts are put under an electric field?

- (1) $\mathrm{Rb}$
- **(2)** $\mathrm{Li}$
- (3) $\mathrm{Na}$
- (4) $\mathrm{K}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Li^{+}}$ being smallest, has maximum charge density
2. $\therefore$ $\mathrm{Li^{+}}$ is most heavily hydrated among all alkali metal ions. Effective size of $\mathrm{Li^{+}}$ in aq solution is therefore, largest.
3. $\therefore$ Moves slowest under electric field.

**Solved independently** (answer withheld)

1. Smaller bare ion means higher charge density, so the extent of hydration follows $\mathrm{Li^+} > \mathrm{Na^+} > \mathrm{K^+} > \mathrm{Rb^+}$.
2. Greater hydration means a larger hydrated radius, so $\mathrm{Li^+(aq)}$ is the largest hydrated ion.
3. A larger hydrated ion moves more slowly in an electric field, so ionic mobility follows $\mathrm{Li^+(aq)} < \mathrm{Na^+(aq)} < \mathrm{K^+(aq)} < \mathrm{Rb^+(aq)}$.
4. The lowest ionic mobility is that of $\mathrm{Li^+}$, which is option $2$.

**Subtopic:** Alkali Metals: Properties and Trends · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 25)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q140_de28f139_30102026.png?v=de28f1399adb)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q140_021f3647_30102026.png?v=021f36479332)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In water the small Li+ carries the thickest hydration shell, so its hydrated ion is the bulkiest and its ionic mobility the lowest -- the reverse of the bare-ion size order
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Rb+ is the largest bare ion printed, so a student applying 'the bigger the ion, the slower it moves' lands there; the stem puts the salts in aqueous solution, where each ion drags a shell of water and the small Li+ becomes the bulkiest mover.
- **Why:** This question requires the stated fact about hydrated size and ionic mobility among the alkali metal ions, demonstrated by the stem asking whose mobility is 'lowest when aqueous solution of their salts are put under an electric field'.
<!--/ecat-->

## Q141

Chemistry · inorganic · The p–Block Elements

Match the interhalogen compounds of column I with the geometry in column II and assign the correct code

| List-I | | List-II | |
|---|---|---|---|
| (a) | $\mathrm{XX'}$ | (i) | T-shape |
| (b) | $\mathrm{XX'_3}$ | (ii) | Pentagonal bipyramidal |
| (c) | $\mathrm{XX'_5}$ | (iii) | Linear |
| (d) | $\mathrm{XX'_7}$ | (iv) | Square-pyramidal |
|  |  | (v) | Tetrahedral |

- (1) (v) (iv) (iii) (ii)
- (2) (iv) (iii) (ii) (i)
- (3) (iii) (iv) (i) (ii)
- **(4)** (iii) (i) (iv) (ii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{XX'} \rightarrow$ Linear
2. $\mathrm{XX'_3} \rightarrow$ Example : $\mathrm{ClF_3} \rightarrow$ T-shape
3. $\mathrm{XX'_5} \rightarrow$ Example : $\mathrm{BrF_5} \rightarrow$ Square pyramidal
4. $\mathrm{XX'_7} \rightarrow$ Example : $\mathrm{IF_7} \rightarrow$ Pentagonal bipyramidal

**Solved independently** (answer withheld)

1. $\mathrm{XX'}$ is a diatomic molecule, so it is linear: (a) $\to$ (iii).
2. In $\mathrm{XX'_3}$ the central X has 3 bond pairs and 2 lone pairs ($sp^3d$), so the shape is T-shaped: (b) $\to$ (i).
3. In $\mathrm{XX'_5}$ the central X has 5 bond pairs and 1 lone pair ($sp^3d^2$), so the shape is square pyramidal: (c) $\to$ (iv).
4. In $\mathrm{XX'_7}$ the central X has 7 bond pairs and no lone pair ($sp^3d^3$), so the shape is pentagonal bipyramidal: (d) $\to$ (ii).
5. The code (iii) (i) (iv) (ii) is option $4$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q141_6528307e_30102026.png?v=6528307e7f26)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q141_a76b8ae9_30102026.png?v=a76b8ae91637)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** VSEPR on the interhalogens: count bonding and lone pairs on the central halogen, so two atoms give linear, three bonds with two lone pairs give T-shape, five bonds with one lone pair give square pyramidal, and seven bonds give pentagonal bipyramidal
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  T-shape and square pyramidal are both interhalogen shapes from the same table, so a student holding the list of shapes without the pair counts hands the five-substituent shape to $\mathrm{XX'_3}$ and the three-substituent shape to $\mathrm{XX'_5}$; square pyramidal needs five bonding pairs and one lone pair, which only $\mathrm{XX'_5}$ has.
- **Why:** This question requires VSEPR applied to each formula to get a shape, demonstrated by column I printing only the formulae '$\mathrm{XX'}$', '$\mathrm{XX'_3}$', '$\mathrm{XX'_5}$', '$\mathrm{XX'_7}$', so each row is settled by counting bonding and lone pairs rather than by recognising a named compound. asks is apply_rule and not compare: that the answer is a pairing is what qtype match_columns already records, and what each row demands is the shape a given number of substituents gives. On nearby_fact against look_alike_term the swap test was applied - replace 'T-shape' and 'Square-pyramidal' with two unlike words and the pull survives, because what carries the student is that both shapes sit in the same interhalogen table, not any resemblance between the names.
- **Note:** Column II prints five shapes for four rows, so (v) Tetrahedral is an unused decoy; options 1 and 2 are both consecutive descending runs of column II, (v)(iv)(iii)(ii) and (iv)(iii)(ii)(i), which is why both are recorded as filler rather than as routes. The options print bare shape codes with no (a)-(d) labels beside them, so the code is read in the printed row order of column I.
<!--/ecat-->

## Q142

Chemistry · physical · The Solid State

Which is the incorrect statement?

- (1) $\mathrm{NaCl(s)}$ is insulator, silicon is semiconductor, silver is conductor, quartz is piezo electric crystal
- **(2)** Frenkel defect is favoured in those ionic compounds in which sizes of cation and anions are almost equal
- **(3)** $\mathrm{FeO_{0.98}}$ has non stoichiometric metal deficiency defect
- (4) Density decreases in case of crystals with Schottky's defect

**Answer** — booklet: (2, 3) · independent solve: (2) · agree

**Publisher's solution**

1. Frenkel defect occurs in those ionic compounds in which size of cation and anion is largely different.
2. Non-stoichiometric ferrous oxide is $\mathrm{Fe_{0.93\text{–}0.96}O_{1.00}}$ and it is due to metal deficiency defect.

**Solved independently** (answer withheld)

1. Option 1: $\mathrm{NaCl(s)}$ is an insulator, Si a semiconductor, Ag a conductor and quartz a piezoelectric crystal, so it is correct.
2. Option 2: Frenkel defect is shown by ionic solids with a large difference in ion sizes (small cation, e.g. $\mathrm{ZnS}$, $\mathrm{AgCl}$); near-equal sizes favour Schottky defect, so it is incorrect.
3. Option 3: $\mathrm{FeO_{0.98}}$ has fewer Fe than O ($\mathrm{Fe^{3+}}$ replaces some $\mathrm{Fe^{2+}}$), a metal deficiency non-stoichiometric defect, so it is correct.
4. Option 4: Schottky defect removes cation-anion pairs from the lattice, so density decreases, which is correct.
5. The incorrect statement is option $2$.

**Subtopic:** Imperfections in Solids · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q142_051e6269_30102026.png?v=051e626995e8)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q142_4c220150_30102026.png?v=4c2201503267)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Point defects: a Frenkel defect needs a large difference in ion size and leaves the density alone, a Schottky defect removes whole ion pairs and lowers the density, and a non-stoichiometric formula shows which ion is in deficit
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The line 'the density is unchanged' sits in the same paragraph as 'the density decreases', one against each of the two stoichiometric defects, so a student who stored the pair of consequences without which defect owns which marks this density claim as the false one; it is Schottky, with cation and anion both missing, that lowers the density.
- **Why:** This question requires each printed defect statement graded against the solid-state chapter's own lines, demonstrated by the stem 'Which is the incorrect statement?' above four independent claims.
- **Note:** The printed key accepts two options -- 'Answer (2 & 3)' -- so options 2 and 3 are both keyed and neither is treated as a wrong option here. Option 3 is keyed incorrect because the formula is printed as FeO(0.98), oxygen in deficit and therefore metal-excess, whereas the metal-deficiency example is written Fe(0.95)O; the tag follows the printed key. Swap test on option 4: replacing 'Schottky' with an unlike word keeps the pull, since the error is importing the neighbouring line's consequence, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q143

Chemistry · physical · Chemical Equilibrium

Which one of the following statements is not correct?

- (1) Enzymes catalyse mainly bio-chemical reactions
- (2) Coenzymes increase the catalytic activity of enzyme
- (3) Catalyst does not initiate any reaction
- **(4)** The value of equilibrium constant is changed in the presence of a catalyst in the reaction at equilibrium

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A catalyst decreases activation energies of both the forward and backward reaction by same amount, therefore, it speeds up both forward and backward reaction by same rate.
2. Equilibrium constant is therefore not affected by catalyst at a given temperature.

**Solved independently** (answer withheld)

1. Statement 1: enzymes are biological catalysts that mainly catalyse biochemical reactions, so it is correct.
2. Statement 2: coenzymes (activators) increase the activity of enzymes, as NCERT states, so it is correct.
3. Statement 3: a catalyst only speeds up a reaction that can already happen and does not start a non-spontaneous reaction, so it is correct.
4. Statement 4: a catalyst lowers $E_a$ equally for both directions, so $k_f$ and $k_b$ rise by the same factor and $K = \frac{k_f}{k_b}$ is unchanged.
5. So statement 4 is not correct, which is option $4$.

**Subtopic:** Effect of a Catalyst on Equilibrium · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q143_49f1adb5_30102026.png?v=49f1adb51e19)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q143_f1c41c0e_30102026.png?v=f1c41c0e977d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A catalyst lowers the activation energy of both directions equally, so it changes how fast equilibrium is reached but never the value of the equilibrium constant
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  'Catalyst does not initiate any reaction' is a printed line and true as written, and it is the only option carrying a negative, so a reader matching the stem's 'not correct' against the wording of the options stops there instead of grading the chemistry.
- **Why:** This question requires each catalyst statement graded against the chapter's own lines, demonstrated by the stem 'Which one of the following statements is not correct?' and by option 4 claiming that 'the value of equilibrium constant is changed in the presence of a catalyst'.
<!--/ecat-->

## Q144

Chemistry · physical · Electrochemistry

In the electrochemical cell $\mathrm{Zn|ZnSO_4(0.01\,M)||CuSO_4(1.0\,M)|Cu}$, the emf of this Daniel cell is $E_1$. When the concentration of $\mathrm{ZnSO_4}$ is changed to $1.0\,\mathrm{M}$ and that of $\mathrm{CuSO_4}$ changed to $0.01\,\mathrm{M}$, the emf changes to $E_2$. From the following, which one is the relationship between $E_1$ and $E_2$? (Given, $\frac{RT}{F} = 0.059$)

- **(1)** $E_1 > E_2$
- (2) $E_2 = 0 \neq E_1$
- (3) $E_1 = E_2$
- (4) $E_1 < E_2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{Zn|ZnSO_4(0.01\,M)||CuSO_4(1.0\,M)|Cu}$
2. $\therefore\ E_1 = E^{o}_{\mathrm{cell}} - \frac{2.303RT}{2\times F}\times\log\frac{(0.01)}{1}$
3. When concentrations are changed
4. $\therefore\ E_2 = E^{o}_{\mathrm{cell}} - \frac{2.303RT}{2F}\times\log\frac{1}{0.01}$
5. i.e., $E_1 > E_2$

**Solved independently** (answer withheld)

1. Cell reaction: $\mathrm{Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu}$, with $n = 2$.
2. Nernst equation: $E = E^\circ_{cell} - \frac{0.059}{2}\log\frac{[\mathrm{Zn^{2+}}]}{[\mathrm{Cu^{2+}}]}$.
3. For $E_1$: $E_1 = E^\circ_{cell} - \frac{0.059}{2}\log\frac{0.01}{1.0} = E^\circ_{cell} - \frac{0.059}{2}(-2) = E^\circ_{cell} + 0.059\,\mathrm{V}$.
4. For $E_2$: $E_2 = E^\circ_{cell} - \frac{0.059}{2}\log\frac{1.0}{0.01} = E^\circ_{cell} - \frac{0.059}{2}(2) = E^\circ_{cell} - 0.059\,\mathrm{V}$.
5. $E_1 - E_2 = 0.118\,\mathrm{V} > 0$, so $E_1 > E_2$, which is option $1$.

**Subtopic:** Nernst Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q144_73c8a2c7_30102026.png?v=73c8a2c710e8)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q144_03ca5e51_30102026.png?v=03ca5e51c595)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Nernst equation for the Daniell cell: the emf falls as the ratio [Zn2+]/[Cu2+] rises, so exchanging 0.01 M and 1.0 M between the half-cells lowers the emf
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  A student who builds the quotient from the metals -- copper ion over zinc ion -- flips the sign of the log term and so flips the comparison; with $Q=\frac{[Zn^{2+}]}{[Cu^{2+}]}$ the first cell has $Q=0.01$ and the second $Q=100$, giving $E_1 = E^\circ + 0.059$ V against $E_2 = E^\circ - 0.059$ V.
- **Why:** This question requires the Nernst equation applied to two concentration sets and the two emfs then compared, demonstrated by the options being the four possible relations between $E_1$ and $E_2$.
<!--/ecat-->

## Q145

Chemistry · organic · General Organic Chemistry

The correct statement regarding electrophile is

- (1) Electrophiles are generally neutral species and can form a bond by accepting a pair of electrons from a nucleophile
- **(2)** Electrophile can be either neutral or positively charged species and can form a bond by accepting a pair of electrons from a nucleophile
- (3) Electrophile is a negatively charged species and can form a bond by accepting a pair of electrons from a nucleophile
- (4) Electrophile is a negatively charged species and can form a bond by accepting a pair of electrons from another electrophile

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Fact.

**Solved independently** (answer withheld)

1. An electrophile is an electron-seeking species that accepts an electron pair from a nucleophile; it can be positively charged (e.g. $\mathrm{H^+}$, $\mathrm{NO_2^+}$) or neutral (e.g. $\mathrm{BF_3}$, carbonyl carbon $>\mathrm{C{=}O}$), so option $2$ is correct while options $1$, $3$ and $4$ are wrong.

**Subtopic:** Electrophile and Nucleophile · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q145_46360738_30102026.png?v=463607380f7e)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q145_4d8c57b8_30102026.png?v=4d8c57b82062)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An electrophile is an electron-pair acceptor, and it may be positively charged, as NO2+ and a carbocation are, or neutral with an empty or polarised orbital, as BF3 and AlCl3 are
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  BF3, AlCl3 and SO3 are the electrophiles stored as neutral molecules, so 'generally neutral species' reads as the careful answer; the clause shuts out NO2+ and the carbocation, which is exactly why the key says 'either neutral or positively charged'.
- **Why:** This question requires the two-part definition of an electrophile -- its charge and what it does with electrons -- demonstrated by the options differing in the charge clause while three of them repeat 'accepting a pair of electrons from a nucleophile'.
<!--/ecat-->

## Q146

Chemistry · inorganic · Coordination Compounds – Practice

The correct order of the stoichiometries of $\mathrm{AgCl}$ formed when $\mathrm{AgNO_3}$ in excess is treated with the complexes : $\mathrm{CoCl_3\cdot 6NH_3}$, $\mathrm{CoCl_3\cdot 5NH_3}$, $\mathrm{CoCl_3\cdot 4NH_3}$ respectively is

- **(1)** 3 $\mathrm{AgCl}$, 2 $\mathrm{AgCl}$, 1 $\mathrm{AgCl}$
- (2) 2 $\mathrm{AgCl}$, 3 $\mathrm{AgCl}$, 1 $\mathrm{AgCl}$
- (3) 1 $\mathrm{AgCl}$, 3 $\mathrm{AgCl}$, 2 $\mathrm{AgCl}$
- (4) 3 $\mathrm{AgCl}$, 1 $\mathrm{AgCl}$, 2 $\mathrm{AgCl}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Complexes are respectively $\mathrm{[Co(NH_3)_6]Cl_3}$, $\mathrm{[Co(NH_3)_5Cl]Cl_2}$ and $\mathrm{[Co(NH_3)_4Cl_2]Cl}$

**Solved independently** (answer withheld)

1. Co(III) has coordination number $6$; ligands not filled by $\mathrm{NH_3}$ are filled by $\mathrm{Cl^-}$ inside the coordination sphere, and only $\mathrm{Cl^-}$ outside the sphere precipitates as $\mathrm{AgCl}$.
2. $\mathrm{CoCl_3\cdot 6NH_3} = [\mathrm{Co(NH_3)_6}]\mathrm{Cl_3}$, so $3$ ionisable $\mathrm{Cl^-}$ give $3\,\mathrm{AgCl}$.
3. $\mathrm{CoCl_3\cdot 5NH_3} = [\mathrm{Co(NH_3)_5Cl}]\mathrm{Cl_2}$, so $2$ ionisable $\mathrm{Cl^-}$ give $2\,\mathrm{AgCl}$.
4. $\mathrm{CoCl_3\cdot 4NH_3} = [\mathrm{Co(NH_3)_4Cl_2}]\mathrm{Cl}$, so $1$ ionisable $\mathrm{Cl^-}$ gives $1\,\mathrm{AgCl}$.
5. The order $3\,\mathrm{AgCl}, 2\,\mathrm{AgCl}, 1\,\mathrm{AgCl}$ is option $1$.

**Subtopic:** Werner’s Theory and Applications of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q146_97e33a53_30102026.png?v=97e33a534d00)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q146_bd550789_30102026.png?v=bd55078910f3)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Only the chlorides outside the coordination sphere are ionisable and precipitate with AgNO3, so with cobalt holding a coordination number of six the three complexes give three, two and one AgCl
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Three misreadings were worked through against the printed options: counting the chlorides locked inside the sphere gives 0, 1, 2; counting the ammine ligands gives 6, 5, 4; reversing the respectively-order gives 1, 2, 3. None of those three lines is printed, and the wrong options are permutations of 3, 2, 1 that no single consistent rule produces.
- **Why:** This question requires Werner's ionisable-chloride count applied to three complexes at once, demonstrated by the stem's 'respectively' and by each option printing three stoichiometries.
- **Note:** All three wrong options are permutations of the keyed values 3, 2, 1, and the straight reversal 1, 2, 3 is not among them, so the usual order distractor is absent from this printing.
<!--/ecat-->

## Q147

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

The IUPAC name of the compound [figure] is ________.

![printed figure: (4E)-2-methyl-3-oxohex-4-enal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q147_481a218e_30102026.svg?v=481a218ea019)

*(4E)-2-methyl-3-oxohex-4-enal*

![drawn: (4E)-2-methyl-3-oxohex-4-enal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q147_question_9cf905f6_30102026.svg?v=9cf905f6693b)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: (4E)-2-methyl-3-oxohex-4-enal `C/C=C/C(=O)C(C)C=O` ![(4E)-2-methyl-3-oxohex-4-enal](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q147_question_s1_e7e47b95_30102026.svg?v=e7e47b95c8d7)

- (1) 5-methyl-4-oxohex-2-en-5-al
- (2) 3-keto-2-methylhex-5-enal
- **(3)** 3-keto-2-methylhex-4-enal
- (4) 5-formylhex-2-en-3-one

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: (4E)-2-methyl-3-oxohex-4-enal with printed carbon numbers: 1 beside the methyl branch, 2 at the CH bearing it, 3 at the ketone carbon, 4 and 5 at the CH=CH carbons, 6 at the terminal CH3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q147_sol_1_d4bd0812_30102026.svg?v=d4bd0812313e)

*(4E)-2-methyl-3-oxohex-4-enal with printed carbon numbers: 1 beside the methyl branch, 2 at the CH bearing it, 3 at the ketone carbon, 4 and 5 at the CH=CH carbons, 6 at the terminal CH3*

![drawn: (4E)-2-methyl-3-oxohex-4-enal with printed carbon numbers: 1 beside the methyl branch, 2 at the CH bearing it, 3 at the ketone carbon, 4 and 5 at the CH=CH carbons, 6 at the terminal CH3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q147_solution_1_442aa061_30102026.svg?v=442aa0610fec)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Aldehydes get higher priority over ketone and alkene in numbering of principal C-chain.
2. $\therefore$ 3-keto-2-methylhex-4-enal

**Solved independently** (answer withheld)

1. From the figure the compound is $\mathrm{OHC{-}CH(CH_3){-}CO{-}CH{=}CH{-}CH_3}$.
2. The aldehyde $\mathrm{-CHO}$ outranks the ketone, so it is the principal group, the suffix is $-\text{al}$ and the CHO carbon is $C_1$.
3. The longest chain containing $C_1$ and the $C{=}C$ has six carbons: $C_1$ (CHO), $C_2$ (CH with $\mathrm{CH_3}$), $C_3$ (C=O), $C_4{=}C_5$, $C_6$ ($\mathrm{CH_3}$).
4. Substituents: methyl at $C_2$, oxo (keto) at $C_3$; double bond starts at $C_4$, so parent is hex-4-enal.
5. Name: $2$-methyl-$3$-oxohex-$4$-enal, which matches option $3$ (3-keto-2-methylhex-4-enal).

**Subtopic:** Nomenclature of Organic Compounds Having Functional Group(s) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q147_76f0989b_30102026.png?v=76f0989b4775)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q147_9159aa74_30102026.png?v=9159aa74df17)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** IUPAC numbering starts from the principal characteristic group: with an aldehyde present the CHO carbon is C1 and takes the suffix, the ketone drops to an oxo (keto) prefix, and the chain is numbered from that end
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Numbering a chain so the double bond gets the lowest locant is a real rule, and running the numbering from the methyl end gives 5-methyl, 4-oxo and hex-2-ene, all three printed in this option; the aldehyde outranks everything here, so C1 is the CHO carbon and the double bond sits at 4.
- **Why:** This question requires IUPAC's numbering and suffix convention applied to the drawn structure, demonstrated by the four options differing only in which group takes the suffix and where the locants fall.
- **Note:** The figure was supplied and read. The keyed option uses the older 'keto' prefix where current IUPAC prints 'oxo', and no option carries the (4E) descriptor the drawn geometry supports; option 3 is still the only name consistent with the drawn skeleton, and the tag follows the printed key.
<!--/ecat-->

## Q148

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The species, having bond angles of $120^\circ$ is

- (1) $\mathrm{NCl_3}$
- **(2)** $\mathrm{BCl_3}$
- (3) $\mathrm{PH_3}$
- (4) $\mathrm{ClF_3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: trichloroborane ($\ce{BCl3}$) drawn trigonal planar, with the Cl–B–Cl bond angle marked 120°](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q148_sol_1_ccc89c2c_30102026.svg?v=ccc89c2c3ef7)

*trichloroborane ($\ce{BCl3}$) drawn trigonal planar, with the Cl–B–Cl bond angle marked 120°*

![drawn: trichloroborane ($\ce{BCl3}$) drawn trigonal planar, with the Cl–B–Cl bond angle marked 120°](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q148_solution_1_7d716837_30102026.svg?v=7d716837e6bc)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. $\mathrm{BCl_3}$: B has 3 bond pairs and 0 lone pairs, so it is $sp^2$ hybridised and trigonal planar with $\angle \mathrm{Cl\text{-}B\text{-}Cl} = 120^\circ$.
2. $\mathrm{NCl_3}$: N has 3 bond pairs and 1 lone pair, so it is trigonal pyramidal with bond angle about $107^\circ$, less than $120^\circ$.
3. $\mathrm{PH_3}$: P has 3 bond pairs and 1 lone pair, so it is pyramidal with bond angle about $93.5^\circ$.
4. $\mathrm{ClF_3}$: Cl has 3 bond pairs and 2 lone pairs ($sp^3d$), so it is T-shaped with $\angle \mathrm{F\text{-}Cl\text{-}F} \approx 87.5^\circ$.
5. Only $\mathrm{BCl_3}$ has $120^\circ$ bond angles, which is option $2$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q148_0b7caac0_30102026.png?v=0b7caac05fdf)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q148_df5b4361_30102026.png?v=df5b4361bceb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** VSEPR counts electron pairs and not bonded atoms: three bond pairs with no lone pair give a trigonal planar shape at 120 degrees, and every lone pair squeezes the bond angle below the ideal value
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Three chlorines around a central atom reads as trigonal planar, so a student counting bonded atoms instead of electron pairs gives NCl3 an angle of 120 degrees; nitrogen also carries a lone pair, which makes the molecule pyramidal with angles near 107 degrees.
- **Why:** This question requires VSEPR applied to four named species, demonstrated by the stem asking for 'the species, having bond angles of 120' with no geometry supplied in the stem.
<!--/ecat-->

## Q149

Chemistry · physical · Chemical Equilibrium

The equilibrium constants of the following are
$\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$ $\quad K_1$
$\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$ $\quad K_2$
$\mathrm{H_2 + \frac{1}{2}O_2 \longrightarrow H_2O}$ $\quad K_3$
The equilibrium constant $(K)$ of the reaction
$\mathrm{2NH_3 + \frac{5}{2}O_2 \overset{K}{\rightleftharpoons} 2NO + 3H_2O}$, will be

- (1) $K_2K_3/K_1$
- (2) $K_2^3K_3/K_1$
- (3) $K_1K_3^3/K_2$
- **(4)** $K_2K_3^3/K_1$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (I) $\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$; $K_1 = \frac{[\mathrm{NH_3}]^2}{[\mathrm{N_2}][\mathrm{H_2}]^3}$
2. (II) $\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$; $K_2 = \frac{[\mathrm{NO}]^2}{[\mathrm{N_2}][\mathrm{O_2}]}$
3. (III) $\mathrm{H_2 + \frac{1}{2}O_2 \longrightarrow H_2O}$; $K_3 = \frac{[\mathrm{H_2O}]}{[\mathrm{H_2}][\mathrm{O_2}]^{1/2}}$
4. $(\mathrm{II} + 3 \times \mathrm{III} - \mathrm{II})$ will give
5. $\mathrm{2NH_3 + \frac{5}{2}O_2 \overset{K}{\rightleftharpoons} 2NO + 3H_2O}$;
6. $\therefore\ K = K_2 \times K_3^3 / K_1$

**Solved independently** (answer withheld)

1. Reversing reaction 1 gives $\mathrm{2NH_3 \rightleftharpoons N_2 + 3H_2}$ with constant $\frac{1}{K_1}$.
2. Reaction 2 is used as written: $\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$ with constant $K_2$.
3. Multiplying reaction 3 by 3 gives $\mathrm{3H_2 + \frac{3}{2}O_2 \rightleftharpoons 3H_2O}$ with constant $K_3^3$.
4. Adding the three: $\mathrm{2NH_3 + \frac{5}{2}O_2 \rightleftharpoons 2NO + 3H_2O}$ ($N_2$ and $3H_2$ cancel, $O_2$ totals $1 + \frac{3}{2} = \frac{5}{2}$).
5. Constants multiply when reactions add: $K = \frac{1}{K_1} \cdot K_2 \cdot K_3^3 = \frac{K_2 K_3^3}{K_1}$, which is option $4$.

**Subtopic:** Law of Chemical Equilibrium · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 27)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q149_fca8456e_30102026.png?v=fca8456e341a)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q149_e0791d80_30102026.png?v=e0791d8098ac)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Adding reactions multiplies their equilibrium constants: reversing a step inverts its K, and taking a step n times raises its K to the nth power
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Reversing reaction 1 and adding reactions 2 and 3 does build the target, so a student who stops there writes $K_2K_3/K_1$; reaction 3 has to be taken three times to supply the 3 H2O, and that puts the power 3 on $K_3$.
- **Why:** This question requires the three printed equilibria combined into the target reaction and their constants combined the same way, demonstrated by the options being four arrangements of $K_1$, $K_2$ and $K_3$.
<!--/ecat-->

## Q150

Chemistry · inorganic · The p–Block Elements

Name the gas that can readily decolourises acidified $\mathrm{KMnO_4}$ solution:

- (1) $\mathrm{NO_2}$
- (2) $\mathrm{P_2O_5}$
- (3) $\mathrm{CO_2}$
- **(4)** $\mathrm{SO_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{SO_2}$ is readily decolourises acidified $\mathrm{KMnO_4}$.

**Solved independently** (answer withheld)

1. Acidified $\mathrm{KMnO_4}$ loses its purple colour only when a reducing agent reduces $\mathrm{MnO_4^-}$ to colourless $\mathrm{Mn^{2+}}$.
2. $\mathrm{P_2O_5}$ (P in $+5$) and $\mathrm{CO_2}$ (C in $+4$) are in their highest oxidation states, so they cannot act as reducing agents.
3. $\mathrm{SO_2}$ (S in $+4$) is readily oxidised to $\mathrm{SO_4^{2-}}$ (S in $+6$): $2\mathrm{MnO_4^-} + 5\mathrm{SO_2} + 2\mathrm{H_2O} \rightarrow 2\mathrm{Mn^{2+}} + 5\mathrm{SO_4^{2-}} + 4\mathrm{H^+}$.
4. So the gas that readily decolourises acidified $\mathrm{KMnO_4}$ is $\mathrm{SO_2}$, which is option $4$.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q150_cd7bab2f_30102026.png?v=cd7bab2f679f)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q150_56141555_30102026.png?v=56141555acf5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** SO2 is a reducing agent: sulphur(IV) is oxidised to sulphate and reduces MnO4- to Mn2+, so acidified permanganate loses its purple colour
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Nitrogen in NO2 sits at +4 with +5 still above it, so a student choosing by 'an oxide whose element can still be oxidised' reaches for the other reactive p-block oxide gas; the equation printed for this test is $5SO_2 + 2MnO_4^- + 2H_2O \to 5SO_4^{2-} + 2Mn^{2+} + 4H^+$, and in acid NO2 is handled as the oxidising agent.
- **Why:** This question requires the reducing behaviour the chapter prints for one named gas, demonstrated by the stem's 'readily decolourises acidified KMnO4 solution'. Swap test applied: replacing NO2 with an unlike name keeps the pull, because what carries the student is 'the other oxidisable oxide in the same chapter', so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q151

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

The most suitable method of separation of $1 : 1$ mixture of ortho and para-nitrophenols is

- (1) Crystallisation
- **(2)** Steam distillation
- (3) Sublimation
- (4) Chromatography

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Steam distillation is the most suitable method of separation of $1 : 1$ mixture of ortho and para nitrophenols as there is intramolecular H-bonds in ortho nitrophenol.

**Solved independently** (answer withheld)

1. In $o$-nitrophenol the $-\mathrm{OH}$ and $-\mathrm{NO_2}$ groups are adjacent, so it forms an intramolecular hydrogen bond (chelation) and exists as discrete molecules with a low boiling point, making it steam volatile.
2. In $p$-nitrophenol the groups are far apart, so it forms intermolecular hydrogen bonds, giving molecular association, a higher boiling point and no steam volatility.
3. A mixture of a steam-volatile and a non-steam-volatile compound is separated by steam distillation, so $o$-nitrophenol distils over and $p$-nitrophenol stays behind; this is option $2$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q151_86e5468d_30102026.png?v=86e5468d17d4)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q151_0df4ae69_30102026.png?v=0df4ae698c38)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** o-Nitrophenol is steam-volatile because its OH is locked to the nitro group by an intramolecular hydrogen bond, while the para isomer is held in an intermolecular network, so steam distillation separates the pair
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Both isomers are solids, and the method the chapter files against solids of differing solubility is crystallisation, so a student choosing from that printed list of four methods takes the one filed under solids; this pair is printed under steam distillation, because only the ortho isomer travels over with the steam.
- **Why:** This question requires the purification method the chapter assigns to this named pair, demonstrated by the stem's '1 : 1 mixture of ortho and para-nitrophenols' and its request for 'the most suitable method of separation'. Swap test applied: replacing 'Crystallisation' with an unlike word keeps the pull, because position in the chapter's printed list of methods is what carries the student, so nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q152

Chemistry · inorganic · The D- and F-Block Elements – Practice

The reason for greater range of oxidation states in actinoids is attributed to

- **(1)** $5f$, $6d$ and $7s$ levels having comparable energies
- (2) $4f$ and $5d$ levels being close in energies
- (3) The radioactive nature of actinoids
- (4) Actinoid contraction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. It is a fact.

**Solved independently** (answer withheld)

1. In actinoids the $5f$, $6d$ and $7s$ energy levels have comparable energies, so electrons from all three can be used in bonding, giving a greater range of oxidation states; this is option $1$ (option $2$ describes lanthanoids, and radioactivity or actinoid contraction do not explain it).

**Subtopic:** Lanthanoids & Actinoids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q152_bf5d0ad9_30102026.png?v=bf5d0ad9f105)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q152_41cacc36_30102026.png?v=41cacc367763)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In the actinoids the 5f, 6d and 7s levels lie close enough in energy for electrons from all three to take part in bonding, which is why their range of oxidation states is wider than the lanthanoids'
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  The sentence being reached for is 'the levels are comparable in energy', and this option prints that sentence with the lanthanoid quantum numbers in it; the actinoid line names 5f, 6d and 7s, and it is the lanthanoids whose +3 state dominates precisely because their levels are not as close.
- **Why:** This question requires the cause the chapter gives for a stated property, demonstrated by the stem 'The reason for greater range of oxidation states in actinoids is attributed to'. Swap test applied: replacing '4f and 5d' with two unlike words kills the pull, because the option works by resembling the right orbital set, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q153

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The element $Z = 114$ has been discovered recently. It will belong to which of the following family group and electronic configuration?

- (1) Oxygen family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{4}$
- (2) Nitrogen family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{6}$
- (3) Halogen family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{5}$
- **(4)** Carbon family, $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $Z = 114$ belong to Group $14$, carbon family
2. Electronic configuration $= [\mathrm{Rn}]5f^{14}6d^{10}7s^{2}7p^{2}$

**Solved independently** (answer withheld)

1. The preceding noble gas is radon, $Z = 86$, so $114 - 86 = 28$ electrons lie beyond the $[\mathrm{Rn}]$ core.
2. Filling in order $7s \to 5f \to 6d \to 7p$: $2 + 14 + 10 = 26$, leaving $28 - 26 = 2$ electrons in $7p$.
3. Configuration: $[\mathrm{Rn}]\,5f^{14}6d^{10}7s^{2}7p^{2}$, i.e. valence shell $ns^{2}np^{2}$.
4. An $ns^{2}np^{2}$ valence shell is group $14$, the carbon family, which is option $4$.

**Subtopic:** Electronic Configurations · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q153_0f611914_30102026.png?v=0f611914aa2f)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q153_2c612c10_30102026.png?v=2c612c1041c9)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Filling past [Rn] runs 5f14, 6d10, 7s2, which reaches element 112, so Z = 114 adds two 7p electrons and lands in group 14, under lead
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  How far 114 sits into the p block is the whole job, and taking the d block to close at 110 instead of 112 puts it four places in, which gives 7p4 and the oxygen family -- the pair that belongs to element 116; [Rn] is 86, and 86 + 14 + 10 + 2 = 112, so only two 7p electrons are left to add.
- **Why:** This question requires the aufbau filling applied past [Rn] and the group then read off the result, demonstrated by the stem asking for 'which ... family group and electronic configuration' with both printed in every option.
<!--/ecat-->

## Q154

Chemistry · physical · Chemical Kinetics

Mechanism of a hypothetical reaction $\mathrm{X_2 + Y_2 \rightarrow 2XY}$ is given below :
(i) $\mathrm{X_2 \rightarrow X + X}$ (fast)
(ii) $\mathrm{X + Y_2 \rightleftharpoons XY + Y}$ (slow)
(iii) $\mathrm{X + Y \rightarrow XY}$ (fast)
The overall order of the reaction will be

- (1) 0
- **(2)** 1.5
- (3) 1
- (4) 2

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The solution of this question is given by assuming step (i) to be reversible which is not given in question
2. Overall rate = Rate of slowest step (ii)
3. $= k[\mathrm{X}]\,[\mathrm{Y_2}]$ ...(1)
4. $k$ = rate constant of step (ii)
5. Assuming step (i) to be reversible, its equilibrium constant,
6. $k_{eq} = \frac{[\mathrm{X}]^{2}}{[\mathrm{X_2}]} \Rightarrow [\mathrm{X}] = k_{eq}^{\frac{1}{2}}[\mathrm{X_2}]^{\frac{1}{2}}$ ...(2)
7. Put (2) in (1)
8. Rate $= kk_{eq}^{\frac{1}{2}}[\mathrm{X_2}]^{\frac{1}{2}}[\mathrm{Y_2}]$
9. Overall order $= \frac{1}{2} + 1 = \frac{3}{2}$

**Solved independently** (answer withheld)

1. The rate-determining step is the slow step (ii), so $\text{Rate} = k[\mathrm{X}][\mathrm{Y_2}]$.
2. $\mathrm{X}$ is an intermediate; treat the fast step (i) as a pre-equilibrium: $K = \frac{[\mathrm{X}]^2}{[\mathrm{X_2}]}$.
3. $[\mathrm{X}] = K^{1/2}[\mathrm{X_2}]^{1/2}$.
4. $\text{Rate} = kK^{1/2}[\mathrm{X_2}]^{1/2}[\mathrm{Y_2}] = k'[\mathrm{X_2}]^{1/2}[\mathrm{Y_2}]$.
5. Overall order $= \frac{1}{2} + 1 = 1.5$, which is option $2$.

**Subtopic:** Order of a Reaction · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 27)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q154_6d893483_30102026.png?v=6d893483fdcd)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q154_afb0b8ad_30102026.png?v=afb0b8ad3954)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The rate law comes from the slow step, but an intermediate cannot stand in it: replacing [X] from the fast X2 dissociation equilibrium puts a half power on [X2] and makes the overall order 1.5
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Reading the orders straight off the slow step gives rate = k[X][Y2] and 1 + 1 = 2; X is an intermediate, and substituting $[X] = K^{1/2}[X_2]^{1/2}$ from the fast first step turns the order into 1.5.
- **Why:** This question requires the rate law built from the slow step with the intermediate eliminated, demonstrated by step (ii) being marked '(slow)' and containing X, which step (i) produces.
<!--/ecat-->

## Q155

Chemistry · physical · Solutions

If molality of the dilute solution is doubled, the value of molal depression constant ($K_f$) will be

- (1) Tripled
- **(2)** Unchanged
- (3) Doubled
- (4) Halved

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $K_f$ (molal depression constant) is a characteristic of solvent and is independent of molality.

**Solved independently** (answer withheld)

1. $K_f = \frac{R \, M_1 \, T_f^2}{1000 \, \Delta_{fus}H}$ depends only on the solvent (its molar mass, freezing point and enthalpy of fusion), not on molality $m$, so doubling $m$ doubles $\Delta T_f = K_f m$ but leaves $K_f$ unchanged, which is option $2$.

**Subtopic:** Depression of Freezing Point · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q155_36ace126_30102026.png?v=36ace126f5e2)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q155_f1732ce5_30102026.png?v=f1732ce59542)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The molal depression constant is a property of the solvent alone, so changing how much solute is dissolved does not change it; what doubles is the freezing-point depression
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  "Doubled" is what happens to $\Delta T_f$ when the molality doubles, and the doubling is transferred from the quantity on the left of $\Delta T_f = K_f m$ to the constant on the right
- **Why:** This question requires knowing which side of $\Delta T_f = K_f m$ changes with concentration, demonstrated by the stem's "If molality of the dilute solution is doubled, the value of molal depression constant ($K_f$) will be".
<!--/ecat-->

## Q156

Chemistry · organic · Hydrocarbons

With respect to the conformers of ethane, which of the following statements is true?

- (1) Both bond angle and bond length change
- **(2)** Both bond angles and bond length remains same
- (3) Bond angle remains same but bond length changes
- (4) Bond angle changes but bond length remains same

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. There is no change in bond angles and bond lengths in the conformations of ethane.
2. There is only change in dihedral angle.

**Solved independently** (answer withheld)

1. Conformers of ethane are interconverted only by free rotation about the $\mathrm{C-C}$ $\sigma$ bond, which changes just the dihedral (torsional) angle between the $\mathrm{C-H}$ bonds on adjacent carbons; the bond angles and bond lengths stay the same, which is option $2$.

**Subtopic:** Isomerism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q156_e3e46e82_30102026.png?v=e3e46e820b02)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q156_90a60af7_30102026.png?v=90a60af76a8e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Conformers of ethane differ only by rotation about the C-C single bond, so every bond length and bond angle stays the same and only the torsion angle between the two CH3 groups changes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Rotation about the C-C bond does change an angle — the torsion angle — and that is read as the bond angle changing, while the option's other half, the bond length staying put, is correct and carries the whole option
- **Why:** This question requires the defining fact about conformers, demonstrated by the stem asking which statement is true "with respect to the conformers of ethane" against option 2's "Both bond angles and bond length remains same".
- **Note:** look_alike_term was considered for option 4, since "bond angle" and "torsion angle" share the word angle. half_right is recorded because the option prints two separate claims and one of them, the unchanged bond length, is correct and is what lets the wrong claim pass; the angle likeness is given in the route.
<!--/ecat-->

## Q157

Chemistry · organic · Alcohols, Phenols and Ethers

The heating of phenyl-methyl ethers with $\mathrm{HI}$ produces.

- **(1)** Phenol
- (2) Benzene
- (3) Ethyl chlorides
- (4) Iodobenzene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: anisole →(HI) phenol + iodomethane ($\ce{CH3I}$)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q157_sol_1_4035bd7b_30102026.svg?v=4035bd7b4cf4)

*anisole →[HI] phenol + iodomethane ($\ce{CH3I}$)*

![drawn: anisole →(HI) phenol + iodomethane ($\ce{CH3I}$)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q157_solution_1_9849ef64_30102026.svg?v=9849ef64f597)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. Phenyl methyl ether is anisole, $\mathrm{C_6H_5{-}O{-}CH_3}$.
2. The ether oxygen is protonated by $\mathrm{HI}$: $\mathrm{C_6H_5{-}\overset{+}{O}H{-}CH_3}$.
3. The $\mathrm{O{-}C_6H_5}$ bond has partial double-bond character (resonance) and an $S_N$ attack on the sp$^2$ ring carbon is not possible, so $\mathrm{I^-}$ attacks the methyl carbon.
4. $\mathrm{C_6H_5OCH_3 + HI \xrightarrow{\Delta} C_6H_5OH + CH_3I}$, so the product is phenol, option $1$.

**Subtopic:** Reactions of Ethers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q157_0d4413b3_30102026.png?v=0d4413b346d8)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q157_33910e02_30102026.png?v=33910e0284e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** HI cleaves an ether at the alkyl carbon, because that is where iodide can substitute; an aryl alkyl ether therefore gives the phenol and the alkyl iodide, never the aryl iodide
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  The iodide is sent to the ring carbon instead of the methyl carbon, which would break the aryl-oxygen bond and give iodobenzene with methanol
- **Why:** This question requires the regiochemistry of ether cleavage by hydroiodic acid, demonstrated by the stem's "heating of phenyl-methyl ethers with $\mathrm{HI}$" and the choice offered between phenol and iodobenzene.
- **Note:** Option 3 as printed, "Ethyl chlorides", names an element absent from the reagents and a group absent from the substrate; it is tagged as printed and recorded as a filler rather than re-judged.
<!--/ecat-->

## Q158

Chemistry · organic · Amines

The correct increasing order of basic strength for the following compounds is

![printed figure: (I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q158_7f60daa3_30102026.svg?v=7f60daa3a0c2)

*(I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline*

![drawn: (I) aniline; (II) 4-nitroaniline; (III) 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q158_question_9f95be4e_30102026.svg?v=9f95be4e596e)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: aniline `Nc1ccccc1` ![aniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q158_question_s1_1e3ada3e_30102026.svg?v=1e3ada3e29d0); 4-nitroaniline `Nc1ccc([N+](=O)[O-])cc1` ![4-nitroaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q158_question_s2_2b4e4196_30102026.svg?v=2b4e41963ced); 4-methylaniline `Cc1ccc(N)cc1` ![4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q158_question_s3_5f1a0db7_30102026.svg?v=5f1a0db74b01)

- (1) $\mathrm{III} < \mathrm{II} < \mathrm{I}$
- **(2)** $\mathrm{II} < \mathrm{I} < \mathrm{III}$
- (3) $\mathrm{II} < \mathrm{III} < \mathrm{I}$
- (4) $\mathrm{III} < \mathrm{I} < \mathrm{II}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $-\mathrm{NO_2}$ has strong $-R$ effect and $-\mathrm{CH_3}$ shows $+R$ effect.
2. $\therefore$ Order of basic strength is

![printed figure: 4-nitroaniline < aniline < 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q158_sol_1_e5339e88_30102026.svg?v=e5339e8891df)

*4-nitroaniline < aniline < 4-methylaniline*

![drawn: 4-nitroaniline < aniline < 4-methylaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q158_solution_1_b982d130_30102026.svg?v=b982d1309305)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. From the figure: $\mathrm{I}$ is aniline $\mathrm{C_6H_5NH_2}$, $\mathrm{II}$ is $p$-nitroaniline, $\mathrm{III}$ is $p$-toluidine ($p$-$\mathrm{CH_3C_6H_4NH_2}$).
2. The $p$-$\mathrm{NO_2}$ group is electron-withdrawing ($-M$, $-I$), so it reduces the availability of the lone pair on $\mathrm{N}$: $\mathrm{II}$ is less basic than $\mathrm{I}$.
3. The $p$-$\mathrm{CH_3}$ group is electron-donating ($+I$, hyperconjugation), so it increases the electron density on $\mathrm{N}$: $\mathrm{III}$ is more basic than $\mathrm{I}$.
4. Increasing order: $\mathrm{II} < \mathrm{I} < \mathrm{III}$, which is option $2$.

**Subtopic:** Chemical Reactions of Amines (Basicity, Alkylation and Acylation) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q158_5fb9bdc4_30102026.png?v=5fb9bdc44505)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q158_61f4cecc_30102026.png?v=61f4cecc8c95)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A para electron-donating methyl group makes the nitrogen lone pair more available and raises basicity, while a para nitro group withdraws it and lowers basicity, so 4-nitroaniline is the weakest base and 4-methylaniline the strongest
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  $\mathrm{III} < \mathrm{I} < \mathrm{II}$ is the correct ranking written from strongest to weakest, so the three compounds are placed right and the sequence is read off against the stem's "increasing"
- **Why:** This question requires the three anilines ranked by how substituents change the availability of the nitrogen lone pair, demonstrated by the stem's "correct increasing order of basic strength" with the figure supplying aniline, 4-nitroaniline and 4-methylaniline as I, II and III.
- **Note:** E1 recorded arrange_in_order; in the current vocabulary that lives on the asks axis, so qtype is mcq with asks: order. The figure was supplied as three drawn structures checked atom for atom against the print, so the compounds behind I, II and III were readable.
<!--/ecat-->

## Q159

Chemistry · inorganic · The p–Block Elements

In which pair of ions both the species contain $\mathrm{S-S}$ bond?

- (1) $\mathrm{S_2O_7^{2-}}$, $\mathrm{S_2O_8^{2-}}$
- (2) $\mathrm{S_4O_6^{2-}}$, $\mathrm{S_2O_7^{2-}}$
- (3) $\mathrm{S_2O_7^{2-}}$, $\mathrm{S_2O_3^{2-}}$
- **(4)** $\mathrm{S_4O_6^{2-}}$, $\mathrm{S_2O_3^{2-}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: disulfane-1,2-disulfonate, $\ce{(S4O6)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q159_sol_1_1908b00b_30102026.svg?v=1908b00bd92f)

*disulfane-1,2-disulfonate, $\ce{[S4O6]^{2-}}$*

![drawn: disulfane-1,2-disulfonate, $\ce{(S4O6)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q159_solution_1_5fc19093_30102026.svg?v=5fc190939b3f)  
*drawn on the booklet's geometry, checked against its SMILES*

![printed figure: thiosulfate, $\ce{(S2O3)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q159_sol_2_977e488a_30102026.svg?v=977e488a8959)

*thiosulfate, $\ce{[S2O3]^{2-}}$*

![drawn: thiosulfate, $\ce{(S2O3)^{2-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q159_solution_2_b1135cfa_30102026.svg?v=b1135cfab65d)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. $\mathrm{S_2O_7^{2-}}$ (pyrosulfate) has the structure $\mathrm{O_3S{-}O{-}SO_3}$, bridged by oxygen, so it has no $\mathrm{S{-}S}$ bond.
2. $\mathrm{S_2O_8^{2-}}$ (peroxodisulfate) has the structure $\mathrm{O_3S{-}O{-}O{-}SO_3}$, bridged by a peroxide link, so it has no $\mathrm{S{-}S}$ bond.
3. $\mathrm{S_2O_3^{2-}}$ (thiosulfate) has the structure $\mathrm{S{-}SO_3}$, a terminal S bonded to the central S, so it contains an $\mathrm{S{-}S}$ bond.
4. $\mathrm{S_4O_6^{2-}}$ (tetrathionate) has the structure $\mathrm{O_3S{-}S{-}S{-}SO_3}$, so it contains $\mathrm{S{-}S}$ bonds.
5. Only the pair $\mathrm{S_4O_6^{2-}}$, $\mathrm{S_2O_3^{2-}}$ has $\mathrm{S{-}S}$ bonds in both species, which is option $4$.

**Subtopic:** Allotropes, Oxyacids and Oxides of Sulphur · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q159_d34d51e3_30102026.png?v=d34d51e315d6)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q159_8692c7d5_30102026.png?v=8692c7d59397)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Thiosulphate and tetrathionate carry sulphur bonded directly to sulphur, while pyrosulphate is bridged through oxygen, S-O-S, and peroxodisulphate through a peroxide link, S-O-O-S
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Thiosulphate is the one ion whose S-S bond is remembered with certainty, and the pair is accepted on that member while pyrosulphate's bridge is assumed to be S-S because its formula begins with $\mathrm{S_2}$
- **Why:** This question requires the printed structures of four sulphur oxoanions, demonstrated by the stem asking in which pair "both the species contain $\mathrm{S-S}$ bond?".
- **Note:** E1 recorded plain_mcq, but each option is a pair of ions and both members must satisfy the stem, so the printed shape has two parts and two_part is recorded; the current qtype vocabulary has no pair value.
<!--/ecat-->

## Q160

Chemistry · physical · Solutions

Which of the following is dependent on temperature?

- (1) Mole fraction
- (2) Weight percentage
- (3) Molality
- **(4)** Molarity

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Molarity includes volume of solution which can change with change in temperature.

**Solved independently** (answer withheld)

1. Mole fraction $x = \frac{n_A}{n_A + n_B}$, weight percentage $= \frac{w_A}{w_{total}} \times 100$ and molality $m = \frac{n_{solute}}{W_{solvent}\,(\mathrm{kg})}$ use only moles and masses, which do not change with temperature.
2. Molarity $M = \frac{n_{solute}}{V_{solution}\,(\mathrm{L})}$ uses the volume of solution.
3. Volume expands or contracts with temperature, so $M$ changes with $T$; this is option $4$.

**Subtopic:** Molarity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q160_09162704_30102026.png?v=09162704603a)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q160_4cab2b59_30102026.png?v=4cab2b59fdb9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only molarity is defined through a volume, and volume expands on heating, so molarity changes with temperature while the mass- and mole-based measures do not
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Molality and molarity differ by two letters, and the student who has the rule "the volume-based one changes with temperature" but not which name carries the volume picks the wrong member of the pair
- **Why:** This question requires which concentration measure is defined through a volume, demonstrated by the stem's "Which of the following is dependent on temperature?" with mole fraction, weight percentage, molality and molarity as the options.
<!--/ecat-->

## Q161

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Of the following, which is the product formed when cyclohexanone undergoes aldol condensation followed by heating?

- (1) 2-cyclohexylcyclohexan-1-ol `OC1CCCCC1C1CCCCC1` ![2-cyclohexylcyclohexan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q161_option_1_s1_947f9300_30102026.svg?v=947f93008fab)
- (2) 2-(2-oxocyclohexylidene)cyclohexan-1-one `O=C1CCCCC1=C1CCCCC1=O` ![2-(2-oxocyclohexylidene)cyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q161_option_2_s1_a6a456c0_30102026.svg?v=a6a456c02b50)
- (3) 2-(2-hydroxycyclohexyl)cyclohexan-1-one `O=C1CCCCC1C1CCCCC1O` ![2-(2-hydroxycyclohexyl)cyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q161_option_3_s1_8f5ba25f_30102026.svg?v=8f5ba25fcac8)
- **(4)** 2-cyclohexylidenecyclohexan-1-one `O=C1CCCCC1=C1CCCCC1` ![2-cyclohexylidenecyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q161_option_4_s1_83d322a4_30102026.svg?v=83d322a49c6b)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: cyclohexanone + cyclohexanone →((i) $\ce{OH-}$ (ii) Δ) 2-cyclohexylidenecyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q161_sol_1_feb2eef2_30102026.svg?v=feb2eef21dc0)

*cyclohexanone + cyclohexanone →[(i) $\ce{OH-}$ (ii) Δ] 2-cyclohexylidenecyclohexan-1-one*

![drawn: cyclohexanone + cyclohexanone →((i) $\ce{OH-}$ (ii) Δ) 2-cyclohexylidenecyclohexan-1-one](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q161_solution_1_c3e11ded_30102026.svg?v=c3e11dede9c2)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. Base removes an $\alpha$-H from cyclohexanone, which gives an enolate (carbanion) at $C_2$.
2. This carbanion attacks the $C=O$ carbon of a second cyclohexanone, which gives the aldol 2-(1-hydroxycyclohexyl)cyclohexan-1-one (a $\beta$-hydroxy ketone).
3. On heating, the aldol loses $H_2O$ (the $OH$ on the ring carbon and the $\alpha$-H), which forms a $C=C$ conjugated with the $C=O$.
4. The product is 2-cyclohexylidenecyclohexan-1-one: one ring keeps its $C=O$ and is joined to the other ring by an exocyclic $C=C$. This is the structure in option $4$; options $1$ and $3$ still carry $OH$ groups and option $2$ has two $C=O$ groups, so none of them can form this way.

**Subtopic:** Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q161_1c547a8e_30102026.png?v=1c547a8e17c9)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q161_e0645aa9_30102026.png?v=e0645aa929f0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Aldol condensation joins two cyclohexanone molecules through the alpha carbon of one and the carbonyl carbon of the other, and heating dehydrates that beta-hydroxy ketone to the alpha,beta-unsaturated ketone
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and none of them was supplied to this step, so no option can be read and no route can be named
- **Why:** This question requires the product of a named carbonyl reaction after dehydration, demonstrated by the stem's "cyclohexanone undergoes aldol condensation followed by heating".
- **Note:** All four options_en values are empty strings and no figure was attached, so the option set is drawn structures this step was not given. The paper itself is intact, so this is not recorded as source damage. A reviewer holding the structures should check two mechanisms: whether the beta-hydroxy ketone, the aldol before the "followed by heating" step, is printed as an option, which would be a condition_missed route on the dehydration; and whether any option shows the new bond made at the carbonyl carbon of both rings or at a carbon other than the alpha carbon, which would be wrong_site_attacked.
<!--/ecat-->

## Q162

Chemistry · organic · Chemistry in Everyday Life

Mixture of chloroxylenol and terpineol acts as

- (1) Antipyretic
- (2) Antibiotic
- (3) Analgesic
- **(4)** Antiseptic

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Mixture of chloroxylenol and terpineol acts as antiseptic.

**Solved independently** (answer withheld)

1. The mixture of chloroxylenol and terpineol is the commercial preparation Dettol, which NCERT lists as an antiseptic, so the answer is option $4$.

**Subtopic:** Antiseptics and Disinfectants · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q162_fc1a7dbc_30102026.png?v=fc1a7dbca8d1)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q162_e2bf060c_30102026.png?v=e2bf060ce1ec)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chloroxylenol with terpineol is the chapter's named antiseptic mixture, applied to living tissue to stop microbes multiplying
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Antibiotics are the class printed immediately beside antiseptics in the antimicrobial section, and a student who knows chloroxylenol acts against bacteria picks the class whose job is described as killing bacteria
- **Why:** This question requires the drug class a named mixture belongs to, demonstrated by the stem's "Mixture of chloroxylenol and terpineol acts as".
<!--/ecat-->

## Q163

Chemistry · physical · Thermodynamics

For a given reaction, $\Delta H = 35.5\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S = 83.6\,\mathrm{JK^{-1}\,mol^{-1}}$. The reaction is spontaneous at : (Assume that $\Delta H$ and $\Delta S$ do not vary with temperature)

- (1) All temperatures
- (2) $T > 298\,\mathrm{K}$
- (3) $T < 425\,\mathrm{K}$
- **(4)** $T > 425\,\mathrm{K}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\because\ \Delta G = \Delta H - T\Delta S$
2. For a reaction to be spontaneous, $\Delta G = -\mathrm{ve}$
3. i.e., $\Delta H < T\Delta S$
4. $\therefore\ T > \frac{\Delta H}{\Delta S} = \frac{35.5 \times 10^{3}\,\mathrm{J}}{83.6\,\mathrm{JK^{-1}}}$
5. i.e., $T > 425\,\mathrm{K}$

**Solved independently** (answer withheld)

1. Spontaneity requires $\Delta G = \Delta H - T\Delta S < 0$.
2. Since $\Delta H > 0$ and $\Delta S > 0$, this holds when $T > \frac{\Delta H}{\Delta S}$.
3. Convert units: $\Delta H = 35.5\,\mathrm{kJ\,mol^{-1}} = 35500\,\mathrm{J\,mol^{-1}}$.
4. $T = \frac{35500}{83.6} \approx 424.6\,\mathrm{K} \approx 425\,\mathrm{K}$.
5. The reaction is spontaneous for $T > 425\,\mathrm{K}$, which is option $4$.

**Subtopic:** Gibbs Energy and Spontaneity · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q163_2f0f4239_30102026.png?v=2f0f42391f68)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q163_7ecda033_30102026.png?v=7ecda03331fa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With both the enthalpy and the entropy change positive, $\Delta G = \Delta H - T\Delta S$ turns negative only above the crossover temperature $\Delta H/\Delta S$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The crossover temperature is worked out correctly as 425 K and then the inequality is written the wrong way round, as though spontaneity were lost rather than gained on heating
- **Why:** This question requires the crossover temperature from $\Delta G = \Delta H - T\Delta S$ with the units reconciled, demonstrated by the stem giving "$\Delta H = 35.5\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S = 83.6\,\mathrm{JK^{-1}\,mol^{-1}}$" and asking when "the reaction is spontaneous".
<!--/ecat-->

## Q164

Chemistry · inorganic · The p–Block Elements

$\mathrm{HgCl_2}$ and $\mathrm{I_2}$ both when dissolved in water containing $\mathrm{I^-}$ ions the pair of species formed is

- **(1)** $\mathrm{HgI_4^{2-}}$, $\mathrm{I_3^-}$
- (2) $\mathrm{Hg_2I_2}$, $\mathrm{I^-}$
- (3) $\mathrm{HgI_2}$, $\mathrm{I_3^-}$
- (4) $\mathrm{HgI_2}$, $\mathrm{I^-}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In a solution containing $\mathrm{HgCl_2}$, $\mathrm{I_2}$ and $\mathrm{I^-}$, both $\mathrm{HgCl_2}$ and $\mathrm{I_2}$ compete for $\mathrm{I^-}$.
2. Since formation constant of $\mathrm{[HgI_4]^{2-}}$ is $1.9 \times 10^{30}$ which is very large as compared with $\mathrm{I_3^-}$ ($K_{\mathrm{f}} = 700$)
3. $\therefore$ $\mathrm{I^-}$ will preferentially combine with $\mathrm{HgCl_2}$.
4. $\mathrm{HgCl_2 + 2I^- \rightarrow \underset{\text{Red ppt}}{HgI_2}\downarrow + 2Cl^-}$
5. $\mathrm{HgI_2 + 2I^- \rightarrow \underset{\text{soluble}}{[HgI_4]^{2-}}}$

**Solved independently** (answer withheld)

1. $\mathrm{HgCl_2 + 2I^- \rightarrow HgI_2\downarrow + 2Cl^-}$ (red precipitate).
2. With excess $\mathrm{I^-}$ the precipitate dissolves: $\mathrm{HgI_2 + 2I^- \rightarrow [HgI_4]^{2-}}$.
3. Iodine dissolves in iodide solution as triiodide: $\mathrm{I_2 + I^- \rightarrow I_3^-}$.
4. The pair of species formed is $\mathrm{HgI_4^{2-}}$ and $\mathrm{I_3^-}$, which is option $1$.

**Subtopic:** Interhalogen Compounds & Important Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q164_e39e4a62_30102026.png?v=e39e4a6258f4)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q164_37d7f197_30102026.png?v=37d7f19724ba)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Excess iodide takes mercury(II) past the red $\mathrm{HgI_2}$ precipitate to the soluble tetraiodomercurate(II) ion, and it takes iodine to the triiodide ion
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The iodine half is right, $\mathrm{I_3^-}$, and the mercury half stops at the red precipitate $\mathrm{HgI_2}$ that forms before the excess iodide dissolves it, so the correct member vouches for the incomplete one
- **Why:** This question requires the products both substrates give with excess iodide, demonstrated by the stem's "$\mathrm{HgCl_2}$ and $\mathrm{I_2}$ both when dissolved in water containing $\mathrm{I^-}$ ions the pair of species formed is".
- **Note:** E1 recorded plain_mcq, but each option is a pair of species and both members must be right, so the printed shape has two parts and two_part is recorded; the current qtype vocabulary has no pair value.
<!--/ecat-->

## Q165

Chemistry · physical · Chemical Kinetics

A first order reaction has a specific reaction rate of $10^{-2}\,\mathrm{s^{-1}}$. How much time will it take for $20\,\mathrm{g}$ of the reactant to reduce to $5\,\mathrm{g}$?

- (1) $346.5$ second
- (2) $693.0$ second
- (3) $238.6$ second
- **(4)** $138.6$ second

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $t_{1/2} = \frac{0.693}{10^{-2}}$ second
2. For the reduction of $20\,\mathrm{g}$ of reactant to $5\,\mathrm{g}$, two $t_{1/2}$ is required.
3. $\therefore\; t = 2 \times \frac{0.693}{10^{-2}}$ second
4. $= 138.6$ second

**Solved independently** (answer withheld)

1. For a first order reaction, $t = \frac{2.303}{k}\log\frac{[A]_0}{[A]}$.
2. $\frac{[A]_0}{[A]} = \frac{20\,\mathrm{g}}{5\,\mathrm{g}} = 4$.
3. $\frac{2.303}{k} = \frac{2.303}{10^{-2}\,\mathrm{s^{-1}}} = 230.3\,\mathrm{s}$.
4. $t = 230.3 \times \log 4 = 230.3 \times 0.6021 = 138.6\,\mathrm{s}$.
5. Check: $t_{1/2} = \frac{0.693}{10^{-2}} = 69.3\,\mathrm{s}$; $20 \to 10 \to 5\,\mathrm{g}$ is two half-lives, $2 \times 69.3 = 138.6\,\mathrm{s}$, which is option $4$.

**Subtopic:** First Order Reactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 29)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q165_cf993b66_30102026.png?v=cf993b66798b)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q165_e173cc26_30102026.png?v=e173cc269b66)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a first order reaction the time depends only on the ratio of the amounts, so a fall from 20 g to 5 g is two half-lives, $2\times 0.693/k$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The stored string $0.693/k$ is divided by $10^{-2}$ with the decimal moved one place too far, turning the 69.3 s half-life into 693 s, which is printed while 69.3 s is not
- **Why:** This question requires a first order time from the ratio of the amounts, demonstrated by the stem's "specific reaction rate of $10^{-2}\,\mathrm{s^{-1}}$" with "$20\,\mathrm{g}$ of the reactant to reduce to $5\,\mathrm{g}$".
- **Note:** Only one distractor has a derivable route; the natural conceptual error here, treating the fall as a single half-life, gives 69.3 s, which is not printed. The other two are recorded as fillers with the values enumerated rather than given forced routes.
<!--/ecat-->

## Q166

Chemistry · organic · Alcohols, Phenols and Ethers

Which one is the most acidic compound?

- (1) 4-nitrophenol `O=[N+]([O-])c1ccc(O)cc1` ![4-nitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q166_option_1_s1_befa77e9_30102026.svg?v=befa77e9b759)
- **(2)** 2,4,6-trinitrophenol `O=[N+]([O-])c1cc([N+](=O)[O-])c(O)c([N+](=O)[O-])c1` ![2,4,6-trinitrophenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q166_option_2_s1_334a7b8b_30102026.svg?v=334a7b8ba7f7)
- (3) 4-methylphenol `Cc1ccc(O)cc1` ![4-methylphenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q166_option_3_s1_b4d7770f_30102026.svg?v=b4d7770f8750)
- (4) phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q166_option_4_s1_4778923b_30102026.svg?v=4778923bbceb)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $-\mathrm{NO_2}$ group has very strong $-I$ & $-R$ effects.

**Solved independently** (answer withheld)

1. Option $1$ is $p$-nitrophenol, option $2$ is $2,4,6$-trinitrophenol (picric acid), option $3$ is $p$-cresol ($p$-$\mathrm{CH_3C_6H_4OH}$) and option $4$ is phenol.
2. Electron-withdrawing $-\mathrm{NO_2}$ groups at ortho/para positions delocalise the negative charge of the phenoxide ion ($-I$ and $-R$), stabilising it and increasing acidity.
3. Electron-donating $-\mathrm{CH_3}$ destabilises the phenoxide ion, so $p$-cresol is less acidic than phenol.
4. Three $-\mathrm{NO_2}$ groups (two ortho, one para) give maximum stabilisation: picric acid $>$ $p$-nitrophenol $>$ phenol $>$ $p$-cresol.
5. The most acidic compound is picric acid, which is option $2$.

**Subtopic:** Acidity of Phenols · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q166_4fb3e81d_30102026.png?v=4fb3e81d272c)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q166_d5201a09_30102026.png?v=d5201a09c3e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Acid strength is set by how well the anion left after the proton goes is stabilised, so among related compounds the one whose conjugate base is most delocalised or most electron-poor is the strongest acid
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn structures and none of them was supplied to this step, so the compounds being ranked cannot be read and no route can be named
- **Why:** This question requires four compounds ranked on one property, demonstrated by the stem's "Which one is the most acidic compound?" with the compounds printed as structures.
- **Note:** All four options_en values are empty strings and no figure was attached, so the option set is drawn structures this step was not given; the paper is intact, so this is not recorded as source damage. A reviewer holding the structures should check whether the ring substituents differ only in position, which would make the dominant route a meta substituent credited with the para effect, i.e. wrong_site_attacked; and whether an alcohol or a carboxylic acid is printed among the phenols, which would instead make it a comparison across classes. asks is recorded as compare from the stem's superlative over four structures; it could not be confirmed against the options.
<!--/ecat-->

## Q167

Chemistry · inorganic · Coordination Compounds – Practice

Correct increasing order for the wavelengths of absorption in the visible region for the complexes of $\mathrm{Co^{3+}}$ is

- (1) $\mathrm{[Co(H_2O)_6]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(en)_3]^{3+}}$
- (2) $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(H_2O)_6]^{3+}}$
- **(3)** $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(H_2O)_6]^{3+}}$
- (4) $\mathrm{[Co(H_2O)_6]^{3+}}$, $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The order of the ligand in the spectrochemical series
2. $\mathrm{H_2O} < \mathrm{NH_3} < \mathrm{en}$
3. Hence, the wavelength of the light observed will be in the order
4. $\mathrm{[Co(H_2O)_6]^{3+}} < \mathrm{[Co(NH_3)_6]^{3+}} < \mathrm{[Co(en)_3]^{3+}}$
5. Thus, wavelength absorbed will be in the opposite order
6. i.e., $\mathrm{[Co(en)_3]^{3+}}$, $\mathrm{[Co(NH_3)_6]^{3+}}$, $\mathrm{[Co(H_2O)_6]^{3+}}$

**Solved independently** (answer withheld)

1. Spectrochemical series for these ligands: $\mathrm{H_2O} < \mathrm{NH_3} < \mathrm{en}$ in field strength.
2. So the splitting energy order is $\Delta_o[\mathrm{Co(H_2O)_6}]^{3+} < \Delta_o[\mathrm{Co(NH_3)_6}]^{3+} < \Delta_o[\mathrm{Co(en)_3}]^{3+}$.
3. Absorbed wavelength is $\lambda = \frac{hc}{\Delta_o}$, so $\lambda$ is inversely proportional to $\Delta_o$.
4. Increasing wavelength: $[\mathrm{Co(en)_3}]^{3+} < [\mathrm{Co(NH_3)_6}]^{3+} < [\mathrm{Co(H_2O)_6}]^{3+}$, which is option $3$.

**Subtopic:** Colour in Coordination Compounds, Crystal Field Theory and Its Limitations · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q167_686548ea_30102026.png?v=686548eaf8c3)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q167_31c2a060_30102026.png?v=31c2a0600b57)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Field strength rises from water to ammonia to ethylenediamine, the splitting $\Delta_o$ rises with it, and the wavelength absorbed is inversely related to the splitting, so the strongest-field complex absorbs the shortest wavelength
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The complexes are ranked by increasing ligand field strength, $\mathrm{H_2O} < \mathrm{NH_3} < \mathrm{en}$, and that sequence is written down as an order of increasing wavelength, with the inverse link between splitting and wavelength left out
- **Why:** This question requires the spectrochemical series combined with the inverse link between splitting and wavelength, demonstrated by the stem's "correct increasing order for the wavelengths of absorption" across the aqua, ammine and en complexes of $\mathrm{Co^{3+}}$.
<!--/ecat-->

## Q168

Chemistry · physical · Ionic Equilibrium

Concentration of the $\mathrm{Ag^{+}}$ ions in a saturated solution of $\mathrm{Ag_2C_2O_4}$ is $2.2 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$. Solubility product of $\mathrm{Ag_2C_2O_4}$ is

- (1) $4.5 \times 10^{-11}$
- **(2)** $5.3 \times 10^{-12}$
- (3) $2.42 \times 10^{-8}$
- (4) $2.66 \times 10^{-12}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Ag_2C_2O_4(s)} \rightleftharpoons \underset{2s}{2\mathrm{Ag^{+}(aq)}} + \underset{s}{\mathrm{C_2O_4^{2-}(aq)}}$
2. $K_{SP} = [\mathrm{Ag^{+}}]^{2}\,[\mathrm{C_2O_4^{2-}}]$
3. $[\mathrm{Ag^{+}}] = 2.2 \times 10^{-4}\,\mathrm{M}$
4. $\therefore\ [\mathrm{C_2O_4^{2-}}] = \frac{2.2 \times 10^{-4}}{2}\,\mathrm{M} = 1.1 \times 10^{-4}\,\mathrm{M}$
5. $\therefore\ K_{SP} = (2.2 \times 10^{-4})^{2}\,(1.1 \times 10^{-4})$
6. $= 5.324 \times 10^{-12}$

**Solved independently** (answer withheld)

1. Dissociation: $\mathrm{Ag_2C_2O_4 \rightleftharpoons 2Ag^{+} + C_2O_4^{2-}}$, so $K_{sp} = [\mathrm{Ag^{+}}]^2[\mathrm{C_2O_4^{2-}}]$.
2. From stoichiometry, $[\mathrm{C_2O_4^{2-}}] = \frac{[\mathrm{Ag^{+}}]}{2} = \frac{2.2 \times 10^{-4}}{2} = 1.1 \times 10^{-4}\,\mathrm{mol\,L^{-1}}$.
3. $[\mathrm{Ag^{+}}]^2 = (2.2 \times 10^{-4})^2 = 4.84 \times 10^{-8}$.
4. $K_{sp} = 4.84 \times 10^{-8} \times 1.1 \times 10^{-4} = 5.324 \times 10^{-12} \approx 5.3 \times 10^{-12}$, which is option $2$.

**Subtopic:** Solubility Product Constant · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q168_91959045_30102026.png?v=91959045205b)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q168_d4426a9e_30102026.png?v=d4426a9eaef6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For $\mathrm{Ag_2C_2O_4}$ the solubility product is $[\mathrm{Ag^+}]^2[\mathrm{C_2O_4^{2-}}]$, and the oxalate concentration is half the silver ion concentration
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The one-to-one solubility product expression is used for a two-to-one salt: $[\mathrm{Ag^+}][\mathrm{C_2O_4^{2-}}] = 2.2\times10^{-4}\times1.1\times10^{-4} = 2.42\times10^{-8}$, with the silver term never squared
- **Why:** This question requires the solubility product written with the correct exponents for a 2:1 salt, demonstrated by the stem giving the concentration of "the $\mathrm{Ag^{+}}$ ions in a saturated solution of $\mathrm{Ag_2C_2O_4}$".
- **Note:** Option 1 is the only distractor whose route does not land exactly on the printed figure: mistaking the silver concentration for the solubility gives $4.3\times10^{-11}$ and the option reads $4.5\times10^{-11}$, the sole option at that order. It is recorded as a trap with that mismatch stated rather than as a filler.
<!--/ecat-->

## Q169

Chemistry · physical · Chemical Equilibrium

A $20\,\mathrm{litre}$ container at $400\,\mathrm{K}$ contains $\mathrm{CO_2(g)}$ at pressure $0.4\,\mathrm{atm}$ and an excess of $\mathrm{SrO}$ (neglect the volume of solid $\mathrm{SrO}$). The volume of the containers is now decreased by moving the movable piston fitted in the container. The maximum volume of the container, when pressure of $\mathrm{CO_2}$ attains its maximum value, will be (Given that : $\mathrm{SrCO_3(s) \rightleftharpoons SrO(s) + CO_2(g)}$. $K_{\mathrm{p}} = 1.6\,\mathrm{atm}$)

- (1) $4\,\mathrm{litre}$
- (2) $2\,\mathrm{litre}$
- **(3)** $5\,\mathrm{litre}$
- (4) $10\,\mathrm{litre}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Max. pressure of $\mathrm{CO_2}$ = Pressure of $\mathrm{CO_2}$ at equilibrium
2. For reaction, $\mathrm{SrCO_3(s) \rightleftharpoons SrO(s) + CO_2}$
3. $K_{\mathrm{p}} = P_{\mathrm{CO_2}} = 1.6\,\mathrm{atm}$ = maximum pressure of $\mathrm{CO_2}$
4. Volume of container at this stage, $V = \frac{nRT}{P}$ ...(i)
5. Since container is sealed and reaction was not earlier at equilibrium
6. $\therefore$ $n$ = constant
7. $n = \frac{PV}{RT} = \frac{0.4 \times 20}{RT}$ ...(ii)
8. Put equation (ii) in equation (i)
9. $V = \left[\frac{0.4 \times 20}{RT}\right]\frac{RT}{1.6} = 5\,\mathrm{L}$

**Solved independently** (answer withheld)

1. For $\mathrm{SrCO_3(s) \rightleftharpoons SrO(s) + CO_2(g)}$, $K_p = p_{\mathrm{CO_2}}$, so the largest possible $\mathrm{CO_2}$ pressure is $1.6\,\mathrm{atm}$.
2. Until $p_{\mathrm{CO_2}}$ reaches $1.6\,\mathrm{atm}$, no $\mathrm{SrCO_3}$ forms, so the moles of $\mathrm{CO_2}$ stay constant and Boyle's law holds at $400\,\mathrm{K}$.
3. $P_1V_1 = P_2V_2 \Rightarrow 0.4 \times 20 = 1.6 \times V_2$.
4. $V_2 = \frac{8}{1.6} = 5\,\mathrm{litre}$, which is option $3$.

**Subtopic:** Homogeneous and Heterogeneous Equilibria · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q169_e5ddcb04_30102026.png?v=e5ddcb04e7a7)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q169_3690a78d_30102026.png?v=3690a78d2ac4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a heterogeneous equilibrium with excess solid, the gas pressure cannot rise above $K_p$: further compression converts the $\mathrm{CO_2}$ into $\mathrm{SrCO_3}$, so the maximum pressure is 1.6 atm and the volume at which it is first reached follows from $P_1V_1 = P_2V_2$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $1.6/0.4 = 4$ is the FACTOR by which the volume must shrink, and 4 is printed as a volume in litres, so the ratio is handed in as the answer
- **Why:** This question requires the ceiling a heterogeneous $K_p$ places on the gas pressure, applied through Boyle's law, demonstrated by the stem asking for "the maximum volume of the container, when pressure of $\mathrm{CO_2}$ attains its maximum value" with "$K_{\mathrm{p}} = 1.6\,\mathrm{atm}$".
- **Note:** The temperature 400 K and the volume of the solid are given only to fix that $K_p$ applies and that the gas volume is the container volume; neither enters the arithmetic.
<!--/ecat-->

## Q170

Chemistry · organic · Haloalkanes and Haloarenes

Identify A and predict the type of reaction

![printed figure: 1-bromo-3-methoxybenzene →($\ce{NaNH2}$) A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q170_344d193f_30102026.svg?v=344d193f2a64)

*1-bromo-3-methoxybenzene →[$\ce{NaNH2}$] A*

![drawn: 1-bromo-3-methoxybenzene →($\ce{NaNH2}$) A](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_question_27fce1c0_30102026.svg?v=27fce1c0311b)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: 1-bromo-3-methoxybenzene `COc1cccc(Br)c1` ![1-bromo-3-methoxybenzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_question_s1_420f0f2e_30102026.svg?v=420f0f2ed6d8)

- (1) 1-bromo-2-methoxybenzene `COc1ccccc1Br` ![1-bromo-2-methoxybenzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_option_1_s1_1426f143_30102026.svg?v=1426f14374e9) — and cine substitution reaction
- (2) methoxybenzene `COc1ccccc1` ![methoxybenzene](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_option_2_s1_f0155961_30102026.svg?v=f0155961c4b6) — and cine substitution reaction
- **(3)** 3-methoxyaniline `COc1cccc(N)c1` ![3-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_option_3_s1_fed4e630_30102026.svg?v=fed4e630d032) — and substitution reaction
- (4) 2-methoxyaniline `COc1ccccc1N` ![2-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_option_4_s1_7f1e1454_30102026.svg?v=7f1e145464eb) — and elimination addition reaction

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: 1-bromo-3-methoxybenzene (H drawn at C-2) with azanide ($\ce{NH2-}$) → 2-bromo-6-methoxybenzen-1-ide → 1,2-didehydro-3-methoxybenzene (Benzyne)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q170_sol_1_dc07f91b_30102026.svg?v=dc07f91b0422)

*1-bromo-3-methoxybenzene (H drawn at C-2) with azanide ($\ce{NH2-}$) → 2-bromo-6-methoxybenzen-1-ide → 1,2-didehydro-3-methoxybenzene (Benzyne)*

![drawn: 1-bromo-3-methoxybenzene (H drawn at C-2) with azanide ($\ce{NH2-}$) → 2-bromo-6-methoxybenzen-1-ide → 1,2-didehydro-3-methoxybenzene (Benzyne)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_solution_1_83b5ac24_30102026.svg?v=83b5ac246c2f)  
*drawn on the booklet's geometry, checked against its SMILES*

![printed figure: 1,2-didehydro-3-methoxybenzene attacked by azanide ($\ce{NH2-}$) at a or b: path a →(X) 2-amino-3-methoxybenzen-1-ide (Less stable); path b → 3-amino-2-methoxybenzen-1-ide, with ammonia ($\ce{H-NH2}$) → 3-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q170_sol_2_e77259b9_30102026.svg?v=e77259b9b085)

*1,2-didehydro-3-methoxybenzene attacked by azanide ($\ce{NH2-}$) at a or b: path a →[X] 2-amino-3-methoxybenzen-1-ide (Less stable); path b → 3-amino-2-methoxybenzen-1-ide, with ammonia ($\ce{H-NH2}$) → 3-methoxyaniline*

![drawn: 1,2-didehydro-3-methoxybenzene attacked by azanide ($\ce{NH2-}$) at a or b: path a →(X) 2-amino-3-methoxybenzen-1-ide (Less stable); path b → 3-amino-2-methoxybenzen-1-ide, with ammonia ($\ce{H-NH2}$) → 3-methoxyaniline](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_drawn/q170_solution_2_adeebdbe_30102026.svg?v=adeebdbec2a4)  
*drawn on the booklet's geometry, checked against its SMILES*

1. More stable as $-$ve charge is close to electron withdrawing group
2. $\because$ Incoming nucleophile ends on same ‘$\mathrm{C}$’ on which ‘$\mathrm{Br}$’ (Leaving group) was present
3. $\therefore$ NOT cine substitution.

**Solved independently** (answer withheld)

1. In $m$-bromoanisole the most acidic ring H is at C-2, flanked by the $-I$ groups $\mathrm{OCH_3}$ and $\mathrm{Br}$, so $\mathrm{NH_2^-}$ removes $\mathrm{H}$ at C-2.
2. Loss of $\mathrm{Br^-}$ from C-3 gives the benzyne with the triple bond between C-2 and C-3 (3-methoxybenzyne).
3. $\mathrm{NH_2^-}$ adds to C-3 so that the resulting carbanion is at C-2, ortho to $\mathrm{OCH_3}$, where it is stabilised by the $-I$ effect of oxygen.
4. Protonation of the C-2 carbanion gives $m$-$\mathrm{CH_3OC_6H_4NH_2}$ ($m$-anisidine) as A.
5. $\mathrm{NH_2}$ occupies the same carbon that carried $\mathrm{Br}$, so the net change is a substitution (not cine substitution); this matches option $3$, while option $4$ names the benzyne mechanism but shows the wrong product ($o$-anisidine).

**Subtopic:** Reactions of Haloarenes · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 30)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q170_8057bc66_30102026.png?v=8057bc664c2c)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q170_ea28fdf8_30102026.png?v=ea28fdf8ba37)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** An unactivated aryl halide treated with sodium amide goes through a benzyne intermediate, so the amino group can arrive at the carbon that carried the halogen or at the carbon next to it
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  each option pairs a drawn structure for A with a reaction-type phrase, and the structures were not supplied to this step: the stored option strings begin at "and", so the half of each option that distinguishes it cannot be read
- **Why:** This question requires both the product of a named reagent and the mechanism class it belongs to, demonstrated by the stem's "Identify A and predict the type of reaction" over the scheme 1-bromo-3-methoxybenzene with $\mathrm{NaNH_2}$.
- **Note:** The stem figure was supplied and readable (1-bromo-3-methoxybenzene with NaNH2 over the arrow), but all four options carry only their trailing text — "and cine substitution reaction" twice, "and substitution reaction", "and elimination addition reaction" — with the structure of A missing, and options 1 and 2 are distinguished by that structure alone. The paper is intact, so this is not recorded as source damage. The mechanism a reviewer holding the option structures should check is the "elimination addition reaction" label on option 4: that is the name a student recalls for $\mathrm{NaNH_2}$ on an aryl halide, and if its structure is the direct-substitution product then the pull is the mechanism name offered against the key's "substitution"; the two cine options should also be checked for which carbon bears the new group, which would be wrong_site_attacked.
<!--/ecat-->

## Q171

Chemistry · organic · Amines

Which of the following reactions is appropriate for converting acetamide to methanamine?

- (1) Stephens reaction
- (2) Gabriels phthalimide synthesis
- (3) Carbylamine reaction
- **(4)** Hoffmann hypobromamide reaction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{CH_3 - \overset{\overset{\displaystyle O}{\|}}{C} - NH_2 + Br_2 + 4NaOH \xrightarrow{\Delta} CH_3 - NH_2 + 2NaBr + Na_2CO_3 + 3H_2O}$
2. This is Hoffmann Bromamide reaction.

**Solved independently** (answer withheld)

1. Acetamide is $\mathrm{CH_3CONH_2}$ (2 C) and methanamine is $\mathrm{CH_3NH_2}$ (1 C), so the conversion is amide to primary amine with loss of one carbon.
2. Hoffmann bromamide degradation does exactly this: $\mathrm{CH_3CONH_2 + Br_2 + 4NaOH \rightarrow CH_3NH_2 + Na_2CO_3 + 2NaBr + 2H_2O}$.
3. Stephens reaction reduces nitriles to aldehydes, Gabriel synthesis makes amines from alkyl halides, and the carbylamine reaction makes isocyanides from primary amines, so none fit; the answer is option $4$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q171_b25aa2e1_30102026.png?v=b25aa2e1dba0)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q171_deb6fa3b_30102026.png?v=deb6fa3b4cd8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** The Hofmann bromamide degradation takes an amide to a primary amine with one carbon fewer, using bromine and alkali, which is why acetamide gives methanamine
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Gabriel's phthalimide synthesis does make primary amines, so a student matching on the product class rather than on the starting material takes it, although it begins from an alkyl halide and phthalimide and not from an amide
- **Why:** This question requires the named reaction that effects one stated conversion, demonstrated by the stem's "appropriate for converting acetamide to methanamine".
- **Note:** The option is printed as "Hoffmann hypobromamide reaction"; tagged as printed.
<!--/ecat-->

## Q172

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following pairs of compounds is isoelectronic and isostructural?

- **(1)** $\mathrm{IBr_2^-}$, $\mathrm{XeF_2}$
- (2) $\mathrm{IF_3}$, $\mathrm{XeF_2}$
- (3) $\mathrm{BeCl_2}$, $\mathrm{XeF_2}$
- (4) $\mathrm{Tel_2}$, $\mathrm{XeF_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{IBr_2^-}$, $\mathrm{XeF_2}$
2. Total number of valence electrons are equal in both the species and both the species are linear also.

**Solved independently** (answer withheld)

1. Count valence electrons in $\mathrm{XeF_2}$: $8 + 2(7) = 22$.
2. Xe in $\mathrm{XeF_2}$ has $2$ bond pairs and $3$ lone pairs, so it is $sp^3d$ and the molecule is linear.
3. Count valence electrons in $\mathrm{IBr_2^-}$: $7 + 2(7) + 1 = 22$, the same as $\mathrm{XeF_2}$.
4. I in $\mathrm{IBr_2^-}$ has $2$ bond pairs and $3$ lone pairs, so it is $sp^3d$ and linear, the same shape as $\mathrm{XeF_2}$.
5. $\mathrm{IF_3}$ has $3$ bond pairs and $2$ lone pairs, so it is T-shaped, not linear.
6. $\mathrm{BeCl_2}$ has $2 + 2(7) = 16$ valence electrons, so it is linear but not isoelectronic with $\mathrm{XeF_2}$.
7. $\mathrm{TeI_2}$ has $6 + 2(7) = 20$ valence electrons and $2$ bond pairs + $2$ lone pairs, so it is bent.
8. Only $\mathrm{IBr_2^-}$ and $\mathrm{XeF_2}$ are both isoelectronic (valence shell) and isostructural, which is option $1$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q172_3d9e875c_30102026.png?v=3d9e875c0b7c)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q172_755ced54_30102026.png?v=755ced5455ad)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $\mathrm{XeF_2}$ has 22 valence electrons and is linear with three lone pairs on the central atom, so a partner must match both the electron count and that shape
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Gaseous $\mathrm{BeCl_2}$ really is linear, so the pair satisfies the isostructural half of the stem and is accepted before the electron count is checked
- **Why:** This question requires valence-electron counts and VSEPR shapes applied to four candidate species, demonstrated by the stem asking which pair "is isoelectronic and isostructural".
- **Note:** E1 recorded plain_mcq, but each option is a pair of species judged whole against two criteria, so two_part is recorded for the printed shape; the current qtype vocabulary has no pair value. Option 4 is printed as "$\mathrm{Tel_2}$" and read as tellurium diiodide.
<!--/ecat-->

## Q173

Chemistry · inorganic · Environmental Chemistry

Which of the following is a sink for $\mathrm{CO}$?

- (1) Oceans
- (2) Plants
- (3) Haemoglobin
- **(4)** Micro-organisms present in the soil

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Micro-organisms present in the soil is a sink for $\mathrm{CO}$.

**Solved independently** (answer withheld)

1. Atmospheric $\mathrm{CO}$ is mainly removed by soil micro-organisms, which oxidise it or use it in their metabolism, so they act as its natural sink; haemoglobin binds $\mathrm{CO}$ but is not an environmental sink, and oceans and plants are sinks for $\mathrm{CO_2}$, not $\mathrm{CO}$. This is option $4$.

**Subtopic:** Air Pollution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q173_b82465de_30102026.png?v=b82465dec7d2)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q173_05c8180f_30102026.png?v=05c8180f9dcf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Soil micro-organisms are the sink that takes carbon monoxide out of the air; oceans and green plants are the sinks named for carbon dioxide
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  CO and CO$_2$ differ by one subscript, and green plants are the sink the book names for CO$_2$, so reading the stem's CO as carbon dioxide puts photosynthesis in the answer slot
- **Why:** This question requires the fact the book states about which agent removes CO from the atmosphere, demonstrated by the stem 'Which of the following is a sink for $\mathrm{CO}$?' offering four coordinate agents with no criterion printed to apply.
- **Note:** Swap test applied on the trap: replace CO in the stem with an unlike species and the pull on 'Plants' dies, because the reach runs through CO being read as CO$_2$ - so the likeness of the two formulas carries it rather than position.
<!--/ecat-->

## Q174

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which one of the following pairs of species have the same bond order?

- **(1)** $\mathrm{CN^{-}}$, $\mathrm{CO}$
- (2) $\mathrm{N_2}$, $\mathrm{O_2^{-}}$
- (3) $\mathrm{CO}$, $\mathrm{NO}$
- (4) $\mathrm{O_2}$, $\mathrm{NO^{+}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{CN^{(-)}}$ and $\mathrm{CO}$ have bond order $3$ each.

**Solved independently** (answer withheld)

1. $\mathrm{CN^-}$ has $6+7+1 = 14$ electrons, so its bond order is $\frac{10-4}{2} = 3$.
2. $\mathrm{CO}$ has $6+8 = 14$ electrons, so its bond order is $\frac{10-4}{2} = 3$; the pair in option $1$ matches.
3. $\mathrm{N_2}$ (14 e$^-$) has bond order $3$, while $\mathrm{O_2^-}$ (17 e$^-$) has $\frac{10-7}{2} = 1.5$, so option $2$ does not match.
4. $\mathrm{NO}$ (15 e$^-$) has $\frac{10-5}{2} = 2.5 \neq 3$, so option $3$ does not match.
5. $\mathrm{O_2}$ (16 e$^-$) has $\frac{10-6}{2} = 2$, while $\mathrm{NO^+}$ (14 e$^-$) has $3$, so option $4$ does not match.
6. Only option $1$ has equal bond orders ($3$ and $3$).

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q174_e46a380f_30102026.png?v=e46a380f47f2)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q174_fe5366b2_30102026.png?v=fe5366b26ea9)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Bond order is (bonding $-$ antibonding)/2 from the molecular-orbital count, so isoelectronic species share it and a charge changes the count
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  $\mathrm{NO^{+}}$ is the member of the ten-valence-electron, bond-order-3 set, and stripped of its charge on the page NO reads as that species, so CO and NO look equal at 3
- **Why:** This question requires the bond order computed from each printed species' electron count, demonstrated by the stem asking which 'pairs of species have the same bond order' while putting charged and neutral species such as $\mathrm{O_2^{-}}$ and $\mathrm{NO^{+}}$ inside the pairs.
- **Note:** Each option is a pair of species accepted or rejected whole, so the printed shape is recorded as two_part; type_patterns called it plain_mcq.
<!--/ecat-->

## Q175

Chemistry · physical · Thermodynamics

A gas is allowed to expand in a well insulated container against a constant external pressure of $2.5\,\mathrm{atm}$ from an initial volume of $2.50\,\mathrm{L}$ to a final volume of $4.50\,\mathrm{L}$. The change in internal energy $\Delta U$ of the gas in joules will be

- **(1)** $-505\,\mathrm{J}$
- (2) $+505\,\mathrm{J}$
- (3) $1136.25\,\mathrm{J}$
- (4) $-500\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

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
2. By the first law, $\Delta U = q + w = w$.
3. $\Delta V = V_f - V_i = 4.50\,\mathrm{L} - 2.50\,\mathrm{L} = 2.00\,\mathrm{L}$.
4. Work against constant external pressure: $w = -P_{ext}\Delta V = -2.5\,\mathrm{atm} \times 2.00\,\mathrm{L} = -5.0\,\mathrm{L\,atm}$.
5. Convert: $-5.0\,\mathrm{L\,atm} \times 101\,\mathrm{J\,L^{-1}\,atm^{-1}} = -505\,\mathrm{J}$.
6. $\Delta U = w = -505\,\mathrm{J}$, which is option $1$.

**Subtopic:** Internal Energy and First Law of Thermodynamics · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 31)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q175_b1704c10_30102026.png?v=b1704c10e06c)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q175_b9af1cc6_30102026.png?v=b9af1cc6b656)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A well insulated container makes $q = 0$, so the first law leaves $\Delta U$ equal to the work, and expansion against an external pressure makes that work negative
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The magnitude is the easy half - $P_{\mathrm{ext}}\Delta V = 2.5 \times 2.00 = 5.0$ L atm $= 505$ J - and reporting it as a gain follows from reading 'the gas does work' as energy arriving in the gas
- **Why:** This question requires the first law applied with $q = 0$ and the work computed from the printed numbers, demonstrated by 'a well insulated container against a constant external pressure of $2.5\,\mathrm{atm}$' with volumes of $2.50\,\mathrm{L}$ and $4.50\,\mathrm{L}$.
<!--/ecat-->

## Q176

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Extraction of gold and silver involves leaching with $\mathrm{CN^{-}}$ ion. Silver is later recovered by

- (1) Zone refining
- **(2)** Displacement with $\mathrm{Zn}$
- (3) Liquation
- (4) Distillation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Zn}$ being more reactive than $\mathrm{Ag}$ and $\mathrm{Au}$, displaces them.
2. From Native ore,
3. $\mathrm{4Ag + 8NaCN + 2H_2O + O_2} \xrightarrow{\text{Leaching}} \underset{\substack{\text{Soluble}\\ \text{Sodium dicyanoargentate(I)}}}{\mathrm{4Na[Ag(CN)_2]}} + \mathrm{4NaOH}$
4. $\mathrm{2Na[Ag(CN)_2] + Zn} \xrightarrow{\text{Displacement}} \mathrm{Na_2[Zn(CN)_4] + 2Ag}\downarrow$

**Solved independently** (answer withheld)

1. Leaching gives the soluble complex: $4\mathrm{Ag} + 8\mathrm{CN^-} + 2\mathrm{H_2O} + \mathrm{O_2} \rightarrow 4[\mathrm{Ag(CN)_2}]^- + 4\mathrm{OH^-}$.
2. Zinc is more electropositive than silver, so it displaces silver from the complex: $2[\mathrm{Ag(CN)_2}]^- + \mathrm{Zn} \rightarrow [\mathrm{Zn(CN)_4}]^{2-} + 2\mathrm{Ag}$, which is option $2$.

**Subtopic:** Concentration of Ores · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q176_04aae98c_30102026.png?v=04aae98c157f)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q176_38af07cf_30102026.png?v=38af07cf9d7e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the cyanide process silver leaves the ore as the soluble complex $[\mathrm{Ag(CN)_2}]^{-}$ and is won back by displacement with the more electropositive zinc
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Reading 'recovered' as 'refined' moves the student into the refining list printed further along the same chapter, where zone refining is the method named for getting a metal very pure
- **Why:** This question requires the fact the book states about the cyanide process, demonstrated by the stem granting the leaching step - 'Extraction of gold and silver involves leaching with $\mathrm{CN^{-}}$ ion' - and asking only how 'Silver is later recovered by'.
- **Note:** asks is recorded as fact_line rather than reaction: the stem grants the leaching and asks which named operation the process uses, and three of the four options are refining techniques rather than reagents acting on a substrate.
<!--/ecat-->

## Q177

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Consider the reactions :
Identify A, X, Y and Z

![printed figure: X ($\ce{C2H6O}$) →(Cu / 573 K) A; A →($\ce{(Ag(NH3)2)+}$, -OH, Δ) Silver mirror observed; A →(-OH, Δ) Y; A + semicarbazide → Z](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q177_e50aa845_30102026.svg?v=e50aa845d527)

*X ($\ce{C2H6O}$) →[Cu / 573 K] A; A →[$\ce{[Ag(NH3)2]+}$, -OH, Δ] Silver mirror observed; A →[-OH, Δ] Y; A + semicarbazide → Z*

Structures: semicarbazide `NNC(N)=O`

- **(1)** A-Ethanal, X-Ethanol, Y-But-2-enal, Z-Semicarbazone
- (2) A-Ethanol, X-Acetaldehyde, Y-Butanone, Z-Hydrazone
- (3) A-Methoxymethane, X-Ethanoic acid, Y-Acetate ion, Z-hydrazine
- (4) A-Methoxymethane, X-Ethanol, Y-Ethanoic acid, Z-Semicarbazide

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Since 'A' gives positive silver mirror test therefore, it must be an aldehyde or $\alpha$-Hydroxyketone.
2. Reaction with semicarbazide indicates that A can be an aldehyde or ketone.
3. Reaction with $\mathrm{OH^{-}}$ i.e., aldol condensation (by assuming alkali to be dilute) indicates that A is aldehyde as aldol reaction of ketones is reversible and carried out in special apparatus.
4. These indicates option (1).

![printed figure: ethanol (X) →(Cu, 573 K) ethanal (A) →($\ce{(Ag(NH3)2)+}$, $\ce{OH-}$, Δ) ethanoic acid; A + semicarbazide → acetaldehyde semicarbazone (Z); A →($\ce{OH-}$) 3-Hydroxybutanal →(Δ) But-2-enal (Y)](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q177_sol_1_42772f52_30102026.svg?v=42772f524330)

*ethanol (X) →[Cu, 573 K] ethanal (A) →[$\ce{[Ag(NH3)2]+}$, $\ce{OH-}$, Δ] ethanoic acid; A + semicarbazide → acetaldehyde semicarbazone (Z); A →[$\ce{OH-}$] 3-Hydroxybutanal →[Δ] But-2-enal (Y)*


**Solved independently** (answer withheld)

1. $X$ ($\mathrm{C_2H_6O}$) that is dehydrogenated by $\mathrm{Cu}/573\,\mathrm{K}$ must be an alcohol, so $X$ is ethanol $\mathrm{CH_3CH_2OH}$.
2. $\mathrm{CH_3CH_2OH} \xrightarrow{\mathrm{Cu},\,573\,\mathrm{K}} \mathrm{CH_3CHO}$, so $A$ is ethanal.
3. Ethanal is an aldehyde, so it reduces Tollens' reagent $[\mathrm{Ag(NH_3)_2}]^+$ and gives the silver mirror, consistent with $A$ = ethanal.
4. Ethanal has $\alpha$-H, so with $\mathrm{OH^-},\,\Delta$ it undergoes aldol condensation: $2\,\mathrm{CH_3CHO} \rightarrow \mathrm{CH_3CH=CHCHO}$, so $Y$ is but-2-enal.
5. $\mathrm{CH_3CHO} + \mathrm{NH_2NHCONH_2} \rightarrow \mathrm{CH_3CH=NNHCONH_2} + \mathrm{H_2O}$, so $Z$ is the semicarbazone.
6. $A$-Ethanal, $X$-Ethanol, $Y$-But-2-enal, $Z$-Semicarbazone matches option $1$.

**Subtopic:** Preparation of Aldehydes, Chemical Reactions: Reactions Due to Alpha Hydrogen · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q177_be50530b_30102026.png?v=be50530b2345)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q177_34647439_30102026.png?v=346474393158)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Copper at 573 K takes hydrogen off ethanol to give ethanal, which answers Tollens' reagent with a silver mirror, self-condenses in warm alkali to but-2-enal, and condenses with semicarbazide to a semicarbazone
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The scheme runs X to A while the stem lists 'A, X, Y and Z' the other way round, so answering in the stem's order puts the alcohol under A and the aldehyde under X, reversing the Cu/573 K dehydrogenation
- **Why:** This question requires each species along the printed scheme to be named from the reagent above its arrow, demonstrated by 'X ($\mathrm{C_2H_6O}$) $\rightarrow$[Cu / 573 K] A' and the silver mirror reported for A.
- **Note:** Options are four-part assignments accepted or rejected whole, so the shape is recorded as two_part; type_patterns called it statement_options. The scheme itself is supplied as figure text and agrees with the printed key, and the failed draw check in the record concerns redrawn structures, not the scheme.
<!--/ecat-->

## Q178

Chemistry · inorganic · Coordination Compounds – Practice

Pick out the correct statement with respect $[\mathrm{Mn(CN)_6}]^{3-}$ :

- **(1)** It is $d^{2}sp^{3}$ hybridised and octahedral
- (2) It is $dsp^{2}$ hybridised and square planar
- (3) It is $sp^{3}d^{2}$ hybridised and octahedral
- (4) It is $sp^{3}d^{2}$ hybridised and tetrahedral

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $[\mathrm{Mn(CN)_6}]^{3-}$
2. $\mathrm{Mn(III)} = [\mathrm{Ar}]3d^{4}$
3. $\mathrm{CN^{-}}$ being strong field ligand forces pairing of electrons
4. This gives $t_{2g}^{4}e_{g}^{0}$
5. $\therefore$ $\mathrm{Mn(III)} = [\mathrm{Ar}]$

![printed figure: orbital-box diagram: 3d boxes ↑↓, ↑, ↑, empty, empty; 4s one empty box; 4p three empty boxes; the two empty 3d boxes, the 4s box and the 4p boxes are enclosed in a dotted box labelled $d^{2}sp^{3}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q178_sol_1_94e13dbf_30102026.svg?v=94e13dbf0130)

*orbital-box diagram: 3d boxes ↑↓, ↑, ↑, empty, empty; 4s one empty box; 4p three empty boxes; the two empty 3d boxes, the 4s box and the 4p boxes are enclosed in a dotted box labelled $d^{2}sp^{3}$*

6. $\because$ Coordination number of $\mathrm{Mn} = 6$
7. $\therefore$ Structure = octahedral
8. $[\mathrm{Mn(CN)_6}]^{3-} =$

![printed figure: (Ar) orbital-box diagram: 3d boxes ↑↓, ↑, ↑, ××, ××; 4s one box ××; 4p three boxes ××, ××, ××; the six ×× boxes are enclosed in a dotted box labelled $d^{2}sp^{3}$](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/figures_agent/q178_sol_2_e058d064_30102026.svg?v=e058d064d986)

*[Ar] orbital-box diagram: 3d boxes ↑↓, ↑, ↑, ××, ××; 4s one box ××; 4p three boxes ××, ××, ××; the six ×× boxes are enclosed in a dotted box labelled $d^{2}sp^{3}$*


**Solved independently** (answer withheld)

1. Oxidation state of Mn: $x + 6(-1) = -3 \Rightarrow x = +3$.
2. $\mathrm{Mn^{3+}}$ has configuration $[\mathrm{Ar}]\,3d^{4}$.
3. $\mathrm{CN^-}$ is a strong-field ligand, so the four $3d$ electrons pair into three orbitals ($t_{2g}^{4}e_g^{0}$, low spin, 2 unpaired electrons).
4. Two inner $3d$ orbitals remain vacant and mix with $4s$ and three $4p$ orbitals: $d^{2}sp^{3}$ hybridisation.
5. Six ligands with $d^{2}sp^{3}$ hybridisation give an octahedral geometry, which is option $1$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q178_54844f8f_30102026.png?v=54844f8ff819)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q178_ef6f03ca_30102026.png?v=ef6f03ca5feb)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $\mathrm{CN^{-}}$ is a strong field ligand, so a six-coordinate Mn(III) complex uses inner 3d orbitals and is $d^{2}sp^{3}$ octahedral; $sp^{3}d^{2}$ is the outer-orbital set of weak field complexes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Six ligands give an octahedron either way, and the two hybridisation labels are the same symbols in a different order, so the one that comes to hand is $sp^{3}d^{2}$, the set learnt for $\mathrm{SF_6}$
- **Why:** This question requires the strong field ligand rule applied to a named complex, demonstrated by the options differing only in hybridisation and shape - 'It is $d^{2}sp^{3}$ hybridised and octahedral' against 'It is $sp^{3}d^{2}$ hybridised and octahedral'.
- **Note:** type_patterns called this plain_mcq; the stem 'Pick out the correct statement' asks for a statement to be judged, which puts it on the statements shape, each statement bundling a hybridisation with a geometry. Swap test applied on the trap: replace $sp^{3}d^{2}$ with an unlike label and the pull disappears, so the likeness of the two symbol strings carries it rather than position.
<!--/ecat-->

## Q179

Chemistry · physical · Structure of Atom

Which one is the wrong statement?

- (1) Half-filled and fully filled orbitals have greater stability due to greater exchange energy, greater symmetry and more balanced arrangement
- **(2)** The energy of $2s$ orbital is less than the energy of $2p$ orbital in case of Hydrogen like atoms
- (3) de-Broglie's wavelength is given by $\lambda = \dfrac{h}{mv}$, where $m$ = mass of the particle, $v$ = group velocity of the particle
- (4) The uncertainty principle is $\Delta E \times \Delta t \geq \dfrac{h}{4\pi}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Energy of $2s$-orbital and $2p$-orbital in case of hydrogen like atoms is equal.

**Solved independently** (answer withheld)

1. For a hydrogen-like atom, $E_n = -\frac{13.6\,Z^2}{n^2}\,\text{eV}$, which depends only on $n$ and not on $l$.
2. So $2s$ ($n=2, l=0$) and $2p$ ($n=2, l=1$) have equal energy: $E_{2s} = E_{2p}$, so statement 2 is wrong.
3. Statement 1 (extra stability of half-filled and fully filled orbitals from exchange energy and symmetry) is correct as NCERT teaches.
4. Statement 3, $\lambda = \frac{h}{mv}$ with $v$ the particle (group) velocity, is correct.
5. Statement 4, $\Delta E \times \Delta t \geq \frac{h}{4\pi}$, is a correct form of the uncertainty principle, so the wrong statement is option $2$.

**Subtopic:** Atomic Orbitals: Shapes, Energies and Nodes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 32)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q179_246ebdb6_30102026.png?v=246ebdb6adb0)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q179_a9867c9d_30102026.png?v=a9867c9dc4a5)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In a one-electron, hydrogen-like atom the orbital energy depends on $n$ alone, so 2s and 2p are degenerate; the 2s-below-2p ordering belongs to many-electron atoms
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Carried past the printed words 'in case of Hydrogen like atoms', the 2s-below-2p ordering reads as true, so the statement left to condemn is the one whose form the chapter does not print, $\Delta E \times \Delta t \geq h/4\pi$
- **Why:** This question requires the orbital-energy rule applied under the condition the statement prints, demonstrated by 'The energy of $2s$ orbital is less than the energy of $2p$ orbital in case of Hydrogen like atoms'.
- **Note:** The trap is hosted on option 4 because the dropped condition in statement 2 is what sends a student on to one of the true statements; held to, the condition settles statement 2 and the question is answered.
<!--/ecat-->

## Q180

Chemistry · organic · Biomolecules

Which of the following statements is not correct?

- (1) Blood proteins thrombin and fibrinogen are involved in blood clotting
- **(2)** Denaturation makes the proteins more active
- (3) Insulin maintains sugar level in the blood of a human body
- (4) Ovalbumin is a simple food reserve in egg-white

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Due to denaturation of proteins, globules unfold and helix get uncoiled and protein loses its biological activity.

**Solved independently** (answer withheld)

1. Thrombin and fibrinogen are blood proteins in the clotting cascade, and insulin regulates blood sugar. Ovalbumin is a simple protein stored in egg white. So options $1$, $3$ and $4$ are correct.
2. Denaturation breaks the secondary and tertiary structure, so the protein loses its biological activity. The statement that denaturation makes proteins more active is wrong, so the answer is option $2$.

**Subtopic:** Denaturation of Proteins and Enzymes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/crops/q180_b8d056b5_30102026.png?v=b8d056b5542d)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2017/2017_D/solutions/q180_26a3cd0b_30102026.png?v=26a3cd0b8d5f)

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Denaturation unfolds a protein's secondary and tertiary structure, so its biological activity is lost, not raised
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Albumin is met as the transport protein of blood plasma, so 'Ovalbumin is a simple food reserve' reads as a storage role pinned on a protein whose job the student believes they already know
- **Why:** This question requires the stated fact about what denaturation does to a protein, demonstrated by the option 'Denaturation makes the proteins more active' standing against the chapter's line that a denatured protein loses its biological activity.
- **Note:** Swap test applied on the trap: replace 'Ovalbumin' with an unlike protein name and the pull disappears, because the reach runs through reading it as serum albumin - so the likeness carries it rather than the position of the line in the chapter.
<!--/ecat-->

