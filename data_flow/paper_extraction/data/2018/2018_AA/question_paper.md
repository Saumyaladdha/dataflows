# NEET (UG) 2018 · Code AA

180 questions · source `NEET_Papers/2018/NEET_2018_Code_AA_official.pdf` · every image a CDN link (0 without one) · 40 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Thermodynamics

The volume ($V$) of a monatomic gas varies with its temperature ($T$), as shown in the graph. The ratio of work done by the gas, to the heat absorbed by it, when it undergoes a change from state A to state B, is

![printed figure: V-T graph: straight line through origin O with process A to B marked by an arrow](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q001_19ec6e88_27102026.svg?v=19ec6e88f97d)

*V-T graph: straight line through origin O with process A to B marked by an arrow*

![drawn: V-T graph: straight line through origin O with process A to B marked by an arrow](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q001_question_825ed9e5_27102026.svg?v=825ed9e5e55b)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\frac{1}{3}$
- (2) $\frac{2}{3}$
- **(3)** $\frac{2}{5}$
- (4) $\frac{2}{7}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Given process is isobaric
2. $dQ = n\,C_p\,dT$
3. $dQ = n\left(\frac{5}{2}R\right)dT$
4. $dW = P\,dV = n\,RdT$
5. Required ratio $= \frac{dW}{dQ} = \frac{nRdT}{n\left(\frac{5}{2}R\right)dT} = \frac{2}{5}$

**Solved independently** (answer withheld)

1. The graph is a straight line through the origin, so $V \propto T$, which means $P$ is constant (isobaric process).
2. Work done at constant pressure: $W = P\,\Delta V = nR\,\Delta T$.
3. Heat absorbed at constant pressure: $Q = nC_p\,\Delta T = \frac{5}{2} nR\,\Delta T$ for a monatomic gas.
4. $\frac{W}{Q} = \frac{nR\,\Delta T}{\frac{5}{2} nR\,\Delta T} = \frac{2}{5}$, which is option $3$.

**Subtopic:** Isobaric Process · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q001_a38fb07f_27102026.png?v=a38fb07fa097)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q001_de7d038b_27102026.png?v=de7d038b62a7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A straight V-T line through the origin is a constant-pressure process, where $W = nR\Delta T$ and the heat supplied is $nC_p\Delta T$ with $C_p = \frac{5}{2}R$ for a monatomic gas
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Putting the internal energy change in place of the heat absorbed -- $C_v = \frac{3}{2}R$ where the process needs $C_p = \frac{5}{2}R$ -- turns the ratio into $\frac{nR\Delta T}{\frac{3}{2}nR\Delta T} = \frac{2}{3}$.
- **Why:** This question requires a ratio computed for the process the graph shows, demonstrated by the stem's 'monatomic gas' with V plotted as a straight line through the origin against T.
- **Note:** The figure supplies one premise -- that V is proportional to T, hence constant pressure -- but the answer is produced by the heat-capacity arithmetic, so asks is calculate rather than read_diagram.
<!--/ecat-->

## Q2

Physics · Waves

The fundamental frequency in an open organ pipe is equal to the third harmonic of a closed organ pipe. If the length of the closed organ pipe is $20\,\mathrm{cm}$, the length of the open organ pipe is

- (1) $12.5\,\mathrm{cm}$
- (2) $8\,\mathrm{cm}$
- **(3)** $13.2\,\mathrm{cm}$
- (4) $16\,\mathrm{cm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For closed organ pipe, third harmonic
2. $= \frac{3v}{4l}$
3. For open organ pipe, fundamental frequency
4. $= \frac{v}{2l'}$
5. Given,
6. $\frac{3v}{4l} = \frac{v}{2l'}$
7. $\Rightarrow l' = \frac{4l}{3 \times 2} = \frac{2l}{3}$
8. $= \frac{2 \times 20}{3} = 13.33\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Fundamental of the open pipe: $f_o = \frac{v}{2L'}$.
2. Third harmonic of the closed pipe: $f_3 = \frac{3v}{4L}$.
3. Set them equal: $\frac{v}{2L'} = \frac{3v}{4L} \Rightarrow L' = \frac{4L}{6} = \frac{2L}{3}$.
4. $L' = \frac{2 \times 20\,\mathrm{cm}}{3} = 13.33\,\mathrm{cm}$, closest to option $3$ ($13.2\,\mathrm{cm}$).

**Subtopic:** Organ Pipe · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q002_3084d1af_27102026.png?v=3084d1afa72c)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q002_67a3e50c_27102026.png?v=67a3e50ca7e4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A closed pipe sounds only odd harmonics, so its third harmonic is $3v/4L$ -- three times its fundamental -- and not the third frequency up the ladder
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Counting 'third' along the frequencies a closed pipe can actually sound -- $v/4L$, $3v/4L$, $5v/4L$ -- lands on $5v/4L$, and equating that with $v/2L_{open}$ gives $L_{open} = 2(20)/5 = 8$ cm instead of $2(20)/3 = 13.3$ cm.
- **Why:** This question requires a length computed by equating two pipe frequencies, demonstrated by 'the fundamental frequency in an open organ pipe is equal to the third harmonic of a closed organ pipe' with the closed length printed as 20 cm.
- **Note:** Two-thirds of 20 cm is 13.3 cm and option 3 prints 13.2 cm; the key is (3) and the tag follows it, with the rounding recorded here rather than treated as a second answer.
<!--/ecat-->

## Q3

Physics · Kinetic Theory of Gases

At what temperature will the rms speed of oxygen molecules become just sufficient for escaping from the Earth's atmosphere? (Given : Mass of oxygen molecule $(m) = 2.76 \times 10^{-26}\,\mathrm{kg}$ Boltzmann's constant $k_B = 1.38 \times 10^{-23}\,\mathrm{JK^{-1}}$)

- (1) $5.016 \times 10^{4}\,\mathrm{K}$
- **(2)** $8.360 \times 10^{4}\,\mathrm{K}$
- (3) $2.508 \times 10^{4}\,\mathrm{K}$
- (4) $1.254 \times 10^{4}\,\mathrm{K}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $V_{\mathrm{escape}} = 11200\,\mathrm{m/s}$
2. Say at temperature $T$ it attains $V_{\mathrm{escape}}$
3. So, $\sqrt{\frac{3k_B T}{m_{\mathrm{O_2}}}} = 11200\,\mathrm{m/s}$
4. On solving,
5. $T = 8.360 \times 10^{4}\,\mathrm{K}$

**Solved independently** (answer withheld)

1. For the molecules to escape, $v_{rms} = v_e = 11.2\,\mathrm{km\,s^{-1}} = 1.12 \times 10^{4}\,\mathrm{m\,s^{-1}}$.
2. $v_{rms} = \sqrt{\frac{3k_BT}{m}} \Rightarrow T = \frac{m v_e^2}{3k_B}$.
3. $v_e^2 = (1.12 \times 10^{4})^2 = 1.2544 \times 10^{8}\,\mathrm{m^2\,s^{-2}}$.
4. $m v_e^2 = 2.76 \times 10^{-26} \times 1.2544 \times 10^{8} = 3.462 \times 10^{-18}\,\mathrm{J}$.
5. $3k_B = 3 \times 1.38 \times 10^{-23} = 4.14 \times 10^{-23}\,\mathrm{J\,K^{-1}}$.
6. $T = \frac{3.462 \times 10^{-18}}{4.14 \times 10^{-23}} \approx 8.36 \times 10^{4}\,\mathrm{K}$, which is option $2$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q003_d3373f37_27102026.png?v=d3373f370c90)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q003_38d2792a_27102026.png?v=38d2792a310e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Escape needs $v_{rms}$ to reach the escape speed of 11.2 km/s, and $\frac{1}{2}mv_{rms}^2 = \frac{3}{2}k_BT$ fixes the temperature at $mv^2/3k_B$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Oxygen is diatomic, so a student who reaches for five degrees of freedom writes $\frac{1}{2}mv^2 = \frac{5}{2}k_BT$ and gets $T = mv^2/5k_B = 5.016\times10^4$ K; the rms speed is set by translation alone, which is $\frac{3}{2}k_BT$.
- **Why:** This question requires a temperature computed from an energy balance, demonstrated by the stem supplying the molecular mass and Boltzmann's constant and asking at what temperature the rms speed suffices 'for escaping from the Earth's atmosphere'.
- **Note:** The escape speed of 11.2 km/s is not printed in the stem; the student has to supply it, which every route above assumes.
<!--/ecat-->

## Q4

Physics · Thermodynamics

The efficiency of an ideal heat engine working between the freezing point and boiling point of water, is

- (1) $6.25\%$
- (2) $20\%$
- **(3)** $26.8\%$
- (4) $12.5\%$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Efficiency of ideal heat engine, $\eta = \left(1 - \frac{T_2}{T_1}\right)$
2. $T_2$ : Sink temperature
3. $T_1$ : Source temperature
4. $\%\eta = \left(1 - \frac{T_2}{T_1}\right) \times 100$
5. $= \left(1 - \frac{273}{373}\right) \times 100$
6. $= \left(\frac{100}{373}\right) \times 100 = 26.8\%$

**Solved independently** (answer withheld)

1. An ideal (Carnot) engine has efficiency $\eta = 1 - \frac{T_c}{T_h}$.
2. Freezing point $T_c = 273\,\text{K}$, boiling point $T_h = 373\,\text{K}$.
3. $\eta = 1 - \frac{273}{373} = \frac{100}{373} \approx 0.268$.
4. $\eta \approx 26.8\%$, which is option $3$.

**Subtopic:** Carnot Engine · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q004_511d0286_27102026.png?v=511d0286ff21)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q004_3f3880a6_27102026.png?v=3f3880a677c4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Carnot efficiency is $1 - T_C/T_H$ with both temperatures in kelvin, so water's freezing and boiling points mean 273 K and 373 K
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The one wrong move this stem invites is putting 0 and 100 degrees Celsius into $1 - T_C/T_H$, which yields 100 per cent, and that is not printed. Each wrong option was then back-solved for the temperature pair it would need: 6.25 per cent needs 273 K against 291 K, 20 per cent needs 273 K against 341 K, 12.5 per cent needs 273 K against 312 K, and no reading of the freezing and boiling points -- Celsius, kelvin, Fahrenheit or Rankine, the last two giving 84.9 and 26.8 per cent -- produces any of those pairs.
- **Why:** This question requires a Carnot efficiency computed from two reservoir temperatures, demonstrated by 'an ideal heat engine working between the freezing point and boiling point of water'.
- **Note:** no_trap is a finding here, not a gap: the Celsius error that this question is usually built to catch gives 100 per cent, which the paper does not print, so the three wrong options are a numerical spread rather than routes.
<!--/ecat-->

## Q5

Physics · Current Electricity

A carbon resistor of $(47 \pm 4.7)\,\mathrm{k\Omega}$ is to be marked with rings of different colours for its identification. The colour code sequence will be

- (1) Yellow – Green – Violet – Gold
- **(2)** Yellow – Violet – Orange – Silver
- (3) Violet – Yellow – Orange – Silver
- (4) Green – Orange – Violet – Gold

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $(47 \pm 4.7)\,\mathrm{k\Omega} = 47 \times 10^{3} \pm 10\%$
2. $\therefore$ Yellow – Violet – Orange – Silver

**Solved independently** (answer withheld)

1. $47\,\mathrm{k\Omega} = 47 \times 10^{3}\,\Omega$.
2. First digit $4 \rightarrow$ Yellow, second digit $7 \rightarrow$ Violet.
3. Multiplier $10^{3} \rightarrow$ Orange.
4. Tolerance $\frac{4.7}{47} \times 100\% = 10\% \rightarrow$ Silver.
5. Sequence Yellow – Violet – Orange – Silver, which is option $2$.

**Subtopic:** Colour Code of Carbon Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q005_7a565565_27102026.png?v=7a565565127f)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q005_3bdb0925_27102026.png?v=3bdb0925db51)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The carbon-resistor code reads the two digit rings first, then the decimal multiplier, then the tolerance: 47 k-ohm is yellow-violet-orange and a 10 per cent tolerance is silver
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Reading the two digit rings in the wrong direction turns 47 into 74, so violet goes before yellow; the multiplier and the tolerance of this option are both right, and only the direction of the digit pair is inverted.
- **Why:** This question requires an agreed code applied to a printed value, demonstrated by '(47 ± 4.7) k-ohm' and options that are sequences of four rings.
- **Note:** The pattern classifier called this arrange_in_order; the answer is a colour sequence, but the sequence is dictated by the code rather than ranked, so asks is apply_rule and the shape is recorded as mcq.
<!--/ecat-->

## Q6

Physics · Current Electricity

A set of '$n$' equal resistors, of value '$R$' each, are connected in series to a battery of emf '$E$' and internal resistance '$R$'. The current drawn is $I$. Now, the '$n$' resistors are connected in parallel to the same battery. Then the current drawn from battery becomes $10\,I$. The value of '$n$' is

- (1) 20
- (2) 11
- **(3)** 10
- (4) 9

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $I = \frac{E}{nR + R}$ ...(i)
2. $10\,I = \frac{E}{\frac{R}{n} + R}$ ...(ii)
3. Dividing (ii) by (i),
4. $10 = \frac{(n + 1)R}{\left(\frac{1}{n} + 1\right)R}$
5. After solving the equation, $n = 10$

**Solved independently** (answer withheld)

1. In series the external resistance is $nR$, so $I = \frac{E}{nR + R} = \frac{E}{(n+1)R}$.
2. In parallel the external resistance is $\frac{R}{n}$, so $10I = \frac{E}{\frac{R}{n} + R} = \frac{nE}{(n+1)R}$.
3. Dividing: $\frac{10I}{I} = \frac{nE/((n+1)R)}{E/((n+1)R)} = n$.
4. $n = 10$, which is option $3$.

**Subtopic:** Combination of Resistors, Relationship Between EMF, Potential Difference and Current With Internal Resistance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q006_4c49ba90_27102026.png?v=4c49ba90f9d3)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q006_f791c8a6_27102026.png?v=f791c8a60472)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With n equal resistors R and an internal resistance also equal to R, the series current is $E/(n+1)R$ and the parallel current is $nE/(n+1)R$, so the parallel arrangement draws exactly n times as much
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Leaving the internal resistance out of the series total makes the ratio $n^2/(n+1)$ instead of n, and setting that equal to 10 gives 10.9, which rounds onto the printed 11; counting the battery's own R as one more resistor in the chain gets to the same 11 by a different door.
- **Why:** This question requires a number computed from two circuit currents, demonstrated by 'the current drawn from battery becomes 10 I' with the internal resistance printed as R.
<!--/ecat-->

## Q7

Physics · Current Electricity

A battery consists of a variable number 'n' of identical cells (having internal resistance 'r' each) which are connected in series. The terminals of the battery are short-circuited and the current I is measured. Which of the graphs shows the correct relationship between I and n?

- (1) ![printed figure: Graph of current I against number of cells n: a curve rising from the origin and levelling off](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q007_option_1_2ab49792_29102026.svg?v=2ab497920ec3) *Graph of current I against number of cells n: a curve rising from the origin and levelling off* ![drawn: Graph of current I against number of cells n: a curve rising from the origin and levelling off](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q007_option_1_d223e263_27102026.svg?v=d223e2639003)  
*drawn on the booklet's geometry, checked against its figure spec*
- (2) ![printed figure: Graph of current I against number of cells n: a straight line rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q007_option_2_c5684c58_27102026.svg?v=c5684c58da0b) *Graph of current I against number of cells n: a straight line rising from the origin O* ![drawn: Graph of current I against number of cells n: a straight line rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q007_option_2_6628d62c_27102026.svg?v=6628d62c7912)  
*drawn on the booklet's geometry, checked against its figure spec*
- **(3)** ![printed figure: Graph of current I against number of cells n: a horizontal line (I constant)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q007_option_3_af553c4b_27102026.svg?v=af553c4b3520) *Graph of current I against number of cells n: a horizontal line (I constant)* ![drawn: Graph of current I against number of cells n: a horizontal line (I constant)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q007_option_3_094aad38_27102026.svg?v=094aad380f91)  
*drawn on the booklet's geometry, checked against its figure spec*
- (4) ![printed figure: Graph of current I against number of cells n: a curve rising from the origin O, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q007_option_4_f12a9d60_27102026.svg?v=f12a9d60fc29) *Graph of current I against number of cells n: a curve rising from the origin O, concave upward* ![drawn: Graph of current I against number of cells n: a curve rising from the origin O, concave upward](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q007_option_4_1f7570db_27102026.svg?v=1f7570dbce42)  
*drawn on the booklet's geometry, checked against its figure spec*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $I = \frac{n\varepsilon}{nr} = \frac{\varepsilon}{r}$
2. So, $I$ is independent of $n$ and $I$ is constant.
3. $\therefore$

![printed figure: Graph of I against n: a horizontal line, I independent of n](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q007_sol_1_a71c69a4_29102026.svg?v=a71c69a488c5)

*Graph of I against n: a horizontal line, I independent of n*

![drawn: Graph of I against n: a horizontal line, I independent of n](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q007_solution_1_dde14bd7_27102026.svg?v=dde14bd78f42)  
*drawn on the booklet's geometry, checked against its figure spec*


**Solved independently** (answer withheld)

1. For $n$ identical cells in series, total emf $= nE$ and total internal resistance $= nr$.
2. Short-circuiting the terminals makes the external resistance $R = 0$.
3. $I = \frac{nE}{nr + 0} = \frac{E}{r}$, which does not depend on $n$.
4. A constant $I$ against $n$ is a horizontal line, which is the graph in option $3$.

**Subtopic:** Combination of Cells · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q007_0c6d2784_27102026.png?v=0c6d278427b9)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q007_2102d0ba_27102026.png?v=2102d0badd5e)

---

<!--ecat-->
#### Categories

- **Type:** **New type (proposed)** (`new_type`) — a printed shape none of the above describes
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Short-circuiting n identical cells in series multiplies the emf and the internal resistance by the same n, so the current E/r does not change as n changes
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The four options are graphs and the option content reached this step as four empty strings, so no curve could be compared with any other; the stem and the key were read, but no option is available to carry a route.
- **Why:** This question requires how the short-circuit current responds to the number of cells, demonstrated by 'the terminals of the battery are short-circuited and the current I is measured' with n cells of internal resistance r each.
- **Note:** A reviewer holding the printed graphs should check for the curve that rises with n: nE over nr cancels to E/r, so the correct graph is a horizontal line, and the option worth examining is the one drawn increasing with n, which is what a student gets by scaling the emf with n while leaving the internal resistance at r. The paper itself is intact; only the option images were not supplied here.
<!--/ecat-->

## Q8

Physics · Wave Optics

Unpolarised light is incident from air on a plane surface of a material of refractive index '$\mu$'. At a particular angle of incidence '$i$', it is found that the reflected and refracted rays are perpendicular to each other. Which of the following options is correct for this situation?

- (1) $i=\sin^{-1}\left(\frac{1}{\mu}\right)$
- **(2)** Reflected light is polarised with its electric vector perpendicular to the plane of incidence
- (3) Reflected light is polarised with its electric vector parallel to the plane of incidence
- (4) $i=\tan^{-1}\left(\frac{1}{\mu}\right)$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. When reflected light rays and refracted rays are perpendicular, reflected light is polarised with electric field vector perpendicular to the plane of incidence.

![printed figure: Brewster angle: reflected and refracted rays perpendicular](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q008_sol_1_232d21dc_29102026.svg?v=232d21dcb174)

*Brewster angle: reflected and refracted rays perpendicular*

![drawn: Brewster angle: reflected and refracted rays perpendicular](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q008_solution_1_5c9b4de9_27102026.svg?v=5c9b4de9fff6)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Also, $\tan i = \mu$ (Brewster angle)

**Solved independently** (answer withheld)

1. Reflected and refracted rays are perpendicular, so $i + r = 90^\circ$, i.e. $r = 90^\circ - i$.
2. Snell's law: $\sin i = \mu \sin r = \mu \cos i$, so $\tan i = \mu$, i.e. $i = \tan^{-1}\mu$ (Brewster's angle); options $1$ and $4$ are wrong.
3. At Brewster's angle the component with $\vec{E}$ in the plane of incidence is not reflected, so the reflected light is polarised with $\vec{E}$ perpendicular to the plane of incidence, which is option $2$.

**Subtopic:** Polarization by Reflection and Refraction · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q008_21b20224_27102026.png?v=21b202248f95)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q008_5d740392_27102026.png?v=5d740392cc31)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** When the reflected and refracted rays are perpendicular the angle of incidence is Brewster's angle, tan i = mu, and the reflected light is completely polarised with its electric vector perpendicular to the plane of incidence
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Knowing that reflection at this angle polarises the light but not which way the electric vector lies, a student takes the plane the ray is drawn in -- the plane of incidence -- as the plane the vibrations keep to; the surviving vibrations are the ones at right angles to that plane.
- **Why:** This question requires a known rule applied to a stated situation, demonstrated by 'the reflected and refracted rays are perpendicular to each other' fixing the angle of incidence as the polarising angle.
- **Note:** Two options are formulas and two are statements about polarisation; the stem asks which option is correct rather than instructing the student to judge statements, so the shape is mcq.
<!--/ecat-->

## Q9

Physics · Wave Optics

In Young's double slit experiment the separation $d$ between the slits is $2\,\mathrm{mm}$, the wavelength $\lambda$ of the light used is $5896\,\mathrm{\AA}$ and distance $D$ between the screen and slits is $100\,\mathrm{cm}$. It is found that the angular width of the fringes is $0.20^\circ$. To increase the fringe angular width to $0.21^\circ$ (with same $\lambda$ and $D$) the separation between the slits needs to be changed to

- (1) $2.1\,\mathrm{mm}$
- **(2)** $1.9\,\mathrm{mm}$
- (3) $1.8\,\mathrm{mm}$
- (4) $1.7\,\mathrm{mm}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Angular width $= \frac{\lambda}{d}$
2. $0.20^\circ = \frac{\lambda}{2\,\mathrm{mm}}$ ...(i)
3. $0.21^\circ = \frac{\lambda}{d}$ ...(ii)
4. Dividing we get, $\frac{0.20}{0.21} = \frac{d}{2\,\mathrm{mm}}$
5. $\therefore\ d = 1.9\,\mathrm{mm}$

**Solved independently** (answer withheld)

1. Angular width of fringes in YDSE: $\theta = \frac{\lambda}{d}$, independent of $D$.
2. With $\lambda$ fixed, $\theta d = \text{constant}$, so $\frac{d'}{d} = \frac{\theta}{\theta'} = \frac{0.20^\circ}{0.21^\circ}$.
3. $d' = 2\,\mathrm{mm} \times \frac{0.20}{0.21} \approx 1.905\,\mathrm{mm} \approx 1.9\,\mathrm{mm}$, which is option $2$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q009_b2f2b7a1_27102026.png?v=b2f2b7a1f859)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q009_fe75768f_27102026.png?v=fe75768faf84)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Angular fringe width is lambda over d, so it is inversely proportional to the slit separation and widening the fringes means narrowing d in the same ratio
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Scaling d in step with the angular width -- $d' = 2 \times 21/20 = 2.1$ mm -- treats the two as directly proportional; in $\theta = \lambda/d$ the separation sits in the denominator, so a wider fringe needs a smaller d, 1.9 mm.
- **Why:** This question requires a new slit separation computed from a ratio of angular widths, demonstrated by 'to increase the fringe angular width to 0.21 degrees (with same lambda and D)'.
- **Note:** The printed data are mutually inconsistent: 5896 angstrom with d = 2 mm gives an angular width of about 0.017 degrees, not the 0.20 degrees the stem reports. The question is still answerable, and is answered, by the inverse proportion, which is what the key rests on.
<!--/ecat-->

## Q10

Physics · Ray Optics

An astronomical refracting telescope will have large angular magnification and high angular resolution, when it has an objective lens of

- **(1)** Large focal length and large diameter
- (2) Large focal length and small diameter
- (3) Small focal length and large diameter
- (4) Small focal length and small diameter

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For telescope, angular magnification $= \frac{f_0}{f_E}$
2. So, focal length of objective lens should be large.
3. Angular resolution $= \frac{D}{1.22\lambda}$ should be large.
4. So, objective should have large focal length $(f_0)$ and large diameter $D$.

**Solved independently** (answer withheld)

1. Angular magnification of a refracting telescope is $m = \frac{f_o}{f_e}$, so a large objective focal length $f_o$ gives large magnification.
2. Limit of resolution is $\Delta\theta = \frac{1.22\lambda}{D}$, so resolving power $\frac{1}{\Delta\theta} = \frac{D}{1.22\lambda}$ increases with objective diameter $D$.
3. Large $f_o$ and large $D$ together match option $1$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q010_36072c24_27102026.png?v=36072c244080)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q010_94918b48_27102026.png?v=94918b48119e)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An objective serves two different ends at once: magnification goes with its focal length, $f_o/f_e$, and resolution goes with its diameter, $D/1.22\lambda$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Large focal length is read off the magnification formula correctly, and then a small aperture is added because a narrow opening is remembered as giving the sharper, cleaner image; resolving power rises with the diameter, so a small objective resolves less.
- **Why:** This question requires one rule applied to each of two properties of the same lens, demonstrated by the stem asking for 'large angular magnification and high angular resolution' and every option pairing a focal length with a diameter.
- **Note:** The pattern classifier called this statement_options; each option is a focal length crossed with a diameter and scores nothing if half right, which is the two_part shape.
<!--/ecat-->

## Q11

Physics · Modern Physics

The ratio of kinetic energy to the total energy of an electron in a Bohr orbit of the hydrogen atom, is

- (1) $2 : -1$
- **(2)** $1 : -1$
- (3) $1 : 1$
- (4) $1 : -2$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{KE} = -(\text{total energy})$
2. So, Kinetic energy : total energy $= 1 : -1$

**Solved independently** (answer withheld)

1. Coulomb force supplies the centripetal force: $\frac{mv^2}{r} = \frac{ke^2}{r^2}$, so $K = \frac{1}{2}mv^2 = \frac{ke^2}{2r}$.
2. Potential energy: $U = -\frac{ke^2}{r} = -2K$.
3. Total energy: $E = K + U = -\frac{ke^2}{2r} = -K$.
4. $K : E = K : (-K) = 1 : -1$, which is option $2$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 4)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q011_3ffafdc5_27102026.png?v=3ffafdc53f3a)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q011_96aa5387_27102026.png?v=96aa5387254f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a Bohr orbit the kinetic energy equals the magnitude of the total energy and half the magnitude of the potential energy, so KE : E = 1 : -1
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  1 : -2 is a true Bohr ratio -- it is kinetic energy to POTENTIAL energy, 13.6 eV against -27.2 eV -- so a student who remembers the factor of two attached to the kinetic energy answers with the pair the stem did not ask about.
- **Why:** This question requires a ratio obtained from the Bohr energy relations, demonstrated by 'the ratio of kinetic energy to the total energy' and options that keep the sign.
<!--/ecat-->

## Q12

Physics · Modern Physics

An electron of mass $m$ with an initial velocity $\vec{V} = V_0\hat{i}$ $(V_0 > 0)$ enters an electric field $\vec{E} = -E_0\hat{i}$ $(E_0 = \text{constant} > 0)$ at $t = 0$. If $\lambda_0$ is its de-Broglie wavelength initially, then its de-Broglie wavelength at time $t$ is

- (1) $\lambda_0 t$
- (2) $\lambda_0\left(1+\dfrac{eE_0}{mV_0}t\right)$
- **(3)** $\dfrac{\lambda_0}{\left(1+\dfrac{eE_0}{mV_0}t\right)}$
- (4) $\lambda_0$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Initial de-Broglie wavelength
2. $\lambda_0 = \frac{h}{mV_0}$ $\quad ...(i)$

![printed figure: Electron moving with velocity V0 in field E0 pointing left; force F on it points left](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q012_sol_1_933ad969_29102026.svg?v=933ad969be33)

*Electron moving with velocity V0 in field E0 pointing left; force F on it points left*

![drawn: Electron moving with velocity V0 in field E0 pointing left; force F on it points left](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q012_solution_1_4da24b6d_27102026.svg?v=4da24b6dcd66)  
*drawn on the booklet's geometry, checked against its figure spec*

3. Acceleration of electron
4. $a = \frac{eE_0}{m}$
5. Velocity after time 't'
6. $V = \left(V_0 + \frac{eE_0}{m}t\right)$
7. So, $\lambda = \frac{h}{mV} = \frac{h}{m\left(V_0 + \frac{eE_0}{m}t\right)}$
8. $= \frac{h}{mV_0\left[1 + \frac{eE_0}{mV_0}t\right]} = \frac{\lambda_0}{\left[1 + \frac{eE_0}{mV_0}t\right]}$ $\quad ...(ii)$
9. Divide (ii) by (i),
10. $\lambda = \frac{\lambda_0}{\left[1 + \frac{eE_0}{mV_0}t\right]}$

**Solved independently** (answer withheld)

1. Force on the electron: $\vec{F} = (-e)\vec{E} = (-e)(-E_0\hat{i}) = eE_0\hat{i}$, along its velocity.
2. Acceleration: $a = \frac{eE_0}{m}$ along $+\hat{i}$.
3. Velocity at time $t$: $v = V_0 + \frac{eE_0}{m}t = V_0\left(1 + \frac{eE_0}{mV_0}t\right)$.
4. De-Broglie wavelength: $\lambda = \frac{h}{mv} = \frac{h}{mV_0\left(1 + \frac{eE_0}{mV_0}t\right)}$.
5. Since $\lambda_0 = \frac{h}{mV_0}$, $\lambda = \frac{\lambda_0}{1 + \frac{eE_0}{mV_0}t}$, which is option $3$.

**Subtopic:** de Broglie Wavelength of an Accelerated Charged Particle · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q012_4466ee8f_27102026.png?v=4466ee8f6c2a)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q012_bf7fba0a_27102026.png?v=bf7fba0a5f9d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The force on the electron is along its motion, so the momentum grows linearly in time and the de Broglie wavelength h/mv falls by the same factor the speed rises
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The speed is worked out correctly as $V_0(1 + eE_0t/mV_0)$, and then the factor is placed in the numerator of the wavelength; in $\lambda = h/mv$ the speed is in the denominator, so the same factor must divide $\lambda_0$.
- **Why:** This question requires an expression derived from the force and the de Broglie relation, demonstrated by the stem giving $\vec{E} = -E_0\hat{i}$ against $\vec{V} = V_0\hat{i}$ and asking for the wavelength 'at time t'.
<!--/ecat-->

## Q13

Physics · Modern Physics

For a radioactive material, half-life is $10\,\text{minutes}$. If initially there are $600$ number of nuclei, the time taken (in minutes) for the disintegration of $450$ nuclei is

- (1) 30
- (2) 10
- **(3)** 20
- (4) 15

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Number of nuclei remaining $= 600 - 450 = 150$
2. $\frac{N}{N_0} = \left(\frac{1}{2}\right)^{n}$
3. $\frac{150}{600} = \left(\frac{1}{2}\right)^{\frac{t}{t_{1/2}}}$
4. $\left(\frac{1}{2}\right)^{2} = \left(\frac{1}{2}\right)^{\frac{t}{t_{1/2}}}$
5. $t = 2t_{1/2} = 2 \times 10$
6. $= 20\,\text{minute}$

**Solved independently** (answer withheld)

1. Nuclei remaining: $N = 600 - 450 = 150$.
2. $\frac{N}{N_0} = \frac{150}{600} = \frac{1}{4} = \left(\frac{1}{2}\right)^2$, so $n = 2$ half-lives.
3. $t = n\,T_{1/2} = 2 \times 10\,\text{min} = 20\,\text{min}$, which is option $3$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q013_4914db58_27102026.png?v=4914db58eac3)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q013_fb87672a_27102026.png?v=fb87672a60bc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Radioactive decay goes by halves, so the time is set by the fraction REMAINING: 150 nuclei left out of 600 is one quarter, which is two half-lives
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Treating the decay as a steady rate -- 300 nuclei gone in the first 10 minutes, so 30 a minute -- makes 450 take 15 minutes; decay slows as nuclei run out, and the second 10 minutes removes only 150 more.
- **Why:** This question requires a time computed from the fraction of the sample left, demonstrated by 'initially there are 600 number of nuclei' with 'the disintegration of 450 nuclei' asked about.
<!--/ecat-->

## Q14

Physics · Modern Physics

When the light of frequency $2\nu_0$ (where $\nu_0$ is threshold frequency), is incident on a metal plate, the maximum velocity of electrons emitted is $v_1$. When the frequency of the incident radiation is increased to $5\nu_0$, the maximum velocity of electrons emitted from the same plate is $v_2$. The ratio of $v_1$ to $v_2$ is

- (1) $4 : 1$
- (2) $1 : 4$
- **(3)** $1 : 2$
- (4) $2 : 1$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $E = W_0 + \frac{1}{2}mv^2$
2. $h(2\nu_0) = h\nu_0 + \frac{1}{2}mv_1^2$
3. $h\nu_0 = \frac{1}{2}mv_1^2$ ...(i)
4. $h(5\nu_0) = h\nu_0 + \frac{1}{2}mv_2^2$
5. $4h\nu_0 = \frac{1}{2}mv_2^2$ ...(ii)
6. Divide (i) by (ii),
7. $\frac{1}{4} = \frac{v_1^2}{v_2^2}$
8. $\frac{v_1}{v_2} = \frac{1}{2}$

**Solved independently** (answer withheld)

1. Einstein's photoelectric equation: $\frac{1}{2}mv_{max}^2 = h\nu - h\nu_0$.
2. At $2\nu_0$: $\frac{1}{2}mv_1^2 = 2h\nu_0 - h\nu_0 = h\nu_0$.
3. At $5\nu_0$: $\frac{1}{2}mv_2^2 = 5h\nu_0 - h\nu_0 = 4h\nu_0$.
4. Dividing: $\frac{v_1^2}{v_2^2} = \frac{1}{4}$.
5. $\frac{v_1}{v_2} = \frac{1}{2}$, i.e. $1 : 2$, which is option $3$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q014_27efe430_27102026.png?v=27efe430d4f6)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q014_9b82adcc_27102026.png?v=9b82adcca6f8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** The photoelectric equation gives the maximum kinetic energy as $h(\nu - \nu_0)$, so the energies here stand as 1 to 4 and the speeds, being square roots, as 1 to 2
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  The energies come out right -- $h\nu_0$ against $4h\nu_0$ -- and the square root is then left undone, so the energy ratio 1 : 4 is reported as the speed ratio; speed goes as the square root of kinetic energy, which makes it 1 : 2.
- **Why:** This question requires how many times one quantity changes when another is changed, demonstrated by the frequency moving from $2\nu_0$ to $5\nu_0$ and the answer asked for as 'the ratio of $v_1$ to $v_2$'.
<!--/ecat-->

## Q15

Physics · Semiconductor Electronics

In the circuit shown in the figure, the input voltage $V_i$ is $20\,\mathrm{V}$, $V_{BE} = 0$ and $V_{CE} = 0$. The values of $I_B$, $I_C$ and $\beta$ are given by

![printed figure: Common-emitter transistor: input Vi through base resistor RB (500 kΩ), collector resistor RC (4 kΩ) to 20 V, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q015_8d02cb5e_29102026.svg?v=8d02cb5edb1f)

*Common-emitter transistor: input Vi through base resistor RB (500 kΩ), collector resistor RC (4 kΩ) to 20 V, emitter grounded*

![drawn: Common-emitter transistor: input Vi through base resistor RB (500 kΩ), collector resistor RC (4 kΩ) to 20 V, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q015_question_329a024c_27102026.svg?v=329a024c7989)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $I_B = 20\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 250$
- (2) $I_B = 25\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 200$
- (3) $I_B = 40\,\mu\mathrm{A}$, $I_C = 10\,\mathrm{mA}$, $\beta = 250$
- **(4)** $I_B = 40\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 125$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $V_{BE} = 0$
2. $V_{CE} = 0$
3. $V_{b} = 0$

![printed figure: Common-emitter npn transistor: V_i through R_B = 500 kOhm to the base, R_C = 4 kOhm from 20 V to the collector, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q015_sol_1_2210e85e_29102026.svg?v=2210e85e70f8)

*Common-emitter npn transistor: V_i through R_B = 500 kOhm to the base, R_C = 4 kOhm from 20 V to the collector, emitter grounded*

![drawn: Common-emitter npn transistor: V_i through R_B = 500 kOhm to the base, R_C = 4 kOhm from 20 V to the collector, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q015_solution_1_91cc405a_27102026.svg?v=91cc405a7107)  
*drawn on the booklet's geometry, checked against its figure spec*

4. $I_{C} = \frac{(20 - 0)}{4 \times 10^{3}}$
5. $I_{C} = 5 \times 10^{-3} = 5\,\mathrm{mA}$
6. $V_{i} = V_{BE} + I_{B}R_{B}$
7. $V_{i} = 0 + I_{B}R_{B}$
8. $20 = I_{B} \times 500 \times 10^{3}$
9. $I_{B} = \frac{20}{500 \times 10^{3}} = 40\,\mu\mathrm{A}$
10. $\beta = \frac{I_{C}}{I_{b}} = \frac{25 \times 10^{-3}}{40 \times 10^{-6}} = 125$

**Solved independently** (answer withheld)

1. With $V_{BE} = 0$, the full input voltage drops across $R_B$: $I_B = \frac{V_i}{R_B} = \frac{20\,\mathrm{V}}{500 \times 10^{3}\,\Omega}$.
2. $I_B = 4 \times 10^{-5}\,\mathrm{A} = 40\,\mu\mathrm{A}$.
3. With $V_{CE} = 0$, the full $20\,\mathrm{V}$ supply drops across $R_C$: $I_C = \frac{20\,\mathrm{V}}{4 \times 10^{3}\,\Omega}$.
4. $I_C = 5 \times 10^{-3}\,\mathrm{A} = 5\,\mathrm{mA}$.
5. $\beta = \frac{I_C}{I_B} = \frac{5 \times 10^{-3}}{40 \times 10^{-6}} = 125$, which is option $4$.

**Subtopic:** Transistor as an Amplifier (Common Emitter Configuration): Voltage, Current and Power Gain · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q015_db679d97_27102026.png?v=db679d970b7d)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q015_3310f061_27102026.png?v=3310f061614e)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With $V_{BE} = 0$ the whole input voltage sits across the base resistor and with $V_{CE} = 0$ the whole supply sits across the collector resistor, so $I_B = 20/500\,\mathrm{k}\Omega$, $I_C = 20/4\,\mathrm{k}\Omega$ and $\beta = I_C/I_B$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The base current is worked out correctly as 40 microamperes, and since two options print that value, taking the first one that matches leaves $I_C$ unchecked -- here it reads 10 mA, twice what 20 V across 4 kilo-ohms gives.
- **Why:** This question requires three quantities computed from the circuit, demonstrated by 'the values of $I_B$, $I_C$ and $\beta$ are given by' with $V_i = 20$ V and $V_{BE} = V_{CE} = 0$.
- **Note:** The figure reached this step as a drawn spec carrying both resistor values, 500 kilo-ohms and 4 kilo-ohms, and the 20 V supply, so the arithmetic above could be checked; each option is a triple accepted or rejected whole, which is the two_part shape.
<!--/ecat-->

## Q16

Physics · Semiconductor Electronics

In a p-n junction diode, change in temperature due to heating

- (1) Does not affect resistance of p-n junction
- (2) Affects only forward resistance
- (3) Affects only reverse resistance
- **(4)** Affects the overall V - I characteristics of p-n junction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Due to heating, number of electron-hole pairs will increase, so overall resistance of diode will change.
2. Due to which forward biasing and reversed biasing both are changed.

**Solved independently** (answer withheld)

1. Heating increases thermally generated electron-hole pairs, so minority carrier density rises: reverse saturation current $I_0$ increases (reverse resistance falls), and the forward current at a given $V$ increases (forward resistance falls), so the overall $V$-$I$ characteristic changes, which is option $4$.

**Subtopic:** VI Characteristics of PN Junction Diode · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 5)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q016_fc9dd339_27102026.png?v=fc9dd3395d47)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q016_926361a1_27102026.png?v=926361a16c59)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Heating a junction generates more carriers on both sides of it, so the whole V-I characteristic shifts -- the forward knee falls and the reverse saturation current rises
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The forward branch is the one drawn and discussed, and 'the barrier potential falls as the temperature rises' is a forward-bias statement, so a student who holds that one fact restricts the effect to the forward resistance; the claim is true as far as it goes and fails on the word 'only'.
- **Why:** This question requires a stated fact about what heating does to a junction, demonstrated by three options confining the effect to one branch with 'only' and the fourth extending it to 'the overall V - I characteristics'.
- **Note:** asks is fact_line rather than apply_rule because nothing is applied to a new case: the answer is the textbook statement about how temperature changes the characteristic.
<!--/ecat-->

## Q17

Physics · Semiconductor Electronics

In the combination of the following gates the output Y can be written in terms of inputs A and B as

![printed figure: Logic circuit: A and B feed two AND gates (each with one inverted input) whose outputs go to an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q017_9515fd85_29102026.svg?v=9515fd85a98b)

*Logic circuit: A and B feed two AND gates (each with one inverted input) whose outputs go to an OR gate giving Y*

![drawn: Logic circuit: A and B feed two AND gates (each with one inverted input) whose outputs go to an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q017_question_107ddfd4_27102026.svg?v=107ddfd47327)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\overline{\mathrm{A}\cdot\mathrm{B}}+\mathrm{A}\cdot\mathrm{B}$
- **(2)** $\mathrm{A}\cdot\overline{\mathrm{B}}+\overline{\mathrm{A}}\cdot\mathrm{B}$
- (3) $\overline{\mathrm{A}\cdot\mathrm{B}}$
- (4) $\overline{\mathrm{A}+\mathrm{B}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Two NOT gates feeding two AND gates (A and NOT B, NOT A and B) whose outputs feed an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q017_sol_1_820026f0_27102026.svg?v=820026f0e82a)

*Two NOT gates feeding two AND gates (A and NOT B, NOT A and B) whose outputs feed an OR gate giving Y*

![drawn: Two NOT gates feeding two AND gates (A and NOT B, NOT A and B) whose outputs feed an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q017_solution_1_3b2a199a_27102026.svg?v=3b2a199adc6e)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\mathrm{Y} = (\mathrm{A}\cdot\overline{\mathrm{B}} + \overline{\mathrm{A}}\cdot\mathrm{B})$

**Solved independently** (answer withheld)

1. From the figure, $B$ crosses over $A$'s branch and passes through the upper NOT gate, so the upper AND gate receives $A$ and $\overline{B}$, giving $A\cdot\overline{B}$.
2. $A$ branches down through the lower NOT gate, and $B$ branches down directly, so the lower AND gate gives $\overline{A}\cdot B$.
3. The OR gate combines them: $Y = A\cdot\overline{B} + \overline{A}\cdot B$, which is option $2$.

**Subtopic:** Logic Gates · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q017_003dc57c_27102026.png?v=003dc57ccbac)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q017_5b2abc5e_27102026.png?v=5b2abc5ef266)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Each AND gate in the printed circuit receives one input inverted, so the OR of their outputs is $A\cdot\bar{B} + \bar{A}\cdot B$, the exclusive-OR that is true only when the inputs differ
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Reading the bubbles as sitting on gate outputs rather than on single input lines turns one branch into a NAND, $\overline{A\cdot B}$, and leaves the other as a plain AND, so the OR of the two is written as $\overline{A\cdot B} + A\cdot B$; in the figure each bubble is on an input wire feeding an AND gate.
- **Why:** This question requires the printed circuit to be read and turned into an expression, demonstrated by 'in the combination of the following gates the output Y can be written in terms of inputs A and B as'.
- **Note:** The figure reached this step as a drawn spec with the two inverted input lines, the two AND gates and the final OR, so the circuit could be traced and the key confirmed.
<!--/ecat-->

## Q18

Physics · Electromagnetic Waves

An em wave is propagating in a medium with a velocity $\vec{V} = V\hat{i}$. The instantaneous oscillating electric field of this em wave is along $+y$ axis. Then the direction of oscillating magnetic field of the em wave will be along

- (1) $-y$ direction
- **(2)** $+z$ direction
- (3) $-z$ direction
- (4) $-x$ direction

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\vec{E} \times \vec{B} = \vec{V}$
2. $(E\hat{j}) \times (\vec{B}) = V\hat{i}$
3. So, $\vec{B} = B\hat{k}$
4. Direction of propagation is along $+z$ direction.

**Solved independently** (answer withheld)

1. The direction of propagation of an em wave is along $\vec{E} \times \vec{B}$.
2. Here $\vec{E} \parallel \hat{j}$ and propagation $\parallel \hat{i}$, so $\hat{j} \times \hat{B} = \hat{i}$.
3. Since $\hat{j} \times \hat{k} = \hat{i}$, $\hat{B} = +\hat{k}$, i.e. the $+z$ direction, which is option $2$.

**Subtopic:** Transverse Nature of Electromagnetic Waves · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 6)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q018_fb508381_27102026.png?v=fb5083819bd7)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q018_e65a2af7_27102026.png?v=e65a2af766f1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In an electromagnetic wave E, B and the direction of travel form a right-handed set, so with travel along x and E along +y the magnetic field lies along +z
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Taking the cross product the other way round -- $\vec{B}\times\vec{E}$ in place of $\vec{E}\times\vec{B}$ -- keeps the z axis but flips the sense, giving $-z$; the order that matters is E then B, which points along the direction of propagation.
- **Why:** This question requires a known rule applied to a stated geometry, demonstrated by 'propagating in a medium with a velocity $\vec{V} = V\hat{i}$' and the electric field 'along $+y$ axis'.
<!--/ecat-->

## Q19

Physics · Ray Optics

The refractive index of the material of a prism is $\sqrt{2}$ and the angle of the prism is $30^\circ$. One of the two refracting surfaces of the prism is made a mirror inwards, by silver coating. A beam of monochromatic light entering the prism from the other face will retrace its path (after reflection from the silvered surface) if its angle of incidence on the prism is

- (1) $30^\circ$
- **(2)** $45^\circ$
- (3) $60^\circ$
- (4) Zero

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For retracing its path, light ray should be normally incident on silvered face.

![printed figure: Prism of angle 30 degrees with a silvered face: the ray refracted at M meets the silvered face normally and retraces its path](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q019_sol_1_bd94df5d_29102026.svg?v=bd94df5d9ad4)

*Prism of angle 30 degrees with a silvered face: the ray refracted at M meets the silvered face normally and retraces its path*

![drawn: Prism of angle 30 degrees with a silvered face: the ray refracted at M meets the silvered face normally and retraces its path](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q019_solution_1_7bd60cc2_27102026.svg?v=7bd60cc2dfb5)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Applying Snell's law at M,
3. $\frac{\sin i}{\sin 30^\circ} = \frac{\sqrt{2}}{1}$
4. $\Rightarrow \sin i = \sqrt{2} \times \frac{1}{2}$
5. $\sin i = \frac{1}{\sqrt{2}}$ i.e. $i = 45^\circ$

**Solved independently** (answer withheld)

1. The ray retraces its path only if it strikes the silvered face along the normal, so $r_2 = 0^\circ$.
2. Since $r_1 + r_2 = A$, we get $r_1 = A = 30^\circ$.
3. Snell's law at the first face: $\sin i = \mu \sin r_1 = \sqrt{2} \times \sin 30^\circ = \frac{1}{\sqrt{2}}$.
4. $i = 45^\circ$, which is option $2$.

**Subtopic:** Prism · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q019_3da5741b_27102026.png?v=3da5741b3eef)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q019_6f6f73c7_27102026.png?v=6f6f73c7beaf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ray retraces its path only if it meets the silvered face along that face's normal, which fixes the refraction angle at the entry face equal to the prism angle; Snell's law then gives the angle of incidence
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The retrace condition hands you the refraction angle inside the glass, $r = 30^\circ$, which is also the prism angle already printed in the stem, so the work stops one line before Snell's law is used.
- **Why:** This question requires the retrace condition converted into a refraction angle and then Snell's law at the entry face, demonstrated by "will retrace its path (after reflection from the silvered surface)" with both the prism angle and the refractive index supplied.
<!--/ecat-->

## Q20

Physics · Ray Optics

An object is placed at a distance of $40\,\mathrm{cm}$ from a concave mirror of focal length $15\,\mathrm{cm}$. If the object is displaced through a distance of $20\,\mathrm{cm}$ towards the mirror, the displacement of the image will be

- (1) $30\,\mathrm{cm}$ towards the mirror
- **(2)** $36\,\mathrm{cm}$ away from the mirror
- (3) $30\,\mathrm{cm}$ away from the mirror
- (4) $36\,\mathrm{cm}$ towards the mirror

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Object O on the principal axis 40 cm in front of a concave mirror of focal length 15 cm](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q020_sol_1_36fd7328_27102026.svg?v=36fd7328fd06)

*Object O on the principal axis 40 cm in front of a concave mirror of focal length 15 cm*

![drawn: Object O on the principal axis 40 cm in front of a concave mirror of focal length 15 cm](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q020_solution_1_4d862c77_27102026.svg?v=4d862c772e69)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\frac{1}{f} = \frac{1}{v_1} + \frac{1}{u}$
2. $-\frac{1}{15} = \frac{1}{v_1} - \frac{1}{40}$
3. $\Rightarrow \frac{1}{v_1} = \frac{1}{-15} + \frac{1}{40}$
4. $v_1 = -24\,\mathrm{cm}$
5. When object is displaced by $20\,\mathrm{cm}$ towards mirror.
6. Now,
7. $u_2 = -20$
8. $\frac{1}{f} = \frac{1}{v_2} + \frac{1}{u_2}$
9. $\frac{1}{-15} = \frac{1}{v_2} - \frac{1}{20}$
10. $\frac{1}{v_2} = \frac{1}{20} - \frac{1}{15}$
11. $v_2 = -60\,\mathrm{cm}$
12. So, image shifts away from mirror by $= 60 - 24 = 36\,\mathrm{cm}$.

**Solved independently** (answer withheld)

1. Mirror formula $\frac{1}{v} + \frac{1}{u} = \frac{1}{f}$ with $f = -15\,\mathrm{cm}$.
2. Initially $u = -40\,\mathrm{cm}$: $\frac{1}{v} = -\frac{1}{15} + \frac{1}{40} = -\frac{1}{24}$, so $v_1 = -24\,\mathrm{cm}$.
3. After moving $20\,\mathrm{cm}$ towards the mirror, $u = -20\,\mathrm{cm}$: $\frac{1}{v} = -\frac{1}{15} + \frac{1}{20} = -\frac{1}{60}$, so $v_2 = -60\,\mathrm{cm}$.
4. $|v_2| - |v_1| = 60 - 24 = 36\,\mathrm{cm}$, with the image moving farther from the mirror, which is option $2$.

**Subtopic:** Mirror Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q020_dbec45be_27102026.png?v=dbec45bebfab)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q020_8abfd60f_27102026.png?v=8abfd60f4935)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The mirror equation solved at two object distances gives two image distances, and the image displacement is the difference between them, with its direction read off those two numbers
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The 36 cm is the magnitude the correct calculation gives; the direction is then taken from the object's motion -- the object moved towards the mirror, so the image is said to move towards it.
- **Why:** This question requires the mirror equation solved at two object distances and the two image positions compared, demonstrated by "if the object is displaced through a distance of 20 cm towards the mirror, the displacement of the image will be".
- **Note:** E1 recorded this as statement_options on a count of 15 full-statement options, but the printed options are a number plus a direction ($36\,\mathrm{cm}$ away from the mirror), not statements to be judged, so the shape here is mcq.
<!--/ecat-->

## Q21

Physics · Electromagnetic Induction

The magnetic potential energy stored in a certain inductor is $25\,\mathrm{mJ}$, when the current in the inductor is $60\,\mathrm{mA}$. This inductor is of inductance

- (1) $1.389\,\mathrm{H}$
- (2) $138.88\,\mathrm{H}$
- (3) $0.138\,\mathrm{H}$
- **(4)** $13.89\,\mathrm{H}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Energy stored in inductor
2. $U = \frac{1}{2}LI^{2}$
3. $25 \times 10^{-3} = \frac{1}{2} \times L \times (60 \times 10^{-3})^{2}$
4. $L = \frac{25 \times 2 \times 10^{6} \times 10^{-3}}{3600}$
5. $= \frac{500}{36}$
6. $= 13.89\,\mathrm{H}$

**Solved independently** (answer withheld)

1. Energy stored in an inductor: $U = \frac{1}{2} L I^2$, so $L = \frac{2U}{I^2}$.
2. Substitute $U = 25\,\mathrm{mJ} = 0.025\,\mathrm{J}$ and $I = 60\,\mathrm{mA} = 0.06\,\mathrm{A}$: $L = \frac{2 \times 0.025}{(0.06)^2}$.
3. $L = \frac{0.05}{0.0036} = 13.89\,\mathrm{H}$, which is option $4$.

**Subtopic:** Energy Stored in an Inductor · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 7)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q021_cdfd8170_27102026.png?v=cdfd8170b09b)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q021_a5c93aba_27102026.png?v=a5c93abac6d1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Magnetic energy stored in an inductor is $\tfrac12 LI^2$, so $L = 2U/I^2$ -- and both milli prefixes have to be turned into powers of ten before dividing
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Writing $25\,\mathrm{mJ}$ as $2.5\times10^{-3}\,\mathrm{J}$ instead of $25\times10^{-3}\,\mathrm{J}$ and dividing by the same $I^2 = 3.6\times10^{-3}$ gives $1.389\,\mathrm{H}$ -- the key's own digits with the decimal point one place to the left.
- **Why:** This question requires $\tfrac12 LI^2$ rearranged and the prefixes converted, demonstrated by "the magnetic potential energy stored ... is $25\,\mathrm{mJ}$, when the current in the inductor is $60\,\mathrm{mA}$".
- **Note:** All three wrong options carry the same digits as the key at different powers of ten (1.389 / 138.88 / 0.138 against 13.89), so the whole distractor set is prefix arithmetic and no option is filler.
<!--/ecat-->

## Q22

Physics · Electrostatics

An electron falls from rest through a vertical distance $h$ in a uniform and vertically upward directed electric field $E$. The direction of electric field is now reversed, keeping its magnitude the same. A proton is allowed to fall from rest in it through the same vertical distance $h$. The time of fall of the electron, in comparison to the time of fall of the proton is

- (1) 10 times greater
- (2) 5 times greater
- **(3)** Smaller
- (4) Equal

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $h = \frac{1}{2}\frac{eE}{m}t^{2}$
2. $\therefore\ t = \sqrt{\frac{2hm}{eE}}$
3. $\therefore\ t \propto \sqrt{m}$ as 'e' is same for electron and proton.
4. $\because$ Electron has smaller mass so it will take smaller time.

**Solved independently** (answer withheld)

1. With $\vec E$ upward, the force on the electron $-e\vec E$ points downward, so $a_e = \frac{eE}{m_e}$ (gravity negligible).
2. With $\vec E$ reversed (downward), the force on the proton $+e\vec E$ points downward, so $a_p = \frac{eE}{m_p}$.
3. Falling from rest through $h$: $h = \frac{1}{2} a t^2 \Rightarrow t = \sqrt{\frac{2h}{a}} = \sqrt{\frac{2hm}{eE}}$.
4. $\frac{t_e}{t_p} = \sqrt{\frac{m_e}{m_p}} \ll 1$, so the electron's time of fall is smaller, which is option $3$.

**Subtopic:** Motion of Charged Particle in Uniform Electric Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q022_8d335770_27102026.png?v=8d3357702a5a)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q022_9fc9e5b6_27102026.png?v=9fc9e5b6ef27)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** A charge released from rest in a uniform field has $a = qE/m$, so the time to cover a fixed height goes as $\sqrt{m}$ -- the electron, 1836 times lighter, takes about 43 times less
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The stem says "falls from rest through a vertical distance $h$" and "time of fall", and the free-fall result $t = \sqrt{2h/g}$ carries no mass in it, so the two times come out equal; here the acceleration is $qE/m$, which does carry the mass.
- **Why:** This question requires knowing how the time over a fixed height scales with the particle's mass when the driving force is electric, demonstrated by "the time of fall of the electron, in comparison to the time of fall of the proton is" with options that are comparisons rather than numbers.
<!--/ecat-->

## Q23

Physics · Capacitance

The electrostatic force between the metal plates of an isolated parallel plate capacitor $C$ having a charge $Q$ and area $A$, is

- (1) Proportional to the square root of the distance between the plates
- (2) Linearly proportional to the distance between the plates
- **(3)** Independent of the distance between the plates
- (4) Inversely proportional to the distance between the plates

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For isolated capacitor $Q = \text{Constant}$
2. $F_{\text{plate}} = \frac{Q^{2}}{2A\varepsilon_{0}}$
3. $F$ is Independent of the distance between plates.

**Solved independently** (answer withheld)

1. The capacitor is isolated, so the charge $Q$ on the plates stays constant.
2. Field due to one plate: $E_1 = \frac{\sigma}{2\varepsilon_0} = \frac{Q}{2\varepsilon_0 A}$.
3. Force on the other plate: $F = Q E_1 = \frac{Q^2}{2\varepsilon_0 A}$.
4. $F$ contains no $d$, so it is independent of the distance between the plates, which is option $3$.

**Subtopic:** The Parallel Plate Capacitor · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q023_e1a73e36_27102026.png?v=e1a73e3675b2)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q023_1ad3be91_27102026.png?v=1ad3be91a920)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** One plate sits in the other plate's field $Q/2\varepsilon_0 A$, so at fixed charge the attraction $Q^2/2\varepsilon_0 A$ contains no separation at all
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Holding the voltage fixed and writing $F = QE = QV/d$ puts the separation straight into the denominator, but the quantity held fixed here is the charge, because the stem calls the capacitor isolated.
- **Why:** This question requires knowing how the inter-plate force depends on separation when the charge rather than the voltage is held fixed, demonstrated by "the metal plates of an isolated parallel plate capacitor $C$ having a charge $Q$ and area $A$" with the options stating four dependences on distance.
- **Note:** E1 recorded this as statement_options on a count of 15 full-statement options, but no statement block is printed and each option merely completes the stem's sentence with a dependence on distance, so the shape here is mcq.
<!--/ecat-->

## Q24

Physics · Waves

A tuning fork is used to produce resonance in a glass tube. The length of the air column in this tube can be adjusted by a variable piston. At room temperature of $27^\circ\mathrm{C}$ two successive resonances are produced at $20\,\mathrm{cm}$ and $73\,\mathrm{cm}$ of column length. If the frequency of the tuning fork is $320\,\mathrm{Hz}$, the velocity of sound in air at $27^\circ\mathrm{C}$ is

- (1) $350\,\mathrm{m/s}$
- **(2)** $339\,\mathrm{m/s}$
- (3) $330\,\mathrm{m/s}$
- (4) $300\,\mathrm{m/s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $v = 2(\nu)[L_2 - L_1]$
2. $= 2 \times 320\,[73 - 20] \times 10^{-2}$
3. $= 339.2\,\mathrm{ms^{-1}}$
4. $= 339\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. For a closed pipe, two successive resonance lengths differ by half a wavelength: $l_2 - l_1 = \frac{\lambda}{2}$.
2. $\frac{\lambda}{2} = 73\,\mathrm{cm} - 20\,\mathrm{cm} = 53\,\mathrm{cm}$, so $\lambda = 106\,\mathrm{cm} = 1.06\,\mathrm{m}$.
3. $v = f\lambda = 320\,\mathrm{Hz} \times 1.06\,\mathrm{m} = 339.2\,\mathrm{m/s} \approx 339\,\mathrm{m/s}$, which is option $2$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q024_b312754b_27102026.png?v=b312754b6928)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q024_53fba21a_27102026.png?v=53fba21a0319)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Successive resonance lengths in a tube differ by half a wavelength, so $\lambda = 2(73-20)\,\mathrm{cm}$ and $v = f\lambda$ -- the measurement decides the speed, not a remembered value
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The stem prints "$27^\circ\mathrm{C}$" twice, and the temperature relation $v = 331\sqrt{300/273} \approx 347\,\mathrm{m/s}$ answers "how fast is sound at $27^\circ\mathrm{C}$" rather than "what did this tube measure", landing on the printed $350\,\mathrm{m/s}$.
- **Why:** This question requires the wavelength taken from the gap between successive resonances and then $v = f\lambda$, demonstrated by "two successive resonances are produced at $20\,\mathrm{cm}$ and $73\,\mathrm{cm}$ of column length" with the fork's frequency supplied.
<!--/ecat-->

## Q25

Physics · Oscillations

A pendulum is hung from the roof of a sufficiently high building and is moving freely to and fro like a simple harmonic oscillator. The acceleration of the bob of the pendulum is $20\,\mathrm{m/s^2}$ at a distance of $5\,\mathrm{m}$ from the mean position. The time period of oscillation is

- (1) $2\,\mathrm{s}$
- **(2)** $\pi\,\mathrm{s}$
- (3) $2\pi\,\mathrm{s}$
- (4) $1\,\mathrm{s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $|a| = \omega^{2}y$
2. $\Rightarrow 20 = \omega^{2}(5)$
3. $\Rightarrow \omega = 2\,\mathrm{rad/s}$
4. $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi\,\mathrm{s}$

**Solved independently** (answer withheld)

1. In SHM the magnitude of acceleration is $|a| = \omega^2 x$.
2. $\omega^2 = \frac{a}{x} = \frac{20\,\mathrm{m/s^2}}{5\,\mathrm{m}} = 4\,\mathrm{s^{-2}}$.
3. $\omega = 2\,\mathrm{rad/s}$.
4. $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi\,\mathrm{s}$, which is option $2$.

**Subtopic:** Calculate Time Period of SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 7)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q025_dd4dc6cf_27102026.png?v=dd4dc6cf5c31)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q025_a161b64e_27102026.png?v=a161b64e0194)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In simple harmonic motion the acceleration is $\omega^2x$, so the ratio of acceleration to displacement gives $\omega^2$ and the period follows from $T = 2\pi/\omega$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $\omega^2 = a/x = 20/5 = 4$ gives $\omega = 2$, and 2 is printed as an option in seconds, so the angular frequency gets handed in as the period; the period still has to be worked out, $T = 2\pi/2 = \pi$ s.
- **Why:** This question requires a period computed from the stem's two numbers, demonstrated by 'the acceleration of the bob is 20 m/s^2 at a distance of 5 m from the mean position'.
<!--/ecat-->

## Q26

Physics · Magnetic Effect of Electric Current

A metallic rod of mass per unit length $0.5\,\mathrm{kg\,m^{-1}}$ is lying horizontally on a smooth inclined plane which makes an angle of $30^\circ$ with the horizontal. The rod is not allowed to slide down by flowing a current through it when a magnetic field of induction $0.25\,\mathrm{T}$ is acting on it in the vertical direction. The current flowing in the rod to keep it stationary is

- (1) $14.76\,\mathrm{A}$
- (2) $5.98\,\mathrm{A}$
- (3) $7.14\,\mathrm{A}$
- **(4)** $11.32\,\mathrm{A}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For equilibrium,

![printed figure: Rod on a 30 degree incline: vertical B, horizontal force IlB, components IlB cos 30 up the slope and mg sin 30 down the slope](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q026_sol_1_2509ffc4_27102026.svg?v=2509ffc48bc9)

*Rod on a 30 degree incline: vertical B, horizontal force IlB, components IlB cos 30 up the slope and mg sin 30 down the slope*

![drawn: Rod on a 30 degree incline: vertical B, horizontal force IlB, components IlB cos 30 up the slope and mg sin 30 down the slope](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q026_solution_1_fbe48d6f_27102026.svg?v=fbe48d6f2704)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $mg\sin 30^\circ = I\ell B\cos 30^\circ$
3. $I = \frac{mg}{\ell B}\tan 30^\circ$
4. $= \frac{0.5\times 9.8}{0.25\times\sqrt{3}} = 11.32\,\mathrm{A}$

**Solved independently** (answer withheld)

1. Current flows horizontally along the rod and $\vec B$ is vertical, so the force $F = BIl$ on the rod is horizontal, perpendicular to the rod.
2. Along the incline, the component $BIl\cos 30^\circ$ must balance $mg\sin 30^\circ$.
3. $I = \frac{(m/l)\,g\tan 30^\circ}{B}$.
4. $I = \frac{0.5 \times 9.8 \times 0.5774}{0.25} = \frac{2.829}{0.25} \approx 11.32\,\mathrm{A}$, which is option $4$.

**Subtopic:** Magnetic Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q026_b5f23543_27102026.png?v=b5f235438681)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q026_41e2542d_27102026.png?v=41e2542dc957)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A vertical field puts a horizontal force $BIL$ on the horizontal rod, so balance along the smooth incline needs $BIL\cos\theta = mg\sin\theta$, giving $I = (m/L)g\tan\theta/B$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The two mistakes this setup invites were both worked through and neither is printed: taking the field perpendicular to the incline instead of vertical gives $I = (m/L)g\sin\theta/B = 9.8$ A, and balancing the weight itself rather than its component along the slope gives 17 A. Each wrong option was then back-solved for the incline angle it would need, and none of the three corresponds to the printed 30 degrees.
- **Why:** This question requires a current computed from a force balance on an incline, demonstrated by 'a magnetic field of induction 0.25 T is acting on it in the vertical direction' with the slope at 30 degrees.
- **Note:** Three fillers is unusual, so the enumeration was done twice: the values the printed data can produce are 9.8 A, 11.32 A and 17 A for the sine, tangent and cosine readings of the geometry, and only 11.32 A is on the page. The no_trap here is a finding about the option set, not a gap in the search.
<!--/ecat-->

## Q27

Physics · Magnetic Effect of Electric Current

A thin diamagnetic rod is placed vertically between the poles of an electromagnet. When the current in the electromagnet is switched on, then the diamagnetic rod is pushed up, out of the horizontal magnetic field. Hence the rod gains gravitational potential energy. The work required to do this comes from

- (1) The lattice structure of the material of the rod
- (2) The magnetic field
- **(3)** The current source
- (4) The induced electric field due to the changing magnetic field

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Energy of current source will be converted into potential energy of the rod.

**Solved independently** (answer withheld)

1. Switching on the current builds up the magnetic field, and the diamagnetic rod is repelled out of it, gaining gravitational potential energy $\Delta U = mgh$.
2. A magnetic field only stores and transfers energy; the energy it holds, and any work done through it, is supplied by the source that drives the current in the electromagnet, so the work comes from the current source, option $3$.

**Subtopic:** Diamagnetism · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 8)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q027_1d9fa184_27102026.png?v=1d9fa18469e1)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q027_533c7739_27102026.png?v=533c7739b040)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** A diamagnetic rod is pushed out of a field, and the energy for that comes from the source maintaining the current, because moving the rod changes the flux and the source has to work against the induced emf
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The magnetic field is what pushes the rod, and naming the pusher answers a different question from naming the supplier; the field is held up by the electromagnet's current, so the energy is drawn from whatever keeps that current flowing.
- **Why:** This question requires the causal account of where the energy comes from, demonstrated by 'the rod gains gravitational potential energy. The work required to do this comes from'.
- **Note:** asks is reason_line because the answer is a cause rather than a quantity or a rule applied to a case; it is the only question in the group of that kind.
<!--/ecat-->

## Q28

Physics · Alternating Current

An inductor $20\,\mathrm{mH}$, a capacitor $100\,\mu\mathrm{F}$ and a resistor $50\,\Omega$ are connected in series across a source of emf, $V = 10 \sin 314\,t$. The power loss in the circuit is

- (1) $2.74\,\mathrm{W}$
- (2) $0.43\,\mathrm{W}$
- **(3)** $0.79\,\mathrm{W}$
- (4) $1.13\,\mathrm{W}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $P_{av} = \left(\frac{V_{RMS}}{Z}\right)^{2} R$
2. $Z = \sqrt{R^{2} + \left(\omega L - \frac{1}{\omega C}\right)^{2}} = 56\,\Omega$
3. $\therefore\ P_{av} = \left(\frac{10}{\left(\sqrt{2}\right)56}\right)^{2} \times 50 = 0.79\,\mathrm{W}$

**Solved independently** (answer withheld)

1. $X_L = \omega L = 314 \times 0.02 = 6.28\,\Omega$.
2. $X_C = \frac{1}{\omega C} = \frac{1}{314 \times 100\times10^{-6}} = 31.85\,\Omega$.
3. $X_C - X_L = 31.85 - 6.28 = 25.57\,\Omega$.
4. $Z^2 = R^2 + (X_C - X_L)^2 = 2500 + 653.8 = 3153.8\,\Omega^2$.
5. $V_{rms}^2 = \left(\frac{10}{\sqrt{2}}\right)^2 = 50\,\mathrm{V^2}$.
6. $P = I_{rms}^2 R = \frac{V_{rms}^2 R}{Z^2} = \frac{50 \times 50}{3153.8} \approx 0.79\,\mathrm{W}$, which is option $3$.

**Subtopic:** Power in an AC Circuit · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 8)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q028_b32b9209_27102026.png?v=b32b92090acc)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q028_ffb821c7_27102026.png?v=ffb821c7208b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Power in a series RLC circuit is $I_{rms}^2R$ with $I_{rms} = V_{rms}/Z$, and Z combines the net reactance with R in quadrature, not by plain addition
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Adding the resistance and the net reactance straight -- $50 + 25.6 = 75.6\ \Omega$ instead of $\sqrt{50^2 + 25.6^2} = 56.2\ \Omega$ -- gives $I_{rms} = 0.094$ A and a power of 0.43 W; the two must be combined at right angles because the voltages across R and across the reactance are a quarter cycle apart.
- **Why:** This question requires a power computed from the circuit's impedance, demonstrated by 'an inductor 20 mH, a capacitor 100 microfarad and a resistor 50 ohm are connected in series' with $V = 10\sin 314t$.
<!--/ecat-->

## Q29

Physics · Magnetic Effect of Electric Current

Current sensitivity of a moving coil galvanometer is $5\,\mathrm{div/mA}$ and its voltage sensitivity (angular deflection per unit voltage applied) is $20\,\mathrm{div/V}$. The resistance of the galvanometer is

- **(1)** $250\,\Omega$
- (2) $25\,\Omega$
- (3) $40\,\Omega$
- (4) $500\,\Omega$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Current sensitivity
2. $I_S = \frac{\mathrm{NBA}}{\mathrm{C}}$
3. Voltage sensitivity
4. $V_S = \frac{\mathrm{NBA}}{\mathrm{CR_G}}$
5. So, resistance of galvanometer
6. $R_G = \frac{I_S}{V_S} = \frac{5 \times 1}{20 \times 10^{-3}} = \frac{5000}{20} = 250\,\Omega$

**Solved independently** (answer withheld)

1. Current sensitivity $I_s = \frac{\phi}{I} = 5\,\mathrm{div/mA} = 5000\,\mathrm{div/A}$.
2. Voltage sensitivity $V_s = \frac{\phi}{V} = \frac{\phi}{IG} = \frac{I_s}{G}$.
3. $G = \frac{I_s}{V_s} = \frac{5000\,\mathrm{div/A}}{20\,\mathrm{div/V}} = 250\,\Omega$, which is option $1$.

**Subtopic:** Moving Coil Galvanometer · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q029_e358deb9_27102026.png?v=e358deb9a790)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q029_f87160de_27102026.png?v=f87160de998c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Voltage sensitivity is current sensitivity divided by the galvanometer's resistance, so R is the ratio of the two once the milliampere is converted: 5000 div/A over 20 div/V
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Converting 5 div/mA with the wrong power of ten -- reading the milliampere as $10^{-2}$ A, which makes the current sensitivity 500 div/A instead of 5000 -- turns the ratio into $500/20 = 25\ \Omega$ in place of 250.
- **Why:** This question requires a resistance computed from two sensitivities, demonstrated by 'current sensitivity ... is 5 div/mA and its voltage sensitivity ... is 20 div/V'.
<!--/ecat-->

## Q30

Physics · Work, Energy and Power

A body initially at rest and sliding along a frictionless track from a height $h$ (as shown in the figure) just completes a vertical circle of diameter $AB = D$. The height $h$ is equal to

![printed figure: A body slides from height h down a frictionless incline into a vertical circular loop of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q030_8c330b5f_27102026.svg?v=8c330b5f7252)

*A body slides from height h down a frictionless incline into a vertical circular loop of diameter AB*

![drawn: A body slides from height h down a frictionless incline into a vertical circular loop of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q030_question_e6ed7c61_27102026.svg?v=e6ed7c61a358)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\frac{7}{5}D$
- (2) $D$
- (3) $\frac{3}{2}D$
- **(4)** $\frac{5}{4}D$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Body sliding down a frictionless incline from height h into a vertical loop of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q030_sol_1_d1edf608_27102026.svg?v=d1edf60879c5)

*Body sliding down a frictionless incline from height h into a vertical loop of diameter AB*

![drawn: Body sliding down a frictionless incline from height h into a vertical loop of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q030_solution_1_aa76c18a_27102026.svg?v=aa76c18aadec)  
*drawn on the booklet's geometry, checked against its figure spec*

1. As track is frictionless, so total mechanical energy will remain constant
2. $\mathrm{T.M.E}_{I} = \mathrm{T.M.E}_{F}$
3. $0 + mgh = \frac{1}{2}mv_{L}^{2} + 0$
4. $h = \frac{v_{L}^{2}}{2g}$
5. For completing the vertical circle, $v_{L} \geq \sqrt{5gR}$
6. $h = \frac{5gR}{2g} = \frac{5}{2}R = \frac{5}{4}D$

**Solved independently** (answer withheld)

1. The radius of the circle is $R = \frac{D}{2}$.
2. To just complete the vertical circle, the speed at the lowest point $A$ must satisfy $v_A^2 = 5gR$.
3. The track is frictionless and the body starts from rest at height $h$ above $A$, so $mgh = \frac{1}{2}m v_A^2$.
4. $gh = \frac{5gR}{2} \Rightarrow h = \frac{5R}{2}$.
5. $h = \frac{5}{2}\cdot\frac{D}{2} = \frac{5}{4}D$, which is option $4$.

**Subtopic:** Motion in a Vertical Circular Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q030_dd536503_27102026.png?v=dd536503826e)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q030_a52ff9d0_27102026.png?v=a52ff9d0d376)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Just completing a vertical loop needs $v^2 = gR$ at the top, so the starting height is the full diameter plus a quarter of it, $h = 5D/4$
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Dropping the stem's condition 'just completes' leaves only the requirement of reaching the top, so $mgh = mgD$ and $h = D$; a body arriving at the top with no speed leaves the track, and keeping contact needs a further $v^2 = gR$, worth another $D/4$ of height.
- **Why:** This question requires a height computed from energy conservation under a stated condition, demonstrated by 'just completes a vertical circle of diameter AB = D'.
- **Note:** The figure reached this step as a drawn spec showing h measured from the level of the loop's lowest point, which is the reading the key rests on.
<!--/ecat-->

## Q31

Physics · Rotational Motion

Three objects, A : (a solid sphere), B : (a thin circular disk) and C : (a circular ring), each have the same mass $M$ and radius $R$. They all spin with the same angular speed $\omega$ about their own symmetry axes. The amounts of work ($W$) required to bring them to rest, would satisfy the relation

- (1) $W_{B} > W_{A} > W_{C}$
- (2) $W_{A} > W_{B} > W_{C}$
- **(3)** $W_{C} > W_{B} > W_{A}$
- (4) $W_{A} > W_{C} > W_{B}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Work done required to bring them rest
2. $\Delta W = \Delta KE$
3. $\Delta W = \frac{1}{2}I\omega^{2}$
4. $\Delta W \propto I$ for same $\omega$
5. $W_{A} : W_{B} : W_{C} = \frac{2}{5}MR^{2} : \frac{1}{2}MR^{2} : MR^{2}$
6. $= \frac{2}{5} : \frac{1}{2} : 1$
7. $= 4 : 5 : 10$
8. $\Rightarrow W_{C} > W_{B} > W_{A}$

**Solved independently** (answer withheld)

1. By the work-energy theorem, $W = K_{rot} = \frac{1}{2} I \omega^2$; with the same $\omega$, $W \propto I$.
2. $I_A = \frac{2}{5}MR^2$ (solid sphere), $I_B = \frac{1}{2}MR^2$ (disk about its axis), $I_C = MR^2$ (ring about its axis).
3. $I_C > I_B > I_A \Rightarrow W_C > W_B > W_A$, which is option $3$.

**Subtopic:** Kinetic Energy of a Rigid Body Rotating About a Given Axis · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q031_0218d35b_27102026.png?v=0218d35b9cdc)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q031_07d9cfe0_27102026.png?v=07d9cfe05a98)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** The work needed to stop a spinning body is its rotational kinetic energy $\frac{1}{2}I\omega^2$, so with $M$, $R$ and $\omega$ fixed the ranking is the ranking of $I$: ring $MR^2$, disc $\frac{1}{2}MR^2$, sphere $\frac{2}{5}MR^2$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Ranking the bodies by how much material each contains rather than by where that material sits puts the solid sphere first and the thin ring last, which is the exact inverse of the moment-of-inertia order; $I$ is set by distance from the axis, and the ring carries all its mass at $R$.
- **Why:** This question requires three standard moments of inertia compared against one another, demonstrated by the stem fixing 'the same mass $M$ and radius $R$' and 'the same angular speed $\omega$' so that only mass distribution separates the three, and by options that are inequality chains such as '$W_C > W_B > W_A$'.
<!--/ecat-->

## Q32

Physics · Work, Energy and Power

A moving block having mass $m$, collides with another stationary block having mass $4m$. The lighter block comes to rest after collision. When the initial velocity of the lighter block is $v$, then the value of coefficient of restitution $(e)$ will be

- (1) $0.8$
- **(2)** $0.25$
- (3) $0.5$
- (4) $0.4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to law of conservation of linear momentum,
2. $mv + 4m \times 0 = 4mv' + 0$
3. $v' = \frac{v}{4}$
4. $e = \frac{\text{Relative velocity of separation}}{\text{Relative velocity of approach}} = \frac{\frac{v}{4}}{v}$
5. $e = \frac{1}{4} = 0.25$

**Solved independently** (answer withheld)

1. Conserve momentum: $m v + 4m(0) = m(0) + 4m v_2$.
2. Solve: $v_2 = \frac{v}{4}$.
3. Coefficient of restitution: $e = \frac{v_2 - v_1'}{v_1 - u_2} = \frac{v/4 - 0}{v - 0}$.
4. $e = \frac{1}{4} = 0.25$, which is option $2$.

**Subtopic:** Problem on Coefficient of Restitution · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q032_223f6872_27102026.png?v=223f687231db)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q032_2c07ec94_27102026.png?v=2c07ec948015)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Coefficient of restitution is the separation speed divided by the approach speed, and the post-collision speed of the struck block comes from momentum conservation, which holds in every collision, not from energy conservation, which does not
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Taking the collision to conserve kinetic energy gives $\frac{1}{2}mv^2 = \frac{1}{2}(4m)v_2^2$, so $v_2 = v/2$ and $e = 0.5$; the lighter block stopping dead is itself the sign that energy was lost, and only momentum survives.
- **Why:** This question requires a number computed from the stem's masses and velocity, demonstrated by 'the value of coefficient of restitution $(e)$ will be' with four bare numbers as options.
<!--/ecat-->

## Q33

Physics · Laws of Motion

Which one of the following statements is incorrect?

- (1) Frictional force opposes the relative motion.
- (2) Limiting value of static friction is directly proportional to normal reaction.
- (3) Rolling friction is smaller than sliding friction.
- **(4)** Coefficient of sliding friction has dimensions of length.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Coefficient of sliding friction has no dimension.
2. $f = \mu_s N$
3. $\Rightarrow \mu_s = \frac{f}{N}$

**Solved independently** (answer withheld)

1. Friction opposes relative motion (or impending relative motion) between surfaces, so statement $1$ is correct.
2. $f_s^{\max} = \mu_s N$, so the limiting static friction is directly proportional to $N$; statement $2$ is correct.
3. Rolling friction is much smaller than sliding friction; statement $3$ is correct.
4. $\mu_k = \frac{f_k}{N} = \frac{[MLT^{-2}]}{[MLT^{-2}]} = [M^0L^0T^0]$, dimensionless, so statement $4$ is incorrect, which is option $4$.

**Subtopic:** Kinetic Friction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 9)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q033_f3da4b2c_27102026.png?v=f3da4b2cbdb4)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q033_adb5111b_27102026.png?v=adb5111b4f58)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The coefficient of friction is the ratio of two forces and therefore dimensionless; the other three sentences are the friction laws as the textbook states them
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Dropping the word 'relative' turns the sentence into the blanket claim that friction always opposes motion, which the walker appears to break, so the statement gets marked as the incorrect one; friction there still opposes the backward slip of sole on ground.
- **Why:** This question requires the friction laws as stated judged one at a time against a negated task, demonstrated by 'Coefficient of sliding friction has dimensions of length' being the only option that contradicts $\mu = f/N$.
<!--/ecat-->

## Q34

Physics · Kinematics

A toy car with charge $q$ moves on a frictionless horizontal plane surface under the influence of a uniform electric field $\vec{E}$. Due to the force $q\vec{E}$, its velocity increases from $0$ to $6\,\mathrm{m/s}$ in one second duration. At that instant the direction of the field is reversed. The car continues to move for two more seconds under the influence of this field. The average velocity and the average speed of the toy car between $0$ to $3$ seconds are respectively

- (1) $1\,\mathrm{m/s}$, $3.5\,\mathrm{m/s}$
- **(2)** $1\,\mathrm{m/s}$, $3\,\mathrm{m/s}$
- (3) $2\,\mathrm{m/s}$, $4\,\mathrm{m/s}$
- (4) $1.5\,\mathrm{m/s}$, $3\,\mathrm{m/s}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Toy car path A to B and back to C with velocities at t = 0, 1, 2, 3](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q034_sol_1_c42d696e_27102026.svg?v=c42d696e3279)

*Toy car path A to B and back to C with velocities at t = 0, 1, 2, 3*

![drawn: Toy car path A to B and back to C with velocities at t = 0, 1, 2, 3](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q034_solution_1_ec04b6eb_27102026.svg?v=ec04b6eb76e8)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Acceleration $a = \frac{6-0}{1} = 6\,\mathrm{ms^{-2}}$
2. For $t = 0$ to $t = 1\,\mathrm{s}$,
3. $S_1 = \frac{1}{2}\times 6(1)^2 = 3\,\mathrm{m}$ ...(i)
4. For $t = 1\,\mathrm{s}$ to $t = 2\,\mathrm{s}$,
5. $S_2 = 6.1 - \frac{1}{2}\times 6(1)^2 = 3\,\mathrm{m}$ ...(ii)
6. For $t = 2\,\mathrm{s}$ to $t = 3\,\mathrm{s}$,
7. $S_3 = 0 - \frac{1}{2}\times 6(1)^2 = -3\,\mathrm{m}$ ...(iii)
8. Total displacement $S = S_1 + S_2 + S_3 = 3\,\mathrm{m}$
9. Average velocity $= \frac{3}{3} = 1\,\mathrm{ms^{-1}}$
10. Total distance travelled $= 9\,\mathrm{m}$
11. Average speed $= \frac{9}{3} = 3\,\mathrm{ms^{-1}}$

**Solved independently** (answer withheld)

1. Acceleration magnitude: $a = \frac{6-0}{1} = 6\,\mathrm{m/s^2}$.
2. From $0$ to $1\,\mathrm{s}$: $s_1 = \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$ forward.
3. After reversal the car decelerates at $6\,\mathrm{m/s^2}$, so it stops at $t = 2\,\mathrm{s}$: $s_2 = 6(1) - \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$ forward.
4. From $2$ to $3\,\mathrm{s}$ it accelerates backward from rest: $s_3 = \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$ backward.
5. Net displacement $= 3 + 3 - 3 = 3\,\mathrm{m}$; total distance $= 3 + 3 + 3 = 9\,\mathrm{m}$.
6. Average velocity $= \frac{3}{3} = 1\,\mathrm{m/s}$; average speed $= \frac{9}{3} = 3\,\mathrm{m/s}$, which is option $2$.

**Subtopic:** Average Velocity, Average Speed · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 9)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q034_b177a39b_27102026.png?v=b177a39b1704)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q034_a16240ac_27102026.png?v=a16240acee4d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Average velocity is net displacement over total time and average speed is path length over the same total time; reversing the field turns the car round, so the two numbers come apart
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The path length is worked out correctly as $9$ m, giving $9/3 = 3$ m/s for the average speed, and then the $3$ m of net displacement is divided by the 'two more seconds' the stem prints for the reversed-field phase, giving $1.5$ m/s instead of $1$ m/s.
- **Why:** This question requires two numbers computed from the stem's acceleration and timings, demonstrated by 'The average velocity and the average speed of the toy car between $0$ to $3$ seconds are respectively' and options that print a pair of values.
<!--/ecat-->

## Q35

Physics · Laws of Motion

A block of mass $m$ is placed on a smooth inclined wedge ABC of inclination $\theta$ as shown in the figure. The wedge is given an acceleration 'a' towards the right. The relation between $a$ and $\theta$ for the block to remain stationary on the wedge is

![printed figure: Block m on a smooth hatched wedge ABC of inclination θ, wedge accelerated a to the right](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q035_fcea1f77_29102026.svg?v=fcea1f779456)

*Block m on a smooth hatched wedge ABC of inclination θ, wedge accelerated a to the right*

![drawn: Block m on a smooth hatched wedge ABC of inclination θ, wedge accelerated a to the right](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q035_question_17267fc1_27102026.svg?v=17267fc16d00)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $a = g\cos\theta$
- (2) $a = \dfrac{g}{\sin\theta}$
- (3) $a = \dfrac{g}{\mathrm{cosec}\,\theta}$
- **(4)** $a = g\tan\theta$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Free-body diagram of the block on the accelerating wedge: N, mg, pseudo force ma and the components of N](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q035_sol_1_e1ef0f86_29102026.svg?v=e1ef0f8620f9)

*Free-body diagram of the block on the accelerating wedge: N, mg, pseudo force ma and the components of N*

![drawn: Free-body diagram of the block on the accelerating wedge: N, mg, pseudo force ma and the components of N](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q035_solution_1_5375972a_27102026.svg?v=5375972a5394)  
*drawn on the booklet's geometry, checked against its figure spec*

1. In non-inertial frame,
2. $N\sin\theta = ma$ ...(i)
3. $N\cos\theta = mg$ ...(ii)
4. $\tan\theta = \frac{a}{g}$
5. $a = g\tan\theta$

**Solved independently** (answer withheld)

1. The incline is smooth, so the only forces on the block are its weight $mg$ (down) and the normal reaction $N$, perpendicular to face AB, pointing up and to the right.
2. For the block to stay at rest relative to the wedge it must move with acceleration $a$ to the right, so horizontally $N\sin\theta = ma$.
3. Vertically there is no acceleration, so $N\cos\theta = mg$.
4. Dividing the two equations gives $\tan\theta = \frac{a}{g}$, so $a = g\tan\theta$, which is option $4$.

**Subtopic:** Pseudo Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q035_03d9c0f3_27102026.png?v=03d9c0f34628)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q035_92362dbd_27102026.png?v=92362dbd9e6b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A block stays put on a smooth accelerating wedge when gravity and the horizontal pseudo-force balance along the incline: $mg\sin\theta = ma\cos\theta$, hence $a = g\tan\theta$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $g/\mathrm{cosec}\,\theta$ is $g\sin\theta$, the true acceleration of a block sliding freely down a smooth incline of this angle, printed in a form that hides the familiar expression; this stem asks for the wedge acceleration that stops the block sliding at all.
- **Why:** This question requires a symbolic relation derived from the force balance in the accelerating frame, demonstrated by 'The relation between $a$ and $\theta$ for the block to remain stationary on the wedge' with four trigonometric expressions as options.
- **Note:** The figure was supplied and adds only the labelled wedge ABC and the rightward arrow for $a$, both already stated in the stem, so it does not gate the answer.
<!--/ecat-->

## Q36

Physics · Rotational Motion

The moment of the force, $\vec{F} = 4\hat{i} + 5\hat{j} - 6\hat{k}$ at $(2, 0, -3)$, about the point $(2, -2, -2)$, is given by

- (1) $-7\hat{i} - 8\hat{j} - 4\hat{k}$
- (2) $-4\hat{i} - \hat{j} - 8\hat{k}$
- (3) $-8\hat{i} - 4\hat{j} - 7\hat{k}$
- **(4)** $-7\hat{i} - 4\hat{j} - 8\hat{k}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Position vectors r0 (O to A) and r (O to P), with r - r0 from A to P and force F acting through P](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q036_sol_1_c3bff137_27102026.svg?v=c3bff13722d9)

*Position vectors r0 (O to A) and r (O to P), with r - r0 from A to P and force F acting through P*

![drawn: Position vectors r0 (O to A) and r (O to P), with r - r0 from A to P and force F acting through P](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q036_solution_1_d66d8c48_27102026.svg?v=d66d8c48aa39)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\vec{\tau} = (\vec{r} - \vec{r}_0) \times \vec{F}$ ...(i)
2. $\vec{r} - \vec{r}_0 = (2\hat{i} + 0\hat{j} - 3\hat{k}) - (2\hat{i} - 2\hat{j} - 2\hat{k})$
3. $= 0\hat{i} + 2\hat{j} - \hat{k}$
4. $\vec{\tau} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & 2 & -1 \\ 4 & 5 & -6 \end{vmatrix} = -7\hat{i} - 4\hat{j} - 8\hat{k}$

**Solved independently** (answer withheld)

1. Position vector of the point of application relative to the pivot: $\vec{r} = (2-2)\hat{i} + (0-(-2))\hat{j} + (-3-(-2))\hat{k} = 2\hat{j} - \hat{k}$.
2. Moment of force: $\vec{\tau} = \vec{r} \times \vec{F} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & 2 & -1 \\ 4 & 5 & -6 \end{vmatrix}$.
3. $\hat{i}$ component: $(2)(-6) - (-1)(5) = -12 + 5 = -7$.
4. $\hat{j}$ component: $-[(0)(-6) - (-1)(4)] = -4$.
5. $\hat{k}$ component: $(0)(5) - (2)(4) = -8$.
6. $\vec{\tau} = -7\hat{i} - 4\hat{j} - 8\hat{k}$, which is option $4$.

**Subtopic:** Problems on Torque of a Force About the Axis of Rotation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q036_a105a8a5_27102026.png?v=a105a8a53abf)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q036_d443bd66_27102026.png?v=d443bd663747)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Torque about a point is $\vec{\tau} = \vec{r} \times \vec{F}$ with $\vec{r}$ drawn from that point to the force's point of application, and the component formulas follow the cyclic order $x \to y \to z$
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  With $\vec{r} = (0, 2, -1)$ the three cofactors come out $-7$, $-4$ and $-8$; entering $r_xF_y - r_yF_x = -8$ in the $\hat{j}$ slot and $r_zF_x - r_xF_z = -4$ in the $\hat{k}$ slot breaks the cyclic order and prints this option, with the correct $-7\hat{i}$ still in front.
- **Why:** This question requires a vector computed from the stem's numbers, demonstrated by 'The moment of the force, $\vec{F} = 4\hat{i} + 5\hat{j} - 6\hat{k}$ at $(2, 0, -3)$, about the point $(2, -2, -2)$' naming a point of application and a different pivot.
<!--/ecat-->

## Q37

Physics · Units and Measurements

A student measured the diameter of a small steel ball using a screw gauge of least count $0.001\,\mathrm{cm}$. The main scale reading is $5\,\mathrm{mm}$ and zero of circular scale division coincides with 25 divisions above the reference level. If screw gauge has a zero error of $-0.004\,\mathrm{cm}$, the correct diameter of the ball is

- (1) $0.053\,\mathrm{cm}$
- (2) $0.525\,\mathrm{cm}$
- (3) $0.521\,\mathrm{cm}$
- **(4)** $0.529\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Diameter of the ball
2. $= \mathrm{MSR} + \mathrm{CSR} \times (\text{Least count}) - \text{Zero error}$
3. $= 0.5\,\mathrm{cm} + 25 \times 0.001 - (-0.004)$
4. $= 0.5 + 0.025 + 0.004$
5. $= 0.529\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Main scale reading: $\text{MSR} = 5\,\mathrm{mm} = 0.5\,\mathrm{cm}$.
2. Circular scale reading: $\text{CSR} = 25 \times 0.001\,\mathrm{cm} = 0.025\,\mathrm{cm}$.
3. Observed reading: $0.5 + 0.025 = 0.525\,\mathrm{cm}$.
4. Correct reading $=$ observed $-$ zero error: $0.525 - (-0.004) = 0.529\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q037_a4ec8db7_27102026.png?v=a4ec8db78750)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q037_0787dfa1_27102026.png?v=0787dfa196b9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A screw-gauge reading is corrected by subtracting the zero error with its sign, so a negative zero error makes the true diameter larger than the reading
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The correction is applied the wrong way round: $0.525 - 0.004 = 0.521$ cm, because the minus sign on the stem's zero error is dropped before subtracting.
- **Why:** This question requires computing a corrected screw-gauge diameter from the stem's numbers, demonstrated by 'If screw gauge has a zero error of $-0.004\,\mathrm{cm}$, the correct diameter of the ball is'.
- **Note:** Both candidate traps were checked: 0.525 cm is the uncorrected reading and 0.521 cm is the correction applied in the wrong direction. The sign of the negative zero error is the discriminating step the stem spotlights, so the one trap sits on option 3 and the uncorrected reading is carried as the second route.
<!--/ecat-->

## Q38

Physics · Rotational Motion

A solid sphere is rotating freely about its symmetry axis in free space. The radius of the sphere is increased keeping its mass same. Which of the following physical quantities would remain constant for the sphere?

- (1) Rotational kinetic energy
- (2) Moment of inertia
- (3) Angular velocity
- **(4)** Angular momentum

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\tau_{ex} = 0$
2. So, $\frac{dL}{dt} = 0$
3. i.e. $L = \text{constant}$
4. So angular momentum remains constant.

**Solved independently** (answer withheld)

1. In free space no external torque acts: $\tau_{ext} = 0 \Rightarrow L = I\omega = \text{constant}$.
2. $I = \frac{2}{5}MR^2$ increases as $R$ increases with $M$ fixed, so moment of inertia changes.
3. $\omega = \frac{L}{I}$ decreases, so angular velocity changes.
4. $K = \frac{L^2}{2I}$ decreases, so rotational kinetic energy changes; only angular momentum is constant, option $4$.

**Subtopic:** Conservation of Angular Momentum · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 11)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q038_e47c658f_27102026.png?v=e47c658f5ad1)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q038_4cb520d2_27102026.png?v=4cb520d25e24)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** With no external torque, angular momentum is the quantity that survives a change of shape, while the moment of inertia, the angular velocity and the rotational kinetic energy all shift
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  'Rotating freely in free space' is read as a spin nothing can alter, so conservation is attached to $\omega$ instead of to $L = I\omega$.
- **Why:** This question requires applying the zero-external-torque rule to a change of shape, demonstrated by 'rotating freely about its symmetry axis in free space' together with 'the radius of the sphere is increased keeping its mass same'.
- **Note:** All three wrong options are the three other quantities in $L = I\omega$ and $K = L^2/2I$, each reachable by conserving the wrong one, so no option here is filler.
<!--/ecat-->

## Q39

Physics · Gravitation

The kinetic energies of a planet in an elliptical orbit about the Sun, at positions A, B and C are $K_A$, $K_B$ and $K_C$, respectively. AC is the major axis and SB is perpendicular to AC at the position of the Sun S as shown in the figure. Then

![printed figure: Elliptical orbit with major axis AC and SB perpendicular to AC at the Sun S](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q039_93b73e10_27102026.svg?v=93b73e10e6a4)

*Elliptical orbit with major axis AC and SB perpendicular to AC at the Sun S*

![drawn: Elliptical orbit with major axis AC and SB perpendicular to AC at the Sun S](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q039_question_7fc8a66f_27102026.svg?v=7fc8a66f4a62)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $K_B < K_A < K_C$
- **(2)** $K_A > K_B > K_C$
- (3) $K_A < K_B < K_C$
- (4) $K_B > K_A > K_C$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Elliptical orbit with major axis AC, Sun S, SB perpendicular to AC, velocities V_A and V_C](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q039_sol_1_ee8dfc60_29102026.svg?v=ee8dfc60b528)

*Elliptical orbit with major axis AC, Sun S, SB perpendicular to AC, velocities V_A and V_C*

![drawn: Elliptical orbit with major axis AC, Sun S, SB perpendicular to AC, velocities V_A and V_C](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q039_solution_1_b47ef736_27102026.svg?v=b47ef7368a64)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Point A is perihelion and C is aphelion.
2. So, $V_A > V_B > V_C$
3. So, $K_A > K_B > K_C$

**Solved independently** (answer withheld)

1. From the figure, $S$ lies on $AC$ close to $A$, so $r_A < r_B < r_C$ where $r$ is the distance from the Sun.
2. Angular momentum about $S$ is conserved (Kepler's second law), so the planet moves fastest when nearest the Sun and slowest when farthest.
3. Hence $v_A > v_B > v_C$.
4. Since $K = \frac{1}{2}mv^2$, $K_A > K_B > K_C$, which is option $2$.

**Subtopic:** Kepler's Law · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q039_9f90f513_27102026.png?v=9f90f51309f5)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q039_80c3cbbe_27102026.png?v=80c3cbbe24a1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A planet is fastest where it is nearest the Sun, and on an ellipse the perihelion end, the point on the perpendicular through the focus and the aphelion end sit at increasing distances
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The distances from S are ordered correctly off the figure and then read as 'farther from the Sun means faster', which prints the key's ranking backwards.
- **Why:** This question requires ranking three kinetic energies by distance from the focus, demonstrated by the options being orderings such as '$K_A > K_B > K_C$' rather than values.
- **Note:** asks is recorded as order because the answer is a ranking; the figure contributes one fact the stem does not state, namely that S lies nearer A than C. The sketch's own geometry is loose: the spec places S at x=135 on an ellipse centred at x=230 with semi-axes 182 and 67, so S is not at the geometric focus and the drawn SB (57 units) is shorter than SA (87 units). The printed key is unaffected, since a true ellipse always has $b^2/a > a-c$.
<!--/ecat-->

## Q40

Physics · Gravitation

If the mass of the Sun were ten times smaller and the universal gravitational constant were ten times larger in magnitude, which of the following is not correct?

- (1) Time period of a simple pendulum on the Earth would decrease
- (2) Walking on the ground would become more difficult
- (3) Raindrops will fall faster
- **(4)** ‘$g$’ on the Earth will not change

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. If Universal Gravitational constant becomes ten times, then $G' = 10\,G$
2. So, acceleration due to gravity increases.
3. i.e. (4) is wrong option.

**Solved independently** (answer withheld)

1. Acceleration due to gravity on Earth depends only on Earth's mass and radius: $g = \frac{G M_E}{R_E^2}$; the Sun's mass does not enter.
2. With $G' = 10G$ and $M_E$ unchanged: $g' = \frac{(10G) M_E}{R_E^2} = 10g$, so $g$ changes and option $4$ is false.
3. $T = 2\pi\sqrt{\frac{l}{g'}}$ decreases as $g' > g$, so option $1$ is true.
4. Weight $mg'$ increases, so walking is harder (option $2$ true), and raindrops' terminal speed $v_t \propto g$ increases (option $3$ true).
5. The statement that is not correct is option $4$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q040_058df170_27102026.png?v=058df170784b)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q040_aa4dfb1a_27102026.png?v=aa4dfb1ac99f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** On the Earth's surface $g = GM_E/R^2$ carries G, so a ten-times-larger G multiplies g tenfold, while the Sun's mass never enters g at all
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Only the Sun's smaller mass is carried forward, so g on the Earth is taken as unchanged; a pendulum on the Earth then keeps its period and 'would decrease' reads as the statement that is not correct.
- **Why:** This question requires applying $g = GM_E/R^2$ to the stated change in G and then grading each consequence, demonstrated by option 4, '‘$g$’ on the Earth will not change', being the claim that fails.
- **Note:** The dropped-G reading makes each of statements 1-3 read as 'not correct', so this device is set-level; it is recorded on option 1 because that option additionally carries the inverted $T$-$g$ route. The shape is four full claims graded for correctness - the codebook's E1 statement_options - but no statement block or lettered list is printed and the stem does not name statements, so qtype stays mcq under the shape rule.
<!--/ecat-->

## Q41

Physics · Rotational Motion

A solid sphere is in rolling motion. In rolling motion a body possesses translational kinetic energy $(K_t)$ as well as rotational kinetic energy $(K_r)$ simultaneously. The ratio $K_t : (K_t + K_r)$ for the sphere is

- (1) $10 : 7$
- **(2)** $5 : 7$
- (3) $7 : 10$
- (4) $2 : 5$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $K_t = \frac{1}{2}mv^2$
2. $K_t + K_r = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2 = \frac{1}{2}mv^2 + \frac{1}{2}\left(\frac{2}{5}mr^2\right)\left(\frac{v}{r}\right)^2$
3. $= \frac{7}{10}mv^2$
4. So, $\frac{K_t}{K_t + K_r} = \frac{5}{7}$

**Solved independently** (answer withheld)

1. For a solid sphere $I = \frac{2}{5}mR^2$ and in rolling $\omega = \frac{v}{R}$.
2. $K_t = \frac{1}{2}mv^2$.
3. $K_r = \frac{1}{2}I\omega^2 = \frac{1}{2}\cdot\frac{2}{5}mR^2\cdot\frac{v^2}{R^2} = \frac{1}{5}mv^2$.
4. $K_t + K_r = \frac{1}{2}mv^2 + \frac{1}{5}mv^2 = \frac{7}{10}mv^2$.
5. $\frac{K_t}{K_t + K_r} = \frac{1/2}{7/10} = \frac{5}{7}$, so the ratio is $5 : 7$, which is option $2$.

**Subtopic:** Rolling Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q041_24e0ca23_27102026.png?v=24e0ca23d4f7)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q041_3a08b623_27102026.png?v=3a08b623af93)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a rolling body the split of kinetic energy is fixed by its moment of inertia: with $I = \frac{2}{5}mr^2$ a solid sphere carries five sevenths of its energy in translation
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\frac{7}{10}mv^2$ is the rolling sphere's total kinetic energy, and 7 : 10 is that remembered coefficient handed in before the asked ratio is ever formed.
- **Why:** This question requires computing a numerical energy ratio from the sphere's moment of inertia, demonstrated by 'The ratio $K_t : (K_t + K_r)$ for the sphere is'.
<!--/ecat-->

## Q42

Physics · Mechanical Properties of Fluids

A small sphere of radius 'r' falls from rest in a viscous liquid. As a result, heat is produced due to viscous force. The rate of production of heat when the sphere attains its terminal velocity, is proportional to

- **(1)** $r^{5}$
- (2) $r^{2}$
- (3) $r^{3}$
- (4) $r^{4}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Power $= 6\pi\eta r V_T \cdot V_T = 6\pi\eta r V_T^{2}$
2. $V_T \propto r^{2}$
3. $\Rightarrow$ Power $\propto r^{5}$

**Solved independently** (answer withheld)

1. At terminal velocity the rate of heat production equals the power of the viscous force: $P = F_v \, v_t$.
2. Stokes' law gives $F_v = 6\pi\eta r v_t$, so $P = 6\pi\eta r v_t^{2}$.
3. Terminal velocity $v_t = \frac{2 r^{2} (\rho - \sigma) g}{9\eta}$, so $v_t \propto r^{2}$.
4. $P \propto r \, (r^{2})^{2} = r^{5}$, which is option $1$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q042_127c1439_27102026.png?v=127c143982ac)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q042_3da60b65_27102026.png?v=3da60b652a35)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** At terminal velocity the gravitational work all goes to heat, so the rate is (effective weight) times (terminal velocity), that is $r^3 \times r^2$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $v_t \propto r^2$ is the proportionality the chapter prints for a sphere in a viscous liquid, and the stem's phrase 'attains its terminal velocity' points at it, so the velocity's power is handed in as the heat rate's.
- **Why:** This question requires chaining Stokes' terminal velocity with rate = force $\times$ velocity to reach a power of r, demonstrated by 'The rate of production of heat when the sphere attains its terminal velocity, is proportional to'.
- **Note:** The four options are the rungs of the derivation ladder - $r^2$ for the velocity, $r^3$ for the force, $r^4$ for a dropped square and $r^5$ for the product - so every wrong option carries a route and none is filler.
<!--/ecat-->

## Q43

Physics · Thermal Properties of Matter

The power radiated by a black body is $P$ and it radiates maximum energy at wavelength, $\lambda_0$. If the temperature of the black body is now changed so that it radiates maximum energy at wavelength $\frac{3}{4}\lambda_0$, the power radiated by it becomes $nP$. The value of $n$ is

- **(1)** $\frac{256}{81}$
- (2) $\frac{4}{3}$
- (3) $\frac{3}{4}$
- (4) $\frac{81}{256}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. We know,
2. $\lambda_{\mathrm{max}}\,T = \text{constant}$ (Wien's law)
3. So, $\lambda_{\mathrm{max}_1}T_1 = \lambda_{\mathrm{max}_2}T_2$
4. $\Rightarrow \lambda_0\,T = \frac{3\lambda_0}{4}T'$
5. $\Rightarrow T' = \frac{4}{3}T$
6. So, $\frac{P_2}{P_1} = \left(\frac{T'}{T}\right)^4 = \left(\frac{4}{3}\right)^4 = \frac{256}{81}$

**Solved independently** (answer withheld)

1. Wien's displacement law: $\lambda_m T = \text{constant}$, so $\lambda_0 T = \frac{3}{4}\lambda_0 T'$.
2. $T' = \frac{4}{3}T$.
3. Stefan-Boltzmann law: $P \propto T^4$, so $n = \frac{P'}{P} = \left(\frac{T'}{T}\right)^4$.
4. $n = \left(\frac{4}{3}\right)^4 = \frac{256}{81}$, which is option $1$.

**Subtopic:** Radiation Laws · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q043_852fa283_27102026.png?v=852fa283aea5)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q043_f3950e28_27102026.png?v=f3950e282ee1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Wien's law ties the peak wavelength to $1/T$ and Stefan's law ties the radiated power to $T^4$, so the power scales as the inverse fourth power of the peak wavelength
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Stefan's fourth power is applied to the wavelength factor itself, $\left(\frac{3}{4}\right)^4 = \frac{81}{256}$, because Wien's inverse step between $\lambda_m$ and $T$ is skipped.
- **Why:** This question requires finding how many times the radiated power changes when the peak wavelength changes, demonstrated by 'the power radiated by it becomes $nP$. The value of $n$ is'.
<!--/ecat-->

## Q44

Physics · Mechanical Properties of Solids

Two wires are made of the same material and have the same volume. The first wire has cross-sectional area $A$ and the second wire has cross-sectional area $3A$. If the length of the first wire is increased by $\Delta l$ on applying a force $F$, how much force is needed to stretch the socond wire by the same amount?

- (1) $4\,F$
- (2) $6\,F$
- **(3)** $9\,F$
- (4) $F$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Wire 1 :

![printed figure: The second wire (area A, length 3l) pulled to the right by force F](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q044_sol_1_2569e317_29102026.svg?v=2569e3174125)

*The second wire (area A, length 3l) pulled to the right by force F*

![drawn: The second wire (area A, length 3l) pulled to the right by force F](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q044_solution_1_91c8aed7_27102026.svg?v=91c8aed7215f)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Wire 2 :

![printed figure: Second wire drawn as a cylinder of area 3A and length l, pulled by force F' at its right end](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q044_sol_2_ca934070_29102026.svg?v=ca934070f5d8)

*Second wire drawn as a cylinder of area 3A and length l, pulled by force F' at its right end*

![drawn: Second wire drawn as a cylinder of area 3A and length l, pulled by force F' at its right end](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q044_solution_2_4e062a82_27102026.svg?v=4e062a828036)  
*drawn on the booklet's geometry, checked against its figure spec*

3. For wire 1,
4. $\Delta l = \left(\frac{F}{AY}\right)3l \quad \ldots(\mathrm{i})$
5. For wire 2,
6. $\frac{F'}{3A} = Y\frac{\Delta l}{l}$
7. $\Rightarrow \Delta l = \left(\frac{F'}{3AY}\right)l \quad \ldots(\mathrm{ii})$
8. From equation (i) & (ii),
9. $\Delta l = \left(\frac{F}{AY}\right)3l = \left(\frac{F'}{3AY}\right)l$
10. $\Rightarrow \boxed{F' = 9F}$

**Solved independently** (answer withheld)

1. Same volume: $A l_1 = 3A\, l_2 \Rightarrow l_2 = \frac{l_1}{3}$.
2. From Young's modulus, $F = \frac{Y A\, \Delta l}{l}$, so for the first wire $F = \frac{Y A\, \Delta l}{l_1}$.
3. For the second wire, $F_2 = \frac{Y (3A)\, \Delta l}{l_1/3} = 9\frac{Y A\, \Delta l}{l_1}$.
4. $F_2 = 9F$, which is option $3$.

**Subtopic:** Determination of Young's Modulus · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q044_af9adc2a_27102026.png?v=af9adc2a55a6)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q044_670bf5b7_27102026.png?v=670bf5b7f49f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** In $F = YA\Delta l/l$ the geometry enters as $A/l$, and at fixed volume the length falls as the area rises, so the force for a given extension scales as the square of the area
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Young's modulus is taken as the whole story - same material, same extension, so the same force - and the $A/l$ factor in $F = YA\Delta l/l$ never gets used.
- **Why:** This question requires finding the factor by which the stretching force changes when the cross-section changes at fixed volume, demonstrated by 'how much force is needed to stretch the socond wire by the same amount?'
- **Note:** Our record prints 'socond' for 'second' in the stem; it is a spelling slip that does not touch the physics or the key, and the question is tagged as printed. Two fillers were awarded only after checking all the factor combinations the stem supplies (3, 1/3, 9), none of which yields 4 or 6.
<!--/ecat-->

## Q45

Physics · Thermodynamics

A sample of $0.1\,\mathrm{g}$ of water at $100^\circ\mathrm{C}$ and normal pressure ($1.013 \times 10^{5}\,\mathrm{N\,m^{-2}}$) requires $54\,\mathrm{cal}$ of heat energy to convert to steam at $100^\circ\mathrm{C}$. If the volume of the steam produced is $167.1\,\mathrm{cc}$, the change in internal energy of the sample, is

- (1) $42.2\,\mathrm{J}$
- **(2)** $208.7\,\mathrm{J}$
- (3) $104.3\,\mathrm{J}$
- (4) $84.5\,\mathrm{J}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\Delta Q = \Delta U + \Delta W$
2. $\Rightarrow\ 54 \times 4.18 = \Delta U + 1.013 \times 10^{5}(167.1 \times 10^{-6} - 0)$
3. $\Rightarrow\ \Delta U = 208.7\,\mathrm{J}$

**Solved independently** (answer withheld)

1. Convert the heat supplied: $Q = 54\,\mathrm{cal} \times 4.18\,\mathrm{J/cal} \approx 225.7\,\mathrm{J}$.
2. Volume change: $\Delta V = 167.1\,\mathrm{cc} - 0.1\,\mathrm{cc} = 167.0\,\mathrm{cc} = 1.670 \times 10^{-4}\,\mathrm{m^3}$ (0.1 g of water occupies 0.1 cc).
3. Work done by the sample: $W = P\Delta V = 1.013 \times 10^{5} \times 1.670 \times 10^{-4} \approx 16.9\,\mathrm{J}$.
4. First law: $\Delta U = Q - W \approx 225.7 - 16.9 = 208.8\,\mathrm{J}$.
5. This matches $208.7\,\mathrm{J}$, which is option $2$.

**Subtopic:** Heat, Internal Energy, and Work · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q045_37614542_27102026.png?v=37614542f590)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q045_ff587820_27102026.png?v=ff587820015d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The first law splits the latent heat of vaporisation: part of it pushes the atmosphere back through $P\Delta V$ and the remainder raises the internal energy
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Worked every single misstep this problem admits and none of them is printed: leaving the work out gives $\Delta U = Q = 225.7$ J, reversing its sign gives $Q+W = 242.6$ J, and leaving the heat in calories gives $54 - 16.9 = 37.1$ J. The three wrong options sit at $208.7/2 = 104.3$ J, at 84.5 J and at $84.5/2 = 42.2$ J, which is a doubling spread around the key rather than the output of any route.
- **Why:** This question requires computing an internal-energy change from the heat supplied and the work of expansion, demonstrated by 'requires $54\,\mathrm{cal}$ of heat energy' and 'the volume of the steam produced is $167.1\,\mathrm{cc}$' feeding 'the change in internal energy of the sample, is'.
- **Note:** Three fillers on one question is unusual, so the search was repeated: the errors this relation admits - omitting $P\Delta V$, adding it instead of subtracting, and skipping the calorie-to-joule conversion - give 225.7 J, 242.6 J and 37.1 J, none of which is among the options. The wrong options are instead a times-two spread (42.2 and 84.5, 104.3 and 208.7), so no_trap is recorded as the finding rather than a label being forced onto a number with no route.
<!--/ecat-->

## Q46

Chemistry · physical · Redox Reactions

The correct order of N-compounds in its decreasing order of oxidation states is

- (1) $\mathrm{HNO_3}$, $\mathrm{NH_4Cl}$, $\mathrm{NO}$, $\mathrm{N_2}$
- (2) $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{NH_4Cl}$, $\mathrm{N_2}$
- **(3)** $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{N_2}$, $\mathrm{NH_4Cl}$
- (4) $\mathrm{NH_4Cl}$, $\mathrm{N_2}$, $\mathrm{NO}$, $\mathrm{HNO_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{H}\overset{+5}{\mathrm{N}}\mathrm{O_3}$ , $\overset{+2}{\mathrm{N}}\mathrm{O}$, $\overset{0}{\mathrm{N}}\mathrm{_2}$, $\overset{-3}{\mathrm{N}}\mathrm{H_4Cl}$
2. Hence, the correct option is (3).

**Solved independently** (answer withheld)

1. In $\mathrm{HNO_3}$: $(+1) + x + 3(-2) = 0 \Rightarrow x = +5$.
2. In $\mathrm{NO}$: $x + (-2) = 0 \Rightarrow x = +2$.
3. In $\mathrm{N_2}$ (element): $x = 0$.
4. In $\mathrm{NH_4Cl}$: $x + 4(+1) + (-1) = 0 \Rightarrow x = -3$.
5. Decreasing order $+5 > +2 > 0 > -3$: $\mathrm{HNO_3}, \mathrm{NO}, \mathrm{N_2}, \mathrm{NH_4Cl}$, which is option $3$.

**Subtopic:** Oxidation Number · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q046_a65fb85c_27102026.png?v=a65fb85ca57a)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q046_ce3edd62_27102026.png?v=ce3edd62db98)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Oxidation number of nitrogen from the sum-of-states rule, then ranked on the signed value: +5 in HNO3, +2 in NO, 0 in N2, -3 in NH4Cl
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Option 4 holds the same four species in increasing order, so a student who assigns $+5$, $+2$, $0$, $-3$ correctly and then writes the sorted list upward from the most reduced species lands on it, while the stem asked for the decreasing order.
- **Why:** This question requires nitrogen's oxidation number in four species to be computed and then placed in the sequence the stem names, demonstrated by 'decreasing order of oxidation states' with every option printed as a full four-term ordering.
- **Note:** E1_question_type is arrange_in_order, which has no counterpart on the current qtype axis; the printed shape is one question with four answers, so qtype is mcq and the ordering is carried by asks: order.
<!--/ecat-->

## Q47

Chemistry · inorganic · The p–Block Elements

Which one of the following elements is unable to form $\mathrm{MF_6^{3-}}$ ion?

- **(1)** $\mathrm{B}$
- (2) $\mathrm{Al}$
- (3) $\mathrm{Ga}$
- (4) $\mathrm{In}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\because$ '$\mathrm{B}$' has no vacant $d$-orbitals in its valence shell, so it can't extend its covalency beyond $4$.
2. i.e. '$\mathrm{B}$' cannot form the ion like $\mathrm{MF_6^{3(-)}}$ i.e. $\mathrm{BF_6^{3(-)}}$.
3. Hence, the correct option is (1).

**Solved independently** (answer withheld)

1. Boron is in period 2, so it has only $2s$ and $2p$ orbitals and no $d$ orbitals; its maximum covalency is $4$ (as in $\mathrm{[BF_4]^-}$), so it cannot form $\mathrm{BF_6^{3-}}$, while $\mathrm{Al}$, $\mathrm{Ga}$ and $\mathrm{In}$ have $d$ orbitals available and can form $\mathrm{MF_6^{3-}}$, which makes the answer option $1$.

**Subtopic:** Anomalous behaviour of Boron & Diagonal Relationship (B–Si) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q047_7e18aa3d_27102026.png?v=7e18aa3dbe21)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q047_6ff0b641_27102026.png?v=6ff0b641fc80)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Boron's valence shell has no d orbitals, so its maximum covalence is four: BF4- exists and BF6^3- cannot, while Al, Ga and In reach six
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  A student who holds the inert-pair line for the bottom of group 13 reads 'unable to form $\mathrm{MF_6^{3-}}$' as 'unwilling to be $+3$' and picks In, the heavy member that discussion is printed around; the ion fails only where there are too few orbitals, which is boron.
- **Why:** This question requires the stated limit on boron's covalence, demonstrated by the four options being the lighter group-13 elements and the species printed as '$\mathrm{MF_6^{3-}}$', which only a metal with six usable orbitals can form.
<!--/ecat-->

## Q48

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Considering Ellingham diagram, which of the following metals can be used to reduce alumina?

- **(1)** $\mathrm{Mg}$
- (2) $\mathrm{Zn}$
- (3) $\mathrm{Fe}$
- (4) $\mathrm{Cu}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The metal which is more reactive than '$\mathrm{Al}$' can reduce alumina i.e. '$\mathrm{Mg}$' should be the correct option.

**Solved independently** (answer withheld)

1. A metal reduces another metal's oxide when its own oxide line on the Ellingham diagram lies below that oxide's line, giving $\Delta_r G^\circ < 0$ for the coupled reaction.
2. The $\mathrm{MgO}$ line lies below the $\mathrm{Al_2O_3}$ line, so $3\mathrm{Mg} + \mathrm{Al_2O_3} \rightarrow 3\mathrm{MgO} + 2\mathrm{Al}$ has $\Delta_r G^\circ < 0$.
3. The $\mathrm{ZnO}$, $\mathrm{FeO}$ and $\mathrm{Cu_2O}$ lines lie above $\mathrm{Al_2O_3}$, so $\mathrm{Zn}$, $\mathrm{Fe}$ and $\mathrm{Cu}$ cannot reduce alumina; the answer is option $1$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q048_6c0eb00d_27102026.png?v=6c0eb00dd583)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q048_274e91b5_27102026.png?v=274e91b5a7d1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** On an Ellingham diagram one metal reduces another's oxide only when its own oxide line lies lower; MgO's line lies below that of Al2O3, so magnesium reduces alumina
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Zinc is the reducing agent the same metallurgy chapter names, displacing silver and gold from their cyanide complexes, so a student carrying 'Zn reduces metal compounds' ticks it without checking where ZnO's line sits against $\mathrm{Al_2O_3}$'s.
- **Why:** This question requires the Ellingham criterion applied to four candidate metals, demonstrated by 'Considering Ellingham diagram, which of the following metals can be used to reduce alumina'.
<!--/ecat-->

## Q49

Chemistry · inorganic · The p–Block Elements

The correct order of atomic radii in group 13 elements is

- (1) $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{Tl} < \mathrm{In}$
- (2) $\mathrm{B} < \mathrm{Al} < \mathrm{Ga} < \mathrm{In} < \mathrm{Tl}$
- (3) $\mathrm{B} < \mathrm{Al} < \mathrm{In} < \mathrm{Ga} < \mathrm{Tl}$
- **(4)** $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{Tl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\begin{array}{|l|c|c|c|c|c|}\hline \text{Elements} & \mathrm{B} & \mathrm{Ga} & \mathrm{Al} & \mathrm{In} & \mathrm{Tl} \\ \hline \text{Atomic radii (pm)} & 85 & 135 & 143 & 167 & 170 \\ \hline \end{array}$

**Solved independently** (answer withheld)

1. Down group 13 the atomic radius generally increases as new shells are added.
2. Ga comes after the 3d series, and the 10 poorly shielding $3d$ electrons raise $Z_{\text{eff}}$, so $r_{\mathrm{Ga}}\,(135\,\text{pm}) < r_{\mathrm{Al}}\,(143\,\text{pm})$.
3. In and Tl are larger still: $r_{\mathrm{In}} = 167\,\text{pm} < r_{\mathrm{Tl}} = 170\,\text{pm}$.
4. Order: $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{Tl}$, which is option $4$.

**Subtopic:** General properties & Trends of Group 13 (Boron Family) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q049_73845aae_27102026.png?v=73845aae5377)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q049_061132ab_27102026.png?v=061132abce8f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Atomic radius in group 13 is not monotonic: the d-block contraction leaves Ga smaller than Al, so the order is B < Ga < Al < In < Tl
- **Trap:** **New trap (proposed)** (`new_trap`) — a way of catching a student that none of the above describes — option 2  
  Option 2 is the group trend with no break in it, which is what a student writes who holds 'atomic radius increases down a group' and applies it straight to B, Al, Ga, In, Tl; group 13 is the group where that increase fails once, at Al to Ga.
- **Proposed:** `ignores_exception` — the option is exactly what the general rule gives, and the question is built on the one place the series breaks. condition_missed was ruled out because no condition is printed in the stem for the rule to be applied outside - the rulebook's own tie-break puts a printed condition under condition_missed and a remembered exception elsewhere. formula_misused was ruled out because the trend is remembered correctly, not misremembered or swapped for another relation; what fails is its reach. half_right was ruled out because the failure is not a part of a compound claim but the application of a rule where it does not hold.
- **Why:** This question requires the break in the group-13 radius series to be known and placed, demonstrated by option 4 and option 2 differing only in whether Ga comes before or after Al.
- **Note:** E1_question_type is arrange_in_order, which the current qtype axis does not carry; the printed shape is a plain question with four answers, so qtype is mcq with asks: order.
<!--/ecat-->

## Q50

Chemistry · inorganic · The p–Block Elements

> ⚠ The independent solve chose (3); the booklet prints (1).

Which of the following statements is not true for halogens?

- **(1)** All but fluorine show positive oxidation states
- (2) All are oxidizing agents
- (3) All form monobasic oxyacids
- (4) Chlorine has the highest electron-gain enthalpy

**Answer** — booklet: (1) · independent solve: (3) · differs

**Publisher's solution**

1. Due to high electronegativity and small size, $\mathrm{F}$ forms only one oxoacid, $\mathrm{HOF}$ known as Fluoric (I) acid.
2. Oxidation number of $\mathrm{F}$ is $+1$ in $\mathrm{HOF}$.

**Solved independently** (answer withheld)

1. Fluorine, the most electronegative element, shows only the $-1$ state; Cl, Br, I also show $+1, +3, +5, +7$, so statement 1 is true.
2. Halogens readily accept electrons ($X_2 + 2e^- \rightarrow 2X^-$), so all are oxidising agents and statement 2 is true.
3. Iodine forms $\mathrm{H_5IO_6}$ (orthoperiodic acid), which is polybasic, so not all halogen oxyacids are monobasic and statement 3 is false.
4. Electron-gain enthalpy is most negative for Cl ($-349\,\mathrm{kJ\,mol^{-1}}$), not F, because F is small and has strong electron repulsion, so statement 4 is true.
5. The statement that is not true is option $3$.

**Subtopic:** General Properties & Trends of Group 17 (Halogens) · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q050_d228dcf3_27102026.png?v=d228dcf36723)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q050_0e8f4ccb_27102026.png?v=0e8f4ccba323)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Halogen group properties as NCERT states them, including the fluorine exception: fluorine's one oxoacid HOF is named fluoric(I) acid, so the claim that only fluorine lacks a positive oxidation state is the one that fails
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Fluorine holds the maximum of the neighbouring property, electronegativity, so a student who carries 'fluorine is top of every electron-attracting property' judges the chlorine claim untrue and ticks it; electron gain enthalpy is the one property whose maximum sits on chlorine, not fluorine.
- **Why:** This question requires four printed claims about halogens to be graded against the chapter's own lines, demonstrated by 'Which of the following statements is not true for halogens?' with each option a complete claim.
- **Note:** The key rests on fluorine's single oxoacid being named fluoric(I) acid, i.e. on crediting fluorine with a positive state in HOF; read as plain oxidation-number arithmetic (H +1, F -1, O 0) option 1 would be true. Tagged as printed, with that basis recorded rather than re-judged.
<!--/ecat-->

## Q51

Chemistry · inorganic · Chemical Bonding and Molecular Structure

In the structure of $\mathrm{ClF_3}$, the number of lone pair of electrons on central atom ‘Cl’ is

- (1) Four
- **(2)** Two
- (3) One
- (4) Three

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The structure of $\mathrm{ClF_3}$ is

![printed figure: Lewis/VSEPR diagram of chlorine trifluoride ($\ce{ClF3}$): central Cl single-bonded to three F atoms (one left, one up, one down), two lone-pair orbital lobes (each with paired arrows) drawn on Cl to the right, and three lone pairs drawn as dots on each F](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q051_sol_1_860a4abd_29102026.svg?v=860a4abd2bb7)

*Lewis/VSEPR diagram of chlorine trifluoride ($\ce{ClF3}$): central Cl single-bonded to three F atoms (one left, one up, one down), two lone-pair orbital lobes (each with paired arrows) drawn on Cl to the right, and three lone pairs drawn as dots on each F*

2. The number of lone pair of electrons on central $\mathrm{Cl}$ is $2$.

**Solved independently** (answer withheld)

1. Chlorine (group 17) has $7$ valence electrons.
2. Three electrons form three $\mathrm{Cl-F}$ bond pairs.
3. Remaining electrons $= 7 - 3 = 4$, i.e. $\frac{4}{2} = 2$ lone pairs on Cl (5 electron pairs, $sp^3d$, T-shaped), which is option $2$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q051_a0a5d48f_27102026.png?v=a0a5d48f61fa)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q051_7ee5fb9c_27102026.png?v=7ee5fb9ceb27)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Lone pairs on a central atom from the valence count: chlorine's seven electrons less the three used in Cl-F bonds leave four non-bonding electrons, that is two lone pairs, giving the T-shaped AX3E2 arrangement
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Four is exactly the count of non-bonding electrons, $7-3=4$, so a student who does the valence bookkeeping right and then reports electrons where the stem asked for pairs reads off Four instead of halving it to Two.
- **Why:** This question requires the valence-electron count applied to the named central atom, demonstrated by 'the number of lone pair of electrons on central atom Cl' with the options being bare counts.
<!--/ecat-->

## Q52

Chemistry · organic · Alcohols, Phenols and Ethers

Identify the major products P, Q and R in the following sequence of reactions:

![printed figure: benzene + $\ce{CH3CH2CH2Cl}$ →(Anhydrous $\ce{AlCl3}$); P →((i) $\ce{O2}$, (ii) $\ce{H3O+}$/Δ) Q + R](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q052_d04c63e7_29102026.svg?v=d04c63e71887)

*benzene + $\ce{CH3CH2CH2Cl}$ →[Anhydrous $\ce{AlCl3}$]; P →[(i) $\ce{O2}$, (ii) $\ce{H3O+}$/Δ] Q + R*

Structures: benzene `c1ccccc1`; 1-chloropropane `CCCCl`

- (1) (propan-2-yl)benzene `CC(C)c1ccccc1`; phenol `Oc1ccccc1`; propan-2-ol `CC(C)O`
- (2) propylbenzene `CCCc1ccccc1`; benzaldehyde `O=Cc1ccccc1`; benzoic acid `O=C(O)c1ccccc1`
- (3) propylbenzene `CCCc1ccccc1`; benzaldehyde `O=Cc1ccccc1`; ethanol `CCO`
- **(4)** (propan-2-yl)benzene `CC(C)c1ccccc1`; phenol `Oc1ccccc1`; propan-2-one `CC(C)=O`

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: $\ce{CH3CH2CH2-Cl}$ + aluminium trichloride → $\ce{CH3CH2CH2^{δ+}...Cl...AlCl3^{δ-}}$ (Incipient carbocation); (Incipient carbocation) →(1, 2–H Shift) $\ce{CH3-CH^{δ+}-CH3}$ with Cl...$\ce{AlCl3^{δ-}}$](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q052_sol_1_7c3b0354_27102026.svg?v=7c3b03541623)

*$\ce{CH3CH2CH2-Cl}$ + aluminium trichloride → $\ce{CH3CH2CH2^{δ+}...Cl...AlCl3^{δ-}}$ (Incipient carbocation); (Incipient carbocation) →[1, 2–H Shift] $\ce{CH3-CH^{δ+}-CH3}$ with Cl...$\ce{AlCl3^{δ-}}$*

1. Now,

![printed figure: benzene →($\ce{CH3-CH^+-CH3}$) (propan-2-yl)benzene (P); (P) →($\ce{O2}$) 2-phenylpropan-2-yl hydroperoxide; 2-phenylpropan-2-yl hydroperoxide →($\ce{H+/H2O}$, Hydroperoxide Rearrangement) propan-2-one (R) + phenol (Q)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q052_sol_2_aecf54be_29102026.svg?v=aecf54be798a)

*benzene →[$\ce{CH3-CH^+-CH3}$] (propan-2-yl)benzene (P); (P) →[$\ce{O2}$] 2-phenylpropan-2-yl hydroperoxide; 2-phenylpropan-2-yl hydroperoxide →[$\ce{H+/H2O}$, Hydroperoxide Rearrangement] propan-2-one (R) + phenol (Q)*


**Solved independently** (answer withheld)

1. $\mathrm{CH_3CH_2CH_2Cl + AlCl_3 \rightarrow CH_3CH_2CH_2^+ + AlCl_4^-}$.
2. A 1,2-hydride shift converts the primary carbocation to the more stable secondary one: $\mathrm{CH_3CH_2CH_2^+ \rightarrow (CH_3)_2CH^+}$.
3. Electrophilic substitution on benzene gives cumene: $\mathrm{C_6H_6 + (CH_3)_2CH^+ \rightarrow C_6H_5CH(CH_3)_2}$ = P.
4. Air oxidation of P gives cumene hydroperoxide: $\mathrm{C_6H_5CH(CH_3)_2 + O_2 \rightarrow C_6H_5C(CH_3)_2OOH}$.
5. Acid hydrolysis with heat: $\mathrm{C_6H_5C(CH_3)_2OOH \xrightarrow{H_3O^+/\Delta} C_6H_5OH + CH_3COCH_3}$, so Q = phenol and R = acetone, which is option $4$.

**Subtopic:** Preparation of Phenols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q052_77de09b2_27102026.png?v=77de09b2657d)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q052_5da3432e_27102026.png?v=5da3432e8203)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Friedel-Crafts alkylation with a primary halide rearranges to the isopropyl cation, so benzene gives cumene, and cumene with $\mathrm{O_2}$ then $\mathrm{H_3O^+}$ gives phenol plus acetone
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  all four `options_en` values are empty strings in this packet and no option figure was supplied, so no printed wrong option exists to test a route against
- **Why:** This question requires the products of a two-step named route, demonstrated by the scheme printing "Anhydrous AlCl3" over the first arrow and "(i) O2, (ii) H3O+/Delta" over the second with products Q + R.
- **Note:** The options were not supplied to this step: options_en holds four empty strings and figure_image carries only the question scheme (shows: question). The printed paper almost certainly draws structures there, so this is a reach limit of this packet, not evidence that the paper is faulty, and no trap is asserted. A reviewer holding the printed options should check for a set built on P = n-propylbenzene, i.e. the primary propyl cation used without the hydride shift to isopropyl, which would carry Q and R to a cresol-type pair instead of phenol + acetone. E1's pattern returned arrange_in_order, fired by the words "sequence of reactions"; nothing is to be put in order here, and the stem asks for P, Q and R together, which is the multi-part shape recorded as two_part.
<!--/ecat-->

## Q53

Chemistry · organic · Biomolecules

Which of the following compounds can form a zwitterion?

- (1) Benzoic acid
- (2) Acetanilide
- (3) Aniline
- **(4)** Glycine

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\underset{\substack{\downarrow \\ \mathrm{p}K_a\,=\,9.60}}{\mathrm{H_3\overset{\oplus}{N}}}\mathrm{-CH_2-}\underset{\substack{\downarrow \\ \mathrm{p}K_a\,=\,2.34}}{\mathrm{COOH}} \rightleftharpoons \mathrm{H_3\overset{\oplus}{N}-CH_2-COO^{-}}$ (Zwitterion form)
2. $\rightleftharpoons \mathrm{H_2N-CH_2-COO^{-}}$

**Solved independently** (answer withheld)

1. A zwitterion needs both an acidic group and a basic group in the same molecule, so an internal proton transfer can occur.
2. Glycine $\mathrm{H_2N{-}CH_2{-}COOH}$ has both, giving $\mathrm{H_3\overset{+}{N}{-}CH_2{-}COO^-}$; benzoic acid has only $\mathrm{-COOH}$, aniline only $\mathrm{-NH_2}$, and acetanilide only a non-basic amide $\mathrm{-NHCOCH_3}$, so the answer is option $4$.

**Subtopic:** Proteins Classification and Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q053_18ab1b1f_27102026.png?v=18ab1b1fb2cb)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q053_84352b1d_27102026.png?v=84352b1d441a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A zwitterion needs an acidic and a basic group in the SAME molecule, which is why amino acids such as glycine carry $\mathrm{-NH_3^+}$ and $\mathrm{-COO^-}$ together
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The $\mathrm{-COOH}$ group is the half of glycine that gives up the proton, so whoever holds "the zwitterion comes from the carboxyl group" picks the one carboxylic acid on the page; benzoic acid has nothing to catch that proton
- **Why:** This question requires the stated fact that an amino acid carries an acidic and a basic group in one molecule, demonstrated by the options being four unlike compounds of which only glycine is an amino acid.
<!--/ecat-->

## Q54

Chemistry · organic · Polymers

Regarding cross-linked or network polymers, which of the following statements is incorrect?

- (1) Examples are bakelite and melamine.
- (2) They are formed from bi- and tri-functional monomers.
- (3) They contain covalent bonds between various linear polymer chains.
- **(4)** They contain strong covalents bonds in their polymer chains.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Cross linked or network polymers are formed from bi-functional and tri-functional monomers and contain strong covalent bonds between various linear polymer chains, e.g. bakelite, melamine etc.
2. Option (4) is not related to cross-linking.
3. So option (4) should be the correct option.

**Solved independently** (answer withheld)

1. NCERT: cross-linked (network) polymers are formed from bi-functional and tri-functional monomers, so option $2$ is correct.
2. They contain strong covalent bonds between various linear polymer chains, so option $3$ is correct.
3. Bakelite and melamine are the NCERT examples, so option $1$ is correct.
4. Option $4$ puts the strong covalent bonds within the chains instead of between them, which misstates the feature that defines the class, so the incorrect statement is option $4$.

**Subtopic:** Classification of Polymers Based on Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q054_7d12d855_27102026.png?v=7d12d855e42e)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q054_d85bca63_27102026.png?v=d85bca63d094)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What defines a cross-linked or network polymer is covalent bonds BETWEEN the linear chains, not covalent bonds along a chain, which every polymer has
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Option 3 is NCERT's own sentence about network polymers, and once the phrase "strong covalent bonds" has been recognised in option 4 as the remembered line, the hunt for the incorrect statement moves to the only other bonding claim on the page
- **Why:** This question requires the stated defining feature of a network polymer, demonstrated by option 3 reading "covalent bonds between various linear polymer chains" against option 4's "in their polymer chains".
<!--/ecat-->

## Q55

Chemistry · organic · Amines

Nitration of aniline in strong acidic medium also gives m-nitroaniline because

- (1) In absence of substituents nitro group always goes to m-position.
- (2) In electrophilic substitution reactions amino group is meta directive.
- (3) Inspite of substituents nitro group always goes to only m-position.
- **(4)** In acidic (strong) medium aniline is present as anilinium ion.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: aniline ⇌($\ce{H+}$) anilinium ion (Anilinium ion)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q055_sol_1_5dcfe9d4_27102026.svg?v=5dcfe9d47720)

*aniline ⇌[$\ce{H+}$] anilinium ion (Anilinium ion)*

![drawn: aniline ⇌($\ce{H+}$) anilinium ion (Anilinium ion)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q055_solution_1_27c89e90_27102026.svg?v=27c89e90139d)  
*drawn on the booklet's geometry, checked against its SMILES*

1. $-\overset{\oplus}{\mathrm{N}}\mathrm{H_3}$ is m-directing, hence besides para ($51\%$) and ortho ($2\%$), meta product ($47\%$) is also formed in significant yield.

**Solved independently** (answer withheld)

1. In strong acid (conc. $HNO_3 + H_2SO_4$) aniline is protonated: $C_6H_5NH_2 + H^+ \rightarrow C_6H_5NH_3^+$.
2. The $-NH_3^+$ group of the anilinium ion is electron-withdrawing and meta-directing, so nitration of it gives m-nitroaniline, which is option $4$.

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q055_17de449f_27102026.png?v=17de449f4d9b)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q055_bfe778b3_27102026.png?v=bfe778b3ba9e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In strong acid aniline is protonated to the anilinium ion, and $\mathrm{-NH_3^+}$ is an electron-withdrawing, meta-directing group although $\mathrm{-NH_2}$ is ortho/para directing
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The meta product is printed in the stem as a fact, so reading the directing effect straight off it gives "the amino group must be meta directive"; the meta direction belongs to the anilinium ion that the acid creates, not to the amino group
- **Why:** This question requires the reason the textbook gives for the meta product, demonstrated by the stem's trailing "because" after "in strong acidic medium".
- **Note:** On the nearby_fact versus look_alike_term test: "amino group" and "anilinium ion" do share a root, but swapping them for two unlike names leaves the pull intact, because what carries the student is the meta product granted in the stem rather than the resemblance of the words. Position of the fact, not likeness, so nearby_fact. E1 returned statement_options; the stem is a trailing "because" with no lettered block, so the live axis records mcq.
<!--/ecat-->

## Q56

Chemistry · organic · Biomolecules

The difference between amylose and amylopectin is

- (1) Amylopectin have $1 \rightarrow 4$ $\alpha$-linkage and $1 \rightarrow 6$ $\beta$-linkage
- (2) Amylose have $1 \rightarrow 4$ $\alpha$-linkage and $1 \rightarrow 6$ $\beta$-linkage
- **(3)** Amylopectin have $1 \rightarrow 4$ $\alpha$-linkage and $1 \rightarrow 6$ $\alpha$-linkage
- (4) Amylose is made up of glucose and galactose

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Amylose and Amylopectin are polymers of $\alpha$-D-glucose, so $\beta$-link is not possible.
2. Amylose is linear with $1 \rightarrow 4$ $\alpha$-linkage whereas Amylopectin is branched and has both $1 \rightarrow 4$ and $1 \rightarrow 6$ $\alpha$-linkages.
3. So option (3) should be the correct option.

**Solved independently** (answer withheld)

1. Amylose and amylopectin are both starch polymers of $\alpha$-D-glucose only, so option $4$ (glucose and galactose) is false.
2. Amylose is an unbranched chain joined by $\alpha(1 \rightarrow 4)$ glycosidic links, with no $1 \rightarrow 6$ linkage, so option $2$ is false.
3. Amylopectin has $\alpha(1 \rightarrow 4)$ chains with branches joined by $\alpha(1 \rightarrow 6)$ links, not $\beta$, so option $1$ is false and option $3$ is correct.

**Subtopic:** Polysaccharides · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 14)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q056_dfefb871_27102026.png?v=dfefb8710d12)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q056_0d4c2869_27102026.png?v=0d4c2869de36)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Both starch fractions are glucose polymers; amylose is linear with $\alpha$-1,4 links only, while amylopectin adds $\alpha$-1,6 links at its branch points
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  It names the right polymer and the right pair of linkage positions and then calls the branch link $\beta$, which is the one word that fails; nothing in the branched-polymer picture says which anomeric form the branch uses
- **Why:** This question requires telling two look-alike starch fractions apart by their linkages, demonstrated by the stem "The difference between amylose and amylopectin is" and by three options differing only in polymer name and Greek letter.
- **Note:** E1 returned null with the comment that the options are reactions; they are not - all four are prose claims about linkages, so the shape is a plain completion mcq.
<!--/ecat-->

## Q57

Chemistry · physical · Basic Concepts of Chemistry

A mixture of $2.3\,\mathrm{g}$ formic acid and $4.5\,\mathrm{g}$ oxalic acid is treated with conc. $\mathrm{H_2SO_4}$. The evolved gaseous mixture is passed through $\mathrm{KOH}$ pellets. Weight (in g) of the remaining product at STP will be

- **(1)** $2.8$
- (2) $3.0$
- (3) $1.4$
- (4) $4.4$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\underset{2.3\,\mathrm{g}\text{ or }\left(\frac{1}{20}\,\mathrm{mol}\right)}{\mathrm{HCOOH}} \xrightarrow{\mathrm{Conc.\,H_2SO_4}} \underset{\frac{1}{20}\,\mathrm{mol}}{\mathrm{CO(g)}} + \mathrm{H_2O(l)}$
2. $\underset{4.5\,\mathrm{g}\text{ or }\left(\frac{1}{20}\,\mathrm{mol}\right)}{\begin{array}{c}\mathrm{COOH}\\ |\\ \mathrm{COOH}\end{array}} \xrightarrow{\mathrm{Conc.\,H_2SO_4}} \underset{\frac{1}{20}\,\mathrm{mol}}{\mathrm{CO(g)}} + \underset{\frac{1}{20}\,\mathrm{mol}}{\mathrm{CO_2\,(g)}} + \mathrm{H_2O(l)}$
3. Gaseous mixture formed is $\mathrm{CO}$ and $\mathrm{CO_2}$ when it is passed through $\mathrm{KOH}$, only $\mathrm{CO_2}$ is absorbed. So the remaining gas is $\mathrm{CO}$.
4. So, weight of remaining gaseous product $\mathrm{CO}$ is
5. $\frac{2}{20} \times 28 = 2.8\,\mathrm{g}$
6. So, the correct option is (1)

**Solved independently** (answer withheld)

1. $n_{\mathrm{HCOOH}} = \frac{2.3}{46} = 0.05\,\mathrm{mol}$.
2. $\mathrm{HCOOH} \xrightarrow{\text{conc. } \mathrm{H_2SO_4}} \mathrm{CO} + \mathrm{H_2O}$, giving $0.05\,\mathrm{mol}$ CO.
3. $n_{\mathrm{(COOH)_2}} = \frac{4.5}{90} = 0.05\,\mathrm{mol}$.
4. $\mathrm{(COOH)_2} \xrightarrow{\text{conc. } \mathrm{H_2SO_4}} \mathrm{CO} + \mathrm{CO_2} + \mathrm{H_2O}$, giving $0.05\,\mathrm{mol}$ CO and $0.05\,\mathrm{mol}$ $\mathrm{CO_2}$.
5. KOH pellets absorb $\mathrm{CO_2}$ (and moisture), so only CO remains: $0.05 + 0.05 = 0.10\,\mathrm{mol}$.
6. $m_{\mathrm{CO}} = 0.10 \times 28 = 2.8\,\mathrm{g}$, which is option $1$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q057_1778f0f0_27102026.png?v=1778f0f01a79)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q057_6875f2c3_27102026.png?v=6875f2c344dd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Conc. $\mathrm{H_2SO_4}$ dehydrates formic acid to CO and oxalic acid to CO + $\mathrm{CO_2}$, and KOH absorbs only the acidic gas $\mathrm{CO_2}$, so the CO from both acids survives
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Counting the CO from the $2.3\,\mathrm{g}$ of formic acid alone gives $0.05 \times 28 = 1.4\,\mathrm{g}$; the oxalic acid is written off as the $\mathrm{CO_2}$ source and its equal $0.05\,\mathrm{mol}$ of CO is never added
- **Why:** This question requires computing a mass from two dehydration equations and a gas-absorption step, demonstrated by the stem giving $2.3\,\mathrm{g}$ and $4.5\,\mathrm{g}$ and asking for the "Weight (in g) of the remaining product".
- **Note:** The stem's "at STP" is idle: a mass is asked for, not a volume. Tagged as printed.
<!--/ecat-->

## Q58

Chemistry · inorganic · The s-Block Elements

Which of the following oxides is most acidic in nature?

- (1) $\mathrm{BaO}$
- **(2)** $\mathrm{BeO}$
- (3) $\mathrm{MgO}$
- (4) $\mathrm{CaO}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{BeO} < \mathrm{MgO} < \mathrm{CaO} < \mathrm{BaO}$
2. $\xrightarrow{\hspace{6em}}$ Basic character increases.
3. So, the most acidic should be $\mathrm{BeO}$.
4. In fact, $\mathrm{BeO}$ is amphoteric oxide while other given oxides are basic.

**Solved independently** (answer withheld)

1. Group 2 oxides become more basic down the group: $\mathrm{BeO} < \mathrm{MgO} < \mathrm{CaO} < \mathrm{BaO}$.
2. $\mathrm{BeO}$ is amphoteric (small, highly polarising $\mathrm{Be^{2+}}$ gives covalent character), while the others are basic, so $\mathrm{BeO}$ is the most acidic, option $2$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q058_f9c7f4f7_27102026.png?v=f9c7f4f7f9ae)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q058_75643f60_27102026.png?v=75643f603590)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Across group 2 the oxides run from amphoteric BeO to strongly basic BaO, because the smaller, more polarising cation makes its oxide more acidic
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  A student carrying the group-2 trend as one sentence, 'basic character increases down the group', flips it into 'acidic character increases down the group' and takes the bottom member BaO; BaO is in fact the most basic of the four and it is the top member BeO that is amphoteric.
- **Why:** This question requires four oxides of one group to be ranked on acidity by cation size and polarising power, demonstrated by 'most acidic in nature' set against BaO, BeO, MgO and CaO.
<!--/ecat-->

## Q59

Chemistry · inorganic · Environmental Chemistry

Which oxide of nitrogen is not a common pollutant introduced into the atmosphere both due to natural and human activity?

- (1) $\mathrm{N_2O}$
- (2) $\mathrm{NO_2}$
- **(3)** $\mathrm{N_2O_5}$
- (4) $\mathrm{NO}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Fact

**Solved independently** (answer withheld)

1. $\mathrm{NO}$ and $\mathrm{NO_2}$ form from $\mathrm{N_2}$ and $\mathrm{O_2}$ during lightning (natural) and high-temperature combustion in engines (human), so they are common pollutants.
2. $\mathrm{N_2O}$ comes from soil microbial action (natural) and fertiliser use and combustion (human), so it is also a common pollutant.
3. $\mathrm{N_2O_5}$ is not released as a common pollutant by either route, so the answer is option $3$.

**Subtopic:** Air Pollution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q059_09f07ddf_27102026.png?v=09f07ddfc9c9)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q059_c57f5f56_27102026.png?v=c57f5f568155)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The oxides of nitrogen that the air-pollution section lists as entering the atmosphere from both natural and human sources are N2O, NO and NO2; N2O5 is not one of them
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  N2O is met as laughing gas and as a greenhouse gas rather than inside the NOx paragraph on air pollution, so a student hunting for the oxide that is not a common pollutant takes the one whose pollutant role is printed in a different place.
- **Why:** This question requires the stated membership of the taught list of nitrogen oxides that pollute the air from natural and human sources, demonstrated by 'not a common pollutant introduced into the atmosphere both due to natural and human activity'.
- **Note:** Stem is negated (NOT), so each wrong option is a true pollutant; the routes above name what carries a student to one of them rather than to another.
<!--/ecat-->

## Q60

Chemistry · organic · Alcohols, Phenols and Ethers

The compound A on treatment with $\mathrm{Na}$ gives B, and with $\mathrm{PCl_5}$ gives C. B and C react together to give diethyl ether. A, B and C are in the order

- (1) $\mathrm{C_2H_5Cl}$, $\mathrm{C_2H_6}$, $\mathrm{C_2H_5OH}$
- (2) $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5Cl}$, $\mathrm{C_2H_5ONa}$
- (3) $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_6}$, $\mathrm{C_2H_5Cl}$
- **(4)** $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_5Cl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\underset{(\mathrm{A})}{\mathrm{C_2H_5OH}} \xrightarrow{\mathrm{Na}} \underset{(\mathrm{B})}{\mathrm{C_2H_5\overset{-}{O}\,Na^{+}}}$
2. $\underset{(\mathrm{A})}{\mathrm{C_2H_5OH}} \xrightarrow{\mathrm{PCl_5}} \underset{(\mathrm{C})}{\mathrm{C_2H_5Cl}}$
3. $\underset{(\mathrm{B})}{\mathrm{C_2H_5\overset{-}{O}\,Na^{+}}} + \underset{(\mathrm{C})}{\mathrm{C_2H_5Cl}} \xrightarrow{\mathrm{S_N2}} \mathrm{C_2H_5OC_2H_5}$
4. So the correct option is (4)

**Solved independently** (answer withheld)

1. $2\,\mathrm{C_2H_5OH} + 2\,\mathrm{Na} \rightarrow 2\,\mathrm{C_2H_5ONa} + \mathrm{H_2}$, so A is $\mathrm{C_2H_5OH}$ and B is $\mathrm{C_2H_5ONa}$.
2. $\mathrm{C_2H_5OH} + \mathrm{PCl_5} \rightarrow \mathrm{C_2H_5Cl} + \mathrm{POCl_3} + \mathrm{HCl}$, so C is $\mathrm{C_2H_5Cl}$.
3. Williamson synthesis: $\mathrm{C_2H_5ONa} + \mathrm{C_2H_5Cl} \rightarrow \mathrm{C_2H_5OC_2H_5} + \mathrm{NaCl}$, giving diethyl ether.
4. The order A, B, C is $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_5Cl}$, which is option $4$.

**Subtopic:** Preparation of Ethers by Williamson Ether Synthesis, Reactions of Alcohols · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q060_4f0631c9_27102026.png?v=4f0631c9b947)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q060_1aabc500_27102026.png?v=1aabc5002c43)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Williamson ether synthesis: sodium turns ethanol into sodium ethoxide, PCl5 turns it into ethyl chloride, and alkoxide plus halide give diethyl ether
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Ethanol for A and ethyl chloride for C are both right, but 'sodium acting on an organic compound' pulls up the Wurtz reaction and the student writes ethane for B; ethane carries no leaving group and no nucleophile, so it cannot combine with ethyl chloride to give an ether.
- **Why:** This question requires each reagent to be mapped to the species it makes from ethanol and the pairing then read back from the product, demonstrated by 'B and C react together to give diethyl ether'.
- **Note:** Each option is an ordered triple A, B, C accepted or rejected whole, which is why qtype is two_part rather than mcq even though the pattern classifier returned plain_mcq.
<!--/ecat-->

## Q61

Chemistry · organic · Hydrocarbons

The compound $\mathrm{C_7H_8}$ undergoes the following reactions:
$\mathrm{C_7H_8} \xrightarrow{3\mathrm{Cl_2}/\Delta} \mathrm{A} \xrightarrow{\mathrm{Br_2}/\mathrm{Fe}} \mathrm{B} \xrightarrow{\mathrm{Zn/HCl}} \mathrm{C}$
The product 'C' is

- (1) 3-bromo-2,4,6-trichlorotoluene
- (2) o-bromotoluene
- **(3)** m-bromotoluene
- (4) p-bromotoluene

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: toluene ($\ce{C7H8}$) →(3Cl₂, Δ) (trichloromethyl)benzene (A) →(Br₂, Fe) 1-bromo-3-(trichloromethyl)benzene (B); (B) →(Zn, HCl) 1-bromo-3-methylbenzene (C)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q061_sol_1_9181475b_29102026.svg?v=9181475bc614)

*toluene ($\ce{C7H8}$) →[3Cl₂, Δ] (trichloromethyl)benzene (A) →[Br₂, Fe] 1-bromo-3-(trichloromethyl)benzene (B); (B) →[Zn, HCl] 1-bromo-3-methylbenzene (C)*

![drawn: toluene ($\ce{C7H8}$) →(3Cl₂, Δ) (trichloromethyl)benzene (A) →(Br₂, Fe) 1-bromo-3-(trichloromethyl)benzene (B); (B) →(Zn, HCl) 1-bromo-3-methylbenzene (C)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q061_solution_1_3b4775c6_27102026.svg?v=3b4775c623d4)  
*drawn on the booklet's geometry, checked against its SMILES*

1. So, the correct option is (3)

**Solved independently** (answer withheld)

1. $\mathrm{C_7H_8}$ is toluene, $\mathrm{C_6H_5CH_3}$.
2. Excess $\mathrm{Cl_2}$ with heat substitutes all three side-chain H atoms by free radicals: $\mathrm{C_6H_5CH_3} \xrightarrow{3\mathrm{Cl_2}/\Delta} \mathrm{C_6H_5CCl_3}$ (A, benzotrichloride).
3. $-\mathrm{CCl_3}$ is strongly electron-withdrawing, so it is deactivating and meta-directing.
4. $\mathrm{C_6H_5CCl_3} \xrightarrow{\mathrm{Br_2}/\mathrm{Fe}} m\text{-}\mathrm{BrC_6H_4CCl_3}$ (B).
5. $\mathrm{Zn/HCl}$ reduces $-\mathrm{CCl_3}$ to $-\mathrm{CH_3}$ and leaves the aryl C-Br bond alone: $m\text{-}\mathrm{BrC_6H_4CCl_3} \rightarrow m\text{-}\mathrm{BrC_6H_4CH_3}$ (C).
6. C is m-bromotoluene, which is option $3$.

**Subtopic:** Chemical and Physical Properties of Benzene · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 15)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q061_a94b1d49_27102026.png?v=a94b1d491d6c)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q061_c6956103_27102026.png?v=c69561031e92)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Side-chain chlorination turns toluene's CH3 into CCl3, which directs the incoming bromine meta, and Zn/HCl afterwards restores the CH3
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Reading the Br2/Fe step as bromination of toluene itself brings in the methyl group's ortho/para direction and puts bromine para; at that point in the scheme the methyl has already become CCl3, which is meta-directing.
- **Why:** This question requires tracking which group sits on the ring at the moment of bromination, demonstrated by the printed order '3Cl2/Delta, then Br2/Fe, then Zn/HCl' and by three options differing only in where the bromine sits.
- **Note:** The pattern classifier called this reaction_scheme; the reduced qtype vocabulary has no scheme value, so the shape is recorded as mcq with the multi-arrow scheme living in the stem.
<!--/ecat-->

## Q62

Chemistry · organic · Hydrocarbons

Hydrocarbon (A) reacts with bromine by substitution to form an alkyl bromide which by Wurtz reaction is converted to gaseous hydrocarbon containing less than four carbon atoms. (A) is

- (1) $\mathrm{CH_3-CH_3}$
- (2) $\mathrm{CH_2=CH_2}$
- (3) $\mathrm{CH\equiv CH}$
- **(4)** $\mathrm{CH_4}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: methane (A) →(Br₂/hν) bromomethane; bromomethane →(Na/dry ether, Wurtz reaction) ethane](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q062_sol_1_a86efe20_29102026.svg?v=a86efe202b77)

*methane (A) →[Br₂/hν] bromomethane; bromomethane →[Na/dry ether, Wurtz reaction] ethane*

![drawn: methane (A) →(Br₂/hν) bromomethane; bromomethane →(Na/dry ether, Wurtz reaction) ethane](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q062_solution_1_49fb9556_27102026.svg?v=49fb95569700)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Hence the correct option is (4)

**Solved independently** (answer withheld)

1. Wurtz coupling doubles the carbon count: $2\,\mathrm{RBr} + 2\,\mathrm{Na} \rightarrow \mathrm{R{-}R} + 2\,\mathrm{NaBr}$, so the product has fewer than four carbons only if $\mathrm{R}$ has one carbon.
2. Alkenes and alkynes ($\mathrm{CH_2=CH_2}$, $\mathrm{CH\equiv CH}$) add $\mathrm{Br_2}$ rather than undergoing substitution, so options $2$ and $3$ are excluded.
3. $\mathrm{CH_3CH_3} \xrightarrow{\mathrm{Br_2}} \mathrm{C_2H_5Br} \xrightarrow{\mathrm{Na}} \mathrm{C_4H_{10}}$, which has four carbons, so option $1$ is excluded.
4. $\mathrm{CH_4} + \mathrm{Br_2} \xrightarrow{h\nu} \mathrm{CH_3Br} + \mathrm{HBr}$, then $2\,\mathrm{CH_3Br} + 2\,\mathrm{Na} \rightarrow \mathrm{CH_3{-}CH_3}$ (gaseous, $2$ carbons), so (A) is $\mathrm{CH_4}$, option $4$.

**Subtopic:** Preparation of Alkane, Chemical Properties of Alkane · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 15)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q062_dc926713_27102026.png?v=dc9267135d31)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q062_7e7b5692_27102026.png?v=7e7b5692f644)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Only an alkane reacts with bromine by substitution, and Wurtz coupling doubles the carbon count, so the starting hydrocarbon must have one carbon to end at a two-carbon gas
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  Ethane satisfies 'reacts with bromine by substitution' and is the alkane the chapter brominates, so a student who stops at that clause picks it; its Wurtz product is butane, C4H10, with four carbons, which the stem's 'less than four carbon atoms' excludes.
- **Why:** This question requires working backwards through a substitution and a Wurtz coupling under a carbon-count limit, demonstrated by 'converted to gaseous hydrocarbon containing less than four carbon atoms'.
<!--/ecat-->

## Q63

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following molecules represents the order of hybridisation $\mathrm{sp^2}$, $\mathrm{sp^2}$, $\mathrm{sp}$, $\mathrm{sp}$ from left to right atoms?

- (1) $\mathrm{CH_2=CH-CH=CH_2}$
- **(2)** $\mathrm{CH_2=CH-C\equiv CH}$
- (3) $\mathrm{HC\equiv C-C\equiv CH}$
- (4) $\mathrm{CH_3-CH=CH-CH_3}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{\overset{sp^2}{C}H_2=\overset{sp^2}{C}H-\overset{sp}{C}\equiv\overset{sp}{C}H}$
2. Number of orbital require in hybridization $=$ Number of $\sigma$-bonds around each carbon atom.

**Solved independently** (answer withheld)

1. A carbon in a $\mathrm{C=C}$ double bond is $\mathrm{sp^2}$ and a carbon in a $\mathrm{C\equiv C}$ triple bond is $\mathrm{sp}$; a carbon with only single bonds is $\mathrm{sp^3}$.
2. Option 1, $\mathrm{CH_2=CH-CH=CH_2}$: $\mathrm{sp^2, sp^2, sp^2, sp^2}$, so it does not match.
3. Option 3, $\mathrm{HC\equiv C-C\equiv CH}$: $\mathrm{sp, sp, sp, sp}$, so it does not match.
4. Option 4, $\mathrm{CH_3-CH=CH-CH_3}$: $\mathrm{sp^3, sp^2, sp^2, sp^3}$, so it does not match.
5. Option 2, $\mathrm{CH_2=CH-C\equiv CH}$: $\mathrm{sp^2, sp^2, sp, sp}$, which matches, so the answer is option $2$.

**Subtopic:** Hybridisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q063_977e8a54_27102026.png?v=977e8a54c15d)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q063_fc1cfab4_27102026.png?v=fc1cfab4c506)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A carbon's hybridisation follows the bonds it carries: a doubly bonded carbon is sp2 and a triply bonded carbon is sp, read atom by atom along the chain
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Buta-1,3-diene matches the first two entries of 'sp2, sp2, sp, sp' and is the conjugated molecule the chapter drills, so a student who checks the left-hand pair and stops never tests the last two carbons, which are sp2 and not sp.
- **Why:** This question requires a hybridisation to be assigned to each carbon in turn and the whole sequence matched, demonstrated by the stem's 'order of hybridisation sp2, sp2, sp, sp from left to right atoms'.
<!--/ecat-->

## Q64

Chemistry · organic · General Organic Chemistry

Which of the following carbocations is expected to be most stable?

- **(1)** 6-Y-4-nitrocyclohexa-2,4-dien-1-ylium `*C1C=C([N+](=O)[O-])C=C[CH+]1` ![6-Y-4-nitrocyclohexa-2,4-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q064_option_1_s1_b659dc74_27102026.svg?v=b659dc74df99)
- (2) 4-Y-1-nitrocyclohexa-2,5-dien-1-ylium `*C1C=C[C+]([N+](=O)[O-])C=C1` ![4-Y-1-nitrocyclohexa-2,5-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q064_option_2_s1_9f8a1550_27102026.svg?v=9f8a15502218)
- (3) 6-Y-3-nitrocyclohexa-2,4-dien-1-ylium `*C1C=CC([N+](=O)[O-])=C[CH+]1` ![6-Y-3-nitrocyclohexa-2,4-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q064_option_3_s1_e42fed28_27102026.svg?v=e42fed283836)
- (4) 6-Y-1-nitrocyclohexa-2,4-dien-1-ylium `*C1C=CC=C[C+]1[N+](=O)[O-]` ![6-Y-1-nitrocyclohexa-2,4-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q064_option_4_s1_569b3a3e_27102026.svg?v=569b3a3eb3f6)

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $-\mathrm{NO_2}$ group exhibit $-I$ effect and it decreases with increase in distance.
2. In option (1) positive charge present on C-atom at maximum distance so $-I$ effect reaching to it is minimum and stability is maximum.

**Solved independently** (answer withheld)

1. Each option is an arenium ion (sigma complex) with the sp$^3$ carbon $C_1$ bearing H and Y; the $+$ charge is delocalised over $C_2$, $C_4$ and $C_6$ (ortho and para to $C_1$).
2. $\mathrm{NO_2}$ is strongly electron-withdrawing ($-I$, $-R$), so a resonance form with $+$ on the carbon bearing $\mathrm{NO_2}$ is strongly destabilising.
3. Option $1$: $\mathrm{NO_2}$ is on $C_5$ (meta to $C_1$), which never carries the $+$ charge.
4. Options $2$ and $3$: $\mathrm{NO_2}$ is on $C_4$ (para), and option $4$: $\mathrm{NO_2}$ is on $C_2$ (ortho); in each a resonance form places $+$ on $C$–$\mathrm{NO_2}$.
5. Hence option $1$ is the most stable carbocation.

**Subtopic:** Resonance Effect · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 16)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q064_2cea5685_27102026.png?v=2cea56857ed5)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q064_b5774e6f_27102026.png?v=b5774e6fde3e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A carbocation is stabilised most when the positive charge is delocalised by resonance, and only after that by hyperconjugation from attached alkyl groups
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the four options are drawn carbocations and arrived blank in this record, so no option's pull can be inspected
- **Why:** This question requires the carbocation-stability rules to be applied to four drawn cations, demonstrated by the stem 'Which of the following carbocations is expected to be most stable?' with no criterion printed beside it.
- **Note:** All four options_en strings are empty and no figure_image was supplied, so the structures that carry the whole discrimination were not available to this step; the paper itself is intact, so this is the reach of this step and not damage to the question. A reviewer holding the printed options should check whether the three wrong cations are a plain primary/secondary/tertiary series set against a resonance-delocalised one: if so the device to record is a student ranking by the count of attached alkyl groups and missing that delocalisation outranks hyperconjugation. qtype and asks are taken from the stem alone, which is complete.
<!--/ecat-->

## Q65

Chemistry · organic · General Organic Chemistry

> ⚠ The independent solve chose (2); the booklet prints (3).

Which of the following is correct with respect to $-I$ effect of the substituents? ($\mathrm{R}$ = alkyl)

- (1) $-\mathrm{NH_2} > -\mathrm{OR} > -\mathrm{F}$
- (2) $-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$
- **(3)** $-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$
- (4) $-\mathrm{NR_2} > -\mathrm{OR} > -\mathrm{F}$

**Answer** — booklet: (3) · independent solve: (2) · differs

**Publisher's solution**

1. $-I$ effect increases on increasing electronegativity of atom.
2. So, correct order of $-I$ effect is $-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$.
3. *Most appropriate Answer is option (3), however option (2) may also be correct answer.

**Solved independently** (answer withheld)

1. The $-I$ effect of a substituent increases with the electronegativity of the atom bonded to the chain: $\mathrm{F} > \mathrm{O} > \mathrm{N}$.
2. So $-\mathrm{F} > -\mathrm{OR} > -\mathrm{NR_2}$ and likewise $-\mathrm{F} > -\mathrm{OR} > -\mathrm{NH_2}$; options $1$ and $4$ are reversed and wrong.
3. Option $2$ ($-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$) and option $3$ ($-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$) are both consistent with this order; option $2$ is chosen as the like-for-like comparison implied by the stem's "($\mathrm{R}$ = alkyl)".

**Subtopic:** Inductive Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q065_db55c6c7_27102026.png?v=db55c6c7d194)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q065_601402ac_27102026.png?v=601402acd1a5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The $-I$ pull of a substituent follows the electronegativity of the atom joined to the chain, N < O < F, which is the reverse of the order in which the same groups donate by resonance
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  $-\mathrm{NH_2} > -\mathrm{OR} > -\mathrm{F}$ is the taught order for resonance donation ($+M$), so a student who has learnt that one series and not the inductive one writes it down here
- **Why:** This question requires the three substituents to be ordered by inductive withdrawal rather than by donation, demonstrated by the same trio being printed in both directions, '$-\mathrm{NH_2} > -\mathrm{OR} > -\mathrm{F}$' and '$-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$'.
- **Note:** The key is printed as 'Answer (3*)'. Option 2 runs in the same N < O < F direction as the key, so it is defensible on the electronegativity argument the key itself rests on; tagged as printed, with the doubt recorded in the flag. E1 called this statement_options from option length, but the options are three-term inequalities, not statements to be judged, so the printed shape is mcq with an order as the answer.
<!--/ecat-->

## Q66

Chemistry · organic · Alcohols, Phenols and Ethers

In the reaction

The electrophile involved is

![printed figure: phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate ($\ce{O^-Na^+}$ with CHO ortho)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q066_e678da23_29102026.svg?v=e678da23b205)

*phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate ($\ce{O^-Na^+}$ with CHO ortho)*

![drawn: phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate ($\ce{O^-Na^+}$ with CHO ortho)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q066_question_2ef7e4e1_27102026.svg?v=2ef7e4e14160)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q066_question_s1_5c574068_27102026.svg?v=5c5740685d27); trichloromethane `ClC(Cl)Cl` ![trichloromethane](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q066_question_s2_36c42d8f_27102026.svg?v=36c42d8f41aa); sodium hydroxide `[Na+].[OH-]` ![sodium hydroxide](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q066_question_s3_95b7ee63_27102026.svg?v=95b7ee636c6c); sodium 2-formylphenolate `O=Cc1ccccc1[O-].[Na+]` ![sodium 2-formylphenolate](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q066_question_s4_9f16c73a_27102026.svg?v=9f16c73a4515)

- (1) Dichloromethyl anion $\left(\overset{\oplus}{\mathrm{C}}\mathrm{HCl_2}\right)$
- (2) Formyl cation $\left(\overset{\oplus}{\mathrm{C}}\mathrm{HO}\right)$
- (3) Dichloromethyl cation $\left(\overset{\oplus}{\mathrm{C}}\mathrm{HCl_2}\right)$
- **(4)** Dichlorocarbene $\left(:\mathrm{CCl_2}\right)$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. It is Reimer-Tiemann reaction. The electrophile formed is $:\mathrm{CCl_2}$ (Dichlorocarbene) according to the following reaction
2. $\mathrm{CHCl_3} + \mathrm{OH^-} \rightleftharpoons \overset{\ominus}{\ddot{\mathrm{C}}}\mathrm{Cl_3} + \mathrm{H_2O}$
3. $\overset{\ominus}{\ddot{\mathrm{C}}}\mathrm{Cl_3} \longrightarrow \underset{\text{Electrophile}}{:\mathrm{CCl_2}} + \mathrm{Cl^-}$

**Solved independently** (answer withheld)

1. The reaction of phenol with $\mathrm{CHCl_3}$ and $\mathrm{NaOH}$ giving o-hydroxybenzaldehyde (as sodium salt) is the Reimer-Tiemann reaction.
2. $\mathrm{CHCl_3} + \mathrm{OH^-} \rightarrow \mathrm{^-CCl_3} + \mathrm{H_2O}$.
3. $\mathrm{^-CCl_3} \rightarrow :\mathrm{CCl_2} + \mathrm{Cl^-}$, giving the electron-deficient dichlorocarbene.
4. The phenoxide ring attacks $:\mathrm{CCl_2}$ at the ortho position; the $-\mathrm{CHCl_2}$ group is hydrolysed by alkali to $-\mathrm{CHO}$.
5. So the electrophile is dichlorocarbene $(:\mathrm{CCl_2})$, which is option $4$.

**Subtopic:** Reactions of Phenols · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q066_1dede5e8_27102026.png?v=1dede5e8e0e0)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q066_5ec7732e_27102026.png?v=5ec7732ece52)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** In the Reimer-Tiemann reaction chloroform and alkali make dichlorocarbene, a neutral carbon with only six electrons, and that is the electrophile that attacks the phenoxide ring
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  a student reads the $-\mathrm{CHO}$ group in the printed product, works backwards and names the formyl cation, which is the electrophile of the other formylation they have learnt
- **Why:** This question requires the electrophile to be generated from the printed reagents rather than read off the product, demonstrated by the scheme printing '$\mathrm{CHCl_3}$ + $\mathrm{NaOH}$' on the left and a $-\mathrm{CHO}$ group on the right.
- **Note:** Option 1 is named 'Dichloromethyl anion' but the formula beside it is stored with a plus sign, $\overset{\oplus}{\mathrm{C}}\mathrm{HCl_2}$, which is the same symbol as option 3; the printed paper would carry a minus there. The name states the species unambiguously, so the discrimination is intact and the question is tagged as printed, but the charge glyph on option 1 is worth a repair pass.
<!--/ecat-->

## Q67

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Carboxylic acids have higher boiling points than aldehydes, ketones and even alcohols of comparable molecular mass. It is due to their

- (1) More extensive association of carboxylic acid via van der Waals force of attraction
- (2) Formation of carboxylate ion
- (3) Formation of intramolecular H-bonding
- **(4)** Formation of intermolecular H-bonding

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Due to formation of intermolecular H-bonding in carboxylic acid, association occurs.
2. Hence boiling point increases and become more than the boiling point of aldehydes, ketones and alcohols of comparable molecular masses.

**Solved independently** (answer withheld)

1. Carboxylic acids are more extensively associated through $\text{intermolecular}$ hydrogen bonding ($\mathrm{RCOOH}$ dimers), which raises their boiling points above aldehydes, ketones and alcohols of comparable mass, so option $4$.

**Subtopic:** Physical Properties of Aldehydes, Ketones, and Carboxylic Acids · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q067_c516a059_27102026.png?v=c516a059c2b5)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q067_39449e77_27102026.png?v=39449e77b42e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Carboxylic acids boil high because two molecules lock together through a pair of hydrogen bonds between one $\mathrm{O-H}$ and the other's $\mathrm{C=O}$, so the unit that has to be vaporised is the dimer
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'intramolecular' and 'intermolecular' differ by two letters, and a student who has the words hydrogen bonding right but the prefixes interchangeable marks the first of the pair they see
- **Why:** This question requires the stated reason for a granted fact about boiling points, demonstrated by the stem ending 'It is due to their' and the options offering rival forces.
- **Note:** Applied the swap test of the nearby_fact / look_alike_term pair: replace 'intramolecular' with an unlike word and option 3 stops pulling, because the resemblance of the two prefixes is what carries a student there, so look_alike_term rather than nearby_fact. E1 called this statement_options; the options are noun phrases completing 'due to their', not statements judged for truth, so the printed shape is mcq.
<!--/ecat-->

## Q68

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Compound A, $\mathrm{C_8H_{10}O}$, is found to react with $\mathrm{NaOI}$ (produced by reacting Y with $\mathrm{NaOH}$) and yields a yellow precipitate with characteristic smell.

A and Y are respectively

- **(1)** 1-phenylethanol `CC(O)c1ccccc1` ![1-phenylethanol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q068_option_1_s1_0fe451bb_27102026.svg?v=0fe451bb1798) — and $\mathrm{I_2}$
- (2) 2-phenylethanol `OCCc1ccccc1` ![2-phenylethanol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q068_option_2_s1_fa53e0c9_27102026.svg?v=fa53e0c9c920) — and $\mathrm{I_2}$
- (3) (4-methylphenyl)methanol `Cc1ccc(CO)cc1` ![(4-methylphenyl)methanol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q068_option_3_s1_ab1d3b9a_27102026.svg?v=ab1d3b9a182b) — and $\mathrm{I_2}$
- (4) 2,4-dimethylphenol `Cc1ccc(O)c(C)c1` ![2,4-dimethylphenol](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q068_option_4_s1_900dfb8d_27102026.svg?v=900dfb8d54f1) — and $\mathrm{I_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Option (1) is secondary alcohol which on oxidation gives phenylmethyl ketone (Acetophenone).
2. This on reaction with $\mathrm{I_2}$ and $\mathrm{NaOH}$ form iodoform and sodium benzoate.
3. $\mathrm{2NaOH + I_2 \rightarrow NaOI + NaI + H_2O}$

![printed figure: 1-phenylethanol (A) →(NaOI) acetophenone; acetophenone →($\ce{I2}$, NaOH) sodium benzoate + iodoform $\ce{CHI3}$ (yellow ppt)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q068_sol_1_313efc16_29102026.svg?v=313efc16abad)

*1-phenylethanol (A) →[NaOI] acetophenone; acetophenone →[$\ce{I2}$, NaOH] sodium benzoate + iodoform $\ce{CHI3}$ (yellow ppt)*

![drawn: 1-phenylethanol (A) →(NaOI) acetophenone; acetophenone →($\ce{I2}$, NaOH) sodium benzoate + iodoform $\ce{CHI3}$ (yellow ppt)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q068_solution_1_b7301b41_27102026.svg?v=b7301b418af4)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. Yellow precipitate with characteristic smell from NaOI is iodoform, $\mathrm{CHI_3}$, so NaOI comes from $\mathrm{I_2 + NaOH}$ and $Y = \mathrm{I_2}$.
2. The iodoform test is positive only for compounds with a $\mathrm{CH_3CH(OH)-}$ or $\mathrm{CH_3CO-}$ group.
3. Option 1, $\mathrm{C_6H_5CH(OH)CH_3}$ ($\mathrm{C_8H_{10}O}$), has $\mathrm{CH_3CH(OH)-}$; options 2 (primary alcohol $\mathrm{-CH_2CH_2OH}$), 3 (benzylic $\mathrm{-CH_2OH}$) and 4 (a phenol) do not.
4. $\mathrm{C_6H_5CH(OH)CH_3 + 4I_2 + 6NaOH \rightarrow C_6H_5COONa + CHI_3\downarrow + 5NaI + 5H_2O}$, so A and Y are option $1$.

**Subtopic:** Chemical Reactions: Oxidation (Tollens Test and Fehling Test) · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q068_0633b4e2_27102026.png?v=0633b4e275a7)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q068_1cc9fd88_27102026.png?v=1cc9fd88d737)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** A yellow precipitate with a characteristic smell is iodoform, and only a $\mathrm{CH_3CO-}$ or $\mathrm{CH_3CH(OH)-}$ group gives it with $\mathrm{NaOI}$, which is made from iodine and alkali
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  the compound half of every option is a drawn structure and only the trailing text 'and $\mathrm{I_2}$' reached this step, so no option's pull can be inspected
- **Why:** This question requires two species to be named together from one bench observation, demonstrated by the stem 'A and Y are respectively' after 'yields a yellow precipitate with characteristic smell'.
- **Note:** Every options_en string reads only 'and $\mathrm{I_2}$': the structure for A was drawn in the paper and did not come through, and no figure_image was supplied. Y is therefore identical across all four options, so the whole discrimination sits in the missing structures. The paper is intact; this is the reach of this step. A reviewer holding the printed options should check whether the wrong structures are $\mathrm{C_8H_{10}O}$ isomers without a $\mathrm{CH_3CH(OH)-}$ group, such as 2-phenylethanol, the methyl anisoles or phenetole: if so the device to record is a student who checks only the molecular formula $\mathrm{C_8H_{10}O}$ and the presence of an $\mathrm{-OH}$, and not whether a methyl sits on the carbinol carbon. E1 called this plain_mcq, but the stem reads 'A and Y are respectively', so the printed shape is two_part.
<!--/ecat-->

## Q69

Chemistry · inorganic · The D- and F-Block Elements – Practice

Match the metal ions given in Column I with the spin magnetic moments of the ions given in Column II and assign the correct code :

| List-I | | List-II | |
|---|---|---|---|
| a | $\mathrm{Co^{3+}}$ | i | $\sqrt{8}\,\mathrm{BM}$ |
| b | $\mathrm{Cr^{3+}}$ | ii | $\sqrt{35}\,\mathrm{BM}$ |
| c | $\mathrm{Fe^{3+}}$ | iii | $\sqrt{3}\,\mathrm{BM}$ |
| d | $\mathrm{Ni^{2+}}$ | iv | $\sqrt{24}\,\mathrm{BM}$ |
|  |  | v | $\sqrt{15}\,\mathrm{BM}$ |

- (1) iv i ii iii
- (2) i ii iii iv
- **(3)** iv v ii i
- (4) iii v i ii

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{Co^{3+}} = [\mathrm{Ar}]\,3d^{6}$, Unpaired $e^{-}(n) = 4$
2. Spin magnetic moment $= \sqrt{4(4+2)} = \sqrt{24}\,\mathrm{BM}$
3. $\mathrm{Cr^{3+}} = [\mathrm{Ar}]\,3d^{3}$, Unpaired $e^{-}(n) = 3$
4. Spin magnetic moment $= \sqrt{3(3+2)} = \sqrt{15}\,\mathrm{BM}$
5. $\mathrm{Fe^{3+}} = [\mathrm{Ar}]\,3d^{5}$, Unpaired $e^{-}(n) = 5$
6. Spin magnetic moment $= \sqrt{5(5+2)} = \sqrt{35}\,\mathrm{BM}$
7. $\mathrm{Ni^{2+}} = [\mathrm{Ar}]\,3d^{8}$, Unpaired $e^{-}(n) = 2$
8. Spin magnetic moment $= \sqrt{2(2+2)} = \sqrt{8}\,\mathrm{BM}$

**Solved independently** (answer withheld)

1. Spin-only formula: $\mu = \sqrt{n(n+2)}\,\mathrm{BM}$, where $n$ is the number of unpaired electrons.
2. $\mathrm{Co^{3+}}$ is $3d^6$ (free ion), $n = 4$, so $\mu = \sqrt{4 \times 6} = \sqrt{24}\,\mathrm{BM}$ (iv).
3. $\mathrm{Cr^{3+}}$ is $3d^3$, $n = 3$, so $\mu = \sqrt{3 \times 5} = \sqrt{15}\,\mathrm{BM}$ (v).
4. $\mathrm{Fe^{3+}}$ is $3d^5$, $n = 5$, so $\mu = \sqrt{5 \times 7} = \sqrt{35}\,\mathrm{BM}$ (ii).
5. $\mathrm{Ni^{2+}}$ is $3d^8$, $n = 2$, so $\mu = \sqrt{2 \times 4} = \sqrt{8}\,\mathrm{BM}$ (i).
6. Code a-iv, b-v, c-ii, d-i is option $3$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q069_9f0cab1f_27102026.png?v=9f0cab1ffb38)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q069_2adf1891_27102026.png?v=2adf1891b238)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spin-only magnetic moment comes out of the free ion's d-electron count through $\mu=\sqrt{n(n+2)}$ BM: $\mathrm{Co^{3+}}$ is $3d^6$ with $n=4$, $\mathrm{Cr^{3+}}$ is $3d^3$ with $n=3$, $\mathrm{Fe^{3+}}$ is $3d^5$ with $n=5$ and $\mathrm{Ni^{2+}}$ is $3d^8$ with $n=2$
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Option 1 carries the two rows a free-ion count gives most directly, $\mathrm{Co^{3+}}$ with $\sqrt{24}$ BM and $\mathrm{Fe^{3+}}$ with $\sqrt{35}$ BM, and breaks on $\mathrm{Cr^{3+}}$, which it gives $\sqrt{8}$ BM — the value for two unpaired electrons, which is what you get by stripping all three electrons out of Cr's 3d subshell and leaving the 4s electron in place.
- **Why:** This question requires the spin-only moment computed from each ion's d-electron count, demonstrated by Column II printing $\sqrt{8}$, $\sqrt{35}$, $\sqrt{3}$, $\sqrt{24}$ and $\sqrt{15}$ BM — the values of $\sqrt{n(n+2)}$ for $n=2,5,1,4$ and $3$ unpaired electrons.
- **Note:** asks is calculate, not compare: each row produces a number out of $\sqrt{n(n+2)}$, and compare must not be used merely because the answer is a pairing code. arithmetic_slip was the runner-up label and half_right was taken, because two of option 1's four pairs are right and its two failures have separate origins — a miscounted $\mathrm{Cr^{3+}}$ configuration, and the leftover value then forced onto $\mathrm{Ni^{2+}}$.
<!--/ecat-->

## Q70

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which one of the following ions exhibits d-d transition and paramagnetism as well?

- (1) $\mathrm{MnO_4^{-}}$
- (2) $\mathrm{Cr_2O_7^{2-}}$
- (3) $\mathrm{CrO_4^{2-}}$
- **(4)** $\mathrm{MnO_4^{2-}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{CrO_4^{2-}} \Rightarrow \mathrm{Cr^{6+}} = [\mathrm{Ar}]$
2. Unpaired electron $(n) = 0$; Diamagnetic
3. $\mathrm{Cr_2O_7^{2-}} \Rightarrow \mathrm{Cr^{6+}} = [\mathrm{Ar}]$
4. Unpaired electron $(n) = 0$; Diamagnetic
5. $\mathrm{MnO_4^{2-}} = \mathrm{Mn^{6+}} = [\mathrm{Ar}]\,3d^{1}$
6. Unpaired electron $(n) = 1$; Paramagnetic
7. $\mathrm{MnO_4^{-}} = \mathrm{Mn^{7+}} = [\mathrm{Ar}]$
8. Unpaired electron $(n) = 0$; Diamagnetic

**Solved independently** (answer withheld)

1. In $\mathrm{MnO_4^{-}}$, $x + 4(-2) = -1 \Rightarrow x = +7$, so Mn is $3d^0$: no d-d transition, diamagnetic.
2. In $\mathrm{Cr_2O_7^{2-}}$ and $\mathrm{CrO_4^{2-}}$, Cr is $+6$, so $3d^0$: no d-d transition, diamagnetic.
3. In $\mathrm{MnO_4^{2-}}$, $x + 4(-2) = -2 \Rightarrow x = +6$, so Mn is $3d^1$ with one unpaired electron.
4. A $d^1$ ion is paramagnetic and can show a d-d transition, so the answer is option $4$.

**Subtopic:** Ionisation Enthalpies, Formation of Coloured Ions & Formation of Complex Compounds, Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q070_f1b84369_27102026.png?v=f1b843693f58)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q070_7a7ec64f_27102026.png?v=7a7ec64f1b16)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Both a d-d transition and paramagnetism need at least one electron in the d subshell, so the d count worked out from the metal's oxidation state decides which oxoanion qualifies
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  permanganate and manganate are the same five atoms one charge apart, so a student fixed on 'the deeply coloured manganese oxoanion' marks $\mathrm{MnO_4^-}$ without counting the charge through to the oxidation state
- **Why:** This question requires the d-electron count to be derived from each oxidation state and both printed criteria applied to it, demonstrated by the stem asking for 'd-d transition and paramagnetism as well' over four oxoanions of Mn and Cr.
- **Note:** Applied the swap test: replace $\mathrm{MnO_4^-}$ with an unlike $d^0$ ion and the pull on option 1 weakens, because what carries a student there is that permanganate and manganate are the same formula one charge apart, so look_alike_term rather than nearby_fact.
<!--/ecat-->

## Q71

Chemistry · inorganic · Coordination Compounds – Practice

Iron carbonyl, $\mathrm{Fe(CO)_5}$ is

- (1) Trinuclear
- **(2)** Mononuclear
- (3) Tetranuclear
- (4) Dinuclear

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Based on the number of metal atoms present in a complex, they are classified into mononuclear, dinuclear, trinuclear and so on.
2. eg: $\mathrm{Fe(CO)_5}$ : mononuclear
3. $\mathrm{Co_2(CO)_8}$ : dinuclear
4. $\mathrm{Fe_3(CO)_{12}}$: trinuclear
5. Hence, option (2) should be the right answer.

**Solved independently** (answer withheld)

1. $\mathrm{Fe(CO)_5}$ has one Fe centre bonded to five terminal CO ligands (trigonal bipyramidal), so it is mononuclear, which is option $2$.

**Subtopic:** Bonding in Coordination Compounds and Metal Carbonyls · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q071_92aee140_27102026.png?v=92aee14072b3)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q071_d16746cd_27102026.png?v=d16746cdc060)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nuclearity counts the metal atoms in a carbonyl: Fe(CO)5 has one iron and is mononuclear, while Fe2(CO)9 and Fe3(CO)12 are the di- and trinuclear members of the same family
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Fe2(CO)9 with its bridging carbonyls is printed beside Fe(CO)5 in the metal-carbonyl section, so a student who recalls 'iron carbonyl has bridging CO groups between two metal centres' answers for the neighbour in the series instead of for the formula on the page.
- **Why:** This question requires the stated nuclearity of a named carbonyl, demonstrated by the stem printing Fe(CO)5 against four options that are only the rungs of the nuclearity ladder.
<!--/ecat-->

## Q72

Chemistry · inorganic · Coordination Compounds – Practice

The type of isomerism shown by the complex $\mathrm{[CoCl_2(en)_2]}$ is

- (1) Ionization isomerism
- (2) Coordination isomerism
- **(3)** Geometrical isomerism
- (4) Linkage isomerism

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In $\mathrm{[CoCl_2(en)_2]}$, Coordination number of $\mathrm{Co}$ is $6$ and this compound has octahedral geometry.

![printed figure: octahedral geometry diagram of $\ce{(CoCl2(en)2)}$ with the two Cl ligands axial (above and below Co) and the two en ligands spanning the equatorial plane on opposite sides: Trans-form (optically inactive)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q072_sol_1_0af07a18_29102026.svg?v=0af07a18bcc6)

*octahedral geometry diagram of $\ce{[CoCl2(en)2]}$ with the two Cl ligands axial (above and below Co) and the two en ligands spanning the equatorial plane on opposite sides: Trans-form (optically inactive)*


![printed figure: octahedral geometry diagram of $\ce{(CoCl2(en)2)}$ with one Cl axial and one Cl equatorial (adjacent, cis) and the two en ligands spanning the remaining positions: cis-form (optically active)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q072_sol_2_0c3f0784_29102026.svg?v=0c3f07849dfa)

*octahedral geometry diagram of $\ce{[CoCl2(en)2]}$ with one Cl axial and one Cl equatorial (adjacent, cis) and the two en ligands spanning the remaining positions: cis-form (optically active)*

2. As per given option, type of isomerism is geometrical isomerism.

**Solved independently** (answer withheld)

1. $\mathrm{[CoCl_2(en)_2]}$ is an octahedral complex of type $\mathrm{[M(AA)_2B_2]}$, which exists as cis and trans isomers, so it shows geometrical isomerism (option $3$).

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q072_bee8a1a1_27102026.png?v=bee8a1a1ccbd)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q072_f996caac_27102026.png?v=f996caac1207)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Each kind of isomerism has a structural requirement, and [CoCl2(en)2] meets only the one for geometrical isomerism: two identical ligands that can sit cis or trans in an octahedron
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Ionisation isomerism is taught on examples where a chloride swaps between the inside and the outside of the coordination sphere, and the two chlorides printed in this formula bring that example to mind; here there is nothing outside the brackets to swap with.
- **Why:** This question requires each isomerism type's structural requirement to be tested against a printed formula, demonstrated by '[CoCl2(en)2]' carrying no counter ion, no second coordination sphere and no ambidentate ligand.
<!--/ecat-->

## Q73

Chemistry · inorganic · Coordination Compounds – Practice

The geometry and magnetic behaviour of the complex $\mathrm{[Ni(CO)_4]}$ are

- (1) Square planar geometry and paramagnetic
- **(2)** Tetrahedral geometry and diamagnetic
- (3) Square planar geometry and diamagnetic
- (4) Tetrahedral geometry and paramagnetic

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{Ni}(28)$ : $[\mathrm{Ar}]3d^{8}\,4s^{2}$
2. $\because$ $\mathrm{CO}$ is a strong field ligand
3. Configuration would be :

![printed figure: orbital-box diagram of Ni in $\ce{(Ni(CO)4)}$: five 3d boxes each with a paired electron arrow, then one box and three boxes each holding an electron pair (× ×) donated by CO, labelled CO, CO CO CO, enclosed in a dotted box marked sp³-hybridisation](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q073_sol_1_a83002d5_27102026.svg?v=a83002d50016)

*orbital-box diagram of Ni in $\ce{[Ni(CO)4]}$: five 3d boxes each with a paired electron arrow, then one box and three boxes each holding an electron pair (× ×) donated by CO, labelled CO, CO CO CO, enclosed in a dotted box marked sp³-hybridisation*

4. For, four '$\mathrm{CO}$'-ligands hybridisation would be $sp^{3}$ and thus the complex would be diamagnetic and of tetrahedral geometry.

![printed figure: tetracarbonylnickel, Ni bonded to four CO at the corners of a tetrahedron (dotted edges)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q073_sol_2_743eea1c_29102026.svg?v=743eea1cb7f6)

*tetracarbonylnickel, Ni bonded to four CO at the corners of a tetrahedron (dotted edges)*

![drawn: tetracarbonylnickel, Ni bonded to four CO at the corners of a tetrahedron (dotted edges)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q073_solution_2_1398e594_27102026.svg?v=1398e594f726)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. In $\mathrm{[Ni(CO)_4]}$, CO is neutral, so the oxidation state of Ni is $0$: $\mathrm{Ni}: [\mathrm{Ar}]\,3d^{8}4s^{2}$.
2. CO is a strong-field ligand, so the $4s$ electrons pair into $3d$, giving $3d^{10}4s^{0}$.
3. The empty $4s$ and three $4p$ orbitals hybridise to $sp^{3}$, accepting four CO lone pairs, so the geometry is tetrahedral.
4. All $10$ $d$ electrons are paired, so there are $0$ unpaired electrons and the complex is diamagnetic, which is option $2$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q073_e3a823fc_27102026.png?v=e3a823fc0058)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q073_b7c9b091_27102026.png?v=b7c9b091402c)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In Ni(CO)4 the nickel is in the zero oxidation state with a filled 3d10 shell, so it hybridises sp3 to a tetrahedron and has no unpaired electron left to make it paramagnetic
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The geometry half is right, but 'tetrahedral nickel is paramagnetic' is carried over from [NiCl4]2-, where Ni2+ is d8 with two unpaired electrons; in Ni(CO)4 the nickel is Ni(0) with d10 and nothing unpaired.
- **Why:** This question requires a rule to be applied twice over, once for geometry and once for magnetism, demonstrated by the stem asking for 'the geometry and magnetic behaviour' and every option pairing one of each.
- **Note:** The pattern classifier called this statement_options; each option is in fact a two-part answer accepted or rejected whole, which is the two_part shape.
<!--/ecat-->

## Q74

Chemistry · physical · Ionic Equilibrium

Following solutions were prepared by mixing different volumes of $\mathrm{NaOH}$ and $\mathrm{HCl}$ of different concentrations : pH of which one of them will be equal to 1?

- **(a)** $60\,\mathrm{mL}\ \dfrac{\mathrm{M}}{10}\ \mathrm{HCl} + 40\,\mathrm{mL}\ \dfrac{\mathrm{M}}{10}\ \mathrm{NaOH}$
- **(b)** $55\,\mathrm{mL}\ \dfrac{\mathrm{M}}{10}\ \mathrm{HCl} + 45\,\mathrm{mL}\ \dfrac{\mathrm{M}}{10}\ \mathrm{NaOH}$
- **(c)** $75\,\mathrm{mL}\ \dfrac{\mathrm{M}}{5}\ \mathrm{HCl} + 25\,\mathrm{mL}\ \dfrac{\mathrm{M}}{5}\ \mathrm{NaOH}$
- **(d)** $100\,\mathrm{mL}\ \dfrac{\mathrm{M}}{10}\ \mathrm{HCl} + 100\,\mathrm{mL}\ \dfrac{\mathrm{M}}{10}\ \mathrm{NaOH}$

- (1) d
- (2) a
- (3) b
- **(4)** c

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Meq of $\mathrm{HCl} = 75 \times \frac{1}{5} \times 1 = 15$
2. Meq of $\mathrm{NaOH} = 25 \times \frac{1}{5} \times 1 = 5$
3. Meq of $\mathrm{HCl}$ in resulting solution $= 10$
4. Molarity of $[\mathrm{H^{+}}]$ in resulting mixture $= \frac{10}{100} = \frac{1}{10}$
5. $\mathrm{pH} = -\log[\mathrm{H^{+}}] = -\log\left[\frac{1}{10}\right] = 1.0$

**Solved independently** (answer withheld)

1. (a): $n_{H^+} = 60 \times 0.1 - 40 \times 0.1 = 2\,\mathrm{mmol}$, $[H^+] = \frac{2}{100} = 0.02\,\mathrm{M}$, $\mathrm{pH} \approx 1.7$.
2. (b): $n_{H^+} = 55 \times 0.1 - 45 \times 0.1 = 1\,\mathrm{mmol}$, $[H^+] = \frac{1}{100} = 0.01\,\mathrm{M}$, $\mathrm{pH} = 2$.
3. (c): $n_{H^+} = 75 \times 0.2 - 25 \times 0.2 = 15 - 5 = 10\,\mathrm{mmol}$.
4. (c): $[H^+] = \frac{10\,\mathrm{mmol}}{100\,\mathrm{mL}} = 0.1\,\mathrm{M}$, so $\mathrm{pH} = -\log(0.1) = 1$.
5. (d): $100 \times 0.1 - 100 \times 0.1 = 0$, complete neutralisation, $\mathrm{pH} = 7$.
6. Only (c) gives $\mathrm{pH} = 1$; (c) is option $4$.

**Subtopic:** pH Scale · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 18)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q074_50c21f75_27102026.png?v=50c21f75ef00)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q074_528a2ce8_27102026.png?v=528a2ce8bfaf)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** pH $1$ means $[\mathrm{H^+}]=0.1\,\mathrm{M}$ in the mixture that results: take millimoles of acid minus millimoles of base, then divide by the total volume, not by the volume of acid left over.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Dividing the $2$ millimoles of excess acid by the $20\,\mathrm{mL}$ of unneutralised HCl instead of by the $100\,\mathrm{mL}$ of mixture gives exactly $0.1\,\mathrm{M}$ and pH $1$, where the dilution into the full volume gives $0.02\,\mathrm{M}$ and pH $1.7$.
- **Why:** This question requires the surplus strong acid in each printed mixture reduced to a concentration and then to a pH, demonstrated by '$75\,\mathrm{mL}\ \mathrm{M}/5\ \mathrm{HCl} + 25\,\mathrm{mL}\ \mathrm{M}/5\ \mathrm{NaOH}$' having to be worked out before the stem's 'equal to 1' can be matched to anything.
- **Note:** The dropped-dilution slip reaches (a) and (b) alike, since $\frac{2}{20}$ and $\frac{1}{10}$ are both $0.1\,\mathrm{M}$, which is presumably why both letters are printed as options. The trap is recorded on (a) because the slip needs no fractional millimoles there, $6-4=2$ over $20\,\mathrm{mL}$, while (b) requires carrying $5.5$ and $4.5$ - a property of the arithmetic, not a claim about who picks what. The question's one discriminating fact is that (c) alone is $\mathrm{M}/5$ rather than $\mathrm{M}/10$: $15-5=10$ mmol in $100\,\mathrm{mL}$ is $0.1\,\mathrm{M}$, pH $1$, which the printed key confirms. E1_question_type is the plain_mcq default, but a lettered list a-d is printed and the four options are the bare letters, so qtype is statements.
<!--/ecat-->

## Q75

Chemistry · physical · Surface Chemistry

On which of the following properties does the coagulating power of an ion depend?

- **(1)** Both magnitude and sign of the charge on the ion
- (2) Size of the ion alone
- (3) The magnitude of the charge on the ion alone
- (4) The sign of charge on the ion alone

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Coagulation of colloidal solution by using an electrolyte depends on the charge present (positive or negative) on colloidal particles as well as on its size.
2. Coagulating power of an electrolyte depends on the magnitude of charge present on effective ion of electrolyte.

**Solved independently** (answer withheld)

1. By the Hardy-Schulze rule, the coagulating ion must carry a charge opposite in sign to the colloidal particles, and its coagulating power increases with the magnitude of its charge (e.g. $Al^{3+} > Ba^{2+} > Na^{+}$ for a negative sol), so it depends on both the magnitude and the sign of the charge, which is option $1$.

**Subtopic:** Coagulation of Colloids and Hardy-Schulze Rule · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q075_f650de2b_27102026.png?v=f650de2b80cd)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q075_6cdf8cd3_27102026.png?v=6cdf8cd3f753)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Hardy-Schulze rule has two halves: the coagulating ion must carry charge opposite in sign to the colloidal particle, and the greater the magnitude of that charge the greater its coagulating power
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The rule is usually carried as the one sentence 'the greater the valence of the coagulating ion, the greater its power', which names only the magnitude, so a student answers with the half they hold and drops the requirement that the sign be opposite to the colloid's.
- **Why:** This question requires the stated content of the Hardy-Schulze rule, demonstrated by the options splitting it into its sign half, its magnitude half and both together.
- **Note:** Option 1 bundles two properties, but the stem asks a single question about dependence rather than for two answers, so the shape stays mcq rather than two_part.
<!--/ecat-->

## Q76

Chemistry · physical · States of Matter

Given van der Waals constant for $\mathrm{NH_3}$, $\mathrm{H_2}$, $\mathrm{O_2}$ and $\mathrm{CO_2}$ are respectively $4.17$, $0.244$, $1.36$ and $3.59$, which one of the following gases is most easily liquefied?

- (1) $\mathrm{O_2}$
- (2) $\mathrm{H_2}$
- **(3)** $\mathrm{NH_3}$
- (4) $\mathrm{CO_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. van der waal constant ‘$a$’, signifies intermolecular forces of attraction.
2. Higher is the value of ‘$a$’, easier will be the liquefaction of gas.

**Solved independently** (answer withheld)

1. The listed constants are the van der Waals attraction constant $a$, which measures the strength of intermolecular attraction.
2. A larger $a$ means stronger attraction, so the gas liquefies more easily.
3. $a(\mathrm{NH_3}) = 4.17 > a(\mathrm{CO_2}) = 3.59 > a(\mathrm{O_2}) = 1.36 > a(\mathrm{H_2}) = 0.244$, so $\mathrm{NH_3}$ (option $3$) is most easily liquefied.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q076_740f1106_27102026.png?v=740f110607f3)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q076_02623c20_27102026.png?v=02623c200343)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The van der Waals constant a measures the strength of intermolecular attraction, and the gas with the largest a is the easiest to liquefy
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  H2 carries the smallest printed constant, 0.244, and a student who holds the link between a and liquefaction the wrong way round -- small a meaning a gas that gives in easily -- reads the bottom of the row as the answer instead of the top.
- **Why:** This question requires a known rule to be applied to printed data, demonstrated by the stem supplying the four van der Waals constants and then asking which gas 'is most easily liquefied'.
<!--/ecat-->

## Q77

Chemistry · physical · Ionic Equilibrium

The solubility of $\mathrm{BaSO_4}$ in water is $2.42 \times 10^{-3}\,\mathrm{g\,L^{-1}}$ at $298\,\mathrm{K}$. The value of its solubility product $(K_{sp})$ will be (Given molar mass of $\mathrm{BaSO_4}$ = $233\,\mathrm{g\,mol^{-1}}$)

- (1) $1.08 \times 10^{-14}\,\mathrm{mol^2\,L^{-2}}$
- (2) $1.08 \times 10^{-12}\,\mathrm{mol^2\,L^{-2}}$
- **(3)** $1.08 \times 10^{-10}\,\mathrm{mol^2\,L^{-2}}$
- (4) $1.08 \times 10^{-8}\,\mathrm{mol^2\,L^{-2}}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Solubility of $\mathrm{BaSO_4}$, $s = \frac{2.42 \times 10^{-3}}{233}\,(\mathrm{mol\,L^{-1}})$
2. $= 1.04 \times 10^{-5}\,(\mathrm{mol\,L^{-1}})$
3. $\underset{}{\mathrm{BaSO_4(s)}} \rightleftharpoons \underset{s}{\mathrm{Ba^{2+}(aq)}} + \underset{s}{\mathrm{SO_4^{2-}(aq)}}$
4. $K_{sp} = [\mathrm{Ba^{2+}}]\,[\mathrm{SO_4^{2-}}] = s^{2}$
5. $= (1.04 \times 10^{-5})^{2}$
6. $= 1.08 \times 10^{-10}\,\mathrm{mol^{2}\,L^{-2}}$

**Solved independently** (answer withheld)

1. Molar solubility: $s = \frac{2.42 \times 10^{-3}\,\mathrm{g\,L^{-1}}}{233\,\mathrm{g\,mol^{-1}}} = 1.04 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$.
2. $\mathrm{BaSO_4 \rightleftharpoons Ba^{2+} + SO_4^{2-}}$, so $[\mathrm{Ba^{2+}}] = [\mathrm{SO_4^{2-}}] = s$ and $K_{sp} = s^2$.
3. $K_{sp} = (1.0386 \times 10^{-5})^2 = 1.08 \times 10^{-10}\,\mathrm{mol^2\,L^{-2}}$, which is option $3$.

**Subtopic:** Solubility Product Constant · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q077_497fbf94_27102026.png?v=497fbf94f5d0)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q077_7add477f_27102026.png?v=7add477f9bfc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a 1:1 salt the solubility product is the square of the molar solubility, so the solubility in grams per litre must first be divided by the molar mass
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Dividing 2.42 by 233 gives 0.0104, and a student who writes that as $1.04\times10^{-1}$ instead of $1.04\times10^{-2}$ before attaching the $10^{-3}$ gets $s = 1.04\times10^{-4}$, whose square is the printed $1.08\times10^{-8}$ -- one power of ten away from the right answer with the same mantissa.
- **Why:** This question requires a number computed from the stem's own data, demonstrated by 'solubility of BaSO4 in water is 2.42e-3 g/L' with the molar mass supplied so that Ksp can be worked out.
<!--/ecat-->

## Q78

Chemistry · physical · Basic Concepts of Chemistry

In which case is number of molecules of water maximum?

- (1) $0.00224\,\mathrm{L}$ of water vapours at $1\,\mathrm{atm}$ and $273\,\mathrm{K}$
- (2) $0.18\,\mathrm{g}$ of water
- **(3)** $18\,\mathrm{mL}$ of water
- (4) $10^{-3}\,\mathrm{mol}$ of water

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. (1) Moles of water $= \frac{0.00224}{22.4} = 10^{-4}$
2. Molecules of water $=$ mole $\times N_A = 10^{-4}\,N_A$
3. (2) Molecules of water $=$ mole $\times N_A = \frac{0.18}{18}N_A$
4. $= 10^{-2}\,N_A$
5. (3) Mass of water $= 18 \times 1 = 18\,\mathrm{g}$
6. Molecules of water $=$ mole $\times N_A = \frac{18}{18}N_A$
7. $= N_A$
8. (4) Molecules of water $=$ mole $\times N_A = 10^{-3}\,N_A$

**Solved independently** (answer withheld)

1. At $1\,\mathrm{atm}$ and $273\,\mathrm{K}$, $n_1 = \frac{0.00224\,\mathrm{L}}{22.4\,\mathrm{L\,mol^{-1}}} = 10^{-4}\,\mathrm{mol}$.
2. $n_2 = \frac{0.18\,\mathrm{g}}{18\,\mathrm{g\,mol^{-1}}} = 10^{-2}\,\mathrm{mol}$.
3. With density $1\,\mathrm{g\,mL^{-1}}$, $18\,\mathrm{mL}$ of water is $18\,\mathrm{g}$, so $n_3 = \frac{18}{18} = 1\,\mathrm{mol}$.
4. $n_4 = 10^{-3}\,\mathrm{mol}$.
5. Number of molecules is proportional to $n$, and $n_3 = 1\,\mathrm{mol}$ is the largest, which is option $3$.

**Subtopic:** Mole Concept · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q078_379adf4a_27102026.png?v=379adf4a7d29)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q078_9c61943f_27102026.png?v=9c61943f67b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Molecule counts can only be compared after every quantity is turned into moles: a volume of gas through 22.4 L at STP, a mass through 18 g per mole, and a volume of liquid water through its density of 1 g per mL
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Leaving out the one conversion the stem does not spell out, millilitres of liquid water to grams through its density, makes option 3 look unusable and 0.18 g the largest amount left at 0.01 mol; with the density step taken, 18 mL is 18 g, which is a full mole.
- **Why:** This question requires every printed quantity to be computed into moles before the largest can be named, demonstrated by the four cases being given as a gas volume, a mass, a liquid volume and a mole count.
<!--/ecat-->

## Q79

Chemistry · physical · Chemical Kinetics

The correct difference between first and second order reactions is that

- (1) A first-order reaction can catalyzed; a second-order reaction cannot be catalyzed
- **(2)** The half-life of a first-order reaction does not depend on $[\mathrm{A}]_0$; the half-life of a second-order reaction does depend on $[\mathrm{A}]_0$
- (3) The rate of a first-order reaction does not depend on reactant concentrations; the rate of a second-order reaction does depend on reactant concentrations
- (4) The rate of a first-order reaction does depend on reactant concentrations; the rate of a second-order reaction does not depend on reactant concentrations

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For first order reaction, $t_{1/2} = \frac{0.693}{k}$, which is independent of initial concentration of reactant.
2. For second order reaction, $t_{1/2} = \frac{1}{k[A_0]}$, which depends on initial concentration of reactant.

**Solved independently** (answer withheld)

1. For a first-order reaction, $t_{1/2} = \frac{0.693}{k}$, which is independent of $[\mathrm{A}]_0$.
2. For a second-order reaction, $t_{1/2} = \frac{1}{k[\mathrm{A}]_0}$, which depends on $[\mathrm{A}]_0$.
3. Options 3 and 4 are wrong because both rate laws ($r = k[\mathrm{A}]$ and $r = k[\mathrm{A}]^2$) depend on concentration; option 1 is wrong because either order can be catalysed, so the answer is option $2$.

**Subtopic:** Half-Life of a Reaction · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 19)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q079_652f4683_27102026.png?v=652f46835daf)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q079_4ef3c447_27102026.png?v=4ef3c447c2e6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Both first and second order rates depend on concentration; what separates the two orders is the half-life, constant for first order and inversely proportional to the initial concentration for second order
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The opening clause, that a first-order rate does depend on concentration, is true and is the clause a student can check at once, so verifying it and taking the option leaves the second clause -- that a second-order rate does not depend on concentration -- untested.
- **Why:** This question requires two neighbouring concepts to be held apart on the one property that actually differs, demonstrated by the stem asking for 'the correct difference between first and second order reactions' while three options offer differences that do not hold.
- **Note:** The pattern classifier called this statement_options; the stem is not an instruction to judge statements and prints no lettered block, so under the reduced qtype vocabulary the shape is mcq.
<!--/ecat-->

## Q80

Chemistry · inorganic · The s-Block Elements

Among $\mathrm{CaH_2}$, $\mathrm{BeH_2}$, $\mathrm{BaH_2}$, the order of ionic character is

- (1) $\mathrm{BeH_2} < \mathrm{BaH_2} < \mathrm{CaH_2}$
- (2) $\mathrm{CaH_2} < \mathrm{BeH_2} < \mathrm{BaH_2}$
- **(3)** $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$
- (4) $\mathrm{BaH_2} < \mathrm{BeH_2} < \mathrm{CaH_2}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For $2^{\mathrm{nd}}$ group hydrides, on moving down the group metallic character of metals increases so ionic character of metal hydride increases.
2. Hence the option (3) should be correct option.

**Solved independently** (answer withheld)

1. Down group 2 ($\mathrm{Be} \to \mathrm{Ca} \to \mathrm{Ba}$) atomic size increases and electronegativity decreases, so the metal gives up electrons more readily and the M-H bond becomes more ionic.
2. $\mathrm{BeH_2}$ is covalent (polymeric) because small $\mathrm{Be^{2+}}$ has high polarising power, so it is least ionic.
3. Hence ionic character: $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$, which is option $3$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 20)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q080_fc5556ea_27102026.png?v=fc5556ea7cf1)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q080_af520ccb_27102026.png?v=af520ccb8cea)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Ionic character of group-2 hydrides increases down the group as the metal grows more electropositive: BeH2 is covalent and polymeric, BaH2 is a saline hydride
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Putting BeH2 at the bottom is right, and then CaH2 is lifted to the top because calcium hydride is the hydride met by name as the ionic, saline one -- hydrolith; that swaps the Ca and Ba adjacency, which is the only place the option fails.
- **Why:** This question requires three members of one group to be sequenced on a trend, demonstrated by the stem's 'the order of ionic character is' and by every option being an inequality chain.
- **Note:** The pattern classifier called this statement_options; the options are inequality chains rather than statements to judge, so the shape is recorded as mcq.
<!--/ecat-->

## Q81

Chemistry · physical · Redox Reactions

Consider the change in oxidation state of Bromine corresponding to different emf values as shown in the diagram below :

Then the species undergoing disproportionation is

![printed figure: Latimer (reduction potential) diagram of bromine: $\ce{BrO4^-}$ →(1.82 V) $\ce{BrO3^-}$ →(1.5 V) $\ce{HBrO}$ →(1.595 V) $\ce{Br2}$ →(1.0652 V) $\ce{Br^-}$](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q081_5c186109_27102026.svg?v=5c18610929a3)

*Latimer (reduction potential) diagram of bromine: $\ce{BrO4^-}$ →[1.82 V] $\ce{BrO3^-}$ →[1.5 V] $\ce{HBrO}$ →[1.595 V] $\ce{Br2}$ →[1.0652 V] $\ce{Br^-}$*

- (1) $\mathrm{Br_2}$
- (2) $\mathrm{BrO_4^-}$
- (3) $\mathrm{BrO_3^-}$
- **(4)** $\mathrm{HBrO}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\overset{+1}{\mathrm{HBrO}} \longrightarrow \overset{0}{\mathrm{Br_2}}$, $E^{\circ}_{\mathrm{HBrO/Br_2}} = 1.595\,\mathrm{V}$
2. $\overset{+1}{\mathrm{HBrO}} \longrightarrow \overset{+5}{\mathrm{BrO_3^-}}$, $E^{\circ}_{\mathrm{BrO_3^-/HBrO}} = 1.5\,\mathrm{V}$
3. $E^{\circ}_{\mathrm{cell}}$ for the disproportionation of $\mathrm{HBrO}$,
4. $E^{\circ}_{\mathrm{cell}} = E^{\circ}_{\mathrm{HBrO/Br_2}} - E^{\circ}_{\mathrm{BrO_3^-/HBrO}}$
5. $= 1.595 - 1.5$
6. $= 0.095\,\mathrm{V} = +\,\mathrm{ve}$
7. Hence, option (3) is correct answer.

**Solved independently** (answer withheld)

1. A species disproportionates if $E^\circ_{cell} = E^\circ_{\text{(its reduction)}} - E^\circ_{\text{(reduction of the higher state to it)}} > 0$.
2. For $\mathrm{HBrO}$: $E^\circ_{cell} = E^\circ_{\mathrm{HBrO/Br_2}} - E^\circ_{\mathrm{BrO_3^-/HBrO}} = 1.595 - 1.5 = +0.095\,\mathrm{V} > 0$, spontaneous.
3. For $\mathrm{Br_2}$: $E^\circ_{cell} = 1.0652 - 1.595 = -0.53\,\mathrm{V} < 0$, not spontaneous.
4. For $\mathrm{BrO_3^-}$: $E^\circ_{cell} = 1.5 - 1.82 = -0.32\,\mathrm{V} < 0$, not spontaneous.
5. $\mathrm{BrO_4^-}$ has Br in its highest state ($+7$) and cannot be oxidised, so it cannot disproportionate.
6. Hence $\mathrm{HBrO}$ disproportionates, which is option $4$.

**Subtopic:** Types of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q081_24771439_27102026.png?v=24771439601a)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q081_50d8f43d_27102026.png?v=50d8f43db938)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** On a Latimer diagram a species disproportionates when the reduction potential on its right exceeds the one on its left; for HBrO 1.595 V to the right beats 1.5 V to the left
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  The disproportionation of bromine in alkali, 3Br2 + 6OH- giving 5Br- and BrO3-, is a reaction carried in memory, so a student answers with the species that disproportionates in that reaction instead of reading the two potentials the diagram places either side of each species.
- **Why:** This question requires the two potentials flanking each species to be read off the printed diagram and compared, demonstrated by 'the species undergoing disproportionation is' set under a chain carrying 1.82, 1.5, 1.595 and 1.0652 V.
- **Note:** The figure was supplied to this step as text and as a scheme with all four potentials and their directions, so the diagram could be read and the trap confirmed.
<!--/ecat-->

## Q82

Chemistry · physical · Redox Reactions

For the redox reaction
$\mathrm{MnO_4^{-} + C_2O_4^{2-} + H^{+} \longrightarrow Mn^{2+} + CO_2 + H_2O}$
The correct coefficients of the reactants for the balanced equation are
$\mathrm{MnO_4^{-}}$ \quad $\mathrm{C_2O_4^{2-}}$ \quad $\mathrm{H^{+}}$

- (1) $2$ \quad $16$ \quad $5$
- **(2)** $2$ \quad $5$ \quad $16$
- (3) $16$ \quad $5$ \quad $2$
- (4) $5$ \quad $16$ \quad $2$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

![printed figure: Reduction (bracket from $\ce{MnO4^-}$ to $\ce{Mn^2+}$); $\ce{MnO4^-}$ (Mn +7) + $\ce{C2O4^2-}$ (C +3) + $\ce{H+}$ → $\ce{Mn^2+}$ + $\ce{CO2}$ (C +4) + $\ce{H2O}$; Oxidation (bracket from $\ce{C2O4^2-}$ to $\ce{CO2}$)](https://d30lmobgrc5gb8.cloudfront.net/general/29102026/neet_papers/2018/2018_AA/figures_agent/q082_sol_1_9fd13b67_29102026.svg?v=9fd13b675d25)

*Reduction (bracket from $\ce{MnO4^-}$ to $\ce{Mn^2+}$); $\ce{MnO4^-}$ (Mn +7) + $\ce{C2O4^2-}$ (C +3) + $\ce{H+}$ → $\ce{Mn^2+}$ + $\ce{CO2}$ (C +4) + $\ce{H2O}$; Oxidation (bracket from $\ce{C2O4^2-}$ to $\ce{CO2}$)*

![drawn: Reduction (bracket from $\ce{MnO4^-}$ to $\ce{Mn^2+}$); $\ce{MnO4^-}$ (Mn +7) + $\ce{C2O4^2-}$ (C +3) + $\ce{H+}$ → $\ce{Mn^2+}$ + $\ce{CO2}$ (C +4) + $\ce{H2O}$; Oxidation (bracket from $\ce{C2O4^2-}$ to $\ce{CO2}$)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_drawn/q082_solution_1_e5f4ff8c_27102026.svg?v=e5f4ff8cde25)  
*drawn on the booklet's geometry, checked against its SMILES*

1. n-factor of $\mathrm{MnO_4^{-}} \Rightarrow 5$
2. n-factor of $\mathrm{C_2O_4^{2-}} \Rightarrow 2$
3. Ratio of n-factors of $\mathrm{MnO_4^{-}}$ and $\mathrm{C_2O_4^{2-}}$ is $5 : 2$
4. So, molar ratio in balanced reaction is $2 : 5$
5. $\therefore$ The balanced equation is
6. $\mathrm{2MnO_4^{-} + 5C_2O_4^{2-} + 16H^{+} \rightarrow 2Mn^{2+} + 10CO_2 + 8H_2O}$

**Solved independently** (answer withheld)

1. In $\mathrm{MnO_4^-}$, Mn goes from $+7$ to $+2$ in $\mathrm{Mn^{2+}}$: a gain of $5e^-$ per Mn.
2. In $\mathrm{C_2O_4^{2-}}$, each C goes from $+3$ to $+4$ in $\mathrm{CO_2}$: a loss of $2e^-$ per oxalate ion.
3. Equate electrons (LCM $10$): $2\,\mathrm{MnO_4^-} + 5\,\mathrm{C_2O_4^{2-}} \rightarrow 2\,\mathrm{Mn^{2+}} + 10\,\mathrm{CO_2}$.
4. Balance O with water: LHS has $8 + 20 = 28$ O, $\mathrm{CO_2}$ has $20$, so $8\,\mathrm{H_2O}$ on the right.
5. Balance H: $8\,\mathrm{H_2O}$ needs $16\,\mathrm{H^+}$; charge check: $-2 - 10 + 16 = +4 = 2(+2)$.
6. Coefficients $2, 5, 16$ for $\mathrm{MnO_4^-}, \mathrm{C_2O_4^{2-}}, \mathrm{H^+}$, which is option $2$.

**Subtopic:** Balancing of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q082_7c256bdf_27102026.png?v=7c256bdfaa70)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q082_c0162af0_27102026.png?v=c0162af0dd30)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Balancing a redox equation by electron balance: each $\mathrm{MnO_4^-}$ takes $5$ electrons and each $\mathrm{C_2O_4^{2-}}$ gives $2$, so the two cross to $2:5$, and the oxygen then fixes $16\,\mathrm{H^+}$.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Reading the doubled permanganate half-reaction $2\mathrm{MnO_4^-}+16\mathrm{H^+}+10e^-\to2\mathrm{Mn^{2+}}+8\mathrm{H_2O}$ straight into the three answer columns writes $2$, then $16$, then the per-manganese electron figure $5$ - so the $16$ that belongs to $\mathrm{H^+}$ lands in the $\mathrm{C_2O_4^{2-}}$ column and the $5$ that belongs to $\mathrm{C_2O_4^{2-}}$ lands under $\mathrm{H^+}$.
- **Why:** This question requires the electron and charge balance of a printed equation worked out and the three coefficients delivered together, demonstrated by the stem printing the columns '$\mathrm{MnO_4^-}$ $\mathrm{C_2O_4^{2-}}$ $\mathrm{H^+}$' and every option filling all three at once.
- **Note:** E1_question_type is the plain_mcq default, but the stem prints a header row of three species and each option is a row of three coefficients that must all be right together, which is the several-blanks-answered-together shape; qtype is therefore two_part, with the caveat that there are three columns here rather than two. The trap label is half_right because the answer is a three-part row of which option 1 gets the first part right and the other two wrong; the codebook's `reversed` is explicitly not for 'one swapped pair inside a longer order', which is what option 1 is relative to the key.
<!--/ecat-->

## Q83

Chemistry · physical · Chemical Equilibrium

Which one of the following conditions will favour maximum formation of the product in the reaction, $\mathrm{A_2(g)} + \mathrm{B_2(g)} \rightleftharpoons \mathrm{X_2(g)}\ \Delta_r H = -X\,\mathrm{kJ}$?

- (1) High temperature and high pressure
- (2) Low temperature and low pressure
- **(3)** Low temperature and high pressure
- (4) High temperature and low pressure

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{A_2(g)} + \mathrm{B_2(g)} \rightleftharpoons \mathrm{X_2(g)};\ \Delta H = -x\,\mathrm{kJ}$
2. On increasing pressure equilibrium shifts in a direction where pressure decreases i.e. forward direction.
3. On decreasing temperature, equilibrium shifts in exothermic direction i.e., forward direction.
4. So, high pressure and low temperature favours maximum formation of product.

**Solved independently** (answer withheld)

1. $\Delta_r H = -X\,\mathrm{kJ} < 0$, so the forward reaction is exothermic and lowering temperature shifts equilibrium towards $\mathrm{X_2}$.
2. $\Delta n_g = 1 - (1+1) = -1$, so increasing pressure shifts equilibrium towards fewer gas moles, i.e. towards $\mathrm{X_2}$.
3. Low temperature and high pressure is option $3$.

**Subtopic:** Factors Affecting Equilibrium · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q083_8d47c8df_27102026.png?v=8d47c8dfc306)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q083_f44f6b44_27102026.png?v=f44f6b44fba9)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Le Chatelier's principle applied twice: an exothermic reaction is pushed forward by cooling, and a reaction whose gas moles fall from two to one is pushed forward by compression
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  High pressure is the right half, read correctly off two moles of gas becoming one, and then high temperature is added because heating is remembered as the way to drive a reaction on; for an exothermic reaction heat is a product, so warming shifts it back.
- **Why:** This question requires one rule applied to two variables at once, demonstrated by the stem's 'which one of the following conditions' set against options that cross high and low temperature with high and low pressure.
- **Note:** Each option is a temperature crossed with a pressure and scores nothing if half right, so the shape is two_part rather than mcq.
<!--/ecat-->

## Q84

Chemistry · physical · Chemical Kinetics

When initial concentration of the reactant is doubled, the half-life period of a zero order reaction

- (1) Is tripled
- **(2)** Is doubled
- (3) Is halved
- (4) Remains unchanged

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Half life of zero order
2. $t_{1/2} = \frac{[A_0]}{2K}$
3. $t_{1/2}$ will be doubled on doubling the initial concentration.

**Solved independently** (answer withheld)

1. For a zero order reaction, $[R] = [R]_0 - kt$, so at $t_{1/2}$, $[R] = \frac{[R]_0}{2}$ gives $t_{1/2} = \frac{[R]_0}{2k}$.
2. Doubling the initial concentration: $t_{1/2}' = \frac{2[R]_0}{2k} = 2\,t_{1/2}$.
3. The half-life is doubled, which is option $2$.

**Subtopic:** Half-Life of a Reaction, Zero Order Reactions · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q084_bdad34d0_27102026.png?v=bdad34d08d1c)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q084_d4ccbba2_27102026.png?v=d4ccbba2ac02)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a zero order reaction t_half = [A]0/2k, so the half-life is directly proportional to the initial concentration
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Applying the first-order half-life, $t_{1/2} = 0.693/k$, which carries no concentration at all, makes the answer 'unchanged'; the zero-order half-life is $[A]_0/2k$, where the initial concentration sits in the numerator.
- **Why:** This question requires how many times one quantity changes when another is doubled, demonstrated by 'when initial concentration of the reactant is doubled, the half-life period of a zero order reaction' with options that are bare factors.
<!--/ecat-->

## Q85

Chemistry · physical · Thermodynamics

The bond dissociation energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are in the ratio of $1 : 0.5 : 1$. $\Delta H$ for the formation of $\mathrm{XY}$ is $-200\,\mathrm{kJ\,mol^{-1}}$. The bond dissociation energy of $\mathrm{X_2}$ will be

- **(1)** $800\,\mathrm{kJ\,mol^{-1}}$
- (2) $100\,\mathrm{kJ\,mol^{-1}}$
- (3) $200\,\mathrm{kJ\,mol^{-1}}$
- (4) $400\,\mathrm{kJ\,mol^{-1}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The reaction for $\Delta_f H^\circ(\mathrm{XY})$
2. $\frac{1}{2}\mathrm{X_2(g)} + \frac{1}{2}\mathrm{Y_2(g)} \longrightarrow \mathrm{XY(g)}$
3. Bond energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are $X$, $\frac{X}{2}$, $X$ respectively
4. $\therefore\ \Delta H = \left(\frac{X}{2} + \frac{X}{4}\right) - X = -200$
5. On solving, we get
6. $\Rightarrow -\frac{X}{2} + \frac{X}{4} = -200$
7. $\Rightarrow X = 800\,\mathrm{kJ/mole}$

**Solved independently** (answer withheld)

1. Let the bond dissociation energies be $a$ for $\mathrm{X_2}$, $0.5a$ for $\mathrm{Y_2}$ and $a$ for $\mathrm{XY}$.
2. Formation reaction: $\tfrac{1}{2}\mathrm{X_2} + \tfrac{1}{2}\mathrm{Y_2} \rightarrow \mathrm{XY}$.
3. $\Delta H = \sum BE_{\text{reactants}} - \sum BE_{\text{products}} = \tfrac{1}{2}a + \tfrac{1}{2}(0.5a) - a = -0.25a$.
4. $-0.25a = -200\,\mathrm{kJ\,mol^{-1}} \Rightarrow a = 800\,\mathrm{kJ\,mol^{-1}}$, which is option $1$.

**Subtopic:** Bond Enthalpy (ΔBondH°) · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 21)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q085_e3a1fe90_27102026.png?v=e3a1fe90143e)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q085_e2e38899_27102026.png?v=e2e388990d22)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Bond enthalpy arithmetic: $\Delta H$ is bonds broken minus bonds formed, and a formation enthalpy is quoted per mole of product, so $\mathrm{X_2}$ and $\mathrm{Y_2}$ enter as half a mole each.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Writing the formation as $\mathrm{X_2+Y_2\to 2XY}$ instead of $\tfrac{1}{2}\mathrm{X_2}+\tfrac{1}{2}\mathrm{Y_2}\to\mathrm{XY}$ doubles every coefficient, so the net term becomes $-0.5x$ and $x=400$ instead of $-0.25x$ and $x=800$.
- **Why:** This question requires the bond-enthalpy relation applied to numbers supplied in the stem, demonstrated by 'the bond dissociation energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are in the ratio of $1 : 0.5 : 1$' having to be combined with '$\Delta H$ for the formation of $\mathrm{XY}$ is $-200\,\mathrm{kJ\,mol^{-1}}$' before any option can be read.
<!--/ecat-->

## Q86

Chemistry · physical · States of Matter

The correction factor ‘$a$’ to the ideal gas equation corresponds to

- (1) Electric field present between the gas molecules
- (2) Volume of the gas molecules
- (3) Density of the gas molecules
- **(4)** Forces of attraction between the gas molecules

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In real gas equation, $\left(\mathrm{P}+\frac{\mathrm{an}^{2}}{\mathrm{V}^{2}}\right)(\mathrm{V}-\mathrm{nb})=\mathrm{nRT}$
2. van der Waal’s constant, ‘$a$’ signifies intermolecular forces of attraction.

**Solved independently** (answer withheld)

1. In the van der Waals equation $\left(P + \frac{a n^2}{V^2}\right)(V - nb) = nRT$, the term $\frac{a n^2}{V^2}$ corrects the pressure for the forces of attraction between gas molecules (while $b$ corrects for molecular volume), so the answer is option $4$.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 21)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q086_b019210a_27102026.png?v=b019210acb5b)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q086_ce9c0292_27102026.png?v=ce9c02922c30)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In van der Waals' equation the constant $a$ corrects the pressure for attraction between molecules, while $b$ corrects the volume for the space the molecules themselves occupy.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  'Volume of the gas molecules' is the other correction printed in the same equation, so a student who remembers that one constant is for volume and one for attraction, but not which is which, takes the one he can picture.
- **Why:** This question requires the stated meaning of one named constant, demonstrated by the stem 'The correction factor ‘$a$’ to the ideal gas equation corresponds to' supplying no data to work on.
- **Note:** E1_question_type reads `statement_options`, decided on option length, but the printed options are noun phrases completing the stem ('Volume of the gas molecules'), not statements to be judged, so the shape on the page is a plain MCQ and qtype is recorded as mcq.
<!--/ecat-->

## Q87

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Consider the following species : $\mathrm{CN^{+}}$, $\mathrm{CN^{-}}$, $\mathrm{NO}$ and $\mathrm{CN}$ Which one of these will have the highest bond order?

- (1) $\mathrm{CN^{+}}$
- **(2)** $\mathrm{CN^{-}}$
- (3) $\mathrm{NO}$
- (4) $\mathrm{CN}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\mathrm{NO}$ : $(\sigma 1s)^{2}$, $(\sigma^{*}1s)^{2}$, $(\sigma 2s)^{2}$,$(\sigma^{*}2s)^{2}$,$(\sigma 2p_{z})^{2}$, $(\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}$,$(\pi^{*}2p_{x})^{1} = (\pi^{*}2p_{y})^{0}$
2. $\mathrm{BO} = \frac{10-5}{2} = 2.5$
3. $\mathrm{CN^{-}}$ : $(\sigma 1s)^{2}$, $(\sigma^{*}1s)^{2}$, $(\sigma 2s)^{2}$,$(\sigma^{*}2s)^{2}$, $(\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}$,$(\sigma 2p_{z})^{2}$
4. $\mathrm{BO} = \frac{10-4}{2} = 3$
5. $\mathrm{CN}$ : $(\sigma 1s)^{2}$, $(\sigma^{*}1s)^{2}$, $(\sigma 2s)^{2}$,$(\sigma^{*}2s)^{2}$, $(\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}$,$(\sigma 2p_{z})^{1}$
6. $\mathrm{BO} = \frac{9-4}{2} = 2.5$
7. $\mathrm{CN^{+}}$ : $(\sigma 1s)^{2}$, $(\sigma^{*}1s)^{2}$, $(\sigma 2s)^{2}$,$(\sigma^{*}2s)^{2}$, $(\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}$
8. $\mathrm{BO} = \frac{8-4}{2} = 2$
9. Hence, option(2) should be the right answer.

**Solved independently** (answer withheld)

1. Count electrons: $\mathrm{C}=6$, $\mathrm{N}=7$, $\mathrm{O}=8$, so $\mathrm{CN^{+}}=12$, $\mathrm{CN}=13$, $\mathrm{CN^{-}}=14$, $\mathrm{NO}=15$.
2. $\mathrm{CN^{+}}$ (12 e$^-$): $\text{BO} = \frac{8-4}{2} = 2$.
3. $\mathrm{CN}$ (13 e$^-$): $\text{BO} = \frac{9-4}{2} = 2.5$.
4. $\mathrm{CN^{-}}$ (14 e$^-$, isoelectronic with $\mathrm{N_2}$): $\text{BO} = \frac{10-4}{2} = 3$.
5. $\mathrm{NO}$ (15 e$^-$): $\text{BO} = \frac{10-5}{2} = 2.5$.
6. Highest bond order is $3$ for $\mathrm{CN^{-}}$, which is option $2$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 21)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q087_804344e7_27102026.png?v=804344e7ab60)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q087_adff510a_27102026.png?v=adff510a9707)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Bond order is $\frac{N_b-N_a}{2}$ read off the MO filling, so the $14$-electron species isoelectronic with $\mathrm{N_2}$ carries the triple bond.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  The three CN species rise in bond order as electrons are added at $12$, $13$ and $14$, so continuing 'more electrons, stronger bond' to NO's $15$ lands on NO, whose extra electron in fact enters an antibonding $\pi^*$ and pulls the order down to $2.5$.
- **Why:** This question requires the bond-order rule applied to species for which no values are supplied, demonstrated by 'Which one of these will have the highest bond order?' asked over the printed set $\mathrm{CN^+}$, $\mathrm{CN^-}$, $\mathrm{NO}$ and $\mathrm{CN}$.
<!--/ecat-->

## Q88

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Magnesium reacts with an element (X) to form an ionic compound. If the ground state electronic configuration of (X) is $1s^{2}\,2s^{2}\,2p^{3}$, the simplest formula for this compound is

- (1) $\mathrm{Mg_2X}$
- (2) $\mathrm{MgX_2}$
- (3) $\mathrm{Mg_2X_3}$
- **(4)** $\mathrm{Mg_3X_2}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Element $(\mathrm{X})$ electronic configuration
2. $1s^{2}\,2s^{2}\,2p^{3}$
3. So, valency of $\mathrm{X}$ will be $3$.
4. Valency of $\mathrm{Mg}$ is $2$.
5. Formula of compound formed by $\mathrm{Mg}$ and $\mathrm{X}$ will be $\mathrm{Mg_3X_2}$.

**Solved independently** (answer withheld)

1. The configuration $1s^{2}\,2s^{2}\,2p^{3}$ has $7$ electrons, so X is nitrogen with $3$ valence electrons short of an octet in $2p$.
2. X gains $3$ electrons to form $\mathrm{X^{3-}}$, while Mg loses $2$ electrons to form $\mathrm{Mg^{2+}}$.
3. Charge balance: $3(+2) + 2(-3) = 0$, so the formula is $\mathrm{Mg_3X_2}$, which is option $4$.

**Subtopic:** Covalent and Ionic Bond · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q088_3606e3da_27102026.png?v=3606e3dabc5d)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q088_ec0228d0_27102026.png?v=ec0228d0719a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An ionic formula comes from crossing the ion charges: $1s^{2}\,2s^{2}\,2p^{3}$ is five valence electrons, three short of an octet, so $\mathrm{X^{3-}}$ with $\mathrm{Mg^{2+}}$ gives $\mathrm{Mg_3X_2}$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Writing each element's own valency as its own subscript instead of crossing them states the $3:2$ ratio backwards, so the $2$ lands on magnesium and the $3$ on X.
- **Why:** This question requires a valency rule applied to data supplied in the stem, demonstrated by 'If the ground state electronic configuration of (X) is $1s^{2}\,2s^{2}\,2p^{3}$, the simplest formula for this compound is'.
<!--/ecat-->

## Q89

Chemistry · physical · The Solid State

Iron exhibits bcc structure at room temperature. Above $900^\circ\mathrm{C}$, it transforms to fcc structure. The ratio of density of iron at room temperature to that at $900^\circ\mathrm{C}$ (assuming molar mass and atomic radii of iron remains constant with temperature) is

- **(1)** $\frac{3\sqrt{3}}{4\sqrt{2}}$
- (2) $\frac{4\sqrt{3}}{3\sqrt{2}}$
- (3) $\frac{\sqrt{3}}{\sqrt{2}}$
- (4) $\frac{1}{2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For BCC lattice : $Z = 2$, $a = \frac{4r}{\sqrt{3}}$
2. For FCC lattice : $Z = 4$, $a = 2\sqrt{2}\,r$
3. $\therefore \frac{d_{25^\circ\mathrm{C}}}{d_{900^\circ\mathrm{C}}} = \frac{\left(\frac{ZM}{N_A a^3}\right)_{\mathrm{BCC}}}{\left(\frac{ZM}{N_A a^3}\right)_{\mathrm{FCC}}}$
4. $= \frac{2}{4}\left(\frac{2\sqrt{2}\,r}{\frac{4r}{\sqrt{3}}}\right)^{3}$
5. $= \left(\frac{3\sqrt{3}}{4\sqrt{2}}\right)$

**Solved independently** (answer withheld)

1. Density $d = \frac{Z M}{N_A a^3}$, so with $M$ constant $d \propto \frac{Z}{a^3}$.
2. For bcc, $Z = 2$ and $\sqrt{3}a = 4r$, so $a_{bcc} = \frac{4r}{\sqrt{3}}$.
3. $d_{bcc} \propto \frac{2}{(4r/\sqrt{3})^3} = \frac{2 \cdot 3\sqrt{3}}{64 r^3} = \frac{3\sqrt{3}}{32 r^3}$.
4. For fcc, $Z = 4$ and $\sqrt{2}a = 4r$, so $a_{fcc} = 2\sqrt{2}r$.
5. $d_{fcc} \propto \frac{4}{(2\sqrt{2}r)^3} = \frac{4}{16\sqrt{2} r^3} = \frac{1}{4\sqrt{2} r^3}$.
6. $\frac{d_{bcc}}{d_{fcc}} = \frac{3\sqrt{3}}{32} \times 4\sqrt{2} = \frac{3\sqrt{6}}{8} = \frac{3\sqrt{3}}{4\sqrt{2}}$, which is option $1$.

**Subtopic:** Density and Edge Length Calculations for Cubic Unit Cells · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 22)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q089_fdf74e5d_27102026.png?v=fdf74e5dc5a5)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q089_80c490c6_27102026.png?v=80c490c649ed)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Cubic-cell density is $\rho=\frac{ZM}{a^{3}N_A}$, and a constant atomic radius does not mean a constant edge, because $a=4r/\sqrt{3}$ in bcc and $a=4r/\sqrt{2}$ in fcc.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Reading 'assuming molar mass and atomic radii of iron remains constant' as 'everything except the atoms per cell is constant' leaves $\rho\propto Z$, and the ratio then looks like $2:4=\frac{1}{2}$.
- **Why:** This question requires the cubic-cell density relation chained with the two radius-to-edge relations, demonstrated by options such as '$\frac{3\sqrt{3}}{4\sqrt{2}}$' that contain no quantity the stem supplies a number for.
- **Note:** The answer is printed as a ratio, but nothing is varied against anything else here, so asks is calculate rather than relation: the value is derived from $\rho=\frac{ZM}{a^{3}N_A}$ together with $a=4r/\sqrt{3}$ and $a=4r/\sqrt{2}$, which the brief files as a derivation even when the result is symbolic.
<!--/ecat-->

## Q90

Chemistry · physical · Structure of Atom

Which one is a wrong statement?

- **(1)** ![printed figure: orbital-box diagram of N: $1s^2$ (↑↓), $2s^2$ (↑↓), $2p_x^1$ (↑), $2p_y^1$ (↑), $2p_z^1$ (↓)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q090_option_1_bb2b5368_27102026.svg?v=bb2b5368ad83) *orbital-box diagram of N: $1s^2$ [↑↓], $2s^2$ [↑↓], $2p_x^1$ [↑], $2p_y^1$ [↑], $2p_z^1$ [↓]* — The electronic configuration of N atom is
- (2) An orbital is designated by three quantum numbers while an electron in an atom is designated by four quantum numbers
- (3) Total orbital angular momentum of electron in 's' orbital is equal to zero
- (4) The value of m for $d_{z}2$ is zero

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. According to Hund's Rule of maximum multiplicity, the correct electronic configuration of $\mathrm{N}$-atom is

![printed figure: orbital-box diagrams of N: $1s^2$ (↑↓), $2s^2$ (↑↓), $2p^3$ (↑)(↑)(↑) OR $1s^2$ (↑↓), $2s^2$ (↑↓), $2p^3$ (↓)(↓)(↓)](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/figures_agent/q090_sol_1_9dfe3fe2_27102026.svg?v=9dfe3fe21f9f)

*orbital-box diagrams of N: $1s^2$ [↑↓], $2s^2$ [↑↓], $2p^3$ [↑][↑][↑] OR $1s^2$ [↑↓], $2s^2$ [↑↓], $2p^3$ [↓][↓][↓]*

2. $\therefore$ Option (1) violates Hund's Rule.

**Solved independently** (answer withheld)

1. An orbital is specified by $n, l, m_l$ and an electron additionally by $m_s$, so option $2$ is true.
2. For an $s$ orbital $l = 0$, so orbital angular momentum $\sqrt{l(l+1)}\,\frac{h}{2\pi} = 0$; option $3$ is true.
3. The $d_{z^2}$ orbital is the $m_l = 0$ member of the $d$ set; option $4$ is true.
4. Since options $2$, $3$ and $4$ are correct, the wrong statement is option $1$ (the N atom configuration shown).

**Subtopic:** Filling of Orbitals in Atom · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 22)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q090_c3eac0aa_27102026.png?v=c3eac0aa4d55)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q090_62c883c2_27102026.png?v=62c883c267ba)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Quantum-number bookkeeping: an orbital takes three quantum numbers and an electron four, $l=0$ makes the orbital angular momentum zero, and $d_{z^{2}}$ is the $m=0$ member of the $d$ set.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Option 1, which is the keyed answer, reads 'The electronic configuration of N atom is' and then stops, so the claim the key calls wrong is not in our record; the three readable options were checked and each is a correct statement, which leaves no wrong option whose route could be written.
- **Why:** This question requires four printed claims about orbitals and quantum numbers to be graded one at a time, demonstrated by the stem 'Which one is a wrong statement?' standing above options that are each a standalone claim.
- **Note:** Option 1 is truncated in our record and it is the keyed answer, so under codebook rule 0.5 no trap is written and other_options is left empty; the record should be marked source_incomplete and repaired. A reviewer holding the printed paper should check whether what is missing is an orbital-box diagram for nitrogen with the three $2p$ electrons drawn paired, in which case the mechanism to confirm is the Hund's-rule filling of $2p^{3}$. Also: E1_question_type is the plain_mcq default, but the stem grades whole statements printed as the options, which is the statement_options shape and so qtype statements.
<!--/ecat-->

## Q91

Biology · botany · Photosynthesis in Higher Plants

Oxygen is not produced during photosynthesis by

- (1) Cycas
- (2) Nostoc
- **(3)** Green sulphur bacteria
- (4) Chara

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Green sulphur bacteria do not use $\mathrm{H_2O}$ as source of proton, therefore they do not evolve $\mathrm{O_2}$.

**Solved independently** (answer withheld)

1. Green sulphur bacteria use $\mathrm{H_2S}$ instead of $\mathrm{H_2O}$ as the hydrogen donor, so their photosynthesis is anoxygenic and gives sulphur rather than $\mathrm{O_2}$; Cycas, Nostoc (a cyanobacterium) and Chara all photolyse water and release $\mathrm{O_2}$, so the answer is option $3$.

**Subtopic:** Photosynthesis Experiments · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q091_50436283_27102026.png?v=504362831676)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q091_27d54d3d_27102026.png?v=27d54d3daeba)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Oxygen comes out of photosynthesis only where water is the electron donor; green sulphur bacteria use H2S instead and deposit sulphur, so their photosynthesis is anoxygenic.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Nostoc is the other prokaryote in the option set, so a student holding 'oxygen evolution belongs to plants and algae, bacterial photosynthesis does not evolve oxygen' picks the cyanobacterium and stops there.
- **Why:** This question requires the one named organism NCERT states does not evolve oxygen, demonstrated by the stem 'Oxygen is not produced during photosynthesis by' set against four named photosynthetic organisms.
- **Note:** The task is negated ('not'), and that is where the work sits: three options are oxygen-evolving and one is not.
<!--/ecat-->

## Q92

Biology · botany · Sexual Reproduction in Flowering Plants

Double fertilization is

- (1) Fusion of two male gametes with one egg
- (2) Fusion of one male gamete with two polar nuclei
- (3) Fusion of two male gametes of a pollen tube with two different eggs
- **(4)** Syngamy and triple fusion

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Double fertilization is a unique phenomenon that occur in angiosperms only.
2. Syngamy + Triple fusion = Double fertilization

**Solved independently** (answer withheld)

1. In the embryo sac, one male gamete fuses with the egg (syngamy) and the other fuses with the two polar nuclei (triple fusion); both events together make up double fertilisation, so the answer is option $4$.

**Subtopic:** Double Fertilisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q092_d13a5fcb_27102026.png?v=d13a5fcb05d2)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q092_cc1aa1fc_27102026.png?v=cc1aa1fc9832)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Double fertilisation is the two fusions of one embryo sac taken together: syngamy, one male gamete with the egg, and triple fusion, the other male gamete with the two polar nuclei.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  'Fusion of one male gamete with two polar nuclei' is the textbook's own description of triple fusion, so a student who recognises it as true reads the word double as the two polar nuclei and ticks it.
- **Why:** This question requires NCERT's own naming of the two fusions as one event, demonstrated by option 4 reading 'Syngamy and triple fusion' while option 2 prints only one of the two.
- **Note:** E1's pattern called this statement_options, which is retired vocabulary; no lettered statement block is printed and the stem asks a single question, so under the brief's rule 1 long sentences as options leave qtype at mcq. On the trap axis I weighed half_right as a true but incomplete set, but the printed statement is the complete and accurate definition of a different named event, triple fusion, so answers_other_question says more.
<!--/ecat-->

## Q93

Biology · botany · Organisms and Populations

Which one of the following plants shows a very close relationship with a species of moth, where none of the two can complete its life cycle without the other?

- (1) Banana
- **(2)** Yucca
- (3) Hydrilla
- (4) Viola

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Yucca have an obligate mutualism with a species of moth i.e. Pronuba.

**Solved independently** (answer withheld)

1. The Yucca plant is pollinated only by the Yucca moth, whose larvae develop in the ovary on some seeds, so neither can complete its life cycle without the other; this is option $2$.

**Subtopic:** Mutualism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q093_adfc1592_27102026.png?v=adfc15921dcf)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q093_7a3e6a2d_27102026.png?v=7a3e6a2d69b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Yucca and its moth are the printed obligate mutualism: the moth is the plant's only pollinator and its larvae feed on the developing seeds, so neither completes its life cycle without the other.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  I checked each distractor for a printed partner: banana is carried for parthenocarpy, Hydrilla for water pollination and Viola for cleistogamous flowers, and not one of the three is printed with any animal, let alone a moth; the obligate pairs taught are fig-wasp and Yucca-moth, and only Yucca is in the option set.
- **Why:** This question requires the named mutualistic pair NCERT prints, demonstrated by the stem asking which plant shows a relationship where 'none of the two can complete its life cycle without the other'.
- **Note:** Three fillers here follow from a check rather than from leaving options unexamined: each distractor is a plant carried for a different reproductive phenomenon and none of the three is printed with an animal partner. If a reviewer holds an edition that pairs any of the three with an insect, this should be revisited.
<!--/ecat-->

## Q94

Biology · botany · Sexual Reproduction in Flowering Plants

Pollen grains can be stored for several years in liquid nitrogen having a temperature of

- **(1)** $-196\,^{\circ}\mathrm{C}$
- (2) $-80\,^{\circ}\mathrm{C}$
- (3) $-120\,^{\circ}\mathrm{C}$
- (4) $-160\,^{\circ}\mathrm{C}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Pollen grains can be stored for several years in liquid nitrogen at $-196\,^{\circ}\mathrm{C}$ (Cryopreservation)

**Solved independently** (answer withheld)

1. Pollen banks store pollen grains in liquid nitrogen at $-196\,^{\circ}\mathrm{C}$, which is option $1$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q094_8fca90c5_27102026.png?v=8fca90c5294e)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q094_dfead07d_27102026.png?v=dfead07db5cc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pollen banks keep viable pollen for years in liquid nitrogen, whose temperature is -196 degrees Celsius.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The stem names the coolant, so the whole content of the question is one stored number; I checked the other three values for a route and none is the boiling point of nitrogen, none is bounded or produced by anything in the stem, and none is a rounding of -196.
- **Why:** This question requires the temperature NCERT prints for storing pollen in liquid nitrogen, demonstrated by the stem supplying the coolant - 'stored for several years in liquid nitrogen having a temperature of' - and leaving only the value.
- **Note:** One mechanism I could not confirm from the printed text and a reviewer may want to test: -80 degrees Celsius is the standard deep-freezer figure for biological storage, and if any line in the source attaches it to storing biological material then option 2 becomes answers_other_question rather than a filler.
<!--/ecat-->

## Q95

Biology · botany · Mineral Nutrition

Which of the following elements is responsible for maintaining turgor in cells?

- **(1)** Potassium
- (2) Sodium
- (3) Magnesium
- (4) Calcium

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Potassium helps in maintaining turgidity of cells.

**Solved independently** (answer withheld)

1. As the NCERT mineral nutrition chapter teaches, potassium ($\mathrm{K^+}$) maintains the anion-cation balance and cell turgidity, and it drives stomatal opening and closing, which is option $1$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q095_5fad29c0_27102026.png?v=5fad29c0e680)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q095_a4c283b5_27102026.png?v=a4c283b5fede)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Potassium is the element tied to turgor: it is the cation that moves into the guard cells and sets the anion-cation balance that holds water in the cell.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Sodium is the cation attached to osmotic and water balance everywhere else in the syllabus, so a student reaching for the ion that controls water in a cell names it without checking which elements are essential to plants.
- **Why:** This question requires the element NCERT names for maintaining turgor, demonstrated by the stem 'Which of the following elements is responsible for maintaining turgor in cells?' set against four cations.
- **Note:** On nearby_fact against look_alike_term I applied the swap test: potassium and sodium do not resemble each other as words, and the pull survives renaming, because what carries it is sodium's own osmotic role learnt elsewhere and its being the other monovalent cation taught beside potassium.
<!--/ecat-->

## Q96

Biology · botany · Respiration in Plants

What is the role of $\mathrm{NAD^{+}}$ in cellular respiration?

- (1) It is a nucleotide source for ATP synthesis.
- **(2)** It functions as an electron carrier.
- (3) It functions as an enzyme.
- (4) It is the final electron acceptor for anaerobic respiration.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In cellular respiration, $\mathrm{NAD^{+}}$ act as an electron carrier.

**Solved independently** (answer withheld)

1. $\mathrm{NAD^{+}}$ is reduced to $\mathrm{NADH + H^{+}}$ during glycolysis and the Krebs cycle and carries the electrons to the electron transport system, so it functions as an electron carrier, which is option $2$.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q096_577be08d_27102026.png?v=577be08d849b)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q096_c2346037_27102026.png?v=c234603778a8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NAD+ works as a carrier in respiration: it takes up electrons and hydrogen at the dehydrogenase steps and hands them to the electron transport chain, being reoxidised each round.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  NAD+ really is an electron acceptor, so an option reading 'final electron acceptor for anaerobic respiration' matches the half the student is sure of and adds the word anaerobic, which is where the fate of NADH matters most.
- **Why:** This question requires the role NCERT states for NAD+ in respiration, demonstrated by option 2 reading 'It functions as an electron carrier' against three rival roles offered for the same molecule.
- **Note:** E1's pattern called this statement_options, retired vocabulary; no lettered statement block is printed and the stem asks a single question, so qtype is mcq under the brief's rule 1. On the trap axis the option carries two parts - electron acceptor, true of NAD+, and final acceptor in anaerobic respiration, false - which is the multi-part case half_right is for; wrong_site_attacked was weighed and set aside because no stage of the pathway is misnamed, only NAD+'s standing within it.
<!--/ecat-->

## Q97

Biology · botany · Mineral Nutrition

In which of the following forms is iron absorbed by plants?

- (1) Free element
- (2) Ferrous
- **(3)** Ferric
- (4) Both ferric and ferrous

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Iron is absorbed by plants in the form of ferric ions. (According to NCERT)
2. *Plants absorb iron in both form i.e. $\mathrm{Fe^{++}}$ and $\mathrm{Fe^{+++}}$. (Preferably $\mathrm{Fe^{++}}$)

**Solved independently** (answer withheld)

1. NCERT (Mineral Nutrition) states that plants obtain iron in the form of ferric ions, $\mathrm{Fe^{3+}}$, which is option $3$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q097_f6ed3626_27102026.png?v=f6ed36262260)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q097_1afc2659_27102026.png?v=1afc2659a879)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The mineral nutrition chapter gives the absorbed form of iron as the ferric ion, Fe3+, not the free metal and not the ferrous ion.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Ferric and ferrous are one stem with the two oxidation-state endings, so a student who recalls that iron enters as an ion but not which ending carries Fe3+ takes ferrous.
- **Why:** This question requires the absorbed form the chapter states for iron, demonstrated by the options setting 'Ferrous' against 'Ferric' as the only difference between them.
- **Note:** The answer line is printed 'Answer (3*)' and our record does not say what the asterisk marks; accepted_answers holds only '3', so the tags follow option 3 as printed. The doubt is worth recording because plant physiology outside the textbook has Fe2+ taken up at the root after reduction, which makes 'Ferrous' defensible on the subject while the key rests on the textbook's printed line - a reviewer should establish what the asterisk means in the source.
<!--/ecat-->

## Q98

Biology · both · Biotechnology and Its Applications

Which of the following is commonly used as a vector for introducing a DNA fragment in human lymphocytes?

- (1) $\lambda$ phage
- (2) Ti plasmid
- **(3)** Retrovirus
- (4) pBR 322

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Retrovirus is commonly used as vector for introducing a DNA fragment in human lymphocyte.
2. Gene therapy : Lymphocyte from blood of patient are grown in culture outside the body, a functional gene is introduced by using a retroviral vector, into these lymphocyte.

**Solved independently** (answer withheld)

1. Disarmed retroviruses, which can infect animal cells and integrate their DNA, are the vectors used to introduce DNA into human cells such as lymphocytes, so the answer is option $3$ (Ti plasmid is for plants; $\lambda$ phage and pBR 322 are for E. coli).

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q098_98e60cca_27102026.png?v=98e60cca06a3)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q098_c93627e4_27102026.png?v=c93627e432f4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A gene is carried into a human cell by a retroviral vector; the plasmid and phage vectors of the chapter work in bacteria and in plants.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Strike out the stem's 'in human lymphocytes' and pBR 322 answers 'which is commonly used as a vector', because it is the vector the chapter prints and diagrams.
- **Why:** This question requires the vector the chapter states for human cells, demonstrated by the stem's printed condition 'in human lymphocytes'.
<!--/ecat-->

## Q99

Biology · both · Biotechnology and Its Applications

Use of bioresources by multinational companies and organisations without authorisation from the concerned country and its people is called

- (1) Biodegradation
- **(2)** Biopiracy
- (3) Bio-infringement
- (4) Bioexploitation

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Biopiracy is term used for or refer to the use of bioresources by multinational companies and other organisation without proper authorisation from the countries and people concerned with compensatory payment (definition of biopiracy given in NCERT).

**Solved independently** (answer withheld)

1. Using a country's bioresources without authorisation from that country and its people is called $\text{biopiracy}$, which is option $2$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q099_fce75d77_27102026.png?v=fce75d77e71c)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q099_5e9bc84b_27102026.png?v=5e9bc84bf3a6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Taking a country's bioresources or traditional knowledge without its authorisation and without sharing the benefit is biopiracy.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the other three against the chapter. 'Biodegradation' is the ecology word for the breaking down of material by microbes and touches none of the stem's printed terms - bioresources, authorisation, multinational companies. 'Bio-infringement' and 'Bioexploitation' name no defined concept in the chapter, whose words for this are patent, benefit sharing and biopiracy, so there is no stated sentence that could be misremembered into either; the only one of the four the chapter uses is the key.
- **Why:** This question requires the term the chapter states for unauthorised use of bioresources, demonstrated by the stem reproducing its definition - 'without authorisation from the concerned country and its people'.
- **Note:** The finding here is no_trap: of the three wrong options one is a real term belonging to another chapter's subject matter and two are compounds that no line of this chapter uses, so none carries a route from a stated fact.
<!--/ecat-->

## Q100

Biology · both · Biotechnology and Its Applications

In India, the organisation responsible for assessing the safety of introducing genetically modified organisms for public use is

- (1) Research Committee on Genetic Manipulation (RCGM)
- (2) Council for Scientific and Industrial Research (CSIR)
- (3) Indian Council of Medical Research (ICMR)
- **(4)** Genetic Engineering Appraisal Committee (GEAC)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Indian Government has setup organisation such as GEAC (Genetic Engineering Appraisal Committee) which will make decisions regarding the validity of GM research and safety of introducing GM-organism for public services. (Direct from NCERT).

**Solved independently** (answer withheld)

1. As NCERT teaches, the Indian Government set up the Genetic Engineering Appraisal Committee (GEAC) to decide on the validity of GM research and the safety of introducing GM organisms for public services, which is option $4$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q100_2a9bc176_27102026.png?v=2a9bc176b1db)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q100_312a479f_27102026.png?v=312a479f087f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** GEAC is the Indian body that clears the release of a genetically modified organism for public use.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  RCGM is the other committee standing over genetic manipulation in India, the one that oversees the research stage, so a student who holds 'a committee on genetic manipulation' without which stage it clears takes the name that repeats the stem's words.
- **Why:** This question requires the body the chapter names for GM clearance, demonstrated by the stem's 'responsible for assessing the safety of introducing genetically modified organisms for public use'.
- **Note:** E1_question_type reads statement_options, but each option is an organisation's name with its abbreviation rather than a statement to be judged, so the printed shape is a plain mcq. Option 1 is printed 'Research Committee on Genetic Manipulation (RCGM)' while the body is the Review Committee on Genetic Manipulation; this does not touch the key.
<!--/ecat-->

## Q101

Biology · both · Biotechnology: Principles and Processes

The correct order of steps in Polymerase Chain Reaction (PCR) is

- (1) Denaturation, Extension, Annealing
- (2) Annealing, Extension, Denaturation
- (3) Extension, Denaturation, Annealing
- **(4)** Denaturation, Annealing, Extension

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. This technique is used for making multiple copies of gene (or DNA) of interest in vitro.
2. Each cycle has three steps
3. (i) Denaturation
4. (ii) Primer annealing
5. (iii) Extension of primer

**Solved independently** (answer withheld)

1. Each PCR cycle runs denaturation (strand separation), then primer annealing, then extension by thermostable DNA polymerase, which is option $4$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q101_f294a6d6_27102026.png?v=f294a6d6027e)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q101_6e5a2e27_27102026.png?v=6e5a2e27f0c0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** One PCR cycle melts the duplex, lets the primers bind the single strands and then lets the polymerase copy from them: denaturation, annealing, extension.
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Annealing read as the two separated template strands pairing up again puts that step after the copying, which keeps denaturation in first place and lands on denaturation-extension-annealing.
- **Why:** This question requires the stated sequence of one PCR cycle, demonstrated by the stem's 'The correct order of steps'; no option prints that order inverted, so option 1 is tagged as the annealing step placed at the wrong stage rather than as reversed, which the rulebook withholds from a single swapped pair.
- **Note:** Options 2 and 3 are the correct cycle rotated to a different starting step, which is why both are recorded as traps rather than as filler.
<!--/ecat-->

## Q102

Biology · both · Molecular Basis of Inheritance

Select the correct match

- (1) T.H. Morgan - Transduction
- (2) $\mathrm{F_2}$ $\times$ Recessive parent - Dihybrid cross
- **(3)** Ribozyme - Nucleic acid
- (4) G. Mendel - Transformation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ribozyme is a catalytic RNA, which is nucleic acid.

**Solved independently** (answer withheld)

1. T.H. Morgan worked on linkage and recombination in $Drosophila$, not transduction, so option $1$ is wrong.
2. Crossing an offspring with the recessive parent is a test cross, not a dihybrid cross, so option $2$ is wrong.
3. A ribozyme is a catalytic RNA, which is a nucleic acid, so option $3$ is correct.
4. Transformation was discovered by Griffith, not G. Mendel, so option $4$ is wrong.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q102_266c798c_27102026.png?v=266c798cbb05)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q102_9b528310_27102026.png?v=9b528310d140)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A ribozyme is an RNA, that is a nucleic acid acting as an enzyme; transformation belongs to Griffith and transduction to Zinder and Lederberg, not to Mendel or Morgan.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The discoverers of transduction are held far less firmly than Griffith's transformation, so a student who can strike out 'G. Mendel - Transformation' has nothing left with which to strike out 'T.H. Morgan - Transduction' and accepts it as the correct match.
- **Why:** This question requires the one stated association each printed pair claims, demonstrated by 'Ribozyme - Nucleic acid' holding while the other three attach a process to the wrong worker or the wrong cross; the pull on 'T.H. Morgan - Transduction' survives if the names are swapped for unlike ones, because what carries it is the block of classical attributions printed together and not any likeness between 'Morgan' and 'Zinder', so the trap is nearby_fact.
- **Note:** E1_question_type reads match_the_lists, but no two columns and no pairing code are printed: each option is a single pair accepted or rejected whole, carried here as qtype statements.
<!--/ecat-->

## Q103

Biology · both · Biotechnology and Its Applications

A ‘new’ variety of rice was patented by a foreign company, though such varieties have been present in India for a long time. This is related to

- (1) Lerma Rojo
- (2) Sharbati Sonora
- (3) Co-667
- **(4)** Basmati

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In 1997, an American company got patent rights on Basmati rice through the US patent and trademark office that was actually been derived from Indian farmer’s varieties.
2. The diversity of rice in India is one of the richest in the world, 27 documented varieties of Basmati are grown in India.
3. Indian basmati was crossed with semi-dwarf varieties and claimed as an invention or a novelty.
4. Sharbati Sonora and Lerma Rojo are varieties of wheat.

**Solved independently** (answer withheld)

1. Patenting a rice variety that has long been grown in India is the biopiracy case of Basmati rice, patented by a US company, so the answer is option $4$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q103_3b94f541_27102026.png?v=3b94f5419f05)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q103_154ebec4_27102026.png?v=154ebec422be)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biopiracy: Basmati is the Indian rice whose 'new' variety was patented abroad although Indian farmers had grown it for centuries
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Lerma Rojo is the one plainly foreign name among four variety names, so a student matching the stem's 'patented by a foreign company' to a name instead of to the crop lands there; the stem says rice, and Lerma Rojo is a wheat variety.
- **Why:** This question requires the one named variety NCERT records in its biopiracy example, demonstrated by 'patented by a foreign company, though such varieties have been present in India for a long time', which points at a documented case rather than at a criterion to apply.
<!--/ecat-->

## Q104

Biology · both · Principles of Inheritance and Variation

Which of the following pairs is wrongly matched?

- (1) XO type sex determination : Grasshopper
- (2) ABO blood grouping : Co-dominance
- **(3)** Starch synthesis in pea : Multiple alleles
- (4) T.H. Morgan : Linkage

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Starch synthesis in pea is controlled by pleiotropic gene.
2. Other options (1, 2 & 4) are correctly matched.

**Solved independently** (answer withheld)

1. Grasshopper males are $XO$, so XO type sex determination : Grasshopper is correct.
2. In ABO blood groups $I^A$ and $I^B$ are both expressed in $I^AI^B$, so ABO : Co-dominance is correct.
3. T.H. Morgan worked out linkage in $Drosophila$, so T.H. Morgan : Linkage is correct.
4. Starch synthesis in pea is controlled by one gene (alleles $B$, $b$); seed starch grain size shows incomplete dominance and the gene has pleiotropic effects, not multiple alleles, so option $3$ is the wrongly matched pair.

**Subtopic:** Incomplete Dominance & Co-dominance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q104_32f4e12b_27102026.png?v=32f4e12b4f36)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q104_3367c0d4_27102026.png?v=3367c0d41f2e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT's worked examples of inheritance patterns: starch synthesis in pea is its incomplete-dominance case, while ABO blood grouping carries both co-dominance and multiple allelism
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  ABO is the chapter's headline multiple-allele example, so a student holding that single tag reads 'Co-dominance' as the planted error and marks this pair as the mismatch; NCERT uses ABO for both, since alleles A and B are co-dominant in group AB.
- **Why:** This question requires each printed concept-to-example pairing to be checked against the one the chapter states, demonstrated by option 3's 'Starch synthesis in pea : Multiple alleles', where the pea starch gene is the text's incomplete-dominance case.
- **Note:** The pattern called this statement_options; the printed options are concept-example pairs accepted or rejected whole, which the retired vocabulary calls pair_options. Both map to qtype statements, so the recorded shape is unaffected.
<!--/ecat-->

## Q105

Biology · both · Principles of Inheritance and Variation

Select the correct statement

- (1) Spliceosomes take part in translation
- **(2)** Punnett square was developed by a British scientist
- (3) Franklin Stahl coined the term ‘‘linkage’’
- (4) Transduction was discovered by S. Altman

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Punnett square was developed by a British geneticist, Reginald C. Punnett.
2. Franklin Stahl proved semi-conservative mode of replication.
3. Transduction was discovered by Zinder and Laderberg.
4. Spliceosome formation is part of post-transcriptional change in Eukaryotes

**Solved independently** (answer withheld)

1. Spliceosomes remove introns during $\text{hnRNA}$ splicing, not translation, so option $1$ is false.
2. The Punnett square was devised by Reginald C. Punnett, a British geneticist, so option $2$ is true.
3. The term linkage was coined by T. H. Morgan, not Franklin Stahl, so option $3$ is false.
4. Transduction was discovered by Zinder and Lederberg, not S. Altman, so option $4$ is false; the answer is option $2$.

**Subtopic:** Monohybrid Cross · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 24)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q105_189115a0_27102026.png?v=189115a0e734)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q105_bacfc17b_27102026.png?v=bacfc17b7350)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Attribution of the standard genetics tools and terms: the Punnett square is named after Reginald Punnett, a British geneticist
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Splicing sits one step away from translation in the central dogma, so a student who has learnt the spliceosome as the machine that works on mRNA accepts the verb from the next step; the spliceosome removes introns from pre-mRNA in the nucleus, before any ribosome is involved.
- **Why:** This question requires four separate stated facts to be checked one at a time against the text, demonstrated by option 2's 'Punnett square was developed by a British scientist' standing alone as a claim with no lettered block to select from.
<!--/ecat-->

## Q106

Biology · both · Molecular Basis of Inheritance

The experimental proof for semiconservative replication of DNA was first shown in a

- (1) Plant
- **(2)** Bacterium
- (3) Fungus
- (4) Virus

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Semi-conservative DNA replication was first shown in Bacterium $\textit{Escherichia coli}$ by Matthew Meselson and Franklin Stahl.

**Solved independently** (answer withheld)

1. Meselson and Stahl (1958) gave the first experimental proof of semiconservative replication by growing $E.\ coli$ in $^{15}\mathrm{N}$ medium, then $^{14}\mathrm{N}$, and separating DNA by CsCl density gradient; $E.\ coli$ is a bacterium, which is option $2$.

**Subtopic:** Experimental Proof that DNA is Semiconservative · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q106_73d347ea_27102026.png?v=73d347ea10cf)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q106_3826e3de_27102026.png?v=3826e3decf45)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Meselson and Stahl's heavy-nitrogen experiment on E. coli is the first demonstration of semiconservative DNA replication; Taylor's Vicia faba work extended it to higher organisms
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  A plant demonstration of semiconservative replication genuinely exists - Taylor's tritiated-thymidine work on Vicia faba root tips, printed in the same section - so a student who recalls that experiment answers 'plant'; the stem's word 'first' is what sends the answer to the E. coli culture.
- **Why:** This question requires the organism of the first demonstration, demonstrated by the stem's 'was first shown in a', which separates the E. coli experiment from the later plant demonstration.
<!--/ecat-->

## Q107

Biology · botany · Reproduction in Organisms

Which of the following flowers only once in its life-time?

- (1) Mango
- (2) Jackfruit
- **(3)** Bamboo species
- (4) Papaya

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Bamboo species are monocarpic i.e., flower generally only once in its life-time after $50$-$100$ years.
2. Jackfruit, papaya and mango are polycarpic i.e., produce flowers and fruits many times in their life-time.

**Solved independently** (answer withheld)

1. Bamboo species flower only once in their life-time, generally after $50$-$100$ years, while mango, jackfruit and papaya flower every season, so the answer is option $3$.

**Subtopic:** Phases of Life Cycle: Juvenile and Reproductive Phase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q107_a7f89cb4_27102026.png?v=a7f89cb4f05e)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q107_438f0d03_27102026.png?v=438f0d03e1a4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Monocarpic flowering: bamboo species grow vegetatively for decades, flower once, fruit and die
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each of the other three against the stem's own criterion, 'flowers only once in its life-time': mango, jackfruit and papaya all flower and fruit in successive seasons, so each contradicts the criterion instead of competing with bamboo, and the chapter's once-in-a-lifetime examples are bamboo and Strobilanthus kunthiana.
- **Why:** This question requires the named plant the chapter gives as flowering once in its lifetime, demonstrated by the stem's 'flowers only once in its life-time' matching the bamboo example.
- **Note:** Recorded as no_trap after examining all three wrong options, not in place of examining them: each is a perennial fruit tree whose flowering habit contradicts the stem's criterion, so none offers a route a prepared student walks.
<!--/ecat-->

## Q108

Biology · botany · Reproduction in Organisms

Offsets are produced by

- (1) Parthenocarpy
- **(2)** Mitotic divisions
- (3) Meiotic divisions
- (4) Parthenogenesis

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Offset is a vegetative part of a plant, formed by mitosis.
2. Meiotic divisions do not occur in somatic cells.
3. Parthenogenesis is the formation of embryo from ovum or egg without fertilisation.
4. Parthenocarpy is the fruit formed without fertilisation, (generally seedless)

**Solved independently** (answer withheld)

1. Offsets (e.g. in water hyacinth) are vegetative propagules of asexual reproduction, formed from somatic cells by mitosis, so the answer is option $2$.

**Subtopic:** Asexual Reproduction and Vegetative Propagation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q108_e250bc21_27102026.png?v=e250bc21a769)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q108_32582aad_27102026.png?v=32582aad875d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Offsets are vegetative propagules: a lateral shoot built by ordinary mitotic division, so the daughter plant is a clone of the parent
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  'Meiotic' and 'mitotic' are one letter apart, and the student carries 'reproduction runs through meiosis', so the reduction division is picked for a structure that copies the parent exactly; only mitosis keeps the chromosome number and the genotype unchanged.
- **Why:** This question requires the kind of nuclear division behind a vegetative propagule, demonstrated by the options setting 'Mitotic divisions' against 'Meiotic divisions' for a structure that reproduces the parent plant.
<!--/ecat-->

## Q109

Biology · both · Molecular Basis of Inheritance

Select the correct match

- (1) Matthew Meselson and F. Stahl - Pisum sativum
- (2) Alfred Hershey and Martha Chase - TMV
- (3) Alec Jeffreys - Streptococcus pneumoniae
- **(4)** Francois Jacob and Jacques Monod - Lac operon

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Francois Jacob and Jacque Monod proposed model of gene regulation known as operon model/lac operon.
2. Alec Jeffreys – DNA fingerprinting technique.
3. Matthew Meselson and F. Stahl – Semi-conservative DNA replication in E. coli.
4. Alfred Hershey and Martha Chase – Proved DNA as genetic material not protein

**Solved independently** (answer withheld)

1. Meselson and Stahl used $E.\ coli$, not $Pisum\ sativum$; Hershey and Chase used bacteriophage, not TMV; Alec Jeffreys devised DNA fingerprinting, not work on $Streptococcus\ pneumoniae$ (Griffith); Jacob and Monod proposed the lac operon, so option $4$ is correct.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q109_23749fee_27102026.png?v=23749fee1d19)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q109_d66aaebc_27102026.png?v=d66aaebc9610)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each classic genetics experiment is tied to one material: Jacob and Monod built the lac operon model, Meselson and Stahl used E. coli, Hershey and Chase used bacteriophage
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Hershey and Chase did work on a virus, so a student holding only 'they used viruses' accepts TMV; their virus was bacteriophage T2, and TMV is the material of the work on RNA as genetic material.
- **Why:** This question requires each worker to be held together with the material actually used, demonstrated by option 4's 'Francois Jacob and Jacques Monod - Lac operon' being the only pair whose two halves come out of one printed account.
- **Note:** E1_question_type reads match_the_lists, but no two lists are printed and list_i and list_ii are both empty: the shape on the page is four worker-material pairs each accepted or rejected whole, which the retired vocabulary calls pair_options and which maps to qtype statements.
<!--/ecat-->

## Q110

Biology · botany · Sexual Reproduction in Flowering Plants

Which of the following has proved helpful in preserving pollen as fossils?

- (1) Oil content
- (2) Cellulosic intine
- (3) Pollenkitt
- **(4)** Sporopollenin

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sporopollenin cannot be degraded by enzyme; strong acids and alkali, therefore it is helpful in preserving pollen as fossil.
2. Pollenkitt – Help in insect pollination.
3. Cellulosic Intine – Inner sporoderm layer of pollen grain known as intine made up cellulose & pectin.
4. Oil content – No role is pollen preservation.

**Solved independently** (answer withheld)

1. The pollen exine is made of sporopollenin, which resists high temperatures, strong acids and alkalis, and no enzyme is known to degrade it, so it preserves pollen as fossils: option $4$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q110_502ea9ae_27102026.png?v=502ea9aead8f)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q110_0bf29405_27102026.png?v=0bf29405ac11)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Sporopollenin in the exine is one of the most resistant organic materials known, which is why pollen grains survive as fossils
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The intine is the other pollen-wall layer and the option names its material correctly, so a student who holds the two-layer wall but not which layer is the tough one picks it; the resistant material is sporopollenin in the outer exine, while the intine is a thin layer of cellulose and pectin.
- **Why:** This question requires the component the chapter gives as the cause of pollen's survival, demonstrated by the stem granting that pollen is preserved as fossils and asking which material 'has proved helpful' in it.
- **Note:** asks is reason_line rather than fact_line because the stem grants the observation - pollen preserved as fossils - and sets four rival components against each other to account for it.
<!--/ecat-->

## Q111

Biology · botany · Organisms and Populations

Natality refers to

- (1) Number of individuals leaving the habitat
- **(2)** Birth rate
- (3) Death rate
- (4) Number of individuals entering a habitat

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Natality refers to birth rate.
2. Death rate – Mortality
3. Number of individual entering a habitat is – Immigration
4. Number of individual leaving the habital – Emigration

**Solved independently** (answer withheld)

1. Natality is the number of births during a given period in the population that add to the initial density, i.e. the birth rate, which is option $2$.

**Subtopic:** Life History Variation and Population Attributes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q111_ca180b8a_27102026.png?v=ca180b8a1515)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q111_bfb825f5_27102026.png?v=bfb825f5389f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Natality is the birth rate, the number added to a population per unit time; mortality, immigration and emigration are the other three population attributes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Natality and mortality are learnt as one rhyming pair of rates, and here only the definitions are printed, so a student who has not pinned which word is which reads 'natality' as the loss term; natality shares its root with natal and native, and is the birth rate.
- **Why:** This question requires the stated definition of one of the four population attributes, demonstrated by 'Natality refers to' with the options printing the definitions of birth rate, death rate, immigration and emigration.
<!--/ecat-->

## Q112

Biology · botany · Environmental Issues

World Ozone Day is celebrated on

- **(1)** $16^{\text{th}}$ September
- (2) $21^{\text{st}}$ April
- (3) $5^{\text{th}}$ June
- (4) $22^{\text{nd}}$ April

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. World Ozone day is celebrated on $16^{\text{th}}$ September.
2. $5^{\text{th}}$ June - World Environment Day
3. $21^{\text{st}}$ April - National Yellow Bat Day
4. $22^{\text{nd}}$ April - National Earth Day

**Solved independently** (answer withheld)

1. World Ozone Day marks the signing of the Montreal Protocol on $16^{\text{th}}$ September 1987, so it falls on $16^{\text{th}}$ September, which is option $1$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q112_d1aba15d_27102026.png?v=d1aba15d8251)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q112_653f4aa4_27102026.png?v=653f4aa4da52)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** World Ozone Day falls on 16 September, the anniversary of the signing of the Montreal Protocol
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  5 June is World Environment Day, the environmental date the chapter and the school calendar repeat most, so it is produced when any environmental-date question is asked; the ozone day is 16 September.
- **Why:** This question requires a stored calendar date, demonstrated by 'World Ozone Day is celebrated on' with four observance dates as options and nothing in the stem to reason from.
- **Note:** The question turns on a date rather than on subject content; tagged as printed.
<!--/ecat-->

## Q113

Biology · botany · Environmental Issues

Which of the following is a secondary pollutant?

- (1) $\mathrm{SO_2}$
- (2) $\mathrm{CO_2}$
- (3) $\mathrm{CO}$
- **(4)** $\mathrm{O_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{O_3}$ (ozone) is a secondary pollutant.
2. These are formed by the reaction of primary pollutant.
3. $\mathrm{CO}$ – Quantitative pollutant
4. $\mathrm{CO_2}$ – Primary pollutant
5. $\mathrm{SO_2}$ – Primary pollutant

**Solved independently** (answer withheld)

1. SO$_2$, CO$_2$ and CO are emitted directly from sources such as fuel combustion, so they are primary pollutants; O$_3$ forms in the air when NO$_x$ and hydrocarbons react in sunlight, so $\mathrm{O_3}$ (option $4$) is the secondary pollutant.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q113_b2954ffa_27102026.png?v=b2954ffaf907)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q113_c58cfaa6_27102026.png?v=c58cfaa65314)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Primary pollutants are emitted as such; a secondary pollutant such as tropospheric ozone is manufactured in the air out of primary pollutants and sunlight
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  SO2 is the pollutant a student holds with an atmospheric afterlife attached - it is converted to sulphuric acid in acid rain - so the word secondary finds it; what is secondary in that story is the acid, while SO2 itself leaves the chimney already as SO2.
- **Why:** This question requires which named gas carries the printed label 'secondary pollutant', demonstrated by 'Which of the following is a secondary pollutant?' offering four gases with no criterion stated in the stem to apply.
<!--/ecat-->

## Q114

Biology · botany · Organisms and Populations

Niche is

- (1) the range of temperature that the organism needs to live
- (2) the physical space where an organism lives
- (3) all the biological factors in the organism's environment
- **(4)** the functional role played by the organism where it lives

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ecological niche was termed by J. Grinnel.
2. It refers the functional role played by the organism where it lives.

**Solved independently** (answer withheld)

1. NCERT: each organism has a range of conditions it can tolerate, resources it uses and a distinct functional role in the ecosystem, together called its niche; so niche is the functional role played by the organism where it lives, which is option $4$.

**Subtopic:** Biome, Environmental Factors & Four Levels of Biological Organisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q114_25d282cb_27102026.png?v=25d282cb065e)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q114_865fd031_27102026.png?v=865fd031e919)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Niche is the functional role an organism plays where it lives - habitat is the address, niche is the profession
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  That sentence is the definition of habitat, the term introduced in the same breath as niche, so a student who has kept the two as one idea picks it; the niche is what the organism does there, not the space it sits in.
- **Why:** This question requires the strict definition of niche held apart from its neighbouring terms, demonstrated by option 2's 'the physical space where an organism lives', which is the definition of habitat.
<!--/ecat-->

## Q115

Biology · botany · Ecosystem

What type of ecological pyramid would be obtained with the following data?
Secondary consumer : $120\,\mathrm{g}$
Primary consumer : $60\,\mathrm{g}$
Primary producer : $10\,\mathrm{g}$

- (1) Upright pyramid of numbers
- (2) Pyramid of energy
- **(3)** Inverted pyramid of biomass
- (4) Upright pyramid of biomass

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The given data depicts the inverted pyramid of biomass, usually found in aquatic ecosystem.
2. Pyramid of energy is always upright
3. Upright pyramid of biomass and numbers are not possible, as the data depicts primary producer is less than primary consumer and this is less than secondary consumers.

**Solved independently** (answer withheld)

1. The values are given in grams ($\mathrm{g}$), so they measure standing biomass, not numbers or energy.
2. Biomass rises up the trophic levels: $10\,\mathrm{g} < 60\,\mathrm{g} < 120\,\mathrm{g}$, so the producer base is the narrowest level.
3. A pyramid with its narrowest level at the base is inverted, so this is an inverted pyramid of biomass, which is option $3$.

**Subtopic:** Ecological Pyramids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q115_5d678b27_27102026.png?v=5d678b2752e1)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q115_0d25dde2_27102026.png?v=0d25dde2134d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A pyramid of biomass stands on its head whenever the producers' standing crop is smaller than the biomass of the consumers it supports
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The remembered rule that biomass pyramids are upright is carried in and the printed figures are never used; 10 g of producers under 60 g and 120 g above is the case that inverts the pyramid.
- **Why:** This question requires the pyramid rule applied to the supplied standing-crop figures, demonstrated by 'Primary producer : 10 g' sitting under 'Secondary consumer : 120 g'.
- **Note:** asks is apply_rule rather than calculate because the stem's three figures are only compared, with no quantity produced by the student.
<!--/ecat-->

## Q116

Biology · botany · Environmental Issues

In stratosphere, which of the following elements acts as a catalyst in degradation of ozone and release of molecular oxygen?

- (1) $\mathrm{Fe}$
- **(2)** $\mathrm{Cl}$
- (3) Carbon
- (4) Oxygen

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. UV rays act on CFCs, releasing $\mathrm{Cl}$ atoms, chlorine reacts with ozone in sequential method converting into oxygen
2. Carbon, oxygen and $\mathrm{Fe}$ are not related to ozone layer depletion

**Solved independently** (answer withheld)

1. UV radiation in the stratosphere breaks CFCs and releases $\mathrm{Cl}$ atoms, which catalyse the reaction $\mathrm{O_3} \rightarrow \mathrm{O_2}$ without being used up, so the answer is option $2$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q116_a5e7ae65_27102026.png?v=a5e7ae65a962)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q116_f7974d3f_27102026.png?v=f7974d3f8abe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** UV frees chlorine atoms from CFCs in the stratosphere, and each Cl atom degrades ozone to molecular oxygen catalytically, without being used up
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The culprit molecule is a chlorofluorocarbon, so a student who holds 'CFCs destroy ozone' and is now asked for an element picks the element the name ends in; the atom UV releases and that attacks ozone is Cl.
- **Why:** This question requires the element the chapter names as the catalyst of ozone breakdown, demonstrated by 'acts as a catalyst in degradation of ozone and release of molecular oxygen'.
- **Note:** The swap test was applied: carbon and chlorine do not resemble each other as words, and carbon is reachable only because it is printed inside chlorofluorocarbon beside the chlorine, so the label is nearby_fact.
<!--/ecat-->

## Q117

Biology · both · Biomolecules

The two functional groups characteristic of sugars are

- (1) Carbonyl and phosphate
- (2) Carbonyl and methyl
- (3) Hydroxyl and methyl
- **(4)** Carbonyl and hydroxyl

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sugar is a common term used to denote carbohydrate.
2. Carbohydrates are polyhydroxy aldehyde, ketone or their derivatives, which means they have carbonyl and hydroxyl groups.

**Solved independently** (answer withheld)

1. Sugars (carbohydrates) are polyhydroxy aldehydes or ketones, so their characteristic groups are the carbonyl ($\mathrm{C{=}O}$) and the hydroxyl ($\mathrm{-OH}$), which is option $4$.

**Subtopic:** How To Analyse Chemical Composition? · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q117_1faae524_27102026.png?v=1faae52481d0)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q117_f0eb5610_27102026.png?v=f0eb56105d40)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sugars are polyhydroxy aldehydes or ketones, so every sugar carries hydroxyl groups together with one carbonyl group
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Carbonyl is secured from the aldehyde-or-ketone half of the definition, then phosphate is carried over from the sugar-phosphate backbone the student has drawn in nucleotides; the group that stands beside the carbonyl in every sugar is hydroxyl.
- **Why:** This question requires both defining groups at once, demonstrated by 'The two functional groups characteristic of sugars are', with each wrong option offering one right group and one wrong one.
- **Note:** The pattern returned plain_mcq by default, but the stem asks for two groups together and each option is a pair accepted or rejected whole, so the shape recorded is two_part: the answer has two halves and half right scores nothing.
<!--/ecat-->

## Q118

Biology · botany · Biological Classification

Which among the following is not a prokaryote?

- (1) Nostoc
- (2) Mycobacterium
- **(3)** Saccharomyces
- (4) Oscillatoria

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Saccharomyces i.e. yeast is an eukaryote (unicellular fungi)
2. Mycobacterium – a bacterium
3. Oscillatoria and Nostoc are cyanobacteria.

**Solved independently** (answer withheld)

1. $Nostoc$ and $Oscillatoria$ are cyanobacteria, $Mycobacterium$ is a bacterium (all Monera, prokaryotes), while $Saccharomyces$ is yeast, a eukaryotic fungus, so the answer is option $3$.

**Subtopic:** Eubacteria, Ascomycetes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q118_919b269e_27102026.png?v=919b269e2dbc)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q118_3445ad87_27102026.png?v=3445ad87d640)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Cyanobacteria such as Nostoc and Oscillatoria are prokaryotes despite the old name blue-green algae; Saccharomyces is a yeast, and so a eukaryote
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Nostoc is printed under the old name blue-green algae, and algae are filed with the plant-like eukaryotes, so a student answering from that name marks it as the organism that is not a prokaryote; cyanobacteria sit in Monera and have no nucleus.
- **Why:** This question requires the one named organism that sits outside Monera, demonstrated by 'Which among the following is not a prokaryote?' printing two cyanobacteria, one bacterium and one yeast.
- **Note:** The blue-green-algae route stands equally on option 4; it is recorded as the trap on option 1 because Nostoc is the genus the cyanobacteria sentence names, and option 4 carries the same route as an other_options trap rather than being treated as filler.
<!--/ecat-->

## Q119

Biology · both · Cell: The Unit of Life

The Golgi complex participates in

- (1) Respiration in bacteria
- **(2)** Formation of secretory vesicles
- (3) Fatty acid breakdown
- (4) Activation of amino acid

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Golgi complex, after processing releases secretory vesicles from their trans-face.

**Solved independently** (answer withheld)

1. The Golgi complex packages and modifies materials from the ER and buds them off as secretory vesicles, so it participates in the formation of secretory vesicles, which is option $2$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q119_df396388_27102026.png?v=df39638872d0)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q119_02c40518_27102026.png?v=02c40518db17)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Golgi apparatus packages and dispatches: it glycosylates what the ER sends it and buds the material off as secretory vesicles
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Fatty acid breakdown belongs to the microbodies and mitochondria printed a paragraph away in the same run of cell organelles, so a student who holds the organelle list but not which does what assigns it here; the Golgi's printed business is glycosylation and packaging.
- **Why:** This question requires the stated function of a named organelle, demonstrated by 'The Golgi complex participates in' with 'Formation of secretory vesicles' set against three functions belonging to other structures.
<!--/ecat-->

## Q120

Biology · botany · Photosynthesis in Higher Plants

Which of the following is not a product of light reaction of photosynthesis?

- (1) NADPH
- **(2)** NADH
- (3) ATP
- (4) Oxygen

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. ATP, NADPH and oxygen are products of light reaction, while NADH is a product of respiration process.

**Solved independently** (answer withheld)

1. The light reaction produces ATP (photophosphorylation), NADPH (reduction of NADP$^+$) and $O_2$ (photolysis of water); NADH is not one of its products, so the answer is option $2$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q120_11eb5aff_27102026.png?v=11eb5aff6201)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q120_3a1a42ff_27102026.png?v=3a1a42ffb3f6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The light reaction yields ATP, NADPH and O2; NADH is the reduced coenzyme of respiration, not of photosynthesis
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  NADPH and NADH are one letter apart, so a student who holds the two coenzymes the wrong way round - NADH for photosynthesis, NADPH for respiration - reads NADPH as the intruder; photosystem I reduces NADP+, which is why the light reaction's coenzyme is NADPH.
- **Why:** This question requires the light reaction's products held apart from respiration's, demonstrated by the options printing NADPH and NADH side by side under 'not a product of light reaction of photosynthesis'.
<!--/ecat-->

## Q121

Biology · both · Cell: The Unit of Life

Which of the following is true for nucleolus?

- (1) It takes part in spindle formation
- (2) It is a membrane-bound structure
- (3) Larger nucleoli are present in dividing cells
- **(4)** It is a site for active ribosomal RNA synthesis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Nucleolus is a non membranous structure and is a site of r-RNA synthesis.

**Solved independently** (answer withheld)

1. The nucleolus has no membrane, is the site of active ribosomal RNA synthesis, and is larger in cells actively doing protein synthesis rather than in dividing cells. It plays no part in spindle formation, so option $4$ is correct.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q121_8c408564_27102026.png?v=8c40856415c3)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q121_b3d6a2e4_27102026.png?v=b3d6a2e4c04f)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The nucleolus is a non-membrane-bound region of the nucleus where ribosomal RNA is transcribed, and its size tracks how much protein a cell is making
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  NCERT's sentence in the same paragraph reads 'Larger and more numerous nucleoli are present in cells actively carrying out protein synthesis', and this option keeps the opening words while changing the ending to 'dividing cells', so the remembered phrase vouches for a qualifier it never carried.
- **Why:** This question requires the one printed fact about what the nucleolus does, demonstrated by option 4 'It is a site for active ribosomal RNA synthesis' standing against three rival claims about the same body.
- **Note:** E1's pattern read the four full-statement options as statement_options; the stem 'Which of the following is true for nucleolus?' asks for a claim to be judged, so qtype is statements even though no lettered block is printed.
<!--/ecat-->

## Q122

Biology · botany · Transport in Plants

Stomatal movement is not affected by

- **(1)** $\mathrm{O_2}$ concentration
- (2) Light
- (3) Temperature
- (4) $\mathrm{CO_2}$ concentration

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Light, temperature and concentration of $\mathrm{CO_2}$ affect opening and closing of stomata while they are not affected by $\mathrm{O_2}$ concentration.

**Solved independently** (answer withheld)

1. Light, temperature and $\mathrm{CO_2}$ concentration all change guard cell turgor and so control stomatal movement; $\mathrm{O_2}$ concentration does not, which is option $1$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q122_adb0fbaa_27102026.png?v=adb0fbaafb4b)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q122_ad1285be_27102026.png?v=ad1285be9fe4)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stomatal movement answers to light, temperature, CO2 concentration, water status and hormones; the surrounding O2 level is not one of those cues
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Temperature does affect stomatal movement, but it is the item least likely to be carried on a student's list of cues, so once light and CO2 are recognised as genuine controls temperature becomes the odd one out and is ticked as the factor with no effect.
- **Why:** This question requires the printed list of factors that affect stomatal movement, demonstrated by the stem 'Stomatal movement is not affected by' setting three listed factors against the one gas that is not on the list.
<!--/ecat-->

## Q123

Biology · both · Cell Cycle and Cell Division

The stage during which separation of the paired homologous chromosomes begins is

- (1) Diakinesis
- **(2)** Diplotene
- (3) Pachytene
- (4) Zygotene

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Synaptonemal complex disintegrates.
2. Terminalisation begins at diplotene stage i.e. chiasmata start to shift towards end.

**Solved independently** (answer withheld)

1. In prophase I, diplotene begins when the synaptonemal complex dissolves and the recombined homologous chromosomes of each bivalent tend to separate from each other except at the sites of crossing over (chiasmata), so the answer is option $2$ (Diplotene).

**Subtopic:** Prophase I and Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q123_8887db2c_27102026.png?v=8887db2c31b3)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q123_4ee1841f_27102026.png?v=4ee1841fb348)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Across prophase I the homologues pair at zygotene, cross over at pachytene, start to come apart at diplotene when the synaptonemal complex dissolves, and are fully apart by diakinesis
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Diakinesis is the substage printed immediately after diplotene and is where the bivalents finish coming apart, so a student holding the sequence but not the stem's word 'begins' takes the stage where separation is complete.
- **Why:** This question requires the prophase I substage NCERT names for the start of separation, demonstrated by the stem's 'separation of the paired homologous chromosomes begins' set against four printed substages.
- **Note:** nearby_fact over look_alike_term: swapping the substage names for two unlike words leaves the pull intact, because what carries the student is diakinesis sitting next to diplotene in the printed sequence, not any resemblance between the words.
<!--/ecat-->

## Q124

Biology · botany · Anatomy of Flowering Plants

Stomata in grass leaf are

- (1) Rectangular
- (2) Kidney shaped
- **(3)** Dumb-bell shaped
- (4) Barrel shaped

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Grass being a monocot, has Dumb-bell shaped stomata in their leaves.

**Solved independently** (answer withheld)

1. In grasses the stomatal guard cells are $\text{dumb-bell shaped}$ (dicots have bean/kidney-shaped guard cells), so the answer is option $3$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q124_099a9f48_27102026.png?v=099a9f48941f)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q124_dc967a93_27102026.png?v=dc967a933762)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Guard cells are bean- or kidney-shaped in dicots but dumb-bell shaped in grasses, so the group the leaf belongs to decides the stomatal shape
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Kidney-shaped is the guard-cell shape taught as the default, and a student who answers from that default without using the stem's word 'grass' lands on it.
- **Why:** This question requires the guard-cell shape stated for grasses rather than the dicot default, demonstrated by the stem naming 'grass leaf' while option 2 prints the shape that is correct once that word is dropped.
- **Note:** condition_missed over nearby_fact: the two shapes do sit in one NCERT sentence, but what the student drops is the printed condition 'grass', and kidney-shaped becomes the right answer the moment that word is removed.
<!--/ecat-->

## Q125

Biology · botany · Anatomy of Flowering Plants

Secondary xylem and phloem in dicot stem are produced by

- (1) Phellogen
- **(2)** Vascular cambium
- (3) Apical meristems
- (4) Axillary meristems

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Vascular cambium is partially secondary
2. Form secondary xylem towards its inside and secondary phloem towards outsides.
3. $4 - 10$ times more secondary xylem is produced than secondary phloem.

**Solved independently** (answer withheld)

1. During secondary growth the vascular cambium divides, cutting off secondary xylem towards the inside and secondary phloem towards the outside, so the answer is option $2$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q125_fc8f7df1_27102026.png?v=fc8f7df130ea)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q125_5785601b_27102026.png?v=5785601be35d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In a dicot stem the secondary xylem and phloem come from the vascular cambium, while the cork cambium or phellogen makes only the periderm
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Phellogen is the other cambium printed in the same secondary-growth section, so a student who holds 'secondary growth runs on two cambia' without the products attached to each name picks it.
- **Why:** This question requires which meristem is credited with secondary vascular tissue, demonstrated by the stem 'Secondary xylem and phloem in dicot stem are produced by' with the two cambia and two apical-type meristems printed side by side.
- **Note:** nearby_fact over look_alike_term: swapping 'phellogen' for an unlike word leaves the pull intact, because what carries the student is its being the other cambium of the same section, not any resemblance to 'vascular cambium'.
<!--/ecat-->

## Q126

Biology · botany · Morphology of Flowering Plants

Pneumatophores occur in

- (1) Carnivorous plants
- (2) Free-floating hydrophytes
- **(3)** Halophytes
- (4) Submerged hydrophytes

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Halophytes like mangrooves have pneumatophores.
2. Apogeotropic (–vely geotropic) roots having lenticels called pneumathodes to uptake $\mathrm{O_2}$.

**Solved independently** (answer withheld)

1. Pneumatophores are aerial respiratory roots that grow upward out of waterlogged saline soil in mangroves such as $Rhizophora$, which are halophytes, so the answer is option $3$.

**Subtopic:** The Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q126_e9872170_27102026.png?v=e9872170cb01)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q126_3b133789_27102026.png?v=3b133789c1e3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pneumatophores are the upward-growing breathing roots of mangroves such as Rhizophora, and mangroves of saline swamps are halophytes, not freshwater hydrophytes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  'Halophyte' and 'hydrophyte' differ only in the prefix, so a student who knows these roots belong to plants standing in water reaches for the -phyte word that means water and takes the submerged form as the one most in need of air.
- **Why:** This question requires the plant group pneumatophores are tied to, demonstrated by the stem 'Pneumatophores occur in' offering three wet-habitat classes of which only 'Halophytes' covers the mangrove.
- **Note:** look_alike_term over nearby_fact: nothing about hydrophytes is printed beside the pneumatophore line, so position cannot be doing the work, which leaves the one-prefix difference between halophyte and hydrophyte as the pull.
<!--/ecat-->

## Q127

Biology · botany · Anatomy of Flowering Plants

Casparian strips occur in

- (1) Cortex
- (2) Pericycle
- (3) Epidermis
- **(4)** Endodermis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Endodermis have casparian strip on radial and inner tangential wall.
2. It is suberin rich.

**Solved independently** (answer withheld)

1. Casparian strips are suberin thickenings on the tangential and radial walls of the $\text{endodermis}$ cells, so the answer is option $4$.

**Subtopic:** Dicotyledonous and Monocotyledonous Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q127_9a245bd3_27102026.png?v=9a245bd39a2f)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q127_5935f3b6_27102026.png?v=5935f3b6e601)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Casparian strip is a suberised band in the walls of the endodermal cells, and it is the endodermis alone that carries it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The strip lies in the innermost layer of the cortex and is taught as the barrier that stops water travelling on through the cortex, so a student who keeps the region and the function but not the layer's own name answers 'cortex'.
- **Why:** This question requires the one root layer the Casparian strip is printed for, demonstrated by the stem 'Casparian strips occur in' with four layers of the same root section offered side by side.
- **Note:** nearby_fact over look_alike_term: swapping the layer names for unlike words leaves the pull intact, because what carries the student is the strip's position at the cortex boundary rather than any resemblance between 'cortex' and 'endodermis'.
<!--/ecat-->

## Q128

Biology · botany · Anatomy of Flowering Plants

Plants having little or no secondary growth are

- (1) Conifers
- (2) Deciduous angiosperms
- **(3)** Grasses
- (4) Cycads

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Grasses are monocots and monocots usually do not have secondary growth.
2. Palm like monocots have anomalous secondary growth.

**Solved independently** (answer withheld)

1. Grasses are monocots, whose vascular bundles are closed (they have no cambium), so they show little or no secondary growth, while conifers, cycads and deciduous dicot trees all have it. The answer is option $3$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q128_4071048a_27102026.png?v=4071048a1359)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q128_b6c45540_27102026.png?v=b6c45540ce7f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Secondary growth needs a vascular cambium, which monocots such as grasses never form, while conifers, cycads and dicot trees all thicken by cambial activity
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The secondary-growth section's next paragraph says the cambium is less active in winter, and a student who carries that line maps a tree that drops its leaves and stands dormant onto 'little or no secondary growth'.
- **Why:** This question requires which plant group is printed as lacking a vascular cambium, demonstrated by the stem 'Plants having little or no secondary growth are' with one monocot group set against three cambium-bearing groups.
<!--/ecat-->

## Q129

Biology · botany · Morphology of Flowering Plants

Sweet potato is a modified

- (1) Tap root
- **(2)** Adventitious root
- (3) Stem
- (4) Rhizome

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sweet potato is a modified adventitious root for storage of food
2. Rhizomes are underground modified stem
3. Tap root is primary root directly elongated from the redicle

**Solved independently** (answer withheld)

1. NCERT Class 11 (Morphology of Flowering Plants) lists sweet potato as an adventitious root swollen to store food, so the answer is option $2$.

**Subtopic:** The Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q129_b750bb10_27102026.png?v=b750bb1082aa)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q129_f634d7d6_27102026.png?v=f634d7d6d4e3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Swollen storage organs have to be traced to their origin: carrot and turnip store in a tap root, sweet potato in an adventitious root, and potato in a stem
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  NCERT's storage-root sentence pairs the swollen tap roots of carrot and turnip with the swollen adventitious roots of sweet potato, so a student who remembers only 'swollen food-storing root' takes the first half of that sentence.
- **Why:** This question requires the organ sweet potato is printed as a modification of, demonstrated by the stem 'Sweet potato is a modified' offering two kinds of root and two kinds of stem.
- **Note:** Option 3 also carries a name-likeness route, 'potato' inside 'sweet potato'; the headline trap is kept on option 1 because the key is adventitious root rather than simply root, and the tap-root-versus-adventitious split is the one the printed storage sentence decides.
<!--/ecat-->

## Q130

Biology · botany · Plant Kingdom

Which of the following statements is correct?

- (1) Horsetails are gymnosperms
- (2) *Selaginella* is heterosporous, while *Salvinia* is homosporous
- **(3)** Ovules are not enclosed by ovary wall in gymnosperms
- (4) Stems are usually unbranched in both *Cycas* and *Cedrus*

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Gymnosperms have naked ovule.
2. Called phanerogams without womb/ovary

**Solved independently** (answer withheld)

1. Horsetails ($Equisetum$) are pteridophytes, not gymnosperms, so option $1$ is false.
2. $Selaginella$ and $Salvinia$ are both heterosporous, so option $2$ is false.
3. In gymnosperms the ovules are naked, not enclosed by an ovary wall, so option $3$ is true.
4. $Cycas$ stem is unbranched but $Cedrus$ stem is branched, so option $4$ is false; the answer is option $3$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q130_0f5c232c_27102026.png?v=0f5c232c0f0f)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q130_73c57513_27102026.png?v=73c5751337cf)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperms bear naked ovules with no ovary wall around them, and each rival line pairs two taxa whose printed traits are not in fact the same
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Selaginella and Salvinia are printed together in one sentence as the two heterosporous pteridophytes, and this option keeps the Selaginella half right while flipping the Salvinia half, so the clause that matches the remembered pair vouches for the clause that does not.
- **Why:** This question requires four printed lines about plant groups to be graded one by one, demonstrated by option 3 'Ovules are not enclosed by ovary wall in gymnosperms' being the one that matches the book.
- **Note:** E1's pattern returned the default plain_mcq, but each option is a full statement and the stem reads 'Which of the following statements is correct?', so the printed shape is statements.
<!--/ecat-->

## Q131

Biology · botany · Biological Classification

Select the wrong statement :

- **(1)** Pseudopodia are locomotory and feeding structures in Sporozoans
- (2) Mushrooms belong to Basidiomycetes
- (3) Cell wall is present in members of Fungi and Plantae
- (4) Mitochondria are the powerhouse of the cell in all kingdoms except Monera

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Pseudopodia are locomotory structures in sarcodines (Amoeboid)

**Solved independently** (answer withheld)

1. Pseudopodia (false feet) are the locomotory and food-capturing structures of amoeboid protozoans such as $Amoeba$, not of Sporozoans like $Plasmodium$, so statement $1$ is wrong; mushrooms are Basidiomycetes, Fungi and Plantae have cell walls, and Monera (prokaryotes) lack mitochondria, so the answer is option $1$.

**Subtopic:** Protozoans · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 28)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q131_b0acb8cf_27102026.png?v=b0acb8cf6b92)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q131_c72cdf39_27102026.png?v=c72cdf397aa4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pseudopodia are the locomotory and feeding organs of the amoeboid protozoans, while sporozoans are defined by an infectious spore-like stage
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Cell walls are printed for Monera and for some Protista as well, so a student hunting for the faulty statement reads 'Fungi and Plantae' as a set with a kingdom missing and marks the incompleteness as the error.
- **Why:** This question requires four kingdom-level lines to be graded against the printed text, demonstrated by option 1 'Pseudopodia are locomotory and feeding structures in Sporozoans' moving the amoeboid protozoans' organ to the sporozoans.
<!--/ecat-->

## Q132

Biology · botany · Biological Classification

After karyogamy followed by meiosis, spores are produced exogenously in

- **(1)** Agaricus
- (2) Alternaria
- (3) Neurospora
- (4) Saccharomyces

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In Agaricus (a genus of basidiomycetes), basidiospores or meiospores are produced exogenously.
2. Neurospora (a genus of ascomycetes) produces ascospores as meiospores but endogenously inside the ascus.)
3. Alternaria (a genus of deuteromycetes) does not produce sexual spores.
4. Saccharomyces (Unicellular ascomycetes) produces ascospores, endogenously.

**Solved independently** (answer withheld)

1. Spores formed exogenously after karyogamy and meiosis are basidiospores, borne on the basidium in Basidiomycetes; Agaricus is a basidiomycete while Neurospora and Saccharomyces form endogenous ascospores and Alternaria lacks a known sexual stage, so the answer is option $1$.

**Subtopic:** Basidiomycetes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q132_9cace14d_27102026.png?v=9cace14de611)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q132_0ee84804_27102026.png?v=0ee84804e052)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Basidiospores form outside, on the surface of the basidium, whereas ascospores form inside a sac, so an exogenous sexual spore points to a basidiomycete such as Agaricus
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Karyogamy followed by meiosis is exactly the sequence printed for ascospore formation, so a student who uses the first half of the stem and drops the word 'exogenously' answers with the ascomycete the chapter names for genetic work.
- **Why:** This question requires the class whose sexual spores are borne on the outside of the spore-bearing cell, demonstrated by the stem's 'spores are produced exogenously' separating Agaricus from three fungi whose spores are not.
- **Note:** Considered asks: apply_rule, since the stem supplies a two-part criterion; kept at fact_line because both halves are printed lines — basidiospores being exogenous and Agaricus being a basidiomycete — rather than a rule carried to a new case.
<!--/ecat-->

## Q133

Biology · botany · The Living World

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Herbarium | (i) | It is a place having a collection of preserved plants and animals |
| b | Key | (ii) | A list that enumerates methodically all the species found in an area with brief description aiding identification |
| c | Museum | (iii) | Is a place where dried and pressed plant specimens mounted on sheets are kept |
| d | Catalogue | (iv) | A booklet containing a list of characters and their alternates which are helpful in identification of various taxa. |

- (1) (ii) (iv) (iii) (i)
- (2) (iii) (ii) (i) (iv)
- (3) (i) (iv) (iii) (ii)
- **(4)** (iii) (iv) (i) (ii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Herbarium – Dried and pressed plant specimen
2. Key – Identification of various taxa
3. Museum – Plant and animal specimen are preserved
4. Catalogue – Alphabetical listing of species

**Solved independently** (answer withheld)

1. Herbarium $\rightarrow$ (iii): dried, pressed plant specimens mounted on sheets; key $\rightarrow$ (iv): booklet of characters and their alternates for identification; museum $\rightarrow$ (i): collection of preserved plants and animals; catalogue $\rightarrow$ (ii): methodical list of species of an area with brief descriptions.
2. The sequence $a$-(iii), $b$-(iv), $c$-(i), $d$-(ii) matches option $4$.

**Subtopic:** Taxonomy and Systematics · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q133_a6e3c5cb_27102026.png?v=a6e3c5cb0604)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q133_1aff1ffb_27102026.png?v=1aff1ffb4d69)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Four taxonomic aids, each with its own definition: a herbarium holds dried and pressed plant specimens on sheets, a museum keeps preserved plants and animals, a key runs on contrasting characters, and a catalogue lists the species of an area.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Column II prints two descriptions that both close on the word identification, so a student holding only 'a key is the list that helps you identify species' takes (ii) for the key and is left with (iv) for the catalogue.
- **Why:** This question requires the definition NCERT prints for each named taxonomic aid, demonstrated by Column II spelling out 'dried and pressed plant specimens mounted on sheets' for one row and 'a list of characters and their alternates' for another, each settleable on its own.
- **Note:** asks is fact_line and not compare: every row can be decided against one printed definition without reference to the other rows, which is the test the brief sets for keeping compare off match questions. On nearby_fact against look_alike_term I applied the swap test - herbarium/museum and key/catalogue are not alike as words, and the pull survives renaming because all four definitions sit in one NCERT section.
<!--/ecat-->

## Q134

Biology · botany · Plant Kingdom

Winged pollen grains are present in

- (1) Mango
- (2) Cycas
- (3) Mustard
- **(4)** Pinus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In Pinus, winged pollen grains are present.
2. It is extended outer exine on two lateral sides to form the wings of pollen.
3. It is the characteristic feature, only in Pinus.
4. Pollen grains of Mustard, Cycas & Mango are not winged shaped.

**Solved independently** (answer withheld)

1. Pinus (a gymnosperm) is wind pollinated, and its pollen grains have two air-filled wings, so the answer is option $4$.

**Subtopic:** Gymnosperms · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 28)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q134_8ead9506_27102026.png?v=8ead950671a1)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q134_0cd34a36_27102026.png?v=0cd34a36e5e5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pinus pollen carries two air-filled wings that keep it aloft for wind pollination; no other plant in the option set is printed with winged pollen
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Cycas is the other gymnosperm the chapter names, printed in the same breath as Pinus, so a student who turns the question into 'which of these is a gymnosperm' has two names to choose from and takes the wrong one.
- **Why:** This question requires the genus whose pollen is printed as winged, demonstrated by the stem 'Winged pollen grains are present in' setting two gymnosperms against two angiosperms.
- **Note:** Two fillers are recorded on purpose: both angiosperm options have no printed pollen description to work from, so the question's only live decision is Pinus against Cycas.
<!--/ecat-->

## Q135

Biology · botany · Plant Kingdom

Which one is wrongly matched?

- (1) Gemma cups – Marchantia
- (2) Biflagellate zoospores – Brown algae
- **(3)** Uniflagellate gametes – Polysiphonia
- (4) Unicellular organism – Chlorella

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Polysiphonia is a genus of red algae, where asexual spores and gametes are non-motile or non-flagellated.
2. Other options (1, 2 & 4) are correctly matched

**Solved independently** (answer withheld)

1. Gemma cups occur on the thallus of $Marchantia$, Brown algae (Phaeophyceae) form pear-shaped biflagellate zoospores, and $Chlorella$ is a unicellular green alga, so options $1$, $2$ and $4$ are correctly matched.
2. $Polysiphonia$ is a red alga (Rhodophyceae), whose gametes are non-motile with no flagella, so 'Uniflagellate gametes – Polysiphonia' is wrongly matched, which is option $3$.

**Subtopic:** Rhodophyceae · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 29)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q135_819a1b29_27102026.png?v=819a1b29ac43)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q135_1c88fd76_27102026.png?v=1c88fd76c861)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Red algae such as Polysiphonia have non-motile gametes, while biflagellate zoospores belong to the brown algae and flagellated gametes to the green ones
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The flagellar features of the three algal classes are printed as one running comparison, so a student who has 'biflagellate' pinned to the green algae of Chlamydomonas reads the brown-alga row as the misfit and marks it.
- **Why:** This question requires each printed feature to be checked against the group it is tied to, demonstrated by option 3 'Uniflagellate gametes – Polysiphonia' giving flagella to a red alga whose gametes are non-motile.
- **Note:** E1's pattern read the options as statement_options; what is printed is four feature-and-organism pairs accepted or rejected whole, with no two columns and no pairing code, so qtype is recorded as two_part rather than match_columns.
<!--/ecat-->

## Q136

Biology · zoology · Breathing and Exchange of Gases

Which of the following options correctly represents the lung conditions in asthma and emphysema, respectively?

- (1) Increased respiratory surface; Inflammation of bronchioles
- (2) Increased number of bronchioles; Increased respiratory surface
- **(3)** Inflammation of bronchioles; Decreased respiratory surface
- (4) Decreased respiratory surface; Inflammation of bronchioles

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Asthma is a difficulty in breathing causing wheezing due to inflammation of bronchi and bronchioles.
2. Emphysema is a chronic disorder in which alveolar walls are damaged due to which respiratory surface is decreased.

**Solved independently** (answer withheld)

1. Asthma is difficulty in breathing caused by inflammation of the bronchi and bronchioles, and emphysema is a chronic disorder in which alveolar walls are damaged so the respiratory surface is decreased; the pair (Inflammation of bronchioles; Decreased respiratory surface) is option $3$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q136_46d70276_27102026.png?v=46d70276b34d)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q136_4cc19172_27102026.png?v=4cc19172f6e0)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Asthma is inflammation of the bronchi and bronchioles, while emphysema destroys alveolar walls and so cuts the respiratory surface
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  This option carries both printed facts with the two disorders exchanged, so a student who recalls the pair of lung conditions but not which name goes with which reads 'respectively' the wrong way round.
- **Why:** This question requires each disorder's printed lung condition to be put in the right slot, demonstrated by the stem asking for 'asthma and emphysema, respectively' while option 4 prints the same two conditions exchanged.
- **Note:** Considered asks: compare, since two disorders are held apart; kept at fact_line because each half is a printed definition read off the disorder's own line rather than a discrimination between look-alike quantities.
<!--/ecat-->

## Q137

Biology · zoology · Body Fluids and Circulation

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Tricuspid valve | i | Between left atrium and left ventricle |
| b | Bicuspid valve | ii | Between right ventricle and pulmonary artery |
| c | Semilunar valve | iii | Between right atrium and right ventricle |

- (1) a-i, b-ii, c-iii
- (2) a-i, b-iii, c-ii
- **(3)** a-iii, b-i, c-ii
- (4) a-ii, b-i, c-iii

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Tricuspid valves are AV valve present between right atrium and right ventricle.
2. Bicuspid valves are AV valve present between left atrium and left ventricle.
3. Semilunar valves are present at the openings of aortic and pulmonary aorta.

**Solved independently** (answer withheld)

1. Tricuspid valve guards the opening between the right atrium and right ventricle, so $a \rightarrow iii$; bicuspid (mitral) valve guards the left atrium-left ventricle opening, so $b \rightarrow i$; semilunar valve is at the opening of the pulmonary artery from the right ventricle, so $c \rightarrow ii$; this is option $3$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q137_c1fd3070_27102026.png?v=c1fd3070c9fd)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q137_1e012443_27102026.png?v=1e0124436380)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each heart valve has a fixed station: the tricuspid guards the right atrio-ventricular opening, the bicuspid or mitral guards the left, and the semilunar valves guard the ventricle-to-artery exits.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Placing the semilunar valve at the pulmonary exit settles c-ii and leaves only which side carries three cusps and which two, so a student who has stored 'bicuspid and tricuspid, one left one right' without which is which lands on a-i, b-iii.
- **Why:** This question requires the position NCERT states for each named valve, demonstrated by Column II printing bare locations - 'Between right atrium and right ventricle' - with no criterion supplied to apply.
- **Note:** The codebook excludes one swapped pair inside a longer order from reversed, which is why the a/b interchange in option 2 is not tagged that way. On look_alike_term against nearby_fact I applied the swap test: rename the two valves to unlike words, mitral and tricuspid, and the pull weakens, so the resemblance of the -cuspid names is what is carrying it.
<!--/ecat-->

## Q138

Biology · zoology · Breathing and Exchange of Gases

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Tidal volume | i | $2500 - 3000\,\mathrm{mL}$ |
| b | Inspiratory Reserve volume | ii | $1100 - 1200\,\mathrm{mL}$ |
| c | Expiratory Reserve volume | iii | $500 - 550\,\mathrm{mL}$ |
| d | Residual volume | iv | $1000 - 1100\,\mathrm{mL}$ |

- (1) i iv ii iii
- **(2)** iii i iv ii
- (3) iii ii i iv
- (4) iv iii ii i

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Tidal volume is volume of air inspired or expired during normal respiration.
2. It is approximately $500\,\mathrm{mL}$.
3. Inspiratory reserve volume is additional volume of air a person can inspire by a forceful inspiration.
4. It is around $2500 - 3000\,\mathrm{mL}$.
5. Expiratory reserve volume is additional volume of air a person can be expired by a forceful expiration.
6. This averages $1000 - 1100\,\mathrm{mL}$.
7. Residual volume is volume of air remaining in lungs even after forceful expiration.
8. This averages $1100 - 1200\,\mathrm{mL}$.

**Solved independently** (answer withheld)

1. Tidal volume is about $500\,\mathrm{mL}$, so a matches iii ($500 - 550\,\mathrm{mL}$).
2. Inspiratory reserve volume is $2500 - 3000\,\mathrm{mL}$, so b matches i.
3. Expiratory reserve volume is $1000 - 1100\,\mathrm{mL}$, so c matches iv.
4. Residual volume is $1100 - 1200\,\mathrm{mL}$, so d matches ii.
5. The sequence iii, i, iv, ii is option $2$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q138_feb6891f_27102026.png?v=feb6891fa092)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q138_8d685ad0_27102026.png?v=8d685ad049fa)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The four respiratory volumes carry fixed printed figures: tidal 500-550 mL, inspiratory reserve 2500-3000 mL, expiratory reserve 1000-1100 mL and residual 1100-1200 mL.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Tidal volume at 500-550 mL strikes out options 1 and 4, which leaves only which reserve volume is the 2500-3000 mL one, and reading reserve as the extra air that can still be pushed out puts the big figure on expiratory reserve volume.
- **Why:** This question requires the figures NCERT tabulates against each named respiratory volume, demonstrated by Column II being nothing but four ranges, '500 - 550 mL' among them, with no quantity to compute.
- **Note:** asks is fact_line even though the facts are printed numbers: nothing is computed from the stem, so calculate does not apply.
<!--/ecat-->

## Q139

Biology · zoology · Neural Control and Coordination

The transparent lens in the human eye is held in its place by

- (1) smooth muscles attached to the iris
- (2) ligaments attached to the iris
- **(3)** ligaments attached to the ciliary body
- (4) smooth muscles attached to the ciliary body

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Lens in the human eye is held in its place by suspensory ligaments attached to the ciliary body.

**Solved independently** (answer withheld)

1. NCERT: the eye ball contains a transparent crystalline lens which is held in place by ligaments attached to the ciliary body, so the answer is option $3$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q139_62f3c646_27102026.png?v=62f3c646954b)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q139_86aa22d0_27102026.png?v=86aa22d0ce70)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The lens hangs from the ciliary body on suspensory ligaments, while the ciliary muscle only changes its curvature and the iris only sizes the pupil
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  This option gets the attachment site right and the tissue wrong, and a student who remembers the ciliary muscle as the thing that acts on the lens accepts it because the familiar words 'ciliary body' are in it.
- **Why:** This question requires the printed attachment of the lens, demonstrated by option 3 'ligaments attached to the ciliary body' standing against options that keep one of its two words and change the other.
- **Note:** E1's pattern read these as statement_options, but each option is a short phrase completing the stem rather than a claim to be judged, so qtype is mcq. The option set is a two-by-two grid, tissue type crossed with attachment site, which is what puts the pulled option one word away from the key.
<!--/ecat-->

## Q140

Biology · zoology · Chemical Coordination and Integration

Which of the following is an amino acid derived hormone?

- (1) Estradiol
- (2) Ecdysone
- **(3)** Epinephrine
- (4) Estriol

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Epinephrine is derived from tyrosine amino acid by the removal of carboxyl group.
2. It is a catecholamine.

**Solved independently** (answer withheld)

1. Estradiol, estriol (oestrogens) and ecdysone (insect moulting hormone) are steroids, while epinephrine is an amino acid (tyrosine) derivative, so option $3$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q140_e6697717_27102026.png?v=e66977170833)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q140_eff5093b_27102026.png?v=eff5093be3ed)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hormones are grouped by chemical nature, and epinephrine is the amino-acid derivative while estradiol, estriol and ecdysone are all steroids
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Estradiol is printed in the very sentence that names epinephrine, one clause away under the steroids, so a student who remembers the name from the chemical-nature list but not which class it sat in takes it.
- **Why:** This question requires the chemical class the book assigns each hormone to, demonstrated by the stem 'Which of the following is an amino acid derived hormone?' with three steroids printed against one tyrosine derivative.
- **Note:** nearby_fact over look_alike_term: the four options share an initial E, but estradiol does not resemble epinephrine beyond that letter, and replacing estradiol with any other steroid from the same printed list — cortisol, say — would leave the pull untouched, so position in the printed list is doing the work.
<!--/ecat-->

## Q141

Biology · zoology · Locomotion and Movement

Which of the following hormones can play a significant role in osteoporosis?

- **(1)** Estrogen and Parathyroid hormone
- (2) Progesterone and Aldosterone
- (3) Aldosterone and Prolactin
- (4) Parathyroid hormone and Prolactin

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Estrogen promotes the activity of osteoblast and inhibits osteoclast.
2. In an ageing female osteoporosis occurs due to deficiency of estrogen.
3. Parathormone promotes mobilisation of calcium from bone into blood.
4. Excessive activity of parathormone causes demineralisation leading to osteoporosis.

**Solved independently** (answer withheld)

1. Osteoporosis is an age-related loss of bone mass, and NCERT names decreased estrogen as a common cause. Parathyroid hormone raises blood $\mathrm{Ca^{2+}}$ by resorbing bone, so it also affects bone mass. Aldosterone, progesterone and prolactin play no significant part, so the answer is option $1$.

**Subtopic:** Disorders of Muscular and Skeletal System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q141_302a4794_27102026.png?v=302a4794b067)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q141_4a1fd884_27102026.png?v=4a1fd88441ce)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Osteoporosis is tied to the fall in estrogen after menopause and to parathyroid hormone, which demineralises bone to raise blood calcium
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Parathyroid hormone is the bone-dissolving hormone printed in the chapter, so a student who finds it in an option treats the option as confirmed and never tests the second name in the pair.
- **Why:** This question requires both hormones that the printed account of osteoporosis names, demonstrated by option 1 'Estrogen and Parathyroid hormone' being the only pair in which neither name has to be excused.
- **Note:** Each option is a pair of hormones accepted or rejected whole, so qtype is recorded as two_part even though E1's pattern returned the default plain_mcq.
<!--/ecat-->

## Q142

Biology · zoology · Neural Control and Coordination

Which of the following structures or regions is incorrectly paired with its functions?

- (1) Hypothalamus : production of releasing hormones and regulation of temperature, hunger and thirst.
- **(2)** Limbic system : consists of fibre tracts that interconnect different regions of brain; controls movement.
- (3) Medulla oblongata : controls respiration and cardiovascular reflexes.
- (4) Corpus callosum : band of fibers connecting left and right cerebral hemispheres.

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Limbic system is emotional brain.
2. It controls all emotions in our body but not movements.

**Solved independently** (answer withheld)

1. As NCERT teaches it, the hypothalamus makes releasing hormones and regulates temperature, hunger and thirst, the medulla controls respiration and cardiovascular reflexes, and the corpus callosum is the band of fibres joining the two cerebral hemispheres. So options $1$, $3$ and $4$ are correctly paired. The limbic system, together with the hypothalamus, regulates sexual behaviour, emotional reactions and motivation. It is not a set of interconnecting fibre tracts and does not control movement, so option $2$ is the incorrect pairing.

**Subtopic:** Forebrain · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q142_1a6a4d33_27102026.png?v=1a6a4d33868a)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q142_7765f680_27102026.png?v=7765f6806d3d)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named brain region has one job the book gives it: the limbic system runs emotion, motivation and sexual behaviour, while movement is the work of the cerebellum and basal ganglia
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The single word 'incorrectly' is all that makes option 1 wrong; read as 'correctly paired', the hypothalamus line is the fullest textbook match in the set and gets ticked.
- **Why:** This question requires the function stated for each named brain region, demonstrated by 'Limbic system : consists of fibre tracts that interconnect different regions of brain; controls movement.' being the pairing that has to be rejected.
- **Note:** E1 called this statement_options; no lettered block is printed, but the stem does grade each option's structure-to-function pairing as a claim, so qtype statements holds under rule 1.
<!--/ecat-->

## Q143

Biology · zoology · Human Reproduction

The amnion of mammalian embryo is derived from

- (1) mesoderm and trophoblast
- (2) endoderm and mesoderm
- **(3)** ectoderm and mesoderm
- (4) ectoderm and endoderm

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The extraembryonic or foetal membranes are amnion, chorion, allantois and Yolk sac.
2. Amnion is formed from mesoderm on outer side and ectoderm on inner side.
3. Chorion is formed from trophoectoderm and mesoderm whereas allantois and Yolk sac membrane have mesoderm on outerside and endoderm in inner side.

**Solved independently** (answer withheld)

1. The amnion is formed from the somatopleure, which is extraembryonic $\text{ectoderm}$ lined by somatic $\text{mesoderm}$, so it is derived from ectoderm and mesoderm, which is option $3$.

**Subtopic:** Implantation and Embryonic Development · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q143_ed4a2f83_27102026.png?v=ed4a2f83b624)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q143_813a504a_27102026.png?v=813a504a4d64)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The amnion is built from the embryo's own ectoderm with mesoderm outside it; the trophoblast, which is not a germ layer at all, goes into the chorion
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Mesoderm with trophoblast is the right answer for the chorion, the membrane printed alongside the amnion, so a student holding 'the extra-embryonic membranes come from the trophoblast' carries that pairing across to the amnion.
- **Why:** This question requires the germ layers assigned to one named extra-embryonic membrane, demonstrated by the stem 'The amnion of mammalian embryo is derived from' with options that pair layers two at a time. On the nearby-fact test: swap 'trophoblast' for an unlike word and the pull survives, because it is the trophoblast standing beside the amnion in the implantation account that carries the student, not any resemblance between the two names.
- **Note:** The options are sets of layers accepted or rejected whole, the shape the retired vocabulary called pair_options; with no lettered block printed and no statement to grade, rule 1 keeps qtype mcq and the set-valued answer form is recorded here.
<!--/ecat-->

## Q144

Biology · zoology · Human Reproduction

Hormones secreted by the placenta to maintain pregnancy are

- **(1)** hCG, hPL, progestogens, estrogens
- (2) hCG, hPL, estrogens, relaxin, oxytocin
- (3) hCG, hPL, progestogens, prolactin
- (4) hCG, progestogens, estrogens, glucocorticoids

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Placenta releases human chorionic gonadotropic hormone (hCG) which stimulates the Corpus luteum during pregnancy to release estrogen and progesterone and also rescues corpus luteum from regression.
2. Human placental lactogen (hPL) is involved in growth of body of mother and breast.
3. Progesterone maintains pregnancy, keeps the uterus silent by increasing uterine threshold to contractile stimuli.

**Solved independently** (answer withheld)

1. NCERT Class 12 lists the placental hormones that maintain pregnancy as hCG, hPL, estrogens and progestogens; relaxin is secreted by the ovary late in pregnancy, and oxytocin, prolactin and glucocorticoids come from other glands, so the only option with all four placental hormones is option $1$.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q144_8ad96756_27102026.png?v=8ad9675644ec)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q144_4eba25e2_27102026.png?v=4eba25e24c9e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The placenta itself secretes hCG, hPL, progestogens and estrogens; prolactin, cortisol and thyroxine only rise in the mother's blood during pregnancy, and relaxin and oxytocin come from elsewhere
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Three of the four names in option 3 are placental, and the fourth is reached because hPL — human placental lactogen — makes prolactin look like a placental hormone too.
- **Why:** This question requires the list of hormones the placenta itself secretes, demonstrated by every option opening with hCG and differing only in its last one or two names.
- **Note:** E1 called this statement_options; a list of four hormone names is not a statement, so rule 1 keeps qtype mcq. The options are sets judged whole, the retired pair_options shape.
<!--/ecat-->

## Q145

Biology · zoology · Human Reproduction

The difference between spermiogenesis and spermiation is

- (1) In spermiogenesis spermatozoa from sertoli cells are released into the cavity of seminiferous tubules, while in spermiation spermatozoa are formed.
- (2) In spermiogenesis spermatozoa are formed, while in spermiation spermatids are formed.
- (3) In spermiogenesis spermatids are formed, while in spermiation spermatozoa are formed.
- **(4)** In spermiogenesis spermatozoa are formed, while in spermiation spermatozoa are released from sertoli cells into the cavity of seminiferous tubules.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Spermiogenesis is transformation of spermatids into spermatozoa whereas spermiation is the release of the sperms from sertoli cells into the lumen of seminiferous tubule.

**Solved independently** (answer withheld)

1. Spermiogenesis is the transformation of spermatids into spermatozoa, and spermiation is the release of spermatozoa from Sertoli cells into the cavity of the seminiferous tubules, which matches option $4$.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q145_d8c1ab38_27102026.png?v=d8c1ab38355b)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q145_12a03db1_27102026.png?v=12a03db18577)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Spermiogenesis is the shaping of spermatids into spermatozoa; spermiation is the later release of those sperm from the Sertoli cells into the lumen of the seminiferous tubule
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Option 1 is the key with its two clauses traded, so a student who remembers that one of the pair means release, but not which one, puts release under spermiogenesis.
- **Why:** This question requires two neighbouring terms to be held apart, demonstrated by the stem 'The difference between spermiogenesis and spermiation is' and by option 1 carrying the key's own two clauses with their labels exchanged.
- **Note:** E1 called this statement_options on option length; the stem is completed by the option rather than instructing a statement to be graded, so rule 1 keeps qtype mcq.
<!--/ecat-->

## Q146

Biology · zoology · Reproductive Health

The contraceptive ‘SAHELI’

- (1) is an IUD.
- (2) increases the concentration of estrogen and prevents ovulation in females.
- **(3)** blocks estrogen receptors in the uterus, preventing eggs from getting implanted.
- (4) is a post-coital contraceptive.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Saheli is the first non-steroidal, once a week pill.
2. It contains centchroman and its functioning is based upon selective Estrogen Receptor modulation.

**Solved independently** (answer withheld)

1. Saheli is a non-steroidal once-a-week oral contraceptive pill (centchroman); it acts as an anti-estrogen, blocking estrogen receptors in the uterus so implantation is prevented, which is option $3$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q146_16fc63fd_27102026.png?v=16fc63fdf456)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q146_76db9359_27102026.png?v=76db93591cdd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Saheli is a non-steroidal once-a-week pill that blocks estrogen receptors in the uterus, so it acts at implantation and not by the ovulation block of the steroidal pills
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The mechanism printed for the steroidal oral pills — they inhibit ovulation — sits in the same paragraph as Saheli, so a student who files Saheli simply as 'a pill' applies the pill mechanism to it.
- **Why:** This question requires the route attached to one named contraceptive, demonstrated by the options offering four different mechanisms — an IUD, an ovulation block, a receptor block and a post-coital dose — for the single name 'SAHELI'. On the nearby-fact test: replace 'Saheli' and 'the oral pills' with two unlike words and the pull survives, because what carries the student is the pill mechanism printed beside Saheli, not a likeness between names.
- **Note:** The receptor-blocking mechanism the key rests on is finer than the one-line description of Saheli as a non-steroidal once-a-week pill; tagged as printed, with the key left alone.
<!--/ecat-->

## Q147

Biology · botany · Biological Classification

Ciliates differ from all other protozoans in

- (1) using pseudopodia for capturing prey
- (2) having a contractile vacuole for removing excess water
- (3) using flagella for locomotion
- **(4)** having two types of nuclei

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ciliates differs from other protozoans in having  two types of nuclei.
2. eg. Paramoecium have two types of nuclei i.e. macronucleus & micronucleus.

**Solved independently** (answer withheld)

1. Ciliates such as $Paramoecium$ have two types of nuclei, a macronucleus and a micronucleus, which no other protozoan group has, so the answer is option $4$.

**Subtopic:** Protozoans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q147_f079ba0e_27102026.png?v=f079ba0eb2de)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q147_38c88fac_27102026.png?v=38c88face84d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ciliates alone among protozoans carry two kinds of nuclei, a macronucleus and a micronucleus; cilia, contractile vacuoles and the rest are either shared or belong to other protozoan groups
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  A contractile vacuole really is there in a ciliate and really does expel excess water, so the option is a true statement — but the stem asks what sets ciliates apart, and the amoeboid forms keep a contractile vacuole too.
- **Why:** This question requires the diagnostic feature given to ciliates, demonstrated by the stem 'Ciliates differ from all other protozoans in' and by option 2 naming a feature ciliates share with the amoeboid forms.
- **Note:** E1 called this statement_options on option length; the options are four-word phrases completing the stem, so rule 1 keeps qtype mcq.
<!--/ecat-->

## Q148

Biology · zoology · Animal Kingdom

Identify the vertebrate group of animals characterized by crop and gizzard in its digestive system

- **(1)** Aves
- (2) Reptilia
- (3) Amphibia
- (4) Osteichthyes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The digestive tract of Aves has additional chambers in their digestive system as crop and Gizzard.
2. Crop is concerned with storage of food grains.
3. Gizzard is a masticatory organ in birds used to crush food grain.

**Solved independently** (answer withheld)

1. In NCERT Class 11 (Animal Kingdom), the digestive tract of Aves is described as having additional chambers, the crop and the gizzard, so the answer is option $1$ (Aves).

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q148_5c5d4941_27102026.png?v=5c5d49417b6e)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q148_8f3ea71e_27102026.png?v=8f3ea71e0ada)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Birds have no teeth, so their gut carries two extra chambers: a crop that stores food and a muscular gizzard that grinds it
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  A gizzard is taught as the grinding chamber of an animal that cannot chew, and reptiles swallow their prey whole, so the grinding chamber is handed to the class printed immediately before Aves in the same run of vertebrate classes
- **Why:** This question requires the stated fact about which vertebrate class carries extra digestive chambers, demonstrated by the stem's 'crop and gizzard in its digestive system' set against four coordinate classes with no criterion printed to apply.
<!--/ecat-->

## Q149

Biology · zoology · Structural Organisation in Animals

Which of the following features is used to identify a male cockroach from a female cockroach?

- (1) Forewings with darker tegmina
- **(2)** Presence of caudal styles
- (3) Presence of a boat shaped sternum on the $9^{\mathrm{th}}$ abdominal segment
- (4) Presence of anal cerci

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Males bear a pair of short, thread like anal styles which are absent in females.
2. Anal/caudal styles arise from $9^{\mathrm{th}}$ abdominal segment in male cockroach.

**Solved independently** (answer withheld)

1. Caudal (anal) styles are present only in male cockroaches, while anal cerci occur in both sexes and the boat-shaped sternum belongs to the 7th segment of females, so option $2$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q149_ae1cdafc_27102026.png?v=ae1cdafc9d29)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q149_b019a99b_27102026.png?v=b019a99be22b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In the cockroach the male alone carries a pair of anal (caudal) styles on the 9th sternum, while the boat-shaped 7th sternum and the anal cerci belong to the female and to both sexes respectively
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Two remembered fragments of the abdominal account are joined: that a sex character sits on the 9th sternum, and that a boat-shaped sternum is one of the sex characters, which puts the female's structure on the male's segment
- **Why:** This question requires the stated fact about which abdominal appendage is confined to the male, demonstrated by option 2 'Presence of caudal styles' naming the one structure the morphology account gives to the male alone.
- **Note:** The pattern classifier called this statement_options on option length, but the options are noun phrases ('Presence of caudal styles') and the stem asks which feature identifies the male rather than asking statements to be judged, so the printed shape is a plain MCQ and is recorded as mcq.
<!--/ecat-->

## Q150

Biology · zoology · Animal Kingdom

Which one of these animals is not a homeotherm?

- (1) Camelus
- **(2)** Chelone
- (3) Macropus
- (4) Psittacula

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Homeotherm are animals that maintain constant body temperature, irrespective of surrounding temperature.
2. Birds and mammals are homeotherm.
3. Chelone (Turtle) belongs to class reptilia which is Poikilotherm or cold blood.

**Solved independently** (answer withheld)

1. Camelus (camel) and Macropus (kangaroo) are mammals, and Psittacula (parrot) is a bird, so all three are homeotherms; Chelone (turtle) is a reptile, a poikilotherm, so the answer is option $2$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q150_ea173851_27102026.png?v=ea1738516d8e)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q150_0142476b_27102026.png?v=0142476bc998)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Birds and mammals hold their body temperature steady; reptiles do not, so the turtle Chelone is the poikilotherm among these four genus names
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The camel is the animal carried in memory for a body temperature that drifts upward through a desert day to save water, and that drift is read as a failure to regulate
- **Why:** This question requires two stated facts chained - which class each genus is printed under, and which classes are warm-blooded - demonstrated by 'Chelone' being the reptile example in the printed list while Camelus, Macropus and Psittacula sit in the mammal and bird lists.
- **Note:** Which test was applied for nearby_fact against look_alike_term: the option is an animal name that resembles nothing in the key, and what carries the student is the camel's association with temperature drift, so association rather than likeness is doing the work.
<!--/ecat-->

## Q151

Biology · zoology · Animal Kingdom

Which of the following animals does not undergo metamorphosis?

- (1) Moth
- (2) Tunicate
- **(3)** Earthworm
- (4) Starfish

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Metamorphosis refers to transformation of larva into adult.
2. Animal that perform metamorphosis are said to have indirect development.
3. In earthworm development is direct which means no larval stage and hence no metamorphosis.

**Solved independently** (answer withheld)

1. Moth, tunicate (tadpole larva) and starfish (bilateral larva to radial adult) all pass through a larval stage, so they undergo metamorphosis, while the earthworm develops directly with no larva, which is option $3$.

**Subtopic:** Phylum – Annelida · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q151_a564e550_27102026.png?v=a564e5503b68)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q151_16ad4ae6_27102026.png?v=16ad4ae61396)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The earthworm develops directly from the egg, while the moth, the tunicate and the starfish each pass through a larva that has to be transformed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The tunicate is held in memory as the animal whose larva LOSES its tail and notochord on settling, and a loss is read as degeneration rather than as a metamorphosis
- **Why:** This question requires the stated fact about which animal develops without a larva, demonstrated by option 3 'Earthworm' being the one of the four whose account gives direct development.
<!--/ecat-->

## Q152

Biology · botany · Biological Classification

Which of the following organisms are known as chief producers in the oceans?

- (1) Cyanobacteria
- **(2)** Diatoms
- (3) Dinoflagellates
- (4) Euglenoids

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Diatoms are chief producers of the ocean.

**Solved independently** (answer withheld)

1. Among chrysophytes, $\text{diatoms}$ are described as the chief producers in the oceans, which is option $2$.

**Subtopic:** Chrysophytes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q152_1086ade2_27102026.png?v=1086ade204b2)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q152_abe60119_27102026.png?v=abe60119dac1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Diatoms, the chrysophytes, are the group the text names as the chief producers of the oceans
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The dinoflagellate paragraph follows the chrysophyte one and is also about marine photosynthetic protists, so the group remembered for red tides is put in the place of the group the chief-producer line belongs to
- **Why:** This question requires the stated fact that names a group's ecological role, demonstrated by the stem's phrase 'chief producers in the oceans', which the chrysophyte paragraph attaches to diatoms.
<!--/ecat-->

## Q153

Biology · botany · Organisms and Populations

Which one of the following population interactions is widely used in medical science for the production of antibiotics?

- (1) Parasitism
- (2) Mutualism
- (3) Commensalism
- **(4)** Amensalism

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Amensalism/Antibiosis $(0, -)$
2. Antibiotics are chemicals secreted by one microbial group (eg : Penicillium) which harm other microbes (eg : Staphylococcus)
3. It has no effect on Penicillium or the organism which produces it.

**Solved independently** (answer withheld)

1. An antibiotic-producing microbe (e.g. $Penicillium$ secreting penicillin) is itself unaffected ($0$) while the target bacteria are inhibited or killed ($-$); a $(0,-)$ interaction is amensalism, which is option $4$.

**Subtopic:** Commensalism and Ammensalism · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q153_6639b9ff_27102026.png?v=6639b9ffbb1c)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q153_a9f284e3_27102026.png?v=a9f284e362b2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Amensalism is the interaction in which one species is harmed and the other is unaffected, which is what a mould secreting an antibiotic does to bacteria
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The student gets as far as 'one partner is unaffected, so the interaction has a zero in it' and then reaches for the name that differs from the right one by a syllable
- **Why:** This question requires the definition of an interaction applied to a case no line states, demonstrated by the stem's 'production of antibiotics', which has to be mapped onto the one interaction where a species is harmed and its partner unaffected.
- **Note:** Which test was applied for look_alike_term against nearby_fact: commensalism and amensalism are printed together, so position holds, but the names also differ by a syllable, and the rulebook's tie-break gives the resemblance the win.
<!--/ecat-->

## Q154

Biology · botany · Biodiversity and Conservation

All of the following are included in ‘ex-situ conservation’ except

- (1) Botanical gardens
- **(2)** Sacred groves
- (3) Wildlife safari parks
- (4) Seed banks

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Sacred groves – in-situ conservation.
2. Represent pristine forest patch as protected by Tribal groups.

**Solved independently** (answer withheld)

1. Ex-situ conservation protects organisms outside their natural habitat (botanical gardens, wildlife safari parks, seed banks), whereas sacred groves protect them in their natural habitat, which is in-situ, so the exception is option $2$.

**Subtopic:** Ex Situ Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q154_e435846f_27102026.png?v=e435846fa8d6)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q154_e388bd87_27102026.png?v=e388bd87058b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex situ conservation keeps organisms outside their natural habitat - botanical gardens, safari parks, seed banks - whereas a sacred grove protects them where they already live
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A wildlife safari park is sorted by the sound of its name rather than by the test, and 'wildlife' and 'park' are the vocabulary of national parks and sanctuaries, which are the in-situ side
- **Why:** This question requires the stated membership of a printed example list, demonstrated by the stem's 'included in ex-situ conservation' set against four named conservation facilities, one of which is printed on the in-situ side.
<!--/ecat-->

## Q155

Biology · botany · Environmental Issues

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Eutrophication | i | UV-B radiation |
| b | Sanitary landfill | ii | Deforestation |
| c | Snow blindness | iii | Nutrient enrichment |
| d | Jhum cultivation | iv | Waste disposal |

- **(1)** a: iii, b: iv, c: i, d: ii
- (2) a: i, b: iii, c: iv, d: ii
- (3) a: ii, b: i, c: iii, d: iv
- (4) a: i, b: ii, c: iv, d: iii

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. a. Eutrophication iii. Nutrient enrichment
2. b. Sanitary landfill iv. Waste disposal
3. c. Snow blindness i. UV-B radiation
4. d. Jhum cultivation ii. Deforestation

**Solved independently** (answer withheld)

1. Eutrophication is the nutrient enrichment of water bodies, so $a \rightarrow iii$.
2. A sanitary landfill is a method of waste disposal, so $b \rightarrow iv$.
3. Snow blindness is caused by high doses of UV-B radiation inflaming the cornea, so $c \rightarrow i$.
4. Jhum (slash-and-burn) cultivation clears forest, so it causes deforestation, so $d \rightarrow ii$.
5. $a$-$iii$, $b$-$iv$, $c$-$i$, $d$-$ii$ matches option $1$.

**Subtopic:** Ozone Depletion in the Stratosphere, Deforestation and People's Participation in Forest Conservation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q155_94777406_27102026.png?v=947774062859)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q155_706e8400_27102026.png?v=706e84005e1b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each of these environmental terms names its own cause: eutrophication is nutrient enrichment, a sanitary landfill is a waste-disposal site, snow blindness is UV-B damage to the cornea, and jhum cultivation drives deforestation.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Each Column II phrase is the defining phrase of its Column I item, and every wrong code misassigns three of the four rows, so no single misremembered link reaches a printed option - holding eutrophication to nutrient enrichment alone leaves option 1 as the only code carrying a-iii.
- **Why:** This question requires the cause NCERT attaches to each named item, demonstrated by Column II being the bare causes 'Nutrient enrichment' and 'UV-B radiation', the first of which is the textbook's own definition of eutrophication.
- **Note:** no_trap here is structural and was checked before being written: none of the three wrong codes is a single-pair swap of the key - each differs from it in three of four positions - so there is no option a student holding one correct link walks to. Three fillers follows from that finding, not from leaving an option unexamined.
<!--/ecat-->

## Q156

Biology · botany · Organisms and Populations

In a growing population of a country,

- (1) reproductive and pre-reproductive individuals are equal in number.
- (2) reproductive individuals are less than the post-reproductive individuals.
- **(3)** pre-reproductive individuals are more than the reproductive individuals.
- (4) pre-reproductive individuals are less than the reproductive individuals.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Whenever the pre-reproductive individuals or the younger population size is larger than the reproductive group, the population will be an increasing population.

**Solved independently** (answer withheld)

1. In a growing population the age pyramid is triangular with a broad base, so pre-reproductive individuals are more than reproductive individuals, which is option $3$.

**Subtopic:** Life History Variation and Population Attributes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q156_02fac02c_27102026.png?v=02fac02c5584)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q156_f6a89a25_27102026.png?v=f6a89a251efb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A growing population has a broad-based, triangular age pyramid, so its pre-reproductive class outnumbers its reproductive class
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Growth is anchored to the size of the working, reproductive class rather than to the base of the pyramid, which flips the inequality the key states
- **Why:** This question requires a remembered rule applied to a case, demonstrated by the stem 'In a growing population of a country,' which supplies only the growth status and leaves the student to derive which age class is the larger.
- **Note:** The pattern classifier called this statement_options because each option is a full clause, but no lettered statement block is printed and no combination is asked for - the stem is a sentence opener with four rival completions - so it is recorded as mcq.
<!--/ecat-->

## Q157

Biology · zoology · Human Health and Disease

Which part of poppy plant is used to obtain the drug “Smack”?

- (1) Roots
- **(2)** Latex
- (3) Flowers
- (4) Leaves

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. ‘Smack’ also called as brown sugar/Heroin is formed by acetylation of morphine.
2. It is obtained from the latex of unripe capsule of Poppy plant.

**Solved independently** (answer withheld)

1. Smack is heroin (diacetylmorphine), obtained by acetylation of morphine, and morphine is extracted from the latex of the poppy plant $Papaver\ somniferum$, so the answer is option $2$ (Latex).

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q157_5e94da1e_27102026.png?v=5e94da1efd41)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q157_f12e158c_27102026.png?v=f12e158c2b97)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Smack (heroin) is made by acetylating morphine, which is extracted from the latex of the opium poppy
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The source organ of the neighbouring drug in the same section is carried across: the cannabis plant's leaves and flower tops are printed a few lines from the poppy's latex
- **Why:** This question requires the stated fact naming a plant part, demonstrated by the stem's 'Which part of poppy plant is used to obtain the drug Smack', which the chapter answers with the latex that yields morphine.
<!--/ecat-->

## Q158

Biology · both · Molecular Basis of Inheritance

All of the following are part of an operon except

- **(1)** an enhancer
- (2) structural genes
- (3) an operator
- (4) a promoter

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Enhancer sequences are present in eukaryotes.
2. Operon concept is for prokaryotes.

**Solved independently** (answer withheld)

1. An operon, as taught for the $lac$ operon, comprises a promoter, an operator and structural genes; enhancers are eukaryotic regulatory sequences and are not part of an operon, so the answer is option $1$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q158_67883e9c_27102026.png?v=67883e9c6a6a)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q158_96dcb069_27102026.png?v=96dcb06999f9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An operon is a promoter, an operator and the structural genes they control; the enhancer is an element of eukaryotic transcription and has no place in the operon
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked each wrong option against the printed definition of the operon, which names the promoter, the operator and the structural genes as its own parts: every remembered line places all three INSIDE the operon, which is the opposite of what the stem's 'except' requires, so no route built on the printed facts reaches any of them. The only other way to a wrong answer is not knowing what an enhancer is, which lands on no particular option.
- **Why:** This question requires the stated parts of a named genetic unit, demonstrated by option 1 'an enhancer' being the only one of the four that the operon description does not name.
<!--/ecat-->

## Q159

Biology · zoology · Principles of Inheritance and Variation

A woman has an X-linked condition on one of her X chromosomes. This chromosome can be inherited by

- (1) Only grandchildren
- (2) Only sons
- (3) Only daughters
- **(4)** Both sons and daughters

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Woman is a carrier
2. Both son & daughter inherit X–chromosome
3. Although only son be the diseased

**Solved independently** (answer withheld)

1. Each child gets one of the mother's two X chromosomes at random, whatever its sex: sons get $X$ from the mother and $Y$ from the father, and daughters get one $X$ from each parent, so the affected $X^{a}$ can pass to both sons and daughters (option $4$).

**Subtopic:** Sex Determination in Humans · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q159_433cad9a_27102026.png?v=433cad9ab302)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q159_9fb1ca66_27102026.png?v=9fb1ca66b4f3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A mother gives one of her two X chromosomes to every child, so an X-linked allele of hers can reach a son or a daughter; only a father's single X is restricted to his daughters
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  'Only sons' is the right answer to which of a carrier mother's children can be AFFECTED by an X-linked recessive condition, and it is read onto the stem's question of who can RECEIVE the chromosome
- **Why:** This question requires a transmission rule applied to a stated case, demonstrated by the stem 'A woman has an X-linked condition on one of her X chromosomes', which fixes the carrying parent and leaves the student to work out which children can receive that chromosome.
<!--/ecat-->

## Q160

Biology · zoology · Evolution

According to Hugo de Vries, the mechanism of evolution is

- (1) Phenotypic variations
- **(2)** Saltation
- (3) Multiple step mutations
- (4) Minor mutations

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. As per mutation theory given by Hugo de Vries, the evolution is a discontinuous phenomenon or saltatory phenomenon/saltation.

**Solved independently** (answer withheld)

1. Hugo de Vries (evening primrose, $Oenothera$) held that evolution is caused by large, sudden mutations arising in a single step, which he called saltation, so the answer is option $2$.

**Subtopic:** Mechanism of Evolution · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q160_54f46c3d_27102026.png?v=54f46c3de842)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q160_2a98cf8d_27102026.png?v=2a98cf8dc0aa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hugo de Vries held that evolution proceeds by saltation - single-step large mutations - in contrast with the small, gradual variations Darwin worked from
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The adjective from the contrast sentence printed beside the answer is carried over: de Vries is remembered for mutations, and 'small' is remembered from the Darwinian variations he was being set against
- **Why:** This question requires the stated position of a named scientist, demonstrated by the stem 'According to Hugo de Vries, the mechanism of evolution is', which the chapter answers with saltation, a single-step large mutation.
<!--/ecat-->

## Q161

Biology · both · Molecular Basis of Inheritance

AGGTATCGCAT is a sequence from the coding strand of a gene. What will be the corresponding sequence of the transcribed mRNA?

- (1) ACCUAUGCGAU
- (2) UGGTUTCGCAT
- **(3)** AGGUAUCGCAU
- (4) UCCAUAGCGUA

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Coding strand and mRNA has same nucleotide sequence except, ‘T’ – Thymine is replaced by ‘U’–Uracil in mRNA.

**Solved independently** (answer withheld)

1. The mRNA sequence is the same as the coding strand, except that $\mathrm{T}$ is replaced by $\mathrm{U}$, so $\mathrm{AGGTATCGCAT} \rightarrow \mathrm{AGGUAUCGCAU}$, which is option $3$.

**Subtopic:** Transcription Unit and the Gene · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q161_3a2354fe_27102026.png?v=3a2354fe8123)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q161_70eec523_27102026.png?v=70eec523d49a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The mRNA is a copy of the coding strand, base for base, with uracil standing in for thymine, because it is actually built by pairing against the other, template strand
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Complementary base pairing is applied to the strand that is printed, which is the taught operation for a template - drop the stem's word 'coding' and this string is the right answer
- **Why:** This question requires the base-pairing rule applied to a given sequence under the strand named in the stem, demonstrated by 'a sequence from the coding strand of a gene', which decides whether the answer is a copy or a complement.
- **Note:** The pattern classifier called this arrange_in_order because the stem contains the word 'sequence'; nothing is put in order here - the options are four whole strings - so the printed shape is recorded as mcq.
<!--/ecat-->

## Q162

Biology · zoology · Human Reproduction

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Proliferative Phase | i | Breakdown of endometrial lining |
| b | Secretory Phase | ii | Follicular Phase |
| c | Menstruation | iii | Luteal Phase |

- **(1)** ii iii i
- (2) i iii ii
- (3) iii ii i
- (4) iii i ii

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. During proliferative phase, the follicles start developing, hence, called follicular phase.
2. Secretory phase is also called as luteal phase mainly controlled by progesterone secreted by corpus luteum.
3. Estrogen further thickens the endometrium maintained by progesterone.
4. Menstruation occurs due to decline in progesterone level and involves breakdown of overgrown endometrial lining.

**Solved independently** (answer withheld)

1. In the ovary the follicles grow while the endometrium is rebuilt, so the proliferative phase (a) matches the follicular phase (ii).
2. After ovulation the corpus luteum makes progesterone and the endometrium becomes secretory, so the secretory phase (b) matches the luteal phase (iii).
3. Menstruation (c) is the breakdown of the endometrial lining (i).
4. $a-ii,\ b-iii,\ c-i$ is option $1$.

**Subtopic:** Menstrual Cycle · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q162_a39ed56c_27102026.png?v=a39ed56ce2cd)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q162_975496ef_27102026.png?v=975496ef8efe)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The uterine and ovarian names label the same stretches of the menstrual cycle: proliferative is the follicular phase, secretory is the luteal phase, and menstruation is the breakdown of the endometrium.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Menstruation to breakdown of the endometrial lining reads straight off the words, which leaves only which uterine phase pairs with which ovarian phase, and a student who has stored the four phase names as one list without their order gives the proliferative phase the luteal label.
- **Why:** This question requires the alternative name NCERT gives each phase of the menstrual cycle, demonstrated by Column II mixing one event, 'Breakdown of endometrial lining', with two phase names, 'Follicular Phase' and 'Luteal Phase'.
- **Note:** On nearby_fact against look_alike_term I applied the swap test: proliferative/follicular and secretory/luteal are not alike as words, and the pull survives renaming because the four names are printed together in one account of the cycle, so position is doing the work.
<!--/ecat-->

## Q163

Biology · zoology · Excretory Products and Their Elimination

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Glycosuria | i | Accumulation of uric acid in joints |
| b | Gout | ii | Mass of crystallised salts within the kidney |
| c | Renal calculi | iii | Inflammation in glomeruli |
| d | Glomerular nephritis | iv | Presence of glucose in urine |

- (1) ii iii i iv
- (2) i ii iii iv
- (3) iii ii iv i
- **(4)** iv i ii iii

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Glycosuria denotes presence of glucose in the urine.
2. This is observed when blood glucose level rises above $180\,\mathrm{mg}/100\,\mathrm{ml}$ of blood, this is called renal threshold value for glucose.
3. Gout is due to deposition of uric acid crystals in the joint.
4. Renal calculi are precipitates of calcium phosphate produced in the pelvis of the kidney.
5. Glomerular nephritis is the inflammatory condition of glomerulus characterised by proteinuria and haematuria.

**Solved independently** (answer withheld)

1. Glycosuria is the presence of glucose in urine, so $a \rightarrow iv$; gout is accumulation of uric acid crystals in joints, so $b \rightarrow i$; renal calculi are masses of crystallised salts in the kidney, so $c \rightarrow ii$; glomerulonephritis is inflammation of the glomeruli, so $d \rightarrow iii$. The order $iv\ i\ ii\ iii$ is option $4$.

**Subtopic:** Disorders Of The Excretory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q163_9176c3f4_27102026.png?v=9176c3f4c6c8)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q163_6e407975_27102026.png?v=6e407975376f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each of these excretory disorders is named by what it is: glucose in the urine, uric acid crystals in the joints, stones in the kidney and inflamed glomeruli.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Every Column II phrase restates its own term - glycosuria is presence of glucose in urine, glomerular nephritis is inflammation in glomeruli - and all three wrong codes differ from the key in all four positions, so each one requires giving up a pairing the term itself spells out; a-iv alone leaves option 4 as the only code standing.
- **Why:** This question requires the description NCERT prints for each named excretory disorder, demonstrated by Column II restating the terms themselves - 'Presence of glucose in urine' for glycosuria and 'Inflammation in glomeruli' for glomerular nephritis.
- **Note:** no_trap reached by the same structural check as q155: no wrong code is a single-pair swap of the key, so no option is reachable by one misremembered link.
<!--/ecat-->

## Q164

Biology · zoology · Excretory Products and Their Elimination

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Ultrafiltration | i | Henle's loop |
| b | Concentration of urine | ii | Ureter |
| c | Transport of urine | iii | Urinary bladder |
| d | Storage of urine | iv | Malpighian corpuscle |
|  |  | v | Proximal convoluted tubule |

- (1) v iv i ii
- **(2)** iv i ii iii
- (3) iv v ii iii
- (4) v iv i iii

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Ultrafiltration refers to filtration of very fine particles having molecular weight less than $68{,}000$ daltons through malpighian corpuscle.
2. Concentration of urine refers to water absorption from glomerular filtrate as a result of hyperosmolarity in the medulla created by counter-current mechanism in Henle's loop.
3. Urine is carried from kidney to bladder through ureter.
4. Urinary bladder is concerned with storage of urine.

**Solved independently** (answer withheld)

1. Ultrafiltration happens at the glomerulus inside the Malpighian corpuscle, so $a \to iv$.
2. Henle's loop sets up the counter-current mechanism that concentrates urine, so $b \to i$.
3. The ureter carries urine from kidney to bladder, so $c \to ii$.
4. The urinary bladder stores urine, so $d \to iii$.
5. $a\text{-}iv,\ b\text{-}i,\ c\text{-}ii,\ d\text{-}iii$ is option $2$.

**Subtopic:** Human Excretory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 33)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q164_10dd8e9d_27102026.png?v=10dd8e9d209f)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q164_d1c57a16_27102026.png?v=d1c57a1684d2)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The excretory jobs are divided along the tract: ultrafiltration in the Malpighian (renal) corpuscle, concentration of urine by Henle's loop, transport by the ureter and storage in the urinary bladder.
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  The proximal convoluted tubule is where the bulk of water and salts is taken back, so a student who reads concentration of urine as water leaving the filtrate puts that row on the PCT and keeps the other three rows right.
- **Why:** This question requires the part NCERT names for each stated excretory job, demonstrated by Column I printing the jobs - 'Ultrafiltration', 'Storage of urine' - against five named structures in Column II.
- **Note:** Column II carries five entries for four rows, so one structure, the proximal convoluted tubule, is spare, and that spare is the vehicle of the trap. I weighed nearby_fact for option 3, since the PCT is printed beside Henle's loop in the nephron account, but the option does not substitute an adjacent fact: it assigns the same job to the wrong segment, which the codebook files under wrong_site_attacked.
<!--/ecat-->

## Q165

Biology · zoology · Digestion and Absorption

Which of the following gastric cells indirectly help in erythropoiesis?

- (1) Goblet cells
- (2) Mucous cells
- (3) Chief cells
- **(4)** Parietal cells

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Parietal or oxyntic cell is a source of $\mathrm{HCl}$ and intrinsic factor.
2. $\mathrm{HCl}$ converts iron present in diet from ferric to ferrous form so that it can be absorbed easily and used during erythropoiesis.
3. Intrinsic factor is essential for the absorption of vitamin $\mathrm{B_{12}}$ and its deficiency causes pernicious anaemia.

**Solved independently** (answer withheld)

1. Parietal (oxyntic) cells of the gastric glands secrete HCl and intrinsic factor; intrinsic factor is required for absorption of vitamin $B_{12}$, which is needed for erythropoiesis, so they help indirectly: option $4$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q165_6035e22a_27102026.png?v=6035e22a7b25)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q165_98867449_27102026.png?v=9886744904e7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parietal (oxyntic) cells of the gastric gland secrete the intrinsic factor needed to absorb vitamin B12, and without that vitamin red-cell formation fails
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The three gastric cell types are printed in one sentence, and the secretion remembered as 'the factor for vitamin B12' is attached to the other secretory cell in that sentence
- **Why:** This question requires a named cell's stated function carried one step further, demonstrated by the stem's word 'indirectly', which asks for the cell whose secretion makes vitamin B12 absorption possible rather than for a cell that makes blood.
- **Note:** Options 1 and 2 name the same cell type - the text's phrase is 'mucus secreting goblet cells' - so this item effectively offers three cell types, not four.
<!--/ecat-->

## Q166

Biology · zoology · Body Fluids and Circulation

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Fibrinogen | (i) | Osmotic balance |
| b | Globulin | (ii) | Blood clotting |
| c | Albumin | (iii) | Defence mechanism |

- (1) (i) (iii) (ii)
- (2) (i) (ii) (iii)
- (3) (iii) (ii) (i)
- **(4)** (ii) (iii) (i)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Fibrinogen forms fibrin strands during coagulation.
2. These strands forms a network and the meshes of which are occupied by blood cells, this structure finally forms a clot.
3. Antibodies are derived from $\gamma$-Globulin fraction of plasma proteins which means globulins are involved in defence mechanisms.
4. Albumin is a plasma protein mainly responsible for BCOP.

**Solved independently** (answer withheld)

1. Plasma proteins (NCERT): fibrinogen $\rightarrow$ coagulation of blood, so $a \rightarrow (ii)$.
2. Globulins are primarily involved in the defence mechanisms of the body, so $b \rightarrow (iii)$.
3. Albumins help in osmotic balance, so $c \rightarrow (i)$.
4. The sequence $(ii)\,(iii)\,(i)$ matches option $4$.

**Subtopic:** Blood and Plasma · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q166_c04a8351_27102026.png?v=c04a8351356a)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q166_afe5d681_27102026.png?v=afe5d681e503)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each plasma protein has its own job: fibrinogen for blood clotting, globulins for defence, albumins for osmotic balance.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The word immunoglobulin fixes globulin to defence, which leaves only whether fibrinogen or albumin holds the osmotic job, and a student who recalls albumin as the largest plasma fraction gives it the conspicuous function, clotting, and passes osmotic balance to fibrinogen.
- **Why:** This question requires the function NCERT attaches to each named plasma protein, demonstrated by Column II being the bare jobs 'Osmotic balance', 'Blood clotting' and 'Defence mechanism'.
- **Note:** On nearby_fact against look_alike_term I applied the swap test: fibrinogen and albumin are not alike as words, and the pull survives renaming because both are printed in the same list of plasma proteins, so position is doing the work.
<!--/ecat-->

## Q167

Biology · zoology · Breathing and Exchange of Gases

Which of the following is an occupational respiratory disorder?

- (1) Botulism
- **(2)** Silicosis
- (3) Anthracis
- (4) Emphysema

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Silicosis is due to excess inhalation of silica dust in the workers involved grinding or stone breaking industries.
2. Long exposure can give rise to inflammation leading to fibrosis and thus causing serious lung damage.
3. Anthrax is a serious infectious disease caused by Bacillus anthracis.
4. It commonly affects domestic and wild animals.
5. Emphysema is a chronic disorder in which alveolar walls are damaged due to which respiratory surface is decreased.
6. Botulism is a form of food poisoning caused by Clostridium botulinum.

**Solved independently** (answer withheld)

1. Occupational respiratory disorders are caused by prolonged exposure to industrial dust (e.g. silica, asbestos), so $\text{Silicosis}$ (option $2$) is the answer.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q167_2730e77e_27102026.png?v=2730e77e5008)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q167_f5d341b7_27102026.png?v=f5d341b72e20)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Silicosis is the dust-exposure fibrosis the chapter names as an occupational respiratory disorder; emphysema, from the same section, is a smoking disorder
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Emphysema is true as the answer to 'name a chronic respiratory disorder', and the stem's qualifier 'occupational' is dropped on the way to it
- **Why:** This question requires the stated membership of a named disorder class, demonstrated by the stem's qualifier 'occupational respiratory disorder', which separates silicosis from the smoking disorder printed in the same section.
- **Note:** Option 3 is stored as 'Anthracis', the anthrax bacillus's species name, under which the printed key is sound. If the printed paper reads 'Anthracosis', that IS an occupational respiratory disorder and the item would carry two defensible answers - a reviewer should check the paper. Tagged as printed; the key was not re-judged.
<!--/ecat-->

## Q168

Biology · zoology · Locomotion and Movement

Calcium is important in skeletal muscle contraction because it

- (1) Detaches the myosin head from the actin filament.
- (2) Activates the myosin ATPase by binding to it.
- **(3)** Binds to troponin to remove the masking of active sites on actin for myosin.
- (4) Prevents the formation of bonds between the myosin cross bridges and the actin filament.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Signal for contraction increase $\mathrm{Ca^{++}}$ level many folds in the sarcoplasm.
2. $\mathrm{Ca^{++}}$ now binds with sub-unit of troponin (troponin "C") which is masking the active site on actin filament and displaces the sub-unit of troponin.
3. Once the active site is exposed, head of the myosin attaches and initiate contraction by sliding the actin over myosin.

**Solved independently** (answer withheld)

1. Calcium released from the sarcoplasmic reticulum binds to the troponin subunit on the actin thin filament, which removes the masking of the active sites on actin so myosin heads can bind; this is option $3$.

**Subtopic:** Mechanism of Muscle Contraction and Red and White Muscle Fibre · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q168_a9be248b_27102026.png?v=a9be248b8c66)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q168_8d8aade6_27102026.png?v=8d8aade6f25f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Calcium binds troponin on the thin filament and uncovers the actin sites, which is the step that allows myosin cross-bridges to form
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  Calcium's binding is kept but its partner is moved to the thick filament: the head whose ATPase drives the stroke is made the thing calcium switches on
- **Why:** This question requires the stated reason an ion matters in a process, demonstrated by the stem's trailing 'because it', which asks for calcium's own act rather than for any true step of the contraction cycle.
- **Note:** The pattern classifier called this statement_options because the options are full predicates; no lettered statement block is printed and no combination is asked for, so it is recorded as mcq.
<!--/ecat-->

## Q169

Biology · zoology · Neural Control and Coordination

Nissl bodies are mainly composed of

- (1) Nucleic acids and SER
- (2) DNA and RNA
- (3) Proteins and lipids
- **(4)** Free ribosomes and RER

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Nissl granules are present in the cyton and even extend into the dendrite but absent in axon and rest of the neuron.
2. Nissl granules are in fact composed of free ribosomes and RER.
3. They are responsible for protein synthesis.

**Solved independently** (answer withheld)

1. Nissl bodies in the cell body of a neuron are made of $\text{rough ER}$ and $\text{free ribosomes}$, which is option $4$.

**Subtopic:** Neuron as Structural and Functional Unit of Neural System and Types of Axon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q169_56c1af33_27102026.png?v=56c1af33dc43)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q169_e4497db8_27102026.png?v=e4497db85a80)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nissl granules in the neuron's cell body are stacks of rough endoplasmic reticulum with free ribosomes between them, which is why they stain with basic dyes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Two halves are remembered correctly - nucleic acid is present, and the granules are built of endoplasmic reticulum - and the ER is then labelled smooth instead of rough
- **Why:** This question requires the stated composition of a named structure, demonstrated by option 4 'Free ribosomes and RER' being the pairing the neuron account gives for Nissl granules.
<!--/ecat-->

## Q170

Biology · botany · Respiration in Plants

Which of these statements is incorrect?

- (1) Glycolysis operates as long as it is supplied with NAD that can pick up hydrogen atoms
- (2) Glycolysis occurs in cytosol
- (3) Enzymes of TCA cycle are present in mitochondrial matrix
- **(4)** Oxidative phosphorylation takes place in outer mitochondrial membrane

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Oxidative phosphorylation takes place in inner mitochondrial membrane.

**Solved independently** (answer withheld)

1. Glycolysis runs in the cytosol and needs a steady supply of $NAD^+$ to accept hydrogen, so options $1$ and $2$ are correct; TCA cycle enzymes sit in the mitochondrial matrix, so option $3$ is correct; oxidative phosphorylation happens on the inner mitochondrial membrane, so option $4$ is the incorrect statement.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q170_eaf8f426_27102026.png?v=eaf8f42676db)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q170_290b3b51_27102026.png?v=290b3b517c0a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Oxidative phosphorylation happens on the INNER mitochondrial membrane, where the electron transport system and ATP synthase sit
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  The statement carries no 'most' or 'except', so a student holding the one exception - succinate dehydrogenase is bound to the inner membrane, not free in the matrix - reads it as the overstatement and marks it as the incorrect one
- **Why:** This question requires stated facts about where each stage of respiration happens, demonstrated by option 4 'Oxidative phosphorylation takes place in outer mitochondrial membrane', which moves the process off the inner membrane the chapter gives it.
- **Note:** The retired per-option names that describe what is seen here are true_statement_trap (the stem is negated, so a true statement attracts) and ignores_exception (the succinate dehydrogenase case); both map to condition_missed in the live 12-value axis, which is the label recorded.
<!--/ecat-->

## Q171

Biology · both · Cell: The Unit of Life

Select the incorrect match :

- (1) Submetacentric chromosomes – L-shaped chromosomes
- (2) Allosomes – Sex chromosomes
- (3) Lampbrush chromosomes – Diplotene bivalents
- **(4)** Polytene chromosomes – Oocytes of amphibians

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Polytene chromosomes are found in salivary glands of insects of order Diptera.

**Solved independently** (answer withheld)

1. Submetacentric chromosomes appear L-shaped at anaphase (correct match); allosomes are sex chromosomes (correct); lampbrush chromosomes are diplotene bivalents (correct); polytene chromosomes occur in insect salivary glands, not amphibian oocytes, which carry lampbrush chromosomes, so option $4$ is the incorrect match.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q171_6f321425_27102026.png?v=6f3214255600)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q171_5a816a14_27102026.png?v=5a816a14a82b)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each named chromosome type carries one stated association: sub-metacentric with unequal arms, allosomes with the sex pair, lampbrush with diplotene bivalents of amphibian oocytes and polytene with dipteran salivary glands.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Allosome and autosome are the same stem with only the prefix changed, so a student carrying 'autosome' for the printed word reads 'Allosomes - Sex chromosomes' as the mismatch and stops there.
- **Why:** This question requires the one stated association each named chromosome type carries, demonstrated by 'Polytene chromosomes - Oocytes of amphibians' failing only because the amphibian oocyte belongs to lampbrush chromosomes.
- **Note:** E1_question_type reads match_the_lists, but no two columns and no pairing code are printed: each option is a single pair accepted or rejected whole, which is the pair_options shape and is carried here as qtype statements.
<!--/ecat-->

## Q172

Biology · zoology · Digestion and Absorption

Which of the following terms describe human dentition?

- (1) Pleurodont, Monophyodont, Homodont
- **(2)** Thecodont, Diphyodont, Heterodont
- (3) Thecodont, Diphyodont, Homodont
- (4) Pleurodont, Diphyodont, Heterodont

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In humans, dentition is
2. Thecodont : Teeth are present in the sockets of the jaw bone called alveoli.
3. Diphyodont : Teeth erupts twice, temporary milk or deciduous teeth are replaced by a set of permanent or adult teeth.
4. Heterodont dentition : Dentition consists of different types of teeth namely incisors, canine, premolars and molars.

**Solved independently** (answer withheld)

1. Human teeth are embedded in sockets of the jaw bone, so they are $\text{thecodont}$; they arise as two sets (milk then permanent), so they are $\text{diphyodont}$; they are of four types ($I, C, PM, M$), so they are $\text{heterodont}$, which is option $2$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q172_2c56f627_27102026.png?v=2c56f627a76b)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q172_f2915775_27102026.png?v=f29157758c70)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Human teeth are set in sockets (thecodont), come in two successive sets (diphyodont) and in four different kinds (heterodont).
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first two terms of this set are the ones the textbook prints word for word, and a student who checks the set only as far as 'Diphyodont' accepts 'Homodont' unexamined.
- **Why:** This question requires the three stated facts about human teeth together, demonstrated by option 3 carrying 'Thecodont, Diphyodont' correctly and failing only on 'Homodont'.
- **Note:** E1_question_type defaulted to plain_mcq, but each option is a set of three terms accepted or rejected whole - the pair_options shape - so qtype is recorded as statements.
<!--/ecat-->

## Q173

Biology · both · Cell: The Unit of Life

Which of the following events does not occur in rough endoplasmic reticulum?

- (1) Cleavage of signal peptide
- (2) Protein glycosylation
- (3) Protein folding
- **(4)** Phospholipid synthesis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Phospholipid synthesis does not take place in RER.
2. Smooth endoplasmic reticulum are involved in lipid synthesis.

**Solved independently** (answer withheld)

1. Proteins made on RER-bound ribosomes enter the RER lumen, where the signal peptide is cleaved, glycosylation begins and the protein folds, so options $1$, $2$ and $3$ occur in the RER.
2. As NCERT teaches, the smooth ER is the major site of lipid synthesis, so phospholipid synthesis is the event that does not occur in the RER: option $4$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 35)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q173_4dcdb478_27102026.png?v=4dcdb47844f0)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q173_e8d04c82_27102026.png?v=e8d04c82f3e9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The rough ER works on the newly made polypeptide - signal cleavage, folding and the first sugars - while membrane lipids are made on the smooth ER.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Glycoprotein formation is printed under the Golgi, so a student holding 'sugars are added in the Golgi' reads glycosylation as the event the rough ER does not do.
- **Why:** This question requires the stated division of labour between rough and smooth ER, demonstrated by 'Phospholipid synthesis' being the smooth ER's work while the other three options are steps on the newly made chain.
- **Note:** Signal-peptide cleavage and chaperone-assisted folding are not described in the textbook's ER paragraph, so a reviewer may want the syllabus check run on options 1 and 3.
<!--/ecat-->

## Q174

Biology · both · Cell: The Unit of Life

Many ribosomes may associate with a single mRNA to form multiple copies of a polypeptide simultaneously. Such strings of ribosomes are termed as

- (1) Plastidome
- (2) Polyhedral bodies
- **(3)** Polysome
- (4) Nucleosome

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The phenomenon of association of many ribosomes with single m-RNA leads to formation of polyribosomes or polysomes or ergasomes.

**Solved independently** (answer withheld)

1. A string of ribosomes attached to one mRNA, each making a copy of the polypeptide, is called a polysome (polyribosome), which is option $3$.

**Subtopic:** Ribosomes And Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q174_4ce525e8_27102026.png?v=4ce525e8716d)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q174_158c6cad_27102026.png?v=158c6cad90dc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A string of ribosomes translating one mRNA at the same time is a polysome.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  'Beads on a string' is the phrase learnt for nucleosomes, so a student answering the stem's picture of many particles strung along one thread supplies the chromatin term instead of the ribosome term.
- **Why:** This question requires the term stated for ribosomes working together on one mRNA, demonstrated by the stem's own words 'Such strings of ribosomes are termed as'.
<!--/ecat-->

## Q175

Biology · zoology · Human Health and Disease

In which disease does mosquito transmitted pathogen cause chronic inflammation of lymphatic vessels?

- (1) Ringworm disease
- (2) Ascariasis
- **(3)** Elephantiasis
- (4) Amoebiasis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Elephantiasis is caused by roundworm, Wuchereria bancrofti and it is transmitted by Culex mosquito.

**Solved independently** (answer withheld)

1. Wuchereria (W. bancrofti, W. malayi), transmitted by the female Culex mosquito, lives in the lymphatic vessels and causes their chronic inflammation, i.e. elephantiasis/filariasis, which is option $3$; ringworm (fungal, contact), ascariasis (contaminated food/water) and amoebiasis (houseflies as carriers) are not mosquito-borne.

**Subtopic:** Filarial Diseases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q175_44793f27_27102026.png?v=44793f27a86f)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q175_40f4dab1_27102026.png?v=40f4dab165e7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Wuchereria, carried by a mosquito, lodges in the lymphatic vessels, and the chronic inflammation it sets up is elephantiasis.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Ascaris is the other helminth printed in the same list of human parasites, so a student who gets as far as 'the pathogen is a worm' and takes the worm disease held most firmly lands on ascariasis.
- **Why:** This question requires the stated agent-vector-site line of a filarial disease, demonstrated by the stem's two printed conditions 'mosquito transmitted pathogen' and 'chronic inflammation of lymphatic vessels'.
<!--/ecat-->

## Q176

Biology · zoology · Human Health and Disease

Which of the following is not an autoimmune disease?

- **(1)** Alzheimer's disease
- (2) Rheumatoid arthritis
- (3) Psoriasis
- (4) Vitiligo

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Rheumatoid arthritis is an autoimmune disorder in which antibodies are produced against the synovial membrane and cartilage.
2. Vitiligo causes white patches on skin also characterised as autoimmune disorder.
3. Psoriasis is a skin disease that causes itchy or sore patches of thick red skin and is also autoimmune whereas Alzheimer's disease is due to deficiency of neurotransmitter acetylcholine.

**Solved independently** (answer withheld)

1. Rheumatoid arthritis, psoriasis and vitiligo are autoimmune disorders, but Alzheimer's disease is a neurodegenerative disorder (linked to low acetylcholine), so the answer is option $1$.

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q176_84b86449_27102026.png?v=84b864498020)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q176_5db98269_27102026.png?v=5db98269d7fb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In an autoimmune disease the body's own lymphocytes attack self tissue; Alzheimer's disease is degeneration of neurons, not an immune attack.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Rheumatoid arthritis is the one autoimmune disease this chapter names, so dropping the stem's 'not' turns it into the answer.
- **Why:** This question requires separating an immune attack on self tissue from a degenerative disorder, demonstrated by 'Alzheimer's disease' being the only option whose damage is neuronal loss rather than self-directed immunity.
<!--/ecat-->

## Q177

Biology · zoology · Evolution

Among the following sets of examples for divergent evolution, select the incorrect option :

- (1) Brain of bat, man and cheetah
- (2) Heart of bat, man and cheetah
- (3) Forelimbs of man, bat and cheetah
- **(4)** Eye of octopus, bat and man

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Divergent evolution occurs in the same structure, example - forelimbs, heart, brain of vertebrates which have developed along different directions due to adaptation to different needs whereas eye of octopus, bat and man are examples of analogous organs showing convergent evolution.

**Solved independently** (answer withheld)

1. Divergent evolution produces homologous organs: same basic structure and origin, adapted to different needs.
2. Brain, heart and forelimbs of bat, man and cheetah share a common mammalian origin, so options $1$, $2$ and $3$ are correct examples of divergent evolution.
3. The eye of the octopus (mollusc) and the eyes of mammals evolved independently and are analogous, an example of convergent evolution.
4. Hence the incorrect set for divergent evolution is option $4$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q177_8842dfe9_27102026.png?v=8842dfe93933)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q177_cac64baa_27102026.png?v=cac64baa0edd)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homologous organs - one inherited structure put to different uses - are the mark of divergent evolution, while the octopus eye and the vertebrate eye are built on different plans and only look alike.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Strike out the stem's word 'incorrect' and 'Forelimbs of man, bat and cheetah' becomes the answer, because it is the set the textbook itself prints as the example of divergent evolution.
- **Why:** This question requires the stated distinction between homologous and analogous organs, demonstrated by 'Eye of octopus, bat and man' placing the differently built octopus eye inside a set of divergent examples.
- **Note:** E1_question_type reads statement_options; each printed option is a set of one organ and three animals accepted or rejected whole, which carries the same qtype statements.
<!--/ecat-->

## Q178

Biology · botany · Microbes in Human Welfare

Conversion of milk to curd improves its nutritional value by increasing the amount of

- **(1)** Vitamin $\mathrm{B_{12}}$
- (2) Vitamin A
- (3) Vitamin D
- (4) Vitamin E

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Curd is more nourishing than milk.
2. It has enriched presence of vitamins specially Vit-$\mathrm{B_{12}}$.

**Solved independently** (answer withheld)

1. Lactic acid bacteria (LAB) turn milk into curd, and as NCERT teaches, they also increase its vitamin $\mathrm{B_{12}}$ content, so the answer is option $1$.

**Subtopic:** Microbes in Household Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q178_de1cbdc5_27102026.png?v=de1cbdc548f5)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q178_b366d822_27102026.png?v=b366d8223f6d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The lactic acid bacteria that set curd add vitamin B12, which is why curd is nutritionally better than the milk it was made from.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Milk is the food tied to vitamin D and calcium, so a student answering from what the milk already contains rather than from what the bacteria add takes vitamin D.
- **Why:** This question requires the stated gain that lactic acid bacteria give curd, demonstrated by the stem's 'improves its nutritional value by increasing the amount of'; the pull on 'Vitamin D' survives if that name is swapped for an unlike one, because what carries it is milk's own printed vitamin and not any likeness to B12, so the trap is nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q179

Biology · zoology · Evolution

The similarity of bone structure in the forelimbs of many vertebrates is an example of

- (1) Convergent evolution
- (2) Analogy
- **(3)** Homology
- (4) Adaptive radiation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In different vertebrates, bones of forelimbs are similar but their forelimbs are adapted in different way as per their adaptation, hence example of homology.

**Solved independently** (answer withheld)

1. Vertebrate forelimbs (whale, bat, cheetah, human) share the same basic bone plan ($humerus$, $radius$-$ulna$, $carpals$, $metacarpals$, $phalanges$) despite different functions, so they are homologous organs; this is Homology, option $3$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q179_283597aa_27102026.png?v=283597aabd07)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q179_8ee8c45c_27102026.png?v=8ee8c45cbe8c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The same bone plan in the forelimbs of different vertebrates is homology, inherited from a common ancestor; analogy is a shared job reached from different plans.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Homologous and analogous differ by a prefix on the same ending, and a student holding the pair with its two definitions interchanged reads 'similarity of bone structure' as analogy.
- **Why:** This question requires the stated name for one inherited structure found across vertebrates, demonstrated by 'The similarity of bone structure in the forelimbs of many vertebrates'; 'Analogy' is kept as look_alike_term because swapping it for an unlike word kills the pull, which the near-identical homologous/analogous pair is carrying.
<!--/ecat-->

## Q180

Biology · zoology · Principles of Inheritance and Variation

Which of the following characteristics represent ‘Inheritance of blood groups’ in humans?

- **(a)** Dominance
- **(b)** Co-dominance
- **(c)** Multiple allele
- **(d)** Incomplete dominance
- **(e)** Polygenic inheritance

- (1) b, d and e
- **(2)** a, b and c
- (3) b, c and e
- (4) a, c and e

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $I^{A}I^{O}$, $I^{B}I^{O}$ - Dominant–recessive relationship
2. $I^{A}I^{B}$ - Codominance
3. $I^{A}$, $I^{B}$ & $I^{O}$ - 3-different allelic forms of a gene (multiple allelism)

**Solved independently** (answer withheld)

1. ABO blood group is controlled by gene $I$ with three alleles $I^A$, $I^B$, $i$, so it shows multiple alleles (c); $I^A$ and $I^B$ are dominant over $i$ (a); $I^A I^B$ expresses both A and B, so it shows co-dominance (b). Incomplete dominance and polygenic inheritance do not apply, so a, b and c is option $2$.

**Subtopic:** Incomplete Dominance & Co-dominance, Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 36)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/crops/q180_1f549550_27102026.png?v=1f5495501d5e)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/27102026/neet_papers/2018/2018_AA/solutions/q180_22a598c2_27102026.png?v=22a598c28244)

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** ABO blood grouping is one gene with three alleles: $I^A$ and $I^B$ are co-dominant with each other and both dominant over $i$, so dominance, co-dominance and multiple alleles all show in the same system, with no blending and no second gene
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Option 3 keeps the two facts the ABO section is remembered for, co-dominance and multiple alleles, and fills its third slot with polygenic inheritance, reached by reading 'three alleles of one gene' as 'more than one gene'.
- **Why:** This question requires each named inheritance pattern to be checked against what is stated about the ABO gene, demonstrated by polygenic inheritance (e) standing in three of the four options while only 'a, b and c' leaves it out.
- **Note:** half_right was taken over nearby_fact because every wrong option is a set of three items of which two hold and one fails — (e) in options 3 and 4, (d) in option 1 — which is what that label is for.
<!--/ecat-->

