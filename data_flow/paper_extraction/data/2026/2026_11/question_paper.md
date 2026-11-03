# NEET (UG) 2026 · Code 11

180 questions · source `../papers/neet_2026_code-11.pdf` · every image a CDN link (0 without one) · 28 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Units and Measurements

The speed of light in vacuum is taken as unity. If light takes 6 min 40 s to reach the Earth from the Sun, the distance between the Sun and the Earth in new unit is:

- (1) $3 \times 10^{8}$
- (2) $500$
- (3) $3 \times 10^{10}$
- **(4)** $400$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Time, $t = 6$ min $40$ s
2. $= 360 + 40$
3. $= 400\,\mathrm{s}$
4. Distance in new system $d = vt$
5. $= 1 \times 400 = 400$

**Solved independently** (answer withheld)

1. Convert the travel time: $t = 6\ \text{min}\ 40\ \text{s} = 6 \times 60 + 40 = 400\ \text{s}$.
2. In the new system the speed of light is unity, so $c = 1$ distance-unit per second.
3. $d = c\,t = 1 \times 400 = 400$ new units, which is option $4$.

**Subtopic:** System of Units · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q001_65538e54_30102026.png?v=65538e5489fa)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q001_c19fb686_30102026.png?v=c19fb686fc8d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The question makes the speed of light the unit of speed. Then a light travel time is the same number as the distance. You use $d = ct$ with $c = 1$.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Most students pick option 2. 500 is the number you carry for sunlight. The book says sunlight takes 8 min 20 s, which is 500 s, and 1 AU is 500 light-seconds. This question prints 6 min 40 s instead. That is 400 s. So in this unit the distance is 400.
- **Why:** You have to turn the printed travel time into a distance with the speed of light set to one. The question says 'The speed of light in vacuum is taken as unity'.
<!--/ecat-->

## Q2

Physics · Mechanical Properties of Solids

Match List I with List II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Young's Modulus | I. | $\dfrac{\Delta d}{\Delta L}\left(\dfrac{L}{d}\right)$ |
| B. | Compressibility | II. | $\dfrac{FL}{A(\Delta L)}$ |
| C. | Bulk Modulus | III. | $-\dfrac{1}{\Delta P}\left(\dfrac{\Delta V}{V}\right)$ |
| D. | Poisson's Ratio | IV. | $-P\left(\dfrac{V}{\Delta V}\right)$ |

- (1) A-IV, B-I, C-II, D-III
- (2) A-III, B-II, C-I, D-IV
- (3) A-I, B-IV, C-III, D-II
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. Young's Modulus $= \frac{\text{Stress}}{\text{Strain}} = \frac{FL}{A\Delta L}$
2. B. Compressibility $= \frac{1}{\text{Bulk modulus}} = -\frac{1}{\Delta P}\left(\frac{\Delta V}{V}\right)$
3. C. Bulk Modulus $= -P\left(\frac{V}{\Delta V}\right)$
4. D. Poisson's Ratio $= \frac{\text{Lateral strain}}{\text{Longitudinal strain}} = \frac{\Delta d}{\Delta L}\left(\frac{L}{d}\right)$

**Solved independently** (answer withheld)

1. Young's modulus is longitudinal stress over longitudinal strain: $Y = \frac{F/A}{\Delta L/L} = \frac{FL}{A\,\Delta L}$, which is II, so A-II.
2. Compressibility is the reciprocal of bulk modulus: $k = \frac{1}{B} = -\frac{1}{\Delta P}\left(\frac{\Delta V}{V}\right)$, which is III, so B-III.
3. Bulk modulus is $B = -\frac{\Delta P}{\Delta V/V} = -P\left(\frac{V}{\Delta V}\right)$, which is IV, so C-IV.
4. Poisson's ratio is lateral strain over longitudinal strain: $\sigma = \frac{\Delta d/d}{\Delta L/L} = \frac{\Delta d}{\Delta L}\left(\frac{L}{d}\right)$, which is I, so D-I.
5. A-II, B-III, C-IV, D-I is option $4$.

**Subtopic:** Hooke's Law · **Difficulty:** easy (4 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q002_cacb4309_30102026.png?v=cacb43091852)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q002_5c11d43d_30102026.png?v=5c11d43dc9cc)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** You have to tell Young's modulus, bulk modulus, compressibility and Poisson's ratio apart from their formulas. Compressibility is simply 1 divided by the bulk modulus.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. Compressibility is 1 divided by the bulk modulus. Many students remember that the two go together but forget which way round. So they read $-P\left(\frac{V}{\Delta V}\right)$ as compressibility. Option 3 is the only code that pairs B with IV. The correct way is the other way round. The $\frac{1}{\Delta P}$ form is compressibility. So B goes with III and C goes with IV.
- **Why:** The question gives you four quantities and asks you to pair each one with its formula. List I names the moduli. List II prints the formulas, such as '$\frac{FL}{A(\Delta L)}$' and '$-\frac{1}{\Delta P}\left(\frac{\Delta V}{V}\right)$'.
- **Note:** Option 3 also swaps A and D. It is the correct code with every pair put the wrong way round.
<!--/ecat-->

## Q3

Physics · Semiconductor Electronics

The current $I$ in the circuit shown below is: (All diodes are ideal and identical)

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q003_4b16fc66_30102026.png?v=4b16fc662e3b)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q003_question_e8841da8_30102026.svg?v=e8841da87d96)  
*drawn by code/lib/physics_figure.py*

- (1) $\dfrac{5}{3}\,\mathrm{A}$
- (2) $\dfrac{5}{9}\,\mathrm{A}$
- (3) $\dfrac{1}{3}\,\mathrm{A}$
- **(4)** $\dfrac{15}{2}\,\mathrm{A}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For ideal diode, forward resistance $= 0$ and reverse biased resistance $= \infty$
2. $\therefore$ Circuit can be redrawn as,

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q003_sol_1_50aec92d_30102026.png?v=50aec92d0d51)

![drawn: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q003_solution_1_75863e90_30102026.svg?v=75863e90cc80)  
*drawn by code/lib/physics_figure.py*

3. $I = \frac{10}{2} + \frac{10}{4}$
4. $= \frac{30}{4} = \frac{15}{2}\,\mathrm{A}$

**Solved independently** (answer withheld)

1. The battery's $+$ plate feeds the left rail, so conventional current leaves it upward (as the arrow $I$ shows) and crosses every branch from left to right.
2. A diode conducts only when its arrowhead points along the current, i.e. to the right: that is true for the $4\,\Omega$ branch and the $2\,\Omega$ branch.
3. The diodes in the $3\,\Omega$ and $5\,\Omega$ branches point left, so they are reverse biased and those branches carry no current.
4. The two conducting branches are in parallel: $R_{eq} = \frac{4 \times 2}{4 + 2} = \frac{4}{3}\,\Omega$.
5. $I = \frac{V}{R_{eq}} = \frac{10}{4/3} = \frac{30}{4} = \frac{15}{2}\,\mathrm{A}$, which is option $4$.

**Subtopic:** PN Junction Diode Under Forward Bias, PN Junction Diode Under Reverse Bias · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q003_24d18c01_30102026.png?v=24d18c01af98)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q003_fa7454ce_30102026.png?v=fa7454cead07)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An ideal diode either conducts with no voltage drop or blocks completely. So you first cut out every reverse-biased branch. Only then do you combine the resistances.
- **Why:** You have to reduce a network of diodes and resistors to a single current. The question says '(All diodes are ideal and identical)' and the options are currents in amperes.
<!--/ecat-->

## Q4

Physics · Rotational Motion

The angular speed of a flywheel is increased from 600 rpm to 1200 rpm in 10 s. The number of revolutions completed by the flywheel during this time is:

- (1) $900$
- (2) $600$
- **(3)** $150$
- (4) $300$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\alpha = \frac{\omega_2 - \omega_1}{\Delta t} = \left(\frac{1200 - 600}{10}\right)\frac{2\pi}{60} = 2\pi\ \mathrm{rad/s^2}$
2. $\Rightarrow$ Use equation of motion, $\omega_2^{2} = \omega_1^{2} + 2\alpha\theta$
3. $\Rightarrow\ \omega_2 = 1200 \times \frac{2\pi}{60} = 40\pi$
4. $\omega_1 = 600 \times \frac{2\pi}{60} = 20\pi$
5. $(40\pi)^{2} = (20\pi)^{2} + 2 \times 2\pi\theta$
6. $\Rightarrow\ 1200\,\pi^{2} = 4\pi\theta$
7. $\Rightarrow\ \theta = 300\pi$ radian
8. $\Rightarrow$ Number of revolution $= \frac{\theta}{2\pi} = 150$

**Solved independently** (answer withheld)

1. Convert both rates to revolutions per second: $n_1 = \frac{600}{60} = 10\,\mathrm{rev/s}$ and $n_2 = \frac{1200}{60} = 20\,\mathrm{rev/s}$.
2. With uniform angular acceleration the mean rate is $\bar{n} = \frac{n_1 + n_2}{2} = \frac{10 + 20}{2} = 15\,\mathrm{rev/s}$.
3. $N = \bar{n}\,t = 15 \times 10 = 150$ revolutions, which is option $3$.

**Subtopic:** Angular Velocity and Angular Acceleration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q004_fb2993a1_30102026.png?v=fb2993a10c98)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q004_c8d5ca39_30102026.png?v=c8d5ca3916b2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The angular acceleration is uniform. So the number of turns is the average angular speed times the time. You also have to change the rpm to fit the 10 s window.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Most students pick option 1. The average of 600 and 1200 rpm is 900. 900 is printed as an option. So the work stops at the average speed and that number is read as a count of turns. The count still needs the 10 s window: 900 rev/min $\times \frac{10}{60}$ min $= 150$.
- **Why:** You have to count the revolutions over a stated time. The question says 'increased from 600 rpm to 1200 rpm in 10 s' and asks for 'The number of revolutions completed'.
<!--/ecat-->

## Q5

Physics · Oscillations

> ⚠ The independent solve chose (unsure); the booklet prints (3).

For a simple pendulum, having time period $T$, the variation of kinetic energy (K.E.) with time ($t$) is represented by:

![printed figure: Four K.E.-against-t graphs printed as options (1) to (4): a constant line, a sine about a non-zero mean, a rectified sine of period T/2, and a sine through zero](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q005_08ec44fe_30102026.png?v=08ec44fe7e55)

*Four K.E.-against-t graphs printed as options (1) to (4): a constant line, a sine about a non-zero mean, a rectified sine of period T/2, and a sine through zero*

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q005_option_1_f9d67ac6_30102026.png?v=f9d67ac67643) ![drawn: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q005_option_1_ba71d17f_30102026.svg?v=ba71d17f6c83)  
*drawn by code/lib/physics_figure.py* — [graph]
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q005_option_2_0107cc3f_30102026.png?v=0107cc3fdbec) ![drawn: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q005_option_2_851985c1_30102026.svg?v=851985c1619f)  
*drawn by code/lib/physics_figure.py* — [graph]
- **(3)** ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q005_option_3_2c44f48c_30102026.png?v=2c44f48c69db) ![drawn: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q005_option_3_52231f56_30102026.svg?v=52231f56869a)  
*drawn by code/lib/physics_figure.py* — [graph]
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q005_option_4_0ef8978d_30102026.png?v=0ef8978d556c) ![drawn: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q005_option_4_e0f97130_30102026.svg?v=e0f971300a83)  
*drawn by code/lib/physics_figure.py* — [graph]

**Answer** — booklet: (3) · independent solve: (unsure) · ai_unsure

**Publisher's solution**

1. Kinetic energy, $K = \frac{1}{2}mv^{2}$
2. $= \frac{1}{2}mA^{2}\omega^{2}\cos^{2}(\omega t + \phi)$
3. $\therefore\ K \propto \cos^{2}(\omega t + \phi)$

**Solved independently** (answer withheld)

1. For a simple pendulum the bob's speed is $v = A\omega\cos(\omega t + \phi)$, so $K.E. = \tfrac{1}{2}mA^2\omega^2\cos^2(\omega t + \phi)$.
2. $\cos^2$ has period $\frac{\pi}{\omega} = \frac{T}{2}$, so the K.E. curve repeats twice per oscillation and never goes negative, touching zero at the extremes.
3. Option $1$ shows a constant K.E. and option $2$ a single sinusoid of period $T$ dipping below its mean line; neither matches, so the answer must be option $3$ or $4$.
4. The provided option image is cut off after option $2$, so options $3$ and $4$ are not readable and no choice can be made.

**Subtopic:** Energy Conservation in SHM · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 4)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q005_a3c6bfd6_30102026.png?v=a3c6bfd63a9f)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q005_cb253c81_30102026.png?v=cb253c814a62)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A pendulum has its largest kinetic energy at the mean position. It has zero kinetic energy at both ends. So a graph of K.E. against time repeats twice in every period. It never goes below zero.
- **Why:** You have to match a time dependence you already know to a graph. The question says 'the variation of kinetic energy (K.E.) with time ($t$) is represented by' and the four options are graphs.
<!--/ecat-->

## Q6

Physics · Current Electricity

A resistor is connected to a battery of $12\,\mathrm{V}$ emf and internal resistance $2\,\Omega$. If the current in the circuit is $0.6\,\mathrm{A}$, the terminal voltage of the battery is:

- (1) $10\,\mathrm{V}$
- (2) $1.2\,\mathrm{V}$
- (3) $12\,\mathrm{V}$
- **(4)** $10.8\,\mathrm{V}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Circuit can be draw as,

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q006_sol_1_fe3c5722_30102026.png?v=fe3c57222e05)

![drawn: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q006_solution_1_1458327c_30102026.svg?v=1458327ca8cf)  
*drawn by code/lib/physics_figure.py*

2. $\Rightarrow$ Terminal voltage of battery $V = E - ir$
3. $= 12 - 0.6 \times 2 = 10.8\,\mathrm{V}$

**Solved independently** (answer withheld)

1. The terminal voltage of a discharging cell is $V = \varepsilon - I r$.
2. $I r = 0.6 \times 2 = 1.2\,\mathrm{V}$.
3. $V = 12 - 1.2 = 10.8\,\mathrm{V}$, which is option $4$.

**Subtopic:** Terminal Potential Difference · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q006_b52f581e_30102026.png?v=b52f581e66fd)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q006_d65f49b3_30102026.png?v=d65f49b35bb4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Terminal voltage is the emf minus the drop inside the cell. The formula is $V = \varepsilon - Ir$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Most students pick option 2. The first thing the formula gives you is $Ir = 0.6 \times 2 = 1.2\,\mathrm{V}$. 1.2 V is printed as an option. So the work stops at the internal drop. You still have to subtract it from 12 V, which gives 10.8 V.
- **Why:** You have to take the emf and reduce it by the internal drop. The question gives 'internal resistance $2\,\Omega$' and 'the current in the circuit is $0.6\,\mathrm{A}$'.
<!--/ecat-->

## Q7

Physics · Kinetic Theory of Gases

A flask contains argon and chlorine in the ratio of $2 : 1$ by mass. The temperature of the mixture is $27^\circ\mathrm{C}$. The ratio of root mean square speed of the molecules of the two gases $\left(\dfrac{V_{\mathrm{rms}}^{\mathrm{Ar}}}{V_{\mathrm{rms}}^{\mathrm{Cl}}}\right)$ is:

(Atomic mass of argon $= 40.0\,\mathrm{u}$ and molecular mass of chlorine $= 70.0\,\mathrm{u}$)

- **(1)** $\dfrac{\sqrt{7}}{2}$
- (2) $\dfrac{7}{4}$
- (3) $\dfrac{7}{2}$
- (4) $\dfrac{2}{\sqrt{7}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $v_{\mathrm{rms}} = \sqrt{\frac{3RT}{M}}$
2. For same temperature, $v_{\mathrm{rms}} \propto \frac{1}{\sqrt{M}}$
3. $\frac{V_{\mathrm{rms}}^{\mathrm{Ar}}}{V_{\mathrm{rms}}^{\mathrm{Cl}}} = \sqrt{\frac{M_{\mathrm{Cl}}}{M_{\mathrm{Ar}}}} = \sqrt{\frac{70}{40}} = \frac{\sqrt{7}}{2}$

**Solved independently** (answer withheld)

1. $v_{rms} = \sqrt{\frac{3RT}{M}}$, and both gases share the same temperature $T = 300\,\mathrm{K}$.
2. Hence $\frac{v_{rms}^{Ar}}{v_{rms}^{Cl}} = \sqrt{\frac{M_{Cl_2}}{M_{Ar}}} = \sqrt{\frac{70}{40}}$.
3. $\sqrt{\frac{70}{40}} = \sqrt{\frac{7}{4}} = \frac{\sqrt{7}}{2} \approx 1.32$, which is option $1$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q007_061779cb_30102026.png?v=061779cb37f6)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q007_cfbe8f4c_30102026.png?v=cfbe8f4c62ad)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At one temperature $v_{\mathrm{rms}} \propto 1/\sqrt{M}$. So only the molecular masses set the ratio. How much of each gas there is does not matter.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. Since $v_{\mathrm{rms}} \propto 1/\sqrt{M}$, the ratio for argon over chlorine needs the chlorine mass on top. If you copy the masses in the order the question names them you get $\sqrt{40/70} = 2/\sqrt{7}$. That is $\sqrt{7}/2$ turned upside down.
- **Also:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Some students pick option 2. They remember that speed goes down as mass goes up, but they drop the square root. That gives the plain mass ratio $70/40 = 7/4$. The square root is part of the relation, so $7/4$ is just $(\sqrt{7}/2)^2$.
- **Why:** You have to find the factor by which root mean square speed changes with molecular mass at a fixed temperature. The options are pure ratios. 'The temperature of the mixture is $27^\circ\mathrm{C}$' applies to both gases.
- **Note:** The '$2 : 1$ by mass' in the question never enters the answer. Root mean square speed depends on temperature and molecular mass only.
<!--/ecat-->

## Q8

Physics · Ray Optics

A ray of monochromatic light is passing through an equilateral prism ($ABC$) as shown in the figure. The refracted ray ($QR$) is parallel to its base ($BC$) and the angle of incidence ($i$) is $50^\circ$. Then the angle of deviation ($\delta$) is:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q008_d7df0f81_30102026.png?v=d7df0f819453)

- (1) $45^\circ$
- (2) $35^\circ$
- **(3)** $40^\circ$
- (4) $55^\circ$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q008_sol_1_c311e381_30102026.png?v=c311e3813307)

1. $i = e$
2. Equation of prism
3. $i + e = A + \delta$
4. $2i - A = \delta$
5. $2(50) - 60 = \delta$
6. $\delta = 40^\circ$

**Solved independently** (answer withheld)

1. The prism is equilateral, so the refracting angle is $A = 60^\circ$.
2. The refracted ray $QR$ running parallel to the base $BC$ is the symmetric passage, i.e. the minimum-deviation configuration, where $e = i$ and $r_1 = r_2 = A/2$.
3. Prism relation: $\delta = i + e - A = 2i - A$.
4. $\delta = 2 \times 50^\circ - 60^\circ = 40^\circ$, which is option $3$.

**Subtopic:** Prism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q008_2beb2d80_30102026.png?v=2beb2d803c37)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q008_d8f4aec1_30102026.png?v=d8f4aec1655a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The refracted ray runs parallel to the base of an equilateral prism. That tells you this is the minimum deviation ray. Here $i = e$ and $\delta_m = 2i - A$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Most students pick option 4. The relation you carry into the exam is usually written $i = \frac{A + \delta_m}{2}$. Solve it for the wrong symbol and you get $\delta = \frac{60^\circ + 50^\circ}{2} = 55^\circ$. Rearrange it properly for $\delta_m$ and you get $2i - A = 100^\circ - 60^\circ = 40^\circ$.
- **Why:** You have to find the deviation when the ray passes through the prism symmetrically. The question says 'The refracted ray ($QR$) is parallel to its base ($BC$)'. The prism is equilateral, so $A = 60^\circ$, and $i = 50^\circ$.
- **Note:** The figure only draws what the question already says. The equilateral prism, the base-parallel ray and $i = 50^\circ$ are all in the text.
<!--/ecat-->

## Q9

Physics · Modern Physics

Match List I with List II.

Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A. | $E = h\nu$ | I. | de Broglie wavelength |
| B. | Diffraction and Interference | II. | Particle nature of light |
| C. | $\lambda = h/p$ | III. | Wave nature of light |
| D. | Compton effect | IV. | Energy of photon |

- (1) A-IV, B-I, C-II, D-III
- (2) A-IV, B-III, C-II, D-I
- (3) A-I, B-IV, C-III, D-II
- **(4)** A-IV, B-III, C-I, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. $E = h\nu$ is energy of photon
2. B. Diffraction and interference confirm wave nature of light
3. C. $\lambda = \frac{h}{p}$ is de Broglie wavelength of particle.
4. D. Compton effect confirms particle nature of light.

**Solved independently** (answer withheld)

1. $E = h\nu$ is the energy of a photon, so A-IV.
2. Diffraction and interference are the classic demonstrations of the wave nature of light, so B-III.
3. $\lambda = h/p$ is de Broglie's relation for the matter wavelength, so C-I.
4. The Compton effect, photon-electron scattering with a wavelength shift, demonstrates the particle nature of light, so D-II.
5. A-IV, B-III, C-I, D-II is option $4$.

**Subtopic:** Wave Theory of Light, de Broglie Wavelength of Matter Waves · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 6)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q009_407ed4bb_30102026.png?v=407ed4bb608b)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q009_4ae662d4_30102026.png?v=4ae662d4c292)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** You have to say which observations show light acting like a wave and which show it acting like a particle. You also have to know which equation gives the wavelength of a particle.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. The equation $\lambda = h/p$ has momentum in it. Momentum makes a student think of particles. So they pair C with II and read the equation as a statement about the particle nature of light. That leaves the Compton effect holding 'de Broglie wavelength'. In fact $\lambda = h/p$ is the equation that gives de Broglie's wavelength. The Compton effect is a photon colliding like a particle.
- **Why:** The question gives you four entries. You have to pair each one with what it shows. List I prints '$\lambda = h/p$' and 'Compton effect'. List II prints 'de Broglie wavelength' and 'Particle nature of light'.
- **Note:** Option 2 keeps A with IV and B with III, the same as the correct code. It moves only the C and D pair. So the whole question comes down to that one pairing.
<!--/ecat-->

## Q10

Physics · Modern Physics

In the first excited state of hydrogen atom, the energy of its electron is $-3.4\,\mathrm{eV}$. The radial distance of the electron from the hydrogen nucleus in this case is approximately:

(Take $1\,\mathrm{eV} = 1.6 \times 10^{-19}\,\mathrm{J}$, $e = 1.6 \times 10^{-19}\,\mathrm{C}$ and $\dfrac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}\,\mathrm{N\,m^2/C^2}$ )

- (1) $2.1 \times 10^{-9}\,\mathrm{m}$
- (2) $2.1 \times 10^{-8}\,\mathrm{m}$
- **(3)** $2.1 \times 10^{-10}\,\mathrm{m}$
- (4) $2.1 \times 10^{-11}\,\mathrm{m}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\frac{KQ^{2}}{2r} = 3.4\ \mathrm{eV}$
2. $\frac{9 \times 10^{9} \times (1.6 \times 10^{-19})^{2}}{2 \times 3.4 \times 1.6 \times 10^{-19}} = r$
3. $2.1176 \times 10^{-10} = r$
4. $r = 2.1 \times 10^{-10}\ \mathrm{m}$

**Solved independently** (answer withheld)

1. For the Bohr orbit the total energy is $E = -\frac{1}{4\pi\varepsilon_0}\frac{e^2}{2r}$, so $r = \frac{1}{4\pi\varepsilon_0}\frac{e^2}{2|E|}$.
2. Convert the energy: $|E| = 3.4\,\mathrm{eV} = 3.4 \times 1.6 \times 10^{-19} = 5.44 \times 10^{-19}\,\mathrm{J}$.
3. Numerator: $9 \times 10^{9} \times (1.6 \times 10^{-19})^2 = 9 \times 10^{9} \times 2.56 \times 10^{-38} = 2.304 \times 10^{-28}$.
4. Denominator: $2|E| = 1.088 \times 10^{-18}$.
5. $r = \frac{2.304 \times 10^{-28}}{1.088 \times 10^{-18}} = 2.12 \times 10^{-10}\,\mathrm{m}$, which is option $3$.
6. Check: $r_2 = 4a_0 = 4 \times 0.53 \times 10^{-10} = 2.12 \times 10^{-10}\,\mathrm{m}$, the same value.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (4 steps)

**Printed in the booklet** (page 6)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q010_274c9058_30102026.png?v=274c9058de12)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q010_8975e5df_30102026.png?v=8975e5df1c1f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a hydrogen orbit the total energy fixes the radius. The relation is $E = -\frac{1}{4\pi\varepsilon_0}\frac{e^2}{2r}$, so $r = \frac{ke^2}{2|E|}$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Most students pick option 4. All four options read 2.1 and differ only in the power of ten. So the whole question is keeping the exponent straight. Lose one power while changing $3.4\,\mathrm{eV}$ into $5.44 \times 10^{-19}\,\mathrm{J}$ and you get exactly $2.1 \times 10^{-11}\,\mathrm{m}$ instead of $2.1 \times 10^{-10}\,\mathrm{m}$.
- **Why:** You have to work out a radius from an energy the question gives you. The question supplies '$1\,\mathrm{eV} = 1.6 \times 10^{-19}\,\mathrm{J}$' and '$\frac{1}{4\pi\varepsilon_0} = 9 \times 10^{9}$'.
- **Note:** Options 1 and 2 are the same digits with the power of ten moved the other way. You can also reach the correct answer with no conversion at all: $r = n^2 a_0 = 4 \times 0.53\,\mathrm{\AA}$.
<!--/ecat-->

## Q11

Physics · Laws of Motion

A box of mass $15\,\mathrm{kg}$ is kept on the floor of a stationary trolley. The coefficient of static friction between the box and the trolley is $0.12$. Keeping the box in stationary state over the trolley, the maximum acceleration with which the trolley can be moved horizontally in $\mathrm{m\,s^{-2}}$ is:

($g = 10\,\mathrm{m/s^2}$)

- (1) $2.1$
- (2) $1.8$
- (3) $1.5$
- **(4)** $1.2$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q011_sol_1_ea78645a_30102026.png?v=ea78645ada55)

![drawn: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q011_solution_1_967484cc_30102026.svg?v=967484ccf0de)  
*drawn by code/lib/physics_figure.py*

1. $a = \mu g = 0.12 \times 10 = 1.2\ \mathrm{m/s^2}$

**Solved independently** (answer withheld)

1. The only horizontal force available to accelerate the box is static friction from the trolley floor.
2. Its maximum value is $f_{max} = \mu_s N = \mu_s m g = 0.12 \times 15 \times 10 = 18\,\mathrm{N}$.
3. $a_{max} = \frac{f_{max}}{m} = \frac{18}{15} = 1.2\,\mathrm{m\,s^{-2}}$, i.e. $\mu_s g$, independent of the mass.
4. That is option $4$.

**Subtopic:** Static Friction · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 6)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q011_1c466c01_30102026.png?v=1c466c011a1a)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q011_b1e64c4f_30102026.png?v=b1e64c4f982a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The box moves along with the trolley only while static friction supplies its acceleration. So the limit is $\mu g$. The box's own mass cancels out.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Most students pick option 2. The question hands you both $m = 15\,\mathrm{kg}$ and $g = 10\,\mathrm{m/s^2}$. Friction only ever reaches the box as $\mu m g$. So putting the mass where $g$ belongs gives $0.12 \times 15 = 1.8$. Do it properly and divide the friction force $18\,\mathrm{N}$ by the same $15\,\mathrm{kg}$. The mass cancels and you are left with $1.2\,\mathrm{m\,s^{-2}}$.
- **Why:** You have to find the largest acceleration that static friction can pass on. The question asks for 'Keeping the box in stationary state over the trolley, the maximum acceleration with which the trolley can be moved'.
<!--/ecat-->

## Q12

Physics · Capacitance

Five capacitors of capacitances $C_1 = C_2 = C_3 = C_4 = 10\,\mu\mathrm{F}$ and $C_5 = 2.5\,\mu\mathrm{F}$ are connected as shown, along with a battery of $50\,\mathrm{V}$.

The equivalent capacitance and the charges on each capacitor respectively are:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q012_1fd1cb36_30102026.png?v=1fd1cb361eb4)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q012_question_da3caf57_30102026.svg?v=da3caf57efa8)  
*drawn by code/lib/physics_figure.py*

- (1) $5\,\mu\mathrm{F}$, $125\,\mu\mathrm{C}$ on $C_1$ to $C_4$ and $25\,\mu\mathrm{C}$ on $C_5$
- **(2)** $5\,\mu\mathrm{F}$, $125\,\mu\mathrm{C}$ on all capacitors
- (3) $5\,\mu\mathrm{F}$, $250\,\mu\mathrm{C}$ on all capacitors
- (4) $4\,\mu\mathrm{F}$, $250\,\mu\mathrm{C}$ on $C_1$ to $C_4$ and $125\,\mu\mathrm{C}$ on $C_5$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q012_sol_1_8c6b0046_30102026.png?v=8c6b0046b9b7)

![drawn: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q012_solution_1_12660a12_30102026.svg?v=12660a12ffb3)  
*drawn by code/lib/physics_figure.py*

![printed figure: solution_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q012_sol_2_e728cf72_30102026.png?v=e728cf724829)

1. $C_{\mathrm{eq}} = 2.5 + 2.5 = 5\ \mu\mathrm{F}$`
2. $q_1 = q_2 = q_3 = q_4 = 2.5 \times 50 = 125\ \mu\mathrm{C}$
3. $q_5 = 2.5 \times 50 = 125\ \mu\mathrm{C}$

**Solved independently** (answer withheld)

1. Reading the figure, the battery's two terminals are the left node $A$ and the right node $B$; $C_5$ joins $A$ to $B$ directly, and $C_1, C_2, C_3, C_4$ form the outer loop from $A$ up the left side, across the top and down the right side to $B$.
2. So the circuit is the series chain $C_1$-$C_2$-$C_3$-$C_4$ in parallel with $C_5$, both across $50\,\mathrm{V}$.
3. Series chain: $\frac{1}{C_s} = \frac{4}{10}$, so $C_s = 2.5\,\mu\mathrm{F}$.
4. $C_{eq} = C_s + C_5 = 2.5 + 2.5 = 5\,\mu\mathrm{F}$.
5. Charge on the series chain, the same on each of $C_1$ to $C_4$: $Q = C_s V = 2.5 \times 50 = 125\,\mu\mathrm{C}$.
6. $C_5$ has the full $50\,\mathrm{V}$ across it: $Q_5 = 2.5 \times 50 = 125\,\mu\mathrm{C}$, the same value.
7. Therefore $5\,\mu\mathrm{F}$ with $125\,\mu\mathrm{C}$ on every capacitor, which is option $2$.

**Subtopic:** Combination of Capacitors · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 7)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q012_504a1b16_30102026.png?v=504a1b16248f)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q012_a8035bcc_30102026.png?v=a8035bcc95d7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Capacitors in series all carry the same charge. Parallel branches all have the same voltage. Both the equivalent capacitance and every single charge follow from those two rules.
- **Why:** You have to give two answers at once. The question asks 'The equivalent capacitance and the charges on each capacitor respectively are' and every option carries a capacitance and a charge together.
<!--/ecat-->

## Q13

Physics · Gravitation

The amount of work done to raise a mass '$m$' from the surface of the Earth to a height equal to the radius of the Earth '$R$' will be

- (1) $2\,mg\,R$
- (2) $mg\dfrac{R}{4}$
- (3) $mgR$
- **(4)** $mg\dfrac{R}{2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. W.D. $= U_2 - U_1$
2. $= -\frac{GMm}{R + R} - \left(\frac{-GMm}{R}\right)$
3. $= -\frac{GMm}{2R} + \frac{GMm}{R}$
4. $= \frac{GMm}{2R} = \frac{mgR}{2}$

**Solved independently** (answer withheld)

1. Gravitational potential energy at distance $r$ from the centre is $U = -\frac{GMm}{r}$.
2. At the surface $r = R$: $U_i = -\frac{GMm}{R}$. At height $R$ the distance is $r = 2R$: $U_f = -\frac{GMm}{2R}$.
3. $W = U_f - U_i = -\frac{GMm}{2R} + \frac{GMm}{R} = \frac{GMm}{2R}$.
4. Using $g = \frac{GM}{R^2}$, i.e. $GM = gR^2$: $W = \frac{gR^2 m}{2R} = \frac{mgR}{2}$, which is option $4$.

**Subtopic:** Gravitational Potential Energy · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q013_b9ea9c87_30102026.png?v=b9ea9c875aa8)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q013_fddc1a5c_30102026.png?v=fddc1a5c8b4a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The rise here is as big as the Earth's radius. So the work against gravity is the change in $-\frac{GMm}{r}$. For $r$ going from $R$ to $2R$ that comes to $\frac{mgR}{2}$.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Most students pick option 3. They reach for $W = mgh$ and put $h = R$, which gives $mgR$. That answer is right only when the rise is small enough for $g$ to stay steady. Here the question says 'a height equal to the radius of the Earth'. Over that rise $g$ drops to a quarter. The real energy change is $\frac{mgR}{2}$.
- **Why:** You have to find the change in potential energy over a rise that is not small. The question says 'to a height equal to the radius of the Earth' and the options are written in terms of $mgR$.
<!--/ecat-->

## Q14

Physics · Units and Measurements

Each side of a metallic cube of mass $5.580\,\mathrm{kg}$ is measured to the $9.0\,\mathrm{cm}$. Keeping the significant figures in view, the density of the material of the cube can be best expressed as $X \times 10^{3}\,\mathrm{kg\,m^{-3}}$ where the value of $X$ is:

- (1) $7.654$
- (2) $7.6$
- (3) $7.65$
- **(4)** $7.7$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Density $= = \frac{\text{Mass}}{\text{Volume}}$
2. $= \frac{5.580\ \mathrm{kg}}{(9.0\ \mathrm{cm})^{3}}$
3. $= \frac{5.580}{729} \times 10^{6}\ \frac{\mathrm{kg}}{\mathrm{m^3}}$
4. $= 0.007654321 \times 10^{6}\ \frac{\mathrm{kg}}{\mathrm{m^3}}$
5. $= 7.654 \times 10^{3}\ \frac{\mathrm{kg}}{\mathrm{m^3}}$
6. $= 7.7 \times 10^{3}\ \frac{\mathrm{kg}}{\mathrm{m^3}}$
7. Hence, on comparing
8. $X = 7.7$

**Solved independently** (answer withheld)

1. Side in SI: $a = 9.0\,\mathrm{cm} = 0.090\,\mathrm{m}$.
2. Volume: $V = a^3 = (0.090)^3 = 7.29 \times 10^{-4}\,\mathrm{m^3}$.
3. Density: $\rho = \frac{m}{V} = \frac{5.580}{7.29 \times 10^{-4}} = 7654.3\,\mathrm{kg\,m^{-3}} = 7.6543 \times 10^{3}\,\mathrm{kg\,m^{-3}}$.
4. Significant figures: the mass $5.580\,\mathrm{kg}$ has $4$, the side $9.0\,\mathrm{cm}$ has $2$; a product/quotient keeps the smaller count, so $2$.
5. Rounding $7.6543 \times 10^{3}$ to two significant figures gives $7.7 \times 10^{3}$, so $X = 7.7$, which is option $4$.

**Subtopic:** Significant Figures · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 8)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q014_32cff64b_30102026.png?v=32cff64b1257)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q014_80d80161_30102026.png?v=80d801610b72)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** You report a result to as many significant figures as its weakest measurement. Here the side is 9.0 cm, which carries only two.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1. $5.580 / (0.090)^3$ gives 7654.3, so 7.654 is what the calculator shows. If you treat this as a plain division you stop there. But the question adds 'Keeping the significant figures in view'. The side is printed as 9.0 cm, which is two figures. So the density is reported as $7.7 \times 10^3$.
- **Why:** You have to work out a density and then round it by the significant-figure rule. The question says 'Keeping the significant figures in view'. Options 7.654, 7.65, 7.6 and 7.7 are the same number cut at different places.
<!--/ecat-->

## Q15

Physics · Kinematics

> ⚠ The independent solve chose (unsure); the booklet prints (1).

The following plots show variation of velocity ($v$) with time ($t$) of a ball thrown vertically upward, and falling back. Which of the following plots is/are correct?

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q015_b63eac52_30102026.png?v=b63eac52d6d2)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q015_question_51f8f748_30102026.svg?v=51f8f748ec2d)  
*drawn by code/lib/physics_figure.py*

- **(A.)** [graph]
- **(B.)** [graph]
- **(C.)** [graph]
- **(D.)** [graph]
- **(E.)** [graph]

- **(1)** C only
- (2) D only
- (3) B only
- (4) A and E only

**Answer** — booklet: (1) · independent solve: (unsure) · ai_unsure

**Publisher's solution**

1. During the whole journey, acceleration due to gravity is vertically downward.
2. Therefore, slope of velocity vs time curve should be negative throughout the journey.

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q015_sol_1_793102c6_30102026.png?v=793102c68d30)

![drawn: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q015_solution_1_c7c76158_30102026.svg?v=c7c76158f0b6)  
*drawn by code/lib/physics_figure.py*

3. $\therefore$ Statement (C) is correct

**Solved independently** (answer withheld)

1. The question asks which of five printed $v$-$t$ plots correctly describe a ball thrown vertically up and falling back; the correct plot is a straight line of constant negative slope $-g$ crossing $v = 0$ at the top of the flight (taking up as positive).
2. All five candidate plots A to E are drawings; in the input they are recorded as the placeholder text `[graph]`, carrying no information.
3. The only image supplied, papers/figures/2026_11/q015_stem_figure_1.png, is $372 \times 208$ px and contains just one partly-cropped axis pair (a curve falling to zero and rising again) plus the tail of a neighbouring line.
4. With four of the five plots unseen, no option can be settled, so the answer is recorded as unsure.

**Subtopic:** Displacement-Time and Velocity-Time Graphs · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 8)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q015_6651a87f_30102026.png?v=6651a87fde33)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q015_7461d5ae_30102026.png?v=7461d5ae0920)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** A ball thrown up and caught again has one constant downward acceleration all the way. So its $v$-$t$ graph is a single straight line with a fixed slope. It crosses zero at the top of the flight.
- **Why:** You have to judge plotted velocity histories. The question says 'The following plots show variation of velocity ($v$) with time ($t$)' and the lettered items A to E are the plots themselves.
<!--/ecat-->

## Q16

Physics · Oscillations

The sum of kinetic energy and potential energy of a simple pendulum bob is $0.02$ joule. The speed of the simple pendulum bob at equilibrium position is approximately:

(Consider mass of the bob $= 20\,\mathrm{g}$)

- (1) $0.2\,\mathrm{m/s}$
- **(2)** $1.41\,\mathrm{m/s}$
- (3) $14.1\,\mathrm{m/s}$
- (4) $2.0\,\mathrm{m/s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. At equilibrium position
2. Total energy $=$ K.E
3. $\frac{1}{2}mv^{2} = 0.02$
4. $\frac{1}{2} \times 20 \times v^{2} \times 10^{-3} = 2 \times 10^{-2}$
5. $v = \sqrt{2}$
6. $v = 1.41\ \mathrm{m/s}$

**Solved independently** (answer withheld)

1. The total mechanical energy of the bob is constant: $E = K + U = 0.02\,\mathrm{J}$.
2. At the equilibrium (mean) position the potential energy is taken as zero, so the whole $0.02\,\mathrm{J}$ is kinetic.
3. $\tfrac{1}{2}mv^2 = 0.02$ with $m = 20\,\mathrm{g} = 0.02\,\mathrm{kg}$.
4. $v^2 = \frac{2 \times 0.02}{0.02} = 2$, so $v = \sqrt{2} = 1.41\,\mathrm{m/s}$, which is option $2$.

**Subtopic:** Energy Conservation in SHM · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q016_98a7f519_30102026.png?v=98a7f51969d8)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q016_9d1d5ed0_30102026.png?v=9d1d5ed0ceb7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At the mean position all of a pendulum's energy is kinetic. So $\frac{1}{2}mv^2$ equals the total energy, which stays constant.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Most students pick option 4. The algebra ends at $v^2 = \frac{2 \times 0.02}{0.02} = 2$. 2.0 is printed as an option, so the last step gets skipped. You still have to take the square root. The speed is $\sqrt{2} = 1.41\,\mathrm{m/s}$.
- **Why:** You have to find a speed from a total energy the question gives you. It says 'The sum of kinetic energy and potential energy ... is $0.02$ joule' and 'mass of the bob $= 20\,\mathrm{g}$'.
<!--/ecat-->

## Q17

Physics · Wave Optics

In Young's double slit experiment, using monochromatic light of wavelength $\lambda$, the intensity of light at a point on the screen where the path difference is $\lambda$, is $K$ units. The intensity of light at a point where the path difference is $\dfrac{\lambda}{3}$ will be

- **(1)** $\dfrac{K}{4}$
- (2) $K$
- (3) $2K$
- (4) $\dfrac{K}{2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $I = I_0 \cos^{2}\frac{\Delta\phi}{2}$ $[I_0 \to$ maximum intensity$]$
2. $I = I_0 \cos^{2}\frac{K\Delta x}{2}$
3. $K = I_0 \cos^{2}\left(\frac{2\pi}{\lambda} \times \frac{\lambda}{2}\right)$
4. $K = I_0$
5. $K_1 = I_0 \cos^{2}\left(\frac{2\pi}{\lambda} \times \frac{\lambda}{3 \times 2}\right) = I_0 \cos^{2}\left(\frac{\pi}{3}\right)$
6. $K_1 = \frac{I_0}{4}$
7. $\frac{K}{K_1} = 4\ \Rightarrow\ K_1 = \frac{K}{4}$

**Solved independently** (answer withheld)

1. For two equal-intensity coherent sources, $I = 4I_0\cos^2\!\left(\frac{\phi}{2}\right)$, where $I_0$ is the intensity from one slit.
2. A path difference of $\lambda$ gives $\phi = \frac{2\pi}{\lambda}\cdot\lambda = 2\pi$, so $I = 4I_0\cos^2(\pi) = 4I_0 = K$, hence $I_0 = K/4$.
3. A path difference of $\lambda/3$ gives $\phi = \frac{2\pi}{\lambda}\cdot\frac{\lambda}{3} = \frac{2\pi}{3}$.
4. $I = 4I_0\cos^2\!\left(\frac{\pi}{3}\right) = 4I_0\left(\frac{1}{2}\right)^2 = I_0 = \frac{K}{4}$, which is option $1$.

**Subtopic:** Intensity Variation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q017_c31e67d2_30102026.png?v=c31e67d237c4)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q017_07a5273d_30102026.png?v=07a5273dd635)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Two-slit intensity follows $I = I_{\max}\cos^2\frac{\phi}{2}$. A path difference of $\frac{\lambda}{3}$ means a phase difference of $\frac{2\pi}{3}$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Most students pick option 4. Here $\frac{\phi}{2} = 60^\circ$ and $\cos 60^\circ = \frac{1}{2}$. Leave the cosine unsquared and you get $\frac{K}{2}$. But intensity goes with the square of the resultant amplitude. So $K\cos^2 60^\circ = \frac{K}{4}$.
- **Why:** You have to find the factor by which the intensity changes when the path difference changes. The question says 'where the path difference is $\lambda$, is $K$ units' and the options are written as multiples of $K$.
<!--/ecat-->

## Q18

Physics · Semiconductor Electronics

In the circuit shown below, the voltage appearing across the diode $D$ will be of the form:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_41edfc6b_30102026.png?v=41edfc6b9c45)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_question_d3663edf_30102026.svg?v=d3663edf4eef)  
*drawn by code/lib/physics_figure.py*

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_option_1_968755db_30102026.png?v=968755db5e01) ![drawn: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_option_1_da72dc60_30102026.svg?v=da72dc60dc80)  
*drawn by code/lib/physics_figure.py* — [graph]
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_option_2_e5f0f0fb_30102026.png?v=e5f0f0fbfebd) ![drawn: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_option_2_d87ce041_30102026.svg?v=d87ce04164f5)  
*drawn by code/lib/physics_figure.py* — [graph]
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_option_3_8acf3455_30102026.png?v=8acf34557d85) ![drawn: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_option_3_5e33fc40_30102026.svg?v=5e33fc403e7b)  
*drawn by code/lib/physics_figure.py* — [graph]
- **(4)** ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_option_4_e08f05da_30102026.png?v=e08f05da45f7) ![drawn: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_option_4_1f686efe_30102026.svg?v=1f686efe47d4)  
*drawn by code/lib/physics_figure.py* — [graph]

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Voltage drop will be across the diode, when it will be in reverse bias 1

![printed figure: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_sol_1_b26ced08_30102026.png?v=b26ced08fbd0)

![drawn: solution_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_solution_1_502add93_30102026.svg?v=502add93edfa)  
*drawn by code/lib/physics_figure.py*

2. In positive half cycle it will be in reverse biased

![printed figure: solution_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_sol_2_ecd5fe78_30102026.png?v=ecd5fe789380)

![drawn: solution_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_solution_2_2ca57b9b_30102026.svg?v=2ca57b9b3bc5)  
*drawn by code/lib/physics_figure.py*


![printed figure: solution_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q018_sol_3_672bc7ba_30102026.png?v=672bc7babbb6)

![drawn: solution_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q018_solution_3_f50203f6_30102026.svg?v=f50203f65105)  
*drawn by code/lib/physics_figure.py*


**Solved independently** (answer withheld)

1. The circuit is a source $v_i$ in series with a diode $D$ and a load $R$, i.e. a half-wave rectifier.
2. During the half cycle that forward biases $D$, the ideal diode behaves as a short, so $v_D = 0$ and the whole $v_i$ appears across $R$.
3. During the other half cycle $D$ is reverse biased, the current is zero, so there is no drop across $R$ and the entire source voltage stands across the diode: $v_D = v_i$, a single half-sine.
4. Hence $v_D$ must be a half-sine for one half period and flat zero for the other half period.
5. Option $1$ ($|\sin|$, two humps of the same sign) and option $3$ ($-|\sin|$) are full-wave shapes a single diode cannot produce; option $2$ is the undistorted sine, which would need a short in place of the diode.
6. Only option $4$ shows one hump followed by a flat zero, so it is the answer.

**Subtopic:** Half Wave Rectifier · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 10)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q018_f31d01d0_30102026.png?v=f31d01d08514)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q018_5339b5e7_30102026.png?v=5339b5e7c6ba)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** An ideal diode drops no voltage while it conducts and passes nothing while it blocks. So the voltage across it is zero for one half of the input. For the other half it follows the source.
- **Why:** You have to match a diode's blocking behaviour to a waveform. The question says 'the voltage appearing across the diode $D$ will be of the form' and the four options are graphs.
<!--/ecat-->

## Q19

Physics · Alternating Current

An ac circuit contains a resistance of $1\,\mathrm{k\Omega}$, a capacitor of $0.1\,\mu\mathrm{F}$ and an inductor of $1\,\mathrm{mH}$ connected in series. The resonance frequency of the circuit is approximately:

- (1) $13.5\,\mathrm{kHz}$
- (2) $10.1\,\mathrm{kHz}$
- (3) $20.7\,\mathrm{kHz}$
- **(4)** $15.9\,\mathrm{kHz}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Resonance frequency
2. $f_0 = \frac{1}{2\pi\sqrt{LC}}$
3. $= \frac{1}{2\pi\sqrt{1 \times 10^{-7} \times 10^{-3}}}$
4. $= 15.9\ \mathrm{kHz}$

**Solved independently** (answer withheld)

1. At series resonance $X_L = X_C$, giving $f_0 = \frac{1}{2\pi\sqrt{LC}}$; the resistance does not enter.
2. $LC = (1 \times 10^{-3})(0.1 \times 10^{-6}) = 1 \times 10^{-10}$, so $\sqrt{LC} = 1 \times 10^{-5}\,\mathrm{s}$.
3. $f_0 = \frac{1}{2\pi \times 10^{-5}} = \frac{10^{5}}{6.283} = 1.59 \times 10^{4}\,\mathrm{Hz}$.
4. That is $15.9\,\mathrm{kHz}$, which is option $4$.

**Subtopic:** Resonance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q019_23483d80_30102026.png?v=23483d80e607)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q019_bec6451f_30102026.png?v=bec6451ff355)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Series resonance happens where the two reactances cancel. That is at $f = \frac{1}{2\pi\sqrt{LC}}$. The resistance has no say in it.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  There is no real trap here. The other three options are just kilohertz values spread around the answer. $\sqrt{LC} = 10^{-5}\,\mathrm{s}$, so $f = 15.9\,\mathrm{kHz}$. The slips this formula invites move the result by a factor of $2\pi$, which gives 100 kHz, or by a power of ten. Neither slip gives 13.5, 10.1 or 20.7.
- **Why:** You have to find a resonance frequency from an inductance and a capacitance. The question asks 'The resonance frequency of the circuit is approximately' and gives $L = 1\,\mathrm{mH}$ and $C = 0.1\,\mu\mathrm{F}$.
- **Note:** The $1\,\mathrm{k\Omega}$ resistance is printed but you never use it. Resonance depends on $L$ and $C$ alone.
<!--/ecat-->

## Q20

Physics · Wave Optics

In interference and diffraction, the light energy is redistributed. If it reduces in one region, producing a dark fringe, it increases in another region, producing a bright fringe.

Choose the correct answer from the options given below:

- **(A.)** As there is no gain or loss of energy, these phenomena are consistent with the principle of conservation of energy.
- **(B.)** Diffraction and interference are characteristics exhibited only by light waves.

- (1) A is true and B is also true
- (2) A is false, but B is true
- **(3)** A is true, but B is false
- (4) Both A and B are false

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In interference and diffraction there is no loss of energy, the energy gets redistributed.
2. Interference and diffraction both are exhibited in light as well as sound waves.

**Solved independently** (answer withheld)

1. Statement A: in interference and diffraction the light energy is only redistributed, the average over the pattern equalling the incident energy, so the phenomena obey conservation of energy. A is true.
2. Statement B: diffraction and interference are general wave phenomena, shown by sound waves, water waves and matter waves as well as by light, so they are not exclusive to light. B is false.
3. A true and B false is option $3$.

**Subtopic:** Superposition of Waves, Diffraction of Light · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q020_6d421787_30102026.png?v=6d421787baee)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q020_938a7a34_30102026.png?v=938a7a346004)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Interference and diffraction only move energy about. So they break no conservation law. They are also not special to light. Every wave shows them.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1. Statement B reads like a line from the chapter, and every word of it is right except 'only'. Sound shows interference as beats, and water waves spread through a gap. So that one word makes B false, and A stands alone.
- **Why:** You have to check two printed claims against the physics you know. Statement B says these are 'characteristics exhibited only by light waves'. Statement A makes a conservation claim.
<!--/ecat-->

## Q21

Physics · Waves

For a travelling harmonic wave $y(x,\,t) = 2.0 \cos 2\pi(10t - 0.0080x + 0.35)$, where $x$ and $y$ are in cm and $t$ in s. The phase difference between oscillatory motion of two points separated by a distance of $0{\cdot}5\,\mathrm{m}$ is:

- (1) $0.08\,\pi\ \mathrm{rad}$
- **(2)** $0.8\,\pi\ \mathrm{rad}$
- (3) $8\,\pi\ \mathrm{rad}$
- (4) $0.008\,\pi\ \mathrm{rad}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $y(x,\,t) = 2.0\cos 2\pi(10t - 0.008x + 0.35)$
2. Total phase
3. $\phi = 20\pi - 2\pi \times 8 \times 10^{-3}x + 2\pi \times 0.35$
4. $\Delta\phi = k\Delta x$
5. $\Delta\phi = 2\pi \times 8 \times 10^{-3}\,\Delta x$
6. $= 2\pi \times 8 \times 10^{-3} \times \left(\frac{100}{2}\right)$
7. $= 8\pi \times 10^{-1} = 0.8\pi$

**Solved independently** (answer withheld)

1. The phase of the wave is $\Phi = 2\pi(10t - 0.0080x + 0.35)$, with $x$ in cm.
2. At a fixed instant, two points separated by $\Delta x$ differ in phase by $|\Delta\Phi| = 2\pi(0.0080)\,\Delta x$.
3. Convert the separation to the same unit as $x$: $\Delta x = 0.5\,\mathrm{m} = 50\,\mathrm{cm}$.
4. $|\Delta\Phi| = 2\pi \times 0.0080 \times 50 = 2\pi \times 0.4 = 0.8\pi\ \mathrm{rad}$, which is option $2$.

**Subtopic:** Displacement Relation in a Progressive Wave · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 11)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q021_a95602f3_30102026.png?v=a95602f33bfe)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q021_250f3e5a_30102026.png?v=250f3e5ae30e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The phase difference between two points of a travelling wave is $\Delta\phi = 2\pi k\,\Delta x$. You read it off the printed argument. $\Delta x$ has to be in the same unit as $x$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Most students pick option 4. The wave is printed with '$x$ and $y$ are in cm'. So the 0.5 m gap has to go in as 50 cm. Put 0.5 straight into $2\pi \times 0.0080 \times \Delta x$ and you get $0.008\pi$ instead of $0.8\pi$.
- **Why:** You have to work out a phase difference from the wave as printed. The question says 'where $x$ and $y$ are in cm' and also 'two points separated by a distance of $0{\cdot}5\,\mathrm{m}$'.
<!--/ecat-->

## Q22

Physics · Laws of Motion

The magnitude and direction of the acceleration produced in a body of mass $5\,\mathrm{kg}$ when two mutually perpendicular forces $8\,\mathrm{N}$ and $6\,\mathrm{N}$ act on it, are respectively:

- (1) $20\,\mathrm{m\,s^{-2}}$; $\tan^{-1}(4/3)$ with $8\,\mathrm{N}$ force
- (2) $2\,\mathrm{m\,s^{-2}}$; $\tan^{-1}(3/4)$ with $6\,\mathrm{N}$ force
- (3) $2\,\mathrm{m\,s^{-2}}$; $\tan^{-1}(4/3)$ with $8\,\mathrm{N}$ force
- **(4)** $2\,\mathrm{m\,s^{-2}}$; $\tan^{-1}(3/4)$ with $8\,\mathrm{N}$ force

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $F_{\mathrm{net}} = \sqrt{6^{2} + 8^{2}}$
2. $a = \frac{F_{\mathrm{net}}}{m} = \frac{10}{5} = 2\ \mathrm{m/s^2}$
3. $\tan\theta = \frac{6}{8}$
4. $\theta = \tan^{-1}\left(\frac{3}{4}\right)$ from $8\,\mathrm{N}$

**Solved independently** (answer withheld)

1. The two forces are perpendicular, so the resultant is $F = \sqrt{8^2 + 6^2} = \sqrt{100} = 10\,\mathrm{N}$.
2. $a = \frac{F}{m} = \frac{10}{5} = 2\,\mathrm{m\,s^{-2}}$, and the acceleration is along the resultant.
3. Measured from the $8\,\mathrm{N}$ force, the angle satisfies $\tan\theta = \frac{6}{8} = \frac{3}{4}$, so $\theta = \tan^{-1}(3/4) \approx 36.9^\circ$.
4. $2\,\mathrm{m\,s^{-2}}$ at $\tan^{-1}(3/4)$ from the $8\,\mathrm{N}$ force is option $4$.

**Subtopic:** Newton's Second Law of Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q022_a3e05cb6_30102026.png?v=a3e05cb63b5c)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q022_37ef7b05_30102026.png?v=37ef7b053df5)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Forces at right angles add as $\sqrt{F_1^2 + F_2^2}$. For the direction you take the tangent of the other component over the one you measure from.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. Its magnitude is right. Its angle is the two forces taken in the order the question names them: $8/6 = 4/3$. But you measure from the 8 N force, so the opposite component is the 6 N one. The tangent is $6/8 = 3/4$.
- **Also:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Some students pick option 1. They add the squares and divide by the mass but never take the root, which gives $100/5 = 20\,\mathrm{m\,s^{-2}}$. The resultant force is $\sqrt{100} = 10\,\mathrm{N}$, so the acceleration is $2\,\mathrm{m\,s^{-2}}$.
- **Why:** You have to give a magnitude and a direction, and both must be right. The question asks 'The magnitude and direction of the acceleration ... are respectively' and every option names a value and a reference force.
- **Note:** Three options share the magnitude $2\,\mathrm{m\,s^{-2}}$. They differ only in the angle and in the force it is measured from.
<!--/ecat-->

## Q23

Physics · Capacitance

Consider two uncharged capacitors of equal capacitance $200\,\mathrm{pF}$. One of them is charged by a $100\,\mathrm{V}$ supply and disconnected. Now this capacitor is connected to the uncharged capacitor. The amount of electrostatic energy lost in the process is:

- **(1)** $0.5 \times 10^{-6}\,\mathrm{J}$
- (2) $1.0\,\mathrm{J}$
- (3) $1.0 \times 10^{-6}\,\mathrm{J}$
- (4) $0.5\,\mathrm{J}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Energy loss $= \frac{1}{2}\frac{C_1C_2}{C_1 + C_2}V^{2}$
2. $= \frac{1}{2}\left(\frac{200 \times 200}{400}\right) \times 10^{-12}(100)^{2}$
3. $= \frac{1}{2} \times 10^{6} \times 10^{-12} = 0.5 \times 10^{-6}\ \mathrm{J}$

**Solved independently** (answer withheld)

1. Initial stored energy: $U_i = \tfrac{1}{2}CV^2 = \tfrac{1}{2}(200 \times 10^{-12})(100)^2 = 1.0 \times 10^{-6}\,\mathrm{J}$.
2. Initial charge: $Q = CV = (200 \times 10^{-12})(100) = 2.0 \times 10^{-8}\,\mathrm{C}$; this is conserved when the second capacitor is connected.
3. Equal capacitances share the charge equally, so the common potential is $V' = \frac{Q}{2C} = \frac{2.0 \times 10^{-8}}{400 \times 10^{-12}} = 50\,\mathrm{V}$.
4. Final energy: $U_f = 2 \times \tfrac{1}{2}(200 \times 10^{-12})(50)^2 = 5.0 \times 10^{-7}\,\mathrm{J}$.
5. Energy lost $= U_i - U_f = 1.0 \times 10^{-6} - 0.5 \times 10^{-6} = 0.5 \times 10^{-6}\,\mathrm{J}$, which is option $1$.

**Subtopic:** Redistribution of Charges · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q023_ef28e45f_30102026.png?v=ef28e45f5881)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q023_db242541_30102026.png?v=db242541f857)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** You share the charge with an equal uncharged capacitor. That halves the voltage. Each capacitor is then left with only a quarter of the energy. So exactly half the stored energy is lost.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Most students pick option 3. The first number the data give you is $\frac{1}{2}CV^2 = \frac{1}{2} \times 200\,\mathrm{pF} \times (100)^2 = 1.0 \times 10^{-6}\,\mathrm{J}$. That number is printed as an option, so the work stops at the energy stored instead of the energy lost. Half of it survives on the two capacitors. So the loss is $0.5 \times 10^{-6}\,\mathrm{J}$.
- **Why:** You have to find the energy that goes missing after the charge is shared. The question asks for 'The amount of electrostatic energy lost in the process' and gives two equal $200\,\mathrm{pF}$ capacitors.
- **Note:** Options 2 and 4 are the same as options 3 and 1, with the picofarads read as microfarads.
<!--/ecat-->

## Q24

Physics · Work, Energy and Power

The power of a crane, which lifts a mass of $1000\,\mathrm{kg}$ to a height of $20\,\mathrm{m}$ in $10\,\mathrm{s}$ is: ($g = 9.8\,\mathrm{m/s^2}$)

- (1) $19.6\,\mathrm{W}$
- (2) $39.2\,\mathrm{W}$
- **(3)** $19.6\,\mathrm{kW}$
- (4) $39.2\,\mathrm{kW}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Power $= \frac{\text{Work}}{\text{Time}}$
2. $= \frac{mgh}{t}$
3. $= \frac{10^{3} \times 9.8 \times 20}{10} = 19.6\ \mathrm{kW}$

**Solved independently** (answer withheld)

1. Work done against gravity: $W = mgh = 1000 \times 9.8 \times 20 = 1.96 \times 10^{5}\,\mathrm{J}$.
2. $P = \frac{W}{t} = \frac{1.96 \times 10^{5}}{10} = 1.96 \times 10^{4}\,\mathrm{W}$.
3. $1.96 \times 10^{4}\,\mathrm{W} = 19.6\,\mathrm{kW}$, which is option $3$.

**Subtopic:** Power · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 12)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q024_24e8d05e_30102026.png?v=24e8d05e989e)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q024_47a8c2da_30102026.png?v=47a8c2dadbf8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Power is the work done against gravity divided by the time. So $P = \frac{mgh}{t}$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Most students pick option 1. $\frac{1000 \times 9.8 \times 20}{10} = 19600\,\mathrm{W}$. Said in kilowatts that is 19.6, and 19.6 is the figure a student writes down. The same digits are also printed in plain watts. So dropping the factor of a thousand lands you exactly on $19.6\,\mathrm{W}$.
- **Why:** You have to find a power from a mass, a height and a time. The question says 'lifts a mass of $1000\,\mathrm{kg}$ to a height of $20\,\mathrm{m}$ in $10\,\mathrm{s}$'.
- **Note:** The four options are the two numbers 19.6 and 39.2, each printed once in W and once in kW.
<!--/ecat-->

## Q25

Physics · Units and Measurements

In a vernier calliper, 20 VSD coincide with 16 MSD (each division of length $1\,\mathrm{mm}$). The least count of the vernier callipers is:

- (1) $0.2\,\mathrm{cm}$
- (2) $0.01\,\mathrm{cm}$
- **(3)** $0.02\,\mathrm{cm}$
- (4) $0.1\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Least count of vernier callipers
2. L.C. $=$ 1 MSD $-$ 1 VSD $\qquad\ldots$(i)
3. 20 VSD $=$ 16 MSD
4. 1 VSD $= \frac{16}{20}$ MSD
5. From (i)
6. L.C. $=$ 1 MSD $- \frac{16}{20}$ MSD
7. L.C. $= \frac{4}{20}$ MSD
8. L.C. $= \frac{1}{5}\,\mathrm{mm} = 0.2\ \mathrm{mm}$
9. L.C. $= 0.02\ \mathrm{cm}$

**Solved independently** (answer withheld)

1. $20$ vernier divisions span $16$ main-scale divisions, and $1\,\mathrm{MSD} = 1\,\mathrm{mm}$, so $20\,\mathrm{VSD} = 16\,\mathrm{mm}$.
2. $1\,\mathrm{VSD} = \frac{16}{20} = 0.8\,\mathrm{mm}$.
3. Least count $= 1\,\mathrm{MSD} - 1\,\mathrm{VSD} = 1.0 - 0.8 = 0.2\,\mathrm{mm}$.
4. $0.2\,\mathrm{mm} = 0.02\,\mathrm{cm}$, which is option $3$.

**Subtopic:** Least Count · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q025_84827176_30102026.png?v=848271763986)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q025_0663d55b_30102026.png?v=0663d55b1967)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A vernier's least count is one main-scale division minus one vernier division. You work it out from the coincidence the question prints. You do not recall it.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Most students pick option 2. $0.01\,\mathrm{cm}$ is the least count you carry for the callipers you used in the lab, where ten vernier divisions cover nine millimetres. This instrument is not that one. It prints 20 VSD against 16 MSD. So one vernier division is 0.8 mm and the least count is $1 - 0.8 = 0.2\,\mathrm{mm} = 0.02\,\mathrm{cm}$.
- **Why:** You have to work out the least count from the coincidence the question states. It says '20 VSD coincide with 16 MSD (each division of length $1\,\mathrm{mm}$)'.
<!--/ecat-->

## Q26

Physics · Kinematics

When a ruler falls vertically, 5 different persons catch it with different reaction times. ($g = 9.8\,\mathrm{m\,s^{-2}}$)

What is the correct order of the distance travelled by the ruler for each person?

- **(A.)** Person A has reaction time of $0.20\,\mathrm{s}$.
- **(B.)** Person B has reaction time of $0.22\,\mathrm{s}$.
- **(C.)** Person C has reaction time of $0.18\,\mathrm{s}$.
- **(D.)** Person D has reaction time of $0.19\,\mathrm{s}$.
- **(E.)** Person E has reaction time of $0.21\,\mathrm{s}$.

- (1) B > E > A > C > D
- (2) C > D > A > B > E
- **(3)** B > E > A > D > C
- (4) C > D > A > E > B

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\rightarrow$ There will be large distance for large reaction time
2. $\rightarrow$ Descending order of reaction time
3. $\Rightarrow t_B > t_E > t_A > t_D > t_C$
4. $\rightarrow$ Descending order of distance covered
5. $\Rightarrow S_B > S_E > S_A > S_D > S_C$

**Solved independently** (answer withheld)

1. A ruler released from rest falls $d = \tfrac{1}{2}gt^2$, so $d$ grows monotonically with the reaction time $t$.
2. Ranking the times in descending order: $0.22\,(B) > 0.21\,(E) > 0.20\,(A) > 0.19\,(D) > 0.18\,(C)$.
3. Numerically: $d_B = 0.237$, $d_E = 0.216$, $d_A = 0.196$, $d_D = 0.177$, $d_C = 0.159$ m.
4. Hence $B > E > A > D > C$, which is option $3$.

**Subtopic:** Freely Falling Bodies · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q026_ef7d407f_30102026.png?v=ef7d407f3aa0)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q026_906a4786_30102026.png?v=906a47863fbe)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A dropped ruler falls $\frac{1}{2}gt^2$. So the distance rises with the reaction time. The ranking is just the times put in order.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. Sort the five by reaction time starting from the smallest and you get C, D, A, E, B. That exact string is printed as an option. But it has '>' signs between the names, so it claims C's ruler fell the furthest. Distance grows with time. So the order has to start at B's $0.22\,\mathrm{s}$ and end at C's $0.18\,\mathrm{s}$.
- **Why:** You have to rank five cases on one quantity that only rises. The question asks 'What is the correct order of the distance travelled by the ruler for each person?' and the reaction times run from $0.18\,\mathrm{s}$ to $0.22\,\mathrm{s}$.
- **Note:** The four options are the two possible directions of the ranking, each crossed with the two possible orders of the closest pair, C at $0.18\,\mathrm{s}$ and D at $0.19\,\mathrm{s}$.
<!--/ecat-->

## Q27

Physics · Current Electricity

A uniform metallic wire having resistance $4\,\Omega$ is bent to form a square loop ($ABCD$) (see figure). A resistance of $2\,\Omega$ is connected between points $B$ and $D$ and a battery of $2\,\mathrm{V}$ is connected across points $A$ and $C$ as shown in the figure. Now the value of current ($I$) is :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q027_14d97603_30102026.png?v=14d97603e6a4)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q027_question_a48ff989_30102026.svg?v=a48ff9897d2f)  
*drawn by code/lib/physics_figure.py*

- **(1)** $2\,\mathrm{A}$
- (2) $8\,\mathrm{A}$
- (3) $4.5\,\mathrm{A}$
- (4) $4\,\mathrm{A}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\rightarrow$ Each side will have resistance of $1\,\Omega$
2. $\rightarrow$ It is balanced wheat stone bridge
3. $\rightarrow$ No current in the resistance of $2\,\Omega$
4. $\rightarrow$ $[R_{\text{effective}}]_{AC} = 1\,\Omega$
5. $\rightarrow$ $I = \frac{E}{R_{\text{eff.}}} = \frac{2}{1}$
6. $\rightarrow$ $I = 2\,\mathrm{A}$

**Solved independently** (answer withheld)

1. The $4\,\Omega$ wire is uniform and bent into a square, so each of the four sides has resistance $\frac{4}{4} = 1\,\Omega$.
2. The battery is across the diagonal $A$-$C$, and the two routes between them are $A$-$B$-$C$ $= 1 + 1 = 2\,\Omega$ and $A$-$D$-$C$ $= 1 + 1 = 2\,\Omega$.
3. These routes are identical, so $B$ and $D$ are at the same potential: the $2\,\Omega$ bridging them is a balanced-bridge arm and carries no current.
4. The two $2\,\Omega$ arms are then simply in parallel: $R_{AC} = \frac{2 \times 2}{2 + 2} = 1\,\Omega$.
5. $I = \frac{V}{R_{AC}} = \frac{2}{1} = 2\,\mathrm{A}$, which is option $1$.

**Subtopic:** Wheatstone Bridge Principle · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 13)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q027_2ebf5312_30102026.png?v=2ebf53125d5c)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q027_4e3e8cb5_30102026.png?v=4e3e8cb5531b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A square of uniform wire fed at opposite corners is two equal paths in parallel, and each path is two sides long. The resistor on the diagonal sits between two points at the same potential, so it carries no current.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Most students pick option 4. Each side is $1\,\Omega$. Count only one side per corner-to-corner path and you get $1 \parallel 1 = 0.5\,\Omega$ and $I = 4\,\mathrm{A}$. But each path from $A$ to $C$ is two sides in series. So each path is $2\,\Omega$, the pair together is $1\,\Omega$, and $I = 2\,\mathrm{A}$.
- **Why:** You have to find the current through the network once you have reduced it. The question says 'A uniform metallic wire having resistance $4\,\Omega$ is bent to form a square loop' and 'a battery of $2\,\mathrm{V}$ ... connected across points $A$ and $C$'.
- **Note:** The figure only repeats the connections the question already names. So the network is fixed by the text: four $1\,\Omega$ sides, $2\,\Omega$ across $BD$, and the supply across the diagonal $AC$.
<!--/ecat-->

## Q28

Physics · Current Electricity

A room heater is rated $400\,\mathrm{W}$, $220\,\mathrm{V}$. If the supply voltage drops to $200\,\mathrm{V}$, what will be the power consumed (approximately)?

- (1) $200\,\mathrm{W}$
- (2) $400\,\mathrm{W}$
- **(3)** $331\,\mathrm{W}$
- (4) $121\,\mathrm{W}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Rated power of heater
2. $P_0 = \frac{V_0^{2}}{R}\qquad\ldots$(i)
3. Consumed power
4. $P_c = \frac{V^{2}}{R}\qquad\ldots$(ii)$\quad[V \to$ applied voltage$]$
5. From (i) and (ii)
6. $\frac{P_c}{P_0} = \frac{V^{2}}{V_0^{2}}$
7. $P_c = \left[\frac{V}{V_0}\right]^{2}P_0$
8. $P_c = \left[\frac{200}{220}\right]^{2} \times 400$
9. $P_c = 331\ \mathrm{W}$

**Solved independently** (answer withheld)

1. The rating fixes the heater's resistance: $R = \frac{V^2}{P} = \frac{220^2}{400} = \frac{48400}{400} = 121\,\Omega$.
2. The resistance does not change with the supply, so at the reduced voltage $P' = \frac{V'^2}{R}$.
3. $P' = \frac{200^2}{121} = \frac{40000}{121} = 330.6\,\mathrm{W} \approx 331\,\mathrm{W}$, which is option $3$.
4. Equivalently $P' = P\left(\frac{200}{220}\right)^2 = 400 \times 0.826 = 331\,\mathrm{W}$.

**Subtopic:** Electrical Energy and Power · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q028_10b62d34_30102026.png?v=10b62d348179)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q028_1993f73f_30102026.png?v=1993f73ffb4b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A heater's resistance is fixed by its rating. The power it then draws goes with the square of whatever voltage it gets.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Most students pick option 4. The first step is the resistance, $R = \frac{220^2}{400} = 121\,\Omega$. 121 is printed as though it were the answer in watts. You still have one step to go: $P = \frac{200^2}{121} = 331\,\mathrm{W}$.
- **Why:** You have to find the power drawn when the supply voltage changes. The question says 'rated $400\,\mathrm{W}$, $220\,\mathrm{V}$' and 'the supply voltage drops to $200\,\mathrm{V}$'.
<!--/ecat-->

## Q29

Physics · Magnetic Effect of Electric Current

A 100-turn closely wound circular coil of radius $5\,\mathrm{cm}$ has a magnetic field of $3.14 \times 10^{-3}\,\mathrm{T}$ at its centre. The current flowing through the coil, and the magnitude of the magnetic moment of this coil are, respectively :

(Take $\mu_0 = 4\pi \times 10^{-7}\,\mathrm{T\,m/A}$)

- (1) $2\,\mathrm{A}$, $10\,\mathrm{A\,m^2}$
- (2) $2.5\,\mathrm{A}$, $20\,\mathrm{A\,m^2}$
- (3) $2\,\mathrm{A}$, $4\,\mathrm{A\,m^2}$
- **(4)** $2.5\,\mathrm{A}$, $2\,\mathrm{A\,m^2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Magnetic field of a circular loop:
2. $B_0 = \frac{\mu_0 N i}{2R}$
3. $i = \frac{2RB_0}{\mu_0 N} = \frac{2 \times 5 \times 10^{-2} \times 3.14 \times 10^{-3}}{4\pi \times 10^{-7} \times 100}$
4. $i = 2.5\ \mathrm{A}$
5. Magnetic moment
6. $M = NiA$
7. $= 100 \times 2.5 \times 3.14 \times (5 \times 10^{-2})^{2}\ \ [\because A = \pi R^{2}]$
8. $= 2\ \mathrm{A\,m^2}$

**Solved independently** (answer withheld)

1. Field at the centre of a tightly wound circular coil: $B = \frac{\mu_0 N I}{2r}$.
2. Substitute: $3.14 \times 10^{-3} = \frac{(4\pi \times 10^{-7})(100)\,I}{2 \times 0.05} = 4\pi \times 10^{-4}\,I$.
3. $4\pi \times 10^{-4} = 1.2566 \times 10^{-3}$, so $I = \frac{3.14 \times 10^{-3}}{1.2566 \times 10^{-3}} = 2.5\,\mathrm{A}$.
4. Coil area: $A = \pi r^2 = \pi(0.05)^2 = 7.854 \times 10^{-3}\,\mathrm{m^2}$.
5. Magnetic moment: $m = NIA = 100 \times 2.5 \times 7.854 \times 10^{-3} = 1.96 \approx 2\,\mathrm{A\,m^2}$.
6. $2.5\,\mathrm{A}$ with $2\,\mathrm{A\,m^2}$ is option $4$.

**Subtopic:** Magnetic Field on the Axis of a Circular Current Loop, Current Carrying Loop as a Magnetic Dipole · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 14)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q029_69a16dfd_30102026.png?v=69a16dfd275d)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q029_6753c892_30102026.png?v=6753c8923df1)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The field at the centre of a coil is $B = \frac{\mu_0 N I}{2R}$, and that gives you the current. The current then gives the moment $m = NIA$. The area has to be in square metres.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. Its current is right at $2.5\,\mathrm{A}$, and that makes the second half of the pair look right too. The moment needs $A = \pi(0.05)^2 = 7.85 \times 10^{-3}\,\mathrm{m^2}$. Convert $25\,\mathrm{cm^2}$ one power of ten wrong, as $2.5 \times 10^{-2}\,\mathrm{m^2}$, and you get $100 \times 2.5 \times 0.0785 \approx 20$ instead of $2\,\mathrm{A\,m^2}$.
- **Why:** You have to give two answers and both have to be right. The question asks 'The current flowing through the coil, and the magnitude of the magnetic moment of this coil are, respectively' and every option prints a current beside a moment.
<!--/ecat-->

## Q30

Physics · Electromagnetic Induction

A rectangular wire loop of sides $8\,\mathrm{cm}$ and $3\,\mathrm{cm}$ with a small cut, is moving out of a region of uniform magnetic field of magnitude $0.3\,\mathrm{T}$ directed normal to the plane of the loop. The emf developed across the cut, if the velocity of the loop is $2\,\mathrm{cm\,s^{-1}}$, in a direction normal to the shorter side of the loop, will be :

- (1) $4.8 \times 10^{-4}$ volt
- (2) $1.2 \times 10^{-4}$ volt
- (3) $1.3 \times 10^{-4}$ volt
- **(4)** $1.8 \times 10^{-4}$ volt

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Induced emf across the shorter side
2. $E_{\text{induced}} = Bvl\ \ [\because\ \vec{B} \perp \vec{V} \perp \vec{l}\,]$
3. $= 0.3 \times 2 \times 10^{-2} \times 3 \times 10^{-2}$
4. $= 1.8 \times 10^{-4}\ \mathrm{V}$
5. $= 1.8 \times 10^{-4}$ volt

**Solved independently** (answer withheld)

1. The motional emf of an edge of length $l$ moving with speed $v$ perpendicular to a field $B$ normal to the loop is $\varepsilon = Blv$.
2. The velocity is stated to be normal to the shorter side, so it is that $3\,\mathrm{cm}$ edge which sweeps across the field boundary: $l = 0.03\,\mathrm{m}$.
3. Convert the speed: $v = 2\,\mathrm{cm\,s^{-1}} = 0.02\,\mathrm{m\,s^{-1}}$.
4. $\varepsilon = 0.3 \times 0.03 \times 0.02 = 1.8 \times 10^{-4}\,\mathrm{V}$, which is option $4$.
5. Check against the other reading: using the $8\,\mathrm{cm}$ side would give $0.3 \times 0.08 \times 0.02 = 4.8 \times 10^{-4}\,\mathrm{V}$, option 1, the distractor for motion normal to the longer side.

**Subtopic:** Motional EMF · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q030_986b480b_30102026.png?v=986b480b92b0)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q030_6f186732_30102026.png?v=6f1867328ab6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Motional emf is $Blv$. Here $l$ is the edge at right angles to the velocity. That is the edge that actually crosses the boundary of the field region.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1. Ignore the direction clause and the 8 cm side is the one you use: $0.3 \times 0.08 \times 0.02 = 4.8 \times 10^{-4}\,\mathrm{V}$. That is the answer for a loop moving at right angles to the longer side. But the question prints 'in a direction normal to the shorter side'. So the 3 cm edge is the one cutting the field, and the emf is $0.3 \times 0.03 \times 0.02 = 1.8 \times 10^{-4}\,\mathrm{V}$.
- **Why:** You have to find an emf, and its value depends on which edge sweeps through the field. The question says 'in a direction normal to the shorter side of the loop' and gives the sides as '$8\,\mathrm{cm}$ and $3\,\mathrm{cm}$'.
<!--/ecat-->

## Q31

Physics · Modern Physics

Four statements are given ($A$ is mass number):

Choose the correct answer from the options given below:

- **(A.)** The volume of a nucleus is proportional to $A^{1/3}$.
- **(B.)** The volume of a nucleus is proportional to $A$.
- **(C.)** The difference in mass of an atom and its nucleus is called the mass defect.
- **(D.)** The difference in mass of a nucleus and its constituents is called the mass defect.

- (1) A and C are true, but B and D are false
- (2) B and C are true, but A and D are false
- (3) A and D are true, but B and C are false
- **(4)** B and D are true, but A and C are false

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. As we know,
2. Size of nucleus, $r = r_0(A)^{\frac{1}{3}}$
3. $\Rightarrow\ r^{3} = r_0^{3} \cdot A$
4. $\Rightarrow\ V \propto A\ \ \left(\because V = \frac{4}{3}\pi r^{3}\right)$
5. So, option A $\to$ wrong and B $\to$ correct
6. while the difference between the actual mass of nucleus and its constituents is called the mass defect.
7. $\therefore$ option C $\to$ wrong and D $\to$ correct

**Solved independently** (answer withheld)

1. The nuclear radius obeys $R = R_0 A^{1/3}$.
2. Hence the volume $V = \frac{4}{3}\pi R^3 = \frac{4}{3}\pi R_0^3 A$ is proportional to $A$, not to $A^{1/3}$: statement B is true and statement A is false.
3. The mass defect is defined as $\Delta m = [Z m_p + (A-Z) m_n] - M_{\text{nucleus}}$, i.e. the difference between the nucleus and its constituent nucleons: statement D is true.
4. The difference between an atom's mass and its nucleus's mass is just the mass of the orbital electrons (less their binding), not the mass defect: statement C is false.
5. B and D true, A and C false is option $4$.

**Subtopic:** Distance of Closest Approach and Size of Nucleus, Mass Defect and Nuclear Binding Energy · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q031_7c3864ec_30102026.png?v=7c3864ec30d7)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q031_0894e900_30102026.png?v=0894e9005d2f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nuclear volume goes as $A$, not as $A^{1/3}$. The mass defect is the nucleus weighed against its own free protons and neutrons.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. Statement C says 'an atom and its nucleus' where 'a nucleus and its constituents' belongs. The sentence still reads like the definition. But an atom minus its nucleus is only the electrons. So accepting C along with the correct B lands you on option 2. The mass defect is what D states.
- **Why:** You have to check four printed claims one at a time. Statement A says the 'volume of a nucleus is proportional to $A^{1/3}$' and statement B says 'proportional to $A$'.
<!--/ecat-->

## Q32

Physics · Modern Physics

An unknown nucleus has a nuclear density of $2.29 \times 10^{17}\,\mathrm{kg/m^3}$ and mass of $19.926 \times 10^{-27}\,\mathrm{kg}$. Its mass number $A$ is approximately:

(Take $R_0 = 1.2 \times 10^{-15}\,\mathrm{m}$, $4\pi = 12.56$)

- **(1)** $12$
- (2) $20$
- (3) $16$
- (4) $19$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Given
2. $\rho = 2.29 \times 10^{17}\ \mathrm{kg/m^3}$, mass $m = 19.926 \times 10^{-27}\ \mathrm{kg}$
3. $R_0 = 1.2 \times 10^{-15}\ \mathrm{m}$ and $R = R_0 A^{\frac{1}{3}}$
4. Now use volume $= \frac{\text{Mass}}{\text{Density}}$
5. $\Rightarrow\ \frac{4}{3}\pi R^{3} = \frac{M}{\rho}$
6. $\Rightarrow\ \frac{4}{3}\pi\left[R_0(A)^{1/3}\right]^{3} = \frac{M}{\rho}$
7. $\Rightarrow\ \frac{4}{3}\pi R_0^{3}A = \frac{M}{\rho}$
8. $\Rightarrow\ A = \frac{M}{\rho} \times \frac{3}{4\pi \times R_0^{3}} = \frac{19.926 \times 10^{-27} \times 3}{2.29 \times 10^{17} \times 12.56 \times \left(1.2 \times 10^{-15}\right)^{3}} \approx 12$

**Solved independently** (answer withheld)

1. Volume of the nucleus from its density: $V = \frac{M}{\rho} = \frac{19.926 \times 10^{-27}}{2.29 \times 10^{17}} = 8.70 \times 10^{-44}\,\mathrm{m^3}$.
2. The nuclear radius is $R = R_0 A^{1/3}$, so $V = \frac{4}{3}\pi R_0^3 A$.
3. $\frac{4\pi}{3}R_0^3 = \frac{12.56}{3} \times (1.2 \times 10^{-15})^3 = 4.1867 \times 1.728 \times 10^{-45} = 7.235 \times 10^{-45}\,\mathrm{m^3}$.
4. $A = \frac{8.70 \times 10^{-44}}{7.235 \times 10^{-45}} = 12.0$, which is option $1$.
5. Sanity check: $19.926 \times 10^{-27}\,\mathrm{kg} = 12.0\,\mathrm{u}$, consistent with $A = 12$.

**Subtopic:** Distance of Closest Approach and Size of Nucleus · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q032_f3050d89_30102026.png?v=f3050d89db41)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q032_b0574d22_30102026.png?v=b0574d225bfe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Because $R = R_0A^{1/3}$, the volume of a nucleus goes as $A$. So every nucleus has the same density. Divide the mass by the density, then by $\frac{4}{3}\pi R_0^3$, and you get the mass number.
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 4  
  Most students pick option 4. The question prints the mass as $19.926 \times 10^{-27}\,\mathrm{kg}$, and 19 is the front of those same digits. So the mass number gets lifted straight off the printed mass and the density is never touched. Done properly through the volume, $\frac{19.926 \times 10^{-27} / 2.29 \times 10^{17}}{\frac{4}{3}\pi (1.2 \times 10^{-15})^3} = 12$.
- **Proposed:** `stem_digit_echo` — the option reproduces digits printed in the stem as the answer with no operation performed at all. answers_other_question needs the option to be true of something else, and 19 is the mass number of nothing here; arithmetic_slip needs a named wrong operation, and here nothing is computed. The device is the digits themselves being recognisable.
- **Why:** You have to recover a mass number from a density and a mass. The question supplies '$R_0 = 1.2 \times 10^{-15}\,\mathrm{m}$, $4\pi = 12.56$' for the volume step.
- **Note:** Option 2, 20, is the same digits rounded up. It is also what you would get by taking 1 u as $10^{-27}\,\mathrm{kg}$.
<!--/ecat-->

## Q33

Physics · Oscillations

Savitha, a XI standard student, while conducting an experiment to determine the effective length of a simple pendulum $L$, notes down the data of time taken to complete 30 oscillations as $60\,\mathrm{s}$ and hence calculates the length of the simple pendulum as: (Take $\pi^2 = 9.8$, and $g = 9.8\,\mathrm{m/s^2}$)

- (1) $0.75\,\mathrm{m}$
- (2) $1.5\,\mathrm{m}$
- (3) $2\,\mathrm{m}$
- **(4)** $1\,\mathrm{m}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Time taken for $30$ oscillations $= 60\ \mathrm{s}$
2. Time period of simple pendulum $=$ Time taken for 1 oscillation
3. $\Rightarrow\ T = \frac{60}{30} = 2\ \mathrm{s}$
4. $T = 2\pi\sqrt{\frac{l}{g}}\ \Rightarrow\ l = \frac{gT^{2}}{4\pi^{2}} = \frac{9.8 \times 2 \times 2}{4 \times 9.8} = 1\,\mathrm{m}$

**Solved independently** (answer withheld)

1. The period is the total time divided by the number of oscillations: $T = \frac{60}{30} = 2\,\mathrm{s}$.
2. For a simple pendulum $T = 2\pi\sqrt{\frac{L}{g}}$, so $L = \frac{gT^2}{4\pi^2}$.
3. Substituting $g = 9.8$, $T^2 = 4$, $\pi^2 = 9.8$: $L = \frac{9.8 \times 4}{4 \times 9.8} = 1\,\mathrm{m}$.
4. That is option $4$.

**Subtopic:** Time Period of a Simple Pendulum · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q033_63e8a57e_30102026.png?v=63e8a57eb51c)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q033_ce26ab65_30102026.png?v=ce26ab65a969)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Thirty oscillations in 60 s give $T = 2\,\mathrm{s}$. Turn $T = 2\pi\sqrt{L/g}$ around and you get $L = \frac{gT^2}{4\pi^2}$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Most students pick option 3. They square $2\pi$ as $2\pi^2$ instead of $4\pi^2$, which gives $L = \frac{9.8 \times 4}{2 \times 9.8} = 2\,\mathrm{m}$. The whole bracket gets squared, so the denominator is $4\pi^2$ and $L = 1\,\mathrm{m}$.
- **Why:** You have to recover a length from a timing record. The question gives 'time taken to complete 30 oscillations as $60\,\mathrm{s}$' along with '$\pi^2 = 9.8$, and $g = 9.8\,\mathrm{m/s^2}$'.
<!--/ecat-->

## Q34

Physics · Thermodynamics

An electric heater supplies heat to a system at a rate of $100\,\mathrm{W}$. If the system performs work at a rate of $75\,\mathrm{J/s}$, then the rate at which internal energy increases will be:

- (1) $75\,\mathrm{W}$
- (2) $100\,\mathrm{W}$
- (3) $125\,\mathrm{W}$
- **(4)** $25\,\mathrm{W}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Using $1^{\mathrm{st}}$ law of thermodynamics for electric heater,
2. $Q = \Delta U + W$
3. $\Rightarrow\ \frac{dQ}{dt} = \frac{d(\Delta U)}{dt} + \frac{dW}{dt}$
4. $\Rightarrow\ 100\ \mathrm{W} = \frac{d(\Delta U)}{dt} + 75\ \mathrm{W}$
5. $\therefore\ \frac{d(\Delta U)}{dt} = 25\ \mathrm{W}$

**Solved independently** (answer withheld)

1. First law of thermodynamics in rate form: $\frac{dU}{dt} = \frac{dQ}{dt} - \frac{dW}{dt}$.
2. Heat is supplied to the system at $\frac{dQ}{dt} = 100\,\mathrm{W}$ and the system does work at $\frac{dW}{dt} = 75\,\mathrm{J/s}$.
3. $\frac{dU}{dt} = 100 - 75 = 25\,\mathrm{W}$, which is option $4$.

**Subtopic:** Heat, Internal Energy, and Work · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q034_6b20f460_30102026.png?v=6b20f46015aa)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q034_0cc8cd74_30102026.png?v=0cc8cd74e361)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** This is the first law written as a rate. The heat going in, minus the work coming out, is the rise in internal energy.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. They take the 75 J/s as work done on the system instead of by it. That turns the first law into $100 + 75$ and gives 125 W. The question says 'the system performs work'. So that energy leaves, and the internal energy climbs at $100 - 75 = 25\,\mathrm{W}$.
- **Why:** You have to apply the first law with the work going the way the question states. It says 'the system performs work at a rate of $75\,\mathrm{J/s}$'.
<!--/ecat-->

## Q35

Physics · Rotational Motion

A thin wire of length '$L$' and linear mass density '$m$' is bent into a circular ring (in $x$-$y$ plane) with centre '$C$' as shown in figure. The moment of inertia of the ring about an axis $yy'$ will be:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q035_a4cd707e_30102026.png?v=a4cd707e6e20)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q035_question_857658bc_30102026.svg?v=857658bc3508)  
*drawn by code/lib/physics_figure.py*

- (1) $\dfrac{3mL^3}{8\pi}$
- **(2)** $\dfrac{3mL^3}{8\pi^2}$
- (3) $\dfrac{3mL^2}{8\pi}$
- (4) $\dfrac{3mL^2}{8\pi^2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Mass of thin wire $=$ (Linear mass density) $\times$ (Length)
2. $\Rightarrow\ M = mL$
3. $L = 2\pi r$, where $r =$ radius of circular ring $= \frac{L}{2\pi}$
4. Using parallel axis theorem,
5. $I_{yy'} = I_{CM} + Mr^{2} = \frac{Mr^{2}}{2} + Mr^{2} = \frac{3}{2}Mr^{2}$
6. $\Rightarrow\ I_{yy'} = \frac{3}{2} \times (mL) \times \left(\frac{L}{2\pi}\right)^{2} = \frac{3mL^{3}}{8\pi^{2}}$

**Solved independently** (answer withheld)

1. The wire has linear mass density $m$ and length $L$, so the ring's mass is $M = mL$.
2. The circumference fixes the radius: $2\pi R = L$, so $R = \frac{L}{2\pi}$.
3. The figure shows $yy'$ as a line in the $x$-$y$ plane touching the ring at its right-hand point, i.e. a tangent lying in the plane of the ring.
4. About a diameter in its own plane a ring has $I_d = \tfrac{1}{2}MR^2$ (from the perpendicular-axis theorem applied to $I_z = MR^2$).
5. Parallel-axis theorem to the tangent: $I = I_d + MR^2 = \tfrac{1}{2}MR^2 + MR^2 = \tfrac{3}{2}MR^2$.
6. $I = \frac{3}{2}(mL)\left(\frac{L}{2\pi}\right)^2 = \frac{3}{2}\cdot\frac{mL^3}{4\pi^2} = \frac{3mL^3}{8\pi^2}$, which is option $2$.
7. Dimension check: $m$ is a linear density, so $mL^3$ has units $\mathrm{kg\,m^2}$; options 3 and 4 ($mL^2$) are dimensionally wrong.

**Subtopic:** Parallel Axis and Perpendicular Axis Theorem · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 17)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q035_3a671999_30102026.png?v=3a6719998135)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q035_18408eb1_30102026.png?v=18408eb1ccc0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A wire of length $L$ and linear density $m$ becomes a ring of mass $mL$ and radius $L/2\pi$. You have to make both of those swaps before you write the moment of inertia down.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Most students pick option 4. They read the printed $m$ as the ring's mass. That skips the step $M = mL$ and leaves $\frac{3mL^2}{8\pi^2}$. But the question calls $m$ a 'linear mass density'. So the mass carries one more power of $L$ and the answer is $\frac{3mL^3}{8\pi^2}$.
- **Why:** You have to put an expression together from two swaps. The question says 'linear mass density $m$' and 'bent into a circular ring', and the options differ only in the powers of $L$ and $\pi$.
- **Note:** All four options carry the factor $\frac{3}{8}$, which is $\frac{3}{2}MR^2$. So the axis $yy'$ in the figure is a tangent in the plane of the ring. The options are then separated only by how $L$ and $m$ are turned into $R$ and $M$. Option 1 is the matching slip, dropping the square on $2\pi$.
<!--/ecat-->

## Q36

Physics · Current Electricity

A galvanometer of resistance $100\,\Omega$ gives full scale deflection for a current of $1\,\mathrm{mA}$. It is converted into an ammeter of range $0 - 10\,\mathrm{A}$. The shunt required is:

- **(1)** $0.01\,\Omega$
- (2) $0.10\,\Omega$
- (3) $1.0\,\Omega$
- (4) $0.001\,\Omega$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $i_G = 1\ \mathrm{mA} = 0.001\ \mathrm{A}$
2. $i_S = 10 - i_G \simeq 10\ \mathrm{A}$
3. Both shunt resistance and galvanometer are in parallel connection
4. $\therefore\ i_S r_S = i_G R_G$
5. $\Rightarrow\ 10 \times r_s = 0.001 \times 100$
6. $\Rightarrow\ r_s = 0.01\ \Omega$

**Solved independently** (answer withheld)

1. A shunt $S$ carries $I - I_g$ while the galvanometer carries $I_g$, and both have the same voltage across them: $I_g G = (I - I_g)S$.
2. $S = \frac{I_g G}{I - I_g}$.
3. $S = \frac{(1 \times 10^{-3})(100)}{10 - 1 \times 10^{-3}} = \frac{0.1}{9.999} = 0.01\,\Omega$.
4. That is option $1$.

**Subtopic:** Ammeter and Voltmeter in Circuits · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q036_425b3d08_30102026.png?v=425b3d081fae)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q036_06763405_30102026.png?v=06763405f1c9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A shunt carries all the current the coil must not. So you get $S$ from $I_gG = (I - I_g)S$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Most students pick option 2. The first product the data give you is $I_gG = 10^{-3} \times 100 = 0.1$, and $0.10\,\Omega$ is printed as an option. So the work stops there. You still have to divide by the current that must bypass the coil. Dividing by $9.999\,\mathrm{A}$ gives $0.01\,\Omega$.
- **Why:** You have to find the shunt that changes a galvanometer's range. The question says it 'gives full scale deflection for a current of $1\,\mathrm{mA}$' and is 'converted into an ammeter of range $0 - 10\,\mathrm{A}$'.
<!--/ecat-->

## Q37

Physics · Current Electricity

In a metre bridge experiment (see figure), the positions of the cell, $E$, and galvanometer, $G$, are interchanged. We shall observe in the galvanometer:

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q037_326cb92e_30102026.png?v=326cb92eb235)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q037_question_c7546d44_30102026.svg?v=c7546d441a72)  
*drawn by code/lib/physics_figure.py*

- (1) Only the left-sided deflection
- (2) There will be no deflection irrespective of the position of the jockey
- (3) Only the right-sided deflection
- **(4)** Both right-sided and left-sided deflection and at balance point, no deflection

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Position of null point will not change when galvanometer ($G$) and the cell ($E$) are interchanged.
2. There will be no deflection in galvanometer only at balance point.
3. In an unbalanced meter bridge, if $E$ and $G$ are interchanged mutually, then the deflection in galvanometer may be towards left-side or right-side.

**Solved independently** (answer withheld)

1. A metre bridge is a Wheatstone network: $R_1$ and $R_2$ in the gaps, the two parts of the wire as the other arms, with the cell across one diagonal and the galvanometer across the other.
2. Balance means the galvanometer diagonal carries no current, i.e. the two junctions are at equal potential; algebraically $\frac{R_1}{R_2} = \frac{l}{100 - l}$.
3. This condition is symmetric in the two diagonals, so interchanging the cell and the galvanometer leaves the balance point exactly where it was.
4. Therefore the galvanometer still deflects one way on one side of the null point and the other way on the other side, with zero deflection at balance: option $4$.

**Subtopic:** Meter Bridge · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q037_a9147c9c_30102026.png?v=a9147c9cca1f)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q037_b02a36d8_30102026.png?v=b02a36d8bf7c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** The metre bridge balances when $\frac{R_1}{R_2} = \frac{l_1}{l_2}$. That condition does not care which diagonal holds the cell and which holds the galvanometer.
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 2  
  Most students pick option 2. They hold the idea that the galvanometer belongs across the bridge and the cell belongs in the main circuit. So they read the swap as breaking the bridge, and this is the only option that says nothing can be seen. Swapping the two actually leaves the balance condition untouched. The jockey still finds the same null point, with deflections on either side of it.
- **Proposed:** `invariant_change_overread` — the stem announces a change the governing condition is invariant under, and the distractor is what you get by assuming an announced change must show in the observation. condition_missed is for dropping a condition the stem prints, and this student honours the stated swap rather than dropping it; nearby_fact needs a true fact about an adjacent thing, and 'no deflection irrespective of the position of the jockey' describes no metre-bridge arrangement at all.
- **Why:** You have to say what the apparatus does after a stated rewiring. The question says 'the positions of the cell, $E$, and galvanometer, $G$, are interchanged. We shall observe in the galvanometer'.
- **Note:** The figure draws the standard metre bridge the question names. So the swap is fully described in the text.
<!--/ecat-->

## Q38

Physics · Alternating Current

The peak value of an alternating current is $5\,\mathrm{A}$ and frequency is $60\,\mathrm{Hz}$. How long will the current, starting from zero, take to reach the peak value?

- (1) $\dfrac{1}{120}\,\mathrm{s}$
- (2) $\dfrac{1}{60}\,\mathrm{s}$
- (3) $\dfrac{1}{30}\,\mathrm{s}$
- **(4)** $\dfrac{1}{240}\,\mathrm{s}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Alternating current,
2. $i = i_{\text{peak}}\sin(\omega t)$
3. where $\omega = 2\pi f = 2\pi \times 60 = 120\pi\ \mathrm{rad/s}$
4. $\Rightarrow\ i = 5\sin(120\pi t)$
5. $\Rightarrow\ 5 = 5\sin(120\pi t)$
6. $\Rightarrow\ \sin(120\pi t) = 1 = \sin\left(\frac{\pi}{2}\right)$
7. $\therefore\ 120\pi t = \frac{\pi}{2}$
8. $\Rightarrow\ t = \frac{1}{240}\,\mathrm{s}$

**Solved independently** (answer withheld)

1. Take $i = I_0\sin(\omega t)$, which is zero at $t = 0$.
2. The first peak is at $\omega t = \frac{\pi}{2}$, so $t = \frac{\pi}{2\omega}$.
3. With $\omega = 2\pi f$: $t = \frac{\pi}{2(2\pi f)} = \frac{1}{4f}$, i.e. a quarter of the period.
4. $t = \frac{1}{4 \times 60} = \frac{1}{240}\,\mathrm{s}$, which is option $4$.
5. The peak value $5\,\mathrm{A}$ is not needed.

**Subtopic:** Instantaneous Current · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q038_bf648b66_30102026.png?v=bf648b6628d6)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q038_6670a02c_30102026.png?v=6670a02c7ea2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** An alternating current reaches its peak a quarter of a cycle after a zero. So the time asked for is $\frac{T}{4} = \frac{1}{4f}$.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Most students pick option 1. $\frac{1}{120}\,\mathrm{s}$ is a real interval of this current. It is the whole positive hump, from one zero to the next. Read 'starting from zero' to the peak as that whole hump and you land on it. But the peak sits in the middle of the hump, at $\frac{1}{240}\,\mathrm{s}$.
- **Why:** You have to turn a fraction of the period into a time. The question gives 'frequency is $60\,\mathrm{Hz}$' and asks about 'starting from zero, take to reach the peak value'.
- **Note:** The peak value $5\,\mathrm{A}$ is printed but you never use it. Option 2 is the period itself and option 3 is twice the period.
<!--/ecat-->

## Q39

Physics · Magnetic Effect of Electric Current

The figure given below shows a long straight solid wire of circular cross-section of radius '$a$' carrying steady current $I$. The current $I$ is uniformly distributed across its cross-section. The plot which correctly represents the variation of magnetic field ($B$) with distance ($r$) from the axis of the conductor in the region is :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q039_038ef637_30102026.png?v=038ef6370e43)

![drawn: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q039_question_03f54da7_30102026.svg?v=03f54da7c4dd)  
*drawn by code/lib/physics_figure.py*

- **(1)** ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q039_option_1_0f958b44_30102026.png?v=0f958b448559) ![drawn: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q039_option_1_5ebf9c63_30102026.svg?v=5ebf9c630ebe)  
*drawn by code/lib/physics_figure.py* — [graph]
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q039_option_2_6a648777_30102026.png?v=6a648777e4ec) ![drawn: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q039_option_2_3f240d21_30102026.svg?v=3f240d2138ed)  
*drawn by code/lib/physics_figure.py* — [graph]
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q039_option_3_b33ad0d8_30102026.png?v=b33ad0d8ad83) ![drawn: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q039_option_3_8677ddc0_30102026.svg?v=8677ddc0277f)  
*drawn by code/lib/physics_figure.py* — [graph]
- (4) ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q039_option_4_0a17015d_30102026.png?v=0a17015d86d1) ![drawn: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_drawn/2026_11_q039_option_4_32024ef9_30102026.svg?v=32024ef9e887)  
*drawn by code/lib/physics_figure.py* — [graph]

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For a long straight solid wire carrying steady current, which is uniformly distributed across its cross-section, the variation of magnetic field ($B$) with distance ($r$) from axis will be
2. $B = \frac{\mu_0 I r}{2\pi a^{2}}\ \Rightarrow\ B \propto r$, for $r < a$
3. $B = \frac{\mu_0 I}{2\pi r}\ \Rightarrow\ B \propto \frac{1}{r}$, for $r > a$

**Solved independently** (answer withheld)

1. Apply Ampere's law on a circle of radius $r < a$: the enclosed current is $I\frac{\pi r^2}{\pi a^2}$, so $B(2\pi r) = \mu_0 I \frac{r^2}{a^2}$ and $B = \frac{\mu_0 I r}{2\pi a^2}$, a straight line through the origin.
2. At the surface $r = a$ this reaches its maximum $B_{max} = \frac{\mu_0 I}{2\pi a}$.
3. For $r > a$ the whole current is enclosed: $B(2\pi r) = \mu_0 I$, giving $B = \frac{\mu_0 I}{2\pi r}$, a hyperbolic decay.
4. So the correct plot rises linearly from the origin to a sharp peak at $r = a$ and then falls off as $1/r$, approaching zero without reaching it.
5. The only option panel visible in the supplied crop shows exactly this curve and sits in the top-left panel position, i.e. option $1$.

**Subtopic:** Ampere's Circuital Law · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 19)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q039_4ff72661_30102026.png?v=4ff726616e33)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q039_cf5415e5_30102026.png?v=cf5415e50c93)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** In a solid wire carrying current evenly, $B$ grows in proportion to $r$ inside the metal. Outside it falls as $\frac{1}{r}$. So $B$ is largest at the surface.
- **Why:** You have to match a field law that has two parts to a graph. The question says 'The plot which correctly represents the variation of magnetic field ($B$) with distance ($r$) from the axis' and the four options are graphs.
<!--/ecat-->

## Q40

Physics · Semiconductor Electronics

Two statements are given below:

Choose the correct answer from the options given below:

- **(A.)** When the forward bias voltage across a p-n junction diode increases above a certain threshold voltage, the diode current increases significantly.
- **(B.)** This current is called reverse saturation current.

- (1) Both Statements A and B are true
- **(2)** Statement A is true, but Statement B is false
- (3) Both Statements A and B are false
- (4) Statement A is false, but Statement B is true

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $V - I$ characteristics of a forward-biased junction diode
2. When forward bias voltage increases beyond threshold voltage, diode current increases significantly. This is not reverse saturation current.

**Solved independently** (answer withheld)

1. Statement A: beyond the threshold (knee or cut-in) voltage the forward current of a p-n junction diode rises almost exponentially, so A is true.
2. Statement B: the reverse saturation current is the tiny, nearly voltage-independent minority-carrier current that flows under reverse bias, not the large forward current just described, so B is false.
3. A true and B false is option $2$.

**Subtopic:** VI Characteristics of PN Junction Diode · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q040_4a1e6439_30102026.png?v=4a1e6439600c)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q040_921e42ad_30102026.png?v=921e42ad37fb)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The current that climbs steeply past the threshold of a forward-biased diode is the forward current. The reverse saturation current is the small current that flows the other way.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. 'Reverse saturation current' is real diode vocabulary. B also opens with 'This current', so it hangs off A and the two read as one sentence. Once A is accepted, the name in B feels safe too. But that name belongs to the small current under reverse bias. So B is false and A stands.
- **Why:** You have to check a named term against the behaviour it is attached to. Statement A says 'forward bias voltage ... increases above a certain threshold voltage'. Statement B then says 'This current is called reverse saturation current'.
<!--/ecat-->

## Q41

Physics · Electrostatics

Which of the following statements are correct?

Choose the correct answer from the options given below:

- **(A.)** Inside a conductor, the electrostatic field is zero.
- **(B.)** Electric field at the surface of a charged conductor does not depend on its surface charge density.
- **(C.)** The interior of a charged conductor can have no excess charge in the static situation.
- **(D.)** At the surface of a charged conductor, the electrostatic field must be normal to the surface at every point.
- **(E.)** The electrostatic potential is zero everywhere inside a charged conductor.

- (1) A, B and D only
- (2) A, C and E only
- **(3)** A, C and D only
- (4) C, D and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. Electrostatic field is zero inside a conductor.
2. B. Electric field at the surface of a charged conductor $= \frac{\sigma}{\varepsilon_0}\hat{n}$, depends on surface charge density ($\sigma$).
3. C. The interior of a charged conductor cannot have any excess charge in the static situation.
4. D. At the surface of a charged conductor, the electrostatic field $\perp$ surface.
5. E. The electrostatic potential is constant and can be non-zero everywhere inside a charged conductor.

**Solved independently** (answer withheld)

1. A: in electrostatic equilibrium free charges have redistributed until the net field inside the conducting material is zero. True.
2. B: just outside a charged conductor $\vec{E} = \frac{\sigma}{\varepsilon_0}\hat{n}$, which depends directly on the local surface charge density. False.
3. C: by Gauss's law applied to any interior surface, the enclosed charge is zero, so all excess charge resides on the outer surface. True.
4. D: any tangential component would drive surface charge along the surface, contradicting equilibrium, so the field at the surface must be normal at every point. True.
5. E: the conductor is an equipotential, so the potential inside equals the surface potential - a constant, but not zero in general (a charged isolated conductor is at a non-zero potential). False.
6. A, C and D only is option $3$.

**Subtopic:** Conductors in Electrostatics · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 20)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q041_f7b3c2b9_30102026.png?v=f7b3c2b9c003)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q041_a7ce2ecc_30102026.png?v=a7ce2eccc39d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Inside a conductor the field is zero. The potential inside is constant, not zero. At the surface the field is at right angles to the surface and equal to $\sigma/\varepsilon_0$.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. Statement E says about the potential what A correctly says about the field. So once you have accepted A, E looks safe too. But the potential inside a charged conductor is constant and equal to its surface value, which is not zero. So E has to be dropped and D kept.
- **Why:** You have to check five printed claims about conductors one at a time. Statement A says 'Inside a conductor, the electrostatic field is zero'. Statement E says 'The electrostatic potential is zero everywhere inside a charged conductor'.
- **Note:** Statement B is the other false one. The surface field is $\sigma/\varepsilon_0$, so it does depend on the surface charge density.
<!--/ecat-->

## Q42

Physics · Modern Physics

For a metal of work function $6.6\,\mathrm{eV}$, which of the following wavelengths of incident radiation does not give rise to the photoelectric effect?

(Take Planck's constant as $6.6 \times 10^{-34}\,\mathrm{J\,s}$)

- (1) $100\,\mathrm{nm}$
- (2) $150\,\mathrm{nm}$
- **(3)** $200\,\mathrm{nm}$
- (4) $50\,\mathrm{nm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For incident radiation having wavelength ($\lambda$), photoelectric effect doesn't occur when $\frac{hc}{\lambda} <$ work-function
2. $\Rightarrow\ \lambda > \frac{hc}{W_0}$
3. $\Rightarrow\ \lambda > \frac{6.6 \times 10^{-34} \times 3 \times 10^{8}}{6.6 \times 1.6 \times 10^{-19}}$
4. $\Rightarrow\ \lambda > \frac{3 \times 10^{-7}}{1.6}$
5. $\Rightarrow\ \lambda > \frac{300}{1.6}\,\mathrm{nm}$
6. $\Rightarrow\ \lambda = 187.5\ \mathrm{nm}$
7. $\therefore$ Option (3) $200\ \mathrm{nm}$ is correct.

**Solved independently** (answer withheld)

1. Convert the work function: $\phi = 6.6\,\mathrm{eV} = 6.6 \times 1.6 \times 10^{-19} = 1.056 \times 10^{-18}\,\mathrm{J}$.
2. Threshold wavelength: $\lambda_0 = \frac{hc}{\phi} = \frac{(6.6 \times 10^{-34})(3 \times 10^{8})}{1.056 \times 10^{-18}}$.
3. $= \frac{1.98 \times 10^{-25}}{1.056 \times 10^{-18}} = 1.875 \times 10^{-7}\,\mathrm{m} = 187.5\,\mathrm{nm}$.
4. Photoemission occurs only for $\lambda < \lambda_0$; $50$, $100$ and $150\,\mathrm{nm}$ all satisfy this.
5. $200\,\mathrm{nm} > 187.5\,\mathrm{nm}$, so that wavelength gives no photoelectric effect: option $3$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q042_737210fb_30102026.png?v=737210fbab94)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q042_f1ecff8b_30102026.png?v=f1ecff8b843b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Emission needs the photon energy to be above the work function. Since $E = \frac{hc}{\lambda}$, it is the longest wavelength that falls short.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. They read the smallest number on the list as the weakest radiation and pick 50 nm. But energy goes inversely with wavelength. So 50 nm is the most energetic of the four. It is 200 nm, the longest, that sits below the $187.5\,\mathrm{nm}$ threshold.
- **Why:** You have to work out a threshold wavelength and then compare it with the options. The question asks 'which of the following wavelengths of incident radiation does not give rise to the photoelectric effect' and supplies 'Planck's constant as $6.6 \times 10^{-34}\,\mathrm{J\,s}$'.
- **Note:** The question asks which one does not work. So the answer is the single wavelength that fails. Options 1, 2 and 4 all cause emission.
<!--/ecat-->

## Q43

Physics · Ray Optics

In a concave lens, a ray of light emanating from the object parallel to the principal axis of the lens after refraction:

- (1) passes through $2F$, which is the radius of curvature of the lens.
- **(2)** appears to diverge from the first principal focus.
- (3) emerges parallel to the principal axis.
- (4) passes through the second principal focus.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $F_2$ is the second principal focus $\Rightarrow$ It is the virtual image position for object at infinity.
2. $F_1$ is the first principal focus $\Rightarrow$ It is the virtual object position for which image is formed at infinity.
3. The best appropriate answer is option (2), although it should be second principal focus.

**Solved independently** (answer withheld)

1. A concave lens is a diverging lens, so an incident ray parallel to the principal axis bends away from the axis after refraction.
2. The emergent ray therefore never crosses the axis; extended backwards, it meets the axis at the focus on the same side as the incoming light, so it only appears to diverge from that focus.
3. Option 3 (emerges parallel) describes no refraction at all, and option 1 invokes a non-existent 2F rule for lenses, so both are out.
4. Option 4 says the ray 'passes through' a focus, which a diverging lens ray never does - the focus is virtual.
5. Option 2, 'appears to diverge from the principal focus', is the only statement matching the actual behaviour.

**Subtopic:** Lens Formula · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q043_17d1c64f_30102026.png?v=17d1c64f8e7a)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q043_83dc8c45_30102026.png?v=83dc8c4580e0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A diverging lens never brings a ray to a point. A ray parallel to the axis leaves the lens only seeming to come from a focus on the side the light came in.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Most students pick option 4. 'Passes through the second principal focus' is the convex-lens rule word for word. So carrying the converging-lens ray diagram across lands you on it. A concave lens spreads the ray out instead. The refracted ray only appears to come from a focus.
- **Why:** You have to recall the construction rule for a diverging lens. The question says 'In a concave lens, a ray of light emanating from the object parallel to the principal axis of the lens after refraction' and the four options are four statements to choose between.
- **Note:** Only option 2 gets the behaviour right, because 'appears to diverge' is the only wording a concave lens allows. Which number that focus carries is just a naming convention. In the convention many books use, the focus that parallel rays define is called the second principal focus, and this option calls it the first.
<!--/ecat-->

## Q44

Physics · Mechanical Properties of Fluids

A submarine is designed to withstand an absolute pressure of $100\,\mathrm{atm}$. How deep can it go below the water surface?

(Consider the density of water $= 1000\,\mathrm{kg\,m^{-3}}$, $1\,\mathrm{atm} = 1 \times 10^5\,\mathrm{Pa}$ and gravitational acceleration $g = 10\,\mathrm{m/s^2}$)

- **(1)** $990\,\mathrm{m}$
- (2) $9900\,\mathrm{m}$
- (3) $99\,\mathrm{m}$
- (4) $9000\,\mathrm{m}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $P = P_0 + \rho g h$
2. $\Rightarrow\ 100 \times 10^{5} = 10^{5} + 10^{3} \times 10 \times h$
3. $\Rightarrow\ 10^{7} = 10^{5} + 10^{4}h$
4. $\Rightarrow\ 10^{3} = 10 + h$
5. $\Rightarrow\ h = 1000 - 10 = 990\ \mathrm{m}$

**Solved independently** (answer withheld)

1. Absolute pressure at depth $h$ is $P = P_{atm} + \rho g h$.
2. $100 \times 10^{5} = 1 \times 10^{5} + (1000)(10)h$.
3. $\rho g h = 99 \times 10^{5}\,\mathrm{Pa}$, and $\rho g = 1000 \times 10 = 10^{4}\,\mathrm{Pa/m}$.
4. $h = \frac{99 \times 10^{5}}{10^{4}} = 990\,\mathrm{m}$, which is option $1$.

**Subtopic:** Atmospheric and Gauge Pressure · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q044_6732e7e6_30102026.png?v=6732e7e623c8)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q044_753c513e_30102026.png?v=753c513e9941)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The absolute pressure at a depth is the atmosphere plus $\rho g h$. So you have to take the surface atmosphere off the hull's rating before you find the depth.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Most students pick option 2. They leave $g$ out of $\rho g h$. That divides the $9.9 \times 10^6\,\mathrm{Pa}$ by 1000 instead of by $10^4$ and gives 9900 m. With $g = 10\,\mathrm{m/s^2}$ the water column you need is 990 m.
- **Why:** You have to find a depth from a pressure rating. The question says the hull must 'withstand an absolute pressure of $100\,\mathrm{atm}$' and supplies '$1\,\mathrm{atm} = 1 \times 10^5\,\mathrm{Pa}$'.
- **Note:** The word 'absolute' is what makes the answer 990 m rather than 1000 m. One atmosphere is already there at the surface, so it comes off the $10^7\,\mathrm{Pa}$ first.
<!--/ecat-->

## Q45

Physics · Electromagnetic Waves

Match List I with List II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Microwave | I. | Electrons in atoms emit light when they move from a higher energy level to a lower energy level |
| B. | Visible light | II. | Radioactive decay of nucleus |
| C. | Gamma rays | III. | Vibration of atoms and molecules |
| D. | Infra-red rays | IV. | Klystron valve or magnetron valve |

- (1) A–III, B–I, C–II, D–IV
- (2) A–III, B–IV, C–I, D–II
- **(3)** A–IV, B–I, C–II, D–III
- (4) A–IV, B–III, C–II, D–I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A-IV) Microwave — Klystron valve or magnetron valve
2. (B-I) Visible light — Electrons in atoms emit light when they move from a higher energy level to a lower energy level
3. (C-II) Gamma rays — Radioactive decay of nucleus
4. (D-III) Infra-red rays — Vibration of atoms and molecules

**Solved independently** (answer withheld)

1. Microwaves are generated by special vacuum tubes, the klystron and the magnetron, so A-IV.
2. Visible light is emitted when atomic electrons drop from a higher to a lower energy level, so B-I.
3. Gamma rays originate in the nucleus, emitted during radioactive decay, so C-II.
4. Infra-red radiation is produced by the vibration of atoms and molecules (heat radiation), so D-III.
5. A-IV, B-I, C-II, D-III is option $3$.

**Subtopic:** Electromagnetic Spectrum · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 22)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q045_b4038456_30102026.png?v=b40384565597)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q045_429619ed_30102026.png?v=429619ed52a4)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** You have to pair each part of the electromagnetic spectrum with the process that gives it out. Valves make microwaves. Electron transitions make visible light. Nuclear decay makes gamma rays. Vibrating molecules make infra-red.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. A microwave oven heats food by shaking water molecules about. So 'Vibration of atoms and molecules' looks like the microwave entry. That pairs A with III and leaves the klystron valve for infra-red. But the klystron valve and the magnetron valve are what make microwaves. Vibrating molecules give out infra-red.
- **Why:** The question asks you to pair each part of the spectrum with its source. List I prints 'Microwave' and 'Infra-red rays'. List II prints 'Klystron valve or magnetron valve' and 'Vibration of atoms and molecules'.
- **Note:** Option 1 keeps B with I and C with II, the same as the correct code. It swaps only the microwave and infra-red pair. So the question comes down to that single pairing. asks re-pointed from compare: stored facts: which process emits each part of the spectrum. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q46

Chemistry · organic · Amines

Select the reagents that reduce nitriles to primary amines.

Choose the correct answer from the options given below.

- **(A.)** (i) $\mathrm{LiAlH_4}$; (ii) $\mathrm{H_2O}$
- **(B.)** $\mathrm{Sn} + \mathrm{HCl}$
- **(C.)** $\mathrm{H_2/Ni}$
- **(D.)** $\mathrm{Na(Hg)/C_2H_5OH}$
- **(E.)** $\mathrm{Br_2}$/aq. $\mathrm{NaOH}$

- (1) B, D and E only
- **(2)** A, C and D only
- (3) A, D and E only
- (4) A, B and C only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{R-CN} \xrightarrow{\mathrm{Na(Hg)/C_2H_5OH}} \mathrm{R-CH_2-NH_2}$
2. $\mathrm{R-CN} \xrightarrow[\mathrm{(ii)\ H_2O}]{\mathrm{(i)\ LiAlH_4}} \mathrm{R-CH_2-NH_2}$
3. $\mathrm{R-CN} \xrightarrow{\mathrm{Sn+HCl}} \mathrm{R-CHO}$
4. $\mathrm{R-CN} \xrightarrow{\mathrm{H_2/Ni}} \mathrm{R-CH_2-NH_2}$

**Solved independently** (answer withheld)

1. A: $\mathrm{R\text{-}C\equiv N} \xrightarrow{(i)\,LiAlH_4,\ (ii)\,H_2O} \mathrm{R\text{-}CH_2\text{-}NH_2}$. Correct.
2. C: catalytic hydrogenation $\mathrm{R\text{-}C\equiv N} \xrightarrow{H_2/Ni} \mathrm{R\text{-}CH_2\text{-}NH_2}$. Correct.
3. D: sodium amalgam in ethanol is the Mendius reduction, which also delivers the primary amine. Correct.
4. B: $\mathrm{Sn + HCl}$ is the standard reductant for converting nitro compounds to amines, not nitriles.
5. E: $\mathrm{Br_2}$/aq. $\mathrm{NaOH}$ is the Hofmann bromamide degradation, which acts on amides and shortens the chain by one carbon.
6. A, C and D only is option $2$.

**Subtopic:** Methods of Preparation of Amines · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 23)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q046_7bdb4867_30102026.png?v=7bdb4867654f)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q046_35a86dbe_30102026.png?v=35a86dbef8d4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A nitrile goes to a primary amine with hydride, with catalytic hydrogen, or with sodium amalgam in alcohol. Tin and acid, and bromine in alkali, also make primary amines, but from other starting materials.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Most students pick option 4. A and C are both in it and both belong. So the two correct members make the third one look correct too. $\mathrm{Sn} + \mathrm{HCl}$ is the reduction a student files under 'makes a primary amine'. But its starting material is a nitro compound, not a nitrile. To buy it, option 4 has to drop D, and D is the sodium amalgam reduction that does work on nitriles.
- **Why:** You have to judge each listed reagent and say whether it carries out one named conversion. The question says 'Select the reagents that reduce nitriles to primary amines' above a lettered list of five reagent sets.
<!--/ecat-->

## Q47

Chemistry · physical · Surface Chemistry

Match List I with List II :

Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A. | $\mathrm{V_2O_5}$ | I. | Preparation of ammonia from $\mathrm{N_2/H_2}$ mixture |
| B. | $\mathrm{Fe}$ | II. | Polymerisation of alkynes |
| C. | $\mathrm{PdCl_2}$ | III. | Preparation of $\mathrm{H_2SO_4}$ and $\mathrm{SO_2}$ |
| D. | Ni complex | IV. | Oxidation of ethyne to ethanal |

- (1) A-III, B-IV, C-I, D-II
- (2) A-IV, B-I, C-III, D-II
- (3) A-II, B-I, C-IV, D-III
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (A) $\mathrm{V_2O_5} \to$ Catalyses the oxidation of $\mathrm{SO_2}$ into $\mathrm{SO_3}$ in the manufacture of $\mathrm{H_2SO_4}$. (III)
2. (B) $\mathrm{Fe} \to$ Act as catalysts in preparation of ammonia from $\mathrm{N_2/H_2}$ mixture. (I)
3. (C) $\mathrm{PdCl_2} \to$ Oxidation of ethyne to ethanal. (IV)
4. (D) Ni complex $\to$ Polymerisation of alkynes. (II)
5. A $\to$ III, B $\to$ I, C $\to$ IV, D $\to$ II

**Solved independently** (answer withheld)

1. $\mathrm{V_2O_5}$ catalyses $2\mathrm{SO_2} + \mathrm{O_2} \rightarrow 2\mathrm{SO_3}$ in the contact process for sulphuric acid, so A-III.
2. Finely divided $\mathrm{Fe}$ is the Haber-process catalyst for $\mathrm{N_2} + 3\mathrm{H_2} \rightarrow 2\mathrm{NH_3}$, so B-I.
3. $\mathrm{PdCl_2}$ is the Wacker-process catalyst for the oxidation of ethyne to ethanal, so C-IV.
4. Nickel complexes are used in the polymerisation of alkynes, so D-II.
5. A-III, B-I, C-IV, D-II is option $4$.

**Subtopic:** — · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 23)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q047_cbc2db7f_30102026.png?v=cbc2db7f0d23)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q047_b0879f07_30102026.png?v=b0879f072014)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** You have to know which industrial process each catalyst serves. $\mathrm{V_2O_5}$ is used in the contact process. Iron is used in Haber's synthesis. $\mathrm{PdCl_2}$ oxidises ethyne to ethanal. Nickel complexes polymerise alkynes.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. $\mathrm{V_2O_5}$ is filed in memory as 'the oxidation catalyst'. Entry IV is the only one in List II with the word oxidation in it. So the keyword pushes you to pair A with IV. But what $\mathrm{V_2O_5}$ oxidises is $\mathrm{SO_2}$ to $\mathrm{SO_3}$, which is entry III. The ethyne to ethanal oxidation belongs to $\mathrm{PdCl_2}$. Once A takes IV, C is pushed onto III, and that is what option 2 prints.
- **Why:** You have to pair four named catalysts with the processes they serve. The question says 'Match List I with List II' and sets '$\mathrm{V_2O_5}$', 'Fe', '$\mathrm{PdCl_2}$' and 'Ni complex' against four preparations.
- **Note:** asks re-pointed from compare: four stored facts: which process each catalyst serves. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q48

Chemistry · physical · Thermodynamics

Consider the following reaction :

$2\mathrm{A(g)} + \mathrm{B(g)} \rightarrow 2\mathrm{D(g)}$

$\Delta U^{\ominus} = -10\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S^{\ominus} = -44\,\mathrm{JK^{-1}}$ at $298\,\mathrm{K}$.

Identify the correct option with $\Delta G^{\ominus}$ for the reaction and spontaneity of the reaction at $298\,\mathrm{K}$.

(Given : $R = 8.31\,\mathrm{J\,mol^{-1}\,K^{-1}}$)

- (1) $-1.635\,\mathrm{kJ\,mol^{-1}}$, spontaneous
- (2) $-0.63568\,\mathrm{kJ\,mol^{-1}}$, spontaneous
- **(3)** $+0.63568\,\mathrm{kJ\,mol^{-1}}$, non-spontaneous
- (4) $+1.635\,\mathrm{kJ\,mol^{-1}}$, non-spontaneous

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $2\mathrm{A(g)} + \mathrm{B(g)} \to 2\mathrm{D(g)}$
2. $\Delta \mathrm{U}^\circ = -10\ \mathrm{kJ/mol}$
3. $\Delta \mathrm{S}^\circ = -44\ \mathrm{J/K}$
4. $\Delta \mathrm{H}^\circ = \Delta \mathrm{U}^\circ + \Delta n_g \mathrm{RT}$
5. $\Delta \mathrm{H}^\circ = -10 - \frac{1 \times 298 \times (8.31)}{1000} = -10 - 2.48 = -12.48\ \mathrm{kJ/mol}$
6. $\Delta \mathrm{G}^\circ = \Delta \mathrm{H}^\circ - \mathrm{T}\Delta \mathrm{S}^\circ$
7. $= -12.48 - \frac{298 \times (-44)}{1000}$
8. $= -12.48 + 13.112$
9. $= +0.632\ \mathrm{kJ/mol}$
10. Since $\Delta \mathrm{G}^\circ$ comes out to be positive, so given process is non-spontaneous.

**Solved independently** (answer withheld)

1. Change in moles of gas: $\Delta n_g = 2 - (2 + 1) = -1$.
2. $\Delta H^{\ominus} = \Delta U^{\ominus} + \Delta n_g RT = -10000 + (-1)(8.31)(298)$.
3. $(8.31)(298) = 2476.4\,\mathrm{J}$, so $\Delta H^{\ominus} = -10000 - 2476.4 = -12476.4\,\mathrm{J\,mol^{-1}}$.
4. $T\Delta S^{\ominus} = 298 \times (-44) = -13112\,\mathrm{J}$.
5. $\Delta G^{\ominus} = \Delta H^{\ominus} - T\Delta S^{\ominus} = -12476.4 + 13112 = +635.6\,\mathrm{J\,mol^{-1}} = +0.636\,\mathrm{kJ\,mol^{-1}}$.
6. $\Delta G^{\ominus} > 0$, so the reaction is non-spontaneous: option $3$.

**Subtopic:** Gibbs Energy and Spontaneity · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 24)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q048_1e5e9b0f_30102026.png?v=1e5e9b0f94d1)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q048_d3c380a4_30102026.png?v=d3c380a482a4)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The change in the number of gas moles turns $\Delta U$ into $\Delta H$. Then the sign of $\Delta G = \Delta H - T\Delta S$ tells you whether the reaction is spontaneous.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Most students pick option 2. They write the Gibbs equation the other way round, as $T\Delta S^{\ominus} - \Delta H^{\ominus}$. That gives $-13.112 - (-12.476) = -0.636\,\mathrm{kJ\,mol^{-1}}$. The size matches the correct answer but the sign is flipped. The flipped sign then pulls the second half of the option round to 'spontaneous'. So the pair agrees with itself and looks safe.
- **Why:** You have to add $\Delta n_g RT$ to $\Delta U^{\ominus}$, then put the result through $\Delta G^{\ominus} = \Delta H^{\ominus} - T\Delta S^{\ominus}$. The question prints '$\Delta U^{\ominus} = -10\,\mathrm{kJ\,mol^{-1}}$', supplies $R$, and asks for '$\Delta G^{\ominus}$ for the reaction and spontaneity'.
<!--/ecat-->

## Q49

Chemistry · physical · Structure of Atom

Match List I with List II :

Choose the correct answer from the options given below.

| List-I | | List-II | |
|---|---|---|---|
| A. | '$n$' $= 2$, '$l$' $= 1$ | I. | $3d$ |
| B. | '$n$' $= 4$, '$l$' $= 0$ | II. | $2p$ |
| C. | '$n$' $= 5$, '$l$' $= 3$ | III. | $4s$ |
| D. | '$n$' $= 3$, '$l$' $= 2$ | IV. | $5f$ |

- (1) A-IV, B-II, C-III, D-I
- (2) A-II, B-III, C-I, D-IV
- **(3)** A-II, B-III, C-IV, D-I
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. A. $n = 2$, $l = 1$ — $2p$
2. B. $n = 4$, $l = 0$ — $4s$
3. C. $n = 5$, $l = 3$ — $5f$
4. D. $n = 3$, $l = 2$ — $3d$
5. $l$ represents the subshell, for which the values are as following :
6. $l = 0$ — $s$
7. $l = 1$ — $p$
8. $l = 2$ — $d$
9. $l = 3$ — $f$

**Solved independently** (answer withheld)

1. The azimuthal quantum number maps to a letter as $l=0\to s$, $l=1\to p$, $l=2\to d$, $l=3\to f$.
2. A: $n=2,\ l=1$ is the $2p$ subshell, so A-II.
3. B: $n=4,\ l=0$ is the $4s$ subshell, so B-III.
4. C: $n=5,\ l=3$ is the $5f$ subshell, so C-IV.
5. D: $n=3,\ l=2$ is the $3d$ subshell, so D-I.
6. A-II, B-III, C-IV, D-I is option $3$.

**Subtopic:** Quantum Numbers · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q049_d8ae0588_30102026.png?v=d8ae0588b94e)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q049_321423e1_30102026.png?v=321423e19a70)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** You need the letter code for the azimuthal quantum number. 0 is s, 1 is p, 2 is d, 3 is f. You read that together with n to name the orbital.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. A student can hold the code safely up to $l = 1$ and still swap the last two letters, taking $l = 2$ for f and $l = 3$ for d. That wants 5d for C and 3f for D. Neither of those is printed. So the letter decides: C goes to 3d and D goes to 5f. That is exactly option 2, with the two easy rows A-II and B-III left standing.
- **Why:** You have to turn a pair of quantum numbers into an orbital label for each row. List I prints "'$n$' $= 5$, '$l$' $= 3$" and List II holds $3d$, $2p$, $4s$ and $5f$.
- **Note:** asks re-pointed from compare: a stored code: 0 is s, 1 is p, 2 is d, 3 is f. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q50

Chemistry · physical · Ionic Equilibrium

In a qualitative analysis, $\mathrm{Bi^{3+}}$ is detected by appearance of precipitate of $\mathrm{BiO(OH)(s)}$. Calculate pH when the following equilibrium exists at $298\,\mathrm{K}$.

$\mathrm{BiO(OH)(s)} \rightleftharpoons \mathrm{BiO^{+}(aq)} + \mathrm{OH^{-}(aq)}$, $K = 4 \times 10^{-10}$

(Given : $\log 2 = 0.3010$)

- (1) $8.714$
- (2) $4.699$
- (3) $5.286$
- **(4)** $9.301$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{BiO(OH)(s)} \rightleftharpoons \underset{s}{\mathrm{BiO^{+}(aq)}} + \underset{s}{\mathrm{OH^{-}(aq)}}$
2. $\mathrm{K} = \frac{[\mathrm{BiO^{+}}][\mathrm{OH^{-}}]}{[\mathrm{BiO(OH)(s)}]}$
3. $\mathrm{K} = \frac{[\mathrm{BiO^{+}}][\mathrm{OH^{-}}]}{1}$
4. $\mathrm{K} = s \times s = s^{2}$
5. $s = \sqrt{\mathrm{K}} = \sqrt{4 \times 10^{-10}} = 2 \times 10^{-5}\ \mathrm{M}$
6. $[\mathrm{H^{+}}] = \frac{\mathrm{K_w}}{[\mathrm{OH^{-}}]} = \frac{1}{2} \times 10^{-9}$, $\mathrm{pH} = -\log[\mathrm{H^{+}}] = 9 + \log 2 = 9.301$

**Solved independently** (answer withheld)

1. The solid dissolves 1:1, so $[\mathrm{BiO^{+}}] = [\mathrm{OH^{-}}] = s$ and $K = s^2$.
2. $s = \sqrt{4 \times 10^{-10}} = 2 \times 10^{-5}\,\mathrm{M}$, so $[\mathrm{OH^{-}}] = 2 \times 10^{-5}\,\mathrm{M}$.
3. $\mathrm{pOH} = -\log(2 \times 10^{-5}) = 5 - \log 2 = 5 - 0.3010 = 4.699$.
4. $\mathrm{pH} = 14 - \mathrm{pOH} = 14 - 4.699 = 9.301$, which is option $4$.

**Subtopic:** Solubility Product Constant, pH Scale · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q050_5dc06a47_30102026.png?v=5dc06a47dcb9)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q050_a869a098_30102026.png?v=a869a09883d8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a 1:1 sparingly soluble solid, $K = s^2$ gives you $[\mathrm{OH^-}]$. Then pH follows from $\mathrm{pH} + \mathrm{pOH} = 14$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Most students pick option 2. $s = \sqrt{4\times10^{-10}} = 2\times10^{-5}$, so $\mathrm{pOH} = 5 - 0.301 = 4.699$. That number is printed as option 2. Find the hydroxide concentration, take its negative log, and you have the right number in your hand. But you have stopped one step early. You still need $14 - 4.699 = 9.301$.
- **Why:** You have to get the hydroxide concentration from the equilibrium constant printed, then turn it into pH. The question gives '$K = 4 \times 10^{-10}$' and '$\log 2 = 0.3010$' and says 'Calculate pH'.
<!--/ecat-->

## Q51

Chemistry · organic · Biomolecules

The correct statement with regard to the secondary structure of DNA/RNA is

- (1) RNA possesses a single strand helix structure and contains thymine as one of the four bases
- **(2)** DNA possesses a double strand helix structure and contains thymine as one of the four bases
- (3) RNA possesses a double strand helix structure and contains uracil as one of the four bases
- (4) DNA possesses a single strand helix structure and contains uracil as one of the four bases

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. RNA is typically single standard but it contains uracil, not thymine.
2. DNA is secondary structure has a double strand helix consisting of two polynucleotide chains. Its four nitrogenous bases are adenine (A), guanine (G), cytosine (C) and thymine (T).

**Solved independently** (answer withheld)

1. The secondary structure of DNA is the Watson-Crick double helix of two complementary strands; RNA is normally a single strand.
2. DNA's four bases are adenine, guanine, cytosine and thymine, while RNA replaces thymine with uracil.
3. Only the statement 'DNA possesses a double strand helix structure and contains thymine' fits both facts, which is option $2$.

**Subtopic:** Structure and Function of Nucleic Acids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q051_f304eb37_30102026.png?v=f304eb37064c)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q051_c5069d00_30102026.png?v=c5069d00d6e2)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** DNA is a double helix and it is built on thymine. RNA has a single strand and it carries uracil in thymine's place.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Most students pick option 1. 'RNA possesses a single strand helix structure' is the fact students hold most firmly about RNA. Because that half is right, the rest of the sentence looks right too. But the second half swaps the base. RNA's fourth base is uracil, not thymine.
- **Also:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Some students pick option 3. Here the base half is the true one, because uracil does belong to RNA. So a student looking for the word 'uracil' settles on it. The strand half is where it fails. RNA is single-stranded, and the double helix belongs to DNA.
- **Why:** You have to know two facts about each nucleic acid: how many strands it has, and what its fourth base is. The question says 'The correct statement with regard to the secondary structure of DNA/RNA is' and each option joins a strand claim to a base claim.
<!--/ecat-->

## Q52

Chemistry · organic · Isomerism in Organic Compounds

The pair of molecules that are metamers among the following is :

- (1) $\mathrm{CH_3CH_2CH_2OH}$ and $\mathrm{CH_3 - CH(OH) - CH_3}$
- (2) $\mathrm{CH_3CH_2CH_2CH_2CH_3}$ and $\mathrm{(CH_3)_2CHCH_2CH_3}$
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q052_option_3_4d817311_30102026.png?v=4d817311c2fb) — and
- **(4)** $\mathrm{CH_3OCH_2CH_2CH_3}$ and $\mathrm{CH_3CH_2OCH_2CH_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Metamerism arises due to different alkyl chains on either side of the functional group in the molecule pair of molecules $\mathrm{CH_3OCH_2CH_2CH_3}$ and $\mathrm{CH_3CH_2OCH_2CH_3}$ are metamers of each other.

**Solved independently** (answer withheld)

1. Metamers have the same molecular formula and the same functional group, but different alkyl groups attached on either side of that group.
2. Option 1 is propan-1-ol and propan-2-ol, the $\mathrm{-OH}$ sitting at different carbons, so these are position isomers.
3. Option 2 is pentane and 2-methylbutane, differing in carbon skeleton, so these are chain isomers.
4. Option 3 shows propanone and propanal (both $\mathrm{C_3H_6O}$), a ketone against an aldehyde, so these are functional isomers.
5. Option 4 is $\mathrm{CH_3-O-CH_2CH_2CH_3}$ and $\mathrm{CH_3CH_2-O-CH_2CH_3}$, both $\mathrm{C_4H_{10}O}$ ethers but with methyl/propyl against ethyl/ethyl, which is exactly metamerism.
6. The metamer pair is option $4$.

**Subtopic:** Tautomer and Metamer Isomerism · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q052_251a452f_30102026.png?v=251a452f17ab)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q052_f3d44762_30102026.png?v=f3d447627a57)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Metamers have the same formula and the same functional group. They differ only in how the carbons are split on either side of that group.
- **Why:** You have to apply the definition of metamerism to four printed pairs. The question says 'The pair of molecules that are metamers among the following is' and each option prints two structures to be judged together.
- **Note:** Option 3's two members are not in the stored text. So the four options cannot be read as a whole and no trap is named. Of the options that can be read, 1 is a pair of propanols that are position isomers, 2 is a pair of pentanes that are chain isomers, and 4 is a pair of ethers.
<!--/ecat-->

## Q53

Chemistry · inorganic · Coordination Compounds – Practice

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | $\mathrm{[Pt(NH_3)_2Cl_2]}$ | I. | Optical |
| B. | $\mathrm{[Co(en)_3]^{3+}}$ | II. | Solvate |
| C. | $\mathrm{[Co(NH_3)_5NO_2]Cl_2}$ | III. | Geometrical |
| D. | $\mathrm{[Cr(H_2O)_6]Cl_3}$ | IV. | Linkage |

- (1) A-III, B-I, C-II, D-IV
- (2) A-I, B-III, C-II, D-IV
- (3) A-II, B-IV, C-III, D-I
- **(4)** A-III, B-I, C-IV, D-II

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. $\Rightarrow$ Geometrical isomers
2. B. $\Rightarrow$ Optical isomers
3. C. $\mathrm{[Co(NH_3)_5NO_2]Cl_2}$ and $\mathrm{[Co(NH_3)_5(ONO)]Cl_2}$ are linkage isomers
4. D. $\mathrm{[Cr(H_2O)_6]Cl_3}$ and $\mathrm{[Cr(H_2O)_5Cl]Cl_2{\cdot}H_2O}$ are solvate isomers

**Solved independently** (answer withheld)

1. A: $\mathrm{[Pt(NH_3)_2Cl_2]}$ is square planar $\mathrm{MA_2B_2}$, which exists as cis and trans forms, so A-III (geometrical).
2. B: $\mathrm{[Co(en)_3]^{3+}}$ is a tris-chelate with no plane of symmetry, giving non-superimposable mirror images, so B-I (optical).
3. C: in $\mathrm{[Co(NH_3)_5NO_2]Cl_2}$ the ambidentate $\mathrm{NO_2}$ can coordinate through nitrogen (nitro) or oxygen (nitrito), so C-IV (linkage).
4. D: $\mathrm{[Cr(H_2O)_6]Cl_3}$ differs from $\mathrm{[Cr(H_2O)_5Cl]Cl_2\cdot H_2O}$ in how many water molecules are inside the coordination sphere, so D-II (solvate).
5. A-III, B-I, C-IV, D-II is option $4$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 26)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q053_dd221ec5_30102026.png?v=dd221ec5c205)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q053_a4b81e28_30102026.png?v=a4b81e28606f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** You have to say which kind of isomerism each complex can show. $\mathrm{MA_2B_2}$ shows cis-trans. A tris-chelate shows optical isomerism. An ambidentate $\mathrm{NO_2}$ gives linkage isomerism. Water sitting both inside and outside the sphere gives solvate isomerism.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. Solvate isomerism is remembered as 'something sits outside the coordination sphere'. Entry C is the one written with its two chlorides outside. So that reading sends C to II. But solvate isomerism needs the solvent itself to move in and out of the sphere. Only the aqua complex D can do that. Linkage then falls to D in option 1, even though D has no ambidentate ligand to link through.
- **Why:** You have to pair four complexes with the kind of isomerism each can show. List I prints '$\mathrm{[Co(NH_3)_5NO_2]Cl_2}$' and '$\mathrm{[Cr(H_2O)_6]Cl_3}$'. List II holds 'Optical', 'Solvate', 'Geometrical' and 'Linkage'.
- **Note:** asks re-pointed from compare: the isomerism rules applied to each printed formula. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q54

Chemistry · physical · Chemical Kinetics

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Zero order | I. | $\mathrm{mol^{-1}\,L\,s^{-1}}$ |
| B. | First order | II. | $\mathrm{mol^{-2}\,L^{2}\,s^{-1}}$ |
| C. | Second order | III. | $\mathrm{s^{-1}}$ |
| D. | Third order | IV. | $\mathrm{mol\,L^{-1}\,s^{-1}}$ |

- (1) A-IV, B-II, C-I, D-III
- **(2)** A-IV, B-III, C-I, D-II
- (3) A-IV, B-III, C-II, D-I
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Unit for rate constant of $\mathrm{n^{th}}$ order reaction $= \left(\frac{\mathrm{mol}}{\mathrm{L}}\right)^{1-n}\mathrm{s^{-1}}$
2. For zero order reaction $\Rightarrow$ n $= 0$; unit $\Rightarrow \mathrm{mol\ L^{-1}\ s^{-1}}$
3. For first order reaction $\Rightarrow$ n $= 1$; unit $\Rightarrow \mathrm{s^{-1}}$
4. For second order reaction $\Rightarrow$ n $= 2$; unit $\Rightarrow \mathrm{mol^{-1}\ L\ s^{-1}}$
5. For third order reaction $\Rightarrow$ n $= 2$; unit $\Rightarrow \mathrm{mol^{-2}\ L^{2}\ s^{-1}}$

**Solved independently** (answer withheld)

1. For an $n$th order reaction $\mathrm{rate} = k[A]^n$, so $k$ has units $(\mathrm{mol\,L^{-1}})^{1-n}\,\mathrm{s^{-1}}$.
2. A: $n=0$ gives $\mathrm{mol\,L^{-1}\,s^{-1}}$, so A-IV.
3. B: $n=1$ gives $\mathrm{s^{-1}}$, so B-III.
4. C: $n=2$ gives $\mathrm{mol^{-1}\,L\,s^{-1}}$, so C-I.
5. D: $n=3$ gives $\mathrm{mol^{-2}\,L^{2}\,s^{-1}}$, so D-II.
6. A-IV, B-III, C-I, D-II is option $2$.

**Subtopic:** Rate Constant · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 27)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q054_4d720f0a_30102026.png?v=4d720f0aba8d)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q054_2b36c274_30102026.png?v=2b36c2749772)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The units of a rate constant come from rate $= k[\mathrm{A}]^n$. That gives $\mathrm{mol^{1-n}\,L^{n-1}\,s^{-1}}$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Most students pick option 3. They take the power of concentration to be the order itself instead of one less than the order. Second order then comes out as $\mathrm{mol^{-2}\,L^{2}\,s^{-1}}$ and third order as $\mathrm{mol^{-1}\,L\,s^{-1}}$. That is the C-II and D-I of option 3, with the zero-order and first-order rows left alone. Second order needs only one power of $\mathrm{mol^{-1}L}$. That is because $k = \mathrm{rate}/[\mathrm{A}]^2$ takes away two concentrations and the rate puts one back.
- **Why:** You have to work out the units of $k$ for each order and pair them up. List I prints 'Zero order' through to 'Third order'. List II holds four unit combinations.
- **Note:** asks re-pointed from compare: the units derived from rate = k[A]^n for each order. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q55

Chemistry · organic · IUPAC Nomenclature of Organic Chemistry

The correct IUPAC name of the following compound is :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q055_7c0fa346_30102026.png?v=7c0fa34674d0)

- **(1)** 3-ethyl-5-methylheptane
- (2) 2,4-diethylhexane
- (3) 3-methyl-5-ethylheptane
- (4) 3,5-diethylhexane

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. IUPAC name : 3-ethyl-5-methylheptane
2. Numbering of parent chain should follow lowest locant rule.
3. Prefixes should be written in alphabetical order.

**Solved independently** (answer withheld)

1. Pick the longest continuous carbon chain; for this skeleton it runs through seven carbons, so the parent is heptane and names based on hexane (options 2 and 4) are wrong.
2. The two branches on that heptane chain are one ethyl and one methyl, so 'diethyl' names are wrong.
3. Numbering from either end gives the locant set $\{3,5\}$, a tie, so the rule is to give the lowest locant to the substituent cited first alphabetically.
4. Alphabetically ethyl precedes methyl, so ethyl takes $3$ and methyl takes $5$, and the substituents are cited in that same alphabetical order.
5. That gives 3-ethyl-5-methylheptane, option $1$; option 3 is the same skeleton written with the locants and alphabetical order both wrong.

**Subtopic:** Acyclic or Open Chain Compounds · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 27)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q055_60837c53_30102026.png?v=60837c538f5c)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q055_69acc1b7_30102026.png?v=69acc1b7b78e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** You name a branched alkane by the IUPAC rules. Take the longest chain as the parent. Number it so the locants come out as low as possible. Cite the substituents in alphabetical order.
- **Why:** You have to apply the IUPAC rules for choosing the parent chain and citing substituents to a drawn skeleton. The question says 'The correct IUPAC name of the following compound is :' and then prints a structure rather than a formula.
- **Note:** The structure itself is not in the stored text. Only the four names are. So which name belongs to this compound cannot be settled here, and no trap is named.
<!--/ecat-->

## Q56

Chemistry · physical · Structure of Atom

A bulb is rated at $150$ watt, converting $8\%$ energy into light. If energy of one photon is $4.42 \times 10^{-19}\,\mathrm{J}$, how many photons are emitted by the bulb per second?

- **(1)** $2.71 \times 10^{19}$
- (2) $4.06 \times 10^{19}$
- (3) $27.2 \times 10^{19}$
- (4) $1.35 \times 10^{19}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Energy $=$ Power $\times$ time
2. $= 150\ \mathrm{watt} \times 1\ \mathrm{s}$
3. $= 150\ \mathrm{J}$
4. Energy converted to light $= \frac{150 \times 8}{100} = 12\ \mathrm{J}$
5. $\mathrm{E} = \mathrm{nh}\nu$
6. Energy of one photon $= 4.42 \times 10^{-19}$
7. So, n $=$ number of photons $= \frac{\mathrm{E}}{\mathrm{h}\nu} = \frac{12}{4.42 \times 10^{-19}}$
8. $= 2.715 \times 10^{19}$

**Solved independently** (answer withheld)

1. Energy emitted as light each second $= 8\%$ of $150\,\mathrm{W} = \frac{8}{100} \times 150 = 12\,\mathrm{J\,s^{-1}}$.
2. Number of photons per second $n = \dfrac{\text{energy per second}}{\text{energy per photon}} = \dfrac{12}{4.42 \times 10^{-19}}$.
3. $n = 2.715 \times 10^{19} \approx 2.71 \times 10^{19}$ photons per second, which is option $1$.

**Subtopic:** Dual Behaviour of Electromagnetic Radiation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q056_69c71c94_30102026.png?v=69c71c9486ed)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q056_c539572e_30102026.png?v=c539572e093f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The number of photons emitted per second is the light power actually produced divided by the energy of one photon.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Most students pick option 3. Eight per cent of $150\,\mathrm{W}$ is $12\,\mathrm{W}$, and $12 / (4.42 \times 10^{-19}) = 2.71 \times 10^{19}$. Read the efficiency as 80%, or move the decimal one place while taking the percentage, and the useful power becomes $120\,\mathrm{W}$. That gives exactly the $27.2 \times 10^{19}$ printed in option 3.
- **Why:** You have to cut the rated power down to the stated efficiency, then divide by the photon energy. The question says 'rated at 150 watt, converting 8% energy into light' and asks 'how many photons are emitted by the bulb per second'.
<!--/ecat-->

## Q57

Chemistry · organic · Hydrocarbons

Methane reacts with steam at $1273\,\mathrm{K}$ in the presence of nickel catalyst to form :

- (1) $\mathrm{CO}$ and $\mathrm{H_2O}$
- (2) $\mathrm{CO_2}$ and $\mathrm{H_2}$
- **(3)** $\mathrm{CO}$ and $\mathrm{H_2}$
- (4) $\mathrm{CO_2}$ and $\mathrm{H_2O}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{CH_4(g)} + \mathrm{H_2O(g)} \xrightarrow[\Delta\ (1273\,\mathrm{K})]{\mathrm{Ni}} \mathrm{CO} + 3\mathrm{H_2}$
2. (Used for industrial preparation of dihydrogen gas)

**Solved independently** (answer withheld)

1. At $1273\,\mathrm{K}$ over a nickel catalyst methane undergoes steam reforming.
2. $\mathrm{CH_4(g)} + \mathrm{H_2O(g)} \xrightarrow{1273\,\mathrm{K},\ \mathrm{Ni}} \mathrm{CO(g)} + 3\mathrm{H_2(g)}$.
3. The products are carbon monoxide and dihydrogen (water gas or synthesis gas), which is option $3$.

**Subtopic:** Chemical Properties of Alkane · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q057_b3afc9da_30102026.png?v=b3afc9da3e9d)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q057_d23f68bd_30102026.png?v=d23f68bd4b2b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Steam reforming of methane over nickel at about 1273 K stops at synthesis gas. That is carbon monoxide plus hydrogen.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. Steam reforming is taught as the industrial route to hydrogen. The step a student recalls next to it is the water-gas shift, $\mathrm{CO} + \mathrm{H_2O} \rightarrow \mathrm{CO_2} + \mathrm{H_2}$. Option 2 prints the products of that shift. But the nickel-catalysed reaction this question names stops one stage earlier, at $\mathrm{CO} + 3\mathrm{H_2}$.
- **Why:** You have to give the products of one named industrial reaction. The question says 'Methane reacts with steam at 1273 K in the presence of nickel catalyst to form :'.
<!--/ecat-->

## Q58

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Compound P($\mathrm{C_8H_8O}$) gives a red orange precipitate with 2,4-DNP reagent and it does not reduce Fehling's reagent. On drastic oxidation with chromic acid, P gives an aromatic product Q that produces effervescence on treating with aq. $\mathrm{NaHCO_3}$. Compounds P and Q, respectively, are :

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q058_option_1_916e7103_30102026.png?v=916e7103c622) — P =, Q =
- (2) ![printed figure: option_2](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q058_option_2_19ff0787_30102026.png?v=19ff078776b6) — P =, Q =
- **(3)** ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q058_option_3_a36d7a43_30102026.png?v=a36d7a43f786) — P =, Q =
- **(4)** ![printed figure: option_4](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q058_option_4_dc469385_30102026.png?v=dc469385c478) — P =, Q =

**Answer** — booklet: (3, 4) · independent solve: (4) · agree

**Publisher's solution**

1. Degree of unsaturation $= (8 + 1) - \left(\frac{8}{2}\right)$
2. $= 9 - 4 = 5$
3. In question it is mentioned that oxidation under drastic condition, therefore it must be ketone

**Solved independently** (answer withheld)

1. The red-orange 2,4-DNP precipitate shows P contains a carbonyl group ($>\mathrm{C}=\mathrm{O}$).
2. Failure to reduce Fehling's reagent marks P as a ketone rather than an aliphatic aldehyde.
3. With the formula $\mathrm{C_8H_8O}$ and an aromatic skeleton, the ketone is acetophenone, $\mathrm{C_6H_5COCH_3}$, so P is acetophenone and options 2 and 3 are out.
4. Effervescence of Q with aq. $\mathrm{NaHCO_3}$ means Q is a carboxylic acid, since only acids stronger than carbonic acid liberate $\mathrm{CO_2}$.
5. Drastic oxidation of a methyl ketone with chromic acid cleaves the $\mathrm{C-C}$ bond on the carbonyl, so $\mathrm{C_6H_5COCH_3} \to \mathrm{C_6H_5COOH}$ (benzoic acid), not the $\alpha$-keto acid of option 1.
6. P = acetophenone and Q = benzoic acid is option $4$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test), Methods of Preparation of Carboxylic Acids · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 28)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q058_9710498d_30102026.png?v=9710498deaed)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q058_62cbf378_30102026.png?v=62cbf3787044)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A $\mathrm{C_8H_8O}$ compound that is 2,4-DNP positive but Fehling's negative is an aryl ketone. Oxidise its side chain hard and you are left with an aromatic carboxylic acid.
- **Why:** You have to read a substrate and its oxidation product off a set of reagent tests. The question says the compound 'gives a red orange precipitate with 2,4-DNP reagent and it does not reduce Fehling's reagent' and then asks 'Compounds P and Q, respectively, are :'.
- **Note:** The structures in all four options are not in the stored text, so no trap is named. The question text alone fixes P as an aryl ketone of formula $\mathrm{C_8H_8O}$ and Q as the aromatic acid from its drastic oxidation.
<!--/ecat-->

## Q59

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | $\mathrm{C_2H_4}$ | I. | $3\ \sigma$ bonds, $2\ \pi$ bonds |
| B. | $\mathrm{C_2H_2}$ | II. | $3\ \sigma$ bonds, one lone pair |
| C. | $\mathrm{CH_4}$ | III. | $4\ \sigma$ bonds |
| D. | $\mathrm{NH_3}$ | IV. | $5\ \sigma$ bonds, $1\ \pi$ bond |

- (1) A-III, B-IV, C-II, D-I
- **(2)** A-IV, B-I, C-III, D-II
- (3) A-I, B-II, C-IV, D-III
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{C_2H_4} \Rightarrow$
2. Number of $\sigma$ bonds $= 5$
3. Number of $\pi$ bond $= 1$
4. $\mathrm{C_2H_2} \Rightarrow \mathrm{H-C \equiv C-H}$
5. Number of $\sigma$-bonds $= 3$
6. Number of $\pi$-bonds $= 2$
7. $\mathrm{CH_4} \Rightarrow$
8. Number of $\sigma$-bonds $= 4$
9. $\mathrm{NH_3} \Rightarrow$
10. Number of $\sigma$-bonds $= 3$
11. Number of lone pair $=$ one
12. A-IV, B-I, C-III, D-II

**Solved independently** (answer withheld)

1. A: $\mathrm{C_2H_4}$ has four $\mathrm{C-H}$ $\sigma$ bonds plus one $\mathrm{C-C}$ $\sigma$ bond and one $\pi$ bond, i.e. $5\ \sigma$ and $1\ \pi$, so A-IV.
2. B: $\mathrm{C_2H_2}$ has two $\mathrm{C-H}$ $\sigma$ bonds plus one $\mathrm{C-C}$ $\sigma$ bond and two $\pi$ bonds, i.e. $3\ \sigma$ and $2\ \pi$, so B-I.
3. C: $\mathrm{CH_4}$ has four $\mathrm{C-H}$ $\sigma$ bonds and no $\pi$ bond, so C-III.
4. D: $\mathrm{NH_3}$ has three $\mathrm{N-H}$ $\sigma$ bonds and one lone pair on nitrogen, so D-II.
5. A-IV, B-I, C-III, D-II is option $2$.

**Subtopic:** Orbital Overlap Concept · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q059_aac41cd2_30102026.png?v=aac41cd29fe9)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q059_3c9ca1c9_30102026.png?v=3c9ca1c9b3c6)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** You count the bonds in a small molecule. Every link gives one $\sigma$ bond. The extra links of a double or triple bond are $\pi$ bonds. Unshared pairs are counted on their own.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  There is no one trap here. Methane's count is the entry no option can hide: four bonds and nothing else, which is List II entry III. That pairing appears only in option 2. The other three options hand $\mathrm{CH_4}$ a lone pair in option 1, a $\pi$ bond in option 3, or three $\sigma$ bonds with a lone pair in option 4. Each wrong option also gives $\mathrm{NH_3}$ a $\pi$ bond or $\mathrm{C_2H_2}$ a lone pair. So no one of them can be reached by a mistake the other two do not share.
- **Why:** You have to count $\sigma$ bonds, $\pi$ bonds and lone pairs for four molecules and pair the counts up. List I prints '$\mathrm{C_2H_4}$', '$\mathrm{C_2H_2}$', '$\mathrm{CH_4}$' and '$\mathrm{NH_3}$'. List II holds entries such as '$5\ \sigma$ bonds, $1\ \pi$ bond'.
- **Note:** asks re-pointed from compare: the bond-counting rule applied to each molecule. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q60

Chemistry · organic · Haloalkanes and Haloarenes

The following two reactions give the same foul smelling product Z.

[drawn reaction scheme in the stem figure - two reactions, see figure_bbox]

X and Z, respectively, are :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q060_2c61dc66_30102026.png?v=2c61dc66d6a0)

- **(1)** X = $\mathrm{AgCN}$; Z = $\mathrm{C_2H_5NC}$
- (2) X = $\mathrm{KCN}$; Z = $\mathrm{C_2H_5CN}$
- (3) X = $\mathrm{AgCN}$; Z = $\mathrm{C_2H_5CN}$
- (4) X = $\mathrm{KCN}$; Z = $\mathrm{C_2H_5NC}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{C_2H_5Cl} \xrightarrow{\mathrm{AgCN}} \mathrm{C_2H_5NC\ (Z)}$ (foul smell compound)
2. $\mathrm{C_2H_5}\overset{\overset{\mathrm{O}}{\|}}{\mathrm{C}}\mathrm{NH_2} \xrightarrow{\mathrm{Br_2 + NaOH}} \mathrm{C_2H_5NH_2} \xrightarrow[\Delta]{\mathrm{CHCl_3/ethanolic\ KOH}} \mathrm{C_2H_5NC\ (Z)}$
3. So, $\mathrm{X} = \mathrm{AgCN}$
4. $\mathrm{Z} = \mathrm{C_2H_5NC}$

**Solved independently** (answer withheld)

1. Second route, step 1: $\mathrm{C_2H_5CONH_2} \xrightarrow{\mathrm{Br_2,\ NaOH}} \mathrm{C_2H_5NH_2}$, the Hofmann bromamide degradation with loss of one carbon, so Y is ethylamine.
2. Second route, step 2: a primary amine with $\mathrm{CHCl_3}$ and ethanolic $\mathrm{KOH}$ on heating is the carbylamine reaction, giving $\mathrm{C_2H_5NC}$, ethyl isocyanide, which has the characteristic foul smell stated.
3. So $Z = \mathrm{C_2H_5NC}$, which rules out options 2 and 3.
4. First route: $\mathrm{C_2H_5Cl} + X \to \mathrm{C_2H_5NC}$. The ambident cyanide ion attacks through carbon with ionic $\mathrm{KCN}$ (giving the nitrile) but through nitrogen with covalent $\mathrm{AgCN}$ (giving the isocyanide).
5. To get the isocyanide, $X = \mathrm{AgCN}$, so $X = \mathrm{AgCN}$ and $Z = \mathrm{C_2H_5NC}$, which is option $1$.

**Subtopic:** Reactions of Haloalkanes - Nucleophilic Substitution · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 30)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q060_2dd1f19b_30102026.png?v=2dd1f19b8f57)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q060_e6f45f9c_30102026.png?v=e6f45f9ce6e1)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Cyanide is ambidentate. Ionic KCN bonds through carbon and gives a nitrile. Covalent AgCN bonds through nitrogen and gives the foul-smelling isocyanide.
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  Most students pick option 3. They have placed $\mathrm{AgCN}$ correctly as the silver reagent, but they still draw the bond at the carbon. Carbon is the end of $\mathrm{CN^-}$ they have always seen attacking. So they write $\mathrm{C_2H_5CN}$. Silver's covalent cyanide leaves the nitrogen as the donor. So the product is the isocyanide $\mathrm{C_2H_5NC}$. That is what the words 'foul smelling' are pointing at.
- **Also:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Some students pick option 2. The reaction drilled hardest in this chapter is alkyl halide plus $\mathrm{KCN} \rightarrow$ alkyl cyanide. A student who answers from that habit takes both halves of option 2 together. It is a true reaction. But its product is a nitrile, and nitriles are not the foul-smelling compound the question asks for.
- **Why:** You have to settle the reagent and the product of a cyanide substitution together. The question says the two routes 'give the same foul smelling product Z'. The options cross 'X = AgCN' or 'X = KCN' with 'Z = $\mathrm{C_2H_5NC}$' or 'Z = $\mathrm{C_2H_5CN}$'.
<!--/ecat-->

## Q61

Chemistry · physical · Basic Concepts of Chemistry

The number of hydrogen atoms present in 5.4 g of urea is:
(Given: Molar mass of urea : $60\,\mathrm{g\,mol^{-1}}$
$\mathrm{N_A}$ : $6.022 \times 10^{23}$ particles $\mathrm{mol^{-1}}$)

- (1) $1.084 \times 10^{23}$
- (2) $1.084 \times 10^{22}$
- (3) $2.168 \times 10^{22}$
- **(4)** $2.168 \times 10^{23}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Structure of urea : $\mathrm{H_2N} - \overset{\overset{\mathrm{O}}{\|}}{\mathrm{C}} - \mathrm{NH_2}$
2. Mole of urea $= \frac{5.4}{60} = 0.09$
3. Number of hydrogen atoms $= 0.09 \times 4 \times 6.022 \times 10^{23}$
4. $= 2.1679 \times 10^{23}$
5. $\simeq 2.168 \times 10^{23}$

**Solved independently** (answer withheld)

1. Moles of urea $= \dfrac{5.4}{60} = 0.09\ \mathrm{mol}$.
2. Urea is $\mathrm{NH_2CONH_2}$, so each molecule carries $4$ hydrogen atoms.
3. Moles of hydrogen atoms $= 0.09 \times 4 = 0.36\ \mathrm{mol}$.
4. Number of H atoms $= 0.36 \times 6.022 \times 10^{23} = 2.168 \times 10^{23}$, which is option $4$.

**Subtopic:** Mole Concept · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q061_c1df8cbf_30102026.png?v=c1df8cbfbba7)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q061_60e085d0_30102026.png?v=60e085d0333a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The number of atoms of an element is the moles of compound, times the atoms of that element in one formula unit, times Avogadro's number.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Most students pick option 1. $5.4/60 = 0.09\,\mathrm{mol}$. Urea written as $\mathrm{NH_2CONH_2}$ carries four hydrogens, two in each $-\mathrm{NH_2}$. Count only one hydrogen per amide group and you get $0.09 \times 2 \times 6.022\times10^{23} = 1.084\times10^{23}$, which is option 1. The same count is also the number of nitrogen atoms, so the figure feels like it checks out.
- **Why:** You have to take the moles of urea, multiply by the hydrogens in one formula unit, and multiply by Avogadro's number. The question asks for 'The number of hydrogen atoms present in 5.4 g of urea' and supplies the molar mass and $\mathrm{N_A}$.
<!--/ecat-->

## Q62

Chemistry · inorganic · The p–Block Elements

Identify the incorrect statement from the following:

- (1) Nitrogen can form $p\pi\text{-}p\pi$ multiple bonds with itself.
- (2) $\mathrm{P(C_2H_5)_3}$ and $\mathrm{As(C_6H_5)_3}$ form $d\pi\text{-}d\pi$ bond with transition metals.
- (3) Phosphorus, arsenic and antimony show catenation property.
- **(4)** Nitrogen can form $d\pi\text{-}p\pi$ bond with oxygen.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Both nitrogen and oxygen do not contain $d$-orbitals so it cannot form $d\pi\text{-}p\pi$ bond.
2. Phosphorus and Arsenic can form $d\pi\text{-}d\pi$ bond with transition metals. Since both have vacant $d$-orbitals by which it can interact with transition metals and can involve in $d\pi\text{-}d\pi$ interaction.
3. Phosphorous, Arsenic and Antimony show catenation property.

**Solved independently** (answer withheld)

1. Statement 1 is correct: nitrogen's small size lets $2p$ orbitals overlap sideways, giving the $p\pi\text{-}p\pi$ multiple bonding of $\mathrm{N}\equiv\mathrm{N}$.
2. Statement 2 is correct: heavier group 15 donors such as $\mathrm{P(C_2H_5)_3}$ and $\mathrm{As(C_6H_5)_3}$ act as ligands and form $d\pi\text{-}d\pi$ bonds with transition metals.
3. Statement 3 is correct: catenation does occur in P, As and Sb (strongest in phosphorus, falling down the group, essentially absent in bismuth).
4. Statement 4 is wrong: nitrogen belongs to the second period and has no $d$ orbitals available, so it cannot form $d\pi\text{-}p\pi$ bonds; only the heavier elements do this, as in $\mathrm{R_3P{=}O}$.
5. The incorrect statement is option $4$.

**Subtopic:** General Properties & Trends of Group 15 (Nitrogen Family) · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 30)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q062_32167c14_30102026.png?v=32167c14f35c)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q062_8d17d61a_30102026.png?v=8d17d61aa197)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nitrogen has no d orbitals. So it makes $p\pi$-$p\pi$ bonds with itself, but it cannot make the $d\pi$-$p\pi$ bonds the heavier group-15 elements make.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. The phrase a student carries out of this paragraph is '$d\pi$-$p\pi$', from $\mathrm{R_3P{=}O}$. So '$d\pi$-$d\pi$' in option 2 looks like the garbled version and gets marked as the incorrect statement. But the book does state that $\mathrm{P(C_2H_5)_3}$ and $\mathrm{As(C_6H_5)_3}$ form $d\pi$-$d\pi$ bonds with transition metals. The statement that actually fails is option 4, about nitrogen having no d orbitals to bond with.
- **Why:** You have to check four stated facts about group-15 bonding one at a time, and the question is asked the other way round. It says 'Identify the incorrect statement from the following:' and each option is a full claim.
<!--/ecat-->

## Q63

Chemistry · inorganic · Coordination Compounds – Practice

Which one of the following is an ambidentate ligand?

- (1) Ethane-1,2-diamine
- (2) Ethylenediaminetetraacetate ion
- **(3)** Thiocyanate
- (4) Oxalate

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. An ambidentate ligand is a ligand which has two different donor atoms and either of the two ligates in complex.
2. (1) Ethane-1,2-diamine $\to$ didentate
3. (2) Ethylenediamine tetraacetate ion $\to$ hexadentate
4. (3) Thiocyanate ($\mathrm{SCN^{-}}$) $\to$ Ambidentate ligand.
5. (4) Oxalate $\to$ didentate

**Solved independently** (answer withheld)

1. An ambidentate ligand is a monodentate ligand with two different donor atoms, able to bind through either one.
2. Ethane-1,2-diamine is bidentate (two N donors used together) and oxalate is bidentate (two O donors used together), so neither is ambidentate.
3. EDTA$^{4-}$ is hexadentate, binding through two N and four O at once, so it is not ambidentate either.
4. Thiocyanate binds either as $\mathrm{M{\leftarrow}SCN}$ (thiocyanato) or as $\mathrm{M{\leftarrow}NCS}$ (isothiocyanato), so it is ambidentate, option $3$.

**Subtopic:** Ligands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q063_7174d3c5_30102026.png?v=7174d3c53064)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q063_bda98406_30102026.png?v=bda984068968)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An ambidentate ligand has two different donor atoms and binds through one or the other. A didentate ligand binds through two donors at the same time.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. Ethane-1,2-diamine is the standard worked example of a didentate ligand, and 'ambidentate' gets read as the same word. Ambidentate means there is a choice of donor atom. Thiocyanate attaching through sulphur or through nitrogen is the example. It does not mean two nitrogens gripping the metal together.
- **Why:** You have to match one stated definition to the ligand that fits it. The question asks 'Which one of the following is an ambidentate ligand?' and the four options are named ligands.
<!--/ecat-->

## Q64

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

The correct order of increasing metallic character of Na, Be, P, Mg and Si is

- **(1)** $\mathrm{P} < \mathrm{Si} < \mathrm{Be} < \mathrm{Mg} < \mathrm{Na}$
- (2) $\mathrm{P} < \mathrm{Si} < \mathrm{Na} < \mathrm{Mg} < \mathrm{Be}$
- (3) $\mathrm{P} < \mathrm{Mg} < \mathrm{Be} < \mathrm{Si} < \mathrm{Na}$
- (4) $\mathrm{Be} < \mathrm{Si} < \mathrm{P} < \mathrm{Mg} < \mathrm{Na}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. On moving left to right in a period, metallic character decreases and on moving top to bottom in a group, metallic character increases. So, the correct order of increasing metallic character is
2. $\mathrm{P} < \mathrm{Si} < \mathrm{Be} < \mathrm{Mg} < \mathrm{Na}$
3. Electronegativity $\propto \frac{1}{\text{Metallic character}}$
4. Electronegativity (On Pauling scale): $\mathrm{Na}$ $0.9$, $\mathrm{Mg}$ $1.2$, $\mathrm{Be}$ $1.5$, $\mathrm{Si}$ $1.8$, $\mathrm{P}$ $2.1$

**Solved independently** (answer withheld)

1. Metallic character decreases left to right across a period, so within period 3 the order is $\mathrm{P} < \mathrm{Si} < \mathrm{Mg} < \mathrm{Na}$.
2. Metallic character increases down a group, so $\mathrm{Be} < \mathrm{Mg}$ in group 2.
3. Be is a group 2 metal while Si is a metalloid and P a non-metal, so Be is more metallic than both: $\mathrm{P} < \mathrm{Si} < \mathrm{Be}$.
4. Combining gives $\mathrm{P} < \mathrm{Si} < \mathrm{Be} < \mathrm{Mg} < \mathrm{Na}$, which is option $1$.

**Subtopic:** Periodic Trends and Chemical Reactivity · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q064_905f5338_30102026.png?v=905f53384ed7)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q064_637333c9_30102026.png?v=637333c93a3b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Metallic character falls as you go left to right across a period. It rises as you go down a group.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Most students pick option 2. Options 1 and 2 agree that $\mathrm{P} < \mathrm{Si}$ and differ only over the three metals. Option 2 prints $\mathrm{Na} < \mathrm{Mg} < \mathrm{Be}$, which is the correct triple read upwards. A student who carries 'ionisation enthalpy increases up a group' and treats the most metallic as the hardest to ionise puts Be at the metallic end. Be is in fact the least metallic metal here.
- **Why:** You have to arrange five named elements on one periodic trend. The question says 'The correct order of increasing metallic character of Na, Be, P, Mg and Si' and each option is a full ordering.
<!--/ecat-->

## Q65

Chemistry · organic · Alcohols, Phenols and Ethers

Match List I with List II:

Choose the correct answer from the options given below :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q065_ebbaff5e_30102026.png?v=ebbaff5ebe28)

| List-I | | List-II | |
|---|---|---|---|
| A. | [structure diagram - drawn reaction scheme in the stem figure] | (I) | (i) Oleum; (ii) $\mathrm{NaOH}$, $\Delta$; (iii) $\mathrm{H^+}$ |
| B. | $\mathrm{CH_3COOH} \longrightarrow \mathrm{CH_3CH_2OH}$ | (II) | (i) $\mathrm{O_2}$; (ii) $\mathrm{H_2O/H^+}$ |
| C. | $\mathrm{CH_3CH_2CH_2OH} \longrightarrow$ [structure diagram - drawn product in the stem figure] | (III) | (i) $\mathrm{CH_3OH}$, $\mathrm{H^+}$; (ii) $\mathrm{H_2}$, catalyst |
| D | [structure diagram - drawn reaction scheme in the stem figure] | (IV) | (i) conc. $\mathrm{H_2SO_4}$, $\Delta$; (ii) $\mathrm{H^+/H_2O}$ |

- (1) A-II, B-III, C-I, D-IV
- **(2)** A-II, B-III, C-IV, D-I
- (3) A-II, B-IV, C-III, D-I
- (4) A-I, B-III, C-IV, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. A.
2. B. $\mathrm{CH_3COOH} \xrightarrow[\mathrm{(ii)\ H_2,\ catalyst}]{\mathrm{(i)\ CH_3OH,\ H^{+}}} \mathrm{CH_3CH_2OH}$
3. C. $\mathrm{CH_3CH_2CH_2{-}OH} \xrightarrow[\text{Dehydration}]{\mathrm{conc.H_2SO_4/\Delta}} \mathrm{CH_3CH{=}CH_2} \xrightarrow{\mathrm{H^{+}/H_2O}} \mathrm{CH_3}\underset{\mathrm{OH}}{\mathrm{CH}}\mathrm{CH_3}$
4. D

**Solved independently** (answer withheld)

1. A is isopropylbenzene (cumene) $\to$ phenol; this is the cumene process, air oxidation to cumene hydroperoxide then acid hydrolysis, so A-II ((i) $\mathrm{O_2}$; (ii) $\mathrm{H_2O/H^+}$).
2. B is $\mathrm{CH_3COOH} \to \mathrm{CH_3CH_2OH}$; the acid is first esterified with methanol and the ester then hydrogenated to the primary alcohol, so B-III ((i) $\mathrm{CH_3OH}, \mathrm{H^+}$; (ii) $\mathrm{H_2}$, catalyst).
3. C is propan-1-ol $\to$ propan-2-ol; conc. $\mathrm{H_2SO_4}$ with heat dehydrates it to propene, and $\mathrm{H^+/H_2O}$ rehydrates it by Markovnikov addition onto the middle carbon, so C-IV.
4. D is benzene $\to$ phenol; sulphonation with oleum gives benzenesulphonic acid, fusion with $\mathrm{NaOH}$ gives sodium phenoxide and acidification liberates phenol, so D-I.
5. A-II, B-III, C-IV, D-I is option $2$.

**Subtopic:** Preparation of Phenols, Preparation of Alcohols · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 31)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q065_4262f336_30102026.png?v=4262f3364e33)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q065_340f64e2_30102026.png?v=340f64e2a7ab)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** You have to match a conversion with the reagent sequence that brings it about. The numbered steps are taken in the order they are printed.
- **Why:** You have to pair four conversions with the reagent sequences that bring them about. List II prints sets such as '(i) Oleum; (ii) $\mathrm{NaOH}$, $\Delta$; (iii) $\mathrm{H^+}$' against the schemes of List I.
- **Note:** Entries A and D, and the product of C, are drawn structures that are not in the stored text. Only B, $\mathrm{CH_3COOH} \longrightarrow \mathrm{CH_3CH_2OH}$, can be read. One row is not enough to settle the code, so no trap is named. asks re-pointed from compare: a conversion paired with the reagent sequence that does it. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q66

Chemistry · inorganic · The D- and F-Block Elements – Practice

Although $+3$ oxidation state is most common in lanthanoids, cerium still shows $+4$ oxidation state because:

- (1) After losing one more electron, it acquires $4f^{14}$ electronic configuration.
- (2) Its nearest inert gas is Radon.
- (3) Its atomic number is 61.
- **(4)** After losing one more electron, it acquires $4f^{0}$ electronic configuration.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Although $+3$ oxidation state is most common in lanthanoids, cerium still shows $+4$ oxidation state because after losing one more electron it acquires $4f^{0}$ electronic configuration.

**Solved independently** (answer withheld)

1. Cerium's ground configuration is $\mathrm{[Xe]}\,4f^1\,5d^1\,6s^2$.
2. Losing three electrons gives $\mathrm{Ce^{3+}} = \mathrm{[Xe]}\,4f^1$, the usual lanthanoid $+3$ state.
3. Losing the one remaining $4f$ electron gives $\mathrm{Ce^{4+}} = \mathrm{[Xe]}\,4f^{0}$, an empty $f$ subshell matching the xenon core, which is extra stable.
4. That is the $4f^{0}$ configuration of option $4$.

**Subtopic:** Oxidation State · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 32)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q066_9ff92292_30102026.png?v=9ff92292fec5)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q066_33ab22d2_30102026.png?v=33ab22d2bedb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Cerium reaches +4 because the fourth electron leaves it with an empty $4f$ subshell. That is the xenon core.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. The stability argument students carry into this chapter is 'empty, half-filled or completely filled $f$ subshell', and $4f^{14}$ is the filled one. But filled $f$ is what explains ytterbium and lutetium at the far end of the series. Cerium sits at the start with a single $4f$ electron. So losing one more empties the subshell instead of filling it.
- **Why:** You have to give the stated reason for one unusual oxidation state. The question says 'cerium still shows +4 oxidation state because:' and each option offers a possible explanation.
<!--/ecat-->

## Q67

Chemistry · organic · Haloalkanes and Haloarenes

In the following reaction sequence, X and Z respectively are :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q067_560bdb58_30102026.png?v=560bdb58e470)

- (1) ![printed figure: option_1](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q067_option_1_169b7350_30102026.png?v=169b73503182) — $X = \mathrm{POCl_3}$; $Z = \mathrm{CH_3-\underset{\textstyle |}{C}H-CH_3}$ with $\mathrm{Br}$ on the middle carbon [printed as a two-line drawn structure; see option_boxes]
- **(2)** $X = \mathrm{POCl_3}$; $Z = \mathrm{CH_3CH_2CH_2-Br}$
- (3) ![printed figure: option_3](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q067_option_3_633cac8d_30102026.png?v=633cac8d7136) — $X = \mathrm{H_3PO_3}$; $Z = \mathrm{CH_3-\underset{\textstyle |}{C}H-CH_3}$ with $\mathrm{Br}$ on the middle carbon [printed as a two-line drawn structure; see option_boxes]
- (4) $X = \mathrm{H_3PO_3}$; $Z = \mathrm{CH_3CH_2CH_2-Br}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{CH_3CH_2CH_2-OH} \xrightarrow{\mathrm{PCl_5}} \mathrm{CH_3CH_2CH_2Cl} + \mathrm{POCl_3}\ (X) + \mathrm{HCl}$
2. $\mathrm{CH_3CH_2CH_2Cl} \xrightarrow[\Delta]{\text{alc. KOH}} \mathrm{CH_3CH=CH_2}\ (Y)$
3. $\mathrm{CH_3CH=CH_2}\ (Y) \xrightarrow[(\mathrm{C_6H_5CO})_2\mathrm{O_2}]{\mathrm{HBr}} \mathrm{CH_3CH_2CH_2-Br}\ (Z)$
4. So, $\mathrm{X} = \mathrm{POCl_3}$
5. $\mathrm{Z} = \mathrm{CH_3CH_2CH_2Br}$

**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2OH} + \mathrm{PCl_5} \to \mathrm{CH_3CH_2CH_2Cl} + \mathrm{POCl_3} + \mathrm{HCl}$, so $X = \mathrm{POCl_3}$ and options 3 and 4 are out.
2. 1-chloropropane with alcoholic $\mathrm{KOH}$ on heating undergoes dehydrohalogenation, so $Y = \mathrm{CH_3CH{=}CH_2}$ (propene).
3. Benzoyl peroxide $\mathrm{(C_6H_5CO)_2O_2}$ makes $\mathrm{HBr}$ add by a free-radical chain, the peroxide (Kharasch) effect, which is anti-Markovnikov.
4. The bromine therefore lands on the terminal carbon: $Z = \mathrm{CH_3CH_2CH_2Br}$, 1-bromopropane, not the 2-bromo isomer.
5. $X = \mathrm{POCl_3}$ with $Z = \mathrm{CH_3CH_2CH_2Br}$ is option $2$.

**Subtopic:** Methods of Preparation of Haloalkanes from Alcohols, Halogen Exchange, and Hydrocarbons · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 32)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q067_f5987f25_30102026.png?v=f5987f25b1ea)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q067_3fa5593c_30102026.png?v=3fa5593cd28a)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** You have to say which phosphorus by-product a chlorinating reagent leaves behind. You also have to say which carbon of the three-carbon chain the bromine ends up on.
- **Why:** You have to identify a by-product and a bromide together from a printed sequence. The question says 'In the following reaction sequence, X and Z respectively are :'.
- **Note:** The sequence itself is not in the stored text. Whether X is $\mathrm{POCl_3}$ or $\mathrm{H_3PO_3}$ depends on which phosphorus reagent the scheme prints. Whether Z is the 1-bromide or the 2-bromide depends on the conditions it prints. So no trap is named.
<!--/ecat-->

## Q68

Chemistry · inorganic · Coordination Compounds – Practice

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | $[\mathrm{Pt(Cl_2)(NH_3)_2}]$ | (I) | Octahedral |
| B. | $[\mathrm{Co(NH_3)_6}]\mathrm{Cl_3}$ | (II) | Trigonal bipyramidal |
| C. | $[\mathrm{NiCl_4}]^{2-}$ | (III) | Square planar |
| D | $[\mathrm{Fe(CO)_5}]$ | (IV) | Tetrahedral |

- (1) A-III, B-IV, C-I, D-II
- **(2)** A-III, B-I, C-IV, D-II
- (3) A-IV, B-I, C-III, D-II
- (4) A-I, B-III, C-IV, D-II

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In $[\mathrm{Pt(Cl_2)(NH_3)_2}]$; Pt has $dsp^{2}$ hybridisation, so shape of complex is square planar.
2. In $[\mathrm{Co(NH_3)_6}]\mathrm{Cl_3}$; Co has $d^{2}sp^{3}$ hybridisation so shape of complex is octahedral.
3. In $[\mathrm{NiCl_4}]^{2-}$; Ni has $sp^{3}$ hybridisation so shape of complex ion is tetrahedral.
4. In $[\mathrm{Fe(CO)_5}]$; shape of complex is trigonal bipyramidal.

**Solved independently** (answer withheld)

1. A: $\mathrm{[Pt(Cl)_2(NH_3)_2]}$ has a $d^8$ $\mathrm{Pt^{2+}}$ centre with coordination number 4, and $\mathrm{Pt(II)}$ complexes are $dsp^2$ square planar, so A-III.
2. B: $\mathrm{[Co(NH_3)_6]Cl_3}$ has coordination number 6 about $\mathrm{Co^{3+}}$, so it is octahedral, giving B-I.
3. C: $\mathrm{[NiCl_4]^{2-}}$ has $\mathrm{Ni^{2+}}$ with the weak-field chloride, so it stays $sp^3$ tetrahedral, giving C-IV.
4. D: $\mathrm{[Fe(CO)_5]}$ has coordination number 5 with $dsp^3$ hybridisation, so it is trigonal bipyramidal, giving D-II.
5. A-III, B-I, C-IV, D-II is option $2$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 33)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q068_7d0f2d78_30102026.png?v=7d0f2d781d39)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q068_352b92b3_30102026.png?v=352b92b37fc9)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Coordination number alone does not fix the shape. Four-coordinate Pt(II) is square planar. Four-coordinate Ni(II) with chloride is tetrahedral.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3. Two entries are four-coordinate, A and C. The rule you carry over from carbon is that four groups go to the corners of a tetrahedron, so A goes on IV. $[\mathrm{NiCl_4}]^{2-}$ then takes square planar because nothing else is left. The two shapes end up on each other's complexes. Pt(II) is the square planar one. Nickel(II) with four weak-field chlorides is the tetrahedral one.
- **Why:** You have to pair four complexes with their shapes. List I prints '$[\mathrm{Pt(Cl_2)(NH_3)_2}]$' and '$[\mathrm{NiCl_4}]^{2-}$'. List II holds 'Octahedral', 'Trigonal bipyramidal', 'Square planar' and 'Tetrahedral'.
- **Note:** asks re-pointed from compare: the coordination-number-to-shape rules applied to each complex. `compare` is for telling similar things apart, not for a pairing answer -- qtype match_columns already says that.
<!--/ecat-->

## Q69

Chemistry · organic · Alcohols, Phenols and Ethers

The functional group that can be identified through phthalein dye test is :

- (1) Aldehyde
- **(2)** Phenolic
- (3) Carboxylic acid
- (4) Alcohol

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Phthalein Dye test: Phenol on heating with phthalic anhydride in presence of concentrated sulphuric acid forms a colourless condensation compound called phenolphthalein. On further reaction with NaOH it gives pink colour.
2. So phenolic group is correct answer.

**Solved independently** (answer withheld)

1. The phthalein dye test heats the compound with phthalic anhydride and concentrated $\mathrm{H_2SO_4}$, then adds dilute $\mathrm{NaOH}$.
2. A deep pink or dark green colour appears because the phenol condenses with phthalic anhydride to form phenolphthalein, whose alkaline form is coloured.
3. This condensation requires an activated aromatic ring bearing $\mathrm{-OH}$, so the test is specific to the phenolic group, option $2$.
4. Aldehydes (Tollens'/Fehling's), carboxylic acids ($\mathrm{NaHCO_3}$ effervescence) and alcohols (Lucas, ceric ammonium nitrate) are identified by other tests.

**Subtopic:** Test of Phenol · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 33)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q069_5fadd70a_30102026.png?v=5fadd70ab7b9)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q069_33f0f3db_30102026.png?v=33f0f3dbd917)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** The phthalein dye test joins a phenol to phthalic anhydride and gives phenolphthalein. Phenolphthalein turns pink in alkali.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Most students pick option 4. 'Phenolic' and 'Alcohol' are both $-\mathrm{OH}$ groups out of the same chapter. So a student who has filed this test under '$-\mathrm{OH}$ compounds' sees two options that fit that memory. But the condensation needs the aromatic ring the phenol brings, and an alcohol has not got one.
- **Why:** You have to say what one named bench test detects. The question says 'The functional group that can be identified through phthalein dye test is :' and the four options are functional groups.
<!--/ecat-->

## Q70

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

Two products X and Y are formed in the following reaction sequence.

The suitable method that can be used for the separation of products X and Y is :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q070_7cdd71fa_30102026.png?v=7cdd71faaf01)

- **(1)** Fractional distillation
- (2) Sublimation
- (3) Differential extraction
- (4) Continuous extraction

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The ortho and para isomers are separated by fractional distillation under reduced pressure.
2. o-isomer, (M.P. $\to -4^\circ\mathrm{C}$, B.P. $\to 222^\circ\mathrm{C}$)
3. p-isomer, (M.P. $\to 54^\circ\mathrm{C}$, B.P. $\to 238^\circ\mathrm{C}$)

**Solved independently** (answer withheld)

1. Benzene with $\mathrm{CH_3Cl}$ and anhydrous $\mathrm{AlCl_3}$ undergoes Friedel-Crafts alkylation, so $W$ is toluene.
2. The $\mathrm{-CH_3}$ group is activating and ortho/para directing, so nitration of toluene gives two products, $o$-nitrotoluene and $p$-nitrotoluene.
3. Both are neutral organic liquids of nearly the same structure, so no acid-base or solubility difference exists for extraction to exploit, ruling out differential and continuous extraction.
4. Neither isomer sublimes, so sublimation is out as well.
5. The two isomers differ only slightly in boiling point (about $222\,^{\circ}\mathrm{C}$ and $238\,^{\circ}\mathrm{C}$), the exact case for which fractional distillation is used, so the answer is option $1$.

**Subtopic:** Methods of Purification of Organic Compounds · **Difficulty:** unsure (2 steps)

**Printed in the booklet** (page 34)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q070_10956535_30102026.png?v=109565354929)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q070_1a3f0a75_30102026.png?v=1a3f0a751b9d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** You choose a separation technique from how the two products differ. They may differ in boiling point, in how readily they come over with steam, or in how they dissolve between two solvents.
- **Why:** You have to match a separation technique to a particular pair of products. The question says 'The suitable method that can be used for the separation of products X and Y is :'.
- **Note:** The reaction sequence is not in the stored text. So what X and Y actually are cannot be read here, and that is the thing that decides between the four techniques. No trap is named.
<!--/ecat-->

## Q71

Chemistry · physical · Solutions

Identify the correct statements :

Choose the correct answer from the options given below :

- **((A))** The molality of $2.5\,\mathrm{g}$ of ethanoic acid (Molar mass : $60\,\mathrm{g\,mol^{-1}}$) in $75\,\mathrm{g}$ of benzene solution is $0.556\,\mathrm{m}$.
- **((B))** The molarity of a solution containing $5\,\mathrm{g}$ of $\mathrm{NaOH}$ (molar mass : $40\,\mathrm{g\,mol^{-1}}$) in $450\,\mathrm{mL}$ of solution is $0.278\,\mathrm{M}$ at $298\,\mathrm{K}$.
- **((C))** Aquatic species are more comfortable in cold water.
- **((D))** The solubility of gas increases with decrease in pressure.
- **((E))** For a binary mixture of A and B, the number of moles of A and B are $n_{\mathrm{A}}$ and $n_{\mathrm{B}}$ respectively. The mole fraction of B will be $x_{\mathrm{B}} = \dfrac{n_{\mathrm{A}}}{n_{\mathrm{A}} + n_{\mathrm{B}}}$.

- **(1)** A, B and C only
- (2) A and B only
- (3) A and C only
- (4) A, D and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (A) Molality $= \frac{2.5}{60} \times \frac{1000}{75} = 0.556$ molal
2. (B) Molarity $= \frac{5}{40} \times \frac{1000}{450} = 0.278\ \mathrm{M}$
3. (C) Aquatic species are more comfortable in cold water
4. Henry's Law $\mathrm{K_H} \propto \mathrm{Temp} \propto \frac{1}{\text{solubility}}$
5. (D) According to Henry's Law,
6. $\mathrm{P} = \mathrm{K_H}\mathrm{X}$
7. $\mathrm{P} \propto \mathrm{x}$
8. $\mathrm{P} \propto$ Solubility
9. So as $\mathrm{P}\uparrow$, solubility $\uparrow$
10. (E) $\mathrm{x_B} = \frac{\mathrm{n_B}}{\mathrm{n_A} + \mathrm{n_B}}$

**Solved independently** (answer withheld)

1. A: moles of ethanoic acid $= \dfrac{2.5}{60} = 0.04167\ \mathrm{mol}$, and the solvent mass is $75\ \mathrm{g} = 0.075\ \mathrm{kg}$.
2. Molality $= \dfrac{0.04167}{0.075} = 0.556\ \mathrm{m}$, so statement A is correct.
3. B: moles of $\mathrm{NaOH} = \dfrac{5}{40} = 0.125\ \mathrm{mol}$ in $450\ \mathrm{mL} = 0.450\ \mathrm{L}$.
4. Molarity $= \dfrac{0.125}{0.450} = 0.278\ \mathrm{M}$, so statement B is correct.
5. C: the dissolution of a gas is exothermic, so oxygen is more soluble in cold water, and aquatic species are indeed more comfortable in cold water; statement C is correct.
6. D: Henry's law gives $p = K_H x$, so solubility rises with pressure and falls when pressure drops; statement D is wrong.
7. E: by definition $x_{\mathrm{B}} = \dfrac{n_{\mathrm{B}}}{n_{\mathrm{A}} + n_{\mathrm{B}}}$, so the expression printed in E is wrong.
8. A, B and C only is option $1$.

**Subtopic:** Expressing Concentration of Solutions, Solubility of a Gas in a Liquid · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 34)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q071_202f2403_30102026.png?v=202f2403542c)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q071_e37e8964_30102026.png?v=e37e8964e75d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **New ask (proposed)** (`new_asks`) — something the question wants that none of the above describes
- **Concept:** You judge a set of unlike claims one at a time. Two of them are concentrations you work out from masses. Two are about Henry's law, one against pressure and one against temperature. One is the definition of mole fraction.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. A and B are the two statements you can settle on paper. They give $\frac{2.5/60}{0.075} = 0.556\,\mathrm{m}$ and $\frac{5/40}{0.450} = 0.278\,\mathrm{M}$. So both get ticked and the set looks finished. C gets left out because 'Aquatic species are more comfortable in cold water' reads like an aside rather than chemistry. But C is the textbook's own consequence of gas solubility falling as temperature rises. So A, B and C together are the complete set.
- **Proposed:** `verify_mixed_claims` — placed on asks, not trap: the five lettered statements are of unlike kinds, two concentration values that must be computed and three recalled claims about Henry's law and mole fraction, so no one existing value says what the question wants. fact_line would hide the two computations that decide A and B, and calculate would hide the three statements that are settled from stated facts.
- **Why:** You have to judge five lettered claims of different kinds, one at a time, and collect the true ones. The question says 'Identify the correct statements :' above a list that runs from a molality value to the definition '$x_{\mathrm{B}} = \dfrac{n_{\mathrm{A}}}{n_{\mathrm{A}} + n_{\mathrm{B}}}$'.
- **Note:** Statement A prints '75 g of benzene solution'. The value 0.556 m follows only if those 75 g are the benzene, that is the solvent. Read as 75 g of solution, the molality would be 0.575 m. A appears in all four options, so this reading does not change the answer.
<!--/ecat-->

## Q72

Chemistry · organic · Basic Principles and Techniques of Organic Compounds

During Lassaigne's test, the elements present in an organic compound are converted from :

- (1) Ionic form to ionic form
- **(2)** Covalent form to ionic form
- (3) Covalent form to covalent form
- (4) Ionic form to covalent form

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. During Lassaigne's test, the element present in an organic compound are converted from covalent form to ionic form.

**Solved independently** (answer withheld)

1. In an organic compound nitrogen, sulphur and the halogens are held by covalent bonds, so they give no ionic tests in water.
2. Lassaigne's test fuses the compound with sodium metal: $\mathrm{Na} + \mathrm{C} + \mathrm{N} \to \mathrm{NaCN}$, $2\mathrm{Na} + \mathrm{S} \to \mathrm{Na_2S}$, $\mathrm{Na} + \mathrm{X} \to \mathrm{NaX}$.
3. These sodium salts are ionic and dissolve in water to give $\mathrm{CN^-}$, $\mathrm{S^{2-}}$ and $\mathrm{X^-}$, which the usual precipitation tests detect.
4. So the conversion is from covalent form to ionic form, option $2$.

**Subtopic:** Detection of Elements · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q072_304bda4f_30102026.png?v=304bda4ff4ab)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q072_4748b230_30102026.png?v=4748b230f808)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Fusion with sodium in Lassaigne's test breaks the covalent bonds holding nitrogen, sulphur and halogen. It leaves them as sodium salts. So they can then be tested for as ions in water.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Most students pick option 3. Its first half is the fact the whole chapter rests on: in an organic compound these elements are covalently bonded. A student who answers from that alone keeps 'covalent' on both sides of the arrow. That misses the point of the sodium fusion. The fusion makes $\mathrm{NaCN}$, $\mathrm{Na_2S}$ and $\mathrm{NaX}$, which are ionic. Only ions can be precipitated from the water extract.
- **Why:** You have to say what the sodium-fusion step of a named test does to the elements. The question says 'During Lassaigne's test, the elements present in an organic compound are converted from :' and each option pairs a starting form with a final form.
<!--/ecat-->

## Q73

Chemistry · physical · Electrochemistry

A solution of copper sulphate is electrolysed for 10 minutes with a current of 1.5 amperes. The mass of copper deposited at cathode is :
(Given : Molar mass of $\mathrm{Cu} = 63\,\mathrm{g\,mol^{-1}}$;
$1\,\mathrm{F} = 96487\,\mathrm{C\,mol^{-1}}$)

- (1) $1.7018\,\mathrm{g}$
- **(2)** $0.2938\,\mathrm{g}$
- (3) $2.4036\,\mathrm{g}$
- (4) $0.5876\,\mathrm{g}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{CuSO_4} \longrightarrow \mathrm{Cu^{2+}} + \mathrm{SO_4^{2-}}$
2. $2\mathrm{e^{-}} + \mathrm{Cu^{2+}} \longrightarrow \mathrm{Cu(s)}$
3. $\mathrm{W} = \mathrm{zit}$
4. $= \frac{\mathrm{E} \times \mathrm{i}\,\mathrm{t}}{96500}$
5. $= \frac{63 \times 1.5 \times 10 \times 60}{2 \times 96500}$
6. $= \frac{56{,}700}{193000} = 0.2938\ \mathrm{g}$

**Solved independently** (answer withheld)

1. Charge passed $Q = I t = 1.5 \times (10 \times 60) = 900\ \mathrm{C}$.
2. The cathode reaction is $\mathrm{Cu^{2+}} + 2e^{-} \to \mathrm{Cu}$, so $2\ \mathrm{F}$ deposits one mole of copper.
3. Moles of copper $= \dfrac{900}{2 \times 96487} = 4.664 \times 10^{-3}\ \mathrm{mol}$.
4. Mass $= 4.664 \times 10^{-3} \times 63 = 0.2938\ \mathrm{g}$, which is option $2$.

**Subtopic:** Faraday's Laws of Electrolysis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q073_2b544ba9_30102026.png?v=2b544ba9a520)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q073_e7124772_30102026.png?v=e712477212c2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Faraday's first law says the mass deposited is $\dfrac{M}{nF} \times It$. Here $n$ is the number of electrons needed per ion.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Most students pick option 4. $It = 1.5 \times 600 = 900\,\mathrm{C}$. Copper is deposited from $\mathrm{Cu^{2+}}$, so that charge buys $900/(2 \times 96487)$ mol of metal, which is $0.2938\,\mathrm{g}$. Put the molar mass $63$ into $M It / F$ without dividing by the two electrons and you get exactly twice that. That is the $0.5876\,\mathrm{g}$ of option 4.
- **Why:** You have to turn charge into moles of electrons and then into a mass of metal. The question says the solution is 'electrolysed for 10 minutes with a current of 1.5 amperes', and it supplies the molar mass of Cu and the value of 1 F.
<!--/ecat-->

## Q74

Chemistry · physical · Thermodynamics

At a certain temperature, $\mathrm{T\,(K)}$, during a process, $500\,\mathrm{J}$ is absorbed by the system and work of $200\,\mathrm{J}$ is done by the system. Then change in internal energy of the system is :

- (1) $400\,\mathrm{J}$
- **(2)** $300\,\mathrm{J}$
- (3) $700\,\mathrm{J}$
- (4) $500\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. From first law of thermodynamics
2. $\Delta \mathrm{U} = \mathrm{q} + \mathrm{w}$
3. $\mathrm{q} = +500\ \mathrm{J}$
4. $\mathrm{w} = -200\ \mathrm{J}$
5. $\Delta \mathrm{U} = 500 - 200$
6. $= 300\ \mathrm{J}$

**Solved independently** (answer withheld)

1. The first law of thermodynamics gives $\Delta U = q + w$.
2. Heat absorbed by the system is taken positive, so $q = +500\ \mathrm{J}$.
3. Work done by the system leaves it, so in this sign convention $w = -200\ \mathrm{J}$.
4. $\Delta U = 500 + (-200) = +300\ \mathrm{J}$, which is option $2$.

**Subtopic:** Internal Energy and First Law of Thermodynamics · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 35)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q074_5b5d4b8a_30102026.png?v=5b5d4b8a41e7)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q074_d6c26ab0_30102026.png?v=d6c26ab006d3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The first law is $\Delta U = q + w$, and the signs matter. Work done by the system goes in as a negative $w$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. They write $\Delta U = q + w$ and drop the printed $200\,\mathrm{J}$ in as positive, which gives $500 + 200 = 700\,\mathrm{J}$. But the question says the work is done by the system. So that energy leaves the system. Then $w = -200\,\mathrm{J}$ and the internal energy rises by only $300\,\mathrm{J}$.
- **Why:** You have to apply the first law and respect the direction of each energy transfer. The question says '500 J is absorbed by the system and work of 200 J is done by the system'.
<!--/ecat-->

## Q75

Chemistry · physical · Chemical Kinetics

For a certain reaction $\mathrm{R} \rightarrow$ Product, the plot of concentration $[\mathrm{R}]$ vs time has a negative slope as shown. The order of reaction is :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q075_52292301_30102026.png?v=522923014952)

- **(1)** $0$
- (2) $1$
- (3) $2$
- (4) $2.5$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For zero order
2. $[\mathrm{R}] = [\mathrm{R_0}] - \mathrm{kt}$
3. So $-$ve slope shows zero order reaction

**Solved independently** (answer withheld)

1. The plot shows the concentration $[\mathrm{R}]$ itself, not $\ln[\mathrm{R}]$ or $1/[\mathrm{R}]$, falling as a straight line against time.
2. Integrating the rate law for order $n$: only $n=0$ gives $[\mathrm{R}] = [\mathrm{R_0}] - kt$, linear in $[\mathrm{R}]$ versus $t$.
3. First order would be linear only in $\ln[\mathrm{R}]$ versus $t$, and second order only in $1/[\mathrm{R}]$ versus $t$.
4. The figure also labels $k = -\mathrm{slope}$ with intercept $[\mathrm{R_0}]$, matching $[\mathrm{R}] = [\mathrm{R_0}] - kt$ exactly, so the order is $0$, option $1$.

**Subtopic:** Zero Order Reactions · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 35)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q075_1d6cdde4_30102026.png?v=1d6cdde42d3c)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q075_493fb75c_30102026.png?v=493fb75ca9ab)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Only a zero-order reaction gives a straight line when you plot $[\mathrm{R}]$ itself against time. The slope is then $-k$ all the way.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. The straight line with a negative slope that students draw most often in kinetics is the first-order one, $\ln[\mathrm{R}] = \ln[\mathrm{R}]_0 - kt$. So 'straight line, negative slope' comes back as 'first order'. But that line needs $\ln[\mathrm{R}]$ on the vertical axis. This plot has $[\mathrm{R}]$ itself, and a first-order decay drawn that way is a curve whose slope keeps changing.
- **Why:** You have to read an order off the shape of a printed plot. The question says 'the plot of concentration [R] vs time has a negative slope as shown. The order of reaction is :'.
<!--/ecat-->

## Q76

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Identify the correct statement about $\mathrm{ClF_3}$ from the following options :

- **(1)** It has T-shaped geometry with two lone pairs on Cl atom.
- (2) It has T-shaped geometry with three lone pairs on Cl atom.
- (3) It has a trigonal pyramidal geometry with two lone pairs on Cl atom.
- (4) It has a planar trigonal geometry with two lone pairs on Cl atom.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{ClF_3}$ has two lone pairs of electrons on Cl atom with bent T-shape structure (geometry)

**Solved independently** (answer withheld)

1. Chlorine has $7$ valence electrons; three of them form $\mathrm{Cl-F}$ bonds, leaving $4$ electrons as $2$ lone pairs.
2. Total electron pairs around Cl $= 3 + 2 = 5$, so the electron geometry is trigonal bipyramidal with $sp^3d$ hybridisation.
3. The two lone pairs occupy equatorial positions (less repulsion), leaving three fluorines in a T arrangement.
4. So $\mathrm{ClF_3}$ is T-shaped with two lone pairs on chlorine, option $1$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q076_49f85e8b_30102026.png?v=49f85e8bc833)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q076_47f4260a_30102026.png?v=47f4260af279)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Use VSEPR on $\mathrm{ClF_3}$. Three bond pairs and two lone pairs make five pairs in a trigonal bipyramid. The lone pairs take the equatorial sites. So the molecule is T-shaped.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. The shape is the half students hold safely, and option 2 prints it correctly as T-shaped. Because that half is right, the rest of the sentence looks right too. But three lone pairs belongs to linear $\mathrm{XeF_2}$ from the same table. Chlorine has seven valence electrons, three go into bonding, and four are left over. Four electrons are two lone pairs.
- **Why:** You have to count bond pairs and lone pairs on one species and read them as a shape. The question says 'Identify the correct statement about $\mathrm{ClF_3}$' and each option joins a geometry to a lone-pair count.
<!--/ecat-->

## Q77

Chemistry · inorganic · Principles Related to Practical Chemistry

In a test tube containing a salt, a few drops of dilute $\mathrm{H_2SO_4}$ was added, which gave colourless vapours having the smell of vinegar. The vapours turned the blue litmus paper red.
Identify the correct anion from the following :

- (1) Sulphide, $\mathrm{S^{2-}}$
- (2) Sulphate, $\mathrm{SO_4^{2-}}$
- **(3)** Acetate, $\mathrm{CH_3COO^-}$
- (4) Carbonate, $\mathrm{CO_3^{2-}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Salt $+$ dil. $\mathrm{H_2SO_4} \longrightarrow \mathrm{CH_3COOH(Cl)} \longrightarrow$ Acidic in Nature
2. It turns Blue litmus paper in red
3. So, correct Answer is : Acetate, $\mathrm{CH_3COO^{-}}$

**Solved independently** (answer withheld)

1. Dilute $\mathrm{H_2SO_4}$ displaces the weaker acid from its salt, and the smell of vinegar is the smell of acetic acid.
2. Sulphide would give $\mathrm{H_2S}$, which smells of rotten eggs, not vinegar.
3. Carbonate would give $\mathrm{CO_2}$, a colourless but odourless gas.
4. Sulphate gives no gas at all with dilute $\mathrm{H_2SO_4}$.
5. Acetate gives $\mathrm{CH_3COOH}$ vapour, which smells of vinegar and turns blue litmus red, so the anion is acetate, option $3$.

**Subtopic:** Test for Anions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q077_a3a8e118_30102026.png?v=a3a8e118710f)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q077_22d7e51c_30102026.png?v=22d7e51cc189)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** You identify an anion with dilute acid, and the smell of the gas tells them apart. Acetate smells of vinegar. Carbonate has no smell. Sulphide smells of rotten eggs.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Most students pick option 4. Carbonate with dilute $\mathrm{H_2SO_4}$ gives colourless vapours that turn moist blue litmus red. So it fits every observation in the question except one. Drop the words 'the smell of vinegar' and option 4 is a correct answer. Keep them and it fails, because $\mathrm{CO_2}$ has no smell.
- **Why:** You have to name an anion from what is seen and smelt at the bench. The question says there are 'colourless vapours having the smell of vinegar' which 'turned the blue litmus paper red'.
<!--/ecat-->

## Q78

Chemistry · physical · Ionic Equilibrium

At $298\,\mathrm{K}$, a certain buffer solution contains equal concentrations of $\mathrm{X^-}$ and $\mathrm{HX}$, $\mathrm{K_b}$ for $\mathrm{X^-}$ is $10^{-10}$. What is the pH of this buffer solution?

- (1) $2$
- **(2)** $4$
- (3) $6$
- (4) $10$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{HX} \rightleftharpoons \mathrm{H^{+}} + \mathrm{X^{-}}$
2. $\mathrm{K_a} \times \mathrm{K_b} = \mathrm{K_w}$
3. $\mathrm{K_a} = \frac{\mathrm{K_w}}{\mathrm{K_b}} = \frac{10^{-14}}{10^{-10}} = 10^{-4}$
4. $\mathrm{pH} = \mathrm{pK_a} + \log\frac{[\mathrm{X^{-}}]}{[\mathrm{HX}]}$
5. Given that : $[\mathrm{X^{-}}] = [\mathrm{HX}]$
6. $= 4 + \log(1)$
7. $= 4 + 0$
8. $= 4$

**Solved independently** (answer withheld)

1. For a conjugate acid-base pair, $K_a \times K_b = K_w = 10^{-14}$ at $298\ \mathrm{K}$.
2. $K_a(\mathrm{HX}) = \dfrac{10^{-14}}{10^{-10}} = 10^{-4}$, so $\mathrm{p}K_a = 4$.
3. Henderson-Hasselbalch: $\mathrm{pH} = \mathrm{p}K_a + \log\dfrac{[\mathrm{X^-}]}{[\mathrm{HX}]}$.
4. The concentrations are equal, so $\log 1 = 0$ and $\mathrm{pH} = \mathrm{p}K_a = 4$, which is option $2$.

**Subtopic:** Buffer Solutions, Relation Between Ka and Kb · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q078_b43d10b8_30102026.png?v=b43d10b8b587)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q078_caa95eb1_30102026.png?v=caa95eb176cc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a conjugate acid-base pair, $K_a K_b = K_w$. So an equimolar buffer sits at $\mathrm{pH} = \mathrm{p}K_a = 14 - \mathrm{p}K_b$.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Most students pick option 4. With equal concentrations the Henderson equation becomes $\mathrm{pH} = \mathrm{p}K_a$. Feed the printed $10^{-10}$ straight into that and you read off $\mathrm{pH} = 10$. But the printed constant is $K_b$ for $\mathrm{X^-}$, so $10$ is the pOH. $K_a$ for $\mathrm{HX}$ is $10^{-14}/10^{-10} = 10^{-4}$, and the pH is $4$.
- **Why:** You have to turn $K_b$ into $K_a$ before you use the buffer equation. The question gives 'equal concentrations of $\mathrm{X^-}$ and $\mathrm{HX}$' and '$K_b$ for $\mathrm{X^-}$ is $10^{-10}$'.
<!--/ecat-->

## Q79

Chemistry · physical · Electrochemistry

> ⚠ The independent solve chose (1); the booklet prints (4).

Calculate emf of the half cell given below :
$\mathrm{Pt\,(s)\,|\,H_2(g,\,2\,atm)\,|\,HCl\,(aq,\,0.02\,M)}$
$E^{\circ}_{\mathrm{H_2/H^+}} = 0\,\mathrm{V}$
(Given: $\dfrac{2.303\,\mathrm{RT}}{\mathrm{F}} = 0.059$, $\log 2 = 0.3010$)

- (1) $-0.109\,\mathrm{V}$
- (2) $0.035\,\mathrm{V}$
- (3) $-0.035\,\mathrm{V}$
- **(4)** $0.109\,\mathrm{V}$

**Answer** — booklet: (4) · independent solve: (1) · differs

**Publisher's solution**

1. $\mathrm{H_2(g)} \longrightarrow 2\mathrm{H}^{\oplus}\mathrm{(aq)} + 2\mathrm{e}^{\ominus}$
2. $\because \mathrm{E} = \mathrm{E^{o}} - \frac{2.303\mathrm{RT}}{\mathrm{nF}}\log\frac{[\mathrm{H^{+}}]^{2}}{\mathrm{P_{H_2}}}$
3. $[\mathrm{H^{+}}] = 0.02\ \mathrm{M}$ (from HCl )
4. $\mathrm{P_{H_2}} = 2\ \mathrm{atm}$
5. $\frac{2.303\mathrm{RT}}{\mathrm{F}} = 0.059$
6. $\mathrm{E} = 0 - \frac{0.059}{2}\log\frac{(0.02)^{2}}{2}$
7. $= -0.0295\log\left(\frac{0.0004}{2}\right)$
8. $\mathrm{E} = -0.0295\log(2 \times 10^{-4})$
9. $= -0.0295(\log 2 + \log 10^{-4})$
10. $= -0.0295\,[0.301 - 4] = 0.109\ \mathrm{V}$

**Solved independently** (answer withheld)

1. The half-cell reaction written as a reduction is $2\mathrm{H^+} + 2e^{-} \to \mathrm{H_2}$, so $n = 2$.
2. Nernst equation: $E = E^{\circ} - \dfrac{0.059}{2}\log\dfrac{p_{\mathrm{H_2}}}{[\mathrm{H^+}]^2}$ with $E^{\circ} = 0$.
3. HCl is a strong acid, so $[\mathrm{H^+}] = 0.02\ \mathrm{M}$ and $[\mathrm{H^+}]^2 = 4 \times 10^{-4}$.
4. $\dfrac{p_{\mathrm{H_2}}}{[\mathrm{H^+}]^2} = \dfrac{2}{4 \times 10^{-4}} = 5 \times 10^{3}$.
5. $\log(5 \times 10^{3}) = 3 + \log 5 = 3 + (1 - 0.3010) = 3.699$.
6. $E = -0.0295 \times 3.699 = -0.109\ \mathrm{V}$, which is option $1$.

**Subtopic:** Nernst Equation · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 37)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q079_8f8f2206_30102026.png?v=8f8f2206b5f6)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q079_49393378_30102026.png?v=49393378280b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The Nernst equation for the hydrogen electrode is $E = -\dfrac{0.059}{2}\log\dfrac{p_{\mathrm{H_2}}}{[\mathrm{H^+}]^2}$. An electrode potential is always quoted for the reduction.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. The log term is $\log\dfrac{2}{(0.02)^2} = 3.699$, and $0.0295 \times 3.699 = 0.109\,\mathrm{V}$. So the size of the answer is already fixed. Only the sign is left to decide. The cell as drawn shows hydrogen being oxidised from left to right, so you quote $+0.109\,\mathrm{V}$. But an electrode potential is quoted for the reduction. That makes it $-0.109\,\mathrm{V}$.
- **Why:** You have to use the Nernst equation on one electrode where neither the pressure nor the concentration is standard. The question prints '$\mathrm{H_2(g,\,2\,atm)}$', '$\mathrm{HCl\,(aq,\,0.02\,M)}$' and '$2.303\mathrm{RT}/\mathrm{F} = 0.059$'.
<!--/ecat-->

## Q80

Chemistry · inorganic · The D- and F-Block Elements – Practice

The calculated 'spin-only' magnetic moment $\mathrm{Ti^{2+}}$ $(3d^{2})$ is :

- (1) $5.92\,\mathrm{BM}$
- (2) $3.87\,\mathrm{BM}$
- **(3)** $2.84\,\mathrm{BM}$
- (4) $4.90\,\mathrm{BM}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Spin only magnetic moment $\mu = \sqrt{\mathrm{n}(\mathrm{n} + 2)}\ \mathrm{B.M}$
2. n $=$ Number of unpaired $\mathrm{e^{-}(s)}$
3. Electronic configuration of $\mathrm{Ti^{2+}} \Rightarrow [\mathrm{Ar}]4s^{0}3d^{2}$
4. $\mu = \sqrt{2 \times 4}$
5. $= 2.84\ \mathrm{BM}$

**Solved independently** (answer withheld)

1. $\mathrm{Ti^{2+}}$ has the configuration $3d^2$, and by Hund's rule the two electrons occupy separate $d$ orbitals, so $n = 2$ unpaired electrons.
2. Spin-only formula: $\mu = \sqrt{n(n+2)}\ \mathrm{BM}$.
3. $\mu = \sqrt{2(2+2)} = \sqrt{8} = 2.83\ \mathrm{BM}$, which matches option $3$.

**Subtopic:** Magnetic Properties · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 37)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q080_c589e3ff_30102026.png?v=c589e3ffea3f)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q080_04a66b05_30102026.png?v=04a66b05e296)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spin-only magnetic moment is $\mu = \sqrt{n(n+2)}$ BM, where $n$ is the number of unpaired electrons.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  There is no trap here. The question hands you the configuration, '$\mathrm{Ti^{2+}}$ $(3d^{2})$', so $n = 2$ is not in doubt and $\sqrt{8} = 2.84$. The other three options are just the next rows of the same table. $3.87$ is $\sqrt{15}$ for $n = 3$, $4.90$ is $\sqrt{24}$ for $n = 4$ and $5.92$ is $\sqrt{35}$ for $n = 5$. Nothing printed in the question gives you three, four or five unpaired electrons.
- **Why:** You have to put one number through the spin-only formula. The question says 'The calculated spin-only magnetic moment $\mathrm{Ti^{2+}}$ $(3d^{2})$ is :' and it gives you the configuration.
<!--/ecat-->

## Q81

Chemistry · inorganic · The p–Block Elements

Identify the incorrect statement from the following:

- (1) Carbon has the ability to form $p\pi\text{-}p\pi$ multiple bond with itself.
- (2) $\mathrm{ECl_3}$ ($\mathrm{E = B}$ and $\mathrm{Al}$) is a monomer when $\mathrm{E = B}$ and a dimer when $\mathrm{E = Al}$.
- (3) The order of catenation property of Group 14 elements is $\mathrm{C} \gg \mathrm{Si} > \mathrm{Ge} \approx \mathrm{Sn}$.
- **(4)** Oxygen exhibits only $-2$ oxidation state.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. (1) C can form $p\pi\text{-}p\pi$ multiple bond with itself.
2. It is observed when it forms $\mathrm{C} = \mathrm{C}$ and $\mathrm{C} \equiv \mathrm{C}$
3. (2) $\mathrm{ECl_3}$ ($\mathrm{E} = \mathrm{B}$ and $\mathrm{Al}$)
4. $\mathrm{BCl_3}$ does not form dimer.
5. $\mathrm{AlCl_3}$ can form dimer in $\mathrm{Al_2Cl_6}$.
6. (3) Catenation property of group 14 $\mathrm{C} \gg \mathrm{Si} > \mathrm{Ge} \approx \mathrm{Sn}$.
7. (4) Oxygen exhibits oxidation state of $0$ in $\mathrm{O_2}$, $-2$ in oxides, $-1$ in peroxides. So this statement is incorrect.

**Solved independently** (answer withheld)

1. Statement 1 is correct: carbon's small size allows effective $2p$-$2p$ sideways overlap, giving $p\pi\text{-}p\pi$ bonds as in $\mathrm{C}{=}\mathrm{C}$ and $\mathrm{C}\equiv\mathrm{C}$.
2. Statement 2 is correct: $\mathrm{BCl_3}$ stays monomeric because boron is too small to expand its coordination, while $\mathrm{AlCl_3}$ dimerises to $\mathrm{Al_2Cl_6}$ through chlorine bridges.
3. Statement 3 is correct: catenation falls down group 14 as the $\mathrm{E-E}$ bond enthalpy falls, giving $\mathrm{C} \gg \mathrm{Si} > \mathrm{Ge} \approx \mathrm{Sn}$, with lead showing practically none.
4. Statement 4 is wrong: oxygen shows $-1$ in peroxides such as $\mathrm{H_2O_2}$, $-\frac{1}{2}$ in superoxides such as $\mathrm{KO_2}$, $0$ in $\mathrm{O_2}$ and $+2$ in $\mathrm{OF_2}$, so $-2$ is not its only state.
5. The incorrect statement is option $4$.

**Subtopic:** General Properties & Trends of Group 16 (Oxygen Family) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 37)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q081_521dcc5a_30102026.png?v=521dcc5a6861)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q081_e873a20c_30102026.png?v=e873a20c1527)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Oxygen is not always $-2$. It is $-1$ in peroxides, and it is positive in $\mathrm{OF_2}$, because fluorine pulls electrons harder than oxygen does.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. You meet $\mathrm{BCl_3}$ and $\mathrm{AlCl_3}$ together as flat covalent chlorides and as Lewis acids. So you carry boron's single-molecule structure across to aluminium and mark option 2 as the false one. But aluminium completes its octet by bridging. $\mathrm{AlCl_3}$ really is the dimer $\mathrm{Al_2Cl_6}$. The statement that does fail is the word 'only' in option 4.
- **Why:** You have to check four stated facts about p-block elements one at a time, and the question wants the one that is wrong. It says 'Identify the incorrect statement from the following:' and every option is a full claim.
<!--/ecat-->

## Q82

Chemistry · inorganic · Chemical Bonding and Molecular Structure

The correct formal charges on oxygen atoms numbered 2, 1 and 3 respectively are :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q082_1d3d6271_30102026.png?v=1d3d62719260)

- (1) $-1,\ 0,\ +1$
- **(2)** $0,\ +1,\ -1$
- (3) $0,\ 0,\ 0$
- (4) $+1,\ 0,\ -1$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Formal charge $=$ Valence electrons (V) $- \frac{1}{2}$ (shared electrons) (S) $-$ (non-bonding electrons) (L)
2. Formal charge on $2^{\mathrm{nd}}$ oxygen atom $= 6 - \frac{1}{2}(4) - 4 = 0$
3. Formal charge on $1^{\mathrm{st}}$ oxygen atom $= 6 - \frac{1}{2}(6) - 2 = +1$
4. Formal charge on $3^{\mathrm{rd}}$ oxygen atom $= 6 - \frac{1}{2}(2) - 6 = -1$

**Solved independently** (answer withheld)

1. Formal charge $= (\text{valence electrons}) - (\text{lone pair electrons}) - \tfrac{1}{2}(\text{bonding electrons})$, and each oxygen has $6$ valence electrons.
2. Atom 2 is the doubly bonded terminal oxygen with two lone pairs: $\mathrm{FC} = 6 - 4 - \tfrac{1}{2}(4) = 0$.
3. Atom 1 is the central oxygen with one lone pair and three bonds (one double, one single): $\mathrm{FC} = 6 - 2 - \tfrac{1}{2}(6) = +1$.
4. Atom 3 is the singly bonded terminal oxygen with three lone pairs: $\mathrm{FC} = 6 - 6 - \tfrac{1}{2}(2) = -1$.
5. The charges sum to zero, as they must for neutral $\mathrm{O_3}$.
6. Taken in the asked order 2, 1, 3 the answer is $0,\ +1,\ -1$, which is option $2$.

**Subtopic:** Octet Rule · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 38)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q082_1416c789_30102026.png?v=1416c78962f3)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q082_13917c59_30102026.png?v=13917c59c439)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Formal charge on an atom is its valence electrons, minus its lone-pair electrons, minus half the electrons in its bonds. You read all three of those off the drawn structure.
- **Why:** You have to work out a formal charge for each of three labelled atoms and report them in the order asked. The question says 'The correct formal charges on oxygen atoms numbered 2, 1 and 3 respectively are :'.
- **Note:** The numbering sits on the figure, which is not in the stored text, so no trap is named. One thing in the question itself is still worth noticing. It asks for the charges in the order '2, 1 and 3', not 1, 2 and 3. And three of the four options are the same three values $-1$, $0$, $+1$ in different orders.
<!--/ecat-->

## Q83

Chemistry · inorganic · Principles Related to Practical Chemistry

> ⚠ The independent solve chose (3); the booklet prints (4).

Phenolphthalein is used as an indicator for the titration of sodium hydroxide solution against a standard solution of oxalic acid. The colour change that is observed at an alkaline pH close to the equivalence point during this titration is:

- (1) pinkish red to yellow
- (2) yellow to pinkish red
- (3) pink to colourless
- **(4)** colourless to pink

**Answer** — booklet: (4) · independent solve: (3) · differs

**Publisher's solution**

1. Colour of Phenolphthalein before the end point $=$ colourless.
2. Colour of Phenolphthalein close to equivalence point $=$ Pink.
3. $\therefore$ Colour change $=$ Colourless to pink.

**Solved independently** (answer withheld)

1. Phenolphthalein is colourless in acid and pink in alkali, its transition lying at about $\mathrm{pH}\ 8.3$ to $10$, which is why the change is seen at an alkaline pH near the equivalence point.
2. Here the sodium hydroxide is the solution being titrated, so it is the one in the conical flask with the indicator, and the standard oxalic acid is run in from the burette.
3. With alkali in the flask the indicator is pink at the start of the titration.
4. As the acid neutralises the alkali the pH falls through the transition range and the pink is discharged, so the end point is pink to colourless, option $3$.
5. Options 1 and 2 are wrong because phenolphthalein never shows yellow; that is methyl orange.

**Subtopic:** Titration · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 38)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q083_07b34700_30102026.png?v=07b3470038b4)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q083_70186c80_30102026.png?v=70186c80fcaa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Experiment** (`experiment`) — a procedure, its setup, or what its data show
- **Concept:** Phenolphthalein is colourless in acid and pink above about pH 8.3. The acid is in the flask here, so the end point is the first permanent pink.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. You read 'titration of sodium hydroxide solution against a standard solution of oxalic acid' as the alkali being in the flask. Then the indicator starts pink, and the end point becomes the moment the pink goes. But the indicator goes into the oxalic acid in the flask. The alkali is run in from the burette, and it takes the solution from colourless to pink.
- **Also:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Pinkish red to yellow' is the right colour change for this titration with the other indicator you know, methyl orange. Methyl orange is red in acid and yellow in alkali. But the question names phenolphthalein, and phenolphthalein has no yellow form at all.
- **Why:** You need the colour change of a named indicator at a named end point. The question says 'Phenolphthalein is used as an indicator' and asks for 'The colour change that is observed at an alkaline pH close to the equivalence point'.
<!--/ecat-->

## Q84

Chemistry · physical · Basic Concepts of Chemistry

When $1\,\mathrm{dm^3}$ of $\mathrm{CO_2}$ gas is passed over hot coke the volume of gaseous mixture after complete reaction at STP becomes $1.4\,\mathrm{dm^3}$. The composition of the gaseous mixture at STP is:

- (1) $0.8\,\mathrm{dm^3}$ of $\mathrm{CO}$, $0.8\,\mathrm{dm^3}$ of $\mathrm{CO_2}$
- **(2)** $0.8\,\mathrm{dm^3}$ of $\mathrm{CO}$, $0.6\,\mathrm{dm^3}$ of $\mathrm{CO_2}$
- (3) $0.6\,\mathrm{dm^3}$ of $\mathrm{CO}$, $0.8\,\mathrm{dm^3}$ of $\mathrm{CO_2}$
- (4) $0.6\,\mathrm{dm^3}$ of $\mathrm{CO}$, $0.4\,\mathrm{dm^3}$ of $\mathrm{CO_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{CO_2} + \mathrm{C(s)} \to 2\mathrm{CO}$
2. $1$
3. $1 - \mathrm{x} \qquad 2\mathrm{x}$
4. $1 - \mathrm{x} + 2\mathrm{x} = 1 + \mathrm{x} = 1.4$
5. $\mathrm{x} = 0.4\ \mathrm{dm^3}$
6. Volume of $\mathrm{CO_2} = 1 - 0.4 = 0.6\ \mathrm{dm^3}$
7. Volume of $\mathrm{CO} = 2 \times 0.4 = 0.8\ \mathrm{dm^3}$

**Solved independently** (answer withheld)

1. The reaction over hot coke is $\mathrm{CO_2(g)} + \mathrm{C(s)} \to 2\mathrm{CO(g)}$, and the carbon is a solid so only the gases count in the volumes.
2. Let $x\ \mathrm{dm^3}$ of $\mathrm{CO_2}$ react; by Avogadro's law it produces $2x\ \mathrm{dm^3}$ of CO and leaves $(1-x)\ \mathrm{dm^3}$ of $\mathrm{CO_2}$.
3. Total final volume $= (1-x) + 2x = 1 + x$.
4. $1 + x = 1.4$, so $x = 0.4\ \mathrm{dm^3}$.
5. CO formed $= 2 \times 0.4 = 0.8\ \mathrm{dm^3}$ and $\mathrm{CO_2}$ left $= 1 - 0.4 = 0.6\ \mathrm{dm^3}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q084_7076554b_30102026.png?v=7076554b4ccf)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q084_bf208f5a_30102026.png?v=bf208f5a1ebe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** $\mathrm{CO_2} + \mathrm{C} \rightarrow 2\mathrm{CO}$ turns one volume of gas into two. So the rise in the total volume tells you how much gas reacted.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. The two numbers in it are right, but they are put on the wrong gases. The volume grew by $0.4\,\mathrm{dm^3}$. So $0.4$ of the $\mathrm{CO_2}$ reacted and became $0.8\,\mathrm{dm^3}$ of CO, which leaves $0.6\,\mathrm{dm^3}$ of $\mathrm{CO_2}$. The gas that doubled has to be the bigger figure. Option 3 swaps them. And because $0.6 + 0.8$ still adds up to the printed $1.4$, the total gives you no warning.
- **Why:** You have to find how much reacted from a change in volume, then turn that into the two amounts left. The question says '1 dm$^3$ of $\mathrm{CO_2}$ gas is passed over hot coke' and 'the volume of gaseous mixture after complete reaction at STP becomes 1.4 dm$^3$'.
<!--/ecat-->

## Q85

Chemistry · organic · Amines

> ⚠ The independent solve chose (unsure); the booklet prints (3).

The major product Z formed in the following sequence of reactions is

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q085_b25a29cb_30102026.png?v=b25a29cbc8db)

- (1) $\mathrm{C_2H_5NO_2}$
- (2) $\mathrm{C_2H_5-N=N-OH}$
- **(3)** $\mathrm{C_2H_5OH}$
- (4) $\mathrm{C_2H_5NH_2}$

**Answer** — booklet: (3) · independent solve: (unsure) · ai_unsure

**Publisher's solution**

1. $\mathrm{C_2H_6} + \mathrm{Cl_2} \xrightarrow{\mathrm{UV}} \mathrm{C_2H_5Cl}\ (X) + \mathrm{HCl}$
2. $\mathrm{C_2H_5Cl}\ (X) \xrightarrow[-\mathrm{HCl}]{\mathrm{NH_3}} \mathrm{C_2H_5\,NH_2}\ (Y)$
3. $\mathrm{C_2H_5\,NH_2}\ (Y) \xrightarrow[\mathrm{HCl}]{\mathrm{NaNO_2}} [\mathrm{C_2H_5} + \overset{\oplus}{\mathrm{N}}_2\mathrm{Cl}^{-}]$
4. $[\mathrm{C_2H_5} + \overset{\oplus}{\mathrm{N}}_2\mathrm{Cl}^{-}] \xrightarrow{\mathrm{H_2O}} \mathrm{C_2H_5\,OH}\ (Z) + \mathrm{N_2} + \mathrm{HCl}$

**Solved independently** (answer withheld)

1. The stem says 'the following sequence of reactions' but no reaction scheme is present in the input (figure_image is null and there is no option image), so there is no starting material or set of reagents to reason from.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions) · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 39)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q085_09954d63_30102026.png?v=09954d632a6b)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q085_c5bf0662_30102026.png?v=c5bf0662ada8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Following a two-carbon chain through a sequence of reactions to see which group it ends up carrying: nitro, diazohydroxide, hydroxyl or amino.
- **Why:** You have to give the final product of a printed sequence. The question says 'The major product Z formed in the following sequence of reactions is'.
- **Note:** The sequence is not in the stored text. $\mathrm{C_2H_5NH_2}$, $\mathrm{C_2H_5OH}$ and $\mathrm{C_2H_5NO_2}$ are all on offer, and which one is Z depends entirely on which way the scheme runs. So no trap is named.
<!--/ecat-->

## Q86

Chemistry · physical · Chemical Kinetics

Given below is an expression for the rate constant of a first-order reaction occurring at a certain temperature, $\mathrm{T\,(K)}$.
$\ln k = 14.34 - \dfrac{1.25 \times 10^{4}}{\mathrm{T}}$
The energy of activation in $\mathrm{kcal\,mol^{-1}}$ for the reaction is :
(Given: $k$ in $\mathrm{s^{-1}}$, $\mathrm{R} = 1.987\,\mathrm{cal\,mol^{-1}\,K^{-1}}$)

- **(1)** $24.84$
- (2) $14.34$
- (3) $18.63$
- (4) $12.42$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. From Arrhenius equation
2. $\mathrm{k} = \mathrm{A}\,\mathrm{e}^{\frac{-\mathrm{E_a}}{\mathrm{RT}}}$
3. $\ln \mathrm{k} = \ln \mathrm{A} - \frac{\mathrm{E_a}}{\mathrm{RT}}$
4. $\frac{\mathrm{E_a}}{\mathrm{R}} = 1.25 \times 10^{4}$
5. $\mathrm{E_a} = 1.25 \times 10^{4} \times 1.987$
6. $= 24.84\ \mathrm{k\,cal\ mol^{-1}}$

**Solved independently** (answer withheld)

1. The Arrhenius equation in logarithmic form is $\ln k = \ln A - \dfrac{E_a}{RT}$.
2. Matching this with $\ln k = 14.34 - \dfrac{1.25 \times 10^{4}}{T}$ gives $\dfrac{E_a}{R} = 1.25 \times 10^{4}\ \mathrm{K}$.
3. $E_a = 1.25 \times 10^{4} \times 1.987 = 24837.5\ \mathrm{cal\,mol^{-1}}$.
4. Converting, $E_a = 24.84\ \mathrm{kcal\,mol^{-1}}$, which is option $1$.

**Subtopic:** Arrhenius Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 39)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q086_2d3f5f0c_30102026.png?v=2d3f5f0c7e86)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q086_fa51e551_30102026.png?v=fa51e5517779)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Match the printed straight line to $\ln k = \ln A - E_a/RT$. The number multiplying $1/T$ is $E_a/R$, and the number standing alone is $\ln A$.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Most students pick option 2. $14.34$ is the only number in the question that needs no work, and it sits right inside the equation the question is about. But $14.34$ is $\ln A$, the intercept, and it carries no units of energy. The activation energy comes from the other term: $E_a = 1.25 \times 10^{4} \times 1.987 = 24\,840\,\mathrm{cal\,mol^{-1}}$, which is $24.84\,\mathrm{kcal\,mol^{-1}}$.
- **Why:** You have to spot which part of the printed expression is $E_a/R$ and multiply it by R. The question prints '$\ln k = 14.34 - \dfrac{1.25 \times 10^{4}}{\mathrm{T}}$' and supplies 'R = 1.987 cal mol$^{-1}$ K$^{-1}$'.
<!--/ecat-->

## Q87

Chemistry · physical · Chemical Equilibrium

Given below are certain reactions. Identify the reaction for which $\mathrm{K_P} \neq \mathrm{K_C}$ .

- (1) $\mathrm{H_2O(g) + CO(g) \rightleftharpoons H_2(g) + CO_2(g)}$
- **(2)** $\mathrm{N_2\,(g) + 3H_2(g) \rightleftharpoons 2NH_3(g)}$
- (3) $\mathrm{H_2\,(g) + I_2(g) \rightleftharpoons 2HI(g)}$
- (4) $\mathrm{N_2\,(g) + O_2(g) \rightleftharpoons 2NO(g)}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{K_P} = \mathrm{K_C}(\mathrm{RT})^{\Delta \mathrm{n_g}}$
2. For $\mathrm{K_P} = \mathrm{K_C}$ $(\Delta \mathrm{n_g} = 0)$
3. $\mathrm{K_P} \neq \mathrm{K_C}$ $(\Delta \mathrm{n_g} \neq 0)$
4. (1) $\mathrm{H_2O(g)} + \mathrm{CO(g)} \rightleftharpoons \mathrm{H_2(g)} + \mathrm{CO_2(g)}$
5. $\Delta \mathrm{n_g} = 0$ $(\mathrm{K_P} = \mathrm{K_C})$
6. (2) $\mathrm{N_2\,(g)} + 3\mathrm{H_2(g)} \rightleftharpoons 2\mathrm{NH_3(g)}$
7. $\Delta \mathrm{n_g} = -2$ $(\mathrm{K_P} \neq \mathrm{K_C})$
8. (3) $\mathrm{H_2\,(g)} + \mathrm{I_2(g)} \rightleftharpoons 2\mathrm{HI(g)}$
9. $\Delta \mathrm{n_g} = 0$ $(\mathrm{K_P} = \mathrm{K_C})$
10. (4) $\mathrm{N_2\,(g)} + \mathrm{O_2(g)} \rightleftharpoons 2\mathrm{NO(g)}$
11. $\Delta \mathrm{n_g} = 0$ $(\mathrm{K_P} = \mathrm{K_C})$

**Solved independently** (answer withheld)

1. The relation between the two constants is $K_P = K_C (RT)^{\Delta n_g}$, so $K_P = K_C$ exactly when $\Delta n_g = 0$.
2. Option 1: $\mathrm{H_2O} + \mathrm{CO} \rightleftharpoons \mathrm{H_2} + \mathrm{CO_2}$ has $2$ moles of gas on each side, so $\Delta n_g = 0$.
3. Option 2: $\mathrm{N_2} + 3\mathrm{H_2} \rightleftharpoons 2\mathrm{NH_3}$ goes from $4$ moles to $2$ moles, so $\Delta n_g = -2 \neq 0$.
4. Option 3: $\mathrm{H_2} + \mathrm{I_2} \rightleftharpoons 2\mathrm{HI}$ has $2$ moles on each side, so $\Delta n_g = 0$.
5. Option 4: $\mathrm{N_2} + \mathrm{O_2} \rightleftharpoons 2\mathrm{NO}$ has $2$ moles on each side, so $\Delta n_g = 0$.
6. Only option $2$ has $K_P \neq K_C$.

**Subtopic:** Law of Chemical Equilibrium · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 40)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q087_099183ef_30102026.png?v=099183ef0791)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q087_5d2b007a_30102026.png?v=5d2b007a0a5d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** $K_P = K_C (RT)^{\Delta n_g}$. So the two are equal unless the number of moles of gas changes from one side of the equation to the other.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  There is no trap here. Counting the moles of gas on each side clears three options in one sweep. $\mathrm{H_2O + CO \rightleftharpoons H_2 + CO_2}$, $\mathrm{H_2 + I_2 \rightleftharpoons 2HI}$ and $\mathrm{N_2 + O_2 \rightleftharpoons 2NO}$ each go from two moles of gas to two moles of gas. So $\Delta n_g = 0$ and $K_P = K_C$ for every one of them. Nothing printed makes any one of those three look better than the other two.
- **Why:** You have to apply one rule to four printed equations. The question says 'Identify the reaction for which $\mathrm{K_P} \neq \mathrm{K_C}$' and the four options are four balanced equations.
<!--/ecat-->

## Q88

Chemistry · inorganic · Classification of Elements and Periodicity in Properties

Identify the incorrect statement from the following :

- **(1)** The largest and the smallest species among $\mathrm{Mg}$, $\mathrm{Mg^{2+}}$, $\mathrm{Al}$ and $\mathrm{Al^{3+}}$ are $\mathrm{Al}$ and $\mathrm{Mg^{2+}}$ respectively.
- (2) The IUPAC name of the element with atomic number 107 is Unnilseptium.
- (3) The similarity in behaviour of $\mathrm{Li}$ with $\mathrm{Mg}$ is referred to as 'diagonal relationship'
- (4) The oxidation state and covalency of $\mathrm{Al}$ in $[\mathrm{AlCl(H_2O)_5}]^{2+}$ are 3 and 6, respectively.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The largest species is $\mathrm{Mg}$ and the smallest one is $\mathrm{Al^{3+}}$ among $\mathrm{Mg}$, $\mathrm{Mg^{2+}}$, $\mathrm{Al}$ and $\mathrm{Al^{3+}}$.
2. Unnilseptium element has atomic number $107$
3. $\mathrm{Li}$ and $\mathrm{Mg}$ are diagonally related and have similar properties.
4. The oxidation state and covalency of $\mathrm{Al}$ in $[\mathrm{AlCl(H_2O)_5}]^{2+}$ are $+3$ and $6$ respectively
5. $\therefore$ Statement A is incorrect

**Solved independently** (answer withheld)

1. Across period 3 the nuclear charge rises while the shell stays the same, so the neutral atom shrinks: $\mathrm{Mg} > \mathrm{Al}$.
2. Both cations have the neon configuration, so the one with the higher nuclear charge is smaller: $\mathrm{Mg^{2+}} > \mathrm{Al^{3+}}$, and both are far smaller than the parent atoms.
3. The full order is $\mathrm{Mg} > \mathrm{Al} > \mathrm{Mg^{2+}} > \mathrm{Al^{3+}}$, so the largest is $\mathrm{Mg}$ and the smallest is $\mathrm{Al^{3+}}$; statement 1 names $\mathrm{Al}$ and $\mathrm{Mg^{2+}}$ and is therefore wrong.
4. Statement 2 is correct: $107$ gives un-nil-sept-ium, Unnilseptium, in the IUPAC systematic naming of elements above 100.
5. Statement 3 is correct: lithium resembles magnesium, the standard example of a diagonal relationship.
6. Statement 4 is correct: in $[\mathrm{AlCl(H_2O)_5}]^{2+}$ aluminium is in the $+3$ oxidation state and is bonded to six donor atoms, so its covalency is $6$.
7. The incorrect statement is option $1$.

**Subtopic:** Trends in Chemical Properties - Atomic and Ionic Radius · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 40)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q088_e21b556d_30102026.png?v=e21b556dc08a)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q088_d4178f75_30102026.png?v=d4178f75c195)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Across a period the atom gets smaller, and taking electrons away makes it smaller still. So among Mg, Al and their cations, neutral Mg is the largest and $\mathrm{Al^{3+}}$ is the smallest.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Most students pick option 4. You have just read aluminium's oxidation state off the formula as $+3$, and in $\mathrm{AlCl_3}$ the valency and the covalency are the same number. So you carry that three into the second half of the sentence and mark the '6' as the error. But covalency counts bonds, and $[\mathrm{AlCl(H_2O)_5}]^{2+}$ has six ligands around the aluminium. So that statement holds. The one that fails is option 1, where the largest species is Mg, not Al.
- **Why:** You have to check four stated facts about periodic trends one at a time, and the question wants the one that is wrong. It says 'Identify the incorrect statement from the following :' and every option is a full claim.
<!--/ecat-->

## Q89

Chemistry · physical · Solutions

Mixture of chloroform and acetone forms a solution with negative deviation from Raoult's law due to :

- (1) Increase in escaping tendency of molecules of each component.
- **(2)** Formation of hydrogen bonding between acetone and chloroform
- (3) Stronger intermolecular forces between chloroform molecules than those between chloroform and acetone molecules.
- (4) Repulsive forces.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Acetone and chloroform show negative deviation from Raoult's law due to stronger H-bonding between acetone and chloroform mixture.
2. Hence, escaping tendency decreases
3. $\therefore$ Vapour pressure decreases
4. $\therefore$ Boiling point increases.

**Solved independently** (answer withheld)

1. Negative deviation from Raoult's law means the observed vapour pressure is lower than predicted, which happens when the new A-B interaction is stronger than the original A-A and B-B interactions.
2. The three electronegative chlorines of $\mathrm{CHCl_3}$ leave its single hydrogen strongly positive, so it can hydrogen bond to the lone pair on the carbonyl oxygen of acetone.
3. This extra attraction holds the molecules in the liquid, lowering the escaping tendency and so the vapour pressure of both components, which is exactly negative deviation.
4. That is option $2$; option 1 describes positive deviation, and options 3 and 4 describe weaker A-B interaction, which would also give positive deviation.

**Subtopic:** Ideal and Nonideal Solutions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 41)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q089_bb0bf316_30102026.png?v=bb0bf31627e8)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q089_5d64a538_30102026.png?v=5d64a5387836)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A negative deviation from Raoult's law needs the A-B attraction to beat the A-A and B-B attractions. Acetone and chloroform manage that by hydrogen bonding.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. The test you carry is a comparison of A-B against A-A and B-B, and option 3 prints that comparison the wrong way round. Chloroform holding chloroform more tightly than it holds acetone is the condition for a positive deviation. A negative deviation needs the new acetone-chloroform hydrogen bond to be the strongest attraction in the mixture. That is what pulls the vapour pressure down.
- **Why:** You need the stated cause of one named deviation. The question says 'forms a solution with negative deviation from Raoult's law due to :' and each option offers a possible cause.
<!--/ecat-->

## Q90

Chemistry · organic · Hydrocarbons

> ⚠ The independent solve chose (unsure); the booklet prints (3).

The number of chlorine atoms present in the organic products X and Y of the following reactions, respectively, are :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q090_3e8154ea_30102026.png?v=3e8154ea6087)

- (1) 3 and 3
- (2) 6 and 3
- **(3)** 6 and 6
- (4) 3 and 6

**Answer** — booklet: (3) · independent solve: (unsure) · ai_unsure

**Solved independently** (answer withheld)

1. The stem refers to 'the following reactions' but no reaction scheme is present in the input (figure_image is null and option_images is empty), so there are no reactants or reagents from which the products X and Y could be derived.

**Subtopic:** Chemical and Physical Properties of Benzene · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 41)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q090_bb61636d_30102026.png?v=bb61636d986a)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q090_67768a79_30102026.png?v=67768a794bd6)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** How many chlorines each chlorination leaves in its organic product. Substitution and addition put different numbers of chlorines on the same skeleton.
- **Why:** You have to count the chlorines in the product of each of two printed reactions. The question says 'The number of chlorine atoms present in the organic products X and Y of the following reactions, respectively, are :'.
- **Note:** The two reactions are not in the stored text. The options offer only the counts 3 and 6 in the four possible orders, so which count belongs to X and which to Y cannot be settled here. No trap is named.
<!--/ecat-->

## Q91

Biology · botany · Morphology of Flowering Plants

In angiosperms, root hairs arise from which one of the following regions of the root?

- (1) The root cap zone
- (2) The region of meristematic activity
- (3) The region of elongation
- **(4)** The region of maturation

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. From the region of maturation, some epidermal cells form very fine and delicate, thread like structures called root hairs.

**Solved independently** (answer withheld)

1. The root tip has four zones in order: root cap, region of meristematic activity, region of elongation, region of maturation.
2. NCERT Class 11, Ch. 5 (Morphology of Flowering Plants) states that the cells of the region of maturation differentiate and some epidermal cells there form very fine, thread-like structures called root hairs.
3. Hence root hairs arise from the region of maturation, which is option $4$.

**Subtopic:** The Root · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 42)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q091_8a1a4871_30102026.png?v=8a1a487161e2)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q091_1dea0086_30102026.png?v=1dea0086c94a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Root hairs grow out of the epidermis in the region of maturation. By then the cells have stopped elongating and have differentiated.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3, the region of elongation. It is the zone just above the tip, and this is the zone the root's lengthening is named after. So if you store root hairs under 'where the young root is growing', you stop there. But root hairs grow out of cells that have already stopped elongating. That is the region of maturation.
- **Why:** You need one stated fact: which root zone carries root hairs. The four options are the four named zones of the root. The question prints no rule for you to apply.
<!--/ecat-->

## Q92

Biology · botany · Plant Kingdom

In which one of the following, the ovules are not enclosed by an ovary wall and remain exposed?

- (1) Funaria
- **(2)** Pinus
- (3) Selaginella
- (4) Wolffia

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The gymnosperms are plants in which the ovules are not enclosed by any ovary wall and remain exposed, both before and after fertilisation.
2. Pinus is a gymnosperm.
3. Funaria is a moss.
4. Selaginella is a pteridophyte.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 3 (Plant Kingdom) defines gymnosperms as plants in which the ovules are not enclosed by any ovary wall and remain exposed, both before and after fertilisation.
2. $Funaria$ is a moss (bryophyte) and $Selaginella$ a heterosporous pteridophyte, so neither bears ovules at all; $Wolffia$ is an angiosperm with ovules enclosed in an ovary.
3. $Pinus$ is the only gymnosperm listed, so option $2$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 42)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q092_d1c24446_30102026.png?v=d1c244469395)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q092_1fd49249_30102026.png?v=1fd49249d7cc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperms have naked ovules. No ovary wall covers them. Angiosperms keep their ovules inside an ovary.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Nothing here traps you. The question prints the gymnosperm condition, and only one option is a gymnosperm. Funaria is a moss and Selaginella is a pteridophyte. Neither of them forms an ovule at all, so you cannot even test the question's condition on them. Wolffia is a flowering plant, and a flowering plant always keeps its ovules inside an ovary.
- **Why:** You need one stated fact: which named plant has ovules that are not enclosed. The question prints 'the ovules are not enclosed by an ovary wall and remain exposed'. That is the gymnosperm condition.
<!--/ecat-->

## Q93

Biology · both · Molecular Basis of Inheritance

In the lac operon, the z gene codes for

- (1) permease
- (2) transacetylase
- **(3)** beta-galactosidase
- (4) the repressor of lac operon

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In lac operon,
2. i gene codes for - regulator protein
3. z gene codes for - beta-galactosidase
4. y gene codes for - Permease
5. a gene codes for - transacetylase

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 6 (Molecular Basis of Inheritance) states that in the $lac$ operon the gene $z$ codes for beta-galactosidase, which hydrolyses lactose into galactose and glucose.
2. The gene $y$ codes for permease and the gene $a$ for transacetylase; the repressor is coded by the separate $i$ gene.
3. Therefore $z \rightarrow$ beta-galactosidase, option $3$.

**Subtopic:** The Lac Operon · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 42)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q093_c47d2ace_30102026.png?v=c47d2ace4a7b)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q093_ac5a730a_30102026.png?v=ac5a730a78a0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The lac operon has three structural genes, and each one carries one enzyme. z carries beta-galactosidase, y carries permease, a carries transacetylase.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1, permease. Permease is what lets lactose into the cell, and that has to happen before any sugar can be split. So if you line up the operon's products in the order the steps happen, permease comes first. But the question asks about the z gene. Permease is the product of the y gene. The z gene carries beta-galactosidase.
- **Why:** You need one stated fact: which gene of the lac operon makes which enzyme. The question says 'the z gene codes for', and three options are products of that same operon.
<!--/ecat-->

## Q94

Biology · botany · Biodiversity and Conservation

Exploring molecular, genetic and species-level diversity for products of economic importance is called

- (1) Biofortification
- (2) Bioremediation
- **(3)** Bioprospecting
- (4) Biomagnification

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Exploring molecular, genetic and species - level diversity for products of economic importance is called as bioprospecting.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 15 (Biodiversity and Conservation) uses the term bioprospecting for exploring molecular, genetic and species-level diversity for products of economic importance.
2. Biofortification is breeding crops for higher nutrient content, bioremediation is using microbes to clean pollutants, and biomagnification is the increase in concentration of a toxicant at successive trophic levels.
3. Hence option $3$.

**Subtopic:** Biodiversity Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 42)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q094_bd6d7603_30102026.png?v=bd6d76037580)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q094_2d057fd2_30102026.png?v=2d057fd22662)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bioprospecting means searching through biodiversity for products worth selling. The search runs at the level of molecules, genes and species.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1, biofortification. It is the other 'bio-' term in the syllabus about making a crop product more valuable. So the words 'products of economic importance' in the question pull you to it. But biofortification means breeding crops to carry more nutrients. It is not a search through diversity that already exists for new products.
- **Why:** You need the stated meaning of one term. The question says 'Exploring molecular, genetic and species-level diversity for products of economic importance is called', and all four options start with the same prefix.
<!--/ecat-->

## Q95

Biology · both · Biotechnology: Principles and Processes

Match List I with List II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Genetically modified organism | (I) | Agrobacterium tumefaciens |
| B. | Thermostable DNA polymerase | (II) | Bt cotton |
| C. | Ti plasmid | (III) | Thermus aquaticus |
| D. | pBR322 | (IV) | Escherichia coli |

- **(1)** A-II, B-III, C-I, D-IV
- (2) A-II, B-I, C-IV, D-III
- (3) A-I, B-IV, C-III, D-II
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Genetically modified organism - Bt cotton
2. Thermostable DNA polymerase - Thermus aquaticus.
3. Ti plasmid - Agrobacterium tumefaciens
4. pBR322 - Escherichia coli

**Solved independently** (answer withheld)

1. A. Genetically modified organism: Bt cotton is NCERT's standard GMO example, so A-II.
2. B. Thermostable DNA polymerase (Taq polymerase) is isolated from the bacterium $Thermus\ aquaticus$, so B-III.
3. C. The Ti (tumour inducing) plasmid is carried by $Agrobacterium\ tumefaciens$, so C-I.
4. D. pBR322 is the cloning vector derived from $Escherichia\ coli$ plasmid, so D-IV.
5. A-II, B-III, C-I, D-IV matches option $1$.

**Subtopic:** Cloning Vectors, Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 43)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q095_1b1c4638_30102026.png?v=1b1c46386160)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q095_c5a00444_30102026.png?v=c5a00444a4b2)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each tool of recombinant DNA technology came from some organism. Ti plasmid comes from Agrobacterium. Thermostable polymerase comes from Thermus aquaticus. pBR322 comes from E. coli.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Thermostable DNA polymerase has to be Thermus aquaticus. The name itself tells you. Only one option pairs B with III, so that one step almost finishes the question. The pair you could really get wrong is which organism carries Ti plasmid and which carries pBR322. To fall for that you would need A-II, B-III, C-IV, D-I. No option prints that, so nothing really pulls you away.
- **Why:** You only have to know which organism each tool came from. List II is just four names, 'Agrobacterium tumefaciens', 'Thermus aquaticus', 'Escherichia coli'. There is no rule to work out. You either remember the source or you do not.
<!--/ecat-->

## Q96

Biology · botany · Ecosystem

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Productivity | I. | Gross primary productivity minus respiration losses |
| B. | Net primary productivity | II. | Rate of formation of new organic matter by consumers |
| C. | Gross primary productivity | III. | Rate of biomass production |
| D. | Secondary productivity | IV. | Rate of production of organic matter during photosynthesis |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-I, B-II, C-III, D-IV
- (3) A-I, B-III, C-IV, D-II
- (4) A-III, B-I, C-II, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Productivity is the rate of biomass production.
2. Net primary productivity is the Gross primary productivity (GPP) minus respiration losses (R).
3. Gross primary productivity is the rate of production of organic matter during photosynthesis.
4. Secondary productivity is the rate of formation of new organic matter by consumers.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 14 (Ecosystem) defines productivity as the rate of biomass production, so A-III.
2. Net primary productivity is gross primary productivity minus respiration losses ($NPP = GPP - R$), so B-I.
3. Gross primary productivity is the rate of production of organic matter during photosynthesis, so C-IV.
4. Secondary productivity is the rate of formation of new organic matter by consumers, so D-II.
5. A-III, B-I, C-IV, D-II matches option $1$.

**Subtopic:** Productivity · **Difficulty:** medium (4 steps)

**Printed in the booklet** (page 43)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q096_8af446f8_30102026.png?v=8af446f89791)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q096_ec8aebb1_30102026.png?v=ec8aebb157fe)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Productivity is the rate at which biomass is made. GPP is what photosynthesis makes. NPP is GPP minus respiration. Secondary productivity is what consumers make.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. You are taught that NPP is the biomass left over for consumers. So you remember NPP as 'the biomass one' and pair B with III. Then only 'Gross primary productivity minus respiration losses' is left for Productivity. NCERT has it the other way. Productivity itself is the rate of biomass production, and NPP is GPP minus respiration losses.
- **Why:** You have to match each productivity term with the definition NCERT prints for it. List II is made of those definitions, like 'Gross primary productivity minus respiration losses'.
<!--/ecat-->

## Q97

Biology · botany · Biodiversity and Conservation

Since the origin and diversification of life on Earth, there have been five episodes of mass extinction of species. How is the sixth extinction, which is in progress, different from the previous episodes?

- (1) The present net species extinction rate is zero.
- (2) The current species extinction rate is nearly 10 times faster than in previous episodes.
- **(3)** The present species extinction rates are 100 to 1000 times faster than in the pre-human times.
- (4) The current species extinction rates are far lower than those in previous episodes.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The current, sixth episode of mass extinction is estimated to be 100 to 1000 times faster than the ones in the pre-human times and our activities are responsible for the faster rates.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 15 (Biodiversity and Conservation) states that the present species extinction rates are estimated to be $100$ to $1{,}000$ times faster than in the pre-human times, and that human activities are responsible.
2. Options 1 and 4 contradict an extinction crisis being in progress, and the figure in option 2 ($10$ times) is not the textbook value.
3. Hence option $3$.

**Subtopic:** Loss of Biodiversity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 44)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q097_f9f15a05_30102026.png?v=f9f15a05a4d4)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q097_0710895f_30102026.png?v=0710895f01f8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The sixth extinction stands apart because of its speed. It runs at 100 to 1000 times the rate before humans.
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 2  
  Most students pick option 2. It keeps the one thing you are sure of, that extinction is faster now than before. It only shrinks the number to 'nearly 10 times'. If you remember which way the comparison goes but not how big it is, nothing in the question separates option 2 from the right answer. The source gives 100 to 1000 times.
- **Proposed:** `right_direction_wrong_magnitude` — the option restates the keyed comparison correctly in direction and understates its size, so the only thing separating it from the answer is a remembered magnitude. Nothing is computed, so arithmetic_slip does not reach it; nearby_fact needs a true fact about an adjacent thing, and no source states a tenfold figure for anything here.
- **Why:** You need the stated figure for how fast extinction is happening now. Option 3 gives '100 to 1000 times faster than in the pre-human times'. Option 2 gives a different multiplier for the same comparison.
<!--/ecat-->

## Q98

Biology · both · Biomolecules

Alpha-helix is found in which level of protein structure?

- **(1)** Secondary structure
- (2) Tertiary structure
- (3) Primary structure
- (4) Quaternary structure

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Alpha-helix is shown by secondary structure of protein as it has right handed helices.
2. Primary structure is linear and tertiary structure is a hollow ball-like structure. Quaternary structures are formed by more than one polypeptide chains.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 9 (Biomolecules) describes the primary structure as the linear sequence of amino acids in a polypeptide.
2. The secondary structure is the regular local conformation of the backbone; the textbook names the right-handed alpha-helix as this level of structure.
3. Tertiary structure is the overall three-dimensional folding and quaternary structure the arrangement of separate subunits, so option $1$.

**Subtopic:** Proteins And Structure Of Protein · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q098_3fcdfa07_30102026.png?v=3fcdfa074518)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q098_735d5c85_30102026.png?v=735d5c85013f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The alpha-helix is secondary structure. It is the regular local coil of the polypeptide backbone, before the chain folds up as a whole.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2, tertiary. A helix is a shape in three dimensions, so 'three-dimensional' makes you think of the tertiary level. But tertiary structure is the next step up, where the whole chain of helices and sheets folds into a globular shape. The helix itself sits one level below that.
- **Why:** You need the stated level of protein structure that the alpha-helix belongs to. The four options are the four named levels, primary to quaternary.
<!--/ecat-->

## Q99

Biology · botany · Anatomy of Flowering Plants

The main function of bulliform cells in grasses is :

- (1) to make the leaf impermeable to fungal spores.
- (2) to transport water.
- (3) to perform photosynthesis.
- **(4)** to minimize water loss during water stress.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Bulliform cells are large empty colourless cells that lose water and become flaccid in water scarce condition. Hence they curl the leaf inwards to minimise water loss by reducing the exposed surface area.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 6 (Anatomy of Flowering Plants) states that in grasses certain adaxial epidermal cells along the veins become large, empty, colourless bulliform cells.
2. The same passage states that when these cells are turgid the leaf surface is exposed, and when they are flaccid due to water stress they make the leaves curl inwards to minimise water loss.
3. They are neither conducting nor photosynthetic (they are colourless and empty), so option $4$.

**Subtopic:** Dicotyledonous and Monocotyledonous Leaf · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 44)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q099_3256e81f_30102026.png?v=3256e81f86d0)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q099_80ed8646_30102026.png?v=80ed864696be)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bulliform cells are the large empty epidermal cells of a grass leaf. When water is short they go flaccid, the leaf curls inward and it loses less water.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. Bulliform cells are described as large, empty, colourless cells lying along the veins. An empty cell sitting beside a vein sounds like part of the water pipework, so you picture them as a water channel. But they conduct nothing. What they do is lose turgor and roll the leaf up.
- **Why:** You need one stated fact: what a named leaf cell does. The question says 'The main function of bulliform cells in grasses is', and the four options are four possible functions.
<!--/ecat-->

## Q100

Biology · both · Biotechnology: Principles and Processes

Identify the correct sequence of steps in each cycle of Polymerase Chain Reaction :

- (1) Extension $\rightarrow$ Annealing $\rightarrow$ Denaturation
- (2) Annealing $\rightarrow$ Denaturation $\rightarrow$ Extension
- (3) Denaturation $\rightarrow$ Extension $\rightarrow$ Annealing
- **(4)** Denaturation $\rightarrow$ Annealing $\rightarrow$ Extension

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The correct sequence of steps in PCR is
2. Denaturation $\rightarrow$ Annealing $\rightarrow$ Extension

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 11 (Biotechnology: Principles and Processes) describes PCR as repeated cycles of denaturation, annealing of primers and extension.
2. Denaturation at about $94^{\circ}$C separates the two template strands; annealing lets the two oligonucleotide primers pair with the flanking regions; extension by thermostable Taq DNA polymerase then adds nucleotides.
3. The order denaturation $\rightarrow$ annealing $\rightarrow$ extension is option $4$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 44)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q100_18ea0a64_30102026.png?v=18ea0a649aa0)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q100_bfbf20c6_30102026.png?v=bfbf20c6533e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** One PCR cycle runs denaturation, then primer annealing, then extension by a thermostable polymerase.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. Heating to pull the two strands apart is the step you are sure of, so the real choice is only between the two steps that follow. If you picture the polymerase building the new strand first and the primers sitting on it afterwards, you put extension before annealing. But the primers have to bind first, because they are where the polymerase starts.
- **Why:** You need the order of the three steps in one cycle. The question says 'Identify the correct sequence of steps in each cycle', and all four options are orderings of the same three named steps.
- **Note:** Option 1 is the right order written backwards. Option 3 keeps the first step, the one you are sure of, and swaps only the last two.
<!--/ecat-->

## Q101

Biology · both · Cell Cycle and Cell Division

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | $G_1$ phase | I. | Actual cell division occurs |
| B. | S phase | II. | Cell is metabolically active and continuously grows but does not replicate its DNA |
| C. | $G_2$ Phase | III. | Synthesis of DNA occurs and the amount of DNA per cell doubles |
| D. | M phase | IV. | Proteins are synthesized while cell growth continues |

- (1) A-IV, B-I, C-II, D-III
- (2) A-I, B-II, C-III, D-IV
- (3) A-III, B-IV, C-I, D-II
- **(4)** A-II, B-III, C-IV, D-I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. During $\mathrm{G_1}$ phase the cell is metabolically active and continuously grows but does not replicate its DNA.
2. S-phase marks the phase during which DNA synthesis or replication takes place and amount of DNA per cell doubles.
3. During the $\mathrm{G_2}$ phase, proteins are synthesised in preparation for mitosis while cell growth continues.
4. During M phase the actual cell division takes place.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 10 (Cell Cycle and Cell Division) states that $G_1$ is the interval in which the cell is metabolically active and continuously grows but does not replicate its DNA, so A-II.
2. In S phase DNA synthesis occurs and the amount of DNA per cell doubles, so B-III.
3. In $G_2$ phase proteins are synthesised while cell growth continues, so C-IV.
4. M phase is when the actual cell division occurs, so D-I.
5. A-II, B-III, C-IV, D-I matches option $4$.

**Subtopic:** Phases of Cell Cycle · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 45)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q101_df8d9c27_30102026.png?v=df8d9c27f63e)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q101_025cabd7_30102026.png?v=025cabd7db56)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Interphase has three parts. G1 is growth. S phase is where DNA doubles. G2 is protein synthesis. The cell actually divides only in M phase.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Entry III says the amount of DNA per cell doubles. That can only be S phase. Only one option pairs B with III. The real confusion is between the two growth phases, G1's line II against G2's line IV. To fall for that you would need A-IV, B-III, C-II, D-I. No option prints it. The one option that does swap those two also moves DNA doubling to M phase, which you would catch.
- **Why:** You have to know which event NCERT gives to each phase. List II is made of those lines, like 'Synthesis of DNA occurs and the amount of DNA per cell doubles'.
<!--/ecat-->

## Q102

Biology · botany · Biodiversity and Conservation

Which of the following statements are correct?

Choose the correct answer from the options given below:

- **(A.)** The Amazon rainforest being cut and cleared for cultivation of soyabeans is an example of habitat loss.
- **(B.)** Steller's sea cow and passenger pigeon became extinct due to over-exploitation by humans.
- **(C.)** The Nile perch introduced into Lake Victoria in East Africa helped in population growth of cichlid fish in the lake.
- **(D.)** Water hyacinth is an invasive species.
- **(E.)** When a species becomes extinct, the plant and animal species associated with it are not affected.

- (1) A, B and E only
- **(2)** A, B and D only
- (3) C, D and E only
- (4) B, C and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The Nile Perch introduced into Lake Victoria in East Africa led eventually to extinction of an ecologically unique assemblage of more than 200 species of cichlid fish in the lake.
2. When a species become extinct, the plant and animal species associated with it in an obligatory way also become, extinct.
3. Statements, A, B and D are correct.

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 12, Ch. 15 cites the Amazon rain forest being cut and cleared for cultivation of soya beans as habitat loss and fragmentation.
2. B is correct: the same chapter lists Steller's sea cow and the passenger pigeon among species driven to extinction by over-exploitation by humans.
3. C is incorrect: NCERT states the Nile perch introduced into Lake Victoria led to the extinction of an ecologically unique assemblage of more than $200$ species of cichlid fish, not their population growth.
4. D is correct: water hyacinth ($Eichhornia\ crassipes$) is NCERT's standard invasive alien species.
5. E is incorrect: NCERT describes co-extinctions, where the extinction of one species causes the extinction of associated plant and animal species.
6. So A, B and D only, option $2$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** medium (5 steps)

**Printed in the booklet** (page 45)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q102_f7d0640b_30102026.png?v=f7d0640bdbb3)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q102_acdaf044_30102026.png?v=acdaf04460a4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** There are four causes of biodiversity loss, and NCERT gives an example of each. Habitat loss in the Amazon. Over-exploitation of Steller's sea cow. The Nile perch invading Lake Victoria. And co-extinction.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Most students pick option 1. Statement E begins with the co-extinction idea the chapter teaches. Then it puts a 'not' near the end and flips the meaning. You recognise the topic from the first half and mark it correct. To fit it in you have to drop the water hyacinth statement. NCERT says the opposite. When a species goes extinct, the plant and animal species tied to it go extinct too.
- **Why:** You have to judge five printed statements against the lines NCERT gives for the causes of biodiversity loss. The stem asks 'Which of the following statements are correct?' above a block of five lettered lines.
- **Note:** Statement C does the same thing the other way round. The Nile perch is the invasive species NCERT names. But it drove the cichlids to extinction. It did not help their population grow.
<!--/ecat-->

## Q103

Biology · both · Molecular Basis of Inheritance

Which of the following statements are correct with reference to a transcription unit?

Choose the correct answer from the options given below:

- **(A.)** A transcription unit in DNA is defined primarily by three regions : promoter, structural gene and terminator.
- **(B.)** The promoter is said to be located towards the $5'$-end of the structural gene.
- **(C.)** The promoter is a DNA sequence that provides binding site for RNA polymerase.
- **(D.)** The promoter defines the template and coding strands.
- **(E.)** The terminator is located towards the $3'$-end of the coding strand and it defines the end of the process of transcription.

- (1) A, B, C and D only
- (2) A, C, D and E only
- (3) B, C, D and E only
- **(4)** A, B, C , D and E

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The promoter and terminator flank the structural gene in a transcription unit.
2. The promoter is said to be located towards $5'$-end of the structural gene.
3. It is a DNA sequence that provides binding site for RNA polymerase and it is the presence of promoter in a transcription unit that also defines the template and coding strands.
4. The terminator is located towards $3'$-end of the coding strand and it usually defines the end of transcription.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 6 (Molecular Basis of Inheritance) states that a transcription unit in DNA is defined primarily by three regions: a promoter, the structural gene and a terminator, so A is correct.
2. The same section states the promoter is located towards the $5'$-end (upstream) of the structural gene, so B is correct.
3. It further states the promoter is a DNA sequence that provides a binding site for RNA polymerase, so C is correct, and that the presence of the promoter also defines the template and coding strands, so D is correct.
4. It states the terminator is located towards the $3'$-end (downstream) of the coding strand and usually defines the end of the process of transcription, so E is correct.
5. All of A, B, C, D and E are correct, option $4$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 46)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q103_c79e020d_30102026.png?v=c79e020d7abc)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q103_4369e41c_30102026.png?v=4369e41c0495)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A transcription unit has three parts, a promoter, a structural gene and a terminator. The promoter sits at the 5' end and fixes which strand is the template. The terminator sits towards the 3' end of the coding strand.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Most students pick option 1. Every statement here is one of NCERT's own sentences, so the only thing you have to decide is whether to keep E. You remember that the terminator is at the 3' end. You do not remember whether that is the coding strand or the template strand. So you leave E out and take the set of four. NCERT's sentence puts the terminator towards the 3' end of the coding strand.
- **Why:** You have to judge five printed statements that all come from one NCERT paragraph. All five are true. So 'A, B, C , D and E' is the only set that holds, and every shorter option is true but leaves something out.
<!--/ecat-->

## Q104

Biology · botany · The Living World

Which one of the following statements is not true about the universal rules of binomial nomenclature?

- (1) Biological names are generally in Latin
- (2) Both the words in a biological name, when handwritten, are separately underlined or printed in italics
- (3) The specific epithet in the biologial name starts with a small letter
- **(4)** The first word in the biological name represents the specific epithet, while the second component denotes the genus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. According to universal rules of nomenclature, the first word denoting the genus starts with a capital letter with the second components denotes the specific epithet and starts with small letter.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 1 (The Living World) lists the universal rules of nomenclature: biological names are generally in Latin and written in italics; the first word denotes the genus and the second the specific epithet.
2. It also states that when handwritten both words are separately underlined, the genus starts with a capital letter and the specific epithet with a small letter.
3. Options 1, 2 and 3 therefore restate the rules correctly.
4. Option 4 reverses genus and specific epithet, so it is the statement that is not true, option $4$.

**Subtopic:** Diversity in Living World and Binomial Nomenclature · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 46)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q104_3039f99f_30102026.png?v=3039f99f3d46)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q104_23e9321f_30102026.png?v=23e9321f26ad)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The rules of binomial nomenclature: the name is Latin, the genus comes first and is capitalised, the specific epithet comes second and is lower-case, the name is printed in italics and underlined when written by hand.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Most students pick option 2. The question asks which statement is 'not true', and if you read past the 'not' you go hunting for a rule that holds. Option 2 invites a second look because it folds two separate rules into one clause: italics in print, and underlining by hand. Both halves are genuine rules. So if you mark it, you have dropped the stem's 'not true'. The statement that really fails is the one that puts the specific epithet first.
- **Why:** You have to judge four printed rules against the real rules of binomial nomenclature. The question says 'Which one of the following statements is not true', and option 4 says 'The first word in the biological name represents the specific epithet, while the second component denotes the genus'.
<!--/ecat-->

## Q105

Biology · botany · Ecosystem

Match List I with List II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Decomposition | I. | Accumulation of dark coloured amorphous colloidal substance |
| B. | Detritus | II. | Release of inorganic nutrients by the activity of microbes in soil |
| C. | Mineralisation | III. | Breaking down of complex organic matter into inorganic substances. |
| D. | Humification | IV. | Dead remains of plants and animals including fecal matter |

- (1) A-IV, B-III, C-I, D-II
- **(2)** A-III, B-IV, C-II, D-I
- (3) A-I, B-II, C-III, D-IV
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Decomposition is the process of breaking down of complex organic matter into inorganic substance.
2. Detritus includes dead remains of plants and animals including fecal matter and acts as the raw material for decomposition.
3. Degradation of humus by activity of microbes leading to release of inorganic nutrients is called Mineralisation.
4. Accumulation of the dark coloured amorphous substance called humus, is called humification.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 14 (Ecosystem) defines decomposition as the process by which decomposers break down complex organic matter into inorganic substances, so A-III.
2. Dead plant remains such as leaves, bark and flowers, dead animal remains and faecal matter constitute detritus, the raw material for decomposition, so B-IV.
3. Mineralisation is the step in which the humus is further degraded by some microbes to release inorganic nutrients, so C-II.
4. Humification leads to the accumulation of a dark coloured amorphous substance called humus, so D-I.
5. A-III, B-IV, C-II, D-I matches option $2$.

**Subtopic:** Decomposition · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 46)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q105_46cc23e5_30102026.png?v=46cc23e5df89)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q105_62e744bc_30102026.png?v=62e744bc12f0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Detritus is the raw material. Decomposition breaks it down into inorganic matter. Humification builds up humus. Mineralisation releases the nutrients from it.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The two steps you can mix up are the two microbial ones. Humification is the 'dark coloured amorphous colloidal substance'. Mineralisation is the 'Release of inorganic nutrients by the activity of microbes in soil'. Swapping just those two gives you no option. The only option that swaps them also gives the process word Decomposition the dead-remains line and the material word Detritus the breakdown line. You would spot that, so nothing really pulls you away.
- **Why:** You have to match each step of decomposition with the definition NCERT gives it. List II prints them as definitions, like 'Release of inorganic nutrients by the activity of microbes in soil'.
<!--/ecat-->

## Q106

Biology · both · Cell: The Unit of Life

Which one of the following is the site for active ribosomal RNA synthesis?

- (1) Centrosome
- (2) Chromatin
- **(3)** Nucleolus
- (4) Kinetochore

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Nucleolus is the site for active ribosomal RNA synthesis.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 8 (Cell: The Unit of Life) states that the nucleolus is a site for active ribosomal RNA synthesis and that larger and more numerous nucleoli are present in cells actively carrying out protein synthesis.
2. The centrosome organises the spindle, chromatin is the DNA-histone complex and the kinetochore is the spindle attachment site on the centromere.
3. Hence option $3$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 47)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q106_ce144b73_30102026.png?v=ce144b73167c)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q106_d628e579_30102026.png?v=d628e579efc3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The nucleolus is where ribosomal RNA is made and where the ribosome subunits are put together.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2, chromatin. All transcription runs off DNA, and chromatin is where you picture the DNA. So 'rRNA is made on chromatin' follows from something that is true of transcription in general. But the rRNA genes sit in one particular place, the nucleolar organiser. The nucleolus built around it is the named site.
- **Why:** You need one stated fact: where rRNA is made. The question asks 'Which one of the following is the site for active ribosomal RNA synthesis?', and the four options are four named cell structures.
<!--/ecat-->

## Q107

Biology · botany · Respiration in Plants

$2(\mathrm{C_{51}H_{98}C_{6}}) + 145\,\mathrm{O_2} \rightarrow 102\,\mathrm{CO_2} + 98\,\mathrm{H_2O} + \text{energy}$

The Respiratory Quotient (RQ) of a biomolecule used for respiration, as per the above equation would be :

- **(1)** Between $0.5$ and $0.95$
- (2) Less than $0.5$
- (3) $1.0$
- (4) Between $1.25$ and $2$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{R.Q} = \dfrac{\text{Volume of } \mathrm{CO_2} \text{ evolved}}{\text{Volume of } \mathrm{O_2} \text{ consumed}}$
2. As per the given equation,
3. $2(\mathrm{C_{51}H_{98}O_{6}}) + 145\,\mathrm{O_2} \rightarrow 102\,\mathrm{CO_2} + 98\,\mathrm{H_2O} + \text{Energy}$
4. Hence the RQ can be calculated as,
5. $\mathrm{R.Q} = \dfrac{102}{145} = 0.7$
6. This value lies between $0.5$ and $0.95$.

**Solved independently** (answer withheld)

1. The respiratory quotient is defined as $RQ = \dfrac{\text{volume of } CO_2 \text{ evolved}}{\text{volume of } O_2 \text{ consumed}}$.
2. From the given equation, $102$ molecules of $CO_2$ are released for $145$ molecules of $O_2$ consumed.
3. $RQ = \frac{102}{145} = 0.703 \approx 0.7$.
4. NCERT Class 11, Ch. 14 (Respiration in Plants) gives exactly this equation for the fat tripalmitin and states its $RQ$ is about $0.7$.
5. $0.7$ lies between $0.5$ and $0.95$, so option $1$.

**Subtopic:** The Respiratory Balance Sheet, Amphibolic Pathway and Respiratory Quotient · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 47)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q107_015bf080_30102026.png?v=015bf080a481)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q107_8fd70f99_30102026.png?v=8fd70f990c16)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Respiratory quotient is $\mathrm{CO_2}$ released divided by $\mathrm{O_2}$ consumed. You read both numbers straight off the balanced equation. A fat gives about $0.7$.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Most students pick option 3. $\mathrm{RQ} = 1.0$ is the value for a carbohydrate. It is the number you have ready the moment you hear respiratory quotient, so you mark it without ever using the coefficients printed in the equation. The equation gives $\frac{102}{145} = 0.70$, which is the fat value.
- **Why:** You have to work out a ratio from the coefficients printed in the equation. The equation shows '$145\,\mathrm{O_2}$' and '$102\,\mathrm{CO_2}$', and the four options are ranges of RQ values.
- **Note:** The substrate printed in the equation reads $\mathrm{C_{51}H_{98}C_{6}}$. There is a carbon where the six oxygens of the fat belong. The answer only needs the 102 and the 145, so the ratio does not change.
<!--/ecat-->

## Q108

Biology · both · Principles of Inheritance and Variation

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Incomplete dominance | I. | Human skin colour |
| B. | Co-dominance | II. | Inheritance of flower colour in Antirrhinum sp. |
| C. | Pleiotropy | III. | Phenylketonuria disease in humans |
| D. | Polygenic inheritance | IV. | ABO blood groups |

- **(1)** A-II, B-IV, C-III, D-I
- (2) A-I, B-III, C-II, D-IV
- (3) A-I, B-IV, C-III, D-II
- (4) A-II, B-I, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Inheritance of flower colour in snapdragon (Antirrhinum sp.) is an example of incomplete dominance.
2. ABO blood groups exhibit codominance in case of individuals having AB blood group ($\mathrm{I^{A}I^{B}}$)
3. Phenylketonuria in humans is an example of pleiotropy since the gene responsible for it leads to multiple phenotypic effects.
4. Human skin colour is controlled by three pairs of non allelic genes, hence it is an example of polygenic inheritance.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 5 (Principles of Inheritance and Variation) uses flower colour in $Antirrhinum$ (dog flower, snapdragon) as its example of incomplete dominance, so A-II.
2. The ABO blood groups illustrate co-dominance (the $I^A$ and $I^B$ alleles are both expressed in AB individuals) as well as multiple allelism, so B-IV.
3. Phenylketonuria is NCERT's example of pleiotropy, where a single gene affects multiple phenotypic traits (mental retardation, reduced hair and skin pigmentation), so C-III.
4. Human skin colour is NCERT's example of polygenic inheritance, so D-I.
5. A-II, B-IV, C-III, D-I matches option $1$.

**Subtopic:** Incomplete Dominance & Co-dominance, Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 47)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q108_df029795_30102026.png?v=df029795da48)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q108_cb91b03f_30102026.png?v=cb91b03f7e0a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pink flowers in Antirrhinum show incomplete dominance. ABO blood groups show co-dominance. Phenylketonuria shows pleiotropy. Human skin colour shows polygenic inheritance.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. ABO is taught twice, once for multiple alleles and once for co-dominance. If you store 'many alleles' as 'many genes', you file the blood groups under polygenic inheritance and pair D with IV. Then only human skin colour is left for co-dominance. NCERT gives skin colour to polygenic inheritance and ABO to co-dominance.
- **Why:** You have to know which example NCERT gives for each inheritance pattern. List II is made of those examples, like 'Inheritance of flower colour in Antirrhinum sp.' and 'ABO blood groups'.
<!--/ecat-->

## Q109

Biology · both · Molecular Basis of Inheritance

Arrange the following steps of DNA fingerprinting in a correct sequence.

Choose the correct answer from the options given below :

- **(A.)** Isolation of DNA and its digestion by restriction endonucleases.
- **(B.)** Hybridisation using a labelled VNTR probe.
- **(C.)** Transferring of separated DNA fragments to synthetic membranes.
- **(D.)** Detection of hybridised DNA fragments by autoradiography.
- **(E.)** Separation of DNA fragments by electrophoresis.

- (1) A, B, D, C, E
- (2) A, D, B, E, C
- **(3)** A, E, C, B, D
- (4) A, E, B, C, D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The following is the correct sequence of steps of DNA fingerprinting.
2. A. Isolation of DNA and its digestion by restriction endonuclease.
3. B. Probes made complementary to the VNTR locus are allowed to hybridise with the DNA fragments.
4. C. The separated DNA fragments are transferred to synthetic membranes made of nylon or nitrocellulose.
5. D. Finally, the hybridised DNA fragments are detected under X-rays in a technique called autoradiography.
6. E. DNA fragments are separated based on their size by the technique of gel electrophoresis.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 6 (Molecular Basis of Inheritance) lists DNA fingerprinting as: isolation of DNA and its digestion by restriction endonucleases (A).
2. Then separation of DNA fragments by electrophoresis (E).
3. Then transferring (blotting) of the separated fragments to synthetic membranes such as nitrocellulose or nylon (C).
4. Then hybridisation using a labelled VNTR probe (B).
5. Finally detection of the hybridised DNA fragments by autoradiography (D).
6. The order A, E, C, B, D is option $3$.

**Subtopic:** DNA Fingerprinting · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 48)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q109_ba2b4125_30102026.png?v=ba2b4125cc4c)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q109_b3d464d6_30102026.png?v=b3d464d676ec)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** DNA fingerprinting goes in this order. Digestion, then electrophoresis, then blotting onto a membrane, then hybridisation with a labelled VNTR probe, then autoradiography.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. You picture the labelled probe going straight onto the gel. So you put hybridisation before the transfer to the membrane. But Southern blotting has to move the separated fragments onto the synthetic membrane first. Only then can the VNTR probe find them.
- **Why:** You have to put the steps of one named procedure in order. The stem says 'Arrange the following steps of DNA fingerprinting in a correct sequence'. Every option is the same five letters in a different order.
<!--/ecat-->

## Q110

Biology · both · Molecular Basis of Inheritance

Which of the following statements are correct with reference to packaging of DNA helix ?

Choose the correct answer from the options given below :

- **(A.)** Histones are organized to form a unit of eight molecules called histone octamer.
- **(B.)** Histones are negatively charged basic proteins.
- **(C.)** Histones are rich in the basic amino acid residues - lysine and arginine.
- **(D.)** The positively charged DNA is wrapped around the histone octamer to form nucleosome.
- **(E.)** The packaging of chromatin at higher levels requires an additional set of proteins called non-histone chromosomal proteins.

- **(1)** A, C and E only
- (2) B, D and E only
- (3) C, D and E only
- (4) A, B and D only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Eight Histones are combined to form a histone octamer. Histones are positively charged basic proteins that are rich in basic amino acids (lysine and arginine). The negatively charged DNA is wrapped around the histone octamer to form nucleosome. The packaging of chromatin at higher levels require NHC (non histone chromosomal) proteins.

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 12, Ch. 6 states histones are organised to form a unit of eight molecules called a histone octamer.
2. B is incorrect: histones are positively charged basic proteins, not negatively charged.
3. C is correct: histones are rich in the basic amino acid residues lysine and arginine, both of which carry positively charged side chains.
4. D is incorrect: it is the negatively charged DNA that is wrapped around the positively charged histone octamer to form a nucleosome.
5. E is correct: NCERT states that packaging of chromatin at higher levels requires an additional set of proteins collectively referred to as non-histone chromosomal (NHC) proteins.
6. So A, C and E only, option $1$.

**Subtopic:** Packaging of DNA Helix · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 48)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q110_4472852b_30102026.png?v=4472852b563d)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q110_cbf4bd58_30102026.png?v=cbf4bd589696)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a nucleosome, DNA is wound round a core of eight histones. The DNA is negatively charged. The octamer is positively charged, because the histones are rich in lysine and arginine. Non-histone proteins pack it further.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. NCERT's sentence has the negatively charged DNA wrapped around the positively charged histone octamer. You keep the picture but not which half carries which sign. So you let statement D stand. Once D is in, a true statement has to leave the set. Option 3 is the one that drops the histone octamer line.
- **Why:** You have to judge five printed statements against NCERT's account of DNA packaging. Two of them turn the charges round, 'Histones are negatively charged basic proteins' and 'The positively charged DNA is wrapped around the histone octamer'.
<!--/ecat-->

## Q111

Biology · botany · Photosynthesis in Higher Plants

Find the incorrect statement(s) about photosynthesis from the following:

Choose the answer from the options given below:

- **(A.)** The water splitting complex is associated with PS I.
- **(B.)** $\mathrm{C_4}$ plants use the $\mathrm{C_3}$ pathway of $\mathrm{CO_2}$ fixation as the main biosynthetic pathway.
- **(C.)** In $\mathrm{C_4}$ plants, photorespiration does not occur.
- **(D.)** $\mathrm{C_3}$ plants exhibit 'Kranz' anatomy.
- **(E.)** ATP synthesis in chloroplast occurs through chemiosmosis.

- (1) B and C only
- (2) B only
- (3) B and E only
- **(4)** A and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The water splitting complex is associated with PS-II. $\mathrm{C_3}$ pathway is the main biosynthetic pathway for $\mathrm{CO_2}$ fixation in both $\mathrm{C_3}$ and $\mathrm{C_4}$ plants.
2. $\mathrm{C_3}$ plants do not exhibit 'kranz' anatomy.
3. ATP synthesis in chloroplast (Photophosphorylation) occurs by chemiosmosis.

**Solved independently** (answer withheld)

1. A is incorrect: NCERT Class 11, Ch. 13 (Photosynthesis in Higher Plants) states the splitting of water is associated with PS II, on the inner side of the membrane.
2. B is correct: the Calvin (C3) cycle is the main biosynthetic pathway in all photosynthetic plants, C4 plants included, where it runs in the bundle sheath cells.
3. C is correct as NCERT teaches it: C4 plants are listed as lacking photorespiration, because the bundle sheath keeps the CO2 concentration at RuBisCO high.
4. D is incorrect: Kranz anatomy is the special leaf anatomy of C4 plants, not of C3 plants.
5. E is correct: ATP synthesis in the chloroplast is explained by chemiosmosis, driven by a proton gradient across the thylakoid membrane through the $F_0$-$F_1$ ATP synthase.
6. The incorrect statements are A and D, option $4$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water, The C₄ Pathway · **Difficulty:** medium (5 steps)

**Printed in the booklet** (page 49)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q111_eed65843_30102026.png?v=eed65843b3da)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q111_0dd9e1e6_30102026.png?v=0dd9e1e6698a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** C4 plants have Kranz anatomy. They have no photorespiration. They still run the Calvin cycle as their main biosynthetic pathway. Splitting of water belongs to PS II.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1. The stem asks for the incorrect statements. You read it as 'which are correct' and pick the two statements about C4 plants. But both of those are NCERT's own lines. The C3 pathway is the main biosynthetic pathway in C4 plants, and C4 plants lack photorespiration. So the incorrect pair is A and D.
- **Why:** You have to judge five statements, and the stem asks for the wrong ones. It says 'Find the incorrect statement(s) about photosynthesis'. Each of the three wrong options lists only statements that are true.
- **Note:** All three wrong options are made of true statements only. So the whole question rests on the word 'incorrect' in the stem. Statement B pulls you a second way. If you hold 'C4 plants fix carbon by the C4 pathway, not the C3 pathway', B reads like a contradiction. And B is the one statement that every wrong option contains.
<!--/ecat-->

## Q112

Biology · both · Strategies for Enhancement in Food Production

Arrange the following steps of somatic hybridisation in a correct sequence.

Choose the correct answer from the options given below:

- **(A.)** Digestion of cell walls.
- **(B.)** Isolation of naked protoplasts.
- **(C.)** Fusion of protoplasts to get hybrid protoplast.
- **(D.)** Isolation of single cells from two different varieites of plants.
- **(E.)** Growing of hybrid protoplast to form a new plant.

- **(1)** D, A, B, C, E
- (2) E, B, A, D, C
- (3) D, B, A, E, C
- (4) E, A, B, C, D

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Scientist have even isolated single cell  protoplasts from two different varieties of plants each having a desirable character and after digesting their cell walls have been able to isolate naked protoplasts (surrounded by plasma membrane) that can be fused to get hybrid protoplast, which can be further grown to form a new plant.  These hybrids are called somatic hybrids, while the process is called somatic hybridization.
2. So the correct sequence for the formation of somatic hybrids is D, A, B, C, E.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 9 (Strategies for Enhancement in Food Production) describes somatic hybridisation starting from isolated single cells of two different plant varieties (D).
2. Plant cells are then deprived of their cell walls by digestion with enzymes (A).
3. This yields isolated naked protoplasts (B).
4. Protoplasts from the two varieties are fused to give a hybrid protoplast (C).
5. The hybrid protoplast is then grown to form a new plant, a somatic hybrid such as pomato (E).
6. The order D, A, B, C, E is option $1$.

**Subtopic:** Unspecified Topic · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 49)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q112_a7fbe297_30102026.png?v=a7fbe297f22f)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q112_f699c01f_30102026.png?v=f699c01f10a4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Somatic hybridisation goes in this order. Single cells, then the walls are digested, then you have naked protoplasts, then they fuse into a hybrid protoplast, then you grow it into a plant.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The only order you could doubt is whether the walls are digested before or after the protoplasts come out naked. Two options start with E, which is the very last step of all, growing the hybrid protoplast into a plant. You would not start there. The one option that keeps the single cells first and reverses the wall digestion also puts the growing of the hybrid protoplast before the fusion that makes it. So nothing really pulls you away.
- **Why:** You have to put the steps of one named technique in order. The stem says 'Arrange the following steps of somatic hybridisation in a correct sequence'. Every option is the same five letters in a different order.
<!--/ecat-->

## Q113

Biology · botany · Anatomy of Flowering Plants

Match List-I with List-II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Conjunctive tissue | I. | Specialised cells in the vicinity of guard cells |
| B. | Casparian strips | II. | Endodermal cells rich in starch |
| C. | Subsidiary cells | III. | Tissue between xylem and phloem |
| D. | Starch sheath | IV. | Endodermal cells with suberin deposition |

- (1) A-IV, B-III, C-I, D-II
- (2) A-III, B-IV, C-II, D-I
- **(3)** A-III, B-IV, C-I, D-II
- (4) A-IV, B-III, C-II, D-I

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) Conjunctive tissue is the tissue between xylem and phloem.
2. (B) Casparian strips are found in endodermal cells, they are suberin depositions in the cell wall.
3. (C) Subsidiary cells are specialised cells in the vicinity of guard cells.
4. (D) Starch sheath is another name for endodermal cells rich in starch.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 6 (Anatomy of Flowering Plants) calls the parenchymatous tissue lying between the xylem and the phloem the conjunctive tissue, so A-III.
2. The endodermal cells of the dicot root bear a deposition of water-impermeable, waxy suberin in the form of Casparian strips, so B-IV.
3. The specialised epidermal cells surrounding the guard cells are called subsidiary cells, so C-I.
4. In the dicot stem the innermost layer of the cortex is called the starch sheath because its cells are rich in starch grains, so D-II.
5. A-III, B-IV, C-I, D-II matches option $3$.

**Subtopic:** Dicotyledonous and Monocotyledonous Root, Epidermal Tissue System · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 50)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q113_72999728_30102026.png?v=729997285781)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q113_0b2ab9e4_30102026.png?v=0b2ab9e4a086)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Casparian strips are the suberin bands of the endodermis. The starch sheath is the starch-rich endodermis of the stem. Conjunctive tissue lies between xylem and phloem.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Two entries both begin 'Endodermal cells'. II is rich in starch and IV has suberin deposition. Those are the two you could swap. No option swaps them, because B-II with D-IV is not printed. The three wrong options instead put 'Tissue between xylem and phloem' or 'Specialised cells in the vicinity of guard cells' on terms whose names have nothing to do with them. You can see that at once.
- **Why:** You have to know the description NCERT gives each anatomy term. List II prints those descriptions, like 'Endodermal cells with suberin deposition'.
<!--/ecat-->

## Q114

Biology · botany · Plant Growth and Development

Which one of the following is not a characteristic of plant cells in the phase of elongation?

- (1) New cell wall deposition
- (2) Cell enlargement
- (3) Increased vacuolation
- **(4)** Large conspicuous nuclei

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Phase of elongation is characterised by new cell wall deposition, increased vacuolation and enlargement of cell. Presence of large conspicuous nuclei is a feature of cells in the meristematic phase.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 15 (Plant Growth and Development) divides growth into the meristematic, elongation and maturation phases.
2. Of the meristematic phase it states that the cells are rich in protoplasm and possess large conspicuous nuclei, with thin primary cellulosic walls and abundant plasmodesmatal connections.
3. Of the elongation phase it states that increased vacuolation, cell enlargement and new cell wall deposition are the characteristics of the cells.
4. So options 1, 2 and 3 are features of elongation, while large conspicuous nuclei belong to the meristematic phase, making option $4$ the one that is not a characteristic.

**Subtopic:** Phases Of Growth · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 50)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q114_334133be_30102026.png?v=334133be1d4b)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q114_e25e1836_30102026.png?v=e25e1836a279)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the elongation phase the cells enlarge, form vacuoles and lay down new wall. Large conspicuous nuclei belong to the meristematic zone behind it.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Most students pick option 2. Cell enlargement is the one feature the phase is named for, so if you read the question as 'which IS a characteristic' you mark it at once. It really is a characteristic of elongation, and that is why the 'not' in the question is the whole point. The feature that belongs somewhere else is the large conspicuous nuclei of the meristematic zone.
- **Why:** You have to tell the features of the elongation zone apart from the features of the zone behind it. The question asks what is 'not a characteristic of plant cells in the phase of elongation', and 'Large conspicuous nuclei' is one of the options.
<!--/ecat-->

## Q115

Biology · botany · Plant Growth and Development

Match List-I with List-II

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | 2,4-D | I. | Brewing industry |
| B. | $\mathrm{GA_3}$ | II. | Stimulation of stomatal closure |
| C. | Kinetin | III. | Herbicide |
| D. | ABA | IV. | Nutrient mobilisation |

- **(1)** A-III, B-I, C-IV, D-II
- (2) A-IV, B-III, C-II, D-I
- (3) A-I, B-IV, C-III, D-II
- (4) A-I, B-II, C-IV, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. List-I (Growth Regulator) | List-II (Function/Effect)
2. A. 2,4-D (Auxin) | III. Herbicide
3. B. $\mathrm{GA_3}$ (Gibberellic Acid) | I. Brewing industry
4. C. Kinetin (Cytokinin) | IV. Nutrient mobilisation
5. D. ABA (Abscisic Acid) | II. Stimulation of stomatal closure

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 15 (Plant Growth and Development) notes that 2,4-D is used to kill dicotyledonous weeds, i.e. as a herbicide, so A-III.
2. It states that $GA_3$ is used to speed up the malting process in the brewing industry, so B-I.
3. Cytokinins such as kinetin promote nutrient mobilisation, which helps delay leaf senescence, so C-IV.
4. Abscisic acid stimulates the closure of stomata and is called the stress hormone, so D-II.
5. A-III, B-I, C-IV, D-II matches option $1$.

**Subtopic:** Physiological Effects of Plant Growth Regulators, Auxin, Gibberellins and Cytokinins, Ethylene and Abscisic Acid · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 50)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q115_ffc1f6bd_30102026.png?v=ffc1f6bd3bdf)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q115_5958bc62_30102026.png?v=5958bc622872)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** 2,4-D kills dicot weeds. GA3 speeds up malting in the brewing industry. Cytokinins mobilise nutrients. ABA closes the stomata.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  'Nutrient mobilisation' is the one line gibberellin could seem to claim, because GA works in brewing by mobilising the reserves in barley. But no option gives you B-IV unless it also takes 2,4-D off 'Herbicide'. You would spot that, so nothing really pulls you away. NCERT gives nutrient mobilisation to the cytokinins and the brewing industry to GA3.
- **Why:** You have to know the use NCERT states for each growth regulator. List II is made of those uses, like 'Brewing industry' and 'Herbicide'.
<!--/ecat-->

## Q116

Biology · botany · Photosynthesis in Higher Plants

The enzyme required for carboxylation in the Calvin cycle is

- (1) Hexokinase
- (2) PEP carboxylase
- **(3)** RuBP carboxylase - oxygenase
- (4) Carboxypeptidase

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. RuBisCO (RuBP carboxylase -oxygenase) is the enzyme required for carboxylation in the calvin cycle.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 13 (Photosynthesis in Higher Plants) states that in the Calvin cycle RuBP combines with $CO_2$ to form two molecules of 3-PGA, and that this is catalysed by the enzyme RuBP carboxylase-oxygenase, popularly called RuBisCO.
2. PEP carboxylase is the primary $CO_2$-fixing enzyme of the C4 (Hatch and Slack) pathway in mesophyll cells, not of the Calvin cycle.
3. Hexokinase is a glycolytic enzyme and carboxypeptidase a protease, so option $3$.

**Subtopic:** The Calvin Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 51)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q116_e36c9c6e_30102026.png?v=e36c9c6e4f01)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q116_d612aa47_30102026.png?v=d612aa474804)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** RuBisCO is the RuBP carboxylase-oxygenase. It is the enzyme that fixes $\mathrm{CO_2}$ onto RuBP in the Calvin cycle.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2, PEP carboxylase. It is the other carboxylating enzyme in the same chapter, the one that fixes $\mathrm{CO_2}$ in a C4 mesophyll cell. So if you keep only one slot in your head for 'the carboxylase of photosynthesis', you reach for it. But PEP carboxylase belongs to the C4 pathway. The carboxylation inside the Calvin cycle is RuBisCO's.
- **Why:** You need one stated fact: which enzyme does the carboxylation in the Calvin cycle. The question says 'The enzyme required for carboxylation in the Calvin cycle is', and two of the four options are named carboxylases.
<!--/ecat-->

## Q117

Biology · botany · Photosynthesis in Higher Plants

How many ATP and NADPH molecules are required to make one molecule of glucose through the Calvin pathway?

- **(1)** $18$ ATP and $12$ NADPH
- (2) $12$ ATP and $18$ NADPH
- (3) $24$ ATP and $18$ NADPH
- (4) $6$ ATP and $12$ NADPH

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Each turn of Calvin pathway utilizes 3ATP and $\mathrm{NADPH+H^{+}}$ molecules for fixation of $1$ $\mathrm{CO_2}$ molecule.
2. So for $1$ Glucose $6$ turns are required, hence $18$ ATP and $12$ $\mathrm{NADPH+H^{+}}$ are required for glucose synthesis.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 13 states that for every $CO_2$ molecule entering the Calvin cycle, $3$ molecules of ATP and $2$ of NADPH are required.
2. One molecule of glucose requires the fixation of $6$ molecules of $CO_2$, i.e. six turns of the cycle.
3. ATP needed $= 6 \times 3 = 18$.
4. NADPH needed $= 6 \times 2 = 12$.
5. So $18$ ATP and $12$ NADPH, option $1$.

**Subtopic:** The Calvin Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 51)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q117_3e55b92e_30102026.png?v=3e55b92ec275)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q117_042c31df_30102026.png?v=042c31dfb401)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Six turns of the Calvin cycle make one glucose. That costs 18 ATP and 12 NADPH, which is three ATP and two NADPH for each $\mathrm{CO_2}$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Most students pick option 2. You hold the pair of numbers 18 and 12 more firmly than you hold which cofactor each belongs to, and option 2 prints exactly that pair with the two labels swapped. Each $\mathrm{CO_2}$ costs 3 ATP and 2 NADPH. So across six turns ATP has to be the bigger figure.
- **Why:** You need the stated totals of the two cofactors for one glucose. The question asks 'How many ATP and NADPH molecules are required to make one molecule of glucose', and it prints no quantity for you to work from.
<!--/ecat-->

## Q118

Biology · botany · Morphology of Flowering Plants

> ⚠ The independent solve chose (1); the booklet prints (2).

Which of the following floral formula is the correct floral formula of Solanaceae family?

- (1) $\oplus\ \text{⚥}\ \mathrm{K}_{(5)}\,\mathrm{C}_{(5)}\,\mathrm{A}_{5}\,\underline{\mathrm{G}}_{(2)}$
- **(2)** $\oplus\ \text{⚥}\ \mathrm{K}_{(5)}\,\overparen{\mathrm{C}_{(5)}\,\mathrm{A}_{5}}\,\underline{\mathrm{G}}_{(2)}$
- (3) $\oplus\ \text{⚥}\ \mathrm{K}_{5}\,\mathrm{C}_{5}\,\mathrm{A}_{5}\,\underline{\mathrm{G}}_{(2)}$
- (4) $\oplus\ \text{⚥}\ \mathrm{K}_{5}\,\overparen{\mathrm{C}_{(5)}\,\mathrm{A}_{5}}\,\underline{\mathrm{G}}_{(2)}$

**Answer** — booklet: (2) · independent solve: (1) · differs

**Publisher's solution**

1. $\oplus\ \text{⚥}\ \mathrm{K}_{(5)}\,\overparen{\mathrm{C}_{(5)}\,\mathrm{A}_{5}}\,\underline{\mathrm{G}}_{(2)}$
2. Is the floral formula for Solanaceae.
3. It shows actinomorphic, bisexual, pentamerous flower with epipetalous condition
4. Generally in Solanaceae, calyx (K) and Corolla (C) shows fusion in sepals and petals respectively. Hence the floral formula must exhibit gamosepalous and gamopetalous condition.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 5 (Morphology of Flowering Plants) describes the Solanaceae flower as actinomorphic and bisexual, so the formula opens with the radial symmetry and bisexual symbols.
2. Calyx: five sepals, united (gamosepalous), persistent, valvate, giving $K_{(5)}$ - this rules out options 3 and 4, which print $K_5$ for free sepals.
3. Corolla: five petals, united (gamopetalous), valvate, giving $C_{(5)}$; androecium: five stamens, epipetalous, giving $A_5$.
4. Gynoecium: bicarpellary, syncarpous, ovary superior, bilocular, so $\underline{G}_{(2)}$ with the ovary-superior line beneath.
5. The formula $\oplus\ \text{bisexual}\ K_{(5)}\,C_{(5)}\,A_5\,\underline{G}_{(2)}$ is option $1$, exactly as the textbook prints it.

**Subtopic:** Solanaceae, Malvaceae and Cruciferae · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 51)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q118_b2f96d18_30102026.png?v=b2f96d186519)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q118_f1d0fe7d_30102026.png?v=f1d0fe7df84b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Solanaceae floral formula: actinomorphic, bisexual, fused calyx and fused corolla of five, five stamens, bicarpellary superior ovary.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Most students pick option 3. If you carry the family as a set of counts, five sepals, five petals, five stamens, two carpels, you write $\mathrm{K}_5\,\mathrm{C}_5$ and you put brackets only where you are sure of them, on the ovary. Every count in option 3 is right. The part that fails is the fusion. In Solanaceae both the calyx and the corolla are fused, $\mathrm{K}_{(5)}\,\mathrm{C}_{(5)}$.
- **Why:** You need the printed floral formula of a named family. All four options carry the same counts. They differ only in which whorls are bracketed as fused and in whether the epipetalous arc is drawn.
- **Note:** Options 1 and 2 differ by one mark only: the arc joining $\mathrm{C}_{(5)}$ and $\mathrm{A}_5$ for the epipetalous condition. If you are comparing those two, look at that arc and nothing else. Option 3 is wrong on the calyx and corolla brackets whichever of the two is keyed, and that is why the trap is written there.
<!--/ecat-->

## Q119

Biology · botany · Biodiversity and Conservation

Which of the following is an in situ conservation method?

- **(1)** Sacred Groves
- (2) Wildlife Safari Parks
- (3) Botanical Gardens
- (4) Seed Banks

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In-situ conservation is exemplified by sacred groves. Wildlife Safari parks, Botanical gardens, seed banks are examples of in-situ conservation.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 15 (Biodiversity and Conservation) defines in situ conservation as saving the endangered species in its natural habitat, and ex situ conservation as keeping threatened animals and plants outside their natural habitat under special care.
2. The chapter lists biosphere reserves, national parks, wildlife sanctuaries and sacred groves as in situ measures, naming sacred groves in Khasi and Jaintia Hills, Aravalli Hills, Western Ghats and Sarguja and Bastar.
3. Safari parks, botanical gardens, zoological parks and seed banks are given as ex situ measures.
4. Hence option $1$.

**Subtopic:** In Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q119_0cfd6b5f_30102026.png?v=0cfd6b5f80b7)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q119_ac87a33c_30102026.png?v=ac87a33cf254)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In situ conservation protects a species where it already lives. Ex situ takes it out, into botanical gardens, zoos, safari parks and seed banks.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. 'Wildlife' and 'park' are the two words attached to national parks and wildlife sanctuaries, which are in situ. So a wildlife safari park sounds like protection out in the habitat. But a safari park holds animals taken out of their habitat. It is listed with zoos and botanical gardens as ex situ.
- **Why:** You have to sort named facilities into the stated in situ and ex situ classes. The question asks 'Which of the following is an in situ conservation method?', and three of the options are ex situ facilities.
<!--/ecat-->

## Q120

Biology · both · Biotechnology: Principles and Processes

Which of the following statements are not true regarding restriction endonucleases?

Choose the answer from the options given below :

- **(A.)** They are called molecular scissors.
- **(B.)** These are the enzymes responsible for restricting the growth of bacteriophages in E. coli.
- **(C.)** They cut the DNA only at the centre of the palindromic sites.
- **(D.)** They remove nucleotides only from the ends of DNA fragments.
- **(E.)** They recognise specific palindromic base-pair sequences.

- (1) A and B only
- (2) A and E only
- (3) D and E only
- **(4)** C and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Statements C and D are incorrect. Restriction endonucleases usually cut the DNA slightly away from the centre of palindrome sites. They cannot remove nucleotides from the ends of the DNA fragment, which is function of restriction exonuclease.

**Solved independently** (answer withheld)

1. A is true: NCERT Class 12, Ch. 11 (Biotechnology: Principles and Processes) calls restriction enzymes molecular scissors.
2. B is true as NCERT teaches it: it records that in 1963 two enzymes responsible for restricting the growth of bacteriophage in $Escherichia\ coli$ were isolated, one of which cut DNA and was called restriction endonuclease.
3. C is not true: NCERT states that restriction enzymes cut the strand of DNA a little away from the centre of the palindrome sites, but between the same two bases on the opposite strands.
4. D is not true: NCERT states exonucleases remove nucleotides from the ends of the DNA, whereas endonucleases make cuts at specific positions within the DNA.
5. E is true: restriction endonucleases recognise specific palindromic nucleotide sequences.
6. The statements that are not true are C and D, option $4$.

**Subtopic:** Restriction Enzymes and Their Types · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 52)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q120_1e96859b_30102026.png?v=1e96859b36ea)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q120_d63c950f_30102026.png?v=d63c950ffb78)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Restriction endonucleases are the molecular scissors. They read a palindromic sequence and cut a little away from its centre. They cut inside the DNA, not at its ends.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Most students pick option 3. NCERT has the enzyme cutting a little away from the centre of the palindrome. You store the cut as 'at the centre', so statement C looks true and you leave it out. The only set left that still carries D, the untruth you did catch, is option 3. D really is untrue, because endonucleases cut within the DNA. But option 3 also lists E, and E is NCERT's own line, that the enzyme recognises specific palindromic sequences.
- **Why:** You have to judge five statements, and the stem asks for the wrong ones. It says 'Which of the following statements are not true regarding restriction endonucleases?'. The untrue pair is C and D.
- **Note:** Options 1 and 2 are made of true statements only. You reach them by reading the task as 'which are true' instead of 'not true'.
<!--/ecat-->

## Q121

Biology · botany · Morphology of Flowering Plants

In racemose inflorescence, _________.

- (1) The main axis terminates in a flower
- (2) Flowers are solitary
- (3) The growth is limited
- **(4)** Flowers are borne in an acropetal succession

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In racemose type of inflorescence, the main axis continues to grow and the flowers are borne laterally in an acropetal succession. On the contrary, in cymose type of inflorescence, the main axis terminates into a flower and hence, is limited in growth.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 5 (Morphology of Flowering Plants) states that in the racemose type of inflorescence the main axis continues to grow and the flowers are borne laterally in an acropetal succession.
2. Options 1 and 3 describe the cymose type, in which the main axis terminates in a flower and growth is therefore limited.
3. Solitary flowers are not an inflorescence type at all, so option $4$ is correct.

**Subtopic:** The Inflorescence · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 52)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q121_49b1325f_30102026.png?v=49b1325f0560)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q121_c2c0eaed_30102026.png?v=c2c0eaed0538)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a racemose inflorescence the main axis keeps growing and the flowers open from the base upwards, in acropetal succession.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. 'The main axis terminates in a flower' is the defining line for the cymose type, the only other inflorescence named alongside it. So if you hold the two definitions as a pair but not which label goes with which, you pick it. A terminal flower is what stops the axis. In racemose the axis stays alive and the flowers come acropetally.
- **Why:** You need the stated meaning of racemose inflorescence. You have to fill the blank in 'In racemose inflorescence, _________' with one of four descriptions. Two of them, 'The main axis terminates in a flower' and 'The growth is limited', are the cymose condition.
<!--/ecat-->

## Q122

Biology · botany · Sexual Reproduction in Flowering Plants

Arrange the following in the correct developmental sequence related to microsporogenesis :

Choose the correct answer from the options given below :

- **(A.)** Microspore tetrads
- **(B.)** Sporogenous tissue
- **(C.)** Pollen grains
- **(D.)** Pollen mother cells

- (1) D, A, C, B
- **(2)** B, D, A, C
- (3) B, D, C, A
- (4) A, D, C, B

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The process of formation of microspores from a pollen mother cell (PMC) through meiosis is called microsporogenesis.
2. The correct developmental sequence related to microsporogenesis will be -
3. Sporogenous tissue (B) $\rightarrow$ Pollen mother cell (D) $\rightarrow$ Microspore tetrads (A) $\rightarrow$ Pollen grains (C)

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 2 (Sexual Reproduction in Flowering Plants) states that each microsporangium is filled with a homogeneous group of compactly arranged cells called the sporogenous tissue (B).
2. As the anther develops, the cells of the sporogenous tissue undergo meiosis to form microspore tetrads; each such cell that can give rise to a tetrad is a potential pollen or microspore mother cell (D).
3. Meiosis of the pollen mother cell gives a cluster of four cells, the microspore tetrad (A).
4. As the anther matures and dehydrates, the microspores dissociate and develop into pollen grains (C).
5. The order B, D, A, C is option $2$.

**Subtopic:** Microsporangium and Microsporogenesis · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 53)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q122_37426990_30102026.png?v=37426990269e)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q122_ae94617e_30102026.png?v=ae94617e48aa)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Microsporogenesis goes in this order. Sporogenous tissue, then pollen mother cells, then microspore tetrads, then pollen grains.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. You take the tetrad for a later packing of finished pollen. So you put pollen grains before the microspore tetrads. The tetrad is the four microspores still held together right after meiosis of the pollen mother cell. They separate later and become the pollen grains.
- **Why:** You have to put four named stages in order. The stem says 'Arrange the following in the correct developmental sequence related to microsporogenesis'. Every option is the same four letters in a different order.
<!--/ecat-->

## Q123

Biology · both · Biomolecules

Identify the correct statements about biomolecules.

Choose the correct answer from the options given below :

- **(A.)** Lipids are generally water soluble.
- **(B.)** Proteins are polypeptides.
- **(C.)** Polysaccharides are long chains of sugars.
- **(D.)** Adenine and guanine are substituted pyrimidines.
- **(E.)** Almost all enzymes are proteins.

- (1) B, D and E only
- **(2)** B, C and E only
- (3) A, B and C only
- (4) C, D and E only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Statements B, C and E are correct.
2. Statements A and D are not true.
3. Lipids are not water soluble. Adenine and guanine are substituted purines.

**Solved independently** (answer withheld)

1. A is incorrect: NCERT Class 11, Ch. 9 (Biomolecules) treats lipids as the water-insoluble fraction, generally insoluble in water but soluble in organic solvents.
2. B is correct: proteins are polypeptides, linear chains of amino acids linked by peptide bonds.
3. C is correct: polysaccharides are long chains of sugars, described as polymers of monosaccharides such as cellulose, starch, glycogen and inulin.
4. D is incorrect: adenine and guanine are substituted purines; cytosine, uracil and thymine are the substituted pyrimidines.
5. E is correct: NCERT states that almost all enzymes are proteins, with some nucleic acids acting as enzymes (ribozymes).
6. So B, C and E only, option $2$.

**Subtopic:** Biomacromolecules · **Difficulty:** medium (5 steps)

**Printed in the booklet** (page 53)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q123_131cc74e_30102026.png?v=131cc74e0432)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q123_204525c2_30102026.png?v=204525c2e928)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each class of biomolecule has a one-line definition. Lipids are water insoluble. Proteins are polypeptides. Polysaccharides are chains of sugars. Adenine and guanine are substituted purines.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. Purines and pyrimidines are the two base classes taught in a single line, so the two names blur. You let 'Adenine and guanine are substituted pyrimidines' stand as true. Adenine and guanine are the substituted purines. Once D is in your set, one of NCERT's own lines has to go out. Here it is the one on polysaccharides.
- **Why:** You have to judge five one-line statements against NCERT's definitions. The stem says 'Identify the correct statements about biomolecules' above a block of five lettered lines.
- **Note:** If you accept D, option 4 also fits. It drops 'Proteins are polypeptides' instead. Both come from the same purine and pyrimidine slip.
<!--/ecat-->

## Q124

Biology · both · Principles of Inheritance and Variation

Which of the following statements are true with reference to the sex-determination in honeybees?

Choose the correct answer from the options given below :

- **(A.)** An offspring formed from the union of a sperm and an egg, develops as a female (queen or worker).
- **(B.)** An unfertilized egg develops as a male by parthenogenesis.
- **(C.)** A male has half the number of chromosomes than that of a female.
- **(D.)** Males produce sperms by meiosis.
- **(E.)** Honeybees have a haplodiploid sex-determination system.

- **(1)** A, B, C and E only
- (2) B, C, D and E only
- (3) A, B, C and D only
- (4) A, B, D and E only

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In case of honeybees, males have half the number of chromosomes than that of females. The females are diploid, having $32$ chromosomes and males are haploid, i.e., having $16$ chromosomes. This is called as haplodiploid sex-determination system and has special characteristic features, such as, the males produce sperms by mitosis.

**Solved independently** (answer withheld)

1. A is true: NCERT Class 12, Ch. 5 states that in honeybees an offspring formed from the union of a sperm and an egg develops as a female (queen or worker).
2. B is true: an unfertilised egg develops as a male (drone) by parthenogenesis.
3. C is true: because the male arises from an unfertilised haploid egg, he has half the number of chromosomes ($16$) of the diploid female ($32$).
4. D is false: NCERT states that the male honeybee, being haploid, produces sperms by mitosis - meiosis would halve an already haploid set.
5. E is true: this system, in which sex depends on the number of chromosome sets, is called the haplodiploid sex-determination system.
6. So A, B, C and E only, option $1$.

**Subtopic:** Sex Determination in Birds, Insects & Honey Bee · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 53)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q124_624a9d4e_30102026.png?v=624a9d4ed338)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q124_821a8414_30102026.png?v=821a8414d535)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Honeybees use haplodiploid sex determination. A fertilised egg gives a diploid female. An unfertilised egg gives a haploid male. That male makes sperms by mitosis.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Most students pick option 4. Everywhere else in the syllabus gametes are made by meiosis. So you apply the general rule and accept 'Males produce sperms by meiosis'. The same belief makes you throw out the statement that a male has half the chromosomes of a female, because a haploid cell has nothing left to halve. The haploid drone is the exception NCERT states. It produces sperms by mitosis.
- **Why:** You have to judge five statements inside the case the stem names. It says 'with reference to the sex-determination in honeybees'. Statement D is true of animals in general but not of the drone.
- **Note:** All three wrong options contain D. So the whole question rests on one thing. Are the drone's sperms made by mitosis or by meiosis?
<!--/ecat-->

## Q125

Biology · botany · Plant Growth and Development

Heterophyllous development in response to environment is an example of which of the following phenomena?

- (1) Redifferentiation
- (2) Elasticity
- (3) Dedifferentiation
- **(4)** Plasticity

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Plants follow different pathways in response to environment or phases of life to form different kinds of structures. This ability is called plasticity, e.g., heterophylly in cotton, coriander and larkspur.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 15 (Plant Growth and Development) states that plants follow different pathways in response to environment or phases of life to form different kinds of structures, and that this ability is called plasticity.
2. It gives heterophylly in cotton, coriander and larkspur as plasticity due to the phase of life, and the heterophyllous development in buttercup ($Ranunculus$), where submerged and aerial leaves differ in shape, as plasticity in response to the environment.
3. Dedifferentiation and redifferentiation describe a cell regaining and then again losing the capacity to divide, and elasticity is not the term used here.
4. Hence option $4$.

**Subtopic:** Development and Plasticity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q125_799c8da0_30102026.png?v=799c8da08e9c)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q125_9f86caec_30102026.png?v=9f86caec892f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plasticity is a plant's ability to form different structures in different conditions or at different stages of life. Heterophylly is the standard example.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3, dedifferentiation. It is a term from the same section, about a plant cell changing what it had already become. So if you file 'the plant changes its form to suit its surroundings' under that family, you reach for it. But dedifferentiation is mature cells getting back the power to divide. Making two kinds of leaf according to conditions is plasticity.
- **Why:** You need the stated name of a phenomenon. The question asks 'Heterophyllous development in response to environment is an example of which of the following phenomena?', and two of the options are other named terms from the same chapter.
<!--/ecat-->

## Q126

Biology · both · Biomolecules

Which of the following statements are correct regarding amino acids?

Choose the correct answer from the options given below:

- **(A.)** They are substituted methanes.
- **(B.)** Serine is an aromatic amino acid.
- **(C.)** Valine is a neutral amino acid.
- **(D.)** Lysine is an acidic amino acid.

- (1) C and D only
- (2) B and C only
- **(3)** A and C only
- (4) A and B only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Statements A and C are correct while statements B and D are incorrect. Serine is an alcoholic amino acid and lysine is a basic amino acid.

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 11, Ch. 9 (Biomolecules) states that amino acids are substituted methanes, with a hydrogen, a carboxyl group, an amino group and a variable R group on the same carbon.
2. B is incorrect: serine carries a hydroxymethyl side chain; the aromatic amino acids are tyrosine, phenylalanine and tryptophan.
3. C is correct: NCERT classifies amino acids by the number of amino and carboxyl groups as acidic (glutamic acid), basic (lysine) and neutral (valine).
4. D is incorrect: by the same classification lysine is the textbook example of a basic amino acid, not an acidic one.
5. So A and C only, option $3$.

**Subtopic:** Amino Acids and Their Classification · **Difficulty:** medium (4 steps)

**Printed in the booklet** (page 54)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q126_0009b7f6_30102026.png?v=0009b7f6667e)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q126_4f5f6270_30102026.png?v=4f5f62709f90)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Amino acids are substituted methanes. The side group puts each one in a class. Glutamic acid is acidic. Lysine is basic. Valine is neutral. Tyrosine, phenylalanine and tryptophan are aromatic.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. NCERT has one sentence for the classes. Glutamic acid is acidic, lysine is basic, valine is neutral. You keep the three class names but not which name sits in which slot. So you let 'Lysine is an acidic amino acid' stand. In that same sentence lysine is the basic one.
- **Why:** You have to judge four one-line statements against NCERT's classification of amino acids. The stem says 'Which of the following statements are correct regarding amino acids?'. Option 3 is the only set with no wrongly labelled name in it.
<!--/ecat-->

## Q127

Biology · botany · Biodiversity and Conservation

“The Evil Quartet” of biodiversity loss includes which of the following?

- (1) Over-exploitation; Alien species invasions; Air pollution; Co-extinctions
- (2) Habitat loss and fragmentation; Air pollution; Water pollution; Co-extinctions
- **(3)** Habitat loss and fragmentation; over-exploitation; Alien species invasions; Co-extinctions
- (4) Over-exploitation; Alien species invasions; Soil pollution; Co-extinctions

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. 'The Evil Quartet' is the Sobriquet used to describe the four major causes of biodiversity loss which includes Habitat loss and fragmentation, over-exploitation; Alien species invasions and Co-extinctions.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 15 (Biodiversity and Conservation) names the four major causes of biodiversity loss The Evil Quartet.
2. They are listed as (i) habitat loss and fragmentation, (ii) over-exploitation, (iii) alien species invasions and (iv) co-extinctions.
3. Pollution of air, water or soil is not one of the four, which rules out options 1, 2 and 4, leaving option $3$.

**Subtopic:** Causes of Biodiversity Losses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 54)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q127_bc378d8b_30102026.png?v=bc378d8b72b6)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q127_4097dc3e_30102026.png?v=4097dc3ed7bd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Evil Quartet is a fixed list of four drivers of biodiversity loss: habitat loss and fragmentation, over-exploitation, alien species invasions, co-extinctions.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Most students pick option 1. It carries three of the four names and puts air pollution in place of habitat loss. If you hold the quartet as 'the four causes of biodiversity loss' instead of as four fixed names, you accept it, because pollution is a genuine cause taught in the same chapter. The name taken out of the list is habitat loss and fragmentation, and the source calls that the most important cause.
- **Why:** You need to know which names are on a fixed list. Each option bundles four causes that stand or fall together, and three of them are shared between options.
- **Note:** The four options are sets of four named causes. You accept or reject each set whole. No lettered statement block is printed.
<!--/ecat-->

## Q128

Biology · botany · Respiration in Plants

Match List-I with List-II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Glycolysis | I. | Inner mitochondrial membrane |
| B. | ETS | II. | Mitochondrial matrix |
| C. | Accumulation of protons | III. | Cytoplasm |
| D. | Krebs' cycle | IV. | Intermembrane space |

- (1) A-IV, B-II, C-I, D-III
- (2) A-II, B-III, C-IV, D-I
- **(3)** A-III, B-I, C-IV, D-II
- (4) A-I, B-IV, C-III, D-II

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The site of glycolysis is the cytoplasm in all living organisms. Electron transport system is localized in inner mitochondrial membrane. Accumulation of protons occur in intermembrane space and Kreb's Cycle takes place in mitochondrial matrix.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 14 (Respiration in Plants) states that the scheme of glycolysis is carried out in the cytoplasm of the cell, so A-III.
2. The electron transport system is located in the inner mitochondrial membrane, so B-I.
3. In chemiosmosis the proton pump moves protons across the inner membrane, so they accumulate in the intermembrane space, so C-IV.
4. The citric acid or Krebs cycle takes place in the mitochondrial matrix, so D-II.
5. A-III, B-I, C-IV, D-II matches option $3$.

**Subtopic:** Glycolysis, Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 55)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q128_59c908af_30102026.png?v=59c908afa3bb)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q128_423b4fef_30102026.png?v=423b4fefc919)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Glycolysis happens in the cytoplasm. Krebs' cycle runs in the matrix. The electron transport system sits in the inner membrane. The protons it pumps collect in the intermembrane space.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The pair you could confuse is the two mitochondrial compartments, I 'Inner mitochondrial membrane' against IV 'Intermembrane space'. To fall for that you would need B-IV with C-I. No option prints it. Only one option keeps glycolysis in the cytoplasm as A-III, so every wrong option has already moved glycolysis out of the cytoplasm. You would catch that.
- **Why:** You have to know the site NCERT gives each stage of respiration. List II is made of those sites, like 'Inner mitochondrial membrane' and 'Intermembrane space'.
<!--/ecat-->

## Q129

Biology · botany · Sexual Reproduction in Flowering Plants

Which one of the following is a triploid cell?

- (1) Synergid
- (2) Central cell
- (3) Zygote
- **(4)** Primary endosperm cell

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Synergid is haploid, Zygote is diploid, Central cell initially contains two polar nuclei which fuse just before fertilization to form a secondary nucleus ($2n$).
2. Primary endosperm cell (PEC) is triploid.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 2 (Sexual Reproduction in Flowering Plants) describes double fertilisation: one male gamete fuses with the egg (syngamy), the other with the two polar nuclei (triple fusion).
2. Triple fusion involves three haploid nuclei, $n + n + n = 3n$, giving the triploid primary endosperm nucleus within the primary endosperm cell.
3. The synergid is haploid ($n$) and the zygote diploid ($2n$); the central cell before triple fusion carries the two polar nuclei (or the diploid secondary nucleus), not three sets.
4. Hence option $4$.

**Subtopic:** Double Fertilisation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q129_e6877ca9_30102026.png?v=e6877ca965ba)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q129_b1354e67_30102026.png?v=b1354e6762c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Triple fusion makes the primary endosperm cell triploid: two polar nuclei plus one male gamete.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2, the central cell. Triple fusion happens inside the central cell, so if you follow where the second male gamete goes, you name the container it happens in. But before that fusion the central cell holds two haploid polar nuclei. Only after the male gamete joins them is the cell the triploid primary endosperm cell.
- **Why:** You need one stated fact: the ploidy of a named cell of the embryo sac. The question asks 'Which one of the following is a triploid cell?', and the four options are cells of the same embryo sac.
<!--/ecat-->

## Q130

Biology · botany · Sexual Reproduction in Flowering Plants

Which one of the following types of pollination brings genetically different types of pollen grains to the stigma?

- (1) Autogamy
- **(2)** Xenogamy
- (3) Geitonogamy
- (4) Cleistogamy

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Transfer of pollen grains from anther to stigma of a different plant is known as Xenogamy. This is the only type of pollination which brings genetically different types of pollen grains to stigma. Cleistogamy flowers are invariably autogamous.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 2 (Sexual Reproduction in Flowering Plants) defines xenogamy as the transfer of pollen grains from the anther to the stigma of a different plant, and states that this is the only type of pollination which brings genetically different types of pollen grains to the stigma.
2. Autogamy and cleistogamy are pollination within the same flower and geitonogamy is between two flowers of the same plant, so in all three the pollen is genetically identical to the recipient plant.
3. Hence option $2$.

**Subtopic:** Pollination · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 55)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q130_c259479a_30102026.png?v=c259479a7e05)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q130_0727a51a_30102026.png?v=0727a51a0ebc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only xenogamy brings pollen from a different plant, and so genetically different pollen, to a stigma.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3, geitonogamy. It also carries pollen to a different flower, and it also needs a pollinating agent. So if you read 'different flower' as 'different plant', you pick it. But the pollen comes from the same plant. That makes geitonogamy genetically the same as self-pollination.
- **Why:** You need the stated definition that separates four named types of pollination. The question says 'brings genetically different types of pollen grains to the stigma', and the four options are the four -gamy terms.
<!--/ecat-->

## Q131

Biology · botany · Morphology of Flowering Plants

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Marginal | I. | Mustard |
| B. | Axile | II. | Pea |
| C. | Parietal | III. | Marigold |
| D. | Basal | IV. | Lemon |

- **(1)** A-II, B-IV. C-I, D-III
- (2) A-I, B-III. C-II, D-IV
- (3) A-III, B-I. C-IV, D-II
- (4) A-IV, B-II. C-I, D-III

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Marginal placentation is found in pea, axile placentation is found in lemon, parietal placentation is found in mustard and basal placentation is found in marigold.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 5 (Morphology of Flowering Plants) gives marginal placentation, with ovules on the ventral suture ridge of a monocarpellary unilocular ovary, as that of pea, so A-II.
2. In axile placentation the placenta is axial and ovules are attached to it in a multilocular ovary, as in china rose, tomato and lemon, so B-IV.
3. In parietal placentation ovules develop on the inner wall or peripheral part of a false-septate ovary, as in mustard and $Argemone$, so C-I.
4. In basal placentation the placenta develops at the base of the ovary with a single ovule attached, as in sunflower and marigold, so D-III.
5. A-II, B-IV, C-I, D-III matches option $1$.

**Subtopic:** Gynoecium · **Difficulty:** medium (4 steps)

**Printed in the booklet** (page 56)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q131_0e16c3ee_30102026.png?v=0e16c3ee6525)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q131_9c748b36_30102026.png?v=9c748b360855)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each type of placentation has an example. Marginal is pea. Axile is lemon. Parietal is mustard. Basal is marigold.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. A pea pod has one row of ovules, and that row looks as if it sits on an axis. So if you hold axile as 'ovules on an axis', you pair axile with pea and leave lemon for marginal. Marginal means ovules on the ventral suture of a one-chambered ovary. Lemon has many chambers with ovules on the central axis, and that is what NCERT lists under axile.
- **Why:** You have to know which plant NCERT names for each type of placentation. List II is just those plants, 'Mustard', 'Pea', 'Marigold', 'Lemon'.
<!--/ecat-->

## Q132

Biology · botany · Biological Classification

The main criteria used for Five Kingdom Classification proposed By R.H. Whittaker (1969) included :

Choose the correct answer from the options given below :

- **(A.)** Cell structure
- **(B.)** Body organization
- **(C.)** Presence of flagellum
- **(D.)** Reproduction
- **(E.)** Phylogenetic relationships

- (1) A, B, C, D and E
- (2) B, C and D only
- **(3)** A, B, D and E only
- (4) A, B and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The main criteria for five kingdom classification used by (R.H. Whittaker) includes cell structure, body organization, mode of nutrition, reproduction and phylogenetic relationships.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 2 (Biological Classification) states that the main criteria for the five kingdom classification used by R.H. Whittaker include cell structure, thallus organisation, mode of nutrition, reproduction and phylogenetic relationships.
2. A (cell structure), B (body, i.e. thallus, organisation), D (reproduction) and E (phylogenetic relationships) are therefore all on the list.
3. C (presence of flagellum) is not a criterion of the five kingdom scheme; it is used within groups such as the algal or protistan classes.
4. So A, B, D and E only, option $3$.

**Subtopic:** Five-Kingdom Classification & Characteristics · **Difficulty:** medium (5 steps)

**Printed in the booklet** (page 56)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q132_3dcf250c_30102026.png?v=3dcf250c4bed)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q132_53113ed0_30102026.png?v=53113ed08d42)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Whittaker used five criteria for the five kingdoms. Cell structure, thallus organisation, mode of nutrition, reproduction and phylogenetic relationships.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Most students pick option 4. You recall Whittaker's criteria as the structural and evolutionary ones, cell structure, body organisation and phylogeny. So you leave reproduction off the list and take the set of three. Reproduction is on NCERT's list. The only item printed here that is not on it is the presence of a flagellum.
- **Why:** You have to know what is on one printed NCERT list. The stem says 'The main criteria used for Five Kingdom Classification proposed By R.H. Whittaker (1969) included'. Each option is a smaller set picked from five possible criteria.
<!--/ecat-->

## Q133

Biology · both · Biomolecules

Match List I with List II :

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | Trypsin | I. | Intercellular ground substance |
| B. | Morphine | II. | Lectin |
| C. | Concanavalin A | III. | Enzyme |
| D. | Collagen | IV. | Alkaloid |

- **(1)** A-III, B-IV. C-II, D-I
- (2) A-I, B-II. C-III, D-IV
- (3) A-IV, B-III. C-II, D-I
- (4) A-III, B-II. C-IV, D-I

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Trypsin is a proteolytic enzyme.
2. Morphine is a secondary metabolite that belongs to the category of alkaloid.
3. Concanavalin A is a lectin.
4. Collagen acts as an intercellular ground substance.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 9 (Biomolecules) tabulates examples of proteins and their functions; trypsin is listed as an enzyme, so A-III.
2. Morphine, obtained from $Papaver\ somniferum$, is listed among the secondary metabolites as an alkaloid, so B-IV.
3. Concanavalin A is listed in the same table as a lectin, a protein that binds carbohydrates, so C-II.
4. Collagen is listed as the intercellular ground substance and is the most abundant protein in animal tissue, so D-I.
5. A-III, B-IV, C-II, D-I matches option $1$.

**Subtopic:** Primary And Secondary Metabolites, Proteins And Structure Of Protein · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 56)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q133_78e7febf_30102026.png?v=78e7febf5cd8)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q133_9d438028_30102026.png?v=9d438028d9df)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Trypsin is an enzyme. Morphine is an alkaloid. Concanavalin A is a lectin. Collagen is the intercellular ground substance.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. Morphine and concanavalin A are two rows of the same NCERT table of plant secondary metabolites. You remember that both names are in the table. You do not remember which row each one sits in, so you swap the two labels. NCERT prints morphine under alkaloids and concanavalin A under lectins.
- **Why:** You have to know which class NCERT puts each substance in. List II is just those classes, 'Lectin', 'Alkaloid', 'Enzyme'.
<!--/ecat-->

## Q134

Biology · both · Biotechnology: Principles and Processes

Which of the following statements are correct with respect to DNA separation, isolation and visualization?

Choose the correct answer from the options given below :

- **(A.)** The cutting of DNA is done by molecular scissors.
- **(B.)** The DNA fragments separate according to their size in an agarose gel, upon electrophoresis.
- **(C.)** The separated DNA fragments can be seen without staining when exposed to UV light.
- **(D.)** The separated DNA fragments, when stained with ethidium bromide, can be seen in visible light.

- (1) B and D only
- **(2)** A and B only
- (3) B and C only
- (4) A and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The cutting of DNA is possible by the use of restriction enzymes that results in the fragments of DNA. These fragments of DNA can be separated by a technique known as gel electrophoresis.
2. The DNA fragments separate (resolve) according to their size through sieving effect provided by the agarose gel.
3. The separated DNA fragments can be visualised only after staining the DNA with a compound known as ethidium bromide followed by exposure to UV radiation.

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 12, Ch. 11 (Biotechnology: Principles and Processes) calls restriction endonucleases molecular scissors, which cut the DNA.
2. B is correct: in agarose gel electrophoresis the negatively charged DNA fragments move towards the anode and separate according to their size, the smaller the fragment the farther it moves.
3. C is incorrect: NCERT states the separated DNA fragments can be visualised only after staining the DNA with a compound known as ethidium bromide - they are not visible unstained.
4. D is incorrect: after ethidium bromide staining, the bright orange-coloured DNA bands are seen on exposure to UV radiation, not in visible light.
5. So A and B only, option $2$.

**Subtopic:** Separation & Isolation of DNA Fragments (Gel Electrophoresis) · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 57)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q134_c8d7cc32_30102026.png?v=c8d7cc32a7df)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q134_33ef84c9_30102026.png?v=33ef84c90456)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Restriction enzymes cut the DNA into fragments. An agarose gel sorts them by size. You can see them only after staining with ethidium bromide and shining UV light on the gel.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Most students pick option 1. Ethidium bromide is the right stain. The first half of statement D is correct, so you trust the second half too and take the bands to be visible in ordinary light. NCERT puts the stained gel under UV radiation. That is where the DNA shows up as bright orange bands.
- **Why:** You have to judge four statements against NCERT's account of gel electrophoresis. Two of them differ only in the light used, 'seen without staining when exposed to UV light' against 'stained with ethidium bromide, can be seen in visible light'.
<!--/ecat-->

## Q135

Biology · both · Principles of Inheritance and Variation

Which one of the following disorders is caused by the substitution of Glutamic acid (Glu) by Valine (Val) at the sixth position of the beta globin chain of the haemoglobin molecule?

- (1) Thalassemia
- **(2)** Sickle-cell anaemia
- (3) Phenylketonuria
- (4) Haemophilia

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sickle cell anaemia is an autosome linked recessive trait that can be transmitted from parents to offsprings when both partners are carrier for the gene. The defect is caused by the substitution of Glutamic acid (Glu) by Valine (Val) at sixth position of beta globin chain of haemoglobin molecule.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 5 (Principles of Inheritance and Variation) states that sickle-cell anaemia is caused by the substitution of glutamic acid (Glu) by valine (Val) at the sixth position of the beta globin chain of the haemoglobin molecule.
2. The same passage traces it to a single base substitution, GAG to GUG, in the sixth codon of the beta globin gene, giving the mutant haemoglobin HbS.
3. Thalassemia is a quantitative defect in globin chain synthesis, phenylketonuria an enzyme (phenylalanine hydroxylase) defect and haemophilia an X-linked clotting-factor defect.
4. Hence option $2$.

**Subtopic:** Sickle-cell Anaemia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 57)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q135_9aa08741_30102026.png?v=9aa087411c34)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q135_11bbee6e_30102026.png?v=11bbee6e7265)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sickle-cell anaemia is a single amino acid substitution: Glu to Val at position six of the beta globin chain.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1, thalassemia. It is the other beta globin disorder, taught in the same section, and it is also described as a defect of the globin chains. So if you keep one slot for 'beta globin chain', you reach for it. But thalassemia is a shortfall in how much globin is made. It is not a substituted amino acid.
- **Why:** You need one stated fact: the molecular defect in one named disorder. The question prints 'substitution of Glutamic acid (Glu) by Valine (Val) at the sixth position of the beta globin chain', and two of the options are haemoglobin disorders.
<!--/ecat-->

## Q136

Biology · zoology · Chemical Coordination and Integration

Match List I with List II:

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Cortisol | I. | Stimulates the formation of alveoli in mammary glands |
| B. | Aldosterone | II. | Produces anti-inflammatory reactions |
| C. | Cholecystokinin | III. | Stimulates reabsorption of $\mathrm{Na^{+}}$ and water from renal tubule |
| D. | Progesterone | IV. | Stimulates secretion of pancreatic enzymes and bile juice |

- (1) A-III, B-II, C-IV, D-I
- (2) A-IV, B-II, C-I, D-III
- **(3)** A-II, B-III, C-IV, D-I
- (4) A-II, B-III, C-I, D-IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Cortisol produces anti-inflammatory reactions and suppresses the immune response.
2. Aldosterone acts mainly at the renal tubules and stimulates the reabsorption of $\mathrm{Na^{+}}$ and water and excretion of $\mathrm{K^{+}}$ and phosphate ions.
3. Cholecystokinin (CCK) acts on both pancreas and gall bladder and stimulates the secretion of pancreatic enzymes and bile juice, respectively.
4. Progesterone acts on the mammary glands and stimulates the formation of alveoli.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 22 (Chemical Coordination and Integration) states that cortisol (a glucocorticoid) produces anti-inflammatory reactions and suppresses the immune response, so A-II.
2. Aldosterone, the mineralocorticoid of the adrenal cortex, acts mainly on the renal tubules and stimulates the reabsorption of $Na^{+}$ and water, so B-III.
3. Cholecystokinin, secreted by the intestinal mucosa, acts on the pancreas and gall bladder and stimulates the secretion of pancreatic enzymes and bile juice respectively, so C-IV.
4. Progesterone supports pregnancy and acts on the mammary glands, stimulating the formation of alveoli and milk secretion, so D-I.
5. A-II, B-III, C-IV, D-I matches option $3$.

**Subtopic:** Adrenal Gland, Hormones of Heart, Kidney and Gastrointestinal Tract · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 58)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q136_a9b6bacb_30102026.png?v=a9b6bacbcaed)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q136_9a79cc36_30102026.png?v=9a79cc36c37f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cortisol is the glucocorticoid with the anti-inflammatory action. Aldosterone is the mineralocorticoid that reabsorbs Na+ and water. Cholecystokinin acts on the pancreas and bile. Progesterone acts on the mammary alveoli.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Most students pick option 1. Cortisol and aldosterone are the two adrenal cortex hormones, and NCERT prints them in one paragraph. You remember only that one of them works on the kidney. So you reach for the name you know better and pair A with III. It is aldosterone that drives reabsorption of Na+ and water from the renal tubule. Cortisol's listed action is the anti-inflammatory one.
- **Why:** You have to know the action NCERT states for each hormone. List II prints those actions, like 'Stimulates reabsorption of $\mathrm{Na^{+}}$ and water from renal tubule'.
<!--/ecat-->

## Q137

Biology · zoology · Excretory Products and Their Elimination

Arrange the following events occuring in Renin-Angiotensin mechanism in the correct order:

Choose the correct answer from the options given below:

- **(A.)** Increase in blood pressure and Glomerular filtration rate
- **(B.)** Reabsorption of $\mathrm{Na^{+}}$ and water from distal parts of tubule due to Aldosterone
- **(C.)** Fall in Glomerular filtration rate
- **(D.)** Vasoconstriction by Angiotensin II and release of Aldosterone.
- **(E.)** Renin converts Angiotensinogen into Angiotensin I, followed by Angiotensin II.

- (1) A, C, E, B, D
- (2) C, A, B, D, E
- (3) A, D, B, E, C
- **(4)** C, E, D, B, A

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The JGA plays a complex regulatory role
2. A fall in glomerular blood flow/GFR can activate the JG cells to release renin which converts angiotensinogen in blood to angiotensin I and further to angiotensin II
3. Angiotensin II, being a powerful vasoconstrictor, increases the glomerular blood pressure and thereby GFR.
4. Angiotensin II activates the adrenal cortex to release aldosterone.
5. Aldosterone causes reabsorption of $\mathrm{Na^{+}}$ and $\mathrm{H_2O}$ from the distal parts of the tubule. This leads to an increase in blood pressure and GFR.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 19 (Excretory Products and their Elimination) begins the mechanism with a fall in glomerular blood flow, glomerular blood pressure or GFR, which activates the JG cells (C).
2. The JG cells release renin, which converts angiotensinogen in blood to angiotensin I and further to angiotensin II (E).
3. Angiotensin II, a powerful vasoconstrictor, increases the glomerular blood pressure and also activates the adrenal cortex to release aldosterone (D).
4. Aldosterone causes reabsorption of $Na^{+}$ and water from the distal parts of the tubule (B).
5. This leads to an increase in blood pressure and GFR (A).
6. The order C, E, D, B, A is option $4$.

**Subtopic:** Regulation Of Kidney Function · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 58)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q137_e897bba7_30102026.png?v=e897bba73233)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q137_0e138576_30102026.png?v=0e138576ea85)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A fall in glomerular filtration rate starts the renin-angiotensin cascade. Angiotensin II and aldosterone then bring the blood pressure back up, and that is how it ends.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. You take the fall in glomerular filtration rate as the result of the cascade instead of what starts it. So you read the whole sequence from the wrong end and open with the rise in blood pressure. The fall in GFR is what makes the JG cells release renin. So it comes first, and the rise in blood pressure comes last.
- **Why:** You have to put five named events in order. The stem says 'Arrange the following events occuring in Renin-Angiotensin mechanism in the correct order'. A fall in GFR and a rise in blood pressure are printed as two separate items.
<!--/ecat-->

## Q138

Biology · zoology · Breathing and Exchange of Gases

In humans, respiration occurs in the following steps. Arrange these steps in the correct order.

Choose the correct answer from the options given below

- **(A.)** Diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$ between blood and tissues
- **(B.)** Diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$ across alveolar membrane
- **(C.)** Pulmonary ventilation by which atmospheric air is drawn in and $\mathrm{CO_2}$ rich alveolar air is released out
- **(D.)** Cellular respiration
- **(E.)** Transport of gases by the blood

- (1) A, B, C, D, E
- (2) E, A, C, D, B
- **(3)** C, B, E, A, D
- (4) C, A, B, E, D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Respiration involves the following steps:
2. (i) Breathing or pulmonary ventilation by which atmospheric air is drawn in and $\mathrm{CO_2}$ rich alveolar air is released out.
3. (ii) Diffusion of gases across alveolar membrane.
4. (iii) Transport of gases by the blood
5. (iv) Diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$ between blood and tissues
6. (v) Utilisation of $\mathrm{O_2}$ by the cells for catabolic reactions and resultant release of $\mathrm{CO_2}$

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 17 (Breathing and Exchange of Gases) lists respiration in five steps, beginning with breathing or pulmonary ventilation, by which atmospheric air is drawn in and $CO_2$-rich alveolar air released out (C).
2. Second is the diffusion of gases ($O_2$ and $CO_2$) across the alveolar membrane (B).
3. Third is the transport of gases by the blood (E).
4. Fourth is the diffusion of $O_2$ and $CO_2$ between blood and tissues (A).
5. Fifth is utilisation of $O_2$ by the cells for catabolic reactions with release of $CO_2$, i.e. cellular respiration (D).
6. The order C, B, E, A, D is option $3$.

**Subtopic:** Exchange Of Gases · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 59)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q138_b5b8de1d_30102026.png?v=b5b8de1def49)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q138_855cef29_30102026.png?v=855cef293a58)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Respiration has five steps. Ventilation, then diffusion across the alveolar membrane, then transport by the blood, then diffusion into the tissues, then cellular respiration.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. Statements A and B both open 'Diffusion of $\mathrm{O_2}$ and $\mathrm{CO_2}$' and differ only in the site. You fix ventilation first and cellular respiration last. Then you take the two diffusion lines in the order they are printed, which puts the tissues before the alveolar membrane. Gas has to cross the alveolar membrane and be carried by the blood before it can reach a tissue.
- **Why:** You have to put five steps of one process in order. The stem says 'In humans, respiration occurs in the following steps. Arrange these steps in the correct order'.
<!--/ecat-->

## Q139

Biology · zoology · Human Health and Disease

The following are the stages of life cycle of Plasmodium. Arrange the stages in the proper order.

Choose the correct answer from the options given below:

- **(A.)** The parasites reproduce asexually in RBCs, bursting the cells.
- **(B.)** The parasites reproduce asexually in liver cells, bursting the cells and releasing into blood.
- **(C.)** Gametocytes develop in RBCs.
- **(D.)** Sporozoites reach the liver through the blood.
- **(E.)** Female mosquito injects sporozoites into humans during bite.

- **(1)** E, D, B, A, C
- (2) A, B, C, D, E
- (3) C, A, B, D, E
- (4) E, C, D, B, A

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Plasmodium enters the human body as sporozoites through the bite of an infected female Anopheles mosquito. The parasites initially multiply asexually within the liver cells and then attack the RBCs resulting in their rupture.
2. Sexual stages (gametocytes) develop in red blood cells.
3. When a female Anopheles mosquito bites an infected person, these parasites enter the mosquito's body and undergo further development.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 8 (Human Health and Disease) states that $Plasmodium$ enters the human body as sporozoites through the bite of an infected female $Anopheles$ mosquito (E).
2. The parasites initially multiply within the liver cells, which they reach through the blood (D).
3. They then burst the liver cells and are released into the blood (B).
4. The parasites then attack the red blood cells, reproducing asexually and rupturing them, which releases haemozoin and causes the chill and high fever (A).
5. Some parasites in the RBCs develop into gametocytes (C), which are taken up by a feeding mosquito.
6. The order E, D, B, A, C is option $1$.

**Subtopic:** Protozoal Diseases (Malaria) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 59)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q139_7d759c3d_30102026.png?v=7d759c3df8d3)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q139_d49537b1_30102026.png?v=d49537b11a3e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Plasmodium in the human host goes like this. Sporozoites come in with the bite and reach the liver. They multiply there and burst out. They multiply again in the red cells. Only then do they form gametocytes.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. Gametocytes are the stage the mosquito takes up. You keep that link, so you put them next to the bite instead of at the end of the human cycle. In NCERT's sequence the gametocytes develop in the red blood cells after the parasite has multiplied there. A later bite is what collects them.
- **Why:** You have to put the stages of one life cycle in order. The stem says 'The following are the stages of life cycle of Plasmodium. Arrange the stages in the proper order'.
<!--/ecat-->

## Q140

Biology · both · Biotechnology: Principles and Processes

Insertion of a foreign DNA at BamHI site in an E.coli cloning vector pBR322 results in the loss of antibiotic resistance towards:

- (1) Ampicillin and tetracycline
- (2) Ampicillin
- **(3)** Tetracycline
- (4) Gentamycin

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. If one ligate a foreign DNA at the BamHI site of tetracycline resistance gene in the vector pBR322, the recombinant plasmid will lose tetracycline resistance due to insertion of foreign DNA.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 11 (Biotechnology: Principles and Processes) shows pBR322 carrying two selectable markers, $amp^{R}$ (ampicillin resistance) and $tet^{R}$ (tetracycline resistance).
2. The figure places the recognition sites for $BamH$I and $Sal$I within the $tet^{R}$ gene, while $Pst$I and $Pvu$I lie within $amp^{R}$.
3. Ligating foreign DNA at the $BamH$I site therefore disrupts $tet^{R}$ by insertional inactivation; the recombinants grow on ampicillin but not on tetracycline.
4. Ampicillin resistance is unaffected and gentamycin is not a pBR322 marker, so option $3$.

**Subtopic:** Cloning Sites & Vectors for Genes in Plants and Animals · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 59)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q140_71f9cdde_30102026.png?v=71f9cdde6f33)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q140_ac9deed5_30102026.png?v=ac9deed5321d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** pBR322 carries two resistance genes. The BamHI site lies inside the tetracycline gene, so putting DNA in there kills tetracycline resistance only.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. You remember pBR322 as the vector with two resistance genes, ampicillin and tetracycline. If you hold that pair but not which gene the restriction sites sit inside, you name the other member. BamHI cuts within the tetracycline gene. So tetracycline resistance is the one lost, and ampicillin resistance stays behind for you to select on.
- **Why:** You need one stated fact: where a named restriction site sits inside a named vector. The question says 'Insertion of a foreign DNA at BamHI site in an E.coli cloning vector pBR322', and the options offer the vector's two resistance markers singly and together.
<!--/ecat-->

## Q141

Biology · both · Biomolecules

The following reaction depicts the activity of a particular class of enzymes :

Identify the enzymes class ‘E’ from the following options :

![printed figure: question](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/figures_agent/q141_a7b668a0_30102026.png?v=a7b668a0420e)

- (1) Transferases
- (2) Isomerases
- **(3)** Lyases
- (4) Ligases

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Lyases are the enzymes that catalyse removal of groups from substrates by mechanisms other than hydrolysis leaving double bonds.
2. Transferases are the enzymes that catalyse a transfer of a group between a pair of substrates.
3. Isomerases catalyse inter-conversion of optical, geometric or positional isomers.
4. Ligases catalyse the linking together of $2$ compounds.

**Solved independently** (answer withheld)

1. The figure shows a substrate $X-C-C-Y$ converted into $X-Y$ plus $C=C$.
2. Two groups are eliminated from adjacent carbons of the substrate and a double bond appears in the residue, with no water consumed and no group transferred to a second substrate.
3. NCERT Class 11, Ch. 9 (Biomolecules) defines lyases as enzymes that catalyse the removal of groups from substrates by mechanisms other than hydrolysis, leaving double bonds, and prints this exact scheme for them.
4. Transferases move a group between two substrates, isomerases rearrange a single molecule without changing its formula and ligases join two molecules with ATP, none of which matches.
5. Hence option $3$.

**Subtopic:** Classification And Nomenclature Of Enzymes And Cofactors · **Difficulty:** unsure (0 steps)

**Printed in the booklet** (page 60)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q141_3692606b_30102026.png?v=3692606b8a74)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q141_d4e99f43_30102026.png?v=d4e99f4343e8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Enzymes are grouped by the change they bring about: moving a group across, rearranging a molecule inside itself, breaking a bond without water, making a bond at the cost of ATP.
- **Why:** You have to put a printed reaction into one of the six enzyme classes. The question says 'The following reaction depicts the activity of a particular class of enzymes', and the four options are four of those class names.
- **Note:** The reaction that decides the class is in the figure, not in the stem text. So we cannot show which option a named wrong route lands on from the question as it is recorded here. That is why no trap is written.
<!--/ecat-->

## Q142

Biology · zoology · Neural Control and Coordination

The specific receptors for neurotransmitters in a synapse are present on __________.

- (1) Schwann cell
- (2) Pre-synaptic membrane
- (3) Myelin sheath
- **(4)** Post-synaptic membrane

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The specific receptors for neurotransmitters in a synapse are present on post-synaptic membrane.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 21 (Neural Control and Coordination) describes a chemical synapse: the impulse causes synaptic vesicles to fuse with the pre-synaptic membrane and release neurotransmitters into the synaptic cleft.
2. The released neurotransmitters bind to specific receptors present on the post-synaptic membrane, opening ion channels and generating a new potential in the post-synaptic neuron.
3. Hence option $4$.

**Subtopic:** Transmission of Impulses · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 60)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q142_4401247d_30102026.png?v=4401247d9ac5)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q142_6a5c3bcb_30102026.png?v=6a5c3bcb6e20)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Neurotransmitter is released from the pre-synaptic side. It crosses the cleft and binds receptors on the post-synaptic membrane.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2, the pre-synaptic membrane. That is the side you name first, because it is where the vesicles fuse and the transmitter leaves. The two terms differ by one prefix. But the transmitter has to cross the cleft before it can act. So the receptors that bind it sit on the far side.
- **Why:** You need one stated fact: where the receptors of a synapse sit. You have to fill the blank in 'The specific receptors for neurotransmitters in a synapse are present on __________', and the two faces of the synapse are offered against each other.
<!--/ecat-->

## Q143

Biology · both · Principles of Inheritance and Variation

What is the probability of having children with ‘O’ blood group, where both mother and father are heterozygous for ‘A’ and ‘B’ blood group, respectively?

- **(1)** $25\%$
- (2) $0\%$
- (3) $75\%$
- (4) $50\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\because$ Out of four children, one is with blood group 'O'.
2. $\therefore$ The probability of having children with 'O' blood group will be $25\%$

**Solved independently** (answer withheld)

1. A mother heterozygous for blood group A has the genotype $I^{A}i$ and a father heterozygous for blood group B has $I^{B}i$ (NCERT Class 12, Ch. 5, multiple allelism of the $I$ gene).
2. The mother's gametes are $I^{A}$ and $i$, each with probability $\frac{1}{2}$; the father's are $I^{B}$ and $i$, each with probability $\frac{1}{2}$.
3. The four equally likely combinations are $I^{A}I^{B}$ (AB), $I^{A}i$ (A), $I^{B}i$ (B) and $ii$ (O).
4. Blood group O requires the homozygous recessive $ii$, whose probability is $\frac{1}{2}\times\frac{1}{2}=\frac{1}{4}=25\%$.
5. Hence option $1$.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 60)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q143_616e3afe_30102026.png?v=616e3afe1ee6)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q143_cd632a3c_30102026.png?v=cd632a3c668e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A heterozygous A parent and a heterozygous B parent each carry a recessive $i$. So one child in four is $ii$ and is group O.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Most students pick option 2. Drop the word 'heterozygous' and the cross becomes $I^A I^A \times I^B I^B$. Then every child is AB and none can be O, which is exactly option 2. But the question prints 'heterozygous', and that puts an $i$ in each parent. So one of the four squares is $ii$.
- **Why:** You have to work out a probability from the parents' genotypes. The question says 'both mother and father are heterozygous for A and B blood group, respectively', and the options are percentages.
<!--/ecat-->

## Q144

Biology · zoology · Breathing and Exchange of Gases

Match List-I with List-II.

Choose the correct answer from the options given below :

| List-I | | List-II | |
|---|---|---|---|
| A. | ERV (Expiratory Reserve Volume) | I. | $2500-3000\,\mathrm{mL}$ |
| B. | RV (Residual Volume) | II. | $500\,\mathrm{mL}$ |
| C. | IRV (Inspiratory Reserve Volume) | III. | $1000-1100\,\mathrm{mL}$ |
| D | TV (Tidal Volume) | IV. | $1100-1200\,\mathrm{mL}$ |

- **(1)** A-III, B-IV, C-I, D-II
- (2) A-III, B-I, C-IV, D-II
- (3) A-I, B-III, C-II, D-IV
- (4) A-I, B-II, C-III, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. ERV (Expiratory Reserve Volume) - $1000 - 1100\,\mathrm{mL}$
2. RV (Residual Volume) - $1100-1200\,\mathrm{mL}$
3. IRV (Inspiratory Reserve Volume) - $2500-3000\,\mathrm{mL}$
4. TV (Tidal Volume) - $500\,\mathrm{mL}$

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 17 (Breathing and Exchange of Gases) gives expiratory reserve volume as $1000$ to $1100$ mL, so A-III.
2. Residual volume, the air remaining in the lungs after a forcible expiration, is $1100$ to $1200$ mL, so B-IV.
3. Inspiratory reserve volume is $2500$ to $3000$ mL, so C-I.
4. Tidal volume, the volume of air inspired or expired during a normal respiration, is about $500$ mL, so D-II.
5. A-III, B-IV, C-I, D-II matches option $1$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 61)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q144_bec6013a_30102026.png?v=bec6013a80c3)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q144_281913a4_30102026.png?v=281913a430e0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** You just have to remember the lung volumes. Tidal volume is 500 mL. Inspiratory reserve is 2500-3000 mL. Expiratory reserve is 1000-1100 mL. Residual volume is 1100-1200 mL.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The two values you can really mix up are the close ranges '1000-1100 mL' and '1100-1200 mL'. No option swaps them, because A-IV with B-III is not printed. Every wrong option instead moves the 500 mL figure off tidal volume, or the 2500-3000 mL figure off the inspiratory reserve. Those are the two values the chapter stores as single numbers, so you would catch it.
- **Why:** You have to remember the value NCERT prints for each respiratory volume. List II is just those figures, like '$500\,\mathrm{mL}$' and '$2500-3000\,\mathrm{mL}$'.
<!--/ecat-->

## Q145

Biology · both · Evolution

Which of the following is not an example of convergent evolution?

- (1) Flippers of penguins and dolphins
- (2) Eyes of octopuses and mammals
- **(3)** Fore limbs of whales and bats
- (4) Wings of butterflies and birds

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Fore limbs of whales and bats are examples of divergent evolution that show homology.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 7 (Evolution) states that the forelimbs of whales, bats, cheetah and humans share the same pattern of bones - humerus, radius, ulna, carpals, metacarpals and phalanges - though they perform different functions.
2. Such homologous organs indicate common ancestry and illustrate divergent evolution, not convergent evolution.
3. The same chapter gives the eye of the octopus and of mammals, the wings of butterfly and of birds, and the flippers of penguins and dolphins as analogous structures, the result of convergent evolution from different ancestries.
4. So the pair that is not convergent evolution is option $3$.

**Subtopic:** Homology and Analogy · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 61)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q145_a48017d1_30102026.png?v=a48017d1a98d)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q145_dea2cb08_30102026.png?v=dea2cb08bd6e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Convergent evolution gives unrelated groups the same function out of different structures. The whale and bat forelimb is the homology case, not a convergence case.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1. Flippers of penguins and dolphins is one of the standard examples of analogy, so it reads as a correct answer the moment you drop the 'not' in the question. It pulls a second way as well. Both flippers are modified forelimbs. So if you test for convergence by asking whether the bone plan underneath is different, you get the wrong verdict here.
- **Why:** You have to tell analogy from homology across four named pairs. The question asks what is 'not an example of convergent evolution', and 'Fore limbs of whales and bats' is one of the options.
<!--/ecat-->

## Q146

Biology · zoology · Structural Organisation in Animals

Male frogs can be distinguished from female frogs due to the presence of

Choose the correct answer from the options given below

- **(A.)** Bulging eyes
- **(B.)** Vocal sacs
- **(C.)** Webbed digits in feet
- **(D.)** Copulatory pad on first digit of fore limbs
- **(E.)** Olive green-coloured skin with dark irregular spots

- (1) B and C only
- (2) C and E only
- (3) A and B only
- **(4)** B and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Male frogs can be distinguished from female frogs due to the presence of vocal sacs and copulatory pad on first digit of fore limbs.
2. Bulging eyes, webbed digit in feet and olive green-coloured skin with dark irregular spots are common in both male and female frogs.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 7 (Structural Organisation in Animals) states that the male frog can be distinguished by the presence of sound-producing vocal sacs and also a copulatory pad on the first digit of the fore limbs, which are absent in the female frog.
2. Bulging eyes, webbed digits in the hind feet and olive green skin with dark irregular spots are described for the frog generally, so they do not separate the sexes.
3. So B and D only, option $4$.

**Subtopic:** Morphology of Frog · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 61)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q146_99393190_30102026.png?v=99393190e4b3)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q146_2fb58f71_30102026.png?v=2fb58f7158ba)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only two things separate a male frog from a female. The vocal sacs, and the copulatory pad on the first digit of the forelimb.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Most students pick option 3. Bulging eyes come from NCERT's general description of the frog. They are not in the two lines about telling the sexes apart. You read the task as 'which of these are frog features' and accept bulging eyes next to the vocal sacs. Both sexes have bulging eyes. The male's second mark is the copulatory pad on the first digit of the forelimbs.
- **Why:** You have to know the two features NCERT gives for telling a male frog apart. The stem says 'Male frogs can be distinguished from female frogs due to the presence of'. Three items in the block are features of frogs of either sex.
- **Note:** Options 1 and 2 do the same thing with the other two general features, webbed digits and the olive green spotted skin.
<!--/ecat-->

## Q147

Biology · zoology · Animal Kingdom

A group of researchers procured some fish like animals and upon investigation the following characters were observed:

Which of the following species of animals did they consider to fit best with these characters?

- **(A.)** Endoskeleton was made of cartilage.
- **(B.)** Ectoparasitic; as they were found attached on fish skin with their circular sucking mouth.
- **(C.)** Paired fins and scales were absent, but 7 pairs of gill slits were present.

- (1) Scoliodon sp.
- **(2)** Petromyzon sp.
- (3) Exocoetus sp.
- (4) Branchiostoma sp.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Petromyzon sp. have cartilaginous endoskeleton. They have circular sucking mouth. They are ectoparasites on some fishes. Their body is devoid of scales and paired fins. They have 7 pairs (6-15 pairs) of gill slits.
2. Scoliodon and Exocoetus are not parasites.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 4 (Animal Kingdom) describes the Cyclostomata as ectoparasites on some fishes, with an elongated body bearing $6$-$15$ pairs of gill slits for respiration and a sucking circular mouth without jaws.
2. It adds that their body is devoid of scales and paired fins and that their cranium and vertebral column are cartilaginous, which matches all three observations.
3. $Petromyzon$ (lamprey) is NCERT's named example of Cyclostomata.
4. $Scoliodon$ is a cartilaginous fish with paired fins and placoid scales, $Exocoetus$ a bony fish, and $Branchiostoma$ (Amphioxus) a cephalochordate that is a filter feeder, not an ectoparasite.
5. Hence option $2$.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 62)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q147_0529f4f0_30102026.png?v=0529f4f095a0)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q147_671d86aa_30102026.png?v=671d86aad01d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A cyclostome is recognised like this. It is jawless. It is an ectoparasite with a circular sucking mouth. Its endoskeleton is cartilaginous. It has no paired fins and no scales.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1. You stop at the first character given, a cartilaginous endoskeleton, and name the shark. The shark is the example of cartilage in a fish that you have drilled most. But Scoliodon has jaws, paired fins and placoid scales, and it is no ectoparasite. So it answers only one of the three characters printed.
- **Why:** You have to name an organism from the characters printed about it. The stem supplies three observations, like 'Ectoparasitic; as they were found attached on fish skin with their circular sucking mouth'. The options are four named genera.
- **Note:** On the page this is a lettered block of three observed characters. But the answer is a genus, not a combination of letters. qtype is recorded from the lettered block, because that is what is printed.
<!--/ecat-->

## Q148

Biology · both · Evolution

Match List I with List II with respect to chronology of evolution of life forms

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | About 65 mya | (I) | Jawless fish probably evolved |
| B. | About 500 mya | (II) | The dinosaurs suddenly disappeared from the earth |
| C. | About 350 mya | (III) | Seaweeds and few plants probably existed |
| D | About 320 mya | (IV) | Invertebrates were formed and became active |

- (1) A(III), B(IV), C(I), D(II)
- (2) A(I), B(II), C(III), D(IV)
- (3) A(II), B(IV), C(III), D(I)
- **(4)** A(II), B(IV), C(I), D(III)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. About $65$ mya - The dinosaurs suddenly disappeared from the earth.
2. About $500$ mya - Invertebrates were formed and became active.
3. About $350$ mya - Jawless fish probably evolved.
4. About $320$ mya - Seaweeds and few plants probably existed.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 7 (Evolution) states that about $65$ mya the dinosaurs suddenly disappeared from the earth, so A-(II).
2. It states that by about $500$ mya invertebrates were formed and became active, so B-(IV).
3. It states that jawless fish probably evolved around $350$ mya, so C-(I).
4. It states that sea weeds and few plants existed probably around $320$ mya, so D-(III).
5. A-(II), B-(IV), C-(I), D-(III) matches option $4$.

**Subtopic:** Brief Account of Evolution · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 62)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q148_2942e28b_30102026.png?v=2942e28b6aad)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q148_b03fca1a_30102026.png?v=b03fca1a462a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT gives dates for the milestones of life. Invertebrates were formed by 500 mya. Jawless fish came about 350 mya. Seaweeds and a few plants existed about 320 mya. Dinosaurs were gone about 65 mya.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. You expect plants to come before vertebrates. So you give 350 mya to the seaweeds and 320 mya to the jawless fish. NCERT prints it the other way round. Jawless fish probably evolved around 350 mya, and seaweeds and few plants existed around 320 mya.
- **Why:** You have to know the date NCERT prints against each event. List I is just the bare dates, like 'About 350 mya' and 'About 320 mya'.
- **Note:** The stem says 'with respect to chronology of evolution of life forms'. But it gives you both the dates and the events. So you do not have to put anything in order. Each pair is a date-and-event line that NCERT prints.
<!--/ecat-->

## Q149

Biology · zoology · Reproductive Health

Match List I and List II

Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Progestasert | (I) | Barrier made of rubber used by females |
| B. | Multiload 375 | (II) | Oral contraceptive |
| C. | Diaphragm | (III) | Hormone releasing IUD |
| D | Saheli | (IV) | Copper releasing IUD |

- **(1)** A(III), B(IV), C(I), D(II)
- (2) A(IV), B(II), C(I), D(III)
- (3) A(IV), B(III), C(I), D(II)
- (4) A(III), B(IV), C(II), D(I)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Progestasert - Hormone releasing IUD
2. Multiload 375 - Copper releasing IUD
3. Diaphragm - Barrier made of rubber used by females
4. Saheli - Oral contraceptive

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 4 (Reproductive Health) classifies IUDs as non-medicated (Lippes loop), copper releasing (CuT, Cu7, Multiload 375) and hormone releasing (Progestasert, LNG-20).
2. So Progestasert is the hormone releasing IUD, A-(III), and Multiload 375 the copper releasing IUD, B-(IV).
3. Diaphragms, cervical caps and vaults are described as barriers made of rubber that are inserted into the female reproductive tract to cover the cervix, so C-(I).
4. Saheli is described as a new oral contraceptive for females, a non-steroidal pill with a very high contraceptive value, so D-(II).
5. A-(III), B-(IV), C-(I), D-(II) matches option $1$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 63)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q149_66784db5_30102026.png?v=66784db5dca4)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q149_fcc42f10_30102026.png?v=fcc42f1092f0)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Progestasert is a hormone releasing IUD. Multiload 375 is a copper releasing IUD. The diaphragm is a rubber barrier. Saheli is an oral pill.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. NCERT prints Multiload 375 and Progestasert as two rows of the same list of IUDs. You remember that both are IUDs. You do not remember which one releases what, so you swap them. The 375 in Multiload 375 is its copper surface area. Progestasert is named after the progestogen it releases.
- **Why:** You have to know which class NCERT puts each trade name in. List II is made of those classes, like 'Hormone releasing IUD' and 'Copper releasing IUD'.
<!--/ecat-->

## Q150

Biology · zoology · Body Fluids and Circulation

The WBC count of a person’s blood sample is $8000/\mathrm{cu\ mm}$. How many eosinophils and lymphocytes would be in the same blood sample approximately?

- (1) $300-500/\mathrm{cu\ mm}$ and $1200-1500/\mathrm{cu\ mm}$ respectively
- **(2)** $160-240/\mathrm{cu\ mm}$ and $1600-2000/\mathrm{cu\ mm}$ respectively
- (3) $300-500/\mathrm{cu\ mm}$ and $500-700/\mathrm{cu\ mm}$ respectively
- (4) $100-120/\mathrm{cu\ mm}$ and $160-200/\mathrm{cu\ mm}$ respectively

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Eosinophils constitute $2$-$3\%$ of total WBCs. Hence its value is approximately $2$ to $3\%$ of $8000/\mathrm{cu\ mm}$ = $160 - 240/\mathrm{cu\ mm}$
2. Lymphocytes constitute $20$-$25\%$ of total WBCs. Hence its value is approximately $20$ to $25\%$ of $8000/\mathrm{cu\ mm}$ = $1600 - 2000/\mathrm{cu\ mm}$

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 18 (Body Fluids and Circulation) gives the differential leucocyte percentages as neutrophils $60$-$65\%$, eosinophils $2$-$3\%$, basophils $0.5$-$1\%$, lymphocytes $20$-$25\%$ and monocytes $6$-$8\%$.
2. Eosinophils $= 2\%$ to $3\%$ of $8000 = 0.02 \times 8000$ to $0.03 \times 8000 = 160$ to $240$ per cu mm.
3. Lymphocytes $= 20\%$ to $25\%$ of $8000 = 0.20 \times 8000$ to $0.25 \times 8000 = 1600$ to $2000$ per cu mm.
4. These are the figures in option $2$.

**Subtopic:** Formed Elements And Their Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 63)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q150_f681a07e_30102026.png?v=f681a07ead11)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q150_118468ae_30102026.png?v=118468aec20d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The differential WBC count as percentages of the total: eosinophils 2-3 per cent, lymphocytes 20-25 per cent.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3. The list you have learnt holds five percentages, and this question needs two of them. Option 3's lymphocyte figure is what the monocyte share gives: 6 to 8 per cent of 8000 is about 500 to 650. So if you reach into that list and take the neighbouring cell type's percentage, you land there instead of on the 20 to 25 per cent that lymphocytes carry.
- **Why:** You have to apply percentages you have learnt to the total printed in the question. The question says 'The WBC count of a person's blood sample is $8000/\mathrm{cu\ mm}$', and each option gives two absolute counts 'respectively'.
- **Note:** No option here is part-correct. Only one option has either figure right, so half_right does not apply.
<!--/ecat-->

## Q151

Biology · zoology · Human Health and Disease

Match List I with List II:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Nicotine | I. | Causes sense of euphoria and increased energy |
| B. | Morphine | II. | Stimulates adrenal gland to release catecholamines into blood circulation |
| C. | Heroin | III. | Effective sedative and painkiller |
| D. | Cocaine | IV. | A depressant; slows down body function |

- (1) A–III, B–II, C–IV, D–I
- (2) A–II, B–III, C–I, D–IV
- **(3)** A–II, B–III, C–IV, D–I
- (4) A–III, B–II, C–I, D–IV

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Nicotine is present in tobacco and it activates adrenal medulla to release catecholamines into blood circulation, so (A) $\rightarrow$ II
2. Morphine acts as an effective sedative and painkiller. It is an opioid, so (B) $\rightarrow$ III
3. Heroin acts as a depressant and slows down body function, so (C) $\rightarrow$ IV
4. Cocaine acts as a stimulant and causes a sense of euphoria and increased energy, so (D) $\rightarrow$ I
5. Thus, (A) $\rightarrow$ II, (B) $\rightarrow$ III, (C) $\rightarrow$ IV, (D) $\rightarrow$ I

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 8 (Human Health and Disease) states that nicotine stimulates the adrenal gland to release adrenaline and nor-adrenaline (catecholamines) into blood circulation, so A-II.
2. Morphine, extracted from the latex of $Papaver\ somniferum$, is described as a very effective sedative and painkiller, so B-III.
3. Heroin (diacetylmorphine, smack) is described as a depressant that slows down body functions, so C-IV.
4. Cocaine, from $Erythroxylum\ coca$, interferes with dopamine transport and has a potent stimulating action on the CNS, producing a sense of euphoria and increased energy, so D-I.
5. A-II, B-III, C-IV, D-I matches option $3$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 63)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q151_20cd6ee3_30102026.png?v=20cd6ee37c3e)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q151_98be5e5d_30102026.png?v=98be5e5d5d92)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nicotine makes the adrenal gland release catecholamines. Morphine is the sedative painkiller. Heroin is a depressant. Cocaine is the stimulant that gives euphoria.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Most students pick option 2. You remember heroin as the drug that gives a rush. So you give it 'Causes sense of euphoria and increased energy'. That leaves the depressant line for cocaine. NCERT calls heroin a depressant that slows down body functions, and it gives cocaine the euphoria and increased energy.
- **Why:** You have to know the effect NCERT states for each drug. List II prints those effects, like 'A depressant; slows down body function'.
<!--/ecat-->

## Q152

Biology · both · Biotechnology and Its Applications

The human protein named $\alpha$-1-antitrypsin, obtained from transgenic animals, is used for the treatment of ______.

- **(1)** Emphysema
- (2) Alzheimer’s disease
- (3) Rheumatoid arthritis
- (4) Cystic fibrosis

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The human protein named $\alpha$-1-antitrypsin, obtained from transgenic animals, is used for the treatment of emphysema.
2. Transgenic models exist for the study of other diseases, such as Alzheimer's disease, rheumatoid arthritis and cystic fibrosis.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 12 (Biotechnology and its Applications) lists transgenic animals made to produce useful biological products, and names $\alpha$-1-antitrypsin, used to treat emphysema, among them.
2. The same passage mentions attempts to treat phenylketonuria and cystic fibrosis by this route, but the product tied to emphysema is $\alpha$-1-antitrypsin.
3. Hence option $1$.

**Subtopic:** Transgenic Animals · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 64)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q152_904e3440_30102026.png?v=904e344050f2)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q152_fceeb784_30102026.png?v=fceeb7844029)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Alpha-1-antitrypsin from transgenic animals is used against emphysema.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Most students pick option 4, cystic fibrosis. It sits in the same sentence of the source as the answer, the sentence saying trials are on for treating phenylketonuria and cystic fibrosis. So if you remember that sentence as one block but not which disease goes with which product, you pick it. What that sentence names cystic fibrosis for is a trial, not the use of $\alpha$-1-antitrypsin.
- **Why:** You need the stated use of one named transgenic product. You have to fill the blank in 'The human protein named $\alpha$-1-antitrypsin, obtained from transgenic animals, is used for the treatment of ______'.
<!--/ecat-->

## Q153

Biology · zoology · Animal Kingdom

Select the set of fishes which belong to the class Osteichthyes:

- (1) Devil fish, Cuttlefish and Hagfish
- (2) Saw fish, Fighting fish and Dog fish
- (3) Starfish, Hagfish and Cuttlefish
- **(4)** Flying fish, Angel fish and Fighting fish

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Flying fish (Exocoetus) is a marine bony fish. Angel fish (Pterophyllum) and fighting fish (Betta) are aquarium bony fishes.
2. Option (1) is incorrect as:-
3. Devil fish (Octopus) and cuttlefish (Sepia) are molluscs.
4. Hag fish (Myxine) is a cyclostome.
5. Option (2) is incorrect as:-
6. Saw fish (Pristis) and dog fish (Scoliodon) are cartilaginous fishes.
7. Option (3) is incorrect as:-
8. Star fish (Asterias) is an echinoderm.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 4 (Animal Kingdom) lists under Osteichthyes the marine $Exocoetus$ (flying fish) and $Hippocampus$ (sea horse), the freshwater $Labeo$, $Catla$ and $Clarias$, and the aquarium fishes $Betta$ (fighting fish) and $Pterophyllum$ (angel fish).
2. Saw fish ($Pristis$) and dog fish ($Scoliodon$) are listed under Chondrichthyes, and hagfish ($Myxine$) under Cyclostomata.
3. Devil fish ($Octopus$) and cuttlefish ($Sepia$) are molluscs and starfish ($Asterias$) is an echinoderm, so they are not fishes at all.
4. Only option $4$ contains three Osteichthyes members.

**Subtopic:** Class – Cyclostomata, Chondrichthyes and Osteichthyes · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 64)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q153_51c86993_30102026.png?v=51c86993fe20)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q153_423d8d97_30102026.png?v=423d8d97d986)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Osteichthyes are the bony fishes. The cartilaginous saw fish and dog fish are Chondrichthyes, and devil fish, cuttlefish, starfish and hagfish are not fishes at all.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. Saw fish and dog fish are real fishes. So if you test the set by asking whether all three are fishes, instead of whether all three are bony fishes, you accept it. Its fighting fish really is Osteichthyes. But saw fish and dog fish are cartilaginous. That puts them in the sister class and sinks the whole set.
- **Why:** You have to put named animals into a stated class. The question says 'Select the set of fishes which belong to the class Osteichthyes', and each option bundles three names that stand or fall together.
- **Note:** The four options are sets of three names. You accept or reject each set whole. No lettered statement block is printed.
<!--/ecat-->

## Q154

Biology · zoology · Animal Kingdom

Select the incorrect statements from the following:
Choose the answer from the options given below:

- **(A.)** Digestive system in Platyhelminthes is incomplete.
- **(B.)** Bilateral symmetry is a characteristic feature of adult Echinoderms.
- **(C.)** Pseudocoelom is possessed by Aschelminthes.
- **(D.)** Notochord is persistent throughout life in the class Chondrichthyes.
- **(E.)** Members of class Reptilia maintain a constant body temperature.

- (1) A and C only
- **(2)** B and E only
- (3) C and D only
- (4) B and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (A) $\rightarrow$ correct $\rightarrow$ Platyhelminthes have an incomplete digestive system.
2. (B) $\rightarrow$ incorrect $\rightarrow$ Bilateral symmetry is a characteristic feature of larvae of echinoderms. In adult echinoderms, radial symmetry is seen.
3. (C) $\rightarrow$ correct $\rightarrow$ Aschelminthes are characterised by the presence of pseudocoelom.
4. (D) $\rightarrow$ correct $\rightarrow$ Notochord is persistent throughout life in the Chondrichthyes.
5. (E) $\rightarrow$ incorrect $\rightarrow$ Reptiles are cold-blooded organisms and thus, they cannot maintain a constant body temperature.
6. Warm-blooded organisms like birds and mammals can maintain a constant body temperature.
7. Thus, as the incorrect statements are indicated by (B) and (E) only

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 11, Ch. 4 lists the digestive system of Platyhelminthes as incomplete (a single opening).
2. B is incorrect: NCERT states that adult echinoderms are radially symmetrical while their larvae are bilaterally symmetrical.
3. C is correct: the body cavity of Aschelminthes is not lined by mesoderm, so they are pseudocoelomates.
4. D is correct: of Chondrichthyes NCERT states that the notochord is persistent throughout life.
5. E is incorrect: NCERT states that reptiles are poikilotherms, i.e. they do not maintain a constant body temperature.
6. So the incorrect statements are B and E, option $2$.

**Subtopic:** Phylum – Echinodermata and Hemichordata, Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 64)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q154_78e0d291_30102026.png?v=78e0d291cfae)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q154_b5e18fa5_30102026.png?v=b5e18fa52050)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each animal group has lines that identify it. Adult echinoderms are radially symmetrical. Reptiles are poikilotherms. In a cartilaginous fish the notochord stays for life.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Most students pick option 4. You file a notochord that lasts through life under the cyclostomes and the protochordates. So it feels safe to deny it to the cartilaginous fishes, and you mark D as an error. But NCERT's own line for Chondrichthyes is that the notochord is persistent throughout life. The second incorrect statement is E, the reptile's constant body temperature.
- **Why:** You have to judge five statements, and the stem asks for the wrong ones. It says 'Select the incorrect statements from the following'. The incorrect pair is B, bilateral symmetry in adult echinoderms, and E.
<!--/ecat-->

## Q155

Biology · both · Cell: The Unit of Life

Non-membrane bound cell organelles found in both prokaryotic and eukaryotic cells are ______.

- **(1)** Ribosomes
- (2) Lysosomes
- (3) Centrosomes
- (4) Mitochondria

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ribosome is a non-membrane bound cell organelle, found in both prokaryotic and eukaryotic cells.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 8 (Cell: The Unit of Life) states that ribosomes are the granular structures first observed under the electron microscope and that they are not surrounded by any membrane.
2. It adds that the prokaryotic ribosome is 70S (50S + 30S) while eukaryotes have 80S (60S + 40S) ribosomes, so ribosomes occur in both cell types.
3. Lysosomes and mitochondria are membrane-bound and absent from prokaryotes, and the centrosome with its centrioles is confined to animal cells.
4. Hence option $1$.

**Subtopic:** Ribosomes And Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 65)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q155_b9a82593_30102026.png?v=b9a825932c6d)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q155_a0f5e4ff_30102026.png?v=a0f5e4ffe633)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ribosomes are the one organelle with no membrane around it that both prokaryotes and eukaryotes carry.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Most students pick option 3, the centrosome. Drop the question's words 'found in both prokaryotic and eukaryotic cells' and the centrosome answers what is left, because it really does have no membrane around it. But prokaryotes have no centrosome. The only organelle that meets both printed conditions is the ribosome.
- **Why:** You need an organelle that meets two stated conditions at once. The question says 'Non-membrane bound cell organelles found in both prokaryotic and eukaryotic cells', and one option meets only the first of them.
<!--/ecat-->

## Q156

Biology · botany · Organisms and Populations

Which of the following equations depicts Verhulst-Pearl logistic population growth?

- (1) $\dfrac{\mathrm{dN}}{\mathrm{dt}} = \mathrm{rN}\left(\dfrac{\mathrm{K} + \mathrm{N}}{\mathrm{K}}\right).$
- **(2)** $\dfrac{\mathrm{dN}}{\mathrm{dt}} = \mathrm{rN}\left(\dfrac{\mathrm{K} - \mathrm{N}}{\mathrm{K}}\right)$
- (3) $\dfrac{\mathrm{dN}}{\mathrm{dt}} = \mathrm{rN}\left(\dfrac{\mathrm{K} - \mathrm{N}}{\mathrm{N}}\right)$
- (4) $\dfrac{\mathrm{dN}}{\mathrm{dt}} = \mathrm{rN}\left(\dfrac{\mathrm{K}}{\mathrm{K} - \mathrm{N}}\right)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Verhulst-Pearl logistic population growth is depicted by the equation $\dfrac{\mathrm{dN}}{\mathrm{dt}} = \mathrm{rN}\left(\dfrac{\mathrm{K} - \mathrm{N}}{\mathrm{K}}\right)$
2. Where
3. $\mathrm{K}$ = Carrying capacity
4. $\mathrm{r}$ = Intrinsic rate of natural increase
5. $\mathrm{N}$ = Population density at time 't'

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 13 (Organisms and Populations) gives the Verhulst-Pearl logistic growth equation as $\frac{dN}{dt} = rN\left(\frac{K-N}{K}\right)$, where $N$ is population density at time $t$, $r$ the intrinsic rate of natural increase and $K$ the carrying capacity.
2. The form is checked by its limits: when $N \ll K$ the bracket tends to $1$ and growth is nearly exponential; when $N = K$ the bracket is $0$ and growth stops, giving the sigmoid curve.
3. Options 1, 3 and 4 fail these limits (option 4 even diverges as $N \to K$), so option $2$.

**Subtopic:** Logistic Growth · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 65)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q156_c1f68520_30102026.png?v=c1f6852033bd)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q156_67a68572_30102026.png?v=67a6857284e4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The logistic equation carries the brake term $\frac{K-N}{K}$. That is the unused part of the carrying capacity, and it falls to zero as $N$ reaches $K$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. You hold the bracket's two parts, $K$ and $K-N$, more firmly than you hold which one goes on top, and option 4 prints them the other way up. Upside down the term grows without limit as $N$ gets close to $K$. But that is exactly where the logistic curve has to flatten out to no growth at all.
- **Why:** You need the stated form of a named equation. All four options carry the same symbols $r$, $N$ and $K$, and they differ only in the bracket.
<!--/ecat-->

## Q157

Biology · zoology · Body Fluids and Circulation

Select the incorrect statement with reference to Rh grouping.
Choose the answer from the options given below :

- **(A.)** Erythroblastosis foetalis is a condition observed having foetus with $\mathrm{Rh^{-ve}}$ blood and mother with $\mathrm{Rh^{+ve}}$ blood.
- **(B.)** Rh antigen is observed on RBCs in the majority of human beings.
- **(C.)** Before blood transfusion, Rh group should also be matched.
- **(D.)** Rh incompatibility is observed when a pregnant mother is $\mathrm{Rh^{-ve}}$ and the foetus is $\mathrm{Rh^{+ve}}$.
- **(E.)** Erythroblastosis foetalis can be avoided by administering anti-Rh antibodies to the mother immediately after the delivery of the second child.

- (1) C and D only
- (2) A and B only
- **(3)** A and E only
- (4) B and C only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (A) Incorrect $\rightarrow$ A special case of Rh incompatibility has been observed between the $\mathrm{Rh^{-ve}}$ blood of  a pregnant mother with $\mathrm{Rh^{+ve}}$ blood of the foetus.
2. (B) Correct $\rightarrow$ Rh antigen is observed on the surface of RBCs of majority (nearly $80$ percent) of humans.
3. (C) Correct $\rightarrow$ Before blood transfusion, Rh group should also be matched to avoid severe problems of destruction of RBCs.
4. (D) Correct $\rightarrow$ Rh incompatibility (Erythroblastosis foetalis) is observed when a pregnant mother is $\mathrm{Rh^{-ve}}$ and the foetus is $\mathrm{Rh^{+ve}}$.
5. (E) Incorrect $\rightarrow$ Erythroblastosis foetalis can be avoided by administering anti-Rh antibodies to the mother immediately after the delivery of the first child.
6. Thus, the incorrect statements are (A) and (E).

**Solved independently** (answer withheld)

1. A is incorrect: NCERT Class 11, Ch. 18 (Body Fluids and Circulation) describes erythroblastosis foetalis as arising when the mother is $Rh^{-ve}$ and the foetus $Rh^{+ve}$; statement A reverses the two.
2. B is correct: the Rh antigen is observed on the surface of RBCs of the majority (nearly $80$ per cent) of humans.
3. C is correct: NCERT states that the Rh group should also be matched before transfusion, alongside the ABO group.
4. D is correct: Rh incompatibility is precisely the $Rh^{-ve}$ mother with an $Rh^{+ve}$ foetus.
5. E is incorrect: NCERT states this can be avoided by administering anti-Rh antibodies to the mother immediately after the delivery of the first child, not the second.
6. So the incorrect statements are A and E, option $3$.

**Subtopic:** Blood Group and Rh Group · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 65)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q157_a3738b61_30102026.png?v=a3738b619dc5)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q157_8674e558_30102026.png?v=8674e5581f25)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Rh incompatibility needs an Rh-negative mother carrying an Rh-positive foetus. Anti-Rh antibodies are given right after the first delivery.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. Statement E is NCERT's sentence on anti-Rh antibodies with one word changed, 'second child' in place of 'first child'. The sentence looks familiar, so you read straight through it and accept it. Then you have to find the second incorrect statement somewhere else. You do catch A, which has the mother and the foetus the wrong way round. But you also mark B, and B is NCERT's own line. The Rh antigen is on the red cells of about 80 per cent of people.
- **Why:** You have to judge five statements, and the stem asks for the wrong ones. It says 'Select the incorrect statement with reference to Rh grouping'. The incorrect pair is A and E.
- **Note:** Options 1 and 4 are made of true statements only. You reach them by reading the task as 'which are correct'.
<!--/ecat-->

## Q158

Biology · botany · Microbes in Human Welfare

Match List I with List II:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Streptokinase | I. | Immunosuppressive agent |
| B. | Statins | II. | Removal of clots from the blood vessels |
| C. | Lipases | III. | Blood cholesterol-lowering agent |
| D | Cyclosporin A | IV | Detergent formulations |

- (1) A–II, B–III, C–I, D–IV
- (2) A–IV, B–III, C–II, D–I
- (3) A–III, B–II, C–IV, D–I
- **(4)** A–II, B–III, C–IV, D–I

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Streptokinase $\rightarrow$ Used as 'clot buster' for removing clots from the blood vessels
2. Statins $\rightarrow$ Blood cholesterol lowering agent, produced by Monascus purpureus
3. Lipases $\rightarrow$ Used in detergent formulation
4. Cyclosporin A $\rightarrow$ Used as immunosuppressive agent in organ transplant patients and produced by Trichoderma polysporum

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 10 (Microbes in Human Welfare) states that streptokinase, produced by $Streptococcus$ and modified by genetic engineering, is used as a clot buster for removing clots from the blood vessels of patients who have had myocardial infarction, so A-II.
2. Statins, produced by the yeast $Monascus\ purpureus$, act as blood-cholesterol lowering agents by competitively inhibiting the enzyme responsible for cholesterol synthesis, so B-III.
3. Lipases are used in detergent formulations and are helpful in removing oily stains from laundry, so C-IV.
4. Cyclosporin A, produced by the fungus $Trichoderma\ polysporum$, is used as an immunosuppressive agent in organ transplantation, so D-I.
5. A-II, B-III, C-IV, D-I matches option $4$.

**Subtopic:** Chemicals, Enzymes and Other Bioactive Molecules · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 66)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q158_9fba234b_30102026.png?v=9fba234ba49a)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q158_e202a713_30102026.png?v=e202a71364e5)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Microbes give us useful medicines. Streptokinase dissolves clots. Statins lower blood cholesterol. Cyclosporin A suppresses immunity. Lipases go into detergents.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. Streptokinase and statins are the only two heart medicines in the chapter. You hold them as one pair, so you can put either line on either name. Option 3 is that swap. Streptokinase is the clot buster and it comes from Streptococcus. The cholesterol-lowering statin comes from Monascus purpureus.
- **Why:** You have to know the use NCERT states for each microbial product. List II is made of those uses, like 'Removal of clots from the blood vessels' and 'Blood cholesterol-lowering agent'.
<!--/ecat-->

## Q159

Biology · zoology · Breathing and Exchange of Gases

Match List I with List II:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Molluscs | I. | Pulmonary respiration only |
| B. | Reptiles | II. | Branchial respiration |
| C. | Adult amphibians | III. | Cellular respiration |
| D | Amoeba | IV | Pulmonary and cutaneous respiration |

- **(1)** A–II, B–I, C–IV, D–III
- (2) A–I, B–II, C–IV, D–III
- (3) A–II, B–I, C–III, D–IV
- (4) A–III, B–II, C–I, D–IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (A) Molluscs $\rightarrow$ (II) Perform branchial respiration by using feather-like gills
2. (B) Reptiles $\rightarrow$ (I) Perform pulmonary respiration only via lungs
3. (C) Adult amphibians $\rightarrow$ (IV) Perform pulmonary and cutaneous respiration via lungs and moist skin, respectively
4. (D) Amoeba $\rightarrow$ (III) Performs cellular respiration to generate ATP for survival
5. Thus, (A) - II, (B) - I, (C) - IV, (D) - III

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 17 (Breathing and Exchange of Gases) states that special vascularised structures called gills (branchial respiration) are used by most aquatic arthropods and molluscs, so A-II.
2. It states that among vertebrates reptiles, birds and mammals respire through lungs, i.e. pulmonary respiration only, so B-I.
3. It states that amphibians like the frog can respire through their moist skin (cutaneous respiration) as well as through lungs, so C-IV.
4. $Amoeba$, a single-celled organism, exchanges gases directly across its cell surface, leaving D-III.
5. A-II, B-I, C-IV, D-III matches option $1$.

**Subtopic:** Respiratory Organs in Animals · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 66)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q159_304effe6_30102026.png?v=304effe63f2d)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q159_748901cf_30102026.png?v=748901cfc6db)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Molluscs breathe by gills. Reptiles breathe by lungs only. An adult frog uses lungs and its moist skin. Amoeba exchanges gas straight across its surface.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Two of the four options already agree that molluscs have gills and reptiles have lungs. So you only have to decide the last pair. The other choice there gives Amoeba 'Pulmonary and cutaneous respiration'. That would be a single-celled animal with lungs, and you would never accept it. The one option that does swap gills and lungs has to give reptiles branchial respiration. NCERT says in one sentence that reptiles, birds and mammals respire through lungs. So nothing really pulls you away.
- **Why:** You have to know the way of breathing NCERT gives each group. List II is made of those routes, like 'Branchial respiration' and 'Pulmonary and cutaneous respiration'.
- **Note:** 'Cellular respiration' in List II is the only entry left for Amoeba. NCERT does not use that name for it. It describes that kind of exchange as simple diffusion over the body surface.
<!--/ecat-->

## Q160

Biology · both · Principles of Inheritance and Variation

The sixth mutant codon of beta globin gene causing polymerization of Haemoglobin and change in RBC shape is ______.

- **(1)** GUG
- (2) AUG
- (3) GAG
- (4) CAG

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Sickle cell anaemia is an autosomal recessive disorder which is caused by the substitution of Glutamic acid by Valine, at the sixth position of the beta globin chain of the haemoglobin molecule. The substitution of amino acid in the globin protein results due to the single base substitution from GAG to GUG. Hence, GUG is responsible for the change in the shape of RBC.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 5 (Principles of Inheritance and Variation) states that sickle-cell anaemia arises from the substitution of glutamic acid by valine at the sixth position of the beta globin chain.
2. The same passage traces this to a single base substitution at the sixth codon of the beta globin gene, from GAG to GUG.
3. The mutant haemoglobin $HbS$ polymerises under low oxygen tension and changes the biconcave red blood cell into a sickle shape.
4. GAG is the normal (wild-type) codon, so the mutant codon asked for is GUG, option $1$.

**Subtopic:** Sickle-cell Anaemia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 67)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q160_3d4fb90c_30102026.png?v=3d4fb90c52af)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q160_64acbfd0_30102026.png?v=64acbfd07610)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sickling comes from one codon change at the sixth position of the beta globin gene: GAG to GUG, glutamic acid to valine.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Most students pick option 3, GAG. GAG is the sixth codon of the normal beta globin gene. So if you remember the pair GAG and GUG but not which side of the arrow each one is on, you pick it. GAG answers what the codon was before the mutation. The question asks for the mutant one.
- **Why:** You need the stated mutant codon. The question says 'The sixth mutant codon of beta globin gene', and both the normal and the mutant codon are printed among the options.
<!--/ecat-->

## Q161

Biology · zoology · Locomotion and Movement

Choose the correct statements regarding muscle contraction.
Choose the correct answer from the options given below :

- **(A.)** A motor neuron carries a signal sent by the Central Nervous System (CNS) to the sarcolemma of the muscle fibre.
- **(B.)** The neural signal generates an action potential which causes the release of $\mathrm{Ca^{++}}$ into sarcoplasm.
- **(C.)** Increase in $\mathrm{Ca^{++}}$ inactivates the actin for breaking cross bridges.
- **(D.)** Actin binds to the myosin head to form a cross bridge.
- **(E.)** Shortening of sarcomere takes place, by pulling actin filaments towards the centre of 'A' band.

- (1) C and D only
- (2) A and B only
- (3) C and E only
- **(4)** A, B, D and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Statements A, B, D and E are correct while statement C is incorrect.
2. A neural signal reaching neuromuscular junction releases a neurotransmitter (Acetylcholine) which generates an action potential in the sarcolemma. This spreads through muscle fibre and causes the release of $\mathrm{Ca^{++}}$ into the sarcoplasm. This $\mathrm{Ca^{++}}$ binds to the subunit of troponin on actin filaments and thereby remove the masking of active site for myosin on actin and hence facilitates the formation of cross bridge.

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 11, Ch. 20 (Locomotion and Movement) states that muscle contraction is initiated by a signal sent by the central nervous system via a motor neuron, reaching the neuromuscular junction on the sarcolemma.
2. B is correct: the neural signal generates an action potential in the sarcolemma which spreads through the muscle fibre and causes the release of calcium ions into the sarcoplasm.
3. C is incorrect: the increase in $Ca^{++}$ leads to binding of calcium with a subunit of troponin on actin filaments and thereby removes the masking of the active sites for myosin; it activates, not inactivates, the actin.
4. D is correct: using energy from ATP hydrolysis, the myosin head binds to the exposed active sites on actin to form a cross bridge.
5. E is correct: the cross bridge pulls the attached actin filaments towards the centre of the 'A' band, shortening the sarcomere.
6. So A, B, D and E only, option $4$.

**Subtopic:** Mechanism of Muscle Contraction and Red and White Muscle Fibre · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 67)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q161_35157ae2_30102026.png?v=35157ae25c4f)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q161_34e0e0df_30102026.png?v=34e0e0dffd99)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Muscle contraction goes step by step. The motor neuron signals the sarcolemma. An action potential spreads. Calcium is released. A cross bridge forms between actin and the myosin head. The sarcomere shortens.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. NCERT's sentence has the myosin head binding to the exposed sites on actin. Statement D says the same thing from the actin side, and you read that as the sentence turned round, so you reject it. No printed set gives you A, B and E without D. D describes the same cross bridge, just from the other side. Leaving it out gives a set that is true but two statements short.
- **Why:** You have to judge five statements against NCERT's account of contraction. Only one of them is false, 'Increase in $\mathrm{Ca^{++}}$ inactivates the actin for breaking cross bridges'. So the four-statement option is the one that holds.
<!--/ecat-->

## Q162

Biology · zoology · Locomotion and Movement

Which of the following statements are correct with reference to human endoskeleton?
Choose the correct answer from the options given below:

- **(A.)** Human skull is monocondylic.
- **(B.)** The joint between any two adjoining vertebrae is a cartilaginous joint.
- **(C.)** In human beings, the number of cervical vertebrae is seven.
- **(D.)** All ribs except the last 2 pairs are bicephalic.
- **(E.)** The occipital bone of skull is articulated with atlas vertebra.

- (1) B and E only
- **(2)** B, C and E only
- (3) C, D and E only
- (4) A, B and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (A) Incorrect : Human skull is dicondylic. The skull region articulates with the superior region of the vertebral column (Atlas) with the help of two occipital condyles.
2. (B) Correct : The joint present between the adjacent vertebrae of vertebral column is cartilaginous joints.
3. (C) Correct : There are $7$ cervical vertebrae in human beings.
4. (D) Incorrect : All ribs of humans are bicephalic, i.e., they have two articulation surfaces on their dorsal end.
5. (E) Correct : The occipital bone of the skull articultes with the atlas vertebra via occipital condyles, forming the atlanto-occiptal joint.

**Solved independently** (answer withheld)

1. A is incorrect: NCERT Class 11, Ch. 20 (Locomotion and Movement) states that a pair of occipital condyles is present, so the human (mammalian) skull is dicondylic, not monocondylic.
2. B is correct: among cartilaginous joints NCERT gives the joint between the adjacent vertebrae in the vertebral column.
3. C is correct: NCERT states the number of cervical vertebrae is seven in almost all mammals including human beings.
4. D is incorrect: NCERT states that each rib has two articulation surfaces on its dorsal end and is hence called bicephalic, with no exception made for the last two (floating) pairs.
5. E is correct: the occipital condyles of the skull articulate with the first vertebra, the atlas.
6. So B, C and E only, option $2$.

**Subtopic:** Axial Skeleton · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 67)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q162_e52312ca_30102026.png?v=e52312ca232f)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q162_7902c5d7_30102026.png?v=7902c5d7291a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Some facts about the human skeleton. The skull is dicondylic and rests on the atlas. There are seven cervical vertebrae. The joints between vertebrae are cartilaginous. Every rib is bicephalic.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3. The last two pairs of ribs really are NCERT's exception, but for a different reason. They are the floating ribs and they join no sternum in front. You carry that exception across to bicephaly and accept statement D. But each rib has two articulation surfaces on its dorsal end, so all of them are bicephalic.
- **Why:** You have to judge five statements about the human skeleton. The stem says 'Which of the following statements are correct with reference to human endoskeleton?'. Statement D borrows the printed exception, 'All ribs except the last 2 pairs are bicephalic'.
<!--/ecat-->

## Q163

Biology · zoology · Human Reproduction

Spermatogonia undergo a series of cell divisions statements to produce sperms. Select the correct from the following :
Choose the correct answer from the options given below:

- **(A.)** Spermatogonia always undergo meiotic cell division.
- **(B.)** Primary spermatocytes divide mitotically to produce secondary spermatocytes.
- **(C.)** Secondary spermatocytes, through their second meiotic division, produce haploid spermatids.
- **(D.)** Spermatids produce spermatozoa through mitosis.
- **(E.)** Spermatids transform into spermatozoa by spermiogenesis.

- (1) A and E only
- **(2)** C and E only
- (3) A, C and E only
- (4) B, C and D only

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. (A) Incorrect : Spermatogonia undergo mitotic differentiation.
2. (B) Incorrect : Primary spermatocytes undergo $1^{\mathrm{st}}$ meiotic division to form secondary spermatocytes.
3. (C) Correct : Secondary spermatocytes undergo $2^{\mathrm{nd}}$ meiotic division to form the haploid spermatids.
4. (D) Incorrect : Spermatids form spermatozoa through a differentiation process called spermiogenesis.
5. (E) Correct : Spermatids produce spermatozoa via spermiogenesis.
6. Thus, the correct statements are (C) and (E) only.

**Solved independently** (answer withheld)

1. A is incorrect: NCERT Class 12, Ch. 3 (Human Reproduction) states that spermatogonia on the inside wall of the seminiferous tubules multiply by mitotic division; only some of them, as primary spermatocytes, periodically undergo meiosis.
2. B is incorrect: the primary spermatocyte completes the first meiotic division to form two equal haploid secondary spermatocytes, not a mitotic division.
3. C is correct: the secondary spermatocytes undergo the second meiotic division to produce four equal haploid spermatids.
4. D is incorrect: spermatids do not divide at all; they are transformed into spermatozoa.
5. E is correct: NCERT names this transformation of spermatids into spermatozoa spermiogenesis.
6. So C and E only, option $2$.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 68)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q163_0663b87c_30102026.png?v=0663b87c9553)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q163_b5da668d_30102026.png?v=b5da668da079)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Spermatogenesis goes like this. Spermatogonia multiply by mitosis. Primary spermatocytes do the first meiotic division. Secondary spermatocytes do the second. Then spermiogenesis reshapes the spermatids.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Most students pick option 3. Spermatogonia do enter meiosis, as the primary spermatocytes they become. So you read past the word 'always', accept statement A and take the set of three. NCERT has the spermatogonia multiplying by mitotic division. Only some of them go into meiosis, and only now and then.
- **Why:** You have to judge five statements against NCERT's account of sperm formation. One word breaks statement A, 'Spermatogonia always undergo meiotic cell division'.
<!--/ecat-->

## Q164

Biology · zoology · Excretory Products and Their Elimination

The JGA (Juxta Glomerular Apparatus) is a special sensitive region formed by cellular modifications in _______ related to the same nephron.

- (1) Distal convoluted tubule and efferent renal arteriole
- (2) Proximal convoluted tubule and efferent renal arteriole
- (3) Proximal convoluted tubule and afferent renal arteriole
- **(4)** Distal convoluted tubule and afferent renal arteriole

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. JGA is a special sensitive region formed by cellular modifications in the distal convoluted tubule and the afferent arteriole at the location of their contact.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 19 (Excretory Products and their Elimination) states that at the location of contact of the distal convoluted tubule with the afferent arteriole of the same nephron, the cells of both are modified.
2. This specialised sensitive region is called the juxta glomerular apparatus (JGA), whose JG cells release renin when glomerular blood pressure falls.
3. The efferent arteriole and the proximal convoluted tubule are not involved, so option $4$.

**Subtopic:** Human Excretory System · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 68)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q164_82fdcd3a_30102026.png?v=82fdcd3ae70a)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q164_f1f77624_30102026.png?v=f1f776244304)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The juxtaglomerular apparatus is where the distal convoluted tubule touches the afferent arteriole of its own nephron.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Most students pick option 1. It has the tubule right and loses the vessel. Afferent and efferent differ by one prefix, and if you picture the apparatus acting on the blood leaving the glomerulus you take the efferent one. But the apparatus senses the filtrate and adjusts the inflow. So the arteriole it is built into is the one bringing blood in.
- **Why:** You need both halves of a named anatomical site. The four options cross the two tubule names with the two arteriole names.
- **Note:** The answer names one site made of two structures. It is not two separate answers matched one to one. So the shape stays mcq, and the two-part pull is carried on the trap instead.
<!--/ecat-->

## Q165

Biology · botany · Organisms and Populations

Which one of the following is an appropriate example of sexual deceit?

- (1) Female wasp and fig
- **(2)** Ophrys and bumblebee
- (3) Sea anemone and clown fish
- (4) Cuckoo and crow

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Female wasp and fig - Mutualism
2. Ophrys and bumblebee - Sexual deceit
3. Sea anemone and clown fish - Commensalism
4. Cuckoo and crow - Brood Parasitism

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 13 (Organisms and Populations) states that the Mediterranean orchid $Ophrys$ employs 'sexual deceit': one of its petals bears an uncanny resemblance to the female of the bee species in size, colour and markings.
2. The male bee is attracted to what it perceives as a female, pseudocopulates with the flower and, dusted with pollen, pollinates the next flower it visits.
3. The fig and wasp relation is obligate mutualism, sea anemone and clown fish is commensalism, and cuckoo laying eggs in a crow's nest is brood parasitism.
4. Hence option $2$.

**Subtopic:** Mutualism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 68)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q165_a6139ec6_30102026.png?v=a6139ec6dcdc)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q165_ba5916e6_30102026.png?v=ba5916e6f133)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sexual deceit: the Ophrys flower mimics a female bee, so the male tries to copulate with it and the flower gets pollinated.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Most students pick option 4. Drop the word 'sexual' and a cuckoo laying its eggs in a crow's nest is the chapter's other case of one species fooling another. So if you read only 'deceit', you mark it. What makes Ophrys the sexual case is that the flower imitates the female bee and the male tries to copulate with it.
- **Why:** You need an example that meets the stated qualifier. The question asks for 'an appropriate example of sexual deceit', and brood parasitism and a mutualism are also among the options.
<!--/ecat-->

## Q166

Biology · zoology · Structural Organisation in Animals

Choose the correct statements regarding frog’s anatomy:
Choose the correct answer from the options given below:

- **(A.)** Hepatic portal system is the special venous connection between liver and intestine.
- **(B.)** There are twelve pairs of cranial nerves arising from the brain.
- **(C.)** The ureters and oviducts open separately into the cloaca in female frogs.
- **(D.)** Hind-brain consists of cerebellum, medulla oblongata and optic lobes.
- **(E.)** Sinus venosus joins the right atrium of heart.

- (1) A, B and C only
- (2) B and D only
- (3) B and C only
- **(4)** A, C and E only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. A. Correct $\rightarrow$ In frogs, the special venous connection between liver and intestine is called the hepatic portal system.
2. B. Incorrect $\rightarrow$ There are ten pairs of cranial nerves arising from the brain of frog.
3. C. Correct $\rightarrow$ In female frogs, the uterus and oviduct open separately in the cloaca.
4. D. Incorrect $\rightarrow$ In frogs, the midbrain consists of the optic lobes.
5. The hindbrain consists of cerebellum, and medulla oblongata.
6. E. Correct $\rightarrow$ In frogs, a triangular structure called sinus venosus joins the right atrium.
7. Thus, correct statements are (A), (C) and (E)

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 11, Ch. 7 (Structural Organisation in Animals) states that the special venous connection between liver and intestine is called the hepatic portal system, and that between kidney and the lower parts of the body the renal portal system.
2. B is incorrect: NCERT states that ten pairs of cranial nerves arise from the frog's brain; twelve pairs is the mammalian number.
3. C is correct: the oviduct arising from each ovary opens into the cloaca separately, so ureters and oviducts have separate cloacal openings in the female frog.
4. D is incorrect: the mid-brain is characterised by a pair of optic lobes, while the hind-brain consists of the cerebellum and medulla oblongata only.
5. E is correct: the frog's heart has two atria and one ventricle, and a triangular structure called the sinus venosus joins the right atrium.
6. So A, C and E only, option $4$.

**Subtopic:** Anatomy of Frog · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 68)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q166_20177702_30102026.png?v=2017770213f9)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q166_42638ff4_30102026.png?v=42638ff4a42c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Some facts about frog anatomy. The hepatic portal vein runs between liver and intestine. The frog has ten pairs of cranial nerves. The optic lobes are in the midbrain. The sinus venosus opens into the right atrium.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Most students pick option 1. Twelve pairs of cranial nerves is the human figure. You carry it across to the frog and accept statement B next to the two true ones. NCERT gives the frog ten pairs of cranial nerves.
- **Why:** You have to judge five statements about frog anatomy. The stem says 'Choose the correct statements regarding frog's anatomy'. Statement B prints a number, 'twelve pairs of cranial nerves'.
<!--/ecat-->

## Q167

Biology · zoology · Human Reproduction

Match List I with List II related to embryonic development at various months of pregnancy:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | The foetus movement starts and hair appears on the head | (I) | 24 weeks of pregnancy |
| B. | The foetus develops limbs and digits | (II) | 20 weeks of pregnancy |
| C. | The foetus develops external genital organs | (III) | 8 weeks of pregnancy |
| D. | The foetus body is covered with fine hair; eyelids separate and eyelashes are formed | (IV) | 12 weeks of pregnancy |

- (1) A-IV, B-II, C-III, D-I
- **(2)** A-II, B-III, C-IV, D-I
- (3) A-III, B-II, C-IV, D-I
- (4) A-II, B-IV, C-III, D-I

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. By the end of second month of pregnancy ($8$ weeks), the foetus develops limbs and digits
2. By the end of $12$ weeks (first trimester) of pregnancy, most of the major organ system are formed. The limbs and external genital organs are also well developed.
3. During the fifth month ($20$ weeks) of pregnancy, the first movements of the foetus and appearance of hair on the head are usually observed.
4. By the end of about $24$ weeks (ends of second trimester) of pregnancy, the body is covered with fine hair, eye lids separate and eyelashes are formed.
5. So, the correct match is A-II, B-III, C-IV, D-I

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 3 (Human Reproduction) states that by the end of the second month of pregnancy the foetus develops limbs and digits, so B-(III), 8 weeks.
2. It states that by the end of 12 weeks (first trimester) most of the major organ systems are formed, for example the limbs and external genital organs are well developed, so C-(IV).
3. It states that the first movements of the foetus and the appearance of hair on the head are usually observed during the fifth month, i.e. about 20 weeks, so A-(II).
4. It states that by the end of 24 weeks (second trimester) the body is covered with fine hair, the eyelids separate and eyelashes are formed, so D-(I).
5. A-(II), B-(III), C-(IV), D-(I) matches option $2$.

**Subtopic:** Implantation and Embryonic Development · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 69)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q167_cf13adbb_30102026.png?v=cf13adbb090e)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q167_71c67451_30102026.png?v=71c6745115d5)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Foetal development has dated milestones. Limbs and digits form by 8 weeks. External genitals form by 12 weeks. The first movements and head hair come by 20 weeks. Fine body hair and separated eyelids come by 24 weeks.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. NCERT's line for the end of 12 weeks says the limbs and the external genital organs are both well developed. You remember limbs from that one sentence. So you pair 'The foetus develops limbs and digits' with 12 weeks. But limbs and digits are the second-month event, which is the 8-week entry. 12 weeks is left for the external genital organs.
- **Why:** You have to know the week NCERT attaches to each event. List II is just those weeks, like '8 weeks of pregnancy' and '12 weeks of pregnancy'.
<!--/ecat-->

## Q168

Biology · both · Principles of Inheritance and Variation

In a population of a grasshopper species, the chromosome number of some members is 23 and some other members possess 24 chromosomes. The 23 and 24 chromosome-bearing members in this species are ______.

- (1) females and males, respectively
- (2) all males
- **(3)** males and females, respectively
- (4) all females

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In grasshopper sex determination is XX - XO type, in which, males have only one X-chromosome besides the autosome (XO), whereas females have a pair of X-chromosome, besides autosomes (XX).
2. Therefore, the individual with $23$ chromosomes is a male grasshopper and the one with $24$ chromosomes is a female grasshopper.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 5 (Principles of Inheritance and Variation) describes the XO type of sex determination, using the grasshopper as its example.
2. In this type all eggs bear an X chromosome, while half the sperms carry an X and the other half carry none.
3. An egg fertilised by a sperm with X gives a female with two X chromosomes; an egg fertilised by a sperm without a sex chromosome gives a male with only one X.
4. So the male has one chromosome fewer than the female: $23$ chromosomes in males and $24$ in females.
5. The members with $23$ and $24$ chromosomes are therefore males and females respectively, option $3$.

**Subtopic:** Sex Determination in Birds, Insects & Honey Bee · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 69)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q168_ad97ff67_30102026.png?v=ad97ff6768fb)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q168_d9480a23_30102026.png?v=d9480a23609c)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Grasshoppers are XO. The male carries one sex chromosome, and so one chromosome fewer in total than the female.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Most students pick option 1. If you carry the line 'in some animals it is the female that has the odd complement', which is true of birds and butterflies, you give the 23 to females. That lands you on option 1, the right pair the wrong way round. In grasshoppers the male is the XO sex. So 23 is the male count and 24 is the female's.
- **Why:** You have to apply the XO rule to the two counts the question prints. The question says 'the chromosome number of some members is 23 and some other members possess 24', and the options assign the two counts to the two sexes.
<!--/ecat-->

## Q169

Biology · both · Principles of Inheritance and Variation

In which animal do haploid cells divide mitotically to produce gametes?

- **(1)** Male honeybees
- (2) Male earthworms
- (3) Male frogs
- (4) Male grasshoppers

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The male honeybee is haploid and females are diploid. The gamete formation in female honey bee is by meiosis, whereas male honeybee form gametes by mitosis. Thus haploid cell undergoes mitosis in male honeybees.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 5 (Principles of Inheritance and Variation) states that the male honeybee develops from an unfertilised egg by parthenogenesis and is therefore haploid.
2. It adds that the males produce sperms by mitosis, because a haploid cell cannot undergo a reduction division.
3. Earthworms, frogs and grasshoppers are diploid animals whose germ cells form gametes by meiosis.
4. Hence option $1$.

**Subtopic:** Sex Determination in Birds, Insects & Honey Bee · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 70)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q169_d22857ea_30102026.png?v=d22857ea40d8)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q169_5cbc9c57_30102026.png?v=5cbc9c57b3d6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A honeybee drone develops from an unfertilised egg and is haploid in every cell. So it makes its sperm by mitosis, not by meiosis.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Most students pick option 4, the grasshopper. Male grasshoppers are XO, so they carry one chromosome fewer than females. If you read 'one short of the full set' as haploid, you reach for them. But an XO male is still diploid for every other pair, and it makes sperm by meiosis. Only the drone is haploid in every cell, because it came from an unfertilised egg.
- **Why:** You need one stated fact: which animal has haploid males. The question asks 'In which animal do haploid cells divide mitotically to produce gametes?', and the options are the males of four animals.
<!--/ecat-->

## Q170

Biology · zoology · Human Reproduction

Arrange the following cell layers/structures around the female gamete, from outer to inner side :
Choose the correct answer from the options given below :

- **(A.)** Zona pellucida
- **(B.)** Perivitelline space
- **(C.)** Corona radiata
- **(D.)** Plasma membrane of ovum

- (1) D, B, A, C
- (2) C, A, D, B
- **(3)** C, A, B, D
- (4) A, C, B, D

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The cell layer/structure around the female gamete from outer to inner side is :
2. Corona radiata $\rightarrow$ zona pellucida $\rightarrow$ perivitelline space $\rightarrow$ plasma membrane of ovum.
3. So the correct answer is C, A, B, D.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 3 (Human Reproduction) shows the ovulated secondary oocyte surrounded by the corona radiata, the outermost layer of follicular cells, so C comes first.
2. Inside it lies the new membranous layer, the zona pellucida, so A is second.
3. Between the zona pellucida and the oocyte's own membrane is the fluid-filled perivitelline space, so B is third.
4. Innermost is the plasma membrane of the ovum itself, so D is last.
5. The order C, A, B, D is option $3$.

**Subtopic:** Female Gametogenesis (Oogenesis) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q170_7e8bff89_30102026.png?v=7e8bff89e165)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q170_26cbfeb1_30102026.png?v=26cbfeb15072)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The coats of the ovum from outside in. Corona radiata, then zona pellucida, then the perivitelline space, then the ovum's own plasma membrane.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Most students pick option 2. The space is named for the vitelline membrane it surrounds. You take it for a gap lying inside that membrane. So you put the plasma membrane of the ovum before it. The perivitelline space lies between the zona pellucida and the plasma membrane. So the membrane is the innermost of the four.
- **Why:** You have to put four named layers in order from outside to inside. The stem says 'Arrange the following cell layers/structures around the female gamete, from outer to inner side'.
<!--/ecat-->

## Q171

Biology · botany · Microbes in Human Welfare

What is the reason behind production of large holes in ‘Swiss Cheese’?

- **(1)** The production of large amount of $\mathrm{CO_2}$ by $\mathit{Propionibacterium\ sharmanii}$
- (2) The production of large amount of $\mathrm{CO_2}$ by $\mathit{Clostridium\ butylicum}$
- (3) The production of large amount of $\mathrm{CO_2}$ and $\mathrm{H_2}$ by lactic acid bacteria called $\mathit{Lactobacillus}$
- (4) The production of large amount of $\mathrm{CO_2}$ and $\mathrm{H_2}$ by $\mathit{Trichoderma\ polysporum}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The large holes in swiss cheese are due to production of large amount of $\mathrm{CO_2}$ by the bacterium Propionibacterium sharmanii.
2. Clostridium butylicum is commercially utilised for butyric acid production.
3. Curd is formed by Lactobacillus.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 10 (Microbes in Human Welfare) states that the large holes in 'Swiss cheese' are due to the production of a large amount of $CO_2$ by a bacterium named $Propionibacterium\ sharmanii$.
2. $Lactobacillus$ is used to curdle milk into curd, and the strong flavour of Roquefort cheese comes from ripening with a fungus.
3. $Trichoderma\ polysporum$ is the source of cyclosporin A, not a cheese organism.
4. Hence option $1$.

**Subtopic:** Microbes in Household Products · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 70)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q171_5597fbe1_30102026.png?v=5597fbe164c2)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q171_8acdf3d6_30102026.png?v=8acdf3d6e7d6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The large holes in Swiss cheese come from the $\mathrm{CO_2}$ given off by Propionibacterium sharmanii.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Most students pick option 3, Lactobacillus. It is the bacterium every dairy fermentation in the chapter is attached to, curd above all. So if you know cheese is the work of a lactic acid bacterium, you pick the organism you can name. But the holes are made by a different bacterium, Propionibacterium sharmanii, and by $\mathrm{CO_2}$ alone.
- **Why:** You need one stated fact: which organism gives a named product its texture. The question asks for 'the reason behind production of large holes in Swiss Cheese', and the four options are four named microbes, each paired with a gas.
<!--/ecat-->

## Q172

Biology · both · Biotechnology and Its Applications

The toxin proteins isolated from $\mathit{Bacillus\ thuringiensis}$, coded by which of the following genes would contrl cotton bollworms and corn borer, respectively?

- **(1)** $\mathit{cryIAc}$ and $\mathit{cryIAb}$
- (2) $\mathit{cryIAc}$ and $\mathit{cryIIAb}$
- (3) $\mathit{cryIIAb}$ and $\mathit{cryIAc}$
- (4) $\mathit{cryIAc}$ and $\mathit{cryIIIAb}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Specific Bt toxin genes were isolated from Bacillus thuringiensis and incorporated into the several crop plants such as cotton. The choice of genes depends upon the crop and the targeted pest, as most Bt toxins are insect-group specific. The toxin is coded by a gene named cry. The proteins encoded by the genes cryIAc and cryIIAb control the cotton bollworms, that of cryIAb controls corn borer. So, the correct answer is cryIAc for cotton bollworms and cryIAb for corn borer that is represented in option (1)

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 12 (Biotechnology and its Applications) states that the proteins encoded by the genes $cryIAc$ and $cryIIAb$ control the cotton bollworms, and that of $cryIAb$ controls the corn borer.
2. The pair asked for is therefore (cotton bollworm, corn borer) $=$ ($cryIAc$ or $cryIIAb$, $cryIAb$).
3. Option 2 and option 3 name two cotton-bollworm genes or reverse them, and $cryIIIAb$ in option 4 is not NCERT's corn-borer gene.
4. Only option $1$, $cryIAc$ and $cryIAb$, gives the right order.

**Subtopic:** Pest Resistant Plants and Bt Cotton · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 71)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q172_ce36e55b_30102026.png?v=ce36e55b74c6)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q172_31d97046_30102026.png?v=31d970464c8f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** cryIAc toxin is the one used against cotton bollworms, and cryIAb is used against corn borer.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Most students pick option 2. cryIAc and cryIIAb is a pair the source names together, but it names them as the two genes that both control cotton bollworms. So if you remember that pair, you read it as the answer here. The question wants one gene for each of two pests, and the one for corn borer is cryIAb.
- **Why:** You need two stated gene-to-pest assignments at once. The question says 'would contrl cotton bollworms and corn borer, respectively', and each option pairs two cry gene names.
<!--/ecat-->

## Q173

Biology · botany · Ecosystem

Ecological pyramids represent the relationship between the organisms at different trophic levels and they are generally inverted for:

- (1) Pyramid of number in grassland
- (2) Pyramid of energy in pond ecosystem
- (3) Pyramid of biomass in grassland
- **(4)** Pyramid of biomass in sea

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Pyramid of number in grassland ecosystem is upright
2. Pyramid of energy in pond ecosystem is upright
3. Pyramid of biomass in grassland is upright
4. Pyramid of biomass in sea is inverted

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 14 (Ecosystem) states that the pyramid of biomass in the sea is generally inverted, because the biomass of fishes far exceeds that of phytoplankton.
2. The pyramid of numbers and of biomass in a grassland ecosystem are upright; it is the pyramid of numbers in a tree (or parasitic) ecosystem that is inverted.
3. NCERT also states that the pyramid of energy is always upright and can never be inverted, which rules out option 2.
4. Hence option $4$.

**Subtopic:** Ecological Pyramids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 71)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q173_c848a61c_30102026.png?v=c848a61ca176)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q173_d79fc52b_30102026.png?v=d79fc52be076)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Only the biomass pyramid of the sea is inverted, because the standing crop of phytoplankton is smaller than the fish biomass it supports. The energy pyramid is never inverted.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Most students pick option 3. If you have stored 'the biomass pyramid is the one that can turn upside down', you still have to choose an ecosystem, and grassland is the ecosystem the chapter's worked pyramids use. Option 3 has the pyramid type right and the ecosystem wrong. On land the producers outweigh what feeds on them, so the grassland biomass pyramid is upright.
- **Why:** You need a stated exception. The question says 'they are generally inverted for:', and each option pairs a pyramid type with an ecosystem.
<!--/ecat-->

## Q174

Biology · zoology · Reproductive Health

Choose the correct statement regarding GIFT to overcome infertility.

- (1) Ova collected from a female donor are transferred to the uterus of an infertile female.
- (2) Early embryos with up to 8 blastomeres are transferred to the uterus of an infertile female.
- (3) Early embryos with up to 8 blastomeres are transferred into the fallopian tube of an infertile female.
- **(4)** It is the transfer of an ovum collected from a donor into the fallopian tube of another female who cannot produce ovum but can provide suitable envoronment for fertilization and development.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. GIFT is an in-vivo technique used to assist infertility
2. GIFT: Gamete Intra Fallopian Transfer technique facilitates the transfer of an ovum collected from a donor into the fallopian tube of another female who cannot produce one, but can provide suitable environment for fertilization and further development.
3. ZIFT : Zygote Intra Fallopian Transfer is an in-vitro technique in which zygote or early embryo upto $8$ blastomeres is transferred in fallopian tube.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 4 (Reproductive Health) defines GIFT (gamete intra fallopian transfer) as the transfer of an ovum collected from a donor into the fallopian tube of another female who cannot produce one, but can provide a suitable environment for fertilisation and further development.
2. Option 3 describes ZIFT, in which the zygote or early embryo with up to 8 blastomeres is transferred into the fallopian tube.
3. Option 2 describes IUT (intra uterine transfer), in which an embryo with more than 8 blastomeres is transferred into the uterus.
4. Option 1 puts the donor ovum into the uterus rather than the fallopian tube, which is not GIFT.
5. Hence option $4$.

**Subtopic:** Assisted Reproductive Technologies (ART) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 71)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q174_52a78429_30102026.png?v=52a78429564e)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q174_82cc32d9_30102026.png?v=82cc32d97f84)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** GIFT moves an unfertilised donor ovum into the fallopian tube of a woman who cannot produce one of her own but can carry the pregnancy.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Most students pick option 3. It is the source's definition of ZIFT, and it shares the words 'into the fallopian tube' with GIFT. So if you anchor on where the material goes instead of on what is moved, you pick it. GIFT transfers an unfertilised ovum. An early embryo of up to eight blastomeres going to that same place is ZIFT.
- **Why:** You have to judge four competing statements against the stated definition of one named technique. The question says 'Choose the correct statement regarding GIFT', and each option is a full statement to be graded.
- **Note:** Option 2 is, in the same way, the definition of intra uterine transfer.
<!--/ecat-->

## Q175

Biology · both · Cell: The Unit of Life

Choose the correct statements regarding cell organelles and their inclusions.
Choose the correct answer from the options given below :

- **(A.)** The endomembrane system includes Golgi complex, endoplasmic reticulum and mitochondria.
- **(B.)** Rough endoplasmic reticulum bears ribosomes on its surface.
- **(C.)** Both mitochondria and plastids have circular DNA.
- **(D.)** A network of microtubules, microfilaments and intermediate filaments present in the cytoplasm is called cytoskeleton.
- **(E.)** Mitochondrion is a single membrane-bound structure.

- (1) A and B only
- (2) A, B and C only
- (3) C, D and E only
- **(4)** B, C and D only

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. The endomembrane system does not include mitochondria. Mitochondria is a double membrane bound cell organelle.

**Solved independently** (answer withheld)

1. A is incorrect: NCERT Class 11, Ch. 8 (Cell: The Unit of Life) includes the endoplasmic reticulum, Golgi complex, lysosomes and vacuoles in the endomembrane system, and states explicitly that mitochondria, chloroplasts and peroxisomes are not considered part of it because their functions are not coordinated with those components.
2. B is correct: the rough endoplasmic reticulum bears ribosomes attached to its outer surface, which is why it appears rough.
3. C is correct: NCERT states that the mitochondrial matrix possesses a single circular DNA molecule, and that the stroma of plastids contains double-stranded circular DNA.
4. D is correct: the network of filamentous proteinaceous structures - microtubules, microfilaments and intermediate filaments - in the cytoplasm is the cytoskeleton.
5. E is incorrect: the mitochondrion is a double membrane-bound structure, with the inner membrane folded into cristae.
6. So B, C and D only, option $4$.

**Subtopic:** Cell Organelles - Comparative Overview · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 72)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q175_ad40e25c_30102026.png?v=ad40e25c97a0)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q175_dacb6755_30102026.png?v=dacb6755bf56)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The endomembrane system is the ER, the Golgi, the lysosomes and the vacuoles. Mitochondria stand outside it. They have a double membrane and they carry circular DNA, as plastids do.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Most students pick option 2. Statement A names the Golgi complex and the endoplasmic reticulum correctly. That true opening makes you trust the rest, so you accept the mitochondrion on the list too. It is a membrane-bound organelle, so it seems to fit. NCERT keeps mitochondria out of the endomembrane system because their functions are not coordinated with the others. And once you take A in, the cytoskeleton statement has to go out of the set.
- **Why:** You have to judge five statements about organelles. Statement A prints a list that is part correct, 'Golgi complex, endoplasmic reticulum and mitochondria'.
<!--/ecat-->

## Q176

Biology · both · Cell: The Unit of Life

Select the correct statements regarding cell membrane in eukaryotic cell.
Choose the correct answer from the options given below:

- **(A.)** Membrane of human RBCs has approximately $52\%$ protein.
- **(B.)** Major phospholipids are arranged in a bilayer.
- **(C.)** Extensions of the plasma membrane into the cell form mesosomes.
- **(D.)** Tails towards the inner part of lipids are hydrophobic and thus protected from aqueous medium.
- **(E.)** Glycocalyx is present on the outer surface of the plasma membrane.

- (1) C, D and E only
- (2) B, C and E only
- **(3)** A, B and D only
- (4) A, C and E only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In prokaryotes, extensions of plasma membrane into the cell form mesosomes. Eukaryotes lack such structure.
2. Glycocalyx is present on the outer surface of the plasma membrane in prokaryotes. Eukaryotes do not have glycocalyx.
3. Hence, only statement A, B and D are correct.

**Solved independently** (answer withheld)

1. A is correct: NCERT Class 11, Ch. 8 (Cell: The Unit of Life) states that in human beings the membrane of the erythrocyte has approximately $52$ per cent protein and $40$ per cent lipids.
2. B is correct: the major lipids are phospholipids arranged in a bilayer, with the polar heads towards the outer sides.
3. D is correct: the hydrophobic tails point towards the inner part of the bilayer, which ensures the nonpolar tails of saturated hydrocarbons are protected from the aqueous environment.
4. C is incorrect for a eukaryotic cell: NCERT describes the mesosome as a special membranous structure formed by the extension of the plasma membrane into the cell in prokaryotes.
5. E is incorrect in this context: NCERT introduces the glycocalyx as the outermost part of the prokaryotic cell envelope (slime layer or capsule), not as a stated feature of the eukaryotic plasma membrane.
6. So A, B and D only, option $3$.

**Subtopic:** Cell Membrane And Cell Wall · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 72)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q176_9418d0d9_30102026.png?v=9418d0d988e9)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q176_a426ce8e_30102026.png?v=a426ce8ea243)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The eukaryotic plasma membrane is a phospholipid bilayer with the tails turned inwards. In the human red cell it is about 52 per cent protein. Mesosomes and the glycocalyx belong to the prokaryote.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Most students pick option 2. Mesosomes and the glycocalyx are real structures. But they belong to the prokaryotic cell. You judge each statement on its own and take both as correct. You miss that the stem is only about the eukaryotic cell. Keeping them pushes out two of the three lines NCERT gives the eukaryotic membrane, the 52 per cent protein of the human red cell and the hydrophobic tails turned away from water.
- **Why:** You have to judge five statements under the condition the stem states. It says 'Select the correct statements regarding cell membrane in eukaryotic cell'. Statement C describes mesosomes.
- **Note:** All three wrong options contain both C and E, the two prokaryotic structures. So the whole question rests on the words 'in eukaryotic cell' in the stem.
<!--/ecat-->

## Q177

Biology · zoology · Locomotion and Movement

Match List I with List II related to muscular/skeletal system:
Choose the correct answer from the options given below:

| List-I | | List-II | |
|---|---|---|---|
| A. | Tetany | (I) | Inflammation of joints |
| B. | Arthritis | (II) | Autoimmune disorder affecting neuromuscular junction |
| C. | Myasthenia gravis | (III) | Wild contraction in muscle due to low $\mathrm{Ca^{++}}$ in body fluid |
| D | Muscular dystrophy | (IV) | Progressive degeneration of skeletal muscle |

- **(1)** A-III, B-I, C-II, D-IV
- (2) A-I, B-II, C-III, D-IV
- (3) A-IV, B-III, C-II, D-I
- (4) A-III, B-II, C-I, D-IV

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Arthritis is an inflammation of joints.
2. Tetany is rapid spasms (wild contractions) in muscle due to low $\mathrm{Ca^{++}}$ in body fluids.
3. Muscular dystrophy is progressive degeneration of skeletal muscle mostly due to genetic disorder
4. Myasthenia gravis is an autoimmune disorder affecting neuromuscular junction leading to fatigue, weakening and paralysis of skeletal muscle.
5. Hence, A-III, B-I, C-II, D-IV is the correct match.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 20 (Locomotion and Movement) states that rapid spasms (wild contractions) in muscle due to low $Ca^{++}$ in body fluid is called tetany, so A-(III).
2. Arthritis is listed as inflammation of joints, so B-(I).
3. Myasthenia gravis is listed as an auto immune disorder affecting the neuromuscular junction, leading to fatigue, weakening and paralysis of skeletal muscle, so C-(II).
4. Muscular dystrophy is listed as progressive degeneration of skeletal muscle, mostly due to genetic disorder, so D-(IV).
5. A-(III), B-(I), C-(II), D-(IV) matches option $1$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 72)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q177_67893514_30102026.png?v=67893514dbdf)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q177_845c5daa_30102026.png?v=845c5daa6596)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Tetany is cramping from low calcium. Arthritis is inflammation of joints. Myasthenia gravis is an autoimmune attack on the neuromuscular junction. Muscular dystrophy is muscle degeneration that keeps getting worse.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Most students pick option 4. Rheumatoid arthritis is itself an autoimmune disease. So if you hold 'arthritis is autoimmune', you give arthritis the line 'Autoimmune disorder affecting neuromuscular junction'. Then myasthenia gravis is left with the joint inflammation. But the neuromuscular junction is what myasthenia gravis is named for, and NCERT gives arthritis the inflammation of joints.
- **Why:** You have to know the description NCERT gives each muscle or bone disorder. List II prints those descriptions, like 'Autoimmune disorder affecting neuromuscular junction' and 'Inflammation of joints'.
<!--/ecat-->

## Q178

Biology · both · Evolution

Evolution of human appears parallel to the progressive development of brain and language skills. As such, the evolution of individual species in the sequence of their appearance is:

- **(1)** $\mathit{Ramapithecus} \rightarrow \mathit{Homo\ habilis} \rightarrow \mathit{Homo\ erectus} \rightarrow \mathit{Neanderthal} \rightarrow \mathit{Homo\ sapiens}$
- (2) $\mathit{Homo\ sapiens} \rightarrow \mathit{Ramapithecus} \rightarrow \mathit{Homo\ habilis} \rightarrow \mathit{Neanderthal} \rightarrow \mathit{Homo\ erectus}$
- (3) $\mathit{Homo\ habilis} \rightarrow \mathit{Homo\ erectus} \rightarrow \mathit{Ramapithecus} \rightarrow \mathit{Neanderthal} \rightarrow \mathit{Homo\ sapiens}$
- (4) $\mathit{Neanderthal} \rightarrow \mathit{Ramapithecus} \rightarrow \mathit{Homo\ habilis} \rightarrow \mathit{Homo\ erectus} \rightarrow \mathit{Homo\ sapiens}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Evolution of human appears parallel to the progressive development of brain and language skills.
2. The correct chronological order in which human evolution took place is :
3. Ramapithecus $\rightarrow$ Australopithecines $\rightarrow$ Homo habilis $\rightarrow$ Homo erectus $\rightarrow$ Neanderthalensis $\rightarrow$ Homo sapiens

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 7 (Evolution) places $Dryopithecus$ and $Ramapithecus$ at about $15$ mya, the earliest of these forms.
2. It then gives $Homo\ habilis$, the first human-like being with a brain capacity of $650$-$800$ cc, at about $2$ mya.
3. $Homo\ erectus$, with a brain capacity of about $900$ cc, follows at about $1.5$ mya.
4. Neanderthal man, with a brain size of $1400$ cc, lived in near east and central Asia between $100{,}000$ and $40{,}000$ years ago.
5. Modern $Homo\ sapiens$ arose in Africa and migrated across continents during $75{,}000$ to $10{,}000$ years ago, so he comes last.
6. The sequence Ramapithecus, Homo habilis, Homo erectus, Neanderthal, Homo sapiens is option $1$.

**Subtopic:** Origin and Evolution of Man · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 73)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q178_4c430a70_30102026.png?v=4c430a70f9fd)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q178_8677fca2_30102026.png?v=8677fca28978)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The order of appearance: Ramapithecus, then Homo habilis, Homo erectus, Neanderthal and finally Homo sapiens.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Most students pick option 3. The four Homo names sit in a chain you hold well, habilis, erectus, Neanderthal, sapiens, and option 3 keeps that chain whole. It only moves Ramapithecus into the middle of it. But Ramapithecus is not a Homo at all, and it comes before the chain starts. So the one name whose position you are unsure of is the one put out of order.
- **Why:** You need the order in which five named forms appeared. The question asks for 'the evolution of individual species in the sequence of their appearance', and all four options order the same five names.
- **Note:** No option is the exact reverse of the right order. Option 3 shifts one name inside a chain that is otherwise correct, and the project's own mapping files that device under this label.
<!--/ecat-->

## Q179

Biology · zoology · Animal Kingdom

The flightless bird with forelimbs modified as paddle-like structures suited for swimming is known as:

- (1) $\mathit{Struthio}$
- (2) $\mathit{Neophron}$
- **(3)** $\mathit{Aptenodytes}$
- (4) $\mathit{Psittacula}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Neophron is vulture and Psittacula is a parrot. Both perform flight.
2. Struthio is ostrich and Aptenodytes is penguin. Both are flightless birds.
3. In penguins, forelimbs are modified into flippers (paddle like structure) and are used for swimming. In ostriches, forelimbs are small and used for balance while running, not for swimming.

**Solved independently** (answer withheld)

1. NCERT Class 11, Ch. 4 (Animal Kingdom) lists among Aves $Aptenodytes$ (penguin), $Struthio$ (ostrich), $Neophron$ (vulture) and $Psittacula$ (parrot).
2. In Aves the forelimbs are modified into wings; in the penguin they are reduced to stiff paddle-like flippers used for swimming, and the bird cannot fly.
3. $Struthio$ is also flightless but is a running bird, not a swimmer, while $Neophron$ and $Psittacula$ both fly.
4. Hence option $3$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 73)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q179_79be7c06_30102026.png?v=79be7c068af9)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q179_7a519a8f_30102026.png?v=7a519a8f1741)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Aptenodytes, the penguin, is the flightless bird whose forelimbs became paddles for swimming.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Most students pick option 1, Struthio. Drop the question's words 'forelimbs modified as paddle-like structures suited for swimming' and Struthio answers what is left, because the ostrich is the flightless bird the examples are built around. But the ostrich's forelimbs are reduced, not turned into paddles, and it cannot swim with them.
- **Why:** You need a named bird that meets two stated conditions at once. The question says 'The flightless bird with forelimbs modified as paddle-like structures suited for swimming', and another flightless bird is among the options.
<!--/ecat-->

## Q180

Biology · botany · Organisms and Populations

Choose the correct statements regarding population interactions between two species.
Choose the correct answer from the options given below:

- **(A.)** In both parasitism and commensalism, only one species benefits and the other species is harmed.
- **(B.)** Both species benefit in mutualism.
- **(C.)** Both species benefit in commensalism.
- **(D.)** In parasitism, only one species benefits and the other species is harmed.
- **(E.)** In amensalism, one species is harmed and the other is unaffected.

- (1) B and E only
- (2) A and B only
- **(3)** B, D and E only
- (4) A and D only

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In parasitism, one species is benefitted and the other is harmed. Whereas, in commensalism one species gets benefitted and the other remains unaffected.

**Solved independently** (answer withheld)

1. NCERT Class 12, Ch. 13 (Organisms and Populations) tabulates interspecific interactions by the sign of the effect on each species.
2. B is correct: mutualism is $(+,+)$, both species benefit.
3. D is correct: parasitism is $(+,-)$, one species benefits and the other is harmed.
4. E is correct: amensalism is $(-,0)$, one species is harmed and the other is unaffected.
5. A is incorrect because it lumps commensalism with parasitism; commensalism is $(+,0)$, so the second species is not harmed.
6. C is incorrect for the same reason: in commensalism only one species benefits, the other is neither harmed nor benefited.
7. So B, D and E only, option $3$.

**Subtopic:** Commensalism and Ammensalism, Parasitism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 73)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/crops/q180_dcc860e3_30102026.png?v=dcc860e35da5)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/30102026/neet_papers/2026/2026_11/solutions/q180_80fcb364_30102026.png?v=80fcb364e751)

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each interaction is named by who gains and who loses. In mutualism both gain. In parasitism one gains and the other is harmed. In commensalism one gains and the other is unaffected. In amensalism one is harmed and the other is unaffected.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Most students pick option 2. Parasitism and commensalism sit next to each other in NCERT's table of plus, minus and zero. You carry parasitism's minus across to commensalism. So you accept statement A and keep mutualism beside it. In commensalism the second species is neither helped nor harmed. So A fails, and the third correct statement is E, on amensalism.
- **Why:** You have to judge five statements about who gains and who loses in each interaction. Statement A and statement D make the same claim about parasitism. One of them adds commensalism to it and the other does not.
- **Note:** Option 1 works the other way. B and E in it are both correct, but it leaves out D, the parasitism line.
<!--/ecat-->

