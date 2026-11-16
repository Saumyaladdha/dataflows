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
- **Concept:** When the speed of light is made the unit of speed, a distance is numerically just the light-travel time in seconds
- **Trap:** **old ncert answer** (`old_ncert_answer`) — the paper altered one value in an NCERT example or line, and NCERT's own answer is printed as a distractor — option 2  
  500 is the number carried for sunlight: NCERT's own exercise sets the travel time at 8 min 20 s, which is 500 s and so 500 new units, while this paper prints 6 min 40 s, which is 400 s, so the remembered answer is sitting in the options.
- **Why:** This question requires computing the distance as a bare number once the unit of speed is fixed, demonstrated by the stem's 'The speed of light in vacuum is taken as unity' together with the printed time '6 min 40 s'.
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
- **Concept:** Each elastic constant is fixed by which stress it uses and which strain it divides by, and compressibility is the reciprocal of the bulk modulus
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Compressibility is the reciprocal of the bulk modulus, and that sentence alone does not say which of the two printed volume expressions is the reciprocal one, so the pair gets handed over inverted. B-IV with C-III is printed only in option 3, so one inversion carries the whole code.
- **Why:** This question requires telling four elastic constants apart by the stress and the strain inside their defining expressions, demonstrated by List II printing $-\dfrac{1}{\Delta P}\left(\dfrac{\Delta V}{V}\right)$ and $-P\left(\dfrac{V}{\Delta V}\right)$, which are reciprocals of each other.
- **Note:** List II entry IV is printed with $P$ rather than $\Delta P$; the bulk-modulus reading is still the only one available for it, and the pairing is tagged as printed.
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
- **Concept:** An ideal diode conducts only when forward biased, so the bias on each diode decides which resistors are in the current path before Ohm's law is applied
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the current path is fixed by the circuit figure, and the figure was not supplied to this step in readable form, so no option can be tied to a named route
- **Why:** This question requires deciding which diodes conduct and then computing the current, demonstrated by the stem's 'All diodes are ideal and identical' and by options that are currents in amperes.
- **Note:** The circuit itself was not carried into this packet: `figure_image.drawn.spec` is null and only image paths and hashes are present, so I cannot see the source value, the resistor values or which diodes are forward biased. The printed paper is intact, so per rulebook §5.0 this is our reading limit and not `source_damage_artifact`, and I have written no trap rather than infer one. A reviewer holding the figure should check whether $\frac{5}{3}$ A, $\frac{5}{9}$ A and $\frac{1}{3}$ A are the currents obtained by letting a reverse-biased diode conduct, which would put a resistor into the path that the real circuit excludes and give a current smaller than the key's $\frac{15}{2}$ A; if so the trap is `condition_missed` on the diode's bias condition. Separately, `figure_image.drawn.checks.netlist` reads 'not a circuit' for a question whose stem says 'the circuit shown below', which looks like a mis-set check rather than a fact about the question.
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
- **Concept:** Under uniform angular acceleration the revolutions turned equal the average angular speed times the time, once rpm is matched to the length of the interval
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Adding the two angular speeds where the mean was needed: $(10 + 20) \times 10 = 300$ revolutions instead of $\frac{10 + 20}{2} \times 10 = 150$.
- **Why:** This question requires turning an average angular speed in rpm into a revolution count over the stated interval, demonstrated by the stem's 'increased from 600 rpm to 1200 rpm in 10 s' and by options that are plain revolution counts.
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
- **Concept:** Kinetic energy in SHM goes as the square of the speed, so it never goes negative, touches zero at each extreme, and repeats twice in every period
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The constant line is the correct graph for the pendulum's TOTAL energy, so a student holding 'energy is conserved in SHM' plots the conserved quantity; kinetic energy is the part being traded away, and it falls to zero at each extreme.
- **Why:** This question requires matching the shape of a K.E.-against-time curve to the squared speed of SHM, demonstrated by all four options being K.E.-against-$t$ plots, one of them 'a constant line'.
- **Note:** The four options reach this step as the placeholder text '[graph]'; I read them from `figure_image.text` and the coordinates in `figure_image.drawn.spec`, where option (1) is a horizontal line, (2) a sine about a non-zero dashed mean with period $T$, (3) two humps touching zero at 0, $T/2$ and $T$, and (4) a sine crossing below the axis. The printed shape is therefore four graph options, which the retired E1 vocabulary calls `graph_options`, not `plain_mcq` as the pattern decided. The live qtype list has no value for graph options and no field in which a `new_type` proposal could be carried on this axis, so I recorded `mcq` from the retired-vocabulary map and record the printed shape here; `asks: read_diagram` carries the graph-ness.
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
- **Concept:** The terminal voltage of a cell is its emf less the $Ir$ drop across its own internal resistance
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $0.6 \times 2 = 1.2$ V is the only multiplication the problem offers and it is a true voltage — the drop inside the cell — so the work stops one subtraction short of what the stem asked, $12 - 1.2 = 10.8$ V.
- **Why:** This question requires subtracting the internal drop from the emf, demonstrated by the stem giving '$12\,\mathrm{V}$ emf and internal resistance $2\,\Omega$' alongside 'the current in the circuit is $0.6\,\mathrm{A}$'.
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
- **Concept:** At one temperature the rms speed varies inversely as the square root of molar mass, and does not depend on how much of each gas is present
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Copying the masses under the root in the order the stem prints them — 40 for argon over 70 for chlorine — gives $\sqrt{40/70} = \frac{2}{\sqrt{7}}$, the reciprocal of the answer, because $M$ sits in the denominator of $\sqrt{3RT/M}$ and so the heavier gas's mass belongs on top.
- **Why:** This question requires the factor by which rms speed changes when molar mass changes at a fixed temperature, demonstrated by the stem printing the answer as $\left(\dfrac{V_{\mathrm{rms}}^{\mathrm{Ar}}}{V_{\mathrm{rms}}^{\mathrm{Cl}}}\right)$ with all four options bare ratios and no speed asked for.
- **Note:** Two printed quantities play no part in the correct solution: the $2 : 1$ mass ratio of the gases in the flask, and the temperature $27^\circ\mathrm{C}$, which cancels because both gases are at it. `asks` is `relation` rather than `calculate` because the constants cancel and the answer is the factor between two rms speeds, not a computed speed.
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
- **Concept:** At minimum deviation the ray inside a prism runs parallel to the base, so $r_1=r_2=A/2$, $e=i$ and $\delta_m=2i-A$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The minimum-deviation condition is stored as $i=\frac{A+\delta_m}{2}$, and recalling the shape of the fraction but not which letter stands alone reads it off as $\delta=\frac{A+i}{2}=\frac{60^\circ+50^\circ}{2}=55^\circ$.
- **Why:** This question requires the minimum-deviation relation turned into a number, demonstrated by the stem fixing the geometry with 'The refracted ray ($QR$) is parallel to its base ($BC$)' and printing $i=50^\circ$ for an equilateral prism.
- **Note:** The figure was not opened by this step, but it does not decide anything: the stem states in words that the prism is equilateral, that $QR$ is parallel to $BC$ and that $i=50^\circ$, which is the whole input. So `read_diagram` was ruled out and the question is tagged `calculate`.
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
- **Concept:** Which observations and relations show light behaving as a particle and which as a wave, with $\lambda = h/p$ being the matter-wave wavelength rather than evidence of particle nature
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The two secure rows go in first, $E=h\nu$ to photon energy and diffraction to wave nature, and then $\lambda=h/p$ is read as proof of particle nature because momentum is in it. Option 2 is the code that keeps both secure rows and makes exactly that swap, so the student's own correct work vouches for it.
- **Why:** This question requires sorting relations and phenomena into wave behaviour and particle behaviour, demonstrated by List II offering 'Particle nature of light' and 'Wave nature of light' as rival entries beside 'de Broglie wavelength'.
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
- **Concept:** In Bohr's atom the total energy fixes the orbit radius through $E=-\frac{1}{4\pi\varepsilon_0}\frac{e^2}{2r}$, and the first excited state ($n=2$) sits at $4a_0\approx2.1$ angstrom
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The stored size of the hydrogen atom is $0.53$ angstrom, and carrying it as '$0.53$ nm' because atomic sizes are usually quoted in nanometres turns $r=4a_0$ into $2.1\times10^{-9}\,\mathrm{m}$, one power of ten too large.
- **Why:** This question requires a radius computed from a stored relation and the printed constants, demonstrated by the stem supplying $1\,\mathrm{eV}=1.6\times10^{-19}\,\mathrm{J}$ and $\frac{1}{4\pi\varepsilon_0}=9\times10^{9}$ while the four options differ only in their power of ten.
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
- **Concept:** A body rides along with its support only while the force needed stays below limiting static friction, so the ceiling is $a=\mu_s g$ and the mass cancels out
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  A student who expects the printed mass to survive into the answer multiplies the two numbers that have nothing to do with gravity, $\mu_s m=0.12\times15$, and that is exactly the printed $1.8$.
- **Why:** This question requires the limiting static-friction condition turned into an acceleration, demonstrated by the options being bare accelerations in $\mathrm{m\,s^{-2}}$ while the printed $15\,\mathrm{kg}$ cancels from $\mu_s mg=ma$.
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
- **Concept:** Capacitors in series all carry the same charge, while a capacitor bridged across the whole series chain sits at the full battery voltage
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $Q=C_{eq}V=5\,\mu\mathrm{F}\times50\,\mathrm{V}=250\,\mu\mathrm{C}$ is a true number and the right first step, and it gets read back as the charge on each capacitor rather than the charge the battery delivers to the whole combination.
- **Why:** This question requires the equivalent capacitance and the charge on every capacitor to be computed and reported together, demonstrated by 'The equivalent capacitance and the charges on each capacitor respectively are' and by each option bundling a $\mu\mathrm{F}$ value with a charge distribution.
- **Note:** The circuit figure was not opened by this step. The printed key -- $5\,\mu\mathrm{F}$ with $125\,\mu\mathrm{C}$ on every capacitor -- is consistent with only one topology for these five values, $C_1$ to $C_4$ in series across the $50\,\mathrm{V}$ battery with $C_5$ in parallel across that chain, and the routes above are written from that reading; a reviewer holding the figure should confirm it. E1 called this `multi_part_respectively`, which maps onto `two_part`, and the printed shape agrees.
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
- **Concept:** Over a climb comparable with $R$ the work against gravity is the change in $-GMm/r$, not $mgh$, and it comes to $\frac{GMm}{2R}=\frac{mgR}{2}$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  $W=mgh$ with $h=R$ returns $mgR$ in one line, but that formula holds only while $g$ hardly changes over the climb, and here $g$ has fallen to a quarter of its surface value by the top.
- **Why:** This question requires the gravitational potential energy difference across a rise of one Earth radius, demonstrated by 'to a height equal to the radius of the Earth' and by options written symbolically as multiples of $mgR$.
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
- **Concept:** A computed result carries no more significant figures than its least precise input, and the rounding is done once, from the full value
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Rounding $7.654$ to two figures in two moves -- first to $7.65$, then applying the taught 'if the digit dropped is $5$, leave an even preceding digit unchanged' rule -- holds the $6$ and prints $7.6$, where one rounding from the full value gives $7.7$.
- **Why:** This question requires a density computed and then reported to the correct number of significant figures, demonstrated by 'Keeping the significant figures in view' and by the options $7.654$, $7.65$, $7.6$ and $7.7$ being one number printed at four precisions.
- **Note:** The stem reads 'is measured to the $9.0\,\mathrm{cm}$', where 'to the' appears to be a transcription of 'to be'; it changes neither the data nor the answer, so the question is tagged as printed.
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
- **Concept:** A ball thrown up and falling back has one constant downward acceleration throughout, so its velocity-time graph is a single straight line of slope $-g$ that passes through zero at the top
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the five lettered items arrive as '[graph]' placeholders and the options are near-bare letters ('C only', 'D only', 'B only', 'A and E only'), so which curve each letter prints was not supplied to this step
- **Why:** This question requires reading five printed velocity-time plots and judging which one is consistent with a constant downward acceleration, demonstrated by the stem's 'Which of the following plots is/are correct?' standing over five lettered items that carry no text.
- **Note:** The five statements arrive as the literal string '[graph]' and the figure was not opened by this step, so no option-level route can be audited. Per section 5.0 this is our reading limit, not damage to the paper, so the verdict is not source_damage_artifact. A reviewer holding figures_agent/2026_11/q015.png should check: the correct plot must be one straight line of slope $-g$ running from $+v_0$ down through zero into negative values; the letters to examine are any plot that is V-shaped (speed plotted instead of velocity, so the sign never turns), any plot whose slope changes at the highest point, and any plot showing only the upward half. A V-shaped plot would carry 'reversed'; a plot with the slope changing at the top would carry 'condition_missed', since $a=-g$ holds on the way down as well.
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
- **Concept:** At the equilibrium position of a pendulum the whole of the conserved energy is kinetic, so the total energy and the mass fix the speed there
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The working line $v^2 = 2(0.02)/0.02$ comes out as exactly $2$, and $2.0\,\mathrm{m/s}$ is printed, so the number already written down is sitting in the options with a unit on it. That $2$ is $v^2$ in $\mathrm{m^2/s^2}$; the speed is $\sqrt{2} = 1.41\,\mathrm{m/s}$.
- **Why:** This question requires computing a speed from a conserved total energy and a mass, demonstrated by the stem supplying 'the sum of kinetic energy and potential energy ... is $0.02$ joule' plus '(Consider mass of the bob $= 20\,\mathrm{g}$)' against four speeds as options.
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
- **Concept:** Two-slit intensity varies as $\cos^2$ of half the phase difference, so moving from a path difference of $\lambda$ to $\lambda/3$ cuts the intensity to a quarter
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  A student carrying the relation as $I = I_{\max}\cos(\phi/2)$ instead of $I_{\max}\cos^2(\phi/2)$ computes $K\cos 60^{\circ} = K/2$. The cosine of the half phase scales the amplitude, so intensity needs it squared.
- **Why:** This question requires the factor by which intensity changes when the path difference drops from $\lambda$ to $\lambda/3$, demonstrated by the options being printed as multiples of the given value -- '$K/4$', '$2K$', '$K/2$' -- and not as intensities in their own right.
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
- **Concept:** A junction diode passes current in one sense only, so the voltage across the diode itself tracks the source during the half cycle it blocks and sits near zero during the half cycle it conducts
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four options arrive as the literal placeholder '[graph]' and the stem's circuit was not supplied to this step, so no waveform can be read and no route to one can be audited
- **Why:** This question requires reading the printed circuit to see how the diode sits with respect to the source and the rest of the loop, demonstrated by the stem 'In the circuit shown below, the voltage appearing across the diode $D$ will be of the form' with graphs in place of text options.
- **Note:** Options 1-4 are stored as the placeholder string '[graph]' and the stem's circuit exists only as a figure file this step was not given, so nothing about the four waveforms is readable here. Following codebook section 5.0, this is our reach and not source damage -- the paper is intact and the figure is recorded with a path and a checksum -- so no source_incomplete claim is being made and no trap is written. A reviewer holding the figure should check one mechanism in particular: a graph showing the rectified waveform delivered across the load offered where the voltage across the diode was asked. That option would be true of the circuit while answering a different point in it, which is wrong_site_attacked. Shape note: the four options being graphs is what the retired vocabulary called graph_options; the live qtype list has no such value, so the printed shape is recorded as mcq.
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
- **Concept:** At series resonance $X_L = X_C$, so $f = 1/(2\pi\sqrt{LC})$ and the resistance has no say in where resonance sits
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Worked the slips that this problem actually admits and none reaches a printed option: dropping the $2\pi$ gives $100$ kHz, reading $C$ as $0.1$ F gives $15.9$ Hz, reading $L$ as $1$ H gives $0.50$ kHz, using $\sqrt{L/C}$ gives the right digits a decade down, and bringing $R$ in through $\sqrt{1/LC - R^2/4L^2}$ makes the root imaginary. Every unit or $2\pi$ error here moves the answer by a half-decade, so it lands on $1.59$, $5.03$ or $100$ -- never on $13.5$, $10.1$ or $20.7$ kHz.
- **Why:** This question requires substituting converted values into $f = 1/(2\pi\sqrt{LC})$, demonstrated by the stem asking for 'the resonance frequency of the circuit' from '$0.1\,\mu\mathrm{F}$' and '$1\,\mathrm{mH}$' with four frequencies as options.
- **Note:** The $1\,\mathrm{k\Omega}$ is printed but does not enter the resonance frequency; checked whether carrying it into a damped-resonance expression reaches any option, and it does not, so it is a dangling datum rather than a trap route. The three wrong frequencies are a numeric spread around the correct $15.9$ kHz with no derivation behind any of them, which is why this one is no_trap while the other four calculation questions in the group all carry a trap.
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
- **Concept:** Interference and diffraction only move energy about, and they are properties of waves of every kind, not of light alone
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Statement A is almost the stem's own sentence, so it is settled as true, and B then rides along on the true half, because every interference and diffraction example met in the optics chapter is a light example.
- **Why:** This question requires the stated fact that interference and diffraction belong to waves generally rather than to light, demonstrated by statement B's 'characteristics exhibited only by light waves' while the stem has already granted statement A's energy bookkeeping.
- **Note:** E1_question_type reads plain_mcq ('16 default'), but the printed shape is a block of two lettered statements A and B with four truth-combination options, so the shape recorded here is statements. asks is fact_line and not reason_line because the stem's own two sentences supply A's reason, leaving the decision on B's generality.
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
- **Concept:** Only the $x$ term of the phase carries spatial dependence, so $\Delta\phi = 2\pi(0.0080)\,\Delta x$ with $\Delta x$ measured in the equation's own centimetres
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The separation is printed in metres while the equation's $x$ is in cm, so substituting the stem's number as it stands gives $2\pi(0.0080)(0.5) = 0.008\pi$ rad. The missing conversion is the whole factor of $100$ between that option and $0.8\,\pi$.
- **Why:** This question requires computing a phase difference from the $x$ coefficient after matching units, demonstrated by the equation stating 'where $x$ and $y$ are in cm' while the separation is given as '$0{\cdot}5\,\mathrm{m}$'.
- **Note:** The four options sit one decade apart -- $0.008\pi$, $0.08\pi$, $0.8\pi$, $8\pi$ -- so the whole option set is a conversion ladder. The trap is recorded on the rung that the stem's own printed number, $0.5$, lands on when it is used unconverted.
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
- **Concept:** Perpendicular forces add as $\sqrt{F_1^2+F_2^2}$, and the angle of the resultant is measured from whichever force the option names: $\tan\theta = 6/8$ from the $8\,\mathrm{N}$ force
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The magnitude $2\,\mathrm{m\,s^{-2}}$ is right, and a student who forms the tangent by putting the larger force over the smaller writes $\tan^{-1}(4/3)$ while still naming the $8\,\mathrm{N}$ force. $\tan^{-1}(4/3)$ is the angle from the $6\,\mathrm{N}$ force, so the option's two halves do not belong together.
- **Why:** This question requires computing both the acceleration's magnitude and the angle its resultant makes with a named force, demonstrated by the stem asking for 'the magnitude and direction ... respectively' and every option printing a number together with an angle 'with $8\,\mathrm{N}$ force' or 'with $6\,\mathrm{N}$ force'.
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
- **Concept:** When a charged capacitor shares charge with an identical uncharged one the common voltage halves and half the stored energy is lost in the connecting wires
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $1.0 \times 10^{-6}\,\mathrm{J}$ is the energy the charged capacitor starts with, $\frac{1}{2}CV^2 = \frac{1}{2}(200\,\mathrm{pF})(100\,\mathrm{V})^2$, so working out that stored energy and reading 'lost in the process' as 'handed over by the charged capacitor' stops here. Half of it is still stored on the pair afterwards, so the loss is $0.5 \times 10^{-6}\,\mathrm{J}$.
- **Why:** This question requires computing the stored energy before and after charge sharing and subtracting, demonstrated by 'the amount of electrostatic energy lost in the process'.
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
- **Concept:** Average power is the work done against gravity divided by the time taken, $P = mgh/t$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Working in kilojoules gives $mgh = 196\,\mathrm{kJ}$, and dividing by $10\,\mathrm{s}$ leaves the figure $19.6$ with the kilo no longer being tracked. The work is $1.96 \times 10^{5}\,\mathrm{J}$, so the power is $19.6\,\mathrm{kW}$ and not $19.6\,\mathrm{W}$.
- **Why:** This question requires computing $mgh/t$ from the stem's numbers and reporting it in the right power unit, demonstrated by the options pairing $19.6$ and $39.2$ with both W and kW.
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
- **Concept:** Least count of a vernier calliper is one main-scale division minus one vernier-scale division
- **Trap:** **old ncert answer** (`old_ncert_answer`) — the paper altered one value in an NCERT example or line, and NCERT's own answer is printed as a distractor — option 2  
  $0.01\,\mathrm{cm}$ is the least count carried for the textbook calliper, where $10\,\mathrm{VSD}$ coincide with $9\,\mathrm{MSD}$ so that $1\,\mathrm{MSD} - 1\,\mathrm{VSD} = 0.1\,\mathrm{mm}$. This paper changes the instrument to $20\,\mathrm{VSD} = 16\,\mathrm{MSD}$, which makes $1\,\mathrm{VSD} = 0.8\,\mathrm{mm}$ and the least count $0.2\,\mathrm{mm} = 0.02\,\mathrm{cm}$, with the remembered $0.01\,\mathrm{cm}$ left sitting in the options.
- **Why:** This question requires computing $1\,\mathrm{MSD} - 1\,\mathrm{VSD}$ from the printed coincidence, demonstrated by '20 VSD coincide with 16 MSD (each division of length 1 mm)'.
- **Note:** The stem states the division in mm while all four options are printed in cm, so one conversion is baited into the question on top of the altered coincidence ratio.
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
- **Concept:** In free fall from rest the drop grows as $s=\tfrac{1}{2}gt^{2}$, so a longer reaction time always means a longer fall and the ranking of distances is the ranking of times
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The five times are sorted smallest first, with C's $0.18\,\mathrm{s}$ at the head as the quickest reaction, and that ranking is written straight into the chain of '>' signs, which asks for the longest fall first.
- **Why:** This question requires ordering five free-fall distances, demonstrated by the stem's 'What is the correct order of the distance travelled by the ruler for each person?' and options printed as chains of '>'.
- **Note:** E1_question_type reads arrange_in_order; the printed shape is a lettered block A to E with ordering options, so qtype is statements and the ordering is carried by asks: order. The printed $g=9.8\,\mathrm{m\,s^{-2}}$ is never needed, since $s=\tfrac{1}{2}gt^{2}$ rises with $t$ and the distance order is just the time order.
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
- **Concept:** A square of equal-resistance sides fed across one diagonal is a balanced bridge, so the arm across the other diagonal carries no current
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  The uniform wire gives $1\,\Omega$ a side, and carrying that $1\,\Omega$ as the resistance of each A-to-C path gives $1\,\|\,1 = 0.5\,\Omega$ and $I = 2/0.5 = 4\,\mathrm{A}$. Each path runs through two sides, so each path is $2\,\Omega$, the pair is $1\,\Omega$, and $I = 2\,\mathrm{A}$.
- **Why:** This question requires reducing the loop to its two parallel paths and applying Ohm's law, demonstrated by 'a uniform metallic wire having resistance 4 Ω is bent to form a square loop (ABCD)' with the battery across A and C.
- **Note:** The figure marks where I is measured. The stem's own words fix the topology (square ABCD from a 4 Ω uniform wire, 2 Ω between B and D, 2 V across A and C) and the printed key of 2 A is the battery current for the balanced bridge, so the question is tagged as printed; the options are numbers, not bare figure labels.
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
- **Concept:** The nameplate rating fixes the heating element's resistance, so power at any other supply voltage follows $P = V^2/R$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $121$ is the first number the standard route throws up, $R = V^2/P = 220^2/400 = 121\,\Omega$, and finding $121$ among the options closes the question early. It is the element's resistance in ohms, not the power at $200\,\mathrm{V}$, which is $200^2/121 \approx 331\,\mathrm{W}$.
- **Why:** This question requires fixing R from the rating and recomputing $V^2/R$ at the new voltage, demonstrated by 'if the supply voltage drops to 200 V, what will be the power consumed (approximately)'.
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
- **Concept:** Field at the centre of an N-turn coil, $B = \mu_0 N I / 2r$, and the coil's magnetic moment, $m = NIA$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The current comes out right at $2.5\,\mathrm{A}$, and the moment is then $m = NI\pi r^2$ with the area worked out in cm$^2$: converting $78.5\,\mathrm{cm^2}$ with $10^{-3}$ instead of $10^{-4}$ gives $A = 7.85 \times 10^{-2}\,\mathrm{m^2}$ and $m = 20\,\mathrm{A\,m^2}$. The true area is $7.85 \times 10^{-3}\,\mathrm{m^2}$, so $m \approx 2\,\mathrm{A\,m^2}$, and because the stem says 'respectively' the right current on its own scores nothing.
- **Why:** This question requires computing the current from the centre-field relation and then the moment from $NIA$, demonstrated by 'the current flowing through the coil, and the magnitude of the magnetic moment of this coil are, respectively'.
- **Note:** E1 read this as multi_part_respectively, which maps onto qtype two_part: the stem asks for two quantities 'respectively' and each option is a current-and-moment pair judged whole. The four options form a grid of two currents against four moments, and $2\,\mathrm{A}$ fills the second current column with no route behind it.
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
- **Concept:** Motional emf $\varepsilon = BLv$, where $L$ is the side of the loop that cuts across the direction of motion
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The 8 cm side is the one a student calls the length of the loop, and putting it into $\varepsilon = BLv$ gives exactly the printed $0.3 \times 0.08 \times 0.02 = 4.8 \times 10^{-4}$ V; the side that generates the emf is the one lying across the motion, here 3 cm.
- **Why:** This question requires the motional emf computed with the loop side that lies across the motion, demonstrated by the stem fixing the velocity 'in a direction normal to the shorter side of the loop' while printing both 8 cm and 3 cm.
- **Note:** I considered `old_ncert_answer` because the setup is an NCERT exercise with two numbers altered (the shorter side and the speed), but it fails its own test: NCERT's two printed answers for that exercise, $2.4\times10^{-4}$ V and $0.6\times10^{-4}$ V, are not among these options. The altered-number pull is therefore recorded as the route on option 2 and not as the label.
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
- **Concept:** Nuclear radius goes as $A^{1/3}$, so nuclear volume goes as $A$ and nuclear density is the same for every nucleus; mass defect is measured against the separated nucleons, not against the atom
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The remembered $R=R_{0}A^{1/3}$ is treated as the size relation itself and pinned to the volume, so A is ticked true, and the mass-defect definition in D is then read correctly, landing the pair on option 3.
- **Why:** This question requires the stated nuclear volume relation and the stated definition of mass defect, demonstrated by statements A and B offering 'proportional to $A^{1/3}$' and 'proportional to $A$' for the same volume while C and D offer 'an atom and its nucleus' against 'a nucleus and its constituents'.
- **Note:** The four options are a two-by-two grid crossing the volume pair against the mass-defect pair, so each wrong option is exactly one or both of the two errors, which is why all three carry routes and none is filler. asks was tested against relation and rejected: relation is reserved for how many times one quantity changes when another does, and this stem asks which proportionality is the stated one.
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
- **Concept:** Nuclear density is the same for every nucleus, so the mass per nucleon is $\rho \cdot \tfrac{4}{3}\pi R_0^3$ and the mass number is the total mass divided by it
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Taking the nucleon mass as $10^{-27}$ kg instead of $1.66 \times 10^{-27}$ kg turns the printed mass straight into $19.926$, which rounds to the 20 in the options; the correct divisor, which the given density and $R_0$ are there to build, is $1.66 \times 10^{-27}$ kg and gives $12$.
- **Why:** This question requires the mass number computed from the constant nuclear density, demonstrated by the stem supplying a density of $2.29 \times 10^{17}\,\mathrm{kg/m^3}$ together with 'Take $R_0 = 1.2 \times 10^{-15}\,\mathrm{m}$, $4\pi = 12.56$'.
- **Note:** The mass per nucleon that the given density and $R_0$ produce, $1.657 \times 10^{-27}$ kg, is the atomic mass unit, and the printed mass is exactly $12\,\mathrm{u}$ — so the mantissa 19.926 is the full pull of the question and both 20 and 19 are reachable from it.
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
- **Concept:** Period of a simple pendulum from a timed count of oscillations, $T = t/n$, then the length from $L = gT^2/4\pi^2$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Squaring $2\pi$ as $2\pi^2$ instead of $4\pi^2$ halves the denominator, and with $\pi^2 = g = 9.8$ handed over the arithmetic cancels to exactly the printed 2 m.
- **Why:** This question requires the pendulum length computed from a period read off a timed count, demonstrated by the stem printing 'the data of time taken to complete 30 oscillations as 60 s' and handing over '$\pi^2 = 9.8$, and $g = 9.8\,\mathrm{m/s^2}$'.
- **Note:** I checked `asks: experiment` against this one because of the bench framing, and kept `calculate`: the setup contributes nothing beyond converting 30 oscillations in 60 s into $T$, and the named student and the word 'experiment' are dressing on a substitution into $L = gT^2/4\pi^2$.
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
- **Concept:** First law of thermodynamics read as rates: $\dot{U} = \dot{Q} - \dot{W}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  100 W is the rate printed for the heat supply, true of the situation and already in the unit the options use, so it answers how fast heat enters rather than how fast internal energy rises.
- **Why:** This question requires the first law applied as rates, demonstrated by the stem printing one rate of heat supply, '100 W', one rate of work, '75 J/s', and asking for 'the rate at which internal energy increases'.
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
- **Concept:** Parallel-axis theorem on a ring, with the ring's mass obtained as linear density times wire length and its radius from $L = 2\pi R$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Reading the symbol $m$ as the ring's mass puts $I = \tfrac{3}{2}mR^2 = 3mL^2/8\pi^2$ on the page, one power of $L$ short; $m$ is mass per unit length, so the ring's mass is $mL$ and the answer carries $L^3$.
- **Why:** This question requires an expression derived from the parallel-axis theorem with the mass obtained from the wire's length, demonstrated by the stem giving 'length $L$ and linear mass density $m$' while the options differ only in whether $L$ appears squared or cubed and whether $\pi$ is squared.
- **Note:** The figure was not opened at this step. It fixes where $yy'$ lies, and the factor $\tfrac{3}{2}$ common to all four options together with the printed key places it as a tangent in the plane of the ring — but every option already carries that factor, so the pull sits entirely in the printed symbols ($m$ against $mL$, $\pi$ against $\pi^2$) and the trap does not depend on the figure. I also weighed `arithmetic_slip` for option 4, since $M = m$ drops the factor $L$; I kept `formula_misused` because the error is in which quantity is fed to a correctly remembered relation, which is how option 1 of q030 was tagged in this same group.
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
- **Concept:** Converting a galvanometer into an ammeter: the shunt carries everything but the full-scale current, $S = I_g G/(I - I_g)$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Stopping at the product $I_g G = 10^{-3} \times 100 = 0.1$ leaves out the division by $I - I_g \approx 10$, and 0.1 is printed as an option; carrying the division through gives $0.1/9.999 = 0.01\,\Omega$.
- **Why:** This question requires the shunt resistance computed from the full-scale current and the new range, demonstrated by the stem printing 'full scale deflection for a current of 1 mA' against an 'ammeter of range $0 - 10\,\mathrm{A}$'.
- **Note:** The four options are a pure decade ladder (0.001, 0.01, 0.1, 1.0), so every wrong answer here is one or more powers of ten away from the key; only the single-decade one has a named step behind it, which is why the other two are recorded as fillers rather than as further traps.
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
- **Concept:** The Wheatstone bridge balance condition is symmetric between the cell branch and the galvanometer branch, so swapping them keeps a balance point and the galvanometer still swings on either side of it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  The remembered line is that swapping the cell and the galvanometer leaves the bridge balance undisturbed; stretched past the balance point it turns into 'the galvanometer reads zero wherever the jockey sits'.
- **Why:** This question requires reading the outcome at a named instrument after its wiring is changed, demonstrated by 'In a metre bridge experiment (see figure), the positions of the cell, $E$, and galvanometer, $G$, are interchanged. We shall observe in the galvanometer:'. `apply_rule` was the other candidate, since the bridge symmetry rule is what decides it, but the question is asked from a bench setup and wants what is seen in it, which is the narrower value.
- **Note:** The figure was not opened at this step; the stem's 'cell, $E$, and galvanometer, $G$' and the options' reference to the jockey fix the standard metre-bridge wiring, and the interchange result does not depend on the drawing, so this is not the figure-decides case. Options 1 and 3 carry the same 'the deflection cannot change sides' route with the side left arbitrary, so neither dominates the other and the trap was placed on option 2.
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
- **Concept:** For $i=i_0\sin\omega t$ the current climbs from a zero to its peak in a quarter of a period, so the time is $T/4=1/(4f)$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The period $T=\frac{1}{60}$ s is halved once, as if the climb from zero to the peak took half a cycle, giving $\frac{1}{120}$ s instead of the quarter period $\frac{1}{240}$ s.
- **Why:** This question requires a number computed from the stem's frequency, demonstrated by 'How long will the current, starting from zero, take to reach the peak value?' with four fractions of a second as the options.
- **Note:** The peak value $5\,\mathrm{A}$ is unused data: the answer depends on the frequency alone.
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
- **Concept:** Ampere's circuital law in a solid wire carrying a uniform current: $B$ rises in proportion to $r$ inside the wire and falls as $1/r$ outside it, the two branches meeting at the surface $r=a$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are printed as '[graph]' placeholders, so the plots were not supplied to this step and no wrong plot can be described
- **Why:** This question requires picking the plot whose shape matches the field of a uniformly carrying solid conductor, demonstrated by 'The plot which correctly represents the variation of magnetic field ($B$) with distance ($r$) from the axis of the conductor'.
- **Note:** The options arrive as '[graph]' placeholders. The paper itself is intact, so this is a limit of what this step was given and not source damage. A reviewer holding the four plots should check for a reversed-regime plot ($1/r$ from the axis out to $r=a$, then rising) and for a plot that keeps $B\propto r$ past $r=a$; the key, option 1, should be the plot rising linearly to a maximum at $r=a$ and decaying as $1/r$ beyond it. The demand is really equation-to-graph translation, and `read_diagram` is the only figure-facing value on the asks axis.
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
- **Concept:** A forward-biased diode conducts strongly once the forward voltage passes its threshold; the reverse saturation current is the small current on the reverse-bias branch of the same characteristic
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Statement A is recognised as the knee of the forward characteristic and accepted, and since the one current carrying a name in that same V-I discussion is the reverse saturation current, B is read as supplying the name of the current A has just described.
- **Why:** This question requires the named parts of the printed diode characteristic, demonstrated by statement B's 'This current is called reverse saturation current' said of the forward-bias current statement A describes. Applied the swap test of section 5.1: 'reverse saturation current' and 'forward current' do not resemble each other, so the likeness is not doing the work and position on the same V-I curve is, which makes it nearby_fact rather than look_alike_term.
- **Note:** E1_question_type reads statement_i_ii; the printed labels are A and B rather than I and II, and the options are the two-statement truth verdicts, so the shape is recorded as statements. Statement B opens with 'This current', so it cannot be judged without statement A, which is why only one of the four verdicts leaves A true and B false.
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
- **Concept:** In the static case a conductor holds no interior field and no interior excess charge, its surface field is normal and equal to $\sigma/\varepsilon_{0}$, and its interior potential is constant rather than zero
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The zero field inside the conductor is carried one step too far, with $E=0$ read as $V=0$, so E is taken as the potential version of A and joins A and C while D is dropped.
- **Why:** This question requires the stated results for a conductor in the static situation, demonstrated by statement E's 'electrostatic potential is zero everywhere inside a charged conductor' standing against statement A's zero interior field and statement B's 'does not depend on its surface charge density'.
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
- **Concept:** Photoemission needs the photon energy $hc/\lambda$ to exceed the work function, so only wavelengths shorter than the threshold $\lambda_0=hc/\phi$ eject electrons
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The emission condition is stored the wrong way round as $\lambda>\lambda_0$, so the shortest wavelength in the list, $50\,\mathrm{nm}$, is read as the weakest photon and named as the one that fails.
- **Why:** This question requires the threshold wavelength computed from the stem's constants and then compared against each option, demonstrated by 'For a metal of work function $6.6\,\mathrm{eV}$, which of the following wavelengths of incident radiation does not give rise to the photoelectric effect?' with Planck's constant supplied.
- **Note:** The 'not' in the task has no single option it lands on, since $50$, $100$ and $150\,\mathrm{nm}$ all produce emission, so the polarity is carried as one route inside the option 4 trap rather than as the trap for the question.
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
- **Concept:** The ray rule for a diverging lens: a ray arriving parallel to the principal axis leaves appearing to come from a focus on the incoming side, and never actually passes through a focus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The convex-lens rule, that a parallel ray passes through the second principal focus, is the one taught and drawn first, and it is carried straight across to the concave lens.
- **Why:** This question requires the stated ray rule for a diverging lens, demonstrated by 'In a concave lens, a ray of light emanating from the object parallel to the principal axis of the lens after refraction:' with four rival completions and no quantity to work out. On the trap axis I applied the swap test: rename the two foci with two unlike words and the pull on option 4 survives, because what carries the student is the convex-lens case printed beside this one rather than the resemblance of 'first' to 'second', so `nearby_fact` and not `look_alike_term`.
- **Note:** The answer line is printed 'Answer (2*)' and the asterisk matters here: on the usual convention parallel incident rays appear to diverge from the SECOND principal focus of a concave lens, which makes option 4's wording defensible and the key's 'first principal focus' a convention call rather than a physics one. Tagged as printed per the rulebook's section 7 and flagged `arguable_key`; the option 4 route rests on the convex-lens carry-over, which holds whichever way the convention is read.
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
- **Concept:** Absolute pressure at depth is atmospheric pressure plus $\rho g h$, so the depth follows from the gauge part alone: $h=\frac{P_{\text{abs}}-P_{\text{atm}}}{\rho g}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  The depth is taken as the water pressure divided by the density alone, $h=\frac{P}{\rho}$, so $\frac{99\times10^{5}}{1000}$ gives $9900\,\mathrm{m}$ and $g$ never enters.
- **Why:** This question requires a depth computed from the stem's pressure and constants, demonstrated by 'designed to withstand an absolute pressure of $100\,\mathrm{atm}$' together with the supplied '$1\,\mathrm{atm}=1\times10^5\,\mathrm{Pa}$' and $g=10\,\mathrm{m/s^2}$.
- **Note:** Worth recording that the absolute-versus-gauge confusion the word 'absolute' sets up is not baited: ignoring it yields $1000\,\mathrm{m}$, which is not among the options, so every printed distractor is a factor or decade slip instead.
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
- **Concept:** Each band of the electromagnetic spectrum has its own named source: valve oscillators for microwaves, molecular vibration for infra-red, atomic electron jumps for visible light, nuclear decay for gamma rays
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Microwaves are the radiation that sets water molecules rotating and vibrating when an oven heats food, so 'Vibration of atoms and molecules' reads as the microwave entry. That is true of what microwaves do to matter and not of what produces them, and neither list is printed with a heading that says which is wanted.
- **Why:** This question requires the source stated for each band of the spectrum, demonstrated by List II entry IV reading 'Klystron valve or magnetron valve'.
- **Note:** Neither list carries a column heading, so that List II gives the source of each band has to be inferred from its entries; that gap is part of what makes option 1 reachable.
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
- **Concept:** Which reductants act on the nitrile group, as against the reagents that make an amine from a nitro compound or from an amide
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  A student carrying one undivided list of "reagents that make amines by reduction" fills the third slot with Sn + HCl beside $\mathrm{LiAlH_4}$ and $\mathrm{H_2/Ni}$; Sn + HCl reduces a nitro group, so two correct items carry a wrong one through.
- **Why:** This question requires the reagent-to-substrate mapping for nitrile reduction, demonstrated by the stem "Select the reagents that reduce nitriles to primary amines" with "Sn + HCl" and "$\mathrm{Br_2}$/aq. NaOH" sitting among the five lettered items.
- **Note:** The lettered items A–E are reagents rather than claims, so the printed shape is a lettered item list answered by a subset; qtype statements is the current value that carries it, matching E1's list_of_statements. Option 3 is a close rival to the trap — it too keeps two correct items and adds one wrong — and is carried in other_options with a full route; option 4 was taken as the trap because reaching it needs one swap (B for D) while option 3 needs both an inclusion and an exclusion.
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
- **Concept:** Industrial catalysts and the one process each serves: $\mathrm{V_2O_5}$ in the contact process, iron in Haber's synthesis, $\mathrm{PdCl_2}$ in the Wacker oxidation, a nickel complex in alkyne polymerisation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  $\mathrm{V_2O_5}$ is stored as the oxidation catalyst and List II prints 'Oxidation of ethyne to ethanal' in the same table as the contact process, so $\mathrm{V_2O_5}$ is handed the entry that carries the word oxidation and $\mathrm{PdCl_2}$ takes the leftover $\mathrm{H_2SO_4}$ row
- **Why:** This question requires the process the chapter names against each industrial catalyst, demonstrated by List I printing bare formulas such as '$\mathrm{V_2O_5}$' and 'Ni complex' with no criterion supplied from which a pairing could be worked out. On the trap axis I applied the swap test: entries III and IV do not resemble each other as names, and what carries the student is that both sit in the one printed table of industrial catalysts with the right one beside the offered one, so this is nearby_fact and not look_alike_term.
- **Note:** List II prints 'Oxidation of ethyne to ethanal'; the Wacker process oxidises ethene, so the substrate name may be an error in the paper or in our record. Tagged as printed, and the pairing is unaffected because $\mathrm{PdCl_2}$ is the only Wacker catalyst in List I.
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

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** $\Delta H$ must be built from $\Delta U$ by adding $\Delta n_g RT$ for the gas moles lost, and only then does $\Delta G = \Delta H - T\Delta S$ decide spontaneity
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Writing the Gibbs relation the other way round, $T\Delta S^{\ominus} - \Delta H^{\ominus} = -13112 + 12476 = -635.6$ J, gives the same digits with the sign flipped, and a negative $\Delta G$ then reads as spontaneous.
- **Why:** This question requires converting $\Delta U^{\ominus}$ into $\Delta H^{\ominus}$ with the $\Delta n_g RT$ term and then computing $\Delta G^{\ominus} = \Delta H^{\ominus} - T\Delta S^{\ominus}$, demonstrated by the stem printing '$\Delta U^{\ominus} = -10\,\mathrm{kJ\,mol^{-1}}$', 'Given : $R = 8.31$' and asking to 'Identify the correct option with $\Delta G^{\ominus}$ for the reaction and spontaneity'.
- **Note:** Two arithmetic remarks that do not touch the key. (i) The printed data give $\Delta G^{\ominus} = 13112 - 12476.38 = 635.62$ J, while option 3 prints $0.63568$ kJ; option 3 is still the only $+0.6$ value, so the key stands as printed. (ii) Each option pairs a number with a verdict, but the verdict always agrees with the sign of the number beside it, so no option offers a right number with a wrong verdict and `half_right` cannot arise here.
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
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Reading a subshell label off the quantum numbers: $n$ gives the shell digit, and $l = 0, 1, 2, 3$ give $s$, $p$, $d$, $f$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Counting the subshell letters from $l = 1$ instead of $l = 0$ reads '$l$' $= 3$ as a $d$ subshell, and $3d$ is the only $d$ entry printed, after which D is left with $5f$
- **Why:** This question requires the $n$-and-$l$ naming convention applied to each printed pair, demonstrated by List I giving "'$n$' $= 5$, '$l$' $= 3$" and List II the label '$5f$' for it.
- **Note:** Every row is also settled by $n$ alone, since the four shell digits in List II are distinct, so the item discriminates only on students who work from $l$.
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
- **Concept:** For a 1:1 sparingly soluble solid $K = s^2$ fixes $[\mathrm{OH^-}]$, and the pH still needs the $14 - \mathrm{pOH}$ step
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $s = \sqrt{4 \times 10^{-10}} = 2 \times 10^{-5}$ gives $\mathrm{pOH} = 5 - 0.3010 = 4.699$, and handing that in answers for pOH where the stem asked for pH.
- **Why:** This question requires the solubility product solved for $[\mathrm{OH^-}]$ and then converted through pOH to pH, demonstrated by the stem printing '$K = 4 \times 10^{-10}$' with 'Given : $\log 2 = 0.3010$' and asking to 'Calculate pH'.
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
- **Concept:** DNA is a double helix built with thymine; RNA is a single strand carrying uracil in thymine's place
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  'RNA possesses a single strand helix structure' is the headline fact about RNA, and once that clause checks out the sentence is accepted whole without testing 'thymine', which belongs to DNA.
- **Why:** This question requires the stated structural facts of each nucleic acid, demonstrated by the four options differing only in the two printed slots 'single/double strand helix' and 'thymine/uracil'.
- **Note:** E1's pattern recorded `statement_options`; the printed shape agrees — the stem is only the instruction 'The correct statement with regard to the secondary structure of DNA/RNA is' and each option is a full statement to be graded — so it maps onto qtype `statements`. It is the only member of this group whose shape is not a plain mcq.
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
- **Concept:** Metamers share a molecular formula and a functional group but differ in the alkyl groups flanking that group, unlike position or chain isomers
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Option 3 reads only 'and' — the two structures it should carry are absent from our record, so the option set is not all there and any dominant pull could sit in the missing option; options 1, 2 and 4 were read and the key was checked against the printed answer line, but a trap named over a gap would be a guess.
- **Why:** This question requires the definition of a metamer applied to each printed pair, demonstrated by the stem asking for 'The pair of molecules that are metamers' with no criterion printed beside it.
- **Note:** Option 3's content is lost in our record: it stores the connecting word 'and' with both structures dropped, so this is extraction damage rather than anything the paper did, and per rulebook §5a no trap is written. What is visible and should survive the repair: option 1 is a pair of position isomers (propan-1-ol / propan-2-ol), option 2 a pair of chain isomers (n-pentane / 2-methylbutane), and the key, option 4, is the two $\mathrm{C_4H_{10}O}$ ethers whose alkyl groups are distributed differently. A reviewer holding the printed paper should restore option 3 and then decide whether the dominant pull is a neighbouring isomerism type in options 1 and 2 or something in the restored structures. Separately, each option here is a pair accepted or rejected whole (the retired E1 value `pair_options`); the six qtype values cannot record that apart from `mcq`, and the printed layout is a question with four answers and no lettered items, so `mcq` is what I recorded.
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
- **Concept:** Which isomerism a complex can show is decided by its ligand set: a ligand with two donor atoms gives linkage isomers, three bidentate chelates give optical isomers, $\mathrm{MA_2B_2}$ gives cis-trans, and a solvent shared between sphere and lattice gives solvate isomers
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Solvate isomerism is applied as 'the complex contains a solvent molecule', and $\mathrm{[Co(NH_3)_5NO_2]Cl_2}$ carries five $\mathrm{NH_3}$ ligands, so C takes 'Solvate' and 'Linkage' falls to the hexaaqua salt
- **Why:** This question requires the defining condition of each isomerism type applied to the printed ligand set, demonstrated by '$\mathrm{[Co(NH_3)_5NO_2]Cl_2}$' being settled by $\mathrm{NO_2}$ carrying two donor atoms rather than by any stored pairing.
- **Note:** Rows C and D carry the whole discrimination: the key is the only option pairing $\mathrm{NO_2}$ with 'Linkage', and both other wrong options repeat the same C-II, D-IV swap.
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
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The units of a rate constant come out of the rate law: $k = \mathrm{rate}/[A]^n$, so $k$ carries $\mathrm{mol^{1-n}\,L^{n-1}\,s^{-1}}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Second order is read as 'two concentration terms, so $\mathrm{mol^{-2}}$', which lands C on $\mathrm{mol^{-2}\,L^{2}\,s^{-1}}$ instead of $\mathrm{mol^{-1}\,L\,s^{-1}}$, and third order then takes the leftover $\mathrm{mol^{-1}\,L\,s^{-1}}$
- **Why:** This question requires the unit expression derived from $k = \mathrm{rate}/[A]^n$ for each order, demonstrated by List II printing '$\mathrm{mol^{-2}\,L^{2}\,s^{-1}}$' against 'Third order'.
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
- **Concept:** Name the longest chain first, and when both numbering directions give the same locant set the lower locant goes to the substituent cited first alphabetically
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Numbering the heptane chain from the other end also puts substituents at 3 and 5, so with no clash to warn them a student keeps that direction and lists the groups in the order met, inverting both the numbering and the citation order to give 3-methyl-5-ethylheptane.
- **Why:** This question requires the IUPAC parent-chain and locant rules applied to the drawn skeleton, demonstrated by the options setting the same two substituents on a heptane parent with their locants exchanged ('3-ethyl-5-methylheptane' against '3-methyl-5-ethylheptane') and on a hexane parent ('2,4-diethylhexane', '3,5-diethylhexane').
- **Note:** The structure image was not supplied to this step, so the skeleton was reconstructed from the printed key, 3-ethyl-5-methylheptane: $\mathrm{CH_3CH_2CH(C_2H_5)CH_2CH(CH_3)CH_2CH_3}$. That skeleton does contain the six-carbon chain the hexane options name — running from one terminus through the methyl branch — and both diethylhexane names and the 3-methyl-5-ethyl name are fixed by the key alone, so the routes above are auditable without the figure. A reviewer holding the figure should confirm the drawing's orientation, which affects which chain reads as the main one but not whether these routes exist.
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
- **Concept:** Only the fraction of the bulb's power that leaves as light counts, and the photon rate is that power divided by one photon's energy
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Converting $8\%$ by shifting the decimal one place gives the factor $0.8$ and a light power of $120$ W, so $120/(4.42 \times 10^{-19}) = 27.2 \times 10^{19}$ — the key's digits one power of ten up.
- **Why:** This question requires the usable power taken from the efficiency and divided by one photon's energy, demonstrated by the stem printing '$150$ watt, converting $8\%$ energy into light' and 'energy of one photon is $4.42 \times 10^{-19}\,\mathrm{J}$'.
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
- **Concept:** Steam reforming of methane: steam over nickel at $1273\,\mathrm{K}$ gives water gas, $\mathrm{CO}$ and $\mathrm{H_2}$, and the carbon only reaches $\mathrm{CO_2}$ in the later shift step
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The manufacture of dihydrogen from methane is printed as two steps, reforming and then the shift $\mathrm{CO + H_2O \to CO_2 + H_2}$, so the end products of the chain are given instead of what leaves the nickel catalyst at $1273\,\mathrm{K}$.
- **Why:** This question requires the product set assigned to steam reforming of an alkane, demonstrated by the stem fixing reagent and condition — "with steam at $1273\,\mathrm{K}$ in the presence of nickel catalyst" — and leaving only the products to be named.
- **Note:** The four options are two-species product sets accepted or rejected whole, which the retired E1 vocabulary would call pair_options; recorded as mcq because one reaction's product set is a single answer, not two separately-asked blanks, and the stem prints no "respectively".
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
- **Concept:** Reagent tests fix a functional group: 2,4-DNP marks a carbonyl, failure with Fehling's marks a ketone rather than an aldehyde, and effervescence with $\mathrm{NaHCO_3}$ marks the carboxylic acid left after drastic side-chain oxidation
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four options are stored as the bare text "P =, Q =" with the drawn structures absent from our record, so no wrong option can be named and no route to one can be shown
- **Why:** This question requires a substrate and its oxidation product recovered from a set of reagent outcomes, demonstrated by "gives a red orange precipitate with 2,4-DNP reagent and it does not reduce Fehling's reagent" fixing what P must be before Q can be named.
- **Note:** Source incomplete: every option reads "P =, Q =" because the drawn structures did not survive extraction, so no trap is written. Two further things recorded as printed and not re-judged — the answer line reads "Answer (3 or 4)" and accepted_answers carries both 3 and 4, and has_figure is false although the option set plainly held structures. qtype and asks come from the stem, which is intact; E1's multi_part_respectively maps onto two_part via the "P and Q, respectively" ask.
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
- **Concept:** Sigma and pi bookkeeping: every bond contributes one $\sigma$, a double bond adds one $\pi$ and a triple adds two, and a lone pair is not a bond
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  I checked every wrong option against the Lewis structures of the four printed molecules. Each one moves $\mathrm{CH_4}$ off '$4\ \sigma$ bonds' and $\mathrm{NH_3}$ off '$3\ \sigma$ bonds, one lone pair', and in doing so hands carbon a lone pair, $\mathrm{NH_3}$ two $\pi$ bonds or $\mathrm{CH_4}$ five $\sigma$ bonds, none of which any count of the printed formula produces. The one confusable pair in the item, $\mathrm{C_2H_4}$ against $\mathrm{C_2H_2}$, is never offered as a clean swap: no option prints A-I together with B-IV.
- **Why:** This question requires the $\sigma$ and $\pi$ counting rule applied to each printed formula, demonstrated by List II offering '$5\ \sigma$ bonds, $1\ \pi$ bond' to be assigned to '$\mathrm{C_2H_4}$'.
- **Note:** I looked again before settling on three fillers, because three unreached options is a strong claim. The item is decided twice over by single secure facts: '$4\ \sigma$ bonds' for $\mathrm{CH_4}$ and '$3\ \sigma$ bonds, one lone pair' for $\mathrm{NH_3}$ each appear in the key alone, so the two slips a student could actually make, ethene for ethyne and $\mathrm{NH_3}$ for $\mathrm{NH_4^+}$, are each printed only alongside an impossible count.
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
- **Concept:** Ionic $\mathrm{KCN}$ donates through carbon and gives the nitrile, while covalent $\mathrm{AgCN}$ donates through nitrogen and gives the foul-smelling isocyanide
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The smell clue settles $\mathrm{Z = C_2H_5NC}$, and $\mathrm{KCN}$ is then written in as the cyanide source, so the half of the option that is right carries the half that is not.
- **Why:** This question requires knowing which cyanide salt bonds through nitrogen rather than carbon, demonstrated by the options crossing "X = $\mathrm{AgCN}$ / $\mathrm{KCN}$" against "Z = $\mathrm{C_2H_5NC}$ / $\mathrm{C_2H_5CN}$" while the stem prints "the same foul smelling product Z".
- **Note:** The stem's reaction scheme is a figure that was not supplied to this step, so the two substrates could not be read. The tag rests only on words our record does carry — "the following two reactions give the same foul smelling product Z" and the four fully written options — which fix the isocyanide-versus-nitrile decision and agree with the printed key (1). A reviewer holding the figure should confirm the two substrates (expected: an ethyl halide with X, and the carbylamine route from ethanamine) before the routes on options 2 and 3 are relied on.
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
- **Concept:** Mole concept in three moves: mass to moles, moles to molecules, molecules to atoms using the atoms-per-formula-unit count, four H in $\mathrm{CO(NH_2)_2}$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  The subscript outside the bracket in $\mathrm{CO(NH_2)_2}$ is taken as the hydrogen count, so the molecule count $5.42\times10^{22}$ is doubled rather than quadrupled and lands on $1.084\times10^{23}$.
- **Why:** This question requires a mass converted through moles and molecules to an atom count, demonstrated by the stem supplying "Molar mass of urea : $60\,\mathrm{g\,mol^{-1}}$" and $\mathrm{N_A}$ and asking for "the number of hydrogen atoms".
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
- **Concept:** Second-period nitrogen has no d orbitals, so it bonds $p\pi\text{-}p\pi$ only, while the heavier group-15 elements can use d orbitals in $d\pi\text{-}p\pi$ and $d\pi\text{-}d\pi$ bonding
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  $d\pi\text{-}p\pi$ is the notation carried away from the group-15 discussion, so the printed $d\pi\text{-}d\pi$ in the phosphine line reads as the symbol that has been altered and is marked as the incorrect statement.
- **Why:** This question requires four stated group-15 bonding facts to be graded one at a time against the printed text, demonstrated by the instruction "Identify the incorrect statement from the following" standing over four standalone claims with no lettered block.
- **Note:** On the $look\_alike\_term$ against $nearby\_fact$ test: swapping $d\pi\text{-}d\pi$ and $d\pi\text{-}p\pi$ for two unlike words kills the pull on option 2, because nothing but the single-letter difference makes that line look altered — so the resemblance is doing the work. E1 recorded statement_options, which maps onto qtype statements because the stem asks for a statement to be judged.
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
- **Concept:** An ambidentate ligand offers two different donor atoms as alternatives for one bond — thiocyanate through S or through N — which is not the same as a bidentate ligand using two sites at once
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  "Ambidentate" is read as another spelling of "bidentate", and ethane-1,2-diamine is the bidentate ligand named first in every denticity list, so it is picked as the two-site ligand.
- **Why:** This question requires the stated meaning of ambidentate matched to the ligand the text names for it, demonstrated by "Which one of the following is an ambidentate ligand?" set against four named ligands that differ only in denticity.
- **Note:** On the $look\_alike\_term$ against $nearby\_fact$ test: replace "ambidentate" and "bidentate" with two unlike words and the pull to ethane-1,2-diamine dies, because what carries the student is the shared -dentate ending rather than where the ligands are printed — so the resemblance wins.
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
- **Concept:** Metallic character rises down a group and falls across a period, so Be sits below Mg, Mg below Na, and the metalloid Si above the non-metal P
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who has the non-metal end secure and then recalls the trend as running up the group and rightwards across the period writes the three metals as $\mathrm{Na} < \mathrm{Mg} < \mathrm{Be}$, which is this line. Metallic character runs the other way on both axes, so the metal block reads $\mathrm{Be} < \mathrm{Mg} < \mathrm{Na}$.
- **Why:** This question requires the direction of two periodic trends applied to one mixed list, demonstrated by 'the correct order of increasing metallic character of Na, Be, P, Mg and Si' putting a group-2 pair and a period-3 run into a single sequence.
- **Note:** E1 `arrange_in_order` has no counterpart among the six qtype values. The printed shape is one question with four answers, so qtype is `mcq` and the ordering task is carried on `asks: order`.
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
- **Concept:** Which reagent sequence effects a given functional-group conversion: oxidation and acid work-up, sulphonation followed by alkali fusion, esterification followed by reduction, and dehydration followed by hydration
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  three of the four List I rows are placeholders reading '[structure diagram - drawn reaction scheme in the stem figure]', and the stem figure was not supplied to this step, so the conversion each reagent set has to be matched against cannot be read
- **Why:** This question requires the reagent sequence that effects each printed conversion, demonstrated by List II giving '(i) $\mathrm{CH_3OH}$, $\mathrm{H^+}$; (ii) $\mathrm{H_2}$, catalyst' to be matched to '$\mathrm{CH_3COOH} \longrightarrow \mathrm{CH_3CH_2OH}$'.
- **Note:** The paper itself is intact: has_figure is true and figure_image carries a path, a CDN url and a sha256, so this is a limit of what reached this step, not source damage, and I have not set source_damage_artifact. Only row B is readable in text, and its key pairing B-III (ester, then $\mathrm{H_2}$/catalyst) holds, as does the structure of row C, propan-1-ol to a drawn product, whose key pairing IV is conc. $\mathrm{H_2SO_4}$ then $\mathrm{H^+/H_2O}$, i.e. dehydration then Markovnikov hydration. A reviewer holding the figure should check option 1, which differs from the key only in swapping C and D: whether the oleum then NaOH-fusion sequence (I), which belongs to an aromatic scheme, is pulled onto the propan-1-ol row while the dehydration-hydration sequence (IV) goes to the drawn scheme D. Minor record defect: row D's label is printed 'D' where the others carry a full stop.
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
- **Concept:** Cerium reaches +4 because the fourth electron leaves an empty 4f shell, the xenon core
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The stability rule is learnt as the set $4f^{0}$, $4f^{7}$, $4f^{14}$ printed together, so a student who remembers that landing on one of them is what makes the extra ionisation worthwhile, but not where cerium sits in the series, takes the filled one. $\mathrm{Ce^{3+}}$ is $4f^{1}$, so one more electron empties the shell to $4f^{0}$; $4f^{14}$ belongs to the far end of the series.
- **Why:** This question requires the reason the book gives for one lanthanoid leaving its usual +3 state, demonstrated by the stem ending 'cerium still shows $+4$ oxidation state because:' with each option offering a rival cause.
- **Note:** Trap test applied per §5.1: $4f^{14}$ was swapped for an unlike configuration and the pull survives, because what carries the student is the book printing $4f^{0}$, $4f^{7}$ and $4f^{14}$ together as one stability set, not any resemblance between the two symbols. Hence `nearby_fact`, not `look_alike_term`. E1 read the full-sentence options as `statement_options`; no lettered block is printed and nothing is being judged true or false, so qtype is `mcq`.
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
- **Concept:** Which phosphorus by-product leaves when a phosphorus chloride acts on an alcohol, and whether the bromine in the final product ends on the end carbon or the middle one
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the two things that decide the answer — which phosphorus reagent is drawn on the first arrow, and which intermediate Y the middle arrow makes — are printed only in the reaction-scheme figure, which was not supplied to this step, so no route to a wrong option can be confirmed
- **Why:** This question requires the by-product and the final halide of a printed reaction sequence, demonstrated by 'X and Z respectively are' with every option naming a phosphorus species and a bromopropane.
- **Note:** E1 read the words 'reaction sequence' as `arrange_in_order`; the printed shape asks for two blanks together ('X and Z respectively are'), so qtype is `two_part`. The scheme at figures_agent/2026_11/q067.png carries the reagents and was not opened by this step, so no trap is asserted and the paper is NOT recorded as damaged. A reviewer holding the scheme should check two candidate mechanisms: whether option 1, with Br on the middle carbon, is reached by applying Markovnikov addition where the printed condition calls for peroxide (that would be `condition_missed`), and whether options 3 and 4 are reached by quoting $\mathrm{PCl_3}$'s by-product $\mathrm{H_3PO_3}$ for a step drawn with $\mathrm{PCl_5}$, whose by-product is $\mathrm{POCl_3}$. The key is option 2. Options 1 and 3 also carry an editorial aside, '[printed as a two-line drawn structure; see option_boxes]', which is our annotation and not printed on the paper.
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
- **Concept:** Geometry of a complex follows from the number of donor atoms, and for a four-coordinate $d^8$ metal from whether the ligand is strong enough to force square planar instead of tetrahedral
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The rule 'four-coordinate Ni(II) is square planar', learnt from $[\mathrm{Ni(CN)_4}]^{2-}$, is carried onto $[\mathrm{NiCl_4}]^{2-}$, which gives C-III and pushes the Pt row into the only shape left, Tetrahedral.
- **Why:** This question requires the geometry of each complex to be worked out from the formula as printed, demonstrated by List I giving only formulas — "$[\mathrm{NiCl_4}]^{2-}$", "$[\mathrm{Fe(CO)_5}]$" — against the four shape names "Octahedral", "Trigonal bipyramidal", "Square planar", "Tetrahedral".
- **Note:** D-II is printed identically in all four options, so row D decides nothing and the question turns on rows A, B and C. Row A's formula is printed as $[\mathrm{Pt(Cl_2)(NH_3)_2}]$ rather than $[\mathrm{PtCl_2(NH_3)_2}]$; the bracketing is non-standard but the donor-atom count is four either way, so the row is still answerable and the printed key (2) is tagged as it stands.
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
- **Concept:** The phthalein dye test builds phenolphthalein out of the sample and phthalic anhydride, so only a phenolic OH answers it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Phenolphthalein is met first as the indicator for titrating acids, so the word 'phthalein' pulls towards the acidic group, and carboxylic acid is the acid printed next to phenol wherever the acidic organic functional groups are listed together. In this test the sample is a reagent, not the thing titrated: heating with phthalic anhydride builds the dye out of phenol, so the phenolic group is what is identified.
- **Why:** This question requires what a named bench test answers for, demonstrated by 'can be identified through phthalein dye test' with four functional groups as options and no reagent or observation printed to reason from.
- **Note:** Trap test applied per §5.1: 'carboxylic acid' and 'phenolic' do not resemble each other as words, and swapping carboxylic acid for an unlike term leaves the pull intact, because what carries the student is the acidic-groups pairing the book prints together. Hence `nearby_fact`, not `look_alike_term`.
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
- **Concept:** Matching a purification technique to what the two products are; fractional distillation is the technique for liquids whose boiling points lie close together
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  what X and Y actually are is printed only in the reaction-scheme figure, which was not supplied to this step, and every route to sublimation or to either extraction depends on the physical state and the solubility of those two products
- **Why:** This question requires choosing a purification technique for a given pair of products, demonstrated by 'The suitable method that can be used for the separation of products X and Y is' with four named techniques as the options.
- **Note:** E1 read the words 'reaction sequence' as `arrange_in_order`; the answer is a single named method, so qtype is `mcq`. The scheme at figures_agent/2026_11/q070.png was not opened by this step, X and Y could not be identified, and no trap is asserted; the paper is intact, so this is not recorded as damage. A reviewer holding the scheme should check option 2, sublimation, which is the method for a solid that vaporises on heating, and option 3, differential extraction, the method for a solute shared between two immiscible solvents — whichever of those matches the printed products is the pull. The key is option 1.
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
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Molality and molarity worked out from a mass and a volume, and the directions in which a gas's solubility moves with pressure and with temperature
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A student who grades A and B by arithmetic finds nothing to compute in C and hands in the two statements they verified; C is the temperature side of gas solubility and is true, so the set is correct but one statement short.
- **Why:** This question requires computing the concentrations the statements print and grading them, demonstrated by statement (B), "The molarity of a solution containing $5\,\mathrm{g}$ of $\mathrm{NaOH}$ ... in $450\,\mathrm{mL}$ of solution is $0.278\,\mathrm{M}$", which separates option 1 from option 3 and can only be settled by working it out.
- **Note:** Statements A and B print the values that go with their own numbers, unchanged, so old_ncert_answer is ruled out — no altered value leaves a remembered answer among the options. Statement (A) reads "in $75\,\mathrm{g}$ of benzene solution"; the printed $0.556$ m follows only if the 75 g is the solvent ($0.0417/0.075$), since taking it as the whole solution gives $0.575$ m. Tagged as printed; flagging the loose wording only. Option 3 is a near-equal rival to the trap, also one statement short of the key, and is carried in other_options with its own route; option 2 was taken as the trap because reaching it needs no arithmetic to go wrong.
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
- **Concept:** Fusion with sodium in Lassaigne's test turns covalently bound nitrogen, sulphur and halogen into ionic salts, so ordinary inorganic reagents can then detect them
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  A student who is sure of the one fact the stem supplies — the elements in an organic compound are covalently bound — keeps that word for both halves and treats the test as detection rather than conversion. The first half is right and the second fails: covalently held nitrogen gives nothing with $\mathrm{FeSO_4}$, which is why the fusion step ionises it first.
- **Why:** This question requires the direction of the change sodium fusion makes, demonstrated by 'the elements present in an organic compound are converted from:' with the four options being the four pairings of covalent and ionic.
- **Note:** E1 read the phrase options as `statement_options`; no lettered block is printed and no statement is being judged true or false, so qtype is `mcq`.
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
- **Concept:** Faraday's first law with the electron count in it: mass deposited is the equivalent mass times the charge over F, and $\mathrm{Cu^{2+}}$ takes two electrons per atom
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Faraday's law carried as $m = \frac{M I t}{F}$ puts the full molar mass 63 on top and gives $\frac{63 \times 1.5 \times 600}{96487} = 0.5876\,\mathrm{g}$, exactly twice the keyed value, because $\mathrm{Cu^{2+}} + 2e^- \rightarrow \mathrm{Cu}$ never entered the relation
- **Why:** This question requires Faraday's first law applied with the electron count for copper, demonstrated by the stem supplying only "Molar mass of $\mathrm{Cu} = 63\,\mathrm{g\,mol^{-1}}$" and "$1\,\mathrm{F} = 96487\,\mathrm{C\,mol^{-1}}$" while option 4 is exactly twice the keyed value. Ruled out arithmetic_slip because the 2 was never in the student's expression to be dropped; the relation used was the wrong one.
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
- **Concept:** First law of thermodynamics: internal energy change is the heat absorbed minus the work the system does
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  $\Delta U = q + w$ is the form carried in memory and the stem's $200\,\mathrm{J}$ drops straight into it as $w$, giving $500 + 200 = 700\,\mathrm{J}$. In that form $w$ is work done ON the system, and the stem says the system does the work, so the term enters as $-200\,\mathrm{J}$.
- **Why:** This question requires the first law applied with the sign convention attached to work, demonstrated by "work of $200\,\mathrm{J}$ is done by the system" against option 3, which is the two printed numbers added rather than subtracted.
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
- **Concept:** Zero order is the case where concentration itself falls linearly with time, so a straight $[\mathrm{R}]$ against $t$ line fixes the order at 0
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The first-order plot drilled alongside this one, $\ln[\mathrm{R}]$ against $t$, is also a falling straight line of slope $-k$, so a student storing "straight line going down means first order" reads the printed concentration axis as if it carried the logarithm
- **Why:** This question requires reading which quantity sits on the plot's vertical axis before the order can be named, demonstrated by the stem printing "the plot of concentration $[\mathrm{R}]$ vs time has a negative slope" while option 2's first order needs $\ln[\mathrm{R}]$ on that axis. Applied the swap test from section 5.1: replace "1" with an unlike label and the pull survives, because the adjacent printed straight-line plot rather than any resemblance of names carries the student, so nearby_fact and not look_alike_term.
- **Note:** E1 returned reaction_scheme on the text arrow in "$\mathrm{R} \rightarrow$ Product", but no multi-arrow scheme is printed; the shape I can see is a plain single-answer question whose stem carries a graph, so I recorded mcq. The figure file q075.png was not opened by this step. The trap route above rests only on the axis names, which the stem prints in words; a reviewer holding the figure should confirm the plotted line is straight, which the stem's "as shown" and the key of order 0 together imply.
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
- **Concept:** VSEPR on $\mathrm{ClF_3}$: five electron domains on Cl, three bonding and two lone, give a trigonal-bipyramidal parent and a T-shaped molecule
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The T-shape is remembered correctly and the domains are then filled out to six as though the parent were octahedral, which leaves three lone pairs on Cl; chlorine's seven valence electrons minus the three spent in bonds leave four, which is two lone pairs
- **Why:** This question requires VSEPR applied to the five electron domains on Cl, demonstrated by every option pairing a geometry with a lone-pair count, so that "It has T-shaped geometry with three lone pairs on Cl atom." is right in one part and wrong in the other, which is what half_right names.
- **Note:** E1's statement_options maps onto qtype statements here: the stem reads "Identify the correct statement about $\mathrm{ClF_3}$" and each option is a whole claim to be graded, with no lettered block printed above the options.
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
- **Concept:** Identifying an anion from the gas dilute acid drives off: acetate gives acetic acid vapours, and the vinegar smell is what names it
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Carbonate is the anion whose test IS "add dilute acid, get colourless vapours", and $\mathrm{CO_2}$ does redden moist blue litmus, so matching on those two printed observations finishes the job before the third is used. Drop "smell of vinegar" from the stem and carbonate answers it; keep the smell and it cannot, since $\mathrm{CO_2}$ has none.
- **Why:** This question requires an anion identified from what dilute acid releases, demonstrated by "colourless vapours having the smell of vinegar" being the only observation that separates the answer from option 4, since "The vapours turned the blue litmus paper red" holds for carbonate as well.
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
- **Concept:** For a buffer holding equal acid and conjugate base the pH is $\mathrm{pK_a}$, and $\mathrm{pK_a}$ comes from the printed $\mathrm{K_b}$ through $\mathrm{K_a K_b} = \mathrm{K_w}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  10 is this solution's pOH and is true of it: $\mathrm{pK_b} = 10$, and equal $[\mathrm{X^-}]$ and $[\mathrm{HX}]$ make $\mathrm{pOH} = \mathrm{pK_b} = 10$. The stem asked for the pH, which is $14 - 10 = 4$.
- **Why:** This question requires $\mathrm{K_b}$ converted to $\mathrm{K_a}$ before Henderson's equation is used, demonstrated by the stem printing "$\mathrm{K_b}$ for $\mathrm{X^-}$ is $10^{-10}$" and then asking "What is the pH of this buffer solution?", while option 4's 10 is this solution's pOH, true of the system but not the quantity asked for.
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
- **Concept:** Nernst equation for a hydrogen electrode: the log term is fixed by $p_{H_2}$ and $[\mathrm{H^+}]$, and the sign of the half-cell potential follows the direction the half-reaction is written in
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Substituting into the memorised reduction form, $2\mathrm{H^+} + 2e^- \to \mathrm{H_2}$, puts the gas on top: $-\frac{0.059}{2}\log\frac{2}{(0.02)^2} = -0.109$ V, the right magnitude with the sign of the other direction.
- **Why:** This question requires computing a half-cell potential from the Nernst equation with the printed pressure and acid concentration, demonstrated by 'Calculate emf of the half cell' together with the supplied $\frac{2.303\,\mathrm{RT}}{\mathrm{F}} = 0.059$ and $\log 2 = 0.3010$.
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
- **Concept:** Spin-only magnetic moment: count the unpaired electrons in the printed $d$-configuration and put them into $\mu = \sqrt{n(n+2)}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Using the spin form $\mu = \sqrt{4S(S+1)}$ and reading $S$ as the number of unpaired electrons, $S = 2$, gives $\sqrt{24} = 4.90$ BM.
- **Why:** This question requires putting the unpaired-electron count into the spin-only formula, demonstrated by the stem printing the configuration itself, "$\mathrm{Ti^{2+}}$ $(3d^{2})$", and asking for the 'calculated' moment.
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
- **Concept:** Oxygen is not confined to the $-2$ state: peroxides put it at $-1$, superoxides at $-\frac12$ and $\mathrm{OF_2}$ at $+2$
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Boron's drawn dimer in this chapter is the hydride $\mathrm{B_2H_6}$, printed alongside $\mathrm{Al_2Cl_6}$, so a student carrying 'boron is the one that dimerises' reads 'a monomer when E = B' as the planted error and stops there.
- **Why:** This question requires judging four printed claims against the stated facts and naming the one that fails, demonstrated by 'Identify the incorrect statement from the following' set against 'Oxygen exhibits only $-2$ oxidation state.'
- **Note:** Test applied on option 2 for the nearby_fact / look_alike_term choice: $\mathrm{BCl_3}$ and $\mathrm{AlCl_3}$ are not names that resemble each other, and replacing them with two unlike words leaves the pull intact, because what carries the student is a dimer structure printed beside them in the same chapter. Position is doing the work, so nearby_fact.
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
- **Concept:** Formal charge is bookkeeping on a drawn structure: valence electrons minus lone-pair electrons minus half the shared electrons, taken atom by atom
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the stem identifies the oxygens only by numbers printed on a figure, and the figure was not supplied to this step, so no option can be given a route from the printed text
- **Why:** This question requires reading a numbered structure and assigning a formal charge to each oxygen in it, demonstrated by 'The correct formal charges on oxygen atoms numbered 2, 1 and 3 respectively are'.
- **Note:** has_figure is true and the record points at figures_agent/2026_11/q082.png, which this step cannot open. The labels 1, 2 and 3 and the bonds drawn on each oxygen live entirely in that figure, so the paper is intact and the limit is ours, not damage to the source. For a reviewer holding the figure, the keyed triple $0, +1, -1$ for atoms 2, 1 and 3 is the ozone pattern — central oxygen $+1$, one terminal $0$, the other terminal $-1$ — and two mechanisms are worth checking: option 3 ($0, 0, 0$), reached by arguing that the molecule is neutral so every atom must carry zero, and options 1 and 4, which carry the same three charges attached to the atoms in a different order, which is what the out-of-sequence instruction 'numbered 2, 1 and 3 respectively' invites.
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
- **Concept:** Phenolphthalein has two states only — colourless below about pH 8.3 and pink above it — so the end point is read as the first permanent pink when alkali is the solution being run in
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The stem names the sodium hydroxide first, so a student who pictures the alkali in the flask starts from a pink solution and watches the oxalic acid discharge it, reading the same end point backwards as pink to colourless.
- **Why:** This question requires naming what is seen at the end point of a named bench titration with a named indicator, demonstrated by 'Phenolphthalein is used as an indicator ... The colour change that is observed at an alkaline pH close to the equivalence point'.
- **Note:** Tagged as printed. The stem does not say which solution is in the burette, and 'at an alkaline pH close to the equivalence point' is true of both directions through pH 8.3, so option 3 is the end point actually seen when the alkali is the flask solution. The key therefore rests on the convention of running the alkali in from the burette rather than on the indicator chemistry; recorded here, not re-judged.
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
- **Concept:** Gas-volume stoichiometry: $\mathrm{CO_2 + C \to 2CO}$ turns one volume into two, so the rise in total volume equals the volume of $\mathrm{CO_2}$ that reacted
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The two volumes come out right, $0.8$ and $0.6\,\mathrm{dm^3}$, and attaching the $2$ from $2\mathrm{CO}$ to the surviving $\mathrm{CO_2}$ instead of to the $\mathrm{CO}$ formed reports them the other way round, with the total still adding to the printed $1.4\,\mathrm{dm^3}$.
- **Why:** This question requires computing each gas volume from the one-to-two volume change of $\mathrm{CO_2 + C \to 2CO}$ against the measured total, demonstrated by 'the volume of gaseous mixture after complete reaction at STP becomes $1.4\,\mathrm{dm^3}$'.
- **Note:** The pattern classifier returned statement_options on the ground of long options, which contradicts the printed shape: the stem is a numerical stoichiometry problem and asks no statement to be judged, so the shape recorded here is mcq. Its options are pairs of volumes accepted or rejected whole, which is the retired pair_options shape; a reviewer preferring to record that the answer carries two parts would read it as two_part.
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
- **Concept:** The nitrous-acid route from a primary aliphatic amine runs through an unstable diazonium species and finishes at the alcohol
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The reaction sequence is carried entirely in the figure, which was not supplied to this step; the stem prints no reagent and no substrate, so which option a student is carried to cannot be audited from the record I hold
- **Why:** This question requires carrying a printed reaction sequence through to its final product, demonstrated by the stem's 'The major product Z formed in the following sequence of reactions is', the sequence itself being held only in the figure.
- **Note:** The scheme is in figures_agent/2026_11/q085.png, which this step was not given, so no trap is written. The paper is intact, so this is not source damage. A reviewer holding the figure should check option 2, $\mathrm{C_2H_5-N=N-OH}$: in the nitrous-acid reaction of a primary aliphatic amine NCERT prints the unstable diazo/diazonium species immediately before the alcohol, so stopping one step short of Z would be `nearby_fact` on option 2, and option 4, $\mathrm{C_2H_5NH_2}$, would then be the amine the scheme started from. The `concept` above is inferred from the chapter (Amines), the subtopic (nitrous acid) and the printed key $\mathrm{C_2H_5OH}$, and should be confirmed against the figure. E1 returned `arrange_in_order`, which contradicts the printed shape: one product is asked and the four options are single species, so the shape recorded here is mcq.
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
- **Concept:** In the straight-line Arrhenius form the coefficient of $1/T$ is $E_a/R$ and the constant term is $\ln A$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  14.34 is already printed in the stem, and it is $\ln A$, not $E_a/R$; a student who holds the Arrhenius plot as a straight line but has not fixed which term is the slope reports the constant and skips the multiplication by $R$.
- **Why:** This question requires computing a number from the stem's own figures, demonstrated by 'The energy of activation in $\mathrm{kcal\,mol^{-1}}$' asked of the printed slope $1.25 \times 10^{4}$ and the supplied $\mathrm{R} = 1.987\,\mathrm{cal\,mol^{-1}\,K^{-1}}$.
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
- **Concept:** $K_P = K_C(RT)^{\Delta n}$, so the two are equal for every reaction that leaves the number of moles of gas unchanged
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Counting formulas instead of moles turns $\mathrm{H_2 + I_2 \rightleftharpoons 2HI}$ into two particles going to one, so $\Delta n$ comes out as $-1$ and this looks like the reaction where the two constants part company. Keeping the coefficient 2 gives $2 - 2 = 0$ and $K_P = K_C$.
- **Why:** This question requires one stated relation applied to four fresh cases with no quantity produced, demonstrated by the stem's 'Identify the reaction for which $\mathrm{K_P} \neq \mathrm{K_C}$' asked of four printed equations.
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
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** The atom shrinks from Mg to Al and a cation shrinks further as its charge rises, so of Mg, $\mathrm{Mg^{2+}}$, Al and $\mathrm{Al^{3+}}$ the largest is Mg and the smallest is $\mathrm{Al^{3+}}$
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Aluminium is carried as trivalent, so 'covalency ... 6' reads as the planted error and the statement gets ticked as the incorrect one. Covalency counts the bonds actually formed, and five water molecules plus one chloride make six round the same Al whose oxidation state is 3.
- **Why:** This question requires four closely related species told apart by size, demonstrated by the deciding option 'The largest and the smallest species among $\mathrm{Mg}$, $\mathrm{Mg^{2+}}$, $\mathrm{Al}$ and $\mathrm{Al^{3+}}$ are $\mathrm{Al}$ and $\mathrm{Mg^{2+}}$ respectively.'
- **Note:** Test applied on the trap axis: swap 'covalency' in option 4 for an unlike word and the pull dies, because it is the resemblance to 'valency' that supplies the number 3 - so `look_alike_term`, not `nearby_fact`. On option 2 the opposite test holds: Unnilseptium and Bohrium are not alike at all and the pull is positional, the two names sitting in neighbouring columns of the same table. Option 2 is also the one place the key could be argued, since IUPAC's official name for 107 is Bohrium; option 1 is wrong on both of its halves whichever reading is taken, so the printed key stands and is tagged as printed.
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
- **Concept:** Negative deviation from Raoult's law comes from a new attraction in the mixture - here hydrogen bonding between chloroform's C-H and acetone's carbonyl - which holds both components back from the vapour
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Negative deviation really does turn on which attraction is the stronger, so a student holding 'stronger intermolecular forces' without fixing which pair of molecules is compared takes the option that compares chloroform with chloroform. The lowered vapour pressure needs the chloroform-acetone attraction to beat the like-with-like ones, which is the inverse of what this option states.
- **Why:** This question requires the cause the chapter gives for a lowered vapour pressure in one named pair of liquids, demonstrated by the stem's 'forms a solution with negative deviation from Raoult's law due to'.
- **Note:** All three wrong options are statements of positive-deviation physics, so each is reached by the same inversion; the trap of record is placed on option 3 because that option names the very comparison the answer turns on and inverts it.
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
- **Concept:** How many chlorines a benzene chlorination product carries depends on whether chlorine adds across the ring or substitutes on it
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Both reactions are carried entirely in the figure, which was not supplied to this step; with no reagent and no condition printed in the stem, which pair of counts a student is carried to cannot be audited from the record I hold
- **Why:** This question requires two products read off two printed reactions and their chlorines counted together, demonstrated by the stem's 'The number of chlorine atoms present in the organic products X and Y of the following reactions, respectively, are'.
- **Note:** The two reactions are in figures_agent/2026_11/q090.png, which this step was not given, so no trap is written; the paper is intact, so this is not source damage. A reviewer holding the figure should check the three mixed pairs, '3 and 3', '6 and 3' and '3 and 6': each option is a pair accepted or rejected whole, so the candidate mechanism is `half_right` - one of the two products counted correctly and the other read as substitution where the figure shows addition, or the reverse. E1 returned `multi_part_respectively`, which maps onto the current two_part shape and agrees with the printed stem.
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
- **Concept:** The root tip runs root cap, meristematic activity, elongation, maturation, and root hairs belong to the last zone, where epidermal cells have finished differentiating
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Two of the printed zone names begin with the same letters, and a student who has stored the root tip as a list of names plus 'hairs belong to the m-zone' reaches for meristematic activity; root hairs are outgrowths of already differentiated epidermal cells, which only the maturation zone has.
- **Why:** This question requires the one zone the textbook names as hair-bearing, demonstrated by the stem asking 'root hairs arise from which one of the following regions of the root?' with the four printed zones as the options and no criterion given to work out.
- **Note:** E1_question_type reads statement_options ('15 full-statement options'), but the printed options are short noun phrases naming root zones, so the shape recorded here is mcq.
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
- **Concept:** Gymnosperms are the seed plants whose ovules sit naked on the megasporophyll with no ovary wall around them, so no fruit is formed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Selaginella is the pteridophyte taught as the step towards the seed habit, printed immediately before the group whose ovules lie naked, so a student who has stored 'Selaginella begins the seed habit' moves it one group along and treats its ovules as the exposed ones. Selaginella bears spores in strobili and has no ovules at all.
- **Why:** This question requires the defining line of one plant group matched to a named genus, demonstrated by the stem reproducing that line — 'the ovules are not enclosed by an ovary wall and remain exposed' — and offering four taught genera rather than a criterion to extend.
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
- **Concept:** In the lac operon the structural genes pair one-to-one with their products — z with beta-galactosidase, y with permease, a with transacetylase — while the repressor comes from the separate regulatory i gene
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Permease is the product of the y gene, the clause printed immediately after the z gene's in the same sentence, so a student holding the letters z-y-a and the three enzyme names as two separate lists takes the neighbouring product. Permease carries lactose into the cell; beta-galactosidase is the one that splits it.
- **Why:** This question requires the printed gene-to-product pairing inside one operon, demonstrated by the stem naming a single letter — 'in the lac operon, the z gene codes for' — while all four options are real products of that operon's genes.
- **Note:** This is the only member of the group with no filler option: all three wrong options are genuine lac operon products, so each has a printed route behind it.
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
- **Concept:** Bioprospecting is the search through wild biodiversity, at molecular, genetic and species level, for products of economic value
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The four options are 'bio-' terms from four different chapters and are held apart by their endings, so a student who hears 'products of economic importance' and reaches for the bio-word about crops lands on biofortification, which is breeding for nutrient content rather than searching diversity for new products.
- **Why:** This question requires the term the textbook attaches to one printed definition, demonstrated by the stem reproducing that definition — 'exploring molecular, genetic and species-level diversity for products of economic importance' — and asking only what it 'is called'.
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
- **Concept:** Every tool of gene technology has a named source organism: Taq polymerase from Thermus aquaticus, the Ti plasmid from Agrobacterium tumefaciens, pBR322 from Escherichia coli, with Bt cotton as the modified product
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Holding the one pair that is secure, genetically modified organism to Bt cotton, the student carries "plasmid vectors live in E. coli" off the pBR322 line and across to the Ti plasmid row, and the two lines left over then have nowhere to go but B-I and D-III
- **Why:** This question requires the source organism NCERT prints for each named tool of gene technology, demonstrated by List I's "Thermostable DNA polymerase" standing against List II's "Thermus aquaticus" with no criterion printed from which either side could be worked out.
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
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** The productivity vocabulary held apart: productivity is the rate of biomass production, GPP is what photosynthesis fixes, NPP is GPP minus respiration, and secondary productivity is the consumers' share
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  Lines II and IV both open as a rate of organic matter being made, so a student who reads II by its opening words gives it to gross primary productivity, and the photosynthesis line is then the only one left for secondary productivity
- **Why:** This question requires four terms of one family to be held apart on the wording of their definitions, demonstrated by List II printing both "Rate of formation of new organic matter by consumers" and "Rate of production of organic matter during photosynthesis", which differ only after their opening words.
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
- **Concept:** What marks out the sixth, ongoing extinction is its rate: present species extinction rates run 100 to 1000 times the pre-human background rate
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The option gets the direction the chapter teaches — today's rate is faster — and only the factor and the baseline fail, so a student who has stored 'much faster than before' without the printed range stops at the first option that says faster. The printed comparison is 100 to 1000 times, measured against pre-human times, not ten times the earlier episodes.
- **Why:** This question requires the printed rate figure that sets the sixth extinction apart, demonstrated by the stem asking 'how is the sixth extinction, which is in progress, different from the previous episodes?' while three of the four options differ from the key only in the rate they state.
- **Note:** E1_question_type reads statement_options; the options are full sentences, but no lettered block is printed and the stem does not ask which statement is correct, so the shape recorded here is mcq. Option 2's 'nearly 10 times' is a shrunken version of the keyed figure, not a value from an earlier edition — no second printed number can be named, so old_ncert_answer was ruled out.
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
- **Concept:** Protein structure has four levels, and the alpha-helix is secondary structure — the regular hydrogen-bonded coiling of a single polypeptide backbone
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Tertiary is the next level in the printed ladder and the one described as the protein's three-dimensional shape, so a student reasoning 'a helix is a three-dimensional thing' takes it. The regular coil of one backbone is the secondary level; tertiary is that coil folded further into a globular form.
- **Why:** This question requires the level the textbook ties to the regular coil, demonstrated by the stem asking only 'alpha-helix is found in which level of protein structure?' with the four named levels as the options.
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
- **Concept:** Bulliform cells are the large, empty, colourless epidermal cells of a grass leaf whose loss of turgor curls the leaf inwards and cuts water loss
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  NCERT's own sentence on bulliform cells says they absorb water and turn turgid, so that clause carries a student to the water option that is not about loss. Holding water in a storage cell is not moving it: the xylem transports water, and the printed job of these cells is curling the leaf when they go flaccid.
- **Why:** This question requires the function NCERT states for one named epidermal cell type, demonstrated by the stem asking for 'The main function of bulliform cells in grasses' against four unrelated functions with no criterion printed to apply.
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
- **Concept:** One PCR cycle runs denaturation, then primer annealing, then extension, because Taq polymerase needs a bound primer before it can add nucleotides
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Denaturation is the step the cycle unmistakably opens with at 94 degrees, and extension names the DNA synthesis PCR exists for, so the synthesis step gets ranked next and primer annealing is left to the end. Taq has nothing to extend until a primer is bound, so annealing has to sit second.
- **Why:** This question requires the order NCERT gives for the three steps of one PCR cycle, demonstrated by the stem asking for 'the correct sequence of steps in each cycle' while all four options print the same three names in different orders.
- **Note:** E1_question_type is arrange_in_order. The current qtype vocabulary has no order shape, so the printed shape is recorded as mcq and the ordering demand is carried by asks: order.
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
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** What each phase of the cell cycle does: G1 grows without making DNA, S doubles the DNA, G2 builds proteins for division, M divides the cell
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  G1 and G2 are both growth gaps in which no DNA is made, so a student sorting the two lines by their content rather than by which sentence NCERT prints for which gap puts protein synthesis on G1 and "grows but does not replicate its DNA" on G2, and option 1 is the only code holding both
- **Why:** This question requires the two interphase gaps to be told apart on the sentence NCERT prints for each, demonstrated by List II's "Cell is metabolically active and continuously grows but does not replicate its DNA" and "Proteins are synthesized while cell growth continues" both being true of a cell that is not making DNA.
- **Note:** No wrong code shares a single pair with the key, so the trap on option 1 rests entirely on the two G-phase lines being content-true of both gaps, which is also why the swap test gives look_alike_term here rather than nearby_fact. The "not" recorded in negative_words_seen is inside List II's description, not in the instruction.
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
- **Concept:** The causes of biodiversity loss - habitat loss, over-exploitation, alien invasive species and co-extinction - each with its own named example
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The Nile perch, Lake Victoria and the cichlids are held together as one chapter example without the direction of the effect, so statement C reads as that example being quoted back; filing the Amazon soyabean line under farming rather than under habitat loss then leaves B, C and D.
- **Why:** This question requires the fact the chapter states for each cause of biodiversity loss, demonstrated by the stem 'Which of the following statements are correct?' over a lettered block A to E whose options select a subset of the lines.
- **Note:** The 'not' recorded in negative_words_seen sits inside statement E as part of a biological premise, not in the task; the task itself is direct.
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
- **Concept:** A transcription unit is promoter, structural gene and terminator, and the promoter's position is what fixes which strand is template and which is coding
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  E is the only line carrying two claims at once - where the terminator sits and what it does - and it states flatly that it 'defines the end of the process of transcription', so it reads as overclaiming and gets struck, leaving a true but incomplete set of four letters.
- **Why:** This question requires each printed line about the transcription unit to be judged against the stated fact, demonstrated by the stem 'Which of the following statements are correct with reference to a transcription unit?' over a lettered block A to E.
- **Note:** E1_question_type reads arrange_in_order, which the printed shape contradicts - nothing is sequenced, the stem asks which statements are correct and the options are letter combinations. Tagged as the shape on the page. Statement E prints 'it defines the end of the process of transcription' where the source line hedges with 'usually defines', which is what makes a true statement strikeable.
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
- **Concept:** The agreed conventions of binomial nomenclature: genus first with a capital, specific epithet second in lower case, both italicised in print or separately underlined by hand
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  A student who holds the capitalisation rule as one blurred sentence - capital on one word, small letter on the other - and has it the wrong way round reads this true line as the planted error. NCERT puts the capital on the genus and the small letter on the specific epithet, exactly as this option states.
- **Why:** This question requires the wording NCERT gives for the universal rules of binomial nomenclature, demonstrated by option 4 printing 'The first word in the biological name represents the specific epithet, while the second component denotes the genus' with the two terms exchanged.
- **Note:** Options 1, 2 and 3 reproduce three of NCERT's printed rules, so the elimination route is real: a student who holds the genus-first rule securely strikes option 4 at once.
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
- **Concept:** The four parts of decomposition: detritus is the raw material, decomposition breaks it down, mineralisation releases the inorganic nutrients and humification piles up humus
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Humification and mineralisation are printed one after the other as the last two steps, so a student who has decomposition secure takes the humus line for mineralisation, and the nutrient-release line is then the only one left for detritus
- **Why:** This question requires the definition NCERT prints for each step of decomposition, demonstrated by "Accumulation of dark coloured amorphous colloidal substance" standing for humification with no rule given from which it could be derived.
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
- **Concept:** The nucleolus is the nuclear site where ribosomal RNA is actively transcribed
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  RNA is transcribed from DNA, and inside the nucleus the DNA is the chromatin, so a student working from that general rule names chromatin as the site. The rRNA genes do lie in chromatin, but the site NCERT names is the nucleolus, the non-membrane-bound mass where that transcription is gathered.
- **Why:** This question requires the one site NCERT names for ribosomal RNA synthesis, demonstrated by the stem asking for 'the site for active ribosomal RNA synthesis' against four named cell structures with no criterion printed to apply.
- **Note:** Applied the likeness-against-position test on the trap axis: no printed option resembles 'nucleolus' as a word, and chromatin is reached by the rule 'RNA comes from DNA' rather than by position in the text, so the axis falls on the site error and not on look_alike_term or nearby_fact.
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
- **Concept:** Respiratory quotient is CO$_2$ released divided by O$_2$ consumed, and a hydrogen-rich fat burns at about 0.7 while a carbohydrate gives 1
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  RQ $=1$ is the value carried for carbohydrates, printed in the same NCERT passage as the fat value, so a student who recognises 'respiratory quotient' and recites the stock number never divides. Dividing the printed coefficients gives $\frac{102}{145} = 0.70$, which is the fat band, not 1.
- **Why:** This question requires computing a ratio from the numbers printed in the stem, demonstrated by the stem asking for 'The Respiratory Quotient (RQ) of a biomolecule used for respiration, as per the above equation' above an equation printing $102\,\mathrm{CO_2}$ against $145\,\mathrm{O_2}$.
- **Note:** The substrate formula as stored reads $\mathrm{C_{51}H_{98}C_{6}}$, which lists carbon twice; the last element should be O. The answer is decided by the printed $102\,\mathrm{CO_2}$ and $145\,\mathrm{O_2}$ coefficients, so the typo does not change the key, but the stem needs repair before this question is shown.
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
- **Concept:** Each inheritance pattern has its standard example: Antirrhinum for incomplete dominance, ABO for co-dominance, phenylketonuria for pleiotropy, human skin colour for polygenic inheritance
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  ABO blood groups are printed in the multiple-alleles discussion that sits beside polygenic inheritance, and with multiple alleles missing from List I the student files ABO under its neighbour, which leaves human skin colour for co-dominance
- **Why:** This question requires the standard example NCERT prints for each inheritance pattern, demonstrated by "Inheritance of flower colour in Antirrhinum sp." and "ABO blood groups" being offered as named cases rather than as crosses to work through.
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
- **Concept:** The DNA fingerprinting sequence: digest the isolated DNA, separate the fragments by electrophoresis, blot them onto a membrane, hybridise a labelled VNTR probe, then autoradiograph
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  The probe is stored as the step that follows the gel, so hybridisation is placed straight after electrophoresis and the blotting step slides down one place; A, E, B, C, D keeps all five steps and runs the probe one stage too early.
- **Why:** This question requires the taught order of a named procedure, demonstrated by the stem 'Arrange the following steps of DNA fingerprinting in a correct sequence' and four options that are each a five-letter sequence.
- **Note:** E1_question_type is arrange_in_order, for which the three-field vocabulary carries no qtype value; the printed shape is a lettered block A to E, so qtype follows the rulebook's lettered-list clause and the ordering demand is carried by asks: order. The trap is one step held at the wrong stage of the protocol, which §5.1 reversed excludes by its own 'not one swapped pair inside a longer order', so it is recorded under wrong_site_attacked, whose definition covers the right change made at the wrong position, stage or site.
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
- **Concept:** Nucleosome assembly: histones are positively charged basic proteins rich in lysine and arginine, and negatively charged DNA wraps around the histone octamer
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  D is the textbook's own sentence about DNA wrapping around the histone octamer with one word altered, so a reader who has already caught the plain error in B - histones are not negatively charged - recognises D as the familiar line and lets 'positively charged DNA' through.
- **Why:** This question requires each printed line on DNA packaging to be judged against the stated fact, demonstrated by the stem 'Which of the following statements are correct with reference to packaging of DNA helix?' over a lettered block whose options select a subset.
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
- **Concept:** Water splitting belongs to PS II, Kranz anatomy belongs to the C4 leaf, and a C4 plant's main sugar-making pathway is still the C3 cycle
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  PS I and PS II differ by one numeral, so A reads as the familiar water-splitting line and survives the check, and the same one-character slip lets D's Kranz claim stand; needing something incorrect, the reader strikes the two C4 sentences instead and submits B and C.
- **Why:** This question requires each printed line to be judged against the stated fact under a negated task, demonstrated by the stem 'Find the incorrect statement(s) about photosynthesis from the following' over a lettered block A to E.
- **Note:** The stem is negated but the trap is not a polarity slip: the set of correct statements, B, C and E, is not printed as an option, so no option is reached by answering the un-negated question. The 'not' in negative_words_seen also appears inside statement C as part of its premise.
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
- **Concept:** Somatic hybridisation in order: isolate single cells from two varieties, digest the walls, free the naked protoplasts, fuse them, then grow the hybrid protoplast into a plant
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  D and B both open with the word 'isolation', so the two isolation steps are read as consecutive and wall digestion is pushed to third place; D, B, A, E, C keeps all five steps and holds digestion and fusion each one stage out of place.
- **Why:** This question requires the taught order of a named technique, demonstrated by the stem 'Arrange the following steps of somatic hybridisation in a correct sequence' and four options that are each a five-letter sequence.
- **Note:** E1_question_type is arrange_in_order, for which the three-field vocabulary carries no qtype value; the printed shape is a lettered block A to E, so qtype follows the rulebook's lettered-list clause and the ordering demand is carried by asks: order. The trap label follows the same mapping as q109: a step held at the wrong stage is excluded from reversed ('not one swapped pair inside a longer order') and is covered by wrong_site_attacked's 'wrong position, stage or site'.
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
- **Concept:** Where each named plant tissue sits and what it is made of: conjunctive tissue between xylem and phloem, Casparian strips of suberin in the endodermis, subsidiary cells around the guard cells, the starch-rich endodermal layer as the starch sheath
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each List I term is glossed by its own line through a shared word or a transparent one - conjunctive to "Tissue between xylem and phloem", suberin to Casparian strips, starch to starch sheath, "in the vicinity of guard cells" to subsidiary cells - and every wrong code breaks at least one of those glosses, while the one discrimination the lists do set up, two lines that both open "Endodermal cells", is not offered by any code: none pairs Casparian strips with the starch-rich line.
- **Why:** This question requires what each named tissue is made of or sits beside, demonstrated by List II's "Endodermal cells with suberin deposition" naming the Casparian strip by its material.
- **Note:** no_trap here is a finding about the option set, not a gap: the confusion the lists invite - two List II lines both beginning "Endodermal cells", one starch-rich and one suberised - is never printed as a code, since no option pairs Casparian strips with line II. A reviewer who wants to re-open this should check that row first.
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
- **Concept:** The three growth phases of a root tip: meristematic cells are protoplasm-rich with large conspicuous nuclei, while elongating cells vacuolate, enlarge and lay down new wall
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Wall thickening is printed as the maturation phase's business one line further on, so a student scanning for the trait that does not belong strikes out the wall option. NCERT lists new cell wall deposition among the elongation phase's own three characteristics, and the trait borrowed from a neighbouring phase is the large conspicuous nucleus of meristematic cells.
- **Why:** This question requires the three characteristics NCERT lists for the phase of elongation, demonstrated by option 4 'Large conspicuous nuclei' being the trait printed for the meristematic zone instead.
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
- **Concept:** Each plant growth regulator carries one signature use: 2,4-D kills dicot weeds, gibberellin speeds malting in brewing, cytokinin mobilises nutrients, ABA closes stomata
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked all three wrong codes pair by pair: none is a single swap away from the key, each needs three separate displacements, and every one of them moves 2,4-D off 'Herbicide', the pairing the chapter states as a near-definition. The one confusion the chapter does support, gibberellin against cytokinin over 'Nutrient mobilisation', produces A-III, B-IV, C-I, D-II, and that code is not printed.
- **Why:** This question requires the use NCERT states for each growth regulator, demonstrated by List-II printing 'Brewing industry' and 'Herbicide' as uses with no criterion supplied from which they could be derived.
- **Note:** Same key pattern as q128, A-III, B-I, C-IV, D-II, and the same structural outcome. The single confusion the chapter supports here is gibberellin's malting role read as 'Nutrient mobilisation', which NCERT prints under cytokinins; alone it gives A-III, B-IV, C-I, D-II, which is not among the printed options. Every printed wrong code additionally moves 2,4-D off 'Herbicide'.
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
- **Concept:** Carboxylation in the Calvin cycle is done by RuBisCO, which adds CO2 to RuBP; PEP carboxylase does the equivalent first fixation in the C4 pathway
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  PEP carboxylase is the enzyme NCERT names as THE carboxylating enzyme two sections later, in the C4 pathway, so a student carrying "the carboxylating enzyme of photosynthesis" as one item reaches for it. It fixes CO2 into a 4-carbon acid in the mesophyll, which is not a step of the Calvin cycle the stem names.
- **Why:** This question requires the enzyme NCERT names for the carboxylation step of one named pathway, demonstrated by the stem fixing the pathway as "in the Calvin cycle" while two other options are genuine carboxyl-handling enzymes from elsewhere in the syllabus.
- **Note:** Likeness test applied on option 2: PEP carboxylase and RuBP carboxylase-oxygenase share the word "carboxylase", but the stem asks for a carboxylase, so both the right and the wrong name must contain it; replace PEP carboxylase with an unlike name for the C4 enzyme and the pull survives, because what carries the student is that NCERT prints it as a CO2-fixing carboxylase in the same chapter. Hence nearby_fact, not look_alike_term.
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

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Calvin-cycle cost: 3 ATP and 2 NADPH per CO2 fixed, and six turns per glucose, giving 18 ATP and 12 NADPH
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  NCERT prints the per-CO2 cost as 3 ATP and 2 NADPH; a student who stored the two rates as the pair "3 and 2" without fixing which cofactor takes which attaches 2 to ATP and 3 to NADPH, and six turns then give exactly $12$ ATP and $18$ NADPH. Both printed numbers are real totals for this pathway, so nothing in the option looks out of place.
- **Why:** This question requires the ATP and NADPH totals NCERT prints for one glucose, demonstrated by the stem supplying no numbers at all to compute from, only the pathway name in "through the Calvin pathway", while each option is a stored pair.
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
- **Concept:** Solanaceae floral formula: actinomorphic, bisexual, gamosepalous calyx of five, gamopetalous corolla of five, five epipetalous stamens, bicarpellary syncarpous superior ovary
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Fused sepals and fused petals are the two Solanaceae characters a student encodes as brackets, and this option carries both, plus the right stamen count and the right superior bicarpellary ovary. What it drops is the arc joining $\mathrm{C}_{(5)}$ to $\mathrm{A}_{5}$, because epipetaly is a relation between two whorls and leaves no bracket of its own, so the string reads correct while describing stamens free of the corolla.
- **Why:** This question requires the floral formula NCERT prints for one named family, demonstrated by the stem asking "the correct floral formula of Solanaceae family" while all four options use the same notation and differ only in which Solanaceae characters they assert.
- **Note:** The options are notation strings, so the printed shape could be read as a symbolic set; the notation itself is common to all four, and what separates them is whether the calyx is fused and the stamens epipetalous, i.e. printed facts about the family, so asks stays fact_line rather than apply_rule.
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
- **Concept:** In situ conservation protects the organism in its own habitat (biosphere reserves, national parks, sanctuaries, sacred groves); ex situ keeps it outside that habitat (zoos, safari parks, botanical gardens, seed banks)
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  "Wildlife Safari Parks" is built from the same two words as the in situ categories NCERT names, wildlife sanctuary and national park, so a student sorting the options by their names reads it as a protected stretch of habitat. It is an enclosure stocked with animals brought in from elsewhere, which is why NCERT prints it in the ex situ sentence beside zoological parks.
- **Why:** This question requires the category NCERT files each named method under, demonstrated by the stem's "an in situ conservation method" with four methods the book assigns explicitly to one list or the other.
- **Note:** Likeness test applied on option 2: replace "Wildlife Safari Parks" with an unlike ex situ name such as cryopreservation and the pull dies, so the resemblance to "national park" and "wildlife sanctuary" is what carries the student, not mere adjacency in the ex situ list. Hence look_alike_term, which is why this question's label differs from q121's nearby_fact.
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
- **Concept:** Endonucleases cut inside DNA at recognised palindromic sites, a little away from the centre, while removing nucleotides from the ends of a fragment is the exonuclease job
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The chapter's line pairs the cut with 'the centre of the palindrome', so a student holding the phrase without its qualifier marks C true and keeps only D as false. Option 3 is then the one set that carries D, and it pays for that by taking E, which is true.
- **Why:** This question requires the printed facts about what restriction endonucleases do, demonstrated by statement D, 'They remove nucleotides only from the ends of DNA fragments', which is the chapter's description of an exonuclease.
- **Note:** Options 1 and 2 are both all-true sets reached by the same miss of the stem's 'not', and neither dominates the other, so the one trap is recorded on option 3, the only wrong option that follows from a specific content error — statement C read without 'a little away from'. The printed key (4) agrees that C and D are the untrue statements.
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
- **Concept:** Racemose inflorescence: the main axis keeps growing and flowers are borne laterally in acropetal succession; cymose is the opposite, the axis ending in a flower
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The one vivid sentence a student carries out of the inflorescence section is "the main axis terminates in a flower", and it is printed in the cymose paragraph immediately beside racemose, so it comes back attached to whichever of the pair is asked for. It is the defining property of the other type, and it is incompatible with the acropetal succession the racemose axis allows.
- **Why:** This question requires the property NCERT states for one named inflorescence type, demonstrated by the blank in "In racemose inflorescence, _________" being filled by one of four printed properties of inflorescences.
- **Note:** E1 recorded fill_in_blank, which rulebook §1 treats as an overlay rather than a shape; the printed shape is a stem and four coordinate options, so qtype is mcq. Likeness test applied on option 1: racemose and cymose do not resemble each other, and swapping them for two unlike words leaves the pull intact, because the two descriptions are printed side by side. Hence nearby_fact.
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
- **Concept:** Microsporogenesis runs sporogenous tissue to pollen mother cell, then meiosis to a microspore tetrad, then free pollen grains
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The shared word in 'pollen mother cells' and 'pollen grains' invites chaining D straight to C, which pushes the tetrad to the end. The order then has its first two places right and its last two inverted, because the tetrad is what meiosis of the pollen mother cell produces and the grains come out of it.
- **Why:** This question requires the developmental order of the printed stages, demonstrated by the stem's 'Arrange the following in the correct developmental sequence related to microsporogenesis' with four options that differ only in the order of the same four items.
- **Note:** E1 read this as `arrange_in_order`, which has no entry in the current qtype list. The printed shape is a lettered block of four items with ordering options, so qtype is `statements` under the printed-list rule and the ordering demand is carried by asks: order.
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
- **Concept:** Each biomolecule class by its defining chemistry: lipids water-insoluble, proteins polypeptides, polysaccharides long sugar chains, and adenine and guanine substituted purines
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Purine and pyrimidine are the paired names a student stores together for the nitrogenous bases, and D prints the wrong one of the pair against adenine and guanine. Swap 'pyrimidines' for an unlike word and nothing pulls at all, so it is the likeness of the two names doing the work, not where they sit.
- **Why:** This question requires the stated chemical identity of each biomolecule class, demonstrated by statement D, 'Adenine and guanine are substituted pyrimidines', set against the chapter's 'substituted purines'.
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
- **Concept:** Haplodiploid sex determination in honeybees: a fertilised egg gives a diploid female, an unfertilised egg gives a haploid male, and the haploid drone makes sperm by mitosis
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  'Sperms are made by meiosis' is the rule carried over from human gametogenesis, and D offers it for the drone, but the drone is already haploid and has no second chromosome set to halve, so he makes sperm by mitosis. Taking D fills the fourth slot, and the statement squeezed out is E, the one carrying the term a student may not have stored.
- **Why:** This question requires the stated facts of haplodiploid sex determination in honeybees, demonstrated by statement D, 'Males produce sperms by meiosis', which the drone's haploid condition rules out.
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
- **Concept:** Plasticity: the same plant forms different structures, such as different leaf shapes, in response to its environment
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Plasticity and elasticity differ by one syllable and both are borrowed from how a material answers being pushed, so a student who holds the sense of the idea but not the word reaches for the more familiar of the two. Elasticity would mean the leaf springs back to one fixed shape, the opposite of a plant making a different leaf for each environment.
- **Why:** This question requires the name NCERT gives one phenomenon, demonstrated by the stem offering its own printed example, "heterophyllous development in response to environment", and asking which phenomenon it illustrates.
- **Note:** Likeness test applied on option 2: swap elasticity for an unlike chapter term such as senescence and the pull dies, so the near-identical word form is doing the work. Hence look_alike_term, even though options 1 and 3 are also printed in the same section.
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
- **Concept:** Amino acids are substituted methanes, and they are sorted acidic, basic or neutral by the groups the side chain adds: glutamic acid acidic, lysine basic, valine neutral
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Lysine is printed in the same one-line classification as the acidic example, so a student who kept the sentence's three examples but not which label each takes reads D as true, and every amino acid does carry a carboxyl group, which makes 'acidic' feel safe. Swap 'acidic' for an unlike word and the pull survives, because it is the neighbouring printed example carrying the student, not any likeness between the words.
- **Why:** This question requires the chapter's printed classification of named amino acids, demonstrated by statement D, 'Lysine is an acidic amino acid', against the line that names lysine as the basic example.
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

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT's 'evil quartet' is a closed list of four causes of biodiversity loss - habitat loss and fragmentation, over-exploitation, alien species invasions, co-extinctions - and no form of pollution is a member
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Pollution is taught elsewhere in the syllabus as a driver of species loss, so a student holding three of the four names fills the fourth slot with 'Air pollution'. Three of the four printed items are genuine members and the option still scores zero, because the missing member is habitat loss and fragmentation.
- **Why:** This question requires the four names in NCERT's stated list, demonstrated by every option ending in 'Co-extinctions' and differing only in whether a pollution type replaces one of the other three.
- **Note:** Printed shape: each option is a set of four same-kind items accepted or rejected whole (rulebook section 1 `pair_options`, 'half an option right scores zero'). The three-field vocabulary has no value for that shape, so `mcq` is recorded and the shape is reported here. The pattern's `statement_options` also does not match, since no option is a statement to be judged. Options 1 and 4 are one device printed twice, differing only in which pollutant is named; option 1 is recorded as the primary and option 4 carries the identical route under other_options.
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
- **Concept:** Respiration is compartmentalised: glycolysis in the cytoplasm, Krebs' cycle in the matrix, the electron transport chain on the inner membrane, and the proton gradient built up in the intermembrane space
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked all three wrong codes pair by pair: none is a single swap away from the key, and each one moves glycolysis out of the cytoplasm or Krebs' cycle out of the matrix as well. The one confusion this material supports, the inner membrane where the ETS sits against the intermembrane space where protons accumulate, produces A-III, B-IV, C-I, D-II, and that code is not printed.
- **Why:** This question requires the cell compartment NCERT states for each respiratory stage, demonstrated by List-II being four locations, 'Inner mitochondrial membrane', 'Mitochondrial matrix', 'Cytoplasm' and 'Intermembrane space'.
- **Note:** The confusion this question invites is between the inner mitochondrial membrane, where the ETS complexes sit, and the intermembrane space, where the protons pile up. Holding glycolysis in the cytoplasm and Krebs' cycle in the matrix, that confusion reads A-III, B-IV, C-I, D-II, and that code is not among the four printed options. Each printed wrong code vacates the cytoplasm or the matrix in addition, so the finding is no_trap rather than a forced tag.
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
- **Concept:** Triple fusion makes the primary endosperm cell 3n; the egg and its neighbours in the embryo sac stay haploid and syngamy yields only a 2n zygote
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  Triple fusion happens inside the central cell, so a student who remembers where the 3n state is made names the container instead of the product. Before fusion that cell holds only its two haploid polar nuclei; it is 3n only after the male gamete joins them, and from that moment it is called the primary endosperm cell.
- **Why:** This question requires the stated ploidy of one named cell of the embryo sac, demonstrated by the four options being embryo-sac cells with 'triploid' the only criterion printed.
- **Note:** Read as wrong_site_attacked rather than nearby_fact: the central cell and the primary endosperm cell are not two items printed side by side but the same cell before and after triple fusion, so what the student gets wrong is the stage, not a neighbouring item.
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
- **Concept:** Only xenogamy brings pollen from a different plant, so only it delivers genetically different pollen; geitonogamy is cross-pollination in mechanism but a self-pollination genetically
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Geitonogamy moves pollen from one flower to another and needs a pollinating agent to do it, so a student who equates 'another flower' with 'another plant' takes it for the outcrossing case. Both flowers sit on the same plant, so the pollen that arrives is genetically identical to the stigma's own - which is the one thing the stem asks about.
- **Why:** This question requires the one pollination type NCERT ties to genetically different pollen, demonstrated by the stem's phrase 'brings genetically different types of pollen grains to the stigma'; swapping 'geitonogamy' for an unlike word leaves the pull intact, so position and not likeness carries it - nearby_fact, not look_alike_term.
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
- **Concept:** Placentation types are told apart by the standard example of each: marginal in pea, axile in lemon, parietal in mustard, basal in marigold
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Placentation is learnt as an ordered list with one example printed against each type, and this code keeps parietal-mustard and basal-marigold while reading pea and lemon off the neighbouring line, giving marginal-lemon and axile-pea.
- **Why:** This question requires the example NCERT prints for each placentation type, demonstrated by List-II being four plant names, 'Mustard', 'Pea', 'Marigold' and 'Lemon', rather than ovary descriptions a criterion could sort. Swap test applied: replace 'Marginal' and 'Axile' with two unlike words and the pull survives, because adjacency in the printed list of placentation types is doing the work, so nearby_fact rather than look_alike_term.
- **Note:** In our record the separator between the second and third pair of every option is printed as a full stop rather than a comma, for example 'A-II, B-IV. C-I, D-III'. The pairing codes themselves are complete, so this is typographic only and the question is tagged as printed.
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
- **Concept:** Whittaker's criteria for the five-kingdom system: cell structure, thallus or body organisation, mode of nutrition, reproduction and phylogenetic relationships
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Flagella are a character the same chapter uses to describe groups inside the kingdoms, so 'presence of flagellum' reads as another criterion to a student who recalls the list loosely. Accepting C turns a correct four into the all-five option and leaves nothing to rule out. Swap 'presence of flagellum' for an unlike phrase from outside the chapter and the pull dies, so it is position in the chapter doing the work rather than any resemblance to the other criteria.
- **Why:** This question requires the criteria listed for Whittaker's scheme, demonstrated by the stem's 'The main criteria used for Five Kingdom Classification proposed By R.H. Whittaker (1969) included' set against the printed item 'Presence of flagellum'.
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
- **Concept:** Biomolecules are filed by the class NCERT names them under: trypsin an enzyme, morphine an alkaloid, concanavalin A a lectin, collagen the protein of the intercellular ground substance
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Morphine and concanavalin A are printed in the same NCERT table of secondary metabolites, in the rows headed alkaloids and lectins, and this code exchanges the two names between those rows while keeping trypsin-enzyme and collagen-ground substance.
- **Why:** This question requires the class NCERT files each named molecule under, demonstrated by List-II being class names, 'Lectin', 'Enzyme', 'Alkaloid', plus one location, 'Intercellular ground substance'. Swap test applied: 'Morphine' and 'Concanavalin A' resemble each other in nothing, and the pull survives their replacement by unlike words because both are printed in the same secondary-metabolite table, so nearby_fact.
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
- **Concept:** Gel electrophoresis sorts DNA fragments by size, and the bands stay invisible until ethidium bromide staining is viewed under UV
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Statement B is the secure half -- electrophoresis sorts fragments by size -- and statement D keeps NCERT's own reagent, ethidium bromide, altering only the lamp to visible light, so the bundle reads as the printed protocol.
- **Why:** This question requires each printed statement about the separation and visualization protocol to be adjudicated against the line the chapter states, demonstrated by statement D's 'when stained with ethidium bromide, can be seen in visible light' sitting beside statement C's 'can be seen without staining when exposed to UV light', which split one printed sentence into two half-truths.
- **Note:** Every wrong option pairs exactly one true statement with one false one, so all three carry a route and none is filler. That is a property of how the four combinations were built, not padding.
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
- **Concept:** Sickle-cell anaemia is a single substitution - Glu to Val at position 6 of the beta globin chain, a qualitative defect - while thalassaemia reduces how much globin is made
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Thalassaemia is the other beta globin disorder NCERT prints in this same section, so a student who registers the phrase 'beta globin chain' and stops there reaches for it. Thalassaemia is a quantitative fault - less globin synthesised - and no amino acid is substituted anywhere in it.
- **Why:** This question requires the disorder NCERT ties to one named substitution, demonstrated by the stem printing 'substitution of Glutamic acid (Glu) by Valine (Val) at the sixth position of the beta globin chain'; swapping 'Thalassemia' for an unlike word leaves the pull intact, because the shared beta globin content and not the spelling carries it - nearby_fact, not look_alike_term.
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
- **Concept:** One printed action per hormone: cortisol is anti-inflammatory, aldosterone drives sodium and water reabsorption, cholecystokinin drives pancreatic and bile secretion, progesterone forms the mammary alveoli
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Cortisol and aldosterone are the two adrenal cortex hormones printed in consecutive sentences, and the chapter also says cortisol maintains kidney function, so the renal line is read onto cortisol and the anti-inflammatory line onto aldosterone.
- **Why:** This question requires the single action NCERT states for each hormone, demonstrated by List-II printing whole actions such as 'Produces anti-inflammatory reactions' and 'Stimulates secretion of pancreatic enzymes and bile juice'. Swap test applied: 'Cortisol' and 'Aldosterone' resemble each other in nothing, and the pull survives replacement by unlike words because the two are printed in the same adrenal cortex paragraph, so nearby_fact.
- **Note:** Two of the three wrong codes are single transpositions of the key and both carry a route, so this question is the one member of the group with a second entry under role trap.
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
- **Concept:** The renin-angiotensin cascade is switched on by a fall in glomerular filtration and ends with blood pressure and GFR restored
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The cascade is remembered as the body's blood-pressure machinery, so 'Increase in blood pressure and Glomerular filtration rate' reads as the stimulus that sets it going; it is what the cascade produces, and the printed stimulus is 'Fall in Glomerular filtration rate'.
- **Why:** This question requires the steps of the cascade to be placed in causal order, demonstrated by the list printing both 'Fall in Glomerular filtration rate' and 'Increase in blood pressure and Glomerular filtration rate', so which of the two is stimulus and which is result decides the answer.
- **Note:** E1 recorded arrange_in_order, which is retired vocabulary; the current qtype list has no order value, so the printed lettered block is recorded as statements and the ordering demand sits in asks: order.
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
- **Concept:** Human respiration runs as five linked steps: breathing in, exchange across the alveolar membrane, transport in blood, exchange at the tissues, then use of oxygen in the cell
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Both diffusion statements open with the same words, so a student holding the chain as 'ventilation, then diffusion, then transport, then cellular respiration' takes the diffusion step that is listed first -- A, at the tissues -- and puts it where the alveolar exchange belongs.
- **Why:** This question requires the five respiratory steps to be sequenced, demonstrated by 'Arrange these steps in the correct order' printed over two statements that differ only in their site, 'between blood and tissues' and 'across alveolar membrane'.
- **Note:** E1 recorded arrange_in_order, which is retired vocabulary; the printed shape is a lettered block, so qtype is statements and the ordering demand sits in asks: order.
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
- **Concept:** Plasmodium in the human host: sporozoites from the bite multiply in liver cells, then in red cells, and gametocytes form last for the mosquito to pick up
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Gametocytes are filed with the mosquito's share of the cycle, so a student who opens correctly at the bite puts 'Gametocytes develop in RBCs' next to it; the gametocytes form only after the parasite has been through the liver and into the red cells.
- **Why:** This question requires the stages of the malarial cycle to be sequenced, demonstrated by 'Arrange the stages in the proper order' printed over stages that each name their own site -- liver cells, RBCs -- and the bite that starts the human phase.
- **Note:** E1 recorded arrange_in_order, which is retired vocabulary; the printed shape is a lettered block, so qtype is statements and the ordering demand sits in asks: order.
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
- **Concept:** Insertional inactivation: an insert disrupts only the gene it lands inside, and in pBR322 the BamHI site lies within the tetracycline resistance gene, so the recombinant loses tetracycline resistance and keeps ampicillin resistance
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Ampicillin resistance is the other marker printed on the same pBR322 map, so a student holding 'insertion knocks out one of pBR322's two resistance genes' without fixing which gene carries BamHI names it. BamHI and SalI sit inside tetR, and the intact ampR is precisely what the selection plate still relies on.
- **Why:** This question requires which resistance gene of pBR322 carries the named site, demonstrated by the stem's 'Insertion of a foreign DNA at BamHI site'; swapping 'Ampicillin' for an unlike word leaves the pull intact, since the two names do not resemble each other and it is their position on one plasmid map that carries the student - nearby_fact, not look_alike_term.
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
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Enzymes are classed by the kind of change they catalyse, so naming the class means reading what the printed reaction does to the substrate
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the class is decided by the reaction printed as a figure, and only the image path was supplied to this step, so no route to a wrong class can be confirmed
- **Why:** This question requires the enzyme-class criterion applied to a printed transformation, demonstrated by the stem's 'The following reaction depicts the activity of a particular class of enzymes : Identify the enzymes class E from the following options'.
- **Note:** has_figure is true and the deciding content - the reaction itself - exists only as the image at figures_agent/2026_11/q141.png, which this step could not open, so the transformation could not be read. The paper is intact, so this is not source damage. A reviewer holding the figure should check look_alike_term on option 4: Lyases and Ligases differ by two letters, are learnt in the same six-class list, and the rulebook names that pair as the type case; if the figure instead shows a group being moved from one molecule to another, Transferases (option 1) would be the option carrying the route. asks is taken from the stem's instruction to identify the class from a printed reaction, which is the classification rule applied to a new case with no quantity produced. difficulty_level arrives as 'unsure' from an earlier step and was not re-opened.
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
- **Concept:** Chemical transmission across a synapse runs one way: the pre-synaptic membrane releases the transmitter and the post-synaptic membrane carries the receptors that bind it
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  The pre-synaptic membrane is the side where everything remembered happens — vesicles fuse there and the transmitter is released there — so the receptors get placed on that same membrane. The transmitter has to cross the cleft first, and the receptors sit on the membrane it arrives at.
- **Why:** This question requires the fact NCERT states about which side of a synapse carries the transmitter receptors, demonstrated by 'The specific receptors for neurotransmitters in a synapse are present on __________' offering four named structures with no criterion printed to apply.
- **Note:** E1 called this fill_in_blank; the rulebook treats a printed blank as an overlay rather than a shape (section 1), so the primary shape recorded here is mcq.
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
- **Concept:** In the ABO series $i$ is recessive to both $I^A$ and $I^B$, so two heterozygous parents each carry a hidden $i$ and one child in four is $ii$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Set the cross up from the parents' blood GROUPS instead of the genotypes the stem states and there is no $i$ allele anywhere in it, so an O child reads as impossible. The word 'heterozygous' is exactly what puts a hidden $i$ into each parent.
- **Why:** This question requires computing a probability from the parental genotypes the stem specifies, demonstrated by 'both mother and father are heterozygous for ‘A’ and ‘B’ blood group, respectively' with four percentages as the options.
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
- **Concept:** The four respiratory volumes and their printed values: TV 500 mL, IRV 2500-3000 mL, ERV 1000-1100 mL, RV 1100-1200 mL
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  RV is read as a reserve volume, since 'Residual' and 'Inspiratory Reserve' both shorten to the same R and RV sits inside IRV, so the largest range, 2500-3000 mL, goes to RV and IRV is left with 1100-1200 mL.
- **Why:** This question requires the stored value NCERT gives for each respiratory volume, demonstrated by List-II being four printed figures, '500 mL', '1000-1100 mL', '1100-1200 mL' and '2500-3000 mL'. Swap test applied: replace 'Residual Volume' and 'Inspiratory Reserve Volume' with two unlike words and the pull dies, because the shared R and the abbreviation RV sitting inside IRV are what carry it, so look_alike_term and not nearby_fact.
- **Note:** The other confusion available here, between the two adjacent ranges 1000-1100 mL and 1100-1200 mL for ERV and RV, is not offered by any printed code; a swap of A and B against the key gives A-IV, B-III, which appears in none of the four options. In list_i the fourth label is printed as 'D' without a full stop, which changes nothing in the pairing.
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
- **Concept:** Convergent evolution gives analogous structures — the same job arrived at from different ancestry; one ancestral plan put to different jobs is homology, which is divergent
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Butterfly and bird wings are the pair the text introduces analogy with, so it is the first thing the phrase 'convergent evolution' calls up. It is a correct example of convergent evolution, which is the question with the 'not' taken out.
- **Why:** This question requires knowing which of the printed example pairs belongs to the analogy list and which to the homology list, demonstrated by 'Fore limbs of whales and bats' standing among three pairs the text prints as analogous.
- **Note:** E1 called this statement_options; the printed options are short noun phrases naming a pair of organisms, not statements to judge, so the shape recorded is mcq. I considered asks: compare, since analogy has to be held apart from homology, and did not use it: all four pairs are the text's own printed examples, so what decides the answer is which list each pair is printed in rather than a criterion applied to unfamiliar cases. A reviewer who reads the question as applying the common-ancestry test instead would read it as compare.
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
- **Concept:** Sexual dimorphism in the frog: vocal sacs and the copulatory pad mark the male, while the rest of the frog's external morphology is shared by both sexes
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Vocal sacs are the one male feature a student is sure of, so the choice collapses to its partner, and 'Bulging eyes' is a frog character printed in the same morphology description -- true of the animal, but given for the frog, not for the male.
- **Why:** This question requires the frog features printed as male-only, demonstrated by 'Male frogs can be distinguished from female frogs due to the presence of' standing over three characters -- bulging eyes, webbed digits, olive green skin with dark spots -- that are stated of the frog as a species.
- **Note:** half_right was considered, since each wrong option has two parts; answers_other_question was taken instead because the failing part is a TRUE frog character answering 'features of the frog' rather than a statement with an error in it. That is what separates this question from q134, where the failing statement is factually wrong.
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
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Cyclostome diagnosis: a cartilaginous skeleton with a circular sucking mouth, an ectoparasitic habit, and gill slits but no paired fins or scales
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  'Endoskeleton was made of cartilage' is the headline character of the cartilaginous fishes, whose section sits beside the cyclostomes, so a student who decides on character A alone names that section's example; characters B and C -- a circular sucking mouth and no paired fins or scales -- rule a shark out.
- **Why:** This question requires the three printed diagnostic characters to be applied to four named chordates, demonstrated by 'Which of the following species of animals did they consider to fit best with these characters?' standing over 'attached on fish skin with their circular sucking mouth' and 'Paired fins and scales were absent, but 7 pairs of gill slits were present'.
- **Note:** E1's pattern returned plain_mcq by default, but the printed shape carries a lettered block A-C of observed characters above the options, so qtype is recorded as statements; unlike the other members, the options here are single species names rather than a combination code. Rule 2 therefore bars half_right on option 1, which is a lone wrong name.
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
- **Concept:** The chapter's evolutionary time-line: which life form is dated to 500, 350, 320 and 65 million years ago
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  A student who dates the two remaining rows by what must have come first, rather than by the figures the chapter prints, moves the seaweeds back to 350 mya and the jawless fish forward to 320 mya, which is the code option 3 prints.
- **Why:** This question requires the figure the chapter attaches to each named event, demonstrated by List I printing only bare dates — 'About 65 mya', 'About 500 mya', 'About 350 mya', 'About 320 mya' — with nothing in the stem from which a date could be worked out.
- **Note:** List I's fourth label is printed 'D' without the stop the other three carry; the pairing is unaffected. The key follows the chapter's own wording, which dates seaweeds and few plants later (about 320 mya) than the jawless fish (about 350 mya); tagged as printed.
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
- **Concept:** The contraceptive families — hormone-releasing IUD, copper-releasing IUD, rubber barrier, oral pill — and which named product sits in each
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The copper-releasing IUDs and the hormone-releasing ones are printed in consecutive lines of one list, so a student who has stored 'both of these are IUDs' but not which subtype takes the neighbouring line and exchanges Progestasert with Multiload 375.
- **Why:** This question requires the contraceptive family the chapter assigns to each named product, demonstrated by List II printing the families themselves — 'Hormone releasing IUD', 'Copper releasing IUD', 'Oral contraceptive'. Swap test applied: replace 'Multiload 375' with an unlike word and the trap still stands, because the two names are carried by sitting in the same printed IUD list rather than by resembling each other, so nearby_fact and not look_alike_term.
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
- **Concept:** A leucocyte's absolute count is its share of the differential count applied to the total WBC count: eosinophils 2-3 per cent, lymphocytes 20-25 per cent
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Reaching for 6-8 per cent — the share printed for monocytes in the same differential count — and applying it to the lymphocytes gives $480-640$, which is the $500-700$ band printed here. The share that belongs to lymphocytes is 20-25 per cent, giving $1600-2000$.
- **Why:** This question requires applying the stored differential-count percentages to the total the stem supplies, demonstrated by 'The WBC count of a person’s blood sample is $8000/\mathrm{cu\ mm}$' with every option printed as two absolute counts per cu mm.
- **Note:** E1 called this statement_options; the options are not statements but two numeric bands joined by 'respectively', so the shape recorded is two_part — both bands must be right and half the option right scores nothing.
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
- **Concept:** What each drug of abuse does to the body: nicotine on the adrenal gland, morphine as sedative-painkiller, heroin as depressant, cocaine as stimulant
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Cocaine's euphoria line and heroin's depressant line are printed in the same passage on drug abuse, and a student holding the two only as one block of illicit drugs takes the neighbouring descriptor, handing 'Causes sense of euphoria and increased energy' to heroin.
- **Why:** This question requires the effect the chapter attaches to each drug of abuse, demonstrated by List II printing those effects as the chapter words them — 'Stimulates adrenal gland to release catecholamines into blood circulation', 'Effective sedative and painkiller'. Swap test applied: 'heroin' and 'cocaine' resemble each other in nothing, and the trap survives their replacement by unlike words because the two descriptors sit in one passage, so nearby_fact.
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
- **Concept:** Transgenic animals are used both to make human proteins and to model human diseases; $\alpha$-1-antitrypsin is one of the protein products and the disease it treats is emphysema
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Cystic fibrosis is printed in the sentence straight after the $\alpha$-1-antitrypsin line, as another disease transgenic animals are being aimed at, and again in the list of transgenic disease models — so a student recalling the section lands on the disease next door. Only emphysema is tied to this protein by name.
- **Why:** This question requires the stated fact about which disease $\alpha$-1-antitrypsin is used against, demonstrated by 'The human protein named $\alpha$-1-antitrypsin, obtained from transgenic animals, is used for the treatment of ______' with four disease names and nothing in the stem to reason from.
- **Note:** E1 called this fill_in_blank, which section 1 of the rulebook treats as an overlay, so mcq is recorded as the shape. On the nearby_fact / look_alike_term test: swapping emphysema and cystic fibrosis for two unlike words leaves the trap standing, because what carries the student is the adjacent printed sentence and not any likeness between the two names, so nearby_fact.
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

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Osteichthyes are the bony fishes; several animals carrying 'fish' in their common name are molluscs, echinoderms, cyclostomes or cartilaginous fishes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Fighting fish is Betta, one of the printed Osteichthyes aquarium examples, so recognising that one name vouches for the set. The set is accepted or rejected whole, and saw fish (Pristis) and dog fish (Scoliodon) are both printed under Chondrichthyes.
- **Why:** This question requires knowing which class each named fish is printed under, demonstrated by 'Select the set of fishes which belong to the class Osteichthyes' with each option bundling three common names to be taken whole.
- **Note:** E1 called this statement_options; the options are not statements but sets of three same-kind items accepted or rejected whole, which is the rulebook's pair_options shape (section 1). The current qtype list has no pair value, so it is recorded as two_part, the only multi-part value, on the ground that the answer must hold for every member of the set.
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
- **Concept:** Diagnostic characters of the animal phyla and classes, including the two that get inverted: adult echinoderms are radially symmetrical, and reptiles are poikilothermic
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  'Notochord is persistent throughout life' is the character a student files under the protochordates, so it gets struck from Chondrichthyes. With B already settled, the pair B and D is complete and E never gets read.
- **Why:** This question requires each printed phylum or class character to be judged true or false against the diagnostic lists, demonstrated by 'Bilateral symmetry is a characteristic feature of adult Echinoderms' standing beside 'Pseudocoelom is possessed by Aschelminthes' with no criterion in the stem to apply to either.
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
- **Concept:** A prokaryote has no membrane-bound organelles, so the ribosome is the one organelle the two cell types share
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The centrosome really is a non-membrane-bound organelle, so a student who settles the question on the stem's first clause stops there; the second printed clause, 'found in both prokaryotic and eukaryotic cells', is what rules it out, because a prokaryote has no centrosome.
- **Why:** This question requires the one organelle NCERT describes as lacking a bounding membrane while present in both cell types, demonstrated by the stem's two printed clauses, 'Non-membrane bound cell organelles' and 'found in both prokaryotic and eukaryotic cells'.
- **Note:** E1 reports fill_in_blank; the rulebook treats a printed blank as an overlay, so the shape recorded here is mcq with a blank in the stem. half_right was ruled out because 'Centrosomes' is a lone name, which rule 2 bars from that label; the dropped requirement is printed in the stem, which is condition_missed.
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
- **Concept:** Logistic growth: the braking factor $\frac{K-N}{K}$ cuts the exponential rate $rN$ to zero as the population reaches carrying capacity
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The chapter prints $\frac{dN}{dt} = rN$ for exponential growth just before the logistic form, where the rate climbs with $N$, so a student rebuilding the bracket from that picture writes $\frac{K+N}{K}$; at $N=K$ it gives $2rK$, making growth fastest exactly where it must stop.
- **Why:** This question requires the logistic growth equation as the chapter prints it, demonstrated by the four options differing only in the bracket - '$\frac{K-N}{K}$' against '$\frac{K+N}{K}$', '$\frac{K-N}{N}$' and '$\frac{K}{K-N}$'.
- **Note:** E1 reports statement_options; the four options are printed equations, not statements to be judged, so the shape recorded here is mcq, and rule 1 keeps complex options from making it 'statements'. No filler is recorded because each wrong option clears one of the two anchors of the sigmoid - options 1 and 4 the low-density limit, option 3 the $N=K$ limit - and fails the other.
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
- **Concept:** Rh incompatibility runs one way only, an $\mathrm{Rh^{-ve}}$ mother carrying an $\mathrm{Rh^{+ve}}$ foetus, and the anti-Rh antibodies are given to her after the first delivery
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A prints the mother and foetus the wrong way round, so it is banked at once, and E passes inspection because only the word 'second' is altered in it. The second incorrect statement then has to be found elsewhere, and B's 'majority' is the only line carrying a figure.
- **Why:** This question requires five printed lines about Rh grouping to be checked one at a time against the stated facts, demonstrated by 'Rh incompatibility is observed when a pregnant mother is Rh-ve and the foetus is Rh+ve' being printed as the mirror image of statement A.
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
- **Concept:** Microbial bioactive products and the job each does: clot buster, blood-cholesterol lowering agent, detergent enzyme, immunosuppressant
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Both of these List II entries print the word blood — 'Removal of clots from the blood vessels' and 'Blood cholesterol-lowering agent' — and the chapter names statins and streptokinase in consecutive lines as microbial products acting on blood, so a student holding only 'these two are the blood ones' exchanges them.
- **Why:** This question requires the use the chapter assigns to each microbial product, demonstrated by List II printing those uses — 'Removal of clots from the blood vessels', 'Blood cholesterol-lowering agent', 'Detergent formulations' — with no property in List I from which they could be deduced. Swap test applied: replace 'Statins' with an unlike word and the trap stands, because what carries it is the two products sharing blood as a target in one printed paragraph, not any likeness of name, so nearby_fact.
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
- **Concept:** Modes of gas exchange across animal groups: gills, lungs, lungs plus skin, and diffusion at the cell surface
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong code for a pairing a prepared student could hold: option 2 needs branchial respiration for reptiles, options 3 and 4 need 'Pulmonary and cutaneous respiration' for Amoeba, and option 4 also needs molluscs on cellular respiration. Every code asks for a lung or a gill in an organism that has neither, so no single remembered confusion completes one.
- **Why:** This question requires the mode of gas exchange the chapter assigns to each animal group, demonstrated by List II printing the modes themselves — 'Branchial respiration', 'Pulmonary respiration only', 'Pulmonary and cutaneous respiration', 'Cellular respiration'.
- **Note:** The key pairs Amoeba with 'Cellular respiration'; the chapter's own wording for such organisms is exchange by simple diffusion over the body surface, and List II's term is the paper's. Tagged as printed, with no re-judging of the key.
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
- **Concept:** Sickle-cell anaemia comes from one substitution at the sixth codon of beta globin, GAG to GUG, glutamic acid to valine
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  GAG is the sixth codon printed in the same line as GUG, as the state the mutation starts from, so a student who reads 'sixth codon of beta globin gene' and lets 'mutant' go by answers with the codon that is replaced instead of the one that replaces it.
- **Why:** This question requires the codon that the sickle-cell substitution produces, demonstrated by the stem's 'sixth mutant codon of beta globin gene', which fixes both the position and the mutant side of the pair.
- **Note:** GAG and GUG differ by one letter, so look_alike_term was considered and ruled out by the swap test in 5.1: replace the normal codon with an unlike triplet and the pull survives, because what carries the student is that GAG is the state printed beside the one asked for, not the resemblance. answers_other_question was also ruled out - like the 500-for-400 case in the brief, GAG answers the SAME question asked of the normal gene, not a different question.
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
- **Concept:** The order of events in muscle contraction: $\mathrm{Ca^{++}}$ released into the sarcoplasm unmasks actin so a cross bridge can form, and the actin filaments are then pulled towards the centre of the 'A' band
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  A and B verify at once as the first two printed steps, and D reads as the cross-bridge sentence with its partners swapped, so it is dropped. What is left is the two confirmed steps, which is exactly what this option offers.
- **Why:** This question requires each step of the printed contraction sequence to be checked against the stated mechanism, demonstrated by 'Increase in Ca++ inactivates the actin for breaking cross bridges' placing the relaxation step inside the contraction sequence.
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
- **Concept:** Facts of the human axial skeleton: a dicondylic skull articulating with the atlas, seven cervical vertebrae, cartilaginous joints between adjacent vertebrae, and every rib bicephalic
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The last two pairs of ribs are the one rib exception the chapter teaches, so 'except the last 2 pairs' in D reads as a remembered line. With C and E correct that gives C, D and E, and B is let go because atlas and axis form a pivot joint.
- **Why:** This question requires each stated fact about the axial skeleton to be judged separately against the printed lines, demonstrated by 'All ribs except the last 2 pairs are bicephalic' turning entirely on which rib property the stated exception belongs to.
- **Note:** Statement B is keyed correct and matches the textbook example of a cartilaginous joint, the joint between adjacent vertebrae. Its wording 'any two adjoining vertebrae' is arguable on strict anatomy, since the atlas-axis joint is a synovial pivot. Tagged as printed; this flags the wording, not the key.
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
- **Concept:** Which division sits at which stage of spermatogenesis: spermatogonia multiply by mitosis, the two meiotic divisions give haploid spermatids, and spermiogenesis makes spermatozoa with no division at all
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Spermatogonia do go on to meiosis, so A reads as the headline fact of spermatogenesis and the word 'always' passes unweighed. Added to the two statements that are genuinely correct, it yields A, C and E.
- **Why:** This question requires the division named at each stage of spermatogenesis to be checked against the stated sequence, demonstrated by 'Primary spermatocytes divide mitotically to produce secondary spermatocytes' differing from the printed account only in which division it names.
- **Note:** The stem's words are transposed as extracted, reading 'a series of cell divisions statements to produce sperms. Select the correct from the following'. The task, all five statements and all four options are present, so it was tagged as the 'select the correct statements' item it is.
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

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The JGA is the contact where the distal convoluted tubule returns to touch the afferent arteriole of its own nephron
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The option carries the tubule half a student has fixed, 'Distal convoluted tubule', and settles the vessel by picturing the apparatus where blood leaves the glomerulus, which is the efferent arteriole; the printed answer puts the modified cells on the afferent arteriole, so half of the option scores nothing.
- **Why:** This question requires both structures NCERT names as forming the JGA, demonstrated by the options crossing two tubules with two arterioles, 'Distal convoluted tubule and efferent renal arteriole' against 'Distal convoluted tubule and afferent renal arteriole'.
- **Note:** E1 reports fill_in_blank, an overlay; the printed shape recorded here is two_part because each option is a tubule slot crossed with an arteriole slot and half right scores zero. look_alike_term was considered for afferent/efferent and set aside: the option carries two parts and one of them fails, which is what the 2x2 grid is built on, and the resemblance is named inside the route.
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
- **Concept:** Sexual deceit: the Ophrys flower mimics a female bumblebee, so the male pollinates it while trying to mate
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  The cuckoo laying in a crow's nest with eggs matched to the host's is a genuine deception, so a student who answers on the word 'deceit' lands here; it is the chapter's example of brood parasitism, and the stem's qualifier 'sexual' is what the option fails.
- **Why:** This question requires the named example of sexual deceit, demonstrated by the stem's qualifier 'sexual', which separates 'Ophrys and bumblebee' from the other printed interactions.
- **Note:** Each option names one interaction by its two partners rather than two independently variable slots, so the shape stays mcq and not two_part; 'Ophrys' cannot be recombined with 'crow'.
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
- **Concept:** Frog anatomy as printed: ten pairs of cranial nerves, optic lobes in the mid-brain, a hepatic portal vein between intestine and liver, and the sinus venosus opening into the right atrium
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Twelve pairs of cranial nerves is the count stored for the human brain, so B reads as recall rather than as a claim to test. With A and C verified, A, B and C is complete and E is never weighed.
- **Why:** This question requires each stated fact of frog anatomy to be judged separately against the printed lines, demonstrated by 'There are twelve pairs of cranial nerves arising from the brain' carrying a count that has to be recalled for the frog specifically.
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
- **Concept:** The pregnancy calendar: which foetal development belongs to 8, 12, 20 and 24 weeks
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  The limbs are named twice — with the digits at the end of the second month, and again at 12 weeks where the limbs and external genital organs are said to be well developed — so a student who recalls the 12-week line moves limb development to 12 weeks and is left handing the external genital organs to 8 weeks.
- **Why:** This question requires the week the chapter assigns to each foetal development, demonstrated by the stem asking for 'embryonic development at various months of pregnancy' while List II prints only the weeks — '24 weeks of pregnancy', '20 weeks of pregnancy', '8 weeks of pregnancy', '12 weeks of pregnancy'.
- **Note:** The stem says 'months of pregnancy' while List II is printed in weeks; the pairing is unaffected. nearby_fact was the runner-up label here, since the carrier is the adjacent 12-week line, but what the option changes is the week an event is placed in, so the stage-shift label is used, as in q148.
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
- **Concept:** XO sex determination: the grasshopper male carries a single X and so one chromosome fewer than the female
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  In the human XY scheme the male is marked by a chromosome the female does not have, so a student carrying that picture into XO gives the male the larger count, 24, and reads the two assignments the wrong way round. In XO there is no Y at all, so the male is the 23.
- **Why:** This question requires the XO rule applied to the two counts the stem supplies, demonstrated by 'the chromosome number of some members is 23 and some other members possess 24 chromosomes', with neither sex named in the stem.
- **Note:** E1 reports fill_in_blank, an overlay; the shape recorded here is two_part because the key, 'males and females, respectively', is two assignments that must both hold. This is the one member of the group whose answer is not read off a printed line: the counts 23 and 24 are the paper's, not NCERT's, so the XO rule has to be applied to them.
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
- **Concept:** Haplodiploid sex determination in the honeybee: the drone develops from an unfertilised egg, so his whole set is haploid and his sperms come from mitosis, not meiosis
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The grasshopper is the other insect in the same sex-determination section, where the male carries one X against the female's two, and that unpaired X reads as a half set, so the search for a haploid male stops there; every autosome pair in the male grasshopper is still present in duplicate and his gametes come from meiosis.
- **Why:** This question requires the stated fact that one named animal's males are haploid and form gametes mitotically, demonstrated by the stem's "In which animal" with four unrelated animals as options and no criterion printed to apply to them.
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
- **Concept:** The egg's investments read from the outside in: corona radiata, zona pellucida, perivitelline space, then the ovum's own plasma membrane
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The coverings are usually rehearsed by building outward from the egg itself -- plasma membrane, perivitelline space, zona pellucida, corona radiata -- and written down in that rehearsed direction the answer is D, B, A, C, the exact inversion of the keyed order.
- **Why:** This question requires the stored outer-to-inner sequence of the coverings around the ovum, demonstrated by the stem 'Arrange the following cell layers/structures around the female gamete, from outer to inner side' printing four coordinate layers with no criterion from which the order could be worked out.
- **Note:** E1 returned arrange_in_order, which the v2 qtype axis has no value for; recorded as statements because a lettered A-D block is printed above the options, with the ordering demand carried on the asks axis as order. Option 1 is the exact reverse of the keyed string, which is why reversed rather than half_right applies; options 2 and 4 each move one adjacent pair only.
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
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** The large holes in Swiss cheese are gas pockets: $\mathrm{CO_2}$ released by Propionibacterium sharmanii during ripening
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Option 2 repeats the correct mechanism word for word, "large amount of $\mathrm{CO_2}$", and changes only the bacterium, and Clostridium butylicum is printed in the same chapter's table of microbes and their fermentation products, so the name is taken from that table instead of from the cheese line.
- **Why:** This question requires the cause the textbook gives for a stated observation, demonstrated by the stem's "What is the reason behind production of large holes in 'Swiss Cheese'?".
- **Note:** The pattern classifier called this statement_options on option length, but the stem asks a direct question and the options are rival causes rather than statements to be judged, so the printed shape is mcq.
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
- **Concept:** Bt cry genes are pest-specific: cryIAc and cryIIAb act on the cotton bollworm, cryIAb on the corn borer
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The printed sentence gives the cotton bollworm two genes, cryIAc and cryIIAb, and the corn borer one, cryIAb, so a student recalling it as a block of three names fills both of the question's slots out of the bollworm half and puts cryIIAb where the corn borer gene belongs.
- **Why:** This question requires the two printed gene-to-pest assignments held apart, demonstrated by the stem's "cotton bollworms and corn borer, respectively" and by every option being a pair of gene names accepted or rejected whole.
- **Note:** The pattern classifier returned plain_mcq, but each option is a pair graded whole under "respectively", so the shape recorded is two_part. The stem as stored prints "contrl" for "control"; it does not change what is asked. On the nearby_fact against look_alike_term test: replacing the three gene names with unlike words leaves the pull standing, because what carries the student is the printed pairing of two genes to the bollworm, not the one-numeral likeness of cryIAb and cryIIAb.
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
- **Concept:** A pyramid is inverted when the producers' standing biomass is smaller than the consumers' — the sea, where phytoplankton biomass is less than fish biomass; the energy pyramid is always upright
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The invertible pyramid a student carries is the biomass one, and grassland is the ecosystem the chapter draws its pyramid figures for, so the remembered inversion is placed in the familiar ecosystem. In grassland the standing biomass of the grasses far exceeds that of the herbivores, so that pyramid is upright.
- **Why:** This question requires the stated fact about which pyramid in which ecosystem is inverted, demonstrated by "they are generally inverted for:" followed by four pyramid-and-ecosystem combinations.
- **Note:** The pattern classifier called this statement_options, but the options are noun phrases naming a pyramid and an ecosystem, not statements to be judged, so the shape recorded is mcq. The trap is the right phenomenon placed in the wrong ecosystem; half_right was ruled out because the option is one claim rather than two separately graded answers, and nearby_fact because grassland is not merely printed beside the sea but is the wrong location for an inversion the student has otherwise got right.
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
- **Concept:** GIFT moves a donor's ovum into the fallopian tube of a woman who cannot produce ova; ZIFT and IUT move embryos, and the stage and the destination are what separate the three
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  "Early embryos with up to 8 blastomeres ... into the fallopian tube" is the chapter's definition of ZIFT, printed in the same paragraph as GIFT, so a reader checking each option for truth finds this one true and stops. It is true, and it is about the technique the stem did not name.
- **Why:** This question requires the printed definition of one assisted reproductive technique held apart from its neighbours, demonstrated by the stem's "Choose the correct statement regarding GIFT" against option 3, which prints the ZIFT definition instead.
- **Note:** Option 4 as stored prints "envoronment" for "environment"; the key is unaffected.
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
- **Concept:** What the endomembrane system includes and excludes, and the double membrane and circular DNA that make mitochondria and plastids semi-autonomous
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Statement A names Golgi complex and endoplasmic reticulum, two genuine members of the endomembrane system, and that surrounding truth carries mitochondria along with them; passing A and adding the secure B and C gives exactly A, B and C.
- **Why:** This question requires each printed statement to be checked against the lines NCERT states about the organelles, demonstrated by 'The endomembrane system includes Golgi complex, endoplasmic reticulum and mitochondria' standing or falling on the membership list alone.
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
- **Concept:** Which membrane facts hold for eukaryotic cells, as against mesosomes and glycocalyx, which NCERT prints only for prokaryotes
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  C and E are NCERT's own lines with their prokaryotic setting stripped off -- the infolded plasma membrane that forms a mesosome, and the glycocalyx lying outermost -- so a student matching each statement to remembered text certifies both, keeps the bilayer statement B that is beyond doubt, and B, C and E is the set left.
- **Why:** This question requires each statement to be checked against what NCERT states for the eukaryotic membrane, demonstrated by the stem's 'regarding cell membrane in eukaryotic cell' set against 'Extensions of the plasma membrane into the cell form mesosomes'.
- **Note:** All three wrong options carry C and E together, so the whole discrimination rests on the stem's 'in eukaryotic cell'; the options differ only in which true statement rides along, which is what fixed the trap option by asking which rejections the printed statements themselves support. Statement A's figure agrees with the composition NCERT prints for the human erythrocyte membrane, so the key is tagged as printed with no doubt recorded.
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
- **Concept:** Each muscular-skeletal disorder has one defining sign: tetany a calcium deficit, arthritis joint inflammation, myasthenia gravis an autoimmune attack on the neuromuscular junction, muscular dystrophy progressive muscle degeneration
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Rheumatoid arthritis is the autoimmune disease NCERT names, so a student carrying 'arthritis = autoimmune' takes B-II and, with A-III and D-IV already secure, is left with C-I. Item (II) runs on to say 'affecting neuromuscular junction', which fixes it to myasthenia gravis and to no arthritis.
- **Why:** This question requires each named disorder to be set against the defining line NCERT prints for it, demonstrated by List II reproducing those lines as the items to be paired -- 'Wild contraction in muscle due to low $\mathrm{Ca^{++}}$ in body fluid' and 'Inflammation of joints' -- so every row is settled by a stated fact and no criterion is printed to apply.
- **Note:** List I's fourth label prints as 'D' without the full stop that A-C carry; cosmetic, and it changes no field. The key checks out row by row against the printed List II lines. On the trap axis I ran the section 5.1 swap test before settling: putting an unlike disorder in place of arthritis kills neither the 'autoimmune' pull nor the option's two correct rows, so position is not doing the work (`nearby_fact`) and the names do not resemble each other (`look_alike_term`); what makes option 4 reachable is a four-part code right in two rows and wrong in two, with item (II) accepted on its first half only.
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
- **Concept:** Order of appearance in human evolution: Ramapithecus, then Homo habilis, Homo erectus, Neanderthal man, Homo sapiens
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The printed phrase that Homo habilis was the first human-like being gets read as first in the whole sequence, so the chain is started with habilis and Ramapithecus is dropped in further along. Ramapithecus is dated about 15 million years back, well before habilis at about 2 million.
- **Why:** This question requires the taught order of appearance of human ancestors, demonstrated by the stem's "the evolution of individual species in the sequence of their appearance" and by each option being a five-name chain joined by arrows.
- **Note:** The pattern classifier returned arrange_in_order; the current qtype list carries no ordering shape, so the printed shape is recorded as mcq and the ordering is carried by asks: order. The trap is a correctly known species placed at the wrong point in time; reversed was ruled out because no option prints the inverted chain and that label excludes a single displacement inside a longer order.
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
- **Concept:** Flightlessness alone does not single out one bird in the Aves example list; the penguin is the one whose forelimbs are flattened into swimming paddles, while the ostrich's are reduced for running
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The ostrich is the bird carried in memory as the textbook's flightless bird, and it is printed in the same Aves example line as the penguin, so the first clause of the stem lands on Struthio. Its forelimbs are reduced for running, not flattened into paddles for swimming.
- **Why:** This question requires the stated fact about which named bird has forelimbs modified into paddles, demonstrated by the stem's 'forelimbs modified as paddle-like structures suited for swimming' with four coordinate genus names as options and no criterion printed to apply.
- **Note:** All four options are genus names from the same taught Aves example set, so the discrimination runs on the second clause of the stem alone. The nearby_fact / look_alike_term test applied was the swap test: Struthio and Aptenodytes do not resemble each other as words, and replacing them with two unlike names leaves the pull intact, because what carries the student is the ostrich being the other flightless bird printed in the same example list. E1's plain_mcq agrees with the printed shape.
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
- **Concept:** Who gains and who loses in each pairwise interaction: both benefit in mutualism, one benefits and one is harmed in parasitism, one benefits and one is unaffected in commensalism, one is harmed and one unaffected in amensalism
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A is correctly struck out because commensalism leaves the other species unaffected rather than harmed, and D then repeats A's wording word for word, so the false mark is carried across to it; what is left, B and E, is true but one statement short.
- **Why:** This question requires the benefit-and-harm row NCERT prints for each named interaction, demonstrated by 'In amensalism, one species is harmed and the other is unaffected' being graded on that row alone.
<!--/ecat-->

