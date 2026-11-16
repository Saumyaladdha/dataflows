# NEET (UG) 2018 · Code EE

180 questions · source `NEET_Papers/2018/NEET_2018_Code_EE_official.pdf` · every image a CDN link (0 without one) · 40 figures redrawn

Generated from `questions.json` (schema `neet-pyq/question-record/v3`) by `code/paper_md.py`; edit the pipeline, not this file.

## Q1

Physics · Kinetic Theory of Gases

At what temperature will the rms speed of oxygen molecules become just sufficient for escaping from the Earth's atmosphere? (Given : Mass of oxygen molecule $(m) = 2.76 \times 10^{-26}\,\mathrm{kg}$ Boltzmann's constant $k_B = 1.38 \times 10^{-23}\,\mathrm{JK^{-1}}$)

- (1) $2.508 \times 10^{4}\,\mathrm{K}$
- (2) $5.016 \times 10^{4}\,\mathrm{K}$
- **(3)** $8.360 \times 10^{4}\,\mathrm{K}$
- (4) $1.254 \times 10^{4}\,\mathrm{K}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $V_{\mathrm{escape}} = 11200\,\mathrm{m/s}$
2. Say at temperature $T$ it attains $V_{\mathrm{escape}}$
3. So, $\sqrt{\frac{3k_{B}T}{m_{\mathrm{O_2}}}} = 11200\,\mathrm{m/s}$
4. On solving,
5. $T = 8.360 \times 10^{4}\,\mathrm{K}$

**Solved independently** (answer withheld)

1. Escape requires $v_{rms} = v_e$, with Earth's escape speed $v_e = 11.2\,\mathrm{km\,s^{-1}} = 1.12 \times 10^{4}\,\mathrm{m\,s^{-1}}$.
2. $v_{rms} = \sqrt{\frac{3 k_B T}{m}}$, so $T = \frac{m v_e^{2}}{3 k_B}$.
3. $\frac{m}{3 k_B} = \frac{2.76 \times 10^{-26}}{3 \times 1.38 \times 10^{-23}} = \frac{2}{3} \times 10^{-3}\,\mathrm{K\,s^{2}\,m^{-2}}$.
4. $v_e^{2} = (1.12 \times 10^{4})^{2} = 1.2544 \times 10^{8}\,\mathrm{m^{2}\,s^{-2}}$.
5. $T = \frac{2}{3} \times 10^{-3} \times 1.2544 \times 10^{8} = 8.363 \times 10^{4}\,\mathrm{K} \approx 8.360 \times 10^{4}\,\mathrm{K}$, which is option $3$.

**Subtopic:** RMS Speed and Its Dependence on Temperature · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 2)

![printed question 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q001_bc9fd4ee_03112026.png?v=bc9fd4ee67cd)

Publisher's solution, as printed:

![printed solution 1](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q001_09edbd90_03112026.png?v=09edbd900d7c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Setting the rms speed equal to the escape speed: only the translational share of the energy, $\frac{3}{2}k_BT$, fixes $v_{rms}$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 2  
  Oxygen is diatomic, so a student who equates $\frac12mv^2$ to the molecule's internal energy $\frac52k_BT$ instead of the translational $\frac32k_BT$ gets $T = mv^2/5k_B = 5.016\times10^{4}\,\mathrm{K}$
- **Why:** This question requires computing a temperature from an energy balance between the rms speed and the escape speed, demonstrated by the stem supplying only $m$ and $k_B$ and asking 'at what temperature will the rms speed ... become just sufficient for escaping'.
- **Note:** The escape speed 11.2 km/s is not printed and must be supplied from memory; with $v = 11.2$ exactly the key computes to $8.3625\times10^{4}$ while the option reads $8.360\times10^{4}$, so the paper used a slightly rounded escape speed. Tagged as printed.
<!--/ecat-->

## Q2

Physics · Thermodynamics

The volume (V) of a monatomic gas varies with its temperature (T), as shown in the graph. The ratio of work done by the gas, to the heat absorbed by it, when it undergoes a change from state A to state B, is

![printed figure: V-T graph: straight line through origin O, process A to B along it](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q002_e2c18eab_03112026.svg?v=e2c18eab5184)

*V-T graph: straight line through origin O, process A to B along it*

![drawn: V-T graph: straight line through origin O, process A to B along it](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q002_question_2b4c4a8d_03112026.svg?v=2b4c4a8d15d9)  
*drawn on the booklet's geometry, checked against its figure spec*

- **(1)** $\frac{2}{5}$
- (2) $\frac{1}{3}$
- (3) $\frac{2}{3}$
- (4) $\frac{2}{7}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Given process is isobaric
2. $dQ = n\,C_p\,dT$
3. $dQ = n\left(\frac{5}{2}R\right)dT$
4. $dW = P\,dV = n\,R\,dT$
5. Required ratio $= \frac{dW}{dQ} = \frac{nRdT}{n\left(\frac{5}{2}R\right)dT} = \frac{2}{5}$

**Solved independently** (answer withheld)

1. The graph is a straight line through the origin, so $V \propto T$, which means the pressure is constant (isobaric process).
2. Work done at constant pressure: $W = P\,\Delta V = nR\,\Delta T$.
3. Heat absorbed at constant pressure: $Q = nC_p\,\Delta T$, with $C_p = \frac{5}{2}R$ for a monatomic gas.
4. $\frac{W}{Q} = \frac{nR\,\Delta T}{n\cdot\frac{5}{2}R\,\Delta T} = \frac{2}{5}$, which is option $1$.

**Subtopic:** Isobaric Process · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 2)

![printed question 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q002_32b7cfb7_03112026.png?v=32b7cfb77d19)

Publisher's solution, as printed:

![printed solution 2](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q002_28838945_03112026.png?v=288389456878)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A straight V-T line through the origin means constant pressure, so the heat absorbed is $nC_p\Delta T$ while the work is $nR\Delta T$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Using the monatomic number that is actually stored, $C_v = \frac32R$, in place of the $C_p = \frac52R$ that a constant-pressure change requires turns $W/Q$ into $R/\frac32R = 2/3$
- **Why:** This question requires computing the ratio of work to heat for the process the graph fixes, demonstrated by 'the ratio of work done by the gas, to the heat absorbed by it' together with a V-T line through the origin O.
- **Note:** The figure is supplied as a drawn spec (V-T straight line through O with A and B on it) and is what establishes constant pressure; asks stays calculate rather than read_diagram because nothing is read off the plot as a value - the plot supplies one condition and the answer is then computed from the first law.
<!--/ecat-->

## Q3

Physics · Thermodynamics

The efficiency of an ideal heat engine working between the freezing point and boiling point of water, is

- **(1)** $26.8\%$
- (2) $6.25\%$
- (3) $20\%$
- (4) $12.5\%$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Efficiency of ideal heat engine, $\eta = \left(1 - \frac{T_2}{T_1}\right)$
2. $T_2$ : Sink temperature
3. $T_1$ : Source temperature
4. $\%\eta = \left(1 - \frac{T_2}{T_1}\right) \times 100$
5. $= \left(1 - \frac{273}{373}\right) \times 100$
6. $= \left(\frac{100}{373}\right) \times 100 = 26.8\%$

**Solved independently** (answer withheld)

1. An ideal (Carnot) engine has $\eta = 1 - \frac{T_2}{T_1}$ with temperatures in kelvin.
2. Source at boiling point: $T_1 = 100^\circ\text{C} = 373\,\text{K}$; sink at freezing point: $T_2 = 0^\circ\text{C} = 273\,\text{K}$.
3. $\eta = 1 - \frac{273}{373} = \frac{100}{373}$.
4. $\frac{100}{373} \approx 0.268 = 26.8\%$, which is option $1$.

**Subtopic:** Carnot Engine · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 2)

![printed question 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q003_5408c339_03112026.png?v=5408c33931eb)

Publisher's solution, as printed:

![printed solution 3](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q003_5c87b588_03112026.png?v=5c87b5883391)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Carnot efficiency $1 - T_c/T_h$ with the two fixed points of water put in on the kelvin scale
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Substituting 273 K and 373 K into the Carnot formula and into every misremembered variant of it reaches none of the three wrong options: $1-T_c/T_h = 26.8\%$ (the key), $T_c/T_h = 73.2\%$, $(T_h-T_c)/T_c = 36.6\%$ and the Celsius reading $1-0/100 = 100\%$. The wrong options are the round fractions $1/5$, $1/8$ and $1/16$, and no operation on 273 and 373 produces them.
- **Why:** This question requires computing the Carnot efficiency from the two fixed points of water, demonstrated by 'an ideal heat engine working between the freezing point and boiling point of water'.
- **Note:** no_trap is a finding here, not a gap: the three wrong options are round fractions with no derivation route, and the natural wrong routes (the Celsius substitution giving 100%, the inverted ratio giving 73.2%) are not printed at all.
<!--/ecat-->

## Q4

Physics · Waves

The fundamental frequency in an open organ pipe is equal to the third harmonic of a closed organ pipe. If the length of the closed organ pipe is $20\,\mathrm{cm}$, the length of the open organ pipe is

- **(1)** $13.2\,\mathrm{cm}$
- (2) $12.5\,\mathrm{cm}$
- (3) $8\,\mathrm{cm}$
- (4) $16\,\mathrm{cm}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For closed organ pipe, third harmonic $= \frac{3v}{4l}$
2. For open organ pipe, fundamental frequency $= \frac{v}{2l'}$
3. Given, $\frac{3v}{4l} = \frac{v}{2l'}$
4. $\Rightarrow l' = \frac{4l}{3\times 2} = \frac{2l}{3}$
5. $= \frac{2\times 20}{3} = 13.33\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Fundamental frequency of an open organ pipe of length $L_o$: $f_o = \frac{v}{2L_o}$.
2. Third harmonic of a closed organ pipe of length $L_c$: $f_3 = \frac{3v}{4L_c}$.
3. Set them equal: $\frac{v}{2L_o} = \frac{3v}{4L_c}$.
4. Solve for $L_o$: $L_o = \frac{4L_c}{6} = \frac{2L_c}{3}$.
5. Substitute $L_c = 20\,\mathrm{cm}$: $L_o = \frac{2 \times 20}{3} = 13.33\,\mathrm{cm}$.
6. The nearest option is $13.2\,\mathrm{cm}$, which is option $1$.

**Subtopic:** Organ Pipe · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 2)

![printed question 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q004_2e8cf005_03112026.png?v=2e8cf005ab11)

Publisher's solution, as printed:

![printed solution 4](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q004_b2334f5a_03112026.png?v=b2334f5af737)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A closed pipe sounds only odd harmonics, so its third harmonic is $3v/4L$, and the open pipe's fundamental is $v/2L$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Counting the closed pipe's modes as fundamental, first overtone, second overtone and calling the third one in that list the 'third harmonic' puts $5v/4L$ on the left, and $v/2L_o = 5v/80$ gives $L_o = 8\,\mathrm{cm}$
- **Why:** This question requires computing one pipe's length from a mode-frequency equality, demonstrated by 'the fundamental frequency in an open organ pipe is equal to the third harmonic of a closed organ pipe'.
- **Note:** $2L_c/3 = 13.33\,\mathrm{cm}$ while the keyed option reads 13.2 cm; the key is the only option in the right place and is tagged as printed, but the printed value is a rounding of 13.3 rather than the computed figure.
<!--/ecat-->

## Q5

Physics · Magnetic Effect of Electric Current

A metallic rod of mass per unit length $0.5\,\mathrm{kg\,m^{-1}}$ is lying horizontally on a smooth inclined plane which makes an angle of $30^\circ$ with the horizontal. The rod is not allowed to slide down by flowing a current through it when a magnetic field of induction $0.25\,\mathrm{T}$ is acting on it in the vertical direction. The current flowing in the rod to keep it stationary is

- (1) $7.14\,\mathrm{A}$
- (2) $14.76\,\mathrm{A}$
- (3) $5.98\,\mathrm{A}$
- **(4)** $11.32\,\mathrm{A}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. For equilibrium,

![printed figure: Forces on a current-carrying rod (dot) on a 30° incline in a vertical field B](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q005_sol_1_3697ee31_03112026.svg?v=3697ee312463)

*Forces on a current-carrying rod (dot) on a 30° incline in a vertical field B*

![drawn: Forces on a current-carrying rod (dot) on a 30° incline in a vertical field B](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q005_solution_1_84129a9b_03112026.svg?v=84129a9b91bd)  
*drawn on the booklet's geometry, checked against its figure spec*

2. $mg\sin 30^\circ = IlB\cos 30^\circ$
3. $I = \frac{mg}{lB}\tan 30^\circ$
4. $= \frac{0.5 \times 9.8}{0.25 \times \sqrt{3}} = 11.32\,\mathrm{A}$

**Solved independently** (answer withheld)

1. The rod is horizontal and $\vec B$ is vertical, so the magnetic force $F = BIL$ is horizontal (perpendicular to both).
2. Resolve along the incline: the magnetic force component up the incline is $BIL\cos 30^\circ$ and the gravity component down the incline is $mg\sin 30^\circ$.
3. Equilibrium: $BIL\cos 30^\circ = mg\sin 30^\circ \Rightarrow I = \frac{(m/L)\,g\tan 30^\circ}{B}$.
4. $I = \frac{0.5 \times 9.8 \times 0.5774}{0.25} = \frac{2.829}{0.25} = 11.32\,\mathrm{A}$, which is option $4$.

**Subtopic:** Magnetic Force · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q005_06a1abfb_03112026.png?v=06a1abfbb876)

Publisher's solution, as printed:

![printed solution 5](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q005_dda25ddb_03112026.png?v=dda25ddbb472)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A horizontal rod in a vertical field feels a horizontal force $BIL$, so equilibrium on a smooth incline needs $BIL\cos\theta = mg\sin\theta$, i.e. $I = \lambda g\tan\theta/B$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Every misapplication of the equilibrium condition on the printed data produces a value that is not among the options: $BIL = mg\sin\theta$ gives 9.8 A, $BIL = mg\cos\theta$ gives 16.97 A, $BIL = mg$ gives 19.6 A and $BIL\sin\theta = mg\cos\theta$ gives 33.9 A, while the key is $\lambda g\tan\theta/B = 11.32$ A. The three wrong options are three-figure decimals none of these routes reaches.
- **Why:** This question requires computing the current from a force balance on a smooth incline, demonstrated by 'the rod is not allowed to slide down by flowing a current through it when a magnetic field ... is acting on it in the vertical direction'.
- **Note:** The wrong step closest to hand, balancing $BIL$ against $mg\sin\theta$ and getting 9.8 A, is not printed, which is what makes no_trap the finding here. negative_words_seen records NOT, but it sits inside the premise ('is not allowed to slide down'), not in the task.
<!--/ecat-->

## Q6

Physics · Alternating Current

An inductor $20\,\mathrm{mH}$, a capacitor $100\,\mu\mathrm{F}$ and a resistor $50\,\Omega$ are connected in series across a source of emf, $V = 10\sin 314\,t$. The power loss in the circuit is

- **(1)** $0.79\,\mathrm{W}$
- (2) $2.74\,\mathrm{W}$
- (3) $0.43\,\mathrm{W}$
- (4) $1.13\,\mathrm{W}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $P_{av} = \left(\frac{V_{RMS}}{Z}\right)^{2} R$
2. $Z = \sqrt{R^{2} + \left(\omega L - \frac{1}{\omega C}\right)^{2}} = 56\,\Omega$
3. $\therefore\ P_{av} = \left(\frac{10}{\left(\sqrt{2}\right)56}\right)^{2} \times 50 = 0.79\,\mathrm{W}$

**Solved independently** (answer withheld)

1. From $V = 10\sin 314t$: $V_0 = 10\,\mathrm{V}$ and $\omega = 314\,\mathrm{rad\,s^{-1}}$.
2. $X_L = \omega L = 314 \times 20\times10^{-3} = 6.28\,\Omega$.
3. $X_C = \frac{1}{\omega C} = \frac{1}{314 \times 100\times10^{-6}} = 31.85\,\Omega$.
4. $X_C - X_L = 31.85 - 6.28 = 25.57\,\Omega$.
5. $Z^2 = R^2 + (X_C - X_L)^2 = 2500 + 653.8 = 3153.8\,\Omega^2$, so $Z \approx 56.16\,\Omega$.
6. $V_{rms}^2 = \left(\frac{10}{\sqrt{2}}\right)^2 = 50\,\mathrm{V^2}$.
7. $P = I_{rms}^2 R = \frac{V_{rms}^2 R}{Z^2} = \frac{50 \times 50}{3153.8} \approx 0.79\,\mathrm{W}$, which is option $1$.

**Subtopic:** Power in an AC Circuit · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 3)

![printed question 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q006_1e2df7cd_03112026.png?v=1e2df7cd1761)

Publisher's solution, as printed:

![printed solution 6](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q006_c4d966a0_03112026.png?v=c4d966a0b2de)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Power in a series LCR circuit is $I_{rms}^2R$, with the impedance built by adding $R$ and $(X_C-X_L)$ in quadrature
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Adding resistance and net reactance arithmetically, $Z = 50 + (31.85-6.28) = 75.57\,\Omega$, instead of in quadrature gives $P = V_{rms}^2R/Z^2 = 2500/5712 = 0.43\,\mathrm{W}$
- **Why:** This question requires computing the dissipated power from the source and the three series elements, demonstrated by 'an inductor 20 mH, a capacitor 100 microfarad and a resistor 50 ohm ... across a source of emf, V = 10 sin 314 t'.
<!--/ecat-->

## Q7

Physics · Magnetic Effect of Electric Current

Current sensitivity of a moving coil galvanometer is $5\,\mathrm{div/mA}$ and its voltage sensitivity (angular deflection per unit voltage applied) is $20\,\mathrm{div/V}$. The resistance of the galvanometer is

- (1) $40\,\Omega$
- **(2)** $250\,\Omega$
- (3) $25\,\Omega$
- (4) $500\,\Omega$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Current sensitivity $I_S = \frac{NBA}{C}$
2. Voltage sensitivity $V_S = \frac{NBA}{CR_G}$
3. So, resistance of galvanometer $R_G = \frac{I_S}{V_S} = \frac{5 \times 1}{20 \times 10^{-3}} = \frac{5000}{20} = 250\,\Omega$

**Solved independently** (answer withheld)

1. Voltage sensitivity is current sensitivity divided by resistance: $V_s = \frac{\theta}{V} = \frac{\theta}{IR} = \frac{I_s}{R}$.
2. Convert current sensitivity to SI: $I_s = 5\,\mathrm{div/mA} = 5000\,\mathrm{div/A}$.
3. $R = \frac{I_s}{V_s} = \frac{5000\,\mathrm{div/A}}{20\,\mathrm{div/V}} = 250\,\Omega$, which is option $2$.

**Subtopic:** Moving Coil Galvanometer · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 3)

![printed question 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q007_abf16047_03112026.png?v=abf160472659)

Publisher's solution, as printed:

![printed solution 7](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q007_ea0ec3a2_03112026.png?v=ea0ec3a2c7b1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Galvanometer resistance is the current sensitivity divided by the voltage sensitivity, so the milliampere in div/mA has to be carried into amperes first
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Converting $5\,\mathrm{div/mA}$ with a factor of $10^2$ instead of $10^3$ gives $500\,\mathrm{div/A}$, and $500/20 = 25\,\Omega$ in place of $5000/20 = 250\,\Omega$
- **Why:** This question requires computing a resistance from two sensitivities in mixed units, demonstrated by 'current sensitivity ... is 5 div/mA and its voltage sensitivity ... is 20 div/V'.
<!--/ecat-->

## Q8

Physics · Magnetic Effect of Electric Current

A thin diamagnetic rod is placed vertically between the poles of an electromagnet. When the current in the electromagnet is switched on, then the diamagnetic rod is pushed up, out of the horizontal magnetic field. Hence the rod gains gravitational potential energy. The work required to do this comes from

- **(1)** The current source
- (2) The lattice structure of the material of the rod
- (3) The magnetic field
- (4) The induced electric field due to the changing magnetic field

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Energy of current source will be converted into potential energy of the rod.

**Solved independently** (answer withheld)

1. A diamagnetic rod is repelled from the strong-field region, so it is pushed up and gains gravitational potential energy $\Delta U = mgh$.
2. A magnetic field does no work on charges, since $\vec{F} = q\vec{v} \times \vec{B}$ is perpendicular to $\vec{v}$, so the field is only the agent that transfers energy, not its source.
3. The energy stored in and transferred through the field comes from the current source that establishes and maintains the current in the electromagnet, so the work comes from the current source, which is option $1$.

**Subtopic:** Diamagnetism · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 3)

![printed question 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q008_e8619691_03112026.png?v=e8619691fd12)

Publisher's solution, as printed:

![printed solution 8](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q008_1290626c_03112026.png?v=1290626ced0d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Tracing the energy: the magnetic force on an induced diamagnetic moment does the lifting, but the energy is drawn from the source that holds the current up against the changing flux
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The stem itself says the rod is pushed up by the field, so naming the field answers 'what exerts the force?'; the question asks which agency pays for the gravitational potential energy, and the field's own energy is maintained by the electromagnet's current source
- **Why:** This question requires applying conservation of energy to decide which agency pays for the gain, demonstrated by 'the rod gains gravitational potential energy. The work required to do this comes from'.
- **Note:** asks is apply_rule rather than reason_line because no printed NCERT sentence answers this; the answer is obtained by tracing energy conservation through the electromagnet's circuit.
<!--/ecat-->

## Q9

Physics · Semiconductor Electronics

In the circuit shown in the figure, the input voltage $V_i$ is $20\,\mathrm{V}$, $V_{BE} = 0$ and $V_{CE} = 0$. The values of $I_B$, $I_C$ and $\beta$ are given by

![printed figure: Common-emitter n-p-n transistor: base fed from V_i through R_B = 500 kOhm, collector to 20 V through R_C = 4 kOhm, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q009_87dcc27b_03112026.svg?v=87dcc27b33ba)

*Common-emitter n-p-n transistor: base fed from V_i through R_B = 500 kOhm, collector to 20 V through R_C = 4 kOhm, emitter grounded*

![drawn: Common-emitter n-p-n transistor: base fed from V_i through R_B = 500 kOhm, collector to 20 V through R_C = 4 kOhm, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q009_question_653c00ff_03112026.svg?v=653c00ff7bd8)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $I_B = 40\,\mu\mathrm{A}$, $I_C = 10\,\mathrm{mA}$, $\beta = 250$
- (2) $I_B = 20\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 250$
- (3) $I_B = 25\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 200$
- **(4)** $I_B = 40\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 125$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $V_{BE} = 0$
2. $V_{CE} = 0$
3. $V_{b} = 0$

![printed figure: Common-emitter transistor: V_i through R_B = 500 kOhm to the base, collector through R_C = 4 kOhm to 20 V, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q009_sol_1_4e50a7a6_03112026.svg?v=4e50a7a6b7b3)

*Common-emitter transistor: V_i through R_B = 500 kOhm to the base, collector through R_C = 4 kOhm to 20 V, emitter grounded*

![drawn: Common-emitter transistor: V_i through R_B = 500 kOhm to the base, collector through R_C = 4 kOhm to 20 V, emitter grounded](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q009_solution_1_59ec26f9_03112026.svg?v=59ec26f901d3)  
*drawn on the booklet's geometry, checked against its figure spec*

4. $I_{C} = \frac{(20 - 0)}{4 \times 10^{3}}$
5. $I_{C} = 5 \times 10^{-3} = 5\,\mathrm{mA}$
6. $V_{i} = V_{BE} + I_{B}R_{B}$
7. $V_{i} = 0 + I_{B}R_{B}$
8. $20 = I_{B} \times 500 \times 10^{3}$
9. $I_{B} = \frac{20}{500 \times 10^{3}} = 40\,\mu\mathrm{A}$
10. $\beta = \frac{I_{C}}{I_{b}} = \frac{25 \times 10^{-3}}{40 \times 10^{-6}} = 125$

**Solved independently** (answer withheld)

1. With $V_{BE} = 0$, the whole input voltage drops across $R_B$: $I_B = \frac{V_i}{R_B} = \frac{20\,\mathrm{V}}{500 \times 10^{3}\,\Omega}$.
2. $I_B = 40 \times 10^{-6}\,\mathrm{A} = 40\,\mu\mathrm{A}$.
3. With $V_{CE} = 0$, the whole $20\,\mathrm{V}$ supply drops across $R_C$: $I_C = \frac{20\,\mathrm{V}}{4 \times 10^{3}\,\Omega}$.
4. $I_C = 5 \times 10^{-3}\,\mathrm{A} = 5\,\mathrm{mA}$.
5. $\beta = \frac{I_C}{I_B} = \frac{5 \times 10^{-3}}{40 \times 10^{-6}} = 125$.
6. $I_B = 40\,\mu\mathrm{A}$, $I_C = 5\,\mathrm{mA}$, $\beta = 125$ matches option $4$.

**Subtopic:** Transistor as an Amplifier (Common Emitter Configuration): Voltage, Current and Power Gain · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 3)

![printed question 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q009_2f4f14d1_03112026.png?v=2f4f14d13489)

Publisher's solution, as printed:

![printed solution 9](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q009_1e50b6f4_03112026.png?v=1e50b6f40ff1)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** With $V_{BE}=0$ the base loop fixes $I_B = V_i/R_B$ and with $V_{CE}=0$ the collector loop fixes $I_C = V_{CC}/R_C$; only then is $\beta$ their quotient
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The base loop gives $I_B = 20/500\,\mathrm{k}\Omega = 40\,\mu\mathrm{A}$, which this option prints correctly, and then finishing with a stock current gain of 250 rather than the collector loop gives $I_C = 250\times40\,\mu\mathrm{A} = 10\,\mathrm{mA}$
- **Why:** This question requires computing three quantities that must all hold together, demonstrated by 'the values of $I_B$, $I_C$ and $\beta$ are given by' with each option printing all three.
- **Note:** E1's pattern called this statement_options on the full-statement-options rule, but the options are triples of numerical values judged whole, so the shape recorded is two_part. Each wrong option is internally consistent on $\beta = I_C/I_B$, so the gain cannot be used to strike any of them out. The figure, supplied as a drawn spec, carries $R_B = 500\,\mathrm{k}\Omega$ and $R_C = 4\,\mathrm{k}\Omega$, without which the question cannot be started.
<!--/ecat-->

## Q10

Physics · Semiconductor Electronics

In the combination of the following gates the output Y can be written in terms of inputs A and B as

![printed figure: Inputs A and B through two NOT gates and two AND gates into an OR gate giving output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q010_50a46a97_03112026.svg?v=50a46a975029)

*Inputs A and B through two NOT gates and two AND gates into an OR gate giving output Y*

![drawn: Inputs A and B through two NOT gates and two AND gates into an OR gate giving output Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q010_question_94230e08_03112026.svg?v=94230e087dc5)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\overline{A \cdot B}$
- (2) $\overline{A \cdot B} + A \cdot B$
- **(3)** $A \cdot \overline{B} + \overline{A} \cdot B$
- (4) $\overline{A + B}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Inputs A and B through two NOT gates and two AND gates (A·B̄ and Ā·B) into an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q010_sol_1_151b672b_03112026.svg?v=151b672b5fbd)

*Inputs A and B through two NOT gates and two AND gates (A·B̄ and Ā·B) into an OR gate giving Y*

![drawn: Inputs A and B through two NOT gates and two AND gates (A·B̄ and Ā·B) into an OR gate giving Y](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q010_solution_1_46857bac_03112026.svg?v=46857bac1402)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $Y = (A \cdot \overline{B} + \overline{A} \cdot B)$

**Solved independently** (answer withheld)

1. Tracing the figure, input $A$ goes directly to the upper AND gate and also branches through the lower NOT gate, giving $\overline{A}$ at the lower AND gate.
2. Input $B$ crosses over the $A$ line (the hop) into the upper NOT gate, giving $\overline{B}$ at the upper AND gate, and also branches directly to the lower AND gate.
3. Upper AND output $= A \cdot \overline{B}$.
4. Lower AND output $= \overline{A} \cdot B$.
5. The OR gate gives $Y = A \cdot \overline{B} + \overline{A} \cdot B$, which is option $3$.

**Subtopic:** Logic Gates · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 4)

![printed question 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q010_9ff209eb_03112026.png?v=9ff209eb8d9f)

Publisher's solution, as printed:

![printed solution 10](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q010_8734b8e7_03112026.png?v=8734b8e7095f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Reading a gate network into Boolean form: an inverter on one input of each AND gate, the two ANDs feeding an OR, which is the exclusive-OR combination
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Moving the inversion from the AND inputs to the output of the final gate turns the network into 'OR then NOT', which is $\overline{A+B}$; the bubbles in the figure sit on one input of each AND, not after the OR
- **Why:** This question requires reading the printed gate network and writing it in Boolean form, demonstrated by 'in the combination of the following gates the output Y can be written in terms of inputs A and B as'.
- **Note:** asks is read_diagram because the whole content is the figure's topology; the drawn spec traces A branching over B's wire into one inverter and B into the other, each AND taking one direct and one inverted input, both feeding an OR.
<!--/ecat-->

## Q11

Physics · Semiconductor Electronics

In a p-n junction diode, change in temperature due to heating

- (1) Affects only reverse resistance
- (2) Does not affect resistance of p-n junction
- (3) Affects only forward resistance
- **(4)** Affects the overall $V - I$ characteristics of p-n junction

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Due to heating, number of electron-hole pairs will increase, so overall resistance of diode will change.
2. Due to which forward biasing and reversed biasing both are changed.

**Solved independently** (answer withheld)

1. Heating increases thermal generation of electron-hole pairs, so the intrinsic carrier concentration $n_i$ rises.
2. Higher $n_i$ raises the minority-carrier reverse saturation current $I_0$, so the reverse resistance falls.
3. Higher temperature also lowers the barrier (knee) voltage, so the forward current at a given $V$ rises and the forward resistance falls.
4. Since both forward and reverse behaviour change, the overall $V$-$I$ characteristic is affected, which is option $4$.

**Subtopic:** VI Characteristics of PN Junction Diode · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 4)

![printed question 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q011_b31546b9_03112026.png?v=b31546b9bb52)

Publisher's solution, as printed:

![printed solution 11](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q011_627406cb_03112026.png?v=627406cb155a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Heating a p-n junction shifts both branches of its characteristic: the reverse saturation current rises and the barrier potential falls
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The temperature fact that is actually stored is about the reverse branch, that the reverse saturation current roughly doubles for every ten degrees, so 'affects only reverse resistance' is a true half of the story with the word 'only' accepted along with it
- **Why:** This question requires the stated effect of temperature on a diode's characteristic, demonstrated by the option 'affects the overall V - I characteristics of p-n junction' being the one that covers both branches.
- **Note:** E1's pattern called this statement_options; under the live rule the stem neither prints a lettered block nor asks statements to be judged, so the shape recorded is mcq. negative_words_seen records NOT, but it is the 'does not affect' inside option 2, not a negation of the task.
<!--/ecat-->

## Q12

Physics · Wave Optics

Unpolarised light is incident from air on a plane surface of a material of refractive index '$\mu$'. At a particular angle of incidence '$i$', it is found that the reflected and refracted rays are perpendicular to each other. Which of the following options is correct for this situation?

- (1) Reflected light is polarised with its electric vector parallel to the plane of incidence
- (2) $i = \sin^{-1}\left(\dfrac{1}{\mu}\right)$
- **(3)** Reflected light is polarised with its electric vector perpendicular to the plane of incidence
- (4) $i = \tan^{-1}\left(\dfrac{1}{\mu}\right)$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. When reflected light rays and refracted rays are perpendicular, reflected light is polarised with electric field vector perpendicular to the plane of incidence.

![printed figure: Unpolarised light incident at angle i on a surface of index mu: reflected ray (dots only) perpendicular to refracted ray](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q012_sol_1_10581a78_03112026.svg?v=10581a7842b1)

*Unpolarised light incident at angle i on a surface of index mu: reflected ray (dots only) perpendicular to refracted ray*

![drawn: Unpolarised light incident at angle i on a surface of index mu: reflected ray (dots only) perpendicular to refracted ray](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q012_solution_1_d13b0a6a_03112026.svg?v=d13b0a6aec81)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Also, $\tan i = \mu$ (Brewster angle)

**Solved independently** (answer withheld)

1. Reflected and refracted rays perpendicular gives $i + r = 90^\circ$, so $r = 90^\circ - i$.
2. Snell's law: $\sin i = \mu \sin r = \mu \sin(90^\circ - i) = \mu \cos i$.
3. Hence $\tan i = \mu$, i.e. $i = \tan^{-1}\mu$ (Brewster's law), so options $2$ ($i = \sin^{-1}(1/\mu)$) and $4$ ($i = \tan^{-1}(1/\mu)$) are wrong.
4. At the Brewster angle the component of $\vec{E}$ parallel to the plane of incidence is not reflected, so the reflected light is plane polarised with $\vec{E}$ perpendicular to the plane of incidence, which is option $3$.

**Subtopic:** Polarization by Reflection and Refraction · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 4)

![printed question 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q012_a01b722c_03112026.png?v=a01b722c873e)

Publisher's solution, as printed:

![printed solution 12](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q012_a6ae47fb_03112026.png?v=a6ae47fb667e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** At Brewster's angle the reflected beam keeps no component in the plane of incidence, so it is polarised perpendicular to that plane, and $\tan i_B = \mu$ for light arriving from air
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The two planes get exchanged: it is the refracted beam that is left rich in the component parallel to the plane of incidence, while the reflected beam carries only the perpendicular component, so naming the plane of incidence for the reflected light inverts the pair
- **Why:** This question requires applying the Brewster condition the stem describes to this situation, demonstrated by 'the reflected and refracted rays are perpendicular to each other. Which of the following options is correct for this situation?'.
- **Note:** The four options are of mixed kinds, two polarisation claims and two angle formulas; the stem asks which option is correct rather than asking statements to be judged, so the shape recorded is mcq.
<!--/ecat-->

## Q13

Physics · Wave Optics

In Young's double slit experiment the separation $d$ between the slits is $2\,\mathrm{mm}$, the wavelength $\lambda$ of the light used is $5896\,\mathrm{\mathring{A}}$ and distance $D$ between the screen and slits is $100\,\mathrm{cm}$. It is found that the angular width of the fringes is $0.20^\circ$. To increase the fringe angular width to $0.21^\circ$ (with same $\lambda$ and $D$) the separation between the slits needs to be changed to

- (1) $1.8\,\mathrm{mm}$
- (2) $2.1\,\mathrm{mm}$
- **(3)** $1.9\,\mathrm{mm}$
- (4) $1.7\,\mathrm{mm}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Angular width $= \frac{\lambda}{d}$
2. $0.20^\circ = \frac{\lambda}{2\,\mathrm{mm}}$ ...(i)
3. $0.21^\circ = \frac{\lambda}{d}$ ...(ii)
4. Dividing we get, $\frac{0.20}{0.21} = \frac{d}{2\,\mathrm{mm}}$
5. $\therefore\ d = 1.9\,\mathrm{mm}$

**Solved independently** (answer withheld)

1. Angular fringe width in YDSE: $\theta = \frac{\lambda}{d}$, independent of $D$.
2. With $\lambda$ fixed, $\theta d = \text{constant}$, so $d' = d\,\frac{\theta}{\theta'}$.
3. $d' = 2\,\mathrm{mm} \times \frac{0.20^\circ}{0.21^\circ} = 1.905\,\mathrm{mm} \approx 1.9\,\mathrm{mm}$, which is option $3$.

**Subtopic:** Fringe Width in YDSE · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 4)

![printed question 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q013_dd8b45a1_03112026.png?v=dd8b45a149ae)

Publisher's solution, as printed:

![printed solution 13](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q013_fb3cb130_03112026.png?v=fb3cb130f0cf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Angular fringe width is $\lambda/d$, so the slit separation must move the opposite way to the width: $d' = d\times(0.20/0.21)$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Scaling the separation up in step with the width, $d' = 2\times(0.21/0.20) = 2.1\,\mathrm{mm}$, applies the ratio the right way up for a direct proportionality; the width goes as $\lambda/d$, so the separation must shrink to $2\times(0.20/0.21) = 1.9\,\mathrm{mm}$
- **Why:** This question requires computing the new slit separation from the inverse proportionality, demonstrated by 'to increase the fringe angular width to 0.21 degrees (with same lambda and D) the separation between the slits needs to be changed to'.
- **Note:** The printed $d = 2\,\mathrm{mm}$, $\lambda = 5896$ angstrom and $D = 100\,\mathrm{cm}$ are consistent with the stated 0.20 degrees only to one figure; the answer turns on the ratio 0.20:0.21 alone, so this does not affect the tagging.
<!--/ecat-->

## Q14

Physics · Ray Optics

An astronomical refracting telescope will have large angular magnification and high angular resolution, when it has an objective lens of

- (1) Small focal length and large diameter
- **(2)** Large focal length and large diameter
- (3) Large focal length and small diameter
- (4) Small focal length and small diameter

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For telescope, angular magnification $= \frac{f_0}{f_E}$
2. So, focal length of objective lens should be large.
3. Angular resolution $= \frac{D}{1.22\lambda}$ should be large.
4. So, objective should have large focal length $(f_0)$ and large diameter $D$.

**Solved independently** (answer withheld)

1. Angular magnification of an astronomical telescope is $m = \frac{f_o}{f_e}$, so a large objective focal length $f_o$ gives large magnification.
2. The limit of resolution is $\Delta\theta = \frac{1.22\,\lambda}{D}$, so resolving power $\frac{1}{\Delta\theta} = \frac{D}{1.22\,\lambda}$ increases with objective diameter $D$.
3. Both conditions need large focal length and large diameter, which is option $2$.

**Subtopic:** Resolving and Magnifying Power of Telescope · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q014_5acdcc41_03112026.png?v=5acdcc413ede)

Publisher's solution, as printed:

![printed solution 14](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q014_2604b629_03112026.png?v=2604b629bda7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The telescope objective must satisfy two relations at once: magnification $f_o/f_e$ wants a long focal length and resolving power $D/1.22\lambda$ wants a wide aperture
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  'Power is one over focal length' is the rule carried from the eyepiece and the magnifying glass, so a short focal length reads as high magnification; the large diameter half is right, and that half vouches for the wrong half
- **Why:** This question requires applying two stated relations to one component at once, demonstrated by 'will have large angular magnification and high angular resolution, when it has an objective lens of'.
- **Note:** E1's pattern called this statement_options; each option is in fact a pair of properties accepted or rejected whole, half right scoring nothing, so the shape recorded is two_part.
<!--/ecat-->

## Q15

Physics · Modern Physics

An electron of mass $m$ with an initial velocity $\vec{V} = V_0\hat{i}$ ($V_0 > 0$) enters an electric field $\vec{E} = -E_0\hat{i}$ ($E_0 = \text{constant} > 0$) at $t = 0$. If $\lambda_0$ is its de-Broglie wavelength initially, then its de-Broglie wavelength at time $t$ is

- **(1)** $\dfrac{\lambda_0}{\left(1+\dfrac{eE_0}{mV_0}t\right)}$
- (2) $\lambda_0 t$
- (3) $\lambda_0\left(1+\dfrac{eE_0}{mV_0}t\right)$
- (4) $\lambda_0$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Initial de-Broglie wavelength $\lambda_0 = \frac{h}{mV_0}$ ...(i)

![printed figure: An electron between two field lines of E0 pointing left, with arrows F and V0](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q015_sol_1_dd66db36_03112026.svg?v=dd66db36cef1)

*An electron between two field lines of E0 pointing left, with arrows F and V0*

![drawn: An electron between two field lines of E0 pointing left, with arrows F and V0](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q015_solution_1_990f9aaf_03112026.svg?v=990f9aaf66ff)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Acceleration of electron $a = \frac{eE_0}{m}$
3. Velocity after time 't' $V = \left(V_0 + \frac{eE_0}{m}t\right)$
4. So, $\lambda = \frac{h}{mV} = \frac{h}{m\left(V_0 + \frac{eE_0}{m}t\right)}$
5. $= \frac{h}{mV_0\left[1 + \frac{eE_0}{mV_0}t\right]} = \frac{\lambda_0}{\left[1 + \frac{eE_0}{mV_0}t\right]}$ ...(ii)
6. Divide (ii) by (i), $\lambda = \frac{\lambda_0}{\left[1 + \frac{eE_0}{mV_0}t\right]}$

**Solved independently** (answer withheld)

1. Force on the electron: $\vec{F} = (-e)\vec{E} = (-e)(-E_0\hat{i}) = eE_0\hat{i}$, along $+\hat{i}$, the same direction as $\vec{V}$.
2. Acceleration: $a = \frac{eE_0}{m}$ along $+\hat{i}$, so the electron speeds up.
3. Velocity at time $t$: $v = V_0 + \frac{eE_0}{m}t = V_0\left(1 + \frac{eE_0}{mV_0}t\right)$.
4. Initial wavelength: $\lambda_0 = \frac{h}{mV_0}$.
5. Wavelength at time $t$: $\lambda = \frac{h}{mv} = \frac{h}{mV_0\left(1 + \frac{eE_0}{mV_0}t\right)} = \frac{\lambda_0}{\left(1 + \frac{eE_0}{mV_0}t\right)}$, which is option $1$.

**Subtopic:** de Broglie Wavelength of Matter Waves · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q015_2a38165e_03112026.png?v=2a38165e84d7)

Publisher's solution, as printed:

![printed solution 15](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q015_ddb8d23a_03112026.png?v=ddb8d23a3a8e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The field accelerates the electron along its own velocity, so momentum grows as $mv_0 + eE_0t$ and $\lambda = h/p$ shrinks by the same factor
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  The momentum factor $(1 + eE_0t/mv_0)$ is worked out correctly and then multiplied into $\lambda_0$ instead of dividing it, which is what $\lambda = h/p$ demands
- **Why:** This question requires deriving the wavelength's time dependence from the momentum, demonstrated by 'if $\lambda_0$ is its de-Broglie wavelength initially, then its de-Broglie wavelength at time t is'.
<!--/ecat-->

## Q16

Physics · Modern Physics

For a radioactive material, half-life is $10$ minutes. If initially there are $600$ number of nuclei, the time taken (in minutes) for the disintegration of $450$ nuclei is

- **(1)** $20$
- (2) $30$
- (3) $10$
- (4) $15$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Number of nuclei remaining $= 600 - 450 = 150$
2. $\frac{N}{N_0} = \left(\frac{1}{2}\right)^{n}$
3. $\frac{150}{600} = \left(\frac{1}{2}\right)^{\frac{t}{t_{1/2}}}$
4. $\left(\frac{1}{2}\right)^{2} = \left(\frac{1}{2}\right)^{\frac{t}{t_{1/2}}}$
5. $t = 2t_{1/2} = 2 \times 10$
6. $= 20$ minute

**Solved independently** (answer withheld)

1. Nuclei remaining: $N = 600 - 450 = 150$.
2. $\frac{N}{N_0} = \frac{150}{600} = \frac{1}{4}$.
3. $\frac{1}{4} = \left(\frac{1}{2}\right)^{n}$ gives $n = 2$ half-lives.
4. $t = n\,T_{1/2} = 2 \times 10 = 20$ minutes, which is option $1$.

**Subtopic:** Law of Radioactive Decay · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 5)

![printed question 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q016_f5979a3c_03112026.png?v=f5979a3c339f)

Publisher's solution, as printed:

![printed solution 16](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q016_1feb3aa9_03112026.png?v=1feb3aa971cf)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Decay halves the survivors, not a fixed count: 450 of 600 gone leaves 150, which is two half-lives
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The first ten minutes destroy 300 nuclei, so treating decay as a steady 300 per ten minutes gives 450 nuclei in 15 minutes; the second ten minutes destroy only 150, because each half-life halves what is left
- **Why:** This question requires computing a time from the halving law, demonstrated by 'if initially there are 600 number of nuclei, the time taken (in minutes) for the disintegration of 450 nuclei is'.
<!--/ecat-->

## Q17

Physics · Modern Physics

The ratio of kinetic energy to the total energy of an electron in a Bohr orbit of the hydrogen atom, is

- (1) $1 : 1$
- (2) $2 : -1$
- **(3)** $1 : -1$
- (4) $1 : -2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{KE} = -(\text{total energy})$
2. So, Kinetic energy : total energy $= 1 : -1$

**Solved independently** (answer withheld)

1. Centripetal force from Coulomb attraction: $\frac{mv^2}{r} = \frac{ke^2}{r^2}$, so $K = \frac{1}{2}mv^2 = \frac{ke^2}{2r}$.
2. Potential energy: $U = -\frac{ke^2}{r}$.
3. Total energy: $E = K + U = \frac{ke^2}{2r} - \frac{ke^2}{r} = -\frac{ke^2}{2r} = -K$.
4. $K : E = K : (-K) = 1 : -1$, which is option $3$.

**Subtopic:** Bohr's Atomic Model · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 5)

![printed question 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q017_9ffee995_03112026.png?v=9ffee99542b1)

Publisher's solution, as printed:

![printed solution 17](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q017_a80de78e_03112026.png?v=a80de78e261e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a Bohr orbit the total energy is the negative of the kinetic energy and half the potential energy, so $K:E = 1:-1$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $1:-2$ is the true ratio of kinetic to potential energy in a Bohr orbit, the virial relation the chapter prints; the stem asks for kinetic to total energy, and the total is $-K$, not $-2K$
- **Why:** This question requires forming a ratio from the Bohr energy relations, demonstrated by 'the ratio of kinetic energy to the total energy of an electron in a Bohr orbit'.
- **Note:** The signs printed in the options are what separate the key from option 1, so the sign of the total energy is doing real work here.
<!--/ecat-->

## Q18

Physics · Modern Physics

When the light of frequency $2\nu_0$ (where $\nu_0$ is threshold frequency), is incident on a metal plate, the maximum velocity of electrons emitted is $v_1$. When the frequency of the incident radiation is increased to $5\nu_0$, the maximum velocity of electrons emitted from the same plate is $v_2$. The ratio of $v_1$ to $v_2$ is

- **(1)** $1 : 2$
- (2) $4 : 1$
- (3) $1 : 4$
- (4) $2 : 1$

**Answer** — booklet: (1) · independent solve: (1) · agree

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

1. Einstein's photoelectric equation: $\frac{1}{2}m v_{max}^2 = h\nu - h\nu_0$.
2. For $\nu = 2\nu_0$: $\frac{1}{2}m v_1^2 = h(2\nu_0 - \nu_0) = h\nu_0$.
3. For $\nu = 5\nu_0$: $\frac{1}{2}m v_2^2 = h(5\nu_0 - \nu_0) = 4h\nu_0$.
4. Dividing: $\frac{v_1^2}{v_2^2} = \frac{h\nu_0}{4h\nu_0} = \frac{1}{4}$.
5. $\frac{v_1}{v_2} = \sqrt{\frac{1}{4}} = \frac{1}{2}$, i.e. $1 : 2$, which is option $1$.

**Subtopic:** Photoelectric Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q018_bf6bd39d_03112026.png?v=bf6bd39d397d)

Publisher's solution, as printed:

![printed solution 18](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q018_9e45e0e6_03112026.png?v=9e45e0e6f9c6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The photoelectric equation gives the kinetic energy, and the speed is its square root, so energies in the ratio 1:4 mean speeds in the ratio 1:2
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $h(2\nu_0-\nu_0) : h(5\nu_0-\nu_0)$ is $1:4$, and reporting that as the speed ratio leaves out the square root that turns $\frac12mv^2$ into $v$
- **Why:** This question requires computing a ratio of speeds from the photoelectric equation, demonstrated by 'the ratio of $v_1$ to $v_2$ is' with the two frequencies given as $2\nu_0$ and $5\nu_0$.
<!--/ecat-->

## Q19

Physics · Ray Optics

An object is placed at a distance of $40\,\mathrm{cm}$ from a concave mirror of focal length $15\,\mathrm{cm}$. If the object is displaced through a distance of $20\,\mathrm{cm}$ towards the mirror, the displacement of the image will be

- (1) $30\,\mathrm{cm}$ away from the mirror
- (2) $30\,\mathrm{cm}$ towards the mirror
- **(3)** $36\,\mathrm{cm}$ away from the mirror
- (4) $36\,\mathrm{cm}$ towards the mirror

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Concave mirror (f = 15 cm) with object O on the principal axis 40 cm in front](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q019_sol_1_baea6e49_03112026.svg?v=baea6e49866f)

*Concave mirror (f = 15 cm) with object O on the principal axis 40 cm in front*

![drawn: Concave mirror (f = 15 cm) with object O on the principal axis 40 cm in front](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q019_solution_1_07ff10d1_03112026.svg?v=07ff10d19256)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\frac{1}{f} = \frac{1}{v_1} + \frac{1}{u}$
2. $-\frac{1}{15} = \frac{1}{v_1} - \frac{1}{40}$
3. $\Rightarrow \frac{1}{v_1} = \frac{1}{-15} + \frac{1}{40}$
4. $v_1 = -24\,\mathrm{cm}$
5. When object is displaced by $20\,\mathrm{cm}$ towards mirror.
6. Now, $u_2 = -20$
7. $\frac{1}{f} = \frac{1}{v_2} + \frac{1}{u_2}$
8. $\frac{1}{-15} = \frac{1}{v_2} - \frac{1}{20}$
9. $\frac{1}{v_2} = \frac{1}{20} - \frac{1}{15}$
10. $v_2 = -60\,\mathrm{cm}$
11. So, image shifts away from mirror by $= 60 - 24 = 36\,\mathrm{cm}$.

**Solved independently** (answer withheld)

1. Take the sign convention: $f = -15\,\mathrm{cm}$, initial $u_1 = -40\,\mathrm{cm}$.
2. $\frac{1}{v_1} = \frac{1}{f} - \frac{1}{u_1} = -\frac{1}{15} + \frac{1}{40} = \frac{-8+3}{120} = -\frac{1}{24}$, so $v_1 = -24\,\mathrm{cm}$.
3. Moving the object $20\,\mathrm{cm}$ towards the mirror gives $u_2 = -20\,\mathrm{cm}$.
4. $\frac{1}{v_2} = -\frac{1}{15} + \frac{1}{20} = \frac{-4+3}{60} = -\frac{1}{60}$, so $v_2 = -60\,\mathrm{cm}$.
5. $|v_2| - |v_1| = 60 - 24 = 36\,\mathrm{cm}$, with the image moving farther from the mirror, which is option $3$.

**Subtopic:** Mirror Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 6)

![printed question 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q019_cfdeb98a_03112026.png?v=cfdeb98ad2a3)

Publisher's solution, as printed:

![printed solution 19](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q019_c38c3d1a_03112026.png?v=c38c3d1a46a3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The mirror equation has to be solved at both object positions, because image displacement is the difference of two image distances and is not proportional to the object's displacement
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  The two image distances, $24\,\mathrm{cm}$ and $60\,\mathrm{cm}$, give the right size $36\,\mathrm{cm}$, and the sense is then copied from the object: the object went towards the mirror, so the image is read as going towards it too.
- **Why:** This question requires the mirror equation solved at two object positions and the image distances differenced, demonstrated by the stem supplying both '$40\,\mathrm{cm}$ from a concave mirror of focal length $15\,\mathrm{cm}$' and a further 'displaced through a distance of $20\,\mathrm{cm}$ towards the mirror'.
- **Note:** type_patterns called this `statement_options`; the printed options are a length with a direction attached, not claims to be judged, so the shape recorded here is mcq.
<!--/ecat-->

## Q20

Physics · Ray Optics

The refractive index of the material of a prism is $2$ and the angle of the prism is $30^\circ$. One of the two refracting surfaces of the prism is made a mirror inwards, by silver coating. A beam of monochromatic light entering the prism from the other face will retrace its path (after reflection from the silvered surface) if its angle of incidence on the prism is

- (1) $60^\circ$
- (2) $30^\circ$
- **(3)** $45^\circ$
- (4) Zero

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For retracing its path, light ray should be normally incident on silvered face.

![printed figure: Ray entering a 30° prism at M and striking the silvered face normally, retracing its path](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q020_sol_1_be87de08_03112026.svg?v=be87de085547)

*Ray entering a 30° prism at M and striking the silvered face normally, retracing its path*

![drawn: Ray entering a 30° prism at M and striking the silvered face normally, retracing its path](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q020_solution_1_60804339_03112026.svg?v=60804339b455)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Applying Snell's law at $\mathrm{M}$,
3. $\frac{\sin i}{\sin 30^\circ} = \frac{\sqrt{2}}{1}$
4. $\Rightarrow \sin i = \sqrt{2} \times \frac{1}{2}$
5. $\sin i = \frac{1}{\sqrt{2}}$ i.e. $i = 45^\circ$

**Solved independently** (answer withheld)

1. For the ray to retrace its path after reflection, it must strike the silvered face along the normal, so the angle of incidence on that face is $0^\circ$.
2. Inside the prism the refraction angle at the first face and the angle at the silvered face add to the prism angle: $r_1 + r_2 = A$ with $r_2 = 0$, so $r_1 = A = 30^\circ$.
3. Snell's law at the first face: $\sin i = \mu \sin r_1 = 2 \times \sin 30^\circ = 2 \times \frac{1}{2} = 1$, so $i = 90^\circ$, which is not among the options.
4. If the refractive index is $\sqrt{2}$ instead: $\sin i = \sqrt{2} \times \frac{1}{2} = \frac{1}{\sqrt{2}}$, so $i = 45^\circ$, which is option $3$.

**Subtopic:** Prism · **Difficulty:** unsure (3 steps)

**Printed in the booklet** (page 6)

![printed question 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q020_a58beba6_03112026.png?v=a58beba6c860)

Publisher's solution, as printed:

![printed solution 20](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q020_f7dba75a_03112026.png?v=f7dba75a0d76)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A ray retraces its path out of a silvered prism only if it meets the mirrored face normally, which fixes the internal refraction angle at the prism angle A and leaves $\sin i = \mu \sin A$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  With the refractive index as our record stores it ($\mu=2$) the retrace condition gives $\sin i = 2\sin 30^\circ = 1$, i.e. $i = 90^\circ$, which is not among the four options; with $\mu=\sqrt{2}$ it gives the printed key $45^\circ$. No route to any distractor can be stated until the index is confirmed against the printed paper.
- **Why:** This question requires the normal-incidence retrace condition turned into $\sin i = \mu \sin A$, demonstrated by the stem's 'will retrace its path (after reflection from the silvered surface)' and its printed prism angle of $30^\circ$.
- **Note:** The stem as stored is not solvable: $\mu=2$, $A=30^\circ$ forces $\sin i=1$ and no option matches, while $\mu=\sqrt{2}$ yields exactly the printed key of $45^\circ$, so the stored index has most likely lost its radical in extraction. Tagged as printed; the key is not re-judged. A reviewer holding the printed paper should check whether $60^\circ$ is reached by using the prism angle as the angle of incidence at the silvered face, and whether 'Zero' is reached by confusing normal incidence at the mirror with normal incidence at the entry face — both are plausible and neither can be confirmed on a stem with a missing character.
<!--/ecat-->

## Q21

Physics · Electromagnetic Waves

An em wave is propagating in a medium with a velocity $\vec{V} = V\hat{i}$. The instantaneous oscillating electric field of this em wave is along $+y$ axis. Then the direction of oscillating magnetic field of the em wave will be along

- (1) $-z$ direction
- (2) $-y$ direction
- **(3)** $+z$ direction
- (4) $-x$ direction

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\vec{E} \times \vec{B} = \vec{V}$
2. $(E\hat{j}) \times (\vec{B}) = V\hat{i}$
3. So, $\vec{B} = B\hat{k}$
4. Direction of propagation is along $+z$ direction.

**Solved independently** (answer withheld)

1. The direction of propagation of an em wave is along $\vec{E} \times \vec{B}$.
2. Here $\hat{E} = \hat{j}$ and the propagation direction is $\hat{i}$, so $\hat{j} \times \hat{B} = \hat{i}$.
3. Since $\hat{j} \times \hat{k} = \hat{i}$, $\hat{B} = \hat{k}$, i.e. the $+z$ direction, which is option $3$.

**Subtopic:** Transverse Nature of Electromagnetic Waves · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 7)

![printed question 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q021_3a2c9b3f_03112026.png?v=3a2c9b3f89fb)

Publisher's solution, as printed:

![printed solution 21](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q021_d8fb8aeb_03112026.png?v=d8fb8aeb24f1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** In an electromagnetic wave E, B and the direction of travel form a right-handed triad, with $\vec{E}\times\vec{B}$ pointing along the velocity
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The free axis is correctly found to be z, and then the triad is written the wrong way round — $\vec{B}\times\vec{E}$ along $\vec{V}$ — which flips the sign and gives $-z$.
- **Why:** This question requires the right-handed E-B-V triad applied to the printed axes, demonstrated by the stem fixing '$\vec{V} = V\hat{i}$' and the electric field 'along $+y$ axis' and asking only for a direction.
<!--/ecat-->

## Q22

Physics · Electromagnetic Induction

The magnetic potential energy stored in a certain inductor is $25\,\mathrm{mJ}$, when the current in the inductor is $60\,\mathrm{mA}$. This inductor is of inductance

- (1) $0.138\,\mathrm{H}$
- (2) $1.389\,\mathrm{H}$
- (3) $138.88\,\mathrm{H}$
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

1. Energy stored in an inductor: $U = \frac{1}{2} L I^2$.
2. Rearrange for inductance: $L = \frac{2U}{I^2}$.
3. Convert units: $U = 25\,\mathrm{mJ} = 25 \times 10^{-3}\,\mathrm{J}$, $I = 60\,\mathrm{mA} = 60 \times 10^{-3}\,\mathrm{A}$.
4. $I^2 = (60 \times 10^{-3})^2 = 3.6 \times 10^{-3}\,\mathrm{A^2}$.
5. $L = \frac{2 \times 25 \times 10^{-3}}{3.6 \times 10^{-3}} = \frac{50}{3.6} \approx 13.89\,\mathrm{H}$, which is option $4$.

**Subtopic:** Energy Stored in an Inductor · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 7)

![printed question 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q022_54050217_03112026.png?v=54050217e836)

Publisher's solution, as printed:

![printed solution 22](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q022_4a10c48c_03112026.png?v=4a10c48c1ab3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Energy stored in an inductor is $U=\tfrac{1}{2}LI^2$, so $L=2U/I^2$, and the milli prefix on the current is squared along with the number
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Converting $60\,\mathrm{mA}$ one decimal place short makes it $0.6\,\mathrm{A}$, so $I^2=0.36$ and $L=0.05/0.36=0.138\,\mathrm{H}$.
- **Why:** This question requires $U=\tfrac{1}{2}LI^2$ rearranged for L with both prefixes converted, demonstrated by the stem's '$25\,\mathrm{mJ}$' and '$60\,\mathrm{mA}$' and by the four options running 0.138, 1.389, 13.89 and 138.88 H — one digit string across four decades.
<!--/ecat-->

## Q23

Physics · Current Electricity

A battery consists of a variable number '$n$' of identical cells (having internal resistance '$r$' each) which are connected in series. The terminals of the battery are short-circuited and the current $I$ is measured. Which of the graphs shows the correct relationship between $I$ and $n$?

- **(1)** ![printed figure: Option (1): empty I versus n axes with origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q023_option_1_637de11a_03112026.svg?v=637de11ad2e2) *Option (1): empty I versus n axes with origin O* ![drawn: Option (1): empty I versus n axes with origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q023_option_1_4d2d9932_03112026.svg?v=4d2d9932da04)  
*drawn on the booklet's geometry, checked against its figure spec*
- (2) ![printed figure: Graph of I against n: curve rising from the origin and levelling off](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q023_option_2_efceff49_03112026.svg?v=efceff49346f) *Graph of I against n: curve rising from the origin and levelling off* ![drawn: Graph of I against n: curve rising from the origin and levelling off](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q023_option_2_5ea125ea_03112026.svg?v=5ea125ea3755)  
*drawn on the booklet's geometry, checked against its figure spec*
- (3) ![printed figure: Graph of I against n: a straight line rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q023_option_3_e73316a0_03112026.svg?v=e73316a04d48) *Graph of I against n: a straight line rising from the origin O* ![drawn: Graph of I against n: a straight line rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q023_option_3_0719f986_03112026.svg?v=0719f9861dc7)  
*drawn on the booklet's geometry, checked against its figure spec*
- (4) ![printed figure: Graph of I against n: a concave-up curve rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q023_option_4_9f184ca7_03112026.svg?v=9f184ca769fe) *Graph of I against n: a concave-up curve rising from the origin O* ![drawn: Graph of I against n: a concave-up curve rising from the origin O](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q023_option_4_37c551b8_03112026.svg?v=37c551b894bc)  
*drawn on the booklet's geometry, checked against its figure spec*

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $I = \frac{n\varepsilon}{nr} = \frac{\varepsilon}{r}$
2. So, $I$ is independent of $n$ and $I$ is constant.

![printed figure: Graph of I against n: a horizontal line, I independent of n](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q023_sol_1_b0e4b6bf_03112026.svg?v=b0e4b6bfb923)

*Graph of I against n: a horizontal line, I independent of n*

![drawn: Graph of I against n: a horizontal line, I independent of n](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q023_solution_1_ac06a6c8_03112026.svg?v=ac06a6c87be7)  
*drawn on the booklet's geometry, checked against its figure spec*


**Solved independently** (answer withheld)

1. With $n$ identical cells in series, the total emf is $nE$ and the total internal resistance is $nr$.
2. Short-circuiting the terminals makes the external resistance $R = 0$.
3. $I = \frac{nE}{nr + 0} = \frac{E}{r}$.
4. $I = \frac{E}{r}$ does not depend on $n$, so the $I$-$n$ graph is a horizontal line parallel to the $n$-axis.
5. Options $2$ (saturating curve), $3$ (straight line through the origin) and $4$ (rising concave-up curve) all show $I$ increasing with $n$, so they are wrong; the answer is option $1$.

**Subtopic:** Combination of Cells · **Difficulty:** unsure (3 steps)

**Printed in the booklet** (page 7)

![printed question 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q023_98a11de5_03112026.png?v=98a11de542df)

Publisher's solution, as printed:

![printed solution 23](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q023_b2be202c_03112026.png?v=b2be202c4a84)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** Short-circuiting n identical cells in series gives $I = n\varepsilon/(nr) = \varepsilon/r$, so the current does not depend on how many cells are used
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The four options are graphs and this step was given four empty option strings with no graph image, so which curve each option carries cannot be read and no route to a wrong curve can be named.
- **Why:** This question requires a relation translated into a curve, demonstrated by the stem asking 'Which of the graphs shows the correct relationship between $I$ and $n$?'.
- **Note:** The options arrived as four empty strings and `figure_image` is null, so the option graphs were not supplied to this step; the paper itself plainly printed them. A reviewer holding the graphs should check for a straight line rising through the origin — the curve a student gets by scaling the emf with n while leaving the internal resistance at r — and for a falling $1/n$ curve, from scaling the internal resistance while leaving the emf at one cell's value. Either would be a dropped-term device on the printed options, but neither can be confirmed here.
<!--/ecat-->

## Q24

Physics · Current Electricity

A set of '$n$' equal resistors, of value '$R$' each, are connected in series to a battery of emf '$E$' and internal resistance '$R$'. The current drawn is $I$. Now, the '$n$' resistors are connected in parallel to the same battery. Then the current drawn from battery becomes $10\,I$. The value of '$n$' is

- **(1)** 10
- (2) 20
- (3) 11
- (4) 9

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $I = \frac{E}{nR + R}$ ...(i)
2. $10\,I = \frac{E}{\frac{R}{n} + R}$ ...(ii)
3. Dividing (ii) by (i),
4. $10 = \frac{(n + 1)R}{\left(\frac{1}{n} + 1\right)R}$
5. After solving the equation, $n = 10$

**Solved independently** (answer withheld)

1. In series, total resistance is $nR + R = (n+1)R$, so $I = \frac{E}{(n+1)R}$.
2. In parallel, the $n$ resistors give $\frac{R}{n}$, so total resistance is $\frac{R}{n} + R = \frac{(n+1)R}{n}$.
3. $I' = \frac{E}{(n+1)R/n} = \frac{nE}{(n+1)R} = nI$.
4. $I' = 10I \Rightarrow nI = 10I \Rightarrow n = 10$, which is option $1$.

**Subtopic:** Combination of Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q024_07899914_03112026.png?v=078999144fec)

Publisher's solution, as printed:

![printed solution 24](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q024_2b786c92_03112026.png?v=2b786c9261b5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The battery's internal resistance R stays in the circuit in both arrangements, which makes the series current $E/((n+1)R)$, the parallel current $nE/((n+1)R)$, and their ratio exactly n
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 3  
  Keeping the internal resistance in the parallel circuit but writing the series current as $E/(nR)$ leaves the ratio $n^2/(n+1)$, whose root for a tenfold rise is $10.9$, and 11 is the integer sitting in the options.
- **Why:** This question requires both circuit currents built with the internal resistance kept in each, demonstrated by the stem printing 'internal resistance $R$' and 'the current drawn from battery becomes $10\,I$'.
<!--/ecat-->

## Q25

Physics · Current Electricity

A carbon resistor of $(47 \pm 4.7)\,\mathrm{k\Omega}$ is to be marked with rings of different colours for its identification. The colour code sequence will be

- (1) Violet – Yellow – Orange – Silver
- (2) Yellow – Green – Violet – Gold
- **(3)** Yellow – Violet – Orange – Silver
- (4) Green – Orange – Violet – Gold

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $(47 \pm 4.7)\,\mathrm{k\Omega} = 47 \times 10^{3} \pm 10\%$
2. $\therefore$ Yellow – Violet – Orange – Silver

**Solved independently** (answer withheld)

1. $R = 47\,\mathrm{k\Omega} = 47 \times 10^{3}\,\Omega$.
2. First digit $4$ is Yellow; second digit $7$ is Violet.
3. Multiplier $10^{3}$ is Orange.
4. Tolerance $= \frac{4.7}{47} \times 100\% = 10\%$, which is Silver.
5. Sequence Yellow – Violet – Orange – Silver, which is option $3$.

**Subtopic:** Colour Code of Carbon Resistors · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 7)

![printed question 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q025_fec3a4c8_03112026.png?v=fec3a4c89ea9)

Publisher's solution, as printed:

![printed solution 25](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q025_f2a2d3c4_03112026.png?v=f2a2d3c4691d)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Encoding a resistance into bands: the two digits in order, then the decade multiplier, then the tolerance read as a percentage of the value
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Yellow for 4 and violet for 7 are both correct here, but printed as violet-yellow they encode 74, not 47; the multiplier and tolerance bands in this option are the right ones, so only the digit order has been turned round
- **Why:** This question requires applying the colour-code convention to a stated resistance and tolerance, demonstrated by 'a carbon resistor of (47 plus or minus 4.7) kilo-ohm is to be marked with rings of different colours'.
- **Note:** E1's pattern called this arrange_in_order; the live qtype list has no ordering shape, and each option here is a set of four band values accepted or rejected whole, so two_part is recorded and the ordering demand sits in the route. asks is apply_rule rather than order because the task is to encode a value by an agreed convention, not to rank items. On the reversed tie-break: the swap covers the whole of the two-band digit sequence, not one interior adjacency of a longer order, so reversed holds.
<!--/ecat-->

## Q26

Physics · Waves

A tuning fork is used to produce resonance in a glass tube. The length of the air column in this tube can be adjusted by a variable piston. At room temperature of $27^\circ\mathrm{C}$ two successive resonances are produced at $20\,\mathrm{cm}$ and $73\,\mathrm{cm}$ of column length. If the frequency of the tuning fork is $320\,\mathrm{Hz}$, the velocity of sound in air at $27^\circ\mathrm{C}$ is

- (1) $330\,\mathrm{m/s}$
- (2) $350\,\mathrm{m/s}$
- **(3)** $339\,\mathrm{m/s}$
- (4) $300\,\mathrm{m/s}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $v = 2\,(\nu)\,[L_2 - L_1]$
2. $= 2 \times 320\,[73 - 20] \times 10^{-2}$
3. $= 339.2\,\mathrm{ms^{-1}}$
4. $= 339\,\mathrm{m/s}$

**Solved independently** (answer withheld)

1. Two successive resonance lengths in a resonance tube differ by half a wavelength: $l_2 - l_1 = \frac{\lambda}{2}$.
2. $\frac{\lambda}{2} = 73\,\mathrm{cm} - 20\,\mathrm{cm} = 53\,\mathrm{cm}$.
3. $\lambda = 2 \times 53\,\mathrm{cm} = 106\,\mathrm{cm} = 1.06\,\mathrm{m}$.
4. $v = f\lambda = 320\,\mathrm{Hz} \times 1.06\,\mathrm{m} = 339.2\,\mathrm{m/s}$.
5. $339.2\,\mathrm{m/s} \approx 339\,\mathrm{m/s}$, which is option $3$.

**Subtopic:** Organ Pipe · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 8)

![printed question 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q026_4b578923_03112026.png?v=4b57892311af)

Publisher's solution, as printed:

![printed solution 26](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q026_2b12a184_03112026.png?v=2b12a184b6e8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Two successive resonances in a tube are half a wavelength apart, so $v = f\times2(l_2-l_1)$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  330 m/s is the stock textbook figure for the speed of sound in air, and it is true of air near room temperature; the stem supplies two column lengths and a frequency precisely so that the speed is measured, and the measurement gives $320\times2(0.73-0.20) = 339\,\mathrm{m/s}$
- **Why:** This question requires computing the speed of sound from the separation of two resonances, demonstrated by 'two successive resonances are produced at 20 cm and 73 cm of column length. If the frequency of the tuning fork is 320 Hz'.
<!--/ecat-->

## Q27

Physics · Capacitance

The electrostatic force between the metal plates of an isolated parallel plate capacitor $C$ having a charge $Q$ and area $A$, is

- **(1)** Independent of the distance between the plates
- (2) Proportional to the square root of the distance between the plates
- (3) Linearly proportional to the distance between the plates
- (4) Inversely proportional to the distance between the plates

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For isolated capacitor $Q = \text{Constant}$
2. $F_{\mathrm{plate}} = \frac{Q^{2}}{2A\varepsilon_{0}}$
3. $F$ is Independent of the distance between plates.

**Solved independently** (answer withheld)

1. The capacitor is isolated, so its charge $Q$ stays constant as $d$ changes.
2. Field due to one plate at the other plate: $E_1 = \frac{\sigma}{2\varepsilon_0} = \frac{Q}{2\varepsilon_0 A}$.
3. Force on the other plate: $F = Q E_1 = \frac{Q^2}{2\varepsilon_0 A}$.
4. $F$ contains no $d$, so it is independent of the distance between the plates, which is option $1$.

**Subtopic:** The Parallel Plate Capacitor · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q027_38ee5362_03112026.png?v=38ee5362df47)

Publisher's solution, as printed:

![printed solution 27](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q027_2e998d7a_03112026.png?v=2e998d7aedd6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a fixed charge the field between the plates is $Q/\varepsilon_0A$, so the attraction $Q^2/2\varepsilon_0A$ does not depend on the separation at all
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Writing the stored energy as $Q^2/2C$ and the force as energy over separation gives $F = Q^2/2Cd$, which falls as $1/d$ - but only if $C$ is held fixed, and $C$ itself is $\varepsilon_0A/d$, which cancels the $d$ out
- **Why:** This question requires stating how one quantity depends on another, demonstrated by the options being four rival dependences of the force on 'the distance between the plates' for a capacitor 'having a charge Q and area A'.
- **Note:** asks is relation because the answer is how the force moves when the separation is changed; nothing numerical is produced. E1's pattern called this statement_options, but the options are short dependence phrases, not statements to be judged, so the shape recorded is mcq.
<!--/ecat-->

## Q28

Physics · Electrostatics

An electron falls from rest through a vertical distance $h$ in a uniform and vertically upward directed electric field $E$. The direction of electric field is now reversed, keeping its magnitude the same. A proton is allowed to fall from rest in it through the same vertical distance $h$. The time of fall of the electron, in comparison to the time of fall of the proton is

- **(1)** Smaller
- (2) 10 times greater
- (3) 5 times greater
- (4) Equal

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $h = \frac{1}{2}\frac{eE}{m}t^{2}$
2. $\therefore\ t = \sqrt{\frac{2hm}{eE}}$
3. $\therefore\ t \propto \sqrt{m}$ as ‘$e$’ is same for electron and proton.
4. $\because$ Electron has smaller mass so it will take smaller time.

**Solved independently** (answer withheld)

1. With $\vec{E}$ upward, the force on the electron $-e\vec{E}$ points downward, so $a_e = \frac{eE}{m_e}$ downward.
2. With $\vec{E}$ reversed (downward), the force on the proton $e\vec{E}$ points downward, so $a_p = \frac{eE}{m_p}$ downward.
3. Falling from rest through $h$: $h = \frac{1}{2} a t^2 \Rightarrow t = \sqrt{\frac{2h}{a}} = \sqrt{\frac{2hm}{eE}}$.
4. $\frac{t_e}{t_p} = \sqrt{\frac{m_e}{m_p}} < 1$ since $m_e \ll m_p$.
5. Including gravity, $a_e = g + \frac{eE}{m_e} > a_p = g + \frac{eE}{m_p}$, so still $t_e < t_p$: the electron's time is smaller, option $1$.

**Subtopic:** Motion of Charged Particle in Uniform Electric Field · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 8)

![printed question 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q028_d2869794_03112026.png?v=d28697942afa)

Publisher's solution, as printed:

![printed solution 28](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q028_38a38ecf_03112026.png?v=38a38ecf5e62)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** In an electric field the acceleration is $qE/m$, so the mass does not cancel and the lighter particle crosses the same drop sooner
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  'All bodies fall through the same height in the same time' is true because gravity gives every mass the same acceleration $g$; here the acceleration is $eE/m$, so the electron's much smaller mass makes it the faster faller and the times cannot be equal
- **Why:** This question requires comparing two times of fall under the same field, demonstrated by 'the time of fall of the electron, in comparison to the time of fall of the proton is'.
- **Note:** asks is relation because the options are how-many-times answers about one quantity changing with another (the time with the mass), and no value is computed.
<!--/ecat-->

## Q29

Physics · Oscillations

A pendulum is hung from the roof of a sufficiently high building and is moving freely to and fro like a simple harmonic oscillator. The acceleration of the bob of the pendulum is $20\,\mathrm{m/s^2}$ at a distance of $5\,\mathrm{m}$ from the mean position. The time period of oscillation is

- (1) $2\pi\,\mathrm{s}$
- (2) $2\,\mathrm{s}$
- **(3)** $\pi\,\mathrm{s}$
- (4) $1\,\mathrm{s}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $|a| = \omega^{2}y$
2. $\Rightarrow\ 20 = \omega^{2}(5)$
3. $\Rightarrow\ \omega = 2\,\mathrm{rad/s}$
4. $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi\,\mathrm{s}$

**Solved independently** (answer withheld)

1. In SHM the magnitude of acceleration is $|a| = \omega^2 x$.
2. $\omega^2 = \frac{a}{x} = \frac{20}{5} = 4\,\mathrm{s^{-2}}$.
3. $\omega = 2\,\mathrm{rad/s}$.
4. $T = \frac{2\pi}{\omega} = \frac{2\pi}{2} = \pi\,\mathrm{s}$, which is option $3$.

**Subtopic:** Calculate Time Period of SHM, Acceleration in SHM · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q029_c3c6603a_03112026.png?v=c3c6603a173e)

Publisher's solution, as printed:

![printed solution 29](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q029_fc94c4d0_03112026.png?v=fc94c4d01cb3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In SHM the acceleration is $\omega^2x$, so $\omega = \sqrt{a/x}$ and the period is $2\pi/\omega$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  $\sqrt{20/5} = 2$ is the angular frequency in rad/s, and stopping there offers it as the period; the period is $2\pi/\omega = \pi\,\mathrm{s}$
- **Why:** This question requires computing the period from the acceleration at a stated displacement, demonstrated by 'the acceleration of the bob of the pendulum is 20 m/s squared at a distance of 5 m from the mean position'.
- **Note:** The pendulum framing is decoration: no length or $g$ is given, and the answer comes from $a=\omega^2x$ alone.
<!--/ecat-->

## Q30

Physics · Thermal Properties of Matter

The power radiated by a black body is $P$ and it radiates maximum energy at wavelength, $\lambda_0$. If the temperature of the black body is now changed so that it radiates maximum energy at wavelength $\frac{3}{4}\lambda_0$, the power radiated by it becomes $nP$. The value of $n$ is

- (1) $\frac{3}{4}$
- **(2)** $\frac{256}{81}$
- (3) $\frac{4}{3}$
- (4) $\frac{81}{256}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. We know, $\lambda_{\mathrm{max}}\,T = \text{constant}$ (Wien's law)
2. So, $\lambda_{\mathrm{max}_1}T_1 = \lambda_{\mathrm{max}_2}T_2$
3. $\Rightarrow \lambda_0\,T = \frac{3\lambda_0}{4}T'$
4. $\Rightarrow T' = \frac{4}{3}T$
5. So, $\frac{P_2}{P_1} = \left(\frac{T'}{T}\right)^4 = \left(\frac{4}{3}\right)^4 = \frac{256}{81}$

**Solved independently** (answer withheld)

1. Wien's displacement law: $\lambda_m T = b$ (constant), so $T \propto \frac{1}{\lambda_m}$.
2. $\frac{T'}{T} = \frac{\lambda_0}{\frac{3}{4}\lambda_0} = \frac{4}{3}$.
3. Stefan-Boltzmann law: $P = \sigma A T^4$, so $P \propto T^4$ for the same body.
4. $n = \frac{P'}{P} = \left(\frac{T'}{T}\right)^4 = \left(\frac{4}{3}\right)^4 = \frac{256}{81}$, which is option $2$.

**Subtopic:** Radiation Laws · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 8)

![printed question 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q030_81bdaecb_03112026.png?v=81bdaecbb1b5)

Publisher's solution, as printed:

![printed solution 30](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q030_cf1ad642_03112026.png?v=cf1ad6423de5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** Wien's law makes the temperature inverse to the peak wavelength, and Stefan's law makes the power go as the fourth power of that temperature
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Taking the temperature to follow the wavelength, $T' = \frac34T$, and then raising it to the fourth power gives $(3/4)^4 = 81/256$; Wien's law is $\lambda_mT = $ constant, so a shorter peak wavelength means a hotter body and $T' = \frac43T$
- **Why:** This question requires chaining two radiation laws to a power ratio, demonstrated by 'if the temperature ... is now changed so that it radiates maximum energy at wavelength three-quarters of lambda-zero, the power radiated by it becomes nP'.
<!--/ecat-->

## Q31

Physics · Mechanical Properties of Solids

Two wires are made of the same material and have the same volume. The first wire has cross-sectional area $A$ and the second wire has cross-sectional area $3A$. If the length of the first wire is increased by $\Delta l$ on applying a force $F$, how much force is needed to stretch the socond wire by the same amount?

- **(1)** $9F$
- (2) $4F$
- (3) $6F$
- (4) $F$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Wire 1 :

![printed figure: A wire of area A and length 3l pulled by a force F](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q031_sol_1_fc5a920f_03112026.svg?v=fc5a920fac7c)

*A wire of area A and length 3l pulled by a force F*

![drawn: A wire of area A and length 3l pulled by a force F](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q031_solution_1_38593bcf_03112026.svg?v=38593bcf1f72)  
*drawn on the booklet's geometry, checked against its figure spec*

2. Wire 2 :

![printed figure: The second wire (cross-section 3A, length l) drawn as a horizontal cylinder, pulled to the right by force F′](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q031_sol_2_d293639b_03112026.svg?v=d293639b7d87)

*The second wire (cross-section 3A, length l) drawn as a horizontal cylinder, pulled to the right by force F′*

![drawn: The second wire (cross-section 3A, length l) drawn as a horizontal cylinder, pulled to the right by force F′](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q031_solution_2_22177452_03112026.svg?v=2217745274fb)  
*drawn on the booklet's geometry, checked against its figure spec*

3. For wire 1, $\Delta l = \left(\frac{F}{AY}\right)3l \quad \ldots(\mathrm{i})$
4. For wire 2, $\frac{F'}{3A} = Y\frac{\Delta l}{l}$
5. $\Rightarrow \Delta l = \left(\frac{F'}{3AY}\right)l \quad \ldots(\mathrm{ii})$
6. From equation (i) & (ii), $\Delta l = \left(\frac{F}{AY}\right)3l = \left(\frac{F'}{3AY}\right)l$
7. $\Rightarrow \boxed{F' = 9F}$

**Solved independently** (answer withheld)

1. Equal volumes give $A\,l_1 = 3A\,l_2$, so $l_2 = \frac{l_1}{3}$.
2. From Young's modulus, the extension is $\Delta l = \frac{F L}{A Y}$.
3. First wire: $\Delta l = \frac{F l_1}{A Y}$.
4. Second wire: $\Delta l = \frac{F' (l_1/3)}{3A\,Y} = \frac{F' l_1}{9 A Y}$.
5. Equating the two extensions gives $\frac{F' l_1}{9AY} = \frac{F l_1}{AY}$, so $F' = 9F$, which is option $1$.

**Subtopic:** Determination of Young's Modulus · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 9)

![printed question 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q031_1fc9a96b_03112026.png?v=1fc9a96b1b29)

Publisher's solution, as printed:

![printed solution 31](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q031_27ea0760_03112026.png?v=27ea0760aaa9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At fixed volume the length falls as the area rises, so $F = YA\Delta l/L$ scales as the square of the area
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  Equal volume is read as 'nothing that matters has changed': since $AL$ is the same for both wires, the ratio $A/L$ is taken to be the same too, so the same force is thought to give the same extension - but $AL$ constant makes $A/L$ grow as $A^2$
- **Why:** This question requires stating how many times the force changes when the cross-section changes at fixed volume, demonstrated by 'how much force is needed to stretch the second wire by the same amount'.
<!--/ecat-->

## Q32

Physics · Mechanical Properties of Fluids

A small sphere of radius $'r'$ falls from rest in a viscous liquid. As a result, heat is produced due to viscous force. The rate of production of heat when the sphere attains its terminal velocity, is proportional to

- (1) $r^{3}$
- **(2)** $r^{5}$
- (3) $r^{2}$
- (4) $r^{4}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Power $= 6\pi\eta r V_{T} \cdot V_{T} = 6\pi\eta r V_{T}^{2}$
2. $V_{T} \propto r^{2}$
3. $\Rightarrow$ Power $\propto r^{5}$

**Solved independently** (answer withheld)

1. At terminal velocity, $v_t = \frac{2 r^{2} (\rho - \sigma) g}{9 \eta}$, so $v_t \propto r^{2}$.
2. Viscous force by Stokes' law: $F = 6 \pi \eta r v_t \propto r \cdot r^{2} = r^{3}$.
3. Rate of heat production equals power against viscous force: $P = F v_t \propto r^{3} \cdot r^{2} = r^{5}$, which is option $2$.

**Subtopic:** Stokes' Law and Poiseuille's Equation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q032_66a5a39b_03112026.png?v=66a5a39b57da)

Publisher's solution, as printed:

![printed solution 32](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q032_3532700d_03112026.png?v=3532700d5c6f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** At terminal velocity the heat rate is the viscous force times the speed, $6\pi\eta r v_t\times v_t$, and $v_t$ itself goes as $r^2$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $r^2$ is the true dependence of the terminal velocity, which is the one stored result of this subtopic and the first step of this problem; the rate of heat production is a power, $Fv_t$, and carries three more powers of $r$ than that
- **Why:** This question requires stating how the rate of heat production depends on the radius, demonstrated by 'the rate of production of heat when the sphere attains its terminal velocity, is proportional to'.
- **Note:** The four options are exactly the dropped-factor family of $r^5$: $r^2$ keeps only $v_t$, $r^3$ drops one factor of $v_t$ and $r^4$ drops the radius inside the drag.
<!--/ecat-->

## Q33

Physics · Thermodynamics

A sample of $0.1\,\mathrm{g}$ of water at $100^\circ\mathrm{C}$ and normal pressure ($1.013 \times 10^{5}\,\mathrm{N\,m^{-2}}$) requires $54\,\mathrm{cal}$ of heat energy to convert to steam at $100^\circ\mathrm{C}$. If the volume of the steam produced is $167.1\,\mathrm{cc}$, the change in internal energy of the sample, is

- (1) $104.3\,\mathrm{J}$
- (2) $42.2\,\mathrm{J}$
- **(3)** $208.7\,\mathrm{J}$
- (4) $84.5\,\mathrm{J}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\Delta Q = \Delta U + \Delta W$
2. $\Rightarrow\ 54 \times 4.18 = \Delta U + 1.013 \times 10^{5}(167.1 \times 10^{-6} - 0)$
3. $\Rightarrow\ \Delta U = 208.7\,\mathrm{J}$

**Solved independently** (answer withheld)

1. First law of thermodynamics: $\Delta U = Q - W$, with $W = P\Delta V$ at constant pressure.
2. Heat supplied: $Q = 54\,\mathrm{cal} \times 4.18\,\mathrm{J\,cal^{-1}} \approx 225.7\,\mathrm{J}$.
3. Initial volume of $0.1\,\mathrm{g}$ water $= 0.1\,\mathrm{cc}$, so $\Delta V = 167.1 - 0.1 = 167.0\,\mathrm{cc} = 1.670 \times 10^{-4}\,\mathrm{m^3}$.
4. $W = P\Delta V = 1.013 \times 10^{5} \times 1.670 \times 10^{-4} \approx 16.9\,\mathrm{J}$.
5. $\Delta U = 225.7 - 16.9 \approx 208.8\,\mathrm{J}$, which matches $208.7\,\mathrm{J}$, option $3$.

**Subtopic:** Heat, Internal Energy, and Work · **Difficulty:** easy (3 steps)

**Printed in the booklet** (page 9)

![printed question 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q033_6467834d_03112026.png?v=6467834db399)

Publisher's solution, as printed:

![printed solution 33](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q033_dc21130b_03112026.png?v=dc21130b69ca)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** First law at constant pressure: the internal energy change is the heat put in minus the expansion work $P\Delta V$
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The routes that exist on these numbers are $Q = 54\times4.18 = 225.7\,\mathrm{J}$, $W = 1.013\times10^5\times167\times10^{-6} = 16.9\,\mathrm{J}$ and $\Delta U = 208.7\,\mathrm{J}$ (the key). Dropping the work gives 225.7 J and adding it instead of subtracting gives 242.6 J, and neither is printed; the three wrong options are 0.20, 0.40 and 0.50 of the key, and no operation on 54 cal, $1.013\times10^5\,\mathrm{N\,m^{-2}}$ and 167.1 cc produces those factors.
- **Why:** This question requires computing the internal energy change from the first law, demonstrated by 'requires 54 cal of heat energy to convert to steam ... if the volume of the steam produced is 167.1 cc, the change in internal energy of the sample, is'.
- **Note:** no_trap is the finding, and the evidence is that the two natural wrong answers - the heat alone (225.7 J) and the heat plus the work (242.6 J) - are both absent from the options, while the three printed distractors are fixed fractions of the key with no derivation behind them.
<!--/ecat-->

## Q34

Physics · Rotational Motion

The moment of the force, $\vec{F} = 4\hat{i} + 5\hat{j} - 6\hat{k}$ at $(2, 0, -3)$, about the point $(2, -2, -2)$, is given by

- (1) $-8\hat{i} - 4\hat{j} - 7\hat{k}$
- (2) $-7\hat{i} - 8\hat{j} - 4\hat{k}$
- (3) $-4\hat{i} - \hat{j} - 8\hat{k}$
- **(4)** $-7\hat{i} - 4\hat{j} - 8\hat{k}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Position vectors r0 (O to A) and r (O to P), the vector r - r0 from A to P, and the force F acting along a line through P](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q034_sol_1_67e43d87_03112026.svg?v=67e43d875f23)

*Position vectors r0 (O to A) and r (O to P), the vector r - r0 from A to P, and the force F acting along a line through P*

![drawn: Position vectors r0 (O to A) and r (O to P), the vector r - r0 from A to P, and the force F acting along a line through P](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q034_solution_1_239a693d_03112026.svg?v=239a693d140e)  
*drawn on the booklet's geometry, checked against its figure spec*

1. $\vec{\tau} = (\vec{r} - \vec{r}_0) \times \vec{F}$ ...(i)
2. $\vec{r} - \vec{r}_0 = (2\hat{i} + 0\hat{j} - 3\hat{k}) - (2\hat{i} - 2\hat{j} - 2\hat{k})$
3. $= 0\hat{i} + 2\hat{j} - \hat{k}$
4. $\vec{\tau} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 0 & 2 & -1 \\ 4 & 5 & -6 \end{vmatrix} = -7\hat{i} - 4\hat{j} - 8\hat{k}$

**Solved independently** (answer withheld)

1. The position vector from the point $(2,-2,-2)$ to the point of application $(2,0,-3)$ is $\vec{r} = (2-2)\hat{i} + (0+2)\hat{j} + (-3+2)\hat{k} = 2\hat{j} - \hat{k}$.
2. The moment is $\vec{\tau} = \vec{r} \times \vec{F}$ with $\vec{F} = 4\hat{i} + 5\hat{j} - 6\hat{k}$.
3. $\tau_x = r_y F_z - r_z F_y = (2)(-6) - (-1)(5) = -7$.
4. $\tau_y = r_z F_x - r_x F_z = (-1)(4) - (0)(-6) = -4$.
5. $\tau_z = r_x F_y - r_y F_x = (0)(5) - (2)(4) = -8$.
6. $\vec{\tau} = -7\hat{i} - 4\hat{j} - 8\hat{k}$, which is option $4$.

**Subtopic:** Problems on Torque of a Force About the Axis of Rotation · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 9)

![printed question 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q034_342285b2_03112026.png?v=342285b2d324)

Publisher's solution, as printed:

![printed solution 34](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q034_2732e80a_03112026.png?v=2732e80a4cdb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Moment of a force about a point: shift the position vector to that point first, $\vec r = (0,2,-1)$, then take $\vec r\times\vec F$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The three minors come out as $-7$, $-4$ and $-8$, and this option prints them in the reverse order, attaching the k-value to $\hat i$ and the i-value to $\hat k$
- **Why:** This question requires computing a cross product after shifting the position vector, demonstrated by 'the moment of the force ... at (2, 0, -3), about the point (2, -2, -2)'.
- **Note:** Two of the three wrong options are permutations of the correct components, so the arithmetic alone does not separate them; what separates them is keeping each minor attached to its own unit vector.
<!--/ecat-->

## Q35

Physics · Units and Measurements

A student measured the diameter of a small steel ball using a screw gauge of least count $0.001\,\mathrm{cm}$. The main scale reading is $5\,\mathrm{mm}$ and zero of circular scale division coincides with $25$ divisions above the reference level. If screw gauge has a zero error of $-0.004\,\mathrm{cm}$, the correct diameter of the ball is

- (1) $0.521\,\mathrm{cm}$
- (2) $0.053\,\mathrm{cm}$
- (3) $0.525\,\mathrm{cm}$
- **(4)** $0.529\,\mathrm{cm}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Diameter of the ball
2. $= \mathrm{MSR} + \mathrm{CSR} \times (\text{Least count}) - \text{Zero error}$
3. $= 0.5\,\mathrm{cm} + 25 \times 0.001 - (-0.004)$
4. $= 0.5 + 0.025 + 0.004$
5. $= 0.529\,\mathrm{cm}$

**Solved independently** (answer withheld)

1. Main scale reading: $5\,\mathrm{mm} = 0.5\,\mathrm{cm}$.
2. Circular scale contribution: $25 \times 0.001\,\mathrm{cm} = 0.025\,\mathrm{cm}$.
3. Observed reading: $0.5 + 0.025 = 0.525\,\mathrm{cm}$.
4. Correct reading = observed reading $-$ zero error: $0.525 - (-0.004) = 0.529\,\mathrm{cm}$, which is option $4$.

**Subtopic:** Vernier Calliper and Screw Gauge · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 10)

![printed question 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q035_4a39f72a_03112026.png?v=4a39f72a4347)

Publisher's solution, as printed:

![printed solution 35](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q035_a7858298_03112026.png?v=a78582988dfc)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A screw-gauge reading is main scale plus circular divisions times least count, and a negative zero error has to be added back, not taken off
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  Subtracting the stated zero error instead of subtracting its sign-carrying value gives $0.525 - 0.004 = 0.521\,\mathrm{cm}$; because the error is $-0.004\,\mathrm{cm}$, the correction $0.525 - (-0.004)$ adds and gives 0.529 cm
- **Why:** This question requires computing a corrected instrument reading, demonstrated by 'if screw gauge has a zero error of -0.004 cm, the correct diameter of the ball is'.
<!--/ecat-->

## Q36

Physics · Laws of Motion

A block of mass m is placed on a smooth inclined wedge ABC of inclination $\theta$ as shown in the figure. The wedge is given an acceleration 'a' towards the right. The relation between a and $\theta$ for the block to remain stationary on the wedge is

![printed figure: Block m resting on a smooth hatched wedge ABC of inclination θ, the wedge pushed with acceleration a to the right](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q036_65fb266e_03112026.svg?v=65fb266e54d2)

*Block m resting on a smooth hatched wedge ABC of inclination θ, the wedge pushed with acceleration a to the right*

![drawn: Block m resting on a smooth hatched wedge ABC of inclination θ, the wedge pushed with acceleration a to the right](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q036_question_e482a251_03112026.svg?v=e482a2511f98)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $a = \dfrac{g}{\operatorname{cosec}\theta}$
- (2) $a = g\cos\theta$
- (3) $a = \dfrac{g}{\sin\theta}$
- **(4)** $a = g\tan\theta$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: Forces on a block resting on a wedge accelerating with a, including the pseudo force ma](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q036_sol_1_7bcf8306_03112026.svg?v=7bcf83065b0d)

*Forces on a block resting on a wedge accelerating with a, including the pseudo force ma*

![drawn: Forces on a block resting on a wedge accelerating with a, including the pseudo force ma](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q036_solution_1_dea029b9_03112026.svg?v=dea029b99b50)  
*drawn on the booklet's geometry, checked against its figure spec*

1. In non-inertial frame,
2. $N\sin\theta = ma$ ...(i)
3. $N\cos\theta = mg$ ...(ii)
4. $\tan\theta = \frac{a}{g}$
5. $a = g\tan\theta$

**Solved independently** (answer withheld)

1. The figure shows the incline face rising to the left (from $B$ up to $A$), so its normal points up and to the right. Pushing the wedge to the right can therefore hold the block.
2. In the wedge frame, the block feels gravity $mg$ downward, a pseudo force $ma$ to the left, and the normal force $N$. The surface is smooth, so there is no friction.
3. Gravity's component down the slope (towards $B$) is $mg\sin\theta$.
4. The pseudo force's component up the slope (towards $A$) is $ma\cos\theta$.
5. For equilibrium along the incline: $ma\cos\theta = mg\sin\theta$.
6. $a = g\frac{\sin\theta}{\cos\theta} = g\tan\theta$, which is option $4$.

**Subtopic:** Pseudo Force · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 10)

![printed question 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q036_9fc1b1c2_03112026.png?v=9fc1b1c221f3)

Publisher's solution, as printed:

![printed solution 36](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q036_4b171fe3_03112026.png?v=4b171fe30ede)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In the wedge's frame the block is held by two resolved forces: $ma\cos\theta$ up the slope against $mg\sin\theta$ down it, giving $a = g\tan\theta$
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The component of gravity along the slope, $mg\sin\theta$, is written down correctly and then set against the whole pseudo-force $ma$ rather than its component $ma\cos\theta$, which gives $a = g\sin\theta$ - the option printed as $g/\mathrm{cosec}\,\theta$
- **Why:** This question requires deriving the condition for equilibrium on an accelerating wedge, demonstrated by 'the relation between a and theta for the block to remain stationary on the wedge is'.
- **Note:** The figure is supplied as a drawn spec, with the inclination marked at B and the acceleration arrow pointing right, and it is what fixes which angle is theta. The three wrong options are the three ways of resolving one of the two forces and not the other.
<!--/ecat-->

## Q37

Physics · Kinematics

A toy car with charge $q$ moves on a frictionless horizontal plane surface under the influence of a uniform electric field $\vec{E}$. Due to the force $q\vec{E}$, its velocity increases from $0$ to $6\,\mathrm{m/s}$ in one second duration. At that instant the direction of the field is reversed. The car continues to move for two more seconds under the influence of this field. The average velocity and the average speed of the toy car between $0$ to $3$ seconds are respectively

- (1) $2\,\mathrm{m/s}$, $4\,\mathrm{m/s}$
- (2) $1\,\mathrm{m/s}$, $3.5\,\mathrm{m/s}$
- **(3)** $1\,\mathrm{m/s}$, $3\,\mathrm{m/s}$
- (4) $1.5\,\mathrm{m/s}$, $3\,\mathrm{m/s}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Toy car path A to B and back to C with times, velocities and accelerations](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q037_sol_1_d9812a5f_03112026.svg?v=d9812a5f66df)

*Toy car path A to B and back to C with times, velocities and accelerations*

![drawn: Toy car path A to B and back to C with times, velocities and accelerations](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q037_solution_1_2c71be86_03112026.svg?v=2c71be86235d)  
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

1. Acceleration in the first second: $a = \frac{6 - 0}{1} = 6\,\mathrm{m/s^2}$.
2. Distance in $0$ to $1\,\mathrm{s}$: $s_1 = \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$, ending at $v = 6\,\mathrm{m/s}$.
3. After reversal $a = -6\,\mathrm{m/s^2}$, so the car stops at $t = 2\,\mathrm{s}$: $s_2 = 6(1) - \frac{1}{2}(6)(1)^2 = 3\,\mathrm{m}$.
4. In $2$ to $3\,\mathrm{s}$ it accelerates backward from rest: $s_3 = -\frac{1}{2}(6)(1)^2 = -3\,\mathrm{m}$.
5. Net displacement $= 3 + 3 - 3 = 3\,\mathrm{m}$; total distance $= 3 + 3 + 3 = 9\,\mathrm{m}$.
6. Average velocity $= \frac{3}{3} = 1\,\mathrm{m/s}$; average speed $= \frac{9}{3} = 3\,\mathrm{m/s}$, which is option $3$.

**Subtopic:** Average Velocity, Average Speed · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 10)

![printed question 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q037_34285aa0_03112026.png?v=34285aa0563c)

Publisher's solution, as printed:

![printed solution 37](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q037_0ab14714_03112026.png?v=0ab14714bb47)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Average velocity is net displacement over total time, average speed is path length over total time, and reversing the field makes the two differ
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The path length is handled correctly, giving $9/3 = 3\,\mathrm{m/s}$, and the average velocity is then taken as the mean of the two stages' averages, $3\,\mathrm{m/s}$ for the first second and $0$ for the next two, which is $1.5\,\mathrm{m/s}$ instead of the time-weighted $3/3 = 1\,\mathrm{m/s}$
- **Why:** This question requires computing two different averages over the same interval, demonstrated by 'the average velocity and the average speed of the toy car between 0 to 3 seconds are respectively'.
- **Note:** E1's pattern called this multi_part_respectively, which maps onto the live two_part: both printed values must hold together and half right scores nothing.
<!--/ecat-->

## Q38

Physics · Work, Energy and Power

A moving block having mass $m$, collides with another stationary block having mass $4m$. The lighter block comes to rest after collision. When the initial velocity of the lighter block is $v$, then the value of coefficient of restitution $(e)$ will be

- (1) $0.5$
- (2) $0.8$
- **(3)** $0.25$
- (4) $0.4$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. According to law of conservation of linear momentum,
2. $mv + 4m \times 0 = 4mv' + 0$
3. $v' = \frac{v}{4}$
4. $e = \frac{\text{Relative velocity of separation}}{\text{Relative velocity of approach}} = \frac{\frac{v}{4}}{v}$
5. $e = \frac{1}{4} = 0.25$

**Solved independently** (answer withheld)

1. Linear momentum is conserved: $m v + 4m(0) = m(0) + 4m\,v_2$.
2. Solve for the heavier block's final velocity: $v_2 = \frac{v}{4}$.
3. Coefficient of restitution: $e = \frac{v_2 - v_1'}{v - 0} = \frac{\frac{v}{4} - 0}{v}$.
4. $e = \frac{1}{4} = 0.25$, which is option $3$.

**Subtopic:** Problem on Coefficient of Restitution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q038_10fc295d_03112026.png?v=10fc295d1475)

Publisher's solution, as printed:

![printed solution 38](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q038_9cbeb84c_03112026.png?v=9cbeb84c377e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Momentum fixes the struck block's speed at $v/4$, and the coefficient of restitution is the separation speed over the approach speed
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Conserving kinetic energy instead of momentum gives $\frac12mv^2 = \frac12(4m)v_2^2$, so $v_2 = v/2$ and $e = 0.5$; momentum is what must be conserved in every collision, and it gives $v_2 = v/4$
- **Why:** This question requires computing the coefficient of restitution from the stated outcome, demonstrated by 'the lighter block comes to rest after collision. When the initial velocity of the lighter block is v'.
<!--/ecat-->

## Q39

Physics · Work, Energy and Power

A body initially at rest and sliding along a frictionless track from a height $h$ (as shown in the figure) just completes a vertical circle of diameter $AB = D$. The height $h$ is equal to

![printed figure: A body released from height h slides down a frictionless incline into a vertical loop with diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q039_ca9497df_03112026.svg?v=ca9497df8734)

*A body released from height h slides down a frictionless incline into a vertical loop with diameter AB*

![drawn: A body released from height h slides down a frictionless incline into a vertical loop with diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q039_question_ba20f740_03112026.svg?v=ba20f7408358)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $\frac{3}{2}D$
- (2) $\frac{7}{5}D$
- (3) $D$
- **(4)** $\frac{5}{4}D$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: A body slides from rest at height h down a straight frictionless incline to A and enters a vertical loop of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q039_sol_1_e37d87eb_03112026.svg?v=e37d87eb0dbe)

*A body slides from rest at height h down a straight frictionless incline to A and enters a vertical loop of diameter AB*

![drawn: A body slides from rest at height h down a straight frictionless incline to A and enters a vertical loop of diameter AB](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q039_solution_1_ffa0e683_03112026.svg?v=ffa0e6839390)  
*drawn on the booklet's geometry, checked against its figure spec*

1. As track is frictionless, so total mechanical energy will remain constant
2. $\mathrm{T.M.E_{I}} = \mathrm{T.M.E_{F}}$
3. $0 + mgh = \frac{1}{2}mv_{L}^{2} + 0$
4. $h = \frac{v_{L}^{2}}{2g}$
5. For completing the vertical circle, $v_{L} \geq \sqrt{5gR}$
6. $h = \frac{5gR}{2g} = \frac{5}{2}R = \frac{5}{4}D$

**Solved independently** (answer withheld)

1. The track is frictionless, so mechanical energy is conserved from the release point (height $h$ above A) to the bottom of the loop A: $v_A^2 = 2gh$.
2. The loop radius is $R = \frac{D}{2}$.
3. To just complete the vertical circle, the speed at the top B must satisfy $v_B^2 = gR$.
4. Energy conservation from A to B (rise of $2R$): $v_A^2 = v_B^2 + 4gR = 5gR$.
5. Equate: $2gh = 5gR \Rightarrow h = \frac{5}{2}R$.
6. Substitute $R = \frac{D}{2}$: $h = \frac{5}{2}\cdot\frac{D}{2} = \frac{5}{4}D$, which is option $4$.

**Subtopic:** Motion in a Vertical Circular Motion · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 11)

![printed question 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q039_a09c3d27_03112026.png?v=a09c3d27784c)

Publisher's solution, as printed:

![printed solution 39](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q039_f2459162_03112026.png?v=f24591624696)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** To just complete the loop the speed at the top must satisfy $v^2 = gR$, with $R$ the radius - here half the printed diameter
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  The condition is remembered as $v^2 = gD$ with the printed symbol put straight in, which gives $h = D + D/2 = 3D/2$; the stem prints the diameter $AB = D$, so the radius in the condition is $D/2$ and $h = D + D/4$
- **Why:** This question requires computing the release height from the loop condition, demonstrated by 'just completes a vertical circle of diameter AB = D. The height h is equal to'.
- **Note:** The figure is supplied as a drawn spec and places A at the bottom and B at the top of the loop with h measured from the loop's base, which is the geometry used here.
<!--/ecat-->

## Q40

Physics · Rotational Motion

Three objects, A : (a solid sphere), B : (a thin circular disk) and C : (a circular ring), each have the same mass $M$ and radius $R$. They all spin with the same angular speed $\omega$ about their own symmetry axes. The amounts of work ($W$) required to bring them to rest, would satisfy the relation

- **(1)** $W_C > W_B > W_A$
- (2) $W_B > W_A > W_C$
- (3) $W_A > W_B > W_C$
- (4) $W_A > W_C > W_B$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Work done required to bring them rest
2. $\Delta W = \Delta \mathrm{KE}$
3. $\Delta W = \frac{1}{2}I\omega^{2}$
4. $\Delta W \propto I$ for same $\omega$
5. $W_A : W_B : W_C = \frac{2}{5}MR^{2} : \frac{1}{2}MR^{2} : MR^{2}$
6. $= \frac{2}{5} : \frac{1}{2} : 1$
7. $= 4 : 5 : 10$
8. $\Rightarrow W_C > W_B > W_A$

**Solved independently** (answer withheld)

1. By the work-energy theorem, the work needed to stop each body equals its rotational kinetic energy, $W = \frac{1}{2} I \omega^2$.
2. Since $M$, $R$ and $\omega$ are the same for all three, $W \propto I$.
3. $I_A = \frac{2}{5} M R^2$ (solid sphere), $I_B = \frac{1}{2} M R^2$ (thin disk), $I_C = M R^2$ (ring).
4. $I_C > I_B > I_A$ since $1 > \frac{1}{2} > \frac{2}{5}$.
5. Hence $W_C > W_B > W_A$, which is option $1$.

**Subtopic:** Kinetic Energy of a Rigid Body Rotating About a Given Axis · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 11)

![printed question 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q040_f4f42ef1_03112026.png?v=f4f42ef196c8)

Publisher's solution, as printed:

![printed solution 40](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q040_5ab7d4bf_03112026.png?v=5ab7d4bf432b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** At equal mass, radius and angular speed the work needed to stop a body ranks with its moment of inertia: ring $MR^2$, disc $\frac12MR^2$, sphere $\frac25MR^2$
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Ranking by how solid the bodies look puts the solid sphere first and the thin ring last, which is the exact reverse of the table; what counts is how far the mass sits from the axis, and the ring keeps all of its mass at $R$
- **Why:** This question requires ranking three bodies by a stored moment-of-inertia table, demonstrated by 'the amounts of work (W) required to bring them to rest, would satisfy the relation'.
- **Note:** asks is order because the answer is a ranking of three named bodies; it is not relation, since nothing is changed and no factor is asked for. qtype stays mcq because each option is a single inequality chain rather than a set of independent parts.
<!--/ecat-->

## Q41

Physics · Laws of Motion

Which one of the following statements is incorrect?

- (1) Rolling friction is smaller than sliding friction.
- (2) Frictional force opposes the relative motion.
- (3) Limiting value of static friction is directly proportional to normal reaction.
- **(4)** Coefficient of sliding friction has dimensions of length.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Coefficient of sliding friction has no dimension.
2. $f = \mu_s N$
3. $\Rightarrow \mu_s = \frac{f}{N}$

**Solved independently** (answer withheld)

1. Rolling friction is smaller than sliding friction, so statement $1$ is correct.
2. Friction always opposes relative motion (or impending relative motion) between surfaces, so statement $2$ is correct.
3. $f_s^{\max} = \mu_s N$, so limiting static friction is directly proportional to $N$; statement $3$ is correct.
4. $\mu_k = \frac{f_k}{N} = \frac{[MLT^{-2}]}{[MLT^{-2}]} = [M^0L^0T^0]$, so the coefficient of sliding friction is dimensionless.
5. Statement $4$ (dimensions of length) is therefore incorrect, which is option $4$.

**Subtopic:** Kinetic Friction · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 12)

![printed question 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q041_90ae21b9_03112026.png?v=90ae21b96615)

Publisher's solution, as printed:

![printed solution 41](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q041_95591e71_03112026.png?v=95591e71b847)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The coefficient of friction is a ratio of two forces and so is dimensionless, while the other three friction statements are the chapter's own
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  The chapter's sentence is that friction opposes relative motion or the tendency of relative motion, and this option prints it without the qualifier, so a student hunting the incorrect statement reads the missing words as the flaw and marks a statement that is true as printed
- **Why:** This question requires grading four printed claims about friction against the chapter, demonstrated by 'which one of the following statements is incorrect?' with 'coefficient of sliding friction has dimensions of length' as the false one.
- **Note:** The task polarity is negated ('incorrect'), which is what makes the three true statements reachable; the trap is placed on option 2 because it is the one true statement whose printed wording drops a qualifier the chapter carries.
<!--/ecat-->

## Q42

Physics · Rotational Motion

A solid sphere is in rolling motion. In rolling motion a body possesses translational kinetic energy $(K_t)$ as well as rotational kinetic energy $(K_r)$ simultaneously. The ratio $K_t : (K_t + K_r)$ for the sphere is

- (1) $7 : 10$
- (2) $10 : 7$
- **(3)** $5 : 7$
- (4) $2 : 5$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $K_t = \frac{1}{2}mv^2$
2. $K_t + K_r = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2 = \frac{1}{2}mv^2 + \frac{1}{2}\left(\frac{2}{5}mr^2\right)\left(\frac{v}{r}\right)^2$
3. $= \frac{7}{10}mv^2$
4. So, $\boxed{\frac{K_t}{K_t + K_r} = \frac{5}{7}}$

**Solved independently** (answer withheld)

1. Translational kinetic energy: $K_t = \frac{1}{2} m v^2$.
2. For a solid sphere $I = \frac{2}{5} m r^2$, and rolling without slipping gives $\omega = \frac{v}{r}$.
3. $K_r = \frac{1}{2} I \omega^2 = \frac{1}{2}\left(\frac{2}{5} m r^2\right)\frac{v^2}{r^2} = \frac{1}{5} m v^2$.
4. $K_t + K_r = \frac{1}{2} m v^2 + \frac{1}{5} m v^2 = \frac{7}{10} m v^2$.
5. $\frac{K_t}{K_t + K_r} = \frac{1/2}{7/10} = \frac{5}{7}$, so the ratio is $5 : 7$, which is option $3$.

**Subtopic:** Rolling Motion · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 12)

![printed question 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q042_1189db39_03112026.png?v=1189db39b9ed)

Publisher's solution, as printed:

![printed solution 42](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q042_f9f51efd_03112026.png?v=f9f51efd45aa)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** A rolling solid sphere carries $K_t = \frac12mv^2$ and $K_r = \frac15mv^2$, so the translational share of the total is $5/7$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  $2:5$ is the true ratio of rotational to translational kinetic energy for a rolling solid sphere, and it is also the sphere's own moment-of-inertia coefficient; the stem asks for translational energy against the total, which is $\frac12 : \frac{7}{10} = 5:7$
- **Why:** This question requires computing one ratio among the rolling energies, demonstrated by 'the ratio $K_t : (K_t + K_r)$ for the sphere is'.
<!--/ecat-->

## Q43

Physics · Rotational Motion

A solid sphere is rotating freely about its symmetry axis in free space. The radius of the sphere is increased keeping its mass same. Which of the following physical quantities would remain constant for the sphere?

- (1) Angular velocity
- (2) Rotational kinetic energy
- (3) Moment of inertia
- **(4)** Angular momentum

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\tau_{ex} = 0$
2. So, $\frac{dL}{dt} = 0$
3. i.e. $L$ = constant
4. So angular momentum remains constant.

**Solved independently** (answer withheld)

1. In free space there is no external torque: $\tau_{ext} = 0$.
2. So angular momentum is conserved: $\frac{dL}{dt} = \tau_{ext} = 0 \Rightarrow L = I\omega = \text{constant}$.
3. For a solid sphere $I = \frac{2}{5}MR^2$, so increasing $R$ at fixed $M$ increases $I$ (option $3$ changes).
4. With $L$ fixed and $I$ larger, $\omega = \frac{L}{I}$ decreases (option $1$ changes).
5. $K = \frac{L^2}{2I}$ decreases as $I$ increases (option $2$ changes).
6. Only angular momentum stays constant, which is option $4$.

**Subtopic:** Conservation of Angular Momentum · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 12)

![printed question 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q043_a36684d6_03112026.png?v=a36684d6df46)

Publisher's solution, as printed:

![printed solution 43](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q043_3601ae6b_03112026.png?v=3601ae6bb7cb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** With no external torque the angular momentum $L=I\omega$ is the quantity that stays fixed, so spreading the same mass over a larger radius raises $I$ and lowers both $\omega$ and the rotational kinetic energy
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  "Rotating freely in free space" reads as nothing disturbing the spin, so a student holding the no-torque rule without $L=I\omega$ keeps the angular velocity fixed; the stem's "radius of the sphere is increased" raises $I$, and with $L$ fixed $\omega$ must fall
- **Why:** This question requires a conservation rule applied to a stated change of shape, demonstrated by "The radius of the sphere is increased keeping its mass same" set against four named quantities with no number to compute.
<!--/ecat-->

## Q44

Physics · Gravitation

If the mass of the Sun were ten times smaller and the universal gravitational constant were ten times larger in magnitude, which of the following is not correct?

- (1) Raindrops will fall faster
- (2) Time period of a simple pendulum on the Earth would decrease
- (3) Walking on the ground would become more difficult
- **(4)** ‘$g$’ on the Earth will not change

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. If Universal Gravitational constant becomes ten times, then $G' = 10\,G$
2. So, acceleration due to gravity increases.
3. i.e. (4) is wrong option.

**Solved independently** (answer withheld)

1. Acceleration due to gravity on the Earth is $g = \frac{G M_E}{R_E^2}$, which does not involve the Sun's mass $M_S$.
2. With $G' = 10G$, $g' = \frac{10 G M_E}{R_E^2} = 10g$, so $g$ increases; option $4$ ('$g$' will not change) is not correct.
3. Raindrops reach a terminal speed $v_t \propto g$, so with larger $g$ they fall faster; option $1$ is correct.
4. $T = 2\pi\sqrt{\frac{l}{g}}$ decreases when $g$ increases; option $2$ is correct.
5. Weight $mg$ becomes $10$ times larger, so walking becomes more difficult; option $3$ is correct.
6. The only incorrect statement is option $4$.

**Subtopic:** Gravitational Acceleration · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q044_783dfa32_03112026.png?v=783dfa32fbd6)

Publisher's solution, as printed:

![printed solution 44](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q044_dc8e4302_03112026.png?v=dc8e43027fb6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Surface gravity is $g=GM_E/R_E^{2}$, so it is set by the Earth's own mass and by $G$ — a tenfold $G$ makes $g$ tenfold, while the Sun's mass does not enter it at all
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  A student who has $T=2\pi\sqrt{l/g}$ but carries the direction of the $g$ dependence the wrong way judges a larger $g$ to slow the pendulum, and so marks "period would decrease" as the statement that is not correct
- **Why:** This question requires $g=GM_E/R_E^{2}$ applied to a hypothetical change in the constants, demonstrated by "the universal gravitational constant were ten times larger" with the option "'$g$' on the Earth will not change" as the claim to be graded.
- **Note:** The stem's change to the Sun's mass bears on none of the four options; only the change in $G$ decides the question.
<!--/ecat-->

## Q45

Physics · Gravitation

The kinetic energies of a planet in an elliptical orbit about the Sun, at positions A, B and C are $K_A$, $K_B$ and $K_C$, respectively. AC is the major axis and SB is perpendicular to AC at the position of the Sun S as shown in the figure. Then

![printed figure: Elliptical orbit with major axis AC and SB perpendicular to AC at the Sun S](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q045_55023b92_03112026.svg?v=55023b92b7fe)

*Elliptical orbit with major axis AC and SB perpendicular to AC at the Sun S*

![drawn: Elliptical orbit with major axis AC and SB perpendicular to AC at the Sun S](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q045_question_6bda221d_03112026.svg?v=6bda221d8bff)  
*drawn on the booklet's geometry, checked against its figure spec*

- (1) $K_A < K_B < K_C$
- (2) $K_B < K_A < K_C$
- **(3)** $K_A > K_B > K_C$
- (4) $K_B > K_A > K_C$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: Elliptical orbit with Sun S at a focus; perihelion A, aphelion C, SB perpendicular to major axis AC; velocity V_A down at A and V_C up at C](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q045_sol_1_7d38bf57_03112026.svg?v=7d38bf577c2d)

*Elliptical orbit with Sun S at a focus; perihelion A, aphelion C, SB perpendicular to major axis AC; velocity V_A down at A and V_C up at C*

![drawn: Elliptical orbit with Sun S at a focus; perihelion A, aphelion C, SB perpendicular to major axis AC; velocity V_A down at A and V_C up at C](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q045_solution_1_0d5365ab_03112026.svg?v=0d5365ab1c9c)  
*drawn on the booklet's geometry, checked against its figure spec*

1. Point A is perihelion and C is aphelion.
2. So, $V_A > V_B > V_C$
3. So, $K_A > K_B > K_C$

**Solved independently** (answer withheld)

1. From the figure the Sun $S$ is closer to $A$ than to $C$, so $A$ is perihelion and $C$ is aphelion: $r_A = a(1-e)$, $r_C = a(1+e)$.
2. $SB$ is perpendicular to the major axis at the focus, so $r_B$ is the semi-latus rectum: $r_B = a(1-e^2) = a(1-e)(1+e)$.
3. Since $0 < e < 1$: $a(1-e) < a(1-e)(1+e) < a(1+e)$, so $r_A < r_B < r_C$.
4. By energy conservation (vis-viva) $v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$, so speed and $K = \frac{1}{2}mv^2$ decrease as $r$ increases.
5. Hence $K_A > K_B > K_C$, which is option $3$.

**Subtopic:** Kepler's Law · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 12)

![printed question 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q045_bf331a43_03112026.png?v=bf331a437f9d)

Publisher's solution, as printed:

![printed solution 45](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q045_46fa8101_03112026.png?v=46fa8101b107)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** A planet speeds up as it comes nearer the Sun, and at the focus the perpendicular to the major axis meets the orbit at the semi-latus rectum, a distance that always exceeds the perihelion distance
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The perpendicular from a point is the shortest way to a line, and a student who carries that reflex over to the orbit reads B as the point nearest the Sun; A is then placed second and C last, which gets $K_A>K_C$ right and B wrong
- **Why:** This question requires the three positions ranked by distance from the Sun and then by speed, demonstrated by the options being orderings such as "$K_A > K_B > K_C$" and by the stem fixing B through "SB is perpendicular to AC at the position of the Sun S".
- **Note:** In the stored figure spec the dot marked S sits at x=135 while the drawn ellipse (centre x=230, rx=182, ry=70) has its focus at x=62, so the drawn SB stub measures shorter than the drawn SA. The figure is schematic rather than to scale; the stem's words and the key are consistent and nothing needs repair, but a measured reading of the drawing points at option 4 rather than at the key.
<!--/ecat-->

## Q46

Chemistry · physical · States of Matter

Given van der Waals constant for $\mathrm{NH_3}$, $\mathrm{H_2}$, $\mathrm{O_2}$ and $\mathrm{CO_2}$ are respectively $4.17$, $0.244$, $1.36$ and $3.59$, which one of the following gases is most easily liquefied?

- **(1)** $\mathrm{NH_3}$
- (2) $\mathrm{O_2}$
- (3) $\mathrm{H_2}$
- (4) $\mathrm{CO_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. van der waal constant ‘$a$’, signifies intermolecular forces of attraction.
2. Higher is the value of ‘$a$’, easier will be the liquefaction of gas.

**Solved independently** (answer withheld)

1. The constant $a$ measures intermolecular attractive forces, so a larger $a$ means the gas is easier to liquefy.
2. Compare the values: $a(\mathrm{NH_3}) = 4.17 > a(\mathrm{CO_2}) = 3.59 > a(\mathrm{O_2}) = 1.36 > a(\mathrm{H_2}) = 0.244$.
3. $\mathrm{NH_3}$ has the largest $a$, so it is most easily liquefied, which is option $1$.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q046_f8a053ea_03112026.png?v=f8a053ea8d05)

Publisher's solution, as printed:

![printed solution 46](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q046_1e8ba002_03112026.png?v=1e8ba002081a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The van der Waals constant $a$ measures the attraction between molecules, and the gas with the largest $a$ is the one liquefied most easily
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  $0.244$ is the smallest constant printed, and reading a small $a$ as 'closest to ideal, so easiest to squeeze into a liquid' runs the rule backwards — liquefaction needs strong attraction, i.e. a large $a$.
- **Why:** This question requires the rule 'larger $a$, stronger attraction, easier liquefaction' applied to supplied values, demonstrated by the stem printing '4.17, 0.244, 1.36 and 3.59' and asking which gas is most easily liquefied.
<!--/ecat-->

## Q47

Chemistry · physical · Ionic Equilibrium

Following solutions were prepared by mixing different volumes of $\mathrm{NaOH}$ and $\mathrm{HCl}$ of different concentrations : pH of which one of them will be equal to 1?

- **(a)** $60\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{HCl} + 40\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{NaOH}$
- **(b)** $55\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{HCl} + 45\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{NaOH}$
- **(c)** $75\,\mathrm{mL}\ \frac{\mathrm{M}}{5}\ \mathrm{HCl} + 25\,\mathrm{mL}\ \frac{\mathrm{M}}{5}\ \mathrm{NaOH}$
- **(d)** $100\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{HCl} + 100\,\mathrm{mL}\ \frac{\mathrm{M}}{10}\ \mathrm{NaOH}$

- (1) b
- (2) d
- (3) a
- **(4)** c

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Meq of $\mathrm{HCl} = 75 \times \frac{1}{5} \times 1 = 15$
2. Meq of $\mathrm{NaOH} = 25 \times \frac{1}{5} \times 1 = 5$
3. Meq of $\mathrm{HCl}$ in resulting solution $= 10$
4. Molarity of $[\mathrm{H^{+}}]$ in resulting mixture $= \frac{10}{100} = \frac{1}{10}$
5. $\mathrm{pH} = -\log[\mathrm{H^{+}}] = -\log\left[\frac{1}{10}\right] = 1.0$

**Solved independently** (answer withheld)

1. For (a): $n_{HCl} = 60 \times 0.1 = 6\,\mathrm{mmol}$, $n_{NaOH} = 40 \times 0.1 = 4\,\mathrm{mmol}$, excess $= 2\,\mathrm{mmol}$ in $100\,\mathrm{mL}$, so $[\mathrm{H^+}] = 0.02\,\mathrm{M}$ and $\mathrm{pH} \approx 1.7$.
2. For (b): excess $= 5.5 - 4.5 = 1\,\mathrm{mmol}$ in $100\,\mathrm{mL}$, so $[\mathrm{H^+}] = 0.01\,\mathrm{M}$ and $\mathrm{pH} = 2$.
3. For (c): $n_{HCl} = 75 \times 0.2 = 15\,\mathrm{mmol}$, $n_{NaOH} = 25 \times 0.2 = 5\,\mathrm{mmol}$, excess $= 10\,\mathrm{mmol}$ in $100\,\mathrm{mL}$.
4. $[\mathrm{H^+}] = \frac{10}{100} = 0.1\,\mathrm{M}$, so $\mathrm{pH} = -\log 0.1 = 1$.
5. For (d): $n_{HCl} = n_{NaOH} = 10\,\mathrm{mmol}$, complete neutralisation, $\mathrm{pH} = 7$.
6. Only (c) gives $\mathrm{pH} = 1$, which is option $4$.

**Subtopic:** pH Scale · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 13)

![printed question 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q047_9a20e6a1_03112026.png?v=9a20e6a1b649)

Publisher's solution, as printed:

![printed solution 47](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q047_df2ae6db_03112026.png?v=df2ae6db676e)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** In a strong acid-strong base mixture the pH comes from the surviving H+ spread over the combined volume, not from the stock concentration of the acid
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Mixture a leaves 2 mmol of HCl, and dividing that by the 20 mL by which the acid was in excess instead of by the 100 mL of mixture gives $0.1\,\mathrm{M}$ and pH 1, where the true figure is $0.02\,\mathrm{M}$ and pH 1.7
- **Why:** This question requires computing the surviving H+ concentration over the combined volume of each mixture, demonstrated by 'c. 75 mL M/5 HCl + 25 mL M/5 NaOH' leaving 10 mmol of acid in 100 mL, i.e. 0.1 M.
- **Note:** E1's pattern returned plain_mcq on the 16-default rule, but the printed shape is a lettered block a-d of four mixtures with the four options being those letters, so the shape recorded here is statements. The same single mechanism (dividing the surviving acid by the volume difference instead of the total volume) reaches both option 3 and option 1; it is written as the trap on option 3 and as a route on option 1.
<!--/ecat-->

## Q48

Chemistry · physical · Ionic Equilibrium

The solubility of $\mathrm{BaSO_4}$ in water is $2.42 \times 10^{-3}\,\mathrm{g\,L^{-1}}$ at $298\,\mathrm{K}$. The value of its solubility product $(K_{sp})$ will be (Given molar mass of $\mathrm{BaSO_4} = 233\,\mathrm{g\,mol^{-1}}$)

- **(1)** $1.08 \times 10^{-10}\,\mathrm{mol^{2}\,L^{-2}}$
- (2) $1.08 \times 10^{-14}\,\mathrm{mol^{2}\,L^{-2}}$
- (3) $1.08 \times 10^{-12}\,\mathrm{mol^{2}\,L^{-2}}$
- (4) $1.08 \times 10^{-8}\,\mathrm{mol^{2}\,L^{-2}}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Solubility of $\mathrm{BaSO_4}$, $s = \frac{2.42 \times 10^{-3}}{233}\,(\mathrm{mol\,L^{-1}})$
2. $= 1.04 \times 10^{-5}\,(\mathrm{mol\,L^{-1}})$
3. $\mathrm{BaSO_4(s)} \rightleftharpoons \underset{s}{\mathrm{Ba^{2+}(aq)}} + \underset{s}{\mathrm{SO_4^{2-}(aq)}}$
4. $K_{sp} = [\mathrm{Ba^{2+}}]\,[\mathrm{SO_4^{2-}}] = s^{2}$
5. $= (1.04 \times 10^{-5})^{2}$
6. $= 1.08 \times 10^{-10}\,\mathrm{mol^{2}\,L^{-2}}$

**Solved independently** (answer withheld)

1. Convert solubility to molar solubility: $s = \frac{2.42 \times 10^{-3}\,\mathrm{g\,L^{-1}}}{233\,\mathrm{g\,mol^{-1}}} = 1.0386 \times 10^{-5}\,\mathrm{mol\,L^{-1}}$.
2. Dissociation: $\mathrm{BaSO_4 \rightleftharpoons Ba^{2+} + SO_4^{2-}}$, so $[\mathrm{Ba^{2+}}] = [\mathrm{SO_4^{2-}}] = s$.
3. $K_{sp} = [\mathrm{Ba^{2+}}][\mathrm{SO_4^{2-}}] = s^2$.
4. $K_{sp} = (1.0386 \times 10^{-5})^2 = 1.0787 \times 10^{-10} \approx 1.08 \times 10^{-10}\,\mathrm{mol^{2}\,L^{-2}}$, which is option $1$.

**Subtopic:** Solubility Product Constant · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 13)

![printed question 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q048_213b454d_03112026.png?v=213b454dee57)

Publisher's solution, as printed:

![printed solution 48](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q048_8ae6864b_03112026.png?v=8ae6864b1554)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** For a 1:1 sparingly soluble salt $K_{sp}=s^2$ with $s$ in $\mathrm{mol\,L^{-1}}$, so the $\mathrm{g\,L^{-1}}$ solubility must be divided by the molar mass first
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  $2.42/233 = 0.0104$, and writing it as $0.00104$ loses one decimal place, so $s$ becomes $1.04\times10^{-6}$ instead of $1.04\times10^{-5}$ and $s^2$ comes out as $1.08\times10^{-12}$.
- **Why:** This question requires a $\mathrm{g\,L^{-1}}$ solubility converted to $\mathrm{mol\,L^{-1}}$ and squared, demonstrated by the stem supplying '2.42 × 10⁻³ g L⁻¹' together with 'molar mass of BaSO₄ = 233 g mol⁻¹'.
- **Note:** The stem reproduces the source's own solved problem with its value unaltered, and the key equals the answer the source prints, so no number has been changed and old_ncert_answer cannot apply here.
<!--/ecat-->

## Q49

Chemistry · physical · Surface Chemistry

On which of the following properties does the coagulating power of an ion depend?

- (1) The magnitude of the charge on the ion alone
- **(2)** Both magnitude and sign of the charge on the ion
- (3) Size of the ion alone
- (4) The sign of charge on the ion alone

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Coagulation of colloidal solution by using an electrolyte depends on the charge present (positive or negative) on colloidal particles as well as on its size.
2. Coagulating power of an electrolyte depends on the magnitude of charge present on effective ion of electrolyte.

**Solved independently** (answer withheld)

1. By the Hardy-Schulze rule, the ion that causes coagulation is the one whose charge is opposite in sign to that of the colloidal particles, so the sign of the charge matters.
2. Its coagulating power increases with the magnitude of that charge, e.g. for a negative sol $\mathrm{Al^{3+}} > \mathrm{Ba^{2+}} > \mathrm{Na^{+}}$, so the magnitude matters too; hence both, which is option $2$.

**Subtopic:** Coagulation of Colloids and Hardy-Schulze Rule · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 13)

![printed question 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q049_f1ab37dd_03112026.png?v=f1ab37dd2ddd)

Publisher's solution, as printed:

![printed solution 49](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q049_149b7fdd_03112026.png?v=149b7fdd451e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Hardy–Schulze rule has two clauses: the coagulating ion must carry charge opposite to the sol particles, and its power rises with the magnitude of that charge
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  'Greater the valence, greater the coagulating power' is the half of the rule that gets quoted, and this option is exactly that half with 'alone' attached; the other half is that the ion's charge must be opposite in sign to the sol's.
- **Why:** This question requires both clauses of the stated Hardy–Schulze rule, demonstrated by three options ending in 'alone' against one reading 'Both magnitude and sign of the charge on the ion'.
<!--/ecat-->

## Q50

Chemistry · inorganic · General Principles and Processes of Isolation of Elements

Considering Ellingham diagram, which of the following metals can be used to reduce alumina?

- (1) $\mathrm{Fe}$
- **(2)** $\mathrm{Mg}$
- (3) $\mathrm{Zn}$
- (4) $\mathrm{Cu}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The metal which is more reactive than '$\mathrm{Al}$' can reduce alumina i.e. '$\mathrm{Mg}$' should be the correct option.

**Solved independently** (answer withheld)

1. A metal $M$ can reduce $\mathrm{Al_2O_3}$ only if its oxide line lies below the $\mathrm{Al_2O_3}$ line on the Ellingham diagram, i.e. $\Delta_f G^\circ(M_xO) < \Delta_f G^\circ(\mathrm{Al_2O_3})$ per mole of $\mathrm{O_2}$.
2. The $\mathrm{FeO}$, $\mathrm{ZnO}$ and $\mathrm{Cu_2O}$ lines all lie above the $\mathrm{Al_2O_3}$ line, so $\mathrm{Fe}$, $\mathrm{Zn}$ and $\mathrm{Cu}$ cannot reduce alumina.
3. The $\mathrm{MgO}$ line lies below the $\mathrm{Al_2O_3}$ line (below about $1623\,\mathrm{K}$), so for $3\mathrm{Mg} + \mathrm{Al_2O_3} \rightarrow 3\mathrm{MgO} + 2\mathrm{Al}$, $\Delta_r G^\circ < 0$.
4. Hence $\mathrm{Mg}$ can reduce alumina, which is option $2$.

**Subtopic:** Thermodynamic Principles of Metallurgy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 13)

![printed question 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q050_6aef60bd_03112026.png?v=6aef60bde9b4)

Publisher's solution, as printed:

![printed solution 50](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q050_8dc83488_03112026.png?v=8dc83488fa1b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** On an Ellingham diagram a metal can reduce another's oxide only where its own oxide line lies lower, and magnesium's line lies below aluminium's up to about 1623 K
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The printed Al/Fe couple runs the other way — in the thermite reaction aluminium reduces $\mathrm{Fe_2O_3}$ — so recalling the pair without its direction offers iron as the reducer of alumina.
- **Why:** This question requires the Ellingham criterion applied to four candidate metals, demonstrated by the stem's 'Considering Ellingham diagram, which of the following metals can be used to reduce alumina'.
<!--/ecat-->

## Q51

Chemistry · inorganic · The p–Block Elements

The correct order of atomic radii in group 13 elements is

- (1) $\mathrm{B} < \mathrm{Al} < \mathrm{In} < \mathrm{Ga} < \mathrm{Tl}$
- (2) $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{Tl} < \mathrm{In}$
- (3) $\mathrm{B} < \mathrm{Al} < \mathrm{Ga} < \mathrm{In} < \mathrm{Tl}$
- **(4)** $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{Tl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. | Elements | $\mathrm{B}$ | $\mathrm{Ga}$ | $\mathrm{Al}$ | $\mathrm{In}$ | $\mathrm{Tl}$ |
|---|---|---|---|---|---|
| Atomic radii (pm) | $85$ | $135$ | $143$ | $167$ | $170$ |

**Solved independently** (answer withheld)

1. Down group 13, atomic radius generally increases as new shells are added, so $\mathrm{B}$ is smallest and $\mathrm{In}$, $\mathrm{Tl}$ are largest.
2. $\mathrm{Ga}$ follows the ten $3d$ electrons, which shield poorly, so its effective nuclear charge rises and $r_{\mathrm{Ga}} \approx 135\,\mathrm{pm} < r_{\mathrm{Al}} \approx 143\,\mathrm{pm}$.
3. With $r_{\mathrm{In}} \approx 167\,\mathrm{pm} < r_{\mathrm{Tl}} \approx 170\,\mathrm{pm}$, the order is $\mathrm{B} < \mathrm{Ga} < \mathrm{Al} < \mathrm{In} < \mathrm{Tl}$, which is option $4$.

**Subtopic:** General properties & Trends of Group 13 (Boron Family) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 14)

![printed question 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q051_cce2402e_03112026.png?v=cce2402efb40)

Publisher's solution, as printed:

![printed solution 51](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q051_a2be5436_03112026.png?v=a2be54362907)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Atomic radius in group 13 does not rise steadily: Ga is smaller than Al because the ten intervening 3d electrons shield the nuclear charge poorly
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  'Radius increases down a group' run straight through group 13 gives $\mathrm{B<Al<Ga<In<Tl}$; the rule's condition fails between Al and Ga, where a whole d series has been inserted and shields badly, so Ga comes out the smaller.
- **Why:** This question requires the group-13 radius trend together with its gallium anomaly, demonstrated by two options printing Al before Ga and two printing Ga before Al.
- **Note:** The retired per-option axis would have called this ignores_exception; its live family is condition_missed — the down-group rule applied where its condition, no inserted d series, does not hold. formula_misused was ruled out because the rule is not misremembered, only used outside its range.
<!--/ecat-->

## Q52

Chemistry · inorganic · Chemical Bonding and Molecular Structure

In the structure of $\mathrm{ClF_3}$, the number of lone pairs of electrons on central atom ‘$\mathrm{Cl}$’ is

- (1) One
- (2) Four
- **(3)** Two
- (4) Three

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. The structure of $\mathrm{ClF_3}$ is

![printed figure: chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F atoms (one up, one left, one down), with two lone pairs drawn on Cl to the right and three lone pairs drawn on each F](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q052_sol_1_cb0f0227_03112026.svg?v=cb0f02277d38)

*chlorine trifluoride ($\ce{ClF3}$): Cl bonded to three F atoms (one up, one left, one down), with two lone pairs drawn on Cl to the right and three lone pairs drawn on each F*

2. The number of lone pair of electrons on central $\mathrm{Cl}$ is $2$.

**Solved independently** (answer withheld)

1. Chlorine (group 17) has $7$ valence electrons.
2. Three of these form three $\mathrm{Cl{-}F}$ single bonds, using $3$ electrons from $\mathrm{Cl}$.
3. Non-bonding electrons on $\mathrm{Cl}$: $7 - 3 = 4$, i.e. $\frac{4}{2} = 2$ lone pairs.
4. So $\mathrm{ClF_3}$ has $3$ bond pairs $+ 2$ lone pairs ($sp^3d$, T-shaped), and the answer is Two, option $3$.

**Subtopic:** Valence Shell Electron Pair Repulsion (VSEPR) Theory · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q052_259fa3db_03112026.png?v=259fa3db7892)

Publisher's solution, as printed:

![printed solution 52](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q052_ae6b10c1_03112026.png?v=ae6b10c186e8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Lone pairs on a central atom are what is left of its valence electrons after bonding: chlorine's seven less the three spent on Cl–F bonds leaves four electrons, i.e. two lone pairs
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 2  
  Seven valence electrons on Cl less the three spent on bonds leaves four electrons, and stopping there — without pairing them up — prints 'Four'.
- **Why:** This question requires the valence-electron count applied to an expanded-octet central atom, demonstrated by the stem asking for 'the number of lone pairs of electrons on central atom ‘Cl’' in $\mathrm{ClF_3}$.
<!--/ecat-->

## Q53

Chemistry · physical · Redox Reactions

The correct order of N-compounds in its decreasing order of oxidation states is

- **(1)** $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{N_2}$, $\mathrm{NH_4Cl}$
- (2) $\mathrm{HNO_3}$, $\mathrm{NH_4Cl}$, $\mathrm{NO}$, $\mathrm{N_2}$
- (3) $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{NH_4Cl}$, $\mathrm{N_2}$
- (4) $\mathrm{NH_4Cl}$, $\mathrm{N_2}$, $\mathrm{NO}$, $\mathrm{HNO_3}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{H\overset{+5}{N}O_3}$, $\mathrm{\overset{+2}{N}O}$, $\mathrm{\overset{0}{N}_2}$, $\mathrm{\overset{-3}{N}H_4Cl}$
2. Hence, the correct option is (1).

**Solved independently** (answer withheld)

1. In $\mathrm{HNO_3}$: $(+1) + x + 3(-2) = 0 \Rightarrow x = +5$.
2. In $\mathrm{NO}$: $x + (-2) = 0 \Rightarrow x = +2$.
3. In $\mathrm{N_2}$ (element): $x = 0$.
4. In $\mathrm{NH_4Cl}$ ($\mathrm{NH_4^+}$): $x + 4(+1) = +1 \Rightarrow x = -3$.
5. Decreasing order $+5 > +2 > 0 > -3$ gives $\mathrm{HNO_3}, \mathrm{NO}, \mathrm{N_2}, \mathrm{NH_4Cl}$, which is option $1$.

**Subtopic:** Oxidation Number · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 14)

![printed question 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q053_0e3cb334_03112026.png?v=0e3cb334f796)

Publisher's solution, as printed:

![printed solution 53](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q053_a2d139d1_03112026.png?v=a2d139d1c7bd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Nitrogen's oxidation number is $+5$ in $\mathrm{HNO_3}$, $+2$ in $\mathrm{NO}$, $0$ in $\mathrm{N_2}$ and $-3$ in $\mathrm{NH_4Cl}$, and the ranking goes by the signed value
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  $\mathrm{NH_4Cl}$, $\mathrm{N_2}$, $\mathrm{NO}$, $\mathrm{HNO_3}$ is the same series read the other way — the increasing order, which is how the four values come out when they are listed from the most reduced upwards; the stem asks for decreasing.
- **Why:** This question requires four nitrogen oxidation numbers ranked with their signs, demonstrated by the stem's 'decreasing order of oxidation states' over $\mathrm{HNO_3}$, $\mathrm{NO}$, $\mathrm{N_2}$ and $\mathrm{NH_4Cl}$.
<!--/ecat-->

## Q54

Chemistry · inorganic · The p–Block Elements

> ⚠ The independent solve chose (1); the booklet prints (2).

Which of the following statements is not true for halogens?

- (1) All form monobasic oxyacids
- **(2)** All but fluorine show positive oxidation states
- (3) All are oxidizing agents
- (4) Chlorine has the highest electron-gain enthalpy

**Answer** — booklet: (2) · independent solve: (1) · differs

**Publisher's solution**

1. Due to high electronegativity and small size, $\mathrm{F}$ forms only one oxoacid, $\mathrm{HOF}$ known as Fluoric (I) acid.
2. Oxidation number of $\mathrm{F}$ is $+1$ in $\mathrm{HOF}$.

**Solved independently** (answer withheld)

1. Fluorine, the most electronegative element, shows only the $-1$ state, while $\mathrm{Cl}$, $\mathrm{Br}$ and $\mathrm{I}$ show $+1, +3, +5, +7$; so option $2$ is true.
2. All halogens accept electrons readily ($\mathrm{X_2} + 2e^- \rightarrow 2\mathrm{X^-}$), so all are oxidising agents; option $3$ is true.
3. Electron gain enthalpy is most negative for $\mathrm{Cl}$ (more negative than $\mathrm{F}$ because of the small, crowded $2p$ shell of $\mathrm{F}$); option $4$ is true.
4. The common oxyacids $\mathrm{HOX}$, $\mathrm{HXO_2}$, $\mathrm{HXO_3}$, $\mathrm{HXO_4}$ have one ionisable $\mathrm{H}$, but iodine also forms $\mathrm{H_5IO_6}$, which is polybasic.
5. So option $1$ is the only statement with a counterexample, and it is chosen as the statement that is not true.

**Subtopic:** General Properties & Trends of Group 17 (Halogens) · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 14)

![printed question 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q054_6b200f65_03112026.png?v=6b200f653772)

Publisher's solution, as printed:

![printed solution 54](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q054_8bcc882b_03112026.png?v=8bcc882b8ecf)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Chlorine, not fluorine, has the most negative electron gain enthalpy, because fluorine's compact 2p subshell crowds the incoming electron
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  Electron gain enthalpy becomes less negative down group 17, and running that trend up to the top makes fluorine the highest, so a sentence crediting chlorine reads as the planted error; fluorine is the break the trend does not cover.
- **Why:** This question requires each printed claim about group 17 checked against the stated properties, demonstrated by the stem's 'which of the following statements is not true for halogens'.
- **Note:** Tagged as printed, key not re-judged. Option 2 reads as the source's own sentence — all the halogens except fluorine show $+1$, $+3$, $+5$ and $+7$ — so on that wording it is true and the printed key is open to question; a reviewer should settle it against the printed paper. The three options tagged above are the ones the printed key leaves wrong.
<!--/ecat-->

## Q55

Chemistry · inorganic · The p–Block Elements

Which one of the following elements is unable to form $\mathrm{MF_6^{3-}}$ ion?

- (1) $\mathrm{Ga}$
- **(2)** $\mathrm{B}$
- (3) $\mathrm{Al}$
- (4) $\mathrm{In}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\because$ 'B' has no vacant $d$-orbitals in its valence shell, so it can't extend its covalency beyond $4$.
2. i.e. 'B' cannot form the ion like $\mathrm{MF_6^{3(-)}}$ i.e. $\mathrm{BF_6^{3(-)}}$.
3. Hence, the correct option is (2).

**Solved independently** (answer withheld)

1. Forming $\mathrm{MF_6^{3-}}$ needs the central atom to accept six ligands, i.e. a covalency of $6$.
2. Boron has only the $2s$ and $2p$ orbitals in its valence shell (no $d$ orbitals), so its maximum covalency is $4$, as in $\mathrm{BF_4^-}$.
3. $\mathrm{Al}$, $\mathrm{Ga}$ and $\mathrm{In}$ have vacant $d$ orbitals available, so they can expand to covalency $6$ and form $\mathrm{MF_6^{3-}}$.
4. So $\mathrm{B}$ cannot form $\mathrm{MF_6^{3-}}$, which is option $2$.

**Subtopic:** Anomalous behaviour of Boron & Diagonal Relationship (B–Si) · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 14)

![printed question 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q055_42a3af75_03112026.png?v=42a3af7559ca)

Publisher's solution, as printed:

![printed solution 55](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q055_f2791933_03112026.png?v=f279193380ca)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Boron has no d orbitals, so its maximum covalence is four and it stops at $\mathrm{[BF_4]^-}$, while aluminium and the heavier members form octahedral $\mathrm{[MF_6]^{3-}}$
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  $\mathrm{[AlF_6]^{3-}}$ is the printed example of this very ion — it is the anion of cryolite, $\mathrm{Na_3AlF_6}$ — so aluminium is the name the formula calls up, and it answers 'which element forms it' rather than the stem's 'is unable to form' it.
- **Why:** This question requires the stated covalence limit of boron, demonstrated by the stem asking which element 'is unable to form $\mathrm{MF_6^{3-}}$ ion' among B, Al, Ga and In.
<!--/ecat-->

## Q56

Chemistry · organic · Polymers

Regarding cross-linked or network polymers, which of the following statements is incorrect?

- (1) They contain covalent bonds between various linear polymer chains.
- (2) Examples are bakelite and melamine.
- (3) They are formed from bi- and tri-functional monomers.
- **(4)** They contain strong covalent bonds in their polymer chains.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Cross linked or network polymers are formed from bi-functional and tri-functional monomers and contain strong covalent bonds between various linear polymer chains, e.g. bakelite, melamine etc.
2. Option (4) is not related to cross-linking.
3. So option (4) should be the correct option.

**Solved independently** (answer withheld)

1. Cross-linked (network) polymers are formed from $\text{bi-}$ and $\text{tri-functional}$ monomers, so option $3$ is correct.
2. Their characteristic feature is strong covalent bonds $\textit{between}$ the various linear polymer chains (cross-links), so option $1$ is correct.
3. Bakelite and melamine are standard examples of network polymers, so option $2$ is correct.
4. Option $4$ places the strong covalent bonds $\textit{in}$ the polymer chains rather than between them, which does not describe the defining feature of network polymers, so it is the incorrect statement: option $4$.

**Subtopic:** Classification of Polymers Based on Structure · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 14)

![printed question 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q056_51c366c4_03112026.png?v=51c366c4864f)

Publisher's solution, as printed:

![printed solution 56](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q056_1df1b853_03112026.png?v=1df1b8538a28)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** What defines a cross-linked polymer is covalent bonding BETWEEN the linear chains; covalent bonds running along a chain are present in every polymer and distinguish nothing
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Two options print nearly the same sentence — covalent bonds 'between various linear polymer chains' against 'in their polymer chains' — so a student who holds the sense of the line but not its preposition has to choose between twins, and one who pictures chains as held together by intermolecular forces rejects the first.
- **Why:** This question requires the clause that distinguishes cross-linked polymers, demonstrated by option 1 reading 'covalent bonds between various linear polymer chains' against option 4's 'strong covalent bonds in their polymer chains'.
- **Note:** look_alike_term against nearby_fact: replace the two phrasings with unlike sentences and the pull dies, so it is the resemblance between them that does the work. The retired per-option axis would have called the device single_word_substitution, which has no separate live family. Key tagged as printed: covalent bonds do run along the chains of a cross-linked polymer too, so option 4 is false only as a statement of what makes the class distinctive, and the key rests on the source's preposition.
<!--/ecat-->

## Q57

Chemistry · organic · Amines

Nitration of aniline in strong acidic medium also gives m-nitroaniline because

- (1) Inspite of substituents nitro group always goes to only m-position.
- (2) In absence of substituents nitro group always goes to m-position.
- (3) In electrophilic substitution reactions amino group is meta directive.
- **(4)** In acidic (strong) medium aniline is present as anilinium ion.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: aniline ⇌(H⁺) benzenaminium (Anilinium ion)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q057_sol_1_28628147_03112026.svg?v=2862814730a9)

*aniline ⇌[H⁺] benzenaminium (Anilinium ion)*

![drawn: aniline ⇌(H⁺) benzenaminium (Anilinium ion)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q057_solution_1_9c39220b_03112026.svg?v=9c39220b7395)  
*drawn on the booklet's geometry, checked against its SMILES*

1. $-\overset{\oplus}{\mathrm{N}}\mathrm{H_3}$ is m-directing, hence besides para ($51\%$) and ortho ($2\%$), meta product ($47\%$) is also formed in significant yield.

**Solved independently** (answer withheld)

1. In strong acid the basic $-\mathrm{NH_2}$ group is protonated: $\mathrm{C_6H_5NH_2} + \mathrm{H^+} \rightarrow \mathrm{C_6H_5NH_3^+}$ (anilinium ion).
2. The $-\mathrm{NH_3^+}$ group is electron-withdrawing and meta-directing, so nitration of the anilinium ion gives $m$-nitroaniline alongside the $o$/$p$ products; this matches option $4$, while options $1$, $2$ and $3$ are false general claims (free $-\mathrm{NH_2}$ is $o$/$p$-directing).

**Subtopic:** Chemical Reactions of Amines (Carbylamine, Nitrous Acid, Arylsulphonyl Chloride and Electrophilic Substitution Reactions) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q057_1e71df24_03112026.png?v=1e71df24691f)

Publisher's solution, as printed:

![printed solution 57](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q057_ff3221c2_03112026.png?v=ff3221c2faeb)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** In strongly acidic medium aniline is protonated to the anilinium ion, whose $\mathrm{-NH_3^+}$ group is meta-directing, so part of the nitration product is m-nitroaniline
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Reading the directing effect back off the product — meta product, therefore meta director — credits the $\mathrm{-NH_2}$ group itself with meta direction and drops the stem's 'in strong acidic medium', which is the clause that turns $\mathrm{-NH_2}$ into $\mathrm{-NH_3^+}$.
- **Why:** This question requires the reason the stated medium changes the directing group, demonstrated by the stem's 'Nitration of aniline in strong acidic medium also gives m-nitroaniline because'.
<!--/ecat-->

## Q58

Chemistry · inorganic · The s-Block Elements

Which of the following oxides is most acidic in nature?

- (1) $\mathrm{MgO}$
- (2) $\mathrm{BaO}$
- **(3)** $\mathrm{BeO}$
- (4) $\mathrm{CaO}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{BeO} < \mathrm{MgO} < \mathrm{CaO} < \mathrm{BaO}$
2. $\longrightarrow$ Basic character increases.
3. So, the most acidic should be $\mathrm{BeO}$.
4. In fact, $\mathrm{BeO}$ is amphoteric oxide while other given oxides are basic.

**Solved independently** (answer withheld)

1. All four are group 2 oxides; basic character of these oxides increases down the group as metallic character and ionic size increase.
2. $\mathrm{Be^{2+}}$ is very small and highly polarising, so $\mathrm{BeO}$ is largely covalent and amphoteric, while $\mathrm{MgO}$, $\mathrm{CaO}$ and $\mathrm{BaO}$ are basic.
3. Order of basicity: $\mathrm{BeO} < \mathrm{MgO} < \mathrm{CaO} < \mathrm{BaO}$, so the most acidic is $\mathrm{BeO}$, which is option $3$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 15)

![printed question 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q058_27e017a0_03112026.png?v=27e017a090b8)

Publisher's solution, as printed:

![printed solution 58](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q058_292b53e0_03112026.png?v=292b53e0e782)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Down group 2 the oxides become more basic as the metal becomes more electropositive; BeO alone is amphoteric, which makes it the most acidic oxide of the group
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Filing BeO under 'amphoteric' as a category of its own takes it out of the running and leaves the next member up the group, MgO; amphoteric already includes acidic behaviour, since BeO dissolves in alkali to give beryllate, while MgO reacts with acids only.
- **Why:** This question requires four alkaline-earth oxides told apart on acidic character, demonstrated by the stem's 'most acidic in nature' over MgO, BaO, BeO and CaO with no data printed.
- **Note:** nearby_fact against look_alike_term: swap MgO for an unlike name and the pull survives, because what carries the student is the oxide printed beside BeO in the group-2 row, not any likeness between the two names.
<!--/ecat-->

## Q59

Chemistry · organic · Biomolecules

The difference between amylose and amylopectin is

- **(1)** Amylopectin have $1 \rightarrow 4$ $\alpha$-linkage and $1 \rightarrow 6$ $\alpha$-linkage
- (2) Amylopectin have $1 \rightarrow 4$ $\alpha$-linkage and $1 \rightarrow 6$ $\beta$-linkage
- (3) Amylose have $1 \rightarrow 4$ $\alpha$-linkage and $1 \rightarrow 6$ $\beta$-linkage
- (4) Amylose is made up of glucose and galactose

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Amylose and Amylopectin are polymers of $\alpha$-D-glucose, so $\beta$-link is not possible.
2. Amylose is linear with $1 \rightarrow 4$ $\alpha$-linkage whereas Amylopectin is branched and has both $1 \rightarrow 4$ and $1 \rightarrow 6$ $\alpha$-linkages.
3. So option (1) should be the correct option.

**Solved independently** (answer withheld)

1. Amylose is a linear polymer of $\alpha$-D-glucose joined only by $C_1 \rightarrow C_4$ $\alpha$-glycosidic linkages, so option $3$ (a $1 \rightarrow 6$ $\beta$-linkage in amylose) and option $4$ (galactose in amylose) are wrong.
2. Amylopectin is a branched polymer of $\alpha$-D-glucose: the chain uses $C_1 \rightarrow C_4$ $\alpha$-linkages and the branches use $C_1 \rightarrow C_6$ $\alpha$-linkages, not $\beta$, so option $2$ is wrong.
3. Amylopectin having $1 \rightarrow 4$ $\alpha$ and $1 \rightarrow 6$ $\alpha$ linkages is option $1$.

**Subtopic:** Polysaccharides · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 15)

![printed question 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q059_075ba7d5_03112026.png?v=075ba7d5ba4f)

Publisher's solution, as printed:

![printed solution 59](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q059_13dddf11_03112026.png?v=13dddf1125d3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Starch is two polymers: amylose is a linear chain of alpha-1,4 linked glucose, amylopectin adds alpha-1,6 branch points
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The branch point is carried in memory as 'a second kind of linkage' with no letter attached, and beta is the letter that belongs to the other famous glucose polymer in the same section, cellulose, so the 1 to 6 link gets written beta.
- **Why:** This question requires the stated linkage pattern of the two starch fractions, demonstrated by option 1 reading '1 to 4 alpha-linkage and 1 to 6 alpha-linkage'.
- **Note:** E1_question_type is null and its why-text reads 'options are reactions'; the printed options are claims about glycosidic linkages, not reactions, so the shape recorded here is the plain mcq that is on the page.
<!--/ecat-->

## Q60

Chemistry · physical · Basic Concepts of Chemistry

A mixture of $2.3\,\mathrm{g}$ formic acid and $4.5\,\mathrm{g}$ oxalic acid is treated with conc. $\mathrm{H_2SO_4}$. The evolved gaseous mixture is passed through $\mathrm{KOH}$ pellets. Weight (in g) of the remaining product at STP will be

- (1) $1.4$
- **(2)** $2.8$
- (3) $3.0$
- (4) $4.4$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $\underset{2.3\,\mathrm{g}\text{ or }\left(\frac{1}{20}\,\mathrm{mol}\right)}{\mathrm{HCOOH}} \xrightarrow{\mathrm{Conc.H_2SO_4}} \underset{\frac{1}{20}\,\mathrm{mol}}{\mathrm{CO(g)}} + \mathrm{H_2O(l)}$
2. $\underset{4.5\,\mathrm{g}\text{ or }\left(\frac{1}{20}\,\mathrm{mol}\right)}{\begin{array}{c}\mathrm{COOH}\\ | \\ \mathrm{COOH}\end{array}} \xrightarrow{\mathrm{Conc.H_2SO_4}} \underset{\frac{1}{20}\,\mathrm{mol}}{\mathrm{CO(g)}} + \underset{\frac{1}{20}\,\mathrm{mol}}{\mathrm{CO_2(g)}} + \mathrm{H_2O(l)}$
3. Gaseous mixture formed is $\mathrm{CO}$ and $\mathrm{CO_2}$ when it is passed through $\mathrm{KOH}$, only $\mathrm{CO_2}$ is absorbed.
4. So the remaining gas is $\mathrm{CO}$.
5. So, weight of remaining gaseous product $\mathrm{CO}$ is
6. $\frac{2}{20} \times 28 = 2.8\,\mathrm{g}$
7. So, the correct option is (2)

**Solved independently** (answer withheld)

1. $n(\mathrm{HCOOH}) = \frac{2.3}{46} = 0.05\,\mathrm{mol}$.
2. $\mathrm{HCOOH} \xrightarrow{\text{conc. } \mathrm{H_2SO_4}} \mathrm{CO} + \mathrm{H_2O}$, giving $0.05\,\mathrm{mol}$ CO.
3. $n(\mathrm{H_2C_2O_4}) = \frac{4.5}{90} = 0.05\,\mathrm{mol}$.
4. $\mathrm{H_2C_2O_4} \xrightarrow{\text{conc. } \mathrm{H_2SO_4}} \mathrm{CO} + \mathrm{CO_2} + \mathrm{H_2O}$, giving $0.05\,\mathrm{mol}$ CO and $0.05\,\mathrm{mol}$ $\mathrm{CO_2}$.
5. KOH pellets absorb the acidic $\mathrm{CO_2}$ (and water), so only CO remains: $0.05 + 0.05 = 0.10\,\mathrm{mol}$.
6. $m(\mathrm{CO}) = 0.10 \times 28 = 2.8\,\mathrm{g}$, which is option $2$.

**Subtopic:** Stoichiometry · **Difficulty:** hard (5 steps)

**Printed in the booklet** (page 15)

![printed question 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q060_1dd3e2ed_03112026.png?v=1dd3e2edf5e6)

Publisher's solution, as printed:

![printed solution 60](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q060_822f61c8_03112026.png?v=822f61c8f662)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Conc. sulphuric acid dehydrates formic acid to CO and oxalic acid to CO plus CO2; KOH removes only the acidic CO2, so the mass left is the total CO
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  Formic acid is taken as the only CO source and oxalic acid as the only CO2 source, so the sum stops at $0.05 \times 28 = 1.4$ g instead of $0.1 \times 28 = 2.8$ g.
- **Why:** This question requires a number computed from the stem's masses, demonstrated by 'A mixture of 2.3 g formic acid and 4.5 g oxalic acid' with the answer asked as 'Weight (in g) of the remaining product'.
- **Note:** The stem says 'at STP' although the answer asked for is a mass, so the phrase does no work in the calculation.
<!--/ecat-->

## Q61

Chemistry · organic · Alcohols, Phenols and Ethers

In the reaction
The electrophile involved is

![printed figure: phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q061_949db914_03112026.svg?v=949db914ee44)

*phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate*

![drawn: phenol + $\ce{CHCl3}$ + $\ce{NaOH}$ → sodium 2-formylphenolate](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q061_question_c3da6971_03112026.svg?v=c3da6971577b)  
*drawn on the booklet's geometry, checked against its SMILES*

Structures: phenol `Oc1ccccc1` ![phenol](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q061_question_s1_39283864_03112026.svg?v=392838643b6d); trichloromethane `ClC(Cl)Cl` ![trichloromethane](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q061_question_s2_36c42d8f_03112026.svg?v=36c42d8f41aa); sodium hydroxide `[Na+].[OH-]` ![sodium hydroxide](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q061_question_s3_95b7ee63_03112026.svg?v=95b7ee636c6c); sodium 2-formylphenolate `O=Cc1ccccc1[O-].[Na+]` ![sodium 2-formylphenolate](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q061_question_s4_b7cf7659_03112026.svg?v=b7cf76593c4f)

- (1) Dichloromethyl cation $\left(\overset{\oplus}{\mathrm{C}}\mathrm{HCl_2}\right)$
- (2) Dichloromethyl anion $\left(\overset{\oplus}{\mathrm{C}}\mathrm{HCl_2}\right)$
- (3) Formyl cation $\left(\overset{\oplus}{\mathrm{C}}\mathrm{HO}\right)$
- **(4)** Dichlorocarbene $\left(:\mathrm{CCl_2}\right)$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. It is Reimer-Tiemann reaction. The electrophile formed is $:\mathrm{CCl_2}$ (Dichlorocarbene) according to the following reaction
2. $\mathrm{CHCl_3} + \mathrm{OH^-} \rightleftharpoons \overset{\ominus}{\ddot{\mathrm{C}}}\mathrm{Cl_3} + \mathrm{H_2O}$
3. $\overset{\ominus}{\ddot{\mathrm{C}}}\mathrm{Cl_3} \longrightarrow \underset{\text{Electrophile}}{:\mathrm{CCl_2}} + \mathrm{Cl^-}$

**Solved independently** (answer withheld)

1. The reaction of phenol with $\mathrm{CHCl_3}$ and $\mathrm{NaOH}$ giving an ortho $-\mathrm{CHO}$ group is the Reimer-Tiemann reaction.
2. Base removes a proton from chloroform: $\mathrm{CHCl_3} + \mathrm{OH^-} \rightarrow \mathrm{^{-}CCl_3} + \mathrm{H_2O}$.
3. The trichloromethyl anion loses chloride (alpha-elimination): $\mathrm{^{-}CCl_3} \rightarrow :\mathrm{CCl_2} + \mathrm{Cl^-}$.
4. The electron-deficient $:\mathrm{CCl_2}$ attacks the ortho position of the phenoxide ion, and the resulting $-\mathrm{CHCl_2}$ group is hydrolysed by alkali to $-\mathrm{CHO}$.
5. So the electrophile is dichlorocarbene $:\mathrm{CCl_2}$, which is option $4$.

**Subtopic:** Reactions of Phenols · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 15)

![printed question 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q061_0396268e_03112026.png?v=0396268e1fd8)

Publisher's solution, as printed:

![printed solution 61](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q061_87299313_03112026.png?v=87299313323a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** In the Reimer-Tiemann reaction NaOH turns chloroform into dichlorocarbene, and that neutral electron-deficient carbon is the electrophile the phenoxide ring attacks
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The new group in the printed product is a CHO, so the electrophile is read backwards off the product, and the formyl cation is the genuine electrophile of the other formylation taught, the one from CO and HCl.
- **Why:** This question requires the species a printed reagent generates, demonstrated by the scheme reading phenol plus CHCl3 plus NaOH with the question 'The electrophile involved is'.
- **Note:** The reaction lives in the figure, whose supplied text reads 'phenol + CHCl3 + NaOH gives sodium 2-formylphenolate', so the scheme was readable at this step. In our record option 2 reads 'Dichloromethyl anion' while the formula beside it is printed with a plus-charge symbol; the word and the symbol disagree, which looks like a transcription fault in the stored option rather than a feature of the question, and the printed paper should be checked.
<!--/ecat-->

## Q62

Chemistry · organic · Aldehydes, Ketones, and Carboxylic Acids

Carboxylic acids have higher boiling points than aldehydes, ketones and even alcohols of comparable molecular mass. It is due to their

- (1) Formation of intramolecular H-bonding
- (2) More extensive association of carboxylic acid via van der Waals force of attraction
- (3) Formation of carboxylate ion
- **(4)** Formation of intermolecular H-bonding

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Due to formation of intermolecular H-bonding in carboxylic acid, association occurs.
2. Hence boiling point increases and become more than the boiling point of aldehydes, ketones and alcohols of comparable molecular masses.

**Solved independently** (answer withheld)

1. In $\mathrm{RCOOH}$ the $\mathrm{O{-}H}$ of one molecule hydrogen-bonds to the $\mathrm{C{=}O}$ of another, giving extensive intermolecular H-bonding (cyclic dimers), so the boiling point is higher than that of aldehydes, ketones and alcohols of comparable mass: option $4$.

**Subtopic:** Physical Properties of Aldehydes, Ketones, and Carboxylic Acids · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 16)

![printed question 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q062_599f56c5_03112026.png?v=599f56c584db)

Publisher's solution, as printed:

![printed solution 62](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q062_a20f4d57_03112026.png?v=a20f4d57debd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Carboxylic acids boil high because two molecules hydrogen-bond into a cyclic dimer, an attraction between molecules rather than inside one
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Hydrogen bonding is correctly identified as the cause and then labelled with the neighbouring prefix, intramolecular instead of intermolecular.
- **Why:** This question requires the reason the source gives for a granted fact, demonstrated by the stem ending 'It is due to their' after stating the boiling points as settled.
- **Note:** E1 recorded statement_options; the printed options are noun phrases completing 'It is due to their', not rival statements to be judged, so the shape here is a plain mcq.
<!--/ecat-->

## Q63

Chemistry · organic · Alcohols, Phenols and Ethers

Compound A, $\mathrm{C_8H_{10}O}$, is found to react with $\mathrm{NaOI}$ (produced by reacting Y with $\mathrm{NaOH}$) and yields a yellow precipitate with characteristic smell.
A and Y are respectively

- (1) (4-methylphenyl)methanol `Cc1ccc(CO)cc1` ![(4-methylphenyl)methanol](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_1_s1_c9fc9467_03112026.svg?v=c9fc94673ac3); iodine `II` ![iodine](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_1_s2_473787cf_03112026.svg?v=473787cffdf1) — $\mathrm{H_3C}$–[benzene ring]–$\mathrm{CH_2-OH}$ and $\mathrm{I_2}$
- **(2)** 1-phenylethan-1-ol `CC(O)c1ccccc1` ![1-phenylethan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_2_s1_f240d277_03112026.svg?v=f240d277667d); iodine `II` ![iodine](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_2_s2_473787cf_03112026.svg?v=473787cffdf1) — [benzene ring]–$\mathrm{\underset{\displaystyle OH}{CH}-CH_3}$ and $\mathrm{I_2}$
- (3) 2-phenylethan-1-ol `OCCc1ccccc1` ![2-phenylethan-1-ol](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_3_s1_a7a556ba_03112026.svg?v=a7a556baa4c0); iodine `II` ![iodine](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_3_s2_473787cf_03112026.svg?v=473787cffdf1) — [benzene ring]–$\mathrm{CH_2-CH_2-OH}$ and $\mathrm{I_2}$
- (4) 2,4-dimethylphenol `Cc1ccc(O)c(C)c1` ![2,4-dimethylphenol](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_4_s1_883f3e13_03112026.svg?v=883f3e13dca8); iodine `II` ![iodine](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_option_4_s2_473787cf_03112026.svg?v=473787cffdf1) — $\mathrm{CH_3}$–[benzene ring bearing a $\mathrm{CH_3}$]–$\mathrm{OH}$ and $\mathrm{I_2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Option (2) is secondary alcohol which on oxidation gives phenylmethyl ketone (Acetophenone).
2. This on reaction with $\mathrm{I_2}$ and $\mathrm{NaOH}$ form iodoform and sodium benzoate.
3. $\mathrm{2NaOH + I_2 \rightarrow NaOI + NaI + H_2O}$

![printed figure: 1-phenylethan-1-ol (A) →(NaOI) acetophenone (Acetophenone) →($\ce{I2}$ / NaOH) sodium benzoate (Sodium benzoate) + $\ce{CHI3}$ Iodoform (Yellow PPt)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q063_sol_1_3a40665f_03112026.svg?v=3a40665fd54a)

*1-phenylethan-1-ol (A) →[NaOI] acetophenone (Acetophenone) →[$\ce{I2}$ / NaOH] sodium benzoate (Sodium benzoate) + $\ce{CHI3}$ Iodoform (Yellow PPt)*

![drawn: 1-phenylethan-1-ol (A) →(NaOI) acetophenone (Acetophenone) →($\ce{I2}$ / NaOH) sodium benzoate (Sodium benzoate) + $\ce{CHI3}$ Iodoform (Yellow PPt)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q063_solution_1_a6346b57_03112026.svg?v=a6346b57b130)  
*drawn on the booklet's geometry, checked against its SMILES*


**Solved independently** (answer withheld)

1. The yellow precipitate with a characteristic smell is iodoform, $\mathrm{CHI_3}$, so this is the iodoform test.
2. Hypoiodite is made from iodine and alkali: $\mathrm{I_2 + 2NaOH \rightarrow NaOI + NaI + H_2O}$, so $Y = \mathrm{I_2}$.
3. A positive iodoform test needs a $\mathrm{CH_3CH(OH)-}$ or $\mathrm{CH_3CO-}$ group.
4. Option 1 ($p$-methylbenzyl alcohol) and option 3 (2-phenylethanol) are primary alcohols without $\mathrm{CH_3CH(OH)-}$; option 4 (2,4-dimethylphenol) is a phenol; none gives iodoform.
5. Option 2, $\mathrm{C_6H_5CH(OH)CH_3}$ ($\mathrm{C_8H_{10}O}$), is oxidised by $\mathrm{NaOI}$ to $\mathrm{C_6H_5COCH_3}$, which gives $\mathrm{CHI_3}$ + $\mathrm{C_6H_5COONa}$, so the answer is option $2$.

**Subtopic:** Test of Alcohol · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 16)

![printed question 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q063_f520b531_03112026.png?v=f520b531afb5)

Publisher's solution, as printed:

![printed solution 63](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q063_8cfc9c62_03112026.png?v=8cfc9c62b565)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** The iodoform test needs a methyl group sitting on the carbinol or carbonyl carbon, and NaOI comes from iodine with alkali
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  The test is carried as 'needs a CH3 group', so the ring methyl is counted as that group and the CH2OH beside it supplies the alcohol the test is remembered to need.
- **Why:** This question requires which substrate a named reagent converts to the printed product, demonstrated by 'react with NaOI ... and yields a yellow precipitate with characteristic smell'.
- **Note:** Y is printed as I2 in all four options, so the 'respectively' pair does no discriminating work and only A is being chosen; the shape on the page is still two_part, which is why E1's statement_options was not carried.
<!--/ecat-->

## Q64

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Which of the following molecules represents the order of hybridisation $\mathrm{sp^2}$, $\mathrm{sp^2}$, $\mathrm{sp}$, $\mathrm{sp}$ from left to right atoms?

- (1) $\mathrm{HC \equiv C - C \equiv CH}$
- (2) $\mathrm{CH_2 = CH - CH = CH_2}$
- **(3)** $\mathrm{CH_2 = CH - C \equiv CH}$
- (4) $\mathrm{CH_3 - CH = CH - CH_3}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{\overset{sp^{2}}{C}H_2 = \overset{sp^{2}}{C}H - \overset{sp}{C} \equiv \overset{sp}{C}H}$
2. Number of orbital require in hybridization $=$ Number of $\sigma$-bonds around each carbon atom.

**Solved independently** (answer withheld)

1. A carbon in a $\mathrm{C=C}$ double bond (with no triple bond) is $\mathrm{sp^2}$; a carbon in a $\mathrm{C \equiv C}$ triple bond is $\mathrm{sp}$; a carbon with only single bonds is $\mathrm{sp^3}$.
2. Option 1, $\mathrm{HC \equiv C - C \equiv CH}$: $\mathrm{sp, sp, sp, sp}$, which does not match.
3. Option 2, $\mathrm{CH_2 = CH - CH = CH_2}$: $\mathrm{sp^2, sp^2, sp^2, sp^2}$, which does not match.
4. Option 3, $\mathrm{CH_2 = CH - C \equiv CH}$: $\mathrm{C_1}$ and $\mathrm{C_2}$ are $\mathrm{sp^2}$, and $\mathrm{C_3}$ and $\mathrm{C_4}$ are $\mathrm{sp}$, giving $\mathrm{sp^2, sp^2, sp, sp}$, which matches.
5. Option 4, $\mathrm{CH_3 - CH = CH - CH_3}$: $\mathrm{sp^3, sp^2, sp^2, sp^3}$, which does not match.
6. So the answer is option $3$.

**Subtopic:** Hybridisation · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 16)

![printed question 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q064_3c997212_03112026.png?v=3c997212ccba)

Publisher's solution, as printed:

![printed solution 64](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q064_c52c69fc_03112026.png?v=c52c69fc44d2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Each carbon's hybridisation is read off its own bonding: a doubly bonded carbon is sp2 and a triply bonded carbon is sp
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The first two labels of the printed sequence, sp2 and sp2, are matched against the first two carbons of buta-1,3-diene and the check stops there, leaving the two sp carbons unaccounted for.
- **Why:** This question requires a known rule applied to four printed structures, demonstrated by the stem asking which molecule 'represents the order of hybridisation sp2, sp2, sp, sp from left to right atoms'.
<!--/ecat-->

## Q65

Chemistry · organic · General Organic Chemistry

Which of the following carbocations is expected to be most stable?

- (1) 3-nitro-6-Y-cyclohexa-2,4-dien-1-ylium `*C1C=CC([N+](=O)[O-])=C[CH+]1` ![3-nitro-6-Y-cyclohexa-2,4-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q065_option_1_s1_b8d3feea_03112026.svg?v=b8d3feea86bc)
- **(2)** 4-nitro-6-Y-cyclohexa-2,4-dien-1-ylium `*C1C=C([N+](=O)[O-])C=C[CH+]1` ![4-nitro-6-Y-cyclohexa-2,4-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q065_option_2_s1_86051475_03112026.svg?v=860514754db5)
- (3) 1-nitro-4-Y-cyclohexa-2,5-dien-1-ylium `*C1C=C[C+]([N+](=O)[O-])C=C1` ![1-nitro-4-Y-cyclohexa-2,5-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q065_option_3_s1_734a7b36_03112026.svg?v=734a7b3653b7)
- (4) 1-nitro-6-Y-cyclohexa-2,4-dien-1-ylium `*C1C=CC=C[C+]1[N+](=O)[O-]` ![1-nitro-6-Y-cyclohexa-2,4-dien-1-ylium](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q065_option_4_s1_0dc20b0c_03112026.svg?v=0dc20b0c9782)

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. $-\mathrm{NO_2}$ group exhibit $-I$ effect and it decreases with increase in distance.
2. In option (2) positive charge present on C-atom at maximum distance so $-I$ effect reaching to it is minimum and stability is maximum.

**Solved independently** (answer withheld)

1. Each option is an arenium ion formed when an electrophile $Y^+$ attacks nitrobenzene; $-NO_2$ withdraws electrons by $-I$ and $-M$ effects and destabilises nearby positive charge.
2. In options $3$ and $4$ the $\oplus$ sits on the ring carbon that carries $-NO_2$, so they are the least stable.
3. In option $1$ (para attack) the $\oplus$ is on the carbon meta to $-NO_2$, two bonds away, and this ion's resonance set also includes option $3$, which has $\oplus$ on the $C$-$NO_2$ carbon.
4. In option $2$ (meta attack) the $\oplus$ is on the carbon para to $-NO_2$, three bonds away, so the $-I$ pull is weakest, and its delocalisation goes only to $C_2$ and $C_6$, never to the $C$-$NO_2$ carbon.
5. So the most stable carbocation is option $2$.

**Subtopic:** Resonance Effect · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 16)

![printed question 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q065_0f4fc571_03112026.png?v=0f4fc5711d52)

Publisher's solution, as printed:

![printed solution 65](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q065_2af56fe6_03112026.png?v=2af56fe65823)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Carbocation stability is set by how far the positive charge is spread - resonance into a neighbouring pi system first, then hyperconjugation and the +I push of alkyl groups.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four option fields are empty strings in this record and no figure was stored for the question, so there is no structure to compare against another and no route to any option can be checked.
- **Why:** This question requires four drawn carbocations to be ranked by charge delocalisation, demonstrated by the stem 'Which of the following carbocations is expected to be most stable?' while the four option fields carry no content in this record.
- **Note:** options_en holds four empty strings and figure_image is null while has_figure is false, so the carbocation structures the paper printed were never captured - the option set as stored is empty, which is a repair task rather than a reading limit. A reviewer holding the paper should check whether the pull is a benzylic or allylic cation set against a tertiary alkyl cation, which is the usual device for this subtopic (Resonance Effect), and whether the key, option 2, is the resonance-stabilised one.
<!--/ecat-->

## Q66

Chemistry · organic · General Organic Chemistry

Which of the following is correct with respect to $-\mathrm{I}$ effect of the substituents? ($\mathrm{R}$ = alkyl)

- **(1)** $-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$
- (2) $-\mathrm{NH_2} > -\mathrm{OR} > -\mathrm{F}$
- (3) $-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$
- (4) $-\mathrm{NR_2} > -\mathrm{OR} > -\mathrm{F}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $-\mathrm{I}$ effect increases on increasing electronegativity of atom.
2. So, correct order of $-\mathrm{I}$ effect is $-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$.
3. *Most appropriate Answer is option (1), however option (3) may also be correct answer.

**Solved independently** (answer withheld)

1. The $-\mathrm{I}$ effect of a substituent increases with the electronegativity of the atom bonded to the chain: $\chi_{\mathrm{N}} < \chi_{\mathrm{O}} < \chi_{\mathrm{F}}$.
2. So $-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$ in $-\mathrm{I}$ strength, which is option $1$; options $2$ and $4$ give the reverse order and are false.
3. $-\mathrm{NR_2}$ also bonds through N, and its alkyl groups ($+\mathrm{I}$) make it even less electron-withdrawing than $-\mathrm{NH_2}$, so $-\mathrm{NR_2} < -\mathrm{OR} < -\mathrm{F}$ (option $3$) is also true.
4. Options $1$ and $3$ are both correct; option $1$ is chosen as the best single pick with low confidence.

**Subtopic:** Inductive Effect · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 17)

![printed question 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q066_29088e93_03112026.png?v=29088e93872d)

Publisher's solution, as printed:

![printed solution 66](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q066_9200e431_03112026.png?v=9200e4314659)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** The -I pull of a substituent follows the electronegativity of the atom attached to the chain, N < O < F, and alkyl substitution on that nitrogen weakens it further.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  Ranked by electron release, where $-\mathrm{NH_2}$ genuinely does beat $-\mathrm{OR}$ and $-\mathrm{F}$, the sequence comes out $\mathrm{NH_2 > OR > F}$, so this option is the resonance order written where the inductive one was asked for.
- **Why:** This question requires three substituents ordered by their -I pull, demonstrated by the keyed option '$-\mathrm{NH_2} < -\mathrm{OR} < -\mathrm{F}$' following the electronegativity of the attached atom.
- **Note:** The pattern returned `statement_options`; each option is an ordering rather than a claim about a case, the shape `category_retired.qtype` maps to `mcq` through `arrange_in_order`, so the shape is recorded as `mcq`. Options 1 and 3 state the same N < O < F trend and differ only in $-\mathrm{NH_2}$ against $-\mathrm{NR_2}$, and the answer line is printed 'Answer (1*)'. The tag follows the printed key.
<!--/ecat-->

## Q67

Chemistry · inorganic · Coordination Compounds – Practice

The type of isomerism shown by the complex $\mathrm{[CoCl_2(en)_2]}$ is

- **(1)** Geometrical isomerism
- (2) Ionization isomerism
- (3) Coordination isomerism
- (4) Linkage isomerism

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In $\mathrm{[CoCl_2(en)_2]}$, Coordination number of $\mathrm{Co}$ is $6$ and this compound has octahedral geometry.

![printed figure: octahedral geometry diagram of $\ce{(CoCl2(en)2)}$ with the two Cl trans to each other (one above and one below Co) and both en chelate rings in the equatorial plane; caption: Trans-form (optically inactive)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q067_sol_1_e0fd1948_03112026.svg?v=e0fd19481105)

*octahedral geometry diagram of $\ce{[CoCl2(en)2]}$ with the two Cl trans to each other (one above and one below Co) and both en chelate rings in the equatorial plane; caption: Trans-form (optically inactive)*


![printed figure: octahedral geometry diagram of $\ce{(CoCl2(en)2)}$ with the two Cl cis to each other (one above Co, one at an adjacent equatorial position), one en chelate ring spanning two equatorial positions on the left and the other spanning an equatorial and the lower axial position; caption: cis-form (optically active)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q067_sol_2_33a54441_03112026.svg?v=33a544419f3f)

*octahedral geometry diagram of $\ce{[CoCl2(en)2]}$ with the two Cl cis to each other (one above Co, one at an adjacent equatorial position), one en chelate ring spanning two equatorial positions on the left and the other spanning an equatorial and the lower axial position; caption: cis-form (optically active)*

2. As per given option, type of isomerism is geometrical isomerism.

**Solved independently** (answer withheld)

1. $\mathrm{[CoCl_2(en)_2]}$ is octahedral of the type $\mathrm{[M(AA)_2X_2]}$ with two bidentate $\mathrm{en}$ and two $\mathrm{Cl^-}$ ligands.
2. The two $\mathrm{Cl^-}$ ligands can be adjacent ($cis$) or opposite ($trans$), so the complex shows geometrical isomerism.
3. Ionization isomerism needs a counter-ion outside the sphere, coordination isomerism needs both cationic and anionic complex entities, and linkage isomerism needs an ambidentate ligand; none applies here.
4. Hence the answer is geometrical isomerism, option $1$.

**Subtopic:** Isomerism in Coordination Compounds · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q067_cbcf8015_03112026.png?v=cbcf80159f6e)

Publisher's solution, as printed:

![printed solution 67](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q067_31d20358_03112026.png?v=31d203588acd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Cis-trans isomerism in an octahedral complex with two chelating ligands and two like monodentate ligands; each other structural isomerism needs something this formula does not have - a counter-ion, an ambidentate ligand or a second metal.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Ionisation isomers swap an ion between the inside and the outside of the bracket, and chloride is the ion that does that in the worked examples, so seeing Cl in the formula applies the type without checking that this complex has nothing outside the bracket to swap with.
- **Why:** This question requires each isomerism type's structural requirement tested against the printed formula, demonstrated by '$[\mathrm{CoCl_2(en)_2}]$' carrying no counter-ion, no ambidentate ligand and one metal centre.
<!--/ecat-->

## Q68

Chemistry · inorganic · The D- and F-Block Elements – Practice

Which one of the following ions exhibits d-d transition and paramagnetism as well?

- (1) $\mathrm{CrO_4^{2-}}$
- (2) $\mathrm{MnO_4^{-}}$
- (3) $\mathrm{Cr_2O_7^{2-}}$
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

1. In $\mathrm{CrO_4^{2-}}$, $x + 4(-2) = -2 \Rightarrow x = +6$, so Cr is $3d^0$: no d-d transition and diamagnetic.
2. In $\mathrm{MnO_4^{-}}$, $x + 4(-2) = -1 \Rightarrow x = +7$, so Mn is $3d^0$: no d-d transition and diamagnetic (its colour is from charge transfer).
3. In $\mathrm{Cr_2O_7^{2-}}$, $2x + 7(-2) = -2 \Rightarrow x = +6$, so Cr is $3d^0$: no d-d transition and diamagnetic.
4. In $\mathrm{MnO_4^{2-}}$, $x + 4(-2) = -2 \Rightarrow x = +6$, so Mn is $3d^1$ with one unpaired electron.
5. A $3d^1$ ion can show a d-d transition and is paramagnetic, so the answer is option $4$.

**Subtopic:** Magnetic Properties, Ionisation Enthalpies, Formation of Coloured Ions & Formation of Complex Compounds · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q068_6b699e05_03112026.png?v=6b699e05d8f3)

Publisher's solution, as printed:

![printed solution 68](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q068_8f230602_03112026.png?v=8f2306028e35)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Both a d-d transition and paramagnetism need at least one d electron: $\mathrm{MnO_4^{2-}}$ is Mn(VI), d1, while $\mathrm{MnO_4^-}$, $\mathrm{CrO_4^{2-}}$ and $\mathrm{Cr_2O_7^{2-}}$ are all d0 and coloured by charge transfer.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Permanganate and manganate are the same formula one charge apart, and permanganate is the one whose deep colour is remembered, so the formula gets ticked without the oxidation state being taken to +7.
- **Why:** This question requires an oxidation state worked out from each printed charge and then read for d electrons, demonstrated by the stem asking for 'd-d transition and paramagnetism as well' of four oxoanions; on the trap axis likeness and position both hold for $\mathrm{MnO_4^-}$ against $\mathrm{MnO_4^{2-}}$, and section 5.1 gives the win to likeness.
<!--/ecat-->

## Q69

Chemistry · inorganic · Coordination Compounds – Practice

Iron carbonyl, $\mathrm{Fe(CO)_5}$ is

- (1) Tetranuclear
- (2) Trinuclear
- **(3)** Mononuclear
- (4) Dinuclear

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Based on the number of metal atoms present in a complex, they are classified into mononuclear, dinuclear, trinuclear and so on.
2. eg: $\mathrm{Fe(CO)_5}$ : mononuclear
3. $\mathrm{Co_2(CO)_8}$ : dinuclear
4. $\mathrm{Fe_3(CO)_{12}}$: trinuclear
5. Hence, option (3) should be the right answer.

**Solved independently** (answer withheld)

1. $\mathrm{Fe(CO)_5}$ contains one Fe atom bonded to five terminal CO ligands (trigonal bipyramidal), with no metal-metal bond, so it is mononuclear, which is option $3$.

**Subtopic:** Bonding in Coordination Compounds and Metal Carbonyls · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 17)

![printed question 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q069_dccc4953_03112026.png?v=dccc4953b48c)

Publisher's solution, as printed:

![printed solution 69](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q069_7dbe6e1c_03112026.png?v=7dbe6e1ce62f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Nuclearity counts the metal atoms in a carbonyl: $\mathrm{Fe(CO)_5}$ has one iron and is mononuclear, while $\mathrm{Fe_2(CO)_9}$ is the dinuclear iron carbonyl.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  $\mathrm{Fe_2(CO)_9}$, with its bridging carbonyls, is drawn in the same carbonyl figure as $\mathrm{Fe(CO)_5}$, so recalling 'iron carbonyl' as the bridged dimer answers from the neighbouring structure instead of from the printed formula.
- **Why:** This question requires the nuclearity convention applied to a printed formula, demonstrated by 'Iron carbonyl, $\mathrm{Fe(CO)_5}$' carrying a single metal atom.
<!--/ecat-->

## Q70

Chemistry · inorganic · The D- and F-Block Elements – Practice

Match the metal ions given in Column I with the spin magnetic moments of the ions given in Column II and assign the correct code :

| List-I | | List-II | |
|---|---|---|---|
| a | $\mathrm{Co^{3+}}$ | i | $\sqrt{8}\,\mathrm{BM}$ |
| b | $\mathrm{Cr^{3+}}$ | ii | $\sqrt{35}\,\mathrm{BM}$ |
| c | $\mathrm{Fe^{3+}}$ | iii | $\sqrt{3}\,\mathrm{BM}$ |
| d | $\mathrm{Ni^{2+}}$ | iv | $\sqrt{24}\,\mathrm{BM}$ |
|  |  | v | $\sqrt{15}\,\mathrm{BM}$ |

- **(1)** a-iv, b-v, c-ii, d-i
- (2) a-iv, b-i, c-ii, d-iii
- (3) a-i, b-ii, c-iii, d-iv
- (4) a-iii, b-v, c-i, d-ii

**Answer** — booklet: (1) · independent solve: (1) · agree

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

1. Spin-only magnetic moment: $\mu = \sqrt{n(n+2)}\,\mathrm{BM}$, where $n$ is the number of unpaired electrons.
2. $\mathrm{Co^{3+}}$ is $[\mathrm{Ar}]3d^6$; as a free ion $n = 4$, so $\mu = \sqrt{4 \times 6} = \sqrt{24}\,\mathrm{BM}$, matching (iv).
3. $\mathrm{Cr^{3+}}$ is $[\mathrm{Ar}]3d^3$; $n = 3$, so $\mu = \sqrt{3 \times 5} = \sqrt{15}\,\mathrm{BM}$, matching (v).
4. $\mathrm{Fe^{3+}}$ is $[\mathrm{Ar}]3d^5$; $n = 5$, so $\mu = \sqrt{5 \times 7} = \sqrt{35}\,\mathrm{BM}$, matching (ii).
5. $\mathrm{Ni^{2+}}$ is $[\mathrm{Ar}]3d^8$; $n = 2$, so $\mu = \sqrt{2 \times 4} = \sqrt{8}\,\mathrm{BM}$, matching (i).
6. The match a-iv, b-v, c-ii, d-i is option $1$.

**Subtopic:** Magnetic Properties · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 17)

![printed question 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q070_5e0be563_03112026.png?v=5e0be563b9c0)

Publisher's solution, as printed:

![printed solution 70](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q070_b6a19b36_03112026.png?v=b6a19b36f5c7)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** The spin-only magnetic moment is fixed by the number of unpaired d electrons, $\mu=\sqrt{n(n+2)}$ BM, so each ion's d-electron count has to be built correctly first
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Two of its pairs are exactly the key's — $\mathrm{Co^{3+}}$ with $\sqrt{24}$ and $\mathrm{Fe^{3+}}$ with $\sqrt{35}$ — and the code breaks only at $\mathrm{Cr^{3+}}$: stripping all three electrons out of chromium's $3d^5$ leaves $3d^2$, $n=2$, $\sqrt{8}$ BM, which is printed as (i).
- **Why:** This question requires $\mu=\sqrt{n(n+2)}$ worked out from each ion's d-electron count, demonstrated by Column II printing the five values $\sqrt{8}$, $\sqrt{35}$, $\sqrt{3}$, $\sqrt{24}$ and $\sqrt{15}$ BM.
<!--/ecat-->

## Q71

Chemistry · inorganic · Coordination Compounds – Practice

The geometry and magnetic behaviour of the complex $\mathrm{[Ni(CO)_4]}$ are

- (1) Square planar geometry and diamagnetic
- (2) Square planar geometry and paramagnetic
- **(3)** Tetrahedral geometry and diamagnetic
- (4) Tetrahedral geometry and paramagnetic

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{Ni}(28)$ : $[\mathrm{Ar}]3d^{8}\,4s^{2}$
2. $\because$ $\mathrm{CO}$ is a strong field ligand
3. Configuration would be :

![printed figure: orbital-box diagram: five boxes each holding a pair of electrons (⇅), then four boxes each holding an electron pair (× ×), these four enclosed in a dotted box labelled sp³-hybridisation, with CO written under each of the four boxes (one box, then three adjacent boxes)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q071_sol_1_c201986c_03112026.svg?v=c201986cda42)

*orbital-box diagram: five boxes each holding a pair of electrons (⇅), then four boxes each holding an electron pair (× ×), these four enclosed in a dotted box labelled sp³-hybridisation, with CO written under each of the four boxes (one box, then three adjacent boxes)*

4. For, four '$\mathrm{CO}$'-ligands hybridisation would be $sp^{3}$ and thus the complex would be diamagnetic and of tetrahedral geometry.

![printed figure: tetracarbonylnickel(0), $\ce{(Ni(CO)4)}$, drawn tetrahedral: Ni at the centre bonded by solid lines to CO (top), OC (lower left), CO (right) and CO (bottom), the four CO groups joined by dotted lines outlining the tetrahedron](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q071_sol_2_4aff1d05_03112026.svg?v=4aff1d05000e)

*tetracarbonylnickel(0), $\ce{[Ni(CO)4]}$, drawn tetrahedral: Ni at the centre bonded by solid lines to CO (top), OC (lower left), CO (right) and CO (bottom), the four CO groups joined by dotted lines outlining the tetrahedron*


**Solved independently** (answer withheld)

1. In $\mathrm{[Ni(CO)_4]}$, CO is neutral, so the oxidation state of Ni is $0$: $\mathrm{Ni}(0) = [\mathrm{Ar}]\,3d^8\,4s^2$.
2. CO is a strong-field ligand, so the two $4s$ electrons pair up in $3d$, giving $3d^{10}\,4s^0$.
3. The empty $4s$ and three $4p$ orbitals accept four CO lone pairs: $sp^3$ hybridisation, so the geometry is tetrahedral.
4. With $3d^{10}$ all electrons are paired, so the number of unpaired electrons is $0$ and the complex is diamagnetic, which is option $3$.

**Subtopic:** Valence Bond Theory, Its Limitations and Magnetic Properties of Coordination Compounds · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 18)

![printed question 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q071_eb90297b_03112026.png?v=eb90297b3cf7)

Publisher's solution, as printed:

![printed solution 71](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q071_062fb07d_03112026.png?v=062fb07d50e6)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** CO is a neutral ligand, so nickel in $[\mathrm{Ni(CO)_4}]$ is zero-valent 3d10: sp3 tetrahedral and diamagnetic, unlike the d8 Ni(II) complexes.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Nickel is met as Ni2+ in nearly every complex, and d8 leaves two unpaired electrons, so the geometry comes out right and the magnetism is read off the wrong oxidation state.
- **Why:** This question requires geometry and magnetic behaviour settled together from the metal's oxidation state, demonstrated by the stem asking for 'the geometry and magnetic behaviour' of $[\mathrm{Ni(CO)_4}]$ and by every option pairing one geometry with one magnetic verdict.
- **Note:** The pattern returned `statement_options`, but the stem names two quantities to be answered at once and each option supplies both, which is the retired `multi_part_respectively` shape that `category_retired.qtype` maps to `two_part`. Recorded as the shape on the page.
<!--/ecat-->

## Q72

Chemistry · physical · Chemical Kinetics

The correct difference between first and second order reactions is that

- (1) The rate of a first-order reaction does not depend on reactant concentrations; the rate of a second-order reaction does depend on reactant concentrations
- (2) A first-order reaction can catalyzed; a second-order reaction cannot be catalyzed
- **(3)** The half-life of a first-order reaction does not depend on $[\mathrm{A}]_0$; the half-life of a second-order reaction does depend on $[\mathrm{A}]_0$
- (4) The rate of a first-order reaction does depend on reactant concentrations; the rate of a second-order reaction does not depend on reactant concentrations

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. For first order reaction, $t_{1/2} = \frac{0.693}{k}$, which is independent of initial concentration of reactant.
2. For second order reaction, $t_{1/2} = \frac{1}{k[A_0]}$, which depends on initial concentration of reactant.

**Solved independently** (answer withheld)

1. For a first-order reaction, $\text{rate} = k[\mathrm{A}]$ and for a second-order reaction, $\text{rate} = k[\mathrm{A}]^2$, so both rates depend on reactant concentration; options $1$ and $4$ are false.
2. A catalyst can lower the activation energy of a reaction of any order, so option $2$ is false.
3. First order: $t_{1/2} = \frac{0.693}{k}$, which is independent of $[\mathrm{A}]_0$.
4. Second order: $t_{1/2} = \frac{1}{k[\mathrm{A}]_0}$, which depends on $[\mathrm{A}]_0$, so option $3$ is correct.

**Subtopic:** Half-Life of a Reaction · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 18)

![printed question 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q072_771ea93e_03112026.png?v=771ea93eacea)

Publisher's solution, as printed:

![printed solution 72](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q072_f461519a_03112026.png?v=f461519a5bcb)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** A first-order half-life, $0.693/k$, carries no starting concentration in it; a second-order half-life, $1/(k[\mathrm{A}]_0)$, does - while the rate of both depends on concentration.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Independence of concentration is the thing remembered about first order, and this option attaches it to the rate instead of the half-life; its second clause, that a second-order rate does depend on concentration, is true, so only the first clause has to be caught.
- **Why:** This question requires two neighbouring kinetic orders told apart on one property, demonstrated by the stem 'The correct difference between first and second order reactions is that' and by the keyed clause 'the half-life of a first-order reaction does not depend on $[\mathrm{A}]_0$'.
- **Note:** The pattern returned `statement_options`; the stem is a lead-in only and each option is a full two-clause claim to be graded, which `category_retired.qtype` maps to `statements`.
<!--/ecat-->

## Q73

Chemistry · inorganic · The s-Block Elements

Among $\mathrm{CaH_2}$, $\mathrm{BeH_2}$, $\mathrm{BaH_2}$, the order of ionic character is

- **(1)** $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$
- (2) $\mathrm{BeH_2} < \mathrm{BaH_2} < \mathrm{CaH_2}$
- (3) $\mathrm{CaH_2} < \mathrm{BeH_2} < \mathrm{BaH_2}$
- (4) $\mathrm{BaH_2} < \mathrm{BeH_2} < \mathrm{CaH_2}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. For $2^{\text{nd}}$ group hydrides, on moving down the group metallic character of metals increases so ionic character of metal hydride increases.
2. Hence the option (1) should be correct option.

**Solved independently** (answer withheld)

1. Down group 2 ($\mathrm{Be} \rightarrow \mathrm{Ca} \rightarrow \mathrm{Ba}$) the metal gets larger and more electropositive, so its polarising power falls and the $\mathrm{M-H}$ bond becomes more ionic.
2. $\mathrm{BeH_2}$ is covalent (polymeric), so it is the least ionic.
3. Hence the order is $\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$, which is option $1$.

**Subtopic:** Alkaline Earth Metals: Properties and Trends · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 18)

![printed question 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q073_f9d19fa0_03112026.png?v=f9d19fa03c94)

Publisher's solution, as printed:

![printed solution 73](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q073_8cbd74a9_03112026.png?v=8cbd74a9e9b1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Ionic character of the group 2 hydrides rises with the electropositive character of the metal down the group: BeH2 is covalent and polymeric, CaH2 and BaH2 are saline.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  CaH2 is the hydride the chapter names and nicknames - hydrolith, the one used as a hydrogen source - so ranking by which hydride is printed as the saline one puts calcium at the top and barium underneath it.
- **Why:** This question requires a group trend applied to three named hydrides, demonstrated by the keyed order '$\mathrm{BeH_2} < \mathrm{CaH_2} < \mathrm{BaH_2}$' running down the group.
- **Note:** The pattern returned `statement_options`; the options are orderings, which `category_retired.qtype` maps to `mcq` through `arrange_in_order`.
<!--/ecat-->

## Q74

Chemistry · physical · Basic Concepts of Chemistry

In which case is number of molecules of water maximum?

- **(1)** $18\,\mathrm{mL}$ of water
- (2) $0.00224\,\mathrm{L}$ of water vapours at $1\,\mathrm{atm}$ and $273\,\mathrm{K}$
- (3) $0.18\,\mathrm{g}$ of water
- (4) $10^{-3}\,\mathrm{mol}$ of water

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. (1) Mass of water $= 18 \times 1 = 18\,\mathrm{g}$
2. Molecules of water $=$ mole $\times N_{A} = \frac{18}{18}N_{A}$
3. $= N_{A}$
4. (2) Moles of water $= \frac{0.00224}{22.4} = 10^{-4}$
5. Molecules of water $=$ mole $\times N_{A} = 10^{-4}\,N_{A}$
6. (3) Molecules of water $=$ mole $\times N_{A} = \frac{0.18}{18}N_{A}$
7. $= 10^{-2}\,N_{A}$
8. (4) Molecules of water $=$ mole $\times N_{A} = 10^{-3}\,N_{A}$

**Solved independently** (answer withheld)

1. Molecules are proportional to moles, so compare the moles of water in each option.
2. Option 1: mass $= 18\,\mathrm{mL} \times 1\,\mathrm{g\,mL^{-1}} = 18\,\mathrm{g}$.
3. $n_1 = \frac{18\,\mathrm{g}}{18\,\mathrm{g\,mol^{-1}}} = 1\,\mathrm{mol}$.
4. Option 2: at $1\,\mathrm{atm}$ and $273\,\mathrm{K}$, $n_2 = \frac{0.00224\,\mathrm{L}}{22.4\,\mathrm{L\,mol^{-1}}} = 10^{-4}\,\mathrm{mol}$.
5. Option 3: $n_3 = \frac{0.18\,\mathrm{g}}{18\,\mathrm{g\,mol^{-1}}} = 10^{-2}\,\mathrm{mol}$.
6. Option 4: $n_4 = 10^{-3}\,\mathrm{mol}$.
7. $n_1 = 1\,\mathrm{mol}$ is the largest, so $18\,\mathrm{mL}$ of water has the most molecules, which is option $1$.

**Subtopic:** Mole Concept · **Difficulty:** easy (4 steps)

**Printed in the booklet** (page 18)

![printed question 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q074_bc9affe9_03112026.png?v=bc9affe9db93)

Publisher's solution, as printed:

![printed solution 74](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q074_f6923901_03112026.png?v=f69239013730)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** To count molecules, bring every amount to moles: 18 mL of water is 18 g and so a full mole, against $10^{-2}$, $10^{-3}$ and $10^{-4}$ mol in the other three options.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 3  
  Stopping before the density step leaves 18 mL as a volume with no mass attached, and $0.18/18 = 0.01$ mol is then the largest amount in hand.
- **Why:** This question requires four differently stated amounts brought to a common unit and compared, demonstrated by the options mixing '18 mL of water', '0.00224 L of water vapours', '0.18 g of water' and '$10^{-3}$ mol of water'.
<!--/ecat-->

## Q75

Chemistry · physical · Redox Reactions

Consider the change in oxidation state of Bromine corresponding to different emf values as shown in the diagram below :

Then the species undergoing disproportionation is

![printed figure: Latimer (emf) diagram of bromine oxidation states: $\ce{BrO4-}$ →(1.82 V) $\ce{BrO3-}$ →(1.5 V) $\ce{HBrO}$ →(1.595 V) $\ce{Br2}$ →(1.0652 V) $\ce{Br-}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q075_9397b000_03112026.svg?v=9397b00018ae)

*Latimer (emf) diagram of bromine oxidation states: $\ce{BrO4-}$ →[1.82 V] $\ce{BrO3-}$ →[1.5 V] $\ce{HBrO}$ →[1.595 V] $\ce{Br2}$ →[1.0652 V] $\ce{Br-}$*

- (1) $\mathrm{BrO_3^-}$
- (2) $\mathrm{Br_2}$
- (3) $\mathrm{BrO_4^-}$
- **(4)** $\mathrm{HBrO}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\overset{+1}{\mathrm{HBrO}} \longrightarrow \overset{0}{\mathrm{Br_2}}$, $E^{\circ}_{\mathrm{HBrO/Br_2}} = 1.595\,\mathrm{V}$
2. $\overset{+1}{\mathrm{HBrO}} \longrightarrow \overset{+5}{\mathrm{BrO_3^-}}$, $E^{\circ}_{\mathrm{BrO_3^-/HBrO}} = 1.5\,\mathrm{V}$
3. $E^{\circ}_{\mathrm{cell}}$ for the disproportionation of $\mathrm{HBrO}$,
4. $E^{\circ}_{\mathrm{cell}} = E^{\circ}_{\mathrm{HBrO/Br_2}} - E^{\circ}_{\mathrm{BrO_3^-/HBrO}}$
5. $= 1.595 - 1.5$
6. $= 0.095\,\mathrm{V} = +\mathrm{ve}$
7. Hence, option (4) is correct answer.

**Solved independently** (answer withheld)

1. A species disproportionates spontaneously when $E^\circ$ for its reduction (to its right in the diagram) exceeds $E^\circ$ for its formation by reduction of the species to its left, so that $E^\circ_{cell} = E^\circ_{right} - E^\circ_{left} > 0$.
2. $\mathrm{BrO_4^-}$ is Br in its highest state (+7), so it cannot be oxidised and cannot disproportionate.
3. For $\mathrm{BrO_3^-}$: $E^\circ_{cell} = 1.5 - 1.82 = -0.32\,\mathrm{V} < 0$, not spontaneous.
4. For $\mathrm{HBrO}$: $E^\circ_{cell} = E^\circ_{\mathrm{HBrO/Br_2}} - E^\circ_{\mathrm{BrO_3^-/HBrO}} = 1.595 - 1.5 = +0.095\,\mathrm{V} > 0$, spontaneous.
5. For $\mathrm{Br_2}$: $E^\circ_{cell} = 1.0652 - 1.595 = -0.5298\,\mathrm{V} < 0$, not spontaneous.
6. So $\mathrm{HBrO}$ disproportionates into $\mathrm{BrO_3^-}$ and $\mathrm{Br_2}$, which is option $4$.

**Subtopic:** Types of Redox Reactions · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 19)

![printed question 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q075_030fcdf4_03112026.png?v=030fcdf46a94)

Publisher's solution, as printed:

![printed solution 75](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q075_4493cb1a_03112026.png?v=4493cb1a2482)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Figure reading** (`read_diagram`) — read a figure, graph or drawn structure and answer from it
- **Concept:** On a Latimer diagram a species disproportionates when the potential on its right exceeds the potential on its left: HBrO has 1.595 V out and 1.5 V in.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Bromine's disproportionation in alkali is the reaction carried over from the halogen chapter, so the answer comes from that memory rather than from the printed potentials, which for Br2 read 1.595 V in against 1.0652 V out - the wrong way round.
- **Why:** This question requires two potentials read off the printed diagram and set against each other, demonstrated by the stem's 'as shown in the diagram below' and by HBrO carrying 1.5 V on its left and 1.595 V on its right.
- **Note:** The figure was supplied to this step as text (BrO4- 1.82 V, BrO3- 1.5 V, HBrO 1.595 V, Br2 1.0652 V, Br-), so the diagram could be read and the trap checked against it.
<!--/ecat-->

## Q76

Chemistry · physical · Thermodynamics

The bond dissociation energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are in the ratio of $1 : 0.5 : 1$. $\Delta H$ for the formation of $\mathrm{XY}$ is $-200\,\mathrm{kJ\,mol^{-1}}$. The bond dissociation energy of $\mathrm{X_2}$ will be

- (1) $200\,\mathrm{kJ\,mol^{-1}}$
- **(2)** $800\,\mathrm{kJ\,mol^{-1}}$
- (3) $100\,\mathrm{kJ\,mol^{-1}}$
- (4) $400\,\mathrm{kJ\,mol^{-1}}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The reaction for $\Delta_{f}H^{\circ}(\mathrm{XY})$
2. $\frac{1}{2}\mathrm{X_2(g)} + \frac{1}{2}\mathrm{Y_2(g)} \longrightarrow \mathrm{XY(g)}$
3. Bond energies of $\mathrm{X_2}$, $\mathrm{Y_2}$ and $\mathrm{XY}$ are $X$, $\frac{X}{2}$, $X$ respectively
4. $\therefore\ \Delta H = \left(\frac{X}{2} + \frac{X}{4}\right) - X = -200$
5. On solving, we get
6. $\Rightarrow -\frac{X}{2} + \frac{X}{4} = -200$
7. $\Rightarrow X = 800\,\mathrm{kJ/mole}$

**Solved independently** (answer withheld)

1. Formation reaction of $\mathrm{XY}$: $\tfrac{1}{2}\mathrm{X_2} + \tfrac{1}{2}\mathrm{Y_2} \rightarrow \mathrm{XY}$.
2. Let the bond dissociation energies be $\mathrm{X_2} = a$, $\mathrm{Y_2} = 0.5a$, $\mathrm{XY} = a$.
3. $\Delta H = \sum \text{BE(broken)} - \sum \text{BE(formed)} = \tfrac{1}{2}a + \tfrac{1}{2}(0.5a) - a$.
4. $\Delta H = 0.5a + 0.25a - a = -0.25a$.
5. $-0.25a = -200\,\mathrm{kJ\,mol^{-1}} \Rightarrow a = 800\,\mathrm{kJ\,mol^{-1}}$, which is option $2$.

**Subtopic:** Bond Enthalpy (ΔBondH°) · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 19)

![printed question 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q076_399dc60b_03112026.png?v=399dc60bdd35)

Publisher's solution, as printed:

![printed solution 76](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q076_7b7b5cff_03112026.png?v=7b7b5cffdb01)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Bond enthalpies through Hess's law: $\Delta H_f(\mathrm{XY}) = \tfrac{1}{2}E_{\mathrm{X_2}} + \tfrac{1}{2}E_{\mathrm{Y_2}} - E_{\mathrm{XY}}$, which with the ratio 1 : 0.5 : 1 is $-0.25E_{\mathrm{X_2}}$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 4  
  Writing the equation as $\mathrm{X_2 + Y_2 \to 2XY}$ and then setting its enthalpy to the printed $-200$ instead of $-400$ loses a factor of two: $E + 0.5E - 2E = -0.5E = -200$ gives 400 in place of 800.
- **Why:** This question requires a bond-enthalpy cycle built on a printed ratio, demonstrated by the stem giving '$\Delta H$ for the formation of XY is $-200$ kJ mol$^{-1}$' with the energies 'in the ratio of 1 : 0.5 : 1'.
<!--/ecat-->

## Q77

Chemistry · physical · Chemical Kinetics

When initial concentration of the reactant is doubled, the half-life period of a zero order reaction

- (1) Is halved
- (2) Is tripled
- **(3)** Is doubled
- (4) Remains unchanged

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Half life of zero order
2. $t_{1/2} = \frac{[A_0]}{2K}$
3. $t_{1/2}$ will be doubled on doubling the initial concentration.

**Solved independently** (answer withheld)

1. For a zero order reaction, $[A] = [A]_0 - kt$, so at half-life $\frac{[A]_0}{2} = [A]_0 - k t_{1/2}$.
2. $t_{1/2} = \frac{[A]_0}{2k}$, so $t_{1/2} \propto [A]_0$.
3. $t_{1/2}' = \frac{2[A]_0}{2k} = 2\,t_{1/2}$, so the half-life is doubled, which is option $3$.

**Subtopic:** Half-Life of a Reaction, Zero Order Reactions · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 19)

![printed question 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q077_c979e1bc_03112026.png?v=c979e1bcf600)

Publisher's solution, as printed:

![printed solution 77](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q077_b7917724_03112026.png?v=b7917724bc94)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Proportionality** (`relation`) — how much one quantity changes when another does
- **Concept:** For a zero-order reaction $t_{1/2} = [\mathrm{A}]_0/2k$, so the half-life is proportional to the starting concentration - unlike first order, where it is independent of it.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 4  
  The half-life that does not move with concentration is the first-order one, $0.693/k$, and using that expression here leaves the half-life unchanged when $[\mathrm{A}]_0$ is doubled.
- **Why:** This question requires how far one quantity moves when another is doubled, demonstrated by the stem's 'initial concentration of the reactant is doubled' set against the zero-order half-life $[\mathrm{A}]_0/2k$.
<!--/ecat-->

## Q78

Chemistry · physical · Redox Reactions

For the redox reaction
$\mathrm{MnO_4^- + C_2O_4^{2-} + H^+ \longrightarrow Mn^{2+} + CO_2 + H_2O}$
The correct coefficients of the reactants for the balanced equation are
$\mathrm{MnO_4^-}\quad \mathrm{C_2O_4^{2-}}\quad \mathrm{H^+}$

- (1) $16\quad 5\quad 2$
- (2) $2\quad 16\quad 5$
- **(3)** $2\quad 5\quad 16$
- (4) $5\quad 16\quad 2$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

![printed figure: permanganate ($\ce{MnO4-}$, Mn +7) + oxalate ($\ce{C2O4^2-}$, C +3) + hydron ($\ce{H+}$) → manganese(2+) ($\ce{Mn^2+}$) + carbon dioxide ($\ce{CO2}$, C +4) + water ($\ce{H2O}$); bracket labelled Reduction joins Mn (+7) in $\ce{MnO4-}$ to $\ce{Mn^2+}$; bracket labelled Oxidation joins C (+3) in $\ce{C2O4^2-}$ to C (+4) in $\ce{CO2}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q078_sol_1_a1a70b33_03112026.svg?v=a1a70b33beff)

*permanganate ($\ce{MnO4-}$, Mn +7) + oxalate ($\ce{C2O4^2-}$, C +3) + hydron ($\ce{H+}$) → manganese(2+) ($\ce{Mn^2+}$) + carbon dioxide ($\ce{CO2}$, C +4) + water ($\ce{H2O}$); bracket labelled Reduction joins Mn (+7) in $\ce{MnO4-}$ to $\ce{Mn^2+}$; bracket labelled Oxidation joins C (+3) in $\ce{C2O4^2-}$ to C (+4) in $\ce{CO2}$*

![drawn: permanganate ($\ce{MnO4-}$, Mn +7) + oxalate ($\ce{C2O4^2-}$, C +3) + hydron ($\ce{H+}$) → manganese(2+) ($\ce{Mn^2+}$) + carbon dioxide ($\ce{CO2}$, C +4) + water ($\ce{H2O}$); bracket labelled Reduction joins Mn (+7) in $\ce{MnO4-}$ to $\ce{Mn^2+}$; bracket labelled Oxidation joins C (+3) in $\ce{C2O4^2-}$ to C (+4) in $\ce{CO2}$](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q078_solution_1_e52c5394_03112026.svg?v=e52c5394d1a6)  
*drawn on the booklet's geometry, checked against its SMILES*

1. n-factor of $\mathrm{MnO_4^-} \Rightarrow 5$
2. n-factor of $\mathrm{C_2O_4^{2-}} \Rightarrow 2$
3. Ratio of n-factors of $\mathrm{MnO_4^-}$ and $\mathrm{C_2O_4^{2-}}$ is $5 : 2$
4. So, molar ratio in balanced reaction is $2 : 5$
5. $\therefore$ The balanced equation is
6. $\mathrm{2MnO_4^- + 5C_2O_4^{2-} + 16H^+ \rightarrow 2Mn^{2+} + 10CO_2 + 8H_2O}$

**Solved independently** (answer withheld)

1. Oxidation states: $\mathrm{Mn}$ goes from $+7$ in $\mathrm{MnO_4^-}$ to $+2$ in $\mathrm{Mn^{2+}}$, a gain of $5e^-$ per Mn.
2. $\mathrm{C}$ goes from $+3$ in $\mathrm{C_2O_4^{2-}}$ to $+4$ in $\mathrm{CO_2}$, a loss of $2e^-$ per $\mathrm{C_2O_4^{2-}}$.
3. Equate electrons: $2 \times 5 = 5 \times 2 = 10$, so $2\,\mathrm{MnO_4^-}$ and $5\,\mathrm{C_2O_4^{2-}}$, giving $2\,\mathrm{Mn^{2+}}$ and $10\,\mathrm{CO_2}$.
4. Oxygen: left has $8 + 20 = 28$, right has $20$ in $\mathrm{CO_2}$, so $8\,\mathrm{H_2O}$ are formed, needing $16\,\mathrm{H^+}$.
5. Charge check: $2(-1) + 5(-2) + 16(+1) = +4 = 2(+2)$, balanced.
6. Reactant coefficients $\mathrm{MnO_4^-} : \mathrm{C_2O_4^{2-}} : \mathrm{H^+} = 2 : 5 : 16$, which is option $3$.

**Subtopic:** Balancing of Redox Reactions · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 19)

![printed question 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q078_99254b33_03112026.png?v=99254b33d9e8)

Publisher's solution, as printed:

![printed solution 78](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q078_ed2ca85a_03112026.png?v=ed2ca85ac7d8)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Balancing permanganate against oxalate by electrons: Mn(VII) takes 5 electrons and each $\mathrm{C_2O_4^{2-}}$ gives 2, so 2 $\mathrm{MnO_4^-}$ to 5 $\mathrm{C_2O_4^{2-}}$, and the oxygen balance then fixes 16 $\mathrm{H^+}$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The balanced equation is often written and recited with the acid first - 16 $\mathrm{H^+}$ + 5 $\mathrm{C_2O_4^{2-}}$ + 2 $\mathrm{MnO_4^-}$ - and reading that triple straight onto the printed headers puts the coefficients in exactly the reverse order.
- **Why:** This question requires the electron and oxygen balance of a printed redox equation worked out, demonstrated by the keyed coefficients '2 5 16' standing under the headers $\mathrm{MnO_4^-}$, $\mathrm{C_2O_4^{2-}}$, $\mathrm{H^+}$.
- **Note:** The pattern returned `plain_mcq`, but the stem prints three species as column headers and each option answers all three slots at once - the retired `multi_part_respectively` shape, which `category_retired.qtype` maps to `two_part`. Recorded as the shape on the page.
<!--/ecat-->

## Q79

Chemistry · physical · Chemical Equilibrium

Which one of the following conditions will favour maximum formation of the product in the reaction, $\mathrm{A_2(g)} + \mathrm{B_2(g)} \rightleftharpoons \mathrm{X_2(g)}\ \Delta_r H = -X\,\mathrm{kJ}$?

- **(1)** Low temperature and high pressure
- (2) High temperature and high pressure
- (3) Low temperature and low pressure
- (4) High temperature and low pressure

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. $\mathrm{A_2(g)} + \mathrm{B_2(g)} \rightleftharpoons \mathrm{X_2(g)}$; $\Delta H = -x\,\mathrm{kJ}$
2. On increasing pressure equilibrium shifts in a direction where pressure decreases i.e. forward direction.
3. On decreasing temperature, equilibrium shifts in exothermic direction i.e., forward direction.
4. So, high pressure and low temperature favours maximum formation of product.

**Solved independently** (answer withheld)

1. $\Delta_r H = -X\,\mathrm{kJ} < 0$, so the forward reaction is exothermic and, by Le Chatelier's principle, lowering the temperature shifts equilibrium towards $\mathrm{X_2}$.
2. $\Delta n_g = 1 - (1 + 1) = -1 < 0$, so the forward reaction reduces the number of gas moles.
3. A decrease in gas moles means raising the pressure shifts equilibrium towards $\mathrm{X_2}$.
4. Low temperature and high pressure together give maximum product, which is option $1$.

**Subtopic:** Le Chatelier's Principle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 20)

![printed question 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q079_5dd808a2_03112026.png?v=5dd808a277a6)

Publisher's solution, as printed:

![printed solution 79](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q079_2ce74331_03112026.png?v=2ce7433168d2)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Le Chatelier on an exothermic, mole-decreasing equilibrium: cooling favours the forward reaction and compressing favours the side with fewer gas molecules, which here is the product.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The pressure half is argued correctly from two moles of gas becoming one, and the temperature half comes from treating heating as something that always yields more product, which is a statement about rate and not about where an exothermic equilibrium sits.
- **Why:** This question requires Le Chatelier applied to a stated enthalpy and a stated mole change, demonstrated by '$\mathrm{A_2(g) + B_2(g) \rightleftharpoons X_2(g)}$, $\Delta_r H = -X$ kJ' and the keyed 'Low temperature and high pressure'.
- **Note:** The pattern returned `statement_options`; the stem asks one question and each option is a short pair of conditions rather than a claim to be graded, so the shape is recorded as `mcq`.
<!--/ecat-->

## Q80

Chemistry · physical · States of Matter

The correction factor ‘a’ to the ideal gas equation corresponds to

- (1) Density of the gas molecules
- (2) Electric field present between the gas molecules
- (3) Volume of the gas molecules
- **(4)** Forces of attraction between the gas molecules

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In real gas equation, $\left(\mathrm{P} + \frac{\mathrm{a}n^{2}}{\mathrm{V}^{2}}\right)(\mathrm{V} - n\mathrm{b}) = n\mathrm{RT}$
2. van der Waal’s constant, ‘a’ signifies intermolecular forces of attraction.

**Solved independently** (answer withheld)

1. The van der Waals equation is $\left(p + \frac{a n^2}{V^2}\right)(V - nb) = nRT$, where the term $\frac{a n^2}{V^2}$ corrects the observed pressure because attractive forces between molecules reduce how hard they hit the walls, so $a$ measures the forces of attraction between gas molecules (while $b$ corrects for molecular volume), which is option $4$.

**Subtopic:** Real Gases and van der Waals Equation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 20)

![printed question 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q080_8687107a_03112026.png?v=8687107a452c)

Publisher's solution, as printed:

![printed solution 80](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q080_bc6945e7_03112026.png?v=bc6945e7b8e3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** In van der Waals' equation the constant $a$ restores the pressure lost to intermolecular attraction, while $b$ accounts for the volume the molecules themselves occupy.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The two corrections are printed side by side, so knowing that one is for molecular volume and one for attraction but not which letter carries which takes the volume meaning for $a$.
- **Why:** This question requires the stated meaning of one van der Waals constant, demonstrated by the keyed 'Forces of attraction between the gas molecules' against the volume correction, which is the other constant.
- **Note:** The pattern returned `statement_options`; the stem is a direct question and the options are short noun phrases answering it, so the shape is recorded as `mcq`.
<!--/ecat-->

## Q81

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Magnesium reacts with an element (X) to form an ionic compound. If the ground state electronic configuration of (X) is $1s^{2}\,2s^{2}\,2p^{3}$, the simplest formula for this compound is

- (1) $\mathrm{Mg_{2}X_{3}}$
- (2) $\mathrm{Mg_{2}X}$
- (3) $\mathrm{MgX_{2}}$
- **(4)** $\mathrm{Mg_{3}X_{2}}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Element (X) electronic configuration $1s^{2}\,2s^{2}\,2p^{3}$
2. So, valency of X will be $3$.
3. Valency of $\mathrm{Mg}$ is $2$.
4. Formula of compound formed by $\mathrm{Mg}$ and X will be $\mathrm{Mg_{3}X_{2}}$.

**Solved independently** (answer withheld)

1. $1s^{2}\,2s^{2}\,2p^{3}$ has 5 valence electrons, so $X$ (nitrogen) gains 3 electrons to form $X^{3-}$.
2. Magnesium ($[\mathrm{Ne}]\,3s^{2}$) loses 2 electrons to form $\mathrm{Mg^{2+}}$.
3. Charge balance: $3(+2) + 2(-3) = 0$, so the simplest formula is $\mathrm{Mg_{3}X_{2}}$, which is option $4$.

**Subtopic:** Covalent and Ionic Bond · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q081_871315e0_03112026.png?v=871315e0c977)

Publisher's solution, as printed:

![printed solution 81](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q081_ee0dc845_03112026.png?v=ee0dc845ad6a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A ground state ending $2p^3$ is nitrogen: five valence electrons, hence $\mathrm{X^{3-}}$, which with $\mathrm{Mg^{2+}}$ balances as $\mathrm{Mg_3X_2}$.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The crossover rule gives each ion the other's charge as its subscript; keeping each ion's own charge instead - 2 on Mg and 3 on X - prints the two subscripts the wrong way round.
- **Why:** This question requires an electron configuration read for valency and then combined by charge balance, demonstrated by the stem's '$1s^2 2s^2 2p^3$' and 'forms an ionic compound' with magnesium.
<!--/ecat-->

## Q82

Chemistry · physical · The Solid State

Iron exhibits bcc structure at room temperature. Above $900\,^\circ\mathrm{C}$, it transforms to fcc structure. The ratio of density of iron at room temperature to that at $900\,^\circ\mathrm{C}$ (assuming molar mass and atomic radii of iron remains constant with temperature) is

- (1) $\dfrac{\sqrt{3}}{\sqrt{2}}$
- **(2)** $\dfrac{3\sqrt{3}}{4\sqrt{2}}$
- (3) $\dfrac{4\sqrt{3}}{3\sqrt{2}}$
- (4) $\dfrac{1}{2}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. For BCC lattice : $Z = 2$, $a = \frac{4r}{\sqrt{3}}$
2. For FCC lattice : $Z = 4$, $a = 2\sqrt{2}\,r$
3. $\therefore \frac{d_{25\,^\circ\mathrm{C}}}{d_{900\,^\circ\mathrm{C}}} = \frac{\left(\frac{ZM}{N_A a^3}\right)_{\mathrm{BCC}}}{\left(\frac{ZM}{N_A a^3}\right)_{\mathrm{FCC}}}$
4. $= \frac{2}{4}\left(\frac{2\sqrt{2}\,r}{\frac{4r}{\sqrt{3}}}\right)^{3} = \left(\frac{3\sqrt{3}}{4\sqrt{2}}\right)$

**Solved independently** (answer withheld)

1. Density of a cubic cell: $\rho = \frac{Z M}{N_A a^3}$, with $M$ and $r$ constant.
2. bcc: $Z = 2$ and $\sqrt{3}a = 4r$, so $a_{bcc} = \frac{4r}{\sqrt{3}}$.
3. fcc: $Z = 4$ and $\sqrt{2}a = 4r$, so $a_{fcc} = 2\sqrt{2}\,r$.
4. $\frac{\rho_{bcc}}{\rho_{fcc}} = \frac{Z_{bcc}}{Z_{fcc}}\left(\frac{a_{fcc}}{a_{bcc}}\right)^3 = \frac{2}{4}\left(\frac{2\sqrt{2}\,r\sqrt{3}}{4r}\right)^3$.
5. $\frac{a_{fcc}}{a_{bcc}} = \frac{\sqrt{6}}{2}$, so $\left(\frac{\sqrt{6}}{2}\right)^3 = \frac{6\sqrt{6}}{8}$.
6. $\frac{1}{2} \times \frac{6\sqrt{6}}{8} = \frac{3\sqrt{6}}{8} = \frac{3\sqrt{3}}{4\sqrt{2}}$, which is option $2$.

**Subtopic:** Density and Edge Length Calculations for Cubic Unit Cells · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q082_4c203638_03112026.png?v=4c20363898d5)

Publisher's solution, as printed:

![printed solution 82](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q082_c7aec14b_03112026.png?v=c7aec14bda02)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Calculation** (`calculate`) — put numbers in and get a number out
- **Concept:** Density is $ZM/(a^3N_A)$ with $a = 4r/\sqrt{3}$ for bcc and $4r/\sqrt{2}$ for fcc, so the ratio is $(2/4)(\sqrt{3}/\sqrt{2})^3 = 3\sqrt{3}/4\sqrt{2}$.
- **Trap:** **Arithmetic slip** (`arithmetic_slip`) — the number or the unit is wrong, or a step was stopped short — option 1  
  $\sqrt{3}/\sqrt{2}$ is the ratio of the two edge lengths, $a_{fcc}/a_{bcc}$, so this option is the calculation reported one step early - before the cube and before two atoms per cell are set against four.
- **Why:** This question requires a density expression built from each lattice's edge length and atom count, demonstrated by the stem's bcc-to-fcc change 'assuming molar mass and atomic radii of iron remains constant with temperature'.
<!--/ecat-->

## Q83

Chemistry · inorganic · Chemical Bonding and Molecular Structure

Consider the following species : $\mathrm{CN^{+}}$, $\mathrm{CN^{-}}$, $\mathrm{NO}$ and $\mathrm{CN}$ Which one of these will have the highest bond order?

- (1) $\mathrm{NO}$
- (2) $\mathrm{CN^{+}}$
- **(3)** $\mathrm{CN^{-}}$
- (4) $\mathrm{CN}$

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{NO}$ : $(\sigma 1s)^{2}, (\sigma^{*}1s)^{2}, (\sigma 2s)^{2}, (\sigma^{*}2s)^{2}, (\sigma 2p_{z})^{2}, (\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}, (\pi^{*}2p_{x})^{1} = (\pi^{*}2p_{y})^{0}$
2. $\mathrm{BO} = \frac{10 - 5}{2} = 2.5$
3. $\mathrm{CN^{-}}$ : $(\sigma 1s)^{2}, (\sigma^{*}1s)^{2}, (\sigma 2s)^{2}, (\sigma^{*}2s)^{2}, (\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}, (\sigma 2p_{z})^{2}$
4. $\mathrm{BO} = \frac{10 - 4}{2} = 3$
5. $\mathrm{CN}$ : $(\sigma 1s)^{2}, (\sigma^{*}1s)^{2}, (\sigma 2s)^{2}, (\sigma^{*}2s)^{2}, (\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}, (\sigma 2p_{z})^{1}$
6. $\mathrm{BO} = \frac{9 - 4}{2} = 2.5$
7. $\mathrm{CN^{+}}$ : $(\sigma 1s)^{2}, (\sigma^{*}1s)^{2}, (\sigma 2s)^{2}, (\sigma^{*}2s)^{2}, (\pi 2p_{x})^{2} = (\pi 2p_{y})^{2}$
8. $\mathrm{BO} = \frac{8 - 4}{2} = 2$
9. Hence, option(3) should be the right answer.

**Solved independently** (answer withheld)

1. Count electrons: $\mathrm{C}=6$, $\mathrm{N}=7$, $\mathrm{O}=8$; so $\mathrm{CN^{+}}=12$, $\mathrm{CN}=13$, $\mathrm{CN^{-}}=14$, $\mathrm{NO}=15$ electrons.
2. For $\mathrm{CN^{+}}$ (12 e$^-$): $\sigma1s^2\,\sigma^*1s^2\,\sigma2s^2\,\sigma^*2s^2\,\pi2p^4$, so $BO = \frac{8-4}{2} = 2$.
3. For $\mathrm{CN}$ (13 e$^-$): add $\sigma2p^1$, so $BO = \frac{9-4}{2} = 2.5$.
4. For $\mathrm{CN^{-}}$ (14 e$^-$, isoelectronic with $\mathrm{N_2}$): $\sigma2p^2$, so $BO = \frac{10-4}{2} = 3$.
5. For $\mathrm{NO}$ (15 e$^-$): one electron in $\pi^*2p$, so $BO = \frac{10-5}{2} = 2.5$.
6. Highest bond order is $3$ for $\mathrm{CN^{-}}$, which is option $3$.

**Subtopic:** Molecular Orbital Theory · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 20)

![printed question 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q083_d697eeaf_03112026.png?v=d697eeafda3f)

Publisher's solution, as printed:

![printed solution 83](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q083_683bff58_03112026.png?v=683bff586014)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Bond order from molecular-orbital filling: 14 electrons, as in $\mathrm{CN^-}$ and $\mathrm{N_2}$, give a bond order of 3, and a fifteenth electron enters an antibonding $\pi^*$, which is why NO falls back to 2.5.
- **Trap:** **Formula misused** (`formula_misused`) — the right formula with a wrong power, a dropped term or the wrong quantity — option 1  
  Ranking by total electron count rather than by $(N_b - N_a)/2$ works from 12 up to 14 and then breaks, because the fifteenth electron in NO goes into an antibonding orbital.
- **Why:** This question requires bond orders built by molecular-orbital filling for four related species, demonstrated by the stem listing '$\mathrm{CN^+}$, $\mathrm{CN^-}$, NO and CN' and asking which has the highest.
<!--/ecat-->

## Q84

Chemistry · physical · Structure of Atom

Which one is a wrong statement?

- (1) Total orbital angular momentum of electron in 's' orbital is equal to zero
- **(2)** ![printed figure: orbital-box diagram of the N atom: $1s^{2}$ (↑↓), $2s^{2}$ (↑↓), $2p_{x}^{1}$ (↑), $2p_{y}^{1}$ (↑), $2p_{z}^{1}$ (↓)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q084_option_2_27d12ec5_03112026.svg?v=27d12ec504ae) *orbital-box diagram of the N atom: $1s^{2}$ [↑↓], $2s^{2}$ [↑↓], $2p_{x}^{1}$ [↑], $2p_{y}^{1}$ [↑], $2p_{z}^{1}$ [↓]* — The electronic configuration of N atom is
- (3) An orbital is designated by three quantum numbers while an electron in an atom is designated by four quantum numbers
- (4) The value of $m$ for $\mathrm{d_{z}2}$ is zero

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. According to Hund's Rule of maximum multiplicity, the correct electronic configuration of $\mathrm{N}$-atom is

![printed figure: orbital-box diagram: $1s^{2}$ (↑↓), $2s^{2}$ (↑↓), $2p^{3}$ (↑)(↑)(↑)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q084_sol_1_7f9464b3_03112026.svg?v=7f9464b398bb)

*orbital-box diagram: $1s^{2}$ [↑↓], $2s^{2}$ [↑↓], $2p^{3}$ [↑][↑][↑]*

2. OR

![printed figure: orbital-box diagram: $1s^{2}$ (↑↓), $2s^{2}$ (↑↓), $2p^{3}$ (↓)(↓)(↓)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q084_sol_2_b591b177_03112026.svg?v=b591b177e2bd)

*orbital-box diagram: $1s^{2}$ [↑↓], $2s^{2}$ [↑↓], $2p^{3}$ [↓][↓][↓]*

3. $\therefore$ Option (2) violates Hund's Rule.

**Solved independently** (answer withheld)

1. For an $s$ orbital $l = 0$, so orbital angular momentum $= \sqrt{l(l+1)}\,\frac{h}{2\pi} = 0$; statement 1 is correct.
2. N ($Z = 7$) is $1s^2\,2s^2\,2p^3$, and by Hund's rule the three $2p$ electrons occupy $2p_x^1\,2p_y^1\,2p_z^1$ with parallel spins ($\uparrow\,\uparrow\,\uparrow$).
3. The drawn configuration shows $2p_x \uparrow,\ 2p_y \uparrow,\ 2p_z \downarrow$, which breaks Hund's rule, so statement 2 is wrong.
4. An orbital is fixed by $n, l, m_l$; an electron also needs $m_s$, giving four quantum numbers; statement 3 is correct.
5. The $d_{z^2}$ orbital corresponds to $m_l = 0$; statement 4 is correct.
6. The only wrong statement is option $2$.

**Subtopic:** Filling of Orbitals in Atom · **Difficulty:** medium (4 steps)

**Printed in the booklet** (page 21)

![printed question 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q084_4a6d76d2_03112026.png?v=4a6d76d20748)

Publisher's solution, as printed:

![printed solution 84](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q084_22876693_03112026.png?v=228766933d65)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Quantum-number bookkeeping: $\ell = 0$ for an s orbital leaves zero orbital angular momentum, an orbital takes three quantum numbers and an electron four, and $d_{z^2}$ is the $m = 0$ member of the d set.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Option 2, the option the paper keys, is stored as 'The electronic configuration of N atom is' with the configuration itself missing, so the statement that is supposed to be the wrong one cannot be read and no route to any option can be checked against it.
- **Why:** This question requires four quantum-number statements graded for correctness, demonstrated by the stem 'Which one is a wrong statement?'; the keyed option's content is absent from this record.
- **Note:** Option 2 is truncated: whatever followed 'is' - a configuration or an orbital-box diagram - was not captured, and it is the keyed option. Options 1, 3 and 4 are readable and each states a correct quantum-number fact, so the error must lie in the missing text. A reviewer holding the paper should check whether the printed configuration breaks Hund's rule or the Pauli principle, which is where the trap would sit, and whether any of the three true statements could be misread as the wrong one.
<!--/ecat-->

## Q85

Chemistry · inorganic · Environmental Chemistry

Which oxide of nitrogen is not a common pollutant introduced into the atmosphere both due to natural and human activity?

- **(1)** $\mathrm{N_2O_5}$
- (2) $\mathrm{N_2O}$
- (3) $\mathrm{NO_2}$
- (4) $\mathrm{NO}$

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Fact

**Solved independently** (answer withheld)

1. $\mathrm{NO}$ and $\mathrm{NO_2}$ are common nitrogen-oxide pollutants (lightning and combustion), and $\mathrm{N_2O}$ comes from natural soil processes and from fertiliser use, so all three come from both natural and human activity; $\mathrm{N_2O_5}$ is not a common atmospheric pollutant, which is option $1$.

**Subtopic:** Air Pollution · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q085_f2355293_03112026.png?v=f23552934b11)

Publisher's solution, as printed:

![printed solution 85](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q085_0bcd7345_03112026.png?v=0bcd73459cf5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The nitrogen oxides printed as atmospheric pollutants from both natural and human sources are NO, $\mathrm{NO_2}$ and $\mathrm{N_2O}$; $\mathrm{N_2O_5}$ is not among them.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  $\mathrm{N_2O}$ appears in the greenhouse-gas list rather than in the oxides-of-nitrogen paragraph on air pollution, so revising that paragraph, where NO and $\mathrm{NO_2}$ are named, leaves $\mathrm{N_2O}$ looking like the oxide left out.
- **Why:** This question requires membership of a stated pollutant list, demonstrated by the stem's 'both due to natural and human activity' and by the keyed $\mathrm{N_2O_5}$, for which no source is printed.
<!--/ecat-->

## Q86

Chemistry · organic · Hydrocarbons

Hydrocarbon (A) reacts with bromine by substitution to form an alkyl bromide which by Wurtz reaction is converted to gaseous hydrocarbon containing less than four carbon atoms. (A) is

- (1) $\mathrm{CH \equiv CH}$
- (2) $\mathrm{CH_3 - CH_3}$
- (3) $\mathrm{CH_2 = CH_2}$
- **(4)** $\mathrm{CH_4}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: methane (A) →($\ce{Br2}$/hν) bromomethane →(Na/dry ether, Wurtz reaction) ethane](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q086_sol_1_ebb83f07_03112026.svg?v=ebb83f071225)

*methane (A) →[$\ce{Br2}$/hν] bromomethane →[Na/dry ether, Wurtz reaction] ethane*

![drawn: methane (A) →($\ce{Br2}$/hν) bromomethane →(Na/dry ether, Wurtz reaction) ethane](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q086_solution_1_e0ad5cb2_03112026.svg?v=e0ad5cb23220)  
*drawn on the booklet's geometry, checked against its SMILES*

1. Hence the correct option is (4)

**Solved independently** (answer withheld)

1. Ethene ($\mathrm{CH_2=CH_2}$) and ethyne ($\mathrm{CH\equiv CH}$) react with $\mathrm{Br_2}$ by addition, not substitution, so options $1$ and $3$ are ruled out.
2. For ethane: $\mathrm{CH_3CH_3 + Br_2 \xrightarrow{h\nu} CH_3CH_2Br + HBr}$.
3. Wurtz on it: $\mathrm{2CH_3CH_2Br + 2Na \xrightarrow{dry\ ether} CH_3CH_2CH_2CH_3 + 2NaBr}$, butane has $4$ carbons, not fewer than four, so option $2$ is ruled out.
4. For methane: $\mathrm{CH_4 + Br_2 \xrightarrow{h\nu} CH_3Br + HBr}$.
5. Wurtz on it: $\mathrm{2CH_3Br + 2Na \xrightarrow{dry\ ether} CH_3CH_3 + 2NaBr}$, ethane is a gas with $2 < 4$ carbons, so (A) is $\mathrm{CH_4}$, option $4$.

**Subtopic:** Preparation of Alkane, Chemical Properties of Alkane · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q086_87dc2a9d_03112026.png?v=87dc2a9d889c)

Publisher's solution, as printed:

![printed solution 86](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q086_79b61aba_03112026.png?v=79b61abafe83)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Only an alkane substitutes bromine, and Wurtz coupling then doubles the carbon count: $\mathrm{CH_4 \to CH_3Br \to C_2H_6}$ is the one route here that both substitutes and stays under four carbons.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 2  
  Ethane does substitute bromine and its Wurtz product, n-butane, is a gas, so the option passes everything in the stem except 'less than four carbon atoms' - the coupling takes two carbons to four.
- **Why:** This question requires a two-step route read back to its starting hydrocarbon, demonstrated by the stem's 'by substitution' and 'gaseous hydrocarbon containing less than four carbon atoms'.
<!--/ecat-->

## Q87

Chemistry · organic · Alcohols, Phenols and Ethers

The compound A on treatment with $\mathrm{Na}$ gives B, and with $\mathrm{PCl_5}$ gives C. B and C react together to give diethyl ether. A, B and C are in the order

- (1) $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_6}$, $\mathrm{C_2H_5Cl}$
- (2) $\mathrm{C_2H_5Cl}$, $\mathrm{C_2H_6}$, $\mathrm{C_2H_5OH}$
- (3) $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5Cl}$, $\mathrm{C_2H_5ONa}$
- **(4)** $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_5Cl}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: ethanol ($\ce{C2H5OH}$) (A) →(Na) sodium ethoxide ($\ce{C2H5O^- Na^+}$) (B); A →($\ce{PCl5}$) chloroethane ($\ce{C2H5Cl}$) (C)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q087_sol_1_ac668fc8_03112026.svg?v=ac668fc87222)

*ethanol ($\ce{C2H5OH}$) (A) →[Na] sodium ethoxide ($\ce{C2H5O^- Na^+}$) (B); A →[$\ce{PCl5}$] chloroethane ($\ce{C2H5Cl}$) (C)*

![drawn: ethanol ($\ce{C2H5OH}$) (A) →(Na) sodium ethoxide ($\ce{C2H5O^- Na^+}$) (B); A →($\ce{PCl5}$) chloroethane ($\ce{C2H5Cl}$) (C)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q087_solution_1_27596ceb_03112026.svg?v=27596cebf6d9)  
*drawn by RDKit (code/lib/chem_cards.py)*

1. $\underset{(\mathrm{B})}{\mathrm{C_2H_5O^{-}\,Na^{+}}} + \underset{(\mathrm{C})}{\mathrm{C_2H_5Cl}} \xrightarrow{\mathrm{S_N2}} \mathrm{C_2H_5OC_2H_5}$
2. So the correct option is (4)

**Solved independently** (answer withheld)

1. Diethyl ether $\mathrm{C_2H_5OC_2H_5}$ formed from B and C points to Williamson synthesis, needing an alkoxide and an alkyl halide, so A is $\mathrm{C_2H_5OH}$.
2. $2\mathrm{C_2H_5OH} + 2\mathrm{Na} \rightarrow 2\mathrm{C_2H_5ONa} + \mathrm{H_2}$, so B is $\mathrm{C_2H_5ONa}$.
3. $\mathrm{C_2H_5OH} + \mathrm{PCl_5} \rightarrow \mathrm{C_2H_5Cl} + \mathrm{POCl_3} + \mathrm{HCl}$, so C is $\mathrm{C_2H_5Cl}$.
4. $\mathrm{C_2H_5ONa} + \mathrm{C_2H_5Cl} \rightarrow \mathrm{C_2H_5OC_2H_5} + \mathrm{NaCl}$, confirming the order $\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_5Cl}$, which is option $4$.

**Subtopic:** Preparation of Ethers by Williamson Ether Synthesis, Reactions of Alcohols · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 21)

![printed question 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q087_f0996ac1_03112026.png?v=f0996ac16d91)

Publisher's solution, as printed:

![printed solution 87](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q087_e65d6297_03112026.png?v=e65d6297aea7)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Williamson synthesis: sodium turns ethanol into sodium ethoxide, $\mathrm{PCl_5}$ turns it into ethyl chloride, and the alkoxide and the halide together give diethyl ether.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  A and C are both right in this option and only B fails: sodium is remembered as the reagent that yields a hydrocarbon, so ethane is written where the alkoxide belongs.
- **Why:** This question requires three compounds assigned to three stated reagent steps at once, demonstrated by the stem's 'A, B and C are in the order' and the keyed '$\mathrm{C_2H_5OH}$, $\mathrm{C_2H_5ONa}$, $\mathrm{C_2H_5Cl}$'.
- **Note:** The pattern returned `plain_mcq`, but the stem asks for three compounds together and each option supplies all three - the retired `multi_part_respectively` shape, which `category_retired.qtype` maps to `two_part`.
<!--/ecat-->

## Q88

Chemistry · organic · Hydrocarbons

The compound $\mathrm{C_7H_8}$ undergoes the following reactions: $\mathrm{C_7H_8} \xrightarrow{\mathrm{3Cl_2}/\Delta} \mathrm{A} \xrightarrow{\mathrm{Br_2}/\mathrm{Fe}} \mathrm{B} \xrightarrow{\mathrm{Zn/HCl}} \mathrm{C}$ The product 'C' is

- **(1)** m-bromotoluene
- (2) 3-bromo-2,4,6-trichlorotoluene
- (3) o-bromotoluene
- (4) p-bromotoluene

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

![printed figure: toluene ($\ce{C7H8}$) →($\ce{3Cl2}$, Δ) (trichloromethyl)benzene (A) →($\ce{Br2}$, Fe) 1-bromo-3-(trichloromethyl)benzene (B); B →(Zn, HCl) 1-bromo-3-methylbenzene (C)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q088_sol_1_ee9b2658_03112026.svg?v=ee9b2658296b)

*toluene ($\ce{C7H8}$) →[$\ce{3Cl2}$, Δ] (trichloromethyl)benzene (A) →[$\ce{Br2}$, Fe] 1-bromo-3-(trichloromethyl)benzene (B); B →[Zn, HCl] 1-bromo-3-methylbenzene (C)*

![drawn: toluene ($\ce{C7H8}$) →($\ce{3Cl2}$, Δ) (trichloromethyl)benzene (A) →($\ce{Br2}$, Fe) 1-bromo-3-(trichloromethyl)benzene (B); B →(Zn, HCl) 1-bromo-3-methylbenzene (C)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_drawn/q088_solution_1_aee67273_03112026.svg?v=aee67273bb09)  
*drawn on the booklet's geometry, checked against its SMILES*

1. So, the correct option is (1)

**Solved independently** (answer withheld)

1. $\mathrm{C_7H_8}$ is toluene, $\mathrm{C_6H_5CH_3}$.
2. With $\mathrm{3Cl_2}$ and heat (no catalyst), free-radical side-chain chlorination replaces all three methyl H atoms: $\mathrm{A} = \mathrm{C_6H_5CCl_3}$ (benzotrichloride).
3. The $-\mathrm{CCl_3}$ group is strongly electron-withdrawing, so it deactivates the ring and is meta-directing.
4. Electrophilic bromination with $\mathrm{Br_2/Fe}$ therefore gives $\mathrm{B} = m\text{-}\mathrm{BrC_6H_4CCl_3}$.
5. $\mathrm{Zn/HCl}$ reduces $-\mathrm{CCl_3}$ back to $-\mathrm{CH_3}$, so $\mathrm{C} = m\text{-}\mathrm{BrC_6H_4CH_3}$, m-bromotoluene, which is option $1$.

**Subtopic:** Chemical and Physical Properties of Benzene · **Difficulty:** hard (4 steps)

**Printed in the booklet** (page 22)

![printed question 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q088_48fdd768_03112026.png?v=48fdd7685e1c)

Publisher's solution, as printed:

![printed solution 88](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q088_9acd1760_03112026.png?v=9acd1760a9ef)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** $\mathrm{Cl_2}$ with heat and no catalyst attacks toluene's methyl group; the resulting $-\mathrm{CCl_3}$ is meta-directing for the bromination, and $\mathrm{Zn/HCl}$ then restores the methyl, giving m-bromotoluene.
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 4  
  Taking the first arrow to leave the side chain untouched keeps $-\mathrm{CH_3}$ as the director, and an ortho/para-directing methyl sends the bromine to the para position instead of the meta one.
- **Why:** This question requires three stated conditions applied in sequence to one ring, demonstrated by the printed scheme '$\mathrm{3Cl_2}/\Delta$' then '$\mathrm{Br_2/Fe}$' then '$\mathrm{Zn/HCl}$' with the keyed m-bromotoluene.
<!--/ecat-->

## Q89

Chemistry · organic · Alcohols, Phenols and Ethers

Identify the major products P, Q and R in the following sequence of reactions:

![printed figure: benzene + 1-chloropropane ($\ce{CH3CH2CH2Cl}$) →(Anhydrous $\ce{AlCl3}$) P →((i) $\ce{O2}$ (ii) $\ce{H3O+}$/Δ) Q + R](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q089_b40dd437_03112026.svg?v=b40dd4378264)

*benzene + 1-chloropropane ($\ce{CH3CH2CH2Cl}$) →[Anhydrous $\ce{AlCl3}$] P →[(i) $\ce{O2}$ (ii) $\ce{H3O+}$/Δ] Q + R*

Structures: benzene `c1ccccc1`; 1-chloropropane `CCCCl`

- (1) propylbenzene `CCCc1ccccc1`; benzaldehyde `O=Cc1ccccc1`; ethanol `CCO`
- (2) isopropylbenzene `CC(C)c1ccccc1`; phenol `Oc1ccccc1`; propan-2-ol `CC(C)O`
- (3) propylbenzene `CCCc1ccccc1`; benzaldehyde `O=Cc1ccccc1`; benzoic acid `O=C(O)c1ccccc1`
- **(4)** isopropylbenzene `CC(C)c1ccccc1`; phenol `Oc1ccccc1`; acetone `CC(C)=O`

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

![printed figure: 1-chloropropane ($\ce{CH3CH2CH2-Cl}$) + aluminium chloride ($\ce{AlCl3}$, drawn with three Al-Cl bonds) → propyl ($\ce{CH3CH2CH2}$, δ+) ··· Cl ··· aluminium chloride ($\ce{AlCl3}$, δ-) (Incipient carbocation) →(1, 2-H Shift) propan-2-yl ($\ce{CH3-CH-CH3}$, δ+ on CH) ··· Cl ··· aluminium chloride ($\ce{AlCl3}$, δ-)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q089_sol_1_48cb7eac_03112026.svg?v=48cb7eac25e9)

*1-chloropropane ($\ce{CH3CH2CH2-Cl}$) + aluminium chloride ($\ce{AlCl3}$, drawn with three Al-Cl bonds) → propyl ($\ce{CH3CH2CH2}$, δ+) ··· Cl ··· aluminium chloride ($\ce{AlCl3}$, δ-) (Incipient carbocation) →[1, 2-H Shift] propan-2-yl ($\ce{CH3-CH-CH3}$, δ+ on CH) ··· Cl ··· aluminium chloride ($\ce{AlCl3}$, δ-)*

1. Now,

![printed figure: benzene →($\ce{CH3-CH^+-CH3}$) isopropylbenzene (P) →($\ce{O2}$) (2-hydroperoxypropan-2-yl)benzene →($\ce{H+/H2O}$, Hydroperoxide Rearrangement) phenol (Q) + acetone (R)](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/figures_agent/q089_sol_2_2da1268e_03112026.svg?v=2da1268ec6da)

*benzene →[$\ce{CH3-CH^+-CH3}$] isopropylbenzene (P) →[$\ce{O2}$] (2-hydroperoxypropan-2-yl)benzene →[$\ce{H+/H2O}$, Hydroperoxide Rearrangement] phenol (Q) + acetone (R)*


**Solved independently** (answer withheld)

1. Anhydrous $\mathrm{AlCl_3}$ ionises $\mathrm{CH_3CH_2CH_2Cl}$ to give the primary carbocation $\mathrm{CH_3CH_2\overset{+}{C}H_2}$.
2. A 1,2-hydride shift converts it to the more stable secondary carbocation $\mathrm{(CH_3)_2\overset{+}{C}H}$.
3. Electrophilic substitution of benzene by $\mathrm{(CH_3)_2\overset{+}{C}H}$ gives $\mathrm{P} = \mathrm{C_6H_5CH(CH_3)_2}$ (cumene).
4. Air oxidation of cumene with $\mathrm{O_2}$ gives cumene hydroperoxide $\mathrm{C_6H_5C(CH_3)_2OOH}$.
5. Acid hydrolysis with $\mathrm{H_3O^+}/\Delta$ gives $\mathrm{Q} = \mathrm{C_6H_5OH}$ (phenol) and $\mathrm{R} = \mathrm{CH_3COCH_3}$ (acetone), which is option $4$.

**Subtopic:** Preparation of Phenols · **Difficulty:** hard (3 steps)

**Printed in the booklet** (page 22)

![printed question 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q089_0958dc86_03112026.png?v=0958dc86961d)

Publisher's solution, as printed:

![printed solution 89](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q089_bea60aa6_03112026.png?v=bea60aa6b6d3)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Reaction outcome** (`reaction`) — what a reaction gives, or the reagent it needs
- **Concept:** Friedel-Crafts alkylation of benzene with 1-chloropropane rearranges to cumene, and cumene with $\mathrm{O_2}$ followed by dilute acid gives phenol and acetone.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All four options are drawn structures and this packet carried only the question scheme, so there is nothing to compare between options and no route can be named or audited.
- **Why:** This question requires three products identified from a printed reaction sequence, demonstrated by the stem 'Identify the major products P, Q and R in the following sequence of reactions'; the option structures were not supplied to this step.
- **Note:** options_en holds four empty strings while the figure record carries only the question scheme; its drawn-check message names 'figure option_3' and a structure read as benzoic acid, so the option drawings exist upstream and were simply not passed to this step. The paper is intact, so this is not recorded as source damage (section 5.0). A reviewer holding the options should check two mechanisms: the n-propyl chain rearranging to isopropyl under $\mathrm{AlCl_3}$, so that P is cumene rather than n-propylbenzene, and the cumene-hydroperoxide route giving phenol plus acetone, with benzoic acid - which the figure note reports among the printed option structures - being the side-chain-oxidation answer to a different question. The shape is recorded from the stem, which asks for three products at once; the pattern's `arrange_in_order` reading appears to come from the word 'sequence', which here describes the reactions and not the answer.
<!--/ecat-->

## Q90

Chemistry · organic · Biomolecules

Which of the following compounds can form a zwitterion?

- (1) Aniline
- (2) Benzoic acid
- (3) Acetanilide
- **(4)** Glycine

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\underset{\substack{\downarrow \\ \mathrm{p}K_{a} = 9.60}}{\mathrm{H_3\overset{\oplus}{N}}}\mathrm{\,-\,CH_2\,-\,}\underset{\substack{\downarrow \\ \mathrm{p}K_{a} = 2.34}}{\mathrm{COOH}} \rightleftharpoons \mathrm{H_3\overset{\oplus}{N}\,-\,CH_2\,-\,COO^{-}}$ (Zwitterion form)
2. $\rightleftharpoons \mathrm{H_2N\,-\,CH_2\,-\,COO^{-}}$

**Solved independently** (answer withheld)

1. A zwitterion needs an acidic group and a basic group in the same molecule, so that a proton moves from one to the other.
2. Glycine has $-\mathrm{NH_2}$ and $-\mathrm{COOH}$: $\mathrm{H_2N{-}CH_2{-}COOH} \rightleftharpoons \mathrm{H_3\overset{+}{N}{-}CH_2{-}COO^-}$, a zwitterion.
3. Aniline ($\mathrm{C_6H_5NH_2}$) has only a basic group, benzoic acid ($\mathrm{C_6H_5COOH}$) only an acidic group, and acetanilide ($\mathrm{C_6H_5NHCOCH_3}$) has a non-basic amide N and no acidic group, so none of them forms a zwitterion.
4. So the answer is glycine, option $4$.

**Subtopic:** Proteins Classification and Structure · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 22)

![printed question 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q090_d5ccf31d_03112026.png?v=d5ccf31d7598)

Publisher's solution, as printed:

![printed solution 90](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q090_ad702485_03112026.png?v=ad702485637d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A zwitterion needs an acidic and a basic group on the same molecule: glycine's $-\mathrm{COOH}$ hands its proton to its own $-\mathrm{NH_2}$.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The zwitterion is introduced as the carboxyl group losing a proton, so holding that half of the sentence lands on the only carboxylic acid in the list, with no question asked about where the proton goes.
- **Why:** This question requires the two-group requirement for a zwitterion applied to four named compounds, demonstrated by the keyed 'Glycine' being the only option that carries both $-\mathrm{COOH}$ and $-\mathrm{NH_2}$.
<!--/ecat-->

## Q91

Biology · botany · Plant Kingdom

Which of the following statements is correct?

- **(1)** Ovules are not enclosed by ovary wall in gymnosperms
- (2) Horsetails are gymnosperms
- (3) Selaginella is heterosporous, while Salvinia is homosporous
- (4) Stems are usually unbranched in both Cycas and Cedrus

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Gymnosperms have naked ovule.
2. Called phanerogams without womb/ovary

**Solved independently** (answer withheld)

1. Gymnosperms have naked ovules, not enclosed by an ovary wall, so option $1$ is correct; horsetails ($Equisetum$) are pteridophytes, $Salvinia$ is heterosporous like $Selaginella$, and $Cedrus$ has branched stems, so options $2$, $3$ and $4$ are false.

**Subtopic:** Gymnosperms · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q091_6087e5d8_03112026.png?v=6087e5d86eab)

Publisher's solution, as printed:

![printed solution 91](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q091_f4e22b37_03112026.png?v=f4e22b379a79)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gymnosperms bear naked ovules with no ovary wall around them; Selaginella and Salvinia are both heterosporous, and gymnosperm stems may be unbranched as in Cycas or branched as in Cedrus and Pinus
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The first half is the line NCERT prints — Selaginella is heterosporous — and the sentence then denies the same property to Salvinia, which the same NCERT sentence names as the other heterosporous example.
- **Why:** This question requires each printed statement graded against the lines NCERT states about these groups, demonstrated by 'Which of the following statements is correct?' over four standalone claims, two of which ('Selaginella is heterosporous, while Salvinia is homosporous' and 'Stems are usually unbranched in both Cycas and Cedrus') pair two genera inside one sentence.
- **Note:** E1_question_type is plain_mcq from the 16 default, i.e. no pattern fired. The stem reads 'Which of the following statements is correct?' and each option is a complete claim, so the shape recorded here is statements.
<!--/ecat-->

## Q92

Biology · botany · Morphology of Flowering Plants

Pneumatophores occur in

- **(1)** Halophytes
- (2) Carnivorous plants
- (3) Free-floating hydrophytes
- (4) Submerged hydrophytes

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Halophytes like mangrooves have pneumatophores.
2. Apogeotropic (–vely geotropic) roots having lenticels called pneumathodes to uptake $\mathrm{O_2}$.

**Solved independently** (answer withheld)

1. Pneumatophores are respiratory roots that grow vertically upward out of the soil to take in oxygen, as seen in mangroves such as $Rhizophora$ growing in saline swamps; mangroves are halophytes, which is option $1$.

**Subtopic:** The Root · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 23)

![printed question 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q092_f1319445_03112026.png?v=f13194454236)

Publisher's solution, as printed:

![printed solution 92](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q092_50c8af8f_03112026.png?v=50c8af8fb9ea)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pneumatophores are the vertical breathing roots of mangroves such as Rhizophora, plants of saline swampy ground, i.e. halophytes
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Holding only 'pneumatophores are roots that come up for oxygen', a student picks the habitat class whose plants are furthest from air, the submerged water plants, instead of the salt-marsh class NCERT actually ties the root to.
- **Why:** This question requires the plant group NCERT attaches to pneumatophores, demonstrated by the stem 'Pneumatophores occur in' followed by four bare habitat categories with no criterion printed to apply.
- **Note:** On the nearby_fact against look_alike_term test: halophyte and hydrophyte do resemble each other, but replacing them with unlike wordings ('salt-marsh plants', 'wholly submerged water plants') leaves the oxygen route to option 4 intact, so adjacency of the habitat classes is doing the work, not the likeness of the names.
<!--/ecat-->

## Q93

Biology · botany · Morphology of Flowering Plants

Sweet potato is a modified

- (1) Stem
- (2) Tap root
- **(3)** Adventitious root
- (4) Rhizome

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Sweet potato is a modified adventitious root for storage of food
2. Rhizomes are underground modified stem
3. Tap root is primary root directly elongated from the redicle

**Solved independently** (answer withheld)

1. Sweet potato's edible part is a swollen adventitious root modified for food storage, unlike carrot (tap root) or potato (stem tuber), which is option $3$.

**Subtopic:** The Root · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q093_3bbdf082_03112026.png?v=3bbdf0824f26)

Publisher's solution, as printed:

![printed solution 93](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q093_cebbf112_03112026.png?v=cebbf112522f)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The sweet potato stores food in a swollen adventitious root, whereas the potato's tuber is a modified stem
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The potato is the textbook's example of a storage organ that is a modified stem, and 'sweet potato' differs from it by one word, so the stem answer is carried across to a plant whose swollen organ is a root.
- **Why:** This question requires the organ NCERT names for the sweet potato's food store, demonstrated by the stem 'Sweet potato is a modified' with two root options and two stem options and no criterion printed to decide between them.
<!--/ecat-->

## Q94

Biology · botany · Anatomy of Flowering Plants

Plants having little or no secondary growth are

- **(1)** Grasses
- (2) Conifers
- (3) Deciduous angiosperms
- (4) Cycads

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Grasses are monocots and monocots usually do not have secondary growth.
2. Palm like monocots have anomalous secondary growth.

**Solved independently** (answer withheld)

1. Grasses are monocots, which have no vascular cambium, so they show little or no secondary growth; conifers, cycads and deciduous dicot trees all have a cambium and do grow secondarily, so the answer is option $1$.

**Subtopic:** Secondary Growth · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q094_79280f83_03112026.png?v=79280f839609)

Publisher's solution, as printed:

![printed solution 94](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q094_5552fbf2_03112026.png?v=5552fbf26431)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Secondary growth needs a vascular cambium, which monocots such as grasses do not form, while conifers, cycads and dicot trees all have one
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The three wrong options are the groups whose wood is the textbook's own illustration of secondary growth, so no prepared route reaches them. I checked each: 'little or no' is the only word in the stem that could point elsewhere, and conifer timber, the annual rings of deciduous dicot trees and the cycad trunk are all presented as products of a cambium; none of the three names resembles 'grasses'; and none of them is printed beside the monocot line that says the vascular bundles are closed.
- **Why:** This question requires the group NCERT states lacks a vascular cambium, demonstrated by the stem 'Plants having little or no secondary growth are' with four plant groups and no criterion printed to apply.
- **Note:** The mechanism a reviewer may want to test, which I could not support from the printed words: Cycas is described with an unbranched stem and a crown of pinnate leaves, so a student grouping it with palms by habit might read 'little' as written for cycads. Nothing in the stem or options carries that reading, so it is recorded here rather than tagged.
<!--/ecat-->

## Q95

Biology · botany · Anatomy of Flowering Plants

Casparian strips occur in

- (1) Epidermis
- (2) Cortex
- (3) Pericycle
- **(4)** Endodermi

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Endodermis have casparian strip on radial and inner tangential wall.
2. It is suberin rich.

**Solved independently** (answer withheld)

1. Casparian strips are bands of suberin on the tangential and radial walls of the endodermal cells of the root, so they occur in the endodermis, which is option $4$.

**Subtopic:** Dicotyledonous and Monocotyledonous Root · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 95](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q095_f7507d41_03112026.png?v=f7507d414959)

Publisher's solution, as printed:

![printed solution 95](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q095_9b89534a_03112026.png?v=9b89534a08b6)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Casparian strip is the suberised band in endodermal cell walls of the root, which blocks the apoplastic path and forces water and ions through the cell membranes
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Epidermis and endodermis differ by a prefix, so a student holding only the '-dermis' ending takes the outer layer for the inner one.
- **Why:** This question requires the root layer NCERT names for the Casparian strip, demonstrated by the stem 'Casparian strips occur in' with four layers of the same root section as options.
- **Note:** Option 4 is stored as 'Endodermi' with the final s missing. The word is still unambiguous and the printed answer line reads Answer (4), so the question is tagged as printed; the spelling needs a repair pass. On the trap axis I applied the swap test: replacing epidermis and endodermis with unlike wordings kills the route to option 1, so the likeness is doing the work there, while the route to option 3 survives any renaming because it comes from the layer's position in the sequence.
<!--/ecat-->

## Q96

Biology · botany · Anatomy of Flowering Plants

Secondary xylem and phloem in dicot stem are produced by

- (1) Apical meristems
- (2) Phellogen
- **(3)** Vascular cambium
- (4) Axillary meristems

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Vascular cambium is partially secondary
2. Form secondary xylem towards its inside and secondary phloem towards outsides.
3. $4 - 10$ times more secondary xylem is produced than secondary phloem.

**Solved independently** (answer withheld)

1. The vascular cambium (intrafascicular plus interfascicular cambium ring) divides to form secondary xylem on the inner side and secondary phloem on the outer side, so the answer is option $3$.

**Subtopic:** Secondary Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 23)

![printed question 96](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q096_75e5ac39_03112026.png?v=75e5ac3911c3)

Publisher's solution, as printed:

![printed solution 96](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q096_5e984b84_03112026.png?v=5e984b84aa7e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Secondary xylem and phloem come from the vascular cambium; the cork cambium or phellogen makes cork outwards and secondary cortex inwards
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Phellogen is the other cambium printed in the same secondary-growth account, so a student who knows secondary growth is run by cambia but has not split their products picks it for the secondary vascular tissue.
- **Why:** This question requires the meristem NCERT credits with the secondary vascular tissues, demonstrated by the stem 'Secondary xylem and phloem in dicot stem are produced by' with four named meristems as options.
- **Note:** Swap test applied: phellogen and vascular cambium are already unlike as words, yet the route to option 2 survives, because what carries it is phellogen being printed in the same secondary-growth passage. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q97

Biology · botany · Biological Classification

Select the wrong statement :

- (1) Cell wall is present in members of Fungi and Plantae
- **(2)** Pseudopodia are locomotory and feeding structures in Sporozoans
- (3) Mushrooms belong to Basidiomycetes
- (4) Mitochondria are the powerhouse of the cell in all kingdoms except Monera

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Pseudopodia are locomotory structures in sarcodines (Amoeboid)

**Solved independently** (answer withheld)

1. Option $1$: Fungi (chitin) and Plantae (cellulose) both have a cell wall, so it is true.
2. Option $3$: Mushrooms (e.g. $Agaricus$) belong to Basidiomycetes, so it is true.
3. Option $4$: Monera are prokaryotes and lack mitochondria, while the other kingdoms have them, so it is true.
4. Option $2$: Pseudopodia occur in amoeboid protozoans (Sarcodines); Sporozoans have no locomotory structures, so it is the wrong statement, which is option $2$.

**Subtopic:** Protozoans · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q097_1a090b46_03112026.png?v=1a090b467886)

Publisher's solution, as printed:

![printed solution 97](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q097_cf55ace6_03112026.png?v=cf55ace6be09)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pseudopodia belong to the amoeboid protozoans; sporozoans are the protozoan group with an infectious spore-like stage and no pseudopodia
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  The sentence reads as a list of the kingdoms that have cell walls, and a student checking it for completeness can name two it leaves out — bacteria and diatoms — so the omission is read as the error; what the sentence actually claims is that a wall is present in members of these two, not only in them.
- **Why:** This question requires the structures NCERT assigns to each protozoan group, demonstrated by 'Select the wrong statement :' and by the false option moving pseudopodia, the amoeboid group's structures, to 'Sporozoans'.
- **Note:** E1 recorded statement_options; the stem says 'statement' and each option is a full claim, so the shape here is statements.
<!--/ecat-->

## Q98

Biology · both · Molecular Basis of Inheritance

The experimental proof for semiconservative replication of DNA was first shown in a

- (1) Fungus
- (2) Plant
- **(3)** Bacterium
- (4) Virus

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Semi-conservative DNA replication was first shown in Bacterium Escherichia coli by Matthew Meselson and Franklin Stahl.

**Solved independently** (answer withheld)

1. Meselson and Stahl (1958) first showed semiconservative replication by growing $E.\ coli$ in $^{15}\mathrm{N}$ medium, then moving it to $^{14}\mathrm{N}$ and separating the DNA on a CsCl density gradient. $E.\ coli$ is a bacterium, so the answer is option $3$.

**Subtopic:** Experimental Proof that DNA is Semiconservative · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 23)

![printed question 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q098_5f3b560e_03112026.png?v=5f3b560e48fb)

Publisher's solution, as printed:

![printed solution 98](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q098_e517a4e2_03112026.png?v=e517a4e2fcae)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Meselson and Stahl demonstrated semiconservative replication in the bacterium E. coli; Taylor's later work on a bean plant extended it to higher organisms
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  A plant is the true answer to where semiconservative replication was shown in higher organisms, Taylor's broad-bean experiment, which is printed in the same account; the stem asks where it was shown first.
- **Why:** This question requires the organism named in the first demonstration, demonstrated by 'was first shown in a' and four kinds of organism as options.
<!--/ecat-->

## Q99

Biology · both · Molecular Basis of Inheritance

Select the correct match

- (1) Alec Jeffreys - Streptococcus pneumoniae
- (2) Matthew Meselson and F. Stahl - Pisum sativum
- (3) Alfred Hershey and Martha Chase - TMV
- **(4)** Francois Jacob and Jacques Monod - Lac operon

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Francois Jacob and Jacque Monod proposed model of gene regulation known as operon model/lac operon.
2. Alec Jeffreys – DNA fingerprinting technique.
3. Matthew Meselson and F. Stahl – Semi-conservative DNA replication in E. coli.
4. Alfred Hershey and Martha Chase – Proved DNA as genetic material not protein

**Solved independently** (answer withheld)

1. Alec Jeffreys developed DNA fingerprinting; $\textit{Streptococcus pneumoniae}$ is linked to Griffith's transformation experiment, so option $1$ is wrong.
2. Meselson and Stahl proved semiconservative replication using $\textit{E. coli}$ grown in $^{15}\mathrm{N}$, not $\textit{Pisum sativum}$, so option $2$ is wrong.
3. Hershey and Chase showed DNA is the genetic material using bacteriophage T2, not TMV, so option $3$ is wrong.
4. Jacob and Monod first described the lac operon in $\textit{E. coli}$, so option $4$ is the correct match.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q099_e667f6d8_03112026.png?v=e667f6d8d278)

Publisher's solution, as printed:

![printed solution 99](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q099_531f139d_03112026.png?v=531f139db850)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Jacob and Monod worked out the lac operon; Griffith used Streptococcus pneumoniae, Meselson and Stahl used E. coli, Hershey and Chase used bacteriophage, and Alec Jeffreys developed DNA fingerprinting
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Hershey and Chase did work on a virus, and TMV is the virus this chapter prints elsewhere, so a student holding only 'they used a virus' accepts the wrong member of the right category.
- **Why:** This question requires stated attributions of workers to their material, demonstrated by 'Select the correct match' with each option printing one scientist-and-item pair scored whole.
- **Note:** E1 recorded match_the_lists on a two-lists pattern, but list_i and list_ii are empty, no two columns are printed and the answer is not a pairing code: each option is a single pair accepted or rejected whole. That is the codebook's pair_options shape, recorded here as two_part.
<!--/ecat-->

## Q100

Biology · both · Principles of Inheritance and Variation

Select the correct statement

- (1) Franklin Stahl coined the term ‘‘linkage’’
- (2) Spliceosomes take part in translation
- **(3)** Punnett square was developed by a British scientist
- (4) Transduction was discovered by S. Altman

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Punnett square was developed by a British geneticist, Reginald C. Punnett.
2. Franklin Stahl proved semi-conservative mode of replication.
3. Transduction was discovered by Zinder and Laderberg.
4. Spliceosome formation is part of post-transcriptional change in Eukaryotes

**Solved independently** (answer withheld)

1. The term linkage was coined by T.H. Morgan, not Franklin Stahl, so option $1$ is false.
2. Spliceosomes remove introns during post-transcriptional processing of hnRNA, not translation, so option $2$ is false.
3. The Punnett square was developed by Reginald C. Punnett, a British geneticist, so option $3$ is true.
4. Transduction was discovered by Zinder and Lederberg, not S. Altman (who worked on ribozymes), so option $4$ is false; the answer is option $3$.

**Subtopic:** Monohybrid Cross · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q100_f6aa4c1f_03112026.png?v=f6aa4c1f548e)

Publisher's solution, as printed:

![printed solution 100](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q100_a0ec5c74_03112026.png?v=a0ec5c74728c)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Punnett square is named after R.C. Punnett, a British geneticist; spliceosomes act on the transcript before translation, linkage was named by Morgan, and Altman's work was on RNA as an enzyme
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 2  
  The spliceosome is moved one stage along, from the processing of the transcript to translation, a step made easy by its name sitting one syllable from ribosome, the particle that does translate.
- **Why:** This question requires stated attributions and stated stages graded one by one, demonstrated by 'Select the correct statement' with each option a standalone claim such as 'Spliceosomes take part in translation'.
<!--/ecat-->

## Q101

Biology · both · Principles of Inheritance and Variation

Which of the following pairs is wrongly matched?

- **(1)** Starch synthesis in pea : Multiple alleles
- (2) XO type sex determination : Grasshopper
- (3) ABO blood grouping : Co-dominance
- (4) T.H. Morgan : Linkage

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Starch synthesis in pea is controlled by pleiotropic gene.
2. Other options (2, 3 & 4) are correctly matched.

**Solved independently** (answer withheld)

1. Starch synthesis in pea seeds is controlled by one gene with two alleles $B$ and $b$; $Bb$ gives intermediate-sized starch grains, so the pair shows incomplete dominance, not multiple alleles, and option $1$ is wrongly matched.
2. XO sex determination is seen in grasshopper, ABO blood grouping shows co-dominance ($I^A$ and $I^B$ both expressed) and T.H. Morgan worked out linkage in Drosophila, so options $2$, $3$ and $4$ are correctly matched.

**Subtopic:** Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q101_d55e2ce1_03112026.png?v=d55e2ce1b8f8)

Publisher's solution, as printed:

![printed solution 101](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q101_64af5878_03112026.png?v=64af5878b5bb)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Starch synthesis in pea is the pleiotropy example, one gene affecting more than one trait; multiple allelism is illustrated by the ABO blood groups, which also show codominance of A and B
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  ABO is printed in the same paragraph under two headings, multiple alleles and codominance, so a student whose remembered label for it is the first reads the pairing with the second as the wrong match.
- **Why:** This question requires each printed pairing checked against the example NCERT gives it to, demonstrated by 'Which of the following pairs is wrongly matched?' and by 'Starch synthesis in pea : Multiple alleles' naming the pleiotropy example.
- **Note:** E1 recorded statement_options, but the stem says 'pairs' and each option is one pair scored whole with no printed columns and no pairing code, which is the codebook's pair_options shape; recorded here as two_part.
<!--/ecat-->

## Q102

Biology · botany · Reproduction in Organisms

Offsets are produced by

- (1) Meiotic divisions
- (2) Parthenocarpy
- **(3)** Mitotic divisions
- (4) Parthenogenesis

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Offset is a vegetative part of a plant, formed by mitosis.
2. Meiotic divisions do not occur in somatic cells.
3. Parthenogenesis is the formation of embryo from ovum or egg without fertilisation.
4. Parthenocarpy is the fruit formed without fertilisation, (generally seedless)

**Solved independently** (answer withheld)

1. Offsets (e.g. in water hyacinth, Pistia) are vegetative propagules formed by asexual reproduction, which involves only $\text{mitotic}$ divisions, so the answer is option $3$.

**Subtopic:** Asexual Reproduction and Vegetative Propagation · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 24)

![printed question 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q102_9ee23a95_03112026.png?v=9ee23a957bfe)

Publisher's solution, as printed:

![printed solution 102](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q102_6573889b_03112026.png?v=6573889b8e07)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An offset is a vegetative propagule, so the new plant arises from the parent's own cells by mitosis and is a clone
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Mitosis and meiosis are taught as the pair of divisions, and a student who tags anything called reproduction with meiosis takes the reduction division for a process that is purely vegetative.
- **Why:** This question requires the kind of division NCERT states for a vegetative propagule, demonstrated by the stem 'Offsets are produced by' with two divisions and two modes of reproduction as options.
- **Note:** Swap test applied: mitotic and meiotic do resemble each other, but renaming them equational and reduction division leaves the route to option 1 alive, because what carries it is the two divisions being taught as a pair and reproduction being associated with meiosis. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q103

Biology · botany · Reproduction in Organisms

Which of the following flowers only once in its life-time?

- **(1)** Bamboo species
- (2) Mango
- (3) Jackfruit
- (4) Papaya

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Bamboo species are monocarpic i.e., flower generally only once in its life-time after $50$-$100$ years.
2. Jackfruit, papaya and mango are polycarpic i.e., produce flowers and fruits many times in their life-time.

**Solved independently** (answer withheld)

1. Bamboo species flower only once in their life-time, generally after $50$-$100$ years, then produce many fruits and die, while mango, jackfruit and papaya flower every year, so the answer is option $1$.

**Subtopic:** Phases of Life Cycle: Juvenile and Reproductive Phase · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q103_efa8d1b7_03112026.png?v=efa8d1b7a18a)

Publisher's solution, as printed:

![printed solution 103](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q103_9e03c08b_03112026.png?v=9e03c08bdd7d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Bamboo species stay vegetative for 50 to 100 years, then flower once, fruit heavily and die
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The three wrong options are common fruit trees that flower in season every year, which the stem's 'only once in its life-time' rules out directly. I checked each for a printed line that could carry it here — mango appears in these chapters for polyembryony, not for how often it flowers, and jackfruit and papaya appear in no account of flowering frequency — and for a likeness with 'bamboo', of which there is none.
- **Why:** This question requires the one plant NCERT states flowers a single time, demonstrated by 'Which of the following flowers only once in its life-time?' with four named plants and no criterion printed to apply.
<!--/ecat-->

## Q104

Biology · botany · Sexual Reproduction in Flowering Plants

Which of the following has proved helpful in preserving pollen as fossils?

- (1) Pollenkitt
- (2) Oil content
- (3) Cellulosic intine
- **(4)** Sporopollenin

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sporopollenin cannot be degraded by enzyme; strong acids and alkali, therefore it is helpful in preserving pollen as fossil.
2. Pollenkitt – Help in insect pollination.
3. Cellulosic Intine – Inner sporoderm layer of pollen grain known as intine made up cellulose & pectin.
4. Oil content – No role is pollen preservation.

**Solved independently** (answer withheld)

1. The pollen grain's outer wall, the exine, is made of $\text{sporopollenin}$, one of the most resistant organic materials known; it withstands high temperatures, strong acids and alkalis, and no enzyme is known to degrade it, so pollen grains are well preserved as fossils, which is option $4$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 24)

![printed question 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q104_ffb0d067_03112026.png?v=ffb0d067f66a)

Publisher's solution, as printed:

![printed solution 104](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q104_aab967b8_03112026.png?v=aab967b8761b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sporopollenin in the exine is one of the most resistant organic materials known, which is why pollen grains survive as fossils
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The intine and its cellulose are printed in the same two sentences as the exine and its sporopollenin, so a student who holds 'the pollen wall has two layers with named materials' and not which layer is the tough one picks the other layer's material.
- **Why:** This question requires the stated reason pollen survives as fossils, demonstrated by 'Which of the following has proved helpful in preserving pollen as fossils?' with four components of the same grain as options.
- **Note:** Swap test applied: sporopollenin and cellulosic intine are unlike words, and the route to option 3 survives any renaming, because what carries it is the two layers being printed in one place and learnt as a pair. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q105

Biology · both · Biotechnology and Its Applications

Which of the following is commonly used as a vector for introducing a DNA fragment in human lymphocytes?

- **(1)** Retrovirus
- (2) $\lambda$ phage
- (3) Ti plasmid
- (4) pBR 322

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Retrovirus is commonly used as vector for introducing a DNA fragment in human lymphocyte.
2. Gene therapy : Lymphocyte from blood of patient are grown in culture outside the body, a functional gene is introduced by using a retroviral vector, into these lymphocyte.

**Solved independently** (answer withheld)

1. Human lymphocytes are animal cells; NCERT states disarmed retroviruses are used to deliver desirable genes into animal cells (as in ADA-deficiency gene therapy using lymphocytes), whereas $\lambda$ phage and pBR 322 are vectors for bacteria and the Ti plasmid is a vector for plants, so the answer is option $1$.

**Subtopic:** Gene Therapy and Molecular Diagnosis · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q105_5a9cbfe9_03112026.png?v=5a9cbfe9b77d)

Publisher's solution, as printed:

![printed solution 105](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q105_f30b6a27_03112026.png?v=f30b6a2766d1)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Gene therapy for ADA deficiency puts the functional gene into the patient's lymphocytes with a retroviral vector, which integrates into the animal cell's genome
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The Ti plasmid is the true answer to which vector delivers a gene into a eukaryotic cell in this syllabus — a plant cell, through Agrobacterium — and 'human lymphocytes' are eukaryotic too, so the remembered eukaryote vector is carried across.
- **Why:** This question requires the vector NCERT names for one stated host, demonstrated by 'for introducing a DNA fragment in human lymphocytes' with four real vectors, three of them for other hosts, as options.
<!--/ecat-->

## Q106

Biology · both · Biotechnology: Principles and Processes

The correct order of steps in Polymerase Chain Reaction (PCR) is

- (1) Extension, Denaturation, Annealing
- (2) Denaturation, Extension, Annealing
- (3) Annealing, Extension, Denaturation
- **(4)** Denaturation, Annealing, Extension

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. This technique is used for making multiple copies of gene (or DNA) of interest in vitro.
2. Each cycle has three steps
3. (I) Denaturation
4. (II) Primer annealing
5. (III) Extension of primer

**Solved independently** (answer withheld)

1. Each PCR cycle has three steps in a fixed order: denaturation (heat separates the DNA strands), annealing (primers bind the single strands), then extension (Taq polymerase extends the primers). That order is Denaturation, Annealing, Extension, which is option $4$.

**Subtopic:** Amplification of Gene of Interest Using PCR · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q106_2e1dec48_03112026.png?v=2e1dec4873a1)

Publisher's solution, as printed:

![printed solution 106](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q106_9b912e74_03112026.png?v=9b912e74f4d9)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Sequence** (`order`) — a sequence to put in the right order, or a trend to arrange
- **Concept:** Each PCR cycle runs denaturation, then annealing of the primers, then extension by Taq polymerase; the primer must be bound before the enzyme can add anything
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  Denaturation is placed first, which is right, and then extension is put before annealing by a student who treats the polymerase's work as what follows strand separation; nothing can be extended until a primer has bound.
- **Why:** This question requires three named steps put in their fixed sequence, demonstrated by 'The correct order of steps in Polymerase Chain Reaction (PCR) is' with each option printing all three steps in a different order.
- **Note:** E1 recorded arrange_in_order. The current qtype axis has no ordering value, so the shape is recorded as two_part — each option is a three-item answer scored whole — and the ordering demand is carried on asks: order.
<!--/ecat-->

## Q107

Biology · both · Biotechnology and Its Applications

In India, the organisation responsible for assessing the safety of introducing genetically modified organisms for public use is

- (1) Indian Council of Medical Research (ICMR)
- (2) Research Committee on Genetic Manipulation (RCGM)
- (3) Council for Scientific and Industrial Research (CSIR)
- **(4)** Genetic Engineering Appraisal Committee (GEAC)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Indian Government has setup organisation such as GEAC (Genetic Engineering Appraisal Committee) which will make decisions regarding the validity of GM research and safety of introducing GM-organism for public services. (Direct from NCERT).

**Solved independently** (answer withheld)

1. The body that judges the validity of GM research and the safety of introducing GM organisms for public services in India is the $\text{GEAC}$ (Genetic Engineering Appraisal Committee), which is option $4$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 25)

![printed question 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q107_55606b4d_03112026.png?v=55606b4d80ca)

Publisher's solution, as printed:

![printed solution 107](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q107_3bffb624_03112026.png?v=3bffb624cacd)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** GEAC, the Genetic Engineering Appraisal Committee, is the body set up in India to judge the validity of GM research and the safety of releasing GM organisms for public use
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  Its expansion is built out of near-synonyms of the right body's — a committee, on genetic manipulation rather than genetic engineering, reviewing rather than appraising — so the name itself reads as the description in the stem.
- **Why:** This question requires the body NCERT names for one stated function, demonstrated by 'the organisation responsible for assessing the safety of introducing genetically modified organisms for public use' with four Indian organisations as options.
- **Note:** E1 recorded statement_options from the long options, but each option is the name of an organisation and the stem is a single sentence ending in 'is', so the shape here is mcq.
<!--/ecat-->

## Q108

Biology · both · Biotechnology and Its Applications

Use of bioresources by multinational companies and organisations without authorisation from the concerned country and its people is called

- (1) Bio-infringement
- (2) Biodegradation
- **(3)** Biopiracy
- (4) Bioexploitation

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Biopiracy is term used for or refer to the use of bioresources by multinational companies and other organisation without proper authorisation from the countries and people concerned with compensatory payment (definition of biopiracy given in NCERT).

**Solved independently** (answer withheld)

1. When multinational companies and organisations use a country's bioresources without authorisation from that country and its people, it is called biopiracy, which is option $3$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q108_daaddb03_03112026.png?v=daaddb0301f0)

Publisher's solution, as printed:

![printed solution 108](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q108_fbe47780_03112026.png?v=fbe477806f32)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biopiracy is the term for taking and using bio-resources of a country or community without their authorisation and without compensation
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  The coinage is built like the real term — 'bio-' plus a word for taking what is not yours — and it names the stem's own description, exploitation, so it reads as chapter vocabulary.
- **Why:** This question requires the term NCERT gives to a described practice, demonstrated by the stem ending 'without authorisation from the concerned country and its people is called' with four 'bio-' compounds as options.
- **Note:** Three of the four options are coinages rather than terms of the account, which the retired per-option vocabulary called fabricated_term. Following section 5.0, it is recorded in its live family, look_alike_term: the pull is that the coinage is built like the real term and restates the stem.
<!--/ecat-->

## Q109

Biology · both · Biotechnology and Its Applications

A ‘new’ variety of rice was patented by a foreign company, though such varieties have been present in India for a long time. This is related to

- (1) Co-667
- (2) Lerma Rojo
- (3) Sharbati Sonora
- **(4)** Basmati

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In 1997, an American company got patent rights on Basmati rice through the US patent and trademark office that was actually been derived from Indian farmer’s varieties.
2. The diversity of rice in India is one of the richest in the world, 27 documented varieties of Basmati are grown in India.
3. Indian basmati was crossed with semi-dwarf varieties and claimed as an invention or a novelty.
4. Sharbati Sonora and Lerma Rojo are varieties of wheat.

**Solved independently** (answer withheld)

1. In 1997 an American company was granted a US patent on Basmati rice, a variety grown in India for centuries, which is the standard biopiracy example, so the answer is option $4$.

**Subtopic:** Ethical Issues and Biopiracy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 25)

![printed question 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q109_4d625f2b_03112026.png?v=4d625f2b4026)

Publisher's solution, as printed:

![printed solution 109](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q109_1cd1f754_03112026.png?v=1cd1f754ad49)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Biopiracy: a company abroad patenting a crop variety that has been grown in India for generations, with Basmati rice as the standard case
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Lerma Rojo is the one foreign-bred name in the list, so a student who fixes on the stem's words 'a foreign company' answers with the foreign-sounding variety instead of asking which option is a rice
- **Why:** This question requires the one NCERT case of biopiracy, demonstrated by the stem's 'a ‘new’ variety of rice was patented by a foreign company, though such varieties have been present in India for a long time'.
<!--/ecat-->

## Q110

Biology · both · Molecular Basis of Inheritance

Select the correct match

- **(1)** Ribozyme - Nucleic acid
- (2) T.H. Morgan - Transduction
- (3) $\mathrm{F_2}$ $\times$ Recessive parent - Dihybrid cross
- (4) G. Mendel - Transformation

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Ribozyme is a catalytic RNA, which is nucleic acid.

**Solved independently** (answer withheld)

1. A ribozyme is an RNA molecule that acts as an enzyme, so $\text{Ribozyme} \rightarrow \text{Nucleic acid}$ is a correct match.
2. T.H. Morgan is known for linkage and recombination in \textit{Drosophila}, not transduction, so option $2$ is wrong.
3. Crossing a hybrid with the recessive parent is a test cross, and a dihybrid cross involves two character pairs ($F_1 \times F_1$), so option $3$ is wrong.
4. Transformation was discovered by Griffith, not Mendel, so option $4$ is wrong; the answer is option $1$.

**Subtopic:** RNA World and Types of RNA · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 25)

![printed question 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q110_661457e7_03112026.png?v=661457e72e4a)

Publisher's solution, as printed:

![printed solution 110](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q110_81245dd2_03112026.png?v=81245dd2a342)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A ribozyme is RNA that catalyses a reaction, so an enzyme need not be a protein
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  A cross made with the recessive parent is a named cross, and a student who has kept that much but not the name accepts the only cross name printed beside it
- **Why:** This question requires the stated pairing of a term with what it is, demonstrated by option 1's 'Ribozyme - Nucleic acid'.
- **Note:** type_patterns returned match_the_lists on '4 two lists', but no two columns are printed and there is no pairing code: each option is a single pair accepted or rejected whole, which is the pair-options shape, so qtype is recorded as statements.
<!--/ecat-->

## Q111

Biology · botany · Organisms and Populations

Niche is

- (1) all the biological factors in the organism's environment
- (2) the range of temperature that the organism needs to live
- (3) the physical space where an organism lives
- **(4)** the functional role played by the organism where it lives

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ecological niche was termed by J. Grinnel.
2. It refers the functional role played by the organism where it lives.

**Solved independently** (answer withheld)

1. NCERT defines niche as the unique functional role of an organism in its community, distinct from habitat, which is the physical place where it lives, so the answer is option $4$.

**Subtopic:** Biome, Environmental Factors & Four Levels of Biological Organisation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q111_d7b26275_03112026.png?v=d7b26275366e)

Publisher's solution, as printed:

![printed solution 111](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q111_8dc1d711_03112026.png?v=8dc1d7112ef3)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A niche is the functional role an organism plays where it lives; the place itself is its habitat
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Habitat is defined in the same breath as niche, so a student carrying 'the niche is where an organism lives' answers with the option that names the physical space
- **Why:** This question requires the stated definition of a term, demonstrated by option 4's 'the functional role played by the organism where it lives'; on the trap axis the swap test was applied -- 'niche' and 'habitat' share no letters, so position in the definition pair and not resemblance is what carries the student, which makes it nearby_fact.
<!--/ecat-->

## Q112

Biology · botany · Environmental Issues

Which of the following is a secondary pollutant?

- (1) $\mathrm{CO}$
- (2) $\mathrm{SO_2}$
- (3) $\mathrm{CO_2}$
- **(4)** $\mathrm{O_3}$

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. $\mathrm{O_3}$ (ozone) is a secondary pollutant.
2. These are formed by the reaction of primary pollutant.
3. $\mathrm{CO}$ – Quantitative pollutant
4. $\mathrm{CO_2}$ – Primary pollutant
5. $\mathrm{SO_2}$ – Primary pollutant

**Solved independently** (answer withheld)

1. A secondary pollutant forms in the atmosphere from primary pollutants. $\mathrm{CO}$, $\mathrm{SO_2}$ and $\mathrm{CO_2}$ are emitted directly by combustion (primary), while $\mathrm{O_3}$ forms photochemically from $\mathrm{NO_x}$ and hydrocarbons in sunlight, so it is secondary, which is option $4$.

**Subtopic:** Air Pollution and Its Control · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q112_4e8c4cff_03112026.png?v=4e8c4cff0b13)

Publisher's solution, as printed:

![printed solution 112](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q112_f92b9dc9_03112026.png?v=f92b9dc9d326)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Primary pollutants are emitted as they are; secondary pollutants are made in the air out of them, which is why tropospheric ozone is counted secondary
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  $\mathrm{SO_2}$ is the pollutant the chapter follows into a second substance, sulphuric acid in acid rain, so a student who reads 'secondary' as 'goes on to make something else' answers with it
- **Why:** This question requires the stated membership of NCERT's secondary-pollutant list, demonstrated by the stem's 'which of the following is a secondary pollutant' set against four named gases with no criterion printed.
<!--/ecat-->

## Q113

Biology · botany · Environmental Issues

World Ozone Day is celebrated on

- (1) $5^{\text{th}}$ June
- **(2)** $16^{\text{th}}$ September
- (3) $21^{\text{st}}$ April
- (4) $22^{\text{nd}}$ April

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. World Ozone day is celebrated on $16^{\text{th}}$ September.
2. $5^{\text{th}}$ June - World Environment Day
3. $21^{\text{st}}$ April - National Yellow Bat Day
4. $22^{\text{nd}}$ April - National Earth Day

**Solved independently** (answer withheld)

1. World Ozone Day marks the signing of the Montreal Protocol on $16^{\text{th}}$ September 1987, so the answer is option $2$ ($5^{\text{th}}$ June is World Environment Day and $22^{\text{nd}}$ April is Earth Day).

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q113_c7f424ff_03112026.png?v=c7f424ff4867)

Publisher's solution, as printed:

![printed solution 113](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q113_f3d482e6_03112026.png?v=f3d482e6ee50)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The dates the chapter attaches to environmental observances: 16 September for World Ozone Day, the day the Montreal Protocol was signed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  5 June is the environmental date the same chapter repeats, so a student holding one 'environment day' in memory writes it in here
- **Why:** This question requires one stored calendar date, demonstrated by the stem 'World Ozone Day is celebrated on' set against four bare dates.
<!--/ecat-->

## Q114

Biology · botany · Organisms and Populations

Natality refers to

- (1) Death rate
- (2) Number of individuals leaving the habitat
- **(3)** Birth rate
- (4) Number of individuals entering a habitat

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Natality refers to birth rate.
2. Death rate – Mortality
3. Number of individual entering a habitat is – Immigration
4. Number of individual leaving the habital – Emigration

**Solved independently** (answer withheld)

1. Natality is the number of births in a population during a given period, which is the birth rate (mortality is death rate, emigration is individuals leaving, immigration is individuals entering), so the answer is option $3$.

**Subtopic:** Introduction of Organisms, Populations and Their Growth · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q114_f0f56283_03112026.png?v=f0f562830108)

Publisher's solution, as printed:

![printed solution 114](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q114_2b8bd910_03112026.png?v=2b8bd91056e7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Natality is the birth rate of a population, and mortality the death rate; immigration and emigration are the movements in and out
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Natality and mortality are defined in one line as the two rates of a population, so a student who has stored the pair without which is which reads 'Natality' and answers with the other rate
- **Why:** This question requires the stated meaning of one term, demonstrated by the stem 'Natality refers to' set against the four population parameters; on the trap axis the swap test was applied -- the option is printed as 'Death rate', which shares no part of the word 'Natality', so position in the definition pair and not word resemblance carries the student, which makes it nearby_fact rather than look_alike_term.
<!--/ecat-->

## Q115

Biology · botany · Environmental Issues

In stratosphere, which of the following elements acts as a catalyst in degradation of ozone and release of molecular oxygen?

- (1) Carbon
- (2) $\mathrm{Fe}$
- **(3)** $\mathrm{Cl}$
- (4) Oxygen

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. UV rays act on CFCs, releasing $\mathrm{Cl}$ atoms, chlorine reacts with ozone in sequential method converting into oxygen
2. Carbon, oxygen and $\mathrm{Fe}$ are not related to ozone layer depletion

**Solved independently** (answer withheld)

1. In the stratosphere, UV radiation acts on CFCs and releases free $\mathrm{Cl}$ atoms.
2. $\mathrm{Cl} + \mathrm{O_3} \rightarrow \mathrm{ClO} + \mathrm{O_2}$ releases molecular oxygen.
3. $\mathrm{ClO} + \mathrm{O} \rightarrow \mathrm{Cl} + \mathrm{O_2}$ gives back $\mathrm{Cl}$, so $\mathrm{Cl}$ is not used up and acts as a catalyst, which is option $3$.

**Subtopic:** Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q115_adb4543e_03112026.png?v=adb4543e5189)

Publisher's solution, as printed:

![printed solution 115](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q115_7b59d784_03112026.png?v=7b59d784ee9e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** UV light splits CFCs and frees chlorine atoms, which break ozone down to molecular oxygen without themselves being used up, so chlorine is the catalyst
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Carbon is a constituent of the chlorofluorocarbon the same passage blames, so a student who remembers that CFCs destroy ozone takes an element out of the molecule's name instead of the atom the passage says is released.
- **Why:** This question requires the element NCERT names as the catalyst of ozone breakdown, demonstrated by 'which of the following elements acts as a catalyst in degradation of ozone' with four elements as options.
<!--/ecat-->

## Q116

Biology · botany · Ecosystem

What type of ecological pyramid would be obtained with the following data?
Secondary consumer : $120\,\mathrm{g}$
Primary consumer : $60\,\mathrm{g}$
Primary producer : $10\,\mathrm{g}$

- **(1)** Inverted pyramid of biomass
- (2) Upright pyramid of numbers
- (3) Pyramid of energy
- (4) Upright pyramid of biomass

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The given data depicts the inverted pyramid of biomass, usually found in aquatic ecosystem.
2. Pyramid of energy is always upright
3. Upright pyramid of biomass and numbers are not possible, as the data depicts primary producer is less than primary consumer and this is less than secondary consumers.

**Solved independently** (answer withheld)

1. The values are given in grams ($\mathrm{g}$), so they measure biomass, not numbers or energy.
2. Order the trophic levels: producer $10\,\mathrm{g} < $ primary consumer $60\,\mathrm{g} < $ secondary consumer $120\,\mathrm{g}$.
3. Biomass rises from the base to the top, so the base is narrowest and the pyramid is inverted (as in an aquatic ecosystem with phytoplankton as producers).
4. An inverted pyramid of biomass is option $1$.

**Subtopic:** Ecological Pyramids · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 26)

![printed question 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q116_ab073ff5_03112026.png?v=ab073ff5d7c9)

Publisher's solution, as printed:

![printed solution 116](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q116_36a07cdb_03112026.png?v=36a07cdb7a31)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A pyramid is read from the figures themselves: here biomass rises from 10 g of producers to 120 g of secondary consumers, so the pyramid of biomass is inverted
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 4  
  The standard shape is applied without using the figures: the data are in grams, so the pyramid is one of biomass, and biomass pyramids are taught as upright — which the printed numbers, rising from 10 g to 120 g, contradict.
- **Why:** This question requires a stated rule carried onto supplied figures, demonstrated by 'What type of ecological pyramid would be obtained with the following data?' with 120 g, 60 g and 10 g printed against the three trophic levels.
<!--/ecat-->

## Q117

Biology · both · Cell: The Unit of Life

The Golgi complex participates in

- (1) Fatty acid breakdown
- (2) Respiration in bacteria
- **(3)** Formation of secretory vesicles
- (4) Activation of amino acid

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Golgi complex, after processing releases secretory vesicles from their trans-face.

**Solved independently** (answer withheld)

1. The Golgi complex packages materials and forms secretory vesicles, so option $3$ is correct; bacteria have no Golgi, fatty acid breakdown takes place in mitochondria and peroxisomes, and amino acid activation takes place in the cytoplasm.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 26)

![printed question 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q117_e2375b11_03112026.png?v=e2375b119304)

Publisher's solution, as printed:

![printed solution 117](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q117_deae7280_03112026.png?v=deae7280a339)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The Golgi complex packages material from the ER into vesicles for secretion or for delivery inside the cell, and it is where glycoproteins and glycolipids are formed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The lipid fact printed beside the Golgi's packaging role is that glycolipids are formed there, so a student holding 'Golgi and lipids' accepts the option that names a lipid process, though this one is a breakdown and happens elsewhere.
- **Why:** This question requires the function NCERT states for one organelle, demonstrated by the stem 'The Golgi complex participates in' with four cellular processes as options.
<!--/ecat-->

## Q118

Biology · botany · Photosynthesis in Higher Plants

Which of the following is not a product of light reaction of photosynthesis?

- (1) ATP
- (2) NADPH
- **(3)** NADH
- (4) Oxygen

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. ATP, NADPH and oxygen are products of light reaction, while NADH is a product of respiration process.

**Solved independently** (answer withheld)

1. The light reaction makes $\mathrm{ATP}$ (photophosphorylation), $\mathrm{NADPH}$ (reduction of $\mathrm{NADP^+}$) and $\mathrm{O_2}$ (photolysis of water); $\mathrm{NADH}$ belongs to respiration, not photosynthesis, so the answer is option $3$.

**Subtopic:** Light Reaction, Electron Transport and Splitting Of Water · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 26)

![printed question 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q118_bf15534f_03112026.png?v=bf15534f093c)

Publisher's solution, as printed:

![printed solution 118](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q118_c06c5804_03112026.png?v=c06c580440fe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The light reaction yields ATP, NADPH and oxygen; NADH is the reduced coenzyme of respiration, since photosynthesis reduces NADP+ and not NAD+
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 2  
  NADPH and NADH differ by one letter, so a student who knows a reduced coenzyme is made in the light reaction but not which one strikes out the phosphorylated name and leaves the respiratory one standing.
- **Why:** This question requires the stated products of the light reaction, demonstrated by 'Which of the following is not a product of light reaction of photosynthesis?' printing NADPH and NADH together in the same list.
- **Note:** Swap test applied: renaming the two coenzymes so that they no longer resemble each other kills the route to option 2, so the likeness is what carries it. look_alike_term, not nearby_fact.
<!--/ecat-->

## Q119

Biology · botany · Biological Classification

Which among the following is not a prokaryote?

- **(1)** Saccharomyces
- (2) Nostoc
- (3) Mycobacterium
- (4) Oscillatoria

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Saccharomyces i.e. yeast is an eukaryote (unicellular fungi)
2. Mycobacterium – a bacterium
3. Oscillatoria and Nostoc are cyanobacteria.

**Solved independently** (answer withheld)

1. Saccharomyces is yeast, a fungus with a membrane-bound nucleus, so it is a eukaryote; Nostoc and Oscillatoria (cyanobacteria) and Mycobacterium (bacterium) are prokaryotes, so the answer is option $1$.

**Subtopic:** Kingdom Monera, Ascomycetes · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q119_714acd48_03112026.png?v=714acd48d624)

Publisher's solution, as printed:

![printed solution 119](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q119_9f650338_03112026.png?v=9f650338fb34)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Saccharomyces is a yeast, and so a eukaryotic fungus; Nostoc and Oscillatoria are cyanobacteria and Mycobacterium a bacterium, all of them Monera
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  The prefix myco- belongs to fungi — mycology, mycorrhiza, Mycoplasma — so the bacterium with the fungal-sounding name is read as the non-prokaryote, which is exactly the discrimination this question sets by also printing a real fungus.
- **Why:** This question requires each named genus placed on the prokaryote side or off it, demonstrated by 'Which among the following is not a prokaryote?' printing a yeast alongside a bacterium whose name begins myco-.
- **Note:** Swap test applied to option 3: renaming Mycobacterium so that it carries no fungal prefix kills the route, so the likeness of the name is the carrier. Options 2 and 4 are reached by one route between them, the old name 'blue-green algae', and both are recorded because the route lands on each equally.
<!--/ecat-->

## Q120

Biology · botany · Transport in Plants

Stomatal movement is not affected by

- (1) Temperature
- **(2)** $\mathrm{O_2}$ concentration
- (3) Light
- (4) $\mathrm{CO_2}$ concentration

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Light, temperature and concentration of $\mathrm{CO_2}$ affect opening and closing of stomata while they are not affected by $\mathrm{O_2}$ concentration.

**Solved independently** (answer withheld)

1. Guard-cell turgor, and so stomatal opening, is controlled by light, temperature and $\mathrm{CO_2}$ concentration; $\mathrm{O_2}$ concentration has no such regulatory role, so the answer is option $2$.

**Subtopic:** Transpiration and Stomatal Opening and Closing · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q120_e46b60bf_03112026.png?v=e46b60bfde0d)

Publisher's solution, as printed:

![printed solution 120](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q120_80b9a2e7_03112026.png?v=80b9a2e77172)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Stomatal opening and closing responds to light, temperature, CO2 concentration and water status; oxygen concentration is not among the factors stated
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Temperature is a true factor, and it is the one the account merely lists while giving light and CO2 a mechanism of their own, so a student who holds the mechanisms rather than the list has nothing attaching temperature to the guard cells and reads it as the outsider.
- **Why:** This question requires the membership of the stated list of factors, demonstrated by 'Stomatal movement is not affected by' with three listed factors and one unlisted gas as options.
- **Note:** The retired per-option vocabulary called this device true_statement_trap — a true option failing the task's NOT polarity. Following section 5.0 it is recorded in its live family, answers_other_question: temperature is true and answers the un-negated question. Where the misreading on a negated stem has a name of its own, such as a dropped qualifier or a relocated site, that label is used instead.
<!--/ecat-->

## Q121

Biology · both · Cell: The Unit of Life

Which of the following is true for nucleolus?

- (1) Larger nucleoli are present in dividing cells
- (2) It takes part in spindle formation
- (3) It is a membrane-bound structure
- **(4)** It is a site for active ribosomal RNA synthesis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Nucleolus is a non membranous structure and is a site of r-RNA synthesis.

**Solved independently** (answer withheld)

1. The nucleolus is not bounded by a membrane, so option $3$ is false.
2. Spindle fibres form from microtubules organised by centrosomes, not the nucleolus, so option $2$ is false.
3. Larger and more numerous nucleoli occur in cells actively making protein, and the nucleolus disappears during cell division, so option $1$ is false.
4. The nucleolus is the site of active ribosomal RNA synthesis, which is option $4$.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q121_b80b989a_03112026.png?v=b80b989a1d16)

Publisher's solution, as printed:

![printed solution 121](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q121_6cba034e_03112026.png?v=6cba034e1286)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The nucleolus is a non-membrane-bound region of the nucleus where ribosomal RNA is actively transcribed
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  The line printed beside this one says nucleoli are larger and more numerous in cells actively carrying out protein synthesis; this option keeps the 'larger nucleoli' half and swaps the cell type to dividing, so the half-remembered sentence seems to vouch for it
- **Why:** This question requires judging four whole claims about one organelle against the stated facts, demonstrated by option 4's 'site for active ribosomal RNA synthesis' being the textbook phrase while each other option restates a neighbouring line from the same paragraph.
- **Note:** E1 called this statement_options; the printed shape agrees, since no lettered block is printed and every option is a full claim judged for truth, so qtype is statements rather than mcq.
<!--/ecat-->

## Q122

Biology · both · Cell Cycle and Cell Division

The stage during which separation of the paired homologous chromosomes begins is

- (1) Pachytene
- (2) Diakinesis
- **(3)** Diplotene
- (4) Zygotene

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Synaptonemal complex disintegrates.
2. Terminalisation begins at diplotene stage i.e. chiasmata start to shift towards end.

**Solved independently** (answer withheld)

1. In prophase I, homologues pair in zygotene and cross over in pachytene; at the start of $\text{diplotene}$ the synaptonemal complex dissolves and the paired homologues begin to separate, staying joined only at the chiasmata, so the answer is option $3$.

**Subtopic:** Prophase I and Its Types · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q122_dcdc98e5_03112026.png?v=dcdc98e5cfca)

Publisher's solution, as printed:

![printed solution 122](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q122_2acc6222_03112026.png?v=2acc6222ea93)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homologous chromosomes of each bivalent begin to pull apart at diplotene, when the synaptonemal complex dissolves
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 4  
  Zygotene is the stage attached to the words 'homologous chromosomes pair', and the stem prints 'the paired homologous chromosomes', so the remembered answer to 'when does synapsis begin' is handed in for a question about when separation begins
- **Why:** This question requires the stage the book names for the onset of homologue separation, demonstrated by the stem's 'separation ... begins' set against four consecutive sub-stages of prophase I.
<!--/ecat-->

## Q123

Biology · both · Biomolecules

The two functional groups characteristic of sugars are

- (1) Hydroxyl and methyl
- (2) Carbonyl and phosphate
- (3) Carbonyl and methyl
- **(4)** Carbonyl and hydroxyl

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Sugar is a common term used to denote carbohydrate.
2. Carbohydrates are polyhydroxy aldehyde, ketone or their derivatives, which means they have carbonyl and hydroxyl groups.

**Solved independently** (answer withheld)

1. Sugars (carbohydrates) are polyhydroxy aldehydes or polyhydroxy ketones, so their characteristic groups are the carbonyl group ($>C=O$) and hydroxyl groups ($-OH$), which is option $4$.

**Subtopic:** Chemical Constituents Of Living Cells · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q123_2ddca460_03112026.png?v=2ddca460bdd2)

Publisher's solution, as printed:

![printed solution 123](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q123_da9ffcac_03112026.png?v=da9ffcac6902)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Sugars are polyhydroxy aldehydes or ketones, so a carbonyl group together with hydroxyl groups is what defines them
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The carbonyl half is correct, and phosphate is pulled in from the nucleotide formula, where the sugar is always drawn with a phosphate hung on it, so a group that sits next to the sugar is taken for a group of the sugar
- **Why:** This question requires the two groups named in the definition of a sugar, demonstrated by the options pairing 'Carbonyl' with three different partners so that only the second slot decides the answer.
<!--/ecat-->

## Q124

Biology · botany · Anatomy of Flowering Plants

Stomata in grass leaf are

- **(1)** Dumb-bell shaped
- (2) Rectangular
- (3) Kidney shaped
- (4) Barrel shaped

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Grass being a monocot, has Dumb-bell shaped stomata in their leaves.

**Solved independently** (answer withheld)

1. In grasses the guard cells bounding each stomatal pore are dumb-bell shaped (dicots have bean/kidney-shaped guard cells), so the answer is option $1$.

**Subtopic:** Epidermal Tissue System · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q124_ea2f68b5_03112026.png?v=ea2f68b59385)

Publisher's solution, as printed:

![printed solution 124](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q124_936e7f2b_03112026.png?v=936e7f2b3de9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Guard cells are bean or kidney shaped in most dicots but dumb-bell shaped in grasses
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Kidney shaped is the guard-cell shape the book gives for the general stoma, and it becomes the right answer the moment the word 'grass' is dropped from the stem, so a student reading the stem as 'stomata are' lands here
- **Why:** This question requires the guard-cell shape stated for one named group of plants, demonstrated by the stem's 'in grass leaf', which is the only word separating option 1 from option 3.
<!--/ecat-->

## Q125

Biology · botany · Sexual Reproduction in Flowering Plants

Which one of the following plants shows a very close relationship with a species of moth, where none of the two can complete its life cycle without the other?

- (1) Hydrilla
- (2) Banana
- **(3)** Yucca
- (4) Viola

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Yucca have an obligate mutualism with a species of moth i.e. Pronuba.

**Solved independently** (answer withheld)

1. The plant whose life cycle depends on a moth, and the moth's on it, is $Yucca$ (the moth pollinates it and its larvae feed in the ovary), which is option $3$.

**Subtopic:** Agents of Pollination · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q125_e18668b9_03112026.png?v=e18668b99465)

Publisher's solution, as printed:

![printed solution 125](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q125_0e733ede_03112026.png?v=0e733ede19b0)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Yucca and its moth are the standard case of obligate mutualism, in which pollination and the insect's egg-laying depend on each other
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Hydrilla is the other plant this pollination section names with one specific agent of its own, so a student who remembers that the section ties a named plant to a named partner, but not which plant, reaches for it
- **Why:** This question requires the plant-and-pollinator pair the book names, demonstrated by the stem's 'none of the two can complete its life cycle without the other', which is the textbook's own wording for Yucca and its moth.
<!--/ecat-->

## Q126

Biology · botany · Sexual Reproduction in Flowering Plants

Pollen grains can be stored for several years in liquid nitrogen having a temperature of

- (1) $-120\,^{\circ}\mathrm{C}$
- **(2)** $-196\,^{\circ}\mathrm{C}$
- (3) $-80\,^{\circ}\mathrm{C}$
- (4) $-160\,^{\circ}\mathrm{C}$

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Pollen grains can be stored for several years in liquid nitrogen at $-196\,^{\circ}\mathrm{C}$ (Cryopreservation)

**Solved independently** (answer withheld)

1. Pollen grains are cryopreserved in liquid nitrogen, whose temperature is $-196\,^{\circ}\mathrm{C}$, which is option $2$.

**Subtopic:** Pollen Grain and Their Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 27)

![printed question 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q126_31505e54_03112026.png?v=31505e5435ec)

Publisher's solution, as printed:

![printed solution 126](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q126_b0c80eab_03112026.png?v=b0c80eab885a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pollen banks keep pollen viable for years because liquid nitrogen holds it at -196 degrees Celsius
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  The pollen-storage line prints exactly one temperature, -196 C, against liquid nitrogen; the other three figures are printed nowhere in the chapter and the stem supplies no number to compute from, so no route other than the remembered value reaches any option
- **Why:** This question requires a single stored value from the source line, demonstrated by the stem's 'liquid nitrogen having a temperature of' with four bare temperatures as options and no quantity given to work from.
- **Note:** Called no_trap after checking each distractor separately rather than forcing a number trap: with no figure in the stem to compute with, a distractor could pull only by being a remembered printed value, and none of the three is printed. Three fillers are recorded here because all three wrong options genuinely sit in that position.
<!--/ecat-->

## Q127

Biology · botany · Sexual Reproduction in Flowering Plants

Double fertilization is

- (1) Fusion of two male gametes of a pollen tube with two different eggs
- (2) Fusion of two male gametes with one egg
- (3) Fusion of one male gamete with two polar nuclei
- **(4)** Syngamy and triple fusion

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Double fertilization is a unique phenomenon that occur in angiosperms only.
2. Syngamy $+$ Triple fusion $=$ Double fertilization

**Solved independently** (answer withheld)

1. In the embryo sac, one male gamete fuses with the egg cell (syngamy) and the other fuses with the two polar nuclei (triple fusion); because two fusions occur, this is double fertilization, so the answer is option $4$.

**Subtopic:** Double Fertilisation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q127_6fd3f3c0_03112026.png?v=6fd3f3c063f6)

Publisher's solution, as printed:

![printed solution 127](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q127_67cab9fc_03112026.png?v=67cab9fc7688)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Double fertilisation is the pair of fusions inside one embryo sac: syngamy makes the zygote and triple fusion makes the primary endosperm nucleus.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  Option 3 is the printed account of triple fusion on its own - one male gamete with the two polar nuclei - so a student who recalls that event names it and stops, leaving syngamy out of an answer that needs both fusions.
- **Why:** This question requires the stated two-event definition of double fertilisation, demonstrated by the keyed option reading 'Syngamy and triple fusion' while all three others describe one fusion only.
- **Note:** The pattern returned `statement_options`. The stem is a direct question and the options are candidate answers rather than claims to be graded, so brief rule 1 keeps the shape at `mcq`.
<!--/ecat-->

## Q128

Biology · botany · Photosynthesis in Higher Plants

Oxygen is not produced during photosynthesis by

- **(1)** Green sulphur bacteria
- (2) Cycas
- (3) Nostoc
- (4) Chara

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Green sulphur bacteria do not use $\mathrm{H_2O}$ as source of proton, therefore they do not evolve $\mathrm{O_2}$.

**Solved independently** (answer withheld)

1. Green sulphur bacteria use $\mathrm{H_2S}$ as the electron/hydrogen donor and have only PS I, so photosynthesis is anoxygenic: $\mathrm{CO_2} + 2\mathrm{H_2S} \rightarrow (\mathrm{CH_2O}) + \mathrm{H_2O} + 2\mathrm{S}$, and no $\mathrm{O_2}$ is produced.
2. Cycas (gymnosperm), Nostoc (cyanobacterium) and Chara (green alga) all split water and evolve $\mathrm{O_2}$, so the answer is option $1$.

**Subtopic:** Photosynthesis Experiments · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 27)

![printed question 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q128_49d68443_03112026.png?v=49d684433d81)

Publisher's solution, as printed:

![printed solution 128](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q128_b3d32108_03112026.png?v=b3d321084fbe)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Green sulphur bacteria photosynthesise with H2S as hydrogen donor and release sulphur, not oxygen; every oxygenic photosynthesiser splits water instead.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The H2S-donor fact belongs to the purple and green sulphur bacteria, and Nostoc is the other prokaryote on the list, so the rule 'photosynthetic bacteria do not evolve oxygen' gets applied to the cyanobacterium printed alongside them.
- **Why:** This question requires the stated fact that only the sulphur bacteria use H2S in place of water, demonstrated by the keyed option 'Green sulphur bacteria' standing against three oxygen-evolving photosynthesisers; the swap test puts the trap on position, since replacing 'Nostoc' with an unlike prokaryote name leaves the pull standing while no resemblance to 'green sulphur bacteria' is involved.
<!--/ecat-->

## Q129

Biology · botany · Mineral Nutrition

Which of the following elements is responsible for maintaining turgor in cells?

- (1) Magnesium
- **(2)** Potassium
- (3) Sodium
- (4) Calcium

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Potassium helps in maintaining turgidity of cells.

**Solved independently** (answer withheld)

1. Potassium ($\mathrm{K^+}$) helps keep the anion-cation balance in cells and maintains cell turgidity, for example the $\mathrm{K^+}$ influx that makes guard cells turgid when stomata open, so the answer is option $2$.

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q129_1a3d2ee8_03112026.png?v=1a3d2ee89ce5)

Publisher's solution, as printed:

![printed solution 129](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q129_d93dd873_03112026.png?v=d93dd873a15e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Potassium is the element tied to turgidity - anion-cation balance, stomatal movement and cell turgor - while calcium builds the wall and magnesium the chlorophyll ring.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Calcium's printed job is the cell wall and the middle lamella, so reading 'turgor' as the firmness a wall gives lands on the wall-building element.
- **Why:** This question requires the stated function of one macronutrient, demonstrated by the stem's 'responsible for maintaining turgor in cells' matching the printed potassium line; the swap test puts the trap on adjacency of printed functions rather than on name likeness, since 'calcium' and 'potassium' do not resemble each other and the pull survives any rewording.
<!--/ecat-->

## Q130

Biology · botany · Respiration in Plants

What is the role of $\mathrm{NAD^{+}}$ in cellular respiration?

- (1) It functions as an enzyme.
- (2) It is a nucleotide source for ATP synthesis.
- **(3)** It functions as an electron carrier.
- (4) It is the final electron acceptor for anaerobic respiration.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In cellular respiration, $\mathrm{NAD^{+}}$ act as an electron carrier.

**Solved independently** (answer withheld)

1. In glycolysis and the Krebs cycle, dehydrogenases remove hydrogen from substrates and $\mathrm{NAD^{+}}$ accepts it: $\mathrm{XH_2 + NAD^{+} \rightarrow X + NADH + H^{+}}$.
2. $\mathrm{NADH}$ passes its electrons to the electron transport system and is reoxidised to $\mathrm{NAD^{+}}$, so $\mathrm{NAD^{+}}$ acts as an electron carrier, which is option $3$; it is a coenzyme rather than an enzyme (option $1$), not an ATP nucleotide source (option $2$), and not the final acceptor (option $4$).

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q130_08daf4da_03112026.png?v=08daf4da9109)

Publisher's solution, as printed:

![printed solution 130](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q130_6e691ed4_03112026.png?v=6e691ed49911)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NAD+ is a coenzyme that picks up electrons at the oxidative steps of respiration and hands them to the electron transport chain; it is neither an enzyme nor the terminal acceptor.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  The textbook word for NAD+ is coenzyme, and 'enzyme' sits inside that word, so keeping the word without the prefix turns the carrier's job into the catalyst's.
- **Why:** This question requires the stated role of one respiratory cofactor, demonstrated by the keyed option 'It functions as an electron carrier.'; the resemblance test decides the trap axis, because putting an unlike word in place of 'enzyme' kills the pull, so likeness rather than position carries the student.
- **Note:** The pattern returned `statement_options`. The stem is a direct question about one molecule's role and the options are candidate answers, so brief rule 1 keeps the shape at `mcq`.
<!--/ecat-->

## Q131

Biology · botany · Mineral Nutrition

In which of the following forms is iron absorbed by plants?

- **(1)** Ferric
- (2) Free element
- (3) Ferrous
- (4) Both ferric and ferrous

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Iron is absorbed by plants in the form of ferric ions. (According to NCERT)
2. *Plants absorb iron in both form i.e. $\mathrm{Fe^{++}}$ and $\mathrm{Fe^{+++}}$. (Preferably $\mathrm{Fe^{++}}$)

**Solved independently** (answer withheld)

1. NCERT Class 11 (Mineral Nutrition) states that plants obtain iron as ferric ions, $\mathrm{Fe^{3+}}$, so the answer is option $1$ (Ferric).

**Subtopic:** Essential Mineral Elements: Macronutrients and Micronutrients · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q131_c7ee2c0e_03112026.png?v=c7ee2c0eba81)

Publisher's solution, as printed:

![printed solution 131](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q131_57489f21_03112026.png?v=57489f21bd18)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The mineral-nutrition line states that iron is absorbed as ferric ions, Fe3+, which is why iron is listed as the micronutrient taken up in the largest amount.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 3  
  Ferric and ferrous differ by two letters and name the two states of one metal, so 'iron has two states and the reduced one is the biologically active one' lands on the twin of the printed word.
- **Why:** This question requires the stated form in which one nutrient is absorbed, demonstrated by the keyed option 'Ferric'; on the trap axis both likeness and adjacency hold for ferric against ferrous, and section 5.1 gives the win to likeness.
- **Note:** The answer line is printed 'Answer (1*)' and the asterisk is not explained in our record. The tag follows the printed key. Option 3 is defensible on the subject, since root-surface reduction of Fe3+ to Fe2+ precedes uptake in many plants, while the key follows the printed 'absorbed as ferric ions'.
<!--/ecat-->

## Q132

Biology · botany · Plant Kingdom

Winged pollen grains are present in

- (1) Mustard
- (2) Mango
- (3) Cycas
- **(4)** Pinus

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. In Pinus, winged pollen grains are present.
2. It is extended outer exine on two lateral sides to form the wings of pollen.
3. It is the characteristic feature, only in Pinus.
4. Pollen grains of Mustard, Cycas & Mango are not winged shaped.

**Solved independently** (answer withheld)

1. Pinus pollen grains carry two air-filled sacs (wings) that help wind pollination, so the winged pollen belongs to Pinus, which is option $4$.

**Subtopic:** Gymnosperms · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 28)

![printed question 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q132_1da7f614_03112026.png?v=1da7f6140888)

Publisher's solution, as printed:

![printed solution 132](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q132_40d47347_03112026.png?v=40d47347295e)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Pinus pollen carries two air-filled wings that keep it aloft for wind pollination; no other group on this list has them.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Cycas is the other gymnosperm the chapter names beside Pinus, so holding winged pollen as a gymnosperm feature rather than a pine feature lets either of the two serve.
- **Why:** This question requires the stated owner of one pollen character, demonstrated by the stem 'Winged pollen grains are present in' with four coordinate plant names and no criterion printed to apply; the swap test puts the trap on position, since exchanging 'Cycas' for an unlike gymnosperm name leaves the pull intact.
<!--/ecat-->

## Q133

Biology · botany · Biological Classification

After karyogamy followed by meiosis, spores are produced exogenously in

- (1) Neurospora
- **(2)** Agaricus
- (3) Alternaria
- (4) Saccharomyces

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. In Agaricus (a genus of basidiomycetes), basidiospores or meiospores are produced exogenously.
2. Neurospora (a genus of ascomycetes) produces ascospores as meiospores but endogenously inside the ascus.)
3. Alternaria (a genus of deuteromycetes) does not produce sexual spores.
4. Saccharomyces (Unicellular ascomycetes) produces ascospores, endogenously.

**Solved independently** (answer withheld)

1. In basidiomycetes such as $\textit{Agaricus}$, karyogamy and meiosis take place in the basidium, and the four basidiospores are produced exogenously on it.
2. In ascomycetes such as $\textit{Neurospora}$ and $\textit{Saccharomyces}$, the ascospores produced after karyogamy and meiosis are endogenous, formed inside the ascus.
3. $\textit{Alternaria}$ is a deuteromycete with no known sexual stage, so it has no karyogamy and meiosis at all.
4. So exogenous spores after karyogamy and meiosis occur in $\textit{Agaricus}$, which is option $2$.

**Subtopic:** Basidiomycetes · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q133_e7fed941_03112026.png?v=e7fed9410844)

Publisher's solution, as printed:

![printed solution 133](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q133_a715be1f_03112026.png?v=a715be1f9f38)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Basidiomycetes form basidiospores on the outside of the basidium after karyogamy and meiosis, while ascomycete spores are formed inside the sac-like ascus.
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 3  
  Alternaria's conidia are borne on the outside of the hypha, so anchoring on 'exogenously' and letting the clause 'after karyogamy followed by meiosis' go lands on the fungus whose spores are externally produced but asexual.
- **Why:** This question requires one stated fungal property under a stated condition, demonstrated by the stem's 'After karyogamy followed by meiosis, spores are produced exogenously', which option 3 satisfies only in its second half.
<!--/ecat-->

## Q134

Biology · botany · Plant Kingdom

Which one is wrongly matched?

- **(1)** Uniflagellate gametes – Polysiphonia
- (2) Gemma cups – Marchantia
- (3) Biflagellate zoospores – Brown algae
- (4) Unicellular organism – Chlorella

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Polysiphonia is a genus of red algae, where asexual spores and gametes are non-motile or non-flagellated.
2. Other options (2, 3 & 4) are correctly matched

**Solved independently** (answer withheld)

1. Polysiphonia belongs to Rhodophyceae (red algae), which have no flagellated stages, so its gametes are non-motile and the pairing 'Uniflagellate gametes – Polysiphonia' is wrong.
2. Marchantia reproduces asexually by gemmae formed in gemma cups, so option $2$ is correctly matched.
3. Brown algae (Phaeophyceae) form pear-shaped biflagellate zoospores with two unequal, laterally attached flagella, so option $3$ is correctly matched.
4. Chlorella is a unicellular green alga, so option $4$ is correctly matched.
5. The only wrong match is option $1$.

**Subtopic:** Rhodophyceae · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q134_a51cb65f_03112026.png?v=a51cb65fa6be)

Publisher's solution, as printed:

![printed solution 134](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q134_419e6b33_03112026.png?v=419e6b33aad1)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Red algae such as Polysiphonia reproduce without flagella, so 'uniflagellate gametes' cannot belong to them, while gemma cups, biflagellate zoospores and unicellularity sit correctly with Marchantia, the brown algae and Chlorella.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Two flagella are also the printed character of the green algae, so filing 'biflagellate' under Chlorophyceae makes the brown-algal pairing read as the misfit.
- **Why:** This question requires each printed pairing to be checked against the stated character of its group, demonstrated by the keyed option 'Uniflagellate gametes - Polysiphonia' naming a red alga whose reproduction is non-motile.
- **Note:** The pattern returned `statement_options`. The stem is a bare instruction and each option is a pairing graded whole, the retired `pair_options`/`statement_options` shape that `category_retired.qtype` maps to `statements`.
<!--/ecat-->

## Q135

Biology · botany · The Living World

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Herbarium | (i) | It is a place having a collection of preserved plants and animals |
| b | Key | (ii) | A list that enumerates methodically all the species found in an area with brief description aiding identification |
| c | Museum | (iii) | Is a place where dried and pressed plant specimens mounted on sheets are kept |
| d | Catalogue | (iv) | A booklet containing a list of characters and their alternates which are helpful in identification of various taxa. |

- (1) (i) (iv) (iii) (ii)
- (2) (ii) (iv) (iii) (i)
- (3) (iii) (ii) (i) (iv)
- **(4)** (iii) (iv) (i) (ii)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Herbarium – Dried and pressed plant specimen
2. Key – Identification of various taxa
3. Museum – Plant and animal specimen are preserved
4. Catalogue – Alphabetical listing of species

**Solved independently** (answer withheld)

1. Herbarium (a) is a store of dried, pressed plant specimens mounted on sheets, so $a \rightarrow (iii)$.
2. Key (b) is a booklet of characters and their alternates used to identify taxa, so $b \rightarrow (iv)$.
3. Museum (c) is a place with a collection of preserved plants and animals, so $c \rightarrow (i)$.
4. Catalogue (d) is a methodical list of all species found in an area with brief descriptions, so $d \rightarrow (ii)$.
5. The sequence $(iii),(iv),(i),(ii)$ matches option $4$.

**Subtopic:** Taxonomy and Systematics · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 28)

![printed question 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q135_ca3876ab_03112026.png?v=ca3876ab65ff)

Publisher's solution, as printed:

![printed solution 135](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q135_84d14f77_03112026.png?v=84d14f7731e2)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Herbarium, key, museum and catalogue are four distinct taxonomic aids: two are places that hold specimens, two are documents, and only the key works by contrasting characters
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 3  
  The closing phrase of (ii), 'aiding identification', is the job a key is remembered for, so a student hands (ii) to the Key and is left giving the catalogue (iv) — both places then read correctly and only the two documents are crossed.
- **Why:** This question requires the definition NCERT prints for each taxonomic aid, demonstrated by Column II spelling them out: 'Is a place where dried and pressed plant specimens mounted on sheets are kept'.
<!--/ecat-->

## Q136

Biology · zoology · Chemical Coordination and Integration

Which of the following is an amino acid derived hormone?

- **(1)** Epinephrine
- (2) Estradiol
- (3) Ecdysone
- (4) Estriol

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Epinephrine is derived from tyrosine amino acid by the removal of carboxyl group.
2. It is a catecholamine.

**Solved independently** (answer withheld)

1. Epinephrine is an amino acid derivative (made from tyrosine), while estradiol, ecdysone and estriol are all steroid hormones, so the answer is option $1$.

**Subtopic:** Mechanism of Hormone Action and Chemical Nature of Hormones · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q136_ddff0562_03112026.png?v=ddff0562f16f)

Publisher's solution, as printed:

![printed solution 136](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q136_30b01125_03112026.png?v=30b01125a9c8)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The hormone-chemistry line sorts hormones into amino-acid derivatives such as epinephrine, peptides and proteins, steroids such as estradiol and cortisol, and iodothyronines.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Estradiol is printed in the same sentence as epinephrine, as the steroid example, so keeping the list of examples without which class each belongs to lands on the neighbouring name.
- **Why:** This question requires the stated chemical class of a named hormone, demonstrated by the keyed 'Epinephrine' standing against three steroid-nucleus hormones; the swap test puts the trap on position, since exchanging 'Estradiol' for an unlike steroid name leaves the pull from the shared printed sentence standing.
<!--/ecat-->

## Q137

Biology · zoology · Neural Control and Coordination

Which of the following structures or regions is incorrectly paired with its functions?

- (1) Medulla oblongata : controls respiration and cardiovascular reflexes.
- (2) Hypothalamus : production of releasing hormones and regulation of temperature, hunger and thirst.
- **(3)** Limbic system : consists of fibre tracts that interconnect different  regions of brain; controls movement.
- (4) Corpus callosum : band of fibers connecting left and right cerebral hemispheres.

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Limbic system is emotional brain.
2. It controls all emotions in our body but not movements.

**Solved independently** (answer withheld)

1. Medulla oblongata controls respiration, cardiovascular reflexes and gastric secretions, so option $1$ is correctly paired.
2. Hypothalamus makes releasing hormones and regulates body temperature, hunger and thirst, so option $2$ is correctly paired.
3. Corpus callosum is the band of nerve fibres that connects the left and right cerebral hemispheres, so option $4$ is correctly paired.
4. Limbic system (amygdala, hippocampus and related deep structures) regulates sexual behaviour, emotional reactions and motivation; it is not a set of interconnecting fibre tracts and does not control movement, so option $3$ is incorrectly paired.

**Subtopic:** Forebrain · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 29)

![printed question 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q137_67f68c5c_03112026.png?v=67f68c5c2116)

Publisher's solution, as printed:

![printed solution 137](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q137_9e85353a_03112026.png?v=9e85353a617a)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each brain region carries its own printed job: medulla for respiration and cardiovascular reflexes, hypothalamus for releasing hormones and for temperature, hunger and thirst, corpus callosum as the fibre band between the hemispheres, and the limbic system for emotion and motivation rather than movement.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  Releasing hormones are easy to file under the pituitary, the gland printed next to the hypothalamus, so holding hormone production as the pituitary's business marks the hypothalamus pairing as the wrong one.
- **Why:** This question requires each printed structure-to-function pairing to be matched against the stated one, demonstrated by option 3 attaching a fibre-tract description and 'controls movement' to the limbic system, which the text ties to emotional reactions and motivation.
- **Note:** The pattern returned `statement_options`. The stem is a bare instruction and each option is a structure-to-function pairing graded whole, which `category_retired.qtype` maps to `statements`.
<!--/ecat-->

## Q138

Biology · zoology · Neural Control and Coordination

The transparent lens in the human eye is held in its place by

- **(1)** ligaments attached to the ciliary body
- (2) smooth muscles attached to the iris
- (3) ligaments attached to the iris
- (4) smooth muscles attached to the ciliary body

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Lens in the human eye is held in its place by suspensory ligaments attached to the ciliary body.

**Solved independently** (answer withheld)

1. The crystalline lens is suspended by ligaments (suspensory ligaments) that attach it to the ciliary body, so the answer is option $1$.

**Subtopic:** Sense Organs: The Eye · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 29)

![printed question 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q138_ccafb72c_03112026.png?v=ccafb72c4f3e)

Publisher's solution, as printed:

![printed solution 138](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q138_e864f1d0_03112026.png?v=e864f1d07847)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The lens sits in a capsule slung from the ciliary body by suspensory ligaments; the ciliary muscle alters its curvature but is not what holds it in place.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  The ciliary muscle is the part remembered as acting on the lens during accommodation, so the right structure arrives with the wrong tissue - muscle in place of ligament.
- **Why:** This question requires the stated attachment of the lens, demonstrated by the four options crossing two tissues, 'ligaments' and 'smooth muscles', with two structures, 'ciliary body' and 'iris', so that each wrong option keeps one half of the keyed answer.
- **Note:** The pattern returned `statement_options`; the options are short noun phrases answering one question, so brief rule 1 keeps the shape at `mcq`.
<!--/ecat-->

## Q139

Biology · zoology · Chemical Coordination and Integration

Which of the following hormones can play a significant role in osteoporosis?

- (1) Aldosterone and Prolactin
- **(2)** Estrogen and Parathyroid hormone
- (3) Progesterone and Aldosterone
- (4) Parathyroid hormone and Prolactin

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Estrogen promotes the activity of osteoblast and inhibits osteoclast.
2. In an ageing female osteoporosis occurs due to deficiency of estrogen.
3. Parathormone promotes mobilisation of calcium from bone into blood.
4. Excessive activity of parathormone causes demineralisation leading to osteoporosis.

**Solved independently** (answer withheld)

1. Osteoporosis is an age-related disorder of decreased bone mass, and a fall in $\text{estrogen}$ is a common cause.
2. $\text{PTH}$ raises blood $\text{Ca}^{2+}$ by stimulating bone resorption (demineralisation), so excess PTH also reduces bone mass.
3. Aldosterone (Na$^+$/water balance), prolactin (milk production) and progesterone (pregnancy support) play no significant role in bone mass, so the answer is option $2$.

**Subtopic:** Thyroid Gland and Parathyroid Gland, Gonads · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 29)

![printed question 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q139_bab2c771_03112026.png?v=bab2c771b777)

Publisher's solution, as printed:

![printed solution 139](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q139_54376ef0_03112026.png?v=54376ef0bdbc)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Osteoporosis is the loss of bone mass that follows the fall in estrogen after menopause, and excess parathyroid hormone does the same thing by resorbing bone to raise blood calcium.
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Parathyroid hormone is the printed bone-resorbing hormone, so this option carries the half a student is sure of and prolactin rides in on it unchecked.
- **Why:** This question requires both hormones named in one option to be tied to bone loss, demonstrated by the keyed 'Estrogen and Parathyroid hormone', where half an option right scores nothing.
- **Note:** The pattern returned `plain_mcq`, but each option is a pair of hormones accepted or rejected whole - the retired `pair_options` shape, which `category_retired.qtype` maps to `statements`. Recorded as the shape on the page, as the brief directs.
<!--/ecat-->

## Q140

Biology · zoology · Evolution

Among the following sets of examples for divergent evolution, select the incorrect option :

- (1) Forelimbs of man, bat and cheetah
- (2) Brain of bat, man and cheetah
- (3) Heart of bat, man and cheetah
- **(4)** Eye of octopus, bat and man

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Divergent evolution occurs in the same structure, example - forelimbs, heart, brain of vertebrates which have developed along different directions due to adaptation to different needs whereas eye of octopus, bat and man are examples of analogous organs showing convergent evolution.

**Solved independently** (answer withheld)

1. Divergent evolution produces homologous organs: the same basic structure adapted to different functions.
2. Forelimbs, brain and heart of bat, man and cheetah share a common vertebrate origin, so options $1$, $2$ and $3$ are homologous and correct examples.
3. The eye of an octopus (mollusc) and of mammals (bat, man) are analogous, a result of convergent evolution, so option $4$ is the incorrect example.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 29)

![printed question 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q140_7d0e01ea_03112026.png?v=7d0e01ea6eba)

Publisher's solution, as printed:

![printed solution 140](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q140_f155328c_03112026.png?v=f155328c4de7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Divergent evolution shows up as homologous organs — one ancestral structure in many vertebrates put to different uses; similar eyes in octopus and mammals are analogous, built independently
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Forelimbs of man, bat and cheetah is the set the chapter prints for divergent evolution, so reading the stem as 'pick an example of divergent evolution' lands here; the stem asks for the set that is not one.
- **Why:** This question requires the taught lists of homologous and analogous examples, demonstrated by 'Eye of octopus, bat and man' being the only printed set the source files under analogy.
- **Note:** E1 read this as statement_options; the options are organ-plus-organism sets, not statements to be judged, so the printed shape recorded here is a plain MCQ.
<!--/ecat-->

## Q141

Biology · zoology · Human Health and Disease

Which of the following is not an autoimmune disease?

- (1) Psoriasis
- **(2)** Alzheimer's disease
- (3) Rheumatoid arthritis
- (4) Vitiligo

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Rheumatoid arthritis is an autoimmune disorder in which antibodies are produced against the synovial membrane and cartilage.
2. Vitiligo causes white patches on skin also characterised as autoimmune disorder.
3. Psoriasis is a skin disease that causes itchy or sore patches of thick red skin and is also autoimmune whereas Alzheimer's disease is due to deficiency of neurotransmitter acetylcholine.

**Solved independently** (answer withheld)

1. Psoriasis, rheumatoid arthritis and vitiligo are autoimmune diseases, but Alzheimer's disease is a neurodegenerative disorder that is not autoimmune, so the answer is option $2$.

**Subtopic:** Allergies and Autoimmunity · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 29)

![printed question 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q141_12c64fe9_03112026.png?v=12c64fe913f6)

Publisher's solution, as printed:

![printed solution 141](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q141_e69bcb0d_03112026.png?v=e69bcb0d9f76)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Autoimmunity is the immune system attacking the body's own molecules; Alzheimer's disease is neurodegenerative, caused by protein deposits and neuron loss rather than by self-attack
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  Rheumatoid arthritis is the one autoimmune disease the chapter names, so answering 'which of these IS autoimmune' marks it and the lower-case 'not' is never spent.
- **Why:** This question requires the stated membership of the autoimmune group, demonstrated by the stem's 'is not an autoimmune disease' set over three self-attack disorders and one neurodegenerative one.
<!--/ecat-->

## Q142

Biology · zoology · Principles of Inheritance and Variation

Which of the following characteristics represent ‘Inheritance of blood groups’ in humans?

- **(a)** Dominance
- **(b)** Co-dominance
- **(c)** Multiple allele
- **(d)** Incomplete dominance
- **(e)** Polygenic inheritance

- (1) b, c and e
- (2) b, d and e
- **(3)** a, b and c
- (4) a, c and e

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. $\mathrm{I^{A}I^{O}}$, $\mathrm{I^{B}I^{O}}$ - Dominant–recessive relationship
2. $\mathrm{I^{A}I^{B}}$ - Codominance
3. $\mathrm{I^{A}}$, $\mathrm{I^{B}}$ & $\mathrm{I^{O}}$ - 3-different allelic forms of a gene (multiple allelism)

**Solved independently** (answer withheld)

1. ABO blood groups are controlled by a single gene $I$ with three alleles $I^A$, $I^B$ and $i$, so they show multiple alleles (c).
2. In $I^A I^B$ individuals both alleles are expressed, giving group AB, which is co-dominance (b).
3. $I^A$ and $I^B$ are each completely dominant over $i$ ($I^A i \to A$, $I^B i \to B$), which is dominance (a).
4. Only one gene is involved and no heterozygote shows an intermediate phenotype, so polygenic inheritance (e) and incomplete dominance (d) do not apply.
5. Correct set is $a, b$ and $c$, which is option $3$.

**Subtopic:** Incomplete Dominance & Co-dominance, Pleiotropy, Multiple Alleles & Polygenic Inheritance · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 30)

![printed question 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q142_8746bef0_03112026.png?v=8746bef06f00)

Publisher's solution, as printed:

![printed solution 142](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q142_2c442778_03112026.png?v=2c4427789a40)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** ABO blood grouping is one gene with three alleles, in which I-A and I-B are co-dominant with each other and both are dominant over i
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Co-dominance and multiple alleles are the two things the ABO case is printed for, so an option carrying both reads as already two-thirds checked; the third letter, polygenic inheritance, comes from reading 'more than two alleles' as 'more than one gene'.
- **Why:** This question requires the phenomena the source attributes to ABO inheritance, demonstrated by the stem's 'represent ‘Inheritance of blood groups’ in humans' set over a lettered block of five named phenomena.
- **Note:** The lettered block a–e printed above the options fixes the shape as statements. The block is built from two near-neighbour pairs — co-dominance against incomplete dominance, multiple allele against polygenic inheritance — but each letter is still settled by what the source states about ABO, so asks is fact_line and not compare.
<!--/ecat-->

## Q143

Biology · zoology · Human Health and Disease

In which disease does mosquito transmitted pathogen cause chronic inflammation of lymphatic vessels?

- **(1)** Elephantiasis
- (2) Ringworm disease
- (3) Ascariasis
- (4) Amoebiasis

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Elephantiasis is caused by roundworm, Wuchereria bancrofti and it is transmitted by Culex mosquito.

**Solved independently** (answer withheld)

1. Elephantiasis (filariasis) is caused by the filarial worms $Wuchereria$ ($W.\ bancrofti$, $W.\ malayi$), transmitted by the bite of the female $Culex$ mosquito, and they cause chronic inflammation of the lymphatic vessels, so the answer is option $1$; ringworm, ascariasis and amoebiasis are not mosquito-borne.

**Subtopic:** Filarial Diseases · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q143_382be1be_03112026.png?v=382be1befbd5)

Publisher's solution, as printed:

![printed solution 143](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q143_36fe76ab_03112026.png?v=36fe76abdb9b)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Filariasis, or elephantiasis, is caused by Wuchereria worms carried by female mosquitoes, which live in the lymphatic vessels of the lower limbs and inflame them for years
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Ascariasis is the other round-worm disease and it is printed immediately before elephantiasis in the chapter's disease list, so holding 'worm, chronic, inflammation' without the vector stops a student at the neighbour.
- **Why:** This question requires the disease the source ties to a mosquito-borne worm, demonstrated by the stem's 'chronic inflammation of lymphatic vessels'.
- **Note:** nearby_fact against look_alike_term: swapping 'Ascariasis' for an unlike word leaves the pull standing, because what carries the student is the disease printed beside elephantiasis in the same list, not any likeness in the name.
<!--/ecat-->

## Q144

Biology · zoology · Evolution

The similarity of bone structure in the forelimbs of many vertebrates is an example of

- **(1)** Homology
- (2) Convergent evolution
- (3) Analogy
- (4) Adaptive radiation

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. In different vertebrates, bones of forelimbs are similar but their forelimbs are adapted in different way as per their adaptation, hence example of homology.

**Solved independently** (answer withheld)

1. Vertebrate forelimbs (e.g. whale flipper, bat wing, human arm, cheetah limb) have the same underlying bone pattern from a common ancestor but serve different functions, so they are homologous organs; this is homology, option $1$.

**Subtopic:** Homology and Analogy · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q144_31c243f4_03112026.png?v=31c243f46bb3)

Publisher's solution, as printed:

![printed solution 144](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q144_c6323228_03112026.png?v=c632322854ff)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homologous organs share one ancestral structure whatever their present function; analogy is similar function reached independently in unrelated animals
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Analogy is the term printed next to homology and defined against it, so a student who carries the pair without which half is which sends a structural resemblance to analogy.
- **Why:** This question requires the term the source attaches to its own forelimb example, demonstrated by the stem quoting 'the similarity of bone structure in the forelimbs of many vertebrates'.
- **Note:** nearby_fact against look_alike_term: replace 'homology' and 'analogy' with two unlike words and the pull survives, because the two concepts are taught as a facing pair and position rather than likeness carries the student.
<!--/ecat-->

## Q145

Biology · botany · Microbes in Human Welfare

Conversion of milk to curd improves its nutritional value by increasing the amount of

- (1) Vitamin D
- **(2)** Vitamin $\mathrm{B_{12}}$
- (3) Vitamin A
- (4) Vitamin E

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Curd is more nourishing than milk.
2. It has enriched presence of vitamins specially Vit-$\mathrm{B_{12}}$.

**Solved independently** (answer withheld)

1. Lactic acid bacteria (LAB) such as $\mathit{Lactobacillus}$ convert milk to curd, and they also increase its vitamin $\mathrm{B_{12}}$ content, so the answer is option $2$.

**Subtopic:** Microbes in Household Products · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q145_4a996132_03112026.png?v=4a9961323e7e)

Publisher's solution, as printed:

![printed solution 145](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q145_18f2b4ce_03112026.png?v=18f2b4ce51ec)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lactic acid bacteria curdle milk and raise its vitamin B12, which is why curd is more nutritious than the milk it was made from
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 1  
  Milk is the food vitamin D is tabulated with, fortified milk being its standard dietary source, so keying on 'milk' rather than on the curdling answers a question about milk instead of about the conversion.
- **Why:** This question requires the gain the source credits to lactic acid bacteria, demonstrated by the stem's 'improves its nutritional value by increasing the amount of'.
<!--/ecat-->

## Q146

Biology · botany · Organisms and Populations

Which one of the following population interactions is widely used in medical science for the production of antibiotics?

- (1) Commensalism
- (2) Parasitism
- (3) Mutualism
- **(4)** Amensalism

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Amensalism/Antibiosis $(0, -)$
2. Antibiotics are chemicals secreted by one microbial group (eg : Penicillium) which harm other microbes (eg : Staphylococcus)
3. It has no effect on Penicillium or the organism which produces it.

**Solved independently** (answer withheld)

1. An antibiotic-producing microbe (e.g. $Penicillium$) secretes a chemical that inhibits or kills bacteria while the producer itself is neither benefited nor harmed, i.e. an interaction of type $(0, -)$, which is amensalism, option $4$.

**Subtopic:** Commensalism and Ammensalism · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 30)

![printed question 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q146_dcb31062_03112026.png?v=dcb31062293f)

Publisher's solution, as printed:

![printed solution 146](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q146_8bd03aff_03112026.png?v=8bd03aff91c5)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** Amensalism is the (−, 0) interaction: one species is harmed while the other neither gains nor loses, which is what a mould's antibiotic does to bacteria
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  Commensalism and amensalism differ by three letters and both are the 'one partner unaffected' boxes of the interaction table, so recalling only 'one of them is unaffected' leaves either available; commensalism is (+, 0), with that partner benefiting rather than harmed.
- **Why:** This question requires the interaction table's sign pattern applied to a case the book does not list, demonstrated by the stem naming only 'the production of antibiotics' and no interaction.
- **Note:** look_alike_term against nearby_fact: the two names resemble each other and are also neighbouring rows of the same table, and the rulebook gives the resemblance the win — swapping them for unlike words would cost the pull its force.
<!--/ecat-->

## Q147

Biology · botany · Biodiversity and Conservation

All of the following are included in ‘ex-situ conservation’ except

- (1) Wildlife safari parks
- (2) Botanical gardens
- **(3)** Sacred groves
- (4) Seed banks

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Sacred groves – in-situ conservation.
2. Represent pristine forest patch as protected by Tribal groups.

**Solved independently** (answer withheld)

1. Ex-situ conservation keeps threatened species away from their natural habitat, as in wildlife safari parks, botanical gardens and seed banks (options $1$, $2$, $4$).
2. Sacred groves protect forest patches and their species where they grow naturally, which makes them in-situ conservation, so the exception is option $3$.

**Subtopic:** Ex Situ Conservation, In Situ Conservation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 30)

![printed question 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q147_0361787b_03112026.png?v=0361787bf7ac)

Publisher's solution, as printed:

![printed solution 147](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q147_f3b3493c_03112026.png?v=f3b3493ce961)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Ex-situ conservation keeps the organism away from its natural habitat — zoos, safari parks, botanical gardens, seed banks — while sacred groves are patches protected where they stand, which makes them in-situ
- **Trap:** **Condition dropped** (`condition_missed`) — drop the condition the stem states and the option becomes true — option 1  
  The criterion 'ex-situ' is tested by whether the setting looks like open country, and a wildlife safari park does, so it gets picked as the exception; the enclosure is man-made, which is what puts it in the ex-situ list.
- **Why:** This question requires the membership of the ex-situ list as NCERT states it, demonstrated by 'All of the following are included in 'ex-situ conservation' except' with four named conservation measures and no criterion spelt out in the stem.
<!--/ecat-->

## Q148

Biology · botany · Environmental Issues

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Eutrophication | i | UV-B radiation |
| b | Sanitary landfill | ii | Deforestation |
| c | Snow blindness | iii | Nutrient enrichment |
| d | Jhum cultivation | iv | Waste disposal |

- (1) ii i iii iv
- **(2)** iii iv i ii
- (3) i iii iv ii
- (4) i ii iv iii

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. a. Eutrophication iii. Nutrient enrichment
2. b. Sanitary landfill iv. Waste disposal
3. c. Snow blindness i. UV-B radiation
4. d. Jhum cultivation ii. Deforestation

**Solved independently** (answer withheld)

1. Eutrophication is the nutrient enrichment of a water body, so $a \rightarrow iii$.
2. A sanitary landfill is a method of solid waste disposal, so $b \rightarrow iv$.
3. Snow blindness is inflammation of the cornea caused by high doses of UV-B radiation, so $c \rightarrow i$.
4. Jhum (slash-and-burn) cultivation clears forest, so it leads to deforestation, $d \rightarrow ii$.
5. The sequence $a$-$iii$, $b$-$iv$, $c$-$i$, $d$-$ii$ reads iii iv i ii, which is option $2$.

**Subtopic:** Water Pollution and Its Control, Ozone Depletion in the Stratosphere · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 30)

![printed question 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q148_7a0c87e1_03112026.png?v=7a0c87e1d0c5)

Publisher's solution, as printed:

![printed solution 148](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q148_dfcc2ed6_03112026.png?v=dfcc2ed6b714)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each environmental issue carries its own cause: nutrient enrichment drives eutrophication, a sanitary landfill is a waste-disposal route, UV-B causes snow blindness, and jhum cultivation clears forest
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All three wrong codes were checked row by row. Each one has to break a pairing the printed words give away — 'Eutrophication' against 'Nutrient enrichment', 'Sanitary landfill' against 'Waste disposal' — and no code swaps only the two rows a student could genuinely confuse.
- **Why:** This question requires the cause NCERT names for each issue, demonstrated by Column II being bare causes: 'UV-B radiation', 'Nutrient enrichment'.
<!--/ecat-->

## Q149

Biology · botany · Organisms and Populations

In a growing population of a country,

- **(1)** pre-reproductive individuals are more than the reproductive individuals.
- (2) reproductive and pre-reproductive individuals are equal in number.
- (3) reproductive individuals are less than the post-reproductive individuals.
- (4) pre-reproductive individuals are less than the reproductive individuals.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Whenever the pre-reproductive individuals or the younger population size is larger than the reproductive group, the population will be an increasing population.

**Solved independently** (answer withheld)

1. In a growing (expanding) population the age pyramid is triangular with a broad base, so the pre-reproductive group is the largest and outnumbers the reproductive group, which is option $1$.

**Subtopic:** Life History Variation and Population Attributes · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 31)

![printed question 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q149_b2911a3f_03112026.png?v=b2911a3f9e5f)

Publisher's solution, as printed:

![printed solution 149](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q149_3d2b598a_03112026.png?v=3d2b598a992d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** An age pyramid with a broad base — more pre-reproductive than reproductive individuals — is what a growing population looks like; equal classes give a stable population and a narrow base a declining one
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Reading 'growing' as 'plenty of adults of child-bearing age' puts the reproductive class on top and prints the exact inverse of the key, which is in fact the declining pyramid's shape.
- **Why:** This question requires the age-pyramid rule carried over to a stated case, demonstrated by the stem's condition 'In a growing population of a country' and four rival inequalities between age classes.
- **Note:** E1 recorded statement_options from the full-sentence options. Under the current qtype axis long sentences as options do not make a question statements — the stem neither asks for statements to be judged nor prints a lettered list — so the shape here is mcq.
<!--/ecat-->

## Q150

Biology · zoology · Human Health and Disease

Which part of poppy plant is used to obtain the drug “Smack”?

- (1) Flowers
- (2) Roots
- **(3)** Latex
- (4) Leaves

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. ‘Smack’ also called as brown sugar/Heroin is formed by acetylation of morphine.
2. It is obtained from the latex of unripe capsule of Poppy plant.

**Solved independently** (answer withheld)

1. Smack is heroin, i.e. diacetylmorphine, obtained by acetylation of morphine; morphine is extracted from the latex of the poppy plant $\textit{Papaver somniferum}$, so the part used is latex, which is option $3$.

**Subtopic:** Drugs and Alcohol (Cocaine, Opioids, Cannabinoids) · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 31)

![printed question 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q150_a8c8cc11_03112026.png?v=a8c8cc11ec2b)

Publisher's solution, as printed:

![printed solution 150](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q150_5b4bcbe2_03112026.png?v=5b4bcbe2f31a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Smack, or heroin, is made by acetylating morphine, which is extracted from the latex of the poppy Papaver somniferum
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  In the same drugs paragraph the plant part named is a flower — cannabinoids come from the flower tops of Cannabis — so the organ printed next door is carried over to the poppy, whose own showy flower makes it read as the obvious source.
- **Why:** This question requires the plant part NCERT names as the source of the drug, demonstrated by 'Which part of poppy plant is used to obtain the drug "Smack"?' with four plant parts as options.
- **Note:** Swap test applied: latex and flowers are unlike words, and the route to option 1 survives any renaming because what carries it is the flower top being the plant part printed beside the poppy sentence. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q151

Biology · zoology · Human Reproduction

Hormones secreted by the placenta to maintain pregnancy are

- (1) hCG, hPL, progestogens, prolactin
- **(2)** hCG, hPL, progestogens, estrogens
- (3) hCG, hPL, estrogens, relaxin, oxytocin
- (4) hCG, progestogens, estrogens, glucocorticoids

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Placenta releases human chorionic gonadotropic hormone (hCG) which stimulates the Corpus luteum during pregnancy to release estrogen and progesterone and also rescues corpus luteum from regression.
2. Human placental lactogen (hPL) is involved in growth of body of mother and breast.
3. Progesterone maintains pregnancy, keeps the uterus silent by increasing uterine threshold to contractile stimuli.

**Solved independently** (answer withheld)

1. NCERT states that during pregnancy the placenta acts as an endocrine tissue secreting hCG, hPL, estrogens and progestogens, so option $2$ matches exactly, while options $1$, $3$ and $4$ include prolactin, relaxin/oxytocin or glucocorticoids, which come from other glands.

**Subtopic:** Pregnancy, Parturition, and Lactation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 31)

![printed question 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q151_10bff10a_03112026.png?v=10bff10adbd6)

Publisher's solution, as printed:

![printed solution 151](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q151_63b1c9b6_03112026.png?v=63b1c9b6bf6e)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The placenta acts as an endocrine tissue and secretes hCG, hPL, estrogens and progestogens; relaxin comes from the ovary late in pregnancy and oxytocin and prolactin from the pituitary
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 1  
  Three of the four names are the key's own and only estrogens has been replaced by prolactin, which hPL — human placental lactogen — appears to vouch for, since a lactation hormone in a placental list reads as consistent.
- **Why:** This question requires the membership of the printed list of placental hormones, demonstrated by 'Hormones secreted by the placenta to maintain pregnancy are' with options that are whole sets of four or five hormone names.
- **Note:** Each option here is a set of names accepted or rejected whole — the codebook's pair_options shape, where half an option scores nothing. Of the six qtype values, two_part is the one that records an answer needing several items all right together; mcq would hide that.
<!--/ecat-->

## Q152

Biology · zoology · Reproductive Health

The contraceptive ‘SAHELI’

- **(1)** blocks estrogen receptors in the uterus, preventing eggs from getting implanted.
- (2) is an IUD.
- (3) increases the concentration of estrogen and prevents ovulation in females.
- (4) is a post-coital contraceptive.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Saheli is the first non-steroidal, once a week pill.
2. It contains centchroman and its functioning is based upon selective Estrogen Receptor modulation.

**Solved independently** (answer withheld)

1. Saheli is a non-steroidal, once-a-week oral contraceptive pill (centchroman) that blocks estrogen receptors in the uterus and so prevents implantation; it is not an IUD, does not raise estrogen and is not post-coital, so the answer is option $1$.

**Subtopic:** Artificial Contraceptive Methods · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 31)

![printed question 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q152_e2249332_03112026.png?v=e224933289bb)

Publisher's solution, as printed:

![printed solution 152](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q152_63df94fb_03112026.png?v=63df94fbd069)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Saheli is a non-steroidal once-a-week oral pill that blocks estrogen receptors in the uterus and so prevents implantation, unlike the steroidal pills that work by inhibiting ovulation
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The mechanism printed for oral contraceptives in general — they inhibit ovulation — sits beside the Saheli sentence, so it is carried onto the one pill in the account that is non-steroidal and works on implantation instead.
- **Why:** This question requires the stated description of one named contraceptive, demonstrated by the bare stem 'The contraceptive 'SAHELI'' with four rival claims about what it is and how it acts.
<!--/ecat-->

## Q153

Biology · zoology · Human Reproduction

The amnion of mammalian embryo is derived from

- **(1)** ectoderm and mesoderm
- (2) mesoderm and trophoblast
- (3) endoderm and mesoderm
- (4) ectoderm and endoderm

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The extraembryonic or foetal membranes are amnion, chorion, allantois and Yolk sac.
2. Amnion is formed from mesoderm on outer side and ectoderm on inner side.
3. Chorion is formed from trophoectoderm and mesoderm whereas allantois and Yolk sac membrane have mesoderm on outerside and endoderm in inner side.

**Solved independently** (answer withheld)

1. The amnion of amniotes, mammals included, forms from the $\text{somatopleure}$.
2. $\text{somatopleure} = \text{ectoderm} + \text{somatic mesoderm}$, so the amnion comes from ectoderm and mesoderm, which is option $1$.

**Subtopic:** Implantation and Embryonic Development · **Difficulty:** hard (2 steps)

**Printed in the booklet** (page 31)

![printed question 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q153_b99bcc87_03112026.png?v=b99bcc878af4)

Publisher's solution, as printed:

![printed solution 153](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q153_96f11a69_03112026.png?v=96f11a69b56a)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The amnion is formed from the somatopleure — ectoderm with somatic mesoderm — while the chorion adds mesoderm to the trophoblast and the yolk sac and allantois come from endoderm with mesoderm
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 2  
  Mesoderm with trophoblast is the true derivation of the chorion, the other membrane of the same embryo, so the option is a correct answer to a question the stem did not ask.
- **Why:** This question requires the germ layers NCERT assigns to one named membrane, demonstrated by 'The amnion of mammalian embryo is derived from' with four pairings of germ layers as options.
<!--/ecat-->

## Q154

Biology · zoology · Human Reproduction

The difference between spermiogenesis and spermiation is

- (1) In spermiogenesis spermatids are formed, while in spermiation spermatozoa are formed.
- (2) In spermiogenesis spermatozoa from sertoli cells are released into the cavity of seminiferous tubules, while in spermiation spermatozoa are formed.
- (3) In spermiogenesis spermatozoa are formed, while in spermiation spermatids are formed.
- **(4)** In spermiogenesis spermatozoa are formed, while in spermiation spermatozoa are released from sertoli cells into the cavity of seminiferous tubules.

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Spermiogenesis is transformation of spermatids into spermatozoa whereas spermiation is the release of the sperms from sertoli cells into the lumen of seminiferous tubule.

**Solved independently** (answer withheld)

1. Spermiogenesis is the transformation of spermatids into spermatozoa, and spermiation is the release of the spermatozoa from the Sertoli cells into the cavity of the seminiferous tubules, which matches option $4$.

**Subtopic:** Male Gametogenesis (Spermatogenesis) · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 31)

![printed question 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q154_cf682783_03112026.png?v=cf68278324a6)

Publisher's solution, as printed:

![printed solution 154](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q154_8754a8b3_03112026.png?v=8754a8b33886)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Spermiogenesis is the transformation of spermatids into spermatozoa; spermiation is the later release of those spermatozoa from the Sertoli cells into the cavity of the seminiferous tubule
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 2  
  The two definitions are printed swapped between the two names, and the name 'spermiation' reads as the making of sperm, so the release gets handed to spermiogenesis and the formation to spermiation.
- **Why:** This question requires two neighbouring stages of one process held apart, demonstrated by the stem 'The difference between spermiogenesis and spermiation is' and by option 2 carrying the key's two clauses exchanged.
- **Note:** E1 recorded statement_options from the full-sentence options. The stem is a bare noun phrase and no statement block or lettered list is printed, so the shape here is mcq.
<!--/ecat-->

## Q155

Biology · zoology · Breathing and Exchange of Gases

Which of the following options correctly represents the lung conditions in asthma and emphysema, respectively?

- **(1)** Inflammation of bronchioles; Decreased respiratory surface
- (2) Increased respiratory surface; Inflammation of bronchioles
- (3) Increased number of bronchioles; Increased respiratory surface
- (4) Decreased respiratory surface; Inflammation of bronchioles

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Asthma is a difficulty in breathing causing wheezing due to inflammation of bronchi and bronchioles.
2. Emphysema is a chronic disorder in which alveolar walls are damaged due to which respiratory surface is decreased.

**Solved independently** (answer withheld)

1. Asthma is difficulty in breathing with wheezing caused by inflammation of the bronchi and bronchioles; emphysema is a chronic disorder in which alveolar walls are damaged, so the respiratory surface decreases. In the order asked (asthma, emphysema) this is 'Inflammation of bronchioles; Decreased respiratory surface', which is option $1$.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q155_4cb34dd3_03112026.png?v=4cb34dd38e32)

Publisher's solution, as printed:

![printed solution 155](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q155_ac2d6df4_03112026.png?v=ac2d6df4537e)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Asthma is difficulty in breathing from inflammation of the bronchi and bronchioles; emphysema is damage to alveolar walls, which cuts the respiratory surface
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Both printed conditions are right for this pair of disorders and they are handed to the wrong diseases, which a student does who ties inflammation to the smoker's irritated airways of emphysema and the loss of breathing surface to the asthma attack.
- **Why:** This question requires two similar respiratory disorders told apart by their lung condition, demonstrated by 'the lung conditions in asthma and emphysema, respectively' and by option 4 printing the same two conditions in the other order.
- **Note:** E1 recorded statement_options. The stem ends 'respectively' and each option carries two items scored together, so the shape recorded here is two_part.
<!--/ecat-->

## Q156

Biology · zoology · Body Fluids and Circulation

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Tricuspid valve | i | Between left atrium and left ventricle |
| b | Bicuspid valve | ii | Between right ventricle and pulmonary artery |
| c | Semilunar valve | iii | Between right atrium and right ventricle |

- **(1)** iii i ii
- (2) i ii iii
- (3) i iii ii
- (4) ii i iii

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Tricuspid valves are AV valve present between right atrium and right ventricle.
2. Bicuspid valves are AV valve present between left atrium and left ventricle.
3. Semilunar valves are present at the openings of aortic and pulmonary aorta.

**Solved independently** (answer withheld)

1. The tricuspid valve guards the opening between the right atrium and right ventricle, so $a \to iii$.
2. The bicuspid (mitral) valve guards the opening between the left atrium and left ventricle, so $b \to i$.
3. The semilunar valve guards the opening between the right ventricle and the pulmonary artery, so $c \to ii$.
4. The match $a\text{-}iii,\ b\text{-}i,\ c\text{-}ii$ is option $1$.

**Subtopic:** Human Circulatory System, Structure Of Heart And Chambers Of Heart · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q156_f2189ff5_03112026.png?v=f2189ff506a2)

Publisher's solution, as printed:

![printed solution 156](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q156_b92d4aae_03112026.png?v=b92d4aae6a4a)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The tricuspid valve guards the right atrio-ventricular opening, the bicuspid the left, and the semilunar valves the ventricle-to-artery openings
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 3  
  Option 3 places the semilunar valve correctly at the pulmonary opening and then inverts left and right on the two atrio-ventricular valves, which is where a student who holds 'tricuspid and bicuspid guard the AV openings' without fixing the side ends up.
- **Why:** This question requires the position NCERT states for each heart valve, demonstrated by Column II naming chamber boundaries: 'Between right ventricle and pulmonary artery'.
<!--/ecat-->

## Q157

Biology · zoology · Breathing and Exchange of Gases

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Tidal volume | i | $2500 - 3000\,\mathrm{mL}$ |
| b | Inspiratory Reserve volume | ii | $1100 - 1200\,\mathrm{mL}$ |
| c | Expiratory Reserve volume | iii | $500 - 550\,\mathrm{mL}$ |
| d | Residual volume | iv | $1000 - 1100\,\mathrm{mL}$ |

- (1) iii ii i iv
- (2) i iv ii iii
- **(3)** iii i iv ii
- (4) iv iii ii i

**Answer** — booklet: (3) · independent solve: (3) · agree

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

1. Tidal volume is about $500\,\mathrm{mL}$, so (a) matches (iii) $500 - 550\,\mathrm{mL}$.
2. Inspiratory reserve volume is the largest of the four, $2500 - 3000\,\mathrm{mL}$, so (b) matches (i).
3. Expiratory reserve volume is $1000 - 1100\,\mathrm{mL}$, so (c) matches (iv).
4. Residual volume is $1100 - 1200\,\mathrm{mL}$, so (d) matches (ii).
5. The sequence $a\text{-}iii,\ b\text{-}i,\ c\text{-}iv,\ d\text{-}ii$ is option $3$.

**Subtopic:** Respiratory Volumes and Capacities · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 32)

![printed question 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q157_2ebc8d67_03112026.png?v=2ebc8d672d9c)

Publisher's solution, as printed:

![printed solution 157](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q157_37f286f9_03112026.png?v=37f286f9290b)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** NCERT's table of respiratory volumes: tidal 500-550 mL, inspiratory reserve 2500-3000 mL, expiratory reserve 1000-1100 mL, residual 1100-1200 mL
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Inspiratory Reserve volume' and 'Expiratory Reserve volume' differ by one word, and option 1 hands the large $2500-3000\,\mathrm{mL}$ range to the expiratory reserve while keeping tidal volume right at $500-550\,\mathrm{mL}$.
- **Why:** This question requires the stored range NCERT prints for each respiratory volume, demonstrated by Column II being four numeric ranges, '$500 - 550\,\mathrm{mL}$' among them.
- **Note:** look_alike_term over nearby_fact by the rulebook's swap test: replace 'Inspiratory Reserve volume' and 'Expiratory Reserve volume' with two unlike names and the swap dies, so the resemblance of the names carries the student, not the position of the rows in the table.
<!--/ecat-->

## Q158

Biology · zoology · Excretory Products and Their Elimination

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Glycosuria | i | Accumulation of uric acid in joints |
| b | Gout | ii | Mass of crystallised salts within the kidney |
| c | Renal calculi | iii | Inflammation in glomeruli |
| d | Glomerular nephritis | iv | Presence of in glucose urine |

- (1) iii ii iv i
- (2) ii iii i iv
- (3) i ii iii iv
- **(4)** iv i ii iii

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Glycosuria denotes presence of glucose in the urine.
2. This is observed when blood glucose level rises above $180\,\mathrm{mg}/100\,\mathrm{ml}$ of blood, this is called renal threshold value for glucose.
3. Gout is due to deposition of uric acid crystals in the joint.
4. Renal calculi are precipitates of calcium phosphate produced in the pelvis of the kidney.
5. Glomerular nephritis is the inflammatory condition of glomerulus characterised by proteinuria and haematuria.

**Solved independently** (answer withheld)

1. Glycosuria means glucose is present in the urine, so $a \rightarrow iv$.
2. Gout is the accumulation of uric acid crystals in the joints, so $b \rightarrow i$.
3. Renal calculi are stones, i.e. masses of crystallised salts formed within the kidney, so $c \rightarrow ii$.
4. Glomerular nephritis is inflammation of the glomeruli, so $d \rightarrow iii$.
5. The sequence $iv, i, ii, iii$ matches option $4$.

**Subtopic:** Disorders Of The Excretory System · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 32)

![printed question 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q158_dc7bc752_03112026.png?v=dc7bc752ad3f)

Publisher's solution, as printed:

![printed solution 158](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q158_d9f4691e_03112026.png?v=d9f4691e717f)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each excretory disorder is named from what it shows: glucose in the urine, urate crystals in joints, stones in the kidney, inflamed glomeruli
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All three wrong codes were checked. The one confusion the content offers — gout's urate crystals against renal calculi's crystallised salts — is not printed as an option, and 'Glycosuria', 'Renal calculi' and 'Glomerular nephritis' each repeat a word of their own Column II entry.
- **Why:** This question requires the sign NCERT prints for each excretory disorder, demonstrated by Column II describing them: 'Inflammation in glomeruli'.
- **Note:** Column II item (iv) is stored as 'Presence of in glucose urine'; the words are transposed from 'Presence of glucose in urine'. The pairing is unaffected and no trap is claimed on it, but the line needs repair.
<!--/ecat-->

## Q159

Biology · zoology · Excretory Products and Their Elimination

Match the items given in Column I with those in Column II and select the correct option given below:

| List-I | | List-II | |
|---|---|---|---|
| a | Ultrafiltration | i | Henle's loop |
| b | Concentration of urine | ii | Ureter |
| c | Transport of urine | iii | Urinary bladder |
| d | Storage of urine | iv | Malpighian corpuscle |
|  |  | v | Proximal convoluted tubule |

- (1) a-iv, b-v, c-ii, d-iii
- (2) a-v, b-iv, c-i, d-ii
- **(3)** a-iv, b-i, c-ii, d-iii
- (4) a-v, b-iv, c-i, d-iii

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Ultrafiltration refers to filtration of very fine particles having molecular weight less than $68{,}000$ daltons through malpighian corpuscle.
2. Concentration of urine refers to water absorption from glomerular filtrate as a result of hyperosmolarity in the medulla created by counter-current mechanism in Henle's loop.
3. Urine is carried from kidney to bladder through ureter.
4. Urinary bladder is concerned with storage of urine.

**Solved independently** (answer withheld)

1. Ultrafiltration of blood takes place in the Malpighian corpuscle (glomerulus + Bowman's capsule), so $a \rightarrow iv$.
2. Concentration of urine is brought about by the counter-current mechanism of Henle's loop, so $b \rightarrow i$.
3. Urine is transported from the kidney to the bladder by the ureter, so $c \rightarrow ii$.
4. Urine is stored in the urinary bladder until micturition, so $d \rightarrow iii$.
5. The match $a$-$iv$, $b$-$i$, $c$-$ii$, $d$-$iii$ is option $3$.

**Subtopic:** Human Excretory System · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q159_c435d3aa_03112026.png?v=c435d3aa67db)

Publisher's solution, as printed:

![printed solution 159](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q159_2752da6f_03112026.png?v=2752da6fb30d)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Each step of urine formation and voiding sits in a named part: filtration at the Malpighian corpuscle, concentration in Henle's loop, transport by the ureter, storage in the bladder
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 1  
  Option 1 alters one row only, moving the concentration of urine to the proximal convoluted tubule, which is where 'most of the reabsorption happens in the PCT' puts it.
- **Why:** This question requires the part of the excretory system NCERT assigns to each step, demonstrated by Column II carrying five parts for four steps, with 'Proximal convoluted tubule' left over.
- **Note:** Column II prints five entries against four rows, so the last pairing cannot be closed by striking out the leftover item; the unused entry is the one both wrong-route options reach for.
<!--/ecat-->

## Q160

Biology · both · Cell: The Unit of Life

Which of the following events does not occur in rough endoplasmic reticulum?

- (1) Protein folding
- (2) Cleavage of signal peptide
- (3) Protein glycosylation
- **(4)** Phospholipid synthesis

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Phospholipid synthesis does not take place in RER.
2. Smooth endoplasmic reticulum are involved in lipid synthesis.

**Solved independently** (answer withheld)

1. Rough ER carries ribosomes; proteins entering its lumen have their signal peptide cleaved, are folded and undergo initial glycosylation, so options $1$, $2$ and $3$ occur in RER.
2. NCERT states smooth ER is the major site of lipid synthesis, so phospholipid synthesis does not occur in rough ER, which is option $4$.

**Subtopic:** Endomembrane System And Its Types · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q160_e6c1ad76_03112026.png?v=e6c1ad768436)

Publisher's solution, as printed:

![printed solution 160](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q160_eef4a24b_03112026.png?v=eef4a24b78de)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The rough ER handles newly made proteins — folding, signal-peptide cleavage, glycosylation — while lipid and phospholipid synthesis belongs to the smooth ER
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  Glycosylation is the process the endomembrane account attaches to the Golgi, printed a paragraph away as where glycoproteins and glycolipids are formed, so it reads as the event that belongs elsewhere than the rough ER.
- **Why:** This question requires the division of labour between rough and smooth ER as stated, demonstrated by 'Which of the following events does not occur in rough endoplasmic reticulum?' with three protein-processing events and one lipid one as options.
- **Note:** Swap test applied to option 3: glycosylation and phospholipid synthesis are unlike terms, and the route survives any renaming, because what carries it is glycosylation being printed with the Golgi in the same endomembrane passage. So nearby_fact, not look_alike_term.
<!--/ecat-->

## Q161

Biology · botany · Respiration in Plants

Which of these statements is incorrect?

- (1) Enzymes of TCA cycle are present in mitochondrial matrix
- (2) Glycolysis operates as long as it is supplied with NAD that can pick up hydrogen atoms
- (3) Glycolysis occurs in cytosol
- **(4)** Oxidative phosphorylation takes place in outer mitochondrial membrane

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Oxidative phosphorylation takes place in inner mitochondrial membrane.

**Solved independently** (answer withheld)

1. Statements 1, 2 and 3 are correct: TCA enzymes are in the mitochondrial matrix, glycolysis continues only while $\mathrm{NAD^+}$ is available to accept hydrogen, and glycolysis occurs in the cytosol.
2. Oxidative phosphorylation (electron transport chain and $\mathrm{F_0F_1}$ ATP synthase) takes place on the inner mitochondrial membrane, not the outer membrane, so statement $4$ is the incorrect one.

**Subtopic:** Electron Transport System (ETS) And Oxidative Phosphorylation · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 33)

![printed question 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q161_8de2916f_03112026.png?v=8de2916faab2)

Publisher's solution, as printed:

![printed solution 161](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q161_ff0abbc3_03112026.png?v=ff0abbc343d4)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Glycolysis runs in the cytosol, the TCA cycle in the mitochondrial matrix, and oxidative phosphorylation on the inner mitochondrial membrane, not the outer one
- **Trap:** **Wrong site attacked** (`wrong_site_attacked`) — the reagent is right but it attacks the other site, atom or bond than the one the question turns on — option 3  
  A student holding respiration as the mitochondrion's business relocates glycolysis there and so reads the one sentence that names the cytosol as the incorrect statement.
- **Why:** This question requires the site of each respiratory step as stated, demonstrated by 'Which of these statements is incorrect?' and by the one false option differing from the truth only in naming the 'outer mitochondrial membrane'.
<!--/ecat-->

## Q162

Biology · zoology · Neural Control and Coordination

Nissl bodies are mainly composed of

- (1) Proteins and lipids
- (2) Nucleic acids and SER
- (3) DNA and RNA
- **(4)** Free ribosomes and RER

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Nissl granules are present in the cyton and even extend into the dendrite but absent in axon and rest of the neuron.
2. Nissl granules are in fact composed of free ribosomes and RER.
3. They are responsible for protein synthesis.

**Solved independently** (answer withheld)

1. Nissl bodies are the granular bodies in the neuron cell body and dendrites; they consist of rough endoplasmic reticulum together with free ribosomes, which is option $4$.

**Subtopic:** Neuron as Structural and Functional Unit of Neural System and Types of Axon · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 33)

![printed question 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q162_eeecb5be_03112026.png?v=eeecb5be0b20)

Publisher's solution, as printed:

![printed solution 162](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q162_437ce4a4_03112026.png?v=437ce4a4ff03)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Nissl bodies are the neuron's stacks of rough endoplasmic reticulum together with free ribosomes, which is why they stain with basic dyes
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 2  
  The nucleic-acid half is right — the ribosomal RNA is what makes these bodies stain — and the second half swaps the smooth ER for the rough one, a difference of a single letter in the printed abbreviation.
- **Why:** This question requires the stated composition of one named neuronal structure, demonstrated by 'Nissl bodies are mainly composed of' with options that each pair two components.
- **Note:** SER against RER is a one-letter likeness, but the trap axis takes half_right here because the option carries two parts and only the second fails; the brief reserves look_alike_term for a lone wrong name.
<!--/ecat-->

## Q163

Biology · zoology · Digestion and Absorption

Which of the following terms describe human dentition?

- (1) Thecodont, Diphyodont, Homodont
- (2) Pleurodont, Monophyodont, Homodont
- **(3)** Thecodont, Diphyodont, Heterodont
- (4) Pleurodont, Diphyodont, Heterodont

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. In humans, dentition is
2. Thecodont : Teeth are present in the sockets of the jaw bone called alveoli.
3. Diphyodont : Teeth erupts twice, temporary milk or deciduous teeth are replaced by a set of permanent or adult teeth.
4. Heterodont dentition : Dentition consists of different types of teeth namely incisors, canine, premolars and molars.

**Solved independently** (answer withheld)

1. Each human tooth sits in a socket in the jaw bone, so the attachment is $\text{thecodont}$, not pleurodont. This rules out options $2$ and $4$.
2. Humans form two sets of teeth in a lifetime, temporary milk teeth and permanent adult teeth, so the dentition is $\text{diphyodont}$, not monophyodont.
3. An adult has four different types of teeth (incisors, canines, premolars, molars), so the dentition is $\text{heterodont}$, not homodont. This rules out option $1$.
4. Thecodont, diphyodont and heterodont together are option $3$.

**Subtopic:** Human Digestive System: Alimentary Canal and Associated Glands · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 33)

![printed question 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q163_a727e5ce_03112026.png?v=a727e5ce4f01)

Publisher's solution, as printed:

![printed solution 163](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q163_619be65f_03112026.png?v=619be65f670f)

---

<!--ecat-->
#### Categories

- **Type:** **Two answers** (`two_part`) — the answer has two halves, usually joined by 'respectively'
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Human teeth are thecodont, set in sockets of the jaw bone; diphyodont, with a milk set replaced once; and heterodont, of four different kinds
- **Trap:** **Partly correct** (`half_right`) — one part of the option is right and one part is wrong — option 4  
  Two of the three terms are the key's own and the attachment term is swapped from thecodont to pleurodont, the one axis of the three that cannot be settled by looking at a human mouth, since the socket is inside the bone.
- **Why:** This question requires three stated terms for human teeth held together, demonstrated by 'Which of the following terms describe human dentition?' with options that are triples of terms scored whole.
- **Note:** Each option is a set of three terms accepted or rejected whole, the codebook's pair_options shape; of the six qtype values two_part is the one that records an answer needing several items all right at once.
<!--/ecat-->

## Q164

Biology · both · Cell: The Unit of Life

Select the incorrect match :

- (1) Lampbrush chromosomes – Diplotene bivalents
- (2) Submetacentric chromosomes – L-shaped chromosomes
- (3) Allosomes – Sex chromosomes
- **(4)** Polytene chromosomes – Oocytes of amphibians

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Polytene chromosomes are found in salivary glands of insects of order Diptera.

**Solved independently** (answer withheld)

1. Lampbrush chromosomes are bivalents seen at the diplotene stage of meiosis I (in amphibian oocytes), so option $1$ is a correct match.
2. Submetacentric chromosomes have the centromere slightly away from the middle, so their arms look unequal and they appear L-shaped; option $2$ is a correct match.
3. Allosomes are the sex chromosomes, as distinct from autosomes; option $3$ is a correct match.
4. Polytene chromosomes are found in the salivary glands of dipteran larvae (e.g. $Drosophila$), whereas amphibian oocytes carry lampbrush chromosomes, so option $4$ is the incorrect match.

**Subtopic:** Nucleus, Chromosome And Microbodies · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q164_304d7161_03112026.png?v=304d7161f891)

Publisher's solution, as printed:

![printed solution 164](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q164_9e545d34_03112026.png?v=9e545d34d7cf)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Lampbrush chromosomes are the diplotene bivalents of amphibian oocytes, while polytene chromosomes are the giant banded chromosomes of dipteran salivary glands.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  With the lampbrush fact stored as its site, 'amphibian oocytes', and that site already printed in option 4, the stage 'diplotene bivalents' in option 1 is not recognised as the same fact and option 1 reads as the mismatch.
- **Why:** This question requires the stated pairing of each special chromosome with its site or its shape, demonstrated by 'Polytene chromosomes – Oocytes of amphibians', the one pair whose partner belongs to another chromosome type. Swap test on the trap: 'diplotene bivalents' and 'oocytes of amphibians' resemble each other in no way, and the pull survives, so position in the same printed line carries it.
- **Note:** E1's pattern read this as `match_the_lists`, but no two columns and no pairing code are printed: each option is a pair accepted or rejected whole (codebook §1 `pair_options`), which the retired-value crosswalk maps onto qtype `statements`.
<!--/ecat-->

## Q165

Biology · both · Cell: The Unit of Life

Many ribosomes may associate with a single mRNA to form multiple copies of a polypeptide simultaneously. Such strings of ribosomes are termed as

- **(1)** Polysome
- (2) Plastidome
- (3) Polyhedral bodies
- (4) Nucleosome

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. The phenomenon of association of many ribosomes with single m-RNA leads to formation of polyribosomes or polysomes or ergasomes.

**Solved independently** (answer withheld)

1. Several ribosomes attached along one mRNA, each making a copy of the polypeptide at the same time, form a polyribosome, also called a $\text{polysome}$, which is option $1$.

**Subtopic:** Ribosomes And Cytoskeleton · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q165_d8e8b5c0_03112026.png?v=d8e8b5c0be39)

Publisher's solution, as printed:

![printed solution 165](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q165_cd30af20_03112026.png?v=cd30af20ba72)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** A polysome is the string of ribosomes translating one mRNA at the same time.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 4  
  The stem's 'strings of ribosomes' lands on the beads-on-a-string picture used for nucleosomes, and the shared -some ending finishes the job.
- **Why:** This question requires the stated name for many ribosomes translating one mRNA, demonstrated by the stem supplying the definition itself, 'strings of ribosomes'. Swap test on the trap: replace 'Nucleosome' with a name that neither ends in -some nor carries the beads-on-string picture and the pull dies, so the likeness is doing the work.
<!--/ecat-->

## Q166

Biology · zoology · Evolution

According to Hugo de Vries, the mechanism of evolution is

- (1) Multiple step mutations
- (2) Phenotypic variations
- **(3)** Saltation
- (4) Minor mutations

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. As per mutation theory given by Hugo de Vries, the evolution is a discontinuous phenomenon or saltatory phenomenon/saltation.

**Solved independently** (answer withheld)

1. From his work on evening primrose, Hugo de Vries said that evolution is caused by large mutations in a single step, not by small continuous variations. He called this single-step large mutation $\text{saltation}$, which is option $3$.

**Subtopic:** Mechanism of Evolution · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q166_00fde81f_03112026.png?v=00fde81fd193)

Publisher's solution, as printed:

![printed solution 166](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q166_6b293e70_03112026.png?v=6b293e708d80)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Hugo de Vries held that evolution proceeds by saltation -- single-step large mutations -- and not by the small heritable variations Darwin worked with.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The sentence that gives de Vries his answer also prints Darwin's side of the contrast, so with the word saltation lost and only 'de Vries said mutation' kept, the mutation phrase is taken from the other half of that sentence.
- **Why:** This question requires the term the account attaches to one named worker, demonstrated by the stem naming Hugo de Vries and asking for 'the mechanism of evolution'. Swap test on the trap: 'saltation' and 'minor mutations' resemble each other in no way, and the pull survives, so position inside the book's own contrast sentence is what carries it.
<!--/ecat-->

## Q167

Biology · zoology · Human Reproduction

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Proliferative Phase | i | Breakdown of endometrial lining |
| b | Secretory Phase | ii | Follicular Phase |
| c | Menstruation | iii | Luteal Phase |

- (1) iii ii i
- **(2)** ii iii i
- (3) i iii ii
- (4) iii i ii

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. During proliferative phase, the follicles start developing, hence, called follicular phase.
2. Secretory phase is also called as luteal phase mainly controlled by progesterone secreted by corpus luteum.
3. Estrogen further thickens the endometrium maintained by progesterone.
4. Menstruation occurs due to decline in progesterone level and involves breakdown of overgrown endometrial lining.

**Solved independently** (answer withheld)

1. The proliferative phase, when the endometrium regenerates under oestrogen from growing follicles, is the follicular phase: $a \rightarrow ii$.
2. The secretory phase, when the endometrium is prepared under progesterone from the corpus luteum, is the luteal phase: $b \rightarrow iii$.
3. Menstruation is the breakdown of the endometrial lining: $c \rightarrow i$.
4. The order $ii,\ iii,\ i$ is option $2$.

**Subtopic:** Menstrual Cycle · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 34)

![printed question 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q167_ac8991b5_03112026.png?v=ac8991b5744a)

Publisher's solution, as printed:

![printed solution 167](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q167_9d669aab_03112026.png?v=9d669aab5b5c)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** The menstrual cycle carries two names for each half: the proliferative phase is the follicular phase and the secretory phase is the luteal phase, while menstruation is the breakdown of the endometrial lining
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 1  
  The word 'proliferative' describes something growing, and what grows after ovulation is the corpus luteum, so a student reads proliferative as luteal and secretory as follicular — the two halves of the cycle swapped end for end while the menstruation row stays right.
- **Why:** This question requires the alternative name NCERT gives each phase of the cycle, demonstrated by Column II mixing phase names with an event, 'Breakdown of endometrial lining'.
<!--/ecat-->

## Q168

Biology · both · Molecular Basis of Inheritance

All of the following are part of an operon except

- (1) an operator
- **(2)** an enhancer
- (3) structural genes
- (4) a promoter

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. Enhancer sequences are present in eukaryotes.
2. Operon concept is for prokaryotes.

**Solved independently** (answer withheld)

1. As taught in NCERT (lac operon), an operon consists of a promoter, an operator and structural genes, regulated by a regulator gene; an enhancer is a eukaryotic regulatory element and is not part of an operon, so the answer is option $2$.

**Subtopic:** The Lac Operon · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 34)

![printed question 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q168_38fa1196_03112026.png?v=38fa1196d82e)

Publisher's solution, as printed:

![printed solution 168](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q168_89bda972_03112026.png?v=89bda972a4d7)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** An operon is a promoter, an operator and the structural genes they control; an enhancer is a eukaryotic regulatory sequence and no part of one.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  The promoter is learnt as the upstream site RNA polymerase binds before transcription begins, so once it is pictured outside the block of genes it is counted out of the operon and the enhancer is left in.
- **Why:** This question requires the stated membership of an operon, demonstrated by 'an enhancer' being the one listed element the operon account never names. Swap test on the trap: 'promoter' and 'enhancer' resemble each other in no way, and the pull survives, because the two are described side by side as regulatory sequences.
- **Note:** The negation is on the task ('except'), but the printed membership list decides the answer either way, so the trap recorded is the content route rather than the missed negation.
<!--/ecat-->

## Q169

Biology · both · Molecular Basis of Inheritance

AGGTATCGCAT is a sequence from the coding strand of a gene. What will be the corresponding sequence of the transcribed mRNA?

- **(1)** AGGUAUCGCAU
- (2) ACCUAUGCGAU
- (3) UGGTUTCGCAT
- (4) UCCAUAGCGUA

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Coding strand and mRNA has same nucleotide sequence except, ‘T’ – Thymine is replaced by ‘U’–Uracil in mRNA.

**Solved independently** (answer withheld)

1. The mRNA is complementary to the template strand, so it has the same base sequence as the coding strand, with $\mathrm{U}$ in place of $\mathrm{T}$: $\mathrm{AGGTATCGCAT} \rightarrow \mathrm{AGGUAUCGCAU}$, which is option $1$.

**Subtopic:** Transcription · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 34)

![printed question 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q169_aff0eaa9_03112026.png?v=aff0eaa96b07)

Publisher's solution, as printed:

![printed solution 169](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q169_8264e9d8_03112026.png?v=8264e9d893a9)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** The mRNA copies the coding strand base for base with uracil in place of thymine; the complement of the coding strand is the template, not the message.
- **Trap:** **Reversed** (`reversed`) — the right thing stated backwards: direction, order or ratio — option 4  
  Carrying the rule as 'mRNA is complementary to the DNA' and not checking which strand was printed, every base is paired instead of copied, which yields the template strand written in RNA letters.
- **Why:** This question requires the transcription convention applied to a printed sequence, demonstrated by the stem specifying 'the coding strand of a gene'. The label is `reversed` rather than `formula_misused` because option 4 is the exact complement of the printed strand, that is, the roles of the two strands turned around.
- **Note:** E1's pattern read this as `arrange_in_order` on the word sequence; the printed shape is a plain MCQ whose four options are sequences, and the crosswalk maps that pattern value onto `mcq` in any case.
<!--/ecat-->

## Q170

Biology · zoology · Principles of Inheritance and Variation

A woman has an X-linked condition on one of her X chromosomes. This chromosome can be inherited by

- (1) Only daughters
- (2) Only grandchildren
- (3) Only sons
- **(4)** Both sons and daughters

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Woman is a carrier
2. Both son & daughter inherit X–chromosome
3. Although only son be the diseased

**Solved independently** (answer withheld)

1. A woman is $X^{a}X$ and gives one X chromosome to every child, whatever its sex.
2. A son gets $X$ from his mother and $Y$ from his father, so a son can receive $X^{a}$.
3. A daughter gets one $X$ from each parent, so a daughter can also receive $X^{a}$.
4. So the chromosome can pass to both sons and daughters, which is option $4$.

**Subtopic:** Sex Determination in Humans · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 35)

![printed question 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q170_4e4be0b4_03112026.png?v=4e4be0b44111)

Publisher's solution, as printed:

![printed solution 170](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q170_f8a8bd66_03112026.png?v=f8a8bd663557)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Rule applied** (`apply_rule`) — a rule you already know, used on a case you have not seen
- **Concept:** A mother gives one of her two X chromosomes to every child, son or daughter; which children SHOW an X-linked condition is a separate question.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The carrier-mother pedigree is stored as 'her sons are the affected ones', and that answer is given to a stem which asked who can receive the chromosome.
- **Why:** This question requires the rule for maternal X transmission applied to the stated case, demonstrated by 'This chromosome can be inherited by', which asks who can receive the chromosome and not who shows the condition.
<!--/ecat-->

## Q171

Biology · zoology · Digestion and Absorption

Which of the following gastric cells indirectly help in erythropoiesis?

- (1) Chief cells
- (2) Goblet cells
- (3) Mucous cells
- **(4)** Parietal cells

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Parietal or oxyntic cell is a source of $\mathrm{HCl}$ and intrinsic factor.
2. $\mathrm{HCl}$ converts iron present in diet from ferric to ferrous form so that it can be absorbed easily and used during erythropoiesis.
3. Intrinsic factor is essential for the absorption of vitamin $\mathrm{B_{12}}$ and its deficiency causes pernicious anaemia.

**Solved independently** (answer withheld)

1. Parietal (oxyntic) cells of the gastric glands secrete HCl and Castle's intrinsic factor; intrinsic factor is required for absorbing vitamin $B_{12}$, which is essential for erythropoiesis, so the answer is option $4$.

**Subtopic:** Gastric Glands and Their Cell Types · **Difficulty:** medium (3 steps)

**Printed in the booklet** (page 35)

![printed question 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q171_9620d60c_03112026.png?v=9620d60c7525)

Publisher's solution, as printed:

![printed solution 171](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q171_a60fab74_03112026.png?v=a60fab74aaea)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Parietal (oxyntic) cells secrete intrinsic factor, without which vitamin B12 cannot be absorbed, and B12 is needed to make red cells.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Holding 'the stomach makes the intrinsic factor for B12' without which cell makes it, the other secretory cell from the same one-sentence list of gastric gland cells is taken instead.
- **Why:** This question requires the secretion assigned to one named gastric cell type, demonstrated by 'indirectly help in erythropoiesis', which only the intrinsic factor and vitamin B12 route satisfies. Swap test on the trap: 'chief' and 'parietal' resemble each other in no way, and the pull survives, so position in the gland's printed cell list carries it.
- **Note:** Options 2 and 3 name the same mucus-secreting cells; recorded as a redundancy in the option set rather than as a device.
<!--/ecat-->

## Q172

Biology · zoology · Body Fluids and Circulation

Match the items given in Column I with those in Column II and select the correct option given below :

| List-I | | List-II | |
|---|---|---|---|
| a | Fibrinogen | (i) | Osmotic balance |
| b | Globulin | (ii) | Blood clotting |
| c | Albumin | (iii) | Defence mechanism |

- (1) (iii) (ii) (i)
- (2) (i) (iii) (ii)
- (3) (i) (ii) (iii)
- **(4)** (ii) (iii) (i)

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Fibrinogen forms fibrin strands during coagulation.
2. These strands forms a network and the meshes of which are occupied by blood cells, this structure finally forms a clot.
3. Antibodies are derived from $\gamma$-Globulin fraction of plasma proteins which means globulins are involved in defence mechanisms.
4. Albumin is a plasma protein mainly responsible for BCOP.

**Solved independently** (answer withheld)

1. Fibrinogen is a plasma protein needed for coagulation, so $a \rightarrow (ii)$ Blood clotting.
2. Globulins (immunoglobulins) are mainly involved in the body's defence, so $b \rightarrow (iii)$ Defence mechanism.
3. Albumin helps maintain the osmotic balance of plasma, so $c \rightarrow (i)$ Osmotic balance.
4. The sequence $(ii)\ (iii)\ (i)$ matches option $4$.

**Subtopic:** Blood and Plasma · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 35)

![printed question 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q172_b90ccd80_03112026.png?v=b90ccd808f9f)

Publisher's solution, as printed:

![printed solution 172](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q172_c9bb71bd_03112026.png?v=c9bb71bdad52)

---

<!--ecat-->
#### Categories

- **Type:** **Match the columns** (`match_columns`) — two labelled lists to pair, the answer is a pairing code
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Plasma proteins divide the work: fibrinogen clots blood, globulins defend, albumin holds the osmotic balance
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  All three wrong codes were checked row by row. Each requires fibrinogen to be moved off blood clotting, which the name itself gives away through fibrin, and the one confusion the content offers — globulin against albumin — is not printed as an option, since no code keeps Fibrinogen-(ii) and crosses the other two.
- **Why:** This question requires the function NCERT assigns to each plasma protein, demonstrated by Column II being three bare functions: 'Osmotic balance', 'Blood clotting', 'Defence mechanism'.
<!--/ecat-->

## Q173

Biology · zoology · Breathing and Exchange of Gases

Which of the following is an occupational respiratory disorder?

- (1) Anthracis
- (2) Botulism
- **(3)** Silicosis
- (4) Emphysema

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Silicosis is due to excess inhalation of silica dust in the workers involved grinding or stone breaking industries.
2. Long exposure can give rise to inflammation leading to fibrosis and thus causing serious lung damage.
3. Anthrax is a serious infectious disease caused by Bacillus anthracis.
4. It commonly affects domestic and wild animals.
5. Emphysema is a chronic disorder in which alveolar walls are damaged due to which respiratory surface is decreased.
6. Botulism is a form of food poisoning caused by Clostridium botulinum.

**Solved independently** (answer withheld)

1. Occupational respiratory disorders come from long exposure to dust at work, such as silica dust in stone-grinding or stone-breaking industries, which causes silicosis (option $3$); botulism is food poisoning, emphysema is mainly caused by smoking, and 'Anthracis' is not an occupational disorder.

**Subtopic:** Regulation of Respiration and Disorders of Respiratory System · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 35)

![printed question 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q173_4864cd5f_03112026.png?v=4864cd5fb8d1)

Publisher's solution, as printed:

![printed solution 173](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q173_e34a6cb2_03112026.png?v=e34a6cb2038d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Occupational respiratory disorders are the dust diseases of the workplace, of which silicosis is the named example; emphysema in the same section is the smoking disorder.
- **Trap:** **look alike term** (`look_alike_term`) — two terms RESEMBLE each other and the resemblance is the pull: maturation / meristematic, lyase / ligase, GPP / NPP — option 1  
  'Anthracis' reads as anthracosis, the coal-dust black-lung disease, so the dust-disease set is searched, matched to this word, and the printed name -- the anthrax bacterium's species epithet -- is never looked at again.
- **Why:** This question requires the named occupational dust disease, demonstrated by 'occupational respiratory disorder' in the stem, which 'Silicosis' alone satisfies among the four. Swap test on the trap: replace 'Anthracis' with a disease name that does not resemble anthracosis and the pull dies, so the likeness is doing the work.
- **Note:** Two options carry real routes -- the look-alike in option 1 and the same-section neighbour in option 4. Option 1 is recorded as the single trap because its pull does not depend on a gap in the student's list of disorders, only on the word; option 4's full route is kept under other_options.
<!--/ecat-->

## Q174

Biology · zoology · Locomotion and Movement

Calcium is important in skeletal muscle contraction because it

- **(1)** Binds to troponin to remove the masking of active sites on actin for myosin.
- (2) Detaches the myosin head from the actin filament.
- (3) Activates the myosin ATPase by binding to it.
- (4) Prevents the formation of bonds between the myosin cross bridges and the actin filament.

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Signal for contraction increase $\mathrm{Ca^{++}}$ level many folds in the sarcoplasm.
2. $\mathrm{Ca^{++}}$ now binds with sub-unit of troponin (troponin "C") which is masking the active site on actin filament and displaces the sub-unit of troponin.
3. Once the active site is exposed, head of the myosin attaches and initiate contraction by sliding the actin over myosin.

**Solved independently** (answer withheld)

1. Released $\text{Ca}^{2+}$ binds to the troponin subunit on the actin filament, which moves tropomyosin and unmasks the myosin-binding active sites on actin, so cross bridges can form; this is option $1$, while options $2$, $3$ and $4$ describe ATP-driven detachment, the head's own ATPase activity and the opposite of calcium's effect.

**Subtopic:** Mechanism of Muscle Contraction and Red and White Muscle Fibre · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 35)

![printed question 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q174_2bd970d7_03112026.png?v=2bd970d7642a)

Publisher's solution, as printed:

![printed solution 174](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q174_0c0ba486_03112026.png?v=0c0ba4860e84)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Stated reason** (`reason_line`) — a reason NCERT gives: why it happens
- **Concept:** Calcium binds the troponin subunit and unmasks actin's myosin-binding sites; the ATP that drives the head is the step after it.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The sentence after the calcium step is the one about energy from ATP hydrolysis moving the myosin head, so with 'calcium starts contraction' kept and the troponin clause lost, calcium is attached to that next step.
- **Why:** This question requires the reason calcium is needed, demonstrated by the stem's trailing 'because it' and by option 1 naming the troponin subunit it binds.
- **Note:** qtype `statements` follows the printed shape: the stem is a trailing 'because' and each option is a full mechanism claim judged whole (codebook §1 `statement_options`).
<!--/ecat-->

## Q175

Biology · zoology · Animal Kingdom

Identify the vertebrate group of animals characterized by crop and gizzard in its digestive system

- (1) Amphibia
- **(2)** Aves
- (3) Reptilia
- (4) Osteichthyes

**Answer** — booklet: (2) · independent solve: (2) · agree

**Publisher's solution**

1. The digestive tract of Aves has additional chambers in their digestive system as crop and Gizzard.
2. Crop is concerned with storage of food grains.
3. Gizzard is a masticatory organ in birds used to crush food grain.

**Solved independently** (answer withheld)

1. The digestive tract of birds (Aves) has the additional chambers crop and gizzard, so the answer is option $2$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (1 step)

**Printed in the booklet** (page 36)

![printed question 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q175_0f7648bd_03112026.png?v=0f7648bdc1ce)

Publisher's solution, as printed:

![printed solution 175](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q175_d42f5826_03112026.png?v=d42f58264f3c)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Among vertebrates only birds carry a crop for storing food and a gizzard for grinding it.
- **Trap:** **No trap** (`no_trap`) — nothing pulls; the other options are only filler  
  Checked the other three classes against both named organs: the amphibian, reptile and bony-fish accounts name no storage or grinding chamber in the gut, and the crop and gizzard belong among vertebrates only to Aves -- and otherwise to the cockroach and the earthworm, which the stem's word 'vertebrate' removes. No printed fact about the other three options reaches either organ.
- **Why:** This question requires the stated diagnostic organs of one vertebrate class, demonstrated by 'crop and gizzard in its digestive system', which among vertebrates is attached only to Aves.
- **Note:** `no_trap` here is a finding about the option set: the three wrong options are coordinate vertebrate classes, and the stem's word 'vertebrate' has already removed the cockroach-and-earthworm association that the words crop and gizzard otherwise carry.
<!--/ecat-->

## Q176

Biology · botany · Biological Classification

Ciliates differ from all other protozoans in

- (1) using flagella for locomotion
- (2) using pseudopodia for capturing prey
- (3) having a contractile vacuole for removing excess water
- **(4)** having two types of nuclei

**Answer** — booklet: (4) · independent solve: (4) · agree

**Publisher's solution**

1. Ciliates differs from other protozoans in having two types of nuclei.
2. eg. Paramoecium have two types of nuclei i.e. macronucleus & micronucleus.

**Solved independently** (answer withheld)

1. Ciliates (e.g. $Paramoecium$) are the only protozoans that have two types of nuclei, a macronucleus and a micronucleus, whereas flagella, pseudopodia and contractile vacuoles also occur in other protozoan groups, so the answer is option $4$.

**Subtopic:** Protozoans · **Difficulty:** medium (2 steps)

**Printed in the booklet** (page 36)

![printed question 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q176_e365b2f9_03112026.png?v=e365b2f96a34)

Publisher's solution, as printed:

![printed solution 176](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q176_b69a749f_03112026.png?v=b69a749fca04)

---

<!--ecat-->
#### Categories

- **Type:** **Statements** (`statements`) — lettered statements, the answer is which combination is right
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Only ciliates among protozoans keep two kinds of nucleus, a macronucleus and micronuclei; a contractile vacuole is shared with other protozoan groups.
- **Trap:** **Answers another question** (`answers_other_question`) — true, and about this topic, but it answers something else — option 3  
  The option is true of ciliates -- Paramoecium does void excess water through a contractile vacuole -- so an option set read for truth stops at the first true statement and never tests it against 'differ from all other protozoans'.
- **Why:** This question requires a feature exclusive to one protozoan group, demonstrated by 'differ from all other protozoans', which a true but shared feature such as the contractile vacuole does not satisfy.
- **Note:** The nuclear dimorphism the key rests on is not stated in the ciliate paragraph the other three options are drawn from. Tagged as printed; the key is not ours to re-judge.
<!--/ecat-->

## Q177

Biology · zoology · Structural Organisation in Animals

Which of the following features is used to identify a male cockroach from a female cockroach?

- (1) Presence of a boat shaped sternum on the $9^{\text{th}}$ abdominal segment
- (2) Forewings with darker tegmina
- **(3)** Presence of caudal styles
- (4) Presence of anal cerci

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Males bear a pair of short, thread like anal styles which are absent in females.
2. Anal/caudal styles arise from $9^{\text{th}}$ abdominal segment in male cockroach.

**Solved independently** (answer withheld)

1. Anal (caudal) styles are short, thread-like structures present only in male cockroaches and absent in females, so their presence identifies a male, which is option $3$.

**Subtopic:** Morphology of Cockroach · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 36)

![printed question 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q177_11164c83_03112026.png?v=11164c83551e)

Publisher's solution, as printed:

![printed solution 177](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q177_6da075ed_03112026.png?v=6da075ed207d)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Comparison** (`compare`) — the difference between two things, or the correct pairing
- **Concept:** Caudal (anal) styles on the ninth sternum belong to the male cockroach alone; anal cerci are present in both sexes and the boat-shaped genital pouch is the female's.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 4  
  Anal cerci and caudal styles are described together as the paired appendages at the hind end of the cockroach's abdomen, so with the pair stored but not which of them is sex-limited, the one present in both sexes is chosen.
- **Why:** This question requires a feature one sex has and the other lacks, demonstrated by 'used to identify a male cockroach from a female cockroach', which anal cerci -- borne by both -- do not satisfy. Swap test on the trap: 'anal cerci' and 'caudal styles' resemble each other in no way, and the pull survives, so position in the same description carries it.
<!--/ecat-->

## Q178

Biology · zoology · Animal Kingdom

Which one of these animals is not a homeotherm?

- (1) Macropus
- (2) Camelus
- **(3)** Chelone
- (4) Psittacula

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Homeotherm are animals that maintain constant body temperature, irrespective of surrounding temperature.
2. Birds and mammals are homeotherm.
3. Chelone (Turtle) belongs to class reptilia which is Poikilotherm or cold blood.

**Solved independently** (answer withheld)

1. Homeotherms (warm-blooded animals) are birds and mammals; reptiles are poikilotherms. $Macropus$ (kangaroo) and $Camelus$ (camel) are mammals, $Psittacula$ (parrot) is a bird, while $Chelone$ (turtle) is a reptile, so the answer is option $3$.

**Subtopic:** Class – Amphibia, Reptilia, Aves and Mammalia · **Difficulty:** easy (2 steps)

**Printed in the booklet** (page 36)

![printed question 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q178_886ea3e0_03112026.png?v=886ea3e04c55)

Publisher's solution, as printed:

![printed solution 178](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q178_1e5d0a34_03112026.png?v=1e5d0a348d88)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Homeothermy goes with the bird and mammal classes; Chelone is a turtle, so a reptile, and therefore a poikilotherm.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 2  
  The camel is carried in memory as the desert animal that lets its body temperature swing through the day to save water, and that remembered adaptation is answered in place of the class the genus belongs to.
- **Why:** This question requires the class each printed genus belongs to and which classes are warm-blooded, demonstrated by the four options being genus names listed under Mammalia, Reptilia and Aves. Swap test on the trap: 'Camelus' and 'Chelone' resemble each other in no way, and the pull survives, because what carries it is a remembered adaptation of the camel rather than any likeness of names.
<!--/ecat-->

## Q179

Biology · zoology · Animal Kingdom

Which of the following animals does not undergo metamorphosis?

- **(1)** Earthworm
- (2) Moth
- (3) Tunicate
- (4) Starfish

**Answer** — booklet: (1) · independent solve: (1) · agree

**Publisher's solution**

1. Metamorphosis refers to transformation of larva into adult.
2. Animal that perform metamorphosis are said to have indirect development.
3. In earthworm development is direct which means no larval stage and hence no metamorphosis.

**Solved independently** (answer withheld)

1. Earthworm shows direct development: the young hatch from the cocoon as miniature adults with no larval stage, so it does not undergo metamorphosis, which is option $1$; moth (complete metamorphosis), tunicate (tadpole larva with retrogressive metamorphosis) and starfish (bilateral larva to radial adult) all do.

**Subtopic:** Phylum – Annelida · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 36)

![printed question 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q179_d458c435_03112026.png?v=d458c43568e5)

Publisher's solution, as printed:

![printed solution 179](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q179_97ada502_03112026.png?v=97ada5023130)

---

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Earthworm development is direct, while the moth, the tunicate (retrogressively) and the starfish each pass through a larva that metamorphoses.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 3  
  The tunicate is met as the chordate whose notochord is confined to the larval tail, and that line is answered instead: the adult is taken to have simply lost a tail, which is not counted as a metamorphosis.
- **Why:** This question requires which of the four animals develops without a larval stage, demonstrated by 'does not undergo metamorphosis' set against four animals whose development is classed as direct or indirect. Swap test on the trap: 'Tunicate' and 'Earthworm' resemble each other in no way, and the pull survives, so what carries it is the printed Urochordata line standing in for the metamorphosis fact.
<!--/ecat-->

## Q180

Biology · botany · Biological Classification

Which of the following organisms are known as chief producers in the oceans?

- (1) Dinoflagellates
- (2) Cyanobacteria
- **(3)** Diatoms
- (4) Euglenoids

**Answer** — booklet: (3) · independent solve: (3) · agree

**Publisher's solution**

1. Diatoms are chief producers of the ocean.

**Solved independently** (answer withheld)

1. Among the protists, diatoms (chrysophytes) are described as the chief producers in the oceans, so the answer is option $3$.

**Subtopic:** Chrysophytes · **Difficulty:** medium (1 step)

**Printed in the booklet** (page 36)

![printed question 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/crops/q180_409ab759_03112026.png?v=409ab7597342)

Publisher's solution, as printed:

![printed solution 180](https://d30lmobgrc5gb8.cloudfront.net/general/03112026/neet_papers/2018/2018_EE/solutions/q180_e02b37cb_03112026.png?v=e02b37cb5279)

<!--ecat-->
#### Categories

- **Type:** **MCQ** (`mcq`) — a question and four answers, nothing lettered or listed
- **Asks:** **Stated fact** (`fact_line`) — a fact NCERT states: what, who or where
- **Concept:** Diatoms are named as the chief producers in the oceans -- the photosynthetic chrysophytes whose silica walls pile up as diatomaceous earth.
- **Trap:** **Neighbouring fact** (`nearby_fact`) — a true fact about a neighbouring thing is offered instead — option 1  
  Dinoflagellates are the other marine photosynthetic protists described in the same section, so with 'marine and photosynthetic' held and the title 'chief producers' unattached, that group is answered instead.
- **Why:** This question requires the group the account names as the ocean's chief producers, demonstrated by 'chief producers in the oceans' being the phrase printed in the diatom entry. Swap test on the trap: rename 'Dinoflagellates' to an unlike word and the pull survives, because what carries the student is that it is the other marine photosynthetic protist group of the same section.
<!--/ecat-->

